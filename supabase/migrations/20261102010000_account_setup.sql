-- CR-26 (issue #37, #218 A1): setup on the account, so a guardian's setup choices appear on the student's own device
-- and finished setup is not asked again on another device. Replaces Design's local reference SQL
-- (scripts/local/proposals/cr26_account_setup.sql, removed in the same change).
--
-- * student_planning_preferences gains exam_intent (act | sat | both | undecided), planned_test_date and study_days
--   (ISO weekdays 1-7, 1 to 7 distinct days); daily_minutes widens to 5-30. Read and write rules are unchanged: the
--   student or guardians with view_progress / set_goals read; guardians with set_goals, or the student when
--   independent or outside a household, write (can_set_student_goals).
-- * Practice sessions are 5-30 minutes: practice_sessions.target_minutes, start_practice_session and
--   recommend_practice_set. Both functions are otherwise unchanged.
-- * student_test_scores.score_source adds 'practice_test': a full practice test the family reports. Clients may insert
--   it as they insert 'self_reported' (a guardian with manage_students, or the student's own login). It never appears
--   in student_official_scores (official only), and the app's merit rules read official / self_reported only.
--   'official' and 'practice_estimate' stay server-only.
-- * student_setup_progress(student_id, setup_completed_at, starting_point_answered_at, benchmark_scheduled_for): no
--   client writes; written only through update_setup_progress by the student's own login, or by a guardian with
--   manage_students or set_goals. A household student may finish their own setup and schedule the starting benchmark,
--   but still cannot write the guardian-owned plan. Completion is never undone by a later write (the first time is
--   kept). Readable by anyone who may view the student, and by those who may write it.
--
-- Differences from the reference SQL (all intentional):
-- * update_setup_progress refuses an archived student for every caller (the reference checked archival only for the
--   student's own login), refuses a patch that is not a JSON object or carries an unknown key, and requires the two
--   flags to be JSON booleans and benchmark_scheduled_for to be null or a timestamp. The 60-day limit is unchanged.
-- * student_setup_progress is also readable by the guardians who may write it (manage_students / set_goals without
--   view_progress), the #218 C1 precedent: otherwise they could write a row they can never read back.
-- * Clients read the progress columns and updated_at only; updated_by (a user id) is not granted.
-- * study_days must be distinct (public.iso_weekdays_valid), and planned_test_date is limited to 2020-2100.
-- Objects are altered or replaced in place.

-- Distinct ISO weekdays (1 = Monday ... 7 = Sunday), no nulls. Cardinality is checked by each caller's constraint.
create function public.iso_weekdays_valid(p_days smallint[]) returns boolean
language sql immutable set search_path = '' as $$
  select coalesce(bool_and(d between 1 and 7), true) and count(*) = count(distinct d) and count(d) = count(*)
  from unnest(p_days) d
$$;
revoke all on function public.iso_weekdays_valid(smallint[]) from public, anon;
grant execute on function public.iso_weekdays_valid(smallint[]) to authenticated, service_role;

alter table public.student_planning_preferences
  add column exam_intent text check (exam_intent in ('act', 'sat', 'both', 'undecided')),
  add column planned_test_date date check (planned_test_date between '2020-01-01' and '2100-12-31'),
  add column study_days smallint[] check (study_days is null
    or (cardinality(study_days) between 1 and 7 and public.iso_weekdays_valid(study_days)));
alter table public.student_planning_preferences drop constraint student_planning_preferences_daily_minutes_check;
alter table public.student_planning_preferences add constraint student_planning_preferences_daily_minutes_check
  check (daily_minutes between 5 and 30);
grant insert (exam_intent, planned_test_date, study_days), update (exam_intent, planned_test_date, study_days)
  on public.student_planning_preferences to authenticated;

alter table public.practice_sessions drop constraint practice_sessions_target_minutes_check;
alter table public.practice_sessions add constraint practice_sessions_target_minutes_check
  check (target_minutes between 5 and 30);

create or replace function public.recommend_practice_set(p_student uuid, p_target_minutes integer default 10, p_exam_version uuid default null)
returns table (item_position integer, question_id uuid, skill_id uuid, expected_time_seconds integer, reason text)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.can_view_student(p_student) then raise exception 'Not allowed to view this student' using errcode = '42501'; end if;
  if p_target_minutes is null or p_target_minutes not between 5 and 30 then
    raise exception 'Sessions are 5 to 30 minutes' using errcode = '22023';
  end if;
  return query select * from public.recommend_internal(p_student, p_target_minutes, p_exam_version);
end $$;

create or replace function public.start_practice_session(p_student uuid, p_target_minutes integer default 10,
  p_goal uuid default null, p_exam_version uuid default null) returns uuid
language plpgsql security definer set search_path = '' as $$
declare v_id uuid;
begin
  perform public.require_linked_student(p_student);
  if p_target_minutes is null or p_target_minutes not between 5 and 30 then
    raise exception 'Sessions are 5 to 30 minutes' using errcode = '22023';
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

-- Practice-test scores: kept apart from official scores (student_official_scores reads 'official' only).
alter table public.student_test_scores drop constraint student_test_scores_score_source_check;
alter table public.student_test_scores add constraint student_test_scores_score_source_check
  check (score_source in ('official', 'self_reported', 'practice_estimate', 'practice_test'));
alter policy self_reported_score_insert on public.student_test_scores
  with check (score_source in ('self_reported', 'practice_test') and entered_by = (select auth.uid())
    and (public.can_manage_student(student_id) or exists (select 1 from public.students s
      where s.id = student_id and s.linked_user_id = (select auth.uid()))));
alter policy own_self_reported_score_delete on public.student_test_scores
  using (score_source in ('self_reported', 'practice_test') and entered_by = (select auth.uid()));

create table public.student_setup_progress (
  student_id uuid primary key references public.students(id) on delete cascade,
  setup_completed_at timestamptz,
  starting_point_answered_at timestamptz,
  benchmark_scheduled_for timestamptz,
  updated_by uuid references auth.users(id) on delete set null,
  updated_at timestamptz not null default now()
);
create index student_setup_progress_updated_by_idx on public.student_setup_progress(updated_by);
alter table public.student_setup_progress enable row level security;
revoke all on public.student_setup_progress from anon, authenticated;
grant select, insert, update, delete on public.student_setup_progress to service_role;
grant select (student_id, setup_completed_at, starting_point_answered_at, benchmark_scheduled_for, updated_at)
  on public.student_setup_progress to authenticated;
create policy setup_progress_read on public.student_setup_progress for select to authenticated
  using (public.can_view_student(student_id) or public.can_manage_student(student_id) or public.can_set_student_goals(student_id));
comment on table public.student_setup_progress is
  'CR-26: setup completion, starting-point answer and benchmark schedule per student. Written only by update_setup_progress.';

-- p_patch keys (all optional): setup_completed (boolean; true records completion once), starting_point_answered
-- (boolean; likewise), benchmark_scheduled_for (timestamp or null; present = set or clear it, at most 60 days ahead).
create function public.update_setup_progress(p_student uuid, p_patch jsonb) returns void
language plpgsql volatile security definer set search_path = '' as $$
declare v_key text; v_at timestamptz;
begin
  if p_student is null or not exists (select 1 from public.students s where s.id = p_student and s.archived_at is null
      and (s.linked_user_id = auth.uid() or public.can_manage_student(s.id) or public.can_set_student_goals(s.id))) then
    raise exception 'Not allowed to update setup for this student' using errcode = '42501';
  end if;
  if p_patch is null or jsonb_typeof(p_patch) <> 'object' then
    raise exception 'The setup patch must be a JSON object' using errcode = '22023';
  end if;
  for v_key in select jsonb_object_keys(p_patch) loop
    if v_key not in ('setup_completed', 'starting_point_answered', 'benchmark_scheduled_for') then
      raise exception 'Unknown setup field: %', v_key using errcode = '22023';
    end if;
  end loop;
  if (p_patch ? 'setup_completed' and jsonb_typeof(p_patch->'setup_completed') <> 'boolean')
     or (p_patch ? 'starting_point_answered' and jsonb_typeof(p_patch->'starting_point_answered') <> 'boolean') then
    raise exception 'setup_completed and starting_point_answered are true or false' using errcode = '22023';
  end if;
  if p_patch ? 'benchmark_scheduled_for' and jsonb_typeof(p_patch->'benchmark_scheduled_for') not in ('null', 'string') then
    raise exception 'benchmark_scheduled_for is a timestamp or null' using errcode = '22023';
  end if;
  v_at := (p_patch->>'benchmark_scheduled_for')::timestamptz;
  if v_at > now() + interval '60 days' then
    raise exception 'Schedule the benchmark within 60 days' using errcode = '22023';
  end if;
  insert into public.student_setup_progress as p (student_id, setup_completed_at, starting_point_answered_at,
      benchmark_scheduled_for, updated_by, updated_at)
  values (p_student,
    case when (p_patch->>'setup_completed')::boolean then now() end,
    case when (p_patch->>'starting_point_answered')::boolean then now() end,
    v_at, auth.uid(), now())
  on conflict (student_id) do update set
    -- Completion is never undone by a later write; the first completion time is kept.
    setup_completed_at = coalesce(p.setup_completed_at, excluded.setup_completed_at),
    starting_point_answered_at = coalesce(p.starting_point_answered_at, excluded.starting_point_answered_at),
    benchmark_scheduled_for = case when p_patch ? 'benchmark_scheduled_for' then excluded.benchmark_scheduled_for
                                   else p.benchmark_scheduled_for end,
    updated_by = excluded.updated_by, updated_at = excluded.updated_at;
end $$;
revoke all on function public.update_setup_progress(uuid, jsonb) from public, anon;
grant execute on function public.update_setup_progress(uuid, jsonb) to authenticated, service_role;
comment on function public.update_setup_progress(uuid, jsonb) is
  'CR-26: record setup progress. The student''s own login, or a guardian with manage_students or set_goals.';
