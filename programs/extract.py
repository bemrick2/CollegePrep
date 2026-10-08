"""Candidates from a program-depth run (`programs/runs/<STATE>/<run-id>/`).

Outputs (all deterministic for a given run directory):
  program_lists.json   per institution: every program link found on current-catalog list/navigation pages,
                       with the anchor text exactly as printed, the credential level it states, and the source.
  candidates.jsonl     academic_programs + degree_requirements candidates from program pages and degree
                       maps, produced by the national pipeline's own extractors (catalog_program/v1,
                       program_map/v1), imported unchanged.
  evidence.jsonl       verbatim sentences relevant to CR-14 (direct admission, apply-to-major, pre-major,
                       progression GPA, undeclared, declare-by, change of major, CIP codes, major-specific
                       scholarships). Evidence is review input only: nothing here is a record.
  summary.json         per-institution fetch and extraction counts, used by programs/audit.py.

Extraction never infers: a program's absence from a list is not recorded as "not offered"; a sentence is
copied as printed with its URL and document hash; the credential level comes only from the printed name.
"""
from __future__ import annotations
import hashlib, json, re
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from pipeline import text as T
from pipeline.crawl import Run
from pipeline.extractors import catalog as CAT, programmap as PM, common
from .crawl import program_rule, in_scope, excluded

GRAD = re.compile(r'\b(M\.?\s?S\.?|M\.?\s?A\.?|MBA|M\.?\s?Ed|M\.?\s?F\.?A|Ph\.?\s?D|Ed\.?\s?D|DNP|D\.?\s?P\.?\s?T|J\.?\s?D|'
                  r'Master|Doctor|Graduate|Post[- ]?bacc|Certificate|Minor|Endorsement)\b', re.I)
# PVAMU 2026-27 also prints BSCJ, BSAG, BSCHE and BSDIET ('Criminal Justice, BSCJ'); Liberty 'Biology Education 6-12 Major (B.Ed.)'
BACHELOR = re.compile(r'(?<![A-Za-z]\.)\b(B\.?\s?(A|S|F\.?A|L\.\s?A|M|S\.?N|S\.?W|B\.?A|S\.?E|S\.?E\.?E|S\.?M\.?E|S\.?C\.?E|Arch|Mus|A\.?S|A\.?A\.?S|S\.?Ed|Ed|I\.?S|SCJ|SAG|SCHE|SDIET)\b\.?|'
                      r'Bachelor|\bH?BA\b|\bH?BS\b)', re.I)
ASSOCIATE = re.compile(r'\b(A\.?\s?(A|S|A\.?S|A\.?T|S\.?T|F\.?A)\b\.?|Associate)', re.I)

NOT_BACHELOR_URL = re.compile(r'(^|[/_-])(min|minor|minors|cert|certificate|certificates|grad|graduate|masters?|phd|doctoral)([/_-]|$)', re.I)


def not_bachelor_path(href):
    """A minor, certificate or graduate page by its URL path. A path segment naming a combined degree index
    ('certificate-degree-programs', UAS; 'degree-programs') is not itself a certificate path."""
    path = '/'.join(seg for seg in urlsplit(href).path.split('/') if 'degree' not in seg.lower())
    return bool(NOT_BACHELOR_URL.search(path))
# 'Accounting Major' in an undergraduate catalog: a major whose degree (BA/BS) the list does not print
MAJOR = re.compile(r'\bmajor\b', re.I)
NOT_MAJOR = re.compile(r'\b(minor|certificate|graduate|second\s+major|majors\))', re.I)

