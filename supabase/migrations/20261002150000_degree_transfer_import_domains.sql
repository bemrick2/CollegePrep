-- Builds on 20261002130818_program_catalog_imports.sql.
-- Controlled vocabularies for newly researched credit-policy, appeal and requirement
-- kinds, transfer-policy detail storage, and provenance views.
-- Keep these lists identical to backend/catalog.py CONTROLLED_VALUES.

-- Credit policy kinds: add Cambridge International AS/A Level, Tennessee Statewide
-- Dual Credit challenge exams and state industry-certification exams.
alter table public.credit_policies drop constraint credit_policies_policy_kind_check;
alter table public.credit_policies add constraint credit_policies_policy_kind_check check (policy_kind in (
  'AP','CLEP','IB','dual_enrollment','A_level','DSST','other',
  'cambridge_international','statewide_dual_credit','industry_certification'));

-- Appeal kinds: retention/SAP/dependency/budget routes are stored explicitly so they
-- are never mislabeled as qualifying paid-add-on paths. The documented_paid_path
-- constraint and the year-scoped gate still accept only the three qualifying kinds.
alter table public.appeal_policies drop constraint appeal_policies_appeal_kind_check;
alter table public.appeal_policies add constraint appeal_policies_appeal_kind_check check (appeal_kind in (
  'need_based_special_circumstances','professional_judgment','merit_reconsideration',
  'competing_offer_review','financial_aid_appeal','other',
  'scholarship_retention_appeal','budget_increase','dependency_override','sap_appeal'));

-- A whole-program catalog plan (term sequence, grade and progression rules) is one
-- requirement row whose rule_details holds the reviewed plan.
alter table public.degree_requirements drop constraint degree_requirements_requirement_kind_check;
alter table public.degree_requirements add constraint degree_requirements_requirement_kind_check check (requirement_kind in (
  'total_credits','general_education','major','minor','residency','gpa','other','program_plan'));
create index degree_requirements_program_idx on public.degree_requirements(program_id);

-- Transfer policies: keep the reviewed summary and full payload (residence rules,
-- conflicts, additional sources) alongside the scalar limits.
alter table public.transfer_policies add column summary text,
  add column policy_details jsonb not null default '{}'::jsonb;

-- Provenance views (invoker rights, so verified-only RLS still applies).
create view public.degree_requirements_with_provenance with (security_invoker=true) as
select d.*, p.institution_id, p.program_key, p.program_name, p.credential_level, s.canonical_url as source_url
from public.degree_requirements d
join public.academic_programs p on p.id=d.program_id
join public.sources s on s.id=d.source_id;
create view public.transfer_policies_with_provenance with (security_invoker=true) as
select t.*, s.canonical_url as source_url from public.transfer_policies t join public.sources s on s.id=t.source_id;
grant select on public.degree_requirements_with_provenance, public.transfer_policies_with_provenance to anon, authenticated, service_role;
