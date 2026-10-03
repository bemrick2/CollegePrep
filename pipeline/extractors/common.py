"""Candidate records: contract-shaped records plus the evidence and checks a reviewer needs.

Extractors never mark anything verified. A candidate carries `verification_status: unverified`
until a reviewed decision promotes it (pipeline/promote.py). Every extracted value has a verbatim
snippet from the fetched document; values without one are not emitted.
"""
from __future__ import annotations
import hashlib, json, re
from urllib.parse import urlsplit

from .. import text as T

PIPELINE_VERSION = 'research-pipeline/1'


def candidate_id(domain, institution_key, academic_year, discriminator, extractor):
    raw = json.dumps([domain, institution_key, academic_year, discriminator, extractor], sort_keys=True)
    return hashlib.sha1(raw.encode()).hexdigest()[:16]


def source_of(entry):
    return {'url': T.canonical_url(entry.get('final_url') or entry['url']), 'requested_url': entry['url'], 'sha256': entry.get('sha256'),
            'fetched_at': entry.get('fetched_at'), 'last_modified': entry.get('last_modified'),
            'title': entry.get('title', ''), 'page_file': entry.get('page_file'), 'kind': entry.get('kind')}


def make(domain, inst_key, academic_year, year_basis, record, evidence, entry, extractor, discriminator,
         checks=None, issues=None):
    src = source_of(entry)
    rec = {'institution_key': inst_key, 'academic_year': academic_year, **record,
           'source_url': src['url'], 'verification_status': 'unverified',
           'last_verified_at': (entry.get('fetched_at') or '')[:10]}
    if year_basis == 'source_unlabeled':
        rec['academic_year_basis'] = 'aid_year_in_force_at_review_source_unlabeled'
    # The source document is part of the identity: two pages yielding the same record key must both
    # reach conflict detection instead of the first one silently winning.
    doc = src.get('sha256') or src.get('url')
    return {'candidate_id': candidate_id(domain, inst_key, academic_year, [discriminator, doc], extractor),
            'domain': domain, 'institution_key': inst_key, 'academic_year': academic_year,
            'year_basis': year_basis, 'record': rec, 'evidence': evidence, 'source': src,
            'extractor': extractor, 'pipeline_version': PIPELINE_VERSION,
            'checks': checks or {}, 'issues': list(issues or []) + (
                # A system site shared by several colleges' seeds may describe the system or another campus.
                ['shared_site_attribution_review'] if entry.get('shared_host') and inst_key else [])}


def resolve_year(page, entry, today_year):
    """(academic_year, basis, issues). Unlabeled pages are recorded as the year in force at review."""
    label, basis = T.dominant_year(page.text[:60000], page.title)
    issues = []
    if basis in {'ambiguous_year_labels', 'source_unlabeled'}:
        heads = T.year_labels(' | '.join(page.headings or []))
        if len(heads) == 1:  # one year in the section headings beats archive links in the body
            label, basis = next(iter(heads)), 'labeled_in_heading'
    if basis == 'source_unlabeled':
        # A document whose file name carries the only year ("2025-26-Dual-Enrollment-Agreement-Form.pdf",
        # Carson-Newman) is that year's document even when its text never prints the year.
        name = urlsplit(entry.get('final_url') or entry.get('url', '')).path.rsplit('/', 1)[-1]
        named = T.year_labels(name.replace('_', '-'))
        if len(named) == 1 and re.search(r'\.(pdf|xlsx)$', name, re.I):
            label, basis = next(iter(named)), 'labeled_in_url'
    if basis == 'ambiguous_year_labels':
        issues.append('ambiguous_year_labels')
        return today_year, basis, issues
    if label is None:
        return today_year, 'source_unlabeled', issues
    if label < today_year:
        issues.append(f'stale_year_label:{label}')
    return label, basis, issues


PROFESSIONAL = re.compile(r'(^|[./-])(law|pharmacy|medicine|medical|med|dental|dentistry|graduate|grad|osteopathic|veterinary|'
                          r'cvm|dvm|optometry|pa-program|msn|dnp|seminary)([./-]|$)', re.I)


def professional_source(entry, page) -> bool:
    """Graduate and professional-school pages (host or path) are outside undergraduate planning."""
    u = urlsplit(entry.get('final_url') or entry.get('url', ''))
    hit = PROFESSIONAL.search(u.netloc.split('.')[0]) or PROFESSIONAL.search(u.path)
    return bool(hit) and not re.search(r'undergraduate', page.title or '', re.I)


INTERNATIONAL = re.compile(r'international[\s_-]*(students?|applicants?|admissions?)|/international(?=/|\s|$|\?)', re.I)


def international_source(entry, page):
    """Budgets and awards for international students (PCC, Chemeketa, Centre) are not the domestic figures."""
    return bool(INTERNATIONAL.search((entry.get('url') or '') + ' ' + (page.title or '')))
