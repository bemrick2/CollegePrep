"""CourseLeaf "Plan of Study Grid" tables (the catalog's Sample Plan tab) -> program_plan sequence rows
(`courseleaf_plan/v1`), plus the program record when the page has no "Course List" table for
catalog_program/v1 to read (e.g. OSU Civil Engineering prints its requirements only as the plan).

Rows: a one-cell row names a term or year ("First Year", "Fall"); [code, title, credits] rows are items; a
[_, "Credits", n] row is the printed term subtotal; [_, "Total Credits", n] is the plan total. A code cell
naming one course becomes a course item; joined or alternative cells ("CH 201& CH 204", "CE 383or CE 481")
stay printed text. Nothing is inferred. A page with several grids (one per option) marks every plan
`multiple_plan_grids`, because the grid's option is not reliably labelled -- unless each grid sits under its own
distinct "Bachelor of ..." heading (UO "Degree Map" tables), which then names the plan.
"""
from __future__ import annotations
import hashlib
import re

from pipeline.extractors import common
from pipeline.extractors.catalog import credential, program_name, slug

from programs.years import academic_year_of
EXTRACTOR = 'courseleaf_plan/v1'
ONE = re.compile(r'^([A-Z]{1,5})\s(\d{3}[A-Z]?)$')
TERM = re.compile(r'^(first|second|third|fourth|fifth|freshman|sophomore|junior|senior)\s+year$|^year\s+\d$|^(fall|autumn|winter|spring|summer)(\s+(term|semester|quarter))?(\s+\d)?$'
                  # year rows printed alone: 'Freshman' (JSU, UNI, OSU, UNO), 'Year One' (CU Boulder); 'Semester 1' (UWM)
                  r'|^(freshman|sophomore|junior|senior)$|^year\s+(one|two|three|four|five)$|^semester\s+\d{1,2}$'
                  # 'First Semester' (Clayton, ODU), 'Semester One' (West Chester)
                  r'|^(first|second|third|fourth|fifth|sixth|seventh|eighth)\s+semester$|^semester\s+(one|two|three|four|five|six|seven|eight)$'
                  # '1st Semester' (NJIT)
                  r'|^(1st|2nd|3rd|[4-8]th)\s+semester$'
                  # printed term labels (#229 re-extraction): 'Term 1' (Cal Poly), '1st Year' (Akron), 'Year II' (APU),
                  # 'Semester III' (Lorain CCC), 'Summer Session I' (West Chester), 'Fall I' (Georgetown), 'J-term'
                  # (Quinnipiac), 'Junior and Senior Years' (CSUS), and SPU's 'Any Quarter' / 'Variable' / 'Autumn or Winter'
                  r'|^term\s+\d$|^(1st|2nd|3rd|[4-6]th)\s+year$|^year\s+(i|ii|iii|iv|v)$|^semester\s+(i|ii|iii|iv|v|vi|vii|viii)$'
                  r'|^summer\s+session(\s+(i|ii|\d))?$|^(fall|spring|summer|winter)\s+(i|ii|iii|iv)$|^j-?term$'
                  r'|^(freshman|sophomore|junior|senior)\s+and\s+(freshman|sophomore|junior|senior)\s+years$'
                  r'|^any\s+quarter$|^variable$|^(autumn|fall|winter|spring|summer)\s+or\s+(autumn|fall|winter|spring|summer)$', re.I)

# column headers printed on a term row ('Fall | Hours', UNI 'Fall | Hour', Texas A&M 'Fall | Semester Credit Hours')
HEADER_CELLS = {'credits', 'milestones', 'hours', 'credit hours', 'hour', 'credit', 'semester credit hours', 'semester hours', 'units', 's.h.'}  # 'Fall | S.H.' (YSU)
# the term's subtotal row ('| Hours | 15', '| Credit Hours | 15', '| Semester Credit Hours | 15') and the plan total
# ('Total Hours**', 'Total Semester Credit Hours'): read as the term's credit hours and the printed total, never as items
# 'Term Credits' (NJIT), 'Semester Total' (TMCC)
SUBTOTAL = re.compile(r'^(credits|credit|hours|hour|credit hours|semester credit hours|semester hours|units|term credits|semester total|term total)$', re.I)
# 'Total Hours**' (SRU), 'Total Credit Hours Required:' (TAMUK), 'Minimum Total Hours' (Louisville), 'Minimum Total Credit Hours:' (Kent State)
TOTAL = re.compile(r'^(?:minimum\s+)?total\b[\w\s]*:?\**$', re.I)
# a credit label the reader does not place ('Minimum Semester Hours 30-32', LMU, printed once per year): the plan is held
CREDIT_LABEL = re.compile(r'\b(hours?|credits?|units?)\b\s*:?\**$', re.I)
PLAN_EXTRACTOR = 'courseleaf_plan/v3'
# Plan item cells (v3). A course code as printed: 'ENGL 101', 'MGMT 4010' (four digits), 'ASL 19201' (five), 'BIO SCI 102' / 'M L 250' (a
# two-word subject), 'CHEM 125A'; never a placeholder subject ('XXXX 1201').
PLAN_CODE = r'(?!X{3,}\b)[A-Z]{1,5}(?:\s[A-Z]{1,5})?\s\d{3,5}[A-Z]?'  # five digits: Kent State 'ASL 19201', Notre Dame 'CSE 20311'
PLAN_CODE_CELL = re.compile(rf'^{PLAN_CODE}$')
# alternatives printed in one cell with 'or' joined to the code before it: 'SPAD 281or SPAD 284' (Louisville),
# 'CHEM 121or CHEM 125' (NJIT); the title cell joins the titles the same way ('Principles of Sport Administrationor Sport ...')
PLAN_ALT_CELL = re.compile(rf'^{PLAN_CODE}(?:or\s?{PLAN_CODE})+$')
PLAN_CREDITS = re.compile(r'^\d{1,2}(?:\.\d{1,2})?(?:\s*-\s*\d{1,2}(?:\.\d{1,2})?)?$')
PLAN_MARKERS = {'!', '*', '+', '†', '‡', '#'}  # a marker column before the code (Kent State prints '!' for critical courses)


GENERIC_PLAN_HEADING = re.compile(r'^(all|degree program guide|plan requirements|program requirements|semester sequence|course sequence|'
                                  r'plan of study|sample plan( of study)?|four-year plan|\d{4}\s*-\s*\d{4}( edition)?|prerequisite courses|school of .+)$', re.I)


def plan_item(cells, milestones):
    """One grid row as a plan item with separate fields, or None when the row's cells do not say which field each one is
    (the row is then kept as printed, its cells joined by ' | ').
    {'code', 'title', 'credits'} for a course; {'any_of': [{'code', 'title'}, ...], 'credits'} for alternatives printed in
    one cell; {'text', 'credits'} for a printed requirement row ('General Education: ... - S | 3'). Credits are read only from
    the last cell, only when it prints a number or a range; a blank credits cell gives no credits."""
    marker = None
    if len(cells) >= 3 and (cells[0] in PLAN_MARKERS or not cells[0]) and (PLAN_CODE_CELL.match(cells[1]) or PLAN_ALT_CELL.match(cells[1])
                                                                          or (not cells[0] and cells[1] and not PLAN_CODE_CELL.match(cells[0] or 'x'))):
        marker, cells = cells[0] or None, cells[1:]  # Kent State: ['!', 'ASL 19201', 'ELEMENTARY ...', '4'], ['', 'Kent Core Requirement', '3']
    last = cells[-1] if len(cells) >= 2 else ''
    if last and not PLAN_CREDITS.match(last): return None  # '(3)', 'Varies', '3 or 4': kept as printed
    credits = _credits(last) if last else None
    first = cells[0]
    if PLAN_CODE_CELL.match(first):
        if len(cells) == 3: item = {'code': first, 'title': cells[1]}
        elif len(cells) == 2: item = {'code': first}  # 'MIAD CD 305 | 3'
        else: return None
        if not item.get('title'): item.pop('title', None)
    elif PLAN_ALT_CELL.match(first):
        if len(cells) != 3: return None
        codes = re.split(r'or\s?(?=[A-Z]{1,5}(?:\s[A-Z]{1,5})?\s\d)', first)  # the code cell matched PLAN_ALT_CELL
        titles = re.split(r'(?<=\S)or\s(?=\S)', cells[1]) if cells[1] else []
        # a title cell with a free-standing 'or', '(or' or a trailing 'or' ('Merchandising Analytics or Senior Problem ...',
        # 'Calculus for Business ... 4or', Drexel / USC) does not show where each title ends: kept as printed
        if cells[1] and re.search(r'(^|[\s(])or(\s|$)|or$', cells[1]): return None
        if cells[1] and len(titles) != len(codes): return None  # a title that itself contains 'or ' cannot be split by evidence
        item = {'any_of': [{'code': c, **({'title': t} if cells[1] else {})} for c, t in zip(codes, titles or [''] * len(codes))]}
    elif len(cells) == 2 or (len(cells) == 3 and not cells[1]):
        if not first or re.match(r'^or\b', first, re.I) or re.fullmatch(r'\d{1,2}', first): return None  # 'or ...' rows, footnote-only rows
        item = {'text': first}
    else:
        return None
    if credits is not None: item['credits'] = credits
    if marker: item['marker'] = marker
    return item


def labelled_keys(heads, make):
    """Keys for plans named by their headings. A key is a slug cut at 80 characters, so headings that differ only after
    that ('Model 4-Year Plan–Bachelor of Business Administration–Finance Major Curriculum–Math placement MATH 101' /
    '... MATH 110', LMU 2026-27) would share a key and a candidate id. The last such plan keeps the key (the one stored
    before this rule); earlier ones get a short hash of their full heading."""
    keys = [make(h) for h in heads]
    return [f'{k[:73]}-{hashlib.sha1(h.encode()).hexdigest()[:6]}' if k in keys[i + 1:] else k
            for i, (k, h) in enumerate(zip(keys, heads))]


TRACK_WORD = re.compile(r'\b(concentration|track|emphasis|option)\b', re.I)
TRACK_SENTENCE = re.compile(r'\b(?:the\s+)?(?:below|following|above)\s+plan\s+is\s+for\s+the\s+.{3,120}?\b(?:track|concentration|option|emphasis)\b', re.I)


def single_plan_label(page, heading):
    """A track named for a page's only plan grid, as printed: the line right above the 'Plan of Study Grid' caption when it
    is a short label naming a concentration, track, emphasis or option ('Physical Geography Concentration Plan', CU
    Boulder Geography BS), or the sentence between the grid's heading and its caption that says which track the plan is for
    ('The below plan is for the Greek and/or Latin Language and Literature track of the major.', CU Boulder Classics BA).
    None otherwise; nothing is inferred from the program name."""
    lines = [l.strip() for l in page.text.splitlines() if l.strip()]
    caps = [i for i, l in enumerate(lines) if l in ('Plan of Study Grid', 'Degree Map')]
    if len(caps) != 1 or caps[0] == 0: return None
    k = caps[0]; prev = lines[k - 1]
    if prev != heading and not prev.startswith('|') and len(prev) <= 120 and not prev.endswith(('.', ':')) and TRACK_WORD.search(prev):
        return prev
    j = max((i for i, l in enumerate(lines[:k]) if l == heading), default=None) if heading else None
    for l in (lines[j + 1:k] if j is not None else []):
        for sent in re.split(r'(?<=\.)\s+', l):
            if TRACK_SENTENCE.search(sent): return sent.strip()
    return None


def grids(page):
    return [t for t in page.tables if (t.get('caption') or '').strip().lower() in ('plan of study grid', 'degree map')]


