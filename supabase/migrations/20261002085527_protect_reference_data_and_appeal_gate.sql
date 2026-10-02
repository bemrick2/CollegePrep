-- Prepared against official RLS/Data API documentation. Requires PG15+.
-- Not applied to an unrelated connected project; deployment must be tested.
alter table public.appeal_policies
  add column qualifies_for_paid_addon boolean not null default false,
  add column qualifying_path_evidence text,
  add constraint documented_paid_path check (
    not qualifies_for_paid_addon or (
      offered and appeal_kind in ('merit_reconsideration','competing_offer_review','financial_aid_appeal')
      and source_id is not null and policy_url is not null and policy_url like 'https://%'
      and academic_year is not null
      and nullif(trim(qualifying_path_evidence),'') is not null
    )
  );

-- Compatibility gate fails closed: callers must select an explicit academic year.
create or replace view public.institution_negotiation_addon_eligibility
with (security_invoker = true) as
select institution_id, false as can_offer_negotiation_addon
from public.appeal_policies group by institution_id;

create view public.institution_negotiation_addon_eligibility_by_year
with (security_invoker = true) as
select a.institution_id, a.academic_year,
  coalesce(bool_or(a.offered and a.verification_status='verified'
    and a.qualifies_for_paid_addon
    and a.appeal_kind in ('merit_reconsideration','competing_offer_review','financial_aid_appeal')
    and a.academic_year is not null
    and a.last_verified_at::date between current_date-365 and current_date
    and nullif(trim(a.qualifying_path_evidence),'') is not null
    and a.policy_url like 'https://%' and s.canonical_url like 'https://%'
  ),false) as can_offer_negotiation_addon
from public.appeal_policies a join public.sources s on s.id=a.source_id
group by a.institution_id,a.academic_year;
comment on view public.institution_negotiation_addon_eligibility_by_year is
'Require an explicit academic year. Missing row means false. Generic retention/PJ appeals do not qualify without separately reviewed evidence.';

alter table public.admissions_metrics add column academic_year text,
  add column sat_reading_25 integer, add column sat_reading_75 integer,
  add column sat_math_25 integer, add column sat_math_75 integer;
-- Existing entering-year data are not assigned an academic year by inference.
alter table public.institution_costs add column student_population text,
  add column on_campus_food_housing numeric,
  add column on_campus_other_expenses numeric;
alter table public.academic_programs add column academic_year text;

create table public.degree_requirements (
  id uuid primary key default gen_random_uuid(),
  program_id uuid not null references public.academic_programs(id),
  academic_year text not null,
  requirement_key text not null,
  requirement_kind text not null check (requirement_kind in ('total_credits','general_education','major','minor','residency','gpa','other')),
  minimum_credits numeric check (minimum_credits>=0),
  minimum_gpa numeric,
  rule_details jsonb not null default '{}'::jsonb,
  source_id uuid not null references public.sources(id),
  verification_status public.verification_status not null default 'unverified',
  last_verified_at timestamptz,
  check (verification_status<>'verified' or last_verified_at is not null),
  unique(program_id,academic_year,requirement_key)
);

-- Explicit grants are required under current Supabase Data API defaults.
-- Reference data are publicly readable when verified; clients never edit them.
do $$
declare t text;
begin
  foreach t in array array['institutions','institution_costs','admissions_metrics',
    'academic_programs','state_aid_programs','institutional_awards','credit_policies',
    'transfer_policies','appeal_policies','practice_blueprints','degree_requirements'] loop
    execute format('alter table public.%I enable row level security',t);
    execute format('revoke all on public.%I from anon, authenticated',t);
    execute format('grant select on public.%I to anon, authenticated',t);
    execute format('grant select,insert,update,delete on public.%I to service_role',t);
    execute format('create policy verified_reference_read on public.%I for select to anon, authenticated using (verification_status = ''verified'')',t);
  end loop;
end $$;
alter table public.credit_equivalencies enable row level security;
revoke all on public.credit_equivalencies from anon,authenticated;
grant select on public.credit_equivalencies to anon,authenticated;
grant select,insert,update,delete on public.credit_equivalencies to service_role;
create policy verified_parent_read on public.credit_equivalencies for select to anon,authenticated
using (exists (select 1 from public.credit_policies p where p.id=credit_policy_id and p.verification_status='verified'));

alter table public.sources enable row level security;
revoke all on public.sources from anon,authenticated;
grant select on public.sources to anon,authenticated;
grant select,insert,update,delete on public.sources to service_role;
create policy official_source_read on public.sources for select to anon,authenticated using (authority<>'secondary');

alter table public.data_verification_runs enable row level security;
revoke all on public.data_verification_runs from anon,authenticated;
grant select,insert,update,delete on public.data_verification_runs to service_role;
revoke all on public.institution_negotiation_addon_eligibility from anon,authenticated;
grant select on public.institution_negotiation_addon_eligibility_by_year to anon,authenticated,service_role;
