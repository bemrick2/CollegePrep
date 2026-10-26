# Claude question bank (independent draft workstream)

Original ACT/SAT practice questions drafted by Claude for Prep & Price. Every record here is an **AI-generated draft**. None has had human editorial review. Nothing in this folder is published, imported or wired into the app, and the app's production bank is not touched.

A separate ChatGPT workstream builds its own bank. To keep the two from colliding, every ID here starts with `CLD-`.

## Layout

| Path | What it is |
|---|---|
| `banks/<bank>.json` | Cumulative accepted (PASS) questions. Append-only, versioned. Banks: `act_math`, `act_english`, `act_reading`, `sat_reading_writing` |
| `drafts/<bank>/batch-NNN.json` | Every candidate as written, including ones later rejected |
| `checks/<bank>/batch_NNN.py` | Scripted recomputation of each candidate's answer from the stem's own numbers. It never reads the key |
| `reviews/<bank>/batch-NNN.blind.json` | Answers from a separate blind solver that saw only the stem and choices |
| `reviews/<bank>/batch-NNN.review.json` | Reconciliation per candidate: status, reason, evidence |
| `exports/<bank>.student.json` | Student-facing export with no answers |
| `exports/<bank>.answer_key.json` | Answers, explanations, distractor rationales and hints, keyed by ID |
| `exports/import/<bank>.jsonl` | The same items in the app's `question_import/v1` contract (`docs/product/QUESTION_IMPORT_CONTRACT.md`), all `status: draft`, `origin: ai_drafted` |
| `progress.json` | Counts, skill and difficulty coverage, review totals, last batch, next-batch gaps, audits, file versions |
| `tools/qb.py` | Review, export, screen and audit tool |
| `reference/` | The starter brief and `SAMPLE_QUESTIONS.json`, used as schema examples only |

## Record schema (`cld-qb/1.0`)

`id`, `schema_version`, `exam`, `section`, `reporting_category`, `skill`, `subskill`, `modeling`, `repo_skill_key`, `passage_id`, `figure`, `stem`, `choices` (A–D), `correct_answer`, `explanation`, `distractor_explanations`, `distractor_traps`, `hints`, `strategy`, `remember`, `expected_time_seconds`, `calculator`, `difficulty` (easy/medium/hard), `difficulty_numeric` (2/3/4 on the app's 1–5 scale), `difficulty_basis`, `origin` (`ai_generated`), `author` (`ai:claude`), `license`, `batch`, `draft_candidate`, `created_at`, `validation` (status, method, computed answer, blind answer, confidence and difficulty opinion, flags, evidence file paths), `review_status` (`ai_reviewed_pending_human`) and `human_review` (null).

Passages, used by the verbal banks once they exist, go in each bank's `passages` array under a stable `passage_id`. Questions refer to them by that ID, so passage text is not copied into each question.

## Acceptance pipeline

1. **Draft.** Each candidate is written with a key, a full explanation, a rationale (and trap type) for every wrong choice, hints and a strategy.
2. **Screen** (`qb.py screen act_math N`): structure checks, the scripted recomputation, and a near-duplicate check against the bank, the batch, the starter samples and every stem in the app's fixture bank (`web/src/lib/data/demo/fixtures.ts`). The author also reads the fixture math stems by hand, because token overlap misses paraphrases.
3. **Blind solve.** A separate agent receives only `{cand, stem, choices}` and records its answer, confidence, difficulty opinion and flags.
4. **Reconcile** (`qb.py review act_math N`):
   - **PASS** when key = computed answer = blind answer, with no blocking flag and no duplicate. PASS items are appended to the bank.
   - **REVISE** for a fixable disagreement or structural problem.
   - **REJECT** for duplicates or fundamental flaws.
   - Exports and `progress.json` are rebuilt after every review.
5. **Saves are version-safe.** The bank's hash is checked again just before an atomic replace. The save is refused if any earlier record would change or disappear, or if a batch would be appended twice.

## Specification used

- The ACT Math blueprint follows the enhanced ACT (from spring 2025): 45 questions in 50 minutes, four answer choices, calculator allowed.
- Reporting-category weights are midpoints of the published ranges, as summarised in search results that cite ACT's enhancement FAQ:
  - Preparing for Higher Math is about 80%: Number & Quantity 10–12%, Algebra 17–20%, Functions 17–20%, Geometry 17–20%, Statistics & Probability 12–15%.
  - Integrating Essential Skills is about 20%.
  - Modeling is at least 20%, tagged with `modeling: true`.
- **act.org could not be reached from the build environment** (DNS blocked), so these figures are second-hand. Check them against ACT's current published blueprint before relying on the balance.
- No reference practice exams were supplied, so calibrating style against them is still pending.

## Known limitations (read before trusting the bank)

- **AI review only.** The blind solver is a separate agent with no access to the key. It is still the same model family as the author, so it can share the author's blind spots. Human stages 3–8 in `QUESTION_REVIEW_WORKFLOW.md` still apply in full.
- **Difficulty is uncalibrated and probably inflated.** The blind solver rated most items one level easier than the author did. Both opinions are stored on each record. Treat the 25/50/25 split as the author's intent, not a measurement.
- **Taxonomy mapping is lossy.**
  - The app's taxonomy has no key for nonlinear algebra, so quadratic, radical and exponential algebra items map to `act_functions`.
  - Integrating Essential Skills items map to `act_number_quantity` or `act_geometry`.
  - The bank's own `skill`/`subskill` fields keep the precise classification.
- **Figures.** No item so far needs a drawn figure. Any item that does will carry a `figure` spec for production.
- **Context overlap flagged for human review.** CLD-ACT-M-000006 (successive percent change on a jacket price) shares its *context*, a jacket price changed twice, with an app fixture. Its structure is different (percent of original price, not total cost after a discount plus tax). It passed the automated screen and is kept, but a reviewer should look at it.

## Resuming

```
python3 question_bank/claude/tools/qb.py export            # rebuild exports and progress
python3 question_bank/claude/tools/qb.py audit act_math    # duplicate and balance audit
```

The next batch number and its skill and difficulty gaps are in `progress.json` under `next_batch_guidance`. Start a new batch by writing `drafts/act_math/batch-NNN.json` and `checks/act_math/batch_NNN.py`. Then screen it, build the blind packet (`tools/blind_packet.py`), blind-solve it, and run `review`.

Validate the import export with the app's own validator. It only reads the file:

```
cd web && npx vite-node scripts/validateQuestionImport.ts ../question_bank/claude/exports/import/act_math.jsonl
```