FOOTNOTE_MARK = re.compile(r'^(\d{1,2}|[a-zA-Z]|ii|iii|iv|vi{0,3}|[*†‡§#+^]{1,4})[.)]?$')
FOOTNOTE_INLINE = re.compile(r'^([*†‡§#+^]{1,4})\s?([A-Z(].*)$')  # '**This document serves as a guide ...' (Slippery Rock)
FOOTNOTE_INLINE_NUM = re.compile(r'^(\d{1,2})[.)]?\s?([A-Z].*)$')  # '1 Requires English Composition Placement', '2This course ...' (Nebraska Omaha)
FOOTNOTE_ROW = re.compile(r'^\|\s*(\d{1,2}|[*†‡§#+^]{1,4})\s*\|\s*(.*?)\s*\|?$')  # '| 1 | Select from: EC 222 ...' (JSU prints its notes as table rows)
LIST_LINE = re.compile(r'^(?:[A-Z]{2,5}[\s\xa0]?\d{3}|[•\-–]|\(?[a-z0-9]{1,2}[.)]\s|[Gg]roup\b|[Ss]elect\b|[Cc]hoose\b|[Oo]r\b|[Aa]nd\b|[a-z(])')
# Page text that ends a plan's notes: whole lines only (a note may well mention 'accreditation' or 'apply for admission')
PAGE_TEXT = re.compile(r'^(?:©.*|.*\bcopyright\b.*|back to top|print options|quick links|find us|connect with .*|apply (online|for admission|now)\b.*|'
                       r'contact( us| admissions| information)?\b.{0,60}|.*\bprivacy (statement|policy)\b.*|.*\bwebmaster\b.*|search( catalog| bulletin)?|'
                       r'submit search|catalog navigation|(program |student )?learning outcomes|questions\??|program contacts?\b.{0,40}|degree audit( report)?|'
                       r'accreditation|\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}.{0,40}|.{0,60}\b\d{5}(-\d{4})?|.{0,40}\bedition|\d{4}-\d{4}( [\w ]{0,30})?|'
                       r'toggle|undergraduate|graduate|total( program)? (credits?|hours|credit hours|units)\W*\d[\d\s-]*|.{0,30}navigation|faculty|staff|'
                       r'facebook|twitter|x|youtube|instagram|linkedin|tiktok|flickr|.{0,40}\bnew window\.?|'
                       r'\d+ [A-Z][\w.]*( [A-Z][\w.]*)* (drive|dr\.?|street|st\.?|avenue|ave\.?|road|rd\.?|boulevard|blvd\.?|way|lane|ln\.?|campus)|'
                       r'[A-Z][\w .]+, [A-Z]{2} \d{5}.*|.{0,40}main campus|major code\b.*|revision date\b.*|every effort has been made.*|'
                       r'well prepared for employment.*)$', re.I)
# Page text that ends unmarked notes only (never applied inside a footnote): program descriptions and marketing, the
# institution's name, contact blocks, navigation and page metadata
DESCRIPTION = re.compile(r"\b(you'll|you will|launch your|your (career|future|passion)|why major in|underpins all|guided pathway|is the study of|"
                         r"enables students|opportunities abound|career options)\b|^for (more|additional) (information|questions)\b|"
                         r"^(email|phone|fax|office|location|tel)\s*:|^p\.?\s?o\.? box\b|^\d+ [A-Z][\w.]*( [A-Z][\w.]*)* (st|street|ave|avenue|road|rd|drive|dr|blvd)\.?,?$|"
                         r"\btoggle\b|^on this page$|^last updated\b|^major/concentration:|^students$|^[\w.-]+\.edu$|\(\d{4}\)$|"
                         r"^(the )?([A-Z][\w&.'’-]*\s){0,5}(University|College|Institute)( of( [A-Z][\w&.'’-]*| [a-z]{2,3}){1,5})?\.?$", re.I)
NOTE_HEADING = re.compile(r'^(notes?\b.*|additional information about this plan:?|.{0,40}\b(notes?|requirements?)\s*:?)$', re.I)
PLAN_NOTE = re.compile(r'\b(must|required?|requires|requirements?|may( not)?|cannot|can ?not|count(s|ed)? toward|substitut\w*|in (lieu|place) of|instead of|'
                       r'retake|repeat\w*|grade of|minimum|maximum|only (one|be|if|after)|exclud\w*|except|electives?|select|choose|complete[ds]?|'
                       r'placement|prerequisite|co-?requisite|consult|recommended|eligible|not required|in addition to|no more than|at least|up to|'
                       r'appl(y|ied|ies)|counts?|credits?|credit hours|semester hours|regist\w*|enroll\w*|advis\w*|coordinator|taken|offered|'
                       r'passing|graduat\w*|transfer\w*|courses?)\b', re.I)
END = ('.', '!', '?', ')', '"', '”')
CITED_SYMBOL = re.compile(r'(?<![*†‡§#+^])([*†‡§#^]{1,4})\s*\d*$|^([*†‡§#+^]{1,4})(?=[A-Za-z(])')  # 'Total Hours**', '+*WR 121Z' (Oregon State)


def _lines(page):
    return [re.sub(r'[\s\xa0]+', ' ', l).strip() for l in page.text.splitlines() if l.strip()]


def _grid_tails(page):
    """Per plan grid, what is printed after it up to the next caption or hard stop: (footnotes, rest, stop_line), where rest
    is the list of lines after the footnotes and stop_line the line that ended them (None at the next caption or page end).
    None when the page text does not show one caption per grid."""
    lines = _lines(page)
    caps = [k for k, l in enumerate(lines) if l.lower() in ('plan of study grid', 'degree map')]
    gs = grids(page)
    if len(caps) != len(gs): return None
    heads = {re.sub(r'[\s\xa0]+', ' ', h).strip() for h in (page.headings or [])}
    heads |= {x.strip() for x in re.split(r'\s[|<–-]\s', page.title or '')[1:] if x.strip()}  # the institution's name, as its page title prints it
    heads |= {(g.get('heading') or '').strip() for g in grids(page)[1:] if (g.get('heading') or '').strip()}  # the next grid's own heading
    hard = lambda l: (l.startswith('|') and not FOOTNOTE_ROW.match(l)) or l.lower() in ('plan of study grid', 'degree map', 'course list') or l.startswith('©') or l in heads

    def mark(l, last_num):
        if PAGE_TEXT.search(l): return None, None  # '1 LMU Drive', 'X' (a social link) are page text, not notes
        m = FOOTNOTE_ROW.match(l)
        if m: return m.group(1), m.group(2) or None
        m = FOOTNOTE_MARK.match(l)
        if m: return m.group(1), None
        m = FOOTNOTE_INLINE.match(l)
        if m: return m.group(1), m.group(2)
        m = FOOTNOTE_INLINE_NUM.match(l)  # a number leading its text only when it is the next number ('1 Requires ...')
        if m and int(m.group(1)) == last_num + 1: return m.group(1), m.group(2)
        return None, None

    out = []
    for n, (k, g) in enumerate(zip(caps, gs)):
        stop = caps[n + 1] if n + 1 < len(caps) else len(lines)
        # the grid ends at its last printed row (the total): the first row line after the caption that prints all its cells
        last = next((r for r in reversed(g.get('rows') or []) if any((c or '').strip() for c in r)), [])
        cells = [re.sub(r'[\s\xa0]+', ' ', c).strip() for c in last if (c or '').strip()]
        end = next((j for j in range(k + 1, stop) if lines[j].startswith('|') and all(c in lines[j] for c in cells)), None)
        if end is None or not cells: return None
        j, notes, last_num = end + 1, [], 0
        while j < stop:
            m, first = mark(lines[j], last_num)
            if m is None or hard(lines[j]): break
            if m.isdigit():
                if notes and int(m) <= last_num: break
                last_num = int(m)
            j += 1
            body = [first] if first else []
            if not body and j < stop and not hard(lines[j]) and mark(lines[j], last_num)[0] is not None and not FOOTNOTE_MARK.match(lines[j]):
                body.append(lines[j]); j += 1  # a note whose printed text starts with a symbol ('*' / '*Approved electives ...', NC State)
            while j < stop and not hard(lines[j]) and not PAGE_TEXT.search(lines[j]) and mark(lines[j], last_num)[0] is None:
                body.append(lines[j]); j += 1
            if not body: break
            nxt = mark(lines[j], last_num)[0] if j < stop and not hard(lines[j]) else None
            if nxt is not None and not (nxt.isdigit() and int(nxt) <= last_num):
                notes.append({'marker': m, 'text': ' / '.join(body)}); continue
            # the last note. Its lines run on while they plainly continue it: a list under a line ending in ':' runs to
            # the page text; a line that does not end a sentence is continued by the next; lower-case or list lines continue
            keep = [body[0]]
            if body[0].endswith(':'): keep = body  # a list under the note runs to the page text (South Carolina, Kingsville)
            for l in body[len(keep):]:
                if keep[-1].endswith(':') or any(x.endswith(':') for x in keep) and (LIST_LINE.match(l) or not l.endswith(END)) \
                        or LIST_LINE.match(l):
                    keep.append(l)
                else: break
            notes.append({'marker': m, 'text': ' / '.join(keep)})
            j -= len(body) - len(keep)
            break
        rest = []
        while j < stop and not hard(lines[j]): rest.append(lines[j]); j += 1
        out.append((notes, rest, lines[j] if j < len(lines) and j != stop else None))
    return out


def cited_symbols(g):
    """The symbol markers a grid's cells cite ('Total Hours**', 'PHYS 120*', 'HSS Elective*'). Numbers are not counted: a
    title may end in one ('Calculus 2')."""
    out = set()
    for r in g.get('rows') or []:
        for c in r:
            m = CITED_SYMBOL.search((c or '').strip())
            if not m: continue
            mk = m.group(1) or m.group(2)
            # a prefix may print several marks together ('+*'): each one is cited
            out |= set(mk) if m.group(2) and len(set(mk)) > 1 else {mk}
    return out


def grid_footnotes(page):
    """The footnotes printed right after each plan grid, in grid order: [[{'marker', 'text'}, ...], ...]. CourseLeaf prints
    a marker line and the note's text after the grid's last row ('1' / 'Must make a grade of C or better.', Texas A&M
    2026-27); markers may be numbers ('1', '1.'), letters, roman numerals or symbols ('+', '^', '**', '****'), a number
    or symbol may lead its text on one line ('**This document serves as a guide', '1 Requires English Composition
    Placement'), and JSU prints them as table rows ('| 1 | Select from: ...'). A note's text runs to the next marker, its
    lines joined by ' / '; the last note runs on while its lines plainly continue it. Page text (addresses, social links,
    page metadata) is never a note. Numbered markers must increase (a skipped number is allowed: Saint Louis prints 1, 3, 4).
    When a page prints one legend after the last of several grids and none after the others (Oregon State), the legend is
    kept on each grid whose rows cite one of its markers, marked 'shared'. None when the page text does not show one
    caption per grid, so no note is ever paired with the wrong grid."""
    tails = _grid_tails(page)
    if tails is None: return None
    out = [notes for notes, _, _ in tails]
    if len(out) > 1 and out[-1] and not any(out[:-1]):
        legend = {x['marker'] for x in out[-1]}
        out = [[dict(x, shared=True) for x in out[-1]] if cited_symbols(g) & legend else [] for g in grids(page)[:-1]] + [out[-1]]
    return out


