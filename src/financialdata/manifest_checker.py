"""Read-only audit of SOURCE CSV metadata, preserving source facts."""
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
