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

import contextlib
import datetime as dt
import fcntl
import hashlib
import importlib.util
import json
import os
import re
import subprocess
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
    'sat_math': {'exam': 'SAT', 'section': 'Math', 'prefix': 'CLD-SAT-M-', 'family': 'sat', 'repo_section': 'math'},
}
# 2026-10-27 revision: targets are COMBINED ChatGPT + Claude bank totals (1,000 each for SAT Math, SAT R&W, ACT English
# and ACT Reading; ACT Math paused at its baseline). The combined baselines given by the user already include this
# workstream's export (774 / 262 / 219 / 263). The numbers below are this workstream's live-item targets: its live count
# plus the user's 'more needed' figure, less any items since held (SAT R&W 6, ACT English 1). The other workstream's
# additions are not visible here, so combined reconciliation is pending (see progress.json combined_tracking).
TARGETS = {'act_math': 774, 'act_english': 689, 'act_reading': 684, 'sat_reading_writing': 694, 'sat_math': 1000}
# SAT Math goes first until this checkpoint (counting this workstream's live SAT Math items; combined count pending).
FOCUS_BANK = 'sat_math'
FOCUS_CHECKPOINT = 500
# ACT Math: no bulk expansion; only targeted replacements or missing skills. Rotation covers these banks only.
GROWTH_BANKS = ('sat_math', 'sat_reading_writing', 'act_english', 'act_reading')
# ACT Math is worked first until this many are accepted; after that the bank furthest behind its target goes next.
MATH_FIRST_UNTIL = 200
WORKSTREAM_BRANCH = 'ccr-78c91309-anlh8e'
LOCK_FILE = 'LOCK.json'
LOCK_TTL_MINUTES = 120
DIFFICULTY_NUM = {'easy': 2, 'medium': 3, 'hard': 4}
DIFFICULTY_TARGET = {'easy': 0.25, 'medium': 0.50, 'hard': 0.25}
# Enhanced ACT (2025) math blueprint, midpoints of ACT's published ranges as summarised in search results
# (act.org itself was unreachable from the build environment; see README "Specification").
ACT_MATH_BLUEPRINT = {
    'Number & Quantity': 0.11, 'Algebra': 0.185, 'Functions': 0.185, 'Geometry': 0.185,
    'Statistics & Probability': 0.135, 'Integrating Essential Skills': 0.20,
}
REPO_SKILLS = {'act_algebra_linear', 'act_functions', 'act_geometry', 'act_statistics_probability', 'act_number_quantity'}
# Digital SAT Math domains and approximate shares (College Board: Algebra ~35%, Advanced Math ~35%,
# Problem-Solving and Data Analysis ~15%, Geometry and Trigonometry ~15%). Skill keys match web/src/lib/data/demo/fixtures.ts.
SAT_MATH_BLUEPRINT = {'Algebra': 0.35, 'Advanced Math': 0.35, 'Problem-Solving and Data Analysis': 0.15,
                      'Geometry and Trigonometry': 0.15}
SAT_MATH_REPO_SKILLS = {'Algebra': 'sat_algebra', 'Advanced Math': 'sat_advanced_math',
                        'Problem-Solving and Data Analysis': 'sat_problem_solving_data',
                        'Geometry and Trigonometry': 'sat_geometry_trig'}
# Student-produced responses (SAT grid-ins): about a quarter of SAT Math. Same shape the import validator accepts.
SPR_ANSWER = re.compile(r'^-?(\d+(\.\d+)?|\.\d+|\d+/\d+)$')


def math_blueprint(bank: str) -> dict:
    return SAT_MATH_BLUEPRINT if bank == 'sat_math' else ACT_MATH_BLUEPRINT


def math_repo_skills(bank: str) -> set:
    return set(SAT_MATH_REPO_SKILLS.values()) if bank == 'sat_math' else REPO_SKILLS


def num(s) -> 'Fraction | None':
    from fractions import Fraction
    try:
        return Fraction(str(s).strip().replace('−', '-'))
    except (ValueError, ZeroDivisionError):
        return None


def spr_match(given, accepted: list) -> bool:
    """A student-produced response matches if it equals an accepted answer exactly, or is a decimal of at least
    three places within 0.001 of one (the SAT accepts rounded or truncated decimals that fill the grid)."""
    g = num(given)
    if g is None:
        return False
    for a in accepted:
        v = num(a)
        if v is None:
            continue
        if g == v:
            return True
        gs = str(given).strip()
        if '.' in gs and len(gs.split('.')[1]) >= 3 and abs(g - v) < num('0.001'):
            return True
    return False
