"""Tests for conversational agent admission without inventing runtime authority."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from factory import engine, tasking, entry


class AgentEntryTests(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.folder = self.root / "factory"
        self.folder.mkdir()
        (self.root / "ROADMAP.md").write_text("## P1 — SOURCE\n## P2 — RAW\n", encoding="utf-8")
        (self.root / "TODO.md").write_text(
            "## P1 — SOURCE\n- [ ] Validate unclassified financial PDFs\n",
            encoding="utf-8")
        patches = [
            patch.object(engine, "ROOT", self.root),
            patch.object(engine, "FACTORY", self.folder),
            patch.object(engine, "STATE", self.folder / "state.json"),
            patch.object(engine, "git_sha", return_value="a" * 40),
            patch.object(engine, "git_branch", return_value="main"),
            patch.object(engine, "audit", return_value={"ok": True, "errors": [], "warnings": []})
        ]
        for item in patches:
            item.start()
            self.addCleanup(item.stop)
        tasking.hydrate()

    def test_read_only_arrival_finds_approved_work(self):
        before = engine.STATE.read_bytes()
        result = entry.read_only_admission("chatgpt-restart", "coder")
        self.assertEqual(result["decision"], "APPROVED_WORK_AVAILABLE")
        self.assertEqual(result["selected_blueprint"], "FD-AUTO-P1-MANIFEST-CHECKER")
        self.assertEqual(result["continuity_id"], "FD-AUTONOMY-V1")
        self.assertEqual(result["head_sha"], "a" * 40)
        self.assertFalse(result["github_identity_verified"])
        self.assertTrue(result["read_only"])
        self.assertFalse(result["execution_modes"]["CONNECTED_CODING_AGENT"]["additional_model_api_key_required"])
        self.assertTrue(result["execution_modes"]["HOSTED_ACTIONS_GENERATOR"]["additional_model_api_key_required_for_untemplated_work"])
        self.assertEqual(tuple(result["canonical_files"]), entry.CANONICAL_READ_ORDER)
        self.assertEqual(result["operational_files_after_canonical"][0], "ROADMAP.md")
        self.assertEqual(len(result["canonical_files"]), 11)
        self.assertEqual(engine.STATE.read_bytes(), before)

    def test_waiting_for_ci_is_first_priority(self):
        tasking.mark_published("FD-AUTO-P1-MANIFEST-CHECKER", 7001,
                               "a" * 40, ["tests/test_x.py"],
                               "factory/evidence/test.json")
        result = entry.read_only_admission("chatgpt-restart", "coder")
        self.assertEqual(result["decision"], "CI_ATTESTATION_REQUIRED")
        self.assertEqual(result["pending_ci"][0]["run_id"], 7001)

    def test_program_qualification_after_bootstrap_done(self):
        for seq, task_id in enumerate(("FD-AUTO-P1-MANIFEST-CHECKER",
                                       "FD-AUTO-P1-HASH-CHECKER"), 1):
            tasking.mark_published(task_id, 8000 + seq,
                                   "a" * 40, ["tests/test_x.py"],
                                   "factory/evidence/test.json")
            tasking.reconcile_verdict(task_id, 8000 + seq, "success",
                                     "https://github.com/example/runs/ok")
        before = engine.STATE.read_bytes()
        result = entry.read_only_admission("claude-session", "coder")
        self.assertEqual(result["decision"], "PROGRAM_QUALIFICATION_REQUIRED")
        self.assertIsNone(result["selected_blueprint"])
        self.assertTrue(result["qualification_candidates"])
        self.assertEqual(result["qualification_candidates"][0]["program_id"], "FD-P1")
        self.assertEqual(engine.STATE.read_bytes(), before)

    def test_errors_block_admission(self):
        with patch.object(engine, "audit", return_value={
            "ok": False, "errors": ["INVALID_SOURCE"], "warnings": []}):
            result = entry.read_only_admission("chatgpt-restart", "coder")
        self.assertEqual(result["decision"], "BLOCKED_BY_AUDIT")
        self.assertEqual(result["audit"]["errors"], ["INVALID_SOURCE"])

    def test_identity_and_branch_fail_closed(self):
        with self.assertRaises(ValueError):
            entry.read_only_admission("../../unsafe", "coder")
        with self.assertRaises(ValueError):
            entry.read_only_admission("agent-ok", "administrator")
        with patch.object(engine, "git_branch", return_value="feature/bypass"):
            with self.assertRaises(RuntimeError):
                entry.read_only_admission("agent-ok", "coder")
        with patch.object(engine, "git_sha", return_value=None):
            with self.assertRaises(RuntimeError):
                entry.read_only_admission("agent-ok", "coder")

    def test_event_integrity_enforced(self):
        data = json.loads(engine.STATE.read_text(encoding="utf-8"))
        data["events"][0]["event"] = "ALTERED"
        engine.STATE.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaises(ValueError):
            entry.read_only_admission("agent-ok", "coder")


if __name__ == "__main__":
    unittest.main()
