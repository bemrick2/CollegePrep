#!/usr/bin/env python3
"""Build the complete Claude question-bank export (prep-and-price-claude-complete-export.zip).

Reads only the repository files of this workstream (banks/, drafts/, reviews/, checks/, calibration/, audits/,
exports/import/) and never modifies them. Writes exports/complete/ and the zip next to it.

Usage: python3 -I tools/export_complete.py <validator-output-file>
"""
import datetime as dt
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
OUT = ROOT / 'exports' / 'complete'
ZIP = ROOT / 'exports' / 'prep-and-price-claude-complete-export.zip'
BANKS = ['act_math', 'act_english', 'act_reading', 'sat_reading_writing', 'sat_math']
PREFIX = {'act_math': 'B', 'act_english': 'E', 'act_reading': 'R', 'sat_reading_writing': 'S', 'sat_math': 'Q'}
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def git(*args):
    return subprocess.run(['git', '-C', str(REPO), *args], capture_output=True, text=True).stdout.strip()


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


retired = load(ROOT / 'audits' / 'retired.json')['retired']
pending = load(ROOT / 'audits' / 'pending_revisions.json')['items']

# ---------- read every draft, review and blind-solver file ----------
drafts, reviews, blinds = {}, {}, defaultdict(dict)
for bank in BANKS:
    for f in sorted(glob.glob(str(ROOT / 'drafts' / bank / 'batch-*.json'))):
        n = int(re.search(r'batch-(\d+)\.json', f).group(1))
        drafts[(bank, n)] = (f, load(f))
        r = ROOT / 'reviews' / bank / f'batch-{n:03d}.review.json'
        reviews[(bank, n)] = load(r) if r.exists() else None
        for bf in sorted(glob.glob(str(ROOT / 'reviews' / bank / f'batch-{n:03d}*.blind*.json'))):
            blinds[(bank, n)][os.path.relpath(bf, ROOT)] = load(bf)

raters = defaultdict(dict)
for bank in BANKS:
    for f in sorted(glob.glob(str(ROOT / 'calibration' / f'{bank}_rater_*.json'))):
        raters[bank][os.path.relpath(f, ROOT)] = load(f)['ratings']
calib = {b: load(ROOT / 'calibration' / f'{b}.json') for b in BANKS}

annotations = {}
cand_index = {}            # (bank, cand) -> (batch, draft_file, candidate dict, status)
for (bank, n), (f, d) in drafts.items():
    for c in d['candidates']:
        cand_index[(bank, c['cand'])] = (n, f, c, 'candidate')
    for w in d.get('withdrawn', []):
        if 'item' in w:
            cand_index[(bank, w['cand'])] = (n, f, w['item'], 'withdrawn')
        else:  # a later batch's note about an earlier candidate (e.g. R008-06 noted in batch 9)
            annotations[(bank, w['cand'])] = {'noted_in': os.path.relpath(f, ROOT), 'note': w['reason']}

review_result = {}
for (bank, n), r in reviews.items():
    for res in (r or {}).get('results', []):
        review_result[(bank, res['cand'])] = res

# resubmissions: candidate whose revision_note names an earlier candidate
resubmitted_as = {}
for (bank, cand), (n, f, c, kind) in cand_index.items():
    note = c.get('revision_note') or ''
    m = re.match(r'([BERSQ]\d{3}-\d{2})', note)
    if m and c.get('revision', 1) > 1:
        resubmitted_as.setdefault((bank, m.group(1)), []).append(cand)


def blind_entries(bank, n, cand):
    out = []
    for path, doc in blinds[(bank, n)].items():
        a = doc.get('answers', {}).get(cand)
        if a is None:
            continue
        rnd = re.search(r'\.(round\d)\.', path)
        out.append({'file': path, 'round': rnd.group(1) if rnd else 'final',
                    'solver': doc.get('solver', {}).get('kind'),
                    'kind': 'separate AI agent; separate context; answer-free packet (stem, choices, passage only)',
                    'answer': a.get('answer'), 'confidence': a.get('confidence'),
                    'est_pct_correct': a.get('est_pct_correct'), 'difficulty_opinion': a.get('difficulty_opinion'),
                    'flags': a.get('flags', []), 'notes': a.get('notes')})
    return out


def passage_of(bank_doc, pid):
    if not pid:
        return None
    for p in bank_doc.get('passages', []):
        if p['passage_id'] == pid:
            return p
    return None


