-- Households with permissioned guardians, student accounts (guardian-created, self-created, independent),
-- subscriptions, an exam-version-aware question bank, server-graded attempts with an event log,
-- recommendations, skill estimates, adaptive goals, streaks, inactivity alerts, AI-help hooks and test scores.
-- Requires auth.users and auth.uid() (Supabase; CI uses supabase/tests/support/auth_stub.sql).
-- Clients never write integrity-critical rows directly: those go through security definer RPCs.
-- See docs/HOUSEHOLD_PRACTICE.md.

-- Pure helpers used by constraints and grading.
create function public.is_valid_time_zone(p_tz text) returns boolean
language sql stable set search_path = '' as $$
  select p_tz is not null and exists (select 1 from pg_catalog.pg_timezone_names where name = p_tz)
$$;

-- Parses '3', '-2.5', '.5' and '1/2' style numeric answers; anything else is null.
create function public.parse_numeric_answer(p text) returns numeric
language plpgsql immutable set search_path = '' as $$
declare v text := replace(btrim(coalesce(p, '')), ' ', ''); parts text[];
begin
  if v ~ '^-?[0-9]+/[0-9]+$' then
    parts := string_to_array(v, '/');
    if parts[2]::numeric = 0 then return null; end if;
    return parts[1]::numeric / parts[2]::numeric;
  elsif v ~ '^-?([0-9]+\.?[0-9]*|\.[0-9]+)$' then
    return v::numeric;
  end if;
  return null;
end $$;

