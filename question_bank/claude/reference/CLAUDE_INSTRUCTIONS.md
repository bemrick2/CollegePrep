# Prep & Price — Claude Code question-bank assignment

You are building an independent, original ACT/SAT question bank for Prep & Price. Do not copy or closely paraphrase any reference questions. Treat any practice exams uploaded separately as references only for style, tested skills and difficulty.

Start with ACT Math. Work in batches of 10 accepted questions, and continue up to five batches per run if possible. For each question provide a unique `CLD-ACT-M-000001`-style ID, exam, section, skill, subskill, difficulty (easy/medium/hard), stem, four choices A–D, answer, solution, and explanations for all distractors. Use current exam specifications; verify any uncertainty before proceeding. Maintain approximately 25% easy, 50% medium, 25% hard across the bank. Expand later to ACT English, ACT Reading and digital SAT Reading & Writing, with passage IDs where appropriate.

For quality control, independently solve each problem, verify one unambiguously correct answer, check calculations and distractors, and reject ambiguity, errors, near-duplicates and unoriginal material. Track PASS/REVISE/REJECT, and only export PASS items. Use JSON files grouped by exam/section and a progress.json tracking counts, skill coverage, difficulties, batch number and next steps. Never overwrite accepted items; use atomic/version-safe writes. Make a separate student-facing export without answers. Every 100 accepted questions run a cross-batch audit for near duplicates and skill balance.

Do not publish, deploy, edit the live application, or spend money. If execution cannot continue, save checkpoint and report what was actually completed. If no reference exams are provided, proceed with original questions, noting that reference-based style calibration is pending.

First, inspect SAMPLE_QUESTIONS.json for schema examples only. These are freshly written starter examples, not extracted from the user's prior uploaded practice exams. Validate the sample examples yourself before using them as a schema reference. Then generate and validate 10 new ACT Math questions. Continue sequentially as resources permit.
