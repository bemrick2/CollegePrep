#!/usr/bin/env python3
"""Final whole-bank audit of the reconciled combined bank (all sources, all sections).

Reads (never modifies): combined/reconciled/combined-bank.json, the preserved baseline ZIP, combined/overlays.json,
combined/reviews/*.json, banks/*.json, reviews/<bank>/batch-NNN.review.json, audits/*.json and
combined/audits/dup-*.json.

Checks, per record in its effective content version (overlay repairs applied where the reconciled status relies on them):
  structure        four non-empty, distinct choices A-D; key among them; stem; explanation; passage for verbal items;
                   ACT English underline/edit span present in the passage
  review evidence  Claude: bank validation PASS with blind answer(s) equal to the key and the per-batch review file present;
                   ChatGPT: current-version external AI PASS (baseline) or fresh PASS reviews bound to the content hash
  passage          every passage referenced by a reviewed record resolves; no reviewed record sits on a superseded passage;
                   every ACT English underline/edit span in a passage with reviewed items is either tested by a reviewed
                   item or recorded as acceptable plain text; passage-set sizes
  insertion        literal insertion of every option into blank/underline items (missing space, doubled punctuation,
                   space before punctuation, doubled space)
  duplicates       exact content duplicates among reviewed records; post-baseline near-duplicate pairs and their
                   adjudications
  hints            a hint must not contain the key's distinctive wording
Blocking findings apply to reviewed_draft records only; other statuses are reported for information.

Usage: python3 -I tools/final_audit.py [out.json]
"""
import datetime as dt
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMB = ROOT / 'combined'
BASE_ZIP = COMB / 'baseline' / 'prep-and-price-combined-bank-screening.zip'
BANKS = ['act_math', 'act_english', 'act_reading', 'sat_reading_writing', 'sat_math']
VERBAL = {'English', 'Reading', 'Reading and Writing'}
TODAY = dt.date.today().isoformat()
UL = re.compile(r'\{\{(\d+)\|([^}]*)\}\}')
EDIT = re.compile(r'\[E(\d+)\](.*?)\[/E\1\]', re.S)


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def plain(t):
    return EDIT.sub(r'\2', UL.sub(r'\2', t or ''))


def effective_records():
    """Yield one dict per reconciled record with the content version its status refers to."""
    rec = load(COMB / 'reconciled' / 'combined-bank.json')['records']
    zf = zipfile.ZipFile(BASE_ZIP)
    pre = 'combined-quality-screen/'
    base = {x['id']: x for x in json.loads(zf.read(pre + 'retained-draft-bank.json')) + json.loads(zf.read(pre + 'held-and-reserved.json'))}
    cur, passages, superseded = {}, {}, set()
    for b in BANKS:
        bd = load(ROOT / 'banks' / f'{b}.json')
        for p in bd.get('passages', []):
            passages[p['passage_id']] = p
            if p.get('supersedes_passage'):
                superseded.add(p['supersedes_passage'])
        for q in bd['questions']:
            cur[q['id']] = (b, q)
    out = []
    for r in rec:
        e = dict(r)
        if r['source'] == 'Claude' and r['id'] in cur:
            b, q = cur[r['id']]
            p = passages.get(q.get('passage_id')) or {}
            e.update(bank=b, stem=q['stem'], choices=q.get('choices') or {}, key=q['correct_answer'],
                     accepted_answers=q.get('accepted_answers'), answer_format=q.get('answer_format'),
                     passage_id=q.get('passage_id'), passage=p.get('text', ''), underline=q.get('underline'),
                     explanation=q.get('explanation', ''), hints=q.get('hints') or [], q=q)
        elif r['id'] in base:
            x = base[r['id']]
            raw = x.get('raw') or {}
            e.update(stem=x['stem'], choices=x.get('choices') or {}, key=x['key'], passage_id=x.get('passage_id'),
                     passage=x.get('passage') or '', explanation=raw.get('explanation', ''),
                     hints=raw.get('hints') if isinstance(raw.get('hints'), list) else ([raw['hints']] if raw.get('hints') else []),
                     edit_span=raw.get('edit_span'), raw=raw)
            ov = r.get('overlay') or {}
            if ov.get('proposed') and r['status'] in ('reviewed_draft', 'hold'):
                pr = ov['proposed']
                e.update(stem=pr.get('stem', e['stem']), passage=pr.get('passage', e['passage']),
                         choices=pr.get('choices', e['choices']), key=pr.get('key', e['key']), overlay_applied=True)
        elif r.get('overlay', {}).get('new_record'):
            e.update(r['overlay']['new_record'])
        out.append(e)
    return out, passages, superseded