def plan_notes(page):
    """Unmarked notes printed after each plan grid and its footnotes, as printed: [{'text', 'location'}] per grid, or the
    string 'unclear', or None when grids and captions cannot be paired. A note is a sentence that states a requirement,
    option, exclusion or advice ('Graduation requirements include 3 hours of International and Cultural Diversity', 'FINA
    courses do not count toward the major'); a note ending in ':' keeps the list printed under it, and a line that does not
    end a sentence is continued by the next. Notes run until page text (contacts, addresses, navigation, outcomes,
    footer, disclaimers). The notes are 'unclear' when any other line is printed before that page text (it may belong to
    the notes, so it is never dropped silently), or when a footnote marker is printed after the notes."""
    tails = _grid_tails(page)
    if tails is None: return None
    out = []
    for notes, rest, _ in tails:
        got, k = [], 0
        loc = 'printed after the plan grid' + (' and its footnotes' if notes else '')
        # a footnote that does not end a sentence may run on into the next printed line: the note keeps that location
        after = notes[-1] if notes and not notes[-1]['text'].endswith(END + (':',)) else None
        while k < len(rest):
            l = rest[k]
            if PAGE_TEXT.search(l) or DESCRIPTION.search(l): break
            prev = got[-1]['text'] if got else ''
            if not re.search(r'\w', l): k += 1; continue  # a line of punctuation only ('.')
            heading = NOTE_HEADING.match(l)
            if (FOOTNOTE_INLINE.match(l) or FOOTNOTE_ROW.match(l) or (FOOTNOTE_MARK.match(l) and not l.isdigit())) and not heading:
                break  # a marked note printed after unmarked ones: which mark belongs where is not printed (held below)
            if got and not heading and (any(x.endswith(':') for x in prev.split(' / ')) or not prev.endswith(END) and LIST_LINE.match(l)):
                got[-1]['text'] += ' / ' + l  # the list under a 'Note:' (to the page text) or a sentence printed over two lines
            elif heading or (len(l.split()) >= 5 and PLAN_NOTE.search(l)):
                may = not got and after is not None and not heading
                got.append({'text': l, 'location': f"printed directly after footnote {after['marker']}, which it may continue" if may else loc})
            else: break
            k += 1
        first_page_text = next((i for i, l in enumerate(rest[k:]) if PAGE_TEXT.search(l) or DESCRIPTION.search(l)), len(rest) - k)
        # any line printed before the page text that is not read as a note: it may belong to the plan's notes, so the plan
        # is held rather than the line dropped
        out.append('unclear' if rest[k:k + first_page_text] else got)
    return out


def parse_grid(t):
    """UO grids add a Milestones column ('Fall | Milestones | Credits'): a course row is [code, title, milestone,
    credits] and a text row [text, milestone, credits] (the text cell spans two columns). The milestone is kept in its
    own field, never inside the item text. A text row printed with credits only stays a row with empty text."""
    terms, cur, total, milestones = [], None, None, False
    total_label = [None]
    rows = t.get('rows') or []
    last = max((i for i, r in enumerate(rows) if any((c or '').strip() for c in r)), default=-1)
    span = []  # terms opened since the last subtotal row
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row]
        nonempty = [c for c in cells if c]
        if not nonempty: continue
        # LMU prints its plan total as 'Minimum Semester Hours | 107-128', the grid's last row (and the same label under each
        # year in some plans, which stays held below)
        if i == last and total is None and len(nonempty) == 2 and re.fullmatch(r'minimum\s+semester\s+hours', nonempty[0], re.I) \
                and re.fullmatch(r'\d{1,3}(\s*-\s*\d{1,3})?', nonempty[1]) \
                and sum(1 for r in rows if any(re.fullmatch(r'minimum\s+semester\s+hours', (c or '').strip(), re.I) for c in r)) == 1:
            total = nonempty[1]; total_label[0] = nonempty[0]; continue
        if len(cells) == 1 and not TERM.match(cells[0]):  # a label row the reader does not know ('Third Semeseter', UNO)
            t['_unread_label'] = True
        if len(nonempty) == 1 and not TERM.match(nonempty[0]) and re.search(r'\byear\s+\d\b', nonempty[0], re.I) and nonempty[0].isupper():
            t['_unread_label'] = True  # 'DOCTORAL YEAR 2' / 'YEAR 1, CONTINUED' printed inside a term (Quinnipiac BS/OTD)
        if (len(nonempty) >= 2 and not TERM.match(nonempty[0]) and not ONE.match(nonempty[0])
                and all(c.lower() in HEADER_CELLS for c in nonempty[1:])):  # an unknown term printed with its header ('Term 1 | Units')
            t['_unread_label'] = True
        if TERM.match(nonempty[0]) and all(c.lower() in HEADER_CELLS for c in nonempty[1:]):  # 'Fall | Milestones | Credits' (UO)
            milestones = milestones or any(c.lower() == 'milestones' for c in nonempty[1:])
            cur = {'term_index': len(terms) + 1, 'label': nonempty[0], 'items': []}; terms.append(cur); span.append(cur); continue
        # the label is the row's first cell: a course titled 'Total Rewards' ('MGMT 4010 | Total Rewards | 3', UNO) is a course
        if len(nonempty) == 2 and TOTAL.match(nonempty[0]):
            total = nonempty[-1]; total_label[0] = nonempty[-2]; continue
        if len(nonempty) == 2 and SUBTOTAL.match(nonempty[0]):
            if cur is not None:
                # SLU prints 'Spring' (no rows) then the sessions 'Spring 1' and 'Spring 2', then one subtotal: the subtotal is
                # the parent term's
                sub = re.match(r'^(.*\S)\s+\d$', cur['label'])
                parent = next((x for x in reversed(terms[:-1]) if sub and x['label'].lower() == sub.group(1).lower()), None)
                parent = parent if parent is not None and not parent['items'] else None
                if parent is not None and parent.get('credit_hours'): t['_subtotal_spans'] = True  # each session printed its own subtotal
                elif parent is not None: parent['credit_hours'] = nonempty[1]
                elif sum(1 for x in span if x['items']) > 1: t['_subtotal_spans'] = True  # one subtotal printed for two terms (Marshall)
                else: cur['credit_hours'] = nonempty[1]
            span = []
            continue
        if len(nonempty) == 2 and not cells[0] and CREDIT_LABEL.search(nonempty[0]) and PLAN_CREDITS.match(nonempty[1]):
            t['_unread_label'] = True  # 'Minimum Semester Hours | 30-32' (LMU): a credit row the reader does not place
        if cur is None: continue
        m = ONE.match(cells[0]) if cells and cells[0] else None
        # a decimal credit is kept as printed ('1.5', West Chester B.M. 2026-27 ensembles), never rounded or dropped
        hours = cells[-1] if len(cells) >= 2 and re.fullmatch(r'\d{1,2}(?:\.\d{1,2})?(\s*-\s*\d{1,2}(?:\.\d{1,2})?)?', cells[-1] or '') else None
        if m and len(cells) >= 3 and cells[-1] and not hours:
            cur['items'].append(' | '.join(nonempty))  # '.5', '3 or 4', '1 (0)' (EKU, UIC, Montana): kept as printed, never dropped
        elif m:
            item = {'code': f'{m.group(1)} {m.group(2)}', 'title': cells[1] if len(cells) > 2 else ''}
            if hours: item['credits'] = int(hours) if hours.isdigit() else hours
            if milestones and len(cells) == 4 and cells[2]: item['milestone'] = cells[2]
            cur['items'].append(item)
        elif milestones and len(cells) == 3 and (cells[1] or not cells[0]):
            item = {'text': cells[0]}
            if cells[2]: item['credits'] = int(cells[2]) if cells[2].isdigit() else cells[2]
            if cells[1]: item['milestone'] = cells[1]
            cur['items'].append(item)
        else:
            item = plan_item(cells, milestones)
            cur['items'].append(item if item is not None else ' | '.join(nonempty))
    t['_total_label'] = total_label[0]
    for term in terms: term['items'] = choice_blocks(term['items'])
    return terms, total


# an optional printed label before the instruction ('Jax MIX Experience: select one of the following', JSU) and footnote
# marks after it ('Select one of the following: 1', '... following: 2,3', Texas A&M, Temple) are kept in the item's text
CHOICE_HEADER = re.compile(r'^(?:[A-Z][^:]{0,60}:\s*)?(?:select|choose)\s+(one|two|three|four|five|six|[1-9])\s+(?:(?:course|class)(?:e?s)?\s+)?'
                           r'(?:of|from)\s+the\s+following\s*:?(?:\s*\d{1,2}(?:\s*,\s*\d{1,2})*)?$', re.I)
COUNT_WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}


def _option_row(x):
    """A blank-credit course row that can be one option of a printed choice block: a course or alternatives read into
    fields, or a course row kept as printed ('PHIL/DASC 357E | Ethics', 'GEOL 101& GEOL 102 | Geology', Texas A&M, Marshall)."""
    if isinstance(x, dict):
        return ('code' in x or 'any_of' in x) and not set(x) & {'credits', 'milestone', 'marker'}
    parts = x.split(' | ')
    return bool(OPTION_CODE.match(parts[0])) and not PLAN_CREDITS.match(parts[-1])


OPTION_CODE = re.compile(r'^[A-Z][A-Z&]{1,7}(?:/[A-Z&]{1,8})*(?:\s[A-Z&]{1,5})?\s?\d{3,5}[A-Z]?(?:\s?(?:/|&|or)\s?.*\d{3,5}[A-Z]?)?$')


def _credited(x):
    """A row that prints its own credits, which ends a choice block."""
    if isinstance(x, dict): return 'credits' in x
    return bool(PLAN_CREDITS.match(x.split(' | ')[-1]))


def choice_blocks(items):
    """A printed choice block as one item. 'Select one of the following: | 3' followed by two or more course rows whose credit
    cells are blank (EKU, LMU, Temple 2026-27) is {'choose': 1, 'text': header, 'credits': 3, 'options': [...]}: the options
    are not each required. The options run to the next row that prints credits, or to the term's end, and every row in that
    run must be a course row; otherwise (a text row such as 'GEP Humanities' among them) the block is not grouped, so it is
    never cut short. A header that prints no credits or no count, options with their own credits, or fewer options than
    the count plus one stay as printed rows."""
    out, i = [], 0
    while i < len(items):
        it = items[i]
        m = CHOICE_HEADER.match(it.get('text', '')) if isinstance(it, dict) and set(it) == {'text', 'credits'} else None
        j = i + 1
        while m and j < len(items) and not _credited(items[j]):
            j += 1
        run = items[i + 1:j]
        n = (COUNT_WORDS.get(m.group(1).lower()) or int(m.group(1))) if m else None
        if m and len(run) >= 2 and n < len(run) and all(_option_row(x) for x in run):
            out.append({'choose': n, 'text': it['text'], 'credits': it['credits'], 'options': run}); i = j
        else:
            out.append(it); i += 1
    return out


YEAR_ORDER = {**{w: k for k, w in enumerate(('first year', 'second year', 'third year', 'fourth year', 'fifth year'), 1)},
              **{w: k for k, w in enumerate(('freshman year', 'sophomore year', 'junior year', 'senior year'), 1)},
              **{w: k for k, w in enumerate(('freshman', 'sophomore', 'junior', 'senior'), 1)},
              **{f'year {k}': k for k in range(1, 6)}}


GRID_CHANGE = re.compile(r'\b(in place of|instead of|replac\w*|substitut\w*|add(?:s|ed)?|also take|must take|will take|take[sn]?)\b[^.]{0,80}?\b[A-Z]{2,5}\s?\d{3}'
                         r'|\b[A-Z]{2,5}\s?\d{3}\b[^.]{0,80}?\b(in place of|instead of|replaces?)\b', re.I)


def grid_change_noted(page):
    """A sentence printed between continued plan grids that changes the plan for this program ('Business Honors students take
    BUSN 125 in place of BUSN 101', 'MIS majors add ISTM 250', Texas A&M 2026-27): the merged grids would not show it, so
    the plan is held."""
    lines = [l.strip() for l in page.text.splitlines() if l.strip()]
    caps = [k for k, l in enumerate(lines) if l in ('Plan of Study Grid', 'Degree Map')]
    if len(caps) < 2: return False
    between = lines[caps[0] + 1:caps[-1]]
    return any(GRID_CHANGE.search(l) for l in between if not l.startswith('|'))


