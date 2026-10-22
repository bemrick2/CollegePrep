"""Catalog completeness entries from a reviewed decision (the rule used in review since #175).

    python3 -m programs.catalog_counts --run programs/runs/<ST>/<RUN> --decision programs/decisions/<ST>-<RUN>.json
                                       --out entries.json [--year 2026-2027] [--reviewed 2026-10-08] ik [ik ...]

Every bachelor's entry on the official program list is accounted for: counted, or excluded by name as a combined
bachelor's/master's entry, a department / roadmap / general / commissioning link, a concentration or option of a degree
whose own line the list also prints (VCU 'Chemistry, Bachelor of Science (B.S.) with a concentration in biochemistry' beside
'Chemistry, Bachelor of Science (B.S.)': one program, as programs.extract.listed_emphasis_pages reads it), or an entry
printing no award.
A listed program is verified only when an approved record of the reviewed decision prints the same name, or sits on
that program's own page (http and https are one page) when no other listed name shares that page and the listed
name is not the record's name plus a qualifier ('X: Concentration in Y' is never credited through X's page).
Counts come from the reviewed decision's approvals, never from the autoreview file."""
import argparse, json, re
from urllib.parse import urlsplit
from collections import defaultdict
from pathlib import Path

from programs import extract as X

ZWSP = '​'
COMB = re.compile(r"Accelerated.*(\bM\.?[AS]\b\.?|\bMBA\b|\bMPA\b|Master)|Scholars Roadmap|\s\+\s.*\b(M[A-Z]{1,3}|MPA|MBA)\b|\(3\+2\)|\b3-2\b|4\+1|"
                  r"Dual Acceptance|and MBA\b|to MBA|\bB\.?[AS]\.?/\s?M\.?[AS]\b|\bM\.[AS]\.|/\s?(DDS|MD|PharmD|DPT|OTD)\b|\(B[AS]/D|"
                  r"(?-i:\bB[A-Z]{1,4}/M[A-Z]{1,3}\b)|(?-i:\bB[A-Z]{1,4}-M(?:S|A|[A-Z]{2,3})\b)|"  # ODU '..., BS-MBA' (a hyphenated single award such as 'BS-MT' is not combined); La Salle 'Accounting, BSBA/MBA (4 year)'
                  r"\bto\b.*(?-i:\bM[A-Z]{0,4}\b).*\bAccelerated\b|Dual Degree Acceptance|\bB\.?[AS]\.?/.*\bM\.\s?B\.\s?A\b|"
                  r"(?-i:,\s*B[A-Z]{1,3}\s+to\s+[^,]+,\s*M[A-Z]{1,5}\b)|"
                  r"(?-i:\bBachelor of [A-Z][a-z]+(?: [A-Z][a-z]+)*\s*/\s*Master of\b)|^Bachelor's/Master's\b|"
                  r"\bBachelor's to Master's\b|\bto Master of\b", re.I)  # YSU 'Bachelor's to Master's Track'; '... Option to Master of Respiratory Care'  # JHU 2026-27 'Biology, Bachelor of Arts/Master of Science'; the 'Bachelor's/Master's Degrees' heading  # Roosevelt 'Biology, BA to Secondary Education, MA Accelerated Program'; Georgian 'B.S./... M.B.A.'
