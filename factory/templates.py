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
    if task_id == "FD-AUTO-P1-COVERAGE-DIAGNOSTIC":
        return [
            {"path": "src/financialdata/coverage_checker.py", "content": COVERAGE},
            {"path": "tests/test_coverage_checker.py", "content": COVERAGE_TEST},
        ]
    if task_id == "FD-AUTO-P1-TEMPORAL-DIAGNOSTIC":
        return [
            {"path": "src/financialdata/temporal_checker.py", "content": TEMPORAL},
            {"path": "tests/test_temporal_checker.py", "content": TEMPORAL_TEST},
        ]
    return None

# Reviewed, SOURCE-preserving engineering templates promoted from the P1 program.
COVERAGE = '''"""P1 issuer coverage report: read-only diagnostics, not PDF acquisition."""
import csv
from collections import Counter
from pathlib import Path


def _rows(path, fields):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not set(fields).issubset(reader.fieldnames):
            raise ValueError("Missing required SOURCE columns")
        return list(reader)


def coverage_report(issuer_manifest, document_manifest):
    """Compare source manifests, retaining every source row and version."""
    report = {
        "issuers": 0, "indexed_documents": 0, "master_manifest_documents": 0,
        "unrepresented_documents": 0, "by_issuer": [],
        "unknown_issuer_rows": [], "missing_drive_id_rows": [],
        "duplicate_drive_ids": [], "errors": [],
    }
    try:
        issuers = _rows(issuer_manifest, ("ticker", "pdf_count"))
        documents = _rows(document_manifest, (
            "issuer_folder_ticker", "source_drive_file_id"))
        known = [row for row in issuers if row["ticker"] != "ALL"]
        tickers = [row["ticker"] for row in known]
        if len(tickers) != len(set(tickers)):
            report["errors"].append("DUPLICATE_ISSUER_TICKER")
        if len([row for row in issuers if row["ticker"] == "ALL"]) != 1:
            report["errors"].append("INVALID_TOTAL_ROW")
        report["issuers"] = len(known)
        report["indexed_documents"] = sum(int(row["pdf_count"]) for row in known)
        report["master_manifest_documents"] = len(documents)
        counts = Counter(row["issuer_folder_ticker"] for row in documents)
        identifiers = Counter(row["source_drive_file_id"] for row in documents
                              if row.get("source_drive_file_id"))
        report["duplicate_drive_ids"] = sorted(k for k, n in identifiers.items() if n > 1)
        for row_number, row in enumerate(documents, 2):
            if not row.get("source_drive_file_id"):
                report["missing_drive_id_rows"].append(row_number)
            if row["issuer_folder_ticker"] not in tickers:
                report["unknown_issuer_rows"].append(row_number)
        for row in sorted(known, key=lambda row: row["ticker"]):
            expected = int(row["pdf_count"])
            represented = counts[row["ticker"]]
            report["by_issuer"].append({
                "ticker": row["ticker"], "indexed": expected,
                "manifest": represented, "unrepresented": max(0, expected - represented),
                "excess": max(0, represented - expected)})
        report["unrepresented_documents"] = sum(row["unrepresented"] for row in report["by_issuer"])
        total = next((row for row in issuers if row["ticker"] == "ALL"), None)
        if total and int(total["pdf_count"]) != report["indexed_documents"]:
            report["errors"].append("INDEX_TOTAL_MISMATCH")
    except (ValueError, OSError, UnicodeError, csv.Error) as exc:
        report["errors"].append(type(exc).__name__ + ":" + str(exc)[:120])
    return report
'''

COVERAGE_TEST = '''"""P1 coverage diagnostics must never alter published manifests."""
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
            issuers.write_text("ticker,pdf_count\\nB,1\\nA,2\\nALL,3\\n", encoding="utf-8")
            docs.write_text(
                "issuer_folder_ticker,source_drive_file_id\\nA,one\\nA,one\\n",
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
            issuers.write_text("ticker,pdf_count\\nA,1\\nALL,1\\n", encoding="utf-8")
            docs.write_text(
                "issuer_folder_ticker,source_drive_file_id\\nC,\\n", encoding="utf-8")
            result = coverage_report(issuers, docs)
            self.assertEqual(result["unknown_issuer_rows"], [2])
            self.assertEqual(result["missing_drive_id_rows"], [2])

    def test_corrupt_source_does_not_claim_success(self):
        with TemporaryDirectory() as tmp:
            issuers, docs = Path(tmp) / "issuers.csv", Path(tmp) / "documents.csv"
            issuers.write_text("badcolumn\\nx\\n", encoding="utf-8")
            docs.write_text("issuer_folder_ticker,source_drive_file_id\\nA,1\\n", encoding="utf-8")
            self.assertTrue(coverage_report(issuers, docs)["errors"])
'''

TEMPORAL = '''"""Read-only P1 economic-period completeness: no filename inference."""
import csv
from datetime import date
from pathlib import Path


def temporal_report(path):
    result = {"rows": 0, "resolved": 0, "unresolved_rows": [],
              "invalid_date_rows": [], "reversed_period_rows": [], "errors": []}
    required = {"source_drive_file_id", "economic_period_status",
                "period_start", "period_end"}
    try:
        with Path(path).open(encoding="utf-8-sig", newline="") as source:
            reader = csv.DictReader(source)
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                result["errors"].append("MISSING_TEMPORAL_COLUMNS")
                return result
            for line, row in enumerate(reader, 2):
                result["rows"] += 1
                start, end = (row.get("period_start") or "").strip(), (
                    row.get("period_end") or "").strip()
                status = (row.get("economic_period_status") or "").strip()
                if not (start and end) or status != "CONTENT_RESOLVED":
                    result["unresolved_rows"].append(line)
                    continue
                try:
                    start_date, end_date = date.fromisoformat(start), date.fromisoformat(end)
                except ValueError:
                    result["invalid_date_rows"].append(line)
                    continue
                if start_date > end_date:
                    result["reversed_period_rows"].append(line)
                else:
                    result["resolved"] += 1
    except (OSError, UnicodeError, csv.Error) as exc:
        result["errors"].append(type(exc).__name__)
    return result
'''

TEMPORAL_TEST = '''"""Temporal status never becomes a derived published date."""
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from financialdata.temporal_checker import temporal_report


class TemporalTests(unittest.TestCase):
    def test_different_period_states_without_inference(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "docs.csv"
            p.write_text(
                "source_drive_file_id,economic_period_status,period_start,period_end\\n"
                "a,CONTENT_RESOLVED,2023-01-01,2023-12-31\\n"
                "b,UNRESOLVED,,\\n"
                "c,CONTENT_RESOLVED,2023-13-01,2023-12-31\\n"
                "d,CONTENT_RESOLVED,2025-01-01,2024-12-31\\n", encoding="utf-8")
            before = p.read_bytes()
            result = temporal_report(p)
            self.assertEqual(result["rows"], 4)
            self.assertEqual(result["resolved"], 1)
            self.assertEqual(result["unresolved_rows"], [3])
            self.assertEqual(result["invalid_date_rows"], [4])
            self.assertEqual(result["reversed_period_rows"], [5])
            self.assertEqual(p.read_bytes(), before)

    def test_missing_columns(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "docs.csv"
            p.write_text("id\\nx\\n", encoding="utf-8")
            self.assertIn("MISSING_TEMPORAL_COLUMNS", temporal_report(p)["errors"])
'''
