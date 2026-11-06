"""P1 coverage diagnostics must never alter published manifests."""
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from financialdata.coverage_checker import coverage_report


class CoverageTests(unittest.TestCase):
    def test_incomplete_manifest_keeps_truth(self):
        with TemporaryDirectory() as tmp:
            issuers, docs = Path(tmp) / "issuers.csv", Path(tmp) / "documents.csv"
            issuers.write_text("ticker,pdf_count\nB,1\nA,2\nALL,3\n", encoding="utf-8")
            docs.write_text(
                "issuer_folder_ticker,source_drive_file_id\nA,one\nA,one\n",
                encoding="utf-8")
            before = (issuers.read_bytes(), docs.read_bytes())
            result = coverage_report(issuers, docs)
            self.assertEqual(result["indexed_documents"], 3)
            self.assertEqual(result["master_manifest_documents"], 2)
            self.assertEqual(result["unrepresented_documents"], 1)
            self.assertEqual(result["duplicate_drive_ids"], ["one"])
            self.assertEqual(result["by_issuer"][1]["ticker"], "B")
            self.assertEqual((issuers.read_bytes(), docs.read_bytes()), before)

    def test_unknown_or_missing_id(self):
        with TemporaryDirectory() as tmp:
            issuers, docs = Path(tmp) / "issuers.csv", Path(tmp) / "documents.csv"
            issuers.write_text("ticker,pdf_count\nA,1\nALL,1\n", encoding="utf-8")
            docs.write_text(
                "issuer_folder_ticker,source_drive_file_id\nC,\n", encoding="utf-8")
            result = coverage_report(issuers, docs)
            self.assertEqual(result["unknown_issuer_rows"], [2])
            self.assertEqual(result["missing_drive_id_rows"], [2])

    def test_corrupt_source_does_not_claim_success(self):
        with TemporaryDirectory() as tmp:
            issuers, docs = Path(tmp) / "issuers.csv", Path(tmp) / "documents.csv"
            issuers.write_text("badcolumn\nx\n", encoding="utf-8")
            docs.write_text("issuer_folder_ticker,source_drive_file_id\nA,1\n", encoding="utf-8")
            self.assertTrue(coverage_report(issuers, docs)["errors"])
