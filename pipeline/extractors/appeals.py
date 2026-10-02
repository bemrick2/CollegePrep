"""Financial-aid appeal / reconsideration pages -> appeals candidates (always reviewed).

Finds sentences that describe a documented route (special circumstances / professional judgment,
SAP appeals, scholarship retention, merit reconsideration, competing-offer review) and negative
statements ("cannot match offers"). Each candidate carries the exact sentences. The pipeline never
decides eligibility for the paid add-on: `qualifies_for_paid_addon` is always false here and every
candidate is flagged `semantic_review_required`, because a sentence classifier is not evidence of an
offered process.
"""
from __future__ import annotations
import re

from . import common

EXTRACTOR = 'appeal_sentences/v1'
SENTENCE = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')
KINDS = [  # (appeal_kind, pattern) — order matters: retention and SAP before reconsideration
    ('sap_appeal', r'satisfactory\s+academic\s+progress.{0,80}appeal|\bsap\b.{0,20}appeal|appeal.{0,40}satisfactory\s+academic\s+progress'),
    ('scholarship_retention_appeal', r'(hope|lottery|tels)\b.{0,60}appeal|appeal.{0,40}\b(hope|lottery)\b|'
                                     r'(loss|lost|lose|losing|retain|retention|renew|renewal|forfeit)\w*.{0,60}scholarship.{0,80}appeal|'
                                     r'appeal.{0,60}(loss|lost|retention|renewal)\w*.{0,30}scholarship|scholarship\s+appeal\s+form'),
    ('competing_offer_review', r'competing\s+(offer|award)s?|match(ing|es)?\s+(?:[\w-]+\s+){0,4}(offers?|awards?|packages?)\b.{0,40}'
                               r'(from|other|outside|competing|another)'),
    ('merit_reconsideration', r'(reconsider|re-?evaluat|re-?review|review|appeal)\w*\s+(of\s+)?(your\s+|my\s+|the\s+)?'
                              r'(merit\s+(scholarship|award|aid)|(scholarship|merit)\s+(offer|award\s+amount|amount)|award\s+offer)'),
    ('professional_judgment', r'professional\s+judg(e)?ment'),
    ('need_based_special_circumstances', r'special\s+circumstance|unusual\s+circumstance|change\s+in\s+(your\s+)?(family\s+|household\s+)?(income|financial)'),
    ('budget_increase', r'(cost\s+of\s+attendance|budget)\s+(increase|adjustment)'),
    ('dependency_override', r'dependency\s+(override|status\s+appeal)'),
]
SKIP_SENTENCE = re.compile(r'athlet|student-athlete|conduct|academic\s+(dismissal|integrity)|grade\s+appeal|parking|housing\s+appeal', re.I)
NEGATIVE = re.compile(r"(can\s*not|cannot|can't|do\s+not|does\s+not|don't|will\s+not|unable\s+to|no\s+longer)\s+"
                      r"(match|negotiate|reconsider|accept\s+appeals|consider\s+appeals|re-?evaluate)", re.I)


def extract(inst, entry, page, today_year):
    if common.professional_source(entry, page): return []
    head = (page.title + ' ' + ' '.join(page.headings[:8]) + ' ' + entry.get('url', '')).lower()
    if not re.search(r'appeal|special circumstance|professional judg|reconsider|scholarship|financial aid|sap', head):
        return []
    text = re.sub(r'\s+', ' ', page.text)
    sentences = [s.strip() for s in SENTENCE.split(text) if 30 <= len(s.strip()) <= 600]
    found = {}
    for s in sentences:
        if SKIP_SENTENCE.search(s): continue
        for kind, pat in KINDS:
            if re.search(pat, s, re.I):
                found.setdefault(kind, []).append(s)
                break
    if not found: return []
    year, basis, issues = common.resolve_year(page, entry, today_year)
    out = []
    for kind, sents in found.items():
        statements = [s for s in sents if not s.rstrip().endswith('?')]  # FAQ questions are context, not claims
        negative = [s for s in statements if NEGATIVE.search(s)]
        if not statements: continue
        offered = False if negative and len(negative) == len(statements) else (True if not negative else None)
        rec = {'appeal_kind': kind, 'offered': offered, 'qualifies_for_paid_addon': False,
               'process_summary': sents[0][:600], 'policy_url': common.source_of(entry)['url'],
               'notes': f'Extracted by {EXTRACTOR}; {len(sents)} matching sentence(s), copied verbatim. '
                        'Eligibility for the paid add-on is never set by the pipeline.'}
        if offered is None:
            rec['offered'] = False  # the database needs a value; the conflict is queued for review
        evidence = [{'field': 'sentence', 'value': kind, 'snippet': s[:400]} for s in sents[:6]]
        flags = issues + ['semantic_review_required'] + (['mixed_positive_and_negative_statements'] if offered is None else [])
        out.append(common.make('appeals', inst['institution_key'], year, basis, rec, evidence, entry, EXTRACTOR,
                               {'appeal_kind': kind}, {'sentences': len(sents), 'negative_sentences': len(negative)}, flags))
    return out
