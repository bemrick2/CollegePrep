#!/usr/bin/env python3
"""Mutation checks for the research pipeline's safety rules.

Each entry breaks one rule in the source; the pipeline test suite must then fail ("KILLED").
A surviving mutant means a safety rule has no test. Run: python scripts/mutation_check.py
"""
import concurrent.futures, os, queue, shutil, subprocess, sys, tempfile

MUTS = [
    ('pipeline/extractors/credit.py', "if bad_score and bad_score >= len(eqs) * 0.3: issues = issues + ['score_column_not_scores']", 'pass'),
    ('pipeline/extractors/credit.py', "if eqs and all(not e['institution_course_equivalent'] for e in eqs): issues = issues + ['course_column_missing']", 'pass'),
    ('pipeline/promote.py', 'raise ValueError(f"{c[\'candidate_id\']}: requirement row for program', 'pass  # (f"{c[\'candidate_id\']}: requirement row for program'),
    ('pipeline/exams.py', "r'(?<!art\\s)(?<!art)\\bhistory\\b(?!\\s+of\\s+art)'", "r'\\bhistory\\b'"),
    ('pipeline/extractors/catalog.py', ".split(' - ')[0].split(' | ')[0].strip()", ".split(' - ')[0].strip()"),
    ('pipeline/extractors/merit.py', "cell = re.sub(r'\\([^)]*(?:over|total|years?|4-year|four)[^)]*\\)', '', cell or '', flags=re.I)", 'pass'),
    ('pipeline/extractors/catalog.py', "lambda m: '' if m.group(1) in notes else m.group(0)", 'lambda m: m.group(0)'),
    ('pipeline/extractors/catalog.py', "rd.update(group_type='elective_pool', courses=g['courses'])", "rd.update(group_type='all_required', courses=g['courses'])"),
    ('pipeline/extractors/costs.py', "cols[0]['period'] = cols[1]['period'] = 'semester'; cols[2]['period'] = 'year'", 'pass'),
    ('pipeline/extractors/costs.py', "if c['period'] is None and re.fullmatch(r'\\W*(annual\\s+)?total\\W*', c['header'] or '', re.I): c['period'] = 'year'", 'pass'),
    ('pipeline/extractors/credit.py', '            course = None  # "Credit Granted | 12"', '            pass  # "Credit Granted | 12"'),
    ('pipeline/extractors/cds.py', "issues.append('zero_counts_with_enrollment')", 'pass'),
    ('pipeline/extractors/credit.py', "if score and not re.search(r'\\d', score) and not course: continue", 'pass'),
    ('pipeline/extractors/dual.py', '    if floor:  # ', '    if False:  # '),
    ('pipeline/extractors/transfer.py', 'if part: v = words.get(part.group(1).lower()) or int(part.group(1))', 'pass'),
    ('pipeline/extractors/merit.py', "r'outside[- ]scholarships?|external[- ]scholarships?|third[- ]party|military|veteran|foundation|/isap/|donor[- ]scholarships?|'", "r'^$|'"),
    ('pipeline/extractors/dual.py', 'sat = None if sections else next(', 'sat = None if False else next('),
    ('pipeline/extractors/dual.py', 'if named or not m: return named', 'if not m: return named'),
    ('pipeline/extractors/credit.py', '        course = pick_course()\n        body = rows[1:]', '        body = rows[1:]'),
    ('pipeline/review.py', "key=lambda c: (c['source']['url'].startswith('https://'), len(fields_of(c))", 'key=lambda c: (False, len(fields_of(c))'),
    ('pipeline/crawl.py', "if https_site and url.startswith('http://'):", 'if False:'),
    ('pipeline/extractors/merit.py', 'if any(len(c) > 60 for c in header): continue', 'pass'),
    ('pipeline/extractors/merit.py', "if re.search(r'\\bcollege\\s+gpa\\b', ' '.join(header), re.I): continue", 'pass'),
    ('pipeline/extractors/merit.py', "and not re.search(r'criteria|requirement|eligib|amount|annual|per\\s+year|years?\\b|value|total|\\$', h, re.I)), None)", '), None)'),
    ('pipeline/extractors/dual.py', "if re.search(r'scholarship(?!s)', page.title, re.I) and not re.search(r'eligib|program', page.title, re.I): return []", 'pass'),
    ('pipeline/extractors/dual.py', 'named = [g for g, rx in GRADES if g in listed or re.search(rx, rest, re.I)]', 'named = [g for g, rx in GRADES if re.search(rx, rest, re.I)]'),
    ('pipeline/extractors/dual.py', 'if named or not m: return named', 'if True: return named'),
    ('pipeline/extractors/dual.py', "issues.append('multicolumn_layout_review')", 'pass'),
    ('pipeline/extractors/common.py', "label, basis = next(iter(named)), 'labeled_in_url'", 'pass'),
    ('pipeline/text.py', "if kv and not TRACKING.match(kv.split('=', 1)[0])", 'if kv'),
    ('pipeline/crawl.py', 'and score >= DOC_EXTRA_SCORE and is_document_url(url)', 'and score >= 0'),
    ('pipeline/crawl.py', 'if depth > max_depth and not (depth == max_depth + 1', 'if depth > max_depth and not (False'),
    ('pipeline/topics.py', 'or COURSE_PAGE.search(url): return -1', ': return -1'),
    ('pipeline/crawl.py', 'if not self.allowed(url):', 'if False:'),
    ('pipeline/promote.py', "RANK.get(record['verification_status'], 0) < 3 or ", 'False and '),
    ('pipeline/review.py', "c['issues'].append('conflicts_with_verified_record')", 'pass'),
    ('pipeline/extractors/costs.py', "'on_campus_food_housing': one('food_housing') if primary[0] == 'on_campus' else None", "'on_campus_food_housing': (one('housing') or 0) + (one('food') or 0)"),
    ('pipeline/extractors/credit.py', 'if not hit: continue', "hit = hit or ('AP-X', 'AP X')"),
    ('pipeline/extractors/cds.py', 'if len(nums) >= 3: return nums[-1], nums[:-1], nums[-1] == sum(nums[:-1])', 'if len(nums) >= 3: return nums[-1], nums[:-1], True'),
    ('pipeline/extractors/appeals.py', "'qualifies_for_paid_addon': False", "'qualifies_for_paid_addon': True"),
    ('pipeline/extractors/statepolicy.py', "issues + ['semantic_review_required']", 'issues'),
    ('pipeline/extractors/statepolicy.py', "if inst.get('control') != 'state' or not inst['institution_key'].startswith('state-'): return []", 'pass'),
    ('pipeline/registry.py', "(h not in shared and h != rd and host.endswith('.' + h))", "host.endswith('.' + h)"),
    ('pipeline/registry.py', "if rd in (inst.get('shared_domains') or []):", 'if False:'),
    ('pipeline/review.py', "(STATE_EXTRACTORS if inst.get('control') == 'state' else EXTRACTORS)", 'EXTRACTORS'),
    ('pipeline/extractors/dual.py', "if SCOPED.search(line): tier['course_scope']", "if False: tier['course_scope']"),
    ('pipeline/extractors/costs.py', 'and not private and not HOUSING_RESIDENT.search(h)', ''),
    ('pipeline/registry.py', "if any(host == h or host.endswith('.' + h) for h in inst.get('excluded_hosts') or []): return False", 'pass'),
    ('pipeline/extractors/common.py', "if entry.get('shared_host') and inst_key else []", 'if False else []'),
    ('pipeline/extractors/dual.py', "if GRANT_NO.search(line): note('state_grant_accepted', False, line)", 'if False: pass'),
    ('pipeline/extractors/dual.py', 'if general and len(seen) == 1 and all(t.get(field) is not None for t in general): de[field] = seen.pop()', 'if seen: de[field] = max(seen)'),
    ('pipeline/extractors/dual.py', "head = page.title + ' ' + entry.get('url', '')", "head = page.title + ' ' + entry.get('url', '') + ' dual enrollment'"),
    ('pipeline/review.py', "else: issues.append(f'conflicting_sources:{name}')", 'else: out[name] = vals[0]'),
    ('pipeline/extractors/common.py', "doc = src.get('sha256') or src.get('url')", 'doc = None'),
    ('pipeline/extractors/dual.py', "'fee' if re.search(r'\\bfee', near, re.I) else 'tuition' if re.search(r'tuition', near, re.I) else 'other')", "'tuition')"),
    ('pipeline/extractors/dual.py', "kind = ('state_grant' if GRANT_PAYS.search(line)", "kind = ('state_grant' if False"),
    ('pipeline/extractors/dual.py', 'if gpa_m and NOT_ELIGIBILITY.search(line): gpa_m = None', 'pass'),
    ('pipeline/extractors/transfer.py', 'if not SCOPED_GRADE.search(s):', 'if True:'),
    ('pipeline/extractors/merit.py', "(x if not (PLACEHOLDER.match(x) or PHONE.search(x) or '@' in x or YES_NO.fullmatch(x)) else '' for x in", '(x for x in'),
    ('pipeline/extractors/merit.py', 'lo = None  # "Up to $5,000" is a maximum', 'pass  # "Up to $5,000" is a maximum'),
    ('pipeline/text.py', 'continue  # "PHYS 2010/2011"', 'pass  # "PHYS 2010/2011"'),
    ('pipeline/crawl.py', 'return self.challenges.get(host, 0) >= self.CHALLENGE_STOP', 'return False'),
    ('pipeline/extractors/programmap.py', 'if len(labels) != 1: return []', "labels = labels or {'2026-27': 1}"),
    ('pipeline/extractors/programmap.py', 'cont = last and (last[1] is None or wrapped or', 'cont = last and (last[1] is None or'),
    ('pipeline/extractors/merit.py', "rec_year, rec_basis = T.academic_year(first), 'labeled_entering_class'", "rec_year, rec_basis = T.academic_year(first), 'labeled_in_source'"),
    ('pipeline/extractors/costs.py', 'return []  # budgets for less-than-full-time enrollment', 'pass  # budgets for less-than-full-time enrollment'),
    ('pipeline/extractors/merit.py', 'criteria = next((i for i, h in enumerate(header) if i != renewal and', 'criteria = next((i for i, h in enumerate(header) if'),
    ('pipeline/extractors/transfer.py', 'return []  # hour counts there are award or reverse-transfer conditions', 'pass  # hour counts there are award or reverse-transfer conditions'),
    ('pipeline/extractors/merit.py', "(x if not (PLACEHOLDER.match(x) or PHONE.search(x) or '@' in x or YES_NO.fullmatch(x)) else ''", "(x if not (PLACEHOLDER.match(x) or '@' in x or YES_NO.fullmatch(x)) else ''"),
    ('pipeline/extractors/merit.py', ' or bool(ENROLLMENT.match(nm))', ''),
    ('pipeline/extractors/merit.py', 'elif tier_row and ENROLLMENT.match(nm):', 'elif False:'),
    ('pipeline/extractors/merit.py', "if i == gpa_col and re.search(r'\\d\\.\\d', header[i]) and re.search(r'\\b(act|sat)\\b', v, re.I):", 'if False:'),
    ('pipeline/extractors/merit.py', "f'{name} {v}' if v and SCORE.search(v) and not re.search(r'\\b(act|sat)\\b', v, re.I) else v", "f'{name} {v}' if v else v"),
    ('pipeline/extractors/merit.py', '|\\bno\\s+test|test[\\s-]*optional|without\\s+(a\\s+)?test', ''),
    ('pipeline/extractors/costs.py', "(None if re.search(r'on[- ]campus\\s*/\\s*off[- ]campus|on\\s*(/|and|&|or)\\s*off[- ]campus|on[- ]\\s*(and|&|or)\\s*off[- ]campus', h) else", '(None if False else'),
    ('pipeline/extractors/merit.py', 'lo, hi = None, None  # LSUS', 'pass  # LSUS'),
    ('pipeline/extractors/merit.py', "rec['renewable'] = False  # UL Lafayette", 'pass  # UL Lafayette'),
    ('pipeline/extractors/transfer.py', "r'(?<!non-)(?<!non)developmental|(?:for|exempt\\s+the)\\s+placement|placement\\s+(?:assessment|test|exam)|math(?:ematics)?\\s+and\\s+science|block\\s+transfer|'", "r'^$|'"),
    ('pipeline/extractors/transfer.py', "[] if re.search(r'upper[- ](?:level|division)|not\\s+accredited|unaccredited|toward\\s+the\\s+major|honors|required\\s+to\\s+accept|engineering\\s+programs|option\\s+[a-z]\\b|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)|most", "[] if re.search(r'toward\\s+the\\s+major|honors|required\\s+to\\s+accept|engineering\\s+programs|option\\s+[a-z]\\b|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)|most"),
    ('pipeline/extractors/credit.py', "            issues = issues + ['merged_score_cells']\n", '            pass\n'),
    ('pipeline/extractors/credit.py', "issues = issues + ['score_scale_mismatch']", 'pass'),
    ('pipeline/extractors/credit.py', "            score = f'{level} {score}'", '            pass'),
    ('pipeline/extractors/costs.py', '        return []\n    page_year, page_basis, page_issues', '        pass\n    page_year, page_basis, page_issues'),
    ('pipeline/extractors/merit.py', "r'^(reading|english|math(ematics)?|science|writing|composite)$|'", "r''"),
    ('pipeline/extractors/merit.py', 'if name > 0 and len(row) < len(header): continue', 'pass'),
    ('pipeline/extractors/merit.py', "rec['_issues'] = ['threshold_logic_column']", 'pass'),
    ('pipeline/extractors/transfer.py', "r'this\\s+course|prerequisite|'", "r'^$|'"),
    ('pipeline/extractors/merit.py', "MULTI_YEAR.search(re.sub(r'\\([^)]*\\)', '', amt)) or ", ''),
    ('pipeline/extractors/merit.py', ' or MULTI_X.search(amt)', ''),
    ('pipeline/extractors/merit.py', "r'\\bfull\\s+tuition\\b|", "r'"),
    ('pipeline/extractors/merit.py', '^(gpa|act|sat|clt|psat|scores?|tiers?|level|amount)$|', ''),
    ('pipeline/extractors/transfer.py', "r'average\\s+grade|general\\s+education|'", "r'^$|'"),
    ('pipeline/extractors/credit.py', "issues = issues + ['course_number_missing']", 'pass'),
    ('pipeline/extractors/merit.py', '|\\bper\\s+credit\\b', ''),
    ('pipeline/extractors/merit.py', "|trimesters|quarters|terms)\\b', re.I)  # outside parentheses;", "|terms)\\b', re.I)  # outside parentheses;"),
    ('pipeline/extractors/merit.py', "        vals += [float(a.replace(',', '')), float(b.replace(',', ''))]", '        pass'),
    ('pipeline/extractors/merit.py', '|\\bpell\\b|\\brotc\\b|yellow', '|\\bpell\\b|yellow'),
    ('pipeline/extractors/merit.py', " + (['duplicate_table_versions'] if twins else [])", ''),
    ('pipeline/text.py', "        if ACCREDIT_BEFORE.search((text or '')[max(0, m.start() - 60):m.start()]):\n            continue", '        if False:\n            continue'),
    ('pipeline/extractors/transfer.py', "r'a-levels?|dual\\s+credit\\s+courses|work\\s+experience|work\\s+credit|'", "r'^$|'"),
    ('pipeline/extractors/credit.py', "level = (None if both else 'HL'", "level = ('HL'"),
    ('pipeline/extractors/merit.py', '|sample[- ]aid[- ]packages?|aid[- ]package[- ]examples?|', '|'),
    ('pipeline/extractors/merit.py', "|^(annual\\s+)?totals?$', re.I)", "', re.I)"),
    ('pipeline/extractors/merit.py', "    cell = re.sub(r'\\([^)]*(?:\\bper\\s+|/\\s*|\\bfor\\s+(?:the\\s+)?(?:fall|spring)\\s+)(?:semester|term|trimester|quarter)\\b[^)]*\\)', '', cell, flags=re.I)", '    pass'),
    ('pipeline/extractors/merit.py', '|\\btotal\\s+value\\b', ''),
    ('pipeline/extractors/costs.py', "        'period': ('semester' if re.search(r'per\\s+semester|per\\s+term\\b', h) else\n                   'year'", "        'period': ('year'"),
    ('pipeline/extractors/costs.py', '        return out  # KS (Pitt State)', '        pass  # KS (Pitt State)'),
    ('pipeline/extractors/merit.py', "                rec['eligibility_summary'] = f'Listed under: {context.strip()[:200]}'", '                pass'),
    ('pipeline/extractors/merit.py', '        if sum(1 for r in body if r and PACKAGE_ROW.search(r[0])) >= 2: continue', '        pass'),
    ('pipeline/extractors/merit.py', "|'\n                       r'credits?\\s+completed', re.I)", "', re.I)"),
    ('pipeline/extractors/transfer.py', "r'grade\\s+point\\s+average\\s+of\\s+less\\s+than|when\\s+the\\s+minimum|within\\s+the\\s+last\\s+\\w+\\s+years|'", "r'^$|'"),
    ('pipeline/extractors/transfer.py', '|toward\\s+the\\s+major|honors|required\\s+to\\s+accept|engineering\\s+programs|option\\s+[a-z]\\b|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)|most', '|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)|most'),
    ('pipeline/extractors/transfer.py', "r'another\\s+(?:college|school|institution)|most\\s+(?:[\\w-]+\\s+)?(?:colleges|schools|universities|institutions)|entrance\\s+requirements?', re.I)", "r'^$', re.I)"),
    ('pipeline/extractors/transfer.py', "|toward\\s+the\\s+major|honors|required\\s+to\\s+accept|engineering\\s+programs|option\\s+[a-z]\\b|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)|most\\s+(?:[\\w-]+\\s+)?(?:colleges|schools|universities|institutions)', s, re.I)", "|toward\\s+the\\s+major|honors|required\\s+to\\s+accept|engineering\\s+programs|option\\s+[a-z]\\b|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)', s, re.I)"),
    ('pipeline/extractors/dual.py', 'for m in ([] if question or not_price else PER_HOUR.finditer(line)):', 'for m in ([] if question else PER_HOUR.finditer(line)):'),
    ('pipeline/extractors/credit.py', '            level = cells[lvl].strip().upper()  # NE (UNO)', '            pass  # NE (UNO)'),
    ('pipeline/extractors/merit.py', "|-+|—|–)\\W*$', re.I)", "|-+|—)\\W*$', re.I)"),
    ('pipeline/extractors/merit.py', '            lo, hi = None, None  # ND (Lake Region)', '            pass  # ND (Lake Region)'),
    ('pipeline/extractors/merit.py', '\\b(?:for|over|value|maximum\\s+of)\\s+', '\\b(?:for|over|value)\\s+'),
    ('pipeline/extractors/merit.py', '        amounts = []  # ND (Minot)', '        pass  # ND (Minot)'),
    ('pipeline/extractors/merit.py', '        amount = next((i for i, h in enumerate(header) if i != name and not h.strip() and body', '        amount = next((i for i, h in enumerate(header) if False and body'),
    ('pipeline/extractors/merit.py', '|undocumented|sample', '|sample'),
    ('pipeline/extractors/merit.py', '|yellow\\s+ribbon|', '|'),
    ('pipeline/extractors/merit.py', "r'(?<!renewable\\s)\\b(?:for", "r'\\b(?:for"),
    ('pipeline/extractors/credit.py', '            continue  # MT (MSU-Northern)', '            pass  # MT (MSU-Northern)'),
    ('pipeline/extractors/merit.py', "(\\s*\\([^)]*\\))?$|^\\d+(\\.\\d+)?\\s+credits?\\s+or\\s+more$', re.I)", "$', re.I)"),
    ('pipeline/extractors/merit.py', "|per\\s+semester|/\\s*semester', outside", "|per\\s+semester', outside"),
    ('pipeline/extractors/merit.py', "'offer', 'reward')", "'offer')"),
    ('pipeline/extractors/merit.py', '            continue  # ID (BYU-Idaho)', '            pass  # ID (BYU-Idaho)'),
    ('pipeline/extractors/merit.py', "            if not rec_open_max: rec['award_max'] = hi", "            rec['award_max'] = hi"),
    ('pipeline/extractors/dual.py', "|financial\\s+aid|fall\\s+below|satisfactory\\s+progress|graduation\\s+gpa|'", "|'"),
    ('pipeline/extractors/merit.py', "'award detail', 'offer', 'reward')", "'award detail', 'reward')"),
    ('pipeline/extractors/costs.py', "or column_meaning(cells[0])['period']\n", '\n'),
    ('pipeline/extractors/merit.py', '(?:\\bper\\s+|/\\s*|', '(?:\\bper\\s+|'),
    ('pipeline/extractors/dual.py', " and not re.search(r'scholarship', line, re.I):", ':'),
    ('pipeline/extractors/credit.py', " and not re.fullmatch(r'\\s*(n/?a|none)\\s*', c, re.I)]", ']'),
    ('pipeline/extractors/merit.py', '|\\bfor\\s+(?:the\\s+)?(?:fall|spring)\\s+)(?:semester', ')(?:semester'),
    ('pipeline/extractors/transfer.py', '\\b(?:ENGL?|MATH', '\\b(?:ENGL|MATH'),
    ('pipeline/extractors/transfer.py', '|depending\\s+on\\s+(?:the|your)\\s+(?:program|major)|most', '|most'),
    ('pipeline/extractors/dual.py', "|if\\s+you\\s+(?:don[’\\']?t|do\\s+not)', line, re.I)", "', line, re.I)"),
    ('pipeline/extractors/merit.py', '        if sum(1 for r in body if any(PHONE.search(c) for c in r)) >= 2: continue', '        pass'),
    ('pipeline/extractors/merit.py', "|(?:private|outside|external)[- ]scholarships?|undocumented|", "|undocumented|"),
    ('pipeline/extractors/transfer.py', '(?:english|math(?:ematics)?)\\s+course|', ''),
    ('pipeline/extractors/dual.py', "NOT_ELIGIBILITY = re.compile(r'overload|", "NOT_ELIGIBILITY = re.compile(r'"),
    ('pipeline/extractors/transfer.py', "r'(?<!non-)(?<!non)developmental|", "r'developmental|"),
    ('pipeline/extractors/costs.py', "(t.get('heading') or '') + ' ' + (t.get('lead') or '')[:120]", "(t.get('heading') or '')"),
    ('pipeline/extractors/merit.py', '        if tier_row and NOT_AWARD_NAME.search(title): continue', '        pass'),
    ('pipeline/extractors/merit.py', 'if context.strip() and not nav and not re.search', 'if context.strip() and not re.search'),
    ('pipeline/extractors/merit.py', "|\\bph\\.?\\s?d\\b|\\bdoctoral\\b|\\bmaster\\'?s\\b|", '|'),
    ('pipeline/registry.py', '    return None if label in GENERIC_LABELS else label', '    return label'),
    ('pipeline/registry.py', '        if folder != folders.get(key) and folder in owned:', '        if False:'),
    ('pipeline/extractors/costs.py', '                header = stack_header(header, sub, len(cells) - 1)', '                pass'),
    ('pipeline/extractors/costs.py', '                if header is None: header, titles = [], titles + [STACKED]', '                if header is None: header = []'),
    ('pipeline/extractors/costs.py', "    if home and re.search(rf'\\b{home}\\s+residents?\\b', h, re.I): return 'in_state'", '    pass'),
    ('pipeline/extractors/costs.py', '|without\\s+(a\\s+)?parents?|away', '|away'),
    ('pipeline/extractors/costs.py', "    ctx['period'] = ctx['period'] or next(", "    ctx['period'] = ctx['period'] or None and next("),
    ('pipeline/extractors/transfer.py', 'from\\s+this\\s+list|', ''),
    ('pipeline/extractors/transfer.py', 'does\\s+not\\s+transfer|', ''),
    ('pipeline/extractors/merit.py', '        if a and b / a in (2, 3, 4, 5): return a, a', '        pass'),
    ('pipeline/extractors/merit.py', " or '@' in x or YES_NO", ' or YES_NO'),
    ('pipeline/extractors/merit.py', " or YES_NO.fullmatch(x)) else ''", ") else ''"),
    ('pipeline/extractors/merit.py', " or re.search(r'\\$[\\d,.]+\\s+(?:for\\s+)?(?:the\\s+)?(?:fall|spring)\\b', outside, re.I))", ')'),
    ('pipeline/extractors/merit.py', "\\d{1,2}\\W*$|\\bap\\s+credit\\b|", "\\d{1,2}\\W*$|"),
    ('pipeline/extractors/costs.py', '|not\\s+living\\s+at\\s+home|', '|'),
    ('pipeline/extractors/costs.py', '|at[- ]home|', '|at home|'),
    ('pipeline/extractors/costs.py', "    if not ctx['period'] and lead_period: ctx['period'] = 'semester'", '    pass'),
    ('pipeline/extractors/costs.py', "                   if not re.search(r'(?:credits?|hours?)\\s*$', (t.get('lead') or '')[:m.start()], re.I)]", '                   if True]'),
    ('pipeline/extractors/transfer.py', '(?:semester\\s+)?(?:credit\\s+)?(?:hours\\s+)?of\\s+the', 'of\\s+the'),
    ('pipeline/extractors/transfer.py', "|(?:gpa|grade\\s+point\\s+average)(?:[^.]|\\.(?=\\d)){0,40}\\b(?:for|on|in|during)\\s+the\\s+(?:last|final)|recognition|honors', s, re.I)", "|recognition|honors', s, re.I)"),
    ('pipeline/extractors/transfer.py', "|recognition|honors', s, re.I)", "', s, re.I)"),
    ('pipeline/extractors/transfer.py', '|honors|required\\s+to\\s+accept|engineering\\s+programs|option\\s+[a-z]\\b|', '|'),
    ('pipeline/extractors/transfer.py', "r'composition|unaccredited|", "r'composition|"),
    ('pipeline/extractors/merit.py', "NOT_MERIT = re.compile(r'\\bexamples?\\b|", "NOT_MERIT = re.compile(r'"),
    ('pipeline/extractors/merit.py', "    if re.search(r'(?:^|[-–|:]\\s*)loans?\\s*$', page.title, re.I): return []", '    pass'),
    ('pipeline/extractors/costs.py', 'on[- ]campus\\s*/\\s*off[- ]campus|on\\s*(/|and', 'on\\s*(/|and'),
    ('pipeline/extractors/costs.py', '(a\\s+)?(parents?|family)|', '(a\\s+)?parents?|'),
    ('pipeline/extractors/transfer.py', 'unaccredited|high\\s+school|', 'unaccredited|'),
    ('pipeline/extractors/costs.py', "r'\\bno\\s+out[- ](?:of[- ])?state|", "r'(?!x)x|"),
    ('pipeline/extractors/costs.py', "\\bnot\\s+charge\\s+out[- ]of[- ]state|'", "'"),
    ('pipeline/extractors/costs.py', "r'\\bresidents?\\s*(?:&|and|/)\\s*non-?\\s?residents?'", "r'(?!x)x'"),
    ('pipeline/extractors/costs.py', '(?:midwest|msep|wue|reciprocity)\\W+non', '(?:zzzz)\\W+non'),
    ('pipeline/extractors/costs.py', "|\\bresidents?\\s+of\\s+other\\s+states'", "'"),
    ('pipeline/extractors/costs.py', '        semester_only = True\n', '        pass\n'),
    ('pipeline/extractors/transfer.py', '(?:some|certain|specific|health)\\s+[\\w/ -]{0,60}?programs?\\s+require|', ''),
    ('pipeline/extractors/transfer.py', 'students\\s+planning\\s+to\\s+transfer|', ''),
    ('pipeline/extractors/dual.py', 'overload|petition|', 'overload|'),
    ('pipeline/extractors/dual.py', 'course\\s+requirements\\s+for|', ''),
    ('pipeline/extractors/merit.py', '^\\W*(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\\.?\\s+\\d{1,2}\\W*$|', ''),
    ('pipeline/extractors/merit.py', "r'course[- ]awards|", "r'"),
    ('pipeline/extractors/merit.py', '|\\bclep\\b|examination', '|examination'),
    ('pipeline/extractors/merit.py', '|examination[- ]program|(?:private', '|(?:private'),
    ('pipeline/registry.py', '        if domain in PROGRAM_DEPTH_DOMAINS: continue\n', '        pass\n'),
]
TIMEOUT = 90


