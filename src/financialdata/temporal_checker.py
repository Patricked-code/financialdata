"""Read-only P1 economic-period completeness: no filename inference."""
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
