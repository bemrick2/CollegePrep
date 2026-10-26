#!/usr/bin/env python3
"""Claude question-bank tool (Prep & Price, independent workstream).

Draft questions are reviewed batch by batch and only PASS items are appended to the cumulative bank.

    python3 question_bank/claude/tools/qb.py review act_math 1   # review draft batch 1, append PASS items
    python3 question_bank/claude/tools/qb.py export              # rebuild exports and progress.json
    python3 question_bank/claude/tools/qb.py audit act_math      # cross-batch duplicate and balance audit

A candidate passes only when all of these agree:
  * structural checks (four choices A-D, a rationale for every wrong choice, hints, explanation, enums);
  * the scripted computation in checks/<bank>/batch_NNN.py, which recomputes the answer from the stem's numbers
    and returns the matching choice letter without reading the key;
  * a blind solve by a separate reviewer that saw only the student-facing text (reviews/<bank>/batch-NNN.blind.json);
  * no blocking flag from the blind solver or the author's own review, and no near-duplicate in the bank, in the
    batch, in the supplied samples or in the app's fixture bank.
Anything else is REVISE (fixable) or REJECT. This is AI review only; nothing here is human-approved.

Saves are version-safe: the bank's version and hash are read before the review and checked again just before the
atomic replace, and every previously accepted record must survive byte-for-byte.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SCHEMA_VERSION = 'cld-qb/1.0'
AUTHOR = 'ai:claude'

BANKS = {
    'act_math': {'exam': 'ACT', 'section': 'Math', 'prefix': 'CLD-ACT-M-', 'family': 'act', 'repo_section': 'math'},
    'act_english': {'exam': 'ACT', 'section': 'English', 'prefix': 'CLD-ACT-E-', 'family': 'act', 'repo_section': 'english'},
    'act_reading': {'exam': 'ACT', 'section': 'Reading', 'prefix': 'CLD-ACT-R-', 'family': 'act', 'repo_section': 'reading'},
    'sat_reading_writing': {'exam': 'SAT', 'section': 'Reading and Writing', 'prefix': 'CLD-SAT-RW-', 'family': 'sat', 'repo_section': 'reading_writing'},
}
# Long-term targets from the assignment brief.
TARGETS = {'act_math': 2000, 'verbal_total': 2000}
DIFFICULTY_NUM = {'easy': 2, 'medium': 3, 'hard': 4}
DIFFICULTY_TARGET = {'easy': 0.25, 'medium': 0.50, 'hard': 0.25}
# Enhanced ACT (2025) math blueprint, midpoints of ACT's published ranges as summarised in search results
# (act.org itself was unreachable from the build environment; see README "Specification").
ACT_MATH_BLUEPRINT = {
    'Number & Quantity': 0.11, 'Algebra': 0.185, 'Functions': 0.185, 'Geometry': 0.185,
    'Statistics & Probability': 0.135, 'Integrating Essential Skills': 0.20,
}
REPO_SKILLS = {'act_algebra_linear', 'act_functions', 'act_geometry', 'act_statistics_probability', 'act_number_quantity'}
STRATEGY_KEYS = {'backsolve', 'plug_in_numbers', 'process_of_elimination', 'find_the_trend', 'translate_to_algebra', 'draw_it_out'}
TRAP_KEYS = {'partial_answer', 'wrong_quantity', 'sign_error', 'misread_graph', 'overextend_trend', None}
LETTERS = ['A', 'B', 'C', 'D']


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def read_json(p: Path, default=None):
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding='utf-8'))


def dumps(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2) + '\n'


def sha(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def atomic_write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=p.parent, prefix=f'.{p.name}.', suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def bank_path(bank: str) -> Path:
    return ROOT / 'banks' / f'{bank}.json'


def load_bank(bank: str) -> tuple[dict, str]:
    p = bank_path(bank)
    if not p.exists():
        meta = BANKS[bank]
        data = {'schema_version': SCHEMA_VERSION, 'bank': bank, 'exam': meta['exam'], 'section': meta['section'],
                'id_prefix': meta['prefix'], 'version': 0, 'updated_at': None, 'passages': [], 'questions': []}
        return data, ''
    text = p.read_text(encoding='utf-8')
    return json.loads(text), sha(text)


def save_bank(bank: str, data: dict, expected_hash: str, previous: dict) -> None:
    p = bank_path(bank)
    current = p.read_text(encoding='utf-8') if p.exists() else ''
    if (sha(current) if current else '') != expected_hash:
        sys.exit(f'refusing to save {p}: it changed since it was read (version-safe save)')
    old = {q['id']: json.dumps(q, sort_keys=True) for q in previous.get('questions', [])}
    new = {q['id']: json.dumps(q, sort_keys=True) for q in data['questions']}
    for qid, body in old.items():
        if new.get(qid) != body:
            sys.exit(f'refusing to save {p}: accepted record {qid} would be changed or removed')
    old_p = {x['passage_id']: json.dumps(x, sort_keys=True) for x in previous.get('passages', [])}
    for pid, body in old_p.items():
        if {x['passage_id']: json.dumps(x, sort_keys=True) for x in data['passages']}.get(pid) != body:
            sys.exit(f'refusing to save {p}: passage {pid} would be changed or removed')
    data['version'] = previous.get('version', 0) + 1
    data['updated_at'] = now()
    atomic_write(p, dumps(data))


# ---------------------------------------------------------------------------------------------------------------
# Duplicate screening
# ---------------------------------------------------------------------------------------------------------------

STOP = set('the a an of to and in is for what which if on be by with at as are that this its it from following value'.split())


def tokens(text: str) -> set[str]:
    t = re.sub(r'[^a-z0-9π√²³^/.]+', ' ', text.lower())
    return {w for w in t.split() if w not in STOP}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def reference_stems() -> list[tuple[str, str]]:
    """Stems the bank must not copy: the starter samples and the app's own fixture bank."""
    refs = []
    sample = ROOT / 'reference' / 'SAMPLE_QUESTIONS.json'
    for q in read_json(sample, []) or []:
        refs.append((q['id'], q['stem']))
    fx = REPO / 'web' / 'src' / 'lib' / 'data' / 'demo' / 'fixtures.ts'
    if fx.exists():
        for i, m in enumerate(re.finditer(r"stem:\s*\n?\s*'((?:[^'\\]|\\.)*)'", fx.read_text(encoding='utf-8'))):
            refs.append((f'fixture#{i + 1}', m.group(1)))
    return refs


