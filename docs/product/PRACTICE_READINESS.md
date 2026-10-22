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
| **Questions reserved for assessment never appear in practice** | A **fixed reserved pool** (CR-23 rule, `engine/freshness.ts` `reservedIds`): ACT 3/4/3/3, SAT 4/4 per section, configurable (`RESERVED_PER_SECTION`). Practice never uses it, seen or not; a practice attempt on one is refused and a check attempt on anything else is refused | `LiveSource.startSession` drops reserved questions from the server's pick and fills the time with practice questions only (fresh first, then repeats). The reserve is the question's `pool` once the server serves it, else the same fixed client assignment | Unit (`freshness.test.ts`), demo (`reservedPool.test.tsx`), local (`journeys.local.test.ts`) | **Server enforcement is CR-23, being written by Research (#218).** Until it merges, the live server doesn't refuse a practice attempt on a reserved item; only the client keeps them apart |
| **Repeats are clearly distinguished** | `seen_before` on each item; "Seen before" label | Same, from the student's prior attempts | Local (`liveSource.local.test.ts`: "a new session marks exactly the questions already answered as seen before") | none |
| **Repeats never count as improvement** | Trends use first answers only. A check section that contains repeats isn't compared | Same, on the client | Unit tests (`improving`, `progressCheck`, `freshness`) | Server-side first-answer metrics are CR-23 |
| **Progress checks use only reserved questions, fresh first** | Checks draw from the reserved pool only: unseen reserved first, then reserved repeats (that section gets no verdict). Fewer reserved than the check asks for: the section is shorter, and says so. None: the section isn't measured. Practice questions never fill a check | Same | Unit and component tests (`freshness.test.ts`, `reservedPool.test.tsx`) | A **full-length** reserved form doesn't exist (`FULL_FORM_READY = false`). With today's bank the starting check is shorter (ACT 13 of 27, SAT 8 of 18) and the first mini is all repeats, so it gets no verdict. That is the bank shortage (A1), shown, not hidden |
| **Honest when fresh questions run out** | "No new practice questions left" names how many are set aside for checks and never says every question was answered | Same; the practice screen explains when only reserved questions are left | Component tests (`FreshContentNotice.test.tsx`, `heldForCheck.test.tsx`) | none |
| **No score prediction** | `PRACTICE_ESTIMATES_VALIDATED = false`. Percent right is labeled practice and never converted to an ACT/SAT score | Same | Unit tests | Stays off until a scoring model is validated (CR-3) |

## The bank against the weekly cycle

There are 58 served items. With the fixed reserved pool (one mini check's worth per section, the default):

| Exam | Items | Reserved (checks only) | Practice | Starting check, as the bank allows |
|---|---|---|---|---|
| ACT | 38 (English 10, Math 12, Reading 8, Science 8) | 13 | 25 | 13 of 27 (shortened) |
| SAT | 20 (Reading and Writing 10, Math 10) | 8 | 12 | 8 of 18 (shortened) |

What this means for a student:
- Practice has 25 (ACT) or 12 (SAT) fresh items, whatever the student does first. The default weekly goal is 40, so that's less than one week; after that, practice is review.
- The starting check uses all 13 (ACT) or 8 (SAT) reserved items and says it's shorter than usual. The first mini check can only repeat them, so it says so and gives no verdict.
- Reserving more (`RESERVED_PER_SECTION`) lengthens checks but shrinks practice; with 38 items there is no setting that gives both. The planning target for the bank workstream is `web/src/lib/contentTarget.ts` (ACT, 40 a week, 12 weeks: 414 practice + 53 reserved = 467 at 25% planned review).

This is launch blocker A1 (see `QUESTION_BANK_RECOMMENDATION.md`; new items enter through `QUESTION_IMPORT_CONTRACT.md`). Per the owner's instruction, no replacement bank was generated. The weekly goal wasn't lowered to hide the shortage.