def continued_grids(parsed, headings):
    """Several grids that print one plan: the same heading over each, and year headings that continue from grid to grid
    ('First Year' | 'Second Year', 'Third Year', 'Fourth Year'), one year after another with none repeated or skipped."""
    if len(parsed) < 2 or len(set(headings)) != 1 or not headings[0]: return False
    seq = []
    for terms, _ in parsed:
        years = [YEAR_ORDER.get(t['label'].strip().lower()) for t in terms if not t['items'] and not t.get('credit_hours')]
        if not years or None in years or not terms or terms[0]['items'] or terms[0].get('credit_hours'): return False
        seq += years
    return seq == list(range(seq[0], seq[0] + len(seq))) and seq[0] == 1


def extract(inst, entry, page, year, year_line, have_program):
    """Candidates for the plan grids of one page; `year` is the printed catalog year label (e.g. '2026-2027')."""
    gs = grids(page)
    if not gs or not year: return []
    acad = academic_year_of(year)
    name = program_name(page)
    # with a program record already read from the page (Texas A&M 'Agribusiness - BS' by static_program/v1), the plan is
    # that record's and takes its key (the caller re-keys it); without one, the page title must name a degree
    if not name or (not have_program and not credential(name)): return []
    pkey = slug(name)
    out = []
    parsed = [parse_grid(t) for t in gs]
    notes = grid_footnotes(page)  # printed footnotes, one list per grid; None when they cannot be paired with their grids
    for k, t in enumerate(gs):
        t['_footnotes'] = notes[k] if notes is not None else None
        t['_cited'] = cited_symbols(t)
    pnotes = plan_notes(page)  # unmarked notes printed after each grid (owner decision 2026-10-23)
    for k, t in enumerate(gs):
        t['_plan_notes'] = pnotes[k] if pnotes is not None else []
        # notes printed after the last of several plans' grids: which plans they apply to is not printed
        if pnotes is not None and len(gs) > 1 and k == len(gs) - 1 and pnotes[k]: t['_plan_notes_scope_unclear'] = True
    if not have_program:
        prog = {'program_key': pkey, 'program_name': name, 'catalog_year': year, 'program_url': common.source_of(entry)['url'],
                'credential_level': credential(name), 'notes': f'Extracted by {EXTRACTOR} from the published catalog program page.'}
        totals = {t for _, t in parsed if t and t.isdigit()}
        if len(parsed) == 1 and len(totals) == 1: prog['total_credits'] = int(next(iter(totals)))
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', prog,
                               [{'field': 'program_name', 'value': name, 'snippet': page.title[:200]},
                                {'field': 'catalog_year', 'value': year, 'snippet': year_line[:200]}], entry, EXTRACTOR, {'program_key': pkey}))
    headings = [(t.get('heading') or '').strip() for t in gs]
    if continued_grids(parsed, headings):
        # Texas A&M prints one plan as two grids under the same heading ('First Year' / 'Second Year' ... 'Fourth Year'),
        # each with its own printed total: one plan, its terms in printed order, each total kept as printed (never summed)
        terms = [dict(t, term_index=k) for k, t in enumerate((t for ts, _ in parsed for t in ts), 1)]
        totals = '; '.join(f"{g.get('_total_label') or 'Total Credits'} {tot} (as printed, grid {k} of {len(gs)})" for k, (g, (_, tot)) in enumerate(zip(gs, parsed), 1) if tot)
        merged = {'heading': headings[0], 'caption': gs[0].get('caption'), '_total_label': None,
                  '_cited': set().union(*(g['_cited'] for g in gs)),
                  '_footnotes': None if any(g['_footnotes'] is None for g in gs) else [dict(x, grid=k) for k, g in enumerate(gs, 1) for x in g['_footnotes']],
                  '_plan_notes': 'unclear' if any(g['_plan_notes'] == 'unclear' for g in gs) else [dict(x, grid=k) for k, g in enumerate(gs, 1) for x in g['_plan_notes']],
                  '_unread_label': any(g.get('_unread_label') for g in gs), '_subtotal_spans': any(g.get('_subtotal_spans') for g in gs), '_rule_text': totals}
        gs, parsed, headings = [merged], [(terms, None)], [headings[0]]
        if grid_change_noted(page): merged['_grid_change_note'] = True
    # UO prints one 'Degree Map' per award under its own heading ('Bachelor of Science in Computer Science'): distinct
    # headings label the plans, so several grids are not ambiguous there.
    # a tab or section heading ('Semester Sequence', 'Plan Requirements', '2026-2027 Edition', 'ALL') does not name a plan
    labelled = len(parsed) > 1 and len(set(headings)) == len(headings) and all(h and not GENERIC_PLAN_HEADING.match(h) for h in headings)
    # other headings name a track, concentration or route ('Physical Geography', 'Greek'): the plan is labelled by its printed
    # heading and held until a reviewer confirms each heading names a plan of this program (not a tab or another section)
    track_labels = labelled and not all(re.search(r'\bbachelor\b', h, re.I) for h in headings)
    single_label = single_plan_label(page, headings[0]) if len(parsed) == 1 else None
    plan_keys = labelled_keys(headings, slug) if labelled else []
    for i, (terms, total) in enumerate(parsed, 1):
        if not terms: continue
        if labelled:
            key = plan_keys[i - 1]
        else:
            key = 'sample-plan' if len(parsed) == 1 else f'sample-plan-{i}'
        caption = (gs[i - 1].get('caption') or 'Plan of Study Grid').strip()
        rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence',
              'terms': terms, 'source_section': (headings[i - 1] if labelled else single_label if single_label else f'Sample Plan: {caption}' + (f' {i} of {len(parsed)}' if len(parsed) > 1 else ''))}
        if total: rd['rule_text'] = f"{gs[i - 1].get('_total_label') or 'Total Credits'} {total} (as printed)"
        if gs[i - 1].get('_rule_text'): rd['rule_text'] = gs[i - 1]['_rule_text']
        if gs[i - 1].get('_footnotes'): rd['footnotes'] = gs[i - 1]['_footnotes']  # substitutions, options and notes, as printed
        pn = gs[i - 1].get('_plan_notes')
        if pn and pn != 'unclear': rd['plan_notes'] = [dict(x, scope='this plan') for x in pn]  # unmarked notes, as printed, with where they are printed
        rec = {'program_key': pkey, 'requirement_key': key, 'requirement_kind': 'program_plan', 'rule_details': rd}
        ev = [{'field': 'term', 'value': t['label'], 'snippet': f"{t['label']}: {len(t['items'])} items, {t.get('credit_hours', '?')} credits"} for t in terms]
        issues = ['multiple_plan_grids'] if len(parsed) > 1 and not labelled else ['plan_heading_label'] if (track_labels or single_label) else []
        if gs[i - 1].get('_unread_label'): issues.append('unread_label_row')
        if gs[i - 1].get('_subtotal_spans'): issues.append('subtotal_spans_terms')
        if gs[i - 1].get('_grid_change_note'): issues.append('grid_change_noted')
        if gs[i - 1].get('_footnotes', []) is None: issues.append('footnotes_not_read')
        if gs[i - 1].get('_plan_notes') == 'unclear': issues.append('plan_note_unclear')
        fns = gs[i - 1].get('_footnotes')
        if fns is not None and gs[i - 1].get('_cited', set()) - {x['marker'] for x in fns}:
            issues.append('footnote_missing')  # a row cites a mark ('Total Hours**') whose note is not printed after the grid
        if gs[i - 1].get('_plan_notes_scope_unclear'): issues.append('plan_note_scope_unclear')
        out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, PLAN_EXTRACTOR,
                               {'program_key': pkey, 'requirement_key': key}, {'terms': len(terms)}, issues))
    return out


# ---- Course List tables (courseleaf_list/v1) -------------------------------------------------------------------
# The shared catalog_program/v1 extractor sometimes labels "Select ... from the following" groups all_required
# (issue #95). This reader builds requirement groups from the CourseLeaf "Course List" rows directly and emits only
# what the rows make unambiguous:
#   * consecutive course rows that print their own credits -> one all_required group;
#   * a "Select/Choose ..." row followed by option rows printed WITHOUT credits -> one choose_courses group (a printed
#     course count) or choose_credits group (a printed credit number); the options end at the first row that prints
#     credits, a section heading, or another Select row;
#   * "or CODE" rows join the previous course as {"any_of": [...]}.
# Rows the reader cannot represent exactly (joined "A& B" courses, cross-listed "A/B 101" codes, a Select row whose
# number is not printed, options that print their own credits) put an issue on the group so it is held for review.
LIST_EXTRACTOR = 'courseleaf_list/v1'
SELECT = re.compile(r'^(select|choose|complete)\b', re.I)
LEAD_IN = re.compile(r'^students\s+must\s+(?=(?:take|complete|select|choose)\s+(?:an?\s+additional\s+|at\s+least\s+)?\d{1,2}\s+(?:additional\s+)?'
                     r'(?:credit\s+hours|credits|hours)\s+(?:from|of)\s+the\s+following\b)', re.I)  # WKU Film: 'Students must take an additional 15 credit hours from the following list'
NUMBER_WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
COUNT = re.compile(r'^(?:select|choose|complete|take)\s+(?:(?:a\s+)?(?:minimum|total)\s+of\s+)?(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\s+'
                   # a qualifying word ('two BIOL courses', 'one Fine Arts course'), never a unit: 'Select 5 hours of the
                   # following', 'Select 6 SCH' print a number of credits (SHSU 2026-27)
                   r'(?:additional\s+|more\s+|upper[- ]division\s+|lower[- ]division\s+|(?!(?:hours?|hrs?|credits?|credit|cr|crs|sch|sh|units?|semester)\b)[A-Z]{2,5}\s+)*'
                   r'(?:courses?|of\s+the\s+following|from\s+the\s+following)\b', re.I)
# TAMUSA "Select one of COB's Approved Ethics Electives" over its listed options: a number word, then a named list
COUNT_NAMED = re.compile(r"^(?i:select|choose)\s+(?i:(one|two|three|four|five|six))\s+of\s+(?:[A-Z][\w'’&-]*\s+){1,5}(?i:electives?|courses?)\b")
CREDITS = re.compile(r'^(?:select|choose|complete|take)\s+(?:(?:a\s+)?(?:minimum|total)\s+of\s+(?:at\s+least\s+)?|at\s+least\s+|an\s+additional\s+)?'
                     r'(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)(?:\s*-\s*\d{1,2})?\s+(?:additional\s+)?(?:credits?|credit\s+hours|semester\s+(?:credit\s+)?hours|hours|units|SCH)\b', re.I)
# 'Complete the following:' (UVU) prints an all-required list, not a choice
ALL_FOLLOWING = re.compile(r'^(?:complete|take)\s+(?:all\s+(?:of\s+)?)?the\s+following(?:\s+(?:courses|requirements))?\s*:?\s*$', re.I)


def _num(w):
    return NUMBER_WORDS.get(w.lower()) or int(w)