STRATEGY_KEYS = {'backsolve', 'plug_in_numbers', 'process_of_elimination', 'find_the_trend', 'translate_to_algebra', 'draw_it_out'}
TRAP_KEYS = {'partial_answer', 'wrong_quantity', 'sign_error', 'misread_graph', 'overextend_trend', None}
VERBAL = {'act_english', 'act_reading', 'sat_reading_writing'}
# Reporting-category weights (midpoints). ACT: enhanced-ACT FAQ figures as summarised by search (act.org itself was
# unreachable); SAT: digital SAT Reading and Writing domain shares. Verify against the official pages before relying on them.
VERBAL_BLUEPRINT = {
    'act_english': {'Production of Writing': 0.405, 'Knowledge of Language': 0.205, 'Conventions of Standard English': 0.405},
    'act_reading': {'Key Ideas and Details': 0.48, 'Craft and Structure': 0.295, 'Integration of Knowledge and Ideas': 0.225},
    'sat_reading_writing': {'Craft and Structure': 0.28, 'Information and Ideas': 0.26, 'Standard English Conventions': 0.26,
                            'Expression of Ideas': 0.20},
}
VERBAL_REPO_SKILLS = {
    'act_english': {'act_punctuation', 'act_sentence_structure', 'act_usage', 'act_rhetorical_skills'},
    'act_reading': {'act_main_idea', 'act_inference', 'act_vocabulary_in_context', 'act_author_purpose'},
    'sat_reading_writing': {'sat_craft_structure', 'sat_information_ideas', 'sat_standard_english', 'sat_expression_of_ideas'},
}
VERBAL_STRATEGY_KEYS = {'predict_then_match', 'process_of_elimination', 'read_question_first', 'concise_is_correct', 'locate_evidence'}
VERBAL_TRAP_KEYS = {'extreme_language', 'true_but_irrelevant', 'out_of_scope', 'wordy_redundant', 'comma_splice', 'wrong_transition',
                    'misplaced_modifier', 'nearest_noun_agreement', 'familiar_meaning', 'partial_answer', 'wrong_quantity', None}
UNDERLINE = re.compile(r'\{\{(\d+)\|([^}]*)\}\}')


def plain(template: str) -> str:
    """Passage text with underline markup removed."""
    return UNDERLINE.sub(lambda m: m.group(2), template)


def render(template: str, n: int | None) -> str:
    """The app's convention (fixtures.ts underline()): only underline n is shown, in brackets."""
    return UNDERLINE.sub(lambda m: f'[{m.group(2)}]' if n is not None and int(m.group(1)) == n else m.group(2), template)


def norm_ws(t: str) -> str:
    return re.sub(r'\s+', ' ', t.replace('’', "'").replace('“', '"').replace('”', '"')).strip()
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


SUPERSCRIPTS = str.maketrans('⁰¹⁴⁵⁶⁷⁸⁹⁻', '01456789-')


def tokens(text: str) -> set[str]:
    # Superscript exponents other than ² and ³ were dropped, so 7¹⁰⁰ and 7^100 looked unrelated; map them to digits.
    t = re.sub(r'[^a-z0-9π√²³^/.]+', ' ', text.translate(SUPERSCRIPTS).lower())
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
    return q['stem'] + ' ' + ' '.join((q.get('choices') or {}).values())


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

def structural_problems(c: dict, bank: str = 'act_math', passages: dict | None = None) -> list[str]:
    out = []
    verbal = bank in VERBAL
    spr = c.get('format') == 'spr'
    if spr:
        return spr_problems(c, bank)
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
    traps = VERBAL_TRAP_KEYS if verbal else TRAP_KEYS
    for k, d in c['distractors'].items():
        if not d.get('rationale'):
            out.append(f'no rationale for {k}')
        if d.get('trap') not in traps:
            out.append(f'unknown trap {d.get("trap")} for {k}')
    if c['difficulty'] not in DIFFICULTY_NUM:
        out.append('difficulty must be easy/medium/hard')
    skills = VERBAL_BLUEPRINT[bank] if verbal else math_blueprint(bank)
    if c['skill'] not in skills:
        out.append(f'unknown skill {c["skill"]}')
    if bank == 'sat_math' and c['repo_skill_key'] != SAT_MATH_REPO_SKILLS.get(c['skill']):
        out.append(f'SAT Math skill {c["skill"]} needs repo skill key {SAT_MATH_REPO_SKILLS.get(c["skill"])}')
    if c['repo_skill_key'] not in (VERBAL_REPO_SKILLS[bank] if verbal else math_repo_skills(bank)):
        out.append(f'unknown repo skill key {c["repo_skill_key"]}')
    if c['strategy'].get('key') not in (VERBAL_STRATEGY_KEYS if verbal else STRATEGY_KEYS) or not c['strategy'].get('explanation'):
        out.append('strategy needs a known key and an explanation')
    if verbal:
        pas = (passages or {}).get(c.get('passage_id'))
        if not pas:
            out.append('verbal item needs a passage_id defined in the draft passages')
        else:
            if not c.get('evidence') or norm_ws(c['evidence']) not in norm_ws(plain(pas['text'])):
                out.append('evidence must be a verbatim quote from the passage')
            if bank == 'act_english':
                nums = {int(m.group(1)) for m in UNDERLINE.finditer(pas['text'])}
                if c.get('underline') not in nums and not c.get('essay_level'):
                    out.append('ACT English item needs an underline number that exists in its passage (or essay_level: true)')
                # A choice ending in the same mark that already follows the underlined span renders a doubled mark.
                m = re.search(r'\{\{%s\|[^}]*\}\}([.,;:!?])' % c.get('underline'), pas['text']) if c.get('underline') else None
                if m and any(v.rstrip().endswith(m.group(1)) for v in c['choices'].values()
                             if v not in ('NO CHANGE', 'DELETE the underlined portion.')):
                    out.append(f'a choice ends with "{m.group(1)}", which already follows the underlined span')
    if not (10 <= int(c['expected_time_seconds']) <= 600):
        out.append('expected_time_seconds out of 10-600')
    if len(c['remember'].split()) > 16:
        out.append('remember is over 16 words')
    ans_text = c['choices'].get(c['answer'], '').strip()
    for h in c['hints']:
        if ans_text and re.search(r'(?<![\w.])' + re.escape(ans_text) + r'(?![\w.])', h):
            out.append(f'hint may give the answer away: {h!r}')
    return out


