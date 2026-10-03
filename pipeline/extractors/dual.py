"""Dual-enrollment policy pages -> credit_policies candidates with policy_kind 'dual_enrollment'.

Structured fields (each from a cited line; nothing inferred):
  eligibility_tiers  [{grades, min_hs_gpa, alt_min_act, alt_min_sat, max_credit_hours_per_term, line}]
  min_hs_gpa / alt_min_act / alt_min_sat / max_credit_hours_per_term
                     filled only when every tier on the page agrees (otherwise left out and the
                     tiers carry the detail)
  per_credit_hour_charges  [{amount, kind: tuition|fee|state_grant|other, line}] every per-credit-hour amount as printed
                     (state_grant: an amount the state grant pays, not a price)
                     (often a post-grant price); tuition_per_credit_hour only when the line says tuition
  state_grant_accepted  True only from an explicit positive statement about the state dual-enrollment
                     grant; False only from an explicit negative one; omitted otherwise
  college_gpa_to_continue  GPA students must keep in college courses
Different numbers for the same field outside tiers become `conflicting_values:<field>`.
"""
from __future__ import annotations
import re

from . import common

EXTRACTOR = 'dual_enrollment/v1'
GRADES = [('9', r'\bfreshm[ae]n|\b9th\s+grade|ninth\s+grade'), ('10', r'\bsophomores?\b|\b10th\s+grade|tenth\s+grade'),
          ('11', r'\bjuniors?\b|\b11th\s+grade|eleventh\s+grade'), ('12', r'\bseniors?\b|\b12th\s+grade|twelfth\s+grade')]
GPA = re.compile(r'(?:gpa|grade\s+point\s+average)\s*(?:\(gpa\)\s*)?(?:of|:)?\s*(?:at\s+least\s+|a\s+minimum\s+of\s+)?(\d\.\d{1,2})'
                 r'|(\d\.\d{1,2})\s*\+?\s*(?:\((?:on\s+a\s+)?4\.0\s+scale\)\s*)?(?:or\s+(?:higher|above|better)\s+)?(?:cumulative\s+|unweighted\s+|high\s+school\s+)?(?:gpa|grade\s+point)', re.I)
ACT = re.compile(r'(\d{2})\s*\+?\s*(?:or\s+(?:higher|above)\s+)?(?:on\s+the\s+)?(?:composite\s+)?act\b|\bact\s+(?:composite\s+)?(?:score\s+)?(?:of\s+)?(\d{2})\b', re.I)
SAT = re.compile(r'(\d{3,4})\s*\+?\s*(?:\(?[a-z\s-]*\)?\s*)?(?:on\s+the\s+)?sat\b|\bsat\s+(?:composite\s+|total\s+)?(?:score\s+)?(?:of\s+)?(\d{3,4})\b', re.I)
MAX_HOURS = re.compile(r'(?:maximum\s+of|up\s+to|no\s+more\s+than|max(?:imum)?\.?)\s+(\d{1,2})\s+(?:credit\s+)?(?:hours|credits)', re.I)
PER_HOUR = re.compile(r'\$\s?(\d{1,4})(?:\.(\d{2}))?\s*(?:/|per)\s*(?:credit\s*)?(?:hour|hr|credit)', re.I)
# State programs that pay for dual enrollment: TN Dual Enrollment Grant (DEG), KY Dual Credit Scholarship, ...
GRANT = re.compile(r'dual\s+(?:enrollment|credit)\s+(?:grant|scholarship)|\bDEG\b|state\s+(?:dual\s+(?:enrollment|credit)\s+)?grant|TN\s+(?:DE\s+)?grant', re.I)
TOPIC = re.compile(r'dual[\s_-]*(?:enroll|credit)|concurrent[\s_-]+enrollment|early[\s_-]+college|accelerated[\s_-]+learning', re.I)
GRANT_NO = re.compile(r'(does\s+not|doesn.t|do\s+not|may\s+not|cannot|can.t|not)\s+(be\s+)?(apply|eligible|accept|available|qualify|use|used)|no\s+discounts', re.I)
GRANT_YES = re.compile(r'\b(apply|applies|eligible|accept|accepted|covers|use|may\s+be\s+used|can\s+be\s+used)\b', re.I)
CONTINUE = re.compile(r'maintain\s+(?:a\s+)?(?:cumulative\s+)?(?:college\s+)?(?:gpa\s+of\s+)?(\d\.\d{1,2})\s*(?:cumulative\s+)?(?:college\s+)?(?:gpa)?', re.I)
# A requirement for one kind of course (KCTCS: "Technical Education Dual Credit Courses ... 2.0 GPA") is
# not the page's general minimum.
SCOPED = re.compile(r'career[- ]and[- ]technical|\btechnical\b|\bCTE\b|\bvocational\b', re.I)
# GPA lines that are not the high-school admission minimum: college/dual-enrollment course GPAs, prerequisite
# waivers, placement-test alternatives, single-course prerequisites and special-population programs (TN r5:
# Welch, Nashville State, Columbia State, Freed-Hardeman).
NOT_ELIGIBILITY = re.compile(r'postsecondary\s+courses|courses?\s+attempted|hours\s+of\s+\w+\s+dual\s+enrollment|dual\s+enrollment\s+(?:courses|hours)|'
                             r'waiv|placement|\bIEP\b|gifted|algebra|in\s+the\s+(?:two|three)\s+high\s+school', re.I)