EVIDENCE = [
    ('direct_admission', re.compile(r'\bdirect(ly)?[\s-]+admi(t|ts|tted|ssion|ssions)\b|\badmitted\s+directly\b', re.I)),
    ('apply_to_major', re.compile(r'\b(apply|application|applying)\s+(for|to)\s+(admission\s+(to|into)\s+)?(the\s+|a\s+)?'
                                  r'(major|program|professional|upper[\s-]*division|nursing|school|college|bba|bsn|engineering)|'
                                  r'\badmission\s+(to|into)\s+the\s+(major|program|professional|upper[\s-]*division|nursing|school)|'
                                  r'\b(competitive|selective)\s+admission|\bspace[\s-]+limited\b|\blimited\s+enrollment\b|'
                                  # UVU 'Matriculation Requirements': 'To be considered matriculated in the Accounting degree',
                                  # 'To be admitted to the BSME program', '... for matriculation', 'prior to application'
                                  r'\bmatriculated\s+(in|into)\s+the\b|\bfor\s+matriculation\b|\bto\s+be\s+admitted\s+to\s+the\s+\w+\s+program\b|'
                                  r'\bprior\s+to\s+application\b|\bapplication\s+for\s+acceptance\s+into\s+the\s+program\b', re.I)),
    ('pre_major', re.compile(r'\bpre[\s-](major|nursing|engineering|business|professional|health|computer)', re.I)),
    ('progression', re.compile(r'\b(progression|progress\s+to|continu(e|ation)\s+in\s+the\s+(major|program)|good\s+standing\s+in\s+the\s+major|'
                               r'opt[\s-]+in(to)?\b.{0,80}\bupper[\s-]*division|upper[\s-]*division\s+(admission|courses?|coursework|standing)|'
                               r'admitted\s+(formally\s+)?to\s+(your|the|their)\s+(major|program|department)|restricted,?\s+upper[\s-]*division)', re.I)),
    ('open_declaration', re.compile(r'\b(may|can)\s+(declare|choose|select)\b.{0,80}\b(at\s+any\s+time|anytime|upon\s+(admission|enrollment)|after\s+enrolling)|'
                                    r'\bautomatic(ally)?\s+admi(ssion|tted)\b|\bopen\s+to\s+all\s+students\b', re.I)),
    ('gpa_requirement', re.compile(r'\b(minimum|cumulative|overall|combined|institutional)\b[^.]{0,60}\bG\.?P\.?A\.?\b[^.]{0,30}\b[1-4]\.\d{1,2}\b|'
                                   r'\b[1-4]\.\d{1,2}\b[^.]{0,30}\b(cumulative|overall|minimum)?\s*G\.?P\.?A', re.I)),
    ('undeclared', re.compile(r'\b(undeclared|undecided|exploratory|explor(e|ing)\s+(majors|options|studies)|academic\s+focus)\b', re.I)),
    ('declare_by', re.compile(r'\bdeclare\s+(a|their|your)?\s*major\b[^.]{0,80}\b(by|before|no\s+later|prior\s+to|within|upon)\b', re.I)),
    ('change_major', re.compile(r'\b(change\s+(of\s+)?(a\s+|their\s+|your\s+)?majors?|changing\s+(their\s+|your\s+)?majors?|'
                                r'internal\s+transfer|intra[\s-]*university\s+transfer|transfer\s+(into|to)\s+(the|another)\s+(major|college|school))\b', re.I)),
    ('exam_credit_in_program', re.compile(r'\b(Advanced\s+Placement|AP\s+(exam|credit|score)|International\s+Baccalaureate|IB\s+(exam|credit)|CLEP|dual[\s-](credit|enrollment))\b', re.I)),
    ('cip_code', re.compile(r'\bCIP\b[^0-9]{0,20}\d{2}\.\d{2,4}|\b\d{2}\.\d{4}\b(?=[^\n]{0,80}\b(B\.?S|B\.?A|Bachelor)\b)')),
    ('major_scholarship', re.compile(r'scholarships?\b[^.]{0,120}\b(engineering|computer|computing|business|finance|accounting|nursing|'
                                     r'psycholog|STEM|majors?\s+in)\b|\b(engineering|computer|computing|business|finance|nursing|psycholog)\w*\b[^.]{0,80}scholarships?', re.I)),
]
SENT_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z(“"])')


def sentences(page):
    for line in page.lines:
        if len(line) < 25: continue
        for s in SENT_SPLIT.split(line):
            s = s.strip(' |')
            if 25 <= len(s) <= 600: yield s


def credential_of(name):
    if GRAD.search(name) and not BACHELOR.search(name): return None
    if BACHELOR.search(name): return 'bachelor'
    if ASSOCIATE.search(name): return 'associate'
    return None


YEAR_LABEL = re.compile(r'\b(20\d{2})\s*[-–]\s*(20\d{2})\s+(?:Undergraduate\s+|University\s+|Academic\s+|General\s+|[A-Z][a-z]+\s+Campus\s+)?(Catalog|Catalogue|Bulletin)\b', re.I)  # Pitt regionals: '2026-2027 Johnstown Campus Catalog'

LABEL_FIRST = re.compile(r'(?:Catalog|Catalogue|Bulletin)\s+(20\d{2})\s*[-–]\s*(20\d{2})(?=\s*(?:>|$))', re.I)
SHORT_LABEL = re.compile(r'\b(20\d{2})\s*[-–]\s*(\d{2})\s+(?:Undergraduate\s+|University\s+|Academic\s+|General\s+)?(?:Catalog|Catalogue|Bulletin)\b', re.I)  # UNI '2026-27 University Catalog'
EDITION = re.compile(r'(20\d{2})\s*[-–]\s*(?:20)?(\d{2})\s+Edition', re.I)  # Lewis & Clark '2026-27 Edition'; Stetson '2026-2027 Edition'
BARE_YEAR = re.compile(r'(20\d{2})\s*[-–]\s*(20\d{2})')
HEADER_NAME = re.compile(r'(?:Guide|Catalog|Catalogue|Bulletin)', re.I)
NOT_CURRENT = re.compile(r'\[?\s*(not current|archived?)\b', re.I)  # Acalog selector: "2025-2026 Academic Catalog [NOT CURRENT CATALOGS]"
ARCHIVE_LINK = re.compile(r'\s*(?:Download\s+)?(?:an?\s+)?PDF of\b|\s*Full\s+20\d{2}\s*[-–]\s*(?:20)?\d{2}\s+(?:Catalog|Catalogue|Bulletin)\s*$|\s*20\d{2}\s*[-–]\s*(?:20)?\d{2}\s+(?:[A-Z][a-z]+\s+)?(?:Catalog|Catalogue|Bulletin)\s+PDF\s*$', re.I)  # "PDF of the entire 2025-2026 Catalog", uark "A PDF of the entire 2025-26 Undergraduate catalog.": a download link, not this page's label;
# OSU 2026-27 pages print '2026-2027 Edition' and the print link 'Full 2025-2026 Catalog' (a PDF of last year's catalog);
# UTSA 2026-28 pages print '2026-28 Undergraduate Catalog' and the link '2024-2026 Undergraduate Catalog PDF'


from programs.years import PERIOD_SPANS, academic_year_of  # noqa: E402  (multi-year catalog periods, #153)


def printed_catalog_years(page):
    """Catalog year labels printed anywhere on the page ("2026-2027 Catalog" in a CourseLeaf footer,
    "2026-2027 Bulletin > ..." in a SmartCatalog breadcrumb), excluding 'Select a Catalog' archive menus."""
    found = set()
    lines = page.lines
    for i, line in enumerate(lines):
        if len(line) > 160 or ARCHIVE_LINK.match(line) or NOT_CURRENT.search(line): continue
        # a print-menu slot for a catalog PDF not yet posted ('2025-2026 Academic Catalog' / 'Coming Soon!!!', Stetson) is not this page's label
        if any(re.match(r'\s*coming soon\b', l, re.I) for l in lines[i + 1:i + 3] if l.strip()): continue
        for m in YEAR_LABEL.finditer(line):
            if int(m.group(2)) - int(m.group(1)) in PERIOD_SPANS: found.add((f'{m.group(1)}-{m.group(2)}', line.strip()))
        m = LABEL_FIRST.search(line.strip())  # Linfield "Catalog 2026-2027"; UP "Bulletin 2026-2027 > ..."; Auburn "Auburn Bulletin 2026-2027"
        if m and int(m.group(2)) - int(m.group(1)) in PERIOD_SPANS: found.add((f'{m.group(1)}-{m.group(2)}', line.strip()))
        for m in SHORT_LABEL.finditer(line):
            for k in PERIOD_SPANS:
                if int(m.group(2)) == (int(m.group(1)) + k) % 100: found.add((f'{m.group(1)}-{int(m.group(1)) + k}', line.strip()))
        # UW-Madison's site header prints the catalog name and its year on two lines: 'Guide' / '2026-2027'
        m = BARE_YEAR.fullmatch(line.strip())
        prev = next((l.strip() for l in reversed(lines[max(0, i - 2):i]) if l.strip()), '')
        if m and HEADER_NAME.fullmatch(prev) and int(m.group(2)) - int(m.group(1)) in PERIOD_SPANS:
            found.add((f'{m.group(1)}-{m.group(2)}', f'{prev} {line.strip()}'))
        m = EDITION.fullmatch(line.strip())  # Lewis & Clark header: "2026-27 Edition"
        for k in PERIOD_SPANS if m else ():
            if int(m.group(2)) == (int(m.group(1)) + k) % 100: found.add((f'{m.group(1)}-{int(m.group(1)) + k}', line.strip()))
    menu = sum(1 for l in page.lines if re.fullmatch(r'20\d{2}-20\d{2}\s+(Catalog|Catalogue|Bulletin)', l.strip(), re.I))
    if menu >= 3:  # an archive selector lists every year; only labels used in context (breadcrumb, footer) count
        found = {(y, l) for y, l in found if not re.fullmatch(r'20\d{2}-20\d{2}\s+(Catalog|Catalogue|Bulletin)', l, re.I)}
    # UT Austin prints a two-year catalog ('2026-2028 Undergraduate Catalog') and its yearly edition ('2026-27 Edition'): the
    # edition is the page's own year label; a period stands alone only when no one-year label inside it is printed (Cal Poly)
    single = {y for y, _ in found if int(y[5:9]) - int(y[:4]) == 1}
    found = {(y, l) for y, l in found if int(y[5:9]) - int(y[:4]) == 1 or not any(int(y[:4]) <= int(x[:4]) < int(y[5:9]) for x in single)}
    return found


def printed_line(page, anchor):
    """The list page's own line for a link when it adds the awards: 'Accounting: BA, BS' (UO)."""
    for line in page.lines:
        if line.startswith(anchor) and len(line) > len(anchor) and re.match(r'^\s*[:(,–-]', line[len(anchor):]) and len(line) < 200:
            return line
    return None


def norm_url(u):
    """One key per page: '/x/index.html', '/x/' and '/x' are the same CourseLeaf page."""
    return re.sub(r'(/index\.html?)?/?$', '', u.split('#')[0])


def list_award(label, name):
    """Award of a program-list entry: the printed line, else the link text, else the printed line with the words the
    page glued together pulled apart ('Architecture, B.ArchSmith College of ...', UVU). Classification only."""
    return credential_of(label) or credential_of(name) or credential_of(re.sub(r'(?<=[a-z.])(?=[A-Z][a-z])', ' ', label))


RUN_ON = re.compile(r'(?:(?<=[a-z)])|(?<=\b[AB][A-Z])|(?<=\b[AB][A-Z]{2})|(?<=\b[AB][A-Z]{3}))(?=[A-Z][a-z]+\s+(?:\S+\s+){4,}\S)')


def coursedog_card_name(name):
    """Coursedog program cards print the program's description right after its name with no space ('Accounting -
    BSThe B.S. in Accounting will ...', East Stroudsburg; 'Bachelor of Arts - PsychologyThe mission of ...', Cal
    Lutheran; shared reader request #153). The name is the text before the first point where a capital letter follows
    a lowercase letter, a closing parenthesis or an award with no space, and at least five more words follow."""
    m = RUN_ON.search(name)
    return name[:m.start()].strip() if m and m.start() >= 3 else name


def collect_lists(target, run, entries):
    """Program links on the current catalog's list pages (configured `program_lists`; Acalog navigation pages
    otherwise), deduplicated by URL, each with the text exactly as printed."""
    is_program = program_rule(target)
    cat_filter = (target.get('catalog') or {}).get('list_filter')
    # A list page this run could not fetch but an earlier run of the same catalog stored (NC State 2026-27: the
    # 'University Catalog 2026-2027' undergraduate page is in the discovery run only) is read from that run, as stored.
    docs = [(run, e) for e in entries]
    for ld in (target.get('catalog') or {}).get('list_documents') or []:
        rd = Path(__file__).resolve().parents[1] / ld['run']
        other = Run(rd)  # a run that is not checked out here (a CI run branch holds one run) has no entries
        docs += [(other, {**e, 'role': 'program_list'}) for e in other.entries()
                 if e.get('institution_key') == target['institution_key'] and e.get('url') == ld['url'] and e.get('page_file')]
    have_lists = any(e.get('role') == 'program_list' and e.get('page_file') for _, e in docs)
    out, years = {}, set()
    for src, e in docs:
        roles = ('program_list',) if have_lists else ('catalog_home', 'catalog_nav')
        if e.get('role') not in roles or not e.get('page_file'): continue
        page, d = src.load_page(e['page_file'])
        y, printed = CAT.catalog_year(page)
        if printed: years.add(printed)
        else: years |= {y for y, _ in printed_catalog_years(page)}
        for href, anchor in d.get('links', []):
            name = re.sub(r'\s+', ' ', anchor or '').strip()
            if (target.get('catalog') or {}).get('platform') == 'coursedog': name = coursedog_card_name(name)
            if not name or len(name) > 200 or not in_scope(target, href) or excluded(target, href): continue
            line = printed_line(page, name)
            if not (is_program(href) or line): continue
            label = line or name
            if cat_filter and not re.search(cat_filter, label): continue
            if not_bachelor_path(href):  # UO minors repeat the major's anchor text: /min-anthropology/
                label = name
            nk = norm_url(href)
            # UVU prints the award glued to the next column ('Architecture, B.ArchSmith College of ...'): the link's own text
            # ('Architecture, B.Arch') then carries the award
            award_of = lambda: list_award(label, name)
            if nk in out and out[nk]['credential_level'] is None and award_of() and not not_bachelor_path(href):
                del out[nk]  # the same page linked twice (A-Z index without the award, college list with it): keep the awarded line
            if nk not in out:
                level = None if not_bachelor_path(href) else award_of()
                listed_as = level or ('major' if MAJOR.search(label) and not NOT_MAJOR.search(label) else None)
                out[nk] = {'name': name, 'printed': label, 'url': href, 'credential_level': level, 'listed_as': listed_as,
                             'listed_on': e['url'], 'listed_on_sha256': e.get('sha256'), 'listed_on_title': e.get('title', '')}
    progs = sorted(out.values(), key=lambda p: p['name'].lower())
    return {'printed_years': sorted(years), 'programs': progs,
            'counts': {'links': len(progs), 'bachelor': sum(p['credential_level'] == 'bachelor' for p in progs),
                       'major_unlabeled_degree': sum(p['listed_as'] == 'major' for p in progs),
                       'associate': sum(p['credential_level'] == 'associate' for p in progs),
                       'unclassified': sum(p['credential_level'] is None for p in progs)}}


# KU 2026-27: a program's sample-plan sub-page ('Below is a sample 4-year plan for students pursuing the BA in Anthropology',
# 'The recommended 4-year plan is listed below') repeats the degree's name; the program's own page is its source
# KU 2026-27 sub-pages of a degree open with 'Below is a sample 4-year plan for students pursuing the BA in Theatre.' (engineering:
# 'The recommended 4-year plan is listed below by semester') right under the page heading. KU's degree pages print the same sentence at the end, below the degree's requirements, and other catalogs'
# degree pages carry a 'Recommended Four-Year Plan of Study' heading (Colorado, Maryland, Missouri, Tennessee) or 'The recommended
# 4-year plan is listed below' (KU engineering): none of those is a plan page.
SAMPLE_PLAN_LINE = re.compile(r'(?im)^\s*(?:below is a sample (?:4|four)[- ]year plan for|the recommended (?:4|four)[- ]year plan is listed below)\b')


def sample_plan_page(page):
    """True for a page whose body opens with the sample-plan sentence: the page's program heading is among the two lines
    before it (KU Child Life prints 'Admission to this program has been suspended ...' between them). A degree page prints
    the sentence below its requirements, under another heading (KU 'Major Junior/Senior Hours')."""
    head = (program_heading(page) or '').strip()
    for m in SAMPLE_PLAN_LINE.finditer(page.text or '') if head else ():
        before = [l.strip() for l in page.text[:m.start()].splitlines() if l.strip()]
        if head in before[-2:]: return True
    return False


def program_page_candidates(target, inst, entry, page, today_year):
    found = _program_page_candidates(target, inst, entry, page, today_year)
    if sample_plan_page(page):
        found = [c for c in found if c['domain'] != 'academic_programs']
    return found


def _program_page_candidates(target, inst, entry, page, today_year):
    """catalog_program/v1 (Acalog, CourseLeaf) unchanged; when it finds no printed year in the page header but the
    page itself prints exactly one catalog year label elsewhere (CourseLeaf footer "2026-2027 Catalog"), the same
    extractor runs on a view of the page whose title carries that label, and every candidate records it as an issue
    with the verbatim line. SmartCatalog pages use programs.smartcatalog."""
    plat = (target.get('catalog') or {}).get('platform')
    if plat == 'smartcatalog':
        from . import smartcatalog
        return smartcatalog.extract(inst, entry, page, today_year)
    if plat == 'drupal':
        return static_program_identity(inst, entry, page, today_year)
    if plat == 'coursedog':
        return coursedog_page_identity(inst, entry, page, today_year, target.get('_catalog_year'))
    out = CAT.extract(inst, entry, page, today_year)
    y0, printed0 = CAT.catalog_year(page)
    year, line = printed0, (page.title or '')
    if not out and y0 is None:
        labels = printed_catalog_years(page)
        if len({y for y, _ in labels}) == 1:
            year, line = min(labels)
            view = T.Page(page.text, f'{CAT.program_name(page)} - {year} Catalog', page.tables, page.links, page.headings)
            out = CAT.extract(inst, entry, view, today_year)
            for c in out:  # the year is printed on this same document (e.g. CourseLeaf footer): labeled in source, with its line as evidence
                c['evidence'] = c.get('evidence', []) + [{'field': 'catalog_year', 'value': year, 'snippet': line[:200],
                                                          'note': 'catalog year label printed outside the page header'}]
    if not out and plat in ('courseleaf', 'acalog'):
        out = stated_major_identity(inst, entry, page, today_year)
    if not out and plat == 'courseleaf':
        lk = target.get('_listed') or {}
        listed = lk.get(norm_url(entry.get('url') or '')) or lk.get(entry.get('url'))
        out = department_major_identity(inst, entry, page, today_year, listed) or listed_program_identity(inst, entry, page, today_year, listed)
    if not out and plat == 'courseleaf' and program_heading(page) and credential_of(program_heading(page)) == 'bachelor':
        out = static_program_identity(inst, entry, page, today_year)  # UNI: 'Physics B.S.' heads a page without Course List tables
        name = program_heading(page)
        # UNI heads emphases like majors ('Art: Art History B.A.', whose plan reads 'Art: History Emphasis, B.A.'): a
        # 'Major: Part' name on a page that speaks of emphases, and a dual major, are not programs of their own
        if re.search(r'\bdual major\b', name, re.I) or (':' in name and re.search(r'\bemphas[ie]s\b', page.text, re.I)): out = []
    if not out and plat == 'courseleaf':
        out = degree_line_identity(inst, entry, page, today_year)
        if out: return out  # program record only: UF requirement and plan tables are not read on this path yet
    if not out and plat == 'courseleaf':
        return department_section_candidates(inst, entry, page, today_year)  # several degrees on one page: no plan or list rows read here
    if plat == 'courseleaf' and year:
        from . import courseleaf
        have = any(c['domain'] == 'academic_programs' for c in out)
        plan = courseleaf.extract(inst, entry, page, year, line, have)
        if have and plan:  # plan rows must use the program key the program candidate uses
            pk = next(c['record']['program_key'] for c in out if c['domain'] == 'academic_programs')
            for c in plan: c['record']['program_key'] = pk
        out += plan
        cl = (target.get('_courselists') or {}).get(entry.get('url'))
        if have and cl:  # Course List groups read with their layout (courselist_html/v1), keyed to the program record
            prog = next(c['record'] for c in out if c['domain'] == 'academic_programs')
            awards = len(re.findall(r'\b(BA|BS|BFA|BM|BAS|BBA|BArch|BLA|BMus|BSN)\b', prog['program_name']))
            out += courseleaf.html_candidates(inst, entry, cl[0], cl[1], year, prog['program_key'], max(1, awards), page.text)
        pg = (target.get('_plangrids') or {}).get(entry.get('url'))
        # UAF roadmaps (sc_plangrid with no 'Plan of Study Grid' caption): read with their cell positions when the page gave
        # no plan through courseleaf_plan/v1, so one grid is never read twice
        if have and pg and not any(c['record'].get('requirement_kind') == 'program_plan' for c in out):
            prog = next(c['record'] for c in out if c['domain'] == 'academic_programs')
            out += courseleaf.plangrid_candidates(inst, entry, pg[0], pg[1], year, prog['program_key'])
    return out


SECTION_AWARD = {'bs': r'B\.?\s?S\.?|Bachelor of Science', 'ba': r'B\.?\s?A\.?|Bachelor of Arts', 'bfa': r'B\.?\s?F\.?\s?A\.?|Bachelor of Fine Arts',
                 'bba': r'B\.?\s?B\.?\s?A\.?|Bachelor of Business Administration', 'bla': r'B\.?\s?L\.?\s?A\.?|Bachelor of Landscape Architecture',
                 'bsn': r'B\.?\s?S\.?\s?N\.?|Bachelor of Science in Nursing', 'bm': r'B\.?\s?M\.?|Bachelor of Music',
                 'bse': r'B\.?\s?S\.?\s?E\.?|Bachelor of Science in Education', 'bsw': r'B\.?\s?S\.?\s?W\.?|Bachelor of Social Work'}
SECTION_HEADING = re.compile(r'^(?:Requirements for (?:the )?)?(?P<award>' + '|'.join(f'(?P<{k}>{v})' for k, v in SECTION_AWARD.items()) +
                             r')\s+(?:[Dd]egree\s+)?in\s+(?P<name>[A-Z][^()]*?)(?:\s*\([^()]*\))?\d?$')  # UTSA 'Bachelor of Science Degree in Computer Science'
# a heading that names a part of the degree's page ('... Degree Sequence', '... Degree Requirements', '... Degree Program
# Requirements', '... Major Field', '... Requirements': PVAMU, Tulane, TAMU 2026-27) is not the degree's name as printed
SECTION_PART = re.compile(r'\b(degree\s+(sequence|requirements?|program|plan)|major\s+field|requirements)\s*\d?$', re.I)
# Shared reader requests #153 (CA/NY/PA 2026-27): a heading or title that names a part of a page, a roadmap, an office or a
# policy is not a program's name, wherever it sits: 'B.A. in Theatre Minimum Grade Requirement' (West Chester), 'BS in
# Information Systems Program Educational Objectives' (Drexel), 'Bachelor of Arts in Economics Roadmap - Quantitative
# Reasoning' (SF State), 'Department of Nursing (BSN Pre-licensure)' (Vanguard), 'Requirements for a Bachelor's Degree'
# (UCI), 'Modern Language Language for BA Degree' (Slippery Rock), 'Bachelor's Degree Requirements Archive' (UC Davis)
NOT_PROGRAM_NAME = re.compile(r"\b(minimum\s+grade\s+requirements?|(program\s+)?educational\s+objectives|(student\s+)?learning\s+outcomes|roadmaps?|archive)\b"
                              r"|^\s*(department|school|college|division|office)\s+of\b|^\s*(general\s+)?requirements\s+(for\s+(a|the|all)\b|[-\u2013\u2014])"
                              r"|\bfor\s+(a\s+|the\s+)?B\.?\s?[A-Z]{1,3}\.?\s+degree\b", re.I)
SECTION_NOT_PROGRAM = re.compile(r'\b(option|concentration|track|emphasis|specialization|minor|certificate|endorsement|accelerated|combined|'
                                 r'plan|semester|map|sample|suggested|'
                                 r'dual|double|second|online degree|pathway|pre-|with\b)|\+|/|\band\s+B\.?\s?[A-Z]|\bMaster', re.I)


def _names_degree(anchor, name, award):
    """A link text that is exactly this degree: the name with this award before or after it ('Computer Engineering BS',
    'Bachelor of Science in Computer Engineering'); never another award of the same name ('Economics BS' for a BBA) or a
    longer name ('Accelerated Bachelor of Science in Nursing')."""
    if anchor.startswith(name + ' '): rest = anchor[len(name):]
    elif anchor.endswith(' ' + name): rest = re.sub(r'\s+in$', '', anchor[:-len(name)].strip())
    else: return False
    return re.fullmatch(r'(?:' + SECTION_AWARD[award] + r')', rest.strip(), re.I) is not None


def department_section_candidates(inst, entry, page, today_year):
    """department_section/v1: CourseLeaf department pages that print each bachelor's degree as its own section heading
    ('BS in Biological Sciences (BIO)', 'B.A. in Chemistry': MSState 2026-27). One record per heading; the name is the
    heading as printed, the award the heading's own, the catalog year the page's single current label. Headings for an
    option, concentration, combined or second degree, or with two awards, are not programs. Several programs share the
    department page as their URL."""
    labels = {y for y, _ in printed_catalog_years(page)}
    y0, printed0 = CAT.catalog_year(page)
    if printed0: labels.add(printed0)
    if len(labels) != 1: return []
    year = next(iter(labels)); acad = academic_year_of(year)
    yline = next((l for y, l in printed_catalog_years(page) if y == year), printed0 and (page.title or '')) or year
    # KU 2026-27: a program's sample-plan sub-page ('Below is a sample 4-year plan for students pursuing the BA in
    # Anthropology') repeats the degree heading; the program's own page is its source
    if sample_plan_page(page): return []
    here = norm_url(common.source_of(entry)['url'])
    others = [(norm_url(h), re.sub(r'[^a-z0-9]+', ' ', (a or '').lower()).strip()) for h, a in (page.links or [])]
    out, keys = [], set()
    # UF Geography: 'BA | Specializations: Environmental Geosciences | General Geography | ...' - a section heading that names a
    # specialization the page lists ('Bachelor of Arts in Environmental Geosciences') is not a degree of its own
    specs = {x.strip().lower() for l in re.findall(r'Specializations?:\s*([^\n]+)', page.text or '') for x in l.split('|') if x.strip()}
    for h in page.headings:
        h = h.strip()
        m = SECTION_HEADING.match(h)
        if not m or SECTION_NOT_PROGRAM.search(h) or GRAD.search(m.group('name')): continue
        if m.group('name').strip(' ,').lower() in specs or SECTION_PART.search(h) or NOT_PROGRAM_NAME.search(re.sub(r'^\s*requirements\s+for\s+(the\s+)?', '', h, flags=re.I)): continue
        award = next(k for k in SECTION_AWARD if m.group(k))
        name = m.group('name').strip(' ,')
        # the department page links the degree's own catalog page ('Computer Engineering BS', Wichita; 'Bachelor of Science in
        # Business and Computer Science', WUSTL): that page is the degree's source, not this section
        nm = re.sub(r'[^a-z0-9]+', ' ', name.lower()).strip()
        if nm and any(u != here and _names_degree(a, nm, award) for u, a in others): continue
        key = CAT.slug(f'{name} {award}')
        if key in keys: continue
        keys.add(key)
        printed = re.sub(r'^Requirements for (?:the )?', '', re.sub(r'\d$', '', h)).strip()  # uark: 'Requirements for B.S. in Biology'
        rec = {'program_key': key, 'program_name': printed, 'credential_level': 'bachelor', 'catalog_year': year,
               'program_url': common.source_of(entry)['url'],
               'notes': 'Degree section heading on the catalog department page; the department page lists several degrees.'}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': rec['program_name'], 'snippet': h[:200]},
                                {'field': 'catalog_year', 'value': year, 'snippet': str(yline)[:200]}],
                               entry, 'department_section/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


