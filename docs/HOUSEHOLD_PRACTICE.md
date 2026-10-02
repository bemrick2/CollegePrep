# Households, students and practice progress

Migration `20261002183112_household_practice_progress` adds the first user-data schema. It covers families, student profiles, practice questions, server-graded attempts and weekly goals. The migration needs Supabase Auth (`auth.users`, `auth.uid()`). CI supplies a minimal stand-in in `supabase/tests/support/auth_stub.sql`, which does nothing on a real Supabase project. Tests are in `supabase/tests/household_practice.sql` and `tests/test_household_schema.py`.

## Model

- **profiles**: one row per auth user (display name only).
- **households**: a family. **household_members** links auth users to a household as `guardian` or `student`.
- **students**: a student profile inside a household. A profile can exist with no login (`guardian_managed`). When the student accepts an invitation, `linked_user_id` is set and `account_mode` becomes `student_login`. A login links to at most one student, and a student to at most one login. `archived_at` hides a student from new practice without deleting history.
- **household_invitations**: single-use codes with an expiry. Only the SHA-256 hex digest is stored. A student invitation names the student profile it will link.
- **question_strategies**: named techniques such as `process_of_elimination`, `backsolve`, `plug_in_numbers` and `annotate_passage`. **practice_question_strategies** tags questions with them.
- **practice_questions**: content. It may reference `practice_blueprints`. Status is `draft`, `published` or `retired`. The migration seeds no rows, because strategies and questions are content, not schema.
- **weekly_practice_goals**: per student and ISO week (the week starts on Monday). Each goal has a question target, a minute target or both, and an optional subject. A null subject is the overall weekly goal.
- **practice_sessions** and **practice_attempts**: practice events. All writes go through RPCs.

## Access matrix

| Table | Guardian of household | Linked student | Other authenticated | anon |
|---|---|---|---|---|
| profiles | own row only | own row only | own row only (read, insert, update display_name) | none |
| households | read | read | none | none |
| household_members | read all in household | read own row | none | none |
| students | read; update name, years, archive | read own profile | none | none |
| household_invitations | read (no `code_hash`) | none | none | none |
| question_strategies | read | read | read | none |
| practice_questions | read published, safe columns | same | same | none |
| practice_question_strategies | read for published questions | same | same | none |
| weekly_practice_goals | read, insert, update, delete | read | none | none |
| practice_sessions, practice_attempts | read | read own | none | none |

No client role can insert, update or delete attempts or sessions directly. Households, memberships, students and invitations are created only through RPCs. `service_role` has full table access.

Authenticated users get column-level `SELECT` on `practice_questions` that excludes `correct_answer`, `explanation` and `distractor_rationales`. A client must therefore list columns explicitly, because `select *` is denied.

The helper functions `is_household_guardian`, `is_household_member`, `can_view_student` and `can_manage_student` are `security definer`. RLS policies use them so that policies never query `household_members` recursively under RLS.

## RPCs

All RPCs are `security definer` with `search_path = ''`. They are executable by `authenticated` only. A denial raises SQLSTATE `42501`; invalid input raises `22023`.

| Function | Who | Effect |
|---|---|---|
| `create_household(name)` | any signed-in user | Creates the household and adds the caller as its guardian. |
| `add_student(household, display_name, graduation_year?, grade_level?)` | guardian | Adds a guardian-managed student. |
| `create_household_invitation(household, role, student?, ttl_hours=72)` | guardian | Returns the plaintext code once. TTL is 1–336 hours. Student invitations need an active, unlinked student. |
| `accept_household_invitation(code)` | signed-in user | Validates the code, its expiry and that it is unused. Adds the membership; for a student invitation, also links the student. Marks the code used. |
| `start_practice_session(student, goal?)` / `end_practice_session(session)` | linked student | Optional grouping of attempts. |
| `start_practice_attempt(student, question, session?)` | linked student | The question must be published. Sets `presented_at` to server time and assigns the next `attempt_number`. |
| `submit_practice_attempt(attempt, answer, active_ms?, first_interaction_ms?, hint_count=0, ai_help_used=false, strategy_key?)` | the attempt's student | Can be called once per attempt. Grades the answer on the server and returns `is_correct`, `correct_answer`, `explanation` and `elapsed_ms`. |
| `student_weekly_progress(student, week_start)` | guardian or linked student | Returns a JSON summary of the week (see below). |

## Timing semantics

- **Server time:**
  - `presented_at` is set by `start_practice_attempt`.
  - `submitted_at` is set by `submit_practice_attempt`.
  - `elapsed_ms` is `submitted_at - presented_at`.
  - `is_correct` is computed on the server: whitespace is trimmed and the match is exact, case-sensitive.

  These fields are trustworthy.
- **Client-reported:**
  - `active_ms` is focused time.
  - `first_interaction_ms` is the time to first interaction.
  - `hint_count` and `ai_help_used` record help taken.

  A negative value is rejected, and so is a time longer than the server elapsed time. Nothing is clamped silently.
- **Week boundary:** a week is `[week_start, week_start + 7 days)` in **UTC**, measured on `submitted_at`. `questions_attempted` counts `presented_at` in the same window. An attempt shown on Sunday night and submitted after 00:00 UTC Monday counts toward the next week.

`student_weekly_progress` returns these fields:

- `student_id`, `week_start`
- `goal`: the overall goal's `target_questions` and `target_minutes`, or null
- `questions_attempted`, `questions_submitted`, `correct`
- `accuracy`: null when nothing was submitted
- `total_elapsed_ms`
- `total_active_ms`: null when no client timing was reported
- `median_elapsed_ms`
- `ai_help_attempts`, `hints_used`
- `goal_progress`: `questions_pct` against submitted questions and `minutes_pct` against total elapsed time. Each is null without its target, and the whole object is null without a goal.
- `by_skill`: a list of `{subject, skill, submitted, correct, median_elapsed_ms}`
- `by_strategy`: a list of `{strategy_key, submitted, correct}`

## Deliberate decisions

- **No date of birth is stored.** The schema keeps only the graduation year and grade level.
- **Goals:** guardians set them and students can read them but not change them.
- **No practising as the student:** a guardian cannot start or submit attempts for the student. A guardian-managed student with no login therefore cannot practise until linked.
- **Answers stay hidden until submission:** `correct_answer`, `explanation` and `distractor_rationales` are revealed only in the submit response.
- **Invitation codes:** each code is a 64-character hex string built from two `gen_random_uuid()` values, giving 244 random bits. It is hashed with core `sha256()`, so pgcrypto schema placement does not matter.
- **Week boundaries use UTC.** Per-household time zones are not modelled yet.

## Not done yet

- No UI and no client SDK wrappers.
- No AI-help provider. `ai_help_used` is only recorded.
- No notifications or email reports.
- No question content or strategy catalogue.
- No per-subject goal progress in the RPC; only the overall goal is reported.
- **Not yet applied to the live Supabase project.** For the same reason, this migration is not in `supabase/migration_history.json`. Follow `docs/MIGRATIONS.md` when it is applied.
