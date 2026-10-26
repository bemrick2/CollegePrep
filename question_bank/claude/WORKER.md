# Question-bank worker procedure

This is the standing procedure for any session that continues this workstream: the original session, a scheduled cloud session, or a manual restart. Follow it exactly. The brief is in `reference/CLAUDE_INSTRUCTIONS.md`; limitations are in `README.md`.

## Hard boundaries

- **Allowed:** write only under `question_bank/claude/`, and push only to the branch `ccr-78c91309-anlh8e`.
- **Never** open a pull request, merge, deploy, import into Supabase or the app, edit application code, or spend money on external services.
- Every import line stays `status: draft` and `origin: ai_drafted`. Never describe an item as human-approved.

## 0. Start-up and lock (single writer)

```
cd <repo root>   # bemrick2/CollegePrep
git fetch origin ccr-78c91309-anlh8e && git checkout ccr-78c91309-anlh8e && git merge --ff-only origin/ccr-78c91309-anlh8e
python3 -I question_bank/claude/tools/qb.py lock acquire <HOLDER>
```

- `<HOLDER>` is your session ID (from `get_session`) or another unique string. Reuse the same string for every later lock command.
- **Exit code 3** means another live worker holds the lease, or you lost the race. **Stop immediately** and write nothing.
- The lease expires 120 minutes after its last heartbeat. Every checkpoint renews it.
- If any `lock checkpoint` exits **4**, you have lost the lease. Stop writing at once.
- For the import validator, run `cd web && npm ci --no-audit --no-fund --ignore-scripts` once if `web/node_modules` is missing. Nothing is deployed; it only reads files.

## 1. Pick up where the last run stopped

Read `progress.json`:

| Field | Meaning |
|---|---|
| `next_bank` | Which bank to work on |
| `next_batch_guidance.<bank>.next_batch` | The batch number |
| skill, difficulty and answer-letter gaps | What the next batch should cover |
| `calibration_notes`, `audits` | Findings to act on |

- If `drafts/<bank>/batch-NNN.json` exists but `reviews/<bank>/batch-NNN.review.json` does not, finish that batch rather than starting a new one.
- `review` refuses to append a batch twice, so a re-run after a crash cannot duplicate IDs.

## 2. One batch = 10 candidates

1. **Draft** `drafts/<bank>/batch-NNN.json`, following the existing drafts' shape.
   - Fields: `cand` `BNNN-01`… plus skill, subskill, reporting category, `repo_skill_key`, difficulty, stem, choices A–D, answer, explanation, distractors (rationale and trap for every wrong choice), hints, strategy, remember (16 words or fewer), expected time, modeling, author checklist.
   - Spread the answer letters to close `answer_key_gap_for_next_10`.
   - Close the skill gaps.
   - Aim for the calibrated difficulty gap. Until the bank reaches 25% calibrated-hard, write **4–5 hard items per batch**.
2. **Checks** `checks/<bank>/batch_NNN.py` (math). Each item's answer is recomputed from the stem's numbers by brute force, enumeration or direct formula, and the matching letter is returned via `_util.pick`. Never read the key.
3. **Screen.** Run `qb.py screen <bank> NNN`. Then compare every stem by hand against the app fixture stems (`web/src/lib/data/demo/fixtures.ts`) and the bank. Rewrite anything that shares a setup or context, not just wording.
4. **Blind solve.** Run `tools/blind_packet.py drafts/<bank>/batch-NNN.json <scratch>/batch-NNN.json`. Start a separate agent with the prompt in the next section. It writes `reviews/<bank>/batch-NNN.blind.json`.
5. **Review.** Run `qb.py review <bank> NNN`, which appends PASS items and rebuilds the exports and `progress.json`.
   - For any REVISE item: fix it in a new draft batch, and re-run the blind solve on the changed text before it can pass. Never edit an accepted record.
   - REJECT is final.
6. **Import validator.** Run `cd web && npx vite-node scripts/validateQuestionImport.ts ../question_bank/claude/exports/import/<bank>.jsonl`. It must report 0 problems. If it doesn't, stop and fix it before the next batch.
7. **Checkpoint.** Run `qb.py lock checkpoint <HOLDER> "question bank: <bank> batch NNN (<n> accepted total)"`. This commits, renews the lease and pushes.
8. **Continue** straight to the next batch. Do not wait for approval.

