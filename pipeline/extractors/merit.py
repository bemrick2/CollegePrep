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
SCHOLARSHIP_CONTEXT = re.compile(r'scholarship|merit|\bawards?\b', re.I)  # not "awarding course credit" (AL: Stillman)
NOT_MERIT = re.compile(r'\bexamples?\b|need[- ]based|federal|pell|loan|work[- ]study|graduate|transfer|athletic|tuition|fees?\b|cost|'
                       r'credits?\s+completed', re.I)  # IA (Wartburg): an academic-progress table
NOT_NAME = re.compile(r'^[\d<>=.\s/+%$,-]*$|tuition|\bfees?\b|per credit|per course|deposit|housing|meal|eligib|'
                      r'\bstudents?\s+(is|who|still|are)\b|fall below|balance', re.I)
# Names that are not merit awards (KY: federal aid and loans in an aid table, staff directories, credit-hour bands
# from an academic-standards table).
NOT_AWARD_NAME = re.compile(r'^\W*(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?\s+\d{1,2}\W*$|\bap\s+credit\b|\bph\.?\s?d\b|\bdoctoral\b|\bmaster\'?s\b|\bpell\b|\brotc\b|yellow\s+ribbon|supplemental\s+educational\s+opportunity|\bseog\b|work[- ]study|\bloans?\b|\bplus\b|'
                            r'college\s+access\s+program|counselor(?!(?:\x27|\u2019)?s?\s+(?:award|scholarship))|director|coordinator|specialist|\bassistant\b|officer|advisor|'
                            r'^(fewer|more|less)\s+than\b|^over\s+\d|\bcredit\s+hours?\b|'
                            r'^\W*(books?|supplies|transportation|personal\s+expenses?|loan\s+fees?|room|board|food)\b|'
                            r'^(reading|english|math(ematics)?|science|writing|composite)$|'
                            r'^(gpa|act|sat|clt|psat|scores?|tiers?|level|amount)$|^(annual\s+)?totals?$', re.I)  # OK (Oklahoma Christian): a header row repeated in the body  # AR: UA-PTC placement score rows  # OR: COA rows
NOT_MERIT_PAGE = re.compile(r'course[- ]awards|\bclep\b|examination[- ]program|(?:private|outside|external)[- ]scholarships?|undocumented|sample[- ]aid[- ]packages?|aid[- ]package[- ]examples?|retention|renewal|keep(?:ing)?[- ]your[- ]scholarship|academic[- ]standards|probation|satisfactory[- ]academic[- ]progress|financial[- ]aid[- ]staff|'
                            r'\bstaff\b|directory|meet[- ]the[- ]team|our[- ]team|'
                            # GA r1: lists of other organizations' awards (Agnes Scott outside scholarships, Georgia Southern
                            # military scholarships, West Georgia Tech foundation awards) and international-office waivers (UWG ISAP).
                            r'outside[- ]scholarships?|external[- ]scholarships?|third[- ]party|military|veteran|foundation|/isap/|donor[- ]scholarships?|'
                            r'achievements|recipients|honor[- ]roll|dean.?s[- ]list|/testing/|_credits/|credit[- ]by[- ]exam|'
                            # FL r1: faculty emeriti lists (South Florida), state and federal programs on a college page
                            # (Bright Futures, TEACH Grant) are not institutional merit awards.
                            r'emerit|retirees|bright[- ]futures|/teach\b|teach[- ]grant|\bpell\b', re.I)  # Hampton IB credit table
HEADER_WORDS = re.compile(r'scholarship|award|merit|name|level|tier|amount|value|gpa|act\b|sat\b|criteria|requirement', re.I)
THRESHOLD_CELL = re.compile(r'^\s*[<>≤≥]?\s*\d{1,4}(\.\d{1,2})?\s*(\+|[-–]\s*\d{1,4}(\.\d{1,2})?|or\s+(higher|above))?\s*$', re.I)


