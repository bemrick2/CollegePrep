-- Households, student profiles, practice content, server-graded attempts and weekly progress.
-- Requires auth.users and auth.uid() (Supabase; CI uses supabase/tests/support/auth_stub.sql).
-- Client roles never write attempts directly: grading and timing happen in security definer RPCs.
-- See docs/HOUSEHOLD_PRACTICE.md.

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text check (length(display_name) between 1 and 120),
  created_at timestamptz not null default now()
);

create table public.households (
  id uuid primary key default gen_random_uuid(),
  name text not null check (length(btrim(name)) between 1 and 120),
  created_by uuid not null references auth.users(id),
  created_at timestamptz not null default now()
);

create table public.household_members (
  household_id uuid not null references public.households(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('guardian','student')),
  created_at timestamptz not null default now(),
  primary key (household_id, user_id)
);
create index household_members_user_idx on public.household_members(user_id);

-- No date of birth is stored, by design.
create table public.students (
  id uuid primary key default gen_random_uuid(),
  household_id uuid not null references public.households(id) on delete cascade,
  display_name text not null check (length(btrim(display_name)) between 1 and 120),
  graduation_year integer check (graduation_year between 2000 and 2100),
  grade_level integer check (grade_level between 0 and 13),
  account_mode text not null default 'guardian_managed' check (account_mode in ('guardian_managed','student_login')),
  linked_user_id uuid unique references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  archived_at timestamptz
);
create index students_household_idx on public.students(household_id);

create table public.household_invitations (
  id uuid primary key default gen_random_uuid(),
  household_id uuid not null references public.households(id) on delete cascade,
  role text not null check (role in ('guardian','student')),
  student_id uuid references public.students(id) on delete cascade,
  code_hash text not null unique check (code_hash ~ '^[0-9a-f]{64}$'),
  created_by uuid not null references auth.users(id) on delete cascade,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null,
  accepted_by uuid references auth.users(id) on delete set null,
  accepted_at timestamptz,
  check ((role = 'student') = (student_id is not null))
);
create index household_invitations_household_idx on public.household_invitations(household_id);

create table public.question_strategies (
  id uuid primary key default gen_random_uuid(),
  strategy_key text not null unique check (strategy_key ~ '^[a-z][a-z0-9_]*$'),
  name text not null,
  description text,
  exam_family text,
  subject text,
  created_at timestamptz not null default now()
);

create table public.practice_questions (
  id uuid primary key default gen_random_uuid(),
  blueprint_id uuid references public.practice_blueprints(id),
  exam_family text not null,
  subject text not null,
  domain text,
  skill text,
  difficulty text check (difficulty in ('easy','medium','hard')),
  stem text not null,
  choices jsonb not null default '[]' check (jsonb_typeof(choices) = 'array'),
  correct_answer text not null,
  explanation text,
  expected_time_seconds integer check (expected_time_seconds > 0),
  common_traps jsonb not null default '[]' check (jsonb_typeof(common_traps) = 'array'),
  distractor_rationales jsonb not null default '{}' check (jsonb_typeof(distractor_rationales) = 'object'),
  source_attribution text,
  license text,
  status text not null default 'draft' check (status in ('draft','published','retired')),
  created_at timestamptz not null default now()
);

create table public.practice_question_strategies (
  question_id uuid not null references public.practice_questions(id) on delete cascade,
  strategy_id uuid not null references public.question_strategies(id),
  role text not null default 'primary' check (role in ('primary','secondary')),
  notes text,
  primary key (question_id, strategy_id)
);

