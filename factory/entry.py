"""Read-only admission and program/task navigation for a connected coding agent.

This is an entry point to the EXISTING factory, not another orchestrator.
It never claims tasks, executes code, generates secrets or mutates SOURCE.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
import re
import sys
from factory import engine, tasking, program_factory

CONTINUITY_ID = "FD-AUTONOMY-V1"
ALLOWED_ROLES = ("coder", "planner", "auditor")


def check_identity(agent: str, role: str) -> None:
    if role not in ALLOWED_ROLES:
        raise ValueError("Unsupported role")
    if re.fullmatch(r"[A-Za-z0-9_.-]{2,64}", agent) is None:
        raise ValueError("Invalid descriptive agent label")


def read_only_admission(agent: str, role: str) -> dict:
    """Produce deterministic next-action guidance with no filesystem writes.

    The descriptive agent name is NOT authentication: GitHub credentials
    must be verified by the calling assistant's GitHub integration.
    """
    check_identity(agent, role)
    head = engine.git_sha()
    if not head or re.fullmatch(r"[a-f0-9]{40}", head) is None:
        raise RuntimeError("Git checkout with a readable commit is required")
    engine.assert_main_only()
    state = engine.read_state()
    engine.validate_event_chain(state)
    engine.validate_graph(state)
    continuity = state.get("continuity")
    if not isinstance(continuity, dict) or continuity.get("id") != CONTINUITY_ID:
        raise ValueError("Unknown or absent governed continuity; reconcile with main")
    audit = engine.audit()
    counts = Counter(t["status"] for t in state["tasks"].values())
    program_counts = defaultdict(Counter)
    for task in state["tasks"].values():
        program_counts[task["program_id"]][task["status"]] += 1

    pending = sorted([
        {"id": t["id"], "run_id": t.get("run_id"), "owner": t.get("owner")}
        for t in state["tasks"].values()
        if t["status"] == "PUBLISHED_PENDING_CI"
    ], key=lambda obj: obj["id"])
    selected = tasking.selected(state)
    unqualified = [
        t for t in state["tasks"].values()
        if t["status"] == "BACKLOG" and t.get("kind") == "agent_code"
        and t.get("autonomy") != "READY"
    ]
    priority = {("FD-" + code): i for i, code in enumerate(engine.PROGRAMS)}
    unqualified.sort(key=lambda t: (priority.get(t["program_id"], 999),
                                   t.get("priority", 999), t["id"]))
    program_queue = [{
        "id": pid, "status": p["status"],
        "task_counts": dict(program_counts[pid]),
        "source": p["source"]
    } for pid, p in state["programs"].items()]
    program_queue.sort(key=lambda p: (priority.get(p["id"], 999), p["id"]))

    if not audit["ok"]:
        decision = "BLOCKED_BY_AUDIT"
        next_action = "Inspect audit errors; repair only with verified evidence."
    elif pending:
        decision = "CI_ATTESTATION_REQUIRED"
        next_action = "Reconcile exact pending GitHub Actions run before new work."
    elif selected:
        decision = "APPROVED_WORK_AVAILABLE"
        next_action = "Execute approved blueprint through existing factory-autonomy.yml."
    elif unqualified:
        decision = "PROGRAM_QUALIFICATION_REQUIRED"
        next_action = ("Inspect highest-priority backlog and current SOURCE evidence, "
                       "prepare a bounded, versioned blueprint plus tests, "
                       "validate governance, then admit to the existing task registry.")
    else:
        decision = "NO_ADMISSIBLE_WORK"
        next_action = "Inspect ROADMAP and TODO for newly evidenced work; do not fabricate tasks."

    return {
        "entry_contract": "FD-AGENT-ARRIVAL-V1",
        "continuity_id": CONTINUITY_ID,
        "repository": "Patricked-code/financialdata",
        "branch": "main",
        "head_sha": head,
        "requested_role": role,
        "agent_label": agent,
        "github_identity_verified": False,
        "read_only": True,
        "revision": state["revision"],
        "last_attested_run": continuity.get("last_attested_run"),
        "persisted_next_action": continuity.get("next_action"),
        "decision": decision,
        "next_action": next_action,
        "pending_ci": pending,
        "selected_blueprint": selected["id"] if selected else None,
        "qualification_candidates": [
            {"id": t["id"], "program_id": t["program_id"], "title": t["title"],
             "source": t["source"], "status": t["status"]}
            for t in unqualified[:10]
        ],
        "programs": program_queue,
        "task_counts": dict(counts),
        "audit": {"ok": audit["ok"], "errors": audit["errors"],
                  "warnings": audit["warnings"]},
        "program_qualification": program_factory.assessment(state),
        "canonical_files": [
            "GOVERNANCE.md", "AGENTS.md", "CLAUDE.md",
            "factory/ARRIVAL.md", "factory/CONTINUITY.md",
            "factory/HANDOFF.json", "factory/state.json", "factory/blueprints.json",
            "SUIVI.md", "DECISIONS.md", "TODO.md", "ROADMAP.md",
            "ARCHITECTURE.md", "DATA_MODEL.md", "SOURCES.md",
        ],
        "execution_owner": ".github/workflows/factory-autonomy.yml",
        "note": ("The conversational agent must verify GitHub authorization. "
                 "This command does not admit a new GitHub principal, "
                 "create tasks, claim work, commit or initiate a remote run."),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="FinancialData governed coding-agent arrival")
    parser.add_argument("--role", choices=ALLOWED_ROLES, default="coder")
    parser.add_argument("--agent", required=True)
    arguments = parser.parse_args(argv)
    try:
        print(json.dumps(read_only_admission(arguments.agent, arguments.role),
                         ensure_ascii=False, indent=2))
        return 0
    except (RuntimeError, ValueError, OSError, KeyError) as exc:
        print(json.dumps({"entry_contract": "FD-AGENT-ARRIVAL-V1",
                          "decision": "BLOCKED", "error": str(exc)},
                         ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
