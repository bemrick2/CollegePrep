# Front-end contract requests

These are requests from the front-end (`web/`) to the backend session. Each one names the data the UI needs, the types it expects, and why. The UI already works without them: it either keeps the data in the browser, labels it as demo data, or shows an explicit "not available yet" state. Nothing here creates a competing schema. The backend owns the design; the shapes below describe what the UI reads.

Status as of 2026-10-03 (backend contracts deployed in PR #54). Originally filed 2026-10-02: In the live database: 0 exam versions, 0 skills, 0 questions and 0 households. The 2026-27 verified records cover 12 Tennessee institutions.

| ID | Need | Backend status (PR #54) | UI today |
|---|---|---|---|
| CR-1 | Student planning preferences | ✅ live | `LiveSource` reads/writes `student_planning_preferences` |
| CR-2 | Benchmark sessions | ✅ live | `start_benchmark` → attempts with `p_benchmark` → `complete_benchmark`; history from `practice_benchmarks` (server metrics; the staircase ceiling is shown only for the run just finished) |
| CR-3 | Practice score estimates | ⛔ not produced, by design | No estimate anywhere, demo included; "No score estimate yet" with the reason |
| CR-4 | Household cost projection | ⏳ open | "Unavailable"; the parent view shows published costs and verified savings opportunities instead |
| CR-5 | Passages, remember-this, hint count | ✅ live | Passages and `hint_count` selected with questions; `remember_text` read from the submit result |
| CR-6 | Recommender v2 | ✅ live | No client change needed |
| CR-7 | Institutions with verified records | ✅ live | Comparison suggestions from `institutions_with_verified_records`, four-year schools with costs first |
| CR-8 | Answer-free help content | ✅ live | `concept_summary` and `sections` selected in the catalog |
| CR-9 | Institution level, saved schools | ✅ live | `level` from `compare_institutions`; saved schools via `save_/remove_household_school` (browser only for a student with no household) |
| CR-10 | Canonical exam keys, student exam plan | ⏳ open | College paths match exams by normalized name; the exam list is kept in this browser |
| CR-11 | Numeric test minimums on awards | ⏳ open | Single minimums parsed from `test_requirement` text; ranges/tiers shown as "read criteria" |
| CR-12 | Primary target school | ⏳ open | Designed and working in demo; hidden in live (`supportsPrimarySchool = false`), no client stand-in |
| CR-13 | Major certainty and saved interests | ⏳ open | Asked in onboarding and on Explore majors; kept in this browser |
| CR-14 | Structured program, admission and degree-path fields | ⏳ open | Program match by name; admission/transfer/undeclared shown as unverified questions; progression text quoted |
| CR-15 | Household home state | ⏳ open | Asked (optional) in onboarding and on cost screens; kept in this browser; labelled as the family's answer |

Live content note: the bank has no exam versions, skills or questions yet, so live practice and benchmarks show their empty states until content is loaded.

## CR-1. Student planning preferences

**Need.** Per student:

- `exam_family` (`'act' | 'sat'`)
- `target_score` (`integer | null`; ACT 1–36, SAT 400–1600)
- `goals` (`text[]`; keys `raise_score`, `merit`, `college_credit`, `lower_cost`, `explore`)
- `daily_minutes` (`integer`, 5–15)

**Why.** A parent sets the test and target during onboarding, and the student practises on their own device. Today these live in the browser, so the student never sees what the parent chose. The target drives the "N to go" gap on both dashboards.

**Suggested access.** Same as `weekly_practice_goals`. Read: the student and guardians with `view_progress`. Write: guardians with `set_goals`, and the student when independent or outside a household.

## CR-2. Benchmark sessions

**Need.** A benchmark grouping over existing attempts, plus a way to read past benchmarks:

```
practice_benchmarks: id uuid, student_id uuid, kind text ('initial'|'mini'|'full'),
  exam_version_id uuid, started_at timestamptz, completed_at timestamptz null,
  metrics jsonb null   -- optional server-computed summary
practice_attempts.benchmark_id uuid null
RPC start_benchmark(p_student, p_kind, p_exam_version) -> uuid
RPC complete_benchmark(p_benchmark) -> jsonb   -- per-section accuracy, pacing ratio, skips, returns, answer changes, calibration, traps
```

**Why.**

- Benchmarks run 20–40 minutes. `start_practice_session` only allows 5–15 minutes, so today the UI starts benchmark attempts with no session.
- Without a grouping, benchmark history is per browser, and a parent can't see their student's benchmark.

**Suggested metrics.** The metrics the UI computes are in `web/src/lib/engine/benchmark.ts` (`computeMetrics`). They are a suggested definition, not a requirement.

## CR-3. Practice score estimates

**Need.** Rows in `student_test_scores` with `score_source = 'practice_estimate'`, written by `service_role` after benchmarks and periodically, with `composite` and `section_scores`.

**Why.** Both dashboards show an estimated score next to the target. The UI already reads these rows and labels them "practice estimate — not an official score". It deliberately does not compute a scaled score itself, because that needs a calibrated model. Until rows exist, it shows a "pending" state.

## CR-4. Household cost projection

**Need.**

```
RPC cost_projection(p_student uuid, p_institution_keys text[], p_academic_year text, p_assumptions jsonb)
-> { status: 'available'|'unavailable', reason?: text,
     baseline_total: numeric, optimized_total: numeric, savings: numeric,
     levers: [{ key, label, estimated_savings numeric|null, source_url text|null, academic_year }] }
```

The levers are AP credit, CLEP, dual enrollment, merit awards at the student's score band, and a shorter time to degree.

**Why.** This drives the parent's "Projected cost, Optimized path, Potential savings" panel.

- The product rule is to show financial implications only when verified data supports them.
- The live UI therefore shows "unavailable" and links to the verified per-school comparison. That comparison does real arithmetic: published cost of attendance × years to degree, labelled as sticker price.
- Both sources show "unavailable"; the parent view shows published costs and verified savings opportunities instead (the illustrative demo panel was removed).

## CR-5. Question content fields (needed before the question bank is loaded)

1. **Passage or stimulus.**
   - `practice_questions` has no passage column, but ACT English, Reading and Science and SAT Reading & Writing need one. Several questions often share one passage.
   - Request: a `passage_id` that references `practice_passages(id, body text, title text null)`. Grant it like `stem`.
   - UI convention: in English items, `[bracketed text]` marks the underlined portion, and `[1]`-style markers are sentence numbers. The UI renders both.
2. **"Remember this."** A short takeaway of at most 16 words. Add a `remember_text` column to `practice_questions`, hidden until submit and returned by `submit_practice_attempt`. Today the live UI omits the card.
3. **Hint count.** Hints are hidden, so the client can't tell whether a question has any. Request a granted column or generated count (`hint_count integer`), so the Hint button can be hidden when there are none. Today the live UI shows the button and handles "No more hints".
4. **Choice format.** The UI expects `choices` as `[{ "key": "A", "text": "…" }]`. It also accepts plain strings and maps them to A, B, C…

## CR-6. Recommender diversification (v2)

**Need.** In `recommend_practice_set`, spread a session across skills and sections, and adapt difficulty.

**Why.** In v1, a student with no history gets a whole session ordered by question id, which in practice means all one section. The UI mirrors v1 exactly so that demo and live behave the same. It also labels each item with its reason ("Building a weak skill", "Working on speed", and so on).

## CR-7. Institutions with verified records for a year

**Need.**

```
RPC institutions_with_verified_records(p_academic_year text, p_state text null)
-> [{ institution_key, display_name, city, state_code, control, domains: text[] }]
```

**Why.** In live mode the comparison screen can only offer free-text search across 5,920 institutions. Most of them have no verified current-year records, so a parent can easily compare empty columns. Demo mode suggests the 12 schools that do have verified 2026-27 records.

## CR-8. Answer-free help content (pre-answer "Teach me" and "Test strategy")

**Need.**
- `skills.concept_summary` (`text | null`): a 1–3 sentence lesson on the skill that never refers to a specific question.
- `question_strategies.sections` (`text[]`): sections where the strategy applies (`english`, `math`, `reading`, `science`, `reading_writing`).
- Both readable wherever `skills` and `question_strategies` are readable today; served by the existing table reads (no new RPC).

**Why.** Students ask for help *before* answering. "Teach me" and "Test strategy" must help without revealing the answer, so they can't use the per-question explanations or the question's tagged strategy (those stay hidden until `submit_practice_attempt`). The UI still calls `request_ai_help(attempt, 'concept' | 'strategy')` so help use is recorded.

## CR-9. Institution level and saved schools

**Need.**
1. `level` (`'two_year' | 'four_year'`) on the institution identity returned by `compare_institutions` (and `institutions` reads). Source: IPEDS HD `ICLEVEL`, already used by the research registry.
2. Saved schools per household: `household_id`, `institution_key`, `added_by`, `added_at`; up to ~8 per household. Read: household members with `view_progress`; write: guardians and the linked student.

**Why.**
1. The parent cost outlook multiplies a published annual cost by years to degree. Without the level it can't tell a 2-year college from a 4-year one, so live mode shows cost per year only and never compares across levels.
2. The schools a family is comparing drive the parent dashboard, the cost outlook and (later) college-path suggestions. Today they live in one browser, so a parent's list doesn't follow them to another device or reach the student.

## CR-10. Canonical exam keys and the student's exam plan

**Need.**
1. A canonical exam key on `credit_equivalencies` (for example `exam_key = 'ap:calculus-ab'`), the same across institutions. Today codes vary by school (`AP-CALCAB` / `AP-CALCULUS-AB`, `AP-USH` / `AP-UNITED-STATES-HISTORY`), and names vary too ("AP American History" / "AP United States History").
2. A per-student exam plan: `student_id`, `exam_key`, `score` (null = planned), `taken_on` (optional). Read: household members with `view_progress`; write: guardians and the linked student. Maximum about 20 rows.

**Why.**
1. The College paths screen matches a student's AP/CLEP exams against each saved school's verified table. Until there is a shared key, it matches on a normalized name. An exam a school lists under an unexpected name shows as "Not in the published table", which is safe but can miss credit.
2. The exam list currently lives in one browser, so a parent's entries don't reach the student or another device.

## CR-11. Numeric test minimums on merit awards

**Need.** On `awards` (served by `compare_institutions`): `act_min integer null`, `sat_min integer null`, and `test_criteria_kind` (`'single_minimum' | 'tiered' | 'range' | 'test_optional' | 'none'`), set when the award is reviewed. Tiered awards could add `test_tiers jsonb` (`[{ act_min, sat_min, amount }]`).

**Why.** The parent "What to do next" card and the College paths merit row compare published test minimums with the student's target or official score. Today the minimum exists only as free text ("Minimum 31 ACT / 1390 SAT."). The UI extracts a single minimum only when the text states one plainly, and treats ranges, tiers and anything ambiguous as "read the criteria". That is safe but misses tiered awards such as UTK's Volunteer Scholarship.

## CR-12. Primary target school

**Need.**
- `household_saved_schools.is_primary boolean not null default false`, with at most one primary per household (partial unique index on `household_id where is_primary`).
- `set_household_primary_school(p_household uuid, p_institution_key text null)`: sets the primary; null clears it. The school must already be saved. Same write rule as `save_household_school`.
- `remove_household_school` clears the primary when it removes that school.
- `is_primary` is returned with the saved-schools read.

**Why.** Families compare up to four schools but usually have one they most want. The parent overview elevates that school: its published 4-year cost and the top ways to lower it (merit gap, exam credit, dual enrollment, need-based programs, aid appeal). College paths and the cost outlook list it first.

**UI today.** `DataSource.supportsPrimarySchool` gates the feature. Demo: true, stored in the browser. Live: false, so the control and the dashboard card are hidden and nothing is stored client-side. When this lands, the LiveSource change is the two methods plus the flag.

## CR-13. Major certainty and saved interests

**Need.** `student_academic_interests` with these columns:
- `student_id`
- `certainty`: `'unsure' | 'few' | 'sure' | null`
- `interests jsonb`: `[{ kind: 'area' | 'major', key, focus? }]`, up to 8 entries, with keys from the frontend list in `web/src/lib/engine/interests.ts`; alternatively a lookup table, if research prefers to own it
- `updated_at`

Read: household members with `view_progress`. Write: the linked student and guardians. None of it is required at any step.

**Why.** Onboarding now asks how sure the student is about a major, and they can save broad areas or several possible majors. College paths and Explore majors evaluate every saved school against all of those interests. Today this is stored in one browser, so a parent's view on another device doesn't see it.

## CR-14. Structured program, admission and degree-path fields

**Need.** The fields below are listed in priority order. Each should have the usual source URL, academic year and verification status, and null means "not verified". Never fill them by inference.
1. `academic_programs.cip_code`: 6-digit CIP, so interests match programs by classification instead of by name. All 94 imported programs have it null today.
2. `academic_programs.admission_type`: `'direct' | 'pre_major' | 'open'`. Whether the major requires direct/freshman admission. The UI already renders "Freshman admission required" when it is `direct`.
3. `academic_programs.internal_transfer`: `{ restricted: boolean, criteria_text, gpa_min? }`. Whether changing into the major after enrolling is limited.
4. Institution-level `undeclared_policy`: `{ allowed: boolean, declare_by_text }`. Whether students can start undeclared or exploratory.
5. `credit_equivalencies.applies_to_programs`, or the existing `applies_to_major` populated per program. How AP/CLEP/IB/dual-enrollment credit applies by degree path.
6. `awards.program_keys` / `cip_codes`. Major-specific scholarships as structured links (`major_requirement` text exists but is usually empty).
7. Program coverage completeness flag per institution and year (`programs_complete boolean`). Lets the UI say "not offered" instead of "not in our verified list".

**Why.** The "keeps my options open" view answers each of these per school and per saved interest. Until the fields exist it shows only what's verified today:
- matched program names
- quoted progression text from degree maps (for example UTK CS's "competitive and space-limited")
- shared first-year courses, where two published maps exist

Everything else is shown as a question to ask the school.

## CR-15. Household home state

**Need.** `households.home_state char(2) null` (and the same on a self-managed student profile), editable by guardians (or the student when there's no household), and returned with the household context. Optional everywhere.

**Why.** Cost screens choose a school's in-state or out-of-state published price from the family's home state. Without it, every school showed its cheapest residency price, which understates cost for out-of-state options (for example, a Tennessee family looking at Oregon). The UI labels the state as the family's answer, not a residency determination. When a school publishes no out-of-state price, the UI flags it instead of showing the in-state figure as theirs. The state currently lives in one browser.

## Product decisions flagged (not contract requests)

- **Benchmark counts as practice.** The benchmark's attempts count toward the streak and the weekly goal, because they are ordinary attempts. Students who finish onboarding with a benchmark see "Done for today".
- **Students in a household can't set their own goal.** That is the backend rule. The UI shows the backend error. If students should be able to propose goals, that is a product decision.