DEGREE_LINE = re.compile(r'(?m)^[ \t]*Degree:[ \t]*(Bachelor of [A-Z][A-Za-z]*(?: (?:in|of|and) [A-Z][A-Za-z]*| [A-Z][A-Za-z]*)*)[ \t]*$')


def degree_line_identity(inst, entry, page, today_year):
    """degree_line/v1: a program page headed by the program's name alone ('Accounting') that states its award on one
    line, 'Degree: Bachelor of Science in Accounting' (UF 2026-27). The name is the page heading as printed; the award line
    is the credential evidence; the page must print one current catalog label. Two degree lines, no line, or an option,
    minor, certificate or online-copy heading give no record."""
    if not page.headings: return []
    name = page.headings[0].strip()
    if not name or OPTION_NAME.search(name) or re.search(r'\b(minor|certificate|online)\b', name, re.I): return []
    if name != CAT.program_name(page).strip(): return []
    parts = [x for x in urlsplit(common.source_of(entry)['url']).path.split('/') if x]
    if len(parts) >= 2 and re.fullmatch(r'[A-Z]{2,4}_[A-Z]{2,6}', parts[-2]): return []  # UF 'BLY_BS/BLY_BS01/': a specialization under its major's page
    awards = {m.group(1) for m in DEGREE_LINE.finditer(page.text)}
    labels = printed_catalog_years(page)
    if len(awards) != 1 or len({y for y, _ in labels}) != 1: return []
    m = DEGREE_LINE.search(page.text); award = m.group(1)
    year, line = min(labels); acad = academic_year_of(year)
    rec = {'program_key': CAT.slug(f'{name} {award}'), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'],
           'notes': f'Program name as printed in the page heading; award as stated on the page: "{m.group(0).strip()}"'}
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': name},
                         {'field': 'credential_level', 'value': 'bachelor', 'snippet': m.group(0).strip()[:300]},
                         {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'degree_line/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}'])]


YEAR_HEADING = re.compile(r'^\s*(?:(?:19|20)\d{2}\s*[-–]\s*(?:19|20)?\d{2}\s+)?(?:(?:academic|university|undergraduate|general)\s+)?catalog(?:ue)?(?:\s+(?:19|20)\d{2}\s*[-–]\s*(?:19|20)?\d{2})?\s*$', re.I)


GENERIC_DEGREES = re.compile(r"^\s*(?:bachelor|baccalaureate)(?:['’]?s)?\s+(?:degrees?|programs?)\b", re.I)  # UAS 'Bachelor's Degrees' index


def program_heading(page):
    """The page's first heading, past a heading that only labels the catalog year ('Catalog 2026-2027' above
    'Computer Science B.A.', UAF)."""
    hs = [h for h in (page.headings or [])]
    named = (page.title or '').split(' | ')[0].split(' < ')[0].strip()  # Kent State: 'Accounting - B.B.A. < Kent State University'
    if named and named in [h.strip() for h in hs]: return named  # UVM: '2026-27 Catalogue', 'Quick Links', 'Anthropology B.A.'
    # UC Davis: title 'General Catalog - Business, Bachelor of Science'; the heading runs the college on after the name
    # ('Business, Bachelor of Science Graduate School of Management'): the name is the part the title prints
    tail = named.split(' - ', 1)[1].strip() if ' - ' in named else ''
    if tail and credential_of(tail) == 'bachelor':
        for h in hs:
            rest = h.strip()[len(tail):] if h.strip().startswith(tail + ' ') else ''
            if re.match(r'\s+(college|school|graduate\s+school|division|department|faculty)\s+of\b', rest, re.I): return tail
    while hs and YEAR_HEADING.match(hs[0]): hs = hs[1:]
    return hs[0] if hs else None


# UMD 2026-27 (owner request 2026-10-07): the catalog names a major without its award ('Accounting Major'). The Maryland Higher
# Education Commission's Academic Program Inventory, an official state list of each institution's degree programs, prints the
# program with its degree level ('Univ. of Maryland, College Park | ACCOUNTING | Bachelor's Degree') but not the award either.
# A record is made only when the inventory lists exactly one bachelor's program of that name at the institution; the award stays
# unknown (issue award_not_printed), so such a record can only be partially verified. Nothing is inferred.
INVENTORY_LEVEL_EXTRACTOR = 'inventory_level/v1'
MAJOR_HEADING = re.compile(r'^(?P<name>[A-Z][^()]+?)\s+Major$')


def _inv_norm(s):
    s = re.sub(r'&', ' and ', (s or '').lower())
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9]+', ' ', s)).strip()


def load_level_inventory(target):
    """Rows (institution, program, level) of the target's state inventory document, read from the run that stored it."""
    li = target.get('level_inventory')
    if not li: return None
    run = Run(Path(__file__).resolve().parents[1] / li['run'])
    for e in run.entries():
        if e.get('url') == li['url'] and e.get('page_file'):
            page, _ = run.load_page(e['page_file'])
            rows = [r for t in page.tables for r in t.get('rows') or [] if len(r) == 3 and r[0].strip() == li['institution']]
            return {'entry': e, 'rows': [[c.strip() for c in r] for r in rows], 'institution': li['institution'], 'publisher': li.get('publisher', '')}
    return None


AWARD_PHRASE = re.compile(r"\b(?:Bachelor\s+of\s+(?P<long>Arts|Science|Landscape\s+Architecture|Music(?:\s+Education)?|Fine\s+Arts)|"
                          r"(?<![A-Za-z.])(?P<short>B\.\s?(?:A|S|L\.\s?A|M|F\.\s?A|M\.\s?E)\.)|(?<![A-Za-z.])(?P<bare>BA|BS)(?=\s+(?:degree\s+)?in\s))(?![A-Za-z])")
LONG_SHORT = {'arts': 'B.A.', 'science': 'B.S.', 'landscape architecture': 'B.L.A.', 'music': 'B.M.', 'music education': 'B.M.E.', 'fine arts': 'B.F.A.'}


