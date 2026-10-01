#!/usr/bin/env python3
"""Validate versioned CollegePrep JSON seed files.

No network calls. This validates required provenance and prevents records from
being accidentally marked verified without a source and verification date.
"""

from __future__ import annotations
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

VALID_STATUSES = {
    "verified",
    "partially_verified",
    "unverified",
    "stale",
    "not_applicable",
}

REQUIRED_VERIFIED_FIELDS = {"source_url", "last_verified_at"}

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def iter_records(obj):
    if isinstance(obj, list):
        yield from obj
    elif isinstance(obj, dict):
        if "records" in obj and isinstance(obj["records"], list):
            yield from obj["records"]
        else:
            yield obj

def validate_record(path: Path, record: dict, index: int):
    errors = []
    status = record.get("verification_status")
    if status is not None and status not in VALID_STATUSES:
        errors.append(f"invalid verification_status={status!r}")

    if status == "verified":
        for field in REQUIRED_VERIFIED_FIELDS:
            if not record.get(field):
                errors.append(f"verified record missing {field}")

    if record.get("source_url") and not str(record["source_url"]).startswith("https://"):
        errors.append("source_url must use https://")

    if record.get("last_verified_at"):
        try:
            date.fromisoformat(str(record["last_verified_at"])[:10])
        except ValueError:
            errors.append("last_verified_at is not ISO-8601")

    return [f"{path.relative_to(ROOT)} record {index}: {e}" for e in errors]

def main() -> int:
    errors = []
    files = sorted(DATA.rglob("*.json")) if DATA.exists() else []
    for path in files:
        try:
            payload = load_json(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        for i, record in enumerate(iter_records(payload), start=1):
            if isinstance(record, dict):
                errors.extend(validate_record(path, record, i))

    if errors:
        print("\n".join(errors))
        return 1

    print(f"OK: validated {len(files)} JSON data files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