PLACEHOLDER = re.compile(r'^\W*(n/?a|none|see\s+(?:requirements|criteria|details|below|website)|varies|tbd|-+|—|–)\W*$', re.I)  # ND (Lake Region): an en dash is an empty cell
YES_NO = re.compile(r'\s*(?:yes|no|all|any)\s*', re.I)
PHONE = re.compile(r'\(?\d{3}\)?[\s.-]\d{3}[.-]\d{4}')  # Tougaloo: a contact number in the ACT column is not a score
ENROLLMENT = re.compile(r'^(full|half|part|three[-\s]quarter|3/4)[-\s]time(\s*\([^)]*\))?$|^\d+(\.\d+)?\s+credits?\s+or\s+more$', re.I)  # WY (Northwest): "Full Time (12.0-14.5 credits)", "15.0 credits or more"  # Ole Miss Sumners: amount by enrollment intensity
SCORE = re.compile(r'\b\d{1,4}\b')
PACKAGE_ROW = re.compile(r'federal|pell|state\s+grants?|outside\s+scholarships?|student\s+employment|work[- ]study|\bloans?\b|^total\b', re.I)
_N = r'(?:\d{1,2}|two|three|four|five|six|eight|ten)'
MULTI_YEAR = re.compile(r'(?<!renewable\s)\b(?:for|over|value|maximum\s+of)\s+' + _N + r'\s+(?:fall/spring\s+)?(?:years?|semesters|trimesters|quarters|terms)\b', re.I)  # outside parentheses; ND (VCSU "for two year", Minot "maximum of 4 years")
MULTI_X = re.compile(r'\bx\s*' + _N + r'\s+(?:years|semesters|trimesters|quarters|terms)\b|\b' + _N + r'\s+(?:years|semesters|trimesters|quarters|terms)\s+x\b', re.I)
MERGED_GPA = re.compile(r'^(.*?[A-Za-z)])\s*(\d\.\d{1,2}\s*\+?\s*(?:GPA|grade\s+point\s+average)\.?)\s*$', re.I)
MERGED_TEXT = re.compile(r'^(.{3,80}?\b(?:Scholarship|Award|Grant|Fellowship))(?=[A-Z][a-z])')


PAGE_RESIDENCY = re.compile(r'\bout[- ]of[- ]state\b|\bnon[- ]?residents?\b|\bin[- ]state\b', re.I)
ENTERING_CLASS = re.compile(r'\bfall\s+(20\d{2})\b|\b(20\d{2})\s+(?:in[- ]state\s+|out[- ]of[- ]state\s+|incoming\s+|entering\s+|first[- ]year\s+)*'
                            r'(?:freshm[ae]n|first[- ]year|incoming|entering)\b', re.I)


def _split_name(nm):
    """'Covenant Stone Scholarship3.5+ GPA.' -> ('Covenant Stone Scholarship', '3.5+ GPA.'); 'Theatre ScholarshipOpen to all
    actors' -> ('Theatre Scholarship', None). Cells merged by the page markup (Maryville, TN r5)."""
    m = MERGED_GPA.match(nm)
    if m and not re.search(r'\b(act|sat)\b', m.group(1), re.I): return m.group(1).strip(), m.group(2).strip()
    m = MERGED_TEXT.match(nm)
    return (m.group(1).strip(), None) if m else (nm, None)


