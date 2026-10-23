"""Merit scholarship tables -> awards candidates.

Two published shapes are recognised:
  list: one row per scholarship (name, amount, GPA / ACT / SAT thresholds as printed)
  grid: GPA ranges down the side, test-score ranges across the top, award amounts in the cells
Every cell is copied as printed. Numeric minimums (`thresholds`) are added only when a cell is one
clean number on the right scale; ranges, "or", footnotes and anything else stay text only. Nothing
about automatic consideration, renewal or stacking is inferred.
"""
from __future__ import annotations
import itertools, json, re
from collections import Counter

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
NOT_AWARD_NAME = re.compile(r'^\W*(?:freshman|sophomore|junior|senior)\s+\d+\s*(?:[-–]\s*\d+|\+)\s+credits\W*$|^\W*(?:\d(?:st|nd|rd|th)\s+(?:and\s+\d(?:st|nd|rd|th)\s+)?semester\s+\w+|all\s+(?:freshmen|sophomores|juniors|seniors))\W*$|\bapplicants?:|\((?:final|priority)\)|^\W*in\s+this\s+section\W*$|^\W*(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?\s+\d{1,2}\W*$|\bap\s+credit\b|\bph\.?\s?d\b|\bdoctoral\b|\bmaster\'?s\b|\bpell\b|\brotc\b|yellow\s+ribbon|supplemental\s+educational\s+opportunity|\bseog\b|work[- ]study|\bloans?\b|\bplus\b|'
                            r'college\s+access\s+program|counselor(?!(?:\x27|\u2019)?s?\s+(?:award|scholarship))|director|coordinator|specialist|\bassistant\b|officer|advisor|'
                            r'^(fewer|more|less)\s+than\b|^over\s+\d|\bcredit\s+hours?\b|'
                            r'^\W*(books?|supplies|transportation|personal\s+expenses?|loan\s+fees?|room|board|food)\b|'
                            r'^(reading|english|math(ematics)?|science|writing|composite)$|'
                            r'^(gpa|act|sat|clt|psat|scores?|tiers?|level|amount)$|^(annual\s+)?totals?$', re.I)  # OK (Oklahoma Christian): a header row repeated in the body  # AR: UA-PTC placement score rows  # OR: COA rows
NOT_MERIT_PAGE = re.compile(r'tuition[- ](?:and|&)[- ]fees|international[- ]baccalaureate(?![- ]scholarship)|academicworks|course[- ]awards|\bclep\b|examination[- ]program|(?:private|outside|external)[- ]scholarships?|undocumented|sample[- ]aid[- ]packages?|aid[- ]package[- ]examples?|retention|renewal|keep(?:ing)?[- ]your[- ]scholarship|academic[- ]standards|probation|satisfactory[- ]academic[- ]progress|financial[- ]aid[- ]staff|'
                            r'\bstaff\b|directory|meet[- ]the[- ]team|our[- ]team|'
                            # NY r1: Buffalo State's superseded "scholarships-fall-2024-and-prior" and its faculty awards-recognition page.
                            r'and[- ]prior\b|awards[- ](?:and[- ])?recognition|'
                            # GA r1: lists of other organizations' awards (Agnes Scott outside scholarships, Georgia Southern
                            # military scholarships, West Georgia Tech foundation awards) and international-office waivers (UWG ISAP).
                            r'outside[- ]scholarships?|external[- ]scholarships?|third[- ]party|military|veteran|foundation|/isap/|donor[- ]scholarships?|'
                            r'achievements|recipients|honor[- ]roll|dean.?s[- ]list|/testing/|_credits/|credit[- ]by[- ]exam|'
                            # FL r1: faculty emeriti lists (South Florida), state and federal programs on a college page
                            # (Bright Futures, TEACH Grant) are not institutional merit awards.
                            r'emerit|retirees|bright[- ]futures|/teach\b|teach[- ]grant|\bpell\b', re.I)  # Hampton IB credit table
HEADER_WORDS = re.compile(r'scholarship|award|merit|name|level|tier|amount|value|gpa|act\b|sat\b|criteria|requirement', re.I)
THRESHOLD_CELL = re.compile(r'^\s*[<>≤≥]?\s*\d{1,4}(\.\d{1,2})?\s*(\+|[-–]\s*\d{1,4}(\.\d{1,2})?|(?:or|and)\s+(higher|above|up))?\s*$', re.I)


PLACEHOLDER = re.compile(r'^\W*(n/?a|none|see\s+(?:requirements|criteria|details|below|website)|varies|tbd|-+|—|–)\W*$', re.I)  # ND (Lake Region): an en dash is an empty cell
YES_NO = re.compile(r'\s*(?:yes|no|all|any)\s*', re.I)
PHONE = re.compile(r'\(?\d{3}\)?[\s.-]\d{3}[.-]\d{4}')  # Tougaloo: a contact number in the ACT column is not a score
ENROLLMENT = re.compile(r'^(full|half|part|three[-\s]quarter|3/4)[-\s]time(\s*\([^)]*\))?$|^\d+(\.\d+)?\s+credits?\s+or\s+more$', re.I)  # WY (Northwest): "Full Time (12.0-14.5 credits)", "15.0 credits or more"  # Ole Miss Sumners: amount by enrollment intensity
SCORE = re.compile(r'\b\d{1,4}\b')
PACKAGE_ROW = re.compile(r'federal|pell|state\s+grants?|outside\s+scholarships?|student\s+employment|work[- ]study|\bloans?\b|^total\b', re.I)
_N = r'(?:\d{1,2}|two|three|four|five|six|eight|ten)'
MULTI_YEAR = re.compile(r'(?<!renewable\s)\b(?:for|over|value|maximum\s+of)\s+' + _N + r'\s+(?:fall/spring\s+)?(?:years?|semesters|trimesters|quarters|terms)\b|'
                        r'\b' + _N + r'[\s-]+years?\s+value\b', re.I)  # PA (Penn State campuses): "$26,000 four year value"  # outside parentheses; ND (VCSU "for two year", Minot "maximum of 4 years")
MULTI_X = re.compile(r'\bx\s*' + _N + r'\s+(?:years|semesters|trimesters|quarters|terms)\b|\b' + _N + r'\s+(?:years|semesters|trimesters|quarters|terms)\s+x\b', re.I)
MERGED_GPA = re.compile(r'^(.*?[A-Za-z)])\s*(\d\.\d{1,2}\s*\+?\s*(?:GPA|grade\s+point\s+average)\.?)\s*$', re.I)
MERGED_TEXT = re.compile(r'^(.{3,80}?\b(?:Scholarship|Award|Grant|Fellowship))(?=[A-Z][a-z])')


PAGE_RESIDENCY = re.compile(r'\bout[- ]of[- ]state\b|\bnon[- ]?residents?\b|\bin[- ]state\b', re.I)
# UA: "2027 Out-of-State and International Freshman Automatic Merit Scholarships" names the class entering in fall 2027.
ENTERING_CLASS = re.compile(r'\bfall\s+(20\d{2})\b|\b(20\d{2})\s+(?:in[- ]state\s+|out[- ]of[- ]state\s+|and\s+|international\s+|incoming\s+|entering\s+|first[- ]year\s+)*'
                            r'(?:freshm[ae]n|first[- ]year|incoming|entering)\b', re.I)
STATES = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut',
          'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
          'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
          'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
          'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
          'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
          'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
          'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}

