"""Additive project work-unit projection; one engine.state.json authority."""
from __future__ import annotations

import json
from pathlib import Path
from factory import engine

BLUEPRINTS = Path(__file__).with_name("blueprints.json")
STAGES = ("PLAN", "CODE", "VALIDATE", "PUBLISH", "ATTEST")


def blueprints():
    data = json.loads(BLUEPRINTS.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    ids = [t["id"] for t in data["tasks"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate blueprint task")
    for task in data["tasks"]:
        if task["program_id"] not in {"FD-P1", "FD-P1-R", "FD-P2"}:
            raise ValueError("Unapproved program")
        if not task.get("acceptance") or not task.get("allowed_paths"):
            raise ValueError("Blueprint missing proof and bounded paths")
    return data["tasks"]


def hydrate():
    """Idempotent extension of the existing engine, never a competing queue."""
    engine.assert_main_only()
    engine.bootstrap()
    with engine.exclusive_lock():
        state = engine.read_state()
        added = 0
        for bp in blueprints():
            tid = bp["id"]
            if tid in state["tasks"]:
                existing = state["tasks"][tid]
                if existing.get("blueprint_version") != bp["version"]:
                    raise ValueError("Blueprint version conflict; explicit migration required: " + tid)
                continue
            state["tasks"][tid] = {
                "id": tid, "title": bp["title"], "program_id": bp["program_id"],
                "source": "factory/blueprints.json", "blueprint_version": bp["version"],
                "kind": "agent_code", "autonomy": "READY", "status": "BACKLOG",
                "priority": bp["priority"], "dependencies": bp.get("dependencies", []),
                "criteria": bp["acceptance"], "capability": "coder", "owner": None,
                "lease_until": None, "evidence": None,
                "units": [{"id": tid + "-" + stage, "stage": stage,
                           "status": "BACKLOG", "evidence": None} for stage in STAGES],
            }
            added += 1
        # Every imported TODO task also gets non-executable, traceable work units.
        # Historical DONE is explicitly not evidence that unit-level CI was attested.
        units_added = 0
        for task in state["tasks"].values():
            if "units" in task:
                continue
            stages = STAGES if task.get("kind") == "agent_code" else ("PLAN", "AUDIT", "ATTEST")
            status = "HISTORICAL_NOT_ATTESTED" if task["status"] == "DONE" else "BACKLOG"
            task["units"] = [{"id": task["id"] + "-" + stage, "stage": stage,
                              "status": status, "evidence": None} for stage in stages]
            units_added += 1
        if "continuity" not in state:
            state["continuity"] = {"id": "FD-AUTONOMY-V1",
                                   "next_action": "RECONCILE_THEN_SELECT",
                                   "last_attested_run": None}
            units_added += 1
        # Job roles are separately permissioned workers inside one workflow.
        # They are not independent runtime authorities or model identities.
        roles = ("planner", "coder", "validator", "publisher", "reconciler")
        for role in roles:
            agent_id = "github-actions:" + role
            if agent_id not in state["agents"]:
                state["agents"][agent_id] = {
                    "capabilities": ["workflow_" + role],
                    "mode": "github_actions_role",
                    "admitted_at": engine.utcnow(),
                    "last_seen_sha": engine.git_sha()}
                units_added += 1
        # Only previously attested autonomous tasks may receive role provenance.
        role_for_stage = {"PLAN": "planner", "CODE": "coder",
                          "VALIDATE": "validator", "PUBLISH": "publisher",
                          "ATTEST": "reconciler"}
        for task in state["tasks"].values():
            if not task.get("run_id") or not task.get("autonomy"):
                continue
            for unit in task.get("units", []):
                if "agent_id" not in unit:
                    unit["agent_id"] = "github-actions:" + role_for_stage[unit["stage"]]
                    unit["run_id"] = task["run_id"]
                    units_added += 1
        engine.validate_graph(state)
        if added or units_added:
            engine.record(state, "WORK_UNIT_SYNC", added_blueprints=added,
                          added_unit_sets=units_added,
                          source="factory/blueprints.json", source_sha=engine.git_sha())
            engine.save_state(state)
        return state


def selected(state=None):
    if state is None:
        state = engine.read_state()
    engine.validate_graph(state)
    if any(t["status"] == "PUBLISHED_PENDING_CI" for t in state["tasks"].values()):
        return None
    done = {key for key, item in state["tasks"].items() if item["status"] == "DONE"}
    options = [t for t in state["tasks"].values()
               if t.get("autonomy") == "READY" and t["status"] == "BACKLOG"
               and all(d in done for d in t.get("dependencies", []))]
    return sorted(options, key=lambda t: (t["priority"], t["id"]))[0] if options else None


def proposal_context(task_id):
    state = engine.read_state()
    task = state["tasks"].get(task_id)
    if not task or task.get("autonomy") != "READY" or task["status"] != "BACKLOG":
        raise ValueError("Task not admitted for autonomous coding")
    task_now = selected(state)
    if not task_now or task_now["id"] != task_id:
        raise ValueError("Out-of-order task or unsatisfied dependencies")
    bp = next(b for b in blueprints() if b["id"] == task_id)
    return {"task": bp, "base_sha": engine.git_sha(),
            "continuity_id": "FD-AUTONOMY-V1", "state_revision": state["revision"]}


def mark_published(task_id, run_id, base_sha, paths, evidence_ref):
    """Publish job records work pending independent GitHub run attestation."""
    with engine.exclusive_lock():
        state = engine.read_state()
        task = selected(state)
        if not task or task["id"] != task_id:
            raise ValueError("Changed task selection; fail closed")
        task["status"] = "PUBLISHED_PENDING_CI"
        task["owner"] = "github-actions:" + str(run_id)
        task["evidence"] = evidence_ref
        task["run_id"] = int(run_id)
        task["base_sha"] = base_sha
        task["changed_paths"] = list(paths)
        state["continuity"]["next_action"] = "ATTEST_GITHUB_ACTIONS_RUN_" + str(run_id)
        role_for_stage = {"PLAN": "planner", "CODE": "coder",
                          "VALIDATE": "validator", "PUBLISH": "publisher",
                          "ATTEST": "reconciler"}
        for unit in task["units"]:
            unit["agent_id"] = "github-actions:" + role_for_stage[unit["stage"]]
            unit["run_id"] = int(run_id)
            unit["status"] = "PENDING_CI" if unit["stage"] == "ATTEST" else "DONE"
            unit["evidence"] = evidence_ref if unit["stage"] != "ATTEST" else None
        engine.record(state, "CODE_PUBLISHED_PENDING_CI", task_id=task_id,
                      run_id=run_id, base_sha=base_sha, paths=paths)
        engine.save_state(state)


def reconcile_verdict(task_id, run_id, conclusion, evidence_url):
    if conclusion not in {"success", "failure", "cancelled", "timed_out"}:
        raise ValueError("Not a final GitHub Actions conclusion")
    with engine.exclusive_lock():
        state = engine.read_state()
        task = state["tasks"].get(task_id)
        if task is None or task["status"] != "PUBLISHED_PENDING_CI" or task["run_id"] != int(run_id):
            raise ValueError("No matching published task")
        task["status"] = "DONE" if conclusion == "success" else "BLOCKED"
        state["continuity"]["last_attested_run"] = int(run_id)
        state["continuity"]["next_action"] = ("SELECT_NEXT_ADMISSIBLE" if conclusion == "success"
                                               else "INVESTIGATE_FAILED_RUN_" + str(run_id))
        for unit in task["units"]:
            if unit["stage"] == "ATTEST":
                unit["status"] = "DONE" if conclusion == "success" else "BLOCKED"
                unit["evidence"] = evidence_url
        if conclusion == "success":
            following = selected(state)
            state["continuity"]["next_action"] = ("EXECUTE_" + following["id"] if following
                                                   else "NO_ADMISSIBLE_AUTONOMOUS_TASK")
        engine.record(state, "CI_ATTESTED", task_id=task_id, run_id=run_id,
                      conclusion=conclusion, evidence_url=evidence_url)
        engine.save_state(state)
        return task["status"]


def record_failure(task_id, run_id, stage, max_attempts=3):
    """Persist bounded retries; never loop endlessly on provider/test failures."""
    if stage not in {"GENERATE", "VALIDATE"}:
        raise ValueError("Unknown failure stage")
    with engine.exclusive_lock():
        state = engine.read_state()
        task = selected(state)
        if task is None or task["id"] != task_id:
            raise ValueError("Failure report targets an inadmissible task")
        failures = task.setdefault("failed_runs", [])
        if any(x["run_id"] == int(run_id) for x in failures):
            return task["status"]
        failures.append({"run_id": int(run_id), "stage": stage,
                         "at": engine.utcnow()})
        if len(failures) >= max_attempts:
            task["status"] = "BLOCKED"
            for unit in task.get("units", []):
                if unit["status"] != "DONE":
                    unit["status"] = "BLOCKED"
                    unit["evidence"] = "GITHUB_ACTIONS_RUN_" + str(run_id)
            state["continuity"]["next_action"] = "REVIEW_FAILURES_" + task_id
        else:
            state["continuity"]["next_action"] = "RETRY_" + task_id
        engine.record(state, "AUTONOMOUS_STAGE_FAILED", task_id=task_id,
                      run_id=int(run_id), stage=stage,
                      attempts=len(failures), status=task["status"])
        engine.save_state(state)
        return task["status"]
