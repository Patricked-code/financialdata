"""Standalone, standard-library-only orchestration for FinancialData.

This is a control plane, not an LLM. It never executes arbitrary task text as shell code.
All repository-native writes are explicit and constrained to factory/.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
FACTORY = ROOT / "factory"
STATE = FACTORY / "state.json"
PROGRAM_RE = re.compile(r"^##\s+(P\d+(?:-[A-Z]+)?)\b")
TASK_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s+(.+?)\s*$")
PROGRAMS = ("P0", "P1", "P1-R", "P1-FRESH", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
PROTECTED = ("README.md", "GOVERNANCE.md", "AGENTS.md", "CLAUDE.md", "SUIVI.md",
             "DECISIONS.md", "TODO.md", "ROADMAP.md", "ARCHITECTURE.md", "DATA_MODEL.md",
             "SOURCES.md")
SCHEMA_VERSION = 1


def utcnow():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def root_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT.resolve()):
        raise ValueError("Path outside repository")
    return path


def git_branch():
    proc = subprocess.run(["git", "-C", str(ROOT), "branch", "--show-current"],
                          capture_output=True, text=True, check=False)
    return proc.stdout.strip() if proc.returncode == 0 else None


def git_sha():
    proc = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True, check=False)
    return proc.stdout.strip() if proc.returncode == 0 else None


def assert_main_only():
    branch = git_branch()
    if branch is not None and branch != "main":
        raise RuntimeError("Repository governance: main-only; no branches or PRs")


def initial_state():
    return {"schema_version": SCHEMA_VERSION, "revision": 0,
            "projects": {}, "programs": {}, "tasks": {}, "agents": {}, "events": []}


def read_state():
    if not STATE.exists():
        return initial_state()
    data = json.loads(STATE.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Unsupported factory state schema")
    for key in ("projects", "programs", "tasks", "agents", "events"):
        if key not in data or not isinstance(data[key], dict if key != "events" else list):
            raise ValueError("Corrupted state: " + key)
    return data


def atomic_write(path, data):
    path = root_path(path.relative_to(ROOT))
    if not path.is_relative_to(FACTORY.resolve()):
        raise ValueError("Factory writes may only target factory/")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as output:
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextmanager
def exclusive_lock():
    path = FACTORY / ".lock"
    FACTORY.mkdir(parents=True, exist_ok=True)
    for _ in range(100):
        try:
            path.mkdir()
            (path / "owner").write_text(str(os.getpid()) + "\n" + str(time.time()), encoding="utf-8")
            break
        except FileExistsError:
            try:
                age = time.time() - path.stat().st_mtime
            except FileNotFoundError:
                continue
            if age > 300:
                raise RuntimeError("Stale factory lock; inspect manually before recovery")
            time.sleep(.1)
    else:
        raise TimeoutError("Factory state is locked")
    try:
        yield
    finally:
        (path / "owner").unlink(missing_ok=True)
        path.rmdir()


def record(state, event, **data):
    previous = state["events"][-1]["hash"] if state["events"] else "GENESIS"
    entry = {"sequence": len(state["events"]) + 1, "at": utcnow(), "event": event,
             "data": data, "prev_hash": previous}
    entry["hash"] = digest(canonical(entry))
    state["events"].append(entry)
    state["revision"] += 1


def save_state(state):
    validate_event_chain(state)
    atomic_write(STATE, json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def validate_event_chain(state):
    previous = "GENESIS"
    for i, event in enumerate(state["events"], 1):
        payload = {k: v for k, v in event.items() if k != "hash"}
        if event.get("sequence") != i or event.get("prev_hash") != previous or digest(canonical(payload)) != event.get("hash"):
            raise ValueError("Tampered/invalid event chain at sequence " + str(i))
        previous = event["hash"]


def scan_todo():
    text = (ROOT / "TODO.md").read_text(encoding="utf-8")
    phase = "P1"
    tasks = {}
    for line in text.splitlines():
        section = PROGRAM_RE.match(line)
        if section:
            phase = section.group(1)
        match = TASK_RE.match(line)
        if not match:
            continue
        complete = match.group(1).lower() == "x"
        title = match.group(2).strip()
        task_id = "FD-T-" + digest(phase + "\n" + title)[:12].upper()
        tasks[task_id] = {
            "id": task_id, "title": title, "program_id": "FD-" + phase,
            "source": "TODO.md", "kind": "agent_code",
            "status": "DONE" if complete else "BACKLOG", "priority": 50,
            "dependencies": [], "criteria": ["No regression", "Evidence traceable to sources",
                                               "Update project memory"],
            "capability": "coder", "owner": None, "lease_until": None,
            "evidence": None}
    return tasks


def scan_programs():
    road = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    programs = {}
    for phase in PROGRAMS:
        # Phases are a governed catalog. Source of truth remains ROADMAP.md.
        exists = re.search(r"^##\s+" + re.escape(phase) + r"\b", road, re.M) is not None
        programs["FD-" + phase] = {
            "id": "FD-" + phase, "source": "ROADMAP.md",
            "status": "DEFINED" if exists else "REVIEW_REQUIRED",
            "version": 1, "parent": "FD-ROOT", "description": phase}
    return programs


def ensure_audit_tasks(state):
    seeds = {
        "FD-A-STRUCTURE": ("Validate repository governance and 48-issuer index", 1),
        "FD-A-LINEAGE": ("Validate manifest, CFAC hash register and source consistency", 2)}
    for task_id, (title, priority) in seeds.items():
        if task_id not in state["tasks"]:
            state["tasks"][task_id] = {
                "id": task_id, "title": title, "program_id": "FD-P1",
                "source": "factory/engine.py", "kind": "audit",
                "status": "BACKLOG", "priority": priority, "dependencies": [],
                "criteria": ["Audit report emitted", "No destructive source edits"],
                "capability": "audit", "owner": None, "lease_until": None,
                "evidence": None}


def bootstrap():
    assert_main_only()
    with exclusive_lock():
        state = read_state()
        before = len(state["tasks"])
        state["projects"].setdefault("FD-ROOT", {
            "id": "FD-ROOT", "name": "financialdata", "source": "README.md",
            "version": 1, "status": "ACTIVE"})
        state["programs"].update(scan_programs())
        scanned = scan_todo()
        for task_id, desired in scanned.items():
            if task_id not in state["tasks"]:
                state["tasks"][task_id] = desired
            elif state["tasks"][task_id]["title"] != desired["title"]:
                raise ValueError("Task ID collision")
        ensure_audit_tasks(state)
        if before != len(state["tasks"]) or not STATE.exists():
            record(state, "BACKLOG_SYNC", total=len(state["tasks"]), added=len(state["tasks"]) - before,
                   source_sha=git_sha())
            save_state(state)
        return state


def admit(agent, capabilities):
    assert_main_only()
    if not re.fullmatch(r"[A-Za-z0-9_.-]{2,64}", agent):
        raise ValueError("Invalid agent identity")
    caps = sorted(set(capabilities))
    if not caps or not set(caps).issubset({"audit", "coder"}):
        raise ValueError("Supported capabilities: audit, coder")
    with exclusive_lock():
        state = read_state()
        state["agents"][agent] = {"capabilities": caps, "admitted_at": utcnow(),
                                  "last_seen_sha": git_sha()}
        record(state, "AGENT_ADMITTED", agent=agent, capabilities=caps)
        save_state(state)
    return state["agents"][agent]


def validate_graph(state):
    """Reject orphan programs, missing task dependencies and dependency cycles."""
    projects, programs, tasks = state["projects"], state["programs"], state["tasks"]
    for program in programs.values():
        if program.get("parent") not in projects:
            raise ValueError("Orphan program: " + program["id"])
    for task in tasks.values():
        if task["program_id"] not in programs:
            raise ValueError("Orphan task: " + task["id"])
        for dep in task.get("dependencies", []):
            if dep not in tasks:
                raise ValueError("Missing task dependency: " + dep)
    visited, active = set(), set()
    def visit(task_id):
        if task_id in active:
            raise ValueError("Cyclic task dependency: " + task_id)
        if task_id in visited:
            return
        active.add(task_id)
        for dep in tasks[task_id].get("dependencies", []):
            visit(dep)
        active.remove(task_id)
        visited.add(task_id)
    for task_id in tasks:
        visit(task_id)


def eligible(state, agent):
    if agent not in state["agents"]:
        raise ValueError("Agent not admitted; run admit first")
    validate_graph(state)
    capabilities = set(state["agents"][agent]["capabilities"])
    completed = {key for key, item in state["tasks"].items() if item["status"] == "DONE"}
    candidates = [task for task in state["tasks"].values()
                  if task["status"] == "BACKLOG"
                  and task.get("capability") in capabilities
                  and all(dep in completed for dep in task.get("dependencies", []))]
    return sorted(candidates, key=lambda t: (t["priority"], t["id"]))


def claim(agent):
    assert_main_only()
    with exclusive_lock():
        state = read_state()
        # Idempotent recovery: agent gets the same in-flight task on reconnect.
        active = [t for t in state["tasks"].values()
                  if t["status"] == "CLAIMED" and t["owner"] == agent]
        if active:
            return sorted(active, key=lambda t: t["id"])[0]
        candidates = eligible(state, agent)
        if not candidates:
            return None
        task = candidates[0]
        task["status"] = "CLAIMED"
        task["owner"] = agent
        task["lease_until"] = int(time.time()) + 3600
        record(state, "TASK_CLAIMED", agent=agent, task_id=task["id"], source_sha=git_sha())
        save_state(state)
        return task


def audit():
    errors, warnings = [], []
    for filename in PROTECTED:
        if not (ROOT / filename).is_file():
            errors.append("MISSING_CANONICAL_FILE:" + filename)
    results = {"source_sha": git_sha(), "at": utcnow(), "errors": errors,
               "warnings": warnings, "metrics": {}}
    issuer_file = ROOT / "inventory/p1_issuer_manifest.csv"
    doc_file = ROOT / "inventory/p1_document_manifest.csv"
    hash_file = ROOT / "inventory/hashes/CFAC.csv"
    if issuer_file.is_file():
        with issuer_file.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        issuers = [row for row in rows if row.get("ticker") != "ALL"]
        results["metrics"]["issuers"] = len(issuers)
        totals = [row for row in rows if row.get("ticker") == "ALL"]
        if len(issuers) != 48 or len(totals) != 1:
            errors.append("ISSUER_INDEX_STRUCTURE")
        else:
            total = int(totals[0]["pdf_count"])
            results["metrics"]["source_total"] = total
            if sum(int(row["pdf_count"]) for row in issuers) != total:
                errors.append("ISSUER_INDEX_TOTAL_MISMATCH")
    else:
        errors.append("MISSING_ISSUER_INDEX")
    if doc_file.is_file():
        with doc_file.open(newline="", encoding="utf-8") as fh:
            documents = list(csv.DictReader(fh))
        results["metrics"]["master_manifest_rows"] = len(documents)
        ids = [row["source_drive_file_id"] for row in documents]
        if len(set(ids)) != len(ids):
            errors.append("DOCUMENT_MANIFEST_DUPLICATE_DRIVE_ID")
        if len(documents) < results["metrics"].get("source_total", 0):
            warnings.append("DOCUMENT_MANIFEST_INCOMPLETE")
    else:
        errors.append("MISSING_DOCUMENT_MANIFEST")
    if hash_file.is_file():
        with hash_file.open(newline="", encoding="utf-8") as fh:
            hashed = list(csv.DictReader(fh))
        results["metrics"]["cfac_hash_rows"] = len(hashed)
        hashes = [row["sha256"] for row in hashed]
        if len(hashed) != 114 or any(re.fullmatch("[0-9a-f]{64}", h) is None for h in hashes):
            errors.append("CFAC_HASH_REGISTRY_INVALID")
        results["metrics"]["cfac_exact_duplicate_extra_files"] = len(hashes) - len(set(hashes))
    else:
        warnings.append("CFAC_HASH_REGISTRY_NOT_PRESENT")
    suivi = (ROOT / "SUIVI.md")
    if suivi.is_file() and results["metrics"].get("source_total") == 3157:
        if "3 157" not in suivi.read_text(encoding="utf-8"):
            warnings.append("SUIVI_STALE_V22_VS_V23")
    state = read_state()
    validate_event_chain(state)
    try:
        validate_graph(state)
    except ValueError as exc:
        errors.append("INVALID_TASK_GRAPH:" + str(exc))
    results["metrics"]["projects"] = len(state["projects"])
    results["metrics"]["programs"] = len(state["programs"])
    results["metrics"]["tasks"] = len(state["tasks"])
    results["metrics"]["events"] = len(state["events"])
    results["ok"] = len(errors) == 0
    return results


def finish(agent, task_id, evidence, ok=True):
    assert_main_only()
    if not evidence or len(evidence) > 2048:
        raise ValueError("Provide a traceable evidence reference")
    with exclusive_lock():
        state = read_state()
        task = state["tasks"].get(task_id)
        if not task or task["owner"] != agent or task["status"] != "CLAIMED":
            raise ValueError("Only the claiming agent may finish a claimed task")
        if ok and task["kind"] == "agent_code":
            match = re.search(r"(?:^|[; ])commit:([a-f0-9]{40})(?:;|$)", evidence)
            if match is None or "tests:PASS" not in evidence:
                raise ValueError("Code completion requires full commit SHA and tests:PASS evidence")
            current = git_sha()
            if current is not None and match.group(1) != current:
                raise RuntimeError("Evidence commit is not current main HEAD")
            if audit()["errors"]:
                raise RuntimeError("Preflight audit failed; cannot mark code task done")
        task["status"] = "DONE" if ok else "BLOCKED"
        task["evidence"] = evidence
        task["lease_until"] = None
        record(state, "TASK_DONE" if ok else "TASK_BLOCKED",
               agent=agent, task_id=task_id, evidence=evidence, source_sha=git_sha())
        save_state(state)
        return task


def run(agent, max_tasks=20):
    if max_tasks < 1 or max_tasks > 100:
        raise ValueError("max_tasks must be 1..100")
    results = []
    for _ in range(max_tasks):
        task = claim(agent)
        if task is None:
            break
        if task["kind"] != "audit":
            results.append({"task_id": task["id"], "status": "CLAIMED_FOR_CODE_AGENT",
                            "instruction": "Implement under existing AGENTS.md governance, test, then use complete with real evidence."})
            break
        report = audit()
        evidence_path = FACTORY / "evidence" / (task["id"] + ".json")
        atomic_write(evidence_path, json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        finish(agent, task["id"], "factory/evidence/" + task["id"] + ".json",
               ok=report["ok"])
        results.append({"task_id": task["id"], "status": "DONE" if report["ok"] else "BLOCKED",
                        "report": report})
        if not report["ok"]:
            break
    return results


def status():
    state = read_state()
    counts = {}
    for task in state["tasks"].values():
        counts[task["status"]] = counts.get(task["status"], 0) + 1
    return {"revision": state["revision"], "projects": len(state["projects"]),
            "programs": len(state["programs"]),
            "tasks": len(state["tasks"]), "by_status": counts,
            "admitted_agents": sorted(state["agents"]), "head": git_sha(),
            "last_event": state["events"][-1] if state["events"] else None}


def main(argv=None):
    parser = argparse.ArgumentParser(description="FinancialData self-contained factory")
    subs = parser.add_subparsers(dest="command", required=True)
    for name in ("bootstrap", "status", "audit"):
        subs.add_parser(name)
    admit_parser = subs.add_parser("admit")
    admit_parser.add_argument("--agent", required=True)
    admit_parser.add_argument("--capabilities", nargs="+", required=True)
    next_parser = subs.add_parser("next")
    next_parser.add_argument("--agent", required=True)
    run_parser = subs.add_parser("run")
    run_parser.add_argument("--agent", required=True)
    run_parser.add_argument("--max-tasks", type=int, default=20)
    complete_parser = subs.add_parser("complete")
    complete_parser.add_argument("--agent", required=True)
    complete_parser.add_argument("--task-id", required=True)
    complete_parser.add_argument("--evidence", required=True)
    block_parser = subs.add_parser("block")
    block_parser.add_argument("--agent", required=True)
    block_parser.add_argument("--task-id", required=True)
    block_parser.add_argument("--evidence", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "bootstrap":
            result = status_after_bootstrap()
        elif args.command == "status":
            result = status()
        elif args.command == "audit":
            result = audit()
        elif args.command == "admit":
            result = admit(args.agent, args.capabilities)
        elif args.command == "next":
            result = claim(args.agent)
        elif args.command == "run":
            result = run(args.agent, args.max_tasks)
        elif args.command in ("complete", "block"):
            result = finish(args.agent, args.task_id, args.evidence, ok=args.command == "complete")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (RuntimeError, ValueError, OSError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


def status_after_bootstrap():
    bootstrap()
    return status()


if __name__ == "__main__":
    sys.exit(main())
