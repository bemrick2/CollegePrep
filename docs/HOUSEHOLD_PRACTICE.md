# Households, students and practice

Migration `20261002183112_household_practice_progress` holds the user-data and practice schema. It needs Supabase Auth (`auth.users`, `auth.uid()`). CI supplies a minimal stand-in in `supabase/tests/support/auth_stub.sql`, which does nothing on a real Supabase project.

Tests:

- `supabase/tests/household_access.sql`: accounts, permissions and subscriptions.
- `supabase/tests/practice_engine.sql`: content, grading, analytics.
- `tests/test_household_schema.py`: static privilege checks.

Both SQL tests share fixtures in `supabase/tests/support/test_helpers.sql` and roll back.

The migration seeds no content. Exams, skills, strategies, traps and questions are loaded as data, by `service_role`.

## Accounts

- **profiles**: one row per auth user (display name only).
- **households**: a family, with a `time_zone` (an IANA name, default `UTC`). `created_by` becomes null if the creator's account is deleted; the household survives.
- **household_members**: links a user to a household as a `guardian` or `student`. Guardians carry five flags:
  - `can_manage_students`
  - `can_set_goals`
  - `can_view_progress`
  - `can_manage_members`
  - `can_manage_billing`

  Student members never hold flags (a check constraint enforces this). The household creator gets every flag.
- **students**: a student profile.
  - It stores no date of birth, only graduation year and grade level.
  - `household_id` is null for a profile outside any household.
  - `linked_user_id` is the student's own login, unique per user.
  - `is_independent` marks an adult who manages their own goals.
  - `time_zone` is optional and overrides the household's.
  - If a household is deleted, its students are detached, not deleted.
- **household_invitations**: single-use, expiring codes. Only the SHA-256 hex digest is stored; the plaintext is returned once.
  - A guardian invitation carries a `permissions` list; the default is manage_students, set_goals and view_progress.
  - A student invitation either names a guardian-created profile to claim, or names none, in which case the accepting student brings their own profile.

### Account flows

```
Parent-created, later claimed
  guardian: create_household -> add_student -> create_household_invitation('student', student_id)
  student:  accept_household_invitation(code)  => links profile, account_mode = student_login

Student-created, later joins a parent
  student:  create_self_student_profile(name, ...)       => household_id null, student owns it
  guardian: create_household_invitation('student')       (no student_id)
  student:  accept_household_invitation(code)            => own profile moves into the household

Independent adult
  student:  create_self_student_profile(..., p_independent => true)
            sets own goals; never targetable by a guardian invitation;
            may still join a household only by accepting an invitation themself

Leaving
  student:  leave_household(h)  => membership removed, profile and full history leave with them (household_id = null)
  manager:  remove_household_member(h, user) => same effect for a student; a guardian simply loses access
```

There is only one path that moves a student profile into a household: an invitation accepted by the student. The student-generated join code was left out because it would add a second path doing the same thing. An existing student profile can never be pulled into a household by a guardian.

**Leaving keeps the history with the student.** When a student leaves or is removed, their attempts, goals, sessions and scores stay with their profile. Guardians immediately lose access, and guardians' alert preferences for that student are deleted. This favours the student as the owner of their record. A household that needs to retain history should archive the student rather than remove them.

**Last-manager rule.** `update_member_permissions`, `remove_household_member` and `leave_household` all fail if the household would be left with no member holding `can_manage_members`.

## Subscriptions

- **subscriptions** fields:
  - `owner_user_id`: the payer. Separate from students and from household roles.
  - `household_id`: optional.
  - `plan_key`, `status` (`trialing`, `active`, `past_due`, `canceled`, `incomplete`), `current_period_end`.
  - Provider identifiers.
- **Writes:** only by `service_role`, intended for payment-provider webhooks. No payment logic exists.
- **Reads:** the owner and guardians holding `can_manage_billing` can read the row, except `provider_customer_id` and `provider_subscription_id`, which are never granted to clients.
- **`household_entitlements(household)`:** any household member can call it. It returns only `plan_key`, `status` and `current_period_end`.

## Access matrix

"Progress data" means attempts, attempt events, sessions, session items, AI-help requests, test scores, and the analytics RPCs (`student_weekly_progress`, `student_skill_estimates`, `student_streak`, `recommend_practice_set`, `student_inactivity`).