create table public.weekly_practice_goals (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references public.students(id) on delete cascade,
  week_start date not null check (extract(isodow from week_start) = 1),
  target_questions integer check (target_questions > 0),
  target_minutes integer check (target_minutes > 0),
  subject text,
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
  started_at timestamptz not null default now(),
  ended_at timestamptz,
  goal_id uuid references public.weekly_practice_goals(id) on delete set null
);
create index practice_sessions_student_idx on public.practice_sessions(student_id);

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
  hint_count integer not null default 0 check (hint_count >= 0),
  ai_help_used boolean not null default false,
  strategy_used_id uuid references public.question_strategies(id),
  attempt_number integer not null default 1 check (attempt_number > 0),
  unique (student_id, question_id, attempt_number)
);
create index practice_attempts_student_submitted_idx on public.practice_attempts(student_id, submitted_at);

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
create function public.is_household_guardian(p_household uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.household_members m
    where m.household_id = p_household and m.user_id = auth.uid() and m.role = 'guardian')
$$;

create function public.is_household_member(p_household uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.household_members m
    where m.household_id = p_household and m.user_id = auth.uid())
$$;

create function public.can_manage_student(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s
    join public.household_members m on m.household_id = s.household_id
    where s.id = p_student and m.user_id = auth.uid() and m.role = 'guardian')
$$;

create function public.can_view_student(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s
    where s.id = p_student and s.linked_user_id = auth.uid())
  or public.can_manage_student(p_student)
$$;

-- RPCs
create function public.create_household(p_name text) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_uid uuid := auth.uid(); v_id uuid;
begin
  if v_uid is null then raise exception 'Authentication required' using errcode = '42501'; end if;
  insert into public.households(name, created_by) values (btrim(p_name), v_uid) returning id into v_id;
  insert into public.household_members(household_id, user_id, role) values (v_id, v_uid, 'guardian');
  return v_id;
end $$;

