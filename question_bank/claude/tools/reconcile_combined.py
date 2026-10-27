#!/usr/bin/env python3
"""Reconcile the combined-bank screening baseline with this workstream's current banks.

Reads (never modifies):
  combined/baseline/prep-and-price-combined-bank-screening.zip   (user-supplied baseline, preserved byte-for-byte)
  banks/*.json, audits/retired.json                                (this workstream's append-only banks)
  combined/reviews/*.json                                          (fresh reviews recorded after the baseline)
  combined/overlays.json                                           (proposed repairs and adjudications made after the baseline)

Writes:
  combined/reconciled/combined-bank.json      one record per question ID (all sources), with status and provenance
  combined/reconciled/summary.json            exact counts by section and status
  combined/reconciled/reconciliation-report.md

Status values (exactly one per record):
  reviewed_draft   current content version has independent AI review evidence (blind solve without key) and no open hold
  pending_review   retained, but the current version lacks independent review (self-review only, new, or changed)
  hold             open hold carried from the baseline or raised since (revision, adjudication, blueprint)
  reserved_duplicate  excluded/reserved as a duplicate or template variant (baseline) or retired by a concept-repeat audit
  retired          withdrawn by this workstream after acceptance (superseded by a repair, or retired by audit)
No record is human-approved; difficulty is provisional throughout.

Usage: python3 -I tools/reconcile_combined.py
"""
import datetime as dt
import hashlib
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMB = ROOT / 'combined'
BASE_ZIP = COMB / 'baseline' / 'prep-and-price-combined-bank-screening.zip'
OUT = COMB / 'reconciled'
BANKS = ['act_math', 'act_english', 'act_reading', 'sat_reading_writing', 'sat_math']
SECTION = {'act_math': ('ACT', 'Math'), 'act_english': ('ACT', 'English'), 'act_reading': ('ACT', 'Reading'),
           'sat_reading_writing': ('SAT', 'Reading and Writing'), 'sat_math': ('SAT', 'Math')}
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def norm(s):
    s = re.sub(r'\{\{\d+\|([^}]*)\}\}', r'\1', s or '')
    return re.sub(r'\s+', ' ', s).strip()