| Data | Guardian (flag needed) | Linked student | Other authenticated | anon |
|---|---|---|---|---|
| household, roster of students, member list | any guardian, even with no flags (read); `manage_members` to rename the household or change its time zone | own household, own profile, own membership | none | none |
| add or edit students | `manage_students` | own profile, only when independent or outside a household | none | none |
| invitations | read: any guardian; create a guardian invitation: `manage_members`; create a student invitation: `manage_students` | none | accept with a code | none |
| member flags, removal | `manage_members` | `leave_household` only | none | none |
| weekly goals | read and write: `set_goals`; read: `view_progress` | read; write when independent or outside a household | none | none |
| progress data | `view_progress` | always (own) | none | none |
| subscriptions | `manage_billing` (read, provider identifiers excluded) | none unless owner | owner reads own | none |
| entitlements RPC | any member | any member | none | none |
| alert preferences | own rows, for students the guardian can view | own rows | own rows | none |
| self-reported scores | insert: `manage_students`; delete own entries | insert; delete own entries | none | none |
| catalog (exam versions, types, skills, traps, strategies) | read | read | read | none |
| published questions (safe columns) | read | read | read | none |

Practising is limited to the linked student. Guardians cannot start, answer, skip, request hints or request AI help on the student's behalf. No client role can write attempts, events, sessions, session items, AI-help requests, memberships, invitations, subscriptions or app settings directly.

All functions use `search_path = ''`. Client RPCs and policy helpers are executable by `authenticated` only. Internal helpers are executable by no client role. A denial raises SQLSTATE `42501`; invalid input raises `22023`.

## Practice content

- **exam_families** (`act`, `sat`) and **exam_versions** (`version_key` such as `sat_digital_2024` or `act_enhanced_2025`, with `effective_from` and `effective_to`). Each version stores `rules` as jsonb: sections, timing, question counts, scoring scale and calculator policy. Nothing is hard-coded.
- **question_types** belong to one exam version. A question's type must belong to the question's own version; a composite foreign key enforces this.
- **skills** form a tree (`parent_id`, within one exam family): section, domain and skill. **practice_question_skills** links questions to skills, many-to-many, with at most one primary skill per question.
- **practice_questions** fields:
  - `exam_version_id`, `question_type_id`, `section`.
  - `difficulty`: 1–5, plus an optional `difficulty_calibrated` value and a `difficulty_label`.
  - `expected_time_seconds`, `answer_format`, `accepted_answers`.
  - Ordered `hints`, `teaching_explanation`, `strategy_explanation`.
- **practice_question_distractors**: for each wrong choice, why it is wrong and its `trap_types` classification.
- **practice_question_strategies**: role (primary or secondary), `is_fastest` (the fastest appropriate test-day strategy) and `strategy_explanation`.

**Hidden until submission.** Clients never receive these:

- `accepted_answers`
- `hints`
- `teaching_explanation`
- `strategy_explanation`
- every distractor row
- strategy explanations

Column grants enforce this, so `select *` on `practice_questions` is denied. Hints come out one at a time through `request_hint`. Everything else is returned only by `submit_practice_attempt`.

**Grading** (`grade_answer`):

| `answer_format` | Rule |
|---|---|
| `choice` | Exact match after trimming whitespace (case-sensitive). |
| `numeric` | Numeric equality of parsed values. `1/2`, `2/4`, `.5` and `0.5` are equal. Integers, decimals and simple fractions are parsed; anything else, or a zero denominator, never matches. A check constraint requires stored numeric answers to be parseable. |
| `text` | Case-insensitive match after trimming. |

## Attempts and events

| RPC | Effect |
|---|---|
| `start_practice_attempt(student, question, session?)` | Requires a published question. Sets `presented_at` to server time, assigns the next `attempt_number` and logs `presented`. |
| `record_attempt_event(attempt, 'answered' \| 'skipped' \| 'returned', answer?)` | Logs an answer selection (`changed_answer` when it differs from the previous selection; an identical repeat is not logged), a skip-for-now, or a return to the question. |
| `request_hint(attempt)` | Returns the next hint and the number remaining, increments `hint_count` and logs `hint`. Fails when hints run out or the attempt is submitted. |
| `submit_practice_attempt(attempt, answer, active_ms?, first_interaction_ms?, confidence?, strategy_key?, skipped=false)` | Can be called once per attempt. Computes `submitted_at`, `elapsed_ms` and `is_correct` on the server; stores confidence (1–3) and the strategy used. Returns the grade, elapsed time, accepted answers, explanations, distractor rationales with trap keys, and strategies (fastest first). |
| `request_ai_help(attempt, mode)` | See AI help below. |

