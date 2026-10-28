"""Import-format files and contract-gap report for the final reconciled bank (2026-10-28 package, v2).

Reads the reconciled bank (complete-bank.json from the final package ZIP) and the official Claude import lines
(exports/import/*.jsonl, written by qb.to_import). Writes, under OUT:

  import/v1/<bank>.jsonl   question_import/v1 lines, reviewed_draft Claude records only (lines unchanged)
  import/v2/<bank>.jsonl   the same lines in question_import/v2: contract v2 + author_identity {kind: ai, model: claude}
  import/excluded-from-import.json   lines present in exports/import/*.jsonl that the reconciled bank does not
                                     count (hold, pending, reserved duplicate, retired), with status and reason
  import/chatgpt-contract-gaps.json  every reviewed ChatGPT record, with the contract-required fields it lacks
  import/crosscheck.json   per-line comparison of import content against the reconciled record

Nothing here writes to any database, imports, deploys or publishes. No content is invented: ChatGPT records that
lack required contract fields are reported, not filled in.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK_JSON, OUT = Path(sys.argv[1]), Path(sys.argv[2])
BANKS = {
    'sat_math': ('SAT', 'Math'), 'sat_reading_writing': ('SAT', 'Reading and Writing'),
    'act_english': ('ACT', 'English'), 'act_reading': ('ACT', 'Reading'), 'act_math': ('ACT', 'Math'),
}
records = json.loads(BANK_JSON.read_text(encoding='utf-8'))['records']
by_id = {r['id']: r for r in records}


def norm(s):
    s = re.sub(r'\{\{\d+\|(.*?)\}\}', r'\1', s or '')          # Claude ACT English span markup
    s = re.sub(r'[\[\]]', '', s)                                  # import renders the item's own span in brackets
    return re.sub(r'\s+', ' ', s).strip()


def crosscheck(line, r):
    issues = []
    if norm(line['stem']) != norm(r['stem']):
        issues.append('stem')
    lc = {c['key']: c['text'] for c in line.get('choices') or []}
    if (lc or None) != (r.get('choices') or None):
        issues.append('choices')
    key = r['accepted_answers'] if r.get('accepted_answers') else [r['key']]
    if [str(x) for x in line['accepted_answers']] != [str(x) for x in key]:
        issues.append('key')
    if norm(line.get('passage')) != norm(r.get('passage')):
        issues.append('passage')
    return issues


(OUT / 'import' / 'v1').mkdir(parents=True, exist_ok=True)
(OUT / 'import' / 'v2').mkdir(parents=True, exist_ok=True)
excluded, checks, counts = [], {}, {}
for bank, (exam, section) in BANKS.items():
    src = ROOT / 'exports' / 'import' / f'{bank}.jsonl'
    lines = [json.loads(x) for x in src.read_text(encoding='utf-8').splitlines() if x.strip()]
    keep = []
    for ln in lines:
        rid = ln['import_id'].upper()
        r = by_id.get(rid)
        if r is None or r['status'] != 'reviewed_draft':
            excluded.append({'id': rid, 'bank': bank, 'status': r['status'] if r else 'not in reconciled bank',
                             'reason': r['status_reason'] if r else None})
            continue
        bad = crosscheck(ln, r)
        checks[rid] = bad or 'match'
        keep.append(ln)
    want = {r['id'] for r in records if r['source'] == 'Claude' and r['exam'] == exam
            and r['section'] == section and r['status'] == 'reviewed_draft'}
    have = {ln['import_id'].upper() for ln in keep}
    assert want == have, (bank, sorted(want - have)[:5], sorted(have - want)[:5])
    v1 = ''.join(json.dumps(ln, ensure_ascii=False) + '\n' for ln in keep)
    v2 = ''.join(json.dumps({**ln, 'contract': 'question_import/v2',
                             'author_identity': {'kind': 'ai', 'model': ln['author'].split(':', 1)[1]}},
                            ensure_ascii=False) + '\n' for ln in keep)
    (OUT / 'import' / 'v1' / f'{bank}.jsonl').write_text(v1, encoding='utf-8')
    (OUT / 'import' / 'v2' / f'{bank}.jsonl').write_text(v2, encoding='utf-8')
    counts[bank] = {'source_lines': len(lines), 'import_lines': len(keep), 'excluded': len(lines) - len(keep)}

REQUIRED = {  # contract field -> reconciled-record field it would come from
    'hints (at least one)': 'hints', 'strategy_explanation': 'strategy', 'expected_time_seconds': 'expected_time_seconds',
    'primary_skill_key (taxonomy key)': None, 'distractors (rationale for every wrong choice)': 'distractor_rationales',
}
gaps = []
for r in records:
    if r['source'] != 'ChatGPT' or r['status'] != 'reviewed_draft':
        continue
    missing = []
    for field, src in REQUIRED.items():
        if src is None:
            missing.append(field)                     # ChatGPT skills are free text, not taxonomy keys
        elif src == 'distractor_rationales':
            wrong = [k for k in (r.get('choices') or {}) if k != r['key']]
            dr = r.get(src)
            if isinstance(dr, str) and dr.strip():
                missing.append('distractors (one free-text note, not a rationale per wrong choice)')
            elif r.get('choices') and not all((dr or {}).get(k) for k in wrong):
                missing.append(field)
        elif r.get(src) in (None, [], {}, ''):
            missing.append(field)
    gaps.append({'id': r['id'], 'exam': r['exam'], 'section': r['section'],
                 'source_bank': r['provenance']['source_bank'], 'missing_required': missing})

mismatch = {k: v for k, v in checks.items() if v != 'match'}
(OUT / 'import' / 'excluded-from-import.json').write_text(json.dumps(
    {'note': 'Lines in exports/import/*.jsonl (generated from the raw Claude banks) that the reconciled bank does not '
             'count as reviewed drafts. Left out of import/v1 and import/v2.', 'records': excluded}, indent=1), encoding='utf-8')
(OUT / 'import' / 'chatgpt-contract-gaps.json').write_text(json.dumps(
    {'note': 'Reviewed ChatGPT drafts are not in import format: each lacks contract-required fields. Filling them '
             'means writing new content (hints, strategies, times, distractor rationales, skill mapping), which then '
             'needs its own review. Nothing was invented.',
     'records': len(gaps),
     'missing_field_counts': dict(Counter(f for g in gaps for f in g['missing_required'])),
     'items': gaps}, indent=1), encoding='utf-8')
(OUT / 'import' / 'crosscheck.json').write_text(json.dumps(
    {'compared': len(checks), 'matches': len(checks) - len(mismatch), 'mismatches': mismatch}, indent=1), encoding='utf-8')
print(json.dumps({'counts': counts, 'excluded': len(excluded), 'crosscheck_mismatches': len(mismatch),
                  'chatgpt_gap_records': len(gaps)}, indent=1))