SEAMS = [('MISSING_SPACE', re.compile(r'[a-z][A-Z]|[a-z,;:][a-z]{0}(?<=[,;:])[A-Za-z]')),
         ('DOUBLE_PUNCT', re.compile(r'[,;:.][,;:.]|—[,;:]|[,;:]—')),
         ('SPACE_BEFORE_PUNCT', re.compile(r' [,;:.!?](?!\.)')),
         ('DOUBLE_SPACE', re.compile(r'\S  +\S'))]


def insertion_problems(e):
    """Insert each option literally at the blank or the tested span and look at the seams."""
    out = []
    t = e.get('passage') or ''
    NONREPLACE = ('delete', 'should the writer', 'is considering', 'suppose', 'placed', 'placement', 'would lose', 'would primarily lose')
    if e['section'] == 'English' and any(w in e['stem'].lower() for w in NONREPLACE):
        return out
    if e['section'] == 'English' and e.get('underline'):
        m = re.search(r'\{\{%d\|([^}]*)\}\}' % e['underline'], t)
        if not m:
            return out
        before, after, orig = plain(t[:m.start()]), plain(t[m.end():]), m.group(1)
    elif '______' in t and e['section'] in VERBAL and e['section'] != 'English':
        i = t.index('______')
        before, after, orig = t[:i], t[i + 6:], None
    else:
        return out
    for k, v in (e.get('choices') or {}).items():
        if v.startswith('NO CHANGE'):
            v = orig if orig is not None else v
        if v.startswith(('OMIT', 'DELETE')):
            v = ''
        if orig is None and v.endswith(('.', '?')) and not after.strip():
            pass
        s = before[-30:] + v + after[:30]
        deleting = v == ''
        seam = before[-2:] + v[:2] + '|' + v[-2:] + after[:2]
        for code, rx in SEAMS:
            if code == 'MISSING_SPACE':
                hit = (before[-1:].isalpha() and v[:1].isalpha()) or (v[-1:].isalnum() and after[:1].isalpha()) \
                      or (v[-1:] in ',;:' and after[:1].isalpha())
            elif code == 'DOUBLE_SPACE' and deleting:
                hit = False
            else:
                hit = bool(rx.search(re.sub(r'(?<=[A-Z])\.(?=[,;:])', '', before[-3:] + v + after[:3])))
            if hit:
                out.append({'choice': k, 'code': code, 'text': s})
    return out