create function public.add_student(p_household uuid, p_display_name text,
  p_graduation_year integer default null, p_grade_level integer default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  if not public.is_household_guardian(p_household) then
    raise exception 'Only a guardian of this household can add students' using errcode = '42501';
  end if;
  insert into public.students(household_id, display_name, graduation_year, grade_level)
  values (p_household, btrim(p_display_name), p_graduation_year, p_grade_level) returning id into v_id;
  return v_id;
end $$;

create function public.create_household_invitation(p_household uuid, p_role text,
  p_student uuid default null, p_ttl_hours integer default 72) returns text
language plpgsql security definer set search_path = '' as $$
declare v_code text;
begin
  if not public.is_household_guardian(p_household) then
    raise exception 'Only a guardian of this household can invite members' using errcode = '42501';
  end if;
  if p_role is null or p_role not in ('guardian','student') then
    raise exception 'Invitation role must be guardian or student' using errcode = '22023';
  end if;
  if p_ttl_hours is null or p_ttl_hours not between 1 and 336 then
    raise exception 'Invitation lifetime must be between 1 and 336 hours' using errcode = '22023';
  end if;
  if p_role = 'student' and not exists (select 1 from public.students s where s.id = p_student
      and s.household_id = p_household and s.archived_at is null and s.linked_user_id is null) then
    raise exception 'Student invitations need an active, unlinked student of this household' using errcode = '22023';
  end if;
  if p_role = 'guardian' and p_student is not null then
    raise exception 'Guardian invitations cannot name a student' using errcode = '22023';
  end if;
  -- 244 random bits from two v4 UUIDs; only the SHA-256 digest is stored.
  v_code := replace(gen_random_uuid()::text || gen_random_uuid()::text, '-', '');
  insert into public.household_invitations(household_id, role, student_id, code_hash, created_by, expires_at)
  values (p_household, p_role, p_student, encode(sha256(convert_to(v_code, 'UTF8')), 'hex'),
          auth.uid(), now() + make_interval(hours => p_ttl_hours));
  return v_code;
end $$;

create function public.accept_household_invitation(p_code text) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_uid uuid := auth.uid(); v_inv public.household_invitations; v_student public.students;
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
  if v_inv.role = 'student' then
    select * into v_student from public.students s where s.id = v_inv.student_id for update;
    if v_student.archived_at is not null then raise exception 'This student profile is archived' using errcode = '22023'; end if;
    if v_student.linked_user_id is not null then
      raise exception 'This student profile is already linked to another account' using errcode = '22023';
    end if;
    if exists (select 1 from public.students s where s.linked_user_id = v_uid) then
      raise exception 'Your account is already linked to another student profile' using errcode = '22023';
    end if;
  end if;
  insert into public.household_members(household_id, user_id, role) values (v_inv.household_id, v_uid, v_inv.role);
  if v_inv.role = 'student' then
    update public.students set linked_user_id = v_uid, account_mode = 'student_login' where id = v_student.id;
  end if;
  update public.household_invitations set accepted_by = v_uid, accepted_at = now() where id = v_inv.id;
  return v_inv.household_id;
end $$;

-- Only the student's own login practises; guardians cannot act as the student.
create function public.start_practice_session(p_student uuid, p_goal uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  if not exists (select 1 from public.students s where s.id = p_student
      and s.linked_user_id = auth.uid() and s.archived_at is null) then
    raise exception 'Only the student''s own login can practise' using errcode = '42501';
  end if;
  if p_goal is not null and not exists (select 1 from public.weekly_practice_goals g where g.id = p_goal and g.student_id = p_student) then
    raise exception 'Goal does not belong to this student' using errcode = '22023';
  end if;
  insert into public.practice_sessions(student_id, goal_id) values (p_student, p_goal) returning id into v_id;
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
  perform 1 from public.students s where s.id = p_student
    and s.linked_user_id = auth.uid() and s.archived_at is null for update;
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
  return v_id;
end $$;

create function public.submit_practice_attempt(p_attempt uuid, p_selected_answer text,
  p_active_ms integer default null, p_first_interaction_ms integer default null,
  p_hint_count integer default 0, p_ai_help_used boolean default false, p_strategy_key text default null)
returns table (is_correct boolean, correct_answer text, explanation text, elapsed_ms integer)
language plpgsql security definer set search_path = '' as $$
#variable_conflict use_column
declare v_attempt public.practice_attempts; v_q public.practice_questions; v_strategy uuid; v_elapsed numeric;
begin
  select a.* into v_attempt from public.practice_attempts a
  join public.students s on s.id = a.student_id
  where a.id = p_attempt and s.linked_user_id = auth.uid()
  for update of a;
  if not found then raise exception 'Only the student who started this attempt can submit it' using errcode = '42501'; end if;
  if v_attempt.submitted_at is not null then raise exception 'Attempt was already submitted' using errcode = '22023'; end if;
  if nullif(btrim(p_selected_answer), '') is null then raise exception 'An answer is required' using errcode = '22023'; end if;
  if p_active_ms < 0 or p_first_interaction_ms < 0 or p_hint_count is null or p_hint_count < 0 or p_ai_help_used is null then
    raise exception 'Client timing and hint values must be non-negative' using errcode = '22023';
  end if;
  v_elapsed := floor(extract(epoch from now() - v_attempt.presented_at) * 1000);
  if v_elapsed > 2147483647 then raise exception 'Attempt is too old to submit; start a new attempt' using errcode = '22023'; end if;
  if p_active_ms > v_elapsed or p_first_interaction_ms > v_elapsed then
    raise exception 'Client-reported time exceeds server elapsed time' using errcode = '22023';
  end if;
  if p_strategy_key is not null then
    select st.id into v_strategy from public.question_strategies st where st.strategy_key = p_strategy_key;
    if not found then raise exception 'Unknown strategy %', p_strategy_key using errcode = '22023'; end if;
  end if;
  select q.* into v_q from public.practice_questions q where q.id = v_attempt.question_id;
  update public.practice_attempts a set
    submitted_at = now(), elapsed_ms = v_elapsed, active_ms = p_active_ms,
    first_interaction_ms = p_first_interaction_ms, selected_answer = p_selected_answer,
    is_correct = btrim(p_selected_answer) = btrim(v_q.correct_answer),
    hint_count = p_hint_count, ai_help_used = p_ai_help_used, strategy_used_id = v_strategy
  where a.id = p_attempt;
  return query select btrim(p_selected_answer) = btrim(v_q.correct_answer), v_q.correct_answer, v_q.explanation, v_elapsed::integer;
end $$;

-- Week is [week_start, week_start + 7 days) in UTC on submitted_at; questions_attempted counts presented_at.
create function public.student_weekly_progress(p_student uuid, p_week_start date) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare v_from timestamptz; v_to timestamptz; v_goal public.weekly_practice_goals; v jsonb;
begin
  if not public.can_view_student(p_student) then
    raise exception 'Not allowed to view this student' using errcode = '42501';
  end if;
  if p_week_start is null or extract(isodow from p_week_start) <> 1 then
    raise exception 'week_start must be a Monday' using errcode = '22023';
  end if;
  v_from := p_week_start::timestamp at time zone 'UTC';
  v_to := v_from + interval '7 days';
  select * into v_goal from public.weekly_practice_goals g
  where g.student_id = p_student and g.week_start = p_week_start and g.subject is null;

  with sub as (
    select a.*, q.subject, q.skill from public.practice_attempts a
    join public.practice_questions q on q.id = a.question_id
    where a.student_id = p_student and a.submitted_at >= v_from and a.submitted_at < v_to
  ), totals as (
    select count(*) as submitted, count(*) filter (where is_correct) as correct,
      sum(elapsed_ms) as total_elapsed_ms, sum(active_ms) as total_active_ms,
      round(percentile_cont(0.5) within group (order by elapsed_ms))::bigint as median_elapsed_ms,
      count(*) filter (where ai_help_used) as ai_help_attempts, coalesce(sum(hint_count), 0) as hints_used
    from sub
  )
  select jsonb_build_object(
    'student_id', p_student,
    'week_start', p_week_start,
    'goal', case when v_goal.id is null then null else jsonb_build_object(
      'target_questions', v_goal.target_questions, 'target_minutes', v_goal.target_minutes) end,
    'questions_attempted', (select count(*) from public.practice_attempts a
      where a.student_id = p_student and a.presented_at >= v_from and a.presented_at < v_to),
    'questions_submitted', t.submitted,
    'correct', t.correct,
    'accuracy', case when t.submitted > 0 then round(t.correct::numeric / t.submitted, 4) end,
    'total_elapsed_ms', coalesce(t.total_elapsed_ms, 0),
    'total_active_ms', t.total_active_ms,
    'median_elapsed_ms', t.median_elapsed_ms,
    'ai_help_attempts', t.ai_help_attempts,
    'hints_used', t.hints_used,
    'goal_progress', case when v_goal.id is null then null else jsonb_build_object(
      'questions_pct', round(100.0 * t.submitted / v_goal.target_questions, 1),
      'minutes_pct', round(coalesce(t.total_elapsed_ms, 0) / 600.0 / v_goal.target_minutes, 1)) end,
    'by_skill', coalesce((select jsonb_agg(jsonb_build_object('subject', subject, 'skill', skill,
        'submitted', n, 'correct', c, 'median_elapsed_ms', m) order by subject, skill)
      from (select subject, skill, count(*) n, count(*) filter (where is_correct) c,
              round(percentile_cont(0.5) within group (order by elapsed_ms))::bigint m
            from sub group by subject, skill) s), '[]'::jsonb),
    'by_strategy', coalesce((select jsonb_agg(jsonb_build_object('strategy_key', strategy_key,
        'submitted', n, 'correct', c) order by strategy_key)
      from (select st.strategy_key, count(*) n, count(*) filter (where sub.is_correct) c
            from sub join public.question_strategies st on st.id = sub.strategy_used_id
            group by st.strategy_key) s), '[]'::jsonb))
  into v from totals t;
  return v;
end $$;

-- Privileges: anon gets nothing; authenticated gets the minimum, filtered by RLS.
do $$
declare t text;
begin
  foreach t in array array['profiles','households','household_members','students','household_invitations',
    'question_strategies','practice_questions','practice_question_strategies','weekly_practice_goals',
    'practice_sessions','practice_attempts'] loop
    execute format('alter table public.%I enable row level security', t);
    execute format('revoke all on public.%I from anon, authenticated', t);
    execute format('grant select, insert, update, delete on public.%I to service_role', t);
  end loop;
end $$;

grant select, insert (id, display_name), update (display_name) on public.profiles to authenticated;
create policy own_profile_read on public.profiles for select to authenticated using (id = (select auth.uid()));
create policy own_profile_insert on public.profiles for insert to authenticated with check (id = (select auth.uid()));
create policy own_profile_update on public.profiles for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));

