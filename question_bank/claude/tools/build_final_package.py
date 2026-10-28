#!/usr/bin/env python3
"""Build the final package of the reconciled combined bank (all sources) as one ZIP.

Reads (never modifies) the reconciled bank, the preserved baseline ZIP, overlays, banks, drafts, per-batch review files
and the final audit outputs. Writes exports/final/ and exports/prep-and-price-final-reconciled-bank-<date>.zip:

  complete-bank.json                every reconciled record (all statuses) in its effective content version, with keys,
                                    explanations, provenance, content hash and review evidence
  review-packet-answer-free.json    the reviewed_draft records, student-facing fields only (no keys, explanations,
                                    hints, evidence, skills or validation data)
  keys-and-explanations.json        per reviewed_draft record: key, explanation, distractor rationales, hints,
                                    strategy, evidence and the review evidence
  held-and-rejected.json            every non-reviewed record (pending, hold, reserved duplicate, retired) plus Claude
                                    draft candidates that ended REVISE or REJECT and were never banked
  final-quality-coverage-report.md  counts, coverage, difficulty estimates, audit results, open issues
  audits/                           final audit, resolutions, duplicate screens and adjudications
  manifest.json                     file list with SHA-256 checksums, branch and commit

Usage: python3 -I tools/build_final_package.py
"""
import datetime as dt
import glob
import hashlib
import json
import re
import shutil
import statistics
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import final_audit as F  # noqa: E402

ROOT = F.ROOT
REPO = ROOT.parents[1]
TODAY = dt.date.today().isoformat()
OUT = ROOT / 'exports' / 'final'
ZIP = ROOT / 'exports' / f'prep-and-price-final-reconciled-bank-{TODAY}.zip'
ORDER = ['SAT Math', 'SAT Reading and Writing', 'ACT English', 'ACT Reading', 'ACT Math']
TARGETS = {'SAT Math': 1000, 'SAT Reading and Writing': 1000, 'ACT English': 1000, 'ACT Reading': 1000}
# Approximate published weights (verify against the current official specifications before relying on them).
OFFICIAL = {
    'SAT Reading and Writing': {'Craft and Structure': '~28%', 'Information and Ideas': '~26%',
                                'Standard English Conventions': '~26%', 'Expression of Ideas': '~20%'},
    'SAT Math': {'Algebra': '~35%', 'Advanced Math': '~35%', 'Problem-Solving and Data Analysis': '~15%',
                 'Geometry and Trigonometry': '~15%'},
    'ACT English': {'Production of Writing': '38-43%', 'Knowledge of Language': '13-19%',
                    'Conventions of Standard English': '38-43%'},
    'ACT Reading': {'Key Ideas and Details': '55-60%', 'Craft and Structure': '25-30%',
                    'Integration of Knowledge and Ideas': '13-18%'},
}


# Category inferred from the source skill name, for ChatGPT records whose source gives a skill but no reporting category.
INFER = {
    'Reading and Writing': [
        ('Standard English Conventions', r'^(boundaries|form, structure|modifiers|possessives|pronoun|punctuation|subject-verb|verb)'),
        ('Information and Ideas', r'^(central idea|command of|inferences|logical completion|quantitative evidence)'),
        ('Craft and Structure', r'^(cross-text|function of|text structure|words in context)'),
        ('Expression of Ideas', r'^(rhetorical synthesis|transitions)')],
    'English': [
        ('Conventions of Standard English', r'^(agreement|clause structure|modifier|nonessential|parallel|pronoun|punctuation|sentence boundaries|sentence combination|subordination|verb tense|reference clarity|subject-verb)'),
        ('Knowledge of Language', r'^(concision|precis|style)'),
        ('Production of Writing', r'^(conclusion|organization|relevance|rhetorical function|purpose|clarity of purpose|author claim|scope of conclusion|explicit relationship|transitions)')],
    'Reading': [
        ('Integration of Knowledge and Ideas', r'^(cross-passage|synthesis|evidence and limitations|experimental reasoning|evidence$|author claim limits|application)'),
        ('Craft and Structure', r'^(author attitude|author purpose|function of|purpose of detail|figurative|meaning of statement|narrative|structure|vocabulary|words in context|ending)'),
        ('Key Ideas and Details', r'^(central idea|explicit|detail|inference|cause|sequence|chronology|comparison|character|evidence-based|text evidence|reasoning|turning point)')],
}


