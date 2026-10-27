#!/usr/bin/env python3
"""Turn raw blind-solver answer files for overlay packets into version-bound review results.

For each solver file combined/reviews/<packet>.solver<X>.json, writes combined/reviews/<packet>.<X>.results.json with
one result per item: verdict PASS when the solver's answer equals the key of the proposed version and the solver raised
no blocking (non-'minor:') flag, otherwise HOLD. Keys come from combined/overlays.json (the solver never saw them).

Usage: python3 -I tools/record_overlay_reviews.py <packet-name>
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
packet = sys.argv[1]
over = json.loads((ROOT / 'combined' / 'overlays.json').read_text(encoding='utf-8'))['items']
for f in sorted((ROOT / 'combined' / 'reviews').glob(f'{packet}.solver*.json')):
    tag = f.stem.split('.solver')[-1]
    doc = json.loads(f.read_text(encoding='utf-8'))
    res = {}
    for rid, a in doc['answers'].items():
        ov = over[rid]
        blocking = [x for x in a.get('flags', []) if not str(x).lower().startswith('minor')]
        ok = a.get('answer') == ov['proposed']['key'] and not blocking and a.get('content_hash') == ov['content_hash']
        res[rid] = {'content_hash': ov['content_hash'], 'verdict': 'PASS' if ok else 'HOLD', 'solver': doc.get('solver'),
                    'answer': a.get('answer'), 'key': ov['proposed']['key'], 'confidence': a.get('confidence'),
                    'flags': a.get('flags', []), 'summary': '; '.join(blocking)[:300] or ('answer differs from key' if a.get('answer') != ov['proposed']['key'] else '')}
    out = ROOT / 'combined' / 'reviews' / f'{packet}.{tag}.results.json'
    out.write_text(json.dumps({'packet': packet, 'source_file': str(f.relative_to(ROOT)), 'results': res}, ensure_ascii=False, indent=1), encoding='utf-8')
    print(out.name, sum(r['verdict'] == 'PASS' for r in res.values()), 'PASS /', len(res))
    for rid, r in res.items():
        if r['verdict'] != 'PASS':
            print('  HOLD', rid, r['answer'], r['key'], r['summary'][:150])
