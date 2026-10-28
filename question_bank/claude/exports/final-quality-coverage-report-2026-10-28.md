# Final quality and coverage report: reconciled Prep & Price question bank

Generated 2026-10-28T03:23:05+00:00 from branch `ccr-78c91309-anlh8e`, source commit `fd098654de6c422d80a934909683bb8228fc85fd` (the package files themselves are committed in the next commit).

**Every record is an AI-generated draft. None is human-approved. Difficulty is provisional (AI and author estimates; no student data). Nothing has been imported, deployed or published.**

## Counts (reconciled bank)

| Section | Target | Reviewed drafts (usable) | Claude | ChatGPT | Pending review | Hold | Reserved duplicate | Retired |
|---|---|---|---|---|---|---|---|---|
| SAT Math | 1000 | **1000** | 1000 | 0 | 0 | 0 | 31 | 0 |
| SAT Reading and Writing | 1000 | **1008** | 695 | 313 | 0 | 2 | 22 | 15 |
| ACT English | 1000 | **1002** | 691 | 311 | 0 | 0 | 34 | 11 |
| ACT Reading | 1000 | **1003** | 686 | 317 | 0 | 0 | 39 | 1 |
| ACT Math | paused | **1438** | 759 | 679 | 178 | 16 | 43 | 0 |

Only `reviewed_draft` records count toward targets: the current content version has independent AI blind-review evidence (no key) and no open hold.

## Coverage by reporting category (reviewed drafts)

### SAT Math

| Category | Items | Share | Of which inferred from source skill | Published weight (approx.; verify) |
|---|---|---|---|---|
| Advanced Math | 311 | 31% | 0 | ~35% |
| Algebra | 290 | 29% | 0 | ~35% |
| Problem-Solving and Data Analysis | 203 | 20% | 0 | ~15% |
| Geometry and Trigonometry | 196 | 20% | 0 | ~15% |

### SAT Reading and Writing

| Category | Items | Share | Of which inferred from source skill | Published weight (approx.; verify) |
|---|---|---|---|---|
| Information and Ideas | 292 | 29% | 47 | ~26% |
| Craft and Structure | 269 | 27% | 48 | ~28% |
| Standard English Conventions | 238 | 24% | 35 | ~26% |
| Expression of Ideas | 209 | 21% | 33 | ~20% |

### ACT English

| Category | Items | Share | Of which inferred from source skill | Published weight (approx.; verify) |
|---|---|---|---|---|
| Conventions of Standard English | 491 | 49% | 65 | 38-43% |
| Production of Writing | 334 | 33% | 70 | 38-43% |
| Knowledge of Language | 177 | 18% | 25 | 13-19% |

### ACT Reading

| Category | Items | Share | Of which inferred from source skill | Published weight (approx.; verify) |
|---|---|---|---|---|
| Key Ideas and Details | 432 | 43% | 89 | 55-60% |
| Craft and Structure | 330 | 33% | 50 | 25-30% |
| Integration of Knowledge and Ideas | 241 | 24% | 25 | 13-18% |

Some ChatGPT records give a skill but no reporting category; their category is inferred from the skill name (`reporting_category_inferred`, mapping in `tools/build_final_package.py`). The published weights are approximate and must be checked against the current official specifications.

Main coverage gaps against the published weights: ACT Reading is light on Key Ideas and Details (43% vs 55-60%) and heavy on Integration of Knowledge and Ideas; ACT English is heavy on Conventions (49%) and light on Production of Writing (33% vs 38-43%); SAT Reading and Writing is close to the official split (Standard English Conventions slightly light); SAT Math is heavier on Problem-Solving and Geometry, and lighter on Algebra and Advanced Math, than the official split. These are bank-level shares; a practice form would be assembled to the blueprint.

## Difficulty estimates (provisional)

| Section | Author labels (easy / medium / hard / none) | Blind-solver estimate of % correct: median (IQR) | Solver opinions (easy / medium / hard) |
|---|---|---|---|
| SAT Math | 149 / 707 / 144 / 0 | 55% (45-65%), n=1000 | 174 / 681 / 145 |
| SAT Reading and Writing | 389 / 580 / 35 / 4 | 78% (70-85%), n=695 | 421 / 271 / 3 |
| ACT English | 501 / 478 / 23 / 0 | 75% (70-82%), n=691 | 416 / 272 / 3 |
| ACT Reading | 438 / 527 / 34 / 4 | 82% (75-86%), n=686 | 489 / 195 / 2 |
| ACT Math | 355 / 720 / 363 / 0 | 60% (50-75%), n=715 | 277 / 412 / 70 |

Solver estimates come from AI agents, not students. Verbal items skew easy-to-medium in AI solves. "Hard" labels were not forced. All difficulty data needs student calibration.

## Final whole-bank audit

Run by `tools/final_audit.py` over 5843 reconciled records. Blocking findings: **0**. Nonblocking: 6 (structure:STALE_UNDERLINE_ON_ESSAY_ITEM 4, duplicates:DUPLICATE_RETAINED_BY_OVERRIDE 2).

| Check | What was verified | Result |
|---|---|---|
| Structure | four distinct, non-empty choices A-D with the key among them (or accepted answers for student-produced responses), stem, explanation, passage for verbal items, ACT English underline present | pass (4 stale underline numbers on essay-level items; nonblocking) |
| Review evidence | Claude: bank validation PASS, blind answer = key, review file present, second verbal solver = key; ChatGPT: current-version external PASS or fresh PASS reviews bound to the content hash, overlay applied | pass |
| Passage consistency | passages resolve; no reviewed item on a superseded passage; every ACT English span with an error is tested by a reviewed item or recorded as acceptable text | pass (5 ChatGPT span labels with no item, none an untested error) |
| Literal insertion | every option inserted at its blank or underline; seams checked for missing or doubled spaces, doubled punctuation, space before punctuation | pass after 10 repairs |
| Hints | no hint repeats the key's distinctive wording | pass after 1 repair |
| Duplicates | exact duplicates; post-baseline screen (203 pairs between reviewed records); new whole-bank pairwise and math-signature screen; independent adjudication of every unadjudicated pair | pass after 4 quarantines; 2 pairs kept by recorded override |