def _page_award_name(page):
    """'Orange White Scholarship - One Stop Student Services' -> 'Orange White Scholarship'."""
    first = re.split(r'\s+[-|–—]\s+', page.title or '')[0].strip()
    return first if re.search(r'scholarship|award|grant|fellowship', first, re.I) and len(first) <= 80 else None


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
    # "$11,000 ($44,000 over 4 years)" (Chowan): the multi-year figure is not the annual range
    cell = re.sub(r'\([^)]*(?:over|total|years?|4-year|four)[^)]*\)', '', cell or '', flags=re.I)
    # KS (Dodge City): "$2,000 per year ($1,000 per semester)"; UT (SUU): "$12,000 ($6,000/semester*)"
    # CO (Otero): "$1000 ($500 for Fall Semester and $500 for Spring Semester)"
    cell = re.sub(r'\([^)]*(?:\bper\s+|/\s*|\bfor\s+(?:the\s+)?(?:fall|spring)\s+)(?:semester|term|trimester|quarter)\b[^)]*\)', '', cell, flags=re.I)
    vals = T.money_values(cell or '')
    # MO (Columbia College): "$1,000-2,000" prints the dollar sign once for the whole range
    for a, b in re.findall(r'\$\s*([\d,]{3,})\s*[-–]\s*([\d,]{3,})(?![\d,])', cell or ''):
        vals += [float(a.replace(',', '')), float(b.replace(',', ''))]
    # TX (TAMU-Corpus Christi): "$4,000/$16,000" is the annual award and its four-year total
    pair = re.search(r'\$\s*([\d,]{3,})\s*/\s*\$\s*([\d,]{3,})', cell or '')
    if pair and len(vals) == 2:
        a, b = (float(x.replace(',', '')) for x in pair.groups())
        if a and b / a in (2, 3, 4, 5): return a, a
    return (min(vals), max(vals)) if vals else (None, None)