def chash(stem, choices, key, passage):
    ch = sorted((k, norm(v)) for k, v in (choices or {}).items())
    blob = json.dumps([norm(stem), ch, str(key).strip(), norm(passage)], ensure_ascii=False)
    return hashlib.sha256(blob.encode('utf-8')).hexdigest()[:16]


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def main():
    zf = zipfile.ZipFile(BASE_ZIP)
    pre = 'combined-quality-screen/'
    retained = json.loads(zf.read(pre + 'retained-draft-bank.json'))
    held = json.loads(zf.read(pre + 'held-and-reserved.json'))
    base = {}
    for x in retained + held:
        base[x['id']] = x
    retired = load(ROOT / 'audits' / 'retired.json')['retired']
    reviews = {}
    for f in sorted((COMB / 'reviews').glob('*.json')):
        doc = load(f)
        for rid, r in doc.get('results', {}).items():
            reviews.setdefault(rid, []).append(dict(r, file=str(f.relative_to(ROOT))))
    overlays = load(COMB / 'overlays.json') if (COMB / 'overlays.json').exists() else {'items': {}}

    # current Claude banks
    cur = {}
    for b in BANKS:
        bd = load(ROOT / 'banks' / f'{b}.json')
        ptext = {p['passage_id']: p.get('text', '') for p in bd.get('passages', [])}
        for q in bd['questions']:
            cur[q['id']] = (b, q, ptext.get(q.get('passage_id'), ''))

    records, notes = [], Counter()
    seen = set()
    # 1) every baseline record
    for rid, x in base.items():
        seen.add(rid)
        disp = x['screening']['disposition']
        findings = [f['code'] for f in x['screening'].get('findings', [])]
        rec = {'id': rid, 'source': x['source'], 'exam': x['exam'], 'section': x['section'],
               'source_bank': x.get('source_bank'), 'in_baseline': True, 'baseline_disposition': disp,
               'baseline_findings': findings, 'baseline_current_external_review': x.get('current_external_review'),
               'baseline_content_hash': chash(x['stem'], x['choices'], x['key'], x.get('passage', '')),
               'human_approved': False, 'difficulty_status': 'provisional (AI/author estimate; no student data)'}
        rec['content_hash'] = rec['baseline_content_hash']
        ov = overlays['items'].get(rid)
        if x['source'] == 'Claude':
            c = cur.get(rid)
            if c is None:
                rec['status'] = 'retired'; rec['status_reason'] = 'missing from current bank'
            else:
                b, q, ptxt = c
                h = chash(q['stem'], q.get('choices'), q['correct_answer'], ptxt)
                rec['content_hash'] = h
                rec['changed_since_baseline'] = h != rec['baseline_content_hash']
                if rid in retired:
                    r = retired[rid]
                    rec['status'] = status_for_retired(r)
                    rec['status_reason'] = f"withdrawn after baseline ({r.get('kind')}): {(r.get('shared_idea') or r.get('hold_reason') or '')[:160]}"
                    rec['superseded_by'] = r.get('superseded_by') or r.get('duplicate_of')
                    notes['claude_retired_after_baseline'] += 1
                elif disp != 'retained_draft_pending_full_editorial_review':
                    rec['status'] = 'hold' if disp.startswith('hold') else 'reserved_duplicate'
                    rec['status_reason'] = 'carried from baseline: ' + ', '.join(findings)
                elif rec['changed_since_baseline']:
                    rec['status'] = 'pending_review'; rec['status_reason'] = 'content changed since baseline; fresh review required'
                else:
                    rec['status'] = 'reviewed_draft'
                    rec['status_reason'] = 'current version blind-solved by separate AI reviewer(s) before acceptance (bank validation record)'
        else:
            if disp.startswith('hold'):
                rec['status'] = 'hold'; rec['status_reason'] = 'carried from baseline: ' + ', '.join(findings)
            elif disp.startswith('excluded'):
                rec['status'] = 'reserved_duplicate'; rec['status_reason'] = 'carried from baseline: ' + ', '.join(findings)
            elif x.get('current_external_review'):
                rec['status'] = 'reviewed_draft'; rec['status_reason'] = 'baseline: current-version external AI PASS evidence'
            else:
                rec['status'] = 'pending_review'; rec['status_reason'] = 'baseline: no current-version independent review'
        # fresh reviews recorded after the baseline (bound to a content hash)
        rv = [r for r in reviews.get(rid, []) if r.get('content_hash') == rec['content_hash']]
        if ov:
            rec['overlay'] = ov
            if ov.get('content_hash'):
                rec['content_hash'] = ov['content_hash']
                rv = [r for r in reviews.get(rid, []) if r.get('content_hash') == ov['content_hash']]
        if rv:
            rec['fresh_reviews'] = rv
            verdicts = {r['verdict'] for r in rv}
            if rec['status'] in ('pending_review', 'hold') and verdicts == {'PASS'} and len(rv) >= rec_required(rec) \
                    and not (ov and ov.get('keep_hold')):
                rec['status'] = 'reviewed_draft'
                rec['status_reason'] = 'fresh blind review(s) after baseline: ' + '; '.join(r['file'] for r in rv)
                notes['resolved_by_fresh_review'] += 1
            elif 'REVISE' in verdicts or 'HOLD' in verdicts:
                rec['status'] = 'hold' if rec['status'] != 'reserved_duplicate' else rec['status']
                rec['status_reason'] = 'fresh review found a problem: ' + '; '.join(r.get('summary', '')[:120] for r in rv if r['verdict'] != 'PASS')
        records.append(rec)

    # 2) Claude records not in the baseline (accepted after the 01:17 export, incl. all SAT Math)
    for rid, (b, q, ptxt) in cur.items():
        if rid in seen:
            continue
        ex, sec = SECTION[b]
        rec = {'id': rid, 'source': 'Claude', 'exam': ex, 'section': sec, 'source_bank': f'banks/{b}.json',
               'in_baseline': False, 'batch': q.get('batch'), 'draft_candidate': q.get('draft_candidate'),
               'content_hash': chash(q['stem'], q.get('choices'), q['correct_answer'], ptxt),
               'human_approved': False, 'difficulty_status': 'provisional (AI/author estimate; no student data)'}
        if rid in retired:
            r = retired[rid]
            rec['status'] = status_for_retired(r)
            rec['status_reason'] = f"withdrawn ({r.get('kind')}): {(r.get('shared_idea') or r.get('hold_reason') or '')[:160]}"
        else:
            v = q.get('validation', {})
            if v.get('status') == 'PASS' and v.get('blind_answer') is not None:
                rec['status'] = 'reviewed_draft'
                rec['status_reason'] = 'blind-solved by separate AI reviewer(s) before acceptance: ' + str(v.get('evidence'))
            else:
                rec['status'] = 'pending_review'; rec['status_reason'] = 'no blind-review evidence in bank record'
        rv = [r for r in reviews.get(rid, []) if r.get('content_hash') == rec['content_hash']]
        if rv:
            rec['fresh_reviews'] = rv
            if any(r['verdict'] != 'PASS' for r in rv):
                rec['status'] = 'hold'; rec['status_reason'] = 'fresh review found a problem'
        notes['claude_new_since_baseline'] += 1
        records.append(rec)

    # 3) proposed records that exist only as overlays (e.g. repaired versions of another stream's items)
    for rid, ov in overlays['items'].items():
        if ov.get('new_record') and rid not in {r['id'] for r in records}:
            records.append(ov['new_record'])

    records.sort(key=lambda r: (r['exam'], r['section'], r['id']))
    summ = defaultdict(Counter)
    for r in records:
        summ[f"{r['exam']} {r['section']}"][r['status']] += 1
        summ[f"{r['exam']} {r['section']}"]['_source_' + r['source']] += 1
    table = {}
    for k, c in summ.items():
        table[k] = {s: c.get(s, 0) for s in ['reviewed_draft', 'pending_review', 'hold', 'reserved_duplicate', 'retired']}
        table[k]['active_retained'] = table[k]['reviewed_draft'] + table[k]['pending_review']
        table[k]['by_source'] = {s[8:]: n for s, n in c.items() if s.startswith('_source_')}
    OUT.mkdir(parents=True, exist_ok=True)
    meta = {'generated_at': NOW, 'baseline_zip_sha256': hashlib.sha256(BASE_ZIP.read_bytes()).hexdigest(),
            'baseline_records': len(base), 'claude_current_records': len(cur), 'notes': dict(notes),
            'definitions': __doc__.split('Status values')[1].split('Usage')[0].strip()}
    (OUT / 'combined-bank.json').write_text(json.dumps({'meta': meta, 'records': records}, ensure_ascii=False, indent=1), encoding='utf-8')
    (OUT / 'summary.json').write_text(json.dumps({'meta': meta, 'by_section': table}, ensure_ascii=False, indent=1), encoding='utf-8')
    order = ['SAT Math', 'SAT Reading and Writing', 'ACT English', 'ACT Reading', 'ACT Math']
    lines = ['# Reconciled combined bank', '', f'Generated {NOW}. Baseline: user-supplied combined screening ZIP (sha256 {meta["baseline_zip_sha256"][:16]}...), '
             f'{len(base)} records. Claude current banks: {len(cur)} records. Records are matched by question ID and a normalized content hash '
             '(stem, choices, key, passage text). Claude items already in the baseline are not counted twice.', '',
             '| Section | Reviewed drafts | Pending review | Active retained (reviewed + pending) | Holds | Reserved/duplicate | Retired | By source |',
             '|---|---:|---:|---:|---:|---:|---:|---|']
    for k in order:
        t = table.get(k, {s: 0 for s in ['reviewed_draft', 'pending_review', 'hold', 'reserved_duplicate', 'retired', 'active_retained']} | {'by_source': {}})
        lines.append(f"| {k} | {t['reviewed_draft']} | {t['pending_review']} | {t['active_retained']} | {t['hold']} | {t['reserved_duplicate']} | {t['retired']} | "
                     + ', '.join(f'{s} {n}' for s, n in sorted(t['by_source'].items())) + ' |')
    lines += ['', '"Reviewed" means a separate AI agent answered the current version without the key and agreed with it (verbal: two solvers for Claude items). '
              'It is not human approval; no record is human-approved, rights-cleared, or student-calibrated.', '',
              'Notes: ' + json.dumps(dict(notes))]
    (OUT / 'reconciliation-report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(table, indent=1))


def status_for_retired(r):
    # a defect hold stays an open hold until a repaired version passes fresh review (then: superseded -> retired)
    if r.get('resolution', {}).get('superseded_by'):
        return 'retired'
    if r.get('kind') == 'hold-defect':
        return 'hold'
    return 'reserved_duplicate'


def rec_required(rec):
    return 1


if __name__ == '__main__':
    main()