def infer_category(section, skill):
    for cat, rx in INFER.get(section, []):
        if skill and re.search(rx, skill.strip().lower()):
            return cat
    return None


def git(*a):
    return subprocess.run(['git', '-C', str(REPO), *a], capture_output=True, text=True).stdout.strip()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def render_blind(e):
    t = e.get('passage') or ''
    if e['source'] == 'Claude' and e['section'] == 'English':
        u = e.get('underline')
        return F.UL.sub(lambda m: f'[{m.group(2)}]' if u is not None and int(m.group(1)) == u else m.group(2), t)
    return t


def category(e):
    q = e.get('q') or {}
    raw = e.get('raw') or {}
    return q.get('reporting_category') or raw.get('reporting_category') or raw.get('category') or None


def difficulty(e):
    q = e.get('q') or {}
    raw = e.get('raw') or {}
    v = q.get('validation') or {}
    d = {'label': q.get('difficulty') or raw.get('difficulty_estimate') or raw.get('estimated_difficulty') or raw.get('provisional_difficulty'),
         'label_basis': q.get('difficulty_basis') or raw.get('difficulty_basis') or 'author estimate',
         'ai_calibrated_label': q.get('difficulty_calibrated'),
         'solver_est_pct_correct': v.get('blind_est_pct_correct'),
         'solver_difficulty_opinion': v.get('blind_difficulty_opinion'),
         'status': 'provisional: AI and author estimates only; no student response data'}
    fr = e.get('fresh_reviews') or []
    pcts = [r.get('est_pct_correct') for r in fr if isinstance(r.get('est_pct_correct'), (int, float))]
    if pcts and d['solver_est_pct_correct'] is None:
        d['solver_est_pct_correct'] = round(statistics.mean(pcts))
    ops = [r.get('difficulty_opinion') for r in fr if r.get('difficulty_opinion')]
    if ops and not d['solver_difficulty_opinion']:
        d['solver_difficulty_opinion'] = Counter(ops).most_common(1)[0][0]
    return d


def review_evidence(e):
    q = e.get('q') or {}
    if e['source'] == 'Claude' and q:
        v = q.get('validation') or {}
        return {'kind': 'bank validation record (accepted only if every blind solver matched the key with no non-minor flag)',
                'method': v.get('method'), 'blind_answer': v.get('blind_answer'), 'blind_flags': v.get('blind_flags'),
                'review_file': v.get('evidence'), 'computation': v.get('computation'),
                'revisions_before_pass': v.get('revisions_before_pass'), 'human_review': None}
    fr = e.get('fresh_reviews') or []
    return {'kind': 'fresh blind reviews bound to the content hash' if fr else
            ('baseline current-version external AI PASS' if e.get('baseline_current_external_review') else 'none'),
            'fresh_reviews': [{k: r.get(k) for k in ('file', 'solver', 'verdict', 'answer', 'key', 'content_hash', 'flags')} for r in fr],
            'overlay_applied': bool(e.get('overlay_applied')), 'human_review': None}