def spr_problems(c: dict, bank: str) -> list[str]:
    """Structure of a student-produced-response item: no choices; a canonical answer plus every accepted spelling,
    each short enough for the SAT grid (5 characters for a positive answer, 6 with a minus sign); and at least one
    common wrong value with its rationale, which stands in for distractor rationales."""
    out = []
    if bank != 'sat_math':
        return ['student-produced responses are only used in the SAT Math bank']
    for f in ['cand', 'skill', 'subskill', 'reporting_category', 'difficulty', 'stem', 'answer', 'accepted_answers',
              'explanation', 'common_errors', 'hints', 'strategy', 'expected_time_seconds', 'repo_skill_key', 'remember']:
        if f not in c or c[f] in (None, '', [], {}):
            out.append(f'missing {f}')
    if out:
        return out
    if c.get('choices'):
        out.append('a student-produced response has no choices')
    if not isinstance(c['answer'], str) or not all(isinstance(a, str) for a in c['accepted_answers']):
        out.append('answer and accepted_answers must be strings')
    acc = [str(a) for a in c['accepted_answers']]
    if str(c['answer']) not in acc:
        out.append('the canonical answer must be one of accepted_answers')
    for a in acc:
        if not SPR_ANSWER.match(a):
            out.append(f'accepted answer {a!r} is not a plain number or fraction')
        if len(a) > (6 if a.startswith('-') else 5):
            out.append(f'accepted answer {a!r} does not fit the SAT grid')
        if num(a) is None or num(a) != num(acc[0]) and not spr_match(a, [acc[0]]):
            out.append(f'accepted answer {a!r} is not equivalent to {acc[0]!r}')
    for e in c['common_errors']:
        if not e.get('value') or not e.get('rationale') or e.get('trap') not in TRAP_KEYS:
            out.append('each common error needs a value, a rationale and a known trap key')
        elif spr_match(e['value'], acc):
            out.append(f'common error {e["value"]} equals the answer')
    if c['difficulty'] not in DIFFICULTY_NUM:
        out.append('difficulty must be easy/medium/hard')
    if c['skill'] not in SAT_MATH_BLUEPRINT:
        out.append(f'unknown skill {c["skill"]}')
    elif c['repo_skill_key'] != SAT_MATH_REPO_SKILLS[c['skill']]:
        out.append(f'SAT Math skill {c["skill"]} needs repo skill key {SAT_MATH_REPO_SKILLS[c["skill"]]}')
    if c['strategy'].get('key') not in STRATEGY_KEYS or not c['strategy'].get('explanation'):
        out.append('strategy needs a known key and an explanation')
    if not (10 <= int(c['expected_time_seconds']) <= 600):
        out.append('expected_time_seconds out of 10-600')
    if len(c['remember'].split()) > 16:
        out.append('remember is over 16 words')
    for h in c['hints']:
        for a in acc:
            if re.search(r'(?<![\w./])' + re.escape(a) + r'(?![\w./])', h):
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
    verbal = bank in VERBAL
    checks = {} if verbal else load_checks(bank, n)
    passages = {x['passage_id']: x for x in draft.get('passages', [])}
    blind2 = read_json(ROOT / 'reviews' / bank / f'batch-{n:03d}.blind2.json') if verbal else None
    if verbal and blind2 is None:
        sys.exit('verbal batches need a second independent blind solve: reviews/<bank>/batch-NNN.blind2.json')
    data, h = load_bank(bank)
    if any(q.get('batch') == n for q in data['questions']):
        sys.exit(f'bank already holds records from batch {n}; refusing to append twice (rebuild the review file by hand if it is missing)')
    accepted_before = len(data['questions'])
    previous = json.loads(json.dumps(data))
    refs = [] if verbal else reference_stems()
    bank_refs = [(q['id'], qtext(q, bank)) for q in data['questions']]
    if bank == 'sat_math':
        bank_refs += [(q['id'], qtext(q, 'act_math')) for q in live(load_bank('act_math')[0]['questions'])]
    passage_dups = {}
    if verbal:
        others = [(x['passage_id'], plain(x['text'])) for x in data.get('passages', [])] + reference_passages()
        for pid, x in passages.items():
            mine = tokens(plain(x['text']))
            hits = [{'with': oid, 'similarity': round(jaccard(mine, tokens(t)), 2)} for oid, t in others
                    if oid != pid and jaccard(mine, tokens(t)) >= 0.5]
            if hits:
                passage_dups[pid] = hits
    next_num = 1 + max([int(q['id'][len(meta['prefix']):]) for q in data['questions']] or [0])

    results, batch_refs = [], []
    for c in draft['candidates']:
        cand = c['cand']
        rec = {'cand': cand, 'revision': c.get('revision', 1), 'revision_history': c.get('revision_history', [])}
        probs = structural_problems(c, bank, passages)
        computed = None
        if verbal:
            # No arithmetic to recompute: the 'computed' slot records that the cited evidence is verbatim in the passage.
            computed = c['answer'] if not probs else None
        elif cand in checks:
            try:
                if c.get('format') == 'spr':
                    v = checks[cand](None)
                    computed = str(c['answer']) if spr_match(str(v), c['accepted_answers']) or num(v) == num(c['answer']) else str(v)
                else:
                    computed = checks[cand](c['choices'])
            except Exception as e:  # noqa: BLE001
                probs.append(f'computation check raised {e!r}')
        else:
            probs.append('no computation check')
        b = (blind.get('answers') or {}).get(cand) or {}
        blind_ans = b.get('answer')
        if c.get('format') == 'spr' and blind_ans is not None and spr_match(str(blind_ans), c['accepted_answers']):
            blind_ans = str(c['answer'])
        b2 = ((blind2 or {}).get('answers') or {}).get(cand) or {}
        dups = near_duplicates({'stem': qtext(c, bank)}, bank_refs + refs + batch_refs)
        if verbal and c.get('passage_id') in passage_dups:
            dups = dups + [{'passage': c['passage_id'], 'matches': passage_dups[c['passage_id']]}]
        rec.update({
            'key': c.get('answer'),
            'computed_answer': computed,
            'blind_answer': blind_ans,
            'blind_confidence': b.get('confidence'),
            'blind_difficulty_opinion': b.get('difficulty_opinion'),
            'blind_est_pct_correct': b.get('est_pct_correct'),
            'blind_flags': b.get('flags', []),
            'blind_notes': b.get('notes', ''),
            **({'blind2_answer': b2.get('answer'), 'blind2_flags': b2.get('flags', []),
                'blind2_difficulty_opinion': b2.get('difficulty_opinion')} if verbal else {}),
            'author_checklist': c.get('author_checklist', {}),
            'structural_problems': probs,
            'near_duplicates': dups,
        })
        blocking_flags = [f for f in b.get('flags', []) + (b2.get('flags', []) if verbal else [])
                          if f and not str(f).lower().startswith('minor')]
        if c.get('author_status') == 'REJECT':
            status, reason = 'REJECT', c.get('author_reason', 'rejected by author review')
        elif dups and not c.get('dup_cleared'):
            status, reason = 'REJECT', 'near-duplicate'
        elif probs:
            status, reason = 'REVISE', '; '.join(probs)
        elif computed != str(c['answer']) if c.get('format') == 'spr' else computed != c['answer']:
            status, reason = 'REVISE', f'computed answer {computed} disagrees with key {c["answer"]}'
        elif blind_ans != c['answer']:
            status, reason = 'REVISE', f'blind solver chose {blind_ans}, key is {c["answer"]}'
        elif verbal and b2.get('answer') != c['answer']:
            status, reason = 'REVISE', f'second blind solver chose {b2.get("answer")}, key is {c["answer"]}'
        elif blocking_flags:
            status, reason = 'REVISE', 'blind solver flagged: ' + '; '.join(map(str, blocking_flags))
        elif c['difficulty'] == 'hard' and b.get('difficulty_opinion') == 'easy':
            status, reason = 'REVISE', 'labelled hard but the rubric rater judged it easy; make it genuinely hard or relabel'
        else:
            status, reason = 'PASS', 'key, independent computation and blind solve agree; no blocking flags'
        rec['status'], rec['reason'] = status, reason
        batch_refs.append((cand, qtext(c, bank)))
        if status == 'PASS':
            qid = f'{meta["prefix"]}{next_num:06d}'
            next_num += 1
            rec['id'] = qid
            data['questions'].append(to_record(c, qid, bank, n, rec, blind))
            pid = c.get('passage_id')
            if pid and pid not in {x['passage_id'] for x in data['passages']}:
                data['passages'].append({**passages[pid], 'batch': n, 'origin': 'ai_generated', 'author': AUTHOR,
                                         'license': 'original-owned'})
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
    if len(data['questions']) // 100 > accepted_before // 100:
        record_audit(bank, audit(bank, quiet=True))
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
        'underline': c.get('underline'),
        'evidence': c.get('evidence'),
        'figure': c.get('figure'),
        'stem': c['stem'],
        'answer_format': 'numeric' if c.get('format') == 'spr' else 'choice',
        'choices': None if c.get('format') == 'spr' else c['choices'],
        'correct_answer': str(c['answer']) if c.get('format') == 'spr' else c['answer'],
        **({'accepted_answers': [str(a) for a in c['accepted_answers']], 'common_errors': c['common_errors']}
           if c.get('format') == 'spr' else {}),
        'explanation': c['explanation'],
        'distractor_explanations': {} if c.get('format') == 'spr' else {k: v['rationale'] for k, v in c['distractors'].items()},
        'distractor_traps': {} if c.get('format') == 'spr' else {k: v.get('trap') for k, v in c['distractors'].items()},
        'hints': c['hints'],
        'strategy': c['strategy'],
        'remember': c['remember'],
        'expected_time_seconds': int(c['expected_time_seconds']),
        'calculator': c.get('calculator', 'allowed'),
        'difficulty': c['difficulty'],
        'difficulty_numeric': DIFFICULTY_NUM[c['difficulty']],
        'difficulty_basis': 'provisional editorial estimate; not statistically calibrated',
        'difficulty_calibrated': rec['blind_difficulty_opinion'] or c['difficulty'],
        'difficulty_calibration_basis': 'rubric rating by the blind solver (est. share of typical test-takers correct); AI estimate, not student data',
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
            'blind_est_pct_correct': rec.get('blind_est_pct_correct'),
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

