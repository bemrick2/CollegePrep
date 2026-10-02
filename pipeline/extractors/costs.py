"""Tuition / fees / cost-of-attendance tables -> costs candidates.

Reads labelled money rows from HTML tables and from layout-preserved PDF text. Columns are mapped
to residency and living arrangement from their printed headers. Printed totals are copied; the
sum of components is computed only as a check (`components_reconcile`) and never fills a missing
total. Anything that cannot be mapped unambiguously goes to the exception queue via `issues`.
"""
from __future__ import annotations
import re

from .. import text as T
from . import common

EXTRACTOR = 'cost_table/v1'

ROW_LABELS = [  # (component key, pattern) — first match wins
    ('total', r'^(estimated\s+)?(total|grand total)\b|total\s+(cost|coa|estimated|budget|direct)|cost of attendance\s*$'),
    ('tuition_and_fees', r'tuition\s*(&|and|/)\s*(mandatory\s+|required\s+)?fees|enrollment fees|maintenance\s*(&|and)\s*(program\s+services\s+)?fees'),
    ('food_housing', r'(room|housing)\s*(&|and|/)\s*(board|food|meals)|(food|board|meals)\s*(&|and|/)\s*(housing|room)'),
    ('tuition', r'^(\w+\s+)?tuition\b'),
    ('mandatory_fees', r'^(required|mandatory|student|general|program\s+services?|activity|technology)?\s*fees?\b'),
    ('housing', r'^(on[- ]campus\s+|off[- ]campus\s+)?(housing|room|rent|lodging)\b'),
    ('food', r'^(food|meals?|meal plan|board|dining)\b'),
    ('books_supplies', r'books|supplies|course materials'),
    ('transportation', r'transportation|travel'),
    ('personal', r'personal|miscellaneous|misc\b|living expenses'),
    ('loan_fees', r'loan\s*fees?'),
]
_ROW = [(k, re.compile(p, re.I)) for k, p in ROW_LABELS]


def row_key(label):
    s = re.sub(r'[*†‡:]+', ' ', label or '').strip()
    if not s or len(s) > 80: return None
    for k, rx in _ROW:
        if rx.search(s): return k
    return None


def column_meaning(header):
    h = (header or '').lower()
    residency = ('out_of_state' if re.search(r'out[- ]of[- ]state|non-?\s?resident', h) else
                 'in_state' if re.search(r'in[- ]state|resident|tennessee', h) else None)
    arrangement = ('with_parents_or_family' if re.search(r'with\s*(parent|family)|at home|commut', h) else
                   'off_campus_not_with_family' if re.search(r'off[- ]campus', h) else
                   'on_campus' if re.search(r'on[- ]campus|residence hall|in a dorm', h) else None)
    return residency, arrangement


def _grid_from_table(rows):
    """(column headers, [(label, [cell values...]), ...]) for tables of label + money columns."""
    if len(rows) < 3: return None
    header = rows[0]
    body = []
    for r in rows[1:]:
        if not r: continue
        vals = [T.plain_number(c) for c in r[1:]]
        if any(v is not None for v in vals): body.append((r[0], vals, ' | '.join(r)))
    return header[1:], body


def _grid_from_text(lines):
    """Same shape from layout text: '<label>   $1,234   $5,678' lines under a header line."""
    body, header = [], None
    for i, line in enumerate(lines):
        money = T.money_values(line)
        label = re.split(r'\$', line, 1)[0].strip()
        if money and row_key(label):
            body.append((label, money, line.strip()))
        elif not body and len(re.findall(r'in[- ]state|out[- ]of[- ]state|on[- ]campus|off[- ]campus|with\s+parent|resident', line, re.I)) >= 2:
            header = [c for c in re.split(r'\s{2,}', line.strip()) if c]
    if len(body) < 3: return None
    return header or [], body