def text_of(q: dict) -> str:
    return q['stem'] + ' ' + ' '.join(q['choices'].values())


DUP_THRESHOLD = 0.6


def near_duplicates(q: dict, others: list[tuple[str, str]]) -> list[dict]:
    mine = tokens(q['stem'])
    hits = []
    for oid, ostem in others:
        s = jaccard(mine, tokens(ostem))
        if s >= DUP_THRESHOLD:
            hits.append({'with': oid, 'similarity': round(s, 2)})
    return hits


# ---------------------------------------------------------------------------------------------------------------
# Review
# ---------------------------------------------------------------------------------------------------------------

def structural_problems(c: dict) -> list[str]:
    out = []
    for f in ['cand', 'skill', 'subskill', 'reporting_category', 'difficulty', 'stem', 'choices', 'answer', 'explanation',
              'distractors', 'hints', 'strategy', 'expected_time_seconds', 'repo_skill_key', 'remember']:
        if f not in c or c[f] in (None, '', [], {}):
            out.append(f'missing {f}')
    if out:
        return out
    if list(c['choices'].keys()) != LETTERS:
        out.append('choices must be exactly A-D in order')
    vals = [str(v).strip() for v in c['choices'].values()]
    if len(set(vals)) != 4 or any(not v for v in vals):
        out.append('choices must be four distinct, non-empty values')
    if c['answer'] not in LETTERS:
        out.append('answer must be A-D')
    wrong = [k for k in LETTERS if k != c['answer']]
    if sorted(c['distractors'].keys()) != wrong:
        out.append(f'distractor rationales must cover exactly {wrong}')
    for k, d in c['distractors'].items():
        if not d.get('rationale'):
            out.append(f'no rationale for {k}')
        if d.get('trap') not in TRAP_KEYS:
            out.append(f'unknown trap {d.get("trap")} for {k}')
    if c['difficulty'] not in DIFFICULTY_NUM:
        out.append('difficulty must be easy/medium/hard')
    if c['skill'] not in ACT_MATH_BLUEPRINT:
        out.append(f'unknown skill {c["skill"]}')
    if c['repo_skill_key'] not in REPO_SKILLS:
        out.append(f'unknown repo skill key {c["repo_skill_key"]}')
    if c['strategy'].get('key') not in STRATEGY_KEYS or not c['strategy'].get('explanation'):
        out.append('strategy needs a known key and an explanation')
    if not (10 <= int(c['expected_time_seconds']) <= 600):
        out.append('expected_time_seconds out of 10-600')
    if len(c['remember'].split()) > 16:
        out.append('remember is over 16 words')
    ans_text = c['choices'].get(c['answer'], '').strip()
    for h in c['hints']:
        if ans_text and re.search(r'(?<![\w.])' + re.escape(ans_text) + r'(?![\w.])', h):
            out.append(f'hint may give the answer away: {h!r}')
    return out


