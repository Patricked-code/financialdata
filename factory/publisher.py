"""Privilege-separated publisher and durable cross-session CI reconciler."""
import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from factory import engine, tasking, coder

def git(*args):
    return subprocess.run(["git", *args], cwd=engine.ROOT,
                          check=True, capture_output=True, text=True).stdout.strip()

def clean_main():
    if engine.git_branch() != "main":
        raise RuntimeError("main-only: no branches or PR")
    if git("status", "--porcelain"):
        raise RuntimeError("Dirty worktree: refuse write")

def commit_and_push(message, paths):
    git("add", "--", *paths)
    git("diff", "--cached", "--check")
    git("-c", "user.name=financialdata-factory[bot]",
        "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
        "commit", "-m", message)
    sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:refs/heads/main")
    return sha

def publish(path, run_id):
    """Called only after tests passed in a distinct secrets-free job."""
    clean_main()
    proposal, bp, digest = coder.load_proposal(path)
    if git("rev-parse", "HEAD") != proposal["base_sha"]:
        raise RuntimeError("Unreviewed concurrent main change: fail closed")
    state = engine.read_state()
    task = tasking.selected(state)
    if task is None or task["id"] != proposal["task_id"]:
        raise ValueError("Task no longer admissible")
    report = coder.apply(path)
    paths = report["paths"]
    for item in paths:
        if not (item.startswith("src/financialdata/") or item.startswith("tests/")):
            raise ValueError("Unauthorized generated path")
    evidence_path = "factory/evidence/" + task["id"] + "-" + str(run_id) + ".json"
    evidence = {"continuity_id": "FD-AUTONOMY-V1", "task_id": task["id"],
                "run_id": int(run_id), "base_sha": proposal["base_sha"],
                "payload_sha256": digest, "paths": paths,
                "validation": "SUCCESS_IN_GITHUB_ACTIONS_VALIDATE_JOB",
                "attestation": "PENDING_WORKFLOW_CONCLUSION"}
    engine.atomic_write(engine.ROOT / evidence_path,
                        json.dumps(evidence, sort_keys=True, indent=2) + "\n")
    tasking.mark_published(task["id"], run_id, proposal["base_sha"], paths, evidence_path)
    staged = paths + ["factory/state.json", evidence_path]
    git("add", "--", *staged)
    changed = set(git("diff", "--cached", "--name-only").splitlines())
    if changed != set(staged):
        raise RuntimeError("Unexpected staging delta: " + str(changed.symmetric_difference(set(staged))))
    return commit_and_push("factory: validated work " + task["id"] + " [run " + str(run_id) + "]", staged)

def fetch_run(run_id):
    token, repo = os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        raise RuntimeError("GitHub attestation credentials unavailable")
    req = urllib.request.Request(
        "https://api.github.com/repos/" + repo + "/actions/runs/" + str(run_id),
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.load(response)
    if not data.get("path", "").endswith("factory-autonomy.yml"):
        raise ValueError("Run is not the canonical workflow")
    if data.get("repository", {}).get("full_name") != repo:
        raise ValueError("Wrong repository in attestation")
    return data

def reconcile():
    clean_main()
    before = engine.STATE.read_bytes() if engine.STATE.exists() else None
    tasking.hydrate()
    state = engine.read_state()
    pending = [t for t in state["tasks"].values() if t["status"] == "PUBLISHED_PENDING_CI"]
    if len(pending) > 1:
        raise ValueError("More than one published task: manual reconciliation required")
    updated = before != engine.STATE.read_bytes()
    status = "NO_PENDING"
    if pending:
        item = pending[0]
        run = fetch_run(item["run_id"])
        if run.get("status") == "completed" and run.get("conclusion") in ("success", "failure", "cancelled", "timed_out"):
            status = tasking.reconcile_verdict(item["id"], item["run_id"], run["conclusion"], run["html_url"])
            updated = True
        else:
            status = "PENDING_RUN_" + str(item["run_id"])
    if updated:
        commit_and_push("factory: reconcile canonical task continuity and CI", ["factory/state.json"])
    print(json.dumps({"status": status, "state_updated": updated,
                      "next_task": (tasking.selected() or {}).get("id")}))
    return status

def dispatch_next():
    token, repo = os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        raise RuntimeError("Workflow dispatch not authorized")
    request = urllib.request.Request(
        "https://api.github.com/repos/" + repo + "/actions/workflows/factory-autonomy.yml/dispatches",
        data=json.dumps({"ref": "main"}).encode(), method="POST",
        headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json", "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status != 204:
            raise RuntimeError("Dispatch not accepted")
    print("CONTINUATION_DISPATCHED")

def main(argv=None):
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("publish"); p.add_argument("--proposal", required=True)
    p.add_argument("--run-id", type=int, required=True)
    sub.add_parser("reconcile"); sub.add_parser("dispatch-next")
    args = parser.parse_args(argv)
    try:
        if args.cmd == "publish":
            print(json.dumps({"published_sha": publish(args.proposal, args.run_id)}))
        elif args.cmd == "reconcile":
            reconcile()
        else:
            dispatch_next()
        return 0
    except (ValueError, KeyError, RuntimeError, OSError, subprocess.CalledProcessError,
            urllib.error.URLError) as error:
        print("PUBLISH_GATE_FAILED: " + str(error), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
