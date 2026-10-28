#!/usr/bin/env python3
"""Whole-bank near-duplicate screen: every pair of reviewed_draft records (all sources) within a section family.

dup_screen_combined.py compares post-baseline Claude items with everything else; this screen also covers pairs that
both predate the baseline (ChatGPT-ChatGPT, Claude-ChatGPT, Claude-Claude). Same token metric (stem + choices + local
passage context, Jaccard). Uses the effective content from final_audit.effective_records (overlay repairs applied).
Pairs already adjudicated in combined/audits/dup-adjudication*.json or in the baseline package are marked as such.

Usage: python3 -I tools/dup_screen_all.py [threshold=0.6]
"""
import json
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dup_screen_combined as D  # noqa: E402
import final_audit as F  # noqa: E402

OUT = F.COMB / 'audits' / 'dup-screen-whole-bank.json'


def main():
    thr = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
    recs, _, _ = F.effective_records()
    live = [e for e in recs if e['status'] == 'reviewed_draft' and 'stem' in e]
    adj = {}
    for f in sorted((F.COMB / 'audits').glob('dup-adjudication*.json')):
        for p in F.load(f)['pairs']:
            adj[frozenset((p['a'], p['b']))] = p['verdict']
    zf = zipfile.ZipFile(F.BASE_ZIP)
    base_adj = json.loads(zf.read('combined-quality-screen/duplicate-adjudications.json'))
    base_pairs = set()
    for p in (base_adj if isinstance(base_adj, list) else base_adj.get('pairs', base_adj.get('adjudications', []))):
        ids = [v for k, v in p.items() if isinstance(v, str) and k in ('a', 'b', 'id_a', 'id_b', 'left', 'right', 'kept', 'excluded')]
        if len(ids) >= 2:
            base_pairs.add(frozenset(ids[:2]))
    items = []
    for e in live:
        t = e['stem'] + ' ' + ' '.join(str(v) for v in e['choices'].values()) + ' ' + D.context(e.get('passage', ''), e.get('underline'))
        items.append((e['id'], e['source'], D.fam(e['section']), D.toks(t), e.get('passage_id')))
    fams = defaultdict(list)
    for it in items:
        fams[it[2]].append(it)
    pairs = []
    for fam, its in fams.items():
        index = defaultdict(set)
        for i, it in enumerate(its):
            for w in it[3]:
                index[w].add(i)
        for i, a in enumerate(its):
            cand = defaultdict(int)
            for w in a[3]:
                if len(index[w]) > 400:
                    continue
                for j in index[w]:
                    if j > i:
                        cand[j] += 1
            for j, shared in cand.items():
                b = its[j]
                if shared / max(len(a[3]), len(b[3])) < thr * 0.9:
                    continue
                s = D.jac(a[3], b[3])
                if s >= thr:
                    k = frozenset((a[0], b[0]))
                    pairs.append({'a': a[0], 'b': b[0], 'family': fam, 'similarity': round(s, 2),
                                  'same_passage': bool(a[4] and a[4] == b[4]),
                                  'adjudicated': adj.get(k) or ('baseline' if k in base_pairs else None)})
    pairs = [p for p in pairs if not p['same_passage']]
    # math signature: the stem's mathematical expression (numbers, variables and operators), plus the key's text
    import re
    sig = defaultdict(list)
    for e in live:
        if e['section'] != 'Math':
            continue
        chunks = re.findall(r'[0-9a-z\u00b2\u00b3\u221a\u03c0=+\-\u2212|()/^<>\u2264\u2265.]+', e['stem'].lower().replace(' ', ''))
        chunks = [c.replace('\u2212', '-').strip('.') for c in re.split(r'[?,;:]', ''.join(chunks)) if c]
        expr = ' '.join(sorted(c for c in re.findall(r'[^a-z]*[a-z]?[^a-z]*', e['stem'].lower().replace(' ', '').replace('\u2212', '-'))
                               if re.search(r'[=+\-|^<>/\u2264\u2265]', c) and re.search(r'[0-9]', c) and len(c) >= 5))
        if len(expr) >= 6:
            sig[(expr, str(e['choices'].get(e['key'], '')).strip())].append(e['id'])
    seen = {frozenset((p['a'], p['b'])) for p in pairs}
    for (expr, _), ids in sig.items():
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                k = frozenset((ids[i], ids[j]))
                if k not in seen:
                    seen.add(k)
                    pairs.append({'a': ids[i], 'b': ids[j], 'family': 'math', 'similarity': None, 'math_signature': expr,
                                  'same_passage': False, 'adjudicated': adj.get(k) or ('baseline' if k in base_pairs else None)})
    # the same tested span twice on one passage (ACT English)
    span = defaultdict(list)
    for e in live:
        if e['section'] == 'English' and e.get('passage_id'):
            u = e.get('underline')
            if u is None:
                import re as _re
                m = _re.search(r'\bE(\d+)\b', e['stem'] + ' ' + str((e.get('raw') or {}).get('edit_span') or ''))
                u = 'E' + m.group(1) if m else None
            if u is not None and not e.get('q', {}).get('essay_level'):
                span[(e['passage_id'], str(u))].append(e['id'])
    same_span = [{'passage_id': k[0], 'span': k[1], 'ids': v} for k, v in span.items() if len(v) > 1]
    pairs.sort(key=lambda p: -(p['similarity'] or 1.0))
    out = {'screen': 'whole-bank pairwise (reviewed_draft records, all sources)', 'threshold': thr,
           'records_screened': len(live), 'pairs': pairs, 'same_span_on_one_passage': same_span,
           'note': 'pairs on the same passage are excluded (shared context by design); see same_span_on_one_passage',
           'unadjudicated': sum(1 for p in pairs if not p['adjudicated'])}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(len(live), 'screened;', len(pairs), 'pairs (>=', thr, 'or same math signature);', out['unadjudicated'], 'unadjudicated;', len(same_span), 'same-span groups')


if __name__ == '__main__':
    main()