# ------------------------------------------------------------------ academic year of a merit table
# Precedence (owner, 2026-10-22): the table's own heading/caption/lead label; an entering-class statement in that context;
# an explicit page-level aid-year or entering-term statement; the year heading the table sits under; the page's dominant label.
_YEAR = r'20\d{2}\s*(?:-|–|—|/|to)\s*(?:20)?\d{2}'
AID_YEAR_STATEMENT = re.compile(r'\b(?:effective|valid)\s+for\s+(?:the\s+)?(' + _YEAR + r')|\b(' + _YEAR + r')\s+(?:aid|academic|award|scholarship)\s+year\b|'
                                r'\bscholarships?\s+for\s+(?:the\s+)?(' + _YEAR + r')|\bfor\s+incoming\s+(?:freshm[ae]n|first[- ]year\s+students?)\s+(' + _YEAR + r')', re.I)
ENTERING_TERM = re.compile(r'\b(?:enroll(?:s|ing)?|enter(?:s|ing)?|start(?:s|ing)?|begin(?:s|ning)?)\s+(?:\w+\s+){0,3}?(?:summer\s+(?:or|and|/)\s+)?'
                           r'fall\s+(?:semester\s+)?(?:of\s+)?(20\d{2})\b|\beffective\s+(?:for\s+)?(?:the\s+)?fall\s+(?:semester\s+)?(?:of\s+)?(20\d{2})\b', re.I)
STATEMENT_MERIT = re.compile(r'scholarship|merit|\bawards?\b', re.I)
# VA (Lynchburg): "VTAG is currently $5,000 for the 2023-24 academic year" is a state grant's year, not the merit table's.
STATEMENT_OTHER_AID = re.compile(r'fafsa|\bvtag\b|\bpell\b|federal|\bgrants?\b|\bloans?\b|work[- ]study|cost\s+of\s+attendance|need[- ]based|'
                                 r'transfer|\bgraduate\b|tax\s+year|'
                                 # IN (Manchester): "student-athletes enrolling Fall 2027 ... athletic scholarships" dates another program
                                 r'athlet|\bsports?\b|esports|\bband\b|music|theat(?:er|re)|\bchoir\b|\brotc\b|dual[- ]enrollment|summer\s+(?:camp|program|bridge)', re.I)
# MI (Andrews): "Prior to Fall 2023" and TX (LCU): "(1280 beginning Fall 2023)" say when something changed, not who enters
CHANGE_BEFORE = re.compile(r'\b(?:prior\s+to|before|until|through|since|as\s+of|beginning|starting)\s+(?:with\s+|in\s+)?(?:the\s+)?$', re.I)
STATEMENT_FRESHMAN = re.compile(r'freshm[ae]n|first[- ]year|first[- ]time|new\s+students?', re.I)
CURRENT_TERM = re.compile(r'\b(?:fall|spring|summer)\s+(20\d{2})\b', re.I)
LABELED = {'labeled_in_title', 'labeled_in_heading', 'labeled_in_source', 'labeled_in_url'}


def page_year_statement(page, today_year=None):
    """(academic_year, basis) from explicit page statements: an aid-year label ("effective for the 2027-2028 aid year",
    "Merit scholarships for 2026-27") is a printed year label; an entering term ("enroll for Fall 2027") names the entering
    class. Only sentences about scholarships count, and other aid (VTAG, Pell, FAFSA) never does. Disagreeing statements
    give (None, None)."""
    aid, term = set(), set()
    for s in re.split(r'(?<=[.!?])\s+|\n+', page.text[:60000]):
        if STATEMENT_OTHER_AID.search(s): continue
        if STATEMENT_MERIT.search(s):
            for m in AID_YEAR_STATEMENT.finditer(s):
                if re.search(r'\b(?:beginning|since|starting)\s+(?:in\s+)?(?:the\s+)?$', s[:m.start()], re.I) and not \
                        re.search(r'(?:freshm[ae]n|students?|first[- ]years?)\s+(?:beginning|starting)\s+(?:in\s+)?(?:the\s+)?$', s[:m.start()], re.I):
                    continue  # OK (OBU): when a program began; MA (Elms) "for freshmen beginning in the 2024-2025 academic year" is the class
                aid |= set(T.year_labels(next(g for g in m.groups() if g)))
        elif not STATEMENT_FRESHMAN.search(s): continue  # NV (UNR WUE): "Must be a new freshman* starting Fall 2027"
        for m in ENTERING_TERM.finditer(s):
            verb = m.group(0).split()[0].lower()
            if verb.startswith(('begin', 'start')) and not re.search(r'(?:freshm[ae]n|students?|first[- ]years?|class)\W{0,2}\s+(?:who\s+(?:are\s+)?)?$', s[:m.start()], re.I):
                continue  # TX (LCU): "(1280 beginning Fall 2023)" is when a threshold changed; "freshmen beginning in Fall 2027" enter
            if CHANGE_BEFORE.search(s[:m.start()]): continue
            if m.group(2) and today_year and T.academic_year(int(m.group(2))) < today_year:
                continue  # LA (Louisiana Tech): "Category A (effective Fall 2023)" is when a rule began; it is still in force
            term.add(T.academic_year(int(m.group(1) or m.group(2))))
    if len(aid) == 1: return next(iter(aid)), 'labeled_in_source'
    if not aid and len(term) == 1: return next(iter(term)), 'labeled_entering_class'
    return None, None


def current_terms(page, today_year):
    """Fall or spring terms of the current cycle printed outside other programs (VA: Regent's Fall 2026 / Spring 2027 calendar).
    A term in a transfer, grant, athletics or summer-program sentence, or a summer term, says nothing about the merit chart
    (MA: Elms transfer table, OH: JCU legacy grant, CA: UCSC 'Summer 2026')."""
    out = []
    for s in re.split(r'(?<=[.!?])\s+|\n+', page.text[:60000]):
        if STATEMENT_OTHER_AID.search(s): continue
        out += [m.group(0) for m in CURRENT_TERM.finditer(s) if not m.group(0).lower().startswith('summer') and int(m.group(1)) >= int(today_year[:4])
                and not CHANGE_BEFORE.search(s[:m.start()])]
    return out


CLASS_STATEMENT = re.compile(r'\b(?:new|incoming|entering|first[- ]time)\s+(?:\w+\s+){0,3}?(?:students?|freshm[ae]n|first[- ]years?)\s+'
                             r'(?:\w+\s+){0,2}?in\s+(?:the\s+)?(?:fall\s+(20\d{2})\b|(' + _YEAR + r')\s+academic\s+year)|'
                             r'\bbegin\s+attendance\s+in\s+(?:the\s+)?(?:fall\s+(20\d{2})\b|(' + _YEAR + r')\s+academic\s+year)', re.I)


def class_statements(page):
    """Academic years that sentences about the merit awards name for the entering class ("For new incoming students in Fall 2025,
    we offer these awards"; "The above scholarships apply to first-time freshmen ... who begin attendance in the 2025-2026
    academic year"), read even where the sentence also names transfer students. Used only to detect disagreement."""
    out = set()
    for s in re.split(r'(?<=[.!?])\s+|\n+', page.text[:60000]):
        if not STATEMENT_MERIT.search(s) or re.search(r'previous|prior\s+cohort|averages?\b', s, re.I): continue
        for m in CLASS_STATEMENT.finditer(s):
            fall = m.group(1) or m.group(3)
            out |= {T.academic_year(int(fall))} if fall else set(T.year_labels(m.group(2) or m.group(4)))
    return out


