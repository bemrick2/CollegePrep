# Human question review: workflow and first batch

This is how a person reviews questions before any can be published. It covers the 58 questions already in the app and
any batch imported under `QUESTION_IMPORT_CONTRACT.md`. Nothing here generates questions. Claude's review is not human
approval.

**Launch blocker:** no reviewer has been appointed and no content lead named. The reviewer registry
(`web/src/lib/data/demo/reviewers.json`) is empty, so no sign-off counts at any stage and nothing is human-approved
(0 of 58 today). Nothing in the repository appoints anyone; only the owner adds the first entries.

## The rule

**Only individually approved items can become publication-eligible.** An item is eligible when all of these hold for
that item's current content:
- every editorial stage, 3 to 8, has passed on exactly that content (sign-offs are pinned to the content hash);
- the content lead has confirmed its track (practice, or reserved for checks);
- it isn't retired;
- its answer key was matched by two blind solves of that content, by two different authorized solvers who never
  wrote any version of it;
- for an imported item, its rights check signed the item's exact current rights version.

The ledger (`editorialLedger.ts`), the reviewer registry (`reviewerRegistry.ts`) and the candidate registry
(`questionCandidates.ts`) enforce each condition above in code; the tests cover each rule listed in this document. Eligibility is worked out from the registry's append-only history, so editing a summary field
(a status, a confirmer) doesn't make an item eligible.

