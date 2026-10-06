-- CR-10 (issue #37): canonical exam keys on credit equivalencies, and a per-student exam plan.
-- The importer upserts the closed AP/CLEP catalog (backend/exam_keys.py) and sets exam_key from each row's
-- published exam name. A row whose name is not in the catalog keeps a null key; it is never guessed.

create table public.exam_catalog (
  exam_key text primary key check (exam_key ~ '^(ap|clep):[a-z0-9]+(-[a-z0-9]+)*$'),
  family text not null check (family in ('ap', 'clep')),
  display_name text not null,
  check (split_part(exam_key, ':', 1) = family)
);
alter table public.exam_catalog enable row level security;
revoke all on public.exam_catalog from anon, authenticated;
grant select on public.exam_catalog to anon, authenticated;
grant select, insert, update, delete on public.exam_catalog to service_role;
create policy exam_catalog_read on public.exam_catalog for select to anon, authenticated using (true);
comment on table public.exam_catalog is 'CR-10: canonical AP and CLEP exams. exam_key is the same across institutions.';

alter table public.credit_equivalencies add column exam_key text references public.exam_catalog(exam_key) on update cascade;
create index credit_equivalencies_exam_key on public.credit_equivalencies (exam_key) where exam_key is not null;
comment on column public.credit_equivalencies.exam_key is
  'Canonical exam (exam_catalog) matched from the published exam name; null when the name is not in the catalog.';

-- Read: the student and guardians with view_progress. Write: the household's guardians and the linked student.
create function public.can_edit_student_plans(p_student uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.students s where s.id = p_student
    and (s.linked_user_id = auth.uid() or (s.household_id is not null and public.is_household_guardian(s.household_id))))
$$;
revoke all on function public.can_edit_student_plans(uuid) from public, anon;
grant execute on function public.can_edit_student_plans(uuid) to authenticated, service_role;

create table public.student_exam_plan (
  student_id uuid not null references public.students(id) on delete cascade,
  exam_key text not null references public.exam_catalog(exam_key) on update cascade,
  score integer,  -- null = planned; AP 1-5, CLEP 20-80 (checked by trigger against the exam family)
  taken_on date check (taken_on between date '2000-01-01' and date '2100-12-31'),
  set_by uuid default auth.uid() references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (student_id, exam_key)
);

create function public.check_student_exam_plan() returns trigger
language plpgsql security definer set search_path = '' as $$
declare v_family text;
begin
  select c.family into v_family from public.exam_catalog c where c.exam_key = new.exam_key;
  if new.score is not null and not (
       (v_family = 'ap' and new.score between 1 and 5) or (v_family = 'clep' and new.score between 20 and 80)) then
    raise exception 'score is outside the % scale', v_family using errcode = '23514';
  end if;
  if tg_op = 'INSERT' then
    perform 1 from public.students s where s.id = new.student_id for update;
    if (select count(*) from public.student_exam_plan p where p.student_id = new.student_id) >= 20 then
      raise exception 'A student''s exam plan holds up to 20 exams' using errcode = '22023';
    end if;
  else
    new.updated_at := now();
    new.set_by := coalesce(auth.uid(), old.set_by);
  end if;
  return new;
end $$;
revoke all on function public.check_student_exam_plan() from public, anon, authenticated;
create trigger student_exam_plan_check before insert or update on public.student_exam_plan
  for each row execute function public.check_student_exam_plan();

alter table public.student_exam_plan enable row level security;
revoke all on public.student_exam_plan from anon, authenticated;
grant select, insert, update, delete on public.student_exam_plan to service_role;
grant select, insert (student_id, exam_key, score, taken_on), update (score, taken_on), delete
  on public.student_exam_plan to authenticated;
create policy exam_plan_read on public.student_exam_plan for select to authenticated
  using (public.can_view_student(student_id));
create policy exam_plan_insert on public.student_exam_plan for insert to authenticated
  with check (public.can_edit_student_plans(student_id) and set_by = (select auth.uid()));
create policy exam_plan_update on public.student_exam_plan for update to authenticated
  using (public.can_edit_student_plans(student_id)) with check (public.can_edit_student_plans(student_id));
create policy exam_plan_delete on public.student_exam_plan for delete to authenticated
  using (public.can_edit_student_plans(student_id));
comment on table public.student_exam_plan is
  'CR-10: AP/CLEP exams a student plans or has taken (score null = planned). Up to 20 per student.';
