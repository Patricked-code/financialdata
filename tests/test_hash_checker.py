"""Verifies distinct documents stay distinct when hashes match."""
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from financialdata.hash_checker import check_hash_register

class HashTests(unittest.TestCase):
    def test_exact_duplicates_preserve_two_rows(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "hash.csv"
            path.write_text("source_drive_file_id,sha256\nA," + "a"*64 + "\nB," + "a"*64 + "\n", encoding="utf-8")
            before = path.read_bytes()
            report = check_hash_register(path)
            self.assertEqual(report["total_rows"], 2)
            self.assertEqual(report["distinct_files"], 2)
            self.assertEqual(report["exact_duplicate_groups"][0]["source_drive_file_ids"], ["A", "B"])
            self.assertEqual(path.read_bytes(), before)

    def test_invalid_hash_and_duplicate_id(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "hash.csv"
            path.write_text("source_drive_file_id,sha256\nA,NOT_SHA\nA," + "b"*64 + "\n", encoding="utf-8")
            report = check_hash_register(path)
            self.assertEqual(report["invalid_hash_rows"], [2])
            self.assertEqual(report["duplicate_file_ids"], [3])

    def test_bad_header(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "bad.csv"
            path.write_text("abc\nx\n", encoding="utf-8")
            self.assertIn("MISSING_HASH_REGISTER_COLUMNS", check_hash_register(path)["errors"])
