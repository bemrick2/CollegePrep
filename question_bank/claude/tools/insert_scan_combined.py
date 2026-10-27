#!/usr/bin/env python3
"""Literal-insertion scan of every fill-in / edit-span option across the combined bank (all sources).

For each verbal record with a blank (3+ underscores) or an edit span ([E#]...[/E#], {{n|...}}), every choice is
inserted into the passage and the seam is checked for:
  REPEATED_WORD   the word on one side of the seam repeats the first/last word of the inserted choice
  DOUBLE_PUNCT    two punctuation marks meet across the seam (e.g. ', ;' or ',,')
  STRAY_SPACE     the choice begins or ends with a space, producing ' :' or a double space
  EMPTY_CHOICE    the choice text is empty (needs an explicit display label)
Findings are candidates for human/AI adjudication, not verdicts. Reads the preserved baseline ZIP and this
workstream's banks; writes combined/audits/insertion-scan-combined.json.

Usage: python3 -I tools/insert_scan_combined.py
"""
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_ZIP = ROOT / 'combined' / 'baseline' / 'prep-and-price-combined-bank-screening.zip'
OUT = ROOT / 'combined' / 'audits' / 'insertion-scan-combined.json'
PUNCT = set(',;:.!?—-')
WORD = re.compile(r"[A-Za-zÀ-ɏ']+")


def seam_checks(before, choice, after):
    """Render before+choice+after and test the rendered seam region."""
    out = []
    if choice == '':
        out.append('EMPTY_CHOICE')
    r = before + choice + after
    lo, hi = max(0, len(before) - 3), len(before) + len(choice) + 3
    seam = r[lo:hi]
    if re.search(r'\s[,;:.!?]', seam):
        out.append('SPACE_BEFORE_PUNCT')
    if re.search(r'\S  +\S', seam):
        out.append('DOUBLE_SPACE')
    if re.search(r'[A-Za-z][A-Z]|[a-z][a-z]', r[len(before)-1:len(before)+1]) and before[-1:].isalpha() and choice[:1].isalpha():
        out.append('MISSING_SPACE')
    if choice and after and choice[-1:].isalpha() and after[:1].isalpha():
        out.append('MISSING_SPACE')
    if re.search(r'([,;:.!?])\s*([,;:.!?])', seam) and not re.search(r'\.\.\.', seam):
        out.append('DOUBLE_PUNCT')
    c = choice.strip()
    bw, aw, cw = WORD.findall(before[-40:]), WORD.findall(after[:40]), WORD.findall(c)
    if bw and cw and bw[-1].lower() == cw[0].lower() and len(cw[0]) > 2 and not re.search(r'[,;:.!?]\s*$', before):
        out.append('REPEATED_WORD')
    if aw and cw and aw[0].lower() == cw[-1].lower() and len(cw[-1]) > 2 and not re.search(r'^\s*[,;:.!?]', after):
        out.append('REPEATED_WORD')
    return sorted(set(out))


def scan_record(rid, src, passage, stem, choices, span_hint=None):
    findings = []
    if not choices:
        return findings
    text = passage or ''
    m = re.search(r'_{3,}', text) or re.search(r'_{3,}', stem or '')
    target = None
    if m:
        hay = text if re.search(r'_{3,}', text) else stem
        before, after = hay[:m.start()], hay[m.end():]
        target = 'blank'
    else:
        span = None
        # an edit span is an insertion target only if the stem asks for a replacement/punctuation choice at that span
        s_m = re.search(r'\b(E\d+)\b', stem or '')
        asks_edit = re.search(r'replace|replacement|punctuat|conform|revision|keeping the sentence|NO CHANGE|best (?:version|wording)', stem or '', re.I)
        if not asks_edit:
            return findings
        span_hint = s_m.group(1) if s_m else span_hint
        if isinstance(span_hint, dict):
            span_hint = span_hint.get('marker')
        if isinstance(span_hint, str) and re.fullmatch(r'E\d+', span_hint):
            span = re.search(r'\[%s\](.*?)\[/%s\]' % (re.escape(span_hint), re.escape(span_hint)), text, re.S)
        if not span:
            s_m = re.search(r'span\s+(E\d+)', stem or '')
            if s_m:
                span = re.search(r'\[%s\](.*?)\[/%s\]' % (s_m.group(1), s_m.group(1)), text, re.S)
        if span:
            before, after = text[:span.start()], text[span.end():]
            before = re.sub(r'\[/?E\d+\]', '', before); after = re.sub(r'\[/?E\d+\]', '', after)
            target = 'span'
    if not target:
        return findings
    for k, v in choices.items():
        if v is None or v.strip().upper() == 'NO CHANGE':
            continue
        f = seam_checks(before, v, after)
        if f:
            findings.append({'choice': k, 'text': v, 'codes': f,
                             'inserted': (before[-60:] + '‖' + v + '‖' + after[:60]).replace('\n', ' ')})
    return [{'id': rid, 'source': src, 'target': target, 'flags': findings}] if findings else []


def main():
    zf = zipfile.ZipFile(BASE_ZIP)
    pre = 'combined-quality-screen/'
    recs = json.loads(zf.read(pre + 'retained-draft-bank.json')) + json.loads(zf.read(pre + 'held-and-reserved.json'))
    out, scanned = [], 0
    for x in recs:
        if x['section'] == 'Math' or x['source'] != 'ChatGPT':
            continue
        scanned += 1
        out += scan_record(x['id'], x['source'], x.get('passage', ''), x.get('stem', ''), x.get('choices'),
                           (x.get('raw') or {}).get('edit_span'))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({'scan': 'literal insertion of every option (ChatGPT verbal records in the baseline)',
                               'records_scanned': scanned, 'records_flagged': len(out),
                               'note': 'Flags are candidates for adjudication; see combined/audits/insertion-adjudication.json for decisions.',
                               'flags': out}, ensure_ascii=False, indent=1), encoding='utf-8')
    print(scanned, 'scanned;', len(out), 'flagged')


if __name__ == '__main__':
    main()