GENERIC = re.compile(r"^(Bachelor's (Degree|Concentration|Degree Programs)|Department of .*)$|: Bachelor's Degree\b|Minor, Certificate|Graduate Certificate|\bRoadmap\b|\b(Graduation|Continuance)\s+(Requirements|Regulations)\b|\bReadmission\b|\(Secondary Major\)|^Minor in\b|General Education Requirements|\(Double Major\)|^Bachelor's and Master's Degree Programs$|^Requirements for a Bachelor's Degree$|\bDouble Degree Program", re.I)
ROTC = re.compile(r'\bN?ROTC\b')
LABELED = {'labeled_in_title', 'labeled_in_heading', 'labeled_in_source'}
# UTEP 2026-27 cards run the name into the card's category labels: 'BBA in AccountingBusiness, Management, & Marketing
# BachelorsUndergraduateBusiness Administration' (the labels name the level 'Bachelors' and 'Undergraduate')
CATEGORY_RUN = re.compile(r'(?:[A-Z].*)?Bachelors(?:Online|Fast Track|Professional|Undergraduate|[A-Z]|$)')
# Colorado State's Programs A-Z links each concentration from its degree column ('B.S. Concentration') and each dual degree as
# 'Dual Degree B.S.': a concentration row is one program with its major, identified by the major's page
# ('.../computer-science-major-ai-concentration/' -> '.../computer-science-major/'), and each dual degree by its own page
CONC_AWARD = re.compile(r'^(?:Dual Degree\s+)?B\.(?:\s?[A-Z][a-z]{0,3}\.)+\s+Concentration(?:\s+Option)?$')
MAJOR_OF = re.compile(r'(-major)-[^/]*?concentration(/?)$')
# ODU 2026-27 'Programs, Degrees & Majors' rows run the award on to the row's filter labels: 'Art with a Major in Art History,
# BAArtsUndergraduateBachelor'sHumanitiesCollege of Arts and Letters', 'Chemistry with a Major in ... (BS)UndergraduateBachelor's...'
CREDIT_HOURS = re.compile(r'\s*\(\d+(?:-\d+)?\s+semester credit hours\)[\d,\s]*$')
FILTER_LABELS = re.compile(r"(?<=[A-Za-z)])(?:[A-Z][a-z][A-Za-z&' ]*?)?Undergraduate(?:[A-Z][A-Za-z&' ]*?)?Bachelor's.*$")
AWARD_ONLY = re.compile(r'^(?:Dual Degree\s+)?(?:(?-i:B[A-Z]{1,4}[a-z]{0,3})|B\.\s?[A-Z][A-Za-z]{0,4}\.?(?:\s?[A-Z][a-z]{0,3}\.?)*|Bachelor of [A-Z][a-z]+(?: [A-Z][a-z]+)*)\**$')  # Missouri lists 'BA', 'BS*', 'BSAcc' under each department; never an all-caps name ('BIOLOGY')


def page_key(u):
    """One key per page: scheme, '/index.html', trailing slashes and repeated slashes do not make another page."""
    u = re.sub(r'(?<!:)//+', '/', (u or '').split('#')[0])
    return re.sub(r'^https?://', '', re.sub(r'(/index\.html?)?/*$', '', u)).lower()


def name_key(n):
    return re.sub(r'\W+', '', re.sub(r'Toggle.*', '', n or '')).lower()


def card_name(printed):
    """A list card that prints the name twice ('Anthropology, BAAnthropology, BA'; UW-Madison), or a shortened title
    then the name ('Nutritional Sciences, BS Nutritio...Nutritional Sciences, BS Nutrition and Dietetics'): the name."""
    pr = (printed or '').replace(ZWSP, '').strip()
    h = len(pr) // 2
    if len(pr) % 2 == 0 and h and pr[:h] == pr[h:]: return pr[:h], True
    if '...' in pr:
        head, tail = pr.split('...', 1)
        if head and tail.startswith(head): return tail, True
    return pr, False


SPELLED = {'arts': 'ba', 'science': 'bs', 'fine arts': 'bfa', 'music': 'bm', 'business administration': 'bba'}
# 'Bachelor of Fine Arts in Dance (BFA)' (JHU) repeats its award: the same degree, when the parenthesis names it.
WHOLE_DEGREE = [re.compile(r'^Bachelor of (?P<long>Arts|Science|Fine Arts|Music|Business Administration) in (?P<base>[^,:()]+?)(?: \((?P<same>(?-i:B[A-Z]{1,3}))\))?$'),
                re.compile(r'^(?P<award>(?-i:B[A-Z]{1,3})) in (?P<base>[^,:()]+?)$'),
                re.compile(r'^(?P<base>[^,:()]+?) \((?P<award>(?-i:B[A-Z]{1,3}))\)$'),
                re.compile(r'^(?P<base>[^,:()]+?), (?P<award>(?-i:B[A-Z]{1,3}))$')]


