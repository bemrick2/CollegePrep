"""Research categories, the data domain each feeds, and the keywords used to find their pages.

One table drives crawl priority, extractor routing and coverage reporting, so a category that is
crawled is also measured. Keywords match lowercase link text, URL paths, titles and headings.
"""
from __future__ import annotations
import re
from datetime import date

# category: (data domain it fills, url/anchor keywords, page-text keywords)
CATEGORIES = {
    'tuition_fees': ('costs', ['tuition', 'fees', 'bursar', 'student-accounts', 'tuition-and-fees', 'rates'],
                     ['tuition', 'mandatory fee', 'required fees', 'per credit hour']),
    'cost_of_attendance': ('costs', ['cost-of-attendance', 'cost of attendance', 'coa', 'cost-of-attendance',
                                     'estimated-cost', 'cost', 'budget'],
                           ['cost of attendance', 'estimated cost', 'books', 'housing', 'transportation']),
    'admissions_tests': ('admissions_metrics', ['admission', 'freshman', 'first-year', 'first year', 'profile',
                                                 'test-optional', 'act', 'sat'],
                         ['act', 'sat', 'middle 50', 'admitted students', 'test optional']),
    'common_data_set': ('admissions_metrics', ['common data set', 'common-data-set', 'cds', 'institutional research',
                                                'institutional-research', 'fact book', 'factbook', 'irsa', 'oira'],
                        ['common data set']),
    'merit_scholarships': ('awards', ['scholarship', 'merit', 'award'],
                           ['scholarship', 'renewable', 'minimum gpa', 'act score', 'sat score']),
    'ap_credit': ('credit_policies', ['advanced placement', 'ap-credit', 'ap credit', 'ap-exam', 'ap exam',
                                      'prior-learning', 'prior learning', 'credit-by-exam', 'credit by exam',
                                      'testing-credit', 'exam credit'],
                  ['advanced placement', 'ap exam', 'ap score']),
    'clep_credit': ('credit_policies', ['clep', 'credit-by-exam', 'credit by exam', 'prior-learning'],
                    ['clep']),
    'ib_credit': ('credit_policies', ['international baccalaureate', 'ib-credit', 'ib credit', 'prior-learning'],
                  ['international baccalaureate']),
    'dual_enrollment': ('credit_policies', ['dual enrollment', 'dual-enrollment', 'dual credit', 'dual-credit',
                                            'early college', 'high school students'],
                        ['dual enrollment', 'dual credit']),
    'transfer_credit': ('transfer_policies', ['transfer credit', 'transfer-credit', 'transfer equivalenc',
                                              'transfer-equivalenc', 'transfer information', 'transfer-information',
                                              'transfer'],
                        ['transfer credit', 'equivalenc', 'transferable']),
    'statewide_articulation': ('transfer_policies', ['transfer pathway', 'transfer-pathway', 'articulation',
                                                     'tntransfer', 'guaranteed admission'],
                               ['transfer pathway', 'articulation agreement']),
    'residency': ('transfer_policies', ['residency', 'in-state tuition', 'out-of-state', 'classification of students',
                                        'tuition classification'],
                  ['residency', 'in-state', 'domicile']),
    'degree_requirements': ('degree_requirements', ['catalog', 'catoid', 'courseleaf', 'programs of study',
                                                    'degree requirements', 'four-year plan', 'four-year-plan', '4-year-plan',
                                                    'academic map', 'academic-map', 'degree map', 'degree-map', 'program map',
                                                    'program-map', 'clear path', 'clear-path', 'plan of study', 'plan-of-study',
                                                    'curriculum map', 'curricular-map', 'finish in four', 'finish-in-four'],
                            # 'credit hours' and 'general education' alone matched SAP policies and aid FAQs (KY)
                            ['degree requirements', 'major requirements', 'program requirements', 'general education requirements']),
    'aid_appeals': ('appeals', ['appeal', 'special circumstance', 'special-circumstance', 'professional judgment',
                                'reconsideration', 'satisfactory academic progress', 'sap'],
                    ['appeal', 'special circumstance', 'professional judgment']),
}

CATEGORY_DOMAINS = {c: v[0] for c, v in CATEGORIES.items()}
# Paths that are never research targets (logins, calendars, news, media, giving).
EXCLUDE = re.compile(r'(login|signin|sign-in|cas/|sso|calendar|events?/|news/|/news|athletics|giving|donate|alumni|'
                     r'facebook|twitter|instagram|linkedin|youtube|tiktok|\.(jpg|jpeg|png|gif|svg|mp4|mp3|zip|ics|doc)$)', re.I)


def link_topics(url: str, anchor: str = ''):
    hay = (url + ' ' + anchor).lower().replace('_', '-')
    return sorted(c for c, (_, kws, _) in CATEGORIES.items() if any(k in hay for k in kws))


_WORD = {}


def _rx(k):
    if k not in _WORD:
        _WORD[k] = re.compile(r'(?<![a-z])' + re.escape(k) + r'(?![a-z])')
    return _WORD[k]