GRANT_PAYS = re.compile(r'(?:grant|DEG)\b.{0,80}\b(?:provides?|pays?|covers?|awarded|will\s+receive|receive)\b|\b(?:awarded|receive)\b.{0,40}(?:grant|DEG)\b', re.I)
OFF_TOPIC = re.compile(r'hepatitis|title\s+ix|misconduct|privacy\s+act|immuniz|vaccin', re.I)


def _num(m):
    return next((g for g in m.groups() if g), None)


COMPLETED = re.compile(r'\b(?:complet(?:ed|ion of)|finish(?:ed)?)\s+(?:your\s+|the\s+|their\s+|his or her\s+)?'
                       r'(freshm[ae]n|sophomore|junior|9th\s+grade|10th\s+grade|11th\s+grade)\b', re.I)
NEXT = {'freshman': '10', 'freshmen': '10', 'sophomore': '11', 'junior': '12', '9th grade': '10', '10th grade': '11', '11th grade': '12'}


def _grades(line):
    m = COMPLETED.search(line)  # "Have you completed your sophomore year?" (UTC) means rising juniors and up
    if m:
        first = NEXT[re.sub(r'\s+', ' ', m.group(1).lower())]
        return [g for g in ('10', '11', '12') if int(g) >= int(first)]
    listed = set(re.findall(r'\b(9|10|11|12)th\b(?=[^.;]{0,40}?\bgrades?\b)', line, re.I))  # "10th, 11th, or 12th grade"
    return [g for g, rx in GRADES if g in listed or re.search(rx, line, re.I)]


