-- CR-13 (issue #37): major certainty and saved interests, following the student across devices.
-- Keys come from the frontend's list (web/src/lib/engine/interests.ts); only their shape is checked here.
-- Nothing is required: certainty and interests may both be empty.

create function public.academic_interests_valid(p jsonb) returns boolean
language sql immutable set search_path = '' as $$
  select jsonb_typeof(p) = 'array' and jsonb_array_length(p) <= 8
    and not exists (select 1 from jsonb_array_elements(p) e where
          jsonb_typeof(e) <> 'object'
          or exists (select 1 from jsonb_object_keys(e) k where k not in ('kind', 'key', 'focus'))
          or coalesce(e->>'kind', '') not in ('area', 'major')
          or coalesce(e->>'key', '') !~ '^[a-z0-9]+(-[a-z0-9]+)*$' or length(e->>'key') > 60
          or (e ? 'focus' and jsonb_typeof(e->'focus') <> 'boolean'))
    and (select count(*) from jsonb_array_elements(p) e) = (select count(distinct (e->>'kind', e->>'key')) from jsonb_array_elements(p) e)
    and (select count(*) from jsonb_array_elements(p) e where (e->>'focus')::boolean) <= 1
$$;

create table public.student_academic_interests (
  student_id uuid primary key references public.students(id) on delete cascade,
  certainty text check (certainty in ('unsure', 'few', 'sure')),
  interests jsonb not null default '[]'::jsonb check (public.academic_interests_valid(interests)),
  set_by uuid default auth.uid() references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create trigger student_academic_interests_audit before update on public.student_academic_interests
  for each row execute function public.set_weekly_goal_audit();

alter table public.student_academic_interests enable row level security;
revoke all on public.student_academic_interests from anon, authenticated;
grant select, insert, update, delete on public.student_academic_interests to service_role;
grant select, insert (student_id, certainty, interests), update (certainty, interests), delete
  on public.student_academic_interests to authenticated;
create policy interests_read on public.student_academic_interests for select to authenticated
  using (public.can_view_student(student_id));
create policy interests_insert on public.student_academic_interests for insert to authenticated
  with check (public.can_edit_student_plans(student_id) and set_by = (select auth.uid()));
create policy interests_update on public.student_academic_interests for update to authenticated
  using (public.can_edit_student_plans(student_id)) with check (public.can_edit_student_plans(student_id));
create policy interests_delete on public.student_academic_interests for delete to authenticated
  using (public.can_edit_student_plans(student_id));
comment on table public.student_academic_interests is
  'CR-13: how sure the student is about a major and up to 8 saved areas or majors ({kind, key, focus?}). Optional at every step.';