# ---------- accepted inventory ----------
full, blind, keyrev, quarantine = [], [], [], []
passages_used = defaultdict(dict)
bank_docs = {b: load(ROOT / 'banks' / f'{b}.json') for b in BANKS}
for bank in BANKS:
    bd = bank_docs[bank]
    for q in bd['questions']:
        n = q['batch']
        cand = q['draft_candidate']
        _, draft_file, c, _ = cand_index.get((bank, cand), (n, None, {}, None))
        res = review_result.get((bank, cand), {})
        p = passage_of(bd, q.get('passage_id'))
        if q.get('passage_id') and p is None:
            print('BROKEN PASSAGE REF', q['id'])
        cal = calib[bank]['items'].get(q['id'], {})
        is_math = bank in ('act_math', 'sat_math')
        source = {'bank_file': f'banks/{bank}.json', 'batch': n, 'draft_candidate': cand,
                  'draft_file': os.path.relpath(draft_file, ROOT) if draft_file else None,
                  'review_file': f'reviews/{bank}/batch-{n:03d}.review.json',
                  'branch': 'ccr-78c91309-anlh8e', 'repository': 'bemrick2/CollegePrep',
                  'path_in_repo': 'question_bank/claude'}
        difficulty = {'author_label': q['difficulty'], 'author_numeric_1_to_5': q['difficulty_numeric'],
                      'author_basis': q['difficulty_basis'],
                      'ai_calibrated_label': cal.get('calibrated'), 'ai_ratings': cal.get('ratings'),
                      'ai_calibration_method': calib[bank]['method'],
                      'status': 'PROVISIONAL: AI and author estimates only; no student-response data exists'}
        student = {'id': q['id'], 'exam': q['exam'], 'section': q['section'],
                   'reporting_category': q['reporting_category'], 'skill': q['skill'],
                   'passage_id': q.get('passage_id'),
                   'passage': ({'title': p['title'], 'genre': p.get('genre'), 'text': p['text']} if p else None),
                   'underlined_span_number': q.get('underline'), 'figure': q.get('figure'),
                   'stem': q['stem'], 'answer_format': q.get('answer_format', 'choice'), 'choices': q['choices'], 'calculator': q['calculator'],
                   'expected_time_seconds': q['expected_time_seconds']}
        rec = dict(student)
        rec.update({'source': source, 'subskill': q['subskill'], 'repo_skill_key': q['repo_skill_key'],
                    'modeling': q['modeling'], 'correct_answer': q['correct_answer'],
                    'explanation': q['explanation'], 'distractor_explanations': q['distractor_explanations'],
                    'distractor_traps': q['distractor_traps'], 'hints': q['hints'], 'strategy': q['strategy'],
                    'remember': q['remember'], 'evidence_quote': q.get('evidence'),
                    'difficulty': difficulty, 'author': q['author'], 'origin': q['origin'],
                    'generation_date': q['created_at'],
                    'content_version': c.get('revision', 1), 'schema_version': q['schema_version'],
                    'license_recorded': q['license'],
                    'rights_status': 'NOT CLEARED: license value was set by the author pipeline; no legal, rights or human review has occurred',
                    'review_status': q['review_status'], 'human_review': q['human_review'],
                    'validation_summary': q['validation']})
        if p:
            passages_used[bank][p['passage_id']] = p
        target = full
        if q['id'] in retired:
            quarantine.append({'category': 'retired_after_acceptance', 'id': q['id'], 'bank': bank,
                               'reason': retired[q['id']], 'record': rec})
            target = None
        else:
            full.append(rec)
            blind.append(student)
        # answer key and review history
        rh = {'id': q['id'], 'live': q['id'] not in retired,
              'correct_answer': q['correct_answer'], 'explanation': q['explanation'],
              'distractor_explanations': q['distractor_explanations'], 'distractor_traps': q['distractor_traps'],
              'hints': q['hints'], 'strategy': q['strategy'], 'remember': q['remember'],
              'evidence_quote': q.get('evidence'),
              'review': {
                  'author_self_review': {'kind': 'AUTHOR SELF-REVIEW (the same model that wrote the item); not independent',
                                         'author_checklist': c.get('author_checklist')},
                  'programmatic_verification': (
                      {'kind': 'PROGRAMMATIC: scripted recomputation of the answer from the stem\'s numbers, written by the author',
                       'script': f'checks/{bank}/batch_{n:03d}.py', 'computed_answer': q['validation'].get('computed_answer'),
                       'matches_key': q['validation'].get('computed_answer') == q['correct_answer']} if is_math else
                      {'kind': 'PROGRAMMATIC STRUCTURE CHECKS ONLY: the cited evidence quote is verbatim in the passage, choices are well formed, '
                               'and a near-duplicate screen passed. This is NOT an independent solve; the "computed_answer" field in the '
                               'source record only records that these checks passed.',
                       'evidence_quote_present': q['validation'].get('computed_answer') == q['correct_answer']}),
                  'structure_and_duplicate_screen': {'structural_problems': res.get('structural_problems'),
                                                     'near_duplicates': res.get('near_duplicates')},
                  'separate_blind_solvers': blind_entries(bank, n, cand),
                  'whole_bank_ai_raters': [{'file': f, 'kind': 'separate AI agent rating the whole bank from an answer-free packet',
                                            **r[q['id']]} for f, r in raters[bank].items() if q['id'] in r],
                  'reconciliation': {'status': res.get('status'), 'reason': res.get('reason'),
                                     'revision': res.get('revision'), 'revision_history': res.get('revision_history')},
                  'human_review': None,
                  'human_review_note': 'No human has reviewed any item.'}}
        keyrev.append(rh)