SENTENCE_END = re.compile(r'(?<=[a-z0-9)])[.!?]\s+(?=[A-Z])')
AWARD_LEAD = re.compile(r'^the\s+(?:B\.\s?[A-Z]\.|Bachelor\s+of\s+\w+)\s+degree\b|\b(this|the) major\b|\bmajor (?:leading|leads)\b|\blead(?:s|ing)? to\b|\bculminates? in\b|\brequirements for (?:a|the)\b|\boffers? (?:a|the|both)\b|\bdegree option\b', re.I)


def printed_awards(name, text):
    """Bachelor's awards the page prints for this major, read sentence by sentence from its text ('The B.A. in Theatre
    seeks ...', 'The department curriculum leads to the Bachelor of Arts degree', UMD 2026-27). A sentence counts when it
    names the major or says the major/curriculum leads to the degree; a short navigation line ('Chemistry Major (B.A.,
    B.S.)'), another program's degree ('Bachelor of Science in Information Science' on the Technology and Information
    Design page) and a pointer to degree requirements ('Summary of Bachelor of Science Degree Requirements') do not.
    Returns {award: sentence}."""
    out = {}
    key = _inv_norm(name)
    for line in (text or '').splitlines():
        if len(line.strip()) < 60: continue
        for sent in SENTENCE_END.split(line.strip()):
            if not AWARD_PHRASE.search(sent): continue
            if key not in _inv_norm(sent) and not AWARD_LEAD.search(sent): continue
            for m in AWARD_PHRASE.finditer(sent):
                tail = sent[m.end():m.end() + 120]
                if re.match(r'\s+degree\s+requirements\b', tail, re.I): continue
                mm = re.match(r'\s+(?:degree\s+)?in\s+(?:the\s+)?(?P<prog>[A-Z].*)', tail)
                if mm and not _inv_norm(mm.group('prog')).startswith(key): continue  # 'in <another program>'
                if m.group('bare') and not mm: continue  # a bare 'BA' counts only as 'BA in <this major>'
                aw = (LONG_SHORT[re.sub(r'\s+', ' ', m.group('long').lower())] if m.group('long') else
                      re.sub(r'\s', '', m.group('short')) if m.group('short') else {'BA': 'B.A.', 'BS': 'B.S.'}[m.group('bare')])
                out.setdefault(aw, sent[:300])
    return out


def inventory_level_candidates(inst, entry, page, today_year, inv):
    """A catalog page headed 'X Major' with one printed catalog year, whose name the inventory lists as exactly one
    Bachelor's Degree program of the institution (the inventory truncates names at 40 characters: a name it cuts short
    matches on that prefix)."""
    if not inv: return []
    head = (program_heading(page) or '').strip()
    m = MAJOR_HEADING.match(head)
    if not m: return []
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels)
    want = _inv_norm(m.group('name'))
    hits = [r for r in inv['rows'] if r[2] == "Bachelor's Degree" and (_inv_norm(r[1]) == want or
            (len(r[1]) >= 38 and want.startswith(_inv_norm(r[1])) and len(_inv_norm(r[1])) >= 30))]
    if len(hits) != 1: return []
    row = hits[0]; acad = academic_year_of(year)
    snippet = f"{row[0]} | {row[1]} | {row[2]}"
    awards = printed_awards(m.group('name'), page.text)
    inv_note = (f'The {inv["publisher"]} Academic Program Inventory lists "{row[1]}" as a Bachelor\'s Degree program of {row[0]} '
                '(degree level only; it prints no award).')
    if awards:
        note = ('Program name and catalog year as printed on the catalog page; the page prints the award' + ('s ' if len(awards) > 1 else ' ')
                + ', '.join(sorted(awards)) + ' in its text (quoted in the evidence). ' + inv_note)
    else:
        note = ('Program name and catalog year as printed on the catalog page; the page does not state which bachelor\'s award this major '
                'leads to, so no award is recorded. ' + inv_note)
    rec = {'program_key': CAT.slug(head), 'program_name': head, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'], 'notes': note}
    ie = inv['entry']
    ev = [{'field': 'program_name', 'value': head, 'snippet': head},
          {'field': 'catalog_year', 'value': year, 'snippet': line[:200]},
          {'field': 'credential_level', 'value': 'bachelor', 'snippet': snippet, 'url': ie['url'], 'sha256': ie.get('sha256')}]
    ev += [{'field': 'award', 'value': a, 'snippet': l} for a, l in sorted(awards.items())]
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec, ev,
                        entry, INVENTORY_LEVEL_EXTRACTOR, {'program_key': rec['program_key']}, {}, [] if awards else ['award_not_printed'])]


def static_program_identity(inst, entry, page, today_year):
    """Static HTML catalogs (George Fox, Rhodes): the program record only (name as printed in the page heading, the
    bachelor award it names, the catalog year printed on the page). Requirement lists are not read here."""
    name = (program_heading(page) or (page.title or '').split(' | ')[0]).strip()
    # an option or track page ('Civil Engineering - BS, Coastal Engineering Track', Texas A&M) gives its candidate, and the
    # extraction loop drops it unless the official list prints it as the degree's only entry (drops_option_page)
    if credential_of(name) != 'bachelor' or GENERIC_DEGREES.match(name) or NOT_PROGRAM_NAME.search(name): return []
    labels = {y for y, _ in printed_catalog_years(page)}
    if len(labels) != 1: return []
    year = next(iter(labels)); line = next(l for y, l in printed_catalog_years(page) if y == year)
    acad = academic_year_of(year)
    rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'], 'notes': 'Program heading and catalog year as printed on the catalog page.'}
    issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'static_program/v1', {'program_key': rec['program_key']}, {}, issues)]


def department_major_identity(inst, entry, page, today_year, listed):
    """CourseLeaf department pages that hold one major (UO 'Cinema Studies'): the page prints no award in its name,
    but the catalog's own program list links this exact page with the awards ('Cinema Studies: BA, BS') and the page
    has a '<Name> Major Requirements' heading for that same name. The record is named by the list line as printed;
    the list line is the credential evidence and the heading ties the page to it. A page holding several majors
    ('Majors - Bachelor's Degree') has no such heading and yields nothing."""
    if not listed or listed.get('credential_level') != 'bachelor' or not listed.get('listed_on_sha256'): return []
    name, printed = listed['name'].strip(), listed['printed'].strip()
    if printed == name or OPTION_NAME.search(printed): return []
    heading = f'{name} Major Requirements'
    if heading not in [h.strip() for h in page.headings]: return []
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); acad = academic_year_of(year)
    rec = {'program_key': CAT.slug(printed), 'program_name': printed, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'],
           'notes': f'Named as printed on the catalog program list ({listed["listed_on"]}), which links this department page; '
                    f'the page prints the heading "{heading}".'}
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': printed, 'snippet': printed[:300], 'url': listed['listed_on'], 'sha256': listed.get('listed_on_sha256')},
                         {'field': 'credential_level', 'value': 'bachelor', 'snippet': printed[:300], 'url': listed['listed_on'], 'sha256': listed.get('listed_on_sha256')},
                         {'field': 'program_page_heading', 'value': heading, 'snippet': heading},
                         {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'department_major/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}'])]


AWARD_TOKEN = r'(?:Bachelor\s+of\s+[A-Za-z ]+?|H?B\.?\s?[A-Z]{1,4}\.?(?:[A-Z]\.?){0,3}|B\.\s?[A-Z]\.(?:[A-Z]\.)*|BArch|BMus|BSN|BBA|BFA)'
AWARDS = re.compile(r'%s(?:\s*(?:,|/|and|or|&)\s*%s)*' % (AWARD_TOKEN, AWARD_TOKEN))


def strip_award(name):
    """'Agricultural Business & Economics – BS' -> 'Agricultural Business & Economics'; 'Biology (B.S.)' -> 'Biology'."""
    n = name.strip()
    m = re.match(r'^(.*?)\s*\((.*)\)$', n)
    if m and AWARDS.fullmatch(m.group(2).strip()): return m.group(1).strip()
    m = re.match(r'^(.*?)\s*[,:–—-]\s*(.+)$', n)
    while m and AWARDS.fullmatch(m.group(2).strip()):
        n = m.group(1).strip(); m = re.match(r'^(.*?)\s*[,:–—-]\s*(.+)$', n)
        if not m or not AWARDS.fullmatch(m.group(2).strip()): break
    return n


def listed_program_identity(inst, entry, page, today_year, listed):
    """CourseLeaf program pages whose name prints no award (Auburn 'Agricultural Business & Economics (AGEC)') while the
    catalog's own program list links this exact page with the award ('Agricultural Business & Economics – BS'). The record
    is named by the list line as printed; the page must print the same program name as its title or first heading and
    exactly one catalog year label of its own."""
    if not listed or listed.get('credential_level') != 'bachelor' or not listed.get('listed_on_sha256'): return []
    printed = listed['printed'].strip()
    base = strip_award(printed)
    if not base or base == printed or OPTION_NAME.search(printed): return []
    if any(re.search(r'\bmajors\b', h, re.I) for h in page.headings): return []  # a page holding several majors
    names = [h.strip() for h in page.headings[:3]] + [CAT.program_name(page)]
    norm = lambda x: re.sub(r'\W+', ' ', x).strip().lower()
    # the page names the same program; the only extra text allowed is a parenthesised code or award ('Genetics (GENE)')
    hit = next((n for n in names if n and norm(re.sub(r'(\s*\([^()]{1,12}\))+\s*$', '', n)) == norm(base)), None)
    if not hit: return []
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); acad = academic_year_of(year)
    rec = {'program_key': CAT.slug(printed), 'program_name': printed, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'],
           'notes': f'Named as printed on the catalog program list ({listed["listed_on"]}), which links this page; the page prints "{hit}".'}
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': printed, 'snippet': printed[:300], 'url': listed['listed_on'], 'sha256': listed['listed_on_sha256']},
                         {'field': 'credential_level', 'value': 'bachelor', 'snippet': printed[:300], 'url': listed['listed_on'], 'sha256': listed['listed_on_sha256']},
                         {'field': 'program_page_heading', 'value': hit, 'snippet': hit},
                         {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'listed_program/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}'])]


STATED_BACHELOR = re.compile(r'[^.\n]*\bthis major is available as an? (bachelor of [^.\n]*?) degree\b[^.\n]*\.', re.I)
DEGREE_TYPE = re.compile(r'(?m)^[ \t]*Degree Type:[ \t]*(B\.[ ]?[A-Z]{1,3}\.(?:[ ]?[A-Z]{1,2}\.)?)[ \t]*$')  # NDSU 'Degree Type: B.S.'


def stated_major_identity(inst, entry, page, today_year):
    """'Accounting Major' pages (Linfield) print no award in the name but state it in a sentence: "This major is
    available as a bachelor of arts or bachelor of science degree, ...", or on one line, 'Degree Type: B.S.' (NDSU). The program record keeps the name as printed;
    the award sentence is its credential evidence and goes into the notes verbatim. No sentence, no record."""
    name = CAT.program_name(page).strip()
    if not re.search(r'\bmajor\b', name, re.I) or re.search(r'\bminor\b|post[- ]?baccalaureate|second degree', name, re.I) or OPTION_NAME.search(name): return []
    m = STATED_BACHELOR.search(page.text)
    types = {t.group(0).strip() for t in DEGREE_TYPE.finditer(page.text)}
    if not m and len(types) == 1:  # one stated degree type for the whole page (NDSU); two types name two programs
        m = DEGREE_TYPE.search(page.text)
    labels = printed_catalog_years(page)
    if not m or len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); sentence = m.group(0).strip()
    acad = academic_year_of(year)
    rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'],
           'notes': f'Program name as printed; award as stated on the program page: "{sentence}"'}
    issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': (page.title or name)[:200]},
                         {'field': 'credential_level', 'value': 'bachelor', 'snippet': sentence[:300]},
                         {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                        entry, 'stated_major/v1', {'program_key': rec['program_key']}, {}, issues)]


