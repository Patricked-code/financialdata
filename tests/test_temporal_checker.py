"""Temporal status never becomes a derived published date."""
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
                "source_drive_file_id,economic_period_status,period_start,period_end\n"
                "a,CONTENT_RESOLVED,2023-01-01,2023-12-31\n"
                "b,UNRESOLVED,,\n"
                "c,CONTENT_RESOLVED,2023-13-01,2023-12-31\n"
                "d,CONTENT_RESOLVED,2025-01-01,2024-12-31\n", encoding="utf-8")
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
            p.write_text("id\nx\n", encoding="utf-8")
            self.assertIn("MISSING_TEMPORAL_COLUMNS", temporal_report(p)["errors"])
