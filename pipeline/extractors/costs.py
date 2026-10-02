"""Tuition / fees / cost-of-attendance tables -> costs candidates (v2).

Built from real Tennessee pages, checked against Kentucky, Oregon and Nevada. A table is read as:
  title rows (one cell: "2026-2027 Cost of Attendance", "Tennessee Residents") -> table context
  header row (column meanings: per semester / per year, academic year, residency, living arrangement)
  body rows  (printed label + money per column)
Rules:
- Every printed row is kept verbatim in `components` (label -> value); canonical fields are filled
  only from an unambiguous row. Totals are copied; component sums only check `components_reconcile`.
- Per-year columns win over per-semester columns; a semester-only table is recorded as such
  (`cost_period: semester`) and flagged, never doubled.
- Each academic year printed on the page becomes its own candidate (prior years are history).
- Graduate, professional, online and per-credit tables are skipped.
- PDFs are read only when the document presents itself as a cost/tuition document.
"""
from __future__ import annotations
import re

from .. import text as T
from . import common

EXTRACTOR = 'cost_table/v2'

ROW_LABELS = [  # first match wins
    ('total', r'^\W*(estimated\s+)?(grand\s+)?total\b|total\s+(cost|coa|estimated|budget|direct)|^cost of attendance\s*$'),
    ('tuition_and_fees', r'tuition\s*(&|and|/|\+)\s*(mandatory\s+|required\s+|general\s+)?fees|enrollment fees|maintenance\s*(&|and)\s*(program\s+services\s+)?fees'),
    ('food_housing', r'(room|housing|lodging|residence\s+hall)\s*(&|and|/|\+)\s*(board|food|meals?|meal\s+plan)|(food|board|meals?)\s*(&|and|/|\+)\s*(housing|room|lodging)|living expenses'),
    ('tuition', r'^\W*(\w+\s+)?tuition\b'),
    ('housing', r'^\W*(on[- ]campus\s+|off[- ]campus\s+|basic\s+)?(housing|room|rent|lodging|residence\s+hall)\b'),
    ('food', r'^\W*(food|meals?|meal plan|board|dining)\b'),
    ('books_supplies', r'books|supplies|course materials'),
    ('transportation', r'transportation|travel'),
    ('personal', r'personal|miscellaneous|misc\b'),
    ('loan_fees', r'loan\s*fees?'),
    ('mandatory_fee', r'^\W*(mandatory|required|general|student|university|activity|maintenance|program\s+services?)\s+(student\s+)?fees?\b|^\W*fees\W*$'),
    ('fee', r'\bfees?\b'),
]
_ROW = [(k, re.compile(p, re.I)) for k, p in ROW_LABELS]
SKIP_ROW = re.compile(r'per\s+(credit|hour|week|month|night|course|lab|semester\s+hour)|(semester|credit)\s+hour|/\s*(credit|hour|week)|summer|parking|deposit|audit|transcript|graduation', re.I)
SKIP_TABLE = re.compile(r'graduate|doctor|pharm|physician|law school|medicine|medical|dental|dnp|msn|\bmba\b|nurse practitioner|'
                        r'online|per credit|part[- ]time|summer|international student', re.I)
UNDERGRAD = re.compile(r'undergraduate', re.I)


def row_key(label):
    s = re.sub(r'[*†‡:]+', ' ', label or '').strip()
    if not s or len(s) > 90: return None
    for k, rx in _ROW:
        if rx.search(s): return k
    return None


def money(cell):
    """A cell holding exactly one dollar amount (footnote marks allowed), else None."""
    c = re.sub(r'[*†‡]+', '', cell or '').strip()
    if not c or '%' in c or re.search(r'[a-z]{3,}', c, re.I): return None
    v = T.plain_number(c)
    return v if isinstance(v, (int, float)) and v >= 0 else None


STATE_NAMES = {'AL': 'alabama', 'AK': 'alaska', 'AZ': 'arizona', 'AR': 'arkansas', 'CA': 'california', 'CO': 'colorado',
               'CT': 'connecticut', 'DE': 'delaware', 'FL': 'florida', 'GA': 'georgia', 'HI': 'hawaii', 'ID': 'idaho',
               'IL': 'illinois', 'IN': 'indiana', 'IA': 'iowa', 'KS': 'kansas', 'KY': 'kentucky', 'LA': 'louisiana',
               'ME': 'maine', 'MD': 'maryland', 'MA': 'massachusetts', 'MI': 'michigan', 'MN': 'minnesota',
               'MS': 'mississippi', 'MO': 'missouri', 'MT': 'montana', 'NE': 'nebraska', 'NV': 'nevada',
               'NH': 'new hampshire', 'NJ': 'new jersey', 'NM': 'new mexico', 'NY': 'new york', 'NC': 'north carolina',
               'ND': 'north dakota', 'OH': 'ohio', 'OK': 'oklahoma', 'OR': 'oregon', 'PA': 'pennsylvania',
               'RI': 'rhode island', 'SC': 'south carolina', 'SD': 'south dakota', 'TN': 'tennessee', 'TX': 'texas',
               'UT': 'utah', 'VT': 'vermont', 'VA': 'virginia', 'WA': 'washington', 'WV': 'west virginia',
               'WI': 'wisconsin', 'WY': 'wyoming'}
