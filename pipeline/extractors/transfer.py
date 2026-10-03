"""Transfer-credit and residence rules from policy sentences -> transfer_policies candidates.

Fields: `min_grade` (lowest transferable grade as printed), `max_transfer_credits` (cap on hours from
two-year or all institutions, with the scope kept in notes), `residency_requirement_credits` (hours
that must be earned at the institution). Every value cites its sentence. Several different values
for one field on a page are an exception (`conflicting_values:<field>`), never resolved here.
"""
from __future__ import annotations
import re

from . import common

EXTRACTOR = 'transfer_sentences/v1'
SENTENCE = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')
GRADE = re.compile(r'grades?\s+of\s+["“]?([A-D][+-]?)["”]?\s*(?:\(\d\.\d+\)\s*)?(?:or\s+(?:better|higher|above))', re.I)
MAX_HOURS = re.compile(r'(?:maximum\s+of|no\s+more\s+than|up\s+to|a\s+maximum\s+of)\s+(\d{2,3})\s+(?:semester\s+)?(?:credit\s+)?hours'
                       r'(?=.{0,120}(?:transfer|community|two-year|junior\s+college|2-year))', re.I)
# A grade rule for pass/fail courses or for one module/pathway (Rhodes, TN Tech r5) is not the general minimum.
SCOPED_GRADE = re.compile(r'pass\s*/\s*fail|pass-fail|\bP/F\b|satisfactory/unsatisfactory|\bmodule\b|transfer\s+pathway|\bTTP\b|core\s+block|\bmajor\b', re.I)
RESIDENCE = re.compile(r'(?:(?:last|final)\s+(\d{2})\s+(?:semester\s+)?(?:credit\s+)?hours'
                       r'|(?:at\s+least|minimum\s+of|a\s+minimum\s+of)\s+(\d{2})\s+(?:semester\s+)?(?:credit\s+)?hours'
                       r'(?=.{0,80}(?:in\s+residence|at\s+the\s+university|at\s+the\s+college|through\s+the\s+university|earned\s+at)))', re.I)


def extract(inst, entry, page, today_year):
    if common.professional_source(entry, page): return []
    head = (page.title + ' ' + ' '.join(page.headings[:8]) + ' ' + entry.get('url', '')).lower()
    if 'transfer' not in head and 'residen' not in head and 'graduation requirement' not in head:
        return []
    if re.search(r'scholarship|financial[- ]aid|reverse[- ]transfer', page.title + ' ' + entry.get('url', ''), re.I):
        return []  # hour counts there are award or reverse-transfer conditions (AL: Enterprise, Reid State, Jefferson State)
    text = re.sub(r'\s+', ' ', page.text)
    sentences = [s.strip() for s in SENTENCE.split(text) if 25 <= len(s.strip()) <= 500]
    found = {'min_grade': [], 'max_transfer_credits': [], 'residency_requirement_credits': []}
    for s in sentences:
        if re.search(r'graduate\s+(student|program|degree)|doctoral|master', s, re.I): continue
        if re.search(r'military|joint\s+services|\bACE\b|probation|admitted\s+to\s+[A-Z]{2,}|admission\s+to\s+[A-Z]{2,}', s): continue  # caps for one source or one partner
        if re.search(r'transfer', s, re.I):
            if not SCOPED_GRADE.search(s):
                for m in GRADE.finditer(s): found['min_grade'].append((m.group(1).upper(), s))
            for m in MAX_HOURS.finditer(s): found['max_transfer_credits'].append((int(m.group(1)), s))
        for m in ([] if re.search(r'attempted|probation|suspension|retain\s+this\s+status', s, re.I) else RESIDENCE.finditer(s)):
            v = int(m.group(1) or m.group(2))
            if 12 <= v <= 60: found['residency_requirement_credits'].append((v, s))
    if not any(found.values()): return []
    year, basis, issues = common.resolve_year(page, entry, today_year)
    rec, evidence, notes = {}, [], []
    for field, hits in found.items():
        if not hits: continue
        values = sorted({v for v, _ in hits}, key=str)
        if len(values) > 1:
            issues.append(f'conflicting_values:{field}')
            notes.append(f"{field}: page states {', '.join(map(str, values))}")
            continue
        rec[field] = values[0]
        for v, s in hits[:3]:
            evidence.append({'field': field, 'value': v, 'snippet': s[:400]})
    if not rec and not notes: return []
    rec['policy_url'] = common.source_of(entry)['url']
    rec['notes'] = ('Extracted by ' + EXTRACTOR + '; values copied from the cited sentences. ' + '; '.join(notes)).strip()
    if 'max_transfer_credits' in rec:
        rec['notes'] += ' The cap applies to the scope stated in its sentence (often two-year institutions only).'
    return [common.make('transfer_policies', inst['institution_key'], year, basis, rec, evidence, entry, EXTRACTOR,
                        {}, {'fields': sorted(k for k in rec if k not in {'policy_url', 'notes'})}, issues)]
