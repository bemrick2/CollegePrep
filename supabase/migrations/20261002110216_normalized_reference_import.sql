-- Stable repository key; historical activity is not current operating status.
alter table public.institutions add column institution_key text unique,
  add column identity_academic_year text,
  add column active_as_of_academic_year boolean;
alter table public.institutions alter column active drop not null;
alter table public.institutions alter column active drop default;

create table public.federal_aid_programs (
  id uuid primary key default gen_random_uuid(),
  program_key text not null,
  academic_year text not null,
  policy_details jsonb not null,
  source_id uuid not null references public.sources(id),
  verification_status public.verification_status not null,
  last_verified_at timestamptz,
  unique(program_key,academic_year),
  check (verification_status<>'verified' or last_verified_at is not null)
);
alter table public.federal_aid_programs enable row level security;
revoke all on public.federal_aid_programs from anon,authenticated;
grant select on public.federal_aid_programs to anon,authenticated;
grant select,insert,update,delete on public.federal_aid_programs to service_role;
create policy verified_reference_read on public.federal_aid_programs for select to anon,authenticated using (verification_status='verified');
create policy internal_service_access on public.data_verification_runs for all to service_role using (true) with check (true);

-- Lossless payload/revision ledger is outside exposed API schemas.
create schema if not exists ingestion;
revoke all on schema ingestion from public,anon,authenticated;
grant usage on schema ingestion to service_role;
create table ingestion.reference_records (
  natural_key text primary key,
  domain text not null,
  academic_year text,
  source_file text not null,
  payload jsonb not null,
  imported_at timestamptz not null default now()
);
create table ingestion.reference_revisions (
  id uuid primary key default gen_random_uuid(),
  natural_key text not null,
  previous_payload jsonb not null,
  replaced_at timestamptz not null default now()
);
alter table ingestion.reference_records enable row level security;
alter table ingestion.reference_revisions enable row level security;
grant select,insert,update,delete on ingestion.reference_records,ingestion.reference_revisions to service_role;
create policy internal_service_access on ingestion.reference_records for all to service_role using (true) with check (true);
create policy internal_service_access on ingestion.reference_revisions for all to service_role using (true) with check (true);

-- Source URL exposed through invoker views while sources remain normalized.
create view public.institution_costs_with_provenance with (security_invoker=true) as
select c.*,s.canonical_url as source_url from public.institution_costs c join public.sources s on s.id=c.source_id;
create view public.admissions_metrics_with_provenance with (security_invoker=true) as
select c.*,s.canonical_url as source_url from public.admissions_metrics c join public.sources s on s.id=c.source_id;
grant select on public.institution_costs_with_provenance,public.admissions_metrics_with_provenance to anon,authenticated,service_role;

create index institution_costs_source_idx on public.institution_costs(source_id);
create index admissions_metrics_source_idx on public.admissions_metrics(source_id);
