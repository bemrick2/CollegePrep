-- CR-1 (issue #37): planning preferences that follow the student across devices.
-- Access mirrors weekly_practice_goals: read = the student or guardians with view_progress (or set_goals);
-- write = guardians with set_goals, or the student when independent or outside a household.
create table public.student_planning_preferences (
  student_id uuid primary key references public.students(id) on delete cascade,
  exam_family text check (exam_family in ('act','sat')),
  -- ACT composite 1-36; SAT total 400-1600 in 10-point steps. A target needs its test.
  target_score integer,
  goals text[] not null default '{}'
    check (goals <@ array['raise_score','merit','college_credit','lower_cost','explore']),
  daily_minutes integer check (daily_minutes between 5 and 15),
  set_by uuid default auth.uid() references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check (target_score is null or (exam_family = 'act' and target_score between 1 and 36)
    or (exam_family = 'sat' and target_score between 400 and 1600 and target_score % 10 = 0))
);

create trigger student_planning_preferences_audit before update on public.student_planning_preferences
  for each row execute function public.set_weekly_goal_audit();

alter table public.student_planning_preferences enable row level security;
revoke all on public.student_planning_preferences from anon, authenticated;
grant select, insert, update, delete on public.student_planning_preferences to service_role;
grant select, insert (student_id, exam_family, target_score, goals, daily_minutes),
  update (exam_family, target_score, goals, daily_minutes), delete on public.student_planning_preferences to authenticated;
create policy planning_read on public.student_planning_preferences for select to authenticated
  using (public.can_view_student(student_id) or public.can_set_student_goals(student_id));
create policy planning_insert on public.student_planning_preferences for insert to authenticated
  with check (public.can_set_student_goals(student_id) and set_by = (select auth.uid()));
create policy planning_update on public.student_planning_preferences for update to authenticated
  using (public.can_set_student_goals(student_id)) with check (public.can_set_student_goals(student_id));
create policy planning_delete on public.student_planning_preferences for delete to authenticated
  using (public.can_set_student_goals(student_id));
comment on table public.student_planning_preferences is
  'CR-1: exam family, target score, goals and daily minutes per student. A target is the family''s goal, not an estimate.';