DELIVERY_QUALIFIER = re.compile(r'\s*\((?:online|on campus|hybrid|non-?\u200b?rn)\)\s*$', re.I)  # YSU '(Online)', '(Non-RN)'
TRACK_SUFFIX = re.compile(r'\b(?:Track|Option)$')
TRACK_ENTRY = re.compile(r'^(?P<award>Bachelor of (?:Arts|Science|Fine Arts|Music|Business Administration)|(?-i:B[A-Z]{1,3}))\s+in\s+'
                         r'(?P<rest>[^()]+?)\s+(?:Track|Option)$')


def track_of_listed(line, degrees):
    """YSU 2026-27: 'Bachelor of Arts in Multimedia Communication, Public Relations Track' or 'Bachelor of Science in
    Computer Science Cybersecurity Track' beside 'Bachelor of Science in Computer Science': a track of a degree the same
    list prints. True only when some leading part of the name (before a comma, ' - ' or a word boundary) is that listed
    degree with the same award."""
    m = TRACK_ENTRY.match(line)
    if not m: return False
    award = X._award_key(m.group('award'))
    words = re.split(r'(\s+-\s+|,\s*|\s+)', m.group('rest'))
    for i in range(1, len(words) - 1, 2):  # every separator position, leaving at least one word for the track
        base = ''.join(words[:i])
        if (X.name_key_of(base), award) in degrees: return True
    return False


def whole_degree(name):
    """(name, award) of an entry or record that is exactly one degree in one of four printed forms ('Bachelor of Science in X',
    'BS in X', 'X (BS)', 'X, BS'); None for anything else ('Education (BA) with EC-6 Core Subjects')."""
    n = X.list_line(name).replace(ZWSP, '')
    for rx in WHOLE_DEGREE:
        m = rx.match(n)
        if m:
            award = SPELLED[m.group('long').lower()] if 'long' in rx.groupindex else m.group('award').lower()
            if 'same' in rx.groupindex and m.group('same') and m.group('same').lower() != award:
                return None  # 'Bachelor of Science in X (BA)' names two awards: not one whole degree
            return re.sub(r'\W+', '', m.group('base')).lower(), award
    return None