NAMED_STATE = re.compile(r'\b(non-?\s?)?(' + '|'.join(sorted((n.replace(' ', r'\s+') for n in STATE_NAMES.values()), key=len, reverse=True)) + r')\b', re.I)


def residency(h, home=None):
    """in_state / out_of_state / None. A state name counts only when it is the institution's own state:
    'Ohio and Indiana residents' on a Kentucky page is a reciprocity rate, not in-state tuition."""
    if re.search(r'out[- ]of[- ]state|non-?\s?resident', h, re.I): return 'out_of_state'
    named = [(m.group(1), re.sub(r'\s+', ' ', m.group(2).lower())) for m in NAMED_STATE.finditer(h)
             if not (m.group(2).lower() == 'virginia' and re.search(r'west\s+$', h[:m.start()], re.I))]
    if named:
        if home and all(n == STATE_NAMES.get(home) for _, n in named):
            return 'out_of_state' if any(neg for neg, _ in named) else 'in_state'
        return 'named_other_state'
    if re.search(r'in[- ]state|\bresident', h, re.I): return 'in_state'
    return None


def column_meaning(header, home=None):
    h = (header or '').lower()
    years = T.year_labels(header or '')
    return {
        'residency': residency(h, home),
        'arrangement': ('with_parents_or_family' if re.search(r'with\s*(a\s+)?(parent|family)|at home|commut', h) else
                        'off_campus_not_with_family' if re.search(r'off[- ]campus', h) else
                        'on_campus' if re.search(r'on[- ]campus|residence hall|resident student|residential', h) else
                        'other' if re.search(r'military|on base', h) else None),
        'period': ('year' if re.search(r'per\s+year|annual|academic\s+year|fall\s*(&|and)\s*spring|two\s+semesters|yearly|\byear\b', h) else
                   'semester' if re.search(r'per\s+semester|single\s+semester|\bsemester\b|per\s+term', h) else None),
        'year': next(iter(years)) if len(years) == 1 else None,
    }


def parse_tables(rows):
    """Split one HTML table into logical segments and parse each.

    Returns [(title_rows, headers, body)], body = [(label, [values], raw_row_text)]. A new segment
    starts when, after body rows, a one-cell row names a year or a residency (schools often stack
    "Tennessee Residents" and "Non-Tennessee Residents" blocks inside one <table>)."""
    segments, titles, header, body = [], [], None, []

    def close():
        if len(body) >= 2: segments.append((list(titles), header[1:] if header else [], list(body)))

    for r in rows:
        cells = [c.strip() for c in r]
        filled = [c for c in cells if c]
        has_money = any(money(c) is not None for c in cells[1:])
        if body and len(filled) == 1 and not has_money:
            m = column_meaning(filled[0])
            if m['year'] or m['residency']:
                close(); titles, header, body = [filled[0]], None, []
            continue
        if header is None and not body:
            if len(filled) <= 1 and not has_money:
                titles.extend(filled); continue
            if not has_money:
                header = cells; continue
        if has_money and cells and cells[0]:
            body.append((cells[0], [money(c) for c in cells[1:]], ' | '.join(cells)))
    close()
    return segments


def parse_table(rows):
    """First logical segment (kept for callers and tests that expect one table)."""
    segs = parse_tables(rows)
    return segs[0] if segs else None


def _context(t, page, titles):
    return ' '.join([t.get('year_heading') or '', t.get('heading') or '', t.get('caption') or ''] + titles)


def _candidates_from_table(t, inst, entry, page, today_year, page_year, page_basis, page_issues):
    out = []
    for titles, headers, body in parse_tables(t['rows']):
        out += _candidates_from_segment(t, titles, headers, body, inst, entry, page, today_year, page_year, page_basis, page_issues)
    return out


