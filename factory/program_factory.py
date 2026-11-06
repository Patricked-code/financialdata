"""Evidence-gated PROGRAM -> task qualification, using the existing factory authority.

Only pre-reviewed, read-only engineering rules can become READY without an
external approval. Source acquisition, inference and mutations remain blocked.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from factory import engine, tasking

RULESET_VERSION = 1
EVIDENCE = "factory/evidence/program-qualification.json"

RULES = (
    {
        "rule": "P1_DOCUMENT_COVERAGE_DIAGNOSTIC",
        "id": "FD-AUTO-P1-COVERAGE-DIAGNOSTIC",
        "origin_contains": "poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste",
        "requirements": (
            "Develop a read-only Python 3.11 stdlib module that compares the real "
            "p1_issuer_manifest.csv with p1_document_manifest.csv. Count published "
            "manifest rows by issuer and report indexed-vs-manifest differences, "
            "missing source Drive IDs, duplicate Drive IDs and incomplete coverage "
            "WITHOUT claiming missing PDFs were obtained. Include executable unittests."
        ),
        "title": "Implement SOURCE P1 issuer-document coverage diagnostics (read only)",
        "dependencies": ["FD-AUTO-P1-MANIFEST-CHECKER"],
        "priority": 7,
        "evidence_fields": {
            "inventory/p1_issuer_manifest.csv": ("ticker", "pdf_count"),
            "inventory/p1_document_manifest.csv": (
                "issuer_folder_ticker", "source_drive_file_id", "source_file_id"),
        },
        "acceptance": (
            "All calculations rely on manifest rows present in Git",
            "No PDF or SOURCE object is fabricated or modified",
            "Incomplete documentation remains explicit",
            "Unit tests cover duplicates, missing rows and empty manifests",
        ),
    },
    {
        "rule": "P1_TEMPORAL_METADATA_DIAGNOSTIC",
        "id": "FD-AUTO-P1-TEMPORAL-DIAGNOSTIC",
        "origin_contains": "backfill métadonnées temporelles et shards compatibles",
        "requirements": (
            "Develop a read-only Python 3.11 stdlib validator for P1 document "
            "manifest economic_period_status, period_start and period_end. Detect "
            "unresolved, malformed and contradictory published period metadata "
            "without inferring economic periods from filename or folder. Return "
            "a structured reproducible report, with unittest edge cases."
        ),
        "title": "Implement SOURCE P1 economic-period completeness diagnostic (read only)",
        "dependencies": ["FD-AUTO-P1-COVERAGE-DIAGNOSTIC"],
        "priority": 8,
        "evidence_fields": {
            "inventory/p1_document_manifest.csv": (
                "source_drive_file_id", "economic_period_status",
                "period_start", "period_end"),
        },
        "acceptance": (
            "No inferred economic date is written as a published fact",
            "Unresolved periods remain explicitly unresolved",
            "No historical SOURCE data is modified",
            "Tests cover missing, malformed and reversed periods",
        ),
    },
)

EXTERNAL_REQUIREMENTS = (
    ("CFAC", "Needs real live collection/recheck evidence and external source bytes"),
    ("P1-FRESH", "Needs verified BRVM discovery/collector access and deltas"),
    ("périodes économiques fines", "Needs content-based period evidence beyond filename"),
    ("aucune relation", "SUPERSEDES policy guard; not a code-deliverable task"),
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def eligible_program(state):
    return state["programs"].get("FD-P1", {}).get("status") == "DEFINED"


def inspect_rule(rule, state):
    """Pure assessment: never broadens writable paths based on untrusted text."""
    result = {"rule": rule["rule"], "id": rule["id"], "status": "BLOCKED",
              "reason": None, "evidence": {}, "origin_task": None}
    if not eligible_program(state):
        result["reason"] = "ROADMAP_P1_UNVERIFIED"
        return result
    existing = state["tasks"].get(rule["id"])
    if existing:
        if not tasking.evidence_current(existing):
            result["status"] = "STALE_EVIDENCE"
            result["reason"] = "SOURCE_CHANGED_SINCE_QUALIFICATION"
        else:
            result["status"] = "EXISTING"
            result["reason"] = existing["status"]
        return result
    matches = [t for t in state["tasks"].values()
               if t.get("source") == "TODO.md"
               and t.get("program_id") == "FD-P1"
               and t.get("status") == "BACKLOG"
               and rule["origin_contains"] in t["title"]]
    if len(matches) != 1:
        result["reason"] = "TODO_PROVENANCE_NOT_UNAMBIGUOUS"
        return result
    for dependency in rule["dependencies"]:
        if dependency not in state["tasks"] and dependency not in [x["id"] for x in RULES]:
            result["reason"] = "DEPENDENCY_NOT_IN_CANONICAL_STATE"
            return result
    for relpath, required in rule["evidence_fields"].items():
        path = (engine.ROOT / relpath).resolve()
        if not path.is_relative_to(engine.ROOT.resolve()) or not path.is_file():
            result["reason"] = "MISSING_SOURCE_EVIDENCE:" + relpath
            return result
        try:
            with path.open(encoding="utf-8-sig", newline="") as source:
                reader = csv.DictReader(source)
                if not reader.fieldnames or not set(required).issubset(reader.fieldnames):
                    result["reason"] = "MISSING_SOURCE_COLUMNS:" + relpath
                    return result
                count = sum(1 for row in reader if row is not None)
        except (UnicodeError, OSError, csv.Error) as exc:
            result["reason"] = "INVALID_SOURCE_EVIDENCE:" + type(exc).__name__
            return result
        if count == 0:
            result["reason"] = "EMPTY_SOURCE_EVIDENCE:" + relpath
            return result
        result["evidence"][relpath] = {"sha256": sha(path), "rows": count,
                                       "required_columns": list(required)}
    result["origin_task"] = matches[0]["id"]
    result["status"] = "QUALIFIED"
    return result


def assessment(state=None):
    if state is None:
        state = engine.read_state()
    engine.validate_graph(state)
    source_items = [
        {"id": t["id"], "title": t["title"], "status": t["status"]}
        for t in state["tasks"].values()
        if t.get("source") == "TODO.md" and t.get("program_id") == "FD-P1"
        and t["status"] == "BACKLOG"]
    external = []
    for task in source_items:
        matched = next((reason for phrase, reason in EXTERNAL_REQUIREMENTS
                        if phrase.casefold() in task["title"].casefold()), None)
        if matched:
            external.append({"task_id": task["id"], "reason": matched,
                             "status": "EVIDENCE_REQUIRED"})
    return {
        "schema_version": 1,
        "continuity_id": "FD-AUTONOMY-V1",
        "rule_version": RULESET_VERSION,
        "program": "FD-P1",
        "source_head": engine.git_sha(),
        "roadmap_sha256": sha(engine.ROOT / "ROADMAP.md"),
        "todo_sha256": sha(engine.ROOT / "TODO.md"),
        "rules": [inspect_rule(rule, state) for rule in RULES],
        "external_requirements": external,
        "not_in_scope": "Completing PDF extraction, backfills or obtaining external files",
    }


def build(rule, decision):
    return {
        "id": rule["id"], "version": 1, "title": rule["title"],
        "program_id": "FD-P1", "priority": rule["priority"],
        "dependencies": list(rule["dependencies"]),
        "source_task_id": decision["origin_task"],
        "qualification_rule": rule["rule"],
        "qualification_rule_version": RULESET_VERSION,
        "source_evidence": decision["evidence"],
        "allowed_paths": ["src/financialdata/", "tests/"],
        "requirements": rule["requirements"],
        "acceptance": list(rule["acceptance"]),
        "risk_class": "READ_ONLY_ENGINEERING",
    }


def qualify():
    """Append only verified engineering blueprints; persist one decision receipt.

    The caller commits blueprints.json, state.json and evidence in one Git
    commit, using the EXISTING publisher and optimistic main SHA.
    """
    engine.assert_main_only()
    state = engine.read_state()
    engine.validate_event_chain(state)
    if any(t["status"] == "PUBLISHED_PENDING_CI" for t in state["tasks"].values()):
        return {"added": [], "reason": "PENDING_CI"}
    if tasking.selected(state):
        return {"added": [], "reason": "WORK_ALREADY_READY"}
    current = json.loads(tasking.BLUEPRINTS.read_text(encoding="utf-8"))
    if current.get("schema_version") != 1:
        raise ValueError("Unknown blueprint schema")
    before = {item["id"] for item in current["tasks"]}
    verdict = assessment(state)
    additions = []
    for rule, decision in zip(RULES, verdict["rules"]):
        if rule["id"] in before:
            continue
        if decision["status"] != "QUALIFIED":
            continue
        candidate = build(rule, decision)
        additions.append(candidate)
    if not additions:
        return {"added": [], "reason": "NO_NEW_QUALIFIED_WORK", "assessment": verdict}
    # Fail closed before any disk mutation.
    for candidate in additions:
        if not candidate["allowed_paths"] == ["src/financialdata/", "tests/"]:
            raise ValueError("Unreviewed write scope")
    current["tasks"].extend(additions)
    ids = [item["id"] for item in current["tasks"]]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate task after qualification")
    receipt = dict(verdict)
    receipt["added_ids"] = [entry["id"] for entry in additions]
    receipt["policy"] = "READ_ONLY_ENGINEERING_ONLY"
    engine.atomic_write(tasking.BLUEPRINTS,
                        json.dumps(current, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    engine.atomic_write(engine.ROOT / EVIDENCE,
                        json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    # Existing tasking projection remains the only authoritative task database.
    tasking.hydrate()
    return {"added": receipt["added_ids"], "reason": "QUALIFIED_BY_PROGRAM",
            "evidence": EVIDENCE}


def main(argv=None):
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write qualified safe blueprints")
    args = parser.parse_args(argv)
    try:
        result = qualify() if args.apply else assessment()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, RuntimeError, KeyError, OSError, csv.Error) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
