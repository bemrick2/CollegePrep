# Question import contract (`question_import/v2`; `v1` still read)

This is for the separate question-bank workstream. It defines how original questions enter Prep & Price's review pipeline. It doesn't generate questions, and nothing here generates any. The app's own bank is not being replaced.

**The one rule:** an imported question is a **draft**. It is never shown to a student until all three gates have passed:
1. the human editorial stages 3–8 (`CONTENT_PLAN.md` §5, recorded in the editorial ledger, #207);
2. the rights gate (CR-24, Research's #245): an allowed license, attribution where needed, and a recorded origin; a generated item is served only with a `human:` review;
3. the review approval (`approve_practice_question`, CR-21).

Generating a question, by a person or an AI, confers nothing. Passing the validator below only means the item is well-formed enough to start stage 3.

## Version 2: author identities (owner decision, 2026-10-26)

`question_import/v2` adds one required field, `author_identity`. It links every author to a stable identity:

| `author_identity` | `author` | `origin` | Meaning |
|---|---|---|---|
| `{"kind": "ai", "model": "<model>"}` | `ai:<model>` | `ai_drafted` | An AI draft, recorded explicitly as AI authorship. |
| `{"kind": "person", "identity_id": "au-…"}` | the person's name (display only) | any other origin | A person with a recorded identity in `web/src/lib/data/demo/identities.json`. |

- **Identities aren't created by a batch.** The owner, or an active content lead, records each person in `identities.json`. That file ships **empty**, so until someone is recorded, every human-authored v2 line fails validation. Nothing invents an identity. Only an `au-…` id that is recorded counts (never a built-in name such as `constructor`). An identity registry with any problem isn't used: intake refuses the batch, and nobody resolves.
- **Reviewers are linked by id.** When the author is also a reviewer, their identity carries `reviewer_id`. They are then excluded from stages 4, 6 and 8 by id, under any name. The names in the identity and the import are still matched as well; that can only block. A reviewer whose names match an identity must be the one linked to it; a different person with a matching name is recorded in the identity's `distinct_from`, and otherwise the identity registry is unusable. A person's identity may not use the name "AI (Claude)".
- **v1 lines are legacy.** They are still read (the original, B and C banks may arrive in v1), but a human author named in v1 is a **name only** and never counts as a verified identity. Such an item is never publication-eligible. That holds for every version of it, even after a v2 revision. A v1 AI draft (`ai:<model>`, `ai_drafted`) is explicit AI authorship and is resolved.
- **The app's own bank** works the same way. "AI (Claude)" is the bank's recorded AI drafting, so it is resolved. A human author recorded later at stage 2 needs an identity (`au-…`) or an explicit `ai:<model>`, never a bare name. Stage 2 writes the author into the ledger under that key (`authors` and `author_records`), never under a display name, and only a record that matches its key resolves. A human name already in the ledger (a legacy name) stays unresolved, whatever identity shares its display name, so the item is never approved. There is no path that turns a legacy name into an identity.
- **An identity change is a rights change.** `author_identity` is one of the rights fields, so changing it makes a new rights version, and stage 3 must be signed again.

## Provisional planning target

ACT, 40 questions a week, for 12 weeks. This is in `web/src/lib/contentTarget.ts` (`PROVISIONAL_TARGET`), where the bank size and the planned-review share are settings, not constants.

| Setting | Provisional value | Unique items needed |
|---|---|---|
| Practice shown | 40 × 12 = 480 | — |
| Planned review | 25% (configurable, 0–100%) | — |
| Headroom | 15% | — |
| Unique practice items | 480 × 0.75 × 1.15 | 414 |
| Reserved (checks only) | starting check 27 + 2 mini checks × 13 | 53 |
| **Total** | | **467** |

At 0% planned review the total is 605 (552 practice + 53 reserved). `bankSize()` computes any other target.

**This is not approval to launch.** It doesn't promise families that fresh questions will be available. The weekly goal is never lowered to fit the bank. When fresh questions run out, the app says so.

## File format

- A batch is one JSON Lines file: one question per line, UTF-8.
- Each line is a `FixtureQuestion` (`web/src/lib/data/demo/fixtures.ts`) without `id`, plus the provenance fields below.
- A question's database row is built from it by the import path (held while hosted is paused).

| Field | Required | Rule | Database column |
|---|---|---|---|
| `contract` | yes | `"question_import/v2"` (or `"question_import/v1"`, legacy: see Version 2) | — |
| `import_id` | yes | Stable, unique and never reused for different content. Lowercase letters, digits, `-` and `_` | import key |
| `exam_family` | yes | `act` or `sat` | `exam_versions.exam_family` |
| `section` | yes | ACT `english`, `math`, `reading`, `science`; SAT `reading_writing`, `math` | `section` |
| `difficulty` | yes | Integer 1–5. The author's estimate; calibration comes from student data later | `difficulty` |
| `stem` | yes | The question as shown | `stem` |
| `passage` | when used | Original, or with its own license and attribution | `practice_passages` |
| `choices` | choice items | `[{key, text}]`, at least two, keys unique | `choices` |
| `answer_format` | yes | `choice` or `numeric` | `answer_format` |
| `accepted_answers` | yes | Choice: exactly one key, which must be one of the choices. Numeric: the accepted spellings | `accepted_answers` (hidden until submit) |
| `distractors` | choice items | A rationale for every wrong choice, plus its trap type if any | `practice_question_distractors` |
| `hints` | yes | At least one, and none may give the answer away | `hints` |
| `teaching_explanation`, `strategy_explanation` | yes | | same names |
| `remember` | optional | At most 16 words | `remember_text` |
| `expected_time_seconds` | yes | Integer, 10–600 | same |
| `primary_skill_key` | yes | Must exist in the skill taxonomy | `practice_question_skills` |
| `strategies` | optional | `{strategy_key, role, is_fastest, explanation}` | `practice_question_strategies` |
| `origin` | yes | `human_original`, `ai_drafted`, `adapted_public_domain`, `adapted_cc_by`, `licensed` | `origin` (CR-24): `ai_drafted` → `generated`, `licensed` → `licensed`, the rest → `authored`. A `generated` item is served only after a `human:` review |
| `author` | yes | A named person, or `ai:<model>` for an AI draft. Display only; every later reviewer must differ from the author | ledger `author` |
| `author_identity` | v2: yes; v1: not allowed | `{"kind": "ai", "model"}` or `{"kind": "person", "identity_id": "au-…"}` naming a recorded identity (see Version 2) | candidate registry (the version's item); used for author separation, and part of the rights version |
| `license` | yes | One of CR-24's set (#245): `original-owned`, `us-federal-pd`, `public-domain`, `cc-by-4.0`, `cc-by-sa-4.0`, `licensed:<vendor>` | `license` |
| `source_attribution` | when the license needs it | Required for `cc-by-4.0`, `cc-by-sa-4.0` and `licensed:*` (the server's rule), and here also for `public-domain` and `us-federal-pd` so stage 3 can check the source. Official ACT or College Board material is refused without written permission | `source_attribution` |
| `source_url` | optional | Where an adapted source came from | ledger |
| `requested_pool` | yes | `practice` or `assessment`. A request only: the content lead assigns the final pool before any student sees the item | none (the content lead sets `pool`, CR-23, in review) |
| `status` | no | Absent or `draft`. Anything else is refused | `status` (always `draft` on import) |

## Validation

`npx vite-node scripts/validateQuestionImport.ts <batch.jsonl>` (run from `web/`) reads the batch and changes nothing. It prints one problem per line and exits 1 if any are found. The rules are in `web/src/lib/questionImport.ts` and are tested against every current fixture.

**Checked automatically:**
- **Allow-listed fields:** a line carrying any field not in the table above (an id, a pool, an approval, a hash) is refused.
- **Shape:** every required field; enums; difficulty and time ranges; the key is one of the choices; every wrong choice has a rationale; numeric answers are numbers; `remember` length; the skill exists.
- **Duplicates:** within the batch and against the bank. Stem, passage and choices are compared after ignoring case, spacing and punctuation.
- **Never published on arrival:** any status other than `draft` is refused.
- **Rights:**
  - the license must be in the allowed set;
  - attribution is required where the license needs it;
  - `adapted_cc_by` must go with `cc-by-4.0`;
  - official ACT or College Board sources are refused;
  - origin and license must fit each other (an original item is `original-owned`; an adapted public-domain item is `public-domain` or `us-federal-pd`; and so on);
  - an AI draft must name its model, and an `ai:` author must be an AI draft;
  - ACT and College Board names and domains are refused in the source, URL, stem and passage. This is a screen, not proof: stage 3 still checks every source by hand.
- **Duplicates** are checked against the app's fixture bank; once hosted is back, check against the hosted bank too.

**Checked by people, in the ledger (not automatable):**
- **Stage 3, rights:** proof of originality or license (a URL, contract or license text), and the attribution text.
- **Stage 4:** two blind solves, neither by the author, both matching the key.
- **Stage 5, audit:** exactly one defensible answer, plausible distractors, explanations, a hint that doesn't give the answer away, and the right difficulty band.
- **Stage 6:** fairness and sensitivity.
- **Stage 7:** copy edit and accessibility, including alt text that doesn't leak the answer.
- **Stage 8:** approval by a named human who isn't the author. Then `approve_practice_question` records the content hash, and any later edit voids it.

## Reserved (assessment) items

- **Author them first.** Reserved items come before practice items, so checks never depend on what's left over.
- **Never expose them.** An item a student has seen in practice can't move to `assessment`. A reserved item may move to practice or be retired, but never back.
- **Pool sizes per check:**
  - **Starting check:** ACT 27 (7/8/6/6), SAT 18 (9/9).
  - **Each mini check:** ACT 13 (3/4/3/3), SAT 8 (4/4).
  - **Full forms:** each one needs its own unseen form (`QUESTION_BANK_RECOMMENDATION.md`).
- **If the pool is too small,** the app shortens or skips the section and withholds verdicts on repeats (CR-23). It never borrows practice items.

## Hand-off

1. The workstream delivers a JSONL batch plus the rights evidence for each item.
2. Design or the content lead runs the validator, fixes or returns failures, and records passing items with `scripts/intakeQuestionBatch.ts` (`QUESTION_REVIEW_WORKFLOW.md`):
   - each item becomes a draft practice or reserved-assessment candidate, entering the ledger at stage 3;
   - a changed item becomes a new version, and earlier versions are kept;
   - a duplicate of the bank or of an earlier batch is kept as retired, never deleted.
3. Items are published only after stage 8, through the migration and import path. That path is held while hosted is paused.
