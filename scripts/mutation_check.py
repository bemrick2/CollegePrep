#!/usr/bin/env python3
"""Mutation checks for the research pipeline's safety rules.

Each entry breaks one rule in the source; the pipeline test suite must then fail ("KILLED").
A surviving mutant means a safety rule has no test. Run: python scripts/mutation_check.py
"""
import shutil, subprocess, sys

MUTS = [
    ('pipeline/extractors/costs.py', "cols[0]['period'] = cols[1]['period'] = 'semester'; cols[2]['period'] = 'year'", "pass"),
    ('pipeline/extractors/costs.py', "if c['period'] is None and re.fullmatch(r'\\W*(annual\\s+)?total\\W*', c['header'] or '', re.I): c['period'] = 'year'", "pass"),
    ('pipeline/extractors/credit.py', "            course = None  # \"Credit Granted | 12\"", "            pass  # \"Credit Granted | 12\""),
    ('pipeline/extractors/cds.py', "issues.append('zero_counts_with_enrollment')", "pass"),
    ('pipeline/extractors/credit.py', "if score and not re.search(r'\\d', score) and not course: continue", "pass"),
    ('pipeline/extractors/dual.py', "    if floor:  # ", "    if False:  # "),
    ('pipeline/extractors/transfer.py', "if part: v = int(part.group(1))", "pass"),
    ('pipeline/extractors/merit.py', "r'outside[- ]scholarships?|external[- ]scholarships?|third[- ]party|military|veteran|foundation|/isap/|donor[- ]scholarships?', re.I)", "r'^$', re.I)"),
    ('pipeline/extractors/dual.py', "sat = None if sections else next(", "sat = None if False else next("),
    ('pipeline/extractors/dual.py', "if named or not m: return named", "if not m: return named"),
    ('pipeline/extractors/credit.py', "        course = pick_course()\n        body = rows[1:]", "        body = rows[1:]"),
    ('pipeline/review.py', "key=lambda c: (c['source']['url'].startswith('https://'), len(fields_of(c))", "key=lambda c: (False, len(fields_of(c))"),
    ('pipeline/crawl.py', "if https_site and url.startswith('http://'):", "if False:"),
    ('pipeline/extractors/merit.py', "if any(len(c) > 60 for c in header): continue", "pass"),
    ('pipeline/extractors/merit.py', "if re.search(r'\\bcollege\\s+gpa\\b', ' '.join(header), re.I): continue", "pass"),
    ('pipeline/extractors/merit.py', "and not re.search(r'criteria|requirement|eligib|amount|annual|per\\s+year|years?\\b|value|total|\\$', h, re.I)), None)", "), None)"),
    ('pipeline/extractors/dual.py', "if re.search(r'scholarship(?!s)', page.title, re.I) and not re.search(r'eligib|program', page.title, re.I): return []", "pass"),
    ('pipeline/extractors/dual.py', "named = [g for g, rx in GRADES if g in listed or re.search(rx, rest, re.I)]", "named = [g for g, rx in GRADES if re.search(rx, rest, re.I)]"),
    ('pipeline/extractors/dual.py', "if named or not m: return named", "if True: return named"),
    ('pipeline/extractors/dual.py', "issues.append('multicolumn_layout_review')", "pass"),
    ('pipeline/extractors/common.py', "label, basis = next(iter(named)), 'labeled_in_url'", "pass"),
    ('pipeline/text.py', "if kv and not TRACKING.match(kv.split('=', 1)[0])", "if kv"),
    ('pipeline/crawl.py', "and score >= DOC_EXTRA_SCORE and is_document_url(url)", "and score >= 0"),
    ('pipeline/crawl.py', "if depth > max_depth and not (depth == max_depth + 1", "if depth > max_depth and not (False"),
    ('pipeline/topics.py', "or COURSE_PAGE.search(url): return -1", ": return -1"),
    ('pipeline/crawl.py', "if not self.allowed(url):", "if False:"),
    ('pipeline/promote.py', "RANK.get(record['verification_status'], 0) < 3 or ", "False and "),
    ('pipeline/review.py', "c['issues'].append('conflicts_with_verified_record')", "pass"),
    ('pipeline/extractors/costs.py', "'on_campus_food_housing': one('food_housing') if primary[0] == 'on_campus' else None",
     "'on_campus_food_housing': (one('housing') or 0) + (one('food') or 0)"),
    ('pipeline/extractors/credit.py', "if not hit: continue", "hit = hit or ('AP-X', 'AP X')"),
    ('pipeline/extractors/cds.py', "if len(nums) >= 3: return nums[-1], nums[:-1], nums[-1] == sum(nums[:-1])",
     "if len(nums) >= 3: return nums[-1], nums[:-1], True"),
    ('pipeline/extractors/appeals.py', "'qualifies_for_paid_addon': False", "'qualifies_for_paid_addon': True"),
    ('pipeline/extractors/statepolicy.py', "issues + ['semantic_review_required']", "issues"),
    ('pipeline/extractors/statepolicy.py', "if inst.get('control') != 'state' or not inst['institution_key'].startswith('state-'): return []", "pass"),
    ('pipeline/registry.py', "(h not in shared and h != rd and host.endswith('.' + h))", "host.endswith('.' + h)"),
    ('pipeline/registry.py', "if rd in (inst.get('shared_domains') or []):", "if False:"),
    ('pipeline/review.py', "(STATE_EXTRACTORS if inst.get('control') == 'state' else EXTRACTORS)", "EXTRACTORS"),
    ('pipeline/extractors/dual.py', "if SCOPED.search(line): tier['course_scope']", "if False: tier['course_scope']"),
    ('pipeline/extractors/costs.py', "and not private and not HOUSING_RESIDENT.search(h)", ""),
    ('pipeline/registry.py', "if any(host == h or host.endswith('.' + h) for h in inst.get('excluded_hosts') or []): return False", "pass"),
    ('pipeline/extractors/common.py', "if entry.get('shared_host') and inst_key else []", "if False else []"),
    ('pipeline/extractors/dual.py', "if GRANT_NO.search(line): note('state_grant_accepted', False, line)", "if False: pass"),
    ('pipeline/extractors/dual.py', "if general and len(seen) == 1 and all(t.get(field) is not None for t in general): de[field] = seen.pop()",
     "if seen: de[field] = max(seen)"),
    ('pipeline/extractors/dual.py', "head = page.title + ' ' + entry.get('url', '')", "head = page.title + ' ' + entry.get('url', '') + ' dual enrollment'"),
    ('pipeline/review.py', "else: issues.append(f'conflicting_sources:{name}')", "else: out[name] = vals[0]"),
    ('pipeline/extractors/common.py', "doc = src.get('sha256') or src.get('url')", "doc = None"),
    ('pipeline/extractors/dual.py', "'fee' if re.search(r'\\bfee', near, re.I) else 'tuition' if re.search(r'tuition', near, re.I) else 'other')",
     "'tuition')"),
    ('pipeline/extractors/dual.py', "kind = ('state_grant' if GRANT_PAYS.search(line)", "kind = ('state_grant' if False"),
    ('pipeline/extractors/dual.py', "if gpa_m and NOT_ELIGIBILITY.search(line): gpa_m = None", "pass"),
    ('pipeline/extractors/transfer.py', "if not SCOPED_GRADE.search(s):", "if True:"),
    ('pipeline/extractors/merit.py', "(x if not PLACEHOLDER.match(x) else '' for x in", "(x for x in"),
    ('pipeline/extractors/merit.py', "lo = None  # \"Up to $5,000\" is a maximum", "pass  # \"Up to $5,000\" is a maximum"),
    ('pipeline/text.py', "continue  # \"PHYS 2010/2011\"", "pass  # \"PHYS 2010/2011\""),
    ('pipeline/crawl.py', "return self.challenges.get(host, 0) >= self.CHALLENGE_STOP", "return False"),
    ('pipeline/extractors/programmap.py', "if len(labels) != 1: return []", "labels = labels or {'2026-27': 1}"),
    ('pipeline/extractors/programmap.py', "cont = last and (last[1] is None or wrapped or", "cont = last and (last[1] is None or"),
    ('pipeline/extractors/merit.py', "rec_year, rec_basis = T.academic_year(first), 'labeled_entering_class'", "rec_year, rec_basis = T.academic_year(first), 'labeled_in_source'"),
    ('pipeline/extractors/costs.py', "return []  # budgets for less-than-full-time enrollment", "pass  # budgets for less-than-full-time enrollment"),
    ('pipeline/extractors/merit.py', "criteria = next((i for i, h in enumerate(header) if i != renewal and", "criteria = next((i for i, h in enumerate(header) if"),
    ('pipeline/extractors/transfer.py', "return []  # hour counts there are award or reverse-transfer conditions", "pass  # hour counts there are award or reverse-transfer conditions"),
]
failed = False
for f, old, new in MUTS:
    original = open(f).read()
    assert old in original, (f, old)
    try:
        open(f, 'w').write(original.replace(old, new, 1))
        try:
            r = subprocess.run([sys.executable, '-m', 'unittest', 'tests.test_pipeline'], capture_output=True, text=True, timeout=90)
            verdict = 'KILLED ' if r.returncode else 'SURVIVED'
        except subprocess.TimeoutExpired:
            verdict = 'TIMEOUT'
    finally:
        open(f, 'w').write(original)
    print(verdict, f, old[:60], flush=True)
    failed = failed or verdict != 'KILLED '
sys.exit(1 if failed else 0)
