-- CR-9 and CR-7 (issue #37): institution level, household saved schools, and the list of schools
-- that have verified records for a year. See docs/HOUSEHOLD_PRACTICE.md and docs/frontend/CONTRACT_REQUESTS.md.

-- IPEDS HD ICLEVEL, imported with the identity record (data/national/ipeds/*/institutions.csv `level`).
-- Null when the identity has no IPEDS level (never inferred from a name).
alter table public.institutions add column level text
  check (level in ('four_year','two_year','less_than_two_year'));
comment on column public.institutions.level is
  'Highest level of offering from IPEDS HD ICLEVEL (four_year, two_year, less_than_two_year); null when not reported.';

-- Saved schools follow a household across devices. Writes go through the RPCs below (limit, existence, audit).
create table public.household_saved_schools (
  household_id uuid not null references public.households(id) on delete cascade,
  institution_key text not null references public.institutions(institution_key) on update cascade on delete cascade,
  added_by uuid references auth.users(id) on delete set null,
  added_at timestamptz not null default now(),
  primary key (household_id, institution_key)
);
alter table public.household_saved_schools enable row level security;
revoke all on public.household_saved_schools from anon, authenticated;
grant select, insert, update, delete on public.household_saved_schools to service_role;
grant select on public.household_saved_schools to authenticated;

-- Read: guardians with view_progress and the household's student members. Write: any guardian and student member.
create function public.can_view_household_schools(p_household uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select public.has_household_permission(p_household, 'view_progress')
    or exists (select 1 from public.household_members m
      where m.household_id = p_household and m.user_id = auth.uid() and m.role = 'student')
$$;

create policy saved_school_read on public.household_saved_schools for select to authenticated
  using (public.can_view_household_schools(household_id));

create function public.save_household_school(p_household uuid, p_institution_key text) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  if not exists (select 1 from public.institutions i where i.institution_key = p_institution_key) then
    raise exception 'Unknown institution %', p_institution_key using errcode = '22023';
  end if;
  -- Serialise concurrent saves for one household so the limit holds.
  perform 1 from public.households h where h.id = p_household for update;
  if exists (select 1 from public.household_saved_schools s where s.household_id = p_household and s.institution_key = p_institution_key) then
    return;
  end if;
  if (select count(*) from public.household_saved_schools s where s.household_id = p_household) >= 8 then
    raise exception 'A household can save up to 8 schools' using errcode = '22023';
  end if;
  insert into public.household_saved_schools(household_id, institution_key, added_by) values (p_household, p_institution_key, auth.uid());
end $$;

create function public.remove_household_school(p_household uuid, p_institution_key text) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  delete from public.household_saved_schools s where s.household_id = p_household and s.institution_key = p_institution_key;
end $$;

-- Schools with at least one verified record for exactly this academic year (no other year counts).
create function public.institutions_with_verified_records(p_academic_year text, p_state text default null)
returns table (institution_key text, display_name text, city text, state_code text, control text, level text, domains text[])
language plpgsql stable security invoker set search_path = '' as $$
begin
  if p_academic_year is null or p_academic_year !~ '^[0-9]{4}-[0-9]{2}$' then
    raise exception 'academic_year must look like 2026-27' using errcode = '22023';
  end if;
  if p_state is not null and p_state !~ '^[A-Z]{2}$' then
    raise exception 'state must be a two-letter code' using errcode = '22023';
  end if;
  return query
  with v as (
    select c.institution_id, 'costs' as d from public.institution_costs c where c.academic_year = p_academic_year and c.verification_status = 'verified'
    union select a.institution_id, 'admissions_metrics' from public.admissions_metrics a where a.academic_year = p_academic_year and a.verification_status = 'verified'
    union select w.institution_id, 'awards' from public.institutional_awards w where w.academic_year = p_academic_year and w.verification_status = 'verified'
    union select r.institution_id, 'credit_policies' from public.credit_policies r where r.academic_year = p_academic_year and r.verification_status = 'verified'
    union select t.institution_id, 'transfer_policies' from public.transfer_policies t where t.academic_year = p_academic_year and t.verification_status = 'verified'
    union select p.institution_id, 'academic_programs' from public.academic_programs p where p.academic_year = p_academic_year and p.verification_status = 'verified'
    union select ap.institution_id, 'appeals' from public.appeal_policies ap where ap.academic_year = p_academic_year and ap.verification_status = 'verified'
  )
  select i.institution_key, i.display_name, i.city, i.state_code::text, i.control, i.level, array_agg(distinct v.d order by v.d)
  from v join public.institutions i on i.id = v.institution_id
  where i.institution_key is not null and (p_state is null or i.state_code = p_state)
  group by i.institution_key, i.display_name, i.city, i.state_code, i.control, i.level
  order by i.display_name;
end $$;

-- Policies call the helper as the querying role, so authenticated keeps execute (like can_view_student).
revoke all on function public.can_view_household_schools(uuid) from public, anon;
grant execute on function public.can_view_household_schools(uuid) to authenticated, service_role;
do $$
declare f regprocedure;
begin
  foreach f in array array['public.save_household_school(uuid,text)'::regprocedure,
                           'public.remove_household_school(uuid,text)'::regprocedure] loop
    execute format('revoke all on function %s from public, anon', f);
    execute format('grant execute on function %s to authenticated, service_role', f);
  end loop;
end $$;
revoke all on function public.institutions_with_verified_records(text,text) from public;
grant execute on function public.institutions_with_verified_records(text,text) to anon, authenticated, service_role;
comment on function public.institutions_with_verified_records(text,text) is
  'Schools with at least one verified record for exactly p_academic_year, with the domains that have them.';