def main():
    outp = Path(sys.argv[1]) if len(sys.argv) > 1 else COMB / 'audits' / f'final-audit-{TODAY}.json'
    recs, passages, superseded = effective_records()
    reviews_cache = {}
    find = []

    def add(e, check, code, detail, blocking=True):
        find.append({'id': e['id'], 'source': e['source'], 'section': f"{e['exam']} {e['section']}", 'status': e['status'],
                     'check': check, 'code': code, 'detail': detail,
                     'blocking': bool(blocking and e['status'] == 'reviewed_draft')})

    reviewed = [e for e in recs if e['status'] == 'reviewed_draft']
    # ---------- structure
    for e in recs:
        if 'stem' not in e:
            add(e, 'structure', 'NO_CONTENT', 'no content found for this record')
            continue
        ch = e['choices']
        if e.get('answer_format') in ('spr', 'numeric') or (e['source'] == 'Claude' and not ch and e.get('accepted_answers')):
            if not e.get('accepted_answers'):
                add(e, 'structure', 'SPR_NO_ACCEPTED', 'student-produced response without accepted answers')
        else:
            if sorted(ch) != ['A', 'B', 'C', 'D']:
                add(e, 'structure', 'CHOICE_LETTERS', f'choices {sorted(ch)}')
            if any(not str(v).strip() for v in ch.values()):
                add(e, 'structure', 'EMPTY_CHOICE', 'an empty choice')
            vals = [re.sub(r'\s+', ' ', str(v)).strip().lower() for v in ch.values()]
            if len(set(vals)) != len(vals):
                add(e, 'structure', 'DUPLICATE_CHOICE', 'two choices have identical text')
            if str(e['key']).strip() not in ch:
                add(e, 'structure', 'KEY_NOT_IN_CHOICES', f"key {e['key']!r}")
        if not str(e['stem']).strip():
            add(e, 'structure', 'EMPTY_STEM', '')
        if not str(e.get('explanation') or '').strip():
            add(e, 'structure', 'NO_EXPLANATION', '')
        if e['section'] in VERBAL and not (e.get('passage') or '').strip():
            add(e, 'structure', 'NO_PASSAGE', 'verbal item without passage text')
        if e['section'] == 'English' and e['source'] == 'Claude' and e.get('underline'):
            if not re.search(r'\{\{%d\|' % e['underline'], e.get('passage') or ''):
                essay = (e.get('q') or {}).get('essay_level') or not e['stem'].startswith('Which choice is best for the underlined')
                add(e, 'structure', 'STALE_UNDERLINE_ON_ESSAY_ITEM' if essay else 'UNDERLINE_MISSING',
                    f"underline {e['underline']} not in passage" + (' (essay-level item; renders with no highlight)' if essay else ''),
                    blocking=not essay)
    # ---------- review evidence
    for e in reviewed:
        if e['source'] == 'Claude' and e.get('q'):
            v = e['q'].get('validation') or {}
            if v.get('status') != 'PASS':
                add(e, 'review_evidence', 'NO_PASS', 'bank validation status is not PASS')
            ba = v.get('blind_answer')
            if e.get('answer_format') not in ('spr', 'numeric') and str(ba) != str(e['key']):
                add(e, 'review_evidence', 'BLIND_MISMATCH', f'blind answer {ba} vs key {e["key"]}')
            ev = v.get('evidence')
            if not ev or not (ROOT / ev).exists():
                add(e, 'review_evidence', 'REVIEW_FILE_MISSING', str(ev))
            elif e['section'] in VERBAL:
                if ev not in reviews_cache:
                    reviews_cache[ev] = load(ROOT / ev)
                doc = reviews_cache[ev]
                items = doc.get('items') or doc.get('results') or doc.get('candidates') or []
                if isinstance(items, dict):
                    items = list(items.values())
                hit = [x for x in items if x.get('cand') == e['q'].get('draft_candidate') or x.get('candidate') == e['q'].get('draft_candidate')]
                if hit:
                    b2 = hit[0].get('blind2_answer')
                    if b2 is not None and str(b2) != str(e['key']):
                        add(e, 'review_evidence', 'BLIND2_MISMATCH', f'second solver {b2} vs key {e["key"]}')
                    if hit[0].get('status') not in (None, 'PASS'):
                        add(e, 'review_evidence', 'REVIEW_NOT_PASS', str(hit[0].get('status')))
                else:
                    add(e, 'review_evidence', 'NOT_IN_REVIEW_FILE', f"{e['q'].get('draft_candidate')} not found in {ev}", blocking=False)
            if e.get('changed_since_baseline'):
                add(e, 'review_evidence', 'CHANGED_SINCE_BASELINE', 'content changed but status reviewed')
        else:
            fr = e.get('fresh_reviews') or []
            if fr:
                bad = [r for r in fr if r.get('content_hash') != e.get('content_hash') or r.get('verdict') != 'PASS']
                if bad:
                    add(e, 'review_evidence', 'FRESH_REVIEW_UNBOUND', f'{len(bad)} fresh review(s) not PASS or not bound to the current hash')
                keys = {str(r.get('answer')) for r in fr if r.get('answer') is not None}
                if keys and keys != {str(e['key'])}:
                    add(e, 'review_evidence', 'FRESH_BLIND_MISMATCH', f'fresh solver answers {sorted(keys)} vs key {e["key"]}')
            elif not e.get('baseline_current_external_review'):
                add(e, 'review_evidence', 'NO_INDEPENDENT_REVIEW', e.get('status_reason', ''))
            if e.get('overlay') and not e.get('overlay_applied'):
                add(e, 'review_evidence', 'OVERLAY_NOT_APPLIED', 'overlay present but not applied')
    # ---------- passages
    by_pid = defaultdict(list)
    for e in recs:
        if e.get('passage_id'):
            by_pid[(e['source'], e['passage_id'])].append(e)
    for e in reviewed:
        if e['section'] in VERBAL and e['source'] == 'Claude':
            if e.get('passage_id') not in passages:
                add(e, 'passage', 'PASSAGE_UNRESOLVED', str(e.get('passage_id')))
            if e.get('passage_id') in superseded:
                add(e, 'passage', 'ON_SUPERSEDED_PASSAGE', e['passage_id'])
    pc = load(ROOT / 'audits' / 'passage_consistency_act_english_2026-10-28.json')
    accepted_text = set()
    for k in pc['findings'].get('acceptable_text_no_item_needed', {}):
        n, u = k.split()
        accepted_text.add((f'CLD-P-ACT-E-{n}', int(u.lstrip('u'))))
    resf = COMB / 'audits' / f'final-audit-resolutions-{TODAY}.json'
    resolutions = load(resf) if resf.exists() else {}
    for k in resolutions.get('accepted_text_spans_chatgpt_english', {}):
        pid_, lab = k.split()
        accepted_text.add((pid_, lab))
    overrides = {frozenset((o['a'], o['b'])): o for o in resolutions.get('duplicate_overrides_retained', [])}
    orphan = []
    for (src, pid), items in by_pid.items():
        live = [x for x in items if x['status'] == 'reviewed_draft']
        if not live or live[0]['section'] != 'English':
            continue
        t = live[0].get('passage') or ''
        if src == 'Claude':
            spans = {int(n): s for n, s in UL.findall(t)}
            tested = {x.get('underline') for x in live}
        else:
            spans = {'E' + n: s for n, s in EDIT.findall(t)}
            spans.update({lab: s for lab, s in re.findall(r'\[([A-Z]\d+): ([^\]]*)\]', t)})
            tested = set()
            for x in live:
                for m in re.finditer(r'\b(?:span |for )?([A-Z]\d+)\b', x['stem'] + ' ' + str(x.get('edit_span') or '')):
                    tested.add(m.group(1))
        for n, s in spans.items():
            if n not in tested and (pid, n) not in accepted_text:
                orphan.append({'source': src, 'passage_id': pid, 'span': n, 'text': s,
                               'held_items_on_span': [x['id'] for x in items if x['status'] != 'reviewed_draft' and
                                                      (x.get('underline') == n)]})
    sizes = Counter()
    for (src, pid), items in by_pid.items():
        live = [x for x in items if x['status'] == 'reviewed_draft']
        if live and live[0]['section'] in ('English', 'Reading'):
            sizes[f"{live[0]['exam']} {live[0]['section']}"] += 0
    set_sizes = defaultdict(list)
    for (src, pid), items in by_pid.items():
        live = [x for x in items if x['status'] == 'reviewed_draft']
        if live and live[0]['section'] in ('English', 'Reading'):
            set_sizes[f"{live[0]['exam']} {live[0]['section']}"].append(len(live))
    # ---------- insertion
    for e in reviewed:
        for p in insertion_problems(e):
            add(e, 'insertion', p['code'], f"{p['choice']}: {p['text']}")
    # ---------- hints
    for e in reviewed:
        if e['source'] != 'Claude' or not e['choices']:
            continue
        key_txt = str(e['choices'].get(e['key'], ''))
        others = ' '.join(str(v) for k, v in e['choices'].items() if k != e['key']).lower()
        if key_txt in ('NO CHANGE',) or len(key_txt) < 4:
            continue
        for h in e.get('hints') or []:
            if key_txt.lower().strip(' .') in str(h).lower() and key_txt.lower().strip(' .') not in others:
                add(e, 'hints', 'HINT_CONTAINS_KEY', f'hint repeats the key text: {h[:100]}')
    # ---------- duplicates
    exact = defaultdict(list)
    for e in reviewed:
        exact[(e['section'], e.get('content_hash'))].append(e['id'])
    exact_dups = [v for v in exact.values() if len(v) > 1]
    for v in exact_dups:
        for i in v[1:]:
            add(next(x for x in reviewed if x['id'] == i), 'duplicates', 'EXACT_DUPLICATE', f'same content as {v[0]}')
    stem_ch = defaultdict(list)
    for e in reviewed:
        k = (e['section'], re.sub(r'\W+', ' ', plain(e['stem'])).lower().strip(),
             tuple(sorted(re.sub(r'\W+', ' ', str(v)).lower().strip() for v in e['choices'].values())), plain(e.get('passage', ''))[:200])
        stem_ch[k].append(e['id'])
    for v in stem_ch.values():
        if len(v) > 1:
            for i in v[1:]:
                add(next(x for x in reviewed if x['id'] == i), 'duplicates', 'SAME_STEM_AND_CHOICES', f'same stem, choices and passage start as {v[0]}')
    screen = load(COMB / 'audits' / 'dup-screen-post-baseline.json')
    adj = {}
    for f in sorted((COMB / 'audits').glob('dup-adjudication*.json')):
        for p in load(f)['pairs']:
            adj[frozenset((p['a'], p['b']))] = (p['verdict'], f.name)
    status = {e['id']: e['status'] for e in recs}
    pairs_live, pairs_unadj, pairs_dup = 0, [], []
    for p in screen['pairs']:
        a, b = p['claude_id'], p['other_id']
        if status.get(a) != 'reviewed_draft' or status.get(b) != 'reviewed_draft':
            continue
        pairs_live += 1
        v = adj.get(frozenset((a, b)))
        if v is None:
            pairs_unadj.append(p)
            add(next(x for x in reviewed if x['id'] == a), 'duplicates', 'NEAR_DUP_UNADJUDICATED', f"{b} similarity {p['item_similarity']}")
        elif v[0] != 'distinct':
            pairs_dup.append(dict(p, adjudication=v))
            add(next(x for x in reviewed if x['id'] == a), 'duplicates', 'NEAR_DUP_ADJUDICATED_DUPLICATE', f"{b} ({v[1]})")
    whole = COMB / 'audits' / 'dup-screen-whole-bank.json'
    if whole.exists():
        for p in load(whole)['pairs']:
            a_, b_ = p['a'], p['b']
            if status.get(a_) != 'reviewed_draft' or status.get(b_) != 'reviewed_draft':
                continue
            k = frozenset((a_, b_))
            ea = next(x for x in reviewed if x['id'] == a_)
            if not p['adjudicated']:
                add(ea, 'duplicates', 'WHOLEBANK_PAIR_UNADJUDICATED', f"{b_} similarity {p['similarity']}")
            elif p['adjudicated'] not in ('distinct', 'baseline') and k in overrides:
                add(ea, 'duplicates', 'DUPLICATE_RETAINED_BY_OVERRIDE', f"{b_}: {overrides[k]['decision']}", blocking=False)
            elif p['adjudicated'] not in ('distinct', 'baseline'):
                add(ea, 'duplicates', 'WHOLEBANK_ADJUDICATED_DUPLICATE', b_)
    # ---------- summary
    blocking = [f for f in find if f['blocking']]
    counts = Counter(f"{e['exam']} {e['section']}" for e in reviewed)
    report = {
        'audit': 'final whole-bank audit (structure, review evidence, passage consistency, insertion, hints, duplicates)',
        'generated_at': dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        'records': len(recs), 'reviewed_draft': dict(sorted(counts.items())),
        'findings_total': len(find), 'blocking_total': len(blocking),
        'blocking_by_check': dict(Counter(f"{f['check']}:{f['code']}" for f in blocking)),
        'nonblocking_by_check': dict(Counter(f"{f['check']}:{f['code']}" for f in find if not f['blocking'])),
        'act_english_orphan_spans': orphan,
        'passage_set_sizes': {k: {'passages': len(v), 'min': min(v), 'max': max(v), 'mean': round(sum(v) / len(v), 1),
                                  'sets_under_5': sum(1 for n in v if n < 5)} for k, v in set_sizes.items()},
        'near_duplicate_pairs_between_reviewed_records': pairs_live,
        'near_duplicate_pairs_unadjudicated': len(pairs_unadj),
        'near_duplicate_pairs_adjudicated_duplicate': pairs_dup,
        'exact_duplicate_groups': exact_dups,
        'findings': find,
    }
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(report, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('records', 'reviewed_draft', 'findings_total', 'blocking_total', 'blocking_by_check',
                                            'nonblocking_by_check', 'near_duplicate_pairs_between_reviewed_records',
                                            'near_duplicate_pairs_unadjudicated')}, indent=1))
    print('orphan ACT English spans:', len(orphan))


if __name__ == '__main__':
    main()