def major_table_candidates(target, inst, run, es, today_year):
    """A catalog's own table of majors (Lewis & Clark "Majors and Minors": Major | Minor | Discipline, an X marking
    each major) plus the catalog's own statement of the one bachelor's award its undergraduate majors lead to
    (`award_statement`: url + verbatim quote, checked here against the stored page). Each row marked in the Major
    column becomes a program record named as printed. Student-designed majors are not field programs."""
    cat = target.get('catalog') or {}
    conf, aw = cat.get('major_table'), cat.get('award_statement')
    if not conf or not aw: return []
    page_of = {e['url']: e for e in es if e.get('page_file')}
    te, ae = page_of.get(conf), page_of.get(aw['url'])
    if not te or not ae: return []
    tpage, apage = run.load_page(te['page_file'])[0], run.load_page(ae['page_file'])[0]
    if re.sub(r'\s+', ' ', aw['quote']) not in re.sub(r'\s+', ' ', apage.text): return []
    labels = printed_catalog_years(tpage)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); acad = academic_year_of(year)
    out = []
    for t in tpage.tables:
        rows = t.get('rows') or []
        head = [c.strip().lower() for c in rows[0]] if rows else []
        if 'major' not in head or 'discipline' not in head: continue
        mi, di = head.index('major'), head.index('discipline')
        for row in rows[1:]:
            if len(row) <= max(mi, di) or row[mi].strip().upper() != 'X': continue
            name = row[di].strip()
            if not name or re.search(r'student[- ]designed', name, re.I): continue
            rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': aw.get('credential', 'bachelor'), 'catalog_year': year,
                   'program_url': common.source_of(te)['url'],
                   'notes': f'Marked as a major in the catalog\'s Majors and Minors table; award as stated in the catalog ({aw["url"]}): "{aw["quote"]}".'}
            issues = [] if acad >= today_year else [f'stale_year_label:{acad}']
            out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                                   [{'field': 'program_name', 'value': name, 'snippet': ' | '.join(c.strip() for c in row)[:200]},
                                    {'field': 'credential_level', 'value': rec['credential_level'], 'snippet': aw['quote'][:300], 'source_url': aw['url'], 'sha256': ae.get('sha256')},
                                    {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                                   te, 'major_table/v1', {'program_key': rec['program_key']}, {}, issues))
    return out


PRINTED_DEGREE = re.compile(r'^([A-Z][^*†]+?),\s*((?:B\.[A-Za-z.]+)(?:,\s*B\.[A-Za-z.]+)*)$')


def printed_list_candidates(target, inst, run, es, today_year):
    """A catalog page that prints every undergraduate degree as "Name, Award[, Award]" under one heading (UP Bulletin
    "Undergraduate Programs": "Biology, B.S., B.A."; "Civil Engineering, B.S.C.E."). Each such line under the heading
    becomes a program record named as printed; the program URL is the line's own link when the page links it, else
    the list page. Combined bachelor/master lines and post-baccalaureate degrees do not match the pattern."""
    conf = (target.get('catalog') or {}).get('printed_list')
    if not conf: return []
    le = next((e for e in es if e['url'] == conf['url'] and e.get('page_file')), None)
    if not le: return []
    page = run.load_page(le['page_file'])[0]
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, line = min(labels); acad = academic_year_of(year)
    lines = [l.strip() for l in page.lines]
    starts = [i for i, l in enumerate(lines) if l == conf['heading']]
    if not starts: return []
    stop = conf.get('stop')
    by_text = defaultdict(set)
    for u, txt in page.links:
        if txt.strip(): by_text[txt.strip()].add(u)
    links = {t: next(iter(us)) for t, us in by_text.items() if len(us) == 1}  # 'Economics' links two programs: use neither
    out = []
    for l in lines[starts[-1] + 1:]:  # the last occurrence: the first is the table-of-contents entry
        if stop and l == stop: break
        m = PRINTED_DEGREE.match(l)
        if not m: continue
        name = l; key = CAT.slug(name)
        rec = {'program_key': key, 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
               'program_url': links.get(m.group(1).strip(), common.source_of(le)['url']),
               'notes': f'Printed under "{conf["heading"]}" on the catalog page that lists every undergraduate program.'}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                               le, 'printed_list/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


AWARD_HEADING = re.compile(r'^(Bachelor of [A-Z][a-z]+(?: [A-Z][a-z]+)?(?:\s*/\s*Bachelor of [A-Z][a-z]+(?: [A-Z][a-z]+)?)*)$')


def award_heading_candidates(inst, entry, page, today_year):
    """Acalog college pages that list each department's programs under the award they lead to (Eastern Oregon:
    'Bachelor of Arts/Bachelor of Science' / '•' / 'Art Major'). Each bulleted name under a bachelor's award heading
    becomes a program record named as printed; concentrations, minors and certificates are not programs. The catalog
    year is the page's current-catalog label (archived selector entries are marked [NOT CURRENT CATALOGS])."""
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, yline = min(labels); acad = academic_year_of(year)
    lines = [l.strip() for l in page.lines]
    by_text = defaultdict(set)
    for u, txt in page.links:
        if txt.strip(): by_text[txt.strip()].add(u)
    out, seen = [], set()
    i = 0
    while i < len(lines):
        m = AWARD_HEADING.match(lines[i])
        if not m: i += 1; continue
        award = m.group(1); j = i + 1
        while j + 1 < len(lines) and lines[j] == '•':
            name = lines[j + 1]; j += 2
            if OPTION_NAME.search(name) or re.search(r'\b(minor|certificate|concentration)\b|\bw/', name, re.I) or name in seen: continue
            urls = by_text.get(name, set())
            if len(urls) != 1: continue  # the program's own catalog page must be linked from the name
            seen.add(name)
            url = next(iter(urls)); key = CAT.slug(name)
            rec = {'program_key': key, 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year, 'program_url': url,
                   'notes': f'Listed under "{award}" on the catalog college page.'}
            out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                                   [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'credential_level', 'value': 'bachelor', 'snippet': award},
                                    {'field': 'catalog_year', 'value': year, 'snippet': yline[:200]}],
                                   entry, 'award_heading/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
        i = j
    return out


PLAN_YEAR = re.compile(r'^TYPICAL (FIRST|SECOND|THIRD|FOURTH|FIFTH) YEAR CURRICULUM$', re.I)
PLAN_TERM = re.compile(r'^(Fall|Winter|Spring|Summer)$')
PLAN_COURSE = re.compile(r'^([A-Z]{2,5} \d{3}[A-Z]?) (.+?) \((\d{1,2}(?:-\d{1,2})?)\)$')
PLAN_TITLE = re.compile(r'^(.+?) Typical Four Year Curriculum(?: \((?:On-Campus|Online)\))?$')


def college_plan_links(page):
    """{plan url: program name} from an Acalog college page: within one department block (from its 'Go to information
    for ...' line to the next), a 'Four Year Plan(s)' entry belongs to the department's only bachelor's program, or to the
    program whose printed name without ' Major' equals the plan's name before ' Typical Four Year Curriculum'."""
    lines = [l.strip() for l in page.lines]
    by_text = defaultdict(set)
    for u, txt in page.links:
        if txt.strip(): by_text[txt.strip()].add(u)
    starts = [i for i, l in enumerate(lines) if l.startswith('Go to information for ')] + [len(lines)]
    out = {}
    for a, b in zip(starts, starts[1:]):
        block, programs, plans, mode = lines[a:b], [], [], None
        for i, l in enumerate(block):
            if AWARD_HEADING.match(l): mode = 'program'; continue
            if l == 'Four Year Plan(s)': mode = 'plan'; continue
            if l in ('Minor', 'Minors', 'Certificate', 'Certificates', 'Pre-Professional Programs'): mode = None; continue
            if l == '•' and i + 1 < len(block):
                n = block[i + 1]
                if mode == 'program' and not (OPTION_NAME.search(n) or re.search(r'\b(minor|certificate|concentration)\b|\bw/', n, re.I)): programs.append(n)
                elif mode == 'plan' and PLAN_TITLE.match(n): plans.append(n)
        for pl in plans:
            urls = by_text.get(pl, set())
            if len(urls) != 1: continue
            prefix = PLAN_TITLE.match(pl).group(1)
            named = [n for n in programs if n.replace(' Major', '') == prefix]
            target = named[0] if len(named) == 1 else (programs[0] if len(set(programs)) == 1 else None)
            if target: out[next(iter(urls))] = target
    return out


def acalog_plan(inst, entry, page, program_name, today_year):
    """An Acalog 'Typical Four Year Curriculum' page (Eastern Oregon) -> one program_plan sequence: year headings, term
    headings, and each printed line as an item ('ANTH 201 Intro to Archaeology*SSC (5)' as a course item, any other line
    as printed text). 'Note:' lines are kept as printed rules."""
    labels = printed_catalog_years(page)
    if len({y for y, _ in labels}) != 1: return []
    year, yline = min(labels); acad = academic_year_of(year)
    lines = [l.strip() for l in page.lines if l.strip()]
    title = next((l for l in lines if PLAN_TITLE.match(l)), None)
    if not title: return []
    start = lines.index(title)
    terms, cur, yr, notes, issues = [], None, None, [], set()
    for l in lines[start + 1:]:
        if l.startswith('Back to Top') or l.startswith('Print-Friendly') and terms: break
        if PLAN_YEAR.match(l): yr = l; cur = None; continue  # printed as 'TYPICAL FIRST YEAR CURRICULUM'
        if PLAN_TERM.match(l):
            if yr is None: issues.add('term_without_year'); continue
            cur = {'term_index': len(terms) + 1, 'label': f'{yr} — {l}', 'items': []}; terms.append(cur); continue
        if l.startswith('Note:') or cur is None:
            if yr and (l.startswith('Note:') or terms): notes.append(l)
            continue
        m = PLAN_COURSE.match(l)
        if m and ' OR ' not in l.upper().replace(' OR OTHER', ''):
            cr = m.group(3); cur['items'].append({'code': m.group(1), 'title': m.group(2), 'credits': int(cr) if cr.isdigit() else cr})
        else:
            cur['items'].append(l)
    if len(terms) < 4: return []
    key = CAT.slug(title)
    rd = {'schema': 'requirement_group/v1', 'catalog_year': year, 'group_type': 'sequence', 'category': 'recommended_sequence', 'terms': terms,
          'source_section': title}
    if notes: rd['course_rules'] = notes
    rec = {'program_key': CAT.slug(program_name), 'requirement_key': key[:90], 'requirement_kind': 'program_plan', 'rule_details': rd}
    ev = [{'field': 'source_section', 'value': title, 'snippet': title}, {'field': 'catalog_year', 'value': year, 'snippet': yline[:200]}]
    return [common.make('degree_requirements', inst['institution_key'], acad, 'labeled_in_source', rec, ev, entry, 'acalog_plan/v1',
                        {'program_key': rec['program_key'], 'requirement_key': rec['requirement_key']}, {'terms': len(terms)}, sorted(issues))]


BULLET_MAJOR = re.compile(r'^•\s+(.+?\((?:[^()]*\b)?B[A-Z]{1,4}(?:\b[^()]*)?\))$')


def bullet_major_candidates(target, inst, entry, page, today_year):
    """A catalog PDF's list of majors with the degrees awarded, printed as bullets in two columns (King: 'MAJORS (DEGREES
    AWARDED)' / '• Biology (BA, BS)', tracks as 'o ...'). Each bullet whose parentheses name a bachelor's award
    (BA, BS, BBA, BSN, BSW ...) is a program record named as printed; tracks, minors (no award) and graduate degrees
    are not. The catalog year is the title page's '2026-2027 Academic Catalog'."""
    conf = (target.get('catalog') or {}).get('bullet_majors')
    if not conf: return []
    lines = page.lines
    year = yline = None
    for l in lines[:12]:
        m = YEAR_LABEL.search(l)
        if m and int(m.group(2)) == int(m.group(1)) + 1: year, yline = f'{m.group(1)}-{m.group(2)}', l.strip(); break
    if not year: return []
    acad = academic_year_of(year)
    start = next((i for i, l in enumerate(lines) if l.strip().startswith(conf['heading'])), None)
    if start is None: return []
    out, seen = [], set()
    for l in lines[start + 1:]:
        if l.strip() == conf.get('end', 'MINORS'): break
        for frag in re.split(r'\s{3,}', l.strip()):
            m = BULLET_MAJOR.match(frag.strip())
            if not m or m.group(1) in seen: continue
            awards = re.search(r'\(([^()]*)\)$', m.group(1)).group(1)
            if not all(re.fullmatch(r'(RN-)?B[A-Z]{1,4}', a.strip()) for a in awards.split(',')): continue  # 'BSN-DNP' is doctoral
            name = m.group(1).strip(); seen.add(name)
            key = CAT.slug(name)
            rec = {'program_key': key, 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
                   'program_url': common.source_of(entry)['url'], 'notes': f'Listed under "{conf["heading"]}" in the catalog PDF.'}
            out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                                   [{'field': 'program_name', 'value': name, 'snippet': frag.strip()}, {'field': 'catalog_year', 'value': year, 'snippet': yline}],
                                   entry, 'bullet_majors/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


TYPE_LABELS = {'Bachelor of Science', 'Bachelor of Arts', 'Bachelor of Business Admin.', 'Bachelor of Fine Arts', 'Bachelor of Music'}
CIP_IN_NAME = re.compile(r'\s*\(CIP code (\d{2}\.\d{4})\)\s*$')
HOME_EDITION = re.compile(r'^(?:Undergraduate )?Catalog (20\d{2})-(20\d{2})$')


