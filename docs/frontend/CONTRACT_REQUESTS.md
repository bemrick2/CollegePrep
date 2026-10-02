# Front-end contract requests

These are requests from the front-end (`web/`) to the backend session. Each one names the data the UI needs, the types it expects, and why. The UI already works without them: it either keeps the data in the browser, labels it as demo data, or shows an explicit "not available yet" state. Nothing here creates a competing schema. The backend owns the design; the shapes below describe what the UI reads.

Status as of 2026-10-02. In the live database: 0 exam versions, 0 skills, 0 questions and 0 households. The 2026-27 verified records cover 12 Tennessee institutions.

| ID | Need | Priority | UI today |
|---|---|---|---|
| CR-1 | Student planning preferences | High | Browser `localStorage`, per device |
| CR-2 | Benchmark sessions | High | Attempts are recorded; the summary is kept in the browser |
| CR-3 | Practice score estimates | High | Reads `student_test_scores` (`practice_estimate`); shows "pending" when there are none |
| CR-4 | Household cost projection | Medium | Live: "unavailable" state. Demo: illustrative numbers, labelled |
| CR-5 | Question content fields: passage, remember-this, hint count | High (before content load) | Fixtures only |
| CR-6 | Recommender diversification (v2) | Medium | v1 order, mirrored exactly |
| CR-7 | Institutions with verified records for a year | Low | Free-text search over `institutions` |

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
- The demo shows an illustrative panel behind a prominent "Illustrative example" banner.

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

## Product decisions flagged (not contract requests)

- **Benchmark counts as practice.** The benchmark's attempts count toward the streak and the weekly goal, because they are ordinary attempts. Students who finish onboarding with a benchmark see "Done for today".
- **Students in a household can't set their own goal.** That is the backend rule. The UI shows the backend error. If students should be able to propose goals, that is a product decision.
