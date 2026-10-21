# Practice readiness audit

Audited 2026-10-21 on `main`, with every count computed from the repository. This audit added no questions and turned on no score prediction.

Status key:
- **Implemented:** in the code.
- **Local:** checked by tests, including `scripts/local/live_stack.sh test` (real SQL, RLS and RPCs on a disposable PostgreSQL).
- **Hosted:** checked on the hosted project. Nothing is hosted-tested: hosted is paused and deployment is held.

| Requirement | Demo | Live code | Tested | Gap or blocker |
|---|---|---|---|---|
| **Only reviewed questions are served** | `reviewedOnly`: the item's content hash must match an approval | CR-21 gate: `status = 'published'` and `review_current` (migration `20261007140000`) | Local: the seed records approvals through `approve_practice_question` | Not applied on hosted. The approvals are **AI review**: 58 of 58 items have two blind solves plus an audit. **Human-approved: 0 of 58.** The human ledger exists (#207), but no content lead has been named (A2) |
| **Only licensed questions are served** | All 58 are original items; seed attribution is "Prep & Price original demo item" | `license` column exists, but nothing checks it | none | **CR-24, the rights gate, is open** (#218 B2). The stage 3 rights check in the editorial ledger needs an allowed license |
| **Questions reserved for assessment never appear in practice** | Each section's next mini check (ACT 3/4/3/3, SAT 4/4) is held out of the practice pool | **Fixed in this change.** Until now the server's session could serve held questions. `LiveSource.startSession` now drops them using the demo's rule, then tops up with fresh, non-held questions | Local (`journeys.local.test.ts`): no held question appears, and every item is fresh | Interim client rule. The server-side holdout is **CR-23** (#218 B1) |
| **Repeats are clearly distinguished** | `seen_before` on each item; "Seen before" label | Same, from the student's prior attempts | Local (`liveSource.local.test.ts`: "a new session marks exactly the questions already answered as seen before") | none |
| **Repeats never count as improvement** | Trends use first answers only. A check section that contains repeats isn't compared | Same, on the client | Unit tests (`improving`, `progressCheck`, `freshness`) | Server-side first-answer metrics are CR-23 |
| **Progress checks use fresh questions first** | `pickNext` takes unseen questions first; repeats only when a section runs out, and then the section is flagged | Same | Unit tests | A held-out **full-length** form doesn't exist, so "full" checks fall back to a mini (`FULL_FORM_READY = false`) |
| **Honest when fresh questions run out** | "No new practice questions left". It now says how many are held for the next check, instead of claiming every question was answered | Same; the practice screen explains when every remaining fresh question is held for the check | Component tests (`FreshContentNotice.test.tsx`, `heldForCheck.test.tsx`) | none |
| **No score prediction** | `PRACTICE_ESTIMATES_VALIDATED = false`. Percent right is labeled practice and never converted to an ACT/SAT score | Same | Unit tests | Stays off until a scoring model is validated (CR-3) |

## The bank against the weekly cycle

There are 58 served items. Per section, counting what the next mini check holds out:

| Exam | Items | Held for the next check | Fresh for practice before any benchmark | Starting benchmark size |
|---|---|---|---|---|
| ACT | 38 (English 10, Math 12, Reading 8, Science 8) | 13 | 25 | 27 |
| SAT | 20 (Reading and Writing 10, Math 10) | 8 | 12 | 18 |

What this means for a student:
- A student who takes the starting benchmark first has seen 27 of 38 ACT items, or 18 of 20 SAT items.
- What's left is fewer than one mini check holds. So practice is review-only from day one, and the next check can't be fully fresh.
- The app says both plainly. A student who practises before the benchmark gets 25 (ACT) or 12 (SAT) fresh items. The default weekly goal is 40, so that's less than one week.

This is launch blocker A1 (`CONTENT_PLAN.md`: about 430 ACT and 410 SAT items minimum). Per the owner's instruction, no replacement bank was generated. The weekly goal wasn't lowered to hide the shortage.