def entries(run_dir, decision, iks, year='2026-2027', reviewed=''):
    run_dir = Path(run_dir)
    cands = {}
    for line in open(run_dir / 'candidates.jsonl'):
        v = json.loads(line); cands.setdefault(v['candidate_id'], v)
    approved = {a['candidate_id'] for a in json.load(open(decision))['approve']}
    lists = json.load(open(run_dir / 'program_lists.json'))
    manifest = {}
    for line in open(run_dir / 'manifest.jsonl'):
        m = json.loads(line); manifest.setdefault(m['url'], m)
    out = []
    for ik in iks:
        # only a record whose catalog year is printed in its source verifies a listed program (an unlabeled Coursedog API
        # record is promoted as partially verified and never counted)
        progs = [v for v in cands.values() if v['institution_key'] == ik and v['domain'] == 'academic_programs' and v['candidate_id'] in approved
                 and v.get('year_basis', 'labeled_in_source') in LABELED]
        names = {name_key(v['record']['program_name']): v for v in progs}
        # one degree printed two ways ('Bachelor of Science in Human Resource Management' and 'Human Resource Management (BS)',
        # UT Dallas 2026) is one program: list entries and records are also keyed by (name, award)
        dkey = lambda n: (lambda d: 'deg:%s|%s' % d if d else None)(whole_degree(n))
        for v in progs:
            if dkey(v['record']['program_name']): names.setdefault(dkey(v['record']['program_name']), v)
        listing = lists[ik]['programs']
        # an entry the list reader left unclassified but that prints an undotted bachelor's award ('Marketing, BSBA') is a bachelor's entry
        raw = [x for x in listing if x['listed_as'] == 'bachelor' or (x['listed_as'] is None and (X.UNDOTTED_LIST_AWARD.search(x['printed'].replace(ZWSP, '')) or X.credential_of(x['printed']) == 'bachelor'))]
        unlabeled = sorted({card_name(x['printed'])[0] for x in listing if x['listed_as'] in ('major', 'major_unlabeled_degree')})
        seen, b, doubled, filtered, hours = set(), [], 0, 0, 0
        for x in raw:
            k = (name_key(x['printed']), page_key(x['url']))
            if k in seen: continue
            seen.add(k)
            pr, dbl = card_name(x['printed']); doubled += dbl
            h = CREDIT_HOURS.search(pr)  # UT Dallas: 'Bachelor of Arts in Education (120 semester credit hours)1'
            if h: pr = pr[:h.start()]; hours += 1
            f = FILTER_LABELS.search(pr)
            if f: pr = pr[:f.start()]; filtered += 1
            b.append(dict(x, printed=pr))
        glued = labelled = 0
        for x in b:  # Coursedog lists run the description on to the name: 'Accounting - BSThe B.S. in Accounting ...'
            if name_key(x['printed']) in names: continue
            g = [v['record']['program_name'] for v in progs if x['printed'].startswith(v['record']['program_name'])
                 and re.match(r'[A-Z][a-z]+\s', x['printed'][len(v['record']['program_name']):])
                 and len(x['printed']) - len(v['record']['program_name']) >= 30]  # a sentence, not the 'E' of 'BSE'
            c = [v['record']['program_name'] for v in progs if x['printed'].startswith(v['record']['program_name'])
                 and CATEGORY_RUN.match(x['printed'][len(v['record']['program_name']):])]
            if c: x['printed'] = max(c, key=len); labelled += 1
            elif g: x['printed'] = max(g, key=len); glued += 1
        # an entry printing only an award ('BS' under a department heading, Missouri) is identified by its page, not its text
        ident = lambda x: ('page:' + page_key(MAJOR_OF.sub(r'\1\2', x['url'])) if CONC_AWARD.match(x['printed'].strip()) else
                           'page:' + page_key(x['url']) if AWARD_ONLY.match(x['printed'].strip()) else dkey(x['printed']) or name_key(x['printed']))
        comb = [x for x in b if COMB.search(x['printed'])]
        gen = [x for x in b if x not in comb and (GENERIC.search(x['printed']) or ROTC.search(x['printed']))]
        rest = [x for x in b if x not in comb and x not in gen]
        shape = [X.emphasis_entry(X.list_line(x['printed'])) for x in rest]
        degrees = {X._degree_key(X.list_line(x['printed'])) for x, m in zip(rest, shape) if not m} - {None}
        opts = [x for x, m in zip(rest, shape) if m and (X.name_key_of(m.group('base')), X._award_key(m.group('award'))) in degrees]
        opts += [x for x, m in zip(rest, shape) if not m and x not in opts and track_of_listed(X.list_line(x['printed']), degrees)]
        # a track printed on a page under a listed degree's own page (YSU '.../bsas-exercise-science/mat-track/', 'Exercise
        # Science - MAT Track') is that degree's track
        deg_pages = {page_key(x['url']) for x, m in zip(rest, shape) if not m and X._degree_key(X.list_line(x['printed']))}
        opts += [x for x in rest if x not in opts and TRACK_SUFFIX.search(X.list_line(x['printed']))
                 and any(page_key(x['url']).startswith(dp.rstrip('/') + '/') for dp in deg_pages)]
        # the same degree listed again for another delivery ('X (online)' beside 'X') is one program
        plain = {name_key(x['printed']) for x in rest}
        opts += [x for x in rest if x not in opts and DELIVERY_QUALIFIER.search(x['printed'])
                 and name_key(DELIVERY_QUALIFIER.sub('', x['printed'])) in plain]
        deg = [x for x in rest if x not in opts]
        by_page = defaultdict(set)
        for x in deg: by_page[page_key(x['url'])].add(ident(x))
        rec_pages = defaultdict(list)
        for v in progs: rec_pages[page_key(v['source']['requested_url'])].append(v)
        verified = {}
        for x in deg:
            k = ident(x); hit = None if k.startswith('page:') else names.get(k)
            if not hit and len(by_page[page_key(x['url'])]) == 1 and len(rec_pages.get(page_key(x['url']), [])) == 1:
                hit = rec_pages[page_key(x['url'])][0]
                rk = name_key(hit['record']['program_name']); pk = name_key(x['printed'])
                # 'X: Concentration in Y' is not credited through X's page; a college named in parentheses is not a qualifier
                # (UVM 'Computer Science B.A. (College of Arts and Sciences)')
                bare = name_key(DELIVERY_QUALIFIER.sub('', X.COLLEGE_QUALIFIER.sub('', x['printed'])))
                if pk.startswith(rk) and pk != rk and bare != rk: hit = None
            if hit: verified[k] = hit['record']['program_key']
            else: verified.setdefault(k, None)
        n = len(verified); ver = sum(1 for v in verified.values() if v)
        missing = {ident(x): x['printed'] + (f" ({x['url']})" if ident(x).startswith('page:') else '') for x in deg if not verified[ident(x)]}
        miss = sorted(set(missing.values()))
        pages = sorted({x['listed_on'] for x in raw}); lo = pages[0]
        parts = [f"{len(raw)} linked entries on the official {year} program list" + (f" ({len(pages)} pages)" if len(pages) > 1 else '') + " print a bachelor's award"]
        if len(b) < len(raw): parts.append(f"{len(raw) - len(b)} repeat an entry already counted")
        if hours: parts.append(f"{hours} print the degree's credit hours after the name, which are not part of it")
        if filtered: parts.append(f"{filtered} run the award on to the row's filter labels ('Undergraduate', 'Bachelor's', subject and college) and are read up to the award")
        if doubled: parts.append(f"{doubled} print the program name twice (a card title, sometimes shortened, then the name) and are read once")
        conc = [x for x in deg if CONC_AWARD.match(x['printed'].strip())]
        unmapped = [x['url'] for x in conc if not MAJOR_OF.search(x['url'])]
        if unmapped:  # a concentration whose major cannot be told from its link: no count is recorded (Colorado State)
            raise ValueError(f'{ik}: {len(unmapped)} concentration rows name no major in their link, e.g. {unmapped[0]}')
        award_only = sum(1 for x in deg if ident(x).startswith('page:')) - len(conc)
        if award_only: parts.append(f"{award_only} print only an award under a department heading and are identified by their own page")
        plain_ids = {ident(x) for x in deg if x not in conc}
        if conc: parts.append(f"{len(conc)} concentration rows print only an award and are counted with their major, identified by the major's page "
                              f"({len({ident(x) for x in conc} - plain_ids)} majors are listed only through concentrations)")
        if labelled: parts.append(f"{labelled} run the card's category labels on to the name and are matched by the name printed before them")
        if glued: parts.append(f"{glued} run the program description on to the name and are matched by the name printed before it")
        if comb: parts.append(f"not counted, {len(comb)} combined or accelerated bachelor's/master's entries: " + ' | '.join(sorted({x['printed'] for x in comb})))
        if gen: parts.append(f"not counted, {len(gen)} department, roadmap, general or commissioning links that are not a single bachelor's program: " + ' | '.join(sorted({x['printed'] for x in gen})))
        if opts: parts.append(f"not counted, {len(opts)} concentrations or options of a degree whose own line is listed: " + ' | '.join(sorted({x['printed'] for x in opts})))
        if unlabeled: parts.append(f"{len(unlabeled)} further list entries print no award and are not counted: " + ' | '.join(unlabeled))
        repeats = len(deg) - len(conc) - len(plain_ids)
        if repeats: parts.append(f"{repeats} remaining entries repeat a program name listed under another link and are counted once")
        basis = '; '.join(parts) + f". {n} bachelor's programs, {ver} with a verified record printing that name or on that program's own page." \
            + (f" Not recorded (names separated by ' | '): {' | '.join(miss)}." if miss else '')
        e = {'institution_key': ik, 'catalog_url': 'https://' + lo.split('/')[2] + '/', 'catalog_year_label': year,
             'source_evidence': {'url': lo, 'sha256': manifest[lo]['sha256'], 'fetched_at': manifest[lo]['fetched_at']},
             'listed_bachelor_programs': n, 'verified_listed_programs': ver, 'programs_complete': ver == n,
             'completeness_basis': basis, 'reason': f'Reviewed: official current-catalog program list (Research session{", " + reviewed if reviewed else ""}).'}
        if ver == n: e['listed_program_keys'] = sorted(set(verified.values()))
        if n - ver != len(missing) or len(miss) != len(missing): raise ValueError(f'{ik}: {n - ver} unverified but {len(miss)} names')
        out.append(e)
    return out