# ---------- candidates that never became accepted records ----------
for (bank, cand), (n, f, c, kind) in sorted(cand_index.items()):
    res = review_result.get((bank, cand))
    if kind == 'candidate' and res and res['status'] == 'PASS':
        continue
    later = resubmitted_as.get((bank, cand), [])
    later_status = []
    for lc in later:
        lr = review_result.get((bank, lc))
        lid = lr.get('id') if lr else None
        later_status.append({'resubmitted_as': lc, 'status': lr['status'] if lr else 'not reviewed', 'accepted_id': lid})
    if kind == 'withdrawn':
        w = next(x for x in drafts[(bank, n)][1]['withdrawn'] if x['cand'] == cand)
        reason, category = w['reason'], 'withdrawn_before_review'
    elif res is None:
        reason, category = 'drafted but no review record exists', 'incomplete_draft'
    else:
        reason, category = f"{res['status']}: {res.get('reason')}", f"review_{res['status'].lower()}"
    quarantine.append({'category': category, 'candidate': cand, 'bank': bank, 'batch': n,
                       'draft_file': os.path.relpath(f, ROOT), 'reason': reason,
                       'later_resolution': later_status or 'none (not resubmitted)',
                       'pending_revision_log': [x for x in pending if x.get('cand') == cand],
                       'later_annotation': annotations.get((bank, cand)),
                       'blind_solver_records': blind_entries(bank, n, cand),
                       'item_as_drafted': c})

# ---------- cross-copy conflict check (bank vs exports vs import jsonl) ----------
conflicts = []
for bank in BANKS:
    stud = {x['id']: x for x in load(ROOT / 'exports' / f'{bank}.student.json')['questions']}
    akey = load(ROOT / 'exports' / f'{bank}.answer_key.json')
    akey = {x['id']: x for x in (akey['answers'] if 'answers' in akey else akey.get('questions', []))}
    imp = {}
    for line in (ROOT / 'exports' / 'import' / f'{bank}.jsonl').read_text(encoding='utf-8').splitlines():
        if line.strip():
            o = json.loads(line)
            imp[o['import_id']] = o
    for q in bank_docs[bank]['questions']:
        if q['id'] in retired:
            continue
        s = stud.get(q['id'])
        if s is None:
            conflicts.append({'id': q['id'], 'issue': 'missing from student export'})
        elif s.get('stem') != q['stem'] or s.get('choices') != q['choices']:
            conflicts.append({'id': q['id'], 'issue': 'student export differs from bank record'})
        k = akey.get(q['id'])
        if k is None or k.get('correct_answer') != q['correct_answer']:
            conflicts.append({'id': q['id'], 'issue': 'answer-key export missing or differs'})
        im = imp.get(q['id'].lower())
        if im is None:
            conflicts.append({'id': q['id'], 'issue': 'missing from import jsonl'})
        elif im['stem'] != q['stem'] or (im['accepted_answers'][:1] != [q['correct_answer']] if q.get('answer_format') == 'numeric'
                                           else im['accepted_answers'] != [q['correct_answer']]):
            # numeric (grid-in) items list equivalent forms after the key, e.g. ['1.5', '3/2']
            conflicts.append({'id': q['id'], 'issue': 'import jsonl differs from bank record'})

# ---------- checks ----------
ids = [x['id'] for x in full]
problems = []
if len(ids) != len(set(ids)):
    problems.append('duplicate IDs in accepted inventory')
if [x['id'] for x in blind] != ids or [x['id'] for x in keyrev if x['live']] != ids:
    problems.append('full / blind / answer-key ID lists do not match')
