# Unresolved issues

All 5,843 records are AI-generated drafts. **None is human-approved.** Nothing has been imported, deployed or published.

Items 1–4 were found while preparing this v2 package (2026-10-28). Items 5–12 are carried unchanged from the 2026-10-28 final quality report.

## Found in this package pass

1. **1,620 reviewed ChatGPT drafts cannot be imported as they stand.** Each lacks fields the import contract requires: 1,620 have no strategy explanation, no expected time and no taxonomy skill key (their skills are free text); 1,448 have no hints; 1,308 lack a rationale for every wrong choice and 30 more have one free-text note instead of per-choice rationales. Filling these means writing new content, which then needs its own review. Nothing was invented. Per-record list: `import/chatgpt-contract-gaps.json`. Decision needed: author the missing fields (then review), or import Claude items only.

2. **The branch's own `exports/import/*.jsonl` include 15 records the reconciled bank does not count** (14 ACT Math reserved duplicates, 1 SAT R&W hold, CLD-SAT-RW-000100). Those files were generated from the raw Claude banks before reconciliation. `import/v1` and `import/v2` in this ZIP leave them out. List: `import/excluded-from-import.json`. Anyone importing from the repository path rather than this ZIP would bring in those 15.

3. **The import contract moved after this branch split from `main`.** `main` (43d4c7269c) is at `question_import/v2`, which requires `author_identity`. This ZIP carries both: `import/v1` (lines exactly as the workstream wrote them) and `import/v2` (same lines, contract v2 and `author_identity: {"kind": "ai", "model": "claude"}`). Both pass `main`'s validator with 0 problems. The question-bank branch itself has not been merged with `main`.

4. **Inaccurate evidence metadata on 2,072 Claude verbal records** (every reviewed SAT R&W, ACT English and ACT Reading item from Claude). Each record's `review_evidence.method` says "scripted recomputation from the stem (checks/)" and names a `checks/<bank>/batch_NNN.py` script. Those scripts do not exist and verbal items have no scripted recomputation. The real evidence (blind solves, present in the review files) is intact. Records were left unchanged to preserve provenance; `review-evidence/evidence-index.json` notes the discrepancy on each. Recommended: correct the method text at source.

5. **636 reviewed ChatGPT drafts rest on weaker evidence than the rest.** Their only evidence is a `current_external_ai_pass_recorded = True` flag in the user-supplied baseline screening ZIP (checksum verified). The underlying external review is not in the repository, so it cannot be inspected here.

## Carried from the final quality report

6. Template duplicate kept by override: PP-VERBAL-20261022-F-017 / PP-VERBAL-20261022-I-011. Recommended: rewrite one span to test a different rule, then a fresh blind review.
7. Template duplicate kept by override: PP-VERBAL-20261022-C-002 / PP-VERBAL-20261022-K-001. Same constraint.
8. Four Claude ACT English essay-level items (CLD-ACT-E-000445, -000452, -000456, -000471) carry an underline number absent from their passage. Recommended: set underline to null on import.
9. Five ChatGPT ACT English span labels have no item; none marks an untested error. Recommended: strip at render time.
10. On hold: CLD-SAT-RW-000100 (historical key dispute, appositive editorial dispute) and PP-VERBAL-20261022-H-007 (option D arguably also correct).
11. ACT Math: 178 pending review and 16 on hold; generation paused, not worked.
12. ChatGPT overlay repairs are applied in this package, but the ChatGPT source files are unchanged; the owning workstream must adopt them.

## Outstanding for every item

Human review (rights and originality, two human blind solves, content audit, fairness, copy edit, accessibility, named approval), student calibration of difficulty, and the rights gate. All solvers so far are AI agents of the same model family, so they are not independent of the authors. Passing the import validator only makes an item eligible to **start** editorial stage 3.
