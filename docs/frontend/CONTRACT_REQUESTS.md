# Front-end contract requests

These are requests from the front-end (`web/`) to the backend session. Each one names the data the UI needs, the types it expects, and why. The UI already works without them: it either keeps the data in the browser, labels it as demo data, or shows an explicit "not available yet" state. Nothing here creates a competing schema. The backend owns the design; the shapes below describe what the UI reads.

Status as of 2026-10-03 (backend contracts deployed in PR #54). Originally filed 2026-10-02: In the live database: 0 exam versions, 0 skills, 0 questions and 0 households. The 2026-27 verified records cover 12 Tennessee institutions.

| ID | Need | Backend status (PR #54) | UI today |
|---|---|---|---|
| CR-1 | Student planning preferences | ✅ live | `LiveSource` reads/writes `student_planning_preferences` |
| CR-2 | Benchmark sessions | ✅ live | `start_benchmark` → attempts with `p_benchmark` → `complete_benchmark`; history from `practice_benchmarks` (server metrics; the staircase ceiling is shown only for the run just finished) |
| CR-3 | Practice score estimates | ⛔ not produced, by design | No estimate anywhere, demo included; "No score estimate yet" with the reason |
| CR-4 | Household cost projection | 🚧 v2 proposed by Design (migration `20261007120000_cost_projection_v2.sql`), needs Research review | Cost & savings view (`/colleges/savings`) on `cost_projection` v2; the demo runs the same rules in `engine/costProjection.ts` |
| CR-5 | Passages, remember-this, hint count | ✅ live | Passages and `hint_count` selected with questions; `remember_text` read from the submit result |
| CR-6 | Recommender v2 | ✅ live | No client change needed |
| CR-7 | Institutions with verified records | ✅ live | Comparison suggestions from `institutions_with_verified_records`, four-year schools with costs first |
| CR-8 | Answer-free help content | ✅ live | `concept_summary` and `sections` selected in the catalog |
| CR-9 | Institution level, saved schools | ✅ live | `level` from `compare_institutions`; saved schools via `save_/remove_household_school` (browser only for a student with no household) |
| CR-10 | Canonical exam keys, student exam plan | ⏳ open | College paths match exams by normalized name; the exam list is kept in this browser |
| CR-11 | Numeric test minimums on awards | ⏳ open | Single minimums parsed from `test_requirement` text; ranges/tiers shown as "read criteria" |
| CR-12 | Primary target school | ⏳ open | Designed and working in demo; hidden in live (`supportsPrimarySchool = false`), no client stand-in |
| CR-13 | Major certainty and saved interests | ⏳ open | Asked in onboarding and on Explore majors; kept in this browser |
| CR-14 | Structured program, admission and degree-path fields | 🚧 schema in PR #89, data in #91/#92 | Program match by name; admission/transfer/undeclared shown as unverified questions; progression text quoted |
| CR-15 | Household home state | ⏳ open | Asked (optional) in onboarding and on cost screens; kept in this browser; labelled as the family's answer |
| CR-16 | Subscription owner + household entitlement | ⏳ open | No plan, price, paywall or entitlement state anywhere; nothing simulated |
| CR-17 | How each school bills tuition (flat rate or per credit) | ⏳ open | Credit savings counted only as whole terms finished early; the remainder is shown, not counted |
| CR-18 | Loan terms (federal limits, rates) as sourced records | ⏳ open | Families enter planned borrowing; it is shown as borrowed, never as a saving; no limits or rates shown |
| CR-19 | Credit applicability: hours on equivalency rows, elective/gen-ed designations, plans for more majors | ⏳ open | Credit checked course by course against the major's verified plan where one exists; otherwise "unknown"; savings shown only as potential |
| CR-20 | Cost-of-attendance period (academic year vs 12 months) | ⏳ open | COA labelled "academic year"; summer and break living is the family's own number |
| CR-21 | Question review metadata; serve only reviewed items | 🚧 migration `20261007140000` merged (#142), unapplied on hosted | Demo and local DB serve only items whose current content hash a review approved (`questionReview.ts`); live has no review fields |
| CR-22 | Parent emails: weekly-summary opt-in, service-only digest and inactivity payloads, delivery log | ⏳ open (reference SQL in `scripts/local/proposals/cr22_parent_emails.sql`, local only) | Opt-in and email preview behind `VITE_WEEKLY_DIGEST`; sender `supabase/functions/send-weekly-digest` (not deployed) |

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

**Backend response (Program & Degree Deep Dive, PR #89).** Migration `20261005150000_program_depth_cr14`:
- Items 1–3 are columns on `academic_programs` and so appear in `compare_institutions` → `domains.academic_programs`:
  - `cip_code` + `cip_source_url`
  - `admission_type` + `admission_details {quote, source_url, source_sha256, criteria_text?, gpa_min?, paths?}`. `paths` lists a selective first-year path beside the standard one.
  - `internal_transfer {restricted, quote, source_url, criteria_text?, gpa_min?}`
  - `college`
- Items 4 and 7 come from `program_catalog_status(keys, year)`, which returns one `program_catalogs` row per school and year: `programs_complete`, `listed_bachelor_programs`, `completeness_basis` and `undeclared_policy {allowed, quote, source_url, declare_by_text?}`. When `programs_complete` is not true, show "not in our verified list".
- Item 6: `institutional_awards.program_keys` / `cip_codes`.
- Item 5 (per-program credit applicability) is not modelled yet. Printed sample plans (`requirement_kind = 'program_plan'`) carry course codes per term.
- **Partially verified state-inventory records.** Some Tennessee programs come from the THEC Academic Program Inventory: active state-approved programs with CIP, but no year label. They are `partially_verified`, so `compare_institutions` does not return them.

## CR-15. Household home state

**Need.** `households.home_state char(2) null` (and the same on a self-managed student profile), editable by guardians (or the student when there's no household), and returned with the household context. Optional everywhere.

**Why.** Cost screens choose a school's in-state or out-of-state published price from the family's home state. Without it, every school showed its cheapest residency price, which understates cost for out-of-state options (for example, a Tennessee family looking at Oregon). The UI labels the state as the family's answer, not a residency determination. When a school publishes no out-of-state price, the UI flags it instead of showing the in-state figure as theirs. The state currently lives in one browser.

## CR-16. Subscription owner and household entitlement

**Need.** Three pieces, with the full field list and event map in `docs/product/APP_DISTRIBUTION_AND_PAYMENTS.md` ("Entitlement model"):

- `household_subscriptions`, with these fields:
  - `household_id`, `owner_user_id`, `plan_key`
  - `source` (`web | apple | google | comp`), `source_subscription_id`
  - normalised `status`, `auto_renew`, period start/end
  - `environment` (production or sandbox)
- an append-only `household_subscription_events` log
- a `household_entitlement(p_household)` read RPC returning `{ active, plan_key, status, period_end, source, owner_user_id, manage_url_hint }`

Every household member can read the entitlement: guardians with `view_progress` and linked students. Source details are visible only to the owner and to guardians with `can_manage_billing`. Writes come only from server-side handlers:

- the web processor's webhooks
- App Store Server Notifications v2, plus verification of the signed transaction the app sends (`appAccountToken` = household id)
- Play Real-time Developer Notifications, only if Google billing is adopted

**Decision recorded (2026-10-05).** The website is primary. iOS offers the same household plan through Apple IAP, with no external checkout link. Our backend is the system of record; Apple and Google are only payment sources. Android uses the same entitlement model, and adds Play Billing only if policy requires it.

**Why.**
- A web subscriber must sign in to the iOS app and get access without buying again.
- An iOS purchase must also unlock the web and the student's account.
- Ownership (usually a parent) is separate from who uses the app (often the student).

**UI today.** No plan, price, paywall or entitlement state anywhere until this lands. Nothing is simulated.

## CR-4 v2 (proposed by Design, 2026-10-07)

v1 returned `missing_cost` for every school that publishes one price for all students (7 of the 12 schools in the comparison snapshot), and counted exam credit only under a transfer cap, which no school has on file. v2 keeps the signature and v1's rules, and changes:

- **Residency.** Falls back to a verified `not_applicable` row; `cost.residency` says which row was used.
- **Components.** `cost.components` lists tuition, fees, housing and food, books, transportation, personal, other, COA, and `living_and_other` (COA − tuition − fees, only when all three are published).
- **Exam credit.** New `exam_credits` assumption: AP/IB/CLEP/Cambridge credit read from the school's own published equivalency table. It is bounded by a verified exam-credit limit if one exists, and needs no transfer cap.
- **Residency rule.** A verified residency requirement bounds all outside credit against the plan's own credit total.
- **Mechanism.** `credit_savings` gives `mechanism: fewer_terms`, `billing_structure: unknown`, `remainder_credits` and a by-component split.
- **Aid and loans.** Awards and state aid stay listed, never subtracted. `not_counted.loans = 'no_data'`.

SQL tests are in `supabase/tests/frontend_contracts.sql`. The local end-to-end test checks the server against the demo mirror.

## CR-17. How each school bills tuition

**Need.** Per institution and year: `tuition_structure` (`flat_rate` with the credit band, e.g. 12–18, or `per_credit` with the rate), with source.

**Why.** It decides whether credit brought in lowers a term's bill (per credit) or only saves money by finishing early (flat rate). Until then, only whole terms are counted.

## CR-18. Loan terms as sourced records

**Need.** Federal Direct loan annual and aggregate limits by dependency status and year in school, plus the current interest rates and fees, each with a source URL and effective dates.

**Why.** It lets the cost view say how planned borrowing compares with what a student can borrow, and what it costs to repay. Until then, the view shows only what the family enters, labelled as borrowed.

## CR-19. Credit applicability to a major

Today the client checks credit at three levels:
1. **Accepted.** The school's own table awards the course.
2. **Applies.** The awarded course code appears in the selected major's verified term-by-term plan.
3. **Removes a term.** Every item of a whole plan term is covered.

Savings are shown only as potential, under stated assumptions. The UTK snapshot shows the gaps:

- **No hours on core courses.** The courses that matter most carry no `credits_awarded`. For example, AP Calculus BC with a 5 earns MATH 147-148, which fits Terms 1-2 of the CS plan, but its hours are unpublished. Credit that applies to the major therefore can't be counted in dollars.
- **Electives are opaque.** Elective-only credit ("ARTH LD", "ART LD") may fill a plan's elective slot, such as "Arts and Humanities elective", but which slots a course can fill isn't recorded.
- **One plan only.** There is a term-by-term plan for one UTK program only (Computer Science, BS).
- **Same score, different courses.** Several exams list different courses at the same score (UTK AP Physics C E&M, score 4: PHYS 136, or one of PHYS 102/222/231), and the condition that picks between them isn't recorded.

**Need:**
- `credits_awarded` on every equivalency row.
- The general-education or elective attributes of each awarded course, as `satisfies: [category]`.
- The condition that selects between rows at the same score (program, admit term).
- Term-by-term plans for more programs, in the existing `rule_details.terms` shape.

## CR-20. Cost-of-attendance period

**Need.** On `institution_costs`, `period` (`academic_year` with months, or `twelve_month`), from the school's budget page.

**Why.** The view treats the published budget as the academic year, and asks the family for summer and break living separately. If a school's budget already covers twelve months, that would double-count.
## CR-21. Question review metadata

**Need.** These columns on `practice_questions`:
- `review_status` (`approved`, `changes_needed`, `rejected`);
- `reviewed_at`;
- `review_method`;
- `content_hash`.

`start_practice_session`, `start_practice_attempt` and the published-question policy should also require `review_status = 'approved'` and a hash matching the current content, as well as `status = 'published'`.

**Why.** The live bank is empty today. When content is loaded, nothing in the schema says whether an item's key and explanations were checked.

In the app and the local database, an item is served only if a review approved its exact current content. The review record lives at `web/src/lib/data/demo/questionReviews.json`, built by `scripts/local/recordReviews.ts`. The method is two independent blind solves of every item, plus a key and explanation audit; disagreements are worked by hand. It is AI review, not human editorial review, and the record says so (`human_reviewed: false`).

## CR-22. Parent accountability emails

**Need.** A scheduled sender has no signed-in user, so it needs service-role-only data functions. A reference implementation runs on the local disposable database only, in `scripts/local/proposals/cr22_parent_emails.sql`:

- `alert_preferences.weekly_digest`: the guardian opts in per student. Default off; the guardian may write it.
- `parent_email_deliveries(user_id, kind, period_key)`: one row per email sent, so sending is idempotent.
- `weekly_digest_payload(p_week_start date) returns setof jsonb`: one row per opted-in guardian who hasn't already been sent that week. It covers each student's goal, questions submitted, practice days, last practice, up to three focus skills, last progress check and the inactivity state.
- `inactivity_alert_payload() returns setof jsonb`: guardians whose enabled alert threshold is reached, once per stretch without practice. The period key is the student plus their last practice time.
- `mark_parent_email_sent(user, kind, period_key) returns boolean`: false if already recorded.

**How the reference works.** The payload functions call the existing dashboard RPCs as each guardian: `request.jwt.claims` is set to that guardian for the call and then restored. That way the recipients and the numbers follow the same permission checks and rules as the parent dashboard, with no second copy of them. Research may prefer a different mechanism; the payload shapes are what the sender and its tests rely on (`supabase/functions/send-weekly-digest/digest.ts`).

**Decision to flag: service role.** Unlike the invitation function, the sender uses the service-role key, because there is no user session. It reads only through the functions above.

**Deployment (held while Supabase is paused).** After the CR-22 migration is applied:
1. Deploy `send-weekly-digest`.
2. Set its secrets: `DIGEST_CRON_SECRET`, `RESEND_API_KEY`, and optionally `DIGEST_FROM_EMAIL` and `APP_ORIGINS`.
3. Add a scheduler: weekly for `{"mode":"weekly"}` (Monday morning) and daily for `{"mode":"inactivity"}`.
4. Set `VITE_WEEKLY_DIGEST=true` for the web build.

**Tested locally.** `web/scripts/local/parentEmails.local.test.ts` runs the real function under Deno against the local database with a fake mail endpoint. It checks:
- the scheduler secret is required;
- dry-run content matches the dashboard numbers;
- a guardian who did not opt in gets nothing;
- a week's summary is sent once only;
- a failed send is retried, and an inactivity alert is sent once per stretch.

## Product decisions flagged (not contract requests)

- **Benchmark counts as practice.** The benchmark's attempts count toward the streak and the weekly goal, because they are ordinary attempts. Students who finish onboarding with a benchmark see "Done for today".
- **Students in a household can't set their own goal.** That is the backend rule. The UI shows the backend error. If students should be able to propose goals, that is a product decision.
