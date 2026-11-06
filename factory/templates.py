"""Vetted, deterministic source adapters for bootstrap blueprints, not an LLM."""

MANIFEST = '''"""Read-only audit of SOURCE CSV metadata, preserving source facts."""
import csv
from pathlib import Path


def validate_manifest(path):
    """Return a traceable diagnostic without mutating the given CSV."""
    file_path = Path(path)
    report = {"path": str(file_path), "total_rows": 0, "distinct_source_ids": 0,
              "missing_source_ids": [], "duplicate_source_ids": [], "errors": []}
    try:
        with file_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None or "source_drive_file_id" not in reader.fieldnames:
                report["errors"].append("MISSING_SOURCE_DRIVE_FILE_ID_COLUMN")
                return report
            observed = set()
            for row_number, row in enumerate(reader, 2):
                report["total_rows"] += 1
                source_id = row.get("source_drive_file_id")
                source_id = source_id.strip() if isinstance(source_id, str) else ""
                if not source_id:
                    report["missing_source_ids"].append(row_number)
                elif source_id in observed:
                    report["duplicate_source_ids"].append(source_id)
                else:
                    observed.add(source_id)
            report["distinct_source_ids"] = len(observed)
    except (OSError, UnicodeError, csv.Error) as exc:
        report["errors"].append(type(exc).__name__)
    return report
'''

MANIFEST_TEST = '''"""SOURCE manifest verification without data mutations."""
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
            path.write_text("source_drive_file_id,name\\nA,first\\nA,second\\n,missing\\nB,third\\n", encoding="utf-8")
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
            path.write_text("other\\nvalue\\n", encoding="utf-8")
            self.assertIn("MISSING_SOURCE_DRIVE_FILE_ID_COLUMN", validate_manifest(path)["errors"])

    def test_missing_file(self):
        report = validate_manifest("/definitely/absent/document.csv")
        self.assertIn("FileNotFoundError", report["errors"])
'''

HASH = '''"""Structural SHA registry checker; never deletes a source row."""
import csv
from pathlib import Path
import re


def check_hash_register(path):
    report = {"path": str(path), "total_rows": 0, "distinct_files": 0,
              "invalid_hash_rows": [], "duplicate_file_ids": [],
              "exact_duplicate_groups": [], "errors": []}
    ids = set()
    groups = {}
    try:
        with Path(path).open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or not {"source_drive_file_id", "sha256"}.issubset(reader.fieldnames):
                report["errors"].append("MISSING_HASH_REGISTER_COLUMNS")
                return report
            for row_number, row in enumerate(reader, 2):
                report["total_rows"] += 1
                identifier = (row.get("source_drive_file_id") or "").strip()
                value = (row.get("sha256") or "").strip()
                if not identifier or identifier in ids:
                    report["duplicate_file_ids"].append(row_number)
                ids.add(identifier)
                if not re.fullmatch("[a-f0-9]{64}", value):
                    report["invalid_hash_rows"].append(row_number)
                else:
                    groups.setdefault(value, []).append(identifier)
        report["distinct_files"] = len(ids - {""})
        report["exact_duplicate_groups"] = [
            {"sha256": h, "source_drive_file_ids": sorted(files)}
            for h, files in sorted(groups.items()) if len(files) > 1]
    except (OSError, UnicodeError, csv.Error) as exc:
        report["errors"].append(type(exc).__name__)
    return report
'''

HASH_TEST = '''"""Verifies distinct documents stay distinct when hashes match."""
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
            path.write_text("source_drive_file_id,sha256\\nA," + "a"*64 + "\\nB," + "a"*64 + "\\n", encoding="utf-8")
            before = path.read_bytes()
            report = check_hash_register(path)
            self.assertEqual(report["total_rows"], 2)
            self.assertEqual(report["distinct_files"], 2)
            self.assertEqual(report["exact_duplicate_groups"][0]["source_drive_file_ids"], ["A", "B"])
            self.assertEqual(path.read_bytes(), before)

    def test_invalid_hash_and_duplicate_id(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "hash.csv"
            path.write_text("source_drive_file_id,sha256\\nA,NOT_SHA\\nA," + "b"*64 + "\\n", encoding="utf-8")
            report = check_hash_register(path)
            self.assertEqual(report["invalid_hash_rows"], [2])
            self.assertEqual(report["duplicate_file_ids"], [3])

    def test_bad_header(self):
        with TemporaryDirectory() as temp:
            path = Path(temp) / "bad.csv"
            path.write_text("abc\\nx\\n", encoding="utf-8")
            self.assertIn("MISSING_HASH_REGISTER_COLUMNS", check_hash_register(path)["errors"])
'''


def generate(task_id):
    """Return approved code files; None means a real model is required."""
    if task_id == "FD-AUTO-P1-MANIFEST-CHECKER":
        return [
            {"path": "src/financialdata/__init__.py", "content": '"""BRVM source verification package."""\n'},
            {"path": "src/financialdata/manifest_checker.py", "content": MANIFEST},
            {"path": "tests/test_manifest_checker.py", "content": MANIFEST_TEST},
        ]
    if task_id == "FD-AUTO-P1-HASH-CHECKER":
        return [
            {"path": "src/financialdata/hash_checker.py", "content": HASH},
            {"path": "tests/test_hash_checker.py", "content": HASH_TEST},
        ]
    return None