def extract(inst, entry, page, today_year):
    if common.professional_source(entry, page): return []
    head = page.title + ' ' + entry.get('url', '')  # the page itself must be about dual enrollment
    if not TOPIC.search(head): return []
    # A named institutional award ("Bibb Family Dual Enrollment Scholarship", APSU): its GPA and renewal rules
    # are the award's, not the dual enrollment program's.
    # Plural program pages stay ("Student Eligibility for Dual Enrollment Scholarships", AL: Trenholm State).
    if re.search(r'scholarship(?!s)', page.title, re.I) and not re.search(r'eligib|program', page.title, re.I): return []
    lines = [l for l in page.lines if 15 <= len(l) <= 400 and not OFF_TOPIC.search(l)]
    glossary = bool(re.search(r'glossary|definitions|terms\s+to\s+know', head, re.I))  # KY, Owensboro: "GPA of 2.0 (a C average)" defines a term
    tiers, evidence, values = [], [], {}

    def note(field, value, line):
        values.setdefault(field, set()).add(value)
        evidence.append({'field': field, 'value': value, 'snippet': line[:300]})

    context_grades, context_left = [], 0
    charges = []
    for line in lines:
        g = _grades(line)
        if g and not re.search(r'\d', line):
            context_grades, context_left = g, 2  # a heading like "High School Juniors & Seniors" applies to the next lines only
        elif context_left: context_left -= 1
        if not context_left and not (g and not re.search(r'\d', line)): context_grades = []
        gpa_m = GPA.search(line)
        if gpa_m and re.search(r'college|maintain|continu|probation|remain', line, re.I) and not re.search(r'high\s+school', line, re.I):
            gpa_m = None  # a college GPA to keep eligibility, handled below
        if gpa_m and glossary: gpa_m = None
        if gpa_m and NOT_ELIGIBILITY.search(line): gpa_m = None
        if gpa_m:
            gpa = float(_num(gpa_m))
            rng = re.search(r'(\d\.\d{1,2})\s*(?:to|-|–)\s*' + re.escape(_num(gpa_m)) + r'(?!\d)', line)
            if rng and float(rng.group(1)) < gpa:
                gpa = float(rng.group(1))  # "an unweighted 2.5 to 2.79 GPA": the band starts at 2.5
            if 1.5 <= gpa <= 4.0:
                act = next((int(_num(m)) for m in ACT.finditer(line) if 12 <= int(_num(m)) <= 36), None)
                sat = next((int(_num(m)) for m in SAT.finditer(line) if 400 <= int(_num(m)) <= 1600), None)
                hours = next((int(m.group(1)) for m in MAX_HOURS.finditer(line) if 1 <= int(m.group(1)) <= 21), None)
                tier = {'grades': g or context_grades, 'min_hs_gpa': gpa, 'line': line[:300]}
                if SCOPED.search(line): tier['course_scope'] = SCOPED.search(line).group(0).lower()
                if act: tier['alt_min_act'] = act
                if sat: tier['alt_min_sat'] = sat
                if hours: tier['max_credit_hours_per_term'] = hours
                if tier not in tiers: tiers.append(tier)
                evidence.append({'field': 'eligibility_tier', 'value': gpa, 'snippet': line[:300]})
        for m in MAX_HOURS.finditer(line):
            v = int(m.group(1))
            if 1 <= v <= 21 and re.search(r'semester|term|fall|spring', line, re.I) and not re.search(r'summer', line[:m.start()], re.I):
                note('max_credit_hours_per_term', v, line)
        question = '?' in line or re.search(r'^\W*(is|are|do|does|can|will|how|what|why|when)\b|,\s*(are|is|do|does|can|will)\s+(we|you|i|students?)\b', line, re.I)
        for m in ([] if question else PER_HOUR.finditer(line)):  # FAQ questions quote prices they ask about
            v = int(m.group(1)) + (int(m.group(2)) / 100 if m.group(2) and m.group(2) != '00' else 0)
            near = line[max(0, m.start() - 40):m.end() + 30]
            kind = ('state_grant' if GRANT_PAYS.search(line) and re.search(r'grant|DEG', near, re.I) else
                    'fee' if re.search(r'\bfee', near, re.I) else 'tuition' if re.search(r'tuition', near, re.I) else 'other')
            item = {'amount': v, 'kind': kind, 'line': line[:300]}
            if item not in charges: charges.append(item)
            evidence.append({'field': 'per_credit_hour_charge', 'value': v, 'snippet': line[:300]})
        if GRANT.search(line):
            if GRANT_NO.search(line): note('state_grant_accepted', False, line)
            elif GRANT_YES.search(line) and not line.rstrip().endswith('?'): note('state_grant_accepted', True, line)
        m = CONTINUE.search(line)
        if m and re.search(r'college|grant|eligib|DEG', line, re.I):
            v = float(m.group(1))
            if 1.0 <= v <= 4.0: note('college_gpa_to_continue', v, line)
    if not tiers and not values and not charges: return []
    year, basis, issues = common.resolve_year(page, entry, today_year)
    de = {}
    if tiers:
        de['eligibility_tiers'] = tiers
        if any(re.search(r'\S\s{5,}\S', t['line']) for t in tiers):
            issues.append('multicolumn_layout_review')  # Motlow: side-by-side columns interleave words into one line
        general = [t for t in tiers if 'course_scope' not in t]
        for field in ('min_hs_gpa', 'alt_min_act', 'alt_min_sat'):
            seen = {t.get(field) for t in general if t.get(field) is not None}
            if general and len(seen) == 1 and all(t.get(field) is not None for t in general): de[field] = seen.pop()
    if charges:
        de['per_credit_hour_charges'] = charges
        tuition = {c['amount'] for c in charges if c['kind'] == 'tuition'}
        if len(tuition) == 1: de['tuition_per_credit_hour'] = tuition.pop()
    for field, vs in values.items():
        if field == 'state_grant_accepted' and vs == {True, False}:
            # A page can say the grant applies to juniors/seniors and not to sophomores: keep both, flag.
            issues.append('state_grant_mixed_statements'); continue
        if len(vs) > 1:
            if field == 'max_credit_hours_per_term' and tiers and all('max_credit_hours_per_term' in t for t in tiers):
                continue  # per-tier caps already captured in the tiers
            issues.append(f'conflicting_values:{field}'); continue
        de[field] = next(iter(vs))
    rec = {'policy_kind': 'dual_enrollment', 'policy_url': common.source_of(entry)['url'], 'equivalencies': [],
           'dual_enrollment': de,
           'notes': f'Extracted by {EXTRACTOR}; every field cites its line. Eligibility tiers are kept as printed.'}
    checks = {'fields': sorted(k for k in de if k != 'eligibility_tiers'), 'tiers': len(tiers)}
    return [common.make('credit_policies', inst['institution_key'], year, basis, rec, evidence, entry, EXTRACTOR,
                        {'policy_kind': 'dual_enrollment'}, checks, issues)]
