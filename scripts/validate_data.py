#!/usr/bin/env python3
"""Validate versioned CollegePrep JSON seed files.

No network calls. This validates required provenance and prevents records from
being accidentally marked verified without a source and verification date.
"""

from __future__ import annotations
import json
import sys
import re
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend.catalog import records, import_contract_errors, CONTROLLED_VALUES
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

GROUP_TYPES={'all_required','choose_courses','choose_credits','elective_pool','credit_total','gpa_rule','grade_rule','residency_rule','sequence'}
GROUP_CATEGORIES={'general_education','major_core','major_elective','concentration','supporting_coursework','free_elective',
    'university_requirement','program_total','recommended_sequence','minor','other'}

def course_item_errors(item, where):
    if isinstance(item,dict) and 'any_of' in item:
        if not isinstance(item['any_of'],list) or len(item['any_of'])<2:
            return [f'{where}: any_of needs at least two options']
        return [e for option in item['any_of'] for e in course_item_errors(option, where)]
    if not isinstance(item,dict) or not isinstance(item.get('code'),str) or not item['code'].strip():
        return [f'{where}: course items need a code (or any_of)']
    credits=item.get('credits')
    if credits is not None and (isinstance(credits,bool) or not isinstance(credits,(int,float,str))):
        return [f'{where}: credits must be a number or printed range']
    return []

def requirement_group_errors(record):
    """Enforce docs/PROGRAM_DATA.md requirement_group/v1 on rule_details."""
    rd=record['rule_details']; errors=[]
    if rd.get('schema')!='requirement_group/v1':
        return ['rule_details.schema must be requirement_group/v1']
    year=str(record.get('academic_year',''))
    printed=str(rd.get('catalog_year') or '')
    m=re.match(r'^(\d{4})-(\d{2}|\d{4})$',year); n=re.match(r'^(\d{4})\s*[-–]\s*(\d{2}|\d{4})$',printed)
    if not n: errors.append('rule_details.catalog_year must be an explicit year range')
    elif m and (n.group(1)!=m.group(1) or n.group(2)[-2:]!=m.group(2)[-2:]): errors.append('rule_details.catalog_year does not match academic_year')
    gt,cat=rd.get('group_type'),rd.get('category')
    if gt not in GROUP_TYPES: errors.append('invalid rule_details.group_type')
    if cat not in GROUP_CATEGORIES: errors.append('invalid rule_details.category')
    if (gt=='sequence')!=(record.get('requirement_kind')=='program_plan'):
        errors.append('group_type sequence and requirement_kind program_plan go together')
    if gt=='choose_courses' and not (isinstance(rd.get('choose_count'),int) and rd['choose_count']>0):
        errors.append('choose_courses needs a positive integer choose_count')
    if gt=='choose_credits' and not (isinstance(rd.get('choose_credits'),(int,float)) and not isinstance(rd.get('choose_credits'),bool) and rd['choose_credits']>0):
        errors.append('choose_credits needs a positive choose_credits')
    if cat=='concentration' and not rd.get('concentration'): errors.append('concentration groups need a concentration name')
    if gt=='sequence':
        terms=rd.get('terms')
        if not isinstance(terms,list) or not terms: errors.append('sequence groups need terms')
        else:
            for t in terms:
                if not isinstance(t,dict) or not isinstance(t.get('term_index'),int) or not isinstance(t.get('items'),list):
                    errors.append('each term needs term_index and items'); break
    if 'courses' in rd:
        if not isinstance(rd['courses'],list): errors.append('rule_details.courses must be a list')
        else:
            for item in rd['courses']: errors.extend(course_item_errors(item,'rule_details.courses'))
    if 'course_rules' in rd and not (isinstance(rd['course_rules'],list) and all(isinstance(x,str) for x in rd['course_rules'])):
        errors.append('rule_details.course_rules must be a list of strings')
    if gt in {'all_required','choose_courses'} and not rd.get('courses'):
        errors.append(f'{gt} groups need courses')
    if gt=='elective_pool' and not (rd.get('course_rules') or rd.get('courses')):
        errors.append('elective_pool groups need course_rules or courses')
    return errors