_CAL: dict = {}


def calibrated(q: dict, bank: str) -> str:
    """Calibrated difficulty: a recorded re-assessment (calibration/<bank>.json) wins, then the rating stored at
    acceptance, then the author's label. The accepted record itself is never edited."""
    if bank not in _CAL:
        _CAL[bank] = (read_json(ROOT / 'calibration' / f'{bank}.json', {}) or {}).get('items', {})
    if q['id'] in _CAL[bank]:
        return _CAL[bank][q['id']]['calibrated']
    return q.get('difficulty_calibrated') or q['difficulty']


def qtext(q: dict, bank: str) -> str:
    """Text compared for duplicates: math stems alone; verbal stems share wording, so add choices and the span."""
    if bank not in VERBAL:
        return q['stem']
    return ' '.join([q['stem'], *(q.get('choices') or {}).values(), str(q.get('evidence') or '')])


def reference_passages() -> list[tuple[str, str]]:
    fx = REPO / 'web' / 'src' / 'lib' / 'data' / 'demo' / 'fixtures.ts'
    if not fx.exists():
        return []
    out = []
    for m in re.finditer(r'const ((?:EN|RD)_\w+) =\s*\n?\s*"((?:[^"\\]|\\.)*)"', fx.read_text(encoding='utf-8')):
        out.append((f'fixture:{m.group(1)}', plain(m.group(2))))
    return out


