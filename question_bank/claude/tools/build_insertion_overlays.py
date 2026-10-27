#!/usr/bin/env python3
"""Build proposed display repairs (overlays) for insertion-scan flags on other workstreams' records.

Source records are not edited. For each flagged record the proposed version keeps the stem, key letter and meaning,
and changes only how options sit in the passage:
  - options that duplicate punctuation already in the passage drop the duplicate (e.g. 'Even so,' before ',' -> 'Even so');
  - spacing and empty-option problems are fixed by anchoring the word before the blank inside every option
    (official SAT style: 'tool______ will' -> '______ will' with options 'tool,', 'tool;', 'tool', ...).
Each proposed version gets a content hash; it must pass fresh blind review before it counts as reviewed.

Usage: python3 -I tools/build_insertion_overlays.py
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from reconcile_combined import chash  # noqa: E402

BASE_ZIP = ROOT / 'combined' / 'baseline' / 'prep-and-price-combined-bank-screening.zip'
SCAN = ROOT / 'combined' / 'audits' / 'insertion-scan-combined.json'
OVER = ROOT / 'combined' / 'overlays.json'
P = ',;:.!?'


def render(before, choice, after):
    return before + choice + after


def repair(passage, choices):
    """Return (new_passage, new_choices, method) or None if not handled."""
    m = re.search(r'_{3,}', passage)
    span = None
    if not m:
        span = re.search(r'\[(E\d+)\](.*?)\[/\1\]', passage, re.S)
        if not span:
            return None
        before, after = passage[:span.start()], passage[span.end():]
    else:
        before, after = passage[:m.start()], passage[m.end():]
    new = dict(choices)
    method = []
    # 1) duplicate trailing punctuation: option ends with the same mark the passage supplies right after the blank
    a0 = after.lstrip()[:1]
    if a0 and a0 in P and all((v or '').rstrip()[-1:] in P for v in choices.values() if v and v.strip().upper() != 'NO CHANGE'):
        new = {k: (v.rstrip().rstrip(P).rstrip() if v and v.strip().upper() != 'NO CHANGE' else v) for k, v in new.items()}
        method.append('dropped trailing punctuation duplicated by the passage')
    # 2) spacing / empty options at the start: anchor the preceding word inside each option
    needs_anchor = any((v == '') or re.match(r'\s', v or '') or ((v or '')[:1] in P and before.endswith(' '))
                       or ((v or '')[:1].isalpha() and before[-1:].isalpha())
                       for v in new.values() if v is None or v.strip().upper() != 'NO CHANGE')
    if needs_anchor and m:
        wm = re.search(r"(\S+)\s*$", before)
        if not wm:
            return None
        word = wm.group(1)
        base = before[:wm.start()]
        def anchored(v):
            v = (v or '').strip()
            if not v:
                return word
            return word + v if v[:1] in P else word + ' ' + v
        new = {k: anchored(v) for k, v in new.items()}
        before = base
        # ensure a single space after the blank when the option ends in a word/punct and 'after' starts with a word
        after = ' ' + after.lstrip() if after.lstrip()[:1].isalnum() or after.lstrip()[:1] in '(“"' else after
        method.append(f"anchored the preceding word ('{word}') inside every option; removed stray spaces/empty option")
    # 3) trailing spaces inside options that produce a double space before the rest of the sentence
    if after[:1] == ' ' and any((v or '').endswith(' ') for v in new.values()):
        new = {k: (v.rstrip() if v else v) for k, v in new.items()}
        method.append('removed trailing spaces inside options')
    if not method:
        return None
    if m:
        new_passage = before + '______' + after
    else:
        new_passage = passage
    return new_passage, new, '; '.join(method)


def main():
    zf = zipfile.ZipFile(BASE_ZIP)
    pre = 'combined-quality-screen/'
    recs = {x['id']: x for x in json.loads(zf.read(pre + 'retained-draft-bank.json')) + json.loads(zf.read(pre + 'held-and-reserved.json'))}
    scan = json.loads(SCAN.read_text(encoding='utf-8'))
    over = json.loads(OVER.read_text(encoding='utf-8'))
    report = []
    for f in scan['flags']:
        x = recs[f['id']]
        r = repair(x.get('passage', ''), x['choices'])
        if not r:
            report.append((f['id'], 'NOT AUTO-REPAIRED')); continue
        np_, nc, how = r
        h = chash(x['stem'], nc, x['key'], np_)
        over['items'][f['id']] = {
            'kind': 'proposed_display_repair', 'owner': x['source'], 'source_bank': x.get('source_bank'),
            'source_content_version': (x.get('raw') or {}).get('content_version'),
            'reason': 'literal insertion of options produced defective text: ' + ', '.join(sorted({c for fl in f['flags'] for c in fl['codes']})),
            'method': how, 'proposed': {'stem': x['stem'], 'passage': np_, 'choices': nc, 'key': x['key']},
            'content_hash': h, 'status_until_reviewed': 'hold', 'requires_source_adoption': True,
            'note': 'Source file not edited. The proposed version counts as reviewed only after fresh blind solves bound to this content hash.'}
        report.append((f['id'], how))
    OVER.write_text(json.dumps(over, ensure_ascii=False, indent=1), encoding='utf-8')
    for rid, how in report:
        print(rid, '|', how)


if __name__ == '__main__':
    main()