**Difficulty calibration.** Ratings vary a lot from one blind-solver instance to another. In batches 6–8, items of similar depth were rated 25–38% correct by one solver and 40–55% by another. So:

- Treat each batch's rating as **provisional**.
- At every 100-item audit, have a single rater re-rate the **whole bank** with the rubric in one sitting (answer-free packet, chunks of about 50 if needed). Store the result as `calibration/<bank>_rater_<date>.json` and merge it into `calibration/<bank>.json`.
- The re-rated labels drive targeting and the import difficulty. Accepted records stay unchanged.

At every 100 accepted items in a bank, `review` records an automatic audit in `progress.json`. Read it, act on what it finds (duplicates, answer-letter balance, difficulty, thin explanations), and add a written summary to `progress.json` `audits` at the next checkpoint.

### Blind-solver prompt (use verbatim, with the paths filled in)

> You are an independent quality-control reviewer for draft ACT Math multiple-choice questions (enhanced ACT: 4 choices A–D, calculator allowed). BLIND solve: read ONLY `<packet path>`; do NOT open anything under the repository (it contains the keys). Solve each item from scratch (python3 allowed). For each decide the single correct choice, whether exactly one choice is defensible, and whether anything is missing, ambiguous or unrealistic. Real problems go in "flags"; stylistic notes go in "flags" prefixed "minor:". Rate difficulty for the TYPICAL ACT test-taker, not for yourself, using this rubric literally — easy: one routine step or one familiar fact, ~70%+ correct; medium: two or three routine steps or a standard concept with a small twist, 40–69% correct; hard: needs a non-obvious insight or setup, combines concepts, unfamiliar application, or a trap that catches most quick solvers, under 40% correct. Length or arithmetic volume alone does not make an item hard. Write JSON to `<repo>/question_bank/claude/reviews/<bank>/batch-NNN.blind.json` (the only file you may write): {"solver": {"kind": "blind AI solver (separate agent, answer-free packet, rubric v2)", "batch": N}, "answers": {"BNNN-01": {"answer": "B", "confidence": "high|medium|low", "est_pct_correct": 55, "difficulty_opinion": "easy|medium|hard", "flags": [], "notes": "brief work"}}}. Reply with a summary table.

### Verbal anti-tell checklist (from blind-solver flags, batches 3-9)

Blind solvers rate most verbal items easy because they can be answered by test-taking habits instead of reading. Before screening a verbal batch, check every item:

- **Key copies the passage.** If the key repeats a passage sentence almost word for word, paraphrase it, or make a distractor reuse passage wording too.
- **Only hedged choice.** If the key is the only hedged or moderate choice and every distractor says "all", "never", "proven" or "entirely", give at least one distractor moderate wording that is wrong on content.
- **Length cue.** If the key is the longest choice or the only two-part choice, the screen's length warning flags it. Even out the lengths, or give a distractor two parts as well.
- **Throwaway distractors.** Replace any distractor that nobody would pick (vocabulary items with "anniversary", "dressed") with one that fits the sentence's surface meaning.
- **Overlapping items.** Make sure no two items on the same passage test the same inference.
- **Unstated character traits.** Never give an unnamed narrator or character a gender, age or background the passage does not state; write "the narrator" (Reading batch 14 round 1 called a first-person narrator "she" and "granddaughter").
- **Keys that paraphrase one sentence.** A key that restates a single passage sentence makes the item a lookup; build inferences whose support is spread across paragraphs.

### Avoiding concept repeats

