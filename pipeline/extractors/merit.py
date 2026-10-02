"""Merit scholarship tables -> awards candidates.

Two published shapes are recognised:
  list: one row per scholarship (name, amount, GPA / ACT / SAT thresholds as printed)
  grid: GPA ranges down the side, test-score ranges across the top, award amounts in the cells
Every cell is copied as printed. Numeric minimums (`thresholds`) are added only when a cell is one
clean number on the right scale; ranges, "or", footnotes and anything else stay text only. Nothing
about automatic consideration, renewal or stacking is inferred.
"""
from __future__ import annotations
import re

from .. import text as T
from . import common

EXTRACTOR = 'merit_table/v1'
SCHOLARSHIP_CONTEXT = re.compile(r'scholarship|merit|award', re.I)
NOT_MERIT = re.compile(r'need[- ]based|federal|pell|loan|work[- ]study|graduate|transfer|athletic|tuition|fees?\b|cost', re.I)
NOT_NAME = re.compile(r'^[\d<>=.\s/+%$,-]*$|tuition|\bfees?\b|per credit|per course|deposit|housing|meal|eligib|'
                      r'\bstudents?\s+(is|who|still|are)\b|fall below|balance', re.I)
# Names that are not merit awards (KY: federal aid and loans in an aid table, staff directories, credit-hour bands
# from an academic-standards table).
NOT_AWARD_NAME = re.compile(r'\bpell\b|supplemental\s+educational\s+opportunity|\bseog\b|work[- ]study|\bloans?\b|\bplus\b|'
                            r'college\s+access\s+program|counselor|director|coordinator|specialist|\bassistant\b|officer|advisor|'
                            r'^(fewer|more|less)\s+than\b|^over\s+\d|\bcredit\s+hours?\b', re.I)
NOT_MERIT_PAGE = re.compile(r'academic[- ]standards|probation|satisfactory[- ]academic[- ]progress|financial[- ]aid[- ]staff|'
                            r'\bstaff\b|directory|meet[- ]the[- ]team|our[- ]team', re.I)
HEADER_WORDS = re.compile(r'scholarship|award|merit|name|level|tier|amount|value|gpa|act\b|sat\b|criteria|requirement', re.I)
THRESHOLD_CELL = re.compile(r'^\s*[<>≤≥]?\s*\d{1,4}(\.\d{1,2})?\s*(\+|-\s*\d{1,4}(\.\d{1,2})?|or\s+(higher|above))?\s*$', re.I)


def _col(header, *words):
    for i, h in enumerate(header):
        if any(w in h.lower() for w in words): return i
    return None


def _num(cell, lo, hi, decimals=False):
    m = re.fullmatch(r'\s*(?:minimum\s+|min\.?\s+)?(\d{1,4}(?:\.\d{1,2})?)\s*(\+|or\s+(higher|above|better)|and\s+above)?\s*\**\s*', cell or '', re.I)
    if not m: return None
    v = float(m.group(1)) if decimals else (int(m.group(1)) if '.' not in m.group(1) else None)
    return v if v is not None and lo <= v <= hi else None


def _amounts(cell):
    vals = T.money_values(cell or '')
    return (min(vals), max(vals)) if vals else (None, None)


def _list_awards(t, header, body, title, award_type):
    name = _col(header, 'scholarship', 'award', 'name', 'program')
    amount = _col(header, 'amount', 'value', 'award amount', 'annual', 'per year', '$')
    gpa = _col(header, 'gpa', 'grade point')
    act = _col(header, 'act')
    sat = _col(header, 'sat')
    if name is None: name = 0
    if amount is None and gpa is None and act is None and sat is None: return []
    out = []
    for row in body:
        cells = list(row) + [''] * (len(header) - len(row))
        nm = cells[name].strip()
        if not nm or len(nm) > 120 or T.money_values(nm) or NOT_NAME.search(nm) or NOT_AWARD_NAME.search(nm): continue
        if nm.endswith(':') or len(nm.split()) > 12: continue  # worked examples and sentences, not award names
        get = lambda i: cells[i].strip() if i is not None and i < len(cells) else ''
        amt, g, a, s = get(amount), get(gpa), get(act), get(sat)
        if not (amt or g or a or s): continue
        lo, hi = _amounts(amt)
        tier_row = bool(re.search(r'\d.*\b(gpa|act|sat)\b', nm, re.I))
        rec = {'award_name': f"{title}: {nm}" if tier_row else nm, 'award_type': award_type}
        if tier_row:  # the row label is itself the threshold ('3.6+ GPA, 26-27 ACT')
            rec['test_requirement' if re.search(r'\b(act|sat)\b', nm, re.I) else 'gpa_requirement'] = nm
        if amt: rec['award_amount_text'] = amt
        if lo is not None:
            rec['award_min'], rec['award_max'] = lo, hi
        if g: rec['gpa_requirement'] = g
        tests = ' / '.join(x for x in [f'ACT {a}' if a else '', f'SAT {s}' if s else ''] if x)
        if tests: rec['test_requirement'] = tests
        thresholds = {k: v for k, v in {'gpa_min': _num(g, 0, 5, True), 'act_min': _num(a, 1, 36), 'sat_min': _num(s, 400, 1600)}.items() if v is not None}
        if thresholds: rec['thresholds'] = thresholds
        out.append((rec, ' | '.join(cells)))
    return out