`practice_attempt_events` is append-only and stamped with server time. Its kinds are `presented`, `answered`, `changed_answer`, `skipped`, `returned`, `hint`, `ai_help` and `submitted`. Only RPCs write it.

**Skips.** Submitting with `p_skipped => true` closes the attempt with no answer and `is_correct` null. The answers are still revealed. Skipped attempts count in `skipped`, never in `questions_submitted` or accuracy, and they don't count toward streaks or question goals. Their time does count in `total_elapsed_ms`. A `skipped` event logged mid-attempt, followed later by `returned`, records skip-and-come-back behaviour without closing the attempt.

**Timing.**

- Server-computed, trustworthy: `presented_at`, `submitted_at`, `elapsed_ms`, `is_correct`.
- Client-reported: `active_ms` and `first_interaction_ms`. A negative value is rejected, and so is a value greater than the server elapsed time. Nothing is clamped silently.

## Sessions and the recommender (v1 heuristic)

`start_practice_session(student, target_minutes=10, goal?, exam_version?)` takes 5–15 minutes. It stores the planned list in `practice_session_items` (with an ordered position and a reason) from `recommend_practice_set(student, target_minutes, exam_version?)`.

The recommender is SQL and deterministic for the same data:

1. **Candidates:** published questions with an `expected_time_seconds`, optionally from one exam version.
2. **Buckets,** by the primary skill's estimate, in this order:
   1. `weak_knowledge`
   2. `weak_pacing`
   3. `new_skill` (the student has no data on that skill)
   4. `review`
   5. `untagged` (no primary skill)
3. **Order within a bucket:** never-seen questions first, then least recently presented, then by question id as the tie-break.
4. **Time budget:** walk the list, adding each question whose expected time still fits within `target_minutes × 60`. Questions that don't fit are skipped and the walk continues.

It does not spread a set across skills, and it does not adapt difficulty. Those are left for v2.

## Skill estimates: knowledge separate from pacing

`student_skill_estimates(student)` returns one row per primary skill.

- **Data used:** the student's 30 most recent submitted, non-skipped attempts on that skill.
- **Per-skill fields:**
  - `attempts`, `correct`
  - `accuracy` (knowledge)
  - `median_elapsed_ms`
  - `pacing_ratio`: the median of `elapsed / expected_time` (pacing)
- **Flags:**

  | Flag | Rule |
  |---|---|
  | (both) | null (insufficient data) when attempts < 5 |
  | `knowledge_weak` | `accuracy < 0.6` |
  | `pacing_weak` | `accuracy ≥ 0.6` and `pacing_ratio > 1.25`. Null if the questions have no expected time. A student who is wrong *and* slow is flagged for knowledge only, because pacing is meaningless until answers are right. |

These estimates describe practice performance only. They are not predicted scores.

## Weekly goals: fixed and adaptive

`weekly_practice_goals` has a Monday `week_start`, `target_questions` and/or `target_minutes`, an optional subject, and a `goal_mode` (`fixed` or `adaptive`).

- **Who writes goals:** guardians with `can_set_goals`. An independent student, or a student outside any household, writes their own.
- **Who reads goals:** the student and guardians with `can_view_progress`.

`suggest_next_week_goal(student, week_start?)` only proposes targets; the caller applies them as an ordinary goal write. The v1 rule:

1. **History used:** overall goals (no subject) from the previous 4 weeks.
2. **Completion per week:** submitted questions ÷ target, or elapsed minutes ÷ target, capped at 1.5.
3. **History required:** each target needs at least 2 weeks that had that target. Otherwise it is null, with `basis = insufficient_history`.
4. **Adjustment:** the next value starts from the most recent target and is changed by the mean completion:

   | Mean completion | Change |
   |---|---|
   | ≥ 1.0 | +10% |
   | 0.7 – 1.0 | hold |
   | < 0.7 | −15% |

5. **Clamping:** the result is rounded and kept within 5–200 questions and 10–600 minutes.

## Time zones, streaks and weekly progress

