#!/usr/bin/env python3
"""Cross-workstream duplicate screen: Claude items accepted after the combined baseline vs every other record.

Compares each post-baseline Claude record (from combined/reconciled/combined-bank.json + this workstream's banks) with
all ChatGPT records in the baseline ZIP and with all other Claude records, within the same section family
(math vs math across SAT/ACT; verbal by section, plus SAT R&W vs ACT Reading passages). Similarity is word-set
Jaccard on student-facing text (stem + choices, plus passage for verbal). Pairs at or above the threshold are
written for adjudication; similarity alone does not establish a substantive duplicate.

Usage: python3 -I tools/dup_screen_combined.py [threshold]
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_ZIP = ROOT / 'combined' / 'baseline' / 'prep-and-price-combined-bank-screening.zip'
OUT = ROOT / 'combined' / 'audits' / 'dup-screen-post-baseline.json'
STOP = set('the a an of to and in is that for on with as by at it its be this which are was from or what choice'
           ' best text most following based question passage completes conforms conventions standard english'
           ' logical precise word phrase'.split())


def toks(s):
    s = re.sub(r'\{\{\d+\|([^}]*)\}\}', r'\1', s or '')
    return {w for w in re.findall(r"[a-z0-9.]+", s.lower()) if w not in STOP and (len(w) > 2 or any(ch.isdigit() for ch in w))}


def context(passage, underline=None):
    """Local passage context for an item: SAT blanks use the whole short passage; ACT spans use +/-30 words."""
    p = passage or ''
    if underline is not None:
        m = re.search(r'\{\{%s\|([^}]*)\}\}' % underline, p)
        if m:
            pre = re.sub(r'\{\{\d+\|([^}]*)\}\}', r'\1', p[:m.start()]).split()[-30:]
            post = re.sub(r'\{\{\d+\|([^}]*)\}\}', r'\1', p[m.end():]).split()[:30]
            return ' '.join(pre + [m.group(1)] + post)
    m = re.search(r'\[(E\d+)\](.*?)\[/\1\]', p, re.S)
    if m:
        pre = p[:m.start()].split()[-30:]; post = p[m.end():].split()[:30]
        return ' '.join(pre + [m.group(2)] + post)
    return p if len(p.split()) < 160 else ''



def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def fam(sec):
    return 'math' if sec == 'Math' else sec


def main():
    thr = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    zf = zipfile.ZipFile(BASE_ZIP)
    pre = 'combined-quality-screen/'
    base = json.loads(zf.read(pre + 'retained-draft-bank.json')) + json.loads(zf.read(pre + 'held-and-reserved.json'))
    others = []
    for x in base:
        t = x['stem'] + ' ' + ' '.join((x.get('choices') or {}).values()) + ' ' + context(x.get('passage', ''))
        others.append((x['id'], x['source'], fam(x['section']), toks(t), toks(x.get('passage', ''))))
    rec = json.loads((ROOT / 'combined' / 'reconciled' / 'combined-bank.json').read_text(encoding='utf-8'))['records']
    new_ids = {r['id'] for r in rec if r['source'] == 'Claude' and not r['in_baseline'] and r['status'] in ('reviewed_draft', 'pending_review', 'hold')}
    mine = []
    for b in ['act_english', 'act_reading', 'sat_reading_writing', 'sat_math', 'act_math']:
        bd = json.loads((ROOT / 'banks' / f'{b}.json').read_text(encoding='utf-8'))
        pt = {p['passage_id']: p.get('text', '') for p in bd.get('passages', [])}
        sec = 'Math' if 'math' in b else {'act_english': 'English', 'act_reading': 'Reading', 'sat_reading_writing': 'Reading and Writing'}[b]
        for q in bd['questions']:
            t = q['stem'] + ' ' + ' '.join((q.get('choices') or {}).values()) + ' ' + context(pt.get(q.get('passage_id'), ''), q.get('underline'))
            entry = (q['id'], 'Claude', fam(sec), toks(t), toks(pt.get(q.get('passage_id'), '')))
            if q['id'] in new_ids:
                mine.append(entry)
            elif q['id'] not in {o[0] for o in others}:
                others.append(entry)
    pairs = []
    for mid, _, mf, mt, mp in mine:
        for oid, osrc, of, ot, op in others:
            if oid == mid or not (of == mf or {of, mf} == {'Reading', 'Reading and Writing'}):
                continue
            if len(mt) < 6 or len(ot) < 6:
                continue
            s_item = jac(mt, ot)
            s_pass = jac(mp, op) if mp and op else 0.0
            # for passage-based items, a shared passage alone is expected within a set; flag cross-source passage overlap
            if s_item >= thr or (s_pass >= thr and osrc != 'Claude'):
                pairs.append({'claude_id': mid, 'other_id': oid, 'other_source': osrc, 'item_similarity': round(s_item, 2),
                              'passage_similarity': round(s_pass, 2)})
    pairs.sort(key=lambda p: -max(p['item_similarity'], p['passage_similarity']))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({'screen': 'post-baseline Claude items vs all other combined records', 'threshold': thr,
                               'claude_items_screened': len(mine), 'records_compared': len(others), 'pairs': pairs},
                              ensure_ascii=False, indent=1), encoding='utf-8')
    print(len(mine), 'screened vs', len(others), '; pairs:', len(pairs))
    for p in pairs[:60]:
        print(p)


if __name__ == '__main__':
    main()