# One course code as printed: 'BIOL 101', 'IT222' (Purdue Global prints no space), 'ENGL 1302' / 'DANC 1100R' (TAMUSA, UVU:
# four digits and a suffix letter), 'ENG/FILM 366' (WKU: one cross-listed course, kept as printed so the list is not cut).
# A placeholder subject ('XXXX 1201', SHSU 2026-27 applied lessons) is not a course code.
# UWM 2026-27 prints subjects of up to seven letters and of two words ('ARTHIST 101', 'BUS ADM 201', 'BIO SCI 150')
# UW-Madison prints eight letters and '&' ('AGROECOL 101', 'F&W ECOL 248', 'I&C SCI 31'); a connective or other word printed in
# capitals before a number is not a subject ('OR BIL 412', 'MINOR IN 300', 'GRADES 101')
SUBJ = r'(?!(?:OR|AND|IN|OF|AT|TO)\s[A-Z])(?!(?:HOURS|GRADES|MINOR|TOTAL|LEVEL)\b)[A-Z][A-Z&]{0,7}'  # 'OR 541' / 'AT 310' are subjects; hyphenated subjects ('INTER-AG 155') are held by CODEISH, not read
CODE = rf'(?!X{{3,}}\b|X{{3,}}\d){SUBJ}(?:\s[A-Z&]{{1,5}})?(?:/[A-Z&]{{1,8}})*\s?\d{{3,4}}[A-Z]?'
# a row that starts like a course but is not one code (joined, cross-listed, ranged): held as complex, never dropped
CODEISH = re.compile(r'^[A-Z][A-Z&]{0,9}(?:-[A-Z]{1,4})?[\s/]|^[A-Z][A-Z&]{1,9}\d')  # also 'COMPLITTHT 3120', 'E&ES215 & E&ES216'
CODE_CELL = re.compile(rf'^{CODE}$')
OR_ROW = re.compile(rf'^or\s+({CODE})$')
# Rows that print more than one course in the code cell are held with a reason naming the shape (issue #95 recovery).
PAIR_CODE = re.compile(r'\d{3,4}[A-Z]?\s*/\s*\d{3,4}')  # 'BIOL 1306/1106' (TAMUSA): a lecture and its lab


def complex_reasons(text):
    if PAIR_CODE.search(text): return {'complex_course_row', 'lecture_lab_pair_code'}
    if '&' in text: return {'complex_course_row', 'joined_courses_row'}
    return {'complex_course_row'}
NOT_REQUIRED_HEADING = re.compile(r'\b(recommended|suggested|electives?|options?|optional|choose|select|sample|example)\b', re.I)
CREDIT_CELL = re.compile(r'^\d{1,2}(\s*-\s*\d{1,2})?$')


def _item(cells):
    item = {'code': cells[0], 'title': cells[1] if len(cells) > 1 else ''}
    cr = cells[2] if len(cells) > 2 else ''
    if CREDIT_CELL.match(cr): item['credits'] = int(cr) if cr.isdigit() else cr
    return item


def course_list_groups(table):
    """[(section, group)] for one Course List table; group = {'group_type', 'courses', 'rule_text'?, 'choose_count'?,
    'choose_credits'?, 'issues'}."""
    out, section, cur = [], (table.get('heading') or '').strip(), None

    def close():
        nonlocal cur
        if cur and not cur['courses'] and cur['group_type'] in ('choose_courses', 'choose_credits') and re.search(r'\b(following|below|list|series|tracks?|options?|groups?|areas?)\b', cur['rule_text'], re.I):
            cur['issues'].add('options_not_read')  # 'Select 2 credits from the following courses' whose list sits under sub-headings
        if cur and not cur['courses'] and cur['group_type'] in ('choose_courses', 'choose_credits') and not cur['issues']:
            # 'Select an additional 7 credits from courses that count toward either major.': a printed rule, no list
            cur = {'group_type': 'elective_pool', 'course_rules': [cur['rule_text']], 'rule_text': cur['rule_text'], 'courses': [], 'issues': set(),
                   **({'choose_credits': cur['choose_credits']} if 'choose_credits' in cur else {})}
            out.append((section, cur)); cur = None; return
        if cur and (cur['courses'] or cur['issues']):  # a group held for review is still reported
            if cur['group_type'] == 'all_required' and NOT_REQUIRED_HEADING.search(f"{table.get('heading') or ''} {section}"):
                cur['issues'].add('heading_not_all_required')  # 'Recommended ... Elective Coursework', 'Options'
            out.append((section, cur))
        cur = None

    for row in table.get('rows') or []:
        cells = [c.strip() for c in row]
        while cells and cells[-1] == '': cells.pop()
        if not cells or cells[:3] == ['Code', 'Title', 'Credits']: continue
        first = cells[0]
        orm = OR_ROW.match(first)
        if orm:
            if cur and cur['courses'] and 'code' in cur['courses'][-1] or (cur and cur['courses'] and 'any_of' in cur['courses'][-1]):
                prev = cur['courses'][-1]
                opts = prev['any_of'] if 'any_of' in prev else [prev]
                cur['courses'][-1] = {'any_of': opts + [{'code': orm.group(1), 'title': cells[1] if len(cells) > 1 else ''}]}
            elif cur is not None:
                cur['issues'].add('alternative_without_course')
            continue
        is_code = bool(CODE_CELL.match(first))
        complex_code = not is_code and bool(CODEISH.match(first.replace('\u200b', ''))) and bool(re.search(r'\d{3}', first)) and len(first) < 40
        has_credits = len(cells) >= 2 and bool(CREDIT_CELL.match(cells[-1]))
        if SELECT.match(LEAD_IN.sub('', first)):
            close()
            cnt, crd = COUNT.match(LEAD_IN.sub('', first)), CREDITS.match(LEAD_IN.sub('', first))
            cur = {'rule_text': first + (f' {cells[-1]}' if has_credits else ''), 'courses': [], 'issues': set()}
            if cnt: cur['group_type'] = 'choose_courses'; w = cnt.group(1).lower(); cur['choose_count'] = NUMBER_WORDS.get(w) or int(w)
            elif crd: cur['group_type'] = 'choose_credits'; cur['choose_credits'] = _num(crd.group(1))
            else: cur['group_type'] = 'choose_unclear'; cur['issues'].add('choose_number_not_printed')
            continue
        if is_code or complex_code:
            choosing = cur is not None and cur['group_type'] != 'all_required'
            if choosing and not has_credits:
                if complex_code: cur['issues'] |= complex_reasons(first)
                else: cur['courses'].append(_item(cells))
                continue
            if choosing and has_credits and not cur['courses']:  # 'Select one of the following math pairs' + pairs with credits
                cur['issues'].add('options_print_credits')
                if complex_code: cur['issues'] |= complex_reasons(first)
                else: cur['courses'].append(_item(cells))
                continue
            if cur is None or cur['group_type'] != 'all_required':
                close(); cur = {'group_type': 'all_required', 'courses': [], 'issues': set()}
            if complex_code: cur['issues'] |= complex_reasons(first)
            else:
                cur['courses'].append(_item(cells))
                if not has_credits: cur['issues'].add('required_course_without_credits')
            continue
        # a heading row (text only) or a text requirement row (text + credits) ends the current group
        close()
        if len(cells) == 1: section = first
    close()
    return out


def list_candidates(inst, entry, page, year, year_line, program_key):
    acad = academic_year_of(year)
    out, n = [], 0
    for t in page.tables:
        if (t.get('caption') or '').strip().lower() != 'course list': continue
        for section, g in course_list_groups(t):
            n += 1
            gt = g['group_type']
            rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': gt if gt != 'choose_unclear' else 'elective_pool',
                  'category': 'major_core' if gt == 'all_required' else 'major_elective', 'courses': g['courses'],
                  'source_section': ' — '.join(x for x in ((t.get('heading') or '').strip(), section) if x) if section != (t.get('heading') or '').strip() else section}
            if g.get('rule_text'): rd['rule_text'] = g['rule_text']
            if gt == 'choose_unclear': rd['course_rules'] = [g['rule_text']]
            if g.get('course_rules'): rd['course_rules'] = g['course_rules']
            if not rd['courses']: del rd['courses']
            for k in ('choose_count', 'choose_credits'):
                if k in g: rd[k] = g[k]
            key = f'list-{n}-{slug(section or "requirements")}'[:90]
            rec = {'program_key': program_key, 'requirement_key': key, 'requirement_kind': 'major', 'rule_details': rd}
            ev = [{'field': 'source_section', 'value': section, 'snippet': section[:200]}] + ([{'field': 'rule_text', 'value': g['rule_text'], 'snippet': g['rule_text'][:200]}] if g.get('rule_text') else [])
            out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, LIST_EXTRACTOR,
                                   {'program_key': program_key, 'requirement_key': key}, {'courses': len(g['courses'])}, sorted(g['issues'])))
    return out


# ---- Course List tables read with their layout (courselist_html/v1) ---------------------------------------------
# Input: programs.courselist_html tables (row classes, leading indentation). Rules (independent review 2026-10-05):
#   * 'areaheader' / 'areasubheader' rows are section headings;
#   * a non-indented course row is required; consecutive ones form one all_required group;
#   * a non-indented rule row (Select / Choose / "N of the following" / "One of the following") opens a choice whose
#     options are the indented rows that follow it; the choice ends at the next non-indented row;
#   * "or ..." rows join the previous course as {"any_of": [...]}; a joined/cross-listed/range code is not representable;
#   * held with an issue: reference or track tables (approved / distribution / area / group / courses offered /
#     recommended / suggested / sample / option / track / concentration / focus / domain / emphasis / honors / elective
#     headings, or a context paragraph saying to select one or more of them), tables naming one award on a page whose
#     program has several, counts at or above the number of listed options, "up to" / "can include" rules, printed
#     credit ranges for a choice, text options, and any row the reader cannot represent exactly.
HTML_EXTRACTOR = 'courselist_html/v1'
# a heading that prints a choice: 'Prescribed Electives (Choose 9 hours)', 'Major Electives - Select 12 credits'
HEADER_CHOICE = re.compile(r'(\(|[-–:]\s*)(choose|select|complete|take)\s+(one|two|three|four|five|six|\d+)\b', re.I)
RULE_ROW = re.compile(r'^(select|choose|complete|take)\b|^students\s+must\s+(take|complete|select|choose)\s+(an?\s+additional\s+|at\s+least\s+)?\d{1,2}\s+(additional\s+)?(credit\s+hours|credits|hours)\s+(from|of)\s+the\s+following\b|^(one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b.*\b(of|from)\b.*\b(following|list|below)\b|^(one|two|three|four|five|\d+)\s+(courses?\s+)?(of|from)\b', re.I)
REFERENCE_HEADING = re.compile(r'\b(approved|distribution|area\s+[ivx\d]+|group\s+[a-z\d]\b|courses offered|ensembles?|recommended|suggested|sample|example|'
                               r'options?|tracks?|concentrations?|focus|focal|domains?|emphas[ie]s|specialization|honors|electives?|pass/no pass)\b', re.I)
TRACK_HEADING = re.compile(r'\b(options?|tracks?|concentrations?|focus|focal|domains?|emphas[ie]s|specialization|honors)\b', re.I)
CONTEXT_CHOICE = re.compile(r'\b(select|choose|complete)\s+(one|two|at least one|one or more)\b[^.]*\b(focus areas?|tracks?|options?|concentrations?|areas?|domains?|emphases)\b|\bsuggested course combinations\b', re.I)
AWARD_IN_HEADING = re.compile(r'\b(Bachelor of [A-Z][a-z]+|B\.?A\.?|B\.?S\.?|B\.?F\.?A\.?|B\.?M\.?)\b(?![a-z])')
OR_CODE = OR_ROW


def strip_marks(text, tail):
    """A title cell's text without the footnote markers printed at its very end in <sup> ('Strategic Management 3', layout
    sup_tail '3' -> 'Strategic Management'; a tail '2,4' too). Only a tail the stored layout recorded as superscripts is
    removed: a number that is part of the title ('Programming Fundamentals 1') has no <sup> and stays, and a superscript
    inside a title ('20th Century') is not at the end. Layouts stored before superscripts were recorded carry no
    sup_tail and are unchanged."""
    if not tail or not text.endswith(tail) or not text[:-len(tail)].strip(): return text
    return text[:-len(tail)].rstrip()


