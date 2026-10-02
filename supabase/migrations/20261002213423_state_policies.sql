-- State-level policies that apply across institutions: tuition residency classification,
-- statewide articulation / transfer pathways, transfer admission guarantees, dual admission.
-- Same conventions as state_aid_programs: official source, academic year, verification status,
-- verified-only public reads, no client writes. The complete reviewed payload is kept in
-- policy_details (and in the private ingestion ledger).
create table public.state_policies (
  id uuid primary key default gen_random_uuid(),
  state_code char(2) not null,
  policy_kind text not null check (policy_kind in ('tuition_residency','statewide_articulation','transfer_pathway',
    'transfer_guarantee','dual_admission','other')),
  policy_key text not null check (policy_key ~ '^[a-z0-9][a-z0-9-]*$'),
  academic_year text not null,
  title text not null,
  summary text,
  policy_details jsonb not null default '{}'::jsonb,
  official_url text not null,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique (state_code, policy_kind, policy_key, academic_year)
);
create index state_policies_state_idx on public.state_policies(state_code, policy_kind);
create index state_policies_source_idx on public.state_policies(source_id);

alter table public.state_policies enable row level security;
revoke all on public.state_policies from anon, authenticated;
grant select on public.state_policies to anon, authenticated;
grant select, insert, update, delete on public.state_policies to service_role;
create policy verified_reference_read on public.state_policies for select to anon, authenticated
  using (verification_status = 'verified');