def _candidates_from_segment(t, titles, headers, body, inst, entry, page, today_year, page_year, page_basis, page_issues):
    context = _context(t, page, titles)
    if SKIP_TABLE.search(context + ' ' + ' '.join(headers)) and not UNDERGRAD.search(context):
        return []
    # Every printed money row is kept (and counts toward reconciliation); unrecognised rows get key None.
    keyed = [(row_key(label), label, vals, raw) for label, vals, raw in body if not SKIP_ROW.search(label)]
    kinds = {k for k, *_ in keyed}
    if not kinds & {'tuition', 'tuition_and_fees'} or len(kinds) < 2:
        return []
    ncols = max(len(v) for _, _, v, _ in keyed)
    semester_total = None
    home = inst.get('state')
    ctx = column_meaning(context, home)
    cols = []
    for j in range(ncols):
        m = column_meaning(headers[j] if j < len(headers) else '', home)
        for k in ('residency', 'period', 'year'):
            m[k] = m[k] or ctx[k]
        m['header'] = headers[j] if j < len(headers) else ''
        cols.append(m)
    issues = list(page_issues)
    if any(c['period'] == 'year' for c in cols):
        keep = [j for j, c in enumerate(cols) if c['period'] != 'semester']
    else:
        keep = list(range(ncols))
    semester_only = all(cols[j]['period'] == 'semester' for j in keep)
    # Two total rows (per semester / for fall and spring): use the annual one.
    totals = [k for k in keyed if k[0] == 'total']
    if len(totals) > 1:
        coa = [k for k in totals if re.search(r'\bcoa\b|cost\s+of\s+attendance', k[1], re.I)]
        if len(coa) == 1:  # direct/indirect subtotals plus a labelled COA total: the COA total is the total
            keyed = [k for k in keyed if k[0] != 'total' or k is coa[0]] + [(None, k[1], k[2], k[3]) for k in totals if k is not coa[0]]
            totals = [coa[0]]
        annual = [k for k in totals if re.search(r'fall\s*(&|and)\s*spring|year|annual', k[1], re.I)]
        per_sem = [k for k in totals if re.search(r'semester|term', k[1], re.I) and k not in annual]
        if len(totals) == 1:
            pass
        elif annual and per_sem:
            # Components are printed per semester; the annual total is printed separately. Keep both
            # verbatim, reconcile against the semester total, and leave per-semester rows out of the
            # annual canonical fields.
            semester_total = per_sem[0]
            keyed = [k for k in keyed if k[0] != 'total'] + [annual[0]]
            semester_only = False
        elif annual:
            keyed = [k for k in keyed if k[0] != 'total'] + [annual[0]]
            semester_only = False
        else:
            issues.append('multiple_total_rows')
    if semester_only: issues.append('cost_period_semester')
    private = inst.get('control') == 'private_nonprofit'
    page_res = column_meaning(page.title + ' ' + ' '.join(page.headings[:3]), home)['residency']
    groups = {}
    for j in keep:
        c = cols[j]
        res = c['residency'] or page_res or ('not_applicable' if private else None)
        year = c['year'] or page_year
        groups.setdefault((res, year), []).append(j)
    out = []
    for (res, year), js in groups.items():
        g_issues = list(issues)
        if res == 'named_other_state':  # e.g. a reciprocity rate for a neighbouring state's residents
            res = None; g_issues.append('residency_names_another_state')
        if res is None:
            g_issues.append('residency_unknown')
        arrangements, evidence = [], []
        for j in js:
            comp, printed = {}, {}
            for key, label, vals, raw in keyed:
                v = vals[j] if j < len(vals) else None
                if v is None: continue
                printed[label] = v
                if key: comp.setdefault(key, []).append(v)
                evidence.append({'field': f"{cols[j]['arrangement'] or 'column'}:{label}", 'value': v, 'snippet': raw[:240]})
            if printed: arrangements.append((cols[j]['arrangement'], cols[j]['header'], comp, printed))
        if not arrangements: continue
        primary = next((a for a in arrangements if a[0] == 'on_campus'), arrangements[0])
        comp, printed = primary[2], primary[3]
        one = lambda k: comp[k][0] if len(comp.get(k, [])) == 1 else None
        total = one('total')
        parts = [v for lbl, v in printed.items() if row_key(lbl) != 'total']
        checks = {'columns': len(arrangements), 'rows': len(printed)}
        if semester_total is not None:
            j0 = js[arrangements.index(primary)] if len(js) == len(arrangements) else js[0]
            sem = semester_total[2][j0] if j0 < len(semester_total[2]) else None
            if sem is not None:
                printed[semester_total[1]] = sem
                checks['components_per_semester'] = True
                checks['components_reconcile'] = abs(sum(parts) - sem) < 1
                if not checks['components_reconcile']: g_issues.append('components_do_not_reconcile')
                one = lambda k, _o=one: _o(k) if k == 'total' else None  # per-semester rows are not annual fields
        elif total is not None:
            checks['components_reconcile'] = abs(sum(parts) - total) < 1
            if not checks['components_reconcile']: g_issues.append('components_do_not_reconcile')
        # A printed total is a cost of attendance only when indirect costs are part of the table (or the
        # row says so); tuition + fees + room + board alone is the direct (billed) cost.
        total_label = next((lbl for lbl in printed if row_key(lbl) == 'total'), '')
        indirect = any(k in comp for k in ('books_supplies', 'transportation', 'personal'))
        is_coa = indirect or bool(re.search(r'\bcoa\b|cost\s+of\s+attendance', total_label, re.I))
        tuition = one('tuition') or one('tuition_and_fees')
        limit = 60000 if 'cost_period_semester' in g_issues else 120000
        if any(v > (limit * 1.6 if lbl and row_key(lbl) == 'total' else limit) for lbl, v in printed.items()) or (tuition is not None and tuition < 300):
            g_issues.append('implausible_amount')
        if year is None:
            year, basis = today_year, 'source_unlabeled'
        else:
            basis = 'labeled_in_source' if (year != page_year or page_basis.startswith('labeled')) else page_basis
            if year < today_year: g_issues.append(f'stale_year_label:{year}')
        if basis == 'source_unlabeled' and 'ambiguous_year_labels' not in g_issues and len(T.year_labels(page.text[:60000])) > 1:
            g_issues.append('ambiguous_year_labels')
        record = {'residency': res or 'not_applicable', 'currency': 'USD',
                  'cost_period': 'semester' if 'cost_period_semester' in g_issues else 'academic_year',
                  'tuition': one('tuition'), 'mandatory_fees': one('mandatory_fee') if one('tuition') is not None and 'fee' not in comp else None,
                  'books_supplies': one('books_supplies'),
                  'on_campus_food_housing': one('food_housing') if primary[0] == 'on_campus' else None,
                  'total_cost_of_attendance': total if is_coa else None,
                  'components': printed,
                  'notes': f'Extracted by {EXTRACTOR} from the table "{(context or primary[1])[:120]}"; printed rows copied, totals never recomputed.'}
        if total is not None and not is_coa:
            record['total_direct_cost'] = total
            record['notes'] += ' The printed total covers direct (billed) costs only, so it is not a cost of attendance.'
        if one('tuition_and_fees') is not None:
            record['tuition_and_mandatory_fees'] = one('tuition_and_fees')
        if UNDERGRAD.search(context + ' ' + page.title): record['student_population'] = 'undergraduate'
        if len(arrangements) > 1:
            record['living_arrangements'] = [{'arrangement': a or 'unlabeled', 'column_header': h,
                                              'total_cost_of_attendance': c['total'][0] if len(c.get('total', [])) == 1 else None,
                                              'components': p} for a, h, c, p in arrangements]
            if any(a is None for a, *_ in arrangements): g_issues.append('arrangement_unlabeled')
        out.append(common.make('costs', inst['institution_key'], year, basis, record, evidence, entry, EXTRACTOR,
                               {'residency': record['residency']}, checks, sorted(set(g_issues))))
    return out