def page_topics(title: str, headings, text: str):
    """Categories a fetched document covers. Keywords match whole words ('act' is not in 'contact')."""
    head = (title + ' ' + ' '.join(headings or [])).lower()
    body = (text or '')[:20000].lower()
    out = set()
    for c, (_, kws, body_kws) in CATEGORIES.items():
        if any(_rx(k).search(head) for k in kws + body_kws) or sum(len(_rx(k).findall(body)) for k in body_kws) >= 3:
            out.add(c)
    return sorted(out)


YEAR_IN_LINK = re.compile(r'(?<!\d)(20\d{2})(?:\s*[-–_]\s*(?:20)?(\d{2}))?(?!\d)')


def link_years(text: str):
    """First years of academic-year-like labels in a link ('2025-2026', 'cds_2024-25', '2023')."""
    out = []
    for m in YEAR_IN_LINK.finditer(text):
        first = int(m.group(1))
        if m.group(2) is None or int(m.group(2)) == (first + 1) % 100: out.append(first)
    # Two-digit pairs only in the file name ('catalog06-07.pdf', 'fact-book-12_13.pdf').
    name = text.split('?')[0].rstrip('/').rsplit('/', 1)[-1]
    for m in re.finditer(r'(?<!\d)(\d{2})[-_](\d{2})(?!\d)', name):
        a, b = int(m.group(1)), int(m.group(2))
        if b == (a + 1) % 100: out.append(2000 + a)
    return out


PROGRAM_PAGE = re.compile(r'preview_program\.php|[?&]poid=\d+', re.I)
GRAD_PROGRAM = re.compile(r'\b(m\.?s\.?|m\.?a\.?|mba|m\.?ed|ph\.?d|ed\.?d|dnp|graduate|certificate|minor)\b', re.I)
UG_PROGRAM = re.compile(r'\b(b\.?s\.?|b\.?a\.?|b\.?b\.?a|bsn|b\.?f\.?a|b\.?m|bachelor|a\.?s\.?|a\.?a\.?|a\.?a\.?s|associate)\b', re.I)


# Courseleaf catalogs: catalog.<school>.edu/undergraduate/<college>/<department>/<program>/
COURSELEAF_PROGRAM = re.compile(r'^https?://catalogs?\.[^/]+/undergraduate/(?!general|academic-policies|admission|tuition|financial)(?:[^/.]+/){2,4}$', re.I)
COURSELEAF_GRADUATE = re.compile(r'^https?://catalogs?\.[^/]+/(graduate|professional|law|medicine)(/|$)', re.I)


# Clean Catalog sites (TN: Tennessee Tech, Carson-Newman, Lincoln Memorial): <host with "catalog">/programs/<slug>,
# with the program list at /programs (paged with ?page=N).
CLEANCATALOG_PROGRAM = re.compile(r'^https?://(?!grad)[^/]*catalog[^/]*/programs/[a-z0-9][a-z0-9-]+/?$', re.I)
CATALOG_PROGRAM_INDEX = re.compile(r'^https?://(?!grad)[^/]*catalog[^/]*/(?:programs|programs-study|programs-of-study|'
                                   r'ugrequirements/majors|content\.php\?catoid=\d+&navoid=\d+)/?(?:\?(?:page=\d+)?[^/]*)?$', re.I)


def is_program_page(url: str) -> bool:
    """An individual program page in a catalog platform (Acalog preview_program.php?poid=..., Courseleaf
    /undergraduate/<college>/<department>/<program>/, Clean Catalog /programs/<slug>)."""
    return bool(PROGRAM_PAGE.search(url or '') or COURSELEAF_PROGRAM.search(url or '') or CLEANCATALOG_PROGRAM.search(url or ''))


CONTACT_ANCHOR = re.compile(r'^\s*(contact|email|call|directions|map)\b', re.I)


def link_score(url: str, anchor: str = '', today=None) -> int:
    """Crawl priority: more matched categories, documents of known value, and current years rank higher.
    Links whose only year labels are more than two academic years old are skipped: the pipeline is
    after current policy, and archives of old catalogs and surveys would consume the page budget."""
    if EXCLUDE.search(url) or CONTACT_ANCHOR.search(anchor or ''): return -1
    if COURSELEAF_GRADUATE.search(url) and not UG_PROGRAM.search(anchor or ''): return -1  # KY: WKU budget went to graduate pages
    if is_program_page(url):  # anchors are program names, so topic keywords never match them
        if GRAD_PROGRAM.search(anchor) and not UG_PROGRAM.search(anchor): return -1
        return 30 if UG_PROGRAM.search(anchor) else 12
    if CATALOG_PROGRAM_INDEX.search(url) and re.search(r'program|major|degree|stud', url + ' ' + (anchor or ''), re.I):
        return 25  # the list of programs is how the crawl reaches program pages
    topics = link_topics(url, anchor)
    if not topics: return 0
    score = 10 * len(topics)
    low = (url + ' ' + anchor).lower()
    today = today or date.today()
    current = today.year if today.month >= 7 else today.year - 1
    years = [y for y in link_years(low) if 2000 <= y <= current + 1]
    if years:
        newest = max(years)
        if newest < current - 2: return -1
        score += 15 if newest >= current - 1 else 2
    if 'common data set' in low or 'common-data-set' in low or re.search(r'\bcds[_-]?20\d\d', low): score += 40
    if low.endswith('.pdf'): score += 3
    return score