def _list_awards(t, header, body, title, award_type):
    # "Scholarship Criteria" (UTK Orange & White) names the threshold column, not the award.
    name = next((i for i, h in enumerate(header) if any(w in h.lower() for w in ('scholarship', 'award', 'name', 'program'))
                 and not re.search(r'criteria|requirement|eligib|amount|annual|per\s+year|years?\b|value|total|\$', h, re.I)), None)
    # Annual columns win over four-year totals ("Total over 4 years | Total for academic year", AL: AUM).
    multi_year = re.compile(r'4\s*years?|four\s+years?|total\s+over|over\s+\d|cumulative', re.I)
    amount = next((i for words in (('annual', 'per year', 'yearly', 'academic year', 'per academic'), ('amount', 'value', '$', 'award detail', 'offer', 'reward'), ('award',))
                   for i, h in enumerate(header) if i != name and any(w in h.lower() for w in words) and not multi_year.search(h)), None)
    if amount is None:  # ND (Jamestown): "Scholarship | GPA | (blank)" with the amounts under the blank header
        amount = next((i for i, h in enumerate(header) if i != name and not h.strip() and body
                       and sum(1 for r in body if i < len(r) and T.money_values(r[i])) >= 0.8 * len(body)), None)
    gpa = _col(header, 'gpa', 'grade point')
    act = _col(header, 'act')
    sat = _col(header, 'sat')
    if act is not None and sat is not None and act == sat: sat = None
    test = None if (act is not None or sat is not None) else _col(header, 'test', 'superscore', 'score')
    renewal = _col(header, 'renew', 'retain', 'retention', 'maintain', 'to keep')
    criteria = next((i for i, h in enumerate(header) if i != renewal and re.search(r'requirement|criteria|eligib|qualif|\bpoints?\b', h, re.I)), None)
    if criteria in (name, amount, gpa, act, sat, test): criteria = None
    if gpa is not None and gpa in (act, sat):  # one column holds "21-22 ACT / 1060-1120 SAT or 3.00-3.24 GPA"
        test, gpa, act, sat = gpa, None, None, None
    if name is None: name = 0
    if criteria == name: criteria = None  # the threshold column is the row label (tier rows below)
    # UTK In-State Volunteer: "ACT / SAT | Annual Award" - the score column labels the rows, the page names the award.
    threshold_cols = sorted({i for i in (gpa, act, sat, test) if i is not None}) if name in (gpa, act, sat, test) else []
    threshold_label = bool(threshold_cols)
    gpa_col = gpa
    if threshold_label: gpa, act, sat, test = None, None, None, None  # every threshold column labels the row instead
    clean = lambda h: h.strip().strip('*').strip()
    if amount is None and gpa is None and act is None and sat is None and test is None and criteria is None: return []
    out = []
    for row in body:
        if name > 0 and len(row) < len(header): continue  # AR (UCA): merged cells shifted this row; its columns no longer line up
        cells = list(row) + [''] * (len(header) - len(row))
        nm = cells[name].strip()
        if not nm or len(nm) > 120 or T.money_values(nm): continue
        if threshold_label and not re.search(r'\d', nm): continue  # "OR" between tier rows
        if not threshold_label and (NOT_NAME.search(nm) or NOT_AWARD_NAME.search(nm)): continue
        if nm.endswith(':') or len(nm.split()) > 12: continue  # worked examples and sentences, not award names
        get = lambda i: cells[i].strip() if i is not None and i < len(cells) else ''
        # TX (South Texas College) "GPA: Yes/No", (Texas Southmost) "All", (Texas State) contact e-mail cells are not criteria
        amt, g, a, s, tst, crit, ren = (x if not (PLACEHOLDER.match(x) or PHONE.search(x) or '@' in x or YES_NO.fullmatch(x)) else '' for x in (get(amount), get(gpa), get(act), get(sat), get(test), get(criteria), get(renewal)))
        nm, merged_gpa = _split_name(nm)
        if merged_gpa and not g: g = merged_gpa
        if not (amt or g or a or s or tst or crit): continue
        lo, hi = _amounts(amt)
        outside = re.sub(r'\([^)]*\)', '', amt)
        if (re.search(r'semester\s+basis|per\s+semester|/\s*semester', outside, re.I) or re.search(r'\$[\d,.]+\s+(?:for\s+)?(?:the\s+)?(?:fall|spring)\b', outside, re.I)) \
                and not re.search(r'per\s+year|annual|/\s*y(?:ea)?r', outside, re.I):  # TX (South Texas): "$500 Fall & $500 Spring"
            lo, hi = None, None  # ND (Lake Region): "$100–$300 awarded on a semester basis" is not an annual range
        if re.search(r'tuition[^$]*(\+|\bplus\b|\band\b)\s*\$', amt, re.I) or \
           MULTI_YEAR.search(re.sub(r'\([^)]*\)', '', amt)) or MULTI_X.search(amt) or re.search(r'\bfull\s+tuition\b|\bper\s+credit\b|\btotal\s+value\b', amt, re.I):  # KS (K-State Salina): "Total Value: $100,000"  # MO (Logan): "$400 per credit hour" is not an annual award
            # AR (UAPB) "$66,000 for four years"; OK (OU) "$16,000 ($4,000 x 4 years)", (USAO) "total estimated value 8 fall/spring
            # terms", (SWOSU) "$5000 cash per year, full tuition": the printed figure is not the annual award
            lo, hi = None, None  # LSUS: "Tuition & Fees + $1,200 Campus Housing Credit" is not a $1,200 award
        if hi is not None and re.search(r'\bor\s+(?:more|greater|higher)\b|\band\s+up\b', amt, re.I):
            hi = lo if lo is not None else hi; rec_open_max = True  # ID (New Saint Andrews): "$5,000 or more" has no maximum
        else:
            rec_open_max = False
        if lo is not None and re.search(r'\bup\s+to\b', amt, re.I):
            lo = None  # "Up to $5,000" is a maximum; the minimum is not printed
        tier_row = bool(threshold_label) or bool(re.search(r'\d.*\b(gpa|act|sat)\b', nm, re.I)) or bool(ENROLLMENT.match(nm))
        if tier_row and NOT_AWARD_NAME.search(title): continue  # AZ (Prescott): tiers of a Ph.D. scholarship
        rec = {'award_name': f"{title}: {nm}" if tier_row else nm, 'award_type': award_type}
        if threshold_label:  # UTK Out-of-State Volunteer: "4.0+ | 34-36/1490-1600 | $18,000" and "4.0+ | 30-33/... | $9,000"
            parts = [(i, get(i)) for i in threshold_cols if get(i)]
            rec['award_name'] = f"{title}: " + ', '.join(f'{clean(header[i])} {v}' for i, v in parts)
            for i, v in parts:
                if i == gpa_col and re.search(r'\d\.\d', header[i]) and re.search(r'\b(act|sat)\b', v, re.I):
                    # USM: the header is a GPA band and the rows are test ranges ("3.0 - 3.24 GPA" over "23 - 25 ACT Score")
                    rec['gpa_requirement'] = clean(header[i])
                    rec['test_requirement'] = '; '.join(x for x in [rec.get('test_requirement'), v] if x)
                    continue
                key = 'gpa_requirement' if i == gpa_col else 'test_requirement'
                rec[key] = '; '.join(x for x in [rec.get(key), f'{clean(header[i])}: {v}'] if x)
        elif tier_row and ENROLLMENT.match(nm):
            pass  # the row is an enrollment level, not a threshold
        elif tier_row:  # the row label is itself the threshold ('3.6+ GPA, 26-27 ACT')
            rec['test_requirement' if re.search(r'\b(act|sat)\b', nm, re.I) else 'gpa_requirement'] = nm
        if amt: rec['award_amount_text'] = amt
        if re.search(r'\bfor\s+(the\s+)?freshman\s+year|\bone[\s–-]*time\b|\bnon[\s-]*renewable\b', amt, re.I):
            rec['renewable'] = False  # UL Lafayette: "$1,000 for freshman year"
        if hi is not None:
            if lo is not None: rec['award_min'] = lo
            if not rec_open_max: rec['award_max'] = hi
        if g: rec['gpa_requirement'] = g
        # Prefix only bare scores: "ACT: 27+ / SAT: 1220+" already names the test, "Valedictorian" is not a score (Tougaloo).
        label = lambda name, v: f'{name} {v}' if v and SCORE.search(v) and not re.search(r'\b(act|sat)\b', v, re.I) else v
        tests = ' / '.join(x for x in [label('ACT', a), label('SAT', s) if s != a else ''] if x) or tst
        if tests: rec['test_requirement'] = tests
        if crit:  # a bare points range is meaningless without its column name (Southern: "Points | 4,800 - 5,700")
            rec['eligibility_summary'] = (f"{header[criteria].strip()}: {crit}" if re.search(r'\bpoints?\b', header[criteria], re.I) else crit)[:600]
        if ren: rec['renewal_requirements'] = ren[:600]
        thresholds = {k: v for k, v in {'gpa_min': _num(g, 0, 5, True), 'act_min': _num(a, 1, 36), 'sat_min': _num(s, 400, 1600)}.items() if v is not None}
        if thresholds: rec['thresholds'] = thresholds
        if any(re.fullmatch(r'\s*(or|and|&)\s*', c, re.I) for c in cells):
            rec['_issues'] = ['threshold_logic_column']  # AR (ATU): an "or"/"&" column says whether GPA and test are both required
        out.append((rec, ' | '.join(cells)))
    return out


