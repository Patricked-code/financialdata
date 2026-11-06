"""Structural SHA registry checker; never deletes a source row."""
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
