-- CR-26 (issue #37) REFERENCE IMPLEMENTATION, proposed by Design. Applied ONLY to the local disposable database by
-- scripts/local/live_stack.sh; it is not a migration. Research owns the schema and may adopt, change or replace it.
--
-- Setup answers kept on the account instead of one browser, so a guardian's choices appear on the student's device
-- and finished setup isn't asked again elsewhere:
--   student_planning_preferences   + exam_intent, planned_test_date, study_days; daily_minutes widened to 5-30
--   practice sessions              5-30 minutes (start_practice_session, recommend_practice_set, practice_sessions)
--   student_test_scores            + score_source 'practice_test' (client-insertable; never "official")
--   student_setup_progress         setup_completed_at, starting_point_answered_at, benchmark_scheduled_for
-- High school is deliberately not stored (owner decision 2026-10-07: not needed for the first practice plan).

alter table public.student_planning_preferences
  add column exam_intent text check (exam_intent in ('act','sat','both','undecided')),
  add column planned_test_date date,
  add column study_days smallint[] check (study_days is null or (cardinality(study_days) between 1 and 7 and study_days <@ array[1,2,3,4,5,6,7]::smallint[]));
alter table public.student_planning_preferences drop constraint student_planning_preferences_daily_minutes_check;
alter table public.student_planning_preferences add constraint student_planning_preferences_daily_minutes_check check (daily_minutes between 5 and 30);
grant insert (exam_intent, planned_test_date, study_days), update (exam_intent, planned_test_date, study_days) on public.student_planning_preferences to authenticated;

alter table public.practice_sessions drop constraint practice_sessions_target_minutes_check;
alter table public.practice_sessions add constraint practice_sessions_target_minutes_check check (target_minutes between 5 and 30);

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

-- A full practice test the family reports is kept apart from official scores, and never feeds merit comparisons
-- (student_official_scores and the app's merit rules read official / self_reported only).
alter table public.student_test_scores drop constraint student_test_scores_score_source_check;
alter table public.student_test_scores add constraint student_test_scores_score_source_check
  check (score_source in ('official','self_reported','practice_estimate','practice_test'));
drop policy self_reported_score_insert on public.student_test_scores;
create policy self_reported_score_insert on public.student_test_scores for insert to authenticated
  with check (score_source in ('self_reported','practice_test') and entered_by = (select auth.uid())
    and (public.can_manage_student(student_id) or exists (select 1 from public.students s
      where s.id = student_id and s.linked_user_id = (select auth.uid()))));
drop policy own_self_reported_score_delete on public.student_test_scores;
create policy own_self_reported_score_delete on public.student_test_scores for delete to authenticated
  using (score_source in ('self_reported','practice_test') and entered_by = (select auth.uid()));

-- Setup progress follows the student: a guardian who manages the student, or the student's own login, may record
-- it (a household student can't write the guardian-owned plan, but can finish their own setup and schedule the
-- starting benchmark).
create table public.student_setup_progress (
  student_id uuid primary key references public.students(id) on delete cascade,
  setup_completed_at timestamptz,
  starting_point_answered_at timestamptz,
  benchmark_scheduled_for timestamptz,
  updated_by uuid references auth.users(id) on delete set null,
  updated_at timestamptz not null default now()
);
alter table public.student_setup_progress enable row level security;
revoke all on public.student_setup_progress from anon, authenticated;
grant select on public.student_setup_progress to authenticated;
grant all on public.student_setup_progress to service_role;
create policy setup_progress_read on public.student_setup_progress for select to authenticated using (public.can_view_student(student_id));

create function public.update_setup_progress(p_student uuid, p_patch jsonb) returns void
language plpgsql volatile security definer set search_path = '' as $$
begin
  if not (public.can_manage_student(p_student) or public.can_set_student_goals(p_student)
          or exists (select 1 from public.students s where s.id = p_student and s.linked_user_id = auth.uid() and s.archived_at is null)) then
    raise exception 'Not allowed to update setup for this student' using errcode = '42501';
  end if;
  if p_patch ? 'benchmark_scheduled_for' and p_patch->>'benchmark_scheduled_for' is not null
     and (p_patch->>'benchmark_scheduled_for')::timestamptz > now() + interval '60 days' then
    raise exception 'Schedule the benchmark within 60 days' using errcode = '22023';
  end if;
  insert into public.student_setup_progress as p (student_id, setup_completed_at, starting_point_answered_at, benchmark_scheduled_for, updated_by, updated_at)
  values (p_student,
    case when (p_patch->>'setup_completed')::boolean then now() end,
    case when (p_patch->>'starting_point_answered')::boolean then now() end,
    (p_patch->>'benchmark_scheduled_for')::timestamptz, auth.uid(), now())
  on conflict (student_id) do update set
    -- Completion is never undone by a later write; the first completion time is kept.
    setup_completed_at = coalesce(p.setup_completed_at, excluded.setup_completed_at),
    starting_point_answered_at = coalesce(p.starting_point_answered_at, excluded.starting_point_answered_at),
    benchmark_scheduled_for = case when p_patch ? 'benchmark_scheduled_for' then excluded.benchmark_scheduled_for else p.benchmark_scheduled_for end,
    updated_by = excluded.updated_by, updated_at = excluded.updated_at;
end $$;
revoke all on function public.update_setup_progress(uuid, jsonb) from public, anon;
grant execute on function public.update_setup_progress(uuid, jsonb) to authenticated;
