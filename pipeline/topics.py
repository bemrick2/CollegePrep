"""Research categories, the data domain each feeds, and the keywords used to find their pages.

One table drives crawl priority, extractor routing and coverage reporting, so a category that is
crawled is also measured. Keywords match lowercase link text, URL paths, titles and headings.
"""
from __future__ import annotations
import re

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
                                                    'degree requirements', 'four-year plan', 'academic map'],
                            ['degree requirements', 'credit hours', 'general education']),
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


def page_topics(title: str, headings, text: str):
    head = (title + ' ' + ' '.join(headings or [])).lower()
    body = (text or '')[:20000].lower()
    out = set()
    for c, (_, kws, body_kws) in CATEGORIES.items():
        if any(k in head for k in kws + body_kws) or sum(body.count(k) for k in body_kws) >= 3:
            out.add(c)
    return sorted(out)


def link_score(url: str, anchor: str = '') -> int:
    """Crawl priority: more matched categories and PDFs/documents of known value rank higher."""
    if EXCLUDE.search(url): return -1
    topics = link_topics(url, anchor)
    if not topics: return 0
    score = 10 * len(topics)
    low = (url + ' ' + anchor).lower()
    if 'common data set' in low or 'common-data-set' in low or re.search(r'\bcds[_-]?20\d\d', low): score += 40
    if re.search(r'20\d\d\s*[-–]\s*(20)?\d\d', low): score += 5
    if low.endswith('.pdf'): score += 3
    return score