for x in full:
    if x['passage_id'] and not x['passage']:
        problems.append(f"{x['id']}: broken passage reference")
    if x.get('answer_format') == 'numeric':
        # student-produced response (SAT Math grid-in): no choices, a non-empty key, no distractor records
        if x['choices'] or not str(x['correct_answer']).strip():
            problems.append(f"{x['id']}: numeric item has choices or an empty key")
        continue
    if sorted(x['choices']) != ['A', 'B', 'C', 'D'] or any(not v for v in x['choices'].values()):
        problems.append(f"{x['id']}: choices incomplete")
    if x['correct_answer'] not in x['choices']:
        problems.append(f"{x['id']}: key not among choices")
    if len(set(x['choices'].values())) != 4:
        problems.append(f"{x['id']}: duplicate choice text")
    if set(x['distractor_explanations']) != set('ABCD') - {x['correct_answer']}:
        problems.append(f"{x['id']}: distractor explanations do not cover exactly the wrong choices")
LEAK = {'correct_answer', 'explanation', 'distractor_explanations', 'distractor_traps', 'hints', 'strategy', 'remember',
        'evidence', 'evidence_quote', 'validation', 'validation_summary', 'answer', 'key', 'subskill'}
for x in blind:
    bad = LEAK & set(x)
    if bad:
        problems.append(f"{x['id']}: blind record has answer-revealing fields {sorted(bad)}")

# exact and near duplicates within the accepted inventory (same bank)
def toks(s):
    return set(re.sub(r'[^a-z0-9]+', ' ', s.lower()).split())
dup_report = []
by_bank = defaultdict(list)
for x in full:
    by_bank[x['exam'] + ' ' + x['section']].append(x)
for k, xs in by_bank.items():
    seen = {}
    for x in xs:
        sig = (x['stem'], tuple(sorted((x['choices'] or {}).values())), x['passage_id'])
        if sig in seen:
            dup_report.append({'type': 'exact', 'ids': [seen[sig], x['id']]})
        seen[sig] = x['id']
    T = [(x['id'], toks(x['stem'] + ' ' + ' '.join((x['choices'] or {}).values())), x['passage_id']) for x in xs]
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            if T[i][2] and T[i][2] != T[j][2]:
                continue
            a, b = T[i][1], T[j][1]
            s = len(a & b) / max(1, len(a | b))
            if s >= 0.7:
                dup_report.append({'type': 'near (token Jaccard >= 0.70 on stem+choices)', 'similarity': round(s, 2),
                                   'ids': [T[i][0], T[j][0]]})

# ---------- write files ----------
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)
commit = git('rev-parse', 'HEAD')
meta = {'generated_at': NOW, 'repository': 'bemrick2/CollegePrep', 'branch': 'ccr-78c91309-anlh8e',
        'source_commit': commit, 'producer': 'question_bank/claude/tools/export_complete.py'}
all_passages = {b: sorted(passages_used[b].values(), key=lambda p: p['passage_id']) for b in BANKS}


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


write('questions-full.json', {'meta': meta, 'count': len(full),
                              'note': 'Accepted (PASS) and live items only. Retired items are in quarantined-and-incomplete.json. '
                                      'Each question embeds its full passage; the same passages are also listed under "passages".',
                              'passages': all_passages, 'questions': full})
write('questions-blind.json', {'meta': meta, 'count': len(blind),
                               'note': 'Student-facing material only: no keys, explanations, hints, strategies, evidence quotes, subskill labels or validation data.',
                               'questions': blind})
write('answer-key-and-review.json', {'meta': meta, 'count_live': sum(1 for x in keyrev if x['live']),
                                     'count_including_retired': len(keyrev),
                                     'evidence_kinds': {
                                         'author_self_review': 'Checklist written by the same model that wrote the item. Not independent.',
                                         'programmatic_verification': 'Math: a script recomputes the answer from the stem\'s numbers (written by the author, never reads the key). Verbal: structure checks and a check that the cited evidence quote appears verbatim in the passage; NOT an independent solve.',
                                         'separate_blind_solver': 'A separate AI agent, in its own context, given only an answer-free packet. Math: 1 solver per batch. Verbal: 2 solvers per batch. Same model family as the author; not human.',
                                         'whole_bank_ai_raters': 'Separate AI agents that re-solved and re-rated whole banks at audits, from answer-free packets.',
                                         'human_review': 'None. No human has reviewed any item.'},
                                     'items': keyrev})
write('quarantined-and-incomplete.json', {'meta': meta, 'counts': dict(Counter(x['category'] for x in quarantine)),
                                          'note': 'Kept out of accepted totals. "later_resolution" shows when a withdrawn or REVISE candidate was resubmitted and accepted under a new candidate number.',
                                          'items': quarantine,
                                          'cross_copy_conflicts': conflicts})