def validate_record(path: Path, record: dict, index: int, domain=None):
    errors = []
    status = record.get("verification_status")
    if status not in VALID_STATUSES:
        errors.append(f"invalid verification_status={status!r}")
    if status=='verified' and 'source_unlabeled' in record.get('academic_year_basis',''):
        errors.append('unlabeled academic-year evidence cannot be marked verified')

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
            if date.fromisoformat(value[:10]) > datetime.now(timezone.utc).date(): raise ValueError()  # UTC, as fetch dates are
        except (ValueError, TypeError):
            errors.append("last_verified_at is not ISO-8601")

    if domain in {'academic_programs','degree_requirements','transfer_policies'}:
        required=['institution_key','academic_year','source_url','last_verified_at']
        if domain=='academic_programs': required+=['program_key','program_name']
        if domain=='degree_requirements': required+=['program_key','requirement_key','requirement_kind']
        for field in required:
            if not isinstance(record.get(field),str) or not record[field].strip():
                errors.append('missing '+field)
        if domain=='degree_requirements':
            if record.get('requirement_kind') not in CONTROLLED_VALUES['degree_requirements']['requirement_kind']:
                errors.append('invalid requirement_kind')
            if not isinstance(record.get('rule_details'),dict):
                errors.append('rule_details must be an object')
            else:
                errors.extend(requirement_group_errors(record))
        for field in ['total_credits','minimum_credits','minimum_gpa','max_transfer_credits','max_transfer_percent','residency_requirement_credits']:
            value=record.get(field)
            if value is not None and (isinstance(value,bool) or not isinstance(value,(int,float)) or value<0 or (field=='max_transfer_percent' and value>100)):
                errors.append('invalid '+field)
        if 'active' in record and record['active'] is not None and not isinstance(record['active'],bool):
            errors.append('active must be boolean or null')
    try: label=path.relative_to(ROOT)
    except ValueError: label=path
    return [f"{label} record {index}: {e}" for e in errors]

def main() -> int:
    errors = []
    total = 0
    seen = set()
    programs, requirements = set(), []
    try:
        for path, domain, record in records():
            total += 1
            # A requirement row needs its program for the same institution and year (the importer refuses
            # orphans: "Missing program dependency", VA r1 VSU).
            if domain == 'academic_programs': programs.add((record.get('institution_key'), record.get('academic_year'), record.get('program_key')))
            if domain == 'degree_requirements': requirements.append((path, (record.get('institution_key'), record.get('academic_year'), record.get('program_key'))))
            errors.extend(validate_record(path, record, total, domain=domain))
            if domain != 'institutions' and not record.get('academic_year'):
                errors.append(f'{path}: missing academic_year')
            from backend.store import natural_key
            key=natural_key(domain,record)
            if key in seen: errors.append(f'{path}: duplicate natural key {key}')
            seen.add(key)
            # Data that passes validation must also be loadable by the Supabase importer.
            errors.extend(f'{path}: {e}' for e in import_contract_errors(domain, record))
            if record.get('qualifies_for_paid_addon') and (not record.get('qualifying_path_evidence') or record.get('offered') is not True or record.get('appeal_kind') not in {'merit_reconsideration','competing_offer_review','financial_aid_appeal'}):
                errors.append(f'{path}: missing qualifying appeal evidence')
    except (ValueError, TypeError, KeyError) as exc:
        errors.append(str(exc))
    errors.extend(f'{path}: degree requirement without its program {key[2]!r} for {key[1]}' for path, key in requirements if key not in programs)

    if errors:
        print("\n".join(errors))
        return 1

    print(f"OK: validated {total} records")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
