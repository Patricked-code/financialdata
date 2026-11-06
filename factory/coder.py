"""Bounded model-code generator; never run generated code in this process."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import urllib.error
import urllib.request
from factory import engine, tasking

DENIED = {"subprocess", "socket", "urllib", "http", "requests", "ctypes", "importlib", "shutil"}
DENIED_CALLS = {"eval", "exec", "compile", "__import__", "breakpoint"}

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def allowed_file(path, allowed):
    if not isinstance(path, str) or "\\" in path or path.startswith("/"):
        raise ValueError("Absolute or backslash path")
    obj = PurePosixPath(path)
    if ".." in obj.parts or "." in obj.parts or not path.endswith(".py"):
        raise ValueError("Invalid Python path")
    if not (path.startswith("src/financialdata/") or path.startswith("tests/")):
        raise ValueError("Path outside writable code roots")
    if not any(path.startswith(prefix) for prefix in allowed):
        raise ValueError("Blueprint denied path " + path)
    target = engine.ROOT.joinpath(*obj.parts)
    if not target.resolve().is_relative_to(engine.ROOT.resolve()) or target.is_symlink():
        raise ValueError("Symlink escape")
    return target

def validate(proposal):
    if proposal.get("schema_version") != 1 or proposal.get("continuity_id") != "FD-AUTONOMY-V1":
        raise ValueError("Wrong proposal schema")
    bp = next((b for b in tasking.blueprints() if b["id"] == proposal.get("task_id")), None)
    if bp is None or proposal.get("blueprint_version") != bp["version"]:
        raise ValueError("Unapproved blueprint/version")
    if not re.fullmatch("[a-f0-9]{40}", str(proposal.get("base_sha"))):
        raise ValueError("Invalid base SHA")
    files = proposal.get("files")
    if not isinstance(files, list) or not 1 <= len(files) <= 12:
        raise ValueError("Invalid file count")
    seen, size = set(), 0
    for entry in files:
        path, contents = entry.get("path"), entry.get("content")
        if not isinstance(contents, str):
            raise ValueError("Expected code text")
        allowed_file(path, bp["allowed_paths"])
        if path in seen:
            raise ValueError("Repeated file")
        seen.add(path)
        size += len(contents)
        if "\x00" in contents:
            raise ValueError("Invalid NUL character")
        tree = ast.parse(contents, filename=path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                if any(alias.name.split(".")[0] in DENIED for alias in node.names):
                    raise ValueError("Forbidden import")
            if isinstance(node, ast.ImportFrom):
                if (node.module or "").split(".")[0] in DENIED:
                    raise ValueError("Forbidden import")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in DENIED_CALLS:
                raise ValueError("Forbidden operation")
    if size > 160_000 or not any(p.startswith("tests/test_") for p in seen):
        raise ValueError("Size limit or missing unittest file")
    return bp

def save_proposal(proposal, output):
    validate(proposal)
    data = dict(proposal)
    data["payload_sha256"] = hashlib.sha256(canonical(proposal).encode()).hexdigest()
    Path(output).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def load_proposal(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    supplied = data.pop("payload_sha256", None)
    actual = hashlib.sha256(canonical(data).encode()).hexdigest()
    if supplied != actual:
        raise ValueError("Proposal hash mismatch")
    bp = validate(data)
    return data, bp, actual

def apply(path):
    proposal, bp, checksum = load_proposal(path)
    head = subprocess.check_output(["git", "-C", str(engine.ROOT), "rev-parse", "HEAD"], text=True).strip()
    if head != proposal["base_sha"]:
        raise RuntimeError("Stale generation base SHA")
    paths = []
    for entry in proposal["files"]:
        target = allowed_file(entry["path"], bp["allowed_paths"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(entry["content"].replace("\r\n", "\n"), encoding="utf-8", newline="\n")
        paths.append(entry["path"])
    return {"paths": sorted(paths), "task_id": proposal["task_id"],
            "base_sha": head, "payload_sha256": checksum}

def generate(output):
    tasking.hydrate()
    task = tasking.selected()
    if task is None:
        print("NO_ADMISSIBLE_TASK")
        return False
    # Deterministic, reviewed bootstrap blueprints execute without external API
    # credentials. Other blueprints require a genuine model-backed coding call.
    from factory import templates
    seeded_files = templates.generate(task["id"])
    if seeded_files is not None:
        ctx = tasking.proposal_context(task["id"])
        proposal = {"schema_version": 1, "continuity_id": "FD-AUTONOMY-V1",
                    "task_id": task["id"], "blueprint_version": ctx["task"]["version"],
                    "base_sha": ctx["base_sha"], "files": seeded_files}
        save_proposal(proposal, output)
        print("DETERMINISTIC_CODE_GENERATED:" + task["id"])
        return True
    # Real provider is isolated in a single audited adapter. The caller
    # never treats configuration, a truncated response, or a model proposal
    # as a completed task.
    from factory import provider
    ctx = tasking.proposal_context(task["id"])
    bp = ctx["task"]
    governance = (engine.ROOT / "GOVERNANCE.md").read_text(encoding="utf-8")
    files = provider.generate_files(bp, governance)
    proposal = {
        "schema_version": 1, "continuity_id": "FD-AUTONOMY-V1",
        "task_id": task["id"], "blueprint_version": bp["version"],
        "base_sha": ctx["base_sha"], "files": files,
    }
    save_proposal(proposal, output)
    print("MODEL_CODE_GENERATED:" + task["id"])
    return True


def main(argv=None):
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    gen = sub.add_parser("generate"); gen.add_argument("--output", required=True)
    ap = sub.add_parser("apply"); ap.add_argument("--proposal", required=True)
    args = parser.parse_args(argv)
    try:
        result = generate(args.output) if args.command == "generate" else apply(args.proposal)
        print(json.dumps({"ok": bool(result)}))
        return 0
    except (RuntimeError, ValueError, KeyError, OSError, SyntaxError, json.JSONDecodeError) as error:
        print(type(error).__name__ + ":" + str(error), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