def _tier_award(t, header, body, context):
    """One threshold column and one amount column: 'GPA | Merit', '3.0 | $14,000'."""
    if len(header) != 2 or not re.search(r'gpa|act|sat|score', header[0], re.I): return []
    rows = [r for r in body if len(r) >= 2 and THRESHOLD_CELL.match(r[0]) and T.money_values(r[1])]
    if len(rows) < 3 or len(rows) < len(body) - 1: return []
    tiers = [{header[0].strip().lower() or 'threshold': r[0], 'amount_text': r[1]} for r in rows]
    amounts = [v for r in rows for v in T.money_values(r[1])]
    title = (t.get('heading') or t.get('caption') or 'Merit scholarship tiers').strip()
    rec = {'award_name': title[:120], 'award_type': 'institutional_merit', 'award_tiers': tiers,
           'award_min': min(amounts), 'award_max': max(amounts)}
    rec['gpa_requirement' if re.search('gpa', header[0], re.I) else 'test_requirement'] = \
        f"Tiered by {header[0].strip()}: " + '; '.join(f"{r[0]} → {r[1]}" for r in rows)
    return [(rec, ' || '.join(' | '.join(r) for r in [header] + rows))]


def _grid_award(t, header, body, context):
    """GPA x test-score matrix: header cells are score ranges, first column GPA ranges, cells amounts."""
    score_cols = [i for i, h in enumerate(header) if i > 0 and re.search(r'\d{2}', h)]
    if len(score_cols) < 2: return []
    gpa_rows = [r for r in body if r and re.search(r'\d\.\d', r[0])]
    if len(gpa_rows) < 2: return []
    tiers, evidence_rows = [], []
    for r in gpa_rows:
        for i in score_cols:
            if i < len(r) and T.money_values(r[i]):
                tiers.append({'gpa': r[0], 'test': header[i], 'amount_text': r[i]})
        evidence_rows.append(' | '.join(r))
    if len(tiers) < 3: return []
    amounts = [v for tier in tiers for v in T.money_values(tier['amount_text'])]
    title = (t.get('heading') or t.get('caption') or 'Merit scholarship grid').strip()
    rec = {'award_name': title[:120], 'award_type': 'institutional_merit', 'award_tiers': tiers,
           'test_requirement': f"Tiers by {header[0] or 'GPA'} and {', '.join(header[i] for i in score_cols[:2])}…",
           'award_min': min(amounts), 'award_max': max(amounts)}
    return [(rec, ' || '.join([' | '.join(header)] + evidence_rows))]


def extract(inst, entry, page, today_year):
    if not page.tables or common.professional_source(entry, page): return []
    if not SCHOLARSHIP_CONTEXT.search(page.title + ' ' + ' '.join(page.headings[:6]) + ' ' + entry.get('url', '')):
        return []
    if NOT_MERIT_PAGE.search(page.title + ' ' + entry.get('url', '')): return []
    if re.search(r'transfer', entry.get('url', '') + ' ' + page.title, re.I):
        return []  # first-year merit only; transfer awards are a separate category
    year, basis, issues = common.resolve_year(page, entry, today_year)
    out = []
    for t in page.tables:
        rows = [r for r in t['rows'] if any(c.strip() for c in r)]
        if len(rows) < 3: continue
        context = ' '.join([t.get('heading') or '', t.get('caption') or ''])
        if NOT_MERIT.search(context): continue
        header, body = rows[0], rows[1:]
        if NOT_MERIT.search(' '.join(header)) or NOT_NAME.search(context): continue
        if not HEADER_WORDS.search(' '.join(header)): continue  # e.g. worked aid examples, schedules
        shaped = _tier_award(t, header, body, context) or _grid_award(t, header, body, context)
        merit_context = re.search(r'merit|academic|gpa|act|sat|test score', context + ' ' + ' '.join(header) + ' ' + page.title, re.I)
        award_type = 'institutional_merit' if merit_context else 'institutional_other'
        found = shaped or _list_awards(t, header, body, (context or page.title).strip()[:80], award_type)
        if not found or (not shaped and len(found) < 2): continue  # one stray row is not a scholarship table
        t_year = T.year_labels(context)
        rec_year, rec_basis, rec_issues = (year, basis, issues)
        if len(t_year) == 1:
            rec_year, rec_basis = next(iter(t_year)), 'labeled_in_source'
            rec_issues = [i for i in issues if i != 'ambiguous_year_labels' and not i.startswith('stale_year_label')]
            if rec_year < today_year: rec_issues.append(f'stale_year_label:{rec_year}')
        for rec, raw in found:
            ev = [{'field': k, 'value': v, 'snippet': raw[:300]} for k, v in rec.items()
                  if k in {'award_amount_text', 'gpa_requirement', 'test_requirement', 'award_tiers'}]
            if not ev: continue
            rec['notes'] = f'Extracted by {EXTRACTOR} from the table "{(context or page.title)[:100]}"; cells copied as printed.'
            out.append(common.make('awards', inst['institution_key'], rec_year, rec_basis, rec, ev, entry, EXTRACTOR,
                                   {'award_name': rec['award_name']}, {'thresholds': rec.get('thresholds')}, rec_issues))
    return out