def _tier_award(t, header, body, context):
    """One threshold column and one amount column: 'GPA | Merit', '3.0 | $14,000'."""
    if len(header) != 2 or not re.search(r'gpa|act|sat|score', header[0], re.I): return []
    rows = [r for r in body if len(r) >= 2 and THRESHOLD_CELL.match(r[0]) and T.money_values(r[1])]
    if len(rows) < 3 or len(rows) < len(body) - 1: return []
    tiers = [{header[0].strip().lower() or 'threshold': r[0], 'amount_text': r[1]} for r in rows]
    amounts = [v for r in rows for v in T.money_values(r[1])]
    if any(MULTI_YEAR.search(r[1]) or MULTI_X.search(r[1]) for r in rows):
        amounts = []  # ND (Minot): "$10,000 $2,500/year for a maximum of 4 years" mixes totals with annual amounts
    title = (t.get('heading') or t.get('caption') or 'Merit scholarship tiers').strip().lstrip('+-–•*› ').strip()
    rec = {'award_name': title[:120], 'award_type': 'institutional_merit', 'award_tiers': tiers}
    if amounts: rec['award_min'], rec['award_max'] = min(amounts), max(amounts)
    if re.search(r'one[\s–-]*time', header[1], re.I):  # Georgia Southern: "Annual Award Amount (One – Time)"
        rec['renewable'] = False
        rec['award_amount_text'] = header[1].strip()[:120]
    rec['gpa_requirement' if re.search('gpa', header[0], re.I) else 'test_requirement'] = \
        f"Tiered by {header[0].strip()}: " + '; '.join(f"{r[0]} → {r[1]}" for r in rows)
    return [(rec, ' || '.join(' | '.join(r) for r in [header] + rows))]


