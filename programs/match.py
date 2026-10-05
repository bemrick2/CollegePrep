"""Exact matching between a catalog program record and an official program inventory row (THEC).

A match needs the same major name and the same award after normalisation (case, punctuation and spacing only):
'Mechanical Engineering, B.S.M.E.' = 'MECHANICAL ENGINEERING' + 'BSME'; a concentration printed after a colon
('Computer Science: Cyber Security, B.S.') belongs to its major ('COMPUTER SCIENCE' + 'BS'). Anything else stays
unmatched: no similarity scores, no synonyms, and an ambiguous match (two rows) is not used.
"""
from __future__ import annotations
import json, re


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def award(s):
    return re.sub(r'[^A-Z]', '', (s or '').upper())


def split_catalog_name(name):
    """('Computer Science', 'BS') from 'Computer Science: Cyber Security, B.S.' or 'Computer Science (B.S.)'; None when
    no award is printed."""
    m = re.match(r'^(.*?),\s*([A-Za-z.]{2,12})\s*(\(.*\))?$', name.strip()) or \
        re.match(r'^(.*?)\s*\(([A-Za-z.]{2,12})\)\s*$', name.strip())  # 'Accounting (B.B.A.)' (Austin Peay)
    if not m: return None
    major = m.group(1).split(':')[0]
    return norm(major), award(m.group(2))


def match(records, rows):
    """records: catalog program records; rows: THEC inventory rows for the same institution.
    Returns {program_key: row} for unique exact matches."""
    index = {}
    for r in rows:
        index.setdefault((norm(r.get('MajorName')), award(r.get('Award'))), []).append(r)
    out = {}
    for rec in records:
        key = split_catalog_name(rec.get('program_name', ''))
        hits = index.get(key) if key else None
        if hits and len(hits) == 1: out[rec['program_key']] = hits[0]
    return out


def excerpt(row):
    return json.dumps({k: row.get(k) for k in ('InstitutionName', 'MajorName', 'Award', 'MajorTaxCode', 'MajorCipCode')}, ensure_ascii=False)