def load_checks(bank: str, n: int):
    p = ROOT / 'checks' / bank / f'batch_{n:03d}.py'
    spec = importlib.util.spec_from_file_location(f'checks_{bank}_{n}', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHECKS


def review(bank: str, n: int) -> None:
    meta = BANKS[bank]
    draft_p = ROOT / 'drafts' / bank / f'batch-{n:03d}.json'
    blind_p = ROOT / 'reviews' / bank / f'batch-{n:03d}.blind.json'
    review_p = ROOT / 'reviews' / bank / f'batch-{n:03d}.review.json'
    draft = read_json(draft_p)
    blind = read_json(blind_p)
    if draft is None or blind is None:
        sys.exit(f'need {draft_p} and {blind_p}')
    if read_json(review_p) and read_json(review_p).get('appended_ids'):
        sys.exit(f'batch {n} already appended to the bank; refusing to append twice')
    checks = load_checks(bank, n)
    data, h = load_bank(bank)
    previous = json.loads(json.dumps(data))
    refs = reference_stems()
    bank_refs = [(q['id'], q['stem']) for q in data['questions']]
    next_num = 1 + max([int(q['id'][len(meta['prefix']):]) for q in data['questions']] or [0])

    results, batch_refs = [], []
    for c in draft['candidates']:
        cand = c['cand']
        rec = {'cand': cand, 'revision': c.get('revision', 1), 'revision_history': c.get('revision_history', [])}
        probs = structural_problems(c)
        computed = None
        if cand in checks:
            try:
                computed = checks[cand](c['choices'])
            except Exception as e:  # noqa: BLE001
                probs.append(f'computation check raised {e!r}')
        else:
            probs.append('no computation check')
        b = (blind.get('answers') or {}).get(cand) or {}
        blind_ans = b.get('answer')
        dups = near_duplicates(c, bank_refs + refs + batch_refs)
        rec.update({
            'key': c.get('answer'),
            'computed_answer': computed,
            'blind_answer': blind_ans,
            'blind_confidence': b.get('confidence'),
            'blind_difficulty_opinion': b.get('difficulty_opinion'),
            'blind_flags': b.get('flags', []),
            'blind_notes': b.get('notes', ''),
            'author_checklist': c.get('author_checklist', {}),
            'structural_problems': probs,
            'near_duplicates': dups,
        })
        blocking_flags = [f for f in b.get('flags', []) if f and not str(f).lower().startswith('minor')]
        if c.get('author_status') == 'REJECT':
            status, reason = 'REJECT', c.get('author_reason', 'rejected by author review')
        elif dups and not c.get('dup_cleared'):
            status, reason = 'REJECT', 'near-duplicate'
        elif probs:
            status, reason = 'REVISE', '; '.join(probs)
        elif computed != c['answer']:
            status, reason = 'REVISE', f'computed answer {computed} disagrees with key {c["answer"]}'
        elif blind_ans != c['answer']:
            status, reason = 'REVISE', f'blind solver chose {blind_ans}, key is {c["answer"]}'
        elif blocking_flags:
            status, reason = 'REVISE', 'blind solver flagged: ' + '; '.join(map(str, blocking_flags))
        else:
            status, reason = 'PASS', 'key, independent computation and blind solve agree; no blocking flags'
        rec['status'], rec['reason'] = status, reason
        batch_refs.append((cand, c['stem']))
        if status == 'PASS':
            qid = f'{meta["prefix"]}{next_num:06d}'
            next_num += 1
            rec['id'] = qid
            data['questions'].append(to_record(c, qid, bank, n, rec, blind))
        results.append(rec)

    appended = [r['id'] for r in results if r['status'] == 'PASS']
    review_doc = {
        'schema_version': SCHEMA_VERSION, 'bank': bank, 'batch': n, 'reviewed_at': now(),
        'method': draft.get('review_method', REVIEW_METHOD),
        'blind_solver': blind.get('solver', {}),
        'counts': {s: sum(r['status'] == s for r in results) for s in ['PASS', 'REVISE', 'REJECT']},
        'appended_ids': appended,
        'results': results,
    }
    if appended:
        save_bank(bank, data, h, previous)
    atomic_write(review_p, dumps(review_doc))
    print(json.dumps(review_doc['counts']), 'appended:', ', '.join(appended) or 'none')
    for r in results:
        if r['status'] != 'PASS':
            print(f'  {r["cand"]}: {r["status"]} - {r["reason"]}')


REVIEW_METHOD = ('author self-check; scripted recomputation from the stem (checks/); blind solve by a separate AI '
                 'reviewer given only student-facing text; automated structure and near-duplicate screens')


def to_record(c: dict, qid: str, bank: str, n: int, rec: dict, blind: dict) -> dict:
    meta = BANKS[bank]
    return {
        'id': qid,
        'schema_version': SCHEMA_VERSION,
        'exam': meta['exam'],
        'section': meta['section'],
        'reporting_category': c['reporting_category'],
        'skill': c['skill'],
        'subskill': c['subskill'],
        'modeling': bool(c.get('modeling', False)),
        'repo_skill_key': c['repo_skill_key'],
        'passage_id': c.get('passage_id'),
        'figure': c.get('figure'),
        'stem': c['stem'],
        'choices': c['choices'],
        'correct_answer': c['answer'],
        'explanation': c['explanation'],
        'distractor_explanations': {k: v['rationale'] for k, v in c['distractors'].items()},
        'distractor_traps': {k: v.get('trap') for k, v in c['distractors'].items()},
        'hints': c['hints'],
        'strategy': c['strategy'],
        'remember': c['remember'],
        'expected_time_seconds': int(c['expected_time_seconds']),
        'calculator': c.get('calculator', 'allowed'),
        'difficulty': c['difficulty'],
        'difficulty_numeric': DIFFICULTY_NUM[c['difficulty']],
        'difficulty_basis': 'provisional editorial estimate; not statistically calibrated',
        'origin': 'ai_generated',
        'author': AUTHOR,
        'license': 'original-owned',
        'batch': n,
        'draft_candidate': c['cand'],
        'created_at': now(),
        'validation': {
            'status': 'PASS',
            'method': REVIEW_METHOD,
            'computed_answer': rec['computed_answer'],
            'blind_answer': rec['blind_answer'],
            'blind_confidence': rec['blind_confidence'],
            'blind_difficulty_opinion': rec['blind_difficulty_opinion'],
            'blind_flags': rec['blind_flags'],
            'revisions_before_pass': rec['revision'] - 1,
            'evidence': f'reviews/{bank}/batch-{n:03d}.review.json',
            'computation': f'checks/{bank}/batch_{n:03d}.py',
        },
        'review_status': 'ai_reviewed_pending_human',
        'human_review': None,
    }


# ---------------------------------------------------------------------------------------------------------------
# Exports and progress
# ---------------------------------------------------------------------------------------------------------------

def to_import(q: dict, bank: str) -> dict:
    """question_import/v1 line (docs/product/QUESTION_IMPORT_CONTRACT.md). Always a draft."""
    meta = BANKS[bank]
    return {
        'contract': 'question_import/v1',
        'import_id': q['id'].lower(),
        'exam_family': meta['family'],
        'section': meta['repo_section'],
        'difficulty': q['difficulty_numeric'],
        'stem': q['stem'],
        **({'passage': q['passage']} if q.get('passage') else {}),
        'choices': [{'key': k, 'text': v} for k, v in q['choices'].items()],
        'answer_format': 'choice',
        'accepted_answers': [q['correct_answer']],
        'expected_time_seconds': q['expected_time_seconds'],
        'primary_skill_key': q['repo_skill_key'],
        'hints': q['hints'],
        'teaching_explanation': q['explanation'],
        'strategy_explanation': q['strategy']['explanation'],
        'remember': q['remember'],
        'distractors': [{'choice': k, 'rationale': v, 'trap': q['distractor_traps'].get(k)}
                        for k, v in q['distractor_explanations'].items()],
        'strategies': [{'strategy_key': q['strategy']['key'], 'role': 'primary', 'is_fastest': True,
                        'explanation': q['strategy']['explanation']}],
        'origin': 'ai_drafted',
        'author': AUTHOR,
        'license': 'original-owned',
        'source_attribution': None,
        'source_url': None,
        'requested_pool': 'practice',
        'status': 'draft',
    }


def export() -> None:
    ex = ROOT / 'exports'
    files = {}
    for bank in BANKS:
        data, _ = load_bank(bank)
        if not bank_path(bank).exists():
            atomic_write(bank_path(bank), dumps(data))
        qs = data['questions']
        student = [{'id': q['id'], 'exam': q['exam'], 'section': q['section'], 'skill': q['skill'],
                    'subskill': q['subskill'], 'difficulty': q['difficulty'], 'passage_id': q.get('passage_id'),
                    'figure': q.get('figure'), 'stem': q['stem'], 'choices': q['choices']} for q in qs]
        answers = [{'id': q['id'], 'correct_answer': q['correct_answer'], 'explanation': q['explanation'],
                    'distractor_explanations': q['distractor_explanations'], 'hints': q['hints'],
                    'strategy': q['strategy']} for q in qs]
        passages = data.get('passages', [])
        sp = ex / f'{bank}.student.json'
        ap = ex / f'{bank}.answer_key.json'
        ip = ex / 'import' / f'{bank}.jsonl'
        atomic_write(sp, dumps({'bank': bank, 'bank_version': data['version'], 'note': 'Student-facing: no answers.',
                                'passages': passages, 'questions': student}))
        atomic_write(ap, dumps({'bank': bank, 'bank_version': data['version'], 'answers': answers}))
        atomic_write(ip, ''.join(json.dumps(to_import(q, bank), ensure_ascii=False) + '\n' for q in qs))
        files[bank] = {'bank': str(bank_path(bank).relative_to(ROOT)), 'bank_version': data['version'],
                       'student_export': str(sp.relative_to(ROOT)), 'answer_export': str(ap.relative_to(ROOT)),
                       'import_export': str(ip.relative_to(ROOT))}
    write_progress(files)


def dist(qs, key):
    out = {}
    for q in qs:
        out[q[key]] = out.get(q[key], 0) + 1
    return dict(sorted(out.items()))


def write_progress(files: dict) -> None:
    prev = read_json(ROOT / 'progress.json', {}) or {}
    sections, review_totals, batches = {}, {}, {}
    for bank in BANKS:
        data, _ = load_bank(bank)
        qs = data['questions']
        totals = {'PASS': 0, 'REVISE': 0, 'REJECT': 0, 'candidates': 0, 'passed_after_revision': 0}
        done = []
        for rp in sorted((ROOT / 'reviews' / bank).glob('batch-*.review.json')) if (ROOT / 'reviews' / bank).exists() else []:
            r = read_json(rp)
            done.append(r['batch'])
            for res in r['results']:
                totals['candidates'] += 1
                totals[res['status']] += 1
                if res['status'] == 'PASS' and res.get('revision', 1) > 1:
                    totals['passed_after_revision'] += 1
        review_totals[bank] = totals
        batches[bank] = max(done) if done else 0
        n = len(qs)
        sections[bank] = {
            'accepted': n,
            'by_skill': dist(qs, 'skill'),
            'by_subskill': dist(qs, 'subskill'),
            'by_difficulty': dist(qs, 'difficulty'),
            'difficulty_share': {k: round(v / n, 3) for k, v in dist(qs, 'difficulty').items()} if n else {},
            'modeling_items': sum(1 for q in qs if q.get('modeling')),
            'passages': len(data.get('passages', [])),
        }
    m = sections['act_math']
    gaps = {}
    if m['accepted']:
        for skill, share in ACT_MATH_BLUEPRINT.items():
            gaps[skill] = round(share * (m['accepted'] + 10) - m['by_skill'].get(skill, 0), 1)
    under = sorted([k for k, v in gaps.items() if v > 0.5], key=lambda k: -gaps[k])
    diff_gap = {k: round(t * (m['accepted'] + 10) - m['by_difficulty'].get(k, 0), 1) for k, t in DIFFICULTY_TARGET.items()}
    progress = {
        'schema_version': SCHEMA_VERSION,
        'updated_at': now(),
        'workstream': 'Claude independent question bank (draft; AI-reviewed only, no human approval)',
        'id_prefixes': {b: BANKS[b]['prefix'] for b in BANKS},
        'targets': TARGETS,
        'accepted_by_section': {b: sections[b]['accepted'] for b in BANKS},
        'review_totals': review_totals,
        'sections': sections,
        'last_completed_batch': batches,
        'next_batch_guidance': {
            'act_math': {
                'next_batch': batches['act_math'] + 1,
                'underrepresented_skills_vs_blueprint': under,
                'skill_gap_for_next_10': gaps,
                'difficulty_gap_for_next_10': diff_gap,
            },
        },
        'audits': prev.get('audits', []),
        'files': files,
        'next_recommended_work': prev.get('next_recommended_work', []),
        'execution_log': prev.get('execution_log', []),
        'human_review_status': 'none of the accepted items has had human editorial review',
    }
    atomic_write(ROOT / 'progress.json', dumps(progress))
    print(json.dumps(progress['accepted_by_section']), json.dumps(review_totals['act_math']))


def screen(bank: str, n: int) -> None:
    """Pre-review screen of a draft batch: structure, scripted check and near-duplicates. Writes nothing."""
    draft = read_json(ROOT / 'drafts' / bank / f'batch-{n:03d}.json')
    checks = load_checks(bank, n)
    data, _ = load_bank(bank)
    others = [(q['id'], q['stem']) for q in data['questions']] + reference_stems()
    seen = []
    for c in draft['candidates']:
        probs = structural_problems(c)
        try:
            got = checks[c['cand']](c['choices'])
        except Exception as e:  # noqa: BLE001
            got = f'error {e!r}'
        dups = near_duplicates(c, others + seen)
        seen.append((c['cand'], c['stem']))
        ok = not probs and got == c['answer'] and not dups
        print(f"{c['cand']} {'ok ' if ok else 'BAD'} key={c['answer']} computed={got} dups={dups} {probs or ''}")


def audit(bank: str) -> None:
    data, _ = load_bank(bank)
    qs = data['questions']
    pairs = []
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            s = jaccard(tokens(text_of(qs[i])), tokens(text_of(qs[j])))
            if s >= 0.45:
                pairs.append({'a': qs[i]['id'], 'b': qs[j]['id'], 'similarity': round(s, 2)})
    keys = dist([{'k': q['correct_answer']} for q in qs], 'k')
    report = {'bank': bank, 'audited_at': now(), 'accepted': len(qs), 'similar_pairs_ge_0_45': pairs,
              'answer_key_balance': keys, 'by_skill': dist(qs, 'skill'), 'by_difficulty': dist(qs, 'difficulty'),
              'subskills_used_more_than_twice': {k: v for k, v in dist(qs, 'subskill').items() if v > 2}}
    print(dumps(report))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'review':
        review(sys.argv[2], int(sys.argv[3]))
        export()
    elif cmd == 'screen':
        screen(sys.argv[2], int(sys.argv[3]))
    elif cmd == 'export':
        export()
    elif cmd == 'audit':
        audit(sys.argv[2])
    else:
        sys.exit(__doc__)
