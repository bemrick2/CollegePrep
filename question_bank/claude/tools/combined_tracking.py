#!/usr/bin/env python3
"""Per-section tracking for the combined (ChatGPT + Claude) targets set on 2026-10-27.

Writes audits/combined_tracking.json and prints a table. Everything is recomputed from the banks, audits/retired.json,
the review files and the drafts, so the numbers cannot drift from the saved state.

Combined baselines come from the user's message; they already include this workstream's complete export
(generated 2026-10-27T01:17:30Z: ACT Math 774, ACT English 262, ACT Reading 219, SAT R&W 263, SAT Math 0).
The other workstream's banks and the combined screening file were not available here, so anything that needs them
(combined SAT Math baseline, combined reconciliation, cross-bank duplicate screening) is reported as pending.
"""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORT_AT = '2026-10-27T01:17:30+00:00'
SECTIONS = {
    # bank: (label, combined target, combined baseline given by the user, items of ours inside that baseline)
    'sat_math': ('SAT Math', 1000, None, 0),
    'sat_reading_writing': ('SAT Reading & Writing', 1000, 569, 263),
    'act_english': ('ACT English', 1000, 573, 262),
    'act_reading': ('ACT Reading', 1000, 535, 219),
    'act_math': ('ACT Math (paused: targeted work only)', None, 1568, 774),
}


def load(p, default=None):
    p = ROOT / p
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default


def main() -> None:
    retired = (load('audits/retired.json', {}) or {}).get('retired', {})
    exported = set(load('audits/export_2026-10-27_live_ids.json', {'ids': []})['ids'])
    out = {'generated_at': dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
           'export_cutoff': EXPORT_AT,
           'pending': ['combined screening file (prep-and-price-combined-bank-screening.zip) not available in this '
                       'environment: combined-count reconciliation and cross-bank duplicate screening against the '
                       'other workstream are pending',
                       'SAT Math combined baseline not given and not visible here; SAT Math figures are this workstream only'],
           'sections': {}}
    for bank, (label, target, base, ours_in_base) in SECTIONS.items():
        qs = load(f'banks/{bank}.json', {'questions': []})['questions']
        ids = {q['id'] for q in qs}
        new = [q for q in qs if q['created_at'] > EXPORT_AT]
        new_live = [q for q in new if q['id'] not in retired]
        old_held = [i for i in ids if i in retired and i in exported]  # live at export, held or retired since
        new_held = [q['id'] for q in new if q['id'] in retired]
        live = [q for q in qs if q['id'] not in retired]
        reviewed = [q for q in live if (q.get('validation') or {}).get('blind_answer') is not None]
        human = [q for q in live if str(q.get('human_review') or '').lower() in ('approved', 'human_approved')]
        # candidates drafted but not yet reviewed: draft batches without a review file
        unreviewed = 0
        for d in sorted((ROOT / 'drafts' / bank).glob('batch-*.json')):
            n = d.stem.split('-')[1]
            if not (ROOT / 'reviews' / bank / f'batch-{n}.review.json').exists():
                unreviewed += len(json.loads(d.read_text(encoding='utf-8')).get('candidates', []))
        row = {'label': label, 'combined_target': target,
               '1_combined_starting_baseline': base if base is not None else 'pending (not provided / not visible)',
               '2_verified_new_additions_since_export': len(new_live),
               '3_holds_removals_duplicates_since_export': {'baseline_items_held_or_retired': len(old_held),
                                                            'new_items_held_or_retired': len(new_held),
                                                            'ids': sorted(old_held) + sorted(new_held)},
               'this_workstream_live_now': len(live)}
        if base is not None:
            total = base + len(new_live) - len(old_held)
            row['4_reconciled_total'] = f'{total} (provisional: other workstream changes since its baseline not visible)'
            row['4_remaining_to_target'] = (target - total) if target else 'n/a (paused)'
        else:
            row['4_reconciled_total'] = f'pending; this workstream alone: {len(live)}'
            row['4_remaining_to_target'] = f'pending; at most {target - len(live)} if the other workstream has none'
        row['5_current_version_independently_ai_reviewed'] = len(reviewed)
        row['6_unreviewed_candidates'] = unreviewed
        row['6_human_approved'] = len(human)
        out['sections'][bank] = row
    (ROOT / 'audits' / 'combined_tracking.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for bank, r in out['sections'].items():
        print(f"{r['label']}: baseline {r['1_combined_starting_baseline']}; new {r['2_verified_new_additions_since_export']}; "
              f"held/removed {len(r['3_holds_removals_duplicates_since_export']['ids'])}; total {r['4_reconciled_total']}; "
              f"remaining {r['4_remaining_to_target']}; AI-reviewed {r['5_current_version_independently_ai_reviewed']}; "
              f"unreviewed {r['6_unreviewed_candidates']}; human-approved {r['6_human_approved']}")


if __name__ == '__main__':
    main()