FAFSA_REQUIREMENT = re.compile(r'\b(?:complet\w*|submit\w*|fil(?:e|ed|ing)|verif\w*|determined\s+by)\b[^.]{0,40}\bfafsa\b', re.I)
CYCLE_DATE = re.compile(r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?\s+\d{1,2}(?:st|nd|rd|th)?,?\s+(20\d{2})\b', re.I)


def current_cycle(page, today_year):
    """The page prints this cycle's terms or dates (a fall term or a deadline in the current academic year or later). An
    undated merit table on such a page is current-cycle content whose year is unconfirmed; on a page whose only dates are
    old (NY: Alfred State's 2021-22 HEERF page) it is never re-dated as current."""
    start = int(today_year[:4])
    return bool(current_terms(page, today_year)) or any(int(m.group(1)) >= start for m in CYCLE_DATE.finditer(page.text[:60000]))


def merit_text_labels(page):
    """Year labels in the page's text outside sentences and table lines about other aid (FAFSA, Pell, federal or state grants,
    loans, athletics; STATEMENT_OTHER_AID)."""
    def other(s):
        s = re.sub(r'free\s+application\s+for\s+federal\s+student\s+aid', 'FAFSA', s, flags=re.I)
        hits = {m.group(0).lower() for m in STATEMENT_OTHER_AID.finditer(s)}
        if hits <= {'fafsa'} and FAFSA_REQUIREMENT.search(s):
            return False  # OH (Malone): "Completed 2025-26 FAFSA" is an award's requirement and dates that award (ID: "Verifies your 2026-27 FAFSA")
        # MO (SBU): "Freshman & Transfer Scholarships for Fall 2027/Spring 2028" and AL (Stillman) "incoming first-year students,
        # transfers, and current students ... during the 2024-2025 academic year" date first-year awards too
        return bool(hits) and not (hits <= {'transfer'} and STATEMENT_FRESHMAN.search(s))
    return T.year_labels(' '.join(s for s in re.split(r'(?<=[.!?])\s+|\n+', page.text[:60000]) if not other(s)))


def record_year(page, t, year, basis, issues, today_year):
    """(academic_year, basis, issues) for one merit table, by the precedence above."""
    own = ' '.join([t.get('heading') or '', t.get('caption') or '', t.get('lead') or ''])
    clean = [i for i in issues if i != 'ambiguous_year_labels' and not i.startswith('stale_year_label')]
    def done(y, b):
        if b in ('labeled_entering_class', 'labeled_in_heading') and y == year and basis in LABELED: b = basis  # agrees with the page's own label
        # TX (HSUTX): a table led "New Freshmen in Fall 2026" on a page saying the awards are for students who "begin attendance in
        # the 2025-2026 academic year": the page disagrees with itself, so the year is held for review
        other = sorted(class_statements(page) - {y})
        return y, b, clean + ([f'stale_year_label:{y}'] if y < today_year else []) + [f'conflicting_year_statement:{o}' for o in other]
    labels = T.year_labels(own)
    since = {l for m in re.finditer(r'\b(?:effective|beginning|starting|since|as\s+of)\s+(?:in\s+)?(?:the\s+)?(' + _YEAR + ')', own, re.I) for l in T.year_labels(m.group(1))}
    if basis in LABELED and labels and set(labels) <= since and max(labels) < year:
        labels = {}  # PA (Lancaster Bible): "Effective 2024-25, first-time freshmen ..." is when the scale began; the page is labelled 2026-27
    if len(labels) == 1: return done(next(iter(labels)), 'labeled_in_source')
    cls = next((m for m in ENTERING_CLASS.finditer(own) if not CHANGE_BEFORE.search(own[:m.start()])), None) if not labels else None
    cls_year = T.academic_year(int(cls.group(1) or cls.group(2))) if cls else None
    if cls and not (basis in LABELED and cls_year < year):  # MI (Andrews): "Prior to Fall 2023" is not the class the table is for
        return done(cls_year, 'labeled_entering_class')  # the class entering that fall
    stated, stated_basis = page_year_statement(page, today_year)
    # IA (Grand View): one outside award's "for the 2023-2024 academic year" does not re-date a page labelled 2026-27; a statement
    # outranks the page label only when it is not older (KY: Louisville's "entering ... Fall 2027" beside 2026-2027 FAFSA notes)
    if stated and not (basis in LABELED and stated < year): return done(stated, stated_basis)
    under = T.year_labels(t.get('year_heading') or '')
    if len(under) == 1: return done(next(iter(under)), 'labeled_in_heading')
    if basis == 'labeled_in_source' and not merit_text_labels(page) and (year >= today_year or current_cycle(page, today_year)):
        # OH (JCU): the page's only year label is a federal-grant table's "maximum award amounts for 2025-2026"; it never dated
        # the merit table, so the table is unlabeled (held for review), not a 2025-26 award
        return today_year, 'source_unlabeled', clean + [f'page_label_only_in_other_aid:{year}']
    if basis in LABELED and year < today_year and current_terms(page, today_year):
        # VA (Regent): "Aid for 2023-24" statistics and FAFSA notes beside a current chart (Fall 2026 dates) do not date the chart.
        return today_year, 'source_unlabeled', clean + [f'stale_page_label_beside_current_terms:{year}']
    return year, basis, issues


AMOUNT_VARIANT = re.compile(r'resident|commut|in[- ]state|out[- ]of[- ]state|on[- ]campus|off[- ]campus|housing', re.I)


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
    # TN (MTSU): "Amt/Yr" is the annual amount column.
    amount = next((i for words in (('annual', 'per year', 'yearly', 'academic year', 'per academic', '/yr', '/year'), ('amount', 'amt', 'value', '$', 'award detail', 'offer', 'reward'), ('award',))
                   for i, h in enumerate(header) if i != name and any(w in h.lower() for w in words) and not multi_year.search(h)), None)
    money_cols = [i for i, h in enumerate(header) if i != name and body and not multi_year.search(h)
                  and sum(1 for r in body if i < len(r) and T.money_values(r[i])) >= 0.8 * len(body)]
    if amount is None:  # ND (Jamestown): "Scholarship | GPA | (blank)" with the amounts under the blank header
        amount = next((i for i in money_cols if not header[i].strip()), None)
    # VA (UMW in-state): "In-State Residential | In-State Commuter" - two amount columns, each named by its header
    amount_cols = money_cols if amount is None and len(money_cols) > 1 and all(AMOUNT_VARIANT.search(header[i]) for i in money_cols) else []
    # OH (Ashland): 'Student Aid Index (SAI)' and 'Renewal GPA' columns hold dollars too, but they are not amount variants
    gpa = _col(header, 'gpa', 'grade point')
    act = _col(header, 'act')
    sat = _col(header, 'sat')
    clt = _col(header, 'clt')
    combined = act if act is not None and act == sat else None  # VA (UMW): "Min. SAT/ACT* | 1300/27" is one cell for both tests
    if combined is not None: act = sat = None
    test = combined if combined is not None else None if (act is not None or sat is not None) else _col(header, 'test', 'superscore', 'score')
    renewal = _col(header, 'renew', 'retain', 'retention', 'maintain', 'to keep')
    criteria = next((i for i, h in enumerate(header) if i != renewal and re.search(r'requirement|criteria|eligib|qualif|\bpoints?\b', h, re.I)), None)
    if criteria in (name, amount, gpa, act, sat, test): criteria = None
    if gpa is not None and gpa in (act, sat, combined):  # one column holds "21-22 ACT / 1060-1120 SAT or 3.00-3.24 GPA"
        test, gpa, act, sat, combined = gpa, None, None, None, None
    if clt in (name, gpa, act, sat, test, criteria): clt = None
    if name is None: name = 0
    body, inherited = _fill_spans(header, body, name)
    used = {i for i in (name, amount, gpa, act, sat, clt, test, criteria, renewal) if i is not None} | set(amount_cols)
    if criteria == name: criteria = None  # the threshold column is the row label (tier rows below)
    # UTK In-State Volunteer: "ACT / SAT | Annual Award" - the score column labels the rows, the page names the award.
    threshold_cols = sorted({i for i in (gpa, act, sat, test, clt) if i is not None}) if name in (gpa, act, sat, test) else []
    threshold_label = bool(threshold_cols)
    gpa_col, clt_col = gpa, clt
    if threshold_label: gpa, act, sat, test, clt = None, None, None, None, None  # every threshold column labels the row instead (TX: UD's CLT too)
    clean = lambda h: h.strip().strip('*').strip()
    if amount is None and gpa is None and act is None and sat is None and test is None and criteria is None: return []
    out, section = [], ''
    for ri, row in enumerate(body):
        if name > 0 and len(row) < len(header): continue  # AR (UCA): merged cells shifted this row; its columns no longer line up
        cells = list(row) + [''] * (len(header) - len(row))
        nxt = body[ri + 1][name].strip() if ri + 1 < len(body) and name < len(body[ri + 1]) else ''
        if out and re.fullmatch(r'\s*(?:or|and)(?:\s+(?:or|and))*\s*', ' '.join(row), re.I) and re.fullmatch(r'[\d.+\s]*', nxt):  # UTK: 'OR' between named tier rows
            # OK (Oklahoma Christian): "or" then "3.5 | No Score Required" - an alternative path printed under a row; which award it
            # belongs to is a layout reading, so the award above is held for review
            out[-1][0]['_issues'] = out[-1][0].get('_issues', []) + ['alternative_criteria_row']
            continue
        nm = cells[name].strip()
        if not nm or len(nm) > 120 or T.money_values(nm) or PLACEHOLDER.match(nm): continue  # CT (WCSU): 'Varies' is not a name
        if threshold_label and not re.search(r'\d', nm): continue  # "OR" between tier rows
        if not threshold_label and (NOT_NAME.search(nm) or NOT_AWARD_NAME.search(nm)): continue
        if nm.endswith(':') or len(nm.split()) > 12: continue  # worked examples and sentences, not award names
        get = lambda i: cells[i].strip() if i is not None and i < len(cells) else ''
        # TX (South Texas College) "GPA: Yes/No", (Texas Southmost) "All", (Texas State) contact e-mail cells are not criteria
        amt, g, a, s, tst, crit, ren, cl = (x if not (PLACEHOLDER.match(x) or PHONE.search(x) or '@' in x or YES_NO.fullmatch(x)) else '' for x in (get(amount), get(gpa), get(act), get(sat), get(test), get(criteria), get(renewal), get(clt)))
        if amount_cols:
            amt = '; '.join(f'{clean(header[i])}: {get(i)}' for i in amount_cols if get(i) and not PLACEHOLDER.match(get(i)))
        split = amount_cols and len({'out' if re.search(r'out[- ]of[- ]state|non[- ]?res', header[i], re.I) else 'in' for i in amount_cols}) > 1
        if combined is not None and SCORE.search(tst) and not re.search(r'\b(act|sat)\b', tst, re.I):
            tst = f'{clean(header[combined])}: {tst}'  # the header says which number is which test
        nm, merged_gpa = _split_name(nm)
        if merged_gpa and not g: g = merged_gpa
        if not (amt or g or a or s or tst or crit):
            if sum(1 for c in cells if c.strip()) == 1 and not threshold_label: section = nm  # "Alabama Residents" above its rows
            continue
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
        per_year = re.search(r'\(\s*\$\s?([\d,]+)\s*(?:per|/|a|each)\s*(?:year|yr)\s*\)', amt, re.I)
        if per_year and hi is not None and int(per_year.group(1).replace(',', '')) < hi:
            lo = hi = int(per_year.group(1).replace(',', ''))  # PA (Geneva): "$70,000 ($17,500 per year)" is $17,500 a year
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
            rec['award_name'] = f"{title}: " + ', '.join(f'{clean(header[i])} {v}' for i, v in parts if i != clt_col)  # names stay as before CLT was read
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
        if split:  # WV (Shepherd), VA (UMW test-optional): one column per residency - no single range spans both
            lo = hi = None; rec['_issues'] = rec.get('_issues', []) + ['amount_by_residency']
        if hi is not None:
            if lo is not None: rec['award_min'] = lo
            if not rec_open_max: rec['award_max'] = hi
        if g: rec['gpa_requirement'] = g
        # Prefix only bare scores: "ACT: 27+ / SAT: 1220+" already names the test, "Valedictorian" is not a score (Tougaloo).
        label = lambda name, v: f'{name} {v}' if v and SCORE.search(v) and not re.search(r'\b(act|sat)\b', v, re.I) else v
        clt_label = f'CLT {cl}' if cl and SCORE.search(cl) and not re.search(r'\bclt\b', cl, re.I) else cl  # OK (Oklahoma Christian)
        tests = ' / '.join(x for x in [label('ACT', a), label('SAT', s) if s != a else '', clt_label] if x) or tst
        if tests and not re.search(r'\d', tests) and test is not None and re.search(r'requirement|criteria|eligib', header[test], re.I):  # MI (Madonna): "Parent/Grandparent is a Madonna alumna" under a GPA/ACT/SAT header
            if not crit: rec['eligibility_summary'] = tests[:600]
        elif tests: rec['test_requirement'] = tests
        if crit:  # a bare points range is meaningless without its column name (Southern: "Points | 4,800 - 5,700")
            rec['eligibility_summary'] = (f"{header[criteria].strip()}: {crit}" if re.search(r'\bpoints?\b', header[criteria], re.I) else crit)[:600]
        if ren: rec['renewal_requirements'] = ren[:600]
        thresholds = {k: v for k, v in {'gpa_min': _num(g, 0, 5, True), 'act_min': _num(a, 1, 36), 'sat_min': _num(s, 400, 1600)}.items() if v is not None}
        if thresholds: rec['thresholds'] = thresholds
        if any(re.fullmatch(r'\s*(or|and|&)\s*', c, re.I) for c in cells):
            rec['_issues'] = ['threshold_logic_column']  # AR (ATU): an "or"/"&" column says whether GPA and test are both required
        if section:
            rec['_section'] = section
            res = PAGE_RESIDENCY.search(section)
            if res: rec['residency_requirement'] = 'Out-of-state' if re.search(r'out|non', res.group(0), re.I) else 'In-state'
        rec['_tier'] = {k: v for k, v in (('test', tst), ('act', a), ('sat', s), ('clt', cl), ('gpa', g), ('criteria', crit), ('amount_text', amt)) if v}
        rec['_rest'] = tuple(cells[i] for i in range(len(header)) if i not in used and not multi_year.search(header[i]))
        if any(cells[i].strip() for i in inherited[ri] & used):
            rec['_issues'] = rec.get('_issues', []) + ['merged_cell_inferred']  # a field comes from a cell this row did not print
        out.append((rec, ' | '.join(c for i, c in enumerate(cells) if i not in inherited[ri])))
    if threshold_label: labels = {}
    else: labels = {'test': '' if combined is not None else clean(header[test]) if test is not None else '', 'act': 'ACT', 'sat': 'SAT', 'clt': 'CLT',
                    'gpa': clean(header[gpa]) if gpa is not None else 'GPA', 'criteria': '', 'amount_text': ''}
    return _group_rows(out, labels) if labels else [(_drop_private(r), raw) for r, raw in out]


# TX (Dallas Institute): "February 15 - April 16" is a date window, not an award name, even without a year
MONTH_DAY = re.compile(r'\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?\s+\d{1,2}\b', re.I)


def _kind(c):
    c = (c or '').strip()
    if not c: return 'empty'
    if re.fullmatch(r'\$\s?[\d,]+(?:\.\d\d)?\s*\**', c): return 'money_only'
    if T.money_values(c): return 'money'
    if re.search(r'\d\.\d', c): return 'gpa'  # AR (UCA): "Minimum 3.75 ... GPA ... Apply online beginning September 1" is a GPA cell
    if MONTH_DAY.search(c): return 'date'
    if re.fullmatch(r'[\d\s,+/–-]+', c): return 'number'  # a score band ("33–34")
    return 'text'


CRITERIA_HEADER = re.compile(r'\b(?:act|sat|clt|gpa|test|score|criteria|requirement)', re.I)


def _filled(row):
    return sum(bool(c.strip()) for c in row)


def group_label_row(rows, spanned=False):
    """True when rows[0] is a group label printed above the real header (OK, Oklahoma Christian: "Minimum Scores of Recipient"
    over GPA | ACT | SAT). On the printed grid a spanning label is padded to full width, so it is told apart by how many cells
    it fills, not by its length (#273 review)."""
    if len(rows) > 3 and len(rows[0]) == len(rows[1]) == 2 and _filled(rows[0]) == 1 and _filled(rows[1]) == 2 and rows[0][0].strip() \
            and all(HEADER_WORDS.search(c) for c in rows[1]):
        return True  # MI (Andrews): "Current Amounts" above "GPA | ANNUAL AMOUNT"
    if not (len(rows) > 3 and len(rows[0]) >= 2 and _filled(rows[0]) <= 2 and not re.search(r'\d', ' '.join(rows[0])) and len(rows[1]) >= 3):
        return False
    if len(rows[1]) > len(rows[0]): return True
    # padded to the grid's width (only when rows[0] holds a cell merged across columns - a real header with a blank column
    # is not a label: ND, Jamestown "Scholarship | GPA | (blank)"); a lone title in the first column is the table's title, not a group label (AR: UA-PTC)
    return spanned and len(rows[1]) == len(rows[0]) and _filled(rows[1]) > _filled(rows[0]) and not (_filled(rows[0]) == 1 and rows[0][0].strip())


def spans_criteria(t):
    """'cell_spans_criteria_columns' when a body cell is merged across columns and one of the columns it covers is a criterion
    column (ACT, SAT, GPA, test) where that text would take a criterion's label: the printed grid keeps the text in the first
    column, so its label there is a guess (#273 review:
    '3.0 GPA' across ACT | GPA must not read as an ACT criterion). A row that is one cell across the whole table (a section
    label such as "Alabama Residents", or a footnote) labels nothing and is not counted; a group label above the header is
    not the header."""
    grid = T.expand_spans(t)
    if not grid: return None
    head = 1 if group_label_row(grid, any(ri == 0 for ri, _, _ in T.wide_cells(t))) and HEADER_WORDS.search(' '.join(grid[1])) else 0
    header = grid[head]
    for ri, col, cs in T.wide_cells(t):
        if ri <= head: continue
        if col == 0 and cs >= len(header): continue  # the whole row is one cell: a section or footnote row
        crit = [j for j in range(col, min(col + cs, len(header))) if CRITERIA_HEADER.search(header[j])]
        # the text sits in the first column; it is mislabelled when that column is a criterion, or when it covers two criteria
        # (a name cell running into the ACT column, as in "Award C (see Honors College)", is still a name)
        if col in crit or len(crit) > 1:
            return 'cell_spans_criteria_columns'
    return None


def _fill_spans(header, body, name):
    """AR (UCA): cells merged down several rows (rowspan) are printed once, so later rows are short and their cells shift left.
    A short row is re-aligned only when exactly one placement fits every cell to its column's kind (text, GPA, amount, date as
    seen in the full rows), preferring placements that keep the row's own award name; the merged cells take the value of the row above.
    Archived pages lost the rowspan/colspan markup, so which cells were merged is an inference: (rows, inherited) where inherited[i]
    holds the columns of row i that were not printed in that row. Evidence quotes only printed cells, and a record whose fields use
    an inherited cell is held for review (CA: Skyline "TastyPlacement | All Students" printed no amount)."""
    width = len(header)
    full = [r for r in body if len(r) == width]
    if not full or all(len(r) >= width for r in body): return body, [frozenset()] * len(body)
    col_kind = [Counter(_kind(r[i]) for r in full).most_common(1)[0][0] for i in range(width)]
    out, prev, inherited = [], None, []
    for r in body:
        if len(r) >= width or prev is None or len(r) * 2 < width:  # at least half the row must be its own
            out.append(r); inherited.append(frozenset())
            if len(r) == width: prev = r
            continue
        fits = [keep for keep in itertools.combinations(range(width), len(r)) if all(_kind(c) == col_kind[i] for c, i in zip(r, keep))]
        named = [keep for keep in fits if name in keep]
        # AL (Auburn): "33–34 | $15,000" continues the award above it (its name and GPA are merged down); a row may inherit the
        # name only when it prints a criterion and no text of its own (KS: Barclay "Technology Fee ($30 per credit) | $720")
        continues = any(_kind(c) in ('number', 'gpa') for c in r) and not any(_kind(c) == 'text' for c in r)
        fits = named or (fits if continues else [])
        if len(fits) != 1:
            out.append(r); inherited.append(frozenset()); continue
        filled = list(prev)
        for c, i in zip(r, fits[0]): filled[i] = c
        out.append(filled); prev = filled
        inherited.append(frozenset(range(width)) - set(fits[0]))
    return out, inherited


def _level_grid(t, rows, page):
    """NV (UNR): GPA rows x ACT columns (with an SAT row under the ACT header) whose cells name the award level
    ("3.9 GPA, ACT 33, SAT 1450: Presidential"). One record per level; each tier copies the row and column headers.
    The amount is the one the cells print for that level ("Presidential Level $10,000/year") or, when no cell prints it,
    the page's legend ("LUNA $750 /year"); conflicting or missing amounts are left out."""
    h = rows[0]
    if not re.fullmatch(r'\s*(ACT|SAT)\b[^\d]*', h[0], re.I) or sum(bool(re.fullmatch(r'\s*\d{2,4}\s*', c)) for c in h[1:]) < 3: return []
    heads, body = [h], rows[1:]
    if body and re.fullmatch(r'\s*(ACT|SAT)\b[^\d]*', body[0][0], re.I) and len(body[0]) == len(h): heads, body = [h, body[0]], body[1:]
    grid = [r for r in body if len(r) == len(h) and re.fullmatch(r'\s*\d\.\d{1,2}\s*\+?\s*', r[0])]
    if len(grid) < 3 or len(grid) < len(body) - 1: return []
    levels = {}
    for r in grid:
        for i, c in enumerate(r[1:], 1):
            cell = c.rsplit(':', 1)[-1].strip()
            amt = re.search(r'\$\s?[\d,]+\s*(?:/\s*(?:year|yr))?', cell)
            nm = re.sub(r'\s+level$', '', re.sub(r'\s*\$.*$', '', cell), flags=re.I).strip()
            if not nm: continue
            if re.search(r'\d', nm) or len(nm) > 60: return []  # not an award-level grid
            lv = levels.setdefault(nm, {'tiers': [], 'amounts': [], 'cells': []})
            lv['tiers'].append({'gpa': r[0].strip(), **{hh[0].strip().lower(): hh[i].strip() for hh in heads}})
            if amt: lv['amounts'].append(amt.group(0).strip())
            lv['cells'].append(c)
    if len(levels) < 2: return []
    title = (t.get('heading') or t.get('caption') or 'Merit scholarship matrix').strip()
    tests = ' / '.join(hh[0].strip() for hh in heads)
    required = re.search(r'\bACT\s+OR\s+SAT\s+(?:IS\s+)?REQUIRED\b', page.text, re.I)  # NV (UNR): "ACT OR SAT REQUIRED"
    open_to = re.search(r'\b(?:[Oo]pen|[Aa]vailable|[Ll]imited)\s+to\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\s+residents\b', page.text)  # "Open to Nevada residents"
    out = []
    for nm, lv in levels.items():
        amounts, source = lv['amounts'], 'cell'
        if not amounts:
            amounts = [m.group(1).strip() for m in re.finditer(rf'(?<![\w.]){re.escape(nm)}\s*\(?\s*(\$\s?[\d,]+\s*/\s*(?:year|yr))', page.text, re.I)]
            source = 'legend'
        if len({T.money_values(a)[0] for a in amounts}) == 1:
            amounts = amounts[:1]  # "$750 /year" and "($750/yr)" print one amount: the first as printed
        rec = {'award_name': nm, 'award_type': 'institutional_merit', 'award_tiers': lv['tiers'],
               'test_requirement': f"Tiers by {t.get('lead') or 'GPA'} (rows) and the {tests} column headers in the table '{title}'"
                                   + (f" (page: '{required.group(0)}')" if required else '') + f": {len(lv['tiers'])} qualifying combinations listed in award_tiers",
               'eligibility_summary': f'Listed under: {title}'}  # NV (UNR): the matrix label says who it is for ("... for WUE recipients")
        issues = []
        if len(amounts) == 1:
            a = next(iter(amounts)); v = T.money_values(a)[0]
            rec.update(award_amount_text=a, award_min=v, award_max=v)
        else:
            issues.append('level_amount_not_found' if not amounts else 'level_amount_conflict')
        if issues: rec['_issues'] = issues
        if open_to: rec['_open_to'] = open_to.group(1)
        raw = f'{title}: ' + ' | '.join(lv['cells'][:6]) + (f' (amount from the page legend: {nm} {next(iter(amounts))})' if source == 'legend' and len(amounts) == 1 else '')
        out.append((rec, raw))
    return out


def _drop_private(rec):
    for k in ('_tier', '_rest', '_section'): rec.pop(k, None)
    return rec


def _group_rows(out, labels):
    """AL (UAH, UA, UAB): one award printed on several rows, each with its own test-score and GPA pairing (and sometimes its own
    amount) -> one record whose award_tiers keep every row as printed. Keeping only the first row would misstate eligibility."""
    by = {}
    for rec, raw in out: by.setdefault((rec['award_name'], rec.get('_section', '')), []).append((rec, raw))  # one award per printed section
    merged = []
    sections = Counter(name for name, _ in by)
    for (name, sec), grp in by.items():
        if sections[name] > 1 and sec:  # one name under two sections of the table ("Alabama Residents" / "Non-Residents")
            for r, _ in grp: r['award_name'] = f'{name} ({sec})'
        if len(grp) == 1 or not all(set(r['_tier']) - {'amount_text'} for r, _ in grp) or len({json.dumps(r['_tier'], sort_keys=True) for r, _ in grp}) == 1:
            merged.extend((_drop_private(r), raw) for r, raw in grp); continue  # AL (Wallace State): repeated names without criteria are not tiers
        recs = [r for r, _ in grp]
        tiers = [r['_tier'] for r in recs]
        rec = {k: v for k, v in recs[0].items() if k in ('award_name', 'award_type', 'residency_requirement')}
        rec['award_tiers'] = tiers
        cols = [k for k in ('test', 'act', 'sat', 'clt', 'gpa', 'criteria') if any(k in t for t in tiers)]
        text = '; '.join(', '.join(f'{labels[k]} {t[k]}'.strip() for k in cols if t.get(k)) + (f" → {t['amount_text']}" if t.get('amount_text') else '')
                         for t in tiers)
        heads = ' and '.join(labels[k] for k in cols if labels[k]) or 'row'
        key = 'test_requirement' if any(k in cols for k in ('test', 'act', 'sat', 'clt')) else 'gpa_requirement' if 'gpa' in cols else 'eligibility_summary'
        rec[key] = f'Tiers by {heads}: {text}'[:2000]
        amounts = list(dict.fromkeys(t['amount_text'] for t in tiers if t.get('amount_text')))
        if amounts: rec['award_amount_text'] = '; '.join(amounts)
        if all(r.get('award_max') is not None and r.get('award_min') is not None for r in recs):
            rec['award_min'], rec['award_max'] = min(r['award_min'] for r in recs), max(r['award_max'] for r in recs)
        for k in ('renewable', 'renewal_requirements'):
            if len({json.dumps(r.get(k)) for r in recs}) == 1 and recs[0].get(k) is not None: rec[k] = recs[0][k]
        issues = sorted({i for r in recs for i in r.get('_issues', [])})
        if len({r['_rest'] for r in recs}) > 1:
            issues.append('multi_row_award_extra_column')  # another column also varies between the rows; the tiers do not show it
        crit = {}
        for t in tiers: crit.setdefault(json.dumps({k: v for k, v in t.items() if k != 'amount_text'}, sort_keys=True), set()).add(t.get('amount_text'))
        if any(len(v) > 1 for v in crit.values()):
            issues.append('tier_criteria_repeat')  # the same criteria print two amounts: an unread column or section tells them apart
        if issues: rec['_issues'] = issues
        merged.append((rec, ' || '.join(raw for _, raw in grp)))
    return merged


def _tier_award(t, header, body, context):
    """One threshold column and one amount column: 'GPA | Merit', '3.0 | $14,000'."""
    if len(header) == 3 and re.search(r'4[\s-]*years?|four[\s-]*years?', header[2], re.I): header = header[:2]  # AL (JSU): a 4-year total column
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
    if any(len(r) != len(header) for r in gpa_rows): return []  # SD (SDSU): rows shifted under a two-row header would mislabel every tier
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


# A heading that says what the table is about but names no award (AL: South Alabama "Qualifications:", VA: VCU "Eligibility
# criteria"); the page title names the program instead.
GENERIC_HEADING = re.compile(r'\s*(?:qualifications?|eligibility(?:\s+(?:criteria|requirements))?|criteria|requirements|award\s+(?:tiers|amounts?|levels)|'
                             r'amounts?|award\s+grid|scholarship\s+grid|merit\s+scholarship\s+grid|merit\s+scholarship\s+tiers)\s*:?\s*', re.I)
GPA_BAND_HEADER = re.compile(r'(?:\bgpa\b[^|]*\d\.\d|\d\.\d[^|]*\bgpa\b|^\s*(?:gpa\s*)?[<>≥≤=]?\s*\d\.\d{1,3}\s*(?:\+|[-–]\s*\d\.\d{1,3}|&\s*higher|and\s+(?:above|higher))?\s*$)', re.I)
RANK_HEADER = re.compile(r'\btop\s+\d{1,2}\s*%', re.I)
SCORE_LABEL = re.compile(r'\b(?:act|sat|clt|test|scores?)\b', re.I)
SCORE_BAND = re.compile(r'\d{2}|\bno\s+(?:test|score)|without\s+(?:a\s+)?(?:test|score)|submitted\s+scores|test[\s-]*optional', re.I)


def _score_row_grid(t, header, body, context, page=None):
    """Test-score x GPA (or class rank) matrix with score bands down the side: AL (South Alabama) "ACT | SAT | High School GPA
    3.0-3.49 | ...", LA (Louisiana Tech) "Scholarship Name: ACT / SAT Score | GPA 3.0-3.749 | GPA 3.75-4.0", MI (GVSU) "SAT / ACT
    Scores | GPA = 3.3 - 3.49 | ...", TX (Tarleton) "SAT, ACT, or CLT | top 10% | ...". One award; each printed amount cell is a
    tier. A row that does not fill every column, or a cell that is neither an amount nor blank, leaves the table unread."""
    gpa = [i for i, h in enumerate(header) if i and GPA_BAND_HEADER.search(h)]
    rank = [i for i, h in enumerate(header) if i and RANK_HEADER.search(h)]
    crit, kind = (gpa, 'gpa') if len(gpa) >= 2 else (rank, 'class rank') if len(rank) >= 2 else ([], None)
    if not crit or crit != list(range(crit[0], crit[0] + len(crit))) or crit[-1] != len(header) - 1: return []
    lead = list(range(crit[0]))
    if not SCORE_LABEL.search(' '.join(header[i] for i in lead)): return []
    tiers, evidence_rows = [], []
    for r in body:
        if not any(c.strip() for c in r): continue
        if len(r) != len(header): return []
        if not all(SCORE_BAND.search(r[i]) for i in lead if r[i].strip()) or not any(r[i].strip() for i in lead): return []
        parts = []
        for i in lead:
            c, h = r[i].strip(), header[i].strip()
            if not c: continue
            parts.append(c if re.search(r'\b(?:act|sat|clt)\b', c, re.I) or not re.fullmatch(r'(?i)act|sat|clt', h) else f'{h.upper()} {c}')
        label = ' / '.join(parts)
        for i in crit:
            c = r[i].strip()
            if not c or re.fullmatch(r'(?i)n/?a|none|[-–—]+|not\s+eligible[^|]{0,60}', c): continue  # LA (Louisiana Tech): "N/A" is no award there
            if not (T.money_values(c) or re.search(r'tuition|full\s+ride|cost\s+of\s+attendance', c, re.I)): return []
            tiers.append({'test': label, kind: header[i].strip(), 'amount_text': c})
        evidence_rows.append(' | '.join(r))
    if len(evidence_rows) < 2 or len(tiers) < 4: return []
    amounts = [v for tier in tiers for v in T.money_values(tier['amount_text'])]
    if not amounts: return []
    title = (t.get('heading') or t.get('caption') or '').strip().lstrip('+-–•*› ').strip() or 'Merit scholarship grid'
    lead_label = ' / '.join(h.strip() for h in (header[i] for i in lead) if h.strip()) or 'test score'
    rec = {'award_name': title[:120], 'award_type': 'institutional_merit', 'award_tiers': tiers,
           'test_requirement': f'Tiers by {lead_label} and {kind}: ' + '; '.join(f"{x['test']}, {x[kind]} → {x['amount_text']}" for x in tiers),
           'award_min': min(amounts), 'award_max': max(amounts)}
    if kind == 'gpa': rec['gpa_requirement'] = 'Tiers by GPA: ' + '; '.join(header[i].strip() for i in crit)
    return [(rec, ' || '.join([' | '.join(header)] + evidence_rows))]


def table_footnotes(page, header, rows):
    """Footnotes a header points to with asterisks, copied as printed from the lines after the table: VA (Lynchburg) 'Minimum
    GPA* to qualify' -> '*Weighted GPA is used to determine scholarship eligibility...', FL (UNF) 'Amount (per year)*' -> '*The
    amounts are based on 30 credit-hour enrollment'. Only the first matching line after the table counts."""
    marks = sorted({len(m.group(0)) for h in header for m in re.finditer(r'\*+', h)})
    if not marks or not rows: return []
    last = next((c.strip() for c in reversed(rows[-1]) if c.strip()), '')
    start = page.text.find('| ' + header[0].strip()) if header[0].strip() else -1
    end = page.text.find(last, max(start, 0)) if last else -1
    if end < 0: return []
    tail = page.text[end:end + 2000]
    out = []
    for n in marks:
        m = re.search(r'^\s*(\*{' + str(n) + r'}(?!\*)\s*\S.{2,300}?)\s*$', tail, re.M)
        if m: out.append(m.group(1).strip())
    return out


def extract(inst, entry, page, today_year):
    if not page.tables or common.professional_source(entry, page) or common.international_source(entry, page): return []
    if not SCHOLARSHIP_CONTEXT.search(page.title + ' ' + ' '.join(page.headings[:6]) + ' ' + entry.get('url', '')):
        return []
    if NOT_MERIT_PAGE.search(page.title + ' ' + entry.get('url', '')): return []
    if re.search(r'(?:^|[-–|:]\s*)loans?\s*$', page.title, re.I): return []  # WI (UW-Platteville): a loans page's borrowing limits
    if re.search(r'transfer', entry.get('url', '') + ' ' + page.title, re.I) and not re.search(r'freshm[ae]n|first[- ]year', page.title, re.I):
        return []  # first-year merit only; transfer awards are a separate category (KS: KU "Merit Awards for Freshmen & Transfers" is both)
    mixed_transfer = bool(re.search(r'transfer', entry.get('url', '') + ' ' + page.title, re.I))
    year, basis, issues = common.resolve_year(page, entry, today_year)
    out, printed = [], {}
    for t in page.tables:
        grid = T.expand_spans(t)
        rows = [r for r in (grid or t['rows']) if any(c.strip() for c in r)]  # the printed grid when spans were recorded
        span_issue = spans_criteria(t)
        if len(rows) < 3: continue
        context = ' '.join([t.get('heading') or '', t.get('caption') or ''])
        if NOT_MERIT.search(context): continue
        if re.match(r'\s*(?:for\s+)?transfers?\b(?:\s+students?)?\s*:?\s*$', t.get('lead') or '', re.I): continue  # OR (PSU): the "Transfer" grid beside "First Year"
        if re.match(r'\s*(?:prior\s+to|before|until)\s+(?:the\s+)?(?:fall|spring|summer)?\s*(?:semester\s+)?(?:of\s+)?20\d{2}\b', ' '.join([t.get('heading') or '', t.get('lead') or '']).strip(), re.I) \
                and not re.search(r'current', ' '.join(rows[0]), re.I):
            continue  # MI (Andrews): a table headed "Prior to Fall 2023" lists superseded amounts, never a current award
        scope_test = None
        if len(rows) > 3 and _filled(rows[0]) == 1 and (len(rows[0]) == 1 or t.get('spans')) and re.search(r'\d{2}', rows[0][0]) and re.search(r'\b(act|sat)\b', rows[0][0], re.I) and len(rows[0][0]) <= 80:
            scope_test, rows = rows[0][0], rows[1:]  # AL (JSU): "26-28 ACT or 1230-1320 SAT" above a GPA | amount table applies to every row
        header, body = rows[0], rows[1:]
        if group_label_row(rows, any(rows[0] is grid[ri] for ri, _, _ in T.wide_cells(t)) if grid else False) and HEADER_WORDS.search(' '.join(rows[1])) and not any(T.money_values(c) for c in rows[1]) \
                and sum(len(r) > len(rows[1]) for r in rows[2:]) <= 1:
            header, body = rows[1], rows[2:]  # OK (Oklahoma Christian): a spanning group label ("Minimum Scores of Recipient") above the header
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
        # VA (VCU): "Eligibility criteria" heads a GPA grid; under such a heading only a tier grid is read (NY: Brockport's Excelsior
        # "Eligibility" lists student groups, not awards)
        eligibility_heading = bool(re.fullmatch(r'(?i)\s*eligibility(?:\s+criteria|\s+requirements)?\s*:?\s*', context))
        if NOT_MERIT.search(' '.join(header)) or (NOT_NAME.search(context) and not eligibility_heading): continue
        if any(len(c) > 60 for c in header): continue  # a sentence is not a header row (APSU: "Freshmen | Qualifying freshmen have ...")
        if len(header) == 2 and re.fullmatch(r'\s*(requirements?|criteria|items?|attributes?|details?)\s*', header[0], re.I):
            continue  # key/value facts about one award (UTK: "Requirement | Details", "FAFSA Required | No")
        if re.search(r'\bcollege\s+gpa\b', ' '.join(header), re.I): continue  # college-GPA tiers are transfer awards (CBU)
        if not HEADER_WORDS.search(' '.join(header)): continue  # e.g. worked aid examples, schedules
        shaped = _level_grid(t, rows, page) or _tier_award(t, header, body, context) or _grid_award(t, header, body, context) \
            or _score_row_grid(t, header, body, context, page)
        if scope_test:
            if not (shaped and 'award_tiers' in shaped[0][0] and 'test_requirement' not in shaped[0][0]): continue
            shaped[0][0]['test_requirement'] = scope_test
            shaped = [(shaped[0][0], f'{scope_test} || {shaped[0][1]}')]
        merit_context = re.search(r'merit|academic|gpa|act|sat|test score', context + ' ' + ' '.join(header) + ' ' + page.title, re.I)
        award_type = 'institutional_merit' if merit_context else 'institutional_other'
        named = re.sub(r'\bawards?\s+amounts?\b', '', context, flags=re.I)  # "Award Amounts" is a heading, not a name (UTK)
        label = context.strip() if re.search(r'scholarship|award|grant|fellowship', named, re.I) else (_page_award_name(page) or context.strip() or page.title)
        label = label.strip().lstrip('+-–•*› ').strip()  # "+Scholarships" (Thomas University): an accordion icon, not the name
        found = shaped or ([] if eligibility_heading else _list_awards(t, header, body, label[:80], award_type))
        # IA (Graceland): a sample aid package lists federal/state grants, outside scholarships and work beside the award
        if sum(1 for r in body if r and PACKAGE_ROW.search(r[0])) >= 2: continue
        # MO (Southwest Baptist): the same heading over a different table is another year's version; which is which is unclear
        twins = [o for o in page.tables if o is not t and (o.get('heading') or '') == (t.get('heading') or '') and o.get('heading')
                 and o.get('rows') and o['rows'][0] == t['rows'][0] and o['rows'] != t['rows']]
        if not found or (not shaped and len(found) < 2 and not found[0][0].get('award_tiers')): continue  # one stray row is not a scholarship table
        # (IN: Marian Scholar, VT: Champlain - one award printed on several tier rows is a table)
        rec_year, rec_basis, rec_issues = record_year(page, t, year, basis, issues, today_year)
        notes = table_footnotes(page, header, rows)
        for rec, raw in found:
            if mixed_transfer and re.search(r'transfer|athlet', rec['award_name'], re.I):
                continue  # MO (Avila): a first-year-and-transfer page; transfer and athletic awards are other categories
            row_issues = rec.pop('_issues', []) + (['duplicate_table_versions'] if twins else [])
            if shaped and GENERIC_HEADING.fullmatch(rec['award_name'] or ''):  # never a real award name (AL: JSU "Gamecock Tradition")
                head = re.split(r'\s+[-|–—]\s+', page.title or '')[0].strip()  # VA (VCU): a grid headed "Eligibility criteria"
                if re.search(r'scholarship|award|grant|merit', head, re.I) and len(head) <= 80: rec['award_name'] = head
            if notes and not shaped: rec['footnotes'] = notes
            ev = [{'field': k, 'value': v, 'snippet': raw[:300]} for k, v in rec.items()
                  if k in {'award_amount_text', 'gpa_requirement', 'test_requirement', 'award_tiers', 'eligibility_summary', 'renewal_requirements'}]
            ev += [{'field': 'footnotes', 'value': n, 'snippet': n} for n in rec.get('footnotes', [])]
            if not ev: continue
            res = PAGE_RESIDENCY.search(page.title + ' ' + context)
            if res and 'residency_requirement' not in rec:  # "In-State Freshman Scholarships" (AL: UAB has same-named awards per residency)
                rec['residency_requirement'] = 'Out-of-state' if re.search(r'out|non', res.group(0), re.I) else 'In-state'
            home = STATES.get(inst.get('state') or '')
            if home and 'residency_requirement' not in rec and re.search(rf'(?<!non-)(?<!non )(?<!west )(?<!west-)\b{home}\s+residents?\b', page.title + ' ' + context, re.I):
                rec['residency_requirement'] = 'In-state'  # FL (UNF): "Florida Resident Merit-Based (Freshmen)"
            open_to = rec.pop('_open_to', None)
            if open_to and home and open_to == home and 'residency_requirement' not in rec:
                rec['residency_requirement'] = 'In-state'  # NV (UNR): the matrix page says "Open to Nevada residents"
            if home and 'residency_requirement' not in rec and re.search(rf'\bnon[- ]{home}\s+residents?\b', page.title + ' ' + context, re.I):
                rec['residency_requirement'] = 'Out-of-state'  # WV (Concord): "Non-West Virginia Residents"
            other = re.search(r'(?<!non-)(?<!non )\b(' + '|'.join(v for v in STATES.values() if v != home) + r')\s+residents?\b', page.title + ' ' + context, re.I)
            if other and 'residency_requirement' not in rec:
                rec['residency_requirement'] = other.group(0)  # AL (UAH): "Freshman Tennessee Resident Academic Scholarships"
            # AZ (Northland Pioneer): a page-navigation heading ('Social Media') is not where the award is listed
            nav = re.search(r'social\s+media|quick\s+links|follow\s+us|connect\s+with\s+us|related\s+links|footer|navigation|\bmenu\b|academic\s+calendar', context, re.I)
            if context.strip() and not nav and not re.search(r'scholarship|award|grant|fellowship', context, re.I) and 'eligibility_summary' not in rec:
                rec['eligibility_summary'] = f'Listed under: {context.strip()[:200]}'  # IA (Hawkeye): "GED, HiSET, or ELL Graduates"
            rec['notes'] = f'Extracted by {EXTRACTOR} from the table "{(context or page.title)[:100]}"; cells copied as printed.'
            # The table's own label (year removed) lets review tell apart same-named awards on residency pages (UAH, UA, UMW).
            scope = re.sub(r'\s+', ' ', re.sub(T.YEAR_RE.pattern + r'|\b20\d{2}\b', '', context)).strip(' -–:|')
            same = json.dumps([rec, scope, rec_year], sort_keys=True, default=str)
            if printed.get(same, id(t)) != id(t): continue  # AL (South Alabama): the same grid printed twice (desktop and mobile copies)
            printed.setdefault(same, id(t))  # a row repeated inside one table stays (LA: two "Robbins Award" rows)
            out.append(common.make('awards', inst['institution_key'], rec_year, rec_basis, rec, ev, entry, EXTRACTOR,
                                   {'award_name': rec['award_name']}, {'thresholds': rec.get('thresholds'), 'table_scope': scope},
                                   rec_issues + row_issues + ([span_issue] if span_issue else [])))
    return out