grant select on public.households to authenticated;
create policy member_household_read on public.households for select to authenticated using (public.is_household_member(id));

grant select on public.household_members to authenticated;
create policy household_member_read on public.household_members for select to authenticated
  using (user_id = (select auth.uid()) or public.is_household_guardian(household_id));

grant select, update (display_name, graduation_year, grade_level, archived_at) on public.students to authenticated;
create policy student_read on public.students for select to authenticated using (public.can_view_student(id));
create policy guardian_student_update on public.students for update to authenticated
  using (public.can_manage_student(id)) with check (public.can_manage_student(id));

grant select (id, household_id, role, student_id, created_by, created_at, expires_at, accepted_by, accepted_at)
  on public.household_invitations to authenticated;
create policy guardian_invitation_read on public.household_invitations for select to authenticated
  using (public.is_household_guardian(household_id));

grant select on public.question_strategies to authenticated;
create policy strategy_read on public.question_strategies for select to authenticated using (true);

-- correct_answer, explanation and distractor_rationales are revealed only by submit_practice_attempt.
grant select (id, blueprint_id, exam_family, subject, domain, skill, difficulty, stem, choices,
  expected_time_seconds, common_traps, source_attribution, license, status, created_at)
  on public.practice_questions to authenticated;
create policy published_question_read on public.practice_questions for select to authenticated using (status = 'published');