counts = defaultdict(Counter)
for x in full:
    counts[f"{x['exam']} {x['section']}"]['accepted_live'] += 1
for x in quarantine:
    b = x['bank']
    lab = {'act_math': 'ACT Math', 'act_english': 'ACT English', 'act_reading': 'ACT Reading',
           'sat_reading_writing': 'SAT Reading and Writing', 'sat_math': 'SAT Math'}[b]
    counts[lab][x['category']] += 1
manifest = {'meta': meta,
            'counts_by_exam_section_and_status': {k: dict(v) for k, v in counts.items()},
            'accepted_live_total': len(full),
            'unique_passages_used_by_accepted_items': {b: len(passages_used[b]) for b in BANKS},
            'difficulty_provisional': {k: dict(Counter(x['difficulty']['ai_calibrated_label'] for x in full if f"{x['exam']} {x['section']}" == k)) for k in counts},
            'author_difficulty_labels': {k: dict(Counter(x['difficulty']['author_label'] for x in full if f"{x['exam']} {x['section']}" == k)) for k in counts},
            'checks': {'json_parse': 'all package JSON files parsed after writing (see below)',
                       'id_alignment_full_blind_key': 'ok' if not any('do not match' in p for p in problems) else 'FAILED',
                       'problems': problems, 'duplicate_report_within_this_bank': dup_report,
                       'cross_copy_conflicts_bank_vs_exports_vs_import': conflicts},
            'sources_inspected': [
                f'repository bemrick2/CollegePrep, branch ccr-78c91309-anlh8e at {commit}: question_bank/claude/ (banks, drafts, reviews, checks, calibration, audits, exports)',
                'branch origin/main: contains no question_bank/claude directory and no Claude-generated items (checked with git ls-tree)',
                'local git: only branches main and ccr-78c91309-anlh8e exist; no other worktrees',
                'session scratchpad: generator scripts that wrote the draft files; every item they produced is in drafts/, so they add no questions',
                'this conversation context (summarized history): all batches it describes are present in drafts/ and reviews/'],
            'missing_or_inaccessible_sources': [
                'Pre-revision passage text for batches whose passages were corrected after a blind solve (revision_log in the draft file) was overwritten in drafts/; only the revision_log entries and the round-N solver reviews remain.',
                'No other Claude sessions, branches or banks are accessible from this session; none are claimed.',
                "ChatGPT's banks are not included (not produced here)."],
            'files': {}}
write('manifest.json', manifest)

# ---------- supporting files, README, checklist, checksums, zip ----------
validator_out = Path(sys.argv[1]).read_text(encoding='utf-8') if len(sys.argv) > 1 else 'validator not run'
(OUT / 'import-validation-report.txt').write_text(
    'Output of `npx vite-node scripts/validateQuestionImport.ts <file>` (run from web/) on each file in source/exports/import/,\n'
    f'at {NOW}, commit {commit}.\n\n' + validator_out, encoding='utf-8')
src = OUT / 'source'
for d in ['banks', 'drafts', 'reviews', 'checks', 'calibration', 'audits', 'exports/import']:
    shutil.copytree(ROOT / d, src / d, ignore=shutil.ignore_patterns('__pycache__'))
for f in ['progress.json', 'WORKER.md', 'README.md', 'tools/qb.py', 'tools/blind_packet.py', 'tools/calibrate.py',
          'tools/export_complete.py']:
    (src / f).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / f, src / f)
(OUT / 'contract').mkdir()
shutil.copy2(REPO / 'docs' / 'product' / 'QUESTION_IMPORT_CONTRACT.md', OUT / 'contract' / 'QUESTION_IMPORT_CONTRACT.md')
if (REPO / 'docs' / 'product' / 'QUESTION_REVIEW_WORKFLOW.md').exists():
    shutil.copy2(REPO / 'docs' / 'product' / 'QUESTION_REVIEW_WORKFLOW.md', OUT / 'contract' / 'QUESTION_REVIEW_WORKFLOW.md')

C = manifest['counts_by_exam_section_and_status']
qc = Counter(x['category'] for x in quarantine)
rows = '\n'.join(f"| {k} | {v.get('accepted_live', 0)} | {v.get('retired_after_acceptance', 0)} | {v.get('review_revise', 0)} | "
                 f"{v.get('review_reject', 0)} | {v.get('withdrawn_before_review', 0)} | {v.get('incomplete_draft', 0)} |"
                 for k, v in C.items())
diffrows = '\n'.join(f"| {k} | {manifest['author_difficulty_labels'][k]} | {manifest['difficulty_provisional'][k]} |" for k in C)
resolved = sum(1 for x in quarantine if isinstance(x.get('later_resolution'), list)
               and any(r.get('status') == 'PASS' for r in x['later_resolution']))
