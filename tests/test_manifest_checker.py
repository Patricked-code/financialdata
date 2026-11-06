"""SOURCE manifest verification without data mutations."""
import csv
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from financialdata.manifest_checker import validate_manifest

class ManifestTests(unittest.TestCase):
    def test_duplicate_missing_and_no_mutation(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "source.csv"
            path.write_text("source_drive_file_id,name\nA,first\nA,second\n,missing\nB,third\n", encoding="utf-8")
            before = path.read_bytes()
            report = validate_manifest(path)
            self.assertEqual(report["total_rows"], 4)
            self.assertEqual(report["distinct_source_ids"], 2)
            self.assertEqual(report["duplicate_source_ids"], ["A"])
            self.assertEqual(report["missing_source_ids"], [4])
            self.assertEqual(path.read_bytes(), before)

    def test_missing_header(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "bad.csv"
            path.write_text("other\nvalue\n", encoding="utf-8")
            self.assertIn("MISSING_SOURCE_DRIVE_FILE_ID_COLUMN", validate_manifest(path)["errors"])

    def test_missing_file(self):
        report = validate_manifest("/definitely/absent/document.csv")
        self.assertIn("FileNotFoundError", report["errors"])