def run_one(root, mut):
    """Apply one mutant inside a private copy of the tree, run the suite there, restore it."""
    f, old, new = mut
    path = os.path.join(root, f)
    original = open(path).read()
    assert old in original, (f, old)
    try:
        open(path, 'w').write(original.replace(old, new, 1))
        try:
            r = subprocess.run([sys.executable, '-m', 'unittest', 'tests.test_pipeline'], cwd=root, capture_output=True, text=True, timeout=TIMEOUT)
            return 'KILLED ' if r.returncode else 'SURVIVED'
        except subprocess.TimeoutExpired:
            return 'TIMEOUT'
    finally:
        open(path, 'w').write(original)


def main():
    for f, old, _ in MUTS:  # a stale entry fails fast, before any copy or test run
        assert old in open(f).read(), (f, old)
    global TIMEOUT
    workers = max(1, int(os.environ.get('MUTATION_WORKERS') or os.cpu_count() or 1))
    # Parallel suites share the CPU, so each one runs slower; the per-mutant budget scales with the worker count.
    TIMEOUT = int(os.environ.get('MUTATION_TIMEOUT') or 90 * workers)
    tmp = tempfile.mkdtemp(prefix='mutation-')
    skip = shutil.ignore_patterns('.git', 'node_modules', '__pycache__', 'runs')
    roots = queue.Queue()
    for i in range(workers):  # one private tree per worker, so mutants never see each other's edits
        dst = os.path.join(tmp, str(i)); shutil.copytree('.', dst, ignore=skip); roots.put(dst)

    def job(mut):
        root = roots.get()
        try: return mut, run_one(root, mut)
        finally: roots.put(root)

    failed = False
    try:
        with concurrent.futures.ThreadPoolExecutor(workers) as pool:
            for (f, old, _), verdict in pool.map(job, MUTS):
                print(verdict, f, old[:60], flush=True)
                if verdict != 'KILLED ':
                    failed = True
                    # A workflow command, so the surviving mutant shows as a check annotation, not only in the raw log.
                    print(f'::error file={f}::mutant {verdict.strip()}: {old[:120]!r}', flush=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