- **Time zone used:** the student's `time_zone`, else the household's, else UTC. Every time-zone input is validated against `pg_timezone_names`.
- **Week window:** a week is `[week_start 00:00, week_start + 7 days 00:00)` in that local zone. For example, Sunday 23:30 in Los Angeles belongs to the week that is ending.

`student_streak(student, tz?, as_of?)` returns `current_streak`, `longest_streak` and `last_practice_day`.

- A practice day is a local calendar day with at least one submitted, non-skipped attempt.
- The current streak stays alive through yesterday, so it isn't shown as broken before today's practice.

`student_weekly_progress(student, week_start)` requires the linked student or `can_view_progress`. It returns:

- `time_zone`
- `goal` (including `goal_mode`) and `goal_progress`: `questions_pct` and `minutes_pct`, null without a goal
- `questions_attempted`, `questions_submitted`, `skipped` (final skips), `skip_events`, `returns`, `answer_changes`
- `correct`, `accuracy` (null with zero submissions)
- `total_elapsed_ms`, `total_active_ms` (null without client data), `median_elapsed_ms`
- `avg_confidence`, `ai_help_attempts`, `hints_used`
- `streak`: current and longest, as of the end of that week or today
- `skill_summary`: lists of knowledge-weak and pacing-weak skill keys, and a count of skills with insufficient data
- `by_skill` and `by_strategy`

## Inactivity alerts (data only)

- **`alert_preferences`:** keyed by user, student and channel (`email` or `push`), with `inactivity_days` (1–60) and `enabled`. Users manage only their own rows, and only for students they can view.
- **`student_inactivity(days?)`:** lists students in the caller's households, among those the caller has `can_view_progress` for, whose last submitted attempt is older than the threshold, or who have never practised. The threshold is `days` if given, otherwise the caller's smallest enabled preference for that student.
- **No sending:** nothing is sent. A scheduled job or edge function should call this logic as each guardian, or replicate it with `service_role`, and deliver the alerts.

## AI-help hooks

`request_ai_help(attempt, mode)` accepts the modes `hint`, `concept`, `strategy`, `worked_example` and `answer_reveal`. It always inserts an `ai_help_requests` row.

- **Off (default):** while `app_settings` key `ai_help_enabled` is not the JSON value `true`, the request is stored with status `disabled` and the attempt is unchanged.
- **On:** the request is stored as `pending` and an `ai_help` event is logged. If the attempt is still open, `ai_help_used` is set.
- **`answer_reveal`:** rejected until the attempt is submitted.
- **Provider:** a future worker, running as `service_role`, will fill in `response`, `provider`, `model` and `tokens` and set the status to `completed` or `failed`. The student and guardians with `can_view_progress` can read requests.

## Test scores and the merit-aid connection

- **`student_test_scores`:** student, exam version, test date, composite, `section_scores` jsonb, and `score_source` (`official`, `self_reported` or `practice_estimate`).
- **Who writes scores:** clients may insert only `self_reported` scores. Official scores and practice estimates are written by `service_role`.
- **`student_official_scores`:** a view, with `security_invoker`, that exposes only `official` rows. Anything comparing a student with award thresholds must use it, or treat `self_reported` as explicitly unverified. A `practice_estimate` must never be presented as an official score.
- **No eligibility claims:** nothing in this migration states or computes merit eligibility. A later recommendation-engine change can join official or labeled self-reported scores to verified `institutional_awards` thresholds.

## Not done yet

- No UI, client SDK or question content. The exam rules in tests are synthetic fixtures, not official specifications.
- No payment provider, webhook handler or plan catalogue.
- No AI provider, worker, rate limits or instructional-quality evaluation.
- No notification sending, email reports or scheduler.
- No recommender diversification or difficulty adaptation (v1 heuristic only), no item calibration, and no score prediction.
- No deletion or export path for a student's data. Deleting a minor's practice data needs a confirmed, audited path and is a product decision.
- No join request initiated by the student, and no recovery for a household with no remaining manager after account deletion.
- Live since 2026-10-02 (`20261002183112_household_practice_progress`, recorded in `supabase/migration_history.json`). Supabase's security advisor lists the client-callable `SECURITY DEFINER` RPCs as warnings; that is the intended design. The six access helpers (`has_household_permission`, `is_household_*`, `can_*_student`) do not need to be RPC endpoints and are tracked for a move to a non-exposed schema.
