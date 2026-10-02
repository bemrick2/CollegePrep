-- CollegePrep initial normalized schema
-- Created 2026-10-01
-- Designed for Supabase/Postgres.

create extension if not exists pgcrypto;

create type public.verification_status as enum (
  'verified',
  'partially_verified',
  'unverified',
  'stale',
  'not_applicable'
);

create type public.source_authority as enum (
  'federal',
  'state',
  'institution',
  'accreditor',
  'system',
  'other_official',
  'secondary'
);

create table public.sources (
  id uuid primary key default gen_random_uuid(),
  canonical_url text not null unique,
  title text,
  publisher text,
  authority source_authority not null,
  retrieved_at timestamptz not null default now(),
  effective_date date,
  academic_year text,
  notes text
);

create table public.institutions (
  id uuid primary key default gen_random_uuid(),
  unitid integer unique,
  opeid text,
  ipeds_name text not null,
  display_name text not null,
  state_code char(2) not null,
  city text,
  institution_type text,
  control text,
  carnegie_classification text,
  website_url text,
  admissions_url text,
  financial_aid_url text,
  net_price_calculator_url text,
  active boolean not null default true,
  source_id uuid references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index institutions_state_idx on public.institutions(state_code);

create table public.institution_costs (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  academic_year text not null,
  residency text not null check (residency in ('in_state','out_of_state','district','international','not_applicable')),
  tuition numeric,
  mandatory_fees numeric,
  room numeric,
  board numeric,
  books_supplies numeric,
  transportation numeric,
  personal_misc numeric,
  total_cost_of_attendance numeric,
  currency char(3) not null default 'USD',
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(institution_id, academic_year, residency)
);

create table public.admissions_metrics (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  entering_fall_year integer not null,
  applicant_population text not null default 'first_time_first_year',
  applications integer,
  admits integer,
  enrolled integer,
  admit_rate numeric,
  sat_25 integer,
  sat_75 integer,
  act_25 numeric,
  act_75 numeric,
  average_gpa numeric,
  test_policy text,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(institution_id, entering_fall_year, applicant_population)
);

create table public.academic_programs (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  cip_code text,
  program_name text not null,
  credential_level text,
  delivery_mode text,
  catalog_year text,
  total_credits numeric,
  program_url text,
  source_id uuid references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  active boolean not null default true
);
create index academic_programs_inst_idx on public.academic_programs(institution_id);

create table public.state_aid_programs (
  id uuid primary key default gen_random_uuid(),
  state_code char(2) not null,
  program_name text not null,
  program_type text not null,
  academic_year text,
  eligibility_summary text not null,
  residency_requirement text,
  gpa_requirement text,
  test_requirement text,
  income_requirement text,
  award_amount_text text,
  award_min numeric,
  award_max numeric,
  renewable boolean,
  renewal_requirements text,
  application_method text,
  priority_deadline date,
  final_deadline date,
  official_url text not null,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(state_code, program_name, academic_year)
);
create index state_aid_programs_state_idx on public.state_aid_programs(state_code);

create table public.institutional_awards (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  award_name text not null,
  academic_year text,
  award_type text not null,
  automatic_consideration boolean,
  separate_application boolean,
  eligibility_summary text,
  gpa_requirement text,
  test_requirement text,
  residency_requirement text,
  major_requirement text,
  award_amount_text text,
  award_min numeric,
  award_max numeric,
  full_tuition boolean not null default false,
  full_ride boolean not null default false,
  renewable boolean,
  renewal_requirements text,
  deadline date,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(institution_id, award_name, academic_year)
);

create table public.credit_policies (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  policy_kind text not null check (policy_kind in ('AP','CLEP','IB','dual_enrollment','A_level','DSST','other')),
  academic_year text,
  policy_url text not null,
  general_limit_credits numeric,
  residency_credit_requirement numeric,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(institution_id, policy_kind, academic_year)
);

create table public.credit_equivalencies (
  id uuid primary key default gen_random_uuid(),
  credit_policy_id uuid not null references public.credit_policies(id) on delete cascade,
  exam_or_course_code text not null,
  exam_or_course_name text,
  minimum_score text,
  institution_course_equivalent text,
  credits_awarded numeric,
  applies_to_gen_ed boolean,
  applies_to_major boolean,
  notes text,
  unique(credit_policy_id, exam_or_course_code, minimum_score, institution_course_equivalent)
);

create table public.transfer_policies (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  academic_year text,
  policy_url text not null,
  min_grade text,
  max_transfer_credits numeric,
  max_transfer_percent numeric,
  residency_requirement_credits numeric,
  articulation_url text,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(institution_id, academic_year)
);

create table public.appeal_policies (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  academic_year text,
  appeal_kind text not null check (appeal_kind in (
    'need_based_special_circumstances',
    'professional_judgment',
    'merit_reconsideration',
    'competing_offer_review',
    'financial_aid_appeal',
    'other'
  )),
  offered boolean not null,
  policy_url text,
  process_summary text,
  required_documents text,
  deadline_text text,
  contact_method text,
  source_id uuid references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique(institution_id, academic_year, appeal_kind)
);

-- Product gate: never sell/show negotiation add-on unless at least one
-- relevant documented institution appeal/reconsideration path is verified.
create view public.institution_negotiation_addon_eligibility as
select
  institution_id,
  bool_or(
    offered
    and verification_status = 'verified'
    and appeal_kind in ('merit_reconsideration','competing_offer_review','financial_aid_appeal')
  ) as can_offer_negotiation_addon
from public.appeal_policies
group by institution_id;

create table public.practice_blueprints (
  id uuid primary key default gen_random_uuid(),
  exam_family text not null,
  subject text not null,
  domain text not null,
  skill text not null,
  difficulty text,
  source_framework text,
  source_id uuid references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz
);

create table public.data_verification_runs (
  id uuid primary key default gen_random_uuid(),
  started_at timestamptz not null default now(),
  finished_at timestamptz,
  scope text not null,
  records_checked integer not null default 0,
  records_verified integer not null default 0,
  records_flagged integer not null default 0,
  notes text
);

comment on view public.institution_negotiation_addon_eligibility is
'Authoritative product gate for whether the negotiation/appeal add-on may be offered.';
