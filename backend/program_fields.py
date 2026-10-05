"""CR-14 program-depth field rules shared by scripts/validate_data.py and tests.

Mirrors the check constraints of supabase/migrations/20261005150000_program_depth_cr14.sql and adds the
repository-only guarantees the database cannot see across batches:

* A field-level fact (admission_type, internal_transfer, undeclared_policy, cip_code) carries its own
  verbatim quote and official https source; a CIP code also needs its source.
* `program_catalogs.programs_complete = true` needs `listed_program_keys`, one per bachelor program on the
  official list, and every one of them must have a verified academic_programs record for the same
  institution and year. Only then may the product say a school does not offer a program.
"""
from __future__ import annotations
import re

ADMISSION_TYPES = frozenset({'direct', 'pre_major', 'open'})
CIP = re.compile(r'^\d{2}\.\d{4}$')
CIP_PREFIX = re.compile(r'^\d{2}(\.\d{2}(\d{2})?)?$')


def _evidence_errors(obj, name, need_bool=None):
    errs = []
    if not isinstance(obj, dict): return [f'{name} must be an object']
    if need_bool and not isinstance(obj.get(need_bool), bool): errs.append(f'{name}.{need_bool} must be boolean')
    if not isinstance(obj.get('quote'), str) or not obj['quote'].strip(): errs.append(f'{name}.quote (verbatim official text) is required')
    if not str(obj.get('source_url', '')).startswith('https://'): errs.append(f'{name}.source_url must be an official https URL')
    g = obj.get('gpa_min')
    if g is not None and (isinstance(g, bool) or not isinstance(g, (int, float)) or not 0 < g <= 5): errs.append(f'{name}.gpa_min invalid')
    return errs


def field_errors(domain, r):
    errs = []
    if domain == 'academic_programs':
        if r.get('cip_code') is not None:
            if not isinstance(r['cip_code'], str) or not CIP.match(r['cip_code']): errs.append('cip_code must be NN.NNNN')
            if not str(r.get('cip_source_url', '')).startswith('https://'): errs.append('cip_code needs cip_source_url (official https)')
        if r.get('admission_type') is not None:
            if r['admission_type'] not in ADMISSION_TYPES: errs.append('invalid admission_type')
            errs += _evidence_errors(r.get('admission_details'), 'admission_details')
        elif r.get('admission_details') is not None:
            errs.append('admission_details without admission_type')
        if r.get('internal_transfer') is not None:
            errs += _evidence_errors(r['internal_transfer'], 'internal_transfer', need_bool='restricted')
    elif domain == 'program_catalogs':
        for f in ('institution_key', 'academic_year', 'catalog_url', 'source_url'):
            if not isinstance(r.get(f), str) or not r[f].strip(): errs.append('missing ' + f)
        if r.get('catalog_url') and not str(r['catalog_url']).startswith('https://'): errs.append('catalog_url must use https://')
        n = r.get('listed_bachelor_programs')
        if n is not None and (isinstance(n, bool) or not isinstance(n, int) or n < 0): errs.append('invalid listed_bachelor_programs')
        pc = r.get('programs_complete')
        if pc is not None and not isinstance(pc, bool): errs.append('programs_complete must be boolean or null')
        if pc is True:
            keys = r.get('listed_program_keys')
            if not isinstance(n, int) or not (r.get('completeness_basis') or '').strip():
                errs.append('programs_complete needs listed_bachelor_programs and completeness_basis')
            if not isinstance(keys, list) or len(keys) != n or len(set(keys)) != len(keys):
                errs.append('programs_complete needs listed_program_keys: one distinct key per listed bachelor program')
        if r.get('undeclared_policy') is not None:
            errs += _evidence_errors(r['undeclared_policy'], 'undeclared_policy', need_bool='allowed')
    elif domain == 'awards':
        for f in ('program_keys', 'cip_codes'):
            v = r.get(f)
            if v is None: continue
            if not isinstance(v, list) or not v or not all(isinstance(x, str) and x.strip() for x in v): errs.append(f'{f} must be a nonempty list of strings')
            elif f == 'cip_codes' and not all(CIP_PREFIX.match(x) for x in v): errs.append('cip_codes must be NN, NN.NN or NN.NNNN')
        if (r.get('program_keys') or r.get('cip_codes')) and not (r.get('major_requirement') or '').strip():
            errs.append('a program-linked award needs major_requirement quoting the institution\'s stated field')
    return errs


def cross_errors(rows):
    """rows: iterable of (path, domain, record). Completeness and award links must point at verified programs."""
    verified = {(r.get('institution_key'), r.get('academic_year'), r.get('program_key'))
                for _, d, r in rows if d == 'academic_programs' and r.get('verification_status') == 'verified'}
    anyprog = {(r.get('institution_key'), r.get('academic_year'), r.get('program_key')) for _, d, r in rows if d == 'academic_programs'}
    errs = []
    # One program, one record: a state-inventory record (THEC) must not sit beside a catalog record for the same major
    # and award (programs/promote.py folds them together).
    import re
    def key(r):
        m = re.match(r'^(.*?),\s*([A-Za-z.]{2,12})\s*(\(.*\))?$', (r.get('program_name') or '').strip())
        return (re.sub(r'[^a-z0-9]+', ' ', m.group(1).split(':')[0].lower()).strip(), re.sub(r'[^A-Z]', '', m.group(2).upper())) if m else None
    inv, cat = {}, {}
    for path, d, r in rows:
        if d != 'academic_programs' or key(r) is None: continue
        bucket = inv if str(r.get('program_url', '')).startswith('https://thec.ppr.tn.gov/') else cat
        bucket.setdefault((r.get('institution_key'), r.get('academic_year'), key(r)), []).append((path, r.get('program_key')))
    for k, items in inv.items():
        if k in cat:
            errs.append(f'{items[0][0]}: inventory record {items[0][1]!r} duplicates catalog record {cat[k][0][1]!r}')
    for path, d, r in rows:
        if d == 'program_catalogs' and r.get('programs_complete') is True:
            missing = [k for k in r.get('listed_program_keys') or [] if (r['institution_key'], r['academic_year'], k) not in verified]
            if missing: errs.append(f'{path}: programs_complete but {len(missing)} listed programs lack a verified record: {missing[:5]}')
        if d == 'awards':
            for k in r.get('program_keys') or []:
                if (r.get('institution_key'), r.get('academic_year'), k) not in anyprog:
                    errs.append(f'{path}: award {r.get("award_name")!r} links unknown program_key {k!r}')
    return errs