_PASSAGES: dict = {}


def passage_text(q: dict, bank: str) -> str | None:
    if not q.get('passage_id'):
        return None
    if bank not in _PASSAGES:
        _PASSAGES[bank] = {x['passage_id']: x for x in load_bank(bank)[0].get('passages', [])}
    t = _PASSAGES[bank][q['passage_id']]['text']
    return render(t, q.get('underline')) if bank == 'act_english' else plain(t)


def to_import(q: dict, bank: str) -> dict:
    """question_import/v1 line (docs/product/QUESTION_IMPORT_CONTRACT.md). Always a draft."""
    meta = BANKS[bank]
    q = {**q, 'passage': passage_text(q, bank)}
    return {
        'contract': 'question_import/v1',
        'import_id': q['id'].lower(),
        'exam_family': meta['family'],
        'section': meta['repo_section'],
        'difficulty': DIFFICULTY_NUM[calibrated(q, bank)],
        'stem': q['stem'],
        **({'passage': q['passage']} if q.get('passage') else {}),
        **({'choices': [{'key': k, 'text': v} for k, v in q['choices'].items()]} if q.get('choices') else {}),
        'answer_format': q.get('answer_format', 'choice'),
        'accepted_answers': q.get('accepted_answers') or [q['correct_answer']],
        'expected_time_seconds': q['expected_time_seconds'],
        'primary_skill_key': q['repo_skill_key'],
        'hints': q['hints'],
        'teaching_explanation': q['explanation'],
        'strategy_explanation': q['strategy']['explanation'],
        'remember': q['remember'],
        **({'distractors': [{'choice': k, 'rationale': v, 'trap': q['distractor_traps'].get(k)}
                            for k, v in q['distractor_explanations'].items()]} if q.get('choices') else {}),
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


def retired_ids() -> dict:
    """Accepted items later found to repeat another item's concept (audits/retired.json). Bank records stay
    unchanged (append-only); retired items are left out of exports and accepted counts."""
    return (read_json(ROOT / 'audits' / 'retired.json', {}) or {}).get('retired', {})


def live(qs: list) -> list:
    gone = retired_ids()
    return [q for q in qs if q['id'] not in gone]


def export() -> None:
    ex = ROOT / 'exports'
    files = {}
    for bank in BANKS:
        data, _ = load_bank(bank)
        if not bank_path(bank).exists():
            atomic_write(bank_path(bank), dumps(data))
        qs = live(data['questions'])
        student = [{'id': q['id'], 'exam': q['exam'], 'section': q['section'], 'skill': q['skill'],
                    'subskill': q['subskill'], 'difficulty': q['difficulty'], 'passage_id': q.get('passage_id'),
                    'underline': q.get('underline'),
                    'figure': q.get('figure'), 'stem': q['stem'], 'answer_format': q.get('answer_format', 'choice'),
                    'choices': q.get('choices')} for q in qs]
        answers = [{'id': q['id'], 'correct_answer': q['correct_answer'],
                    **({'accepted_answers': q['accepted_answers'], 'common_errors': q.get('common_errors')}
                       if q.get('accepted_answers') else {}),
                    'explanation': q['explanation'],
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
        qs = live(data['questions'])
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
            'retired_after_audit': len(data['questions']) - n,
            'by_skill': dist(qs, 'skill'),
            'by_subskill': dist(qs, 'subskill'),
            'by_difficulty_author': dist(qs, 'difficulty'),
            'by_difficulty_calibrated': dist([{'d': calibrated(q, bank)} for q in qs], 'd'),
            'calibrated_share': {k: round(v / n, 3) for k, v in dist([{'d': calibrated(q, bank)} for q in qs], 'd').items()} if n else {},
            'answer_key_balance': dist([{'k': q['correct_answer']} for q in qs], 'k'),
            'modeling_items': sum(1 for q in qs if q.get('modeling')),
            'spr_items': sum(1 for q in qs if q.get('answer_format') == 'numeric'),
            'passages': len(data.get('passages', [])),
        }
    m = sections['act_math']
    gaps = {}
    if m['accepted']:
        for skill, share in ACT_MATH_BLUEPRINT.items():
            gaps[skill] = round(share * (m['accepted'] + 10) - m['by_skill'].get(skill, 0), 1)
    under = sorted([k for k, v in gaps.items() if v > 0.5], key=lambda k: -gaps[k])
    diff_gap = {k: round(t * (m['accepted'] + 10) - m['by_difficulty_calibrated'].get(k, 0), 1) for k, t in DIFFICULTY_TARGET.items()}
    keys = m['answer_key_balance']
    key_gap = {k: round((m['accepted'] + 10) / 4 - keys.get(k, 0), 1) for k in LETTERS}
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
                'calibrated_difficulty_gap_for_next_10': diff_gap,
                'answer_key_gap_for_next_10': key_gap,
            },
        },
        'sat_math_guidance': sat_math_guidance(sections['sat_math'], batches['sat_math']),
        'verbal_guidance': {b: {'next_batch': batches[b] + 1,
                                'skill_gap_for_next_10': {k: round(v * (sections[b]['accepted'] + 10) - sections[b]['by_skill'].get(k, 0), 1)
                                                          for k, v in VERBAL_BLUEPRINT[b].items()}} for b in VERBAL},
        'section_targets': {b: {'target': TARGETS[b], 'accepted': sections[b]['accepted'],
                                'share_of_target': round(sections[b]['accepted'] / TARGETS[b], 3)} for b in BANKS},
        'total_target': sum(TARGETS.values()),
        'total_accepted': sum(sections[b]['accepted'] for b in BANKS),
        'next_bank_policy': f'{FOCUS_BANK} until {FOCUS_CHECKPOINT} live items; then whichever of {", ".join(GROWTH_BANKS)} has the lowest share of its target. ACT Math: no bulk expansion.',
        'next_bank': next_bank({b: sections[b]['accepted'] for b in BANKS}),
        'audits': prev.get('audits', []),
        'files': files,
        'next_recommended_work': prev.get('next_recommended_work', []),
        'calibration_notes': prev.get('calibration_notes', []),
        'lock': read_json(ROOT / LOCK_FILE, None),
        'execution_log': prev.get('execution_log', []),
        'human_review_status': 'none of the accepted items has had human editorial review',
    }
    atomic_write(ROOT / 'progress.json', dumps(progress))
    print(json.dumps(progress['accepted_by_section']), json.dumps(review_totals['act_math']))


