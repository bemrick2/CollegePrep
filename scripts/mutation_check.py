#!/usr/bin/env python3
"""Mutation checks for the research pipeline's safety rules.

Each entry breaks one rule in the source; the pipeline test suite must then fail ("KILLED").
A surviving mutant means a safety rule has no test. Run: python scripts/mutation_check.py
"""
import shutil, subprocess, sys

MUTS = [
    ('pipeline/crawl.py', "if not self.allowed(url):", "if False:"),
    ('pipeline/promote.py', "RANK.get(record['verification_status'], 0) < 3 or ", "False and "),
    ('pipeline/review.py', "c['issues'].append('conflicts_with_verified_record')", "pass"),
    ('pipeline/extractors/costs.py', "'on_campus_food_housing': one('food_housing') if primary[0] == 'on_campus' else None",
     "'on_campus_food_housing': (one('housing') or 0) + (one('food') or 0)"),
    ('pipeline/extractors/credit.py', "if not hit: continue", "hit = hit or ('AP-X', 'AP X')"),
    ('pipeline/extractors/cds.py', "if len(nums) >= 3: return nums[-1], nums[:-1], nums[-1] == sum(nums[:-1])",
     "if len(nums) >= 3: return nums[-1], nums[:-1], True"),
    ('pipeline/extractors/appeals.py', "'qualifies_for_paid_addon': False", "'qualifies_for_paid_addon': True"),
    ('pipeline/extractors/dual.py', "if GRANT_NO.search(line): note('state_grant_accepted', False, line)", "if False: pass"),
    ('pipeline/extractors/dual.py', "if len(seen) == 1 and all(t.get(field) is not None for t in tiers): de[field] = seen.pop()",
     "if seen: de[field] = max(seen)"),
    ('pipeline/extractors/dual.py', "head = page.title + ' ' + entry.get('url', '')", "head = page.title + ' ' + entry.get('url', '') + ' dual enrollment'"),
    ('pipeline/review.py', "else: issues.append(f'conflicting_sources:{name}')", "else: out[name] = vals[0]"),
    ('pipeline/extractors/common.py', "doc = src.get('sha256') or src.get('url')", "doc = None"),
    ('pipeline/extractors/dual.py', "kind = 'fee' if re.search(r'\\bfee', near, re.I) else 'tuition' if re.search(r'tuition', near, re.I) else 'other'",
     "kind = 'tuition'"),
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
