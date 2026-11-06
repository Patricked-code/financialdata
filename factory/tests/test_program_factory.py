"""Program-level automatic blueprint qualification and SOURCE provenance guards."""
import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from factory import engine, tasking, program_factory, templates, coder


class ProgramQualificationTests(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.folder = self.root / "factory"
        self.folder.mkdir()
        (self.root / "inventory").mkdir()
        (self.root / "ROADMAP.md").write_text(
            "## P1 — Inventaire documentaire exhaustif du corpus existant\n"
            "## P2 — RAW v1\n", encoding="utf-8")
        self.original_todo = (
            "## P1 — SOURCE\n"
            "- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.\n"
            "- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.\n"
            "- [ ] CFAC : recheck live strict du snapshot 94, puis SHA exhaustif.\n")
        (self.root / "TODO.md").write_text(self.original_todo, encoding="utf-8")
        self.issuers = self.root / "inventory/p1_issuer_manifest.csv"
        self.docs = self.root / "inventory/p1_document_manifest.csv"
        self.issuers.write_text(
            "ticker,pdf_count\nA,2\nB,1\nALL,3\n", encoding="utf-8")
        self.docs.write_text(
            "source_drive_file_id,source_file_id,issuer_folder_ticker,"
            "economic_period_status,period_start,period_end\n"
            "z,DRIVE:z,A,UNRESOLVED,,\n", encoding="utf-8")
        self.snapshot = {str(p): p.read_bytes() for p in
                         (self.root / "TODO.md", self.root / "ROADMAP.md",
                          self.issuers, self.docs)}
        # Isolate the historical bootstrap baseline even after the real
        # workflow has already appended its program-qualified blueprints.
        initial_blueprints = json.loads(tasking.BLUEPRINTS.read_text(encoding="utf-8"))
        kept = {"FD-AUTO-P1-MANIFEST-CHECKER", "FD-AUTO-P1-HASH-CHECKER"}
        initial_blueprints["tasks"] = [
            blueprint for blueprint in initial_blueprints["tasks"]
            if blueprint["id"] in kept]
        self.assertEqual(len(initial_blueprints["tasks"]), 2)
        self.blueprints = self.folder / "blueprints.json"
        self.blueprints.write_text(json.dumps(initial_blueprints), encoding="utf-8")
        self.patches = [
            patch.object(engine, "ROOT", self.root),
            patch.object(engine, "FACTORY", self.folder),
            patch.object(engine, "STATE", self.folder / "state.json"),
            patch.object(tasking, "BLUEPRINTS", self.blueprints),
            patch.object(engine, "git_sha", return_value="a"*40),
            patch.object(engine, "git_branch", return_value="main"),
        ]
        for item in self.patches:
            item.start()
            self.addCleanup(item.stop)
        tasking.hydrate()
        # Simulate proven, immutable bootstrap tasks; never alter source TODO.
        with engine.exclusive_lock():
            state = engine.read_state()
            for item in ("FD-AUTO-P1-MANIFEST-CHECKER", "FD-AUTO-P1-HASH-CHECKER"):
                state["tasks"][item]["status"] = "DONE"
            engine.record(state, "FIXTURE_ATTESTATION", run_id=1)
            engine.save_state(state)

    def test_qualified_from_roadmap_and_manifest_evidence(self):
        result = program_factory.qualify()
        self.assertEqual(result["reason"], "QUALIFIED_BY_PROGRAM")
        self.assertEqual(len(result["added"]), 2)
        state = engine.read_state()
        coverage = state["tasks"]["FD-AUTO-P1-COVERAGE-DIAGNOSTIC"]
        temporal = state["tasks"]["FD-AUTO-P1-TEMPORAL-DIAGNOSTIC"]
        self.assertEqual(coverage["status"], "BACKLOG")
        self.assertEqual(temporal["status"], "BACKLOG")
        self.assertEqual(tasking.selected(state)["id"], coverage["id"])
        self.assertEqual(temporal["dependencies"], [coverage["id"]])
        blueprint = next(b for b in tasking.blueprints() if b["id"] == coverage["id"])
        self.assertEqual(blueprint["risk_class"], "READ_ONLY_ENGINEERING")
        self.assertEqual(blueprint["source_evidence"]["inventory/p1_issuer_manifest.csv"]["rows"], 3)
        self.assertTrue(blueprint["source_task_id"].startswith("FD-T-"))
        receipt = json.loads((self.folder / "evidence/program-qualification.json").read_text())
        self.assertEqual(receipt["added_ids"], result["added"])
        for path, data in self.snapshot.items():
            self.assertEqual(Path(path).read_bytes(), data)
        engine.validate_event_chain(state)

    def test_repeated_qualification_does_not_duplicate_blueprints(self):
        program_factory.qualify()
        first = len(tasking.blueprints())
        # tasking.blueprints() returns list, and qualifying twice is a no-op.
        again = program_factory.qualify()
        self.assertEqual(again["added"], [])
        self.assertEqual(first, len(tasking.blueprints()))

    def test_missing_source_evidence_fails_closed(self):
        self.docs.unlink()
        decision = program_factory.qualify()
        self.assertEqual(decision["added"], [])
        # First rule requires docs and blocks; second too.
        self.assertEqual(len(tasking.blueprints()), 2)
        self.assertFalse((self.folder / "evidence/program-qualification.json").exists())
        rules = program_factory.assessment()["rules"]
        self.assertTrue(all(r["status"] == "BLOCKED" for r in rules))

    def test_todo_unrelated_text_fails_closed(self):
        (self.root / "TODO.md").write_text(
            "## P1 — SOURCE\n- [ ] collect every PDF from internet right now\n",
            encoding="utf-8")
        engine.bootstrap()
        result = program_factory.qualify()
        self.assertEqual(result["added"], [])
        self.assertEqual(len(tasking.blueprints()), 2)

    def test_source_drift_suspends_ready_work(self):
        program_factory.qualify()
        self.assertEqual(tasking.selected()["id"], "FD-AUTO-P1-COVERAGE-DIAGNOSTIC")
        self.docs.write_text(self.docs.read_text(encoding="utf-8") + "new,DRIVE:new,B,UNRESOLVED,,\n", encoding="utf-8")
        self.assertIsNone(tasking.selected())
        rules = program_factory.assessment()["rules"]
        self.assertEqual(rules[0]["status"], "STALE_EVIDENCE")
        self.assertEqual(rules[0]["reason"], "SOURCE_CHANGED_SINCE_QUALIFICATION")

    def test_templates_are_bounded_and_python_valid(self):
        for identifier in ("FD-AUTO-P1-COVERAGE-DIAGNOSTIC",
                           "FD-AUTO-P1-TEMPORAL-DIAGNOSTIC"):
            files = templates.generate(identifier)
            self.assertTrue(files)
            self.assertTrue(any(p["path"].startswith("tests/test_") for p in files))
            for item in files:
                compile(item["content"], item["path"], "exec")
        program_factory.qualify()
        bp = next(x for x in tasking.blueprints()
                  if x["id"] == "FD-AUTO-P1-COVERAGE-DIAGNOSTIC")
        proposal = {
            "schema_version": 1, "continuity_id": "FD-AUTONOMY-V1",
            "task_id": bp["id"], "blueprint_version": 1, "base_sha": "a"*40,
            "files": templates.generate(bp["id"]),
        }
        coder.validate(proposal)


if __name__ == "__main__":
    unittest.main()