def sat_math_guidance(m: dict, last_batch: int) -> dict:
    n = m['accepted']
    return {'next_batch': last_batch + 1, 'target': TARGETS['sat_math'], 'checkpoint': FOCUS_CHECKPOINT,
            'skill_gap_for_next_10': {k: round(v * (n + 10) - m['by_skill'].get(k, 0), 1) for k, v in SAT_MATH_BLUEPRINT.items()},
            'calibrated_difficulty_gap_for_next_10': {k: round(t * (n + 10) - m['by_difficulty_calibrated'].get(k, 0), 1)
                                                      for k, t in DIFFICULTY_TARGET.items()},
            'answer_key_gap_for_next_10': {k: round((n + 10) * 0.75 / 4 - m['answer_key_balance'].get(k, 0), 1) for k in LETTERS},
            'spr_items': m.get('spr_items', 0), 'spr_target_share': 0.25}


def screen(bank: str, n: int) -> None:
    """Pre-review screen of a draft batch: structure, scripted check and near-duplicates. Writes nothing."""
    draft = read_json(ROOT / 'drafts' / bank / f'batch-{n:03d}.json')
    verbal = bank in VERBAL
    checks = {} if verbal else load_checks(bank, n)
    passages = {x['passage_id']: x for x in draft.get('passages', [])}
    data, _ = load_bank(bank)
    others = [(q['id'], qtext(q, bank)) for q in data['questions']] + ([] if verbal else reference_stems())
    if bank == 'sat_math':
        others += [(q['id'], qtext(q, 'act_math')) for q in live(load_bank('act_math')[0]['questions'])]
    if verbal:
        po = [(x['passage_id'], plain(x['text'])) for x in data.get('passages', [])] + reference_passages()
        for pid, x in passages.items():
            hits = [(oid, round(jaccard(tokens(plain(x['text'])), tokens(t)), 2)) for oid, t in po
                    if oid != pid and jaccard(tokens(plain(x['text'])), tokens(t)) >= 0.5]
            print(f'passage {pid}: {len(plain(x["text"]).split())} words, near-duplicates {hits}')
    seen = []
    for c in draft['candidates']:
        probs = structural_problems(c, bank, passages)
        if verbal:
            got = c['answer'] if not probs else 'evidence/structure problem'
        else:
            try:
                if c.get('format') == 'spr':
                    v = checks[c['cand']](None)
                    got = str(c['answer']) if spr_match(str(v), c['accepted_answers']) or num(v) == num(c['answer']) else str(v)
                else:
                    got = checks[c['cand']](c['choices'])
            except Exception as e:  # noqa: BLE001
                got = f'error {e!r}'
        dups = near_duplicates({'stem': qtext(c, bank)}, others + seen)
        seen.append((c['cand'], qtext(c, bank)))
        ok = not probs and got == str(c['answer']) and not dups
        print(f"{c['cand']} {'ok ' if ok else 'BAD'} key={c['answer']} computed={got} dups={dups} {probs or ''}")
        # Advisory (math): the stem-only screen missed reworded repeats such as 7^2026 vs 7¹⁰⁰ (superscripts are dropped
        # by tokens()), so also compare stem + choices, as the 100-item audit does, at a lower threshold.
        if not verbal:
            mine = tokens(text_of(c))
            pool = data['questions'] + (load_bank('act_math')[0]['questions'] if bank == 'sat_math' else [])
            close = sorted(((round(jaccard(mine, tokens(text_of(q))), 2), q['id']) for q in pool
                            if q['id'] not in retired_ids()), reverse=True)
            close = [(i, s) for s, i in close if s >= 0.45][:3]
            if close:
                print(f"  warn: stem+choices close to {close} (compare by hand for a concept repeat)")
        # Advisory: the text screen misses concept-level repeats (same idea, new wording), so flag a subskill that is
        # already in the bank or overlaps an existing one heavily; check that item by hand before review.
        sub = tokens(c.get('subskill', ''))
        twins = sorted({q['subskill'] for q in data['questions'] + (load_bank('act_math')[0]['questions'] if bank == 'sat_math' else [])
                        if q.get('subskill') and sub and jaccard(sub, tokens(q['subskill'])) >= 0.6})
        if twins:
            print(f"  warn: subskill overlaps existing bank subskills {twins[:3]} (check for a concept repeat)")
        # SAT Math (and the ACT) list purely numeric choices from least to greatest.
        if bank == 'sat_math' and c.get('choices'):
            vals = [num(v.replace(',', '').replace('$', '').replace('%', '').replace('°', '')) for v in c['choices'].values()]
            if all(v is not None for v in vals) and vals != sorted(vals):
                print("  BAD: numeric choices must be in ascending order (SAT convention)")
        # Advisory only: blind solvers repeatedly flag a key that is clearly the longest choice as a test-wise tell.
        lens = {k: len(v) for k, v in (c.get('choices') or {}).items() if v not in ('NO CHANGE', 'DELETE the underlined portion.')}
        if verbal and c['answer'] in lens and len(lens) > 2:
            rest = max(v for k, v in lens.items() if k != c['answer'])
            if lens[c['answer']] > 1.15 * rest:
                print(f"  warn: key is the longest choice by {lens[c['answer']] - rest} characters (length cue)")