def type_path_candidates(target, inst, run, es, today_year):
    """A catalog whose degree list links each program under a path naming its award (Lincoln Memorial:
    /education/bachelor-of-science/bs-in-education). Each linked name under a bachelor-of-* path is a program record
    named as printed (a trailing '(CIP code 51.3801)' becomes the record's CIP, printed by the institution). Tracks,
    concentrations and early-entry pathways are versions of a degree, not programs. The year is the catalog home's own
    edition title ('Undergraduate Catalog 2026-2027')."""
    conf = (target.get('catalog') or {}).get('type_path_list') or target.get('type_path_list')
    if not conf: return []
    page_of = {e['url']: e for e in es if e.get('page_file')}
    le, he = page_of.get(conf['url']), page_of.get(conf['home'])
    if not le or not he: return []
    hp = run.load_page(he['page_file'])[0]
    m = next((HOME_EDITION.match(l.strip()) for l in hp.lines if HOME_EDITION.match(l.strip())), None)
    if not m or int(m.group(2)) != int(m.group(1)) + 1: return []
    year = f'{m.group(1)}-{m.group(2)}'; yline = m.group(0); acad = academic_year_of(year)
    page = run.load_page(le['page_file'])[0]
    out, seen = [], set()
    for u, t in page.links:
        t = t.strip()
        if not re.search(r'/bachelor-of-[a-z-]+/[^/]+$', u) or not t or t in TYPE_LABELS or u in seen: continue
        if OPTION_NAME.search(t) or re.search(r'\b(track|early (entry|acceptance)|concentration|pathway)\b', t, re.I): continue
        seen.add(u)
        cm = CIP_IN_NAME.search(t); name = CIP_IN_NAME.sub('', t).strip(); key = CAT.slug(name)
        rec = {'program_key': key, 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year, 'program_url': u,
               'notes': 'Linked under a bachelor-of-* award path on the catalog\'s Degrees, Certificates, and Minors page.'}
        if cm: rec.update(cip_code=cm.group(1), cip_source_url=common.source_of(le)['url'])
        ev = [{'field': 'program_name', 'value': name, 'snippet': t}, {'field': 'credential_level', 'value': 'bachelor', 'snippet': u},
              {'field': 'catalog_year', 'value': year, 'snippet': yline, 'source_url': common.source_of(he)['url'], 'sha256': he.get('sha256')}]
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec, ev, le, 'type_path/v1',
                               {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


LISTED_MAJOR = re.compile(r'^(.*?\bMajor \([^)]*\))')


def listed_location_candidates(target, inst, run, es, listed, today_year):
    """A branch campus whose programs are the parent university's catalog programs (OSU-Cascades): the parent catalog's
    Programs page tags each program with the campuses that offer it, and `list_filter` keeps the rows tagged with this
    campus. Each bachelor row becomes a program record for the campus, named as printed (up to the award list), linking
    the parent catalog's program page; the tagged row is the evidence."""
    tag = (target.get('catalog') or {}).get('list_filter')
    if not tag: return []
    page_of = {e['url']: e for e in es if e.get('page_file')}
    out = []
    for p in listed.get('programs', []):
        if p.get('credential_level') != 'bachelor' or tag not in p.get('printed', ''): continue
        m = LISTED_MAJOR.match(p['printed'])
        le = page_of.get(p.get('listed_on'))
        if not m or not le: continue
        labels = printed_catalog_years(run.load_page(le['page_file'])[0])
        if len({y for y, _ in labels}) != 1: continue
        year, line = min(labels); acad = academic_year_of(year); name = m.group(1).strip()
        rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year, 'program_url': p['url'],
               'notes': f'Listed on the catalog Programs page with the campus tag "{tag}".'}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': name, 'snippet': p['printed'][:300]},
                                {'field': 'catalog_year', 'value': year, 'snippet': line[:200]}],
                               le, 'listed_location/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


YEAR_STATEMENT = re.compile(r'[^.\n]*\bthis catalog applies to the (20\d{2})\s*[-–]\s*(20\d{2}) academic year[^.\n]*', re.I)


def coursedog_year(run, es):
    """(year, sentence) from the Coursedog catalog home page: "Information in this catalog applies to the 2026–2027
    academic year ..." (Willamette). None when the home page prints no such statement."""
    for e in es:
        if e.get('role') == 'catalog_home' and e.get('page_file'):
            m = YEAR_STATEMENT.search(run.load_page(e['page_file'])[0].text)
            if m and int(m.group(2)) == int(m.group(1)) + 1:
                return {'year': f'{m.group(1)}-{m.group(2)}', 'line': m.group(0).strip(), 'url': common.source_of(e)['url'], 'sha256': e.get('sha256')}
    return None


def coursedog_page_identity(inst, entry, page, today_year, cat_year):
    """Rendered Coursedog program page (Willamette): the program title printed after the 'Programs/' breadcrumb
    ('Biology (BA)') with its bachelor award, and a printed 'Bachelor of ...' degree line on the same page. The catalog
    year is the catalog home page's own statement of the year it applies to (cat_year), quoted as evidence."""
    lines = [l.strip() for l in page.lines if l.strip()]
    i = next((i for i, l in enumerate(lines) if l == 'Programs/'), None)
    if i is None or i + 1 >= len(lines) or not cat_year: return []
    name = lines[i + 1]
    degree = next((l for l in lines[i + 1:i + 40] if re.match(r'^Bachelor of ', l)), None)
    if credential_of(name) != 'bachelor' or not degree or OPTION_NAME.search(name): return []
    year = cat_year['year']; acad = academic_year_of(year)
    rec = {'program_key': CAT.slug(name), 'program_name': name, 'credential_level': 'bachelor', 'catalog_year': year,
           'program_url': common.source_of(entry)['url'], 'notes': f'Program title and degree ("{degree}") as printed on the catalog program page.'}
    return [common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                        [{'field': 'program_name', 'value': name, 'snippet': name}, {'field': 'credential_level', 'value': 'bachelor', 'snippet': degree},
                         {'field': 'catalog_year', 'value': year, 'snippet': cat_year['line'][:300], 'source_url': cat_year['url'], 'sha256': cat_year['sha256'],
                          'note': "the catalog home page's statement of the academic year the catalog applies to"}],
                        entry, 'coursedog_page/v1', {'program_key': rec['program_key']}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}'])]


PROGRAM_ONLY_ISSUES = ('requirement_groups_skipped',)


OPTION_NAME = re.compile(r'\b(option|concentration|track|emphasis)\b(?!.*\bmajor\b)', re.I)


EMPHASIS_ENTRY = re.compile(r'^(?P<base>[^,]+?)\s+-\s+[^,]*\b(emphasis|concentration|track|option|specialization)\b[^,]*,\s*(?P<award>(?-i:(?:B|A)\.\s?[A-Z][a-z]{0,3}(?:\.[A-Z][a-z]{0,3})*\.?(?![a-z])))', re.I)


# UAS 2026-27: 'Fisheries and Ocean Sciences with a Concentration in Fisheries Science, B.S.' (no 'Fisheries and Ocean Sciences, B.S.')
WITH_EMPHASIS_ENTRY = re.compile(r'^(?P<base>[^,]+?)\s+with\s+an?\s+(?:concentration|emphasis|option|track|specialization)\s+in\s+[^,]+,\s*(?P<award>(?-i:(?:B|A)\.\s?[A-Z][a-z]{0,3}(?:\.[A-Z][a-z]{0,3})*\.?(?![a-z])))', re.I)
# UNH 2026-27: 'Arts Major: Studio Art Option (B.A.)' beside (or without) 'Arts Major (B.A.)'
OPTION_PAREN_ENTRY = re.compile(r'^(?P<base>[^:()]+?):\s+[^:()]*\b(emphasis|concentration|track|option|specialization)\b[^:()]*(?:\([^()]*\)[^:()]*)?\((?P<award>(?-i:(?:B|A)\.\s?[A-Z][a-z]{0,3}(?:\.[A-Z][a-z]{0,3})*\.?))\)', re.I)


# NC State 2026-27: 'Animal Science (BS): Industry Concentration' (no 'Animal Science (BS)' line)
AWARD_PAREN_OPTION_ENTRY = re.compile(r'^(?P<base>[^:()]+?)\s*\((?P<award>(?-i:[AB]\.?\s?[A-Z][A-Za-z]{0,3}\.?(?:[A-Z][a-z]{0,3}\.?)*))\)\s*:\s*[^:]*\b(emphasis|concentration|track|option|specialization)\b', re.I)
# UT Arlington 2026-27 'Data Science BS (Biology)', Texas A&M-Kingsville 'Kinesiology, B.S. (Sport Business)': a degree printed
# only as parenthetical variants (no 'Data Science BS' / 'Kinesiology, B.S.' line)
PAREN_VARIANT_ENTRY = re.compile(r'^(?P<base>[^,()]+?),?\s+(?P<award>(?-i:B[A-Z]{1,4}|B\.\s?[A-Z][a-z]{0,3}\.?(?:[A-Z][a-z]{0,3}\.)?))\s*\((?P<variant>[^()]+)\)\s*$')
# Cal Poly 2026-2028: 'Mechanical Engineering (BS) (San Luis Obispo Campus)' / '(Solano Campus)', each with its own page and
# no 'Mechanical Engineering (BS)' line
PAREN_AWARD_VARIANT_ENTRY = re.compile(r'^(?P<base>[^()]+?)\s*\((?P<award>(?-i:B[A-Z]{1,4}|B\.\s?[A-Z][a-z]{0,3}\.?(?:[A-Z][a-z]{0,3}\.)?))\)\s*\((?P<variant>[^()]+)\)\s*$')
# Texas A&M 2026-27: 'Civil Engineering - BS, Coastal Engineering Track' (no 'Civil Engineering - BS' line)
AWARD_DASH_OPTION_ENTRY = re.compile(r'^(?P<base>[^,]+?)\s+-\s*(?P<award>(?-i:B[A-Z]{1,4}))\s*,\s*[^,]*\b(emphasis|concentration|track|option|specialization)\b[^,]*$', re.I)
# VCU 2026-27: 'Chemistry, Bachelor of Science (B.S.) with a concentration in biochemistry' (no 'Chemistry, Bachelor of Science (B.S.)' line)
LONG_AWARD_WITH_OPTION_ENTRY = re.compile(r'^(?P<base>[^,]+?),\s+Bachelor of [^(),]+?\s*\((?P<award>(?-i:B\.\s?[A-Z][A-Za-z.]*))\)\s+with\s+an?\s+(?:concentration|emphasis|option|track|specialization)\s+in\b', re.I)
# Bryant 2026-27: 'Bachelor of Science in Business Administration: Accounting Concentration'
BACHELOR_OF_OPTION_ENTRY = re.compile(r'^(?P<award>Bachelor of (?:Science|Arts|Fine Arts|Music|Business Administration))\s+in\s+(?P<base>[^:]+?)\s*:\s*[^:]*\b(emphasis|concentration|track|option|specialization)\b', re.I)


LONG_AWARD = {'bachelorofarts': 'ba', 'bachelorofscience': 'bs', 'bachelorofbusinessadministration': 'bba', 'bachelorofmusic': 'bm',
              'bacheloroffinearts': 'bfa'}


name_key_of = lambda base: re.sub(r'\W+', '', base).lower()


def _award_key(a):
    k = re.sub(r'[\s.]', '', a).lower()
    return LONG_AWARD.get(k, k)


def _degree_key(line):
    """(base, award) of a program-list line that names a degree without an emphasis: 'Political Science, B.A.' or
    'Arts Major (B.A.)'."""
    m = re.match(r'^(?P<base>[^,]+?),\s+Bachelor of [^(),]+?\s*\((?P<award>(?-i:B\.\s?[A-Z][A-Za-z.]*))\)\s*$', line)  # VCU 'Chemistry, Bachelor of Science (B.S.)'
    if m: return re.sub(r'\W+', '', m.group('base')).lower(), _award_key(m.group('award'))
    if ',' in line:
        head, rest = line.split(',', 1)
        m = re.match(r'\s*((?-i:(?:B|A)\.\s?[A-Z][a-z]{0,3}(?:\.[A-Z][a-z]{0,3})*\.?(?![a-z])))', rest)
        if m: return re.sub(r'\W+', '', head).lower(), _award_key(m.group(1))
    m = re.match(r'^(?P<base>[^:()]+?)\s*\((?P<award>(?:B|A)\.[^)]*|(?-i:[AB][A-Z]{1,4}))\)', line)
    if m: return re.sub(r'\W+', '', m.group('base')).lower(), _award_key(m.group('award'))
    m = re.match(r'^(?P<award>Bachelor of (?:Science|Arts|Fine Arts|Music|Business Administration))\s+in\s+(?P<base>[^:,()]+?)\s*$', line, re.I)
    if m: return re.sub(r'\W+', '', m.group('base')).lower(), _award_key(m.group('award'))
    m = re.match(r'^(?P<base>[^,():]+?)\s+(?P<award>(?-i:B[A-Z]{1,4}))\s*$', line)  # UT Arlington 'Chemistry BA'
    if m: return re.sub(r'\W+', '', m.group('base')).lower(), _award_key(m.group('award'))
    return None