def _row(r):
    cells = r.get('cells') or []
    first = cells[0] if cells else {'text': '', 'indent': False}
    text = (first.get('text') or '').strip()
    credits = (cells[-1].get('text') or '').strip() if len(cells) > 1 else ''
    title = strip_marks((cells[1].get('text') or '').strip(), cells[1].get('sup_tail')) if len(cells) > 2 or (len(cells) == 2 and first.get('colspan', 1) == 1) else ''
    cls = set(r.get('classes') or []) | set(first.get('spans') or [])
    return {'text': text, 'title': title, 'credits': credits if CREDIT_CELL.match(credits) else '', 'indent': bool(first.get('indent')),
            # '&' outside the subject joins courses; 'F&W ECOL 448' is one course
            'inner': bool(first.get('inner_indent')) or bool(re.search(r'\s&\s|\d.*&', text)), 'header': bool(cls & {'areaheader', 'areasubheader'}),
            'or': 'orclass' in cls or text.lower().startswith('or '), 'code': bool(CODE_CELL.match(text)),
            'codeish': bool(CODEISH.match(text.replace('\u200b', ''))) and bool(re.search(r'\d{3}', text)) and len(text) < 90}


def _course(rw):
    item = {'code': rw['text'], 'title': rw['title']}
    if rw['credits']: item['credits'] = int(rw['credits']) if rw['credits'].isdigit() else rw['credits']
    return item


def html_groups(table, program_awards=1, extra_issues=None):
    """[(section, group)] for one stored course-list table."""
    heading, context = (table.get('heading') or '').strip(), table.get('context') or ''
    out, section, cur = [], '', None
    parent = ''  # the main heading over sub-headings ('Prescribed Electives (Choose 9 hours)' over 'Cross-Cutting Issues')
    table_issues = set(extra_issues or ())
    held_until_header = False
    last_text_ended_choice = [None]
    if CONTEXT_CHOICE.search(context): table_issues.add('context_says_choose_among_tables')
    if program_awards > 1 and AWARD_IN_HEADING.search(heading) and not re.search(r'major requirements', heading, re.I):
        table_issues.add('award_specific_table')

    def close():
        nonlocal cur
        if cur is None: return
        g = cur; cur = None
        if not g['courses'] and not g['rules']:
            if g['type'] == 'all_required' and not g['issues']: return  # a row held for its shape is reported, not dropped
            if re.search(r'\b(following|below|list)\b', g.get('rule_text', ''), re.I) or not g.get('rule_text'):
                g['issues'].add('options_not_read')
            else:  # 'Select an additional 7 credits from courses that count toward either major.': a printed rule, no list
                g['type'] = 'choose_unclear'; g['rules_only'] = True
        where = f'{heading} {section}'
        if HEADER_CHOICE.search(parent if parent != section else '') or HEADER_CHOICE.search(section or ''):
            g['issues'].add('heading_prints_choice')  # TAMUSA 'Prescribed Electives (Choose 9 hours)': the lists below are its options
        if g['type'] == 'all_required' and REFERENCE_HEADING.search(where) and not re.search(r'\b(major|core) requirements\b', section, re.I):
            g['issues'].add('reference_or_track_heading')  # a list under 'Approved ...' / 'Electives' / 'Option' is not a required list
        elif g['type'] != 'all_required' and TRACK_HEADING.search(where):
            g['issues'].add('track_heading')  # a choice inside one track or option applies only to that track
        if g['type'] == 'choose_courses' and g.get('choose_count', 0) >= len(g['courses']) + len(g['rules']):
            g['issues'].add('count_not_below_options')
        if g.get('rule_text') and re.search(r'\b(up to|can include|may include|at most|or an? (additional|other)|or another|advisor approval|approved by)\b', g['rule_text'], re.I):
            g['issues'].add('rule_mixes_other_courses')
        if g['rules']: g['issues'].add('text_option')
        titles = ' '.join(c.get('title', '') for c in g['courses'] for c in (c.get('any_of') or [c]))
        if SUBSTITUTE.search(titles): g['issues'].add('substitute_in_title')  # '(May be replaced by SOC 207)', '(or above)', '(or)'
        if RULE_ROW.match(section or ''): g['issues'].add('section_label_is_rule')
        if held_until_header: g['issues'].add('after_subheading_inside_choice')
        if not table.get('sups_recorded') and any(FOOTNOTED.search(c.get('title', '')) for x in g['courses'] for c in (x.get('any_of') or [x])):
            # a title ending in a number, read from a layout stored before superscripts were recorded: the number may be a
            # footnote marker ('Strategic Management 3', issue #129); held until the page is re-fetched
            g['issues'].add('title_number_unchecked')
        if g['type'] == 'all_required' and g.get('starts_after_rule'):
            g['issues'].add('follows_rule_without_options')  # 'One of the following:' + unindented courses (UO Math & CS)
        g['issues'] |= table_issues
        out.append((section or heading, g))

    for r in table.get('rows') or []:
        rw = _row(r)
        if not rw['text'] or rw['text'] in ('Code',) or re.match(r'^total (credits|hours)', rw['text'], re.I): continue
        ended_by_text, last_text_ended_choice[0] = last_text_ended_choice[0], None
        if rw['header']:
            sub = 'areasubheader' in (r.get('classes') or [])
            if cur is not None and cur['type'] != 'all_required' and sub:
                cur['issues'].add('subheading_inside_choice')  # 'Group 1 / Group 2' or 'Series' under one rule: structure not representable
                close(); held_until_header = True
            else:
                close()  # the group before a main heading still belongs to the held span
                if not sub: held_until_header = False
            if not sub: parent = rw['text']
            section = rw['text']; continue
        if rw['or']:
            m = OR_CODE.match(rw['text'])
            if cur and cur['courses'] and m:
                prev = cur['courses'][-1]
                opts = prev['any_of'] if 'any_of' in prev else [prev]
                cur['courses'][-1] = {'any_of': opts + [{'code': m.group(1), 'title': rw['title']}]}
            elif cur is not None:
                cur['issues'].add('alternative_not_representable')
            else:
                cur = {'type': 'all_required', 'courses': [], 'rules': [], 'issues': {'alternative_not_representable'}}
            continue
        if not rw['indent']:
            if rw['code'] or rw['codeish']:
                if cur is None or cur['type'] != 'all_required':
                    after_rule = cur is not None and cur['type'] != 'all_required' and not cur['courses'] and not cur['rules']
                    close(); cur = {'type': 'all_required', 'courses': [], 'rules': [], 'issues': set(), 'starts_after_rule': after_rule}
                if rw['code'] and not rw['inner']: cur['courses'].append(_course(rw))
                else: cur['issues'] |= complex_reasons(rw['text'])
                continue
            if ALL_FOLLOWING.match(rw['text']):
                close(); cur = {'type': 'all_required', 'courses': [], 'rules': [], 'issues': set(), 'all_following': True}
                continue
            if RULE_ROW.match(rw['text']):
                close()
                t = rw['text'] + (f" {rw['credits']}" if rw['credits'] else '')
                rule = LEAD_IN.sub('', rw['text'])
                crd = CREDITS.match(rule); cnt = COUNT.match(rule) or (None if crd else COUNT_NAMED.match(rule))
                cur = {'type': 'choose_unclear', 'courses': [], 'rules': [], 'issues': set(), 'rule_text': t}
                if cnt: cur['type'] = 'choose_courses'; w = cnt.group(1).lower(); cur['choose_count'] = NUMBER_WORDS.get(w) or int(w)
                elif crd:
                    cur['type'] = 'choose_credits'; cur['choose_credits'] = _num(crd.group(1))
                    if re.search(r'\d\s*-\s*\d', rw['text']): cur['issues'].add('credit_range')
                    # 'Select 48 hours of Electives/Minor | 45' (UNL): the rule and its hours cell disagree
                    if (rw['credits'] or '').strip().isdigit() and cur['choose_credits'] != int(rw['credits']): cur['issues'].add('rule_credits_differ_from_hours')
                else:
                    m = re.match(r'^(one|two|three|four|five|six|\d+)\b', rw['text'], re.I)
                    if m: cur['type'] = 'choose_courses'; w = m.group(1).lower(); cur['choose_count'] = NUMBER_WORDS.get(w) or int(w)
                    else: cur['issues'].add('choose_number_not_printed')
                # 'Select one course each from ACE outcomes 5, 7, and 9 | 9' (UNL): one per area, so the number of courses is
                # not printed as a count
                if re.search(r'\beach\b', rule, re.I): cur['issues'].add('count_per_area')
                continue
            was_choice = cur is not None and cur['type'] != 'all_required' and not rw['credits']
            close()  # any other non-indented text row (a requirement printed as text) ends the group; it is not a group itself
            if was_choice and out: last_text_ended_choice[0] = out[-1][1]  # if indented rows follow, the text was part of the option list
            continue
        # indented row: an option of the open choice
        if cur is not None and cur['type'] == 'all_required' and cur['courses'] and not cur.get('all_following'):
            cur['issues'].add('indented_rows_after_required_course')  # 'DATA 488 ... (or)' + indented alternatives (Linfield)
        if cur is None and ended_by_text is not None:
            ended_by_text['issues'].add('choice_continues_after_text')  # 'Alternative Approved Courses:' + more options
        if cur is not None and cur.get('all_following') and not cur['rules']:
            pass  # 'Complete the following courses:' + indented courses: all of them are required
        elif cur is None or cur['type'] == 'all_required':
            close(); cur = {'type': 'choose_unclear', 'courses': [], 'rules': [], 'issues': {'indented_rows_without_rule'}}
        if rw['code'] and not rw['inner']: cur['courses'].append(_course(rw))
        elif rw['codeish']: cur['issues'] |= complex_reasons(rw['text'])
        else: cur['rules'].append(rw['text'])
    close()
    return out


SUBSTITUTE = re.compile(r'substitut|replac|in lieu|waiv|exception|equivalent|or above|\(or\b|may count|proficiency|placement', re.I)
MAIN_TABLE = re.compile(r'\b((major|degree|pre-major|program) requirements|curriculum|core)\b', re.I)
PARALLEL = re.compile(r'^(.+?)\s*(\([^)]+\)\s*Major Requirements|Major\s*[-–]\s*.+)$', re.I)
# a pick from this table: 'Complete one course from:', 'Choose one course from the following', 'Select One:'; never a degree total
# ('requires a minimum of 120 total hours', 'must complete 40 courses in total')
CONTEXT_PICK = re.compile(r'\b(select|choose|complete|take)\s+(one|two|three|four|five|six|[1-9])\s+(?:(?:course|class)(?:e?s)?\s+)?(?:of|from)\s*(?:the\s+following|the\s+list|this\s+list|:)'
                          r'|^\s*(select|choose)\s+(one|two|three|four|five|six|[1-9])\s*:?\s*$', re.I | re.M)
GER_BOILERPLATE = re.compile(r'body of knowledge as a context for specialization', re.I)  # UWM 2026-27 General Education Requirements
TRACK_PROSE = re.compile(r'\b(choose one track|focus areas?|specializations?|concentrations?|tracks? from|one of the following (tracks|options|concentrations|areas))\b', re.I)
NOT_REQUIREMENT_HEADING = re.compile(r'^(contact information|program educational objectives|double-counting policy|internships?|learning outcomes|'
                                     r'student learning outcomes|program learning outcomes|overview|admission|advising)$', re.I)


def substitution_codes(page_text):
    """Course codes named in the page's own substitution / waiver notes ('MATH 241, MATH 246, or MATH 251Z may be
    substituted'; 'STAT 243Z ... can be taken as substitutes for SOC 312')."""
    codes = set()
    for line in (page_text or '').split('\n'):
        if re.search(r'substitut|in lieu|waive|may be replaced|placement (exam|test)|proficiency (exam|test)', line, re.I):
            # 'in lieu of PHYSICS 125A' (UCI), 'STAT 1772 will substitute for SOC SCI 2020' (UNI)
            found = {re.sub(r'\s+', ' ', m) for m in re.findall(r'\b[A-Z][A-Z&]{1,7}(?:[\s\u00a0][A-Z&]{1,5})?[\s\u00a0]\d{3,4}[A-Z]?\b', line)}
            codes |= found or {'*footnote*'}  # a note naming no course ('Placement test may waive the course requirement.')
    return codes