def next_bank(accepted: dict) -> str:
    if FOCUS_BANK and accepted.get(FOCUS_BANK, 0) < FOCUS_CHECKPOINT:
        return FOCUS_BANK
    return min(GROWTH_BANKS, key=lambda b: (accepted[b] / TARGETS[b], b))


def record_audit(bank: str, report: dict) -> None:
    p = read_json(ROOT / 'progress.json', {}) or {}
    p.setdefault('audits', []).append(report)
    atomic_write(ROOT / 'progress.json', dumps(p))


def audit(bank: str, quiet: bool = False) -> dict:
    data, _ = load_bank(bank)
    qs = data['questions']
    pairs = []
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            s = jaccard(tokens(text_of(qs[i])), tokens(text_of(qs[j])))
            if s >= 0.45:
                pairs.append({'a': qs[i]['id'], 'b': qs[j]['id'], 'similarity': round(s, 2)})
    keys = dist([{'k': q['correct_answer']} for q in qs], 'k')
    thin = [q['id'] for q in qs if len(q['explanation']) < 80
            or any(len(r) < 25 for r in q['distractor_explanations'].values()) or not q.get('hints')]
    report = {'bank': bank, 'audited_at': now(), 'accepted': len(qs), 'similar_pairs_ge_0_45': pairs,
              'answer_key_balance': keys, 'by_skill': dist(qs, 'skill'),
              'by_difficulty_author': dist(qs, 'difficulty'),
              'by_difficulty_calibrated': dist([{'d': calibrated(q, bank)} for q in qs], 'd'),
              'thin_explanations': thin,
              'subskills_used_more_than_twice': {k: v for k, v in dist(qs, 'subskill').items() if v > 2},
              'scope': f'automatic audit at {len(qs)} accepted'}
    if not quiet:
        print(dumps(report))
    return report