create function public.numeric_answers_valid(p_answers jsonb) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(bool_and(jsonb_typeof(e) = 'string' and public.parse_numeric_answer(e #>> '{}') is not null), false)
  from jsonb_array_elements(p_answers) e
$$;

-- choice: exact match after trimming. numeric: numeric equality ('1/2' = '.5' = '0.5').
-- text: case-insensitive match after trimming.
create function public.grade_answer(p_format text, p_accepted jsonb, p_given text) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(bool_or(case p_format
    when 'choice' then btrim(e #>> '{}') = btrim(p_given)
    when 'numeric' then public.parse_numeric_answer(e #>> '{}') = public.parse_numeric_answer(p_given)
    when 'text' then lower(btrim(e #>> '{}')) = lower(btrim(p_given)) end), false)
  from jsonb_array_elements(p_accepted) e
$$;

create function public.local_week_bounds(p_week_start date, p_tz text) returns tstzrange
language sql stable set search_path = '' as $$
  select tstzrange(p_week_start::timestamp at time zone p_tz, (p_week_start + 7)::timestamp at time zone p_tz, '[)')
$$;

-- Accounts
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text check (length(display_name) between 1 and 120),
  created_at timestamptz not null default now()
);

create table public.households (
  id uuid primary key default gen_random_uuid(),
  name text not null check (length(btrim(name)) between 1 and 120),
  -- Nullable so deleting the creator's account never blocks or deletes the household.
  created_by uuid references auth.users(id) on delete set null,
  time_zone text not null default 'UTC' check (public.is_valid_time_zone(time_zone)),
  created_at timestamptz not null default now()
);

create table public.household_members (
  household_id uuid not null references public.households(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('guardian','student')),
  can_manage_students boolean not null default false,
  can_set_goals boolean not null default false,
  can_view_progress boolean not null default false,
  can_manage_members boolean not null default false,
  can_manage_billing boolean not null default false,
  created_at timestamptz not null default now(),
  primary key (household_id, user_id),
  check (role = 'guardian' or not (can_manage_students or can_set_goals or can_view_progress or can_manage_members or can_manage_billing))
);
create index household_members_user_idx on public.household_members(user_id);

-- No date of birth is stored, by design. household_id is null for a self-created profile outside a household.
-- Deleting a household detaches its students rather than deleting their practice history.
create table public.students (
  id uuid primary key default gen_random_uuid(),
  household_id uuid references public.households(id) on delete set null,
  display_name text not null check (length(btrim(display_name)) between 1 and 120),
  graduation_year integer check (graduation_year between 2000 and 2100),
  grade_level integer check (grade_level between 0 and 13),
  account_mode text not null default 'guardian_managed' check (account_mode in ('guardian_managed','student_login')),
  is_independent boolean not null default false,
  linked_user_id uuid unique references auth.users(id) on delete set null,
  time_zone text check (time_zone is null or public.is_valid_time_zone(time_zone)),
  created_at timestamptz not null default now(),
  archived_at timestamptz
);
create index students_household_idx on public.students(household_id);

create table public.household_invitations (
  id uuid primary key default gen_random_uuid(),
  household_id uuid not null references public.households(id) on delete cascade,
  role text not null check (role in ('guardian','student')),
  -- A student invitation either claims this guardian-created profile or, when null, brings the student's own profile.
  student_id uuid references public.students(id) on delete cascade,
  permissions text[] not null default '{}'
    check (permissions <@ array['manage_students','set_goals','view_progress','manage_members','manage_billing']),
  code_hash text not null unique check (code_hash ~ '^[0-9a-f]{64}$'),
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null,
  accepted_by uuid references auth.users(id) on delete set null,
  accepted_at timestamptz,
  check (role = 'student' or student_id is null),
  check (role = 'guardian' or permissions = '{}')
);
create index household_invitations_household_idx on public.household_invitations(household_id);

-- Written only by service_role (payment-provider webhooks). No payments are implemented here.
create table public.subscriptions (
  id uuid primary key default gen_random_uuid(),
  owner_user_id uuid not null references auth.users(id) on delete cascade,
  household_id uuid references public.households(id) on delete set null,
  plan_key text not null,
  status text not null check (status in ('trialing','active','past_due','canceled','incomplete')),
  provider text,
  provider_customer_id text,
  provider_subscription_id text unique,
  current_period_end timestamptz,
  created_at timestamptz not null default now()
);
create index subscriptions_household_idx on public.subscriptions(household_id);

create table public.app_settings (
  key text primary key,
  value jsonb not null,
  updated_at timestamptz not null default now()
);

-- Exam structure. Rules (sections, timing, counts, scoring scale, calculator policy) are data, not code.
create table public.exam_families (
  key text primary key check (key ~ '^[a-z][a-z0-9_]*$'),
  name text not null
);

create table public.exam_versions (
  id uuid primary key default gen_random_uuid(),
  exam_family text not null references public.exam_families(key),
  version_key text not null unique check (version_key ~ '^[a-z][a-z0-9_]*$'),
  name text not null,
  effective_from date not null,
  effective_to date check (effective_to > effective_from),
  rules jsonb not null default '{}' check (jsonb_typeof(rules) = 'object'),
  created_at timestamptz not null default now()
);

create table public.question_types (
  id uuid primary key default gen_random_uuid(),
  exam_version_id uuid not null references public.exam_versions(id) on delete cascade,
  type_key text not null check (type_key ~ '^[a-z][a-z0-9_]*$'),
  name text not null,
  unique (exam_version_id, type_key),
  unique (id, exam_version_id)
);

create table public.skills (
  id uuid primary key default gen_random_uuid(),
  parent_id uuid,
  exam_family text not null references public.exam_families(key),
  section text not null,
  domain text,
  skill_key text not null check (skill_key ~ '^[a-z][a-z0-9_]*$'),
  name text not null,
  unique (exam_family, skill_key),
  unique (id, exam_family),
  foreign key (parent_id, exam_family) references public.skills(id, exam_family)
);

create table public.trap_types (
  id uuid primary key default gen_random_uuid(),
  trap_key text not null unique check (trap_key ~ '^[a-z][a-z0-9_]*$'),
  name text not null,
  description text
);

create table public.question_strategies (
  id uuid primary key default gen_random_uuid(),
  strategy_key text not null unique check (strategy_key ~ '^[a-z][a-z0-9_]*$'),
  name text not null,
  description text,
  exam_family text references public.exam_families(key),
  subject text,
  created_at timestamptz not null default now()
);

create table public.practice_questions (
  id uuid primary key default gen_random_uuid(),
  exam_version_id uuid not null references public.exam_versions(id),
  question_type_id uuid not null,
  blueprint_id uuid references public.practice_blueprints(id),
  section text not null,
  difficulty smallint check (difficulty between 1 and 5),
  difficulty_calibrated double precision,
  difficulty_label text check (difficulty_label in ('easy','medium','hard')),
  stem text not null,
  choices jsonb not null default '[]' check (jsonb_typeof(choices) = 'array'),
  answer_format text not null check (answer_format in ('choice','numeric','text')),
  -- Hidden from clients until submission: accepted_answers, hints, teaching_explanation, strategy_explanation.
  accepted_answers jsonb not null check (jsonb_typeof(accepted_answers) = 'array' and jsonb_array_length(accepted_answers) > 0),
  hints jsonb not null default '[]' check (jsonb_typeof(hints) = 'array'),
  teaching_explanation text,
  strategy_explanation text,
  expected_time_seconds integer check (expected_time_seconds > 0),
  source_attribution text,
  license text,
  status text not null default 'draft' check (status in ('draft','published','retired')),
  created_at timestamptz not null default now(),
  foreign key (question_type_id, exam_version_id) references public.question_types(id, exam_version_id),
  check (answer_format <> 'numeric' or public.numeric_answers_valid(accepted_answers))
);

create table public.practice_question_skills (
  question_id uuid not null references public.practice_questions(id) on delete cascade,
  skill_id uuid not null references public.skills(id),
  is_primary boolean not null default false,
  primary key (question_id, skill_id)
);
create unique index practice_question_skills_primary_idx on public.practice_question_skills(question_id) where is_primary;

-- Why each wrong choice is wrong and which trap it sets. Never granted to clients; revealed on submit.
create table public.practice_question_distractors (
  question_id uuid not null references public.practice_questions(id) on delete cascade,
  choice_key text not null,
  rationale text not null,
  trap_type_id uuid references public.trap_types(id),
  primary key (question_id, choice_key)
);

create table public.practice_question_strategies (
  question_id uuid not null references public.practice_questions(id) on delete cascade,
  strategy_id uuid not null references public.question_strategies(id),
  role text not null default 'primary' check (role in ('primary','secondary')),
  is_fastest boolean not null default false,
  strategy_explanation text,
  notes text,
  primary key (question_id, strategy_id)
);

-- Goals, sessions, attempts
create table public.weekly_practice_goals (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  week_start date not null check (extract(isodow from week_start) = 1),
  target_questions integer check (target_questions > 0),
  target_minutes integer check (target_minutes > 0),
  subject text,
  goal_mode text not null default 'fixed' check (goal_mode in ('fixed','adaptive')),
  set_by uuid default auth.uid() references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check (target_questions is not null or target_minutes is not null)
);
create unique index weekly_practice_goals_unique_idx
  on public.weekly_practice_goals(student_id, week_start, coalesce(subject, ''));

create table public.practice_sessions (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  target_minutes integer not null default 10 check (target_minutes between 5 and 15),
  started_at timestamptz not null default now(),
  ended_at timestamptz,
  goal_id uuid references public.weekly_practice_goals(id) on delete set null
);
create index practice_sessions_student_idx on public.practice_sessions(student_id);

create table public.practice_session_items (
  session_id uuid not null references public.practice_sessions(id) on delete cascade,
  position integer not null check (position > 0),
  question_id uuid not null references public.practice_questions(id),
  reason text not null,
  primary key (session_id, position),
  unique (session_id, question_id)
);

create table public.practice_attempts (
  id uuid primary key default gen_random_uuid(),
  session_id uuid references public.practice_sessions(id) on delete set null,
  student_id uuid not null references public.students(id) on delete cascade,
  question_id uuid not null references public.practice_questions(id),
  presented_at timestamptz not null default now(),
  first_interaction_ms integer check (first_interaction_ms >= 0),
  submitted_at timestamptz,
  elapsed_ms integer check (elapsed_ms >= 0),
  active_ms integer check (active_ms >= 0),
  selected_answer text,
  is_correct boolean,
  skipped boolean not null default false,
  confidence smallint check (confidence between 1 and 3),
  hint_count integer not null default 0 check (hint_count >= 0),
  ai_help_used boolean not null default false,
  strategy_used_id uuid references public.question_strategies(id),
  attempt_number integer not null default 1 check (attempt_number > 0),
  unique (student_id, question_id, attempt_number),
  check (not skipped or (is_correct is null and selected_answer is null))
);
create index practice_attempts_student_submitted_idx on public.practice_attempts(student_id, submitted_at);

-- Append-only, server-timestamped log written only by RPCs.
create table public.practice_attempt_events (
  id bigint generated always as identity primary key,
  attempt_id uuid not null references public.practice_attempts(id) on delete cascade,
  student_id uuid not null references public.students(id) on delete cascade,
  kind text not null check (kind in ('presented','answered','changed_answer','skipped','returned','hint','ai_help','submitted')),
  occurred_at timestamptz not null default now(),
  answer text,
  detail jsonb
);
create index practice_attempt_events_attempt_idx on public.practice_attempt_events(attempt_id, id);
create index practice_attempt_events_student_idx on public.practice_attempt_events(student_id, occurred_at);

create table public.ai_help_requests (
  id uuid primary key default gen_random_uuid(),
  attempt_id uuid not null references public.practice_attempts(id) on delete cascade,
  student_id uuid not null references public.students(id) on delete cascade,
  requested_by uuid references auth.users(id) on delete set null,
  requested_at timestamptz not null default now(),
  mode text not null check (mode in ('hint','concept','strategy','worked_example','answer_reveal')),
  status text not null check (status in ('pending','completed','failed','disabled')),
  response jsonb,
  provider text,
  model text,
  tokens integer check (tokens >= 0)
);
create index ai_help_requests_student_idx on public.ai_help_requests(student_id);

create table public.alert_preferences (
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  student_id uuid not null references public.students(id) on delete cascade,
  channel text not null check (channel in ('email','push')),
  inactivity_days integer not null default 3 check (inactivity_days between 1 and 60),
  enabled boolean not null default true,
  created_at timestamptz not null default now(),
  primary key (user_id, student_id, channel)
);

-- Scores are hooks for comparing with verified award thresholds later; nothing here asserts eligibility.
create table public.student_test_scores (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  exam_version_id uuid not null references public.exam_versions(id),
  test_date date not null,
  composite integer check (composite >= 0),
  section_scores jsonb not null default '{}' check (jsonb_typeof(section_scores) = 'object'),
  score_source text not null check (score_source in ('official','self_reported','practice_estimate')),
  entered_by uuid default auth.uid() references auth.users(id) on delete set null,
  created_at timestamptz not null default now()
);
create index student_test_scores_student_idx on public.student_test_scores(student_id);

create view public.student_official_scores with (security_invoker = true) as
select id, student_id, exam_version_id, test_date, composite, section_scores
from public.student_test_scores where score_source = 'official';

create function public.set_weekly_goal_audit() returns trigger
language plpgsql set search_path = '' as $$
begin
  new.updated_at := now();
  new.set_by := coalesce(auth.uid(), old.set_by);
  return new;
end $$;
create trigger weekly_practice_goals_audit before update on public.weekly_practice_goals
  for each row execute function public.set_weekly_goal_audit();

-- Access helpers. Security definer so policies can consult household_members without recursive RLS.
create function public.is_household_member(p_household uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.household_members m where m.household_id = p_household and m.user_id = auth.uid())
$$;

create function public.is_household_guardian(p_household uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.household_members m
    where m.household_id = p_household and m.user_id = auth.uid() and m.role = 'guardian')
$$;

-- p_permission: manage_students | set_goals | view_progress | manage_members | manage_billing.
create function public.has_household_permission(p_household uuid, p_permission text) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.household_members m
    where m.household_id = p_household and m.user_id = auth.uid() and m.role = 'guardian'
      and case p_permission when 'manage_students' then m.can_manage_students when 'set_goals' then m.can_set_goals
        when 'view_progress' then m.can_view_progress when 'manage_members' then m.can_manage_members
        when 'manage_billing' then m.can_manage_billing else false end)
$$;

-- The linked student always sees their own data; guardians need can_view_progress in the student's current household.
create function public.can_view_student(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s where s.id = p_student
    and (s.linked_user_id = auth.uid() or public.has_household_permission(s.household_id, 'view_progress')))
$$;

create function public.can_manage_student(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s where s.id = p_student
    and public.has_household_permission(s.household_id, 'manage_students'))
$$;

-- Guardians with can_set_goals; the student themself when independent or outside any household.
create function public.can_set_student_goals(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s where s.id = p_student
    and (public.has_household_permission(s.household_id, 'set_goals')
      or (s.linked_user_id = auth.uid() and (s.is_independent or s.household_id is null))))
$$;

-- Internal (not client-callable) helpers.
create function public.student_time_zone(p_student uuid) returns text
language sql stable set search_path = '' as $$
  select coalesce(s.time_zone, h.time_zone, 'UTC') from public.students s
  left join public.households h on h.id = s.household_id where s.id = p_student
$$;

create function public.require_linked_student(p_student uuid) returns void
language plpgsql set search_path = '' as $$
begin
  perform 1 from public.students s where s.id = p_student and s.linked_user_id = auth.uid() and s.archived_at is null;
  if not found then raise exception 'Only the student''s own login can practise' using errcode = '42501'; end if;
end $$;

create function public.require_manager_remains(p_household uuid) returns void
language plpgsql set search_path = '' as $$
begin
  if not exists (select 1 from public.household_members m where m.household_id = p_household and m.can_manage_members) then
    raise exception 'A household must keep at least one member who can manage members' using errcode = '42501';
  end if;
end $$;

-- A departing student user takes their profile and history out of the household.
create function public.detach_member(p_household uuid, p_user uuid) returns void
language plpgsql set search_path = '' as $$
declare v_role text;
begin
  delete from public.household_members m where m.household_id = p_household and m.user_id = p_user returning m.role into v_role;
  if v_role is null then raise exception 'Not a member of this household' using errcode = '22023'; end if;
  if v_role = 'student' then
    with moved as (update public.students s set household_id = null
      where s.household_id = p_household and s.linked_user_id = p_user returning s.id)
    delete from public.alert_preferences a using moved where a.student_id = moved.id and a.user_id <> p_user;
  else
    delete from public.alert_preferences a using public.students s
    where a.user_id = p_user and s.id = a.student_id and s.household_id = p_household;
  end if;
  perform public.require_manager_remains(p_household);
end $$;

-- Per primary skill, using each skill's 30 most recent answered attempts. Thresholds: docs/HOUSEHOLD_PRACTICE.md.
create function public.skill_estimates_internal(p_student uuid)
returns table (skill_id uuid, skill_key text, section text, attempts bigint, correct bigint, accuracy numeric,
  median_elapsed_ms bigint, pacing_ratio numeric, knowledge_weak boolean, pacing_weak boolean)
language sql stable set search_path = '' as $$
  with a as (
    select qs.skill_id, a.is_correct, a.elapsed_ms, q.expected_time_seconds,
      row_number() over (partition by qs.skill_id order by a.submitted_at desc, a.id) as rn
    from public.practice_attempts a
    join public.practice_questions q on q.id = a.question_id
    join public.practice_question_skills qs on qs.question_id = q.id and qs.is_primary
    where a.student_id = p_student and a.submitted_at is not null and not a.skipped
  ), agg as (
    select a.skill_id, count(*) as n, count(*) filter (where a.is_correct) as c,
      round(percentile_cont(0.5) within group (order by a.elapsed_ms))::bigint as med,
      round((percentile_cont(0.5) within group (order by a.elapsed_ms / (a.expected_time_seconds * 1000.0))
        filter (where a.expected_time_seconds is not null))::numeric, 3) as pace
    from a where a.rn <= 30 group by a.skill_id
  )
  select g.skill_id, k.skill_key, k.section, g.n, g.c, round(g.c::numeric / g.n, 4), g.med, g.pace,
    case when g.n >= 5 then g.c::numeric / g.n < 0.6 end,
    case when g.n >= 5 and g.pace is not null then g.c::numeric / g.n >= 0.6 and g.pace > 1.25 end
  from agg g join public.skills k on k.id = g.skill_id
$$;

-- v1 heuristic: weak-knowledge skills, then weak pacing, then unseen skills, then review;
-- within a bucket never-seen questions first, then least recently seen; greedy fill of the time budget.
create function public.recommend_internal(p_student uuid, p_target_minutes integer, p_exam_version uuid)
returns table (item_position integer, question_id uuid, skill_id uuid, expected_time_seconds integer, reason text)
language plpgsql stable set search_path = '' as $$
declare v_budget integer := p_target_minutes * 60; v_used integer := 0; r record;
begin
  item_position := 0;
  for r in
    with est as (select * from public.skill_estimates_internal(p_student)),
    seen as (select a.question_id as qid, max(a.presented_at) as last_seen
      from public.practice_attempts a where a.student_id = p_student group by a.question_id)
    select q.id, qs.skill_id as sid, q.expected_time_seconds as secs, s.last_seen,
      case when e.knowledge_weak then 'weak_knowledge' when e.pacing_weak then 'weak_pacing'
        when qs.skill_id is null then 'untagged' when e.skill_id is null then 'new_skill' else 'review' end as why,
      case when e.knowledge_weak then 0 when e.pacing_weak then 1
        when qs.skill_id is null then 4 when e.skill_id is null then 2 else 3 end as bucket
    from public.practice_questions q
    left join public.practice_question_skills qs on qs.question_id = q.id and qs.is_primary
    left join est e on e.skill_id = qs.skill_id
    left join seen s on s.qid = q.id
    where q.status = 'published' and q.expected_time_seconds is not null
      and (p_exam_version is null or q.exam_version_id = p_exam_version)
    order by bucket, s.last_seen nulls first, q.id
  loop
    exit when v_used >= v_budget;
    continue when v_used + r.secs > v_budget;
    v_used := v_used + r.secs;
    item_position := item_position + 1;
    question_id := r.id; skill_id := r.sid; expected_time_seconds := r.secs; reason := r.why;
    return next;
  end loop;
end $$;

create function public.streak_internal(p_student uuid, p_tz text, p_as_of date)
returns table (current_streak integer, longest_streak integer, last_practice_day date)
language sql stable set search_path = '' as $$
  with d as (
    select distinct (a.submitted_at at time zone p_tz)::date as day from public.practice_attempts a
    where a.student_id = p_student and a.submitted_at is not null and not a.skipped
      and (a.submitted_at at time zone p_tz)::date <= p_as_of
  ), runs as (
    select min(day) as first_day, max(day) as last_day, count(*)::integer as n
    from (select day, day - (row_number() over (order by day))::integer as grp from d) g group by grp
  )
  select coalesce(max(n) filter (where last_day >= p_as_of - 1), 0), coalesce(max(n), 0), max(last_day) from runs
$$;

-- Account RPCs
create function public.create_household(p_name text, p_time_zone text default 'UTC') returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_uid uuid := auth.uid(); v_id uuid;
begin
  if v_uid is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  if not public.is_valid_time_zone(p_time_zone) then raise exception 'Unknown time zone %', p_time_zone using errcode = '22023'; end if;
  insert into public.households(name, created_by, time_zone) values (btrim(p_name), v_uid, p_time_zone) returning id into v_id;
  insert into public.household_members(household_id, user_id, role, can_manage_students, can_set_goals,
    can_view_progress, can_manage_members, can_manage_billing) values (v_id, v_uid, 'guardian', true, true, true, true, true);
  return v_id;
end $$;

create function public.add_student(p_household uuid, p_display_name text,
  p_graduation_year integer default null, p_grade_level integer default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  if not public.has_household_permission(p_household, 'manage_students') then
    raise exception 'Adding students requires the manage-students permission' using errcode = '42501';
  end if;
  insert into public.students(household_id, display_name, graduation_year, grade_level)
  values (p_household, btrim(p_display_name), p_graduation_year, p_grade_level) returning id into v_id;
  return v_id;
end $$;

create function public.create_self_student_profile(p_display_name text, p_graduation_year integer default null,
  p_grade_level integer default null, p_independent boolean default false, p_time_zone text default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_uid uuid := auth.uid(); v_id uuid;
begin
  if v_uid is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  if exists (select 1 from public.students s where s.linked_user_id = v_uid) then
    raise exception 'Your account is already linked to a student profile' using errcode = '22023';
  end if;
  if p_time_zone is not null and not public.is_valid_time_zone(p_time_zone) then
    raise exception 'Unknown time zone %', p_time_zone using errcode = '22023';
  end if;
  insert into public.students(household_id, display_name, graduation_year, grade_level, account_mode,
    is_independent, linked_user_id, time_zone)
  values (null, btrim(p_display_name), p_graduation_year, p_grade_level, 'student_login',
    coalesce(p_independent, false), v_uid, p_time_zone) returning id into v_id;
  return v_id;
end $$;

create function public.create_household_invitation(p_household uuid, p_role text, p_student uuid default null,
  p_ttl_hours integer default 72, p_permissions text[] default null) returns text
language plpgsql security definer set search_path = '' as $$
declare v_code text; v_perms text[];
begin
  if p_role is null or p_role not in ('guardian','student') then
    raise exception 'Invitation role must be guardian or student' using errcode = '22023';
  end if;
  if not public.has_household_permission(p_household, case p_role when 'guardian' then 'manage_members' else 'manage_students' end) then
    raise exception 'Not allowed to invite % members to this household', p_role using errcode = '42501';
  end if;
  if p_ttl_hours is null or p_ttl_hours not between 1 and 336 then
    raise exception 'Invitation lifetime must be between 1 and 336 hours' using errcode = '22023';
  end if;
  if p_role = 'guardian' then
    if p_student is not null then raise exception 'Guardian invitations cannot name a student' using errcode = '22023'; end if;
    v_perms := coalesce(p_permissions, array['manage_students','set_goals','view_progress']);
    if not v_perms <@ array['manage_students','set_goals','view_progress','manage_members','manage_billing'] then
      raise exception 'Unknown permission in %', v_perms using errcode = '22023';
    end if;
  else
    if p_permissions is not null and p_permissions <> '{}' then
      raise exception 'Student invitations carry no permissions' using errcode = '22023';
    end if;
    v_perms := '{}';
    -- Only an unlinked, guardian-created profile can be targeted; self-created and independent profiles never can.
    if p_student is not null and not exists (select 1 from public.students s where s.id = p_student
        and s.household_id = p_household and s.archived_at is null and s.linked_user_id is null) then
      raise exception 'Student invitations can only target an active, unlinked student of this household' using errcode = '22023';
    end if;
  end if;
  -- 244 random bits from two v4 UUIDs; only the SHA-256 digest is stored.
  v_code := replace(gen_random_uuid()::text || gen_random_uuid()::text, '-', '');
  insert into public.household_invitations(household_id, role, student_id, permissions, code_hash, created_by, expires_at)
  values (p_household, p_role, p_student, v_perms, encode(sha256(convert_to(v_code, 'UTF8')), 'hex'),
          auth.uid(), now() + make_interval(hours => p_ttl_hours));
  return v_code;
end $$;

-- The only way a student profile enters a household; always called by the student, so it is their consent.
create function public.accept_household_invitation(p_code text) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_uid uuid := auth.uid(); v_inv public.household_invitations; v_student public.students; v_own public.students;
begin
  if v_uid is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  select * into v_inv from public.household_invitations i
  where i.code_hash = encode(sha256(convert_to(lower(btrim(coalesce(p_code, ''))), 'UTF8')), 'hex')
  for update;
  if not found then raise exception 'Invalid invitation code' using errcode = '22023'; end if;
  if v_inv.accepted_at is not null then raise exception 'Invitation has already been used' using errcode = '22023'; end if;
  if v_inv.expires_at <= now() then raise exception 'Invitation has expired' using errcode = '22023'; end if;
  if exists (select 1 from public.household_members m where m.household_id = v_inv.household_id and m.user_id = v_uid) then
    raise exception 'You are already a member of this household' using errcode = '22023';
  end if;
  select * into v_own from public.students s where s.linked_user_id = v_uid for update;
  if v_inv.role = 'student' and v_inv.student_id is not null then
    select * into v_student from public.students s where s.id = v_inv.student_id for update;
    if v_student.archived_at is not null then raise exception 'This student profile is archived' using errcode = '22023'; end if;
    if v_student.linked_user_id is not null then
      raise exception 'This student profile is already linked to another account' using errcode = '22023';
    end if;
    if v_own.id is not null then
      raise exception 'Your account is already linked to another student profile' using errcode = '22023';
    end if;
    update public.students set linked_user_id = v_uid, account_mode = 'student_login' where id = v_student.id;
  elsif v_inv.role = 'student' then
    if v_own.id is null then raise exception 'Create your student profile before joining a household' using errcode = '22023'; end if;
    if v_own.household_id is not null then raise exception 'Leave your current household first' using errcode = '22023'; end if;
    if v_own.archived_at is not null then raise exception 'This student profile is archived' using errcode = '22023'; end if;
    update public.students set household_id = v_inv.household_id where id = v_own.id;
  end if;
  insert into public.household_members(household_id, user_id, role, can_manage_students, can_set_goals,
    can_view_progress, can_manage_members, can_manage_billing)
  values (v_inv.household_id, v_uid, v_inv.role, 'manage_students' = any(v_inv.permissions), 'set_goals' = any(v_inv.permissions),
    'view_progress' = any(v_inv.permissions), 'manage_members' = any(v_inv.permissions), 'manage_billing' = any(v_inv.permissions));
  update public.household_invitations set accepted_by = v_uid, accepted_at = now() where id = v_inv.id;
  return v_inv.household_id;
end $$;

-- Null arguments leave a flag unchanged.
create function public.update_member_permissions(p_household uuid, p_user uuid,
  p_manage_students boolean default null, p_set_goals boolean default null, p_view_progress boolean default null,
  p_manage_members boolean default null, p_manage_billing boolean default null) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.has_household_permission(p_household, 'manage_members') then
    raise exception 'Changing permissions requires the manage-members permission' using errcode = '42501';
  end if;
  update public.household_members m set
    can_manage_students = coalesce(p_manage_students, m.can_manage_students),
    can_set_goals = coalesce(p_set_goals, m.can_set_goals),
    can_view_progress = coalesce(p_view_progress, m.can_view_progress),
    can_manage_members = coalesce(p_manage_members, m.can_manage_members),
    can_manage_billing = coalesce(p_manage_billing, m.can_manage_billing)
  where m.household_id = p_household and m.user_id = p_user and m.role = 'guardian';
  if not found then raise exception 'No guardian with that id in this household' using errcode = '22023'; end if;
  perform public.require_manager_remains(p_household);
end $$;

create function public.remove_household_member(p_household uuid, p_user uuid) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.has_household_permission(p_household, 'manage_members') then
    raise exception 'Removing members requires the manage-members permission' using errcode = '42501';
  end if;
  perform public.detach_member(p_household, p_user);
end $$;

create function public.leave_household(p_household uuid) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if auth.uid() is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  perform public.detach_member(p_household, auth.uid());
end $$;

create function public.household_entitlements(p_household uuid)
returns table (plan_key text, status text, current_period_end timestamptz)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  return query select s.plan_key, s.status, s.current_period_end from public.subscriptions s
    where s.household_id = p_household order by s.current_period_end desc nulls last, s.created_at desc;
end $$;

-- Practice RPCs. Only the student's own login practises; guardians cannot act as the student.
create function public.recommend_practice_set(p_student uuid, p_target_minutes integer default 10, p_exam_version uuid default null)
returns table (item_position integer, question_id uuid, skill_id uuid, expected_time_seconds integer, reason text)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  if p_target_minutes is null or p_target_minutes not between 5 and 15 then
    raise exception 'Sessions are 5 to 15 minutes' using errcode = '22023';
  end if;
  return query select * from public.recommend_internal(p_student, p_target_minutes, p_exam_version);
end $$;

create function public.start_practice_session(p_student uuid, p_target_minutes integer default 10,
  p_goal uuid default null, p_exam_version uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  perform public.require_linked_student(p_student);
  if p_target_minutes is null or p_target_minutes not between 5 and 15 then
    raise exception 'Sessions are 5 to 15 minutes' using errcode = '22023';
  end if;
  if p_goal is not null and not exists (select 1 from public.weekly_practice_goals g where g.id = p_goal and g.student_id = p_student) then
    raise exception 'Goal does not belong to this student' using errcode = '22023';
  end if;
  insert into public.practice_sessions(student_id, target_minutes, goal_id) values (p_student, p_target_minutes, p_goal)
  returning id into v_id;
  insert into public.practice_session_items(session_id, position, question_id, reason)
  select v_id, r.item_position, r.question_id, r.reason from public.recommend_internal(p_student, p_target_minutes, p_exam_version) r;
  return v_id;
end $$;

create function public.end_practice_session(p_session uuid) returns void
language plpgsql security definer set search_path = '' as $$
begin
  update public.practice_sessions ps set ended_at = now()
  from public.students s
  where ps.id = p_session and s.id = ps.student_id and s.linked_user_id = auth.uid() and ps.ended_at is null;
  if not found then raise exception 'No open session of yours with that id' using errcode = '42501'; end if;
end $$;

create function public.start_practice_attempt(p_student uuid, p_question uuid, p_session uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  -- Locking the student row serialises attempt numbering.
  perform 1 from public.students s where s.id = p_student and s.linked_user_id = auth.uid() and s.archived_at is null for update;
  if not found then raise exception 'Only the student''s own login can practise' using errcode = '42501'; end if;
  if not exists (select 1 from public.practice_questions q where q.id = p_question and q.status = 'published') then
    raise exception 'Question is not available' using errcode = '22023';
  end if;
  if p_session is not null and not exists (select 1 from public.practice_sessions ps
      where ps.id = p_session and ps.student_id = p_student and ps.ended_at is null) then
    raise exception 'Session is not an open session of this student' using errcode = '22023';
  end if;
  insert into public.practice_attempts(session_id, student_id, question_id, presented_at, attempt_number)
  select p_session, p_student, p_question, now(), count(*) + 1
  from public.practice_attempts a where a.student_id = p_student and a.question_id = p_question
  returning id into v_id;
  insert into public.practice_attempt_events(attempt_id, student_id, kind) values (v_id, p_student, 'presented');
  return v_id;
end $$;

-- Locks an open attempt owned by the caller.
create function public.open_attempt_for_caller(p_attempt uuid) returns public.practice_attempts
language plpgsql set search_path = '' as $$
declare v public.practice_attempts;
begin
  select a.* into v from public.practice_attempts a join public.students s on s.id = a.student_id
  where a.id = p_attempt and s.linked_user_id = auth.uid() for update of a;
  if not found then raise exception 'Only the student who started this attempt can change it' using errcode = '42501'; end if;
  if v.submitted_at is not null then raise exception 'Attempt was already submitted' using errcode = '22023'; end if;
  return v;
end $$;

-- p_kind: answered (logged as changed_answer when it differs from the last answer), skipped, returned.
create function public.record_attempt_event(p_attempt uuid, p_kind text, p_answer text default null) returns text
language plpgsql security definer set search_path = '' as $$
declare v public.practice_attempts; v_last text; v_kind text := p_kind;
begin
  v := public.open_attempt_for_caller(p_attempt);
  if p_kind = 'answered' then
    if nullif(btrim(p_answer), '') is null then raise exception 'An answer is required' using errcode = '22023'; end if;
    select e.answer into v_last from public.practice_attempt_events e
    where e.attempt_id = p_attempt and e.kind in ('answered','changed_answer') order by e.id desc limit 1;
    if v_last = btrim(p_answer) then return 'unchanged'; end if;
    if v_last is not null then v_kind := 'changed_answer'; end if;
  elsif p_kind in ('skipped','returned') then
    if p_answer is not null then raise exception 'No answer is recorded with %', p_kind using errcode = '22023'; end if;
  else
    raise exception 'Event kind must be answered, skipped or returned' using errcode = '22023';
  end if;
  insert into public.practice_attempt_events(attempt_id, student_id, kind, answer)
  values (p_attempt, v.student_id, v_kind, btrim(p_answer));
  return v_kind;
end $$;

create function public.request_hint(p_attempt uuid) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v public.practice_attempts; v_hints jsonb;
begin
  v := public.open_attempt_for_caller(p_attempt);
  select q.hints into v_hints from public.practice_questions q where q.id = v.question_id;
  if v.hint_count >= jsonb_array_length(v_hints) then raise exception 'No more hints for this question' using errcode = '22023'; end if;
  update public.practice_attempts set hint_count = hint_count + 1 where id = p_attempt;
  insert into public.practice_attempt_events(attempt_id, student_id, kind, detail)
  values (p_attempt, v.student_id, 'hint', jsonb_build_object('hint_number', v.hint_count + 1));
  return jsonb_build_object('hint_number', v.hint_count + 1, 'hint', v_hints -> v.hint_count,
    'remaining', jsonb_array_length(v_hints) - v.hint_count - 1);
end $$;

-- A final skip closes the attempt with is_correct null; skips never count toward accuracy.
create function public.submit_practice_attempt(p_attempt uuid, p_selected_answer text,
  p_active_ms integer default null, p_first_interaction_ms integer default null,
  p_confidence integer default null, p_strategy_key text default null, p_skipped boolean default false)
returns table (is_correct boolean, skipped boolean, elapsed_ms integer, accepted_answers jsonb,
  teaching_explanation text, strategy_explanation text, distractors jsonb, strategies jsonb)
language plpgsql security definer set search_path = '' as $$
#variable_conflict use_column
declare v public.practice_attempts; v_q public.practice_questions; v_strategy uuid; v_elapsed numeric;
  v_correct boolean; v_last text; v_answer text := nullif(btrim(p_selected_answer), '');
begin
  v := public.open_attempt_for_caller(p_attempt);
  if p_skipped is null then raise exception 'p_skipped must not be null' using errcode = '22023'; end if;
  if p_skipped and v_answer is not null then raise exception 'A skipped attempt has no answer' using errcode = '22023'; end if;
  if not p_skipped and v_answer is null then raise exception 'An answer is required' using errcode = '22023'; end if;
  if p_active_ms < 0 or p_first_interaction_ms < 0 then
    raise exception 'Client timing values must be non-negative' using errcode = '22023';
  end if;
  if p_confidence not between 1 and 3 then raise exception 'Confidence must be 1, 2 or 3' using errcode = '22023'; end if;
  v_elapsed := floor(extract(epoch from now() - v.presented_at) * 1000);
  if v_elapsed > 2147483647 then raise exception 'Attempt is too old to submit; start a new attempt' using errcode = '22023'; end if;
  if p_active_ms > v_elapsed or p_first_interaction_ms > v_elapsed then
    raise exception 'Client-reported time exceeds server elapsed time' using errcode = '22023';
  end if;
  if p_strategy_key is not null then
    select st.id into v_strategy from public.question_strategies st where st.strategy_key = p_strategy_key;
    if not found then raise exception 'Unknown strategy %', p_strategy_key using errcode = '22023'; end if;
  end if;
  select q.* into v_q from public.practice_questions q where q.id = v.question_id;
  if not p_skipped then
    v_correct := public.grade_answer(v_q.answer_format, v_q.accepted_answers, v_answer);
    select e.answer into v_last from public.practice_attempt_events e
    where e.attempt_id = p_attempt and e.kind in ('answered','changed_answer') order by e.id desc limit 1;
    if v_last is not null and v_last <> v_answer then
      insert into public.practice_attempt_events(attempt_id, student_id, kind, answer) values (p_attempt, v.student_id, 'changed_answer', v_answer);
    end if;
  end if;
  update public.practice_attempts a set
    submitted_at = now(), elapsed_ms = v_elapsed, active_ms = p_active_ms, first_interaction_ms = p_first_interaction_ms,
    selected_answer = v_answer, is_correct = v_correct, skipped = p_skipped, confidence = p_confidence,
    strategy_used_id = v_strategy
  where a.id = p_attempt;
  insert into public.practice_attempt_events(attempt_id, student_id, kind, answer)
  values (p_attempt, v.student_id, case when p_skipped then 'skipped' else 'submitted' end, v_answer);
  return query select v_correct, p_skipped, v_elapsed::integer, v_q.accepted_answers, v_q.teaching_explanation,
    v_q.strategy_explanation,
    coalesce((select jsonb_agg(jsonb_build_object('choice', d.choice_key, 'rationale', d.rationale, 'trap', t.trap_key)
      order by d.choice_key) from public.practice_question_distractors d left join public.trap_types t on t.id = d.trap_type_id
      where d.question_id = v_q.id), '[]'::jsonb),
    coalesce((select jsonb_agg(jsonb_build_object('strategy_key', st.strategy_key, 'role', ps.role,
      'is_fastest', ps.is_fastest, 'explanation', ps.strategy_explanation) order by ps.is_fastest desc, st.strategy_key)
      from public.practice_question_strategies ps join public.question_strategies st on st.id = ps.strategy_id
      where ps.question_id = v_q.id), '[]'::jsonb);
end $$;

-- Records every request. While app_settings.ai_help_enabled is not true the request is stored as 'disabled'.
create function public.request_ai_help(p_attempt uuid, p_mode text) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare v public.practice_attempts; v_enabled boolean; v_status text; v_id uuid;
begin
  select a.* into v from public.practice_attempts a join public.students s on s.id = a.student_id
  where a.id = p_attempt and s.linked_user_id = auth.uid() for update of a;
  if not found then raise exception 'Only the student who started this attempt can ask for help' using errcode = '42501'; end if;
  if p_mode is null or p_mode not in ('hint','concept','strategy','worked_example','answer_reveal') then
    raise exception 'Unknown help mode %', p_mode using errcode = '22023';
  end if;
  if p_mode = 'answer_reveal' and v.submitted_at is null then
    raise exception 'The answer can only be revealed after submission' using errcode = '22023';
  end if;
  select (st.value = 'true'::jsonb) into v_enabled from public.app_settings st where st.key = 'ai_help_enabled';
  v_status := case when coalesce(v_enabled, false) then 'pending' else 'disabled' end;
  insert into public.ai_help_requests(attempt_id, student_id, requested_by, mode, status)
  values (p_attempt, v.student_id, auth.uid(), p_mode, v_status) returning id into v_id;
  if v_status = 'pending' then
    -- ai_help_used marks help received before the answer was submitted.
    if v.submitted_at is null then update public.practice_attempts set ai_help_used = true where id = p_attempt; end if;
    insert into public.practice_attempt_events(attempt_id, student_id, kind, detail)
    values (p_attempt, v.student_id, 'ai_help', jsonb_build_object('mode', p_mode, 'request_id', v_id));
  end if;
  return jsonb_build_object('request_id', v_id, 'status', v_status);
end $$;

-- Analytics RPCs (linked student, or guardian with can_view_progress).
create function public.student_skill_estimates(p_student uuid)
returns table (skill_id uuid, skill_key text, section text, attempts bigint, correct bigint, accuracy numeric,
  median_elapsed_ms bigint, pacing_ratio numeric, knowledge_weak boolean, pacing_weak boolean)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  return query select * from public.skill_estimates_internal(p_student) e order by e.section, e.skill_key;
end $$;

create function public.student_streak(p_student uuid, p_tz text default null, p_as_of date default null) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v_tz text; v_as_of date; r record;
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  v_tz := coalesce(p_tz, public.student_time_zone(p_student));
  if not public.is_valid_time_zone(v_tz) then raise exception 'Unknown time zone %', v_tz using errcode = '22023'; end if;
  v_as_of := coalesce(p_as_of, (now() at time zone v_tz)::date);
  select * into r from public.streak_internal(p_student, v_tz, v_as_of);
  return jsonb_build_object('time_zone', v_tz, 'as_of', v_as_of, 'current_streak', r.current_streak,
    'longest_streak', r.longest_streak, 'last_practice_day', r.last_practice_day);
end $$;

-- Week is [week_start, week_start + 7 days) in the student's time zone (student, else household, else UTC).
create function public.student_weekly_progress(p_student uuid, p_week_start date) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v_tz text; v_week tstzrange; v_goal public.weekly_practice_goals; v_streak record; v jsonb;
begin
  if not public.can_view_student(p_student) then
    raise exception 'Not allowed to view this student' using errcode = '42501';
  end if;
  if p_week_start is null or extract(isodow from p_week_start) <> 1 then
    raise exception 'week_start must be a Monday' using errcode = '22023';
  end if;
  v_tz := public.student_time_zone(p_student);
  v_week := public.local_week_bounds(p_week_start, v_tz);
  select * into v_goal from public.weekly_practice_goals g
  where g.student_id = p_student and g.week_start = p_week_start and g.subject is null;
  select * into v_streak from public.streak_internal(p_student, v_tz, least((now() at time zone v_tz)::date, p_week_start + 6));

  with fin as (
    select a.*, k.section as skill_section, k.skill_key from public.practice_attempts a
    left join public.practice_question_skills qs on qs.question_id = a.question_id and qs.is_primary
    left join public.skills k on k.id = qs.skill_id
    where a.student_id = p_student and a.submitted_at <@ v_week
  ), sub as (select * from fin where not skipped),
  totals as (
    select count(*) as submitted, count(*) filter (where is_correct) as correct,
      round(percentile_cont(0.5) within group (order by elapsed_ms))::bigint as median_elapsed_ms,
      round(avg(confidence), 2) as avg_confidence
    from sub
  ), fin_totals as (
    select count(*) filter (where skipped) as skipped, sum(elapsed_ms) as total_elapsed_ms, sum(active_ms) as total_active_ms,
      count(*) filter (where ai_help_used) as ai_help_attempts, coalesce(sum(hint_count), 0) as hints_used
    from fin
  ), ev as (
    select count(*) filter (where kind = 'skipped') as skip_events, count(*) filter (where kind = 'returned') as returns,
      count(*) filter (where kind = 'changed_answer') as answer_changes
    from public.practice_attempt_events e where e.student_id = p_student and e.occurred_at <@ v_week
  ), est as (select * from public.skill_estimates_internal(p_student))
  select jsonb_build_object(
    'student_id', p_student,
    'week_start', p_week_start,
    'time_zone', v_tz,
    'goal', case when v_goal.id is null then null else jsonb_build_object('target_questions', v_goal.target_questions,
      'target_minutes', v_goal.target_minutes, 'goal_mode', v_goal.goal_mode) end,
    'questions_attempted', (select count(*) from public.practice_attempts a where a.student_id = p_student and a.presented_at <@ v_week),
    'questions_submitted', t.submitted,
    'skipped', f.skipped,
    'skip_events', ev.skip_events,
    'returns', ev.returns,
    'answer_changes', ev.answer_changes,
    'correct', t.correct,
    'accuracy', case when t.submitted > 0 then round(t.correct::numeric / t.submitted, 4) end,
    'total_elapsed_ms', coalesce(f.total_elapsed_ms, 0),
    'total_active_ms', f.total_active_ms,
    'median_elapsed_ms', t.median_elapsed_ms,
    'avg_confidence', t.avg_confidence,
    'ai_help_attempts', f.ai_help_attempts,
    'hints_used', f.hints_used,
    'goal_progress', case when v_goal.id is null then null else jsonb_build_object(
      'questions_pct', round(100.0 * t.submitted / v_goal.target_questions, 1),
      'minutes_pct', round(coalesce(f.total_elapsed_ms, 0) / 600.0 / v_goal.target_minutes, 1)) end,
    'streak', jsonb_build_object('current', v_streak.current_streak, 'longest', v_streak.longest_streak),
    'skill_summary', jsonb_build_object(
      'knowledge_weak', coalesce((select jsonb_agg(skill_key order by skill_key) from est where knowledge_weak), '[]'::jsonb),
      'pacing_weak', coalesce((select jsonb_agg(skill_key order by skill_key) from est where pacing_weak), '[]'::jsonb),
      'insufficient_data', (select count(*) from est where knowledge_weak is null)),
    'by_skill', coalesce((select jsonb_agg(jsonb_build_object('section', skill_section, 'skill', skill_key,
        'submitted', n, 'correct', c, 'median_elapsed_ms', m) order by skill_section, skill_key)
      from (select skill_section, skill_key, count(*) n, count(*) filter (where is_correct) c,
              round(percentile_cont(0.5) within group (order by elapsed_ms))::bigint m
            from sub group by skill_section, skill_key) s), '[]'::jsonb),
    'by_strategy', coalesce((select jsonb_agg(jsonb_build_object('strategy_key', strategy_key,
        'submitted', n, 'correct', c) order by strategy_key)
      from (select st.strategy_key, count(*) n, count(*) filter (where sub.is_correct) c
            from sub join public.question_strategies st on st.id = sub.strategy_used_id
            group by st.strategy_key) s), '[]'::jsonb))
  into v from totals t, fin_totals f, ev;
  return v;
end $$;

-- v1 rule per target over up to 4 prior goal weeks (each week's completion capped at 1.5):
-- mean >= 1.0 -> +10%; 0.7..1.0 -> hold; < 0.7 -> -15%. Needs >= 2 weeks; clamped to [5,200] questions, [10,600] minutes.
create function public.suggest_next_week_goal(p_student uuid, p_week_start date default null) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v_tz text; v_week date; r record;
begin
  if not public.can_view_student(p_student) and not public.can_set_student_goals(p_student) then
    raise exception 'Not allowed to view this student' using errcode = '42501';
  end if;
  v_tz := public.student_time_zone(p_student);
  v_week := coalesce(p_week_start, (now() at time zone v_tz)::date - (extract(isodow from (now() at time zone v_tz)::date)::integer - 1) + 7);
  if extract(isodow from v_week) <> 1 then raise exception 'week_start must be a Monday' using errcode = '22023'; end if;
  with weeks as (
    select g.week_start, g.target_questions, g.target_minutes,
      (select count(*) from public.practice_attempts a where a.student_id = p_student and not a.skipped
        and a.submitted_at <@ public.local_week_bounds(g.week_start, v_tz)) as done_q,
      (select coalesce(sum(a.elapsed_ms), 0) / 60000.0 from public.practice_attempts a where a.student_id = p_student
        and a.submitted_at <@ public.local_week_bounds(g.week_start, v_tz)) as done_m
    from public.weekly_practice_goals g
    where g.student_id = p_student and g.subject is null and g.week_start >= v_week - 28 and g.week_start < v_week
  ), stats as (
    select count(*) as weeks,
      -- least() ignores nulls, so weeks without a target are filtered out explicitly.
      count(target_questions) as nq, avg(least(done_q::numeric / target_questions, 1.5)) filter (where target_questions is not null) as cq,
      count(target_minutes) as nm, avg(least(done_m / target_minutes, 1.5)) filter (where target_minutes is not null) as cm,
      (array_agg(target_questions order by week_start desc) filter (where target_questions is not null))[1] as base_q,
      (array_agg(target_minutes order by week_start desc) filter (where target_minutes is not null))[1] as base_m
    from weeks
  )
  select *, case when nq >= 2 then cq end as rq, case when nm >= 2 then cm end as rm into r from stats;
  return jsonb_build_object(
    'student_id', p_student, 'week_start', v_week, 'rule', 'v1', 'weeks_considered', r.weeks,
    'questions_completion', round(r.rq, 3), 'minutes_completion', round(r.rm, 3),
    'target_questions', case when r.rq is not null then least(200, greatest(5, round(r.base_q *
      case when r.rq >= 1 then 1.10 when r.rq >= 0.7 then 1.0 else 0.85 end)))::integer end,
    'target_minutes', case when r.rm is not null then least(600, greatest(10, round(r.base_m *
      case when r.rm >= 1 then 1.10 when r.rm >= 0.7 then 1.0 else 0.85 end)))::integer end,
    'basis', case when r.rq is null and r.rm is null then 'insufficient_history' else 'history' end);
end $$;

-- Students in the caller's households (can_view_progress) with no submitted attempt for the threshold.
-- Threshold: p_days, else the caller's smallest enabled alert_preferences.inactivity_days for that student.
create function public.student_inactivity(p_days integer default null)
returns table (student_id uuid, display_name text, household_id uuid, last_submitted_at timestamptz,
  days_inactive integer, threshold_days integer)
language plpgsql stable security definer set search_path = '' as $$
#variable_conflict use_column
begin
  if p_days is not null and p_days not between 1 and 365 then raise exception 'p_days must be 1 to 365' using errcode = '22023'; end if;
  return query
  with mine as (
    select s.id, s.display_name, s.household_id,
      coalesce(p_days, (select min(ap.inactivity_days) from public.alert_preferences ap
        where ap.user_id = auth.uid() and ap.student_id = s.id and ap.enabled)) as threshold,
      (select max(a.submitted_at) from public.practice_attempts a where a.student_id = s.id) as last_at
    from public.students s
    where s.archived_at is null and public.has_household_permission(s.household_id, 'view_progress')
  )
  select m.id, m.display_name, m.household_id, m.last_at,
    extract(day from now() - m.last_at)::integer, m.threshold
  from mine m
  where m.threshold is not null and (m.last_at is null or m.last_at <= now() - make_interval(days => m.threshold))
  order by m.last_at nulls first, m.id;
end $$;

-- Privileges: anon gets nothing; authenticated gets the minimum, filtered by RLS.
do $$
declare t text;
begin
  foreach t in array array['profiles','households','household_members','students','household_invitations',
    'subscriptions','app_settings','exam_families','exam_versions','question_types','skills','trap_types',
    'question_strategies','practice_questions','practice_question_skills','practice_question_distractors',
    'practice_question_strategies','weekly_practice_goals','practice_sessions','practice_session_items',
    'practice_attempts','practice_attempt_events','ai_help_requests','alert_preferences','student_test_scores'] loop
    execute format('alter table public.%I enable row level security', t);
    execute format('revoke all on public.%I from anon, authenticated', t);
    execute format('grant select, insert, update, delete on public.%I to service_role', t);
  end loop;
end $$;
revoke all on public.student_official_scores from anon, authenticated;
grant select on public.student_official_scores to authenticated, service_role;

grant select, insert (id, display_name), update (display_name) on public.profiles to authenticated;
create policy own_profile_read on public.profiles for select to authenticated using (id = (select auth.uid()));
create policy own_profile_insert on public.profiles for insert to authenticated with check (id = (select auth.uid()));
create policy own_profile_update on public.profiles for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));

grant select, update (name, time_zone) on public.households to authenticated;
create policy member_household_read on public.households for select to authenticated using (public.is_household_member(id));
create policy manager_household_update on public.households for update to authenticated
  using (public.has_household_permission(id, 'manage_members')) with check (public.has_household_permission(id, 'manage_members'));

grant select on public.household_members to authenticated;
create policy household_member_read on public.household_members for select to authenticated
  using (user_id = (select auth.uid()) or public.is_household_guardian(household_id));

-- Any guardian of the household sees the roster; progress data needs can_view_progress.
grant select, update (display_name, graduation_year, grade_level, archived_at, time_zone) on public.students to authenticated;
create policy student_read on public.students for select to authenticated
  using (linked_user_id = (select auth.uid()) or public.is_household_guardian(household_id));
create policy student_update on public.students for update to authenticated
  using (public.can_manage_student(id) or (linked_user_id = (select auth.uid()) and (household_id is null or is_independent)))
  with check (public.can_manage_student(id) or (linked_user_id = (select auth.uid()) and (household_id is null or is_independent)));

grant select (id, household_id, role, student_id, permissions, created_by, created_at, expires_at, accepted_by, accepted_at)
  on public.household_invitations to authenticated;
create policy guardian_invitation_read on public.household_invitations for select to authenticated
  using (public.is_household_guardian(household_id));

-- Provider identifiers stay server-side.
grant select (id, owner_user_id, household_id, plan_key, status, provider, current_period_end, created_at)
  on public.subscriptions to authenticated;
create policy subscription_read on public.subscriptions for select to authenticated
  using (owner_user_id = (select auth.uid()) or public.has_household_permission(household_id, 'manage_billing'));

do $$
declare t text;
begin
  foreach t in array array['exam_families','exam_versions','question_types','skills','trap_types','question_strategies'] loop
    execute format('grant select on public.%I to authenticated', t);
    execute format('create policy catalog_read on public.%I for select to authenticated using (true)', t);
  end loop;
end $$;

-- Answers, hints, explanations and distractor rationales are revealed only through the practice RPCs.
grant select (id, exam_version_id, question_type_id, blueprint_id, section, difficulty, difficulty_calibrated,
  difficulty_label, stem, choices, answer_format, expected_time_seconds, source_attribution, license, status, created_at)
  on public.practice_questions to authenticated;
create policy published_question_read on public.practice_questions for select to authenticated using (status = 'published');

grant select on public.practice_question_skills to authenticated;
create policy published_question_skill_read on public.practice_question_skills for select to authenticated
  using (exists (select 1 from public.practice_questions q where q.id = question_id and q.status = 'published'));

grant select (question_id, strategy_id, role, is_fastest) on public.practice_question_strategies to authenticated;
create policy published_question_strategy_read on public.practice_question_strategies for select to authenticated
  using (exists (select 1 from public.practice_questions q where q.id = question_id and q.status = 'published'));

grant select, insert (student_id, week_start, target_questions, target_minutes, subject, goal_mode),
  update (week_start, target_questions, target_minutes, subject, goal_mode), delete on public.weekly_practice_goals to authenticated;
create policy goal_read on public.weekly_practice_goals for select to authenticated
  using (public.can_view_student(student_id) or public.can_set_student_goals(student_id));
create policy goal_insert on public.weekly_practice_goals for insert to authenticated
  with check (public.can_set_student_goals(student_id) and set_by = (select auth.uid()));
create policy goal_update on public.weekly_practice_goals for update to authenticated
  using (public.can_set_student_goals(student_id)) with check (public.can_set_student_goals(student_id));
create policy goal_delete on public.weekly_practice_goals for delete to authenticated
  using (public.can_set_student_goals(student_id));

do $$
declare t text;
begin
  foreach t in array array['practice_sessions','practice_attempts','practice_attempt_events','ai_help_requests'] loop
    execute format('grant select on public.%I to authenticated', t);
    execute format('create policy student_data_read on public.%I for select to authenticated using (public.can_view_student(student_id))', t);
  end loop;
end $$;
grant select on public.practice_session_items to authenticated;
create policy session_item_read on public.practice_session_items for select to authenticated
  using (exists (select 1 from public.practice_sessions ps where ps.id = session_id and public.can_view_student(ps.student_id)));

grant select, insert (student_id, channel, inactivity_days, enabled), update (inactivity_days, enabled), delete
  on public.alert_preferences to authenticated;
create policy own_alert_read on public.alert_preferences for select to authenticated using (user_id = (select auth.uid()));
create policy own_alert_insert on public.alert_preferences for insert to authenticated
  with check (user_id = (select auth.uid()) and public.can_view_student(student_id));
create policy own_alert_update on public.alert_preferences for update to authenticated
  using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()) and public.can_view_student(student_id));
create policy own_alert_delete on public.alert_preferences for delete to authenticated using (user_id = (select auth.uid()));

-- Clients may only add self-reported scores; official scores and practice estimates are written server-side.
grant select, insert (student_id, exam_version_id, test_date, composite, section_scores, score_source), delete
  on public.student_test_scores to authenticated;
create policy score_read on public.student_test_scores for select to authenticated using (public.can_view_student(student_id));
create policy self_reported_score_insert on public.student_test_scores for insert to authenticated
  with check (score_source = 'self_reported' and entered_by = (select auth.uid())
    and (public.can_manage_student(student_id) or exists (select 1 from public.students s
      where s.id = student_id and s.linked_user_id = (select auth.uid()))));
create policy own_self_reported_score_delete on public.student_test_scores for delete to authenticated
  using (score_source = 'self_reported' and entered_by = (select auth.uid()));

-- Function privileges: client RPCs and helpers for authenticated; internal helpers for nobody but the owner.
do $$
declare f regprocedure;
begin
  for f in select p.oid::regprocedure from pg_catalog.pg_proc p
    where p.pronamespace = 'public'::regnamespace and p.proname = any (array[
      'is_valid_time_zone','parse_numeric_answer','numeric_answers_valid','grade_answer','local_week_bounds',
      'is_household_member','is_household_guardian','has_household_permission','can_view_student','can_manage_student',
      'can_set_student_goals','create_household','add_student','create_self_student_profile','create_household_invitation',
      'accept_household_invitation','update_member_permissions','remove_household_member','leave_household',
      'household_entitlements','recommend_practice_set','start_practice_session','end_practice_session',
      'start_practice_attempt','record_attempt_event','request_hint','submit_practice_attempt','request_ai_help',
      'student_skill_estimates','student_streak','student_weekly_progress','suggest_next_week_goal','student_inactivity'])
  loop
    execute format('revoke all on function %s from public, anon', f);
    execute format('grant execute on function %s to authenticated, service_role', f);
  end loop;
  for f in select p.oid::regprocedure from pg_catalog.pg_proc p
    where p.pronamespace = 'public'::regnamespace and p.proname = any (array[
      'set_weekly_goal_audit','student_time_zone','require_linked_student','require_manager_remains','detach_member',
      'skill_estimates_internal','recommend_internal','streak_internal','open_attempt_for_caller'])
  loop
    execute format('revoke all on function %s from public, anon, authenticated', f);
  end loop;
end $$;