readme = f"""# Prep & Price: complete export of Claude's question bank

Generated {NOW} from `bemrick2/CollegePrep`, branch `ccr-78c91309-anlh8e`, commit `{commit}`
(path `question_bank/claude/`). Producer: `source/tools/export_complete.py`.

**Every item is an AI-generated draft.** No human has reviewed any item. No rights or legal review has occurred.
Nothing here has been imported, deployed or published.

## Exact counts

Accepted and live: **{len(full)}** items.

| Exam / section | Accepted (live) | Retired after acceptance | REVISE | REJECT | Withdrawn before review | Incomplete drafts |
|---|---|---|---|---|---|---|
{rows}

- Unique passages used by accepted items: ACT English {manifest['unique_passages_used_by_accepted_items']['act_english']}, ACT Reading {manifest['unique_passages_used_by_accepted_items']['act_reading']}, SAT Reading and Writing {manifest['unique_passages_used_by_accepted_items']['sat_reading_writing']} (each SAT Reading and Writing item has its own short passage). ACT Math and SAT Math have none.
- Quarantined or incomplete records in total: {len(quarantine)}. Of these, {resolved} were later fixed, resubmitted under a new candidate number and accepted. The accepted version is in `questions-full.json`, and the earlier version stays in `quarantined-and-incomplete.json` with a `later_resolution` link. They are not counted twice.
- Incomplete drafts (drafted but never reviewed): {qc.get('incomplete_draft', 0)}.

## Files

| File | Contents |
|---|---|
| `questions-full.json` | The {len(full)} accepted, live items, each with its full record. This covers: source (bank file, batch, draft candidate, draft and review files, branch); exam, section, category, skill, subskill and modeling flag; the full passage and stable `passage_id`; underlined-span number (ACT English); figure spec; stem and choices; calculator policy; key, explanation, distractor explanations and trap types; hints, strategy and remember line; the cited evidence quote (verbal); provisional difficulty; author, origin and generation date; content version; recorded license and rights status; review status; and the validation summary. |
| `questions-blind.json` | The same {len(blind)} items with the same IDs. It contains only student-facing material: exam, section, category, skill, passage, underlined-span number, figure spec, stem, choices, calculator policy and time. It has no keys, explanations, hints, strategies, evidence quotes, subskill labels or validation data. |
| `answer-key-and-review.json` | For every accepted record, matched by ID: key, explanation and distractor reasoning, plus the review history separated into author self-review, programmatic verification, separate blind solvers (every round), whole-bank AI raters and human review (none). It includes the {len(keyrev) - len(full)} retired records, marked `live: false`. |
| `quarantined-and-incomplete.json` | Retired, REVISE, REJECT and withdrawn candidates, each with its reason, the item as drafted, any blind-solver records, any later resubmission and its outcome, and a check for conflicts between copies. |
| `manifest.json` | Counts, checks, the near-duplicate report, the sources inspected, missing sources and SHA-256 checksums of every file. |
| `quality-screening-checklist.md` | A checklist for screening the combined (Claude + ChatGPT) bank. |
| `import-validation-report.txt` | Output of the repository's own import validator on `source/exports/import/*.jsonl`. |
| `contract/` | `QUESTION_IMPORT_CONTRACT.md` (the `question_import/v1` contract) and `QUESTION_REVIEW_WORKFLOW.md`. |
| `source/` | Unmodified copies of the workstream's source files. `banks/` holds the append-only accepted banks, including retired records. `drafts/` holds every candidate as written. `reviews/` holds the per-batch reconciliation and every blind-solver file, including earlier rounds. `checks/` holds the math recomputation scripts. `calibration/` holds the whole-bank AI ratings. `audits/` holds the retirement, overlap and pending-revision logs. `exports/import/*.jsonl` holds the contract-format files. Also included: `progress.json`, `WORKER.md`, `README.md` and the tools. |

There are no binary assets. {sum(1 for x in full if x.get("figure"))} math items carry a text `figure` description; every item is meant to be solvable from its text, and figures need human checking before production. Tables are written inline in the stem or passage, with `|` separators.

## What the validation evidence does and does not mean

- **Author self-review.** The checklist was written by the same model that wrote the item. It is not independent.
- **Programmatic verification.** For **Math**, a script in `checks/` recomputes the answer from the stem's numbers. The author wrote these scripts, but they never read the key, and the computed answer matches the key for every accepted item. For **verbal** items there is **no** programmatic solve. The checks confirm only the structure, that the cited evidence quote appears word for word in the passage, and a near-duplicate screen. In the source records, the verbal `computed_answer` field only records that those checks passed.
- **Separate blind solvers.** These are separate AI agents of the same model family, each working in its own context from an answer-free packet: one per Math batch and two per verbal batch. An item was accepted only when every solver matched the key and no solver raised a non-minor flag. These solvers are not human and not truly independent of the author model.
- **Whole-bank AI raters.** These are separate AI agents that re-solved and re-rated whole banks at the 100-item audits. Items where a rater disagreed with the key were adjudicated at audits, with notes in `source/progress.json` (`calibration_notes` and `audits`). **The author adjudicated these, so they still need human review.**
- **Human review.** There has been none. `review_status` is `ai_reviewed_pending_human` and `human_review` is null on every record.

## Difficulty is provisional

`difficulty.author_label` is the author's estimate. `difficulty.ai_calibrated_label` is the median of the AI solver and rater ratings, which estimate the share of typical students who would answer correctly. Neither comes from student responses.

| Exam / section | Author labels | AI-calibrated labels |
|---|---|---|
{diffrows}

The independent raters consistently judge verbal items, and many items labelled hard, as easier than the author labels say. **ACT Reading has no item that the raters judge hard.**

## Known issues and flags

1. **Near-duplicates.** The manifest's `duplicate_report_within_this_bank` lists {len(dup_report)} pairs within this bank that share at least 70% of the words in stem and choices. These are lexical candidates for a human to compare, not confirmed duplicates. Concept repeats found at audits were already retired: {len(retired)} items, listed in `source/audits/`. Template-level repeats with changed numbers may remain, because the bank grew from one model's habits. The duplicate screen against ChatGPT's banks has not been done.
2. **Rights.** `license_recorded` is `original-owned` on every item. The pipeline set that value; no legal review backs it. Some verbal passages state real-world facts or name real people and studies, which the blind solvers checked only from memory. SAT passage `CLD-P-SAT-RW-000259` (item `CLD-SAT-RW-000250`) quotes two lines of Christina Rossetti's 1872 poem "Who Has Seen the Wind?". The poem is in the public domain, but the recorded license does not say so.
3. **Earlier passage text.** Some passages were corrected after a blind solve; each such draft's `revision_log` records it. In those cases the draft file was overwritten, so the earlier passage text is not preserved. The round-N solver reviews that prompted each correction are in `source/reviews/` as `*.round*.blind*.json`.
4. **Answer-key letter balance.** Keys are spread across A–D, but at times the spread was uneven. The 600-item audit, for example, found Math keys leaning toward B and C. Later batches weighted keys toward A and D to compensate.
5. **SAT stems referring to an underlined sentence.** These name the sentence in the stem (for example, "The underlined sentence is ...") because the record format has no underline markup for SAT. Rendering would need to add the underline.

## Relation to the repository's import contract

`source/exports/import/*.jsonl` holds the same live items in the repository's `question_import/v1` format (`contract/QUESTION_IMPORT_CONTRACT.md`). Each line has `status: draft`, `origin: ai_drafted`, `author: ai:claude` and `import_id` = lowercased ID. The repository's validator (`web/scripts/validateQuestionImport.ts`) reports **0 problems** for all five files (`import-validation-report.txt`). As the contract states, passing the validator only makes an item eligible to **start** human editorial stage 3; it is not approval. `questions-full.json` and the other package files are **not** in contract format and have not been validated against it.

## Sources and coverage

See `manifest.json` → `sources_inspected` and `missing_or_inaccessible_sources`. In short:
- The complete source of truth is `question_bank/claude/` on branch `ccr-78c91309-anlh8e`.
- `main` contains no Claude items, and no other branches, worktrees or sessions are accessible from here.
- No question was reconstructed from memory, and none was generated for this export.
"""
(OUT / 'README.md').write_text(readme, encoding='utf-8')