FOOTNOTED = re.compile(r'\s\d{1,2}(,\s?\d{1,2})*$')


def html_candidates(inst, entry, cl_entry, tables, year, program_key, program_awards, page_text=''):
    """Table-level holds (second independent review): every Course List table after a page's first is held unless its
    heading names the major/degree requirements, curriculum or core; parallel tables ('Classics (Greek) Major
    Requirements', 'X Major - Y') are all held; once a table's preceding prose says to choose a track / focus area /
    specialization / concentration, that table and every later one is held."""
    acad = academic_year_of(year)
    out, n = [], 0
    lists = [t for t in tables if (t.get('caption') or 'Course List').strip().lower() == 'course list']
    parallel = sum(1 for t in lists if PARALLEL.match((t.get('heading') or '').strip())) >= 2
    tracks_from_here = False
    # TAMUSA opens each program with a credits overview ('Core Curriculum | 42', 'Major Courses | 36', ..., 'Total Credits |
    # 120'): every row an area label with no digits and its hours, ending in a Total row. That table is a summary, not the
    # program's own requirement table, so it does not take the 'first table' place. Nothing else is skipped.
    def overview(t):
        rows = [[(c.get('text') or '').strip() for c in (r.get('cells') or [])] for r in t.get('rows') or [] if 'hidden' not in (r.get('classes') or [])]
        rows = [[c for c in r if c] for r in rows if any(r)]
        if TERM.search((t.get('heading') or '').strip()) or re.search(r'\b(fall|spring|summer|winter)\b', t.get('heading') or '', re.I):
            return False  # Iowa State Accelerated Nursing: 'First Year Summer' is a term of the plan, not an overview
        return (len(rows) >= 3 and re.match(r'^total\b', rows[-1][0], re.I) is not None
                and all(len(r) == 2 and not re.search(r'\d', r[0]) and re.fullmatch(r'\d{1,3}(\s*[-–]\s*\d{1,3})?', r[1]) for r in rows))
    idx = -1
    for t in lists:
        idx += 0 if idx < 0 and overview(t) else 1
        heading = (t.get('heading') or '').strip()
        extra = set()
        if idx > 0 and not MAIN_TABLE.search(heading): extra.add('secondary_table')
        if parallel and PARALLEL.match(heading): extra.add('parallel_tables')
        # UWM's general education paragraph ('... a broad body of knowledge as a context for specialization') is not a choice
        ctx = GER_BOILERPLATE.sub('', t.get('context') or '')
        if CONTEXT_CHOICE.search(ctx) or TRACK_PROSE.search(ctx): tracks_from_here = True
        # 'Complete one course from:' / 'Select One:' / 'a minimum of ...' printed above the table: its rows are choices
        if CONTEXT_PICK.search(ctx): extra.add('context_says_choose')
        if tracks_from_here: extra.add('context_says_choose_among_tables')
        # the nearest heading can be the department's GPA policy printed above the table (TAMUSA 'Department withdrawal')
        label = '' if NOT_REQUIREMENT_HEADING.match(heading) or re.search(r'\b(probation|withdrawal)\b', heading, re.I) else heading
        subs = substitution_codes(page_text)
        for section, g in html_groups(t, program_awards, extra):
            n += 1
            items = [c for x in g['courses'] for c in (x.get('any_of') or [x])]
            if g['type'] == 'all_required' and (subs & {c['code'] for c in items} or
                                                 ('*footnote*' in subs and any(FOOTNOTED.search(c.get('title', '')) for c in items))):
                g['issues'].add('substitution_noted_on_page')  # a footnoted course on a page whose notes allow a waiver or substitute
            gt = {'choose_unclear': 'elective_pool'}.get(g['type'], g['type'])
            rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': gt,
                  'category': 'major_core' if gt == 'all_required' else 'major_elective',
                  'source_section': ' — '.join(x for x in dict.fromkeys((label, '' if section == heading else section)) if x) or 'Course List'}
            if g['courses']: rd['courses'] = g['courses']
            if g.get('rule_text'): rd['rule_text'] = g['rule_text']
            rules = ([g['rule_text']] if gt == 'elective_pool' and g.get('rule_text') else []) + g['rules']
            if rules: rd['course_rules'] = rules
            for k in ('choose_count', 'choose_credits'):
                if k in g: rd[k] = g[k]
            key = f'major-{n}-{slug((section if section != heading else "") or label or "requirements")}'[:90]
            rec = {'program_key': program_key, 'requirement_key': key, 'requirement_kind': 'major', 'rule_details': rd}
            ev = [{'field': 'source_section', 'value': rd['source_section'], 'snippet': rd['source_section'][:200]}]
            if g.get('rule_text'): ev.append({'field': 'rule_text', 'value': g['rule_text'], 'snippet': g['rule_text'][:200]})
            c = common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, HTML_EXTRACTOR,
                            {'program_key': program_key, 'requirement_key': key}, {'courses': len(g['courses'])}, sorted(g['issues']))
            c['layout_source'] = {'url': cl_entry['url'], 'sha256': cl_entry.get('sha256')}
            out.append(c)
    return out


# ---- Roadmap grids read with their cell positions (courseleaf_plangrid/v1) ---------------------------------------
# UAF 2026-27 prints its semester roadmaps as `table.sc_plangrid` with two (or three) terms side by side. The shared page
# parser flattens a row into its cells, so an option row printed under one term's "Complete one of the following:" loses
# its column, and footnote markers run into the course code ('MATH F251X6'). This reader takes the grid as stored by
# programs.courselist_html.plan_grids: every cell names its year and term column in its `header` attribute
# ('year0 year0_Term1_codecol'), footnote markers are the cell's <sup> text, and an option row is indented under its
# rule. Nothing is inferred: a cell without a column, an indented row with no open rule in its column, or a marker that is
# not at the end of a cell holds the plan.
PLANGRID_EXTRACTOR = 'courseleaf_plangrid/v1'
# 'MATH F251X' (UAF), 'BIOL 2403' (SHSU: four digits), 'ENGLSH 1000' / 'AG_S_TCH 1020' (Missouri)
GRID_CODE = re.compile(r'^([A-Z]{2,5}|[A-Z][A-Z_]{1,8})\s(F?\d{3,4}[A-Z]?)$')
GRID_COL = re.compile(r'^(year\d+)_(Term\d+)_(codecol|hourscol)$')
GRID_CHOICE = re.compile(r'^(?:complete|select|choose|take)\s+(?:one|two|three|\d+)\s+of\s+the\s+following\s*:?$', re.I)
RECOMMENDED = re.compile(r'\s*\(\*\)$')


def _credits(s):
    s = (s or '').strip()
    return int(s) if s.isdigit() else s


class _Col:  # a term column found by position (SHSU), shaped like a GRID_COL match
    def __init__(self, year, pos, kind): self.g = (year, pos, kind)
    def group(self, i): return self.g[i - 1]


def _positioned(cells):
    """(column position, cell) for each cell: a cell spans `colspan` columns of the printed grid."""
    pos = 0
    for c in cells:
        yield pos, c
        pos += int(c.get('colspan') or 1)


def parse_plangrid(t, footnote_defs):
    """(terms, total, issues) of one roadmap grid.
    SHSU 2026-27 prints its grids without column headers on the cells ('undefinedcodecol'): a cell's column is then its
    position in the row (colspans counted), and its term is the term label printed at that position in the year's term
    row ('Fall | Hours | Spring | Hours | Summer | Hours'); a code cell sits in its term's column and an hours cell in the
    column after it. Any other cell with text, or a column with no printed term, holds the plan."""
    years, terms, by_col, issues, total = {}, [], {}, set(), None
    positional = not any(GRID_COL.match(h) for row in t.get('rows') or [] for c in row.get('cells') or [] for h in (c.get('header') or '').split())
    year = None
    for row in t.get('rows') or []:
        cls, cells = row.get('classes') or [], row.get('cells') or []
        if 'plangridyear' in cls:
            for c in cells:
                if c.get('id'): years[c['id']] = c['text']
            if positional:
                year = ' '.join(c['text'] for c in cells if c.get('text')).strip() or None
            continue
        if 'plangridterm' in cls:
            if positional:
                for pos, c in _positioned(cells):
                    if c.get('text') and 'hourscol' not in (c.get('classes') or []):
                        term = {'term_index': len(terms) + 1, 'label': f"{year or ''} {c['text']}".strip(), 'items': []}
                        terms.append(term); by_col[(year, pos)] = {'term': term, 'open': None}
                continue
            for c in cells:
                m = GRID_COL.match(c.get('id') or '')
                if m and m.group(3) == 'codecol':
                    term = {'term_index': len(terms) + 1, 'label': f"{years.get(m.group(1), m.group(1))} {c['text']}".strip(), 'items': []}
                    terms.append(term); by_col[(m.group(1), m.group(2))] = {'term': term, 'open': None}
            continue
        if 'plangridtotal' in cls:
            # 'Total Credits 120' (UAF), 'Total Hours: 120-121' (SHSU)
            m = re.search(r'(total (?:credits|hours)):?\s+(\S+)', ' '.join(c['text'] for c in cells), re.I)
            if m: total = m.group(2); t['_total_label'] = m.group(1)
            continue
        slots = {}
        for pos, c in _positioned(cells):
            if positional:
                kinds = [k for k in ('codecol', 'hourscol') if k in (c.get('classes') or [])]
                cols = [_Col(year, pos if kinds[0] == 'codecol' else pos - 1, kinds[0])] if len(kinds) == 1 else []
            else:
                cols = [GRID_COL.match(h) for h in (c.get('header') or '').split()]
                cols = [m for m in cols if m]
            if not cols:
                if c['text']: issues.add('grid_cell_without_column')
                continue
            m = cols[0]; slots.setdefault((m.group(1), m.group(2)), {})[m.group(3)] = c
        for col, s in slots.items():
            if col not in by_col:  # UAF Fifth Year with one term: its sum row still prints an empty second-term cell
                if any(x.get('text') for x in s.values()): issues.add('grid_cell_without_term')
                continue
            st = by_col[col]
            hours = (s.get('hourscol') or {}).get('text', '')
            if 'plangridsum' in cls:
                if hours: st['term']['credit_hours'] = hours
                continue
            code = s.get('codecol')
            if not code or not code['text']:
                if hours: issues.add('credits_without_item')
                continue
            text, sups = code['text'], code.get('sups') or []
            marks = [n for x in sups for n in re.split(r'\s*,\s*', x) if n]  # one <sup> may print several ('20,25')
            if sups:
                tail = code.get('sup_tail') or ''
                if tail and text.endswith(tail): text = text[:-len(tail)].rstrip()
                else: issues.add('footnote_inside_cell')
            item = {}
            if RECOMMENDED.search(text): text = RECOMMENDED.sub('', text); item['recommended'] = True
            m = GRID_CODE.match(text)
            item = {('code' if m else 'text'): (f'{m.group(1)} {m.group(2)}' if m else text), **item}
            if hours: item['credits'] = _credits(hours)
            if marks:
                item['footnotes'] = marks
                if any(n not in footnote_defs for n in marks): issues.add('footnote_not_defined')
                elif any(footnote_defs[n] is None for n in marks): issues.add('footnote_definition_unclear')
            if code.get('indent'):
                if st['open'] is None: issues.add('indented_row_without_rule'); st['term']['items'].append(item)
                else: st['open'].setdefault('options', []).append(item)
                continue
            st['open'] = item if GRID_CHOICE.match(text) else None
            st['term']['items'].append(item)
    for st in by_col.values():
        for it in st['term']['items']:
            if GRID_CHOICE.match(it.get('text', '')) and not it.get('options'): issues.add('rule_without_options')
    if positional:  # columns found by position are checked against the printed sums: each term's hours, then the total
        issues |= _sum_issues(terms, total)
    return terms, total, issues