def emphasis_entry(line):
    """The emphasis, option or variant shape a program-list line prints (None for a line naming a degree itself)."""
    return (EMPHASIS_ENTRY.match(line) or OPTION_PAREN_ENTRY.match(line) or WITH_EMPHASIS_ENTRY.match(line)
                or AWARD_PAREN_OPTION_ENTRY.match(line) or BACHELOR_OF_OPTION_ENTRY.match(line) or PAREN_VARIANT_ENTRY.match(line)
                or AWARD_DASH_OPTION_ENTRY.match(line) or PAREN_AWARD_VARIANT_ENTRY.match(line) or LONG_AWARD_WITH_OPTION_ENTRY.match(line))


def list_line(printed):
    """A program-list entry as read for its shape: words the page glued together pulled apart, spaces collapsed."""
    return re.sub(r'\s+', ' ', re.sub(r'(?<=[a-z.])(?=[A-Z][a-z])', ' ', (printed or '').replace('\u200b', ''))).strip()


def listed_emphasis_pages(lists, norm, offered=None):
    """(institution, page URL) of emphases the official program list prints as bachelor's programs of their own
    ('Political Science - American Government Emphasis, B.A.', UVU 2026-27; 'Arts Major: Studio Art Option (B.A.)',
    UNH 2026-27) when the list has no entry for the base degree ('Political Science, B.A.'; 'Arts Major (B.A.)'). There
    the emphasis is how the degree is offered, and a record for it is the only record of that degree. Where the base
    degree is listed, every emphasis stays an option of it (held)."""
    out = set()
    for ik, v in (lists or {}).items():
        progs = [p for p in (v.get('programs') or []) if p.get('listed_as') == 'bachelor']
        printed = [list_line(p.get('printed')) for p in progs]
        emph = [emphasis_entry(line) for line in printed]
        degrees = {_degree_key(o) for o, m in zip(printed, emph) if not m} - {None}
        for p, m in zip(progs, emph):
            if not m: continue
            key = (name_key_of(m.group('base')), _award_key(m.group('award')))
            # the base degree is listed, or has a program page of its own in the run (NC State 'Computer Science (BS)'
            # beside 'Computer Science (BS): Game Development Concentration'): the emphasis is an option of it
            if key in degrees or key in (offered or {}).get(ik, set()): continue
            out.add((ik, norm(p.get('url'))))
    return out


norm_emph = lambda u: re.sub(r'(/index\.html?)?/?$', '', (u or '').split('#')[0])


def drops_option_page(found, key, url, emphases):
    """An option/emphasis page's candidates are dropped (its rows belong to its major), unless the official list prints it
    as a bachelor's program of its own with no line for the base degree (listed_emphasis_pages)."""
    return any(is_option_page(c) for c in found) and (key, norm_emph(url)) not in emphases


def is_option_page(c):
    """'Studio Art BFA Option' (OSU) is an option inside a major, not a degree program; the major has its own record."""
    return c['domain'] == 'academic_programs' and bool(OPTION_NAME.search(c['record'].get('program_name', '')))


def program_identity(c):
    """A program record states name, award, URL, year and printed total only; a skipped requirement group elsewhere on
    the page does not weaken those facts, so that issue stays on the requirement rows and leaves the program record."""
    if c['domain'] == 'academic_programs':
        moved = [i for i in c['issues'] if i in PROGRAM_ONLY_ISSUES]
        if moved:
            c['issues'] = [i for i in c['issues'] if i not in PROGRAM_ONLY_ISSUES]
            c.setdefault('checks', {})['requirement_issues'] = moved
    return c


THEC_PAGE = 'https://thec.ppr.tn.gov/AcademicProgramInventorySearch'
AWARD_LEVEL = [('bachelor', re.compile(r'^B[A-Z.]{0,6}$|^BACHELOR', re.I)), ('associate', re.compile(r'^A[A-Z.]{0,4}$|^ASSOCIATE', re.I))]


HOME_YEAR = re.compile(r'(?m)^\s*(20\d{2})\s*[-–]\s*(20\d{2})\s*\n+\s*((?:Undergraduate|Graduate)\s+Catalog(?:ue)?)\s*$')


def coursedog_home_year(run, entries):
    """(year, printed lines, home entry) from a Coursedog catalog home that prints '2026-2027' over 'Undergraduate Catalog'
    (Tennessee Tech)."""
    for e in entries:
        if e.get('role') == 'catalog_home' and e.get('page_file'):
            m = HOME_YEAR.search(run.load_page(e['page_file'])[0].text)
            if m and int(m.group(2)) == int(m.group(1)) + 1 and m.group(3).startswith('Undergraduate'):
                return f'{m.group(1)}-{m.group(2)}', f'{m.group(1)}-{m.group(2)} {m.group(3)}', e
    return None, None, None


def catalog_pdf_year(run, entries):
    """(year label, verbatim line, pdf entry) from the catalog's own generated PDF title page ("2026-2027 Catalog")."""
    for e in entries:
        if e.get('role') == 'catalog_pdf' and e.get('page_file'):
            page, _ = run.load_page(e['page_file'])
            for line in page.lines[:12]:
                m = YEAR_LABEL.search(line)
                if m and int(m.group(2)) == int(m.group(1)) + 1: return f'{m.group(1)}-{m.group(2)}', line.strip(), e
    return None, None, None


CODED_PROGRAM = re.compile(r'^([A-Z][A-Z0-9]*_[A-Z0-9_]+|[A-Z][A-Z0-9]*(?:\.[A-Z0-9]+)+|[A-Z]{2,8}) - (.+)$')  # BBA_ACCT (APSU), BIOL.BS (Carson-Newman)
AWARD_SUFFIX = re.compile(r',\s*([A-Z]{2,6}(/[A-Z]{2,4})?|CERT|Certificate|Minor|MINOR|Option)\s*$')


def catalog_pdf_programs(inst, entry, page, today_year):
    """A catalog system's generated full-catalog PDF (Coursedog): each department section prints a 'Programs' block
    listing its programs as 'Mechanical Engineering, BS' before 'Courses'. Bachelor-awarding names (award printed after
    the comma) become program records for the year printed on the PDF title page. A name wrapped onto two lines is
    rejoined only when the first line does not itself end in an award."""
    lines = page.lines
    year = None
    for line in lines[:12]:
        m = YEAR_LABEL.search(line)
        if m and int(m.group(2)) == int(m.group(1)) + 1: year = f'{m.group(1)}-{m.group(2)}'; year_line = line.strip(); break
    if not year: return []
    acad = academic_year_of(year)
    names, i = [], 0
    while i < len(lines):
        if lines[i].strip() == 'Programs':
            j, buf = i + 1, ''
            while j < len(lines) and lines[j].strip() not in ('Courses', 'All Programs') and j - i < 80:
                l = lines[j].strip()
                if re.search(r'\s{3,}|/\s*\d+$', l): break  # two-column layout or a page footer: not a simple list
                coded = CODED_PROGRAM.match(l)
                if coded:  # 'BBA_ACCT - Accounting (B.B.A.)' (Austin Peay): one program per line
                    names.append((coded.group(2).strip(), coded.group(1))); buf = ''; j += 1; continue
                buf = f'{buf} {l}'.strip() if buf and not AWARD_SUFFIX.search(buf) else l
                if AWARD_SUFFIX.search(buf): names.append((buf, None)); buf = ''
                j += 1
            i = j
        i += 1
    out, seen = [], set()
    for n, code in names:
        if code is not None:
            paren = re.search(r'\((B\.[A-Z.]{1,10}|B[A-Z]{1,4})\)\s*$', n)  # '(B.B.A.)', '(BS)'
            if not (paren or re.match(r'^B[A-Z]{1,5}_', code) or re.search(r'\.B[A-Z]{1,4}$', code)): continue  # award in parentheses, code prefix or code suffix
            if OPTION_NAME.search(n) or re.search(r'\bEmph\b|\bcert(ificate)?\b', n, re.I): continue  # emphases inside a major ('Emph.'), certificates
        else:
            m = AWARD_SUFFIX.search(n)
            if not m or not re.fullmatch(r'B[A-Z]{1,5}', m.group(1)): continue  # bachelor awards only; combined BS/MS left out
        key = CAT.slug(n)
        if key in seen: continue
        seen.add(key)
        rec = {'program_key': key, 'program_name': n, 'credential_level': 'bachelor', 'catalog_year': year,
               'program_url': common.source_of(entry)['url'], 'notes': "Listed in a department 'Programs' block of the catalog's generated full PDF."}
        out.append(common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source', rec,
                               [{'field': 'program_name', 'value': n, 'snippet': n}, {'field': 'catalog_year', 'value': year, 'snippet': year_line}],
                               entry, 'catalog_pdf_programs/v1', {'program_key': key}, {}, [] if acad >= today_year else [f'stale_year_label:{acad}']))
    return out


def coursedog_cip(v):
    """'520301' or '52.0201 - Management' -> '52.0301' / '52.0201' (digits as printed, punctuation normalised). A longer
    digit string ('3252030100', a state inventory layout) is not a federal CIP as printed and gives None."""
    m = re.match(r'^\s*(\d{2})\.?(\d{4})(?!\d)', str(v or ''))
    return f'{m.group(1)}.{m.group(2)}' if m else None


def coursedog_candidates(target, inst, entry, page, yr, today_year):
    """Coursedog catalog backend program rows -> academic_programs candidates (undergraduate, active, bachelor awards).
    The catalog year comes from the same catalog's generated PDF title page; without it the year is unlabeled."""
    try:
        rows = json.loads(page.text).get('data') or []
    except (ValueError, AttributeError):
        return []
    year, line, pdf = yr
    home = (target.get('catalog') or {}).get('home', '').rstrip('/')
    out = []
    for r in rows:
        name = (r.get('catalogDisplayName') or '').strip() or (r.get('name') or '').strip()
        deg = (r.get('degreeDesignation') or '').strip()
        if (r.get('level') or '') not in ('UG', '') or (r.get('status') or 'Active') != 'Active': continue
        level = credential_of(f'{name} {deg}') if deg else credential_of(name)
        if level != 'bachelor' or not r.get('programGroupId'): continue
        acad = academic_year_of(year) if year else today_year
        # FAU's feed has no catalogDisplayName and an internal short 'name' ('BA in Lang, Ling and Comparative Lit (LLCP)'); its
        # printed full name is 'longName'. The key stays on the name so records already on file keep their keys.
        shown = (r.get('catalogDisplayName') or '').strip() or (r.get('longName') or '').strip() or name
        rec = {'program_key': CAT.slug(name), 'program_name': shown, 'credential_level': level,
               'program_url': f"{home}/programs/{r['programGroupId']}", 'notes': 'From the catalog backend program list (Coursedog) that the official catalog page loads.'}
        if year: rec['catalog_year'] = year
        cip = coursedog_cip(r.get('cipCode'))
        if cip: rec.update(cip_code=cip, cip_source_url=rec['program_url'])
        ev = [{'field': k, 'value': r.get(k), 'snippet': json.dumps({k: r.get(k)}, ensure_ascii=False)[:200]}
              for k in ('catalogDisplayName', 'name', 'longName', 'degreeDesignation', 'level', 'cipCode', 'status', 'effectiveStartDate', 'programGroupId') if k in r]
        if year: ev.append({'field': 'catalog_year', 'value': year, 'snippet': line, 'source': (pdf or {}).get('url'), 'sha256': (pdf or {}).get('sha256')})
        c = common.make('academic_programs', inst['institution_key'], acad, 'labeled_in_source' if year else 'source_unlabeled', rec, ev, entry,
                        'coursedog_api/v1', {'program_key': rec['program_key'], 'group': r.get('programGroupId')})
        c['record']['source_url'] = rec['program_url']  # the public program page; the backend response hash is in the candidate source
        out.append(c)
    return out


def thec_rows(page):
    try:
        data = json.loads(page.text)
    except ValueError:
        return []
    rows = (data.get('ProgramList') or data.get('programList') or []) if isinstance(data, dict) else (data if isinstance(data, list) else [])
    # one spelling for every key, as the page's own table reads them (MajorName, Award, MajorCipCode, ...)
    canon = {k.lower(): k for k in ('InstitutionName', 'MajorName', 'Award', 'MajorTaxCode', 'MajorCipCode', 'CreditOrClockHours',
                                     'CurrentProgramStatus', 'ProgramId', 'EffectiveStartDate', 'FederalTaxName')}
    return [{canon.get(str(k).lower(), k): v for k, v in r.items()} for r in rows if isinstance(r, dict)]