COST_DOC = re.compile(r'cost of attendance|tuition\s*(&|and)\s*fees|estimated (cost|expenses)|cost estimates?|student budget|tuition rates?', re.I)
NOT_COST_DOC = re.compile(r'common data set|fact\s*book|catalog|handbook|annual report|financial statement|audit', re.I)


def _pdf_tables(page):
    """Rebuild a pseudo-table from layout text lines '<label>  $1  $2' under a header line."""
    rows, header = [], None
    for line in page.lines:
        cells = [c for c in re.split(r'\s{2,}', line.strip()) if c]
        if len(cells) < 2:
            if not rows and cells and not money(cells[0]): header = None
            continue
        if any(money(c) is not None for c in cells[1:]):
            rows.append(cells)
        elif not rows:
            header = cells
    if len(rows) < 3: return []
    return [{'heading': page.title, 'caption': '', 'rows': ([[''] + header] if header else []) + rows}]


def extract(inst, entry, page, today_year):
    if common.professional_source(entry, page): return []
    page_year, page_basis, page_issues = common.resolve_year(page, entry, today_year)
    page_issues = [i for i in page_issues if not i.startswith('stale_year_label')]  # judged per table below
    if page_basis == 'ambiguous_year_labels': page_year = None; page_basis = 'source_unlabeled'; page_issues = []
    tables = page.tables
    if entry.get('kind') in {'pdf', 'xlsx'}:
        head = page.title + ' ' + page.text[:3000] + ' ' + entry.get('url', '')
        if not COST_DOC.search(head) or NOT_COST_DOC.search(head): return []
        if entry.get('kind') == 'pdf': tables = _pdf_tables(page)
    out = []
    for t in tables:
        out += _candidates_from_table(t, inst, entry, page, today_year, page_year, page_basis, page_issues)
    best = {}
    for c in out:  # one candidate per residency and year per page: the one with most evidence
        k = (c['record']['residency'], c['academic_year'])
        if k not in best or len(c['evidence']) > len(best[k]['evidence']): best[k] = c
    return list(best.values())