checklist = """# Quality-screening checklist for the combined bank (Claude + ChatGPT)

This checklist prepares the combined screen. **The combined bank has not been screened.** This export contains only Claude's items.

Record one outcome per question: **PASS**, **REVISE** (fixable, with the specific fix), **QUARANTINE** (needs a decision or more evidence) or **REJECT** (fundamentally flawed or a duplicate). Give a question-level reason for every outcome other than PASS.

## 1. Inventory and identity
- [ ] Load every contributing bank; confirm counts match each bank's manifest.
- [ ] Check ID uniqueness across banks (Claude IDs start with `CLD-`); never re-key silently.
- [ ] Every passage reference resolves; passage sets are complete; no orphan passages.
- [ ] No item reaches students: keep all items `draft` until human stages 3–8 and the rights gate pass.

## 2. Duplicates (across ALL banks, not just within one)
- [ ] Exact duplicates: identical stem + choices (after normalizing whitespace, Unicode minus signs, superscripts and `^`).
- [ ] Near duplicates: high token overlap of stem + choices (Claude's manifest lists pairs within its own bank at ≥ 0.70 Jaccard).
- [ ] **Template duplicates**: same underlying problem with changed numbers, names or context (e.g., "car worth $X loses Y% a year", "units digit of 7^n", "circle tangent to both axes through (a, b)"). Compare by subskill/skill tag *and* solution method, not wording alone.
- [ ] Same passage topic or the same real-world study used in two banks.
- [ ] Two items on the same passage that test the same idea, or where one item's choices give away another's answer.
- [ ] Keep the better item of each duplicate set; record the others as REJECT (duplicate of ID).

## 3. Blind solving (without author keys)
- [ ] A solver who has not seen any key answers every item from student-facing text only (`questions-blind.json` for Claude).
- [ ] Any disagreement with the key → QUARANTINE until adjudicated by a human; never let the author adjudicate alone.
- [ ] Record the solver's confidence and estimated difficulty.

## 4. Correctness and answer quality
- [ ] Exactly one defensible correct answer; no "also arguably correct" choice.
- [ ] Distractors are plausible, distinct, each tied to a real error, and none is accidentally correct.
- [ ] Math: arithmetic, domains and restrictions (division by zero, square roots, logs), units and rounding instructions, exact vs. approximate answers, figure/table consistency, and "not drawn to scale" where relevant.
- [ ] Verbal: the answer is supported by the passage text (cite the line); no outside knowledge needed; English edit spans are unambiguous and "NO CHANGE" is handled correctly; punctuation items have one standard answer.
- [ ] Factual claims in passages are accurate (dates, quantities, named studies), or the passage is clearly fictional.
- [ ] No answer cue: key not systematically longest, not the only choice in a different style, not echoed by the stem.

## 5. Alignment, clarity and difficulty
- [ ] Exam/section alignment (ACT Math, English, Reading; SAT Reading and Writing; SAT Math) and correct category/skill tags.
- [ ] Item format matches the exam (4 choices for ACT enhanced and SAT; SAT one-passage-one-question).
- [ ] Clear, grade-appropriate wording; calculator policy stated where relevant.
- [ ] Difficulty labels marked **provisional**; replace with student-response calibration when available. Note where AI raters and author labels disagree.

## 6. Originality, provenance and rights
- [ ] Origin and author recorded (`ai:claude` / ChatGPT equivalent); every reviewer differs from the author.
- [ ] No official ACT or College Board material, and no close paraphrase of commercial prep items.
- [ ] Quoted text (e.g., public-domain poetry) is identified and licensed correctly.
- [ ] License field is verified by a person before any item is served (`original-owned` was set by a pipeline, not reviewed).

## 7. Outcome record (per question)
| Field | Content |
|---|---|
| id | Original ID |
| bank | Contributing bank |
| outcome | PASS / REVISE / QUARANTINE / REJECT |
| reason | Specific, question-level |
| duplicate_of | ID, if any |
| reviewer | Named person or tool; never the author model alone |
| evidence | Blind-solve result, check performed, source consulted |
"""
(OUT / 'quality-screening-checklist.md').write_text(checklist, encoding='utf-8')

# parse every JSON file in the package and record checksums
parse_errors = []
for p in sorted(OUT.rglob('*.json')):
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        parse_errors.append(f'{p.relative_to(OUT)}: {e}')
manifest['checks']['json_parse'] = {'files_parsed': len(list(OUT.rglob('*.json'))), 'errors': parse_errors}
manifest['files'] = {str(p.relative_to(OUT)): {'sha256': sha256(p), 'bytes': p.stat().st_size}
                     for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'manifest.json'}
write('manifest.json', manifest)
json.loads((OUT / 'manifest.json').read_text(encoding='utf-8'))

if ZIP.exists():
    ZIP.unlink()
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file():
            z.write(p, Path('prep-and-price-claude-complete-export') / p.relative_to(OUT))
with zipfile.ZipFile(ZIP) as z:
    assert z.testzip() is None
print(json.dumps({'accepted_live': len(full), 'quarantined_or_incomplete': len(quarantine), 'problems': problems,
                  'conflicts': len(conflicts), 'near_dup_pairs': len(dup_report), 'json_parse_errors': parse_errors,
                  'zip': str(ZIP), 'zip_bytes': ZIP.stat().st_size}, indent=1))
