#!/usr/bin/env python3
"""Mutation checks for the Program & Degree Deep Dive safety rules (programs/, backend/program_fields.py).

Kept separate from scripts/mutation_check.py (the national pipeline's) so the two workstreams never edit
the same file. Each mutant breaks one rule; tests/test_programs_deep_dive.py must then fail ("KILLED").
"""
import shutil, subprocess, sys

MUTS = [
    # UVU: listed emphases, glued awards, matriculation evidence
    ('programs/extract.py', "    return any(is_option_page(c) for c in found) and (key, norm_emph(url)) not in emphases", "    return any(is_option_page(c) for c in found)"),
    ('programs/autoreview.py', "'program_name', '')) and (c['institution_key'], url_of(c, 'program_url')) not in listed_emphases else", "'program_name', '')) and True else"),
    ('programs/autoreview.py', "\n               and (c['institution_key'], url_of(c, 'program_url')) not in listed_emphases else", "\n               and True else"),
    ('programs/extract.py', " or credential_of(re.sub(r'(?<=[a-z.])(?=[A-Z][a-z])', ' ', label))", ""),
    ('programs/extract.py', "r'\\bprior\\s+to\\s+application\\b|", "r'"),
    # issue #95 recovery: printed code shapes, specific hold reasons, held rows reported not dropped
    ('programs/courseleaf.py', "CODE = r'[A-Z]{1,5}(?:/[A-Z]{1,5})*\\s?\\d{3,4}[A-Z]?'", "CODE = r'[A-Z]{1,5}\\s\\d{3,4}[A-Z]?'"),
    ('programs/courseleaf.py', "    if PAIR_CODE.search(text): return {'complex_course_row', 'lecture_lab_pair_code'}", "    pass"),
    ('programs/courseleaf.py', "            if g['type'] == 'all_required' and not g['issues']: return", "            if g['type'] == 'all_required': return"),
    ('programs/courseleaf.py', "                rule = LEAD_IN.sub('', rw['text'])", "                rule = rw['text']"),
    ('programs/courseleaf.py', "            if ALL_FOLLOWING.match(rw['text']):", "            if False:"),
    ('programs/verify.py', "    if not m: return re.search(rf'\\b{re.escape(code)}\\b', text, re.I) is not None", "    if not m: return True"),
    ('programs/verify.py', "    return re.search(rf'\\b{re.escape(subj)}\\s?{re.escape(num)}\\b', text, re.I) is not None", "    return True"),
    ('programs/courseleaf.py', "        if cur is not None and cur.get('all_following') and not cur['rules']:", "        if False:"),
    ('programs/crawl.py', "return registrable_domain(h) in set(target.get('domains', []))", 'return True'),
    ('programs/crawl.py', "keep = '&'.join(f'{k}={q[k][0]}' for k in ('catoid', 'poid', 'navoid') if k in q)", "keep = p.query"),
    ('programs/crawl.py', "rx = re.compile(r'preview_program\\.php\\?catoid=%s&poid=\\d+' % re.escape(str(cat.get('catoid'))))",
     "rx = re.compile(r'preview_program\\.php\\?catoid=\\d+&poid=\\d+')"),
    ('programs/crawl.py', "if url in seen or not in_scope(target, url): return", 'if url in seen: return'),
    ('programs/crawl.py', "seen = {e['url'] for e in run.entries() if e.get('institution_key') == key}", 'seen = set()'),
    ('programs/extract.py', "if GRAD.search(name) and not BACHELOR.search(name): return None", 'pass'),
    ('programs/extract.py', "if 25 <= len(s) <= 600: yield s", 'yield s'),
    ('backend/program_fields.py', "errs += _evidence_errors(r.get('admission_details'), 'admission_details')", 'pass'),
    ('backend/program_fields.py', "if not str(r.get('cip_source_url', '')).startswith('https://'): errs.append('cip_code needs cip_source_url (official https)')", 'pass'),
    ('backend/program_fields.py', "if missing: errs.append(", 'if False: errs.append('),
    ('backend/program_fields.py', "if not isinstance(keys, list) or len(keys) != n or len(set(keys)) != len(keys):", 'if False:'),
    ('backend/program_fields.py', "if (r.get('program_keys') or r.get('cip_codes')) and not (r.get('major_requirement') or '').strip():", 'if False:'),
    ('programs/smartcatalog.py', "if not name or not BACHELOR.search(name) or NOT_PROGRAM.search(name): return []", "if not name or not BACHELOR.search(name): return []"),
    ('programs/smartcatalog.py', "'group_type': 'all_required' if (REQUIRED.search(heading) and not CHOOSE.search(heading)) else 'elective_pool'", "'group_type': 'elective_pool' if CHOOSE.search(heading) else 'all_required'"),
    ('programs/thec.py', "        if (PROGRAMS, json.dumps(payload, sort_keys=True)) in done: continue", "        pass"),
    ('backend/program_fields.py', "        if k in cat:", "        if False:"),
    ('programs/status.py', "complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE", "complete = not pending and not errors and share >= COVERAGE_SHARE"),
    ('programs/status.py', "complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE", "complete = not unaccounted and not pending and not errors"),
    ('programs/status.py', "complete = not unaccounted and not pending and not errors and share >= COVERAGE_SHARE", "complete = not unaccounted and not errors and share >= COVERAGE_SHARE"),
    ('programs/status.py', "covered = complete or (share is not None and share >= CATALOG_SHARE)", "covered = complete or (share is not None and share > 0)"),
    ('programs/status.py', "folders = {f.parts[-3] for f in (ROOT / 'data/institutions').glob('*/program_catalogs/*.json')}", "folders = set()"),
    ('programs/status.py', "verified = [r for r in progs if r.get('verification_status') == 'verified' and r.get('credential_level') == 'bachelor']", "verified = [r for r in progs if r.get('credential_level') == 'bachelor']"),
    ('programs/status.py', "covered = [r for r in rows if r['status'] in ('covered', 'covered_open_items')]", "covered = [r for r in rows if r['status'] != 'not_started']"),
    ('programs/status.py', "four = [i for i in reg['institutions'] if i.get('level') == 'four_year']", "four = list(reg['institutions'])"),
    ('programs/status.py', "if not (e.get('next_action') or '').strip(): errs.append", "if False: errs.append"),
    ('programs/status.py', "'degree_maps': 'met' if verified and len(plans & vkeys) >= PLAN_SHARE * len(verified)", "'degree_maps': 'met' if plans"),
    ('programs/status.py', "if cur != j: print(", "if False: print("),
    ('programs/extract.py', "    if heading not in [h.strip() for h in page.headings]: return []", "    pass"),
    ('programs/extract.py', "    if printed == name or OPTION_NAME.search(printed): return []", "    pass"),
    ('programs/verify.py', "if not other or norm(r['program_name']) not in norm(other(nev['sha256'])): probs.append", "if False: probs.append"),
    ('programs/verify.py', "if ev.get('field') == 'program_page_heading' and norm(ev.get('value', '')) not in t: probs.append", "if False: probs.append"),
    ('pipeline/crawl.py', "        return 'robots_unreachable' if getattr(rp, 'unreachable', False) else 'disallowed_by_robots'", "        return 'disallowed_by_robots'"),
    ('programs/queue_suggest.py', "            if f['challenged'] and not f['program_pages'] and f['challenged'].most_common(1)[0][1] >= 3:", "            if f['challenged'] or f['robots']:"),
    ('programs/queue_suggest.py', "and f['challenged'].most_common(1)[0][1] >= 3:", ":"),
    ('programs/queue_suggest.py', "            if n and hit == 0:", "            if hit == 0:"),
    ('programs/queue_suggest.py', "        if (k, gap) in have or (k, 'institution') in have: return", "        pass"),
    ('programs/crawl.py', "if is_program(h) and (not tag or role != 'program_list' or tag in (a or ''))]", "if is_program(h)]"),
    ('programs/crawl.py', "    if target.get('crawl_delay') and chost:", "    if False:"),
    ('programs/detect.py', "        pool = [c for c, y in dated.items() if y == newest] or list(cats)", "        pool = list(cats)"),
    ('programs/detect.py', "            if cfgs[f].get('reviewed') or (len(owners) == 1 and f == owners[0]): continue", "            if cfgs[f].get('reviewed') or f in owners: continue"),
    ('programs/detect.py', "        if len(folders) < 2: continue", "        if len(folders) < 1: continue"),
    ('programs/detect.py', "        if q.stem == state or not oreg.exists(): continue", "        if q.stem == state or oreg.exists(): continue"),
    ('programs/build_targets.py', "          | set(c.get('extra_hosts',[]))),'mode'", "          ),'mode'"),
    ('programs/crawl.py', "(b[a-z]{1,5}|ab|major)([-_]|$)', seg)", "(b[a-z]{1,5}|major)([-_]|$)', seg)"),
    ('programs/extract.py', "|General\\s+|[A-Z][a-z]+\\s+Campus\\s+)?(Catalog", "|General\\s+)?(Catalog"),
    ('programs/extract.py', "        emph = [EMPHASIS_ENTRY.match(line) or OPTION_PAREN_ENTRY.match(line) or WITH_EMPHASIS_ENTRY.match(line)\n", "        emph = [EMPHASIS_ENTRY.match(line) or OPTION_PAREN_ENTRY.match(line) or None\n"),
    ('programs/extract.py', "            if key in degrees or key in (offered or {}).get(ik, set()): continue", "            pass"),
    ('programs/crawl.py', " or SKIP_PATH.search(p.path) or excluded(target, u): return False", " or SKIP_PATH.search(p.path): return False"),
    ('programs/extract.py', "BACHELOR = re.compile(r'(?<![A-Za-z]\\.)\\b(B", "BACHELOR = re.compile(r'\\b(B"),
    ('programs/crawl.py', "    elif cat.get('home') and not (cat.get('platform') == 'pdf' and cat['home'] in cat.get('catalog_pdfs', [])):", "    elif cat.get('home'):"),
    ('programs/extract.py', "    path = '/'.join(seg for seg in urlsplit(href).path.split('/') if 'degree' not in seg.lower())", "    path = urlsplit(href).path"),
    ('programs/extract.py', "    named = (page.title or '').split(' | ')[0].split(' < ')[0].strip()", "    named = (page.title or '').split(' | ')[0].strip()"),
    ('programs/extract.py', "    while hs and YEAR_HEADING.match(hs[0]): hs = hs[1:]", "    pass"),
    ('programs/extract.py', "    if credential_of(name) != 'bachelor' or GENERIC_DEGREES.match(name) or NOT_PROGRAM_NAME.search(name): return []", "    if credential_of(name) != 'bachelor' or NOT_PROGRAM_NAME.search(name): return []"),
    ('programs/detect.py', "                if ys: pdfs.append((max(ys), href, m))", "                pdfs.append((max(ys or {0}), href, m))"),
    ('programs/detect.py', "            elif u.path.lower().endswith('.pdf') and CATALOG_WORD.search(a + ' ' + u.path) and not re.search(r'graduate|archive|handbook', a + u.path, re.I):", "            elif u.path.lower().endswith('.pdf') and CATALOG_WORD.search(a + ' ' + u.path):"),
    ('programs/crawl.py', "            **({'degree_map': 0, 'degree_map_index': 0, 'policy_link': 0} if target.get('mode') == 'discover' else {}),", "            **({}),"),
    ('programs/autoreview.py', "               'combined_program' if COMBINED.search(c['record'].get('program_name', '')) else", ""),
    ('programs/autoreview.py', "               'option_name' if OPTION.search(c['record'].get('program_name', '')) and (c['institution_key'], url_of(c, 'program_url')) not in listed_emphases else", ""),
    ('programs/autoreview.py', "'not_verbatim' if verify.get(c['candidate_id']) else 'not_bachelor'", "'not_bachelor'"),
    ('programs/autoreview.py', "               'program_not_approved' if c['record'].get('program_key') not in program_keys[c['institution_key']] else None)", "               None)"),
    ('programs/autoreview.py', "        why = ('untrusted_extractor' if (kind, c['extractor']) not in TRUSTED_REQUIREMENTS else", "        why = ('untrusted_extractor' if False else"),
    ('programs/crawl.py', "            if re.search(r'(^|[-_])(minor|certificate|cert|ms|ma|mba|mfa|med|phd|edd|dnp|pmc|aas|as|aa)([-_]|$)', seg): continue", "            pass"),
    ('programs/crawl.py', "            if not is_program(h) or re.search(r'(^|/)(grad|graduate|graduate-school)(/|$)', urlsplit(h).path.lower()): continue", "            pass"),
    ('programs/extract.py', "    hit = next((n for n in names if n and norm(re.sub(r'(\\s*\\([^()]{1,12}\\))+\\s*$', '', n)) == norm(base)), None)", "    hit = next((n for n in names if n and norm(n).startswith(norm(base))), None)"),
    ('programs/autoreview.py', "               'entry_path_variant' if len(variants[(c['institution_key'], base(c))]) > 1 and plain(c) != c['record'].get('program_name', '').strip()\n               and (c['institution_key'], url_of(c, 'program_url')) not in listed_emphases else\n", ""),
    ('programs/autoreview.py', " and plain(c) != c['record'].get('program_name', '').strip()\n", "\n"),
    ('programs/extract.py', "    if not base or base == unqualified or OPTION_NAME.search(printed): return []", "    pass"),
    ('programs/status.py', "    counted = min(len(verified), max(matched)) if matched else len(verified)", "    counted = len(verified)"),
    ('programs/autoreview.py', "               'graduate_name' if GRADUATE.search(c['record'].get('program_name', '')) else", ""),
    ('backend/program_fields.py', "            errs.append('verified_listed_programs must be an integer between 0 and listed_bachelor_programs')", "            pass"),
    ('programs/promote.py', "        return 0  # a mechanical count never replaces a reviewed one", "        pass"),
    ('programs/promote.py', "    clash = {k: f for k, f in folders.items() if owners.get(f, {k}) - {k} and holder(f) != k}", "    clash = {}"),
    ('programs/status.py', "    reviewed = [c for c in cats if 'Standing review' not in (c.get('notes') or '')]", "    reviewed = cats"),
    # one program name on several pages: only the base page's record and requirement rows
    ('programs/autoreview.py', "               'variant_page' if url_of(c, 'program_url') in variant_pages else", ""),
    ('programs/autoreview.py', "               'variant_page' if url_of(c, 'source_url') in variant_pages else", ""),
    ('programs/autoreview.py', "    base = [b for b in stems if all(o == b or o.startswith((b + '-', b + '_')) for o in stems)]", "    base = sorted(stems)[:1]"),
    ('programs/autoreview.py', "    url = re.sub(r'/general-[A-Za-z0-9]+$', '', url)", "    pass"),
    # Stetson: a not-yet-posted catalog PDF slot is not the page's label; a four-digit 'Edition' label is read
    ('programs/extract.py', "        if any(re.match(r'\\s*coming soon\\b', l, re.I) for l in lines[i + 1:i + 3] if l.strip()): continue", "        pass"),
    ('programs/extract.py', "EDITION = re.compile(r'(20\\d{2})\\s*[-–]\\s*(?:20)?(\\d{2})\\s+Edition', re.I)", "EDITION = re.compile(r'(20\\d{2})\\s*[-–]\\s*(\\d{2})\\s+Edition', re.I)"),
    # CourseLeaf retrieval: a one-word sitemap segment is a course subject, not an award; course catalogs are skipped;
    # catalogs without a sitemap walk their undergraduate section
    ('programs/crawl.py', "            if not re.search(r'[-_]', seg): continue", "            pass"),
    ('programs/crawl.py', "|coursesofinstruction|courses-of-instruction|", "|"),
    ('programs/crawl.py', "                if is_program(h) and re.search(cat['sitemap_program'], h): push(h, 'program_page', url, depth + 1)", "                if is_program(h): push(h, 'program_page', url, depth + 1)"),
    ('programs/crawl.py', "    if cat.get('platform') == 'courseleaf' and cat.get('nav_prefix'):", "    if False:"),
    # department_section/v1: degree sections on department pages
    ('programs/extract.py', "        if not m or SECTION_NOT_PROGRAM.search(h) or GRAD.search(m.group('name')): continue", "        if not m: continue"),
    ('programs/extract.py', "    if len(labels) != 1: return []\n    year = next(iter(labels)); acad = academic_year_of(year)\n    yline", "    year = max(labels); acad = academic_year_of(year)\n    yline"),
    ('programs/extract.py', "                                 r'plan|semester|map|sample|suggested|'", "                                 r''"),
    ('programs/autoreview.py', "(u in seen_url and c['extractor'] not in SHARED_PAGE)", "(u in seen_url)"),
    ('programs/autoreview.py', "(u in seen_url and c['extractor'] not in SHARED_PAGE)", "(False)"),
    ('programs/promote.py', "and c['record']['program_key'] not in on_file_keys\n                        and c['extractor'] != 'department_section/v1')", ")"),
    # NDSU 'Degree Type: B.S.': one stated type only; post-baccalaureate paths are not programs
    ('programs/extract.py', "    if not m and len(types) == 1:", "    if not m and types:"),
    ('programs/extract.py', "|post[- ]?baccalaureate|second degree', name, re.I)", "', name, re.I)"),
    ('programs/extract.py', "                if int(m.group(2)) == (int(m.group(1)) + k) % 100: got.add((f'{m.group(1)}-{int(m.group(1)) + k}', line.strip()))\n        # UW-Madison", "                pass\n        # UW-Madison"),
    ('programs/extract.py', "        if re.search(r'\\bdual major\\b', name, re.I) or (':' in name and re.search(r'\\bemphas[ie]s\\b', page.text, re.I)): out = []", "        pass"),
    # UF degree_line/v1: specialization pages under a major's code; underscore slugs in the base-page rule
    ('programs/extract.py', "    if len(parts) >= 2 and re.fullmatch(r'[A-Z]{2,4}_[A-Z]{2,6}', parts[-2]): return []", "    pass"),
    ('programs/extract.py', "    if len(awards) != 1 or len({y for y, _ in labels}) != 1: return []", "    if not awards or len({y for y, _ in labels}) != 1: return []"),
    ('programs/autoreview.py', "o.startswith((b + '-', b + '_'))", "o.startswith(b + '-')"),
    # UF Geography specializations are not degrees; FAU's Coursedog rows print their long name
    ('programs/extract.py', "        if m.group('name').strip(' ,').lower() in specs or SECTION_PART.search(h) or", "        if SECTION_PART.search(h) or"),
    ('programs/extract.py', "or (r.get('longName') or '').strip() or name", "or name"),
    ('programs/extract.py', "(?:Download\\s+)?(?:an?\\s+)?PDF of", "(?:Download\\s+)?PDF of"),
    # TAMUSA credits overview is not the first table; term headings are never overviews; named elective lists count
    ('programs/courseleaf.py', "        idx += 0 if idx < 0 and overview(t) else 1", "        idx += 1"),
    ('programs/courseleaf.py', "            return False  # Iowa State Accelerated Nursing", "            pass  # Iowa State Accelerated Nursing"),
    ('programs/courseleaf.py', "                crd = CREDITS.match(rule); cnt = COUNT.match(rule) or (None if crd else COUNT_NAMED.match(rule))", "                crd = CREDITS.match(rule); cnt = COUNT.match(rule)"),
    ('programs/courseleaf.py', " or re.search(r'\\b(probation|withdrawal)\\b', heading, re.I) else heading", " else heading"),
    ('programs/courseleaf.py', "            if not sub: parent = rw['text']", "            pass"),
    ('programs/courseleaf.py', "        if HEADER_CHOICE.search(parent if parent != section else '') or HEADER_CHOICE.search(section or ''):", "        if HEADER_CHOICE.search(section or ''):"),
    ('programs/courseleaf.py', "        if HEADER_CHOICE.search(parent if parent != section else '') or HEADER_CHOICE.search(section or ''):", "        if HEADER_CHOICE.search(parent if parent != section else ''):"),
    ('programs/courseleaf.py', "HEADER_CHOICE = re.compile(r'(\\(|[-–:]\\s*)(choose", "HEADER_CHOICE = re.compile(r'([-–:]\\s*)(choose"),
    ('programs/courseleaf.py', "HEADER_CHOICE = re.compile(r'(\\(|[-–:]\\s*)(choose", "HEADER_CHOICE = re.compile(r'(\\()(choose"),
    ('programs/courseleaf.py', "(choose|select|complete|take)\\s+(one|two|three|four|five|six|\\d+)\\b', re.I)", "(choose|select|complete|take)\\s+(\\w+)\\b', re.I)"),
    # issue #129: trailing superscripts are footnote markers; a re-fetch run fetches only its pages
    ('programs/courseleaf.py', "    if not tail or not text.endswith(tail) or not text[:-len(tail)].strip(): return text", "    if not tail: return text"),
    ('programs/courseleaf.py', "title = strip_marks((cells[1].get('text') or '').strip(), cells[1].get('sup_tail'))", "title = (cells[1].get('text') or '').strip()"),
    ('programs/courselist_html.py', "            elif self._td.get('_tail') is not None and not re.fullmatch", "            elif False and self._td.get('_tail') is not None and not re.fullmatch"),
    ('programs/courselist_html.py', "                if self._td.get('_tail') is None: self._td['_tail'] = len(''.join(self._td['text']))", "                self._td['_tail'] = len(''.join(self._td['text']))"),
    ('programs/crawl.py', "    if not target.get('refetch'):\n        if cat.get('platform')", "    if True:\n        if cat.get('platform')"),
    # a title ending in a number from a layout without superscript capture is held (issue #129)
    ('programs/courseleaf.py', "        if not table.get('sups_recorded') and any(FOOTNOTED.search(", "        if False and any(FOOTNOTED.search("),
    ('programs/courselist_html.py', "'caption': '', 'rows': [], 'sups_recorded': True}", "'caption': '', 'rows': []}"),
    # department_section/v1 scope (independent review 2026-10-07)
    ('programs/extract.py', "    if sample_plan_page(page): return []", "    pass"),
    ('programs/extract.py', "        if m.group('name').strip(' ,').lower() in specs or SECTION_PART.search(h) or", "        if m.group('name').strip(' ,').lower() in specs or"),
    ('programs/extract.py', "        if nm and any(u != here and _names_degree(a, nm, award) for u, a in others): continue", "        if nm and any(_names_degree(a, nm, award) for u, a in others): continue"),
    ('programs/extract.py', "    return re.fullmatch(r'(?:' + SECTION_AWARD[award] + r')', rest.strip(), re.I) is not None", "    return credential_of(rest) == 'bachelor'"),
    ('programs/extract.py', "    if anchor.startswith(name + ' '): rest = anchor[len(name):]", "    if name in anchor: rest = anchor.replace(name, '')"),
    # listed concentration lines (NC State 'X (BS): Y Concentration', Bryant 'Bachelor of Science in X: Y Concentration')
    ('programs/extract.py', "                or AWARD_PAREN_OPTION_ENTRY.match(line) or BACHELOR_OF_OPTION_ENTRY.match(line) or PAREN_VARIANT_ENTRY.match(line)", "                or BACHELOR_OF_OPTION_ENTRY.match(line) or PAREN_VARIANT_ENTRY.match(line)"),
    ('programs/extract.py', "                or AWARD_PAREN_OPTION_ENTRY.match(line) or BACHELOR_OF_OPTION_ENTRY.match(line) or PAREN_VARIANT_ENTRY.match(line)", "                or AWARD_PAREN_OPTION_ENTRY.match(line) or PAREN_VARIANT_ENTRY.match(line)"),
    ('programs/extract.py', "            if key in degrees or key in (offered or {}).get(ik, set()): continue", "            if key in degrees: continue"),
    ('programs/extract.py', "|(?-i:[AB][A-Z]{1,4}))\\)', line)", ")\\)', line)"),
    ('programs/extract.py', "    k = re.sub(r'[\\s.]', '', a).lower()", "    k = a.replace(' ', '').rstrip('.').lower()"),
    # KU sample-plan sub-pages give no program record (any reader); PVAMU awards
    ('programs/extract.py', "        found = [c for c in found if c['domain'] != 'academic_programs']", "        pass"),
    ('programs/extract.py', "|S\\.?Ed|Ed|I\\.?S|SCJ|SAG|SCHE|SDIET)\\b", "|S\\.?Ed|I\\.?S|SCJ|SAG|SCHE)\\b"),
    # JHU degree pages
    ('programs/autoreview.py', "        canon = degree_page(us) if base is None else None", "        canon = None"),
    ('programs/autoreview.py', "        canon = degree_page(us) if base is None else None", "        canon = degree_page(us)"),
    ('programs/autoreview.py', "    return out[0] if len(out) == 1 else None", "    return out[0] if out else None"),
    ('programs/autoreview.py', "|bachelors?-degrees?|b-?a|b-?s|bfa|bm)$", "|bachelors?-degrees?)$"),
    # parenthetical variant lines (UT Arlington 'Data Science BS (Biology)', TAMUK 'Kinesiology, B.S. (Sport Business)')
    ('programs/extract.py', "                or AWARD_PAREN_OPTION_ENTRY.match(line) or BACHELOR_OF_OPTION_ENTRY.match(line) or PAREN_VARIANT_ENTRY.match(line)", "                or AWARD_PAREN_OPTION_ENTRY.match(line) or BACHELOR_OF_OPTION_ENTRY.match(line)"),
    ('programs/extract.py', "    return LONG_AWARD.get(k, k)", "    return k"),
    ('programs/extract.py', "    m = re.match(r'^(?P<base>[^,():]+?)\\s+(?P<award>(?-i:B[A-Z]{1,4}))\\s*$', line)", "    m = None"),
    ('programs/extract.py', ",?\\s+(?P<award>(?-i:B[A-Z]{1,4}|B\\.\\s?[A-Z]", ",?\\s+(?P<award>(?i:B[A-Z]{1,4}|B\\.\\s?[A-Z]"),
    # a degree page's own plan heading is not a sample-plan page (Colorado, Maryland, Missouri, Tennessee, KU engineering)
    ('programs/extract.py', "|the recommended (?:4|four)[- ]year plan is listed below)\\b')", ")\\b')"),
    ('programs/extract.py', "SAMPLE_PLAN_LINE = re.compile(r'(?im)^\\s*(?:below is a sample (?:4|four)[- ]year plan for|the recommended (?:4|four)[- ]year plan is listed below)\\b')",
     "SAMPLE_PLAN_LINE = re.compile(r'(?im)^\\s*(below is a |the )?(sample|recommended) (4|four)[- ]year plan\\b')"),
    ('programs/extract.py', "        if head in before[-2:]: return True", "        return True"),
    ('programs/extract.py', "        if head in before[-2:]: return True", "        if head in before[-1:]: return True"),
    ('programs/extract.py', "    head = (program_heading(page) or '').strip()\n    for m in SAMPLE_PLAN_LINE", "    head = next(iter(page.headings or []), '').strip()\n    for m in SAMPLE_PLAN_LINE"),
    # UAF roadmap grids (courseleaf_plangrid/v1)
    ('programs/courseleaf.py', "                if st['open'] is None: issues.add('indented_row_without_rule'); st['term']['items'].append(item)", "                if st['open'] is None: st['term']['items'].append(item)"),
    ('programs/courseleaf.py', "            st['open'] = item if GRID_CHOICE.match(text) else None", "            st['open'] = item if GRID_CHOICE.match(text) else st['open']"),
    ('programs/courseleaf.py', "                if c['text']: issues.add('grid_cell_without_column')", "                pass"),
    ('programs/courseleaf.py', "                if any(n not in footnote_defs for n in marks): issues.add('footnote_not_defined')", "                pass"),
    ('programs/courseleaf.py', "            m = cols[0]; slots.setdefault((m.group(1), m.group(2)), {})[m.group(3)] = c", "            m = cols[0]; slots.setdefault(('year0', 'Term0'), {})[m.group(3)] = c"),
    ('programs/courseleaf.py', "            if GRID_CHOICE.match(it.get('text', '')) and not it.get('options'): issues.add('rule_without_options')", "            pass"),
    ('programs/courseleaf.py', "            marks = [n for x in sups for n in re.split(r'\\s*,\\s*', x) if n]", "            marks = sups"),
    ('programs/verify.py', "                    if not any(x.startswith(printed) and re.sub(r'[\\s,]', '', x[len(printed):]) == re.sub(r'[\\s,]', '', marks) for x in cells):",
     "                    if not any(x.startswith(printed) for x in cells):"),
    ('programs/courselist_html.py', "            if self.table_class != 'sc_courselist':", "            if True:"),
    ('programs/courseleaf.py', "    labelled = len(grids_) > 1 and len(set(heads)) == len(heads) and all(h and h.lower() != 'roadmaps' for h in heads)",
     "    labelled = len(grids_) > 1 and all(h for h in heads)"),
    ('programs/courseleaf.py', "                if any(x.get('text') for x in s.values()): issues.add('grid_cell_without_term')", "                pass"),
    ('programs/autoreview.py', " and not PAREN_VARIANT_ENTRY.match(n) and not PAREN_AWARD_VARIANT_ENTRY", " and not PAREN_AWARD_VARIANT_ENTRY"),
    # Texas A&M 'X - BS, Y Track' list lines; track pages passed to the listed rule
    ('programs/extract.py', "\n                or AWARD_DASH_OPTION_ENTRY.match(line)", ""),
    ('programs/extract.py', "(p.get('printed') or '').replace('\\u200b', '')", "(p.get('printed') or '')"),
    ('programs/extract.py', "    if credential_of(name) != 'bachelor' or GENERIC_DEGREES.match(name) or NOT_PROGRAM_NAME.search(name): return []", "    if credential_of(name) != 'bachelor' or OPTION_NAME.search(name) or GENERIC_DEGREES.match(name) or NOT_PROGRAM_NAME.search(name): return []"),
    # shared reader requests #153: section titles, roadmaps, offices; UC Davis college run-on; Coursedog card descriptions
    ('programs/extract.py', " or GENERIC_DEGREES.match(name) or NOT_PROGRAM_NAME.search(name): return []", " or GENERIC_DEGREES.match(name): return []"),
    ('programs/extract.py', " or SECTION_PART.search(h) or NOT_PROGRAM_NAME.search(re.sub(", " or SECTION_PART.search(h) or (re.sub("),
    ('programs/extract.py', "NOT_PROGRAM_NAME.search(re.sub(r'^\\s*requirements\\s+for\\s+(the\\s+)?', '', h, flags=re.I))", "NOT_PROGRAM_NAME.search(h)"),
    ('programs/extract.py', "|roadmaps?|archive)\\b\"", ")\\b\""),
    ('programs/extract.py', "(?:['’]?s)?", "(?:'?s)?"),
    ('programs/extract.py', "            if re.match(r'\\s+(college|school|graduate\\s+school|division|department|faculty)\\s+of\\b', rest, re.I): return tail", "            if rest: return tail"),
    ('programs/extract.py', "    return name[:m.start()].strip() if m and m.start() >= 3 else name", "    return name"),
    ('programs/extract.py', "(?=[A-Z][a-z]+\\s+(?:\\S+\\s+){4,}\\S)')", "(?=[A-Z][a-z]+)')"),
    # UMD degree level from the MHEC Academic Program Inventory (award never inferred)
    ('programs/extract.py', "    if len(hits) != 1: return []", "    if not hits: return []"),
    ('programs/extract.py', "    hits = [r for r in inv['rows'] if r[2] == \"Bachelor's Degree\" and", "    hits = [r for r in inv['rows'] if"),
    ('programs/extract.py', "(len(r[1]) >= 38 and want.startswith(_inv_norm(r[1])) and len(_inv_norm(r[1])) >= 30)", "False"),
    ('programs/extract.py', "{}, [] if (awards or doc) else ['award_not_printed'])]", "{}, [])]"),
    ('programs/verify.py', "                if not other or norm(ev.get('snippet', '')) not in norm(other(ev['sha256'])): probs.append('credential level row not in its inventory document')", "                pass"),
    ('programs/extract.py', "                if mm and not _inv_norm(mm.group('prog')).startswith(key): continue  # 'in <another program>'", "                pass"),
    ('programs/extract.py', "            if key not in _inv_norm(sent) and not AWARD_LEAD.search(sent): continue", "            pass"),
    ('programs/extract.py', "                if re.match(r'\\s+degree\\s+requirements\\b', tail, re.I): continue", "                pass"),
    ('programs/extract.py', "        if len(line.strip()) < 60: continue", "        pass"),
    ('programs/verify.py', "                if norm(ev.get('snippet', '')) not in src: probs.append('award sentence not verbatim')", "                pass"),
    ('programs/extract.py', "                if m.group('bare') and not mm: continue  # a bare 'BA' counts only as 'BA in <this major>'", "                pass"),
    ('programs/extract.py', "AWARD_LEAD = re.compile(r'^the\\s+(?:B\\.\\s?[A-Z]\\.|Bachelor\\s+of\\s+\\w+)\\s+degree\\b|", "AWARD_LEAD = re.compile(r'"),
    # multi-year catalog periods (Cal Poly '2026-2028', owner decision 2026-10-07)
    ('programs/years.py', "PERIOD_SPANS = (1, 2)", "PERIOD_SPANS = (1,)"),
    ('programs/years.py', "    start = cur if y1 <= cur < y2 else y1", "    start = y1"),
    ('programs/years.py', "    if y2 - y1 <= 1: return f'{y1}-{str(y1 + 1)[2:]}'", "    return f'{y1}-{str(y1 + 1)[2:]}'"),
    ('scripts/validate_data.py', "        if not (1<=y2-y1<=2 and y1<=a<y2 and m.group(2)[-2:]==str(a+1)[-2:]):", "        if not (y1<=a<y2):"),
    ('programs/extract.py', " or not any(int(y[:4]) <= int(x[:4]) < int(y[5:9]) for x in single)}", "}"),
    # Cal Poly 2026-2028: department pages yield to the program page beneath them; general-requirements policy pages
    ('programs/autoreview.py', "               'department_page' if (c['institution_key'], url_of(c, 'program_url')) in department_pages else\n", ""),
    ('programs/autoreview.py', "               'department_page' if (c['institution_key'], url_of(c, 'source_url')) in department_pages else\n", ""),
    ('programs/autoreview.py', "and url_of(c, 'program_url') + '/' + slug(c['record'].get('program_name', '')) in pages[", "and any(v.startswith(url_of(c, 'program_url') + '/') for v in pages["),
    ('programs/autoreview.py', "variant_pages_of([{u for u in us if (k[0], u) not in department_pages} for k, us in pages.items()])", "variant_pages_of(pages.values())"),
    ('programs/extract.py', "^\\s*(general\\s+)?requirements\\s+(for\\s+(a|the|all)\\b|[-\\u2013\\u2014])", "^\\s*requirements\\s+for\\s+(a|the)\\b"),
    # one candidate per id: pages read twice, colliding ids held, plan keys distinct beyond 80 characters
    ('programs/extract.py', "    cands = distinct_candidates(cands)\n", ""),
    ('programs/extract.py', "        if fetch(first) == fetch(c): continue\n", ""),
    ('programs/extract.py', "            if 'candidate_id_collision' not in x['issues']: x['issues'] = x['issues'] + ['candidate_id_collision']", "            pass"),
    ('programs/courseleaf.py', "if k in keys[i + 1:] else k", "if False else k"),
    ('programs/courseleaf.py', "    plan_keys = labelled_keys(headings, slug) if labelled else []", "    plan_keys = [slug(h) for h in headings] if labelled else []"),
    # Cal Poly 2026-2028 campus variants listed without a base line
    ('programs/extract.py', " or PAREN_AWARD_VARIANT_ENTRY.match(line)\n                for line in printed]", "\n                for line in printed]"),
    ('programs/autoreview.py', " and not PAREN_AWARD_VARIANT_ENTRY.match(n) and _degree_key(n)", " and _degree_key(n)"),
    # promote never replaces an owner-corrected record or re-promotes a candidate over the record it produced
    ('programs/promote.py', "    if on_file.get('verification_correction_reason') or nk in corrected_keys(): return 'owner-approved correction on file'", "    pass"),
    ('programs/promote.py', "    if c['candidate_id'] in promoted_ids and not (approval or {}).get('replaces_promoted'): return 'already promoted from this run'", "    pass"),
    ('programs/promote.py', " and not (approval or {}).get('replaces_promoted'): return", ": return"),
    ('programs/promote.py', "        if held:\n", "        if False:\n"),
    # UW-Madison 2026-27 header: 'Guide' / '2026-2027' on two lines
    ('programs/extract.py', "        if m and HEADER_NAME.fullmatch(prev) and int(m.group(2)) - int(m.group(1)) in PERIOD_SPANS:", "        if m and int(m.group(2)) - int(m.group(1)) in PERIOD_SPANS:"),
    ('programs/extract.py', "HEADER_NAME = re.compile(r'(?:Guide|Catalog|Catalogue|Bulletin)', re.I)", "HEADER_NAME = re.compile(r'.*', re.I)"),
    # 2026-10-08 reader fixes: print-menu catalog PDFs (UNO), B.M.A. is not M.A. (Missouri Western), awards from official
    # school/department pages (UMD), college-qualified list lines (Iowa State)
    ('programs/extract.py', "        (menu_found if any(ARCHIVE_LINK.match(l) for l in lines[i + 1:i + 2]) else found).update(got)", "        found.update(got)"),
    ('programs/extract.py', "    if not found: found = menu_found\n", "\n"),
    ('programs/autoreview.py', "(?<!B\\.)\\bM\\.\\s?(A|S|Ed|F\\.?A)\\.", "\\bM\\.\\s?(A|S|Ed|F\\.?A)\\."),
    ('programs/extract.py', "            if len(kinds) == 1:\n                k = kinds.pop()", "            if kinds:\n                k = kinds.pop()"),
    ('programs/extract.py', "            if len(kinds) == 1:\n                k = next(iter(kinds))", "            if kinds:\n                k = next(iter(kinds))"),
    ('programs/extract.py', "        if name.strip() not in d.get('majors', []): continue", "        pass"),
    ('programs/extract.py', "(?![A-Za-z])(?!\\s+[A-Z][a-z])')", "')"),
    ('programs/extract.py', "    doc = None if awards else document_award(head, award_docs)", "    doc = None"),
    ('programs/verify.py', "src = norm(other(ev['sha256'])) if (ev.get('sha256') and ev['sha256'] != c['source'].get('sha256') and other and other(ev['sha256'])) else t", "src = t + ' ' + ' '.join(norm(other(x)) for x in [ev.get('sha256')] if x and other and other(x)) if False else t"),
    ('programs/extract.py', "    unqualified = COLLEGE_QUALIFIER.sub('', printed)", "    unqualified = printed"),
]


def main():
    survived = []
    for path, old, new in MUTS:
        src = open(path, encoding='utf-8').read()
        if src.count(old) != 1:
            print(f'STALE mutant (pattern not found once) in {path}: {old[:70]}'); survived.append(path); continue
        shutil.copy(path, path + '.bak')
        try:
            open(path, 'w', encoding='utf-8').write(src.replace(old, new))
            # no bytecode: a restored source can share the mutant's mtime and size, and a stale .pyc would then run the mutant
            r = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'tests.test_programs_deep_dive'], capture_output=True)
            status = 'KILLED' if r.returncode else 'SURVIVED'
            print(f'{status}: {path}: {old[:70]}')
            if r.returncode == 0: survived.append(path)
        finally:
            shutil.move(path + '.bak', path)
    print(f'{len(MUTS) - len(survived)}/{len(MUTS)} mutants killed')
    return 1 if survived else 0


if __name__ == '__main__':
    raise SystemExit(main())
