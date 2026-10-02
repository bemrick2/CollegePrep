"""Statewide policy pages -> state_policies candidates (transfer guarantee / articulation, tuition residency).

Prose policies are kept as verbatim statements grouped by role, never paraphrased:
  guarantees   sentences stating what is guaranteed or will transfer
  exceptions   sentences limiting a guarantee ("does not guarantee", "competitive", "may require")
  requirements sentences stating what a student must do or meet
  effective    sentences stating when the policy took effect or how often it is reviewed
Every candidate is `semantic_review_required`: grouping sentences by keywords is not proof of meaning.
"""
from __future__ import annotations
import re

from . import common

EXTRACTOR = 'state_policy/v1'
SENTENCE = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')
KINDS = [  # most specific first: a dual-admissions page lives under an "articulation-and-transfer" URL
    ('transfer_guarantee', r'transfer\s+(admission\s+)?guarantee|guaranteed\s+(admission|transfer)'),
    ('dual_admission', r'dual[\s_-]+admission'),
    ('dual_enrollment', r'dual[\s_-]*(enrollment|credit)\s+policy|dual[\s_-]*(enrollment|credit)\b(?!.*(report|success|dashboard))'),
    ('statewide_articulation', r'transfer\s+pathway|articulation|common\s+course|reverse\s+transfer|transfer\s+maps?\b|'
                               r'statewide\s+transfer|transfer\s+agreements?|general\s+education\s+(transfer|certification)|transfer\s+policy'),
    ('tuition_residency', r'residen(cy|t)\s+(classification|status|for\s+tuition|determination)|classification\s+of\s+students|in-state\s+tuition|out-of-state\s+tuition|domicile|determination\s+of\s+residency'),
]
ROLES = [
    ('exceptions', r'(does|do|will)\s+not\s+guarantee|not\s+guaranteed|competitive|may\s+(require|have\s+additional)|except|however|not\s+every'),
    ('guarantees', r'guarantee|will\s+(transfer|be\s+accepted|earn)|junior\s+standing|all\s+courses\s+transfer'),
    ('effective', r'effective|in\s+effect|reviewed\s+annually|updated|beginning\s+(fall|spring)'),
    ('requirements', r'must|required|responsible\s+for|requires?|eligib|domicil|12\s+months|twelve\s+months|lawfully|presum'),
]
NAV = re.compile(r'^(skip to|search|home|contact|go to|section|menu)\b', re.I)


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60]


def extract(inst, entry, page, today_year):
    state = inst.get('state') or (inst['institution_key'][6:] if inst['institution_key'].startswith('state-') else None)
    if not state: return []  # institution pages keep their own domains; this extractor reads statewide sources
    head = page.title + ' ' + entry.get('url', '')
    if re.search(r'report|fact\s*book|minutes|agenda|newsletter|presentation|dashboard', head, re.I): return []  # about policy, not policy
    # Regulations are often titled by number ("Title 013 Chapter 2 Regulation 045"); their subject is the
    # first heading or the opening text ("Determination of residency status for ... tuition assessment").
    opening = ' '.join((page.headings or [])[:3]) + ' ' + ' '.join(l for l in page.lines[:40] if len(l) > 30)[:800]
    kind = next((k for k, rx in KINDS if re.search(rx, head, re.I)), None) or \
        next((k for k, rx in KINDS if re.search(rx, opening, re.I)), None)
    if not kind: return []
    text = ' '.join(l for l in page.lines if len(l) > 40 and not NAV.search(l))
    sentences = [s.strip() for s in SENTENCE.split(text) if 30 <= len(s.strip()) <= 600 and not s.strip().endswith('?')]
    grouped = {}
    for s in sentences:
        role = next((r for r, rx in ROLES if re.search(rx, s, re.I)), None)
        if role: grouped.setdefault(role, []).append(s)
    if not grouped.get('guarantees') and not grouped.get('requirements'): return []
    year, basis, issues = common.resolve_year(page, entry, today_year)
    title = re.split(r'\s+[|–-]\s+', page.title)[0].strip() or kind.replace('_', ' ')
    rec = {'state': state, 'policy_kind': kind, 'policy_key': slug(f'{title}'), 'title': title,
           'summary': (grouped.get('guarantees') or grouped.get('requirements'))[0][:600],
           'statements': {r: v[:12] for r, v in grouped.items()}, 'policy_url': common.source_of(entry)['url'],
           'notes': f'Extracted by {EXTRACTOR}; statements are copied verbatim and grouped by keyword, pending review.'}
    evidence = [{'field': f'statements.{r}', 'value': len(v), 'snippet': v[0][:300]} for r, v in grouped.items()]
    c = common.make('state_policies', None, year, basis, rec, evidence, entry, EXTRACTOR,
                    {'policy_kind': kind, 'policy_key': rec['policy_key']}, {k: len(v) for k, v in grouped.items()},
                    issues + ['semantic_review_required'])
    c['record'].pop('institution_key', None)
    c['institution_key'] = inst['institution_key']
    return [c]