def full(e):
    q = e.get('q') or {}
    raw = e.get('raw') or {}
    dis = q.get('distractor_explanations') or raw.get('reasons_alternatives_fail') or None
    return {
        'id': e['id'], 'source': e['source'], 'exam': e['exam'], 'section': e['section'], 'status': e['status'],
        'status_reason': e.get('status_reason'), 'human_approved': False,
        'provenance': {'source_bank': e.get('source_bank') or e.get('bank'), 'in_baseline': e.get('in_baseline'),
                       'batch': q.get('batch') or raw.get('batch_id') or raw.get('authoring_batch_id'),
                       'draft_candidate': q.get('draft_candidate'), 'author': q.get('author') or raw.get('origin'),
                       'overlay': (e.get('overlay') or {}).get('kind'), 'superseded_by': e.get('superseded_by')},
        'content_hash': e.get('content_hash'), 'content_version': raw.get('content_version') if e['source'] != 'Claude' else 1,
        'reporting_category': category(e),
        'reporting_category_inferred': None if category(e) else infer_category(e['section'], q.get('skill') or raw.get('skill')),
        'skill': q.get('skill') or raw.get('skill'), 'subskill': q.get('subskill'),
        'passage_id': e.get('passage_id'), 'passage': e.get('passage') or None, 'underline': e.get('underline'),
        'stem': e.get('stem'), 'choices': e.get('choices') or None, 'answer_format': q.get('answer_format'),
        'key': e.get('key'), 'accepted_answers': e.get('accepted_answers'),
        'explanation': e.get('explanation'), 'distractor_rationales': dis, 'distractor_traps': q.get('distractor_traps'),
        'hints': e.get('hints') or [], 'strategy': q.get('strategy'), 'remember': q.get('remember'),
        'evidence': q.get('evidence'), 'figure': q.get('figure'), 'calculator': q.get('calculator') or raw.get('calculator_policy'),
        'expected_time_seconds': q.get('expected_time_seconds'),
        'difficulty': difficulty(e), 'review_evidence': review_evidence(e),
    }


def never_banked():
    """Claude draft candidates whose final review outcome was REVISE or REJECT (never banked)."""
    out = []
    accepted_hist = defaultdict(list)
    for f in glob.glob(str(ROOT / 'drafts' / '*' / 'batch-*.json')):
        for c in F.load(f).get('candidates', []):
            for h in c.get('revision_history') or []:
                if h.get('cand'):
                    accepted_hist[h['cand']].append(c['cand'])
    for f in sorted(glob.glob(str(ROOT / 'reviews' / '*' / 'batch-*.review.json'))):
        doc = F.load(f)
        bank = doc.get('bank')
        draftp = ROOT / 'drafts' / bank / f"batch-{int(doc['batch']):03d}.json"
        drafts = {c['cand']: c for c in F.load(draftp).get('candidates', [])} if draftp.exists() else {}
        for r in doc.get('results', []):
            if r.get('status') in ('REVISE', 'REJECT'):
                later = accepted_hist.get(r['cand'], [])
                out.append({'cand': r['cand'], 'bank': bank, 'batch': doc['batch'], 'outcome': r.get('status'),
                            'reason': r.get('reason'), 'blind_flags': r.get('blind_flags'), 'blind2_flags': r.get('blind2_flags'),
                            'later_resubmitted_as': later, 'review_file': str(Path(f).relative_to(ROOT)),
                            'draft': drafts.get(r['cand'])})
    return out


def pct(n, d):
    return f'{100 * n / d:.0f}%' if d else '-'