The near-duplicate screen compares wording, so it misses a repeated *idea* in new words (batch 22's first draft reused the circle through (2, 1), the x + 1/x identity, the no-solution system and the successive-percent jacket). Before drafting, list the bank's existing subskills and pick new ones:

```
python3 -I -c "import json; b=json.load(open('banks/<bank>.json')); print(sorted({q['subskill'] for q in b['questions']}))"
```

`qb.py screen` also prints an advisory when a candidate's subskill overlaps an existing one. Treat that as a prompt to compare the items by hand, not as proof either way.

## 3. Writing genuinely hard items

The rubric rater marks an item hard only when most typical students would miss it for a *reasoning* reason. To get there:

- Require a setup the student must invent: choose a variable, see a symmetry, use a complement, notice a constraint, or work backwards from a condition.
- Combine two domains, e.g. probability with geometry, functions with a real constraint, or ratios with a structural argument.
- Use an unfamiliar context that still reduces to standard ACT content.
- Ask about structure: "which must be true", "for how many values", "what is the greatest possible".
- Build distractors from a precise, common misconception, so each one is the answer to a nearby wrong problem.
- **Don't** fake difficulty with longer arithmetic, ugly numbers or obscure topics outside the ACT.

A candidate labelled hard that the blind solver rates easy is sent to REVISE automatically.

## 4. Sections and targets

- **Targets:** ACT Math 2,000, ACT English 700, ACT Reading 600, SAT Reading & Writing 700. Total 4,000.
- **Policy:** ACT Math first until 200 accepted. After that, `next_bank` picks the bank furthest behind its target.
- **Verbal banks:**
  - **Tooling is a prerequisite.** Before the first verbal batch, extend `qb.py` so that structure checks, skills, the record schema and exports handle verbal items. Use these passage IDs: `CLD-P-ACT-E-000001`, `CLD-P-ACT-R-000001`, `CLD-P-SAT-RW-000001`.
  - Verbal items need no computation check. Each one instead needs a stored evidence span (the passage text that supports the key).
  - Verbal batches must still pass the blind solve and the import validator, and must use skill keys from the app taxonomy (`act_punctuation`, `act_main_idea`, …).
- **Tell the user before the first verbal batch** if the passage-ID scheme has not been agreed with the ChatGPT workstream.

### Verbal batch format (tooling is in place)

**Draft file:** `drafts/<bank>/batch-NNN.json` has a `passages` list and a `candidates` list.

- **Each passage:** `{"passage_id": "CLD-P-ACT-E-000001", "title", "genre", "word_count", "text"}`.
  - ACT English text marks every editable span as `{{n|text}}`, the app's fixture convention.
  - The app shows only the current item's span, in [brackets].
- **Each candidate:** adds `passage_id`, `evidence` (a verbatim quote from the passage that supports the key) and, for ACT English, `underline` (the span number). Skill and `repo_skill_key` come from `VERBAL_BLUEPRINT` and `VERBAL_REPO_SKILLS` in `qb.py`.

**Checks and review:**

- Verbal items have no `checks/` file. The screen instead verifies that the evidence is quoted verbatim, that the underline exists, and that the passage is not a near-duplicate of a fixture or bank passage.
- **Two independent blind solves are required**: `reviews/<bank>/batch-NNN.blind.json` and `…blind2.json`. Use two separate agents with the same prompt, adapted to say "ACT English / ACT Reading / digital SAT Reading and Writing" and to read the passage in each packet item.
- An item passes only if both solves match the key.
- **Passage-level flaws found in review:** passages are append-only once any item from them is accepted, so a flaw in the passage itself (an internal contradiction, a factual error) must be fixed *before* ingesting. Move the round-1 files to `batch-NNN.round1.blind.json` / `.round1.blind2.json`, fix the draft, record the change in the draft's `revision_log`, and re-solve the whole batch blind. Never edit a passage after its items have been solved without re-solving.
- A passage enters the bank's `passages` list only when at least one of its questions passes.

**Formats:**

| Exam | Format |
|---|---|
| ACT English | Passages of about 300–350 words, roughly 10 items each |
| ACT Reading | Passages of about 500–750 words, roughly 8–9 items each |
| SAT Reading & Writing | 25–150-word texts, one question each |

## 5. Stopping

- Release the lease with `qb.py lock release <HOLDER>` when you stop on purpose: budget nearly exhausted, an unresolved blocker, or the user says stop.
- If you are cut off, the lease simply expires after 120 minutes and the next worker takes over from the last pushed checkpoint. Unpushed work in a dead container is lost and redone, never duplicated.
- At each 50-item checkpoint, write a short progress summary to the user, then keep working.