### Resolved during the audit

- CLD-SAT-RW-000053 superseded by CLD-SAT-RW-000724 (two fresh blind solves)
- CLD-SAT-RW-000117 superseded by CLD-SAT-RW-000725 (two fresh blind solves)
- CLD-SAT-RW-000118 superseded by CLD-SAT-RW-000726 (two fresh blind solves)
- CLD-SAT-RW-000127 superseded by CLD-SAT-RW-000727 (two fresh blind solves)
- CLD-SAT-RW-000136 superseded by CLD-SAT-RW-000728 (two fresh blind solves)
- CLD-SAT-RW-000145 superseded by CLD-SAT-RW-000729 (two fresh blind solves)
- CLD-SAT-RW-000172 superseded by CLD-SAT-RW-000730 (two fresh blind solves)
- CLD-SAT-RW-000258 superseded by CLD-SAT-RW-000731 (two fresh blind solves)
- CLD-SAT-RW-000267 superseded by CLD-SAT-RW-000732 (two fresh blind solves)
- CLD-ACT-R-000523 superseded by CLD-ACT-R-000722 (two fresh blind solves)
- CLD-ACT-E-000469 superseded by CLD-ACT-E-000736 (two fresh blind solves)
- CLD-SAT-M-000585 quarantined as a duplicate of CLD-ACT-M-000243; replaced by CLD-SAT-M-001031 (sat_math 93)
- CLD-ACT-M-000736 quarantined as a duplicate of PP-MATH-000084
- PP-MATH-000182 quarantined as a duplicate of PP-MATH-000689
- PP-MATH-000619 quarantined as a duplicate of CLD-ACT-M-000386

Earlier in this phase: the Seneca Village factual overstatement (passage CLD-P-ACT-E-000063) was corrected from Central Park Conservancy sources as CLD-P-ACT-E-000068, and all nine items were re-reviewed and superseded. 14 untested error spans in ACT English passages received their own reviewed items.

## Open issues (not resolved; need human decision)

- Template duplicate kept by override: PP-VERBAL-20261022-F-017 / PP-VERBAL-20261022-I-011. Same subject-verb template (plural subject + "were") on two different essays. Each item tests a deliberate error span in its own passage ("The two pots [H6: was]"); quarantining either item would leave an untested error visible in its passage, and removing either 10-item passage set is disproportionate to template similarity. Recommended human action: rewrite one span to test a different rule, with a fresh blind review.
- Template duplicate kept by override: PP-VERBAL-20261022-C-002 / PP-VERBAL-20261022-K-001. Near-identical singular-subject-with-plural-modifier sentences on two different essays ("A stack of blue scraps [were]"); same constraint as above.
- Four Claude ACT English essay-level items (CLD-ACT-E-000445, -000452, -000456, -000471) carry an underline number that does not exist in their passage. The stems refer to sentences or the whole essay; the items render with no highlight. Recommended: set underline to null on import.
- In the ChatGPT edit-span format the span label (for example "[E9: had counted]") is part of the passage text; a span with no item shows a label that no question uses. None of these five shows an untested error. Recommended: strip labels of untested spans at render time.
- On hold: CLD-SAT-RW-000100 (SAT Reading and Writing): carried from baseline: HISTORICAL_KEY_DISPUTE, APPOSITIVE_EDITORIAL_DISPUTE
- On hold: PP-VERBAL-20261022-H-007 (SAT Reading and Writing): fresh review found a problem: Option D 'dates, and,' is arguably also correct: 'she recorded dates, and, in the second, she described changes in leaf ; Two defe
- ACT Math: 178 records pending review and 16 on hold; bulk generation paused, so these were not worked.
- ChatGPT overlay repairs (display and content) are applied in this package but the ChatGPT source files are unchanged; the owning workstream must adopt them.

## Completed checks versus outstanding work

**Completed (AI only):** author self-check; two separate blind AI solves per verbal item (one adversarial with fact-checking) and one blind solve plus scripted recomputation per Claude math item; near-duplicate screens with independent AI adjudication; the final structural, evidence, passage, insertion, hint and duplicate audit. All solvers are AI agents of the same model family working from answer-free packets, so they are not truly independent of the author.

**Outstanding:**
- human review of every item (rights and originality, two human blind solves, content audit, fairness review, copy edit and accessibility check, named approval)
- student calibration of difficulty and of the solver estimates above
- human decisions on the open issues listed above
- source adoption of the ChatGPT overlays

## Files

| File | Contents |
|---|---|
| `complete-bank.json` | Every reconciled record (all statuses), effective content version, key, explanation, provenance, content hash, difficulty and review evidence |
| `review-packet-answer-free.json` | Reviewed drafts, student-facing fields only (ACT English: only the item's own span in [brackets]) |
| `keys-and-explanations.json` | Keys, explanations, distractor rationales, hints, strategy, evidence, difficulty and review evidence for each reviewed draft |
| `held-and-rejected.json` | Pending, held, reserved and retired records, plus Claude candidates that ended REVISE or REJECT and were never banked (with any later resubmission) |
| `audits/` | Final audit, resolutions, duplicate screens and adjudications, insertion scan, retirements, overlays, fact correction, passage consistency, progress tracker, reconciled summary |
| `manifest.json` | SHA-256 checksums |