def _grid_award(t, header, body, context):
    """GPA x test-score matrix: header cells are score ranges, first column GPA ranges, cells amounts."""
    # Ole Miss: "No Test Score" is a tier column like the score ranges.
    score_cols = [i for i, h in enumerate(header) if i > 0 and re.search(r'\d{2}|\bno\s+test|test[\s-]*optional|without\s+(a\s+)?test', h, re.I)]
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
    title = (t.get('heading') or t.get('caption') or 'Merit scholarship grid').strip().lstrip('+-–•*› ').strip()
    rec = {'award_name': title[:120], 'award_type': 'institutional_merit', 'award_tiers': tiers,
           'test_requirement': f"Tiers by {header[0] or 'GPA'} and {', '.join(header[i] for i in score_cols[:2])}…",
           'award_min': min(amounts), 'award_max': max(amounts)}
    return [(rec, ' || '.join([' | '.join(header)] + evidence_rows))]


def extract(inst, entry, page, today_year):
    if not page.tables or common.professional_source(entry, page) or common.international_source(entry, page): return []
    if not SCHOLARSHIP_CONTEXT.search(page.title + ' ' + ' '.join(page.headings[:6]) + ' ' + entry.get('url', '')):
        return []
    if NOT_MERIT_PAGE.search(page.title + ' ' + entry.get('url', '')): return []
    if re.search(r'(?:^|[-–|:]\s*)loans?\s*$', page.title, re.I): return []  # WI (UW-Platteville): a loans page's borrowing limits
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
        if sum(1 for r in body if any(PHONE.search(c) for c in r)) >= 2: continue  # NM (Luna): a staff contact table, not awards
        if re.search(r'award\s+amounts?', header[0], re.I) and any(T.money_values(c) for c in header[1:]):
            continue  # ID (BYU-Idaho): a transposed table - columns are award levels, rows are attributes ("Qualifications", "Duration")
        if any(T.money_values(c) for c in header[1:]):  # no header row (AL: UWA): infer columns from the cells
            amount_i = next(i for i, c in enumerate(header) if i and T.money_values(c))
            crit_i = next((i for i, c in enumerate(header) if i and i != amount_i and re.search(r'\b(gpa|act|sat)\b', c, re.I)), None)
            header = ['Scholarship'] + [''] * (len(header) - 1)
            header[amount_i] = 'Amount'
            if crit_i is not None: header[crit_i] = 'Requirements'
            body = rows
        if NOT_MERIT.search(' '.join(header)) or NOT_NAME.search(context): continue
        if any(len(c) > 60 for c in header): continue  # a sentence is not a header row (APSU: "Freshmen | Qualifying freshmen have ...")
        if len(header) == 2 and re.fullmatch(r'\s*(requirements?|criteria|items?|attributes?|details?)\s*', header[0], re.I):
            continue  # key/value facts about one award (UTK: "Requirement | Details", "FAFSA Required | No")
        if re.search(r'\bcollege\s+gpa\b', ' '.join(header), re.I): continue  # college-GPA tiers are transfer awards (CBU)
        if not HEADER_WORDS.search(' '.join(header)): continue  # e.g. worked aid examples, schedules
        shaped = _tier_award(t, header, body, context) or _grid_award(t, header, body, context)
        merit_context = re.search(r'merit|academic|gpa|act|sat|test score', context + ' ' + ' '.join(header) + ' ' + page.title, re.I)
        award_type = 'institutional_merit' if merit_context else 'institutional_other'
        named = re.sub(r'\bawards?\s+amounts?\b', '', context, flags=re.I)  # "Award Amounts" is a heading, not a name (UTK)
        label = context.strip() if re.search(r'scholarship|award|grant|fellowship', named, re.I) else (_page_award_name(page) or context.strip() or page.title)
        label = label.strip().lstrip('+-–•*› ').strip()  # "+Scholarships" (Thomas University): an accordion icon, not the name
        found = shaped or _list_awards(t, header, body, label[:80], award_type)
        # IA (Graceland): a sample aid package lists federal/state grants, outside scholarships and work beside the award
        if sum(1 for r in body if r and PACKAGE_ROW.search(r[0])) >= 2: continue
        # MO (Southwest Baptist): the same heading over a different table is another year's version; which is which is unclear
        twins = [o for o in page.tables if o is not t and (o.get('heading') or '') == (t.get('heading') or '') and o.get('heading')
                 and o.get('rows') and o['rows'][0] == t['rows'][0] and o['rows'] != t['rows']]
        if not found or (not shaped and len(found) < 2): continue  # one stray row is not a scholarship table
        t_year = T.year_labels(context)
        rec_year, rec_basis, rec_issues = (year, basis, issues)
        cls = ENTERING_CLASS.search(context) if not t_year and basis == 'source_unlabeled' else None
        if cls:
            first = int(cls.group(1) or cls.group(2))
            rec_year, rec_basis = T.academic_year(first), 'labeled_entering_class'  # the class entering that fall
            rec_issues = [i for i in issues if not i.startswith('stale_year_label')]
            if rec_year < today_year: rec_issues.append(f'stale_year_label:{rec_year}')
        if len(t_year) == 1:
            rec_year, rec_basis = next(iter(t_year)), 'labeled_in_source'
            rec_issues = [i for i in issues if i != 'ambiguous_year_labels' and not i.startswith('stale_year_label')]
            if rec_year < today_year: rec_issues.append(f'stale_year_label:{rec_year}')
        for rec, raw in found:
            row_issues = rec.pop('_issues', []) + (['duplicate_table_versions'] if twins else [])
            ev = [{'field': k, 'value': v, 'snippet': raw[:300]} for k, v in rec.items()
                  if k in {'award_amount_text', 'gpa_requirement', 'test_requirement', 'award_tiers', 'eligibility_summary', 'renewal_requirements'}]
            if not ev: continue
            res = PAGE_RESIDENCY.search(page.title + ' ' + context)
            if res and 'residency_requirement' not in rec:  # "In-State Freshman Scholarships" (AL: UAB has same-named awards per residency)
                rec['residency_requirement'] = 'Out-of-state' if re.search(r'out|non', res.group(0), re.I) else 'In-state'
            # AZ (Northland Pioneer): a page-navigation heading ('Social Media') is not where the award is listed
            nav = re.search(r'social\s+media|quick\s+links|follow\s+us|connect\s+with\s+us|related\s+links|footer|navigation|\bmenu\b|academic\s+calendar', context, re.I)
            if context.strip() and not nav and not re.search(r'scholarship|award|grant|fellowship', context, re.I) and 'eligibility_summary' not in rec:
                rec['eligibility_summary'] = f'Listed under: {context.strip()[:200]}'  # IA (Hawkeye): "GED, HiSET, or ELL Graduates"
            rec['notes'] = f'Extracted by {EXTRACTOR} from the table "{(context or page.title)[:100]}"; cells copied as printed.'
            out.append(common.make('awards', inst['institution_key'], rec_year, rec_basis, rec, ev, entry, EXTRACTOR,
                                   {'award_name': rec['award_name']}, {'thresholds': rec.get('thresholds')}, rec_issues + row_issues))
    return out
