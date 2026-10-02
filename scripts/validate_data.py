#!/usr/bin/env python3
"""Validate versioned CollegePrep JSON seed files.

No network calls. This validates required provenance and prevents records from
being accidentally marked verified without a source and verification date.
"""

from __future__ import annotations
import json
import sys
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend.catalog import records
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
    if status not in VALID_STATUSES:
        errors.append(f"invalid verification_status={status!r}")

    if status == "verified":
        for field in REQUIRED_VERIFIED_FIELDS:
            if not record.get(field):
                errors.append(f"verified record missing {field}")

    if record.get("source_url") and not str(record["source_url"]).startswith("https://"):
        errors.append("source_url must use https://")

    if record.get("last_verified_at"):
        try:
            value = str(record['last_verified_at'])
            if not re.match(r'^\d{4}-\d{2}-\d{2}(?:T|$)', value): raise ValueError()
            if date.fromisoformat(value[:10]) > date.today(): raise ValueError()
        except (ValueError, TypeError):
            errors.append("last_verified_at is not ISO-8601")

    return [f"{path.relative_to(ROOT)} record {index}: {e}" for e in errors]

def main() -> int:
    errors = []
    total = 0
    seen = set()
    try:
        for path, domain, record in records():
            total += 1
            errors.extend(validate_record(path, record, total))
            if domain != 'institutions' and not record.get('academic_year'):
                errors.append(f'{path}: missing academic_year')
            key=(domain,record.get('institution_key'),record.get('state'),record.get('academic_year'),record.get('record_key') or record.get('program_name') or record.get('award_name') or record.get('policy_kind') or record.get('appeal_kind') or record.get('residency'))
            if key in seen: errors.append(f'{path}: duplicate natural key {key}')
            seen.add(key)
            if record.get('qualifies_for_paid_addon') and (not record.get('qualifying_path_evidence') or record.get('offered') is not True or record.get('appeal_kind') not in {'merit_reconsideration','competing_offer_review','financial_aid_appeal'}):
                errors.append(f'{path}: missing qualifying appeal evidence')
    except (ValueError, TypeError, KeyError) as exc:
        errors.append(str(exc))

    if errors:
        print("\n".join(errors))
        return 1

    print(f"OK: validated {total} records")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