def _records(grid, inst, entry, page, today_year, source_text):
    headers, body = grid
    ncols = max(len(v) for _, v, _ in body)
    if ncols == 0: return []
    keys = [(row_key(label), label, vals, raw) for label, vals, raw in body]
    keys = [k for k in keys if k[0]]
    found = {k for k, *_ in keys}
    if not (found & {'tuition', 'tuition_and_fees'}) or len(found) < 2:
        return []
    issues = []
    cols = []
    for j in range(ncols):
        h = headers[j] if j < len(headers) else ''
        cols.append(column_meaning(h) + (h,))
    if headers and len(headers) != ncols:
        issues.append('column_alignment_uncertain')
    page_res, _ = column_meaning(page.title + ' ' + ' '.join(page.headings[:5]))
    is_private = inst.get('control') == 'private_nonprofit'
    year, basis, yissues = common.resolve_year(page, entry, today_year)
    issues += yissues
    low = source_text.lower()
    if 'per semester' in low and not re.search(r'academic year|annual|per year|two semesters|fall\s*(and|&)\s*spring', low):
        issues.append('cost_period_semester')
    # Group columns by residency; each residency gets one record, arrangements become living_arrangements.
    groups = {}
    for j, (res, arr, h) in enumerate(cols):
        res = res or page_res or ('not_applicable' if is_private else None)
        if res is None:
            issues.append('residency_unknown'); res = 'unknown'
        groups.setdefault(res, []).append((j, arr, h))
    out = []
    for res, jcols in groups.items():
        if res == 'unknown' and len(groups) > 1: continue
        arrangements, evidence = [], []
        for j, arr, h in jcols:
            comp = {}
            for key, label, vals, raw in keys:
                if j < len(vals) and vals[j] is not None:
                    comp.setdefault(key, vals[j])
                    evidence.append({'field': f'{arr or "column"}:{key}', 'value': vals[j], 'snippet': raw[:240]})
            if comp: arrangements.append((arr, h, comp))
        if not arrangements: continue
        primary = next((a for a in arrangements if a[0] == 'on_campus'), arrangements[0])
        comp = primary[2]
        parts = [v for k, v in comp.items() if k not in {'total'}]
        checks = {'columns': len(arrangements), 'components': sorted(comp)}
        if 'total' in comp:
            checks['components_reconcile'] = abs(sum(parts) - comp['total']) < 1
        record = {'residency': 'not_applicable' if res == 'unknown' else res, 'currency': 'USD',
                  'cost_period': 'semester' if 'cost_period_semester' in issues else 'academic_year',
                  'tuition': comp.get('tuition'), 'mandatory_fees': comp.get('mandatory_fees'),
                  'books_supplies': comp.get('books_supplies'),
                  'on_campus_food_housing': comp.get('food_housing') if primary[0] == 'on_campus' else None,
                  'total_cost_of_attendance': comp.get('total'),
                  'components': {k: v for k, v in comp.items() if k != 'total'},
                  'notes': f'Extracted by {EXTRACTOR}; printed values copied, totals never recomputed.'}
        if re.search(r'undergraduate', low): record['student_population'] = 'undergraduate'
        if len(arrangements) > 1:
            record['living_arrangements'] = [{'arrangement': a or 'unlabeled', 'column_header': h,
                                              'total_cost_of_attendance': c.get('total'),
                                              **{k: v for k, v in c.items() if k != 'total'}} for a, h, c in arrangements]
            if any(a is None for a, _, _ in arrangements): issues.append('arrangement_unlabeled')
        if checks.get('components_reconcile') is False: issues.append('components_do_not_reconcile')
        out.append(common.make('costs', inst['institution_key'], year, basis, record, evidence, entry,
                               EXTRACTOR, {'residency': record['residency']}, checks, sorted(set(issues))))
    return out


def extract(inst, entry, page, today_year):
    out = []
    for t in page.tables:
        grid = _grid_from_table(t['rows'])
        if grid: out += _records(grid, inst, entry, page, today_year, ' '.join(' '.join(r) for r in t['rows']) + ' ' + page.text[:3000])
    if not out and entry.get('kind') == 'pdf':
        grid = _grid_from_text(page.lines)
        if grid: out += _records(grid, inst, entry, page, today_year, page.text[:20000])
    # One record per residency and year per page: keep the richest table.
    best = {}
    for c in out:
        k = (c['record']['residency'], c['academic_year'])
        if k not in best or len(c['evidence']) > len(best[k]['evidence']): best[k] = c
    return list(best.values())
