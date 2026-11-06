"""Non-regression tests for the standalone factory."""
import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from factory import engine


class FactoryTest(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.factory_dir = self.root / "factory"
        self.factory_dir.mkdir()
        (self.root / "inventory" / "hashes").mkdir(parents=True)
        for name in engine.PROTECTED:
            (self.root / name).write_text(name, encoding="utf-8")
        (self.root / "ROADMAP.md").write_text("## P0 — Governance\n## P1 — Sources\n## P2 — RAW\n", encoding="utf-8")
        (self.root / "TODO.md").write_text(
            "## P1 — Sources\n- [x] Collect initial issuers\n- [ ] Verify PDFs\n"
            "## P2 — Schema\n- [ ] Define RAW v1\n", encoding="utf-8")
        (self.root / "SUIVI.md").write_text("V23 = 3 157 PDF\n", encoding="utf-8")
        issuer = self.root / "inventory" / "p1_issuer_manifest.csv"
        with issuer.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["ordinal", "ticker", "pdf_count", "inventory_path", "status"])
            for i in range(48):
                writer.writerow([i+1, "C"+str(i), "1", "inventory/C.md", "INVENTORIED"])
            writer.writerow(["TOTAL", "ALL", "48", "inventory/index.md", "COMPLETE"])
        (self.root / "inventory" / "p1_document_manifest.csv").write_text(
            "source_drive_file_id,source_filename_raw\nDRIVE:1,one.pdf\n", encoding="utf-8")
        cf = self.root / "inventory" / "hashes" / "CFAC.csv"
        with cf.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["issuer_ticker", "source_drive_file_id", "source_filename_raw",
                             "file_size_bytes", "sha256", "duplicate_group_id", "hash_status"])
            for i in range(114):
                writer.writerow(["CFAC", str(i), str(i) + ".pdf", 100,
                                 f"{i:064x}", "", "COMPUTED_SIZE_VALIDATED"])
        self.patches = [
            patch.object(engine, "ROOT", self.root),
            patch.object(engine, "FACTORY", self.factory_dir),
            patch.object(engine, "STATE", self.factory_dir / "state.json"),
            patch.object(engine, "git_branch", return_value="main"),
            patch.object(engine, "git_sha", return_value="a"*40)
        ]
        for item in self.patches:
            item.start()
            self.addCleanup(item.stop)

    def test_bootstrap_is_idempotent(self):
        state = engine.bootstrap()
        self.assertEqual(len(state["programs"]), len(engine.PROGRAMS))
        self.assertEqual(len(state["tasks"]), 5)
        self.assertEqual(len(engine.bootstrap()["events"]), 1)
        self.assertEqual(len(engine.read_state()["tasks"]), 5)

    def test_source_backlog_and_evidence_chain(self):
        engine.bootstrap()
        engine.admit("auditor-1", ["audit"])
        result = engine.run("auditor-1")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(r["status"] == "DONE" for r in result))
        state = engine.read_state()
        engine.validate_event_chain(state)
        self.assertTrue((self.root / "factory/evidence/FD-A-STRUCTURE.json").is_file())
        self.assertEqual(engine.status()["by_status"]["DONE"], 3)

    def test_coder_claim_recovery_and_ownership(self):
        engine.bootstrap()
        engine.admit("coder-1", ["coder"])
        first = engine.claim("coder-1")
        self.assertEqual(first["kind"], "agent_code")
        self.assertEqual(engine.claim("coder-1")["id"], first["id"])
        with self.assertRaises(ValueError):
            engine.finish("coder-2", first["id"], "commit:123")
        engine.finish("coder-1", first["id"], "commit:"+"a"*40+"; tests:PASS")
        self.assertEqual(engine.read_state()["tasks"][first["id"]]["status"], "DONE")

    def test_no_branch_or_arbitrary_write(self):
        with patch.object(engine, "git_branch", return_value="feature/unsafe"):
            with self.assertRaises(RuntimeError):
                engine.bootstrap()
        with self.assertRaises(ValueError):
            engine.atomic_write(self.root / "TODO.md", "NO")
        self.assertIn("Verify PDFs", (self.root / "TODO.md").read_text(encoding="utf-8"))

    def test_event_tampering_fails(self):
        engine.bootstrap()
        data = json.loads(engine.STATE.read_text(encoding="utf-8"))
        data["events"][0]["event"] = "ALTERED"
        engine.STATE.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaises(ValueError):
            engine.validate_event_chain(engine.read_state())

    def test_audit_detects_stale_suivi_and_duplicates(self):
        engine.bootstrap()
        result = engine.audit()
        self.assertTrue(result["ok"])
        self.assertIn("DOCUMENT_MANIFEST_INCOMPLETE", result["warnings"])
        (self.root / "SUIVI.md").write_text("V22 = 3 137 PDF\n", encoding="utf-8")
        self.assertTrue(engine.audit()["ok"])
        (self.root / "inventory/p1_document_manifest.csv").write_text(
            "source_drive_file_id\nA\nA\n", encoding="utf-8")
        self.assertIn("DOCUMENT_MANIFEST_DUPLICATE_DRIVE_ID", engine.audit()["errors"])


if __name__ == "__main__":
    unittest.main()