def federal_cip(r):
    """THEC prints MajorCipCode as GG.FF.SSSS.XX, where FF.SSSS is the 6-digit federal CIP and FF is also printed as the
    row's MajorTaxCode (Mechanical Engineering BSME '09.14.1901.00' with MajorTaxCode '14' -> 14.1901; checked on all
    1,594 TN public rows of run 2026-10-05-thec2). The federal code is taken only when FF equals the printed MajorTaxCode,
    so the layout is confirmed row by row."""
    m = re.fullmatch(r'(\d{2})\.(\d{2})\.(\d{4})\.(\d{2})', (r.get('MajorCipCode') or '').strip())
    if not m or m.group(2) != str(r.get('MajorTaxCode') or '').strip(): return None
    return f'{m.group(2)}.{m.group(3)}'


def thec_candidates(inst, entry, rows, today_year):
    """THEC Academic Program Inventory rows (state-approved active programs) -> academic_programs candidates with the
    federal CIP code exactly as the inventory prints it. The inventory is not labelled with an academic year: rows are
    the programs active when fetched, recorded for the year in force at review (`source_unlabeled`)."""
    out = []
    for r in rows:
        name, award = (r.get('MajorName') or '').strip(), (r.get('Award') or '').strip()
        level = next((lvl for lvl, rx in AWARD_LEVEL if rx.match(award.replace(' ', ''))), None)
        if not name or level is None: continue
        if (r.get('CurrentProgramStatus') or 'Active').strip().lower() not in ('active', ''): continue
        cip = federal_cip(r)
        rec = {'program_key': CAT.slug(f'{name} {award}'), 'program_name': f'{name}, {award}', 'credential_level': level,
               'program_url': THEC_PAGE, 'notes': 'From the THEC Academic Program Inventory (state-approved active programs).'}
        if cip: rec.update(cip_code=cip, cip_source_url=THEC_PAGE)
        if str(r.get('CreditOrClockHours') or '').strip().isdigit(): rec['total_credits'] = int(r['CreditOrClockHours'])
        ev = [{'field': k, 'value': r.get(k), 'snippet': json.dumps({k: r.get(k)}, ensure_ascii=False)[:200]}
              for k in ('InstitutionName', 'MajorName', 'Award', 'MajorTaxCode', 'MajorCipCode', 'CreditOrClockHours', 'CurrentProgramStatus', 'ProgramId') if k in r]
        c = common.make('academic_programs', inst['institution_key'], today_year, 'source_unlabeled', rec, ev, entry,
                        'thec_inventory/v1', {'program_key': rec['program_key'], 'thec_program_id': r.get('ProgramId')})
        c['record']['source_url'] = THEC_PAGE  # the public search page; the API request and response hash are in the candidate source
        out.append(c)
    return out



def distinct_candidates(cands):
    """One candidate per id. A page reached by two URLs (http/https, a doubled slash, a list link and a sitemap link;
    TX 2026-10-07-flag3) is read twice with the same stored document, so its candidates repeat with only the fetch
    details differing: the first is kept. Candidates that share an id but differ in what they record would make an
    approval ambiguous: all of them get the issue candidate_id_collision, so none is approved by standing review."""
    fetch = lambda c: {**c, 'source': None, 'layout_source': None, 'program_role': None,
                       'record': {k: v for k, v in c['record'].items() if k not in ('source_url', 'program_url')}}
    by_id, out = {}, []
    for c in cands:
        first = by_id.get(c['candidate_id'])
        if first is None: by_id[c['candidate_id']] = c; out.append(c); continue
        if fetch(first) == fetch(c): continue
        for x in (first, c):
            if 'candidate_id_collision' not in x['issues']: x['issues'] = x['issues'] + ['candidate_id_collision']
        out.append(c)
    return out

def extract_run(targets, run_dir, today=None):
    run = Run(Path(run_dir)); today = today or date.today()
    today_year = T.current_academic_year(today)
    entries = run.entries()
    by_inst = defaultdict(list)
    for e in entries: by_inst[e.get('institution_key')].append(e)
    tmap = {t['institution_key']: t for t in targets['institutions']}
    lists, cands, evidence, summary, inventory = {}, [], [], {}, {}
    for key, es in sorted(by_inst.items()):
        t = tmap.get(key, {'institution_key': key, 'catalog': {}})
        roles = defaultdict(lambda: {'fetched': 0, 'ok': 0, 'errors': defaultdict(int)})
        for e in es:
            r = roles[e.get('role') or '?']; r['fetched'] += 1
            if e.get('page_file'): r['ok'] += 1
            elif e.get('error'): r['errors'][e['error'][:40]] += 1
        lists[key] = collect_lists(t, run, es) if t.get('catalog') else {'programs': [], 'counts': {}}
        emphases = listed_emphasis_pages({key: lists[key]}, norm_emph)
        if (t.get('catalog') or {}).get('platform') == 'coursedog': t = {**t, '_catalog_year': coursedog_year(run, es)}
        if t.get('level_inventory'): t = {**t, '_level_inventory': load_level_inventory(t)}
        if (t.get('catalog') or {}).get('platform') == 'courseleaf':
            t = {**t, '_listed': {norm_url(p['url']): p for p in lists[key].get('programs', [])}}
            t = {**t, '_courselists': {e['via']: (e, json.loads(run.load_page(e['page_file'])[0].text)) for e in es if e.get('role') == 'courselist' and e.get('page_file')}}
            t = {**t, '_plangrids': {e['via']: (e, json.loads(run.load_page(e['page_file'])[0].text)) for e in es if e.get('role') == 'plangrid' and e.get('page_file')}}
        n_c = 0; seen_ev = set(); seen_feed_keys = set(); plan_links = {}
        layouts = {x['via']: x for x in es if x.get('role') == 'pdf_layout' and x.get('page_file')}
        if (t.get('catalog') or {}).get('platform') == 'acalog':
            for e in es:
                if e.get('role') == 'catalog_nav' and e.get('page_file'): plan_links.update(college_plan_links(run.load_page(e['page_file'])[0]))
        for e in es:
            if not e.get('page_file'): continue
            page, _ = run.load_page(e['page_file'])
            inst = {'institution_key': key}
            if e.get('role') == 'catalog_pdf':
                for c in catalog_pdf_programs(inst, e, page, today_year) + bullet_major_candidates(t, inst, e, page, today_year):
                    c['program_role'] = 'catalog_pdf'; cands.append(c); n_c += 1
                continue
            if (e.get('role') == 'catalog_api' or (e.get('role') == 'catalog_feed' and '/programs/search/' in e.get('url', ''))) and 'coursedog.com' in e.get('url', ''):
                yr = catalog_pdf_year(run, es)
                if not yr[0]: yr = coursedog_home_year(run, es)
                for c in coursedog_candidates(t, inst, e, page, yr, today_year):
                    k = c['record']['program_key']
                    if k in seen_feed_keys or OPTION_NAME.search(c['record']['program_name']): continue  # feeds overlap; concentrations are not programs
                    seen_feed_keys.add(k)
                    c['program_role'] = 'catalog_api'; cands.append(c); n_c += 1
                continue
            if e.get('role') == 'state_inventory':
                rows = thec_rows(page)
                inventory[key] = rows
                for c in thec_candidates(inst, e, rows, today_year):
                    c['program_role'] = 'state_inventory'; cands.append(c); n_c += 1
                continue
            if e.get('role') == 'catalog_nav' and (t.get('catalog') or {}).get('platform') == 'acalog':
                for c in award_heading_candidates(inst, e, page, today_year):
                    c['program_role'] = 'program_list'; cands.append(c); n_c += 1
            if e.get('role') == 'program_page' and e['url'] in plan_links:
                for c in acalog_plan(inst, e, page, plan_links[e['url']], today_year):
                    c['program_role'] = 'degree_map'; cands.append(c); n_c += 1
                continue
            if e.get('role') == 'program_page' and excluded(t, e.get('url')): continue
            if e.get('role') == 'program_page':
                found = program_page_candidates(t, inst, e, page, today_year)
                if not any(c['domain'] == 'academic_programs' for c in found) and t.get('_level_inventory'):
                    found = inventory_level_candidates(inst, e, page, today_year, t['_level_inventory']) + found
                if drops_option_page(found, key, e.get('url'), emphases):
                    found = []  # the option's rows belong to its major (unless the list prints it as the degree's only entry)
                for c in found:
                    c['program_role'] = 'program_page'; cands.append(program_identity(c)); n_c += 1
            if e.get('kind') == 'pdf' and e.get('role') in ('degree_map', 'policy', 'policy_link'):
                try:
                    pm = PM.extract(inst, e, page, today_year)
                    for c in pm:
                        c['program_role'] = 'degree_map'; cands.append(c); n_c += 1
                    lay = layouts.get(e['url'])
                    pk = next((c['record']['program_key'] for c in pm if c['domain'] == 'academic_programs'), None)
                    if lay and pk:  # two-column Clear Path plan read from word positions (clearpath_plan/v1)
                        from . import clearpath
                        for c in clearpath.extract_layout(inst, e, page.lines, json.loads(run.load_page(lay['page_file'])[0].text), pk, today_year):
                            c['program_role'] = 'degree_map'; cands.append(c); n_c += 1
                except Exception as exc:  # an unusual PDF must not stop the run; it is counted
                    roles['degree_map']['errors'][f'programmap:{type(exc).__name__}'] += 1
            if e.get('role') in ('policy', 'policy_link', 'program_page', 'state_source', 'degree_map_index', 'discover') or key.startswith('state-'):
                for s in sentences(page):
                    for cat, rx in EVIDENCE:
                        if rx.search(s) and (cat, s) not in seen_ev:
                            seen_ev.add((cat, s))
                            evidence.append({'evidence_id': hashlib.sha1(f"{e.get('sha256')}|{s}".encode()).hexdigest()[:14],
                                             'institution_key': key, 'category': cat, 'sentence': s,
                                             'url': common.source_of(e)['url'], 'sha256': e.get('sha256'),
                                             'fetched_at': e.get('fetched_at'), 'page_title': e.get('title', ''),
                                             'role': e.get('role'), 'year_labels': sorted(T.year_labels(page.title + ' ' + page.text[:3000]))})
        for c in listed_location_candidates(t, {'institution_key': key}, run, es, lists[key], today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        for c in type_path_candidates(t, {'institution_key': key}, run, es, today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        for c in printed_list_candidates(t, {'institution_key': key}, run, es, today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        for c in major_table_candidates(t, {'institution_key': key}, run, es, today_year):
            c['program_role'] = 'program_list'; cands.append(c); n_c += 1
        summary[key] = {'roles': {k: {**v, 'errors': dict(v['errors'])} for k, v in roles.items()},
                        'program_list_links': lists[key]['counts'], 'candidates': n_c,
                        'evidence': sum(1 for x in evidence if x['institution_key'] == key)}
    cands = distinct_candidates(cands)
    d = Path(run_dir)
    (d / 'program_lists.json').write_text(json.dumps(lists, indent=1, ensure_ascii=False) + '\n')
    with (d / 'candidates.jsonl').open('w') as f:
        for c in cands: f.write(json.dumps(c, sort_keys=True, ensure_ascii=False) + '\n')
    with (d / 'evidence.jsonl').open('w') as f:
        for x in evidence: f.write(json.dumps(x, sort_keys=True, ensure_ascii=False) + '\n')
    if inventory: (d / 'state_inventory.json').write_text(json.dumps(inventory, indent=1, ensure_ascii=False) + '\n')
    (d / 'summary.json').write_text(json.dumps(summary, indent=1, sort_keys=True) + '\n')
    (d / 'review.md').write_text(review_md(targets, summary, lists))
    return summary


def review_md(targets, summary, lists):
    names = {t['institution_key']: t['name'] for t in targets['institutions']}
    lines = [f"# Program-depth run: {targets['state']}", '',
             '| School | fetched | program links (bachelor) | program pages ok | candidates | evidence | top errors |', '|---|---|---|---|---|---|---|']
    for key, s in sorted(summary.items(), key=lambda kv: names.get(kv[0], kv[0])):
        fetched = sum(v['fetched'] for v in s['roles'].values())
        errs = defaultdict(int)
        for v in s['roles'].values():
            for k, n in v['errors'].items(): errs[k] += n
        top = ', '.join(f'{k}×{n}' for k, n in sorted(errs.items(), key=lambda x: -x[1])[:3])
        c = s['program_list_links']
        lines.append(f"| {names.get(key, key)} | {fetched} | {c.get('links', 0)} ({c.get('bachelor', 0)}) | "
                     f"{s['roles'].get('program_page', {}).get('ok', 0)} | {s['candidates']} | {s['evidence']} | {top} |")
    return '\n'.join(lines) + '\n'
