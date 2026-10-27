#!/usr/bin/env python3
"""Build answer-free blind-review packets for records in the reconciled combined bank that still lack review.

Selects records with status 'pending_review' in a section, groups them by passage so passage sets stay together,
and writes packets of roughly N items to the scratch directory given. Each item carries its content hash so the
review binds to the exact version. A manifest is written to combined/audits/review-packets-<section>.json.

Usage: python3 -I tools/build_review_packets.py <section-slug> <outdir> [items_per_packet]
  section-slug: sat_rw | act_english | act_reading
"""
import json
import sys
import zipfile
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = {'sat_rw': ('SAT', 'Reading and Writing'), 'act_english': ('ACT', 'English'), 'act_reading': ('ACT', 'Reading')}


def main():
    slug, outdir = sys.argv[1], Path(sys.argv[2])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    exam, sec = SEC[slug]
    rec = json.loads((ROOT / 'combined' / 'reconciled' / 'combined-bank.json').read_text(encoding='utf-8'))['records']
    want = {r['id']: r for r in rec if r['exam'] == exam and r['section'] == sec and r['status'] == 'pending_review'}
    zf = zipfile.ZipFile(ROOT / 'combined' / 'baseline' / 'prep-and-price-combined-bank-screening.zip')
    pre = 'combined-quality-screen/'
    base = {x['id']: x for x in json.loads(zf.read(pre + 'retained-draft-bank.json')) + json.loads(zf.read(pre + 'held-and-reserved.json'))}
    groups = OrderedDict()
    for rid in sorted(want):
        x = base[rid]
        key = x.get('passage_id') or ('P:' + (x.get('passage') or '')[:80]) or rid
        groups.setdefault(key, []).append(x)
    packets, cur = [], []
    for key, items in groups.items():
        if cur and len(cur) + len(items) > n:
            packets.append(cur); cur = []
        cur += items
    if cur:
        packets.append(cur)
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for i, items in enumerate(packets, 1):
        name = f'chatgpt-{slug}-{i:02d}'
        pk = {'packet': name, 'note': 'Answer-free. Items sharing a passage appear together; the passage is repeated on each item.',
              'items': [{'id': x['id'], 'content_hash': want[x['id']]['content_hash'], 'passage': x.get('passage', ''),
                         'stem': x['stem'], 'choices': x['choices']} for x in items]}
        (outdir / f'{name}.json').write_text(json.dumps(pk, ensure_ascii=False, indent=1), encoding='utf-8')
        manifest.append({'packet': name, 'items': [x['id'] for x in items]})
    m = ROOT / 'combined' / 'audits' / f'review-packets-{slug}.json'
    m.write_text(json.dumps({'section': f'{exam} {sec}', 'pending_items': len(want), 'packets': manifest}, indent=1), encoding='utf-8')
    print(slug, len(want), 'items in', len(packets), 'packets', [len(p) for p in packets])


if __name__ == '__main__':
    main()