TABLE_DEGREE = re.compile(r'(?P<award>(?:Dual Degree )?B\.[A-Z][A-Za-z.]*?)(?: and (?P<award2>B\.[A-Z][A-Za-z.]*?))?(?P<conc> Concentration(?: Option)?)?')


def table_entries(run_dir, decision, ik, spec, year='2026-2027', reviewed='', records=None):
    """Colorado State 2026-27: the Programs A-Z page is one table, 'Program | Department | College | Level | Campus | Degree type',
    with no header row. Every undergraduate row whose degree type is a bachelor's award is accounted for: a plain row
    ('Computer Engineering' | 'B.S.') is a program; a concentration row ('Computer Science, Artificial Intelligence and Machine
    Learning Concentration' | 'B.S. Concentration') counts with its major, named before its last comma (or, for 'Accounting,
    Business Administration, Accounting Concentration', the plain major the name ends with); 'B.A. and B.F.A.' is two programs.
    Each row's degree-type link is aligned with the table by the page's own link order. A program is verified when an approved
    record sits on the major's page (a concentration link with its '-concentration' suffix removed) or prints the major's name
    and award. spec: {'url': list page, 'program': i, 'level': i, 'degree': i, 'level_value': 'Undergraduate'}."""
    import difflib, gzip
    run_dir = Path(run_dir)
    cands = {}
    for line in open(run_dir / 'candidates.jsonl'):
        v = json.loads(line); cands.setdefault(v['candidate_id'], v)
    approved = {a['candidate_id'] for a in json.load(open(decision))['approve']}
    progs = [v for v in cands.values() if v['institution_key'] == ik and v['domain'] == 'academic_programs' and v['candidate_id'] in approved  # (table count)
             and v.get('year_basis', 'labeled_in_source') in LABELED]
    if records is not None:  # a recount: verified bachelor's records already on file stand in for the decision's approvals
        progs = [{'record': r, 'source': {'requested_url': r.get('program_url') or r['source_url']}} for r in records
                 if r.get('verification_status') == 'verified' and r.get('credential_level') == 'bachelor']
    m = next(json.loads(l) for l in open(run_dir / 'manifest.jsonl') if json.loads(l).get('url') == spec['url'] and json.loads(l).get('page_file'))
    page = json.load(gzip.open(run_dir / 'pages' / m['page_file'], 'rt'))
    rows = [r for t in page['tables'] for r in t['rows'] if len(r) > max(spec['program'], spec['level'], spec['degree'])]
    dtype = lambda t: (t or '').strip()
    # align the rows' degree-type cells with the page's links of the same text, in page order
    texts = {dtype(r[spec['degree']]) for r in rows}
    links = [(u, dtype(t)) for u, t in page['links'] if dtype(t) in texts]
    sm = difflib.SequenceMatcher(None, [dtype(r[spec['degree']]) for r in rows], [t for _, t in links], autojunk=False)
    url_of = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                # labels repeat ('B.S. Concentration'), so an aligned link is kept only when its page name shares a word
                # with the row's name before its first comma (Nutrition Science 'Nursing Concentration' links HDFS's nursing page)
                words = {w for w in re.findall(r'[a-z]{4,}', rows[i1 + k][spec['program']].split(',')[0].lower())}
                slug = urlsplit(links[j1 + k][0]).path.rstrip('/').rsplit('/', 1)[-1].lower()
                if any(w in slug for w in words): url_of[i1 + k] = links[j1 + k][0]
    ug = [(i, r) for i, r in enumerate(rows) if r[spec['level']].strip() == spec['level_value'] and TABLE_DEGREE.fullmatch(dtype(r[spec['degree']]))]
    plain = {r[spec['program']].strip() for _, r in ug if not TABLE_DEGREE.fullmatch(dtype(r[spec['degree']])).group('conc')}
    bylen = sorted(plain, key=len, reverse=True)
    def major_of(name):  # a concentration row's major
        head = name.rsplit(', ', 1)[0]
        if head in plain: return head
        p = next((p for p in bylen if name.startswith(p + ', ')), None) or next((p for p in bylen if head.endswith(', ' + p)), None)
        return p or name.split(', ')[0]
    conc_major = {r[spec['program']].strip(): major_of(r[spec['program']].strip()) for _, r in ug
                  if (TABLE_DEGREE.fullmatch(dtype(r[spec['degree']])).group('conc') or '').strip() == 'Concentration'}
    programs = defaultdict(list)  # (major, award) -> [(row index, row)]
    for i, r in ug:
        d = TABLE_DEGREE.fullmatch(dtype(r[spec['degree']])); name = r[spec['program']].strip()
        if d.group('conc') and 'Option' in d.group('conc'):  # an option of a concentration: the concentration's major
            head = name.rsplit(', ', 1)[0]
            name = conc_major.get(head) or next((m3 for c, m3 in conc_major.items() if c.endswith(', ' + head)), None) or major_of(name)
        elif d.group('conc'):
            name = conc_major[name]
        for a in filter(None, (d.group('award'), d.group('award2'))): programs[(name, a)].append((i, r))
    def rec_award(n):
        m2 = re.search(r'\(?((?:Dual Degree )?B\.[A-Z][A-Za-z.]*?)\)?\s*$', n)
        return m2.group(1) if m2 else None
    rec_pages = defaultdict(list)
    for v in progs: rec_pages[page_key(v['record'].get('program_url') or v['source']['requested_url'])].append(v)
    by_name = defaultdict(list)
    for v in progs:
        n = re.sub(r'^Major in\s+', '', v['record']['program_name']).strip()
        a = rec_award(n); base = re.sub(r',?\s*\(?(?:Dual Degree )?B\.[A-Z][A-Za-z.]*?\)?\s*$', '', n) if a else n
        by_name[(name_key(base), a)].append(v)
    awards_of = defaultdict(set)
    for (n, a) in programs: awards_of[n].add(a)
    verified, used = {}, set()
    for (name, a), members in programs.items():
        hit = None
        for i, r in members:
            u = url_of.get(i)
            if not u: continue
            pk = page_key(MAJOR_OF.sub(r'\1\2', u)) if TABLE_DEGREE.fullmatch(dtype(r[spec['degree']])).group('conc') else page_key(u)
            vs = rec_pages.get(pk, [])
            if len(vs) == 1: hit = vs[0]; break
        if not hit:
            vs = by_name.get((name_key(name), a)) or (by_name.get((name_key(name), None)) if len(awards_of[name]) == 1 else None)
            if vs and len(vs) == 1: hit = vs[0]
        if hit and hit['record']['program_key'] in used: hit = None  # one record verifies one program
        if hit: used.add(hit['record']['program_key'])
        verified[(name, a)] = hit['record']['program_key'] if hit else None
    conc_rows = sum(1 for _, r in ug if TABLE_DEGREE.fullmatch(dtype(r[spec['degree']])).group('conc'))
    n = len(verified); ver = sum(1 for v in verified.values() if v)
    miss = sorted(f'{k[0]}, {k[1]}' for k, v in verified.items() if not v)
    unaligned = sum(1 for i, _ in ug if i not in url_of)
    parts = [f"{len(ug)} undergraduate rows of the official {year} Programs A-Z table print a bachelor's degree type",
             f"{conc_rows} are concentration or option rows counted with their major" + (f"; {unaligned} rows have no link whose page name shares a word with the row, so they are matched by name only" if unaligned else '')]
    basis = '; '.join(parts) + f". {n} bachelor's programs, {ver} with a verified record on the major's page or printing the major's name and award." \
        + (f" Not recorded (names separated by ' | '): {' | '.join(miss).rstrip('.')}." if miss else '')
    e = {'institution_key': ik, 'catalog_url': 'https://' + spec['url'].split('/')[2] + '/', 'catalog_year_label': year,
         'source_evidence': {'url': spec['url'], 'sha256': m['sha256'], 'fetched_at': m['fetched_at']},
         'listed_bachelor_programs': n, 'verified_listed_programs': ver, 'programs_complete': ver == n,
         'completeness_basis': basis, 'reason': f'Reviewed: official current-catalog program list (Research session{", " + reviewed if reviewed else ""}).'}
    if ver == n: e['listed_program_keys'] = sorted(set(verified.values()))
    return e


