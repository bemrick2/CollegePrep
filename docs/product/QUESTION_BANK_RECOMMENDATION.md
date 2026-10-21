# Question bank: how many fresh questions each weekly plan needs

Written 2026-10-21 for the owner's bank-size decision (launch blocker A1). This is a sizing recommendation only. No questions were generated.

## Definitions

- **Unique (fresh) question:** one this student has never been shown. Each student draws from the same pool, so the bank must cover **one student's whole horizon**; it doesn't need to cover all students combined.
- **Repeat:** a question shown before. Repeats are allowed as review and count toward the weekly goal, but they are **never evidence of improvement**. Trends use first answers only, and a check section that contains repeats isn't compared (`PRACTICE_READINESS.md`).
- **Reserved assessment questions (proposed):** a pool for the starting benchmark and every progress check, kept out of practice entirely, so each check uses questions the student hasn't seen.
  - **This is not how the app works today.** Today only each section's *next* mini check is held out of practice (ACT 3/4/3/3, SAT 4/4; `engine/freshness.ts`). The starting benchmark draws from the shared pool.
  - A fully reserved pool needs the server-side holdout (CR-23, #218 B1) or a code change to mark items as assessment-only. The sizing below assumes that change.
- **Check sizes:** the starting benchmark and mini check come from the code [Certain, `engine/benchmark.ts` `PER_SECTION`]. The full-form row is the real test length from `CONTENT_PLAN.md` §2–3: the code caps a "full" check at 99 per section, which in practice means the whole bank.

  | Check | ACT | SAT |
  |---|---|---|
  | Starting benchmark | 27 | 18 |
  | Mini check | 13 | 8 |
  | Full-length form, if one exists | 171 (50 + 45 + 36, plus 40 science) | 98 (54 + 44) |

- **Check cadence** [Certain, code]:
  - A mini check every 35 days, so 2 in 12 weeks and 10 in a year.
  - A full check every 70 days, only once a held-out full form exists. Today `FULL_FORM_READY = false`, so full checks fall back to minis.
- **Headroom: +15%** on practice only [Guessing]. The planner targets weak skills and difficulty bands, so a student doesn't use the bank evenly. Calibrate it after launch.
  - `CONTENT_PLAN.md`'s earlier ≈430 / ≈410 (8 weeks at 40) added the 15% to check items too. Here, reserved items are counted exactly, with no headroom.
- **Known limit:** checks adapt their difficulty, so 13 (ACT) or 8 (SAT) mini items per check may not cover every difficulty a check reaches. A larger reserved pool per check makes a fully fresh check more likely.

## Unique questions needed, per exam

Each row gives:
- **Practice shown:** the weekly goal × weeks.
- **Practice unique (all fresh):** every practice question new, plus headroom.
- **Practice unique (25% review):** a quarter of each week deliberately spent on spaced repeats.
- **Reserved:** starting benchmark plus mini checks.

**Total = unique practice + reserved.** ACT and SAT need separate banks, so each total is per exam.

### ACT

| Plan | Practice shown | Practice unique (all fresh) | Practice unique (25% review) | Reserved | **Total, all fresh** | **Total, 25% review** |
|---|---|---|---|---|---|---|
| 20 a week, 12 weeks | 240 | 276 | 207 | 53 | **329** | **260** |
| 40 a week, 12 weeks | 480 | 552 | 414 | 53 | **605** | **467** |
| 60 a week, 12 weeks | 720 | 828 | 621 | 53 | **881** | **674** |
| 20 a week, 1 year | 1,040 | 1,196 | 897 | 157 | **1,353** | **1,054** |
| 40 a week, 1 year | 2,080 | 2,392 | 1,794 | 157 | **2,549** | **1,951** |
| 60 a week, 1 year | 3,120 | 3,588 | 2,691 | 157 | **3,745** | **2,848** |

### SAT

| Plan | Practice shown | Practice unique (all fresh) | Practice unique (25% review) | Reserved | **Total, all fresh** | **Total, 25% review** |
|---|---|---|---|---|---|---|
| 20 a week, 12 weeks | 240 | 276 | 207 | 34 | **310** | **241** |
| 40 a week, 12 weeks | 480 | 552 | 414 | 34 | **586** | **448** |
| 60 a week, 12 weeks | 720 | 828 | 621 | 34 | **862** | **655** |
| 20 a week, 1 year | 1,040 | 1,196 | 897 | 98 | **1,294** | **995** |
| 40 a week, 1 year | 2,080 | 2,392 | 1,794 | 98 | **2,490** | **1,892** |
| 60 a week, 1 year | 3,120 | 3,588 | 2,691 | 98 | **3,686** | **2,789** |

### Full-length checks

Full checks change the reserved count a lot, because **each full check needs its own unseen form**. A form can't be reused for the same student.
- **12 weeks**, with one full check replacing the second mini: reserved is ACT 211 and SAT 124, instead of 53 and 34.
- **1 year** on the 70-day full cadence means 5 full checks plus 5 minis: reserved is ACT 947 and SAT 548.

That is why the full check falls back to a mini until a held-out form exists. One full form per exam is enough for a single full check in a 12-week plan, and for nothing more.

### Today

There are 58 items: ACT 38, SAT 20. That is less than one week at 40, even before the starting benchmark uses 27 ACT or 18 SAT items.

## Recommendation

1. **Launch with one exam at "40 a week, 12 weeks, 25% review": about 470 unique items for ACT (448 for SAT)**, or about 600 (ACT 605, SAT 586) if every practice question should be fresh.
   - The other option from `CONTENT_PLAN.md` §6 Q1 is both exams at the 8-week minimum: ≈430 ACT plus ≈410 SAT, about 840 items in all. That is about 1.4–1.8 times the one-exam effort, spread over two thinner banks.
   - That matches the default weekly goal and the 12-week horizon in `CONTENT_PLAN.md`.
   - When a student runs out of fresh questions, the app already says so plainly.
   - Launching both exams doubles the authoring work. The table's numbers are per exam.
2. **Don't promise a year of fresh practice at launch.** A year at 40 needs about 1,900–2,550 unique items per exam, about 4.2 times the 12-week bank. Grow toward it by measured demand.
3. **Keep the full check on the mini fallback** until a held-out full form per exam is authored and reviewed: 171 ACT or 98 SAT items, and never used in practice.
4. **Make 25% review a product rule, not a shortfall.** The app already labels review repeats "Keeping it sharp", and they already count toward the goal. It cuts the unique need by about a quarter, and spaced review helps retention [Likely].
5. **Author to the blueprint split** in `CONTENT_PLAN.md` §3: ACT English 29%, Math 26%, Reading 21%, Science 23%; SAT Reading and Writing 55%, Math 45%. Aim for roughly a third each of easy, medium and hard.
6. **Reserved items come first and never enter practice.** Author the 53 (ACT) or 34 (SAT) check items before the practice pool, and mark them assessment-only. That needs CR-23 or the code change above, so the holdout never depends on what's left over.

## Human review and licensing (every item, including the existing 58)

**Review:** CONTENT_PLAN §5 stages 3–8, recorded in the editorial ledger (#207). Each item needs:
- a rights check;
- two blind solves by different people, neither of them the author;
- a content audit;
- a fairness review;
- a copy edit and accessibility check;
- approval by a named content lead.

The ledger enforces this today, and human-approved is currently 0 of 58.

**Effort** [Guessing, from CONTENT_PLAN]: about 50–65 person-minutes per item (author plus reviewers).

| Bank | Person-hours |
|---|---|
| ~470 items | ~390–510 |
| ~600 items | ~500–650 |
| ~2,500 items | ~2,100–2,700 |

SAT Reading and Writing needs a short passage for every item, which is its largest cost.

**Licensing:** every published item must be one of:
- original;
- public domain;
- federal government work;
- CC BY or CC BY-SA, with the required attribution.

Real ACT or SAT items, and passages under copyright, need a written license [Certain that official items are copyrighted by ACT and College Board; any license terms would need counsel].

The server-side rights gate (CR-24, #218 B2) isn't built yet. Until it is, the editorial ledger's stage 3 is the only licence check.

**Decisions for the owner:**
- one exam or both;
- the 25% review rule;
- whether AI-drafted items are acceptable when every item passes human stages 3–8;
- who the content lead is;
- whether to author or license a full-length form.