**Sampling is a process audit, not approval.** The content lead may re-check a random sample of passed items to test
the reviewers. A clean sample says the process works. It never makes an unsampled item eligible. Process rule (the content lead
applies it; it isn't automated): a failed sample reopens every item that reviewer signed off.

## Reviewers and roles

Reviewers are entries in the **reviewer registry**, `web/src/lib/data/demo/reviewers.json` (`reviewerRegistry.ts`).
- **Identity is the reviewer id.** Each person has a stable id (`rv-…`, never reused), the roles they may sign and who
  appointed them: the owner, or an active content lead. A sign-off counts only when its `reviewer_id` is an active entry
  authorized for that stage, whose appointment chain reaches the owner through active content leads with no loop. A
  revoked reviewer's sign-offs stop counting, and so do those of everyone appointed below them (until re-appointed);
  everyone else carries on. A revoked person can be re-appointed under a new id.
- **One person, one id.** Two entries sharing a recorded name (ignoring case, accents and punctuation, but not word
  order: "Li Wang" and "Wang Li" are two people) make the registry unusable until fixed, so one person can't be two
  solvers. Two different people with the same name are recorded with each other's id in `distinct_from`; nobody is
  asked to change their name. **A registry with any problem (a loop, an unknown appointer, a shared name) is not used:
  no sign-off counts.**
- **What code can't check.** The code catches honest duplicates only. Whether an entry is a real, separate person,
  whether `distinct_from` is true, and who added an entry (the owner or a lead) would be enforced by **repository
  review**: `.github/CODEOWNERS` asks for the owner's review of `reviewers.json`, `editorialLedger.json`,
  `identities.json`, the CODEOWNERS file itself and the workflows. **That is not
  enforced today:** `main` has no protection, and every PR is opened and merged as the owner's own account, so owner
  review can't be enforced until sessions use a separate identity (`REVIEW_ENFORCEMENT.md`). A lead could otherwise add
  a second id for themselves under another name.
- **Names are display only.** A sign-off's `by` and a reviewer's `display_name` are shown, never used to decide who
  someone is. Nobody is refused, or let through, for what their name looks like: a reviewer named "Claude Debussy" is
  entered like anyone else. Recorded `aliases` list the other names a person has used.
- **Authors can't review their own items.** Since import contract v2, every author is an identity: an explicit AI model,
  or a person recorded in `identities.json` (empty until the owner or a content lead records someone). When the author
  is also a reviewer, the identity links their reviewer id, and they are excluded from stages 4, 6 and 8 **by id**,
  whatever name either is recorded under. Names are still compared too (ignoring case, accents, spacing, punctuation
  and word order), which can only block. Every author ever recorded stays excluded (authorship is append-only).
  **A human author known only by a name** (a v1 line, or a name in the ledger without an identity) is unresolved, and the
  item is never approved or eligible; nothing treats a legacy name as a verified identity.
- **The sheet is not a signature.** `reviewer_id` is whatever the sheet says; whoever fills it in can type any id. The
  content lead checks each sheet against the people who signed it. The registry only decides what a given id may sign.
- **Dates** are a record; no rule depends on their order. A pass counts only with a real YYYY-MM-DD date no later than
  tomorrow. A **fail always blocks**, whatever its date.

| Role (registry) | Stages | Can't be |
|---|---|---|
| `rights` | 3 | — |
| `solver` ×2 | 4 | the author of any version; the same reviewer id twice |
| `auditor` | 5 | — |
| `fairness` | 6 | an author |
| `copyedit` | 7 | — |
| `approver` | 8 | an author |
| `content_lead` | confirms tracks, retires items, appoints reviewers | an author (for that item's track) |

One person may hold several roles, except that the two solvers must be different reviewer ids. Process rule (not
enforced in code): a solver who has seen the review copy, with the key, can't solve that item.

## Steps for one batch

1. **Issue packets.** From `web/`:
   `npx vite-node scripts/local/editorialPackets.ts <out-dir> --ids <comma-separated ids> [--registry <candidates.json>] [--ledger <path>] [--reviewers <path>]`
   Without `--registry` the items come from the app's bank; with it, from an imported batch (the latest version of
   every candidate that isn't retired). This writes:
   - `blind-*.html` for solvers: no key, hints or explanations;
   - `review-*.html` with the key, for stages 3 and 5–7 (never give these to solvers);
   - `solves-template.csv`, two rows per item, and `signoffs-template.csv` for stages 3 and 5–8;
   - `status.csv`, with each item's source, batch, track, hashes and stage.

   Every row carries the content hash of the text printed, and for imported items the stage-3 row carries the
   `rights_hash` of the rights version printed. Each signer fills in their `reviewer_id`.
2. **Stage 3, rights.** Record the license basis ("original", "public domain: …", "CC BY 4.0: …"). An item without
   evidence fails.
3. **Stage 4, blind solves.** Two solvers work alone, without the key, and record their answer and time.
4. **Stages 5–7.** The auditor checks for one defensible answer, plausible distractors, the explanations, a hint that
   doesn't give the answer away, and the difficulty band. Then the fairness review, then the copy edit and accessibility
   check.
5. **Record.** `npx vite-node scripts/local/recordEditorial.ts <filled.csv> [--registry <candidates.json>]`. A row is
   refused, never guessed at, when:
   - a **pass** comes from a reviewer id that isn't active and authorized for the stage, or from an author at stage 4,
     6 or 8, or is a blind solve with no answer;
   - its hash isn't the current content, or a stage-3 row's `rights_hash` isn't the current rights version;
   - its result isn't exactly `pass` or `fail`, its date isn't YYYY-MM-DD (or is in the future), or `seconds` isn't a
     whole number;
   - it is partly filled in (only a completely blank template row is skipped);
   - the reviewer registry has problems.

   **One refused row and nothing is written**: fix the sheet and run again. A **fail** is recorded from anyone who is
   named on the row, since it can only block. There is no recorded way yet to withdraw a mistaken fail (for example,
   one entered on the wrong item); until there is, the content lead revises the item or makes a reviewed ledger edit. A newer row from the same reviewer replaces only their earlier **pass**
   for that stage and content; a recorded fail is never removed or replaced: it stands until the item is revised.
   For the app's bank, a stage-2 row adds an author by identity, in `author_identity`: a recorded `au-…` id, or
   `ai:<model>`. A bare name is refused, and the author is recorded under that key, never a display name. It needs an
   active content lead who isn't an author (by id or by any name) and isn't the identity being recorded, and the
   current hash; authors are only ever added.
6. **Fix and re-issue.** Any edit changes the hash and voids every earlier sign-off, so the item goes back to stage 3.
   This includes a key change: an earlier key, solve or approval never carries over to revised content.
   - A revision may not return to an earlier version's content; it is refused, so an old review can't revive.
   - Every new version of an imported item has a new **rights version** (`rights_hash`: the version number, content,
     author, origin, license and source). A rights check counts only for the exact version it signed, so an earlier
     check never counts again, even if a revision returns to earlier rights claims; a check of the new version counts as
     soon as it is recorded, the same day or any day. A stage-3 fail with no rights version recorded blocks, and a
     stage-3 fail keeps blocking every later version that makes the same claims (same content, author, origin, license
     and source): a resubmission that changes nothing about the rights never clears it.
7. **Stage 8 and track.** The content lead approves each item individually, and confirms or changes its track:
   - a reserved item may move to practice;
   - a practice item never moves to reserved;
   - an item any student has seen is never reserved.
8. **Publication** stays held while hosted is paused. When it resumes, it goes through the migration and import path:
   `approve_practice_question` (CR-21), the CR-24 rights gate and the CR-23 pool.

## Imported batches

`npx vite-node scripts/intakeQuestionBatch.ts <batch.jsonl> --registry <candidates.json> [--identities <identities.json>] [--write]` (from `web/`).
- **Identities first.** An identity registry with any problem stops the batch.
- **Validation first.** The import validator runs before anything is recorded, and any problem stops the whole batch.
- **What gets recorded:**
  - a new item is a draft on its requested track, unconfirmed;
  - a changed item is a new version, and every earlier version and the history are kept;
  - a duplicate of the app's bank, or of any version of any earlier candidate (retired ones included), is kept as
    **retired**, with `duplicate_of`. It is never deleted and never eligible;
  - a revision that duplicates another item, returns to an earlier version or changes a retired item is refused and
    noted in the history;
  - an `import_id` that is already a bank question's id is refused.
- **Dry run by default.** Without `--write`, no file changes.

Packets and sign-off recording take the same `--registry` file (steps 1 and 5).

**Real banks:** the original, B and C banks have **not** been delivered (#254). The tests use a stand-in batch labelled
TEST ONLY (`web/src/lib/__fixtures__/TEST_ONLY_importBatch.ts`), made of the app's own fixture items in the import
format. Passing those tests validates the tooling, never the real banks.

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
