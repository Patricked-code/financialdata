"""Single-authority scheduler, UTL, replay and generated-code security tests."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from factory import engine, tasking, coder

class AutonomousFactoryTests(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.folder = self.root / "factory"
        self.folder.mkdir()
        (self.root / "ROADMAP.md").write_text("## P1 — SOURCE\n## P1-R — Recognition\n## P2 — RAW\n", encoding="utf-8")
        (self.root / "TODO.md").write_text("## P1 — SOURCE\n- [ ] Verify sources\n", encoding="utf-8")
        self.patches = [
            patch.object(engine, "ROOT", self.root),
            patch.object(engine, "FACTORY", self.folder),
            patch.object(engine, "STATE", self.folder / "state.json"),
            patch.object(engine, "git_branch", return_value="main"),
            patch.object(engine, "git_sha", return_value="a"*40)
        ]
        for item in self.patches:
            item.start()
            self.addCleanup(item.stop)

    def test_blueprints_and_units_idempotent(self):
        state = tasking.hydrate()
        task = state["tasks"]["FD-AUTO-P1-MANIFEST-CHECKER"]
        self.assertEqual(task["program_id"], "FD-P1")
        self.assertEqual([x["stage"] for x in task["units"]], list(tasking.STAGES))
        revision = state["revision"]
        self.assertEqual(tasking.hydrate()["revision"], revision)
        self.assertEqual(tasking.selected()["id"], "FD-AUTO-P1-MANIFEST-CHECKER")

    def test_ci_reconciliation_unlocks_next_task(self):
        tasking.hydrate()
        tid = "FD-AUTO-P1-MANIFEST-CHECKER"
        tasking.mark_published(tid, 12345, "a"*40, ["tests/test_x.py"], "factory/evidence/123.json")
        self.assertIsNone(tasking.selected())
        self.assertEqual(tasking.reconcile_verdict(tid, 12345, "success", "https://github.com/example/actions/runs/12345"), "DONE")
        state = engine.read_state()
        self.assertEqual(state["tasks"][tid]["units"][-1]["status"], "DONE")
        self.assertEqual(tasking.selected()["id"], "FD-AUTO-P1-HASH-CHECKER")
        engine.validate_event_chain(state)

    def test_failed_ci_blocks_dependents(self):
        tasking.hydrate()
        tid = "FD-AUTO-P1-MANIFEST-CHECKER"
        tasking.mark_published(tid, 12345, "a"*40, ["tests/test_x.py"], "factory/evidence/123.json")
        self.assertEqual(tasking.reconcile_verdict(tid, 12345, "failure", "https://github.com/example/actions/runs/12345"), "BLOCKED")
        self.assertIsNone(tasking.selected())

    def test_proposal_security(self):
        bp = tasking.blueprints()[0]
        proposal = {"schema_version": 1, "continuity_id": "FD-AUTONOMY-V1",
                    "task_id": bp["id"], "blueprint_version": bp["version"],
                    "base_sha": "a"*40,
                    "files": [{"path": "src/financialdata/validator.py", "content": "def check():\n    return 1\n"},
                              {"path": "tests/test_manifest.py", "content": "import unittest\n"}]}
        coder.validate(proposal)
        bad = json.loads(json.dumps(proposal))
        bad["files"][0]["path"] = "src/financialdata/../../GOVERNANCE.md"
        with self.assertRaises(ValueError):
            coder.validate(bad)
        bad = json.loads(json.dumps(proposal))
        bad["files"][0]["content"] = "import subprocess\n"
        with self.assertRaises(ValueError):
            coder.validate(bad)

    def test_hash_detects_tampering(self):
        bp = tasking.blueprints()[0]
        item = {"schema_version": 1, "continuity_id": "FD-AUTONOMY-V1",
                "task_id": bp["id"], "blueprint_version": 1, "base_sha": "a"*40,
                "files": [{"path": "tests/test_example.py", "content": "import unittest\n"}]}
        path = self.root / "proposal.json"
        coder.save_proposal(item, path)
        coder.load_proposal(path)
        tampered = json.loads(path.read_text(encoding="utf-8"))
        tampered["files"][0]["content"] = "assert False\n"
        path.write_text(json.dumps(tampered), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            coder.load_proposal(path)

    def test_template_coding_without_secrets_and_real_provider_gate(self):
        tasking.hydrate()
        output = self.root / "generated.json"
        with patch.dict("os.environ", {}, clear=True):
            self.assertTrue(coder.generate(output))
            proposal, bp, sha = coder.load_proposal(output)
            self.assertEqual(proposal["task_id"], "FD-AUTO-P1-MANIFEST-CHECKER")
            self.assertTrue(any(p["path"].startswith("tests/test_") for p in proposal["files"]))
            with patch("factory.templates.generate", return_value=None):
                with self.assertRaisesRegex(RuntimeError, "real provider"):
                    coder.generate(self.root / "non_template.json")

if __name__ == "__main__":
    unittest.main()