def main():
    recs, passages, superseded = F.effective_records()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / 'audits').mkdir(parents=True)
    rows = [full(e) for e in recs]
    by = {r['id']: r for r in rows}
    reviewed = [r for r in rows if r['status'] == 'reviewed_draft']
    head = git('rev-parse', 'HEAD')
    branch = git('rev-parse', '--abbrev-ref', 'HEAD')
    meta = {'generated_at': dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(), 'branch': branch,
            'source_commit': head, 'note': 'AI-generated drafts. No record is human-approved; difficulty is provisional. Nothing imported, deployed or published.'}

    def dump(name, obj):
        (OUT / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

    dump('complete-bank.json', {'meta': meta, 'records': rows})
    dump('review-packet-answer-free.json', {'meta': dict(meta, contents='reviewed_draft records, student-facing fields only'),
        'records': [{'id': r['id'], 'exam': r['exam'], 'section': r['section'], 'passage_id': r['passage_id'],
                     'passage': render_blind(e) or None, 'stem': r['stem'], 'choices': r['choices'],
                     'answer_format': r['answer_format'], 'calculator': r['calculator'], 'figure': r['figure']}
                    for r, e in ((by[e['id']], e) for e in recs if e['status'] == 'reviewed_draft')]})
    dump('keys-and-explanations.json', {'meta': meta, 'records': [
        {k: r[k] for k in ('id', 'key', 'accepted_answers', 'explanation', 'distractor_rationales', 'distractor_traps', 'hints',
                           'strategy', 'remember', 'evidence', 'reporting_category', 'skill', 'subskill', 'difficulty', 'review_evidence')}
        for r in reviewed]})
    nb = never_banked()
    dump('held-and-rejected.json', {'meta': meta,
        'reconciled_not_usable': [r for r in rows if r['status'] != 'reviewed_draft'],
        'claude_candidates_never_banked': nb})
    for f in ['final-audit-%s.json' % TODAY, 'final-audit-resolutions-%s.json' % TODAY, 'dup-screen-whole-bank.json',
              'dup-screen-post-baseline.json', 'dup-adjudication-final-%s.json' % TODAY, 'dup-adjudication-wholebank-%s.json' % TODAY,
              'dup-adjudication-satmath.json', 'insertion-scan-combined.json']:
        p = F.COMB / 'audits' / f
        if p.exists():
            shutil.copy(p, OUT / 'audits' / f)
    for p in [ROOT / 'audits' / 'fact_correction_seneca_village_2026-10-28.json', ROOT / 'audits' / 'passage_consistency_act_english_2026-10-28.json',
              ROOT / 'audits' / 'retired.json', F.COMB / 'overlays.json', F.COMB / 'progress.json', F.COMB / 'reconciled' / 'summary.json']:
        shutil.copy(p, OUT / 'audits' / p.name)

    # ---------- report
    audit = F.load(F.COMB / 'audits' / f'final-audit-{TODAY}.json')
    res = F.load(F.COMB / 'audits' / f'final-audit-resolutions-{TODAY}.json')
    st = defaultdict(Counter)
    src = defaultdict(Counter)
    for r in rows:
        k = f"{r['exam']} {r['section']}"
        st[k][r['status']] += 1
        if r['status'] == 'reviewed_draft':
            src[k][r['source']] += 1
    L = [f'# Final quality and coverage report: reconciled Prep & Price question bank', '',
         f"Generated {meta['generated_at']} from branch `{branch}`, source commit `{head}` (the package files themselves are committed in the next commit).", '',
         '**Every record is an AI-generated draft. None is human-approved. Difficulty is provisional (AI and author estimates; no student data). Nothing has been imported, deployed or published.**', '',
         '## Counts (reconciled bank)', '',
         '| Section | Target | Reviewed drafts (usable) | Claude | ChatGPT | Pending review | Hold | Reserved duplicate | Retired |',
         '|---|---|---|---|---|---|---|---|---|']
    for k in ORDER:
        c = st[k]
        L.append(f"| {k} | {TARGETS.get(k, 'paused')} | **{c['reviewed_draft']}** | {src[k]['Claude']} | {src[k]['ChatGPT']} | {c['pending_review']} | {c['hold']} | {c['reserved_duplicate']} | {c['retired']} |")
    L += ['', 'Only `reviewed_draft` records count toward targets: the current content version has independent AI blind-review evidence (no key) and no open hold.', '']
    L += ['## Coverage by reporting category (reviewed drafts)', '']
    for k in ORDER[:4]:
        live = [r for r in reviewed if f"{r['exam']} {r['section']}" == k]
        c = Counter(r['reporting_category'] or r['reporting_category_inferred'] or 'unclassified' for r in live)
        inf = Counter(r['reporting_category_inferred'] for r in live if not r['reporting_category'] and r['reporting_category_inferred'])
        L += [f'### {k}', '', '| Category | Items | Share | Of which inferred from source skill | Published weight (approx.; verify) |', '|---|---|---|---|---|']
        for cat, n in c.most_common():
            L.append(f"| {cat} | {n} | {pct(n, len(live))} | {inf.get(cat, 0)} | {OFFICIAL.get(k, {}).get(cat, '')} |")
        L.append('')
    L += ['Some ChatGPT records give a skill but no reporting category; their category is inferred from the skill name (`reporting_category_inferred`, mapping in `tools/build_final_package.py`). The published weights are approximate and must be checked against the current official specifications.', '',
          'Main coverage gaps against the published weights: ACT Reading is light on Key Ideas and Details (43% vs 55-60%) and heavy on Integration of Knowledge and Ideas; ACT English is heavy on Conventions (49%) and light on Production of Writing (33% vs 38-43%); SAT Reading and Writing is close to the official split (Standard English Conventions slightly light); SAT Math is heavier on Problem-Solving and Geometry, and lighter on Algebra and Advanced Math, than the official split. These are bank-level shares; a practice form would be assembled to the blueprint.', '']
    L += ['## Difficulty estimates (provisional)', '',
          '| Section | Author labels (easy / medium / hard / none) | Blind-solver estimate of % correct: median (IQR) | Solver opinions (easy / medium / hard) |', '|---|---|---|---|']
    for k in ORDER:
        live = [r for r in reviewed if f"{r['exam']} {r['section']}" == k]
        lab = Counter((r['difficulty']['label'] or 'none').lower() for r in live)
        p = sorted(x['difficulty']['solver_est_pct_correct'] for x in live if isinstance(x['difficulty']['solver_est_pct_correct'], (int, float)))
        q = (f"{statistics.median(p):.0f}% ({p[len(p) // 4]}-{p[3 * len(p) // 4]}%), n={len(p)}" if p else 'n/a')
        op = Counter((r['difficulty']['solver_difficulty_opinion'] or 'none') for r in live)
        L.append(f"| {k} | {lab['easy']} / {lab['medium']} / {lab['hard']} / {sum(v for kk, v in lab.items() if kk not in ('easy', 'medium', 'hard'))} | {q} | {op['easy']} / {op['medium']} / {op['hard']} |")
    L += ['', 'Solver estimates come from AI agents, not students. Verbal items skew easy-to-medium in AI solves. "Hard" labels were not forced. All difficulty data needs student calibration.', '']
    L += ['## Final whole-bank audit', '',
          f"Run by `tools/final_audit.py` over {audit['records']} reconciled records. Blocking findings: **{audit['blocking_total']}**. Nonblocking: {audit['findings_total'] - audit['blocking_total']} ({', '.join(f'{k} {v}' for k, v in audit['nonblocking_by_check'].items())}).", '',
          '| Check | What was verified | Result |', '|---|---|---|',
          '| Structure | four distinct, non-empty choices A-D with the key among them (or accepted answers for student-produced responses), stem, explanation, passage for verbal items, ACT English underline present | pass (4 stale underline numbers on essay-level items; nonblocking) |',
          '| Review evidence | Claude: bank validation PASS, blind answer = key, review file present, second verbal solver = key; ChatGPT: current-version external PASS or fresh PASS reviews bound to the content hash, overlay applied | pass |',
          '| Passage consistency | passages resolve; no reviewed item on a superseded passage; every ACT English span with an error is tested by a reviewed item or recorded as acceptable text | pass (5 ChatGPT span labels with no item, none an untested error) |',
          '| Literal insertion | every option inserted at its blank or underline; seams checked for missing or doubled spaces, doubled punctuation, space before punctuation | pass after 10 repairs |',
          '| Hints | no hint repeats the key\'s distinctive wording | pass after 1 repair |',
          f"| Duplicates | exact duplicates; post-baseline screen ({audit['near_duplicate_pairs_between_reviewed_records']} pairs between reviewed records); new whole-bank pairwise and math-signature screen; independent adjudication of every unadjudicated pair | pass after 4 quarantines; 2 pairs kept by recorded override |", '']
    L += ['### Resolved during the audit', '']
    for s in res['superseded_after_fresh_review']:
        L.append(f"- {s['old']} superseded by {s['new']} (two fresh blind solves)")
    for qd in res['quarantined_duplicates']:
        L.append(f"- {qd['id']} quarantined as a duplicate of {qd['kept']}" + (f"; replaced by {qd['replacement']}" if qd['replacement'] else ''))
    L += ['', 'Earlier in this phase: the Seneca Village factual overstatement (passage CLD-P-ACT-E-000063) was corrected from Central Park Conservancy sources as CLD-P-ACT-E-000068, and all nine items were re-reviewed and superseded. 14 untested error spans in ACT English passages received their own reviewed items.', '']
    L += ['## Open issues (not resolved; need human decision)', '']
    for o in res['duplicate_overrides_retained']:
        L.append(f"- Template duplicate kept by override: {o['a']} / {o['b']}. {o['reason']}")
    L.append(f"- {res['nonblocking_metadata']}")
    L.append(f"- {res['accepted_text_note']}")
    other_holds = [r for r in rows if r['status'] == 'hold' and r['section'] != 'Math']
    for r in other_holds:
        L.append(f"- On hold: {r['id']} ({r['exam']} {r['section']}): {r['status_reason'][:160]}")
    L.append(f"- ACT Math: {st['ACT Math']['pending_review']} records pending review and {st['ACT Math']['hold']} on hold; bulk generation paused, so these were not worked.")
    L.append('- ChatGPT overlay repairs (display and content) are applied in this package but the ChatGPT source files are unchanged; the owning workstream must adopt them.')
    L += ['', '## Completed checks versus outstanding work', '',
          '**Completed (AI only):** author self-check; two separate blind AI solves per verbal item (one adversarial with fact-checking) and one blind solve plus scripted recomputation per Claude math item; near-duplicate screens with independent AI adjudication; the final structural, evidence, passage, insertion, hint and duplicate audit. All solvers are AI agents of the same model family working from answer-free packets, so they are not truly independent of the author.', '',
          '**Outstanding:**',
          '- human review of every item (rights and originality, two human blind solves, content audit, fairness review, copy edit and accessibility check, named approval)',
          '- student calibration of difficulty and of the solver estimates above',
          '- human decisions on the open issues listed above',
          '- source adoption of the ChatGPT overlays', '',
          '## Files', '',
          '| File | Contents |', '|---|---|',
          '| `complete-bank.json` | Every reconciled record (all statuses), effective content version, key, explanation, provenance, content hash, difficulty and review evidence |',
          '| `review-packet-answer-free.json` | Reviewed drafts, student-facing fields only (ACT English: only the item\'s own span in [brackets]) |',
          '| `keys-and-explanations.json` | Keys, explanations, distractor rationales, hints, strategy, evidence, difficulty and review evidence for each reviewed draft |',
          '| `held-and-rejected.json` | Pending, held, reserved and retired records, plus Claude candidates that ended REVISE or REJECT and were never banked (with any later resubmission) |',
          '| `audits/` | Final audit, resolutions, duplicate screens and adjudications, insertion scan, retirements, overlays, fact correction, passage consistency, progress tracker, reconciled summary |',
          '| `manifest.json` | SHA-256 checksums |', '']
    (OUT / 'final-quality-coverage-report.md').write_text('\n'.join(L) + '\n', encoding='utf-8')

    files = sorted(p for p in OUT.rglob('*') if p.is_file())
    dump('manifest.json', dict(meta, counts={k: dict(st[k]) for k in ORDER}, never_banked_candidates=len(nb),
                               files={str(p.relative_to(OUT)): sha(p) for p in files}))
    ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(OUT.rglob('*')):
            if p.is_file():
                z.write(p, f'prep-and-price-final-reconciled-bank/{p.relative_to(OUT)}')
    shutil.copy(OUT / 'final-quality-coverage-report.md', ROOT / 'exports' / f'final-quality-coverage-report-{TODAY}.md')
    shutil.rmtree(OUT)  # the ZIP is the deliverable; the unpacked copy (~40 MB of JSON) is not kept in the repository
    print(ZIP, ZIP.stat().st_size, 'bytes;', len(rows), 'records;', len(reviewed), 'reviewed;', len(nb), 'never-banked candidates')


if __name__ == '__main__':
    main()