def _span(v):
    m = re.fullmatch(r'(\d+(?:\.\d+)?)(?:\s*-\s*(\d+(?:\.\d+)?))?', str(v).strip())
    return (float(m.group(1)), float(m.group(2) or m.group(1))) if m else None


def _sum_issues(terms, total):
    """Issues when a term's item hours do not add up to its printed subtotal, an item in a summed term prints no hours,
    or the subtotals do not add up to the printed total. A printed range ('3-4') adds as a range."""
    out = set()
    sums = []
    for t in terms:
        if not t.get('credit_hours'): continue
        ch = _span(t['credit_hours'])
        parts = [_span(i['credits']) if 'credits' in i else None for i in t['items']]
        if None in parts or ch is None: out.add('term_item_without_hours'); continue
        lo, hi = sum(p[0] for p in parts), sum(p[1] for p in parts)
        if not ((lo, hi) == ch or (ch[0] == ch[1] and lo <= ch[0] <= hi)): out.add('term_hours_differ')
        sums.append(ch)
    tot = _span(total) if total else None
    if tot and sums:
        lo, hi = sum(a for a, _ in sums), sum(b for _, b in sums)
        if not ((lo, hi) == tot or (tot[0] == tot[1] and lo <= tot[0] <= hi)): out.add('total_hours_differ')
    return out


def page_footnotes(text):
    """Footnotes printed on the page after a grid's 'Total Hours: N' line (SHSU): a line holding only the number, then its
    text on the next printed line. They end where the next section starts ('Course List')."""
    lines = [l.strip() for l in (text or '').splitlines() if l.strip()]
    start = next((i for i, l in enumerate(lines) if re.match(r'^\|?\s*total hours:\s*\S+', l, re.I)), None)
    defs = {}
    if start is None: return defs
    i = start + 1
    while i + 1 < len(lines) and re.fullmatch(r'\d{1,2}', lines[i]):
        nxt = lines[i + 2] if i + 2 < len(lines) else ''
        # a number printed twice (SHSU BSN '9'), or a definition whose next line neither starts another footnote nor the
        # 'Course List' section (it may continue), is not read: a plan that uses it is held
        whole = nxt == '' or re.fullmatch(r'\d{1,2}', nxt) or nxt.startswith('Course List') or re.fullmatch(r'Notes:?', nxt)  # SHSU ends the list at 'Notes'
        defs[lines[i]] = None if (lines[i] in defs or not whole) else lines[i + 1]; i += 2
    return defs


def plangrid_candidates(inst, entry, grid_entry, doc, year, program_key, page_text=None):
    """program_plan candidates for a page's roadmap grids (programs.courselist_html.plan_grids output)."""
    acad = academic_year_of(year)
    defs = {} if doc.get('footnotes') else page_footnotes(page_text)
    for t in doc.get('footnotes') or []:
        for r in t.get('rows') or []:
            for c in r.get('cells') or []:
                m = re.match(r'^(\d+)\s*--\s*(.+)$', c.get('text') or '')
                if m: defs[m.group(1)] = m.group(2).strip()
    grids_ = doc.get('grids') or []
    heads = [(t.get('heading') or '').strip() for t in grids_]
    # UAF prints one roadmap per concentration, each under its own heading ('Robotics Concentration', 'Without
    # Concentration'): distinct headings name the plans, so several grids are not ambiguous there
    labelled = len(grids_) > 1 and len(set(heads)) == len(heads) and all(h and h.lower() != 'roadmaps' for h in heads)
    out = []
    road_keys = labelled_keys(heads, lambda h: f'roadmap-{slug(h)}'[:90]) if labelled else []
    for i, t in enumerate(grids_, 1):
        terms, total, issues = parse_plangrid(t, defs)
        if not terms: continue
        if len(grids_) > 1 and not labelled: issues.add('multiple_plan_grids')
        # an unlabelled grid headed for a track, concentration, dual degree or double major ('Semester Plan - Dual Degree
        # Electrical Engineering and Computer Engineering', Missouri) is that route's plan, not the program's: held until reviewed
        heading = t.get('heading') or ''
        if re.search(r'\b(dual degree|double major)\b', heading, re.I) or (not labelled and re.search(r'\b(concentration|track|emphasis|option)\b', heading, re.I)):
            issues.add('plan_heading_label')  # another program's plan is held even when labelled; a labelled track plan is keyed to its track
        key = 'roadmap' if len(grids_) == 1 else (road_keys[i - 1] if labelled else f'roadmap-{i}')
        used = sorted({n for term in terms for it in term['items'] for x in [it, *it.get('options', [])] for n in x.get('footnotes', [])}, key=lambda n: (len(n), n))
        rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence',
              'terms': terms, 'source_section': (heads[i - 1] if labelled else (t.get('heading') or 'Roadmap').strip() + (f' {i} of {len(grids_)}' if len(grids_) > 1 else ''))}
        if used: rd['footnotes'] = {n: defs[n] for n in used if defs.get(n)}
        if total: rd['rule_text'] = f"{t.get('_total_label') or 'Total Credits'} {total} (as printed)"
        rec = {'program_key': program_key, 'requirement_key': key, 'requirement_kind': 'program_plan', 'rule_details': rd}
        ev = [{'field': 'term', 'value': term['label'], 'snippet': f"{term['label']}: {len(term['items'])} items, {term.get('credit_hours', '?')} credits"} for term in terms]
        c = common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, PLANGRID_EXTRACTOR,
                        {'program_key': program_key, 'requirement_key': key}, {'terms': len(terms)}, sorted(issues))
        c['layout_source'] = {'url': grid_entry['url'], 'sha256': grid_entry.get('sha256')}
        out.append(c)
    return out


# UNL 2026-27 '4-Year Plans' tab: no plan table; each plan prints its title (a page heading: 'Anthropology (B.A.)',
# 'Finance - Financial Planning'), then per term '<n> creditsYear <k>: <Fall|Spring|Summer>', then rows printed as
# 'Course: <title>' / '<n> credits' / 'Complete <CODE>' or '<requirement>' / '<n> credits', each optionally followed by a
# printed note ('In consultation with your advisor, ...') and 'Milestone: ...' rows (kept as their printed text).
PLANTEXT_EXTRACTOR = 'courseleaf_plantext/v1'
PT_TERM = re.compile(r'^(?P<cr>\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?) credits?(?P<label>Year \d+: (?:Fall|Spring|Summer|Winter|Interim))$')
PT_CREDITS = re.compile(r'^(?P<cr>\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?) credits?$')
PT_CODE = re.compile(r'^Complete ?(?P<code>[A-Z]{2,5} \d{1,4}[A-Z]?)$')  # 'CompleteBSAD 222' (UNL Finance) as printed
PT_MILESTONE = re.compile(r'^Milestone: ')
PT_NOTE = re.compile(r'^(Complete |In consultation |See |Choose |Select |Take |Work with |Recommend)')


def _pt_lines(page):
    # the plan carousel's arrow controls ('<', '>') are printed between rows; zero-width spaces and no-break spaces are layout
    lines = (re.sub(r'\s+', ' ', l.replace('​', '')).strip() for l in page.text.splitlines())
    return [l for l in lines if l and l not in ('<', '>')]


def _pt_credits(s):
    return s if '-' in s else (float(s) if '.' in s else int(s))


def _pt_range(s):
    a, _, b = str(s).partition('-')
    return float(a), float(b or a)


def _pt_note(line, nxt):
    return (not PT_MILESTONE.match(line) and not PT_TERM.match(line) and not (nxt is not None and PT_CREDITS.match(nxt))
            and (bool(PT_NOTE.match(line)) or (line.endswith('.') and len(line) > 20)))


def plantext_plans(page):
    """[(title, terms, issues)] for each printed plan, in page order. A plan's title must be a page heading."""
    lines, heads = _pt_lines(page), {re.sub(r'\s+', ' ', h.replace('​', '')).strip() for h in page.headings}
    out, i = [], 0
    nxt = lambda k: lines[k] if k < len(lines) else None
    while i < len(lines):
        if not PT_TERM.match(lines[i]): i += 1; continue
        # the title is the heading printed right above the first term (UNL prints its 'PLEASE NOTE' preamble before the title)
        t = i - 1
        title = lines[t] if t >= 0 and lines[t] in heads else None
        terms, issues = [], set() if title else {'no_plan_title'}
        while i < len(lines) and PT_TERM.match(lines[i]):
            m = PT_TERM.match(lines[i]); i += 1
            term = {'term_index': len(terms) + 1, 'label': m.group('label'), 'credit_hours': m.group('cr'), 'items': []}
            while i < len(lines) and not PT_TERM.match(lines[i]):
                if PT_MILESTONE.match(lines[i]) and not (nxt(i + 1) and PT_CREDITS.match(nxt(i + 1))):
                    term['items'].append({'text': lines[i]}); i += 1; continue  # a milestone row, as printed ('Milestone: ...')
                if not (nxt(i + 1) and PT_CREDITS.match(nxt(i + 1))) or PT_CREDITS.match(lines[i]): break
                label, cr = lines[i], _pt_credits(PT_CREDITS.match(lines[i + 1]).group('cr')); i += 2
                c = PT_CODE.match(lines[i]) if i < len(lines) else None
                if label.startswith('Course: ') and c:
                    it = {'code': c.group('code'), 'title': label[len('Course: '):], 'credits': cr}; i += 1
                else:
                    it = {'text': label, 'credits': cr}
                    if label.startswith('Course: '): issues.add('course_without_code')
                notes = []
                while i < len(lines) and _pt_note(lines[i], nxt(i + 1)):
                    notes.append(lines[i]); i += 1
                if notes: it['note'] = ' '.join(notes)
                term['items'].append(it)
            cr = [_pt_range(x['credits']) for x in term['items'] if 'credits' in x]
            lo, hi = sum(a for a, _ in cr), sum(b for _, b in cr)
            a, b = _pt_range(term['credit_hours'])
            if not (lo <= a <= hi and lo <= b <= hi): issues.add('term_credits_differ')
            if not any('credits' in x for x in term['items']): issues.add('empty_term')
            terms.append(term)
            if i < len(lines) and not PT_TERM.match(lines[i]): break
        out.append((title, terms, issues))
    if len(out) == 1: out[0][2].discard('no_plan_title')  # the page's one plan is the major's, titled or not
    return out


def plantext_candidates(inst, entry, page, year, program_key):
    """program_plan candidates for a page's printed 4-year plans (UNL), keyed to the page's program record. Each plan keeps
    its printed title (an option or award plan of the major: 'Art - Ceramics (B.A.)') as source_section."""
    acad = academic_year_of(year)
    plans = plantext_plans(page)
    titles = [t or f'plan {k}' for k, (t, _, _) in enumerate(plans, 1)]
    keys = labelled_keys(titles, lambda h: f'plan-{slug(h)}'[:90]) if len(plans) > 1 else ['plan']
    out = []
    for (title, terms, issues), key in zip(plans, keys):
        rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence',
              'terms': terms, 'source_section': title or '4-Year Plans'}
        rec = {'program_key': program_key, 'requirement_key': key, 'requirement_kind': 'program_plan', 'rule_details': rd}
        ev = [{'field': 'term', 'value': term['label'], 'snippet': f"{term['credit_hours']} credits{term['label']}"} for term in terms]
        if title: ev.insert(0, {'field': 'plan_title', 'value': title, 'snippet': title})
        out.append(common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, PLANTEXT_EXTRACTOR,
                               {'program_key': program_key, 'requirement_key': key}, {'terms': len(terms)}, sorted(issues)))
    return out
