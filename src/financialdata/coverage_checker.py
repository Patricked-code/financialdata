"""P1 issuer coverage report: read-only diagnostics, not PDF acquisition."""
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
