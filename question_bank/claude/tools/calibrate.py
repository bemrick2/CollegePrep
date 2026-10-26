#!/usr/bin/env python3
"""Rebuild calibration/<bank>.json: calibrated difficulty = median of all independent AI ratings for each item.

Sources: the per-batch blind solver rating stored on the record, plus every calibration/<bank>_rater_*.json file.
With an even number of ratings the lower (easier) middle value is used. The author's label is never used, and the
accepted records are not modified. Also reports any rater answer that disagrees with a key (an extra solve check).
"""
import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = {'easy': 0, 'medium': 1, 'hard': 2}
INV = {v: k for k, v in ORDER.items()}

bank = sys.argv[1] if len(sys.argv) > 1 else 'act_math'
qs = json.loads((ROOT / 'banks' / f'{bank}.json').read_text())['questions']
raters = {p.stem.split('_rater_')[1]: json.loads(p.read_text())['ratings']
          for p in sorted((ROOT / 'calibration').glob(f'{bank}_rater_*.json'))}
items, mism = {}, []
for q in qs:
    rs = {}
    if q['validation'].get('blind_difficulty_opinion'):
        rs['blind_batch'] = q['validation']['blind_difficulty_opinion']
    for name, r in raters.items():
        if q['id'] in r:
            rs[f'rater_{name}'] = r[q['id']]['rating']
            if r[q['id']].get('answer') and r[q['id']]['answer'] != q['correct_answer']:
                mism.append({'id': q['id'], 'rater': name, 'answer': r[q['id']]['answer'], 'key': q['correct_answer']})
    vals = sorted(ORDER[v] for v in rs.values())
    if not vals:
        continue
    n = len(vals)
    med = vals[n // 2] if n % 2 else vals[n // 2 - 1]
    items[q['id']] = {'author': q['difficulty'], 'ratings': rs, 'calibrated': INV[med],
                      'changed_from_author': INV[med] != q['difficulty']}
doc = {'bank': bank, 'updated_at': dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
       'method': 'calibrated = median of all independent AI ratings (per-batch blind solver plus every whole-bank or partial rater file); even count uses the lower middle value; author label never used; accepted records unchanged.',
       'caveat': 'AI estimates of student performance, not data from real students.',
       'raters': sorted(raters), 'rater_answer_mismatches': mism, 'items': items}
(ROOT / 'calibration' / f'{bank}.json').write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
print('items', len(items), 'calibrated', dict(Counter(v['calibrated'] for v in items.values())),
      'author', dict(Counter(v['author'] for v in items.values())), 'answer mismatches', mism)