grant select on public.practice_question_strategies to authenticated;
create policy published_question_strategy_read on public.practice_question_strategies for select to authenticated
  using (exists (select 1 from public.practice_questions q where q.id = question_id and q.status = 'published'));

grant select, insert (student_id, week_start, target_questions, target_minutes, subject),
  update (week_start, target_questions, target_minutes, subject), delete on public.weekly_practice_goals to authenticated;
create policy goal_read on public.weekly_practice_goals for select to authenticated using (public.can_view_student(student_id));
create policy guardian_goal_insert on public.weekly_practice_goals for insert to authenticated
  with check (public.can_manage_student(student_id) and set_by = (select auth.uid()));
create policy guardian_goal_update on public.weekly_practice_goals for update to authenticated
  using (public.can_manage_student(student_id)) with check (public.can_manage_student(student_id));
create policy guardian_goal_delete on public.weekly_practice_goals for delete to authenticated
  using (public.can_manage_student(student_id));

grant select on public.practice_sessions to authenticated;
create policy session_read on public.practice_sessions for select to authenticated using (public.can_view_student(student_id));

grant select on public.practice_attempts to authenticated;
create policy attempt_read on public.practice_attempts for select to authenticated using (public.can_view_student(student_id));

do $$
declare f text;
begin
  foreach f in array array['is_household_guardian(uuid)','is_household_member(uuid)','can_view_student(uuid)',
    'can_manage_student(uuid)','create_household(text)','add_student(uuid,text,integer,integer)',
    'create_household_invitation(uuid,text,uuid,integer)','accept_household_invitation(text)',
    'start_practice_session(uuid,uuid)','end_practice_session(uuid)',
    'start_practice_attempt(uuid,uuid,uuid)',
    'submit_practice_attempt(uuid,text,integer,integer,integer,boolean,text)',
    'student_weekly_progress(uuid,date)'] loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;
revoke all on function public.set_weekly_goal_audit() from public, anon, authenticated;