def on_file_approvals(run_dir, folder, ik, root=Path('.'), year='2026-27'):
    """For a recount: the current candidates of a stored run that re-identify a verified bachelor's record already on file
    (same program key, same name on the same program page, or the only verified record on that page), one per page.
    Used for counting only; the recount decision promotes nothing (ODU, 2026-10-21)."""
    f = Path(root) / 'data/institutions' / folder / 'academic_programs' / f'{year}.json'
    recs = [r for r in (json.load(open(f))['records'] if f.exists() else []) if r.get('verification_status') == 'verified' and r.get('credential_level') == 'bachelor']
    keys = {r['program_key'] for r in recs}
    url = lambda r: page_key(r.get('program_url') or r['source_url'])
    pages = {(url(r), name_key(r['program_name'])) for r in recs}
    count = defaultdict(int)
    for r in recs: count[url(r)] += 1
    out, used = [], set()
    for line in open(Path(run_dir) / 'candidates.jsonl'):
        v = json.loads(line)
        if v['institution_key'] != ik or v['domain'] != 'academic_programs': continue
        rec = v['record']; k = (page_key(rec.get('program_url') or v['source']['requested_url']), name_key(rec.get('program_name') or ''))
        # One credited candidate per page, except that each record on file under its own key is credited (a page printing
        # two degrees with a record each, UT Dallas 'Biology (BA, BS)')
        if rec.get('program_key') in keys and (k[0], rec.get('program_key')) not in used:
            out.append({'candidate_id': v['candidate_id']}); used.add((k[0], rec.get('program_key'))); used.add(k[0])
        elif (k in pages or count.get(k[0]) == 1) and k[0] not in used:
            out.append({'candidate_id': v['candidate_id']}); used.add(k[0])
    return out


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument('--run', required=True); a.add_argument('--decision', default=None); a.add_argument('--out', required=True)
    a.add_argument('--year', default='2026-2027'); a.add_argument('--reviewed', default=''); a.add_argument('iks', nargs='+')
    a.add_argument('--on-file', default=None, help='institution folder: credit listed programs through verified records on file (recount)')
    args = a.parse_args(argv)
    decision = args.decision
    if args.on_file:
        import tempfile
        t = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False)
        json.dump({'approve': [x for ik in args.iks for x in on_file_approvals(args.run, args.on_file, ik)]}, t); t.close(); decision = t.name
    es = entries(args.run, decision, args.iks, args.year, args.reviewed)
    json.dump(es, open(args.out, 'w'), indent=1)
    for e in es: print(e['institution_key'], e['verified_listed_programs'], '/', e['listed_bachelor_programs'], 'complete' if e['programs_complete'] else '')


if __name__ == '__main__':
    main()
