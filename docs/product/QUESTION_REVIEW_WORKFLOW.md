# Human question review: workflow and first batch

This is how a person reviews questions before any can be published. It covers the 58 questions already in the app and
any batch imported under `QUESTION_IMPORT_CONTRACT.md`. Nothing here generates questions. Claude's review is not human
approval.

**Launch blocker:** no content lead has been named. Until the owner names one, no question can pass stage 8, and
nothing in the bank is human-approved (0 of 58 today). The work below runs without one up to stage 7.

## The rule

**Only individually approved items can become publication-eligible.** An item is eligible when all of these hold for
that item's current content:
- every editorial stage, 3 to 8, has passed on exactly that content (sign-offs are pinned to the content hash);
- the content lead has confirmed its track (practice, or reserved for checks);
- it isn't retired;
- its answer key was matched by two blind solves of that content, by people who never wrote any version of it.

The ledger (`editorialLedger.ts`) and the candidate registry (`questionCandidates.ts`) enforce this, and the tests
fail if any step is skipped.

**Sampling is a process audit, not approval.** The content lead may re-check a random sample of passed items to test
the reviewers. A clean sample says the process works. It never makes an unsampled item eligible. A failed sample
reopens every item that reviewer signed off.

## Roles

Each person is named; a role, a team or "AI" is refused.

| Role | Stages | Can't be |
|---|---|---|
| Rights checker | 3 | — |
| Two blind solvers | 4 | the author of any version; each other |
| Content auditor | 5 | — |
| Fairness reviewer | 6 | an author |
| Copy and accessibility editor | 7 | — |
| Content lead (approver; confirms tracks) | 8 | an author |

One person may hold several roles, except that the two solvers must be different people. A solver who has seen the
review copy (with the key) can't solve that item.

## Steps for one batch

1. **Issue packets.** From `web/`:
   `npx vite-node scripts/local/editorialPackets.ts <out-dir> --ids <comma-separated ids>`
   This writes:
   - `blind-*.html` for solvers: no key, hints or explanations;
   - `review-*.html` with the key, for stages 3 and 5–7 (never give these to solvers);
   - `solves-template.csv`, two rows per item;
   - `status.csv`, which includes each item's track.

   Every row carries the content hash of the text printed.
2. **Stage 3, rights.** Record the license basis ("original", "public domain: …", "CC BY 4.0: …"). An item without
   evidence fails.
3. **Stage 4, blind solves.** Two solvers work alone, without the key, and record their answer and time.
4. **Stages 5–7.** The auditor checks for one defensible answer, plausible distractors, the explanations, a hint that
   doesn't give the answer away, and the difficulty band. Then the fairness review, then the copy edit and accessibility
   check.
5. **Record.** `npx vite-node scripts/local/recordEditorial.ts <filled.csv>`. A row whose hash isn't the current
   content is refused, so a sign-off can't attach to text nobody saw.
6. **Fix and re-issue.** Any edit changes the hash and voids every earlier sign-off, so the item goes back to stage 4.
   This includes a key change: an earlier key, solve or approval never carries over to revised content.
7. **Stage 8 and track.** The content lead approves each item individually, and confirms or changes its track:
   - a reserved item may move to practice;
   - a practice item never moves to reserved;
   - an item any student has seen is never reserved.
8. **Publication** stays held while hosted is paused. When it resumes, it goes through the migration and import path:
   `approve_practice_question` (CR-21), the CR-24 rights gate and the CR-23 pool.

## Imported batches

`npx vite-node scripts/intakeQuestionBatch.ts <batch.jsonl> --registry <candidates.json> [--write]` (from `web/`).
- **Validation first.** The import validator runs before anything is recorded, and any problem stops the whole batch.
- **What gets recorded:**
  - a new item is a draft on its requested track, unconfirmed;
  - a changed item is a new version, and every earlier version and the history are kept;
  - a duplicate of the app's bank or of an earlier bank is kept as **retired**, with `duplicate_of`. It is never deleted
    and never eligible.
- **Dry run by default.** Without `--write`, no file changes.

**Gap:** `editorialPackets.ts` and `recordEditorial.ts` read only the app's fixture bank. They must read the candidate
registry before an imported batch can be reviewed. That change is next once a batch arrives (#254).

## Proposed first batch (10 items, ACT)

These are the existing AI-drafted items; none is human-reviewed. Reserved items come first, because checks depend on
them. Each track is the app's current assignment, and the content lead confirms it at stage 8.

| Track | Item | Section | Difficulty | Skill | Format |
|---|---|---|---|---|---|
| Reserved | act-english-05 | English | 3 | Punctuation | choice |
| Reserved | act-math-04 | Math | 3 | Functions | choice |
| Reserved | act-math-06 | Math | 3 | Number and quantity | numeric |
| Reserved | act-reading-02 | Reading | 3 | Inference | choice |
| Reserved | act-science-04 | Science | 3 | Experiment design | choice |
| Practice | act-english-01 | English | 1 | Usage | choice |
| Practice | act-math-02 | Math | 2 | Linear algebra | choice |
| Practice | act-math-08 | Math | 3 | Geometry | choice |
| Practice | act-reading-03 | Reading | 4 | Author's purpose | choice |
| Practice | act-science-08 | Science | 5 | Conflicting viewpoints | choice |

Command:
```
npx vite-node scripts/local/editorialPackets.ts review-batch-01 --ids act-english-05,act-math-04,act-math-06,act-reading-02,act-science-04,act-english-01,act-math-02,act-math-08,act-reading-03,act-science-08
```

**Why these:**
- every ACT section, in both tracks;
- difficulty from 1 to 5 in practice;
- the numeric answer format;
- reserved items at difficulty 3, as all current ACT reserved items are.

**Estimated effort:** about 10 minutes a person per item per stage, so roughly 12 to 15 reviewer-hours for the batch
[Guessing]. The batch should first be timed and used to correct this estimate before the 467-item planning target is
scheduled.

## What this doesn't do

- It doesn't approve anything, or switch the serving gate to human approval. That switch is an owner decision (launch
  checklist A2).
- It doesn't calibrate difficulty. Difficulty stays the author's estimate until real students' data exists.
- It doesn't replace the server gates: CR-21 approval, the CR-24 rights gate and the CR-23 pool.