# ---------------------------------------------------------------------------------------------------------------
# Single-writer lock. The lease lives in LOCK.json on the workstream branch, so it holds across containers and
# sessions: taking it is a commit that must fast-forward the remote branch, so of two racing workers only one push
# wins. A local flock stops two processes in one container from writing at once.
# ---------------------------------------------------------------------------------------------------------------

def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(['git', '-C', str(REPO), *args], capture_output=True, text=True, check=check)


def push_with_retry() -> bool:
    import time
    for wait in (0, 2, 4, 8, 16):
        time.sleep(wait)
        r = git('push', 'origin', f'HEAD:{WORKSTREAM_BRANCH}', check=False)
        if r.returncode == 0:
            return True
        if 'rejected' in r.stderr or 'non-fast-forward' in r.stderr or 'fetch first' in r.stderr:
            return False  # someone else moved the branch: never retry over them
    return False


def sync_branch() -> None:
    if git('rev-parse', '--abbrev-ref', 'HEAD').stdout.strip() != WORKSTREAM_BRANCH:
        sys.exit(f'not on {WORKSTREAM_BRANCH}')
    git('fetch', 'origin', WORKSTREAM_BRANCH)
    r = git('merge', '--ff-only', f'origin/{WORKSTREAM_BRANCH}', check=False)
    if r.returncode != 0:
        sys.exit('local branch has diverged from the remote; resolve by hand before writing (lock not taken)')


def lease_live(lock: dict | None) -> bool:
    if not lock or not lock.get('holder'):
        return False
    hb = dt.datetime.fromisoformat(lock['heartbeat_at'])
    return dt.datetime.now(dt.timezone.utc) - hb < dt.timedelta(minutes=lock.get('ttl_minutes', LOCK_TTL_MINUTES))


def commit_and_push(message: str, paths=('question_bank/claude',)) -> bool:
    git('add', *paths)
    if git('diff', '--cached', '--quiet', check=False).returncode == 0:
        return True
    trailer = 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'
    git('commit', '-q', '-m', message if trailer in message else message + '\n\n' + trailer)
    return push_with_retry()


def lock_cmd(action: str, holder: str, message: str = '') -> None:
    lp = ROOT / LOCK_FILE
    if action == 'status':
        lock = read_json(lp, None)
        print(dumps({'lock': lock, 'live': lease_live(lock)}))
        return
    sync_branch()
    lock = read_json(lp, None)
    mine = bool(lock) and lock.get('holder') == holder
    if action == 'acquire':
        if lease_live(lock) and not mine:
            print(f'LOCKED by {lock["holder"]} (heartbeat {lock["heartbeat_at"]}); exiting without writing')
            sys.exit(3)
        t = now()
        atomic_write(lp, dumps({'holder': holder, 'acquired_at': lock['acquired_at'] if mine else t,
                                'heartbeat_at': t, 'ttl_minutes': LOCK_TTL_MINUTES,
                                'previous_holder': None if mine else (lock or {}).get('holder')}))
        if not commit_and_push(f'question bank: lock acquired by {holder}'):
            git('reset', '-q', '--hard', f'origin/{WORKSTREAM_BRANCH}')
            print('lost the race for the lock; exiting without writing')
            sys.exit(3)
        print(f'lock held by {holder}')
    elif action in ('checkpoint', 'release'):
        if not mine:
            print(f'lock is not held by {holder} (holder: {(lock or {}).get("holder")}); stop writing')
            sys.exit(4)
        lock['heartbeat_at'] = now()
        if action == 'release':
            lock.update({'holder': None, 'released_at': now(), 'released_by': holder})
        atomic_write(lp, dumps(lock))
        export()
        msg = message or (f'question bank: checkpoint by {holder}' if action == 'checkpoint' else f'question bank: lock released by {holder}')
        if not commit_and_push(msg):
            print('push rejected: the branch moved under us; stop writing and re-run lock acquire')
            sys.exit(4)
        print(f'{action} pushed')


@contextlib.contextmanager
def local_lock():
    ROOT.mkdir(parents=True, exist_ok=True)
    with open(ROOT / '.qb.lock', 'w') as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            sys.exit('another qb.py process in this container is writing; try again shortly')
        yield


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'review':
        with local_lock():
            review(sys.argv[2], int(sys.argv[3]))
            export()
    elif cmd == 'lock':
        # qb.py lock acquire|checkpoint|release|status <holder> [message]
        lock_cmd(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '', sys.argv[4] if len(sys.argv) > 4 else '')
    elif cmd == 'next':
        print(json.dumps((read_json(ROOT / 'progress.json', {}) or {}).get('next_bank'), ensure_ascii=False))
    elif cmd == 'screen':
        screen(sys.argv[2], int(sys.argv[3]))
    elif cmd == 'export':
        with local_lock():
            export()
    elif cmd == 'audit':
        audit(sys.argv[2])
    else:
        sys.exit(__doc__)
