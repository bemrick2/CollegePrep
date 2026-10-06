-- CR-14: structured program admission, internal transfer and classification fields; per-year program
-- catalog coverage (completeness and undeclared policy); structured award-to-program links.
-- Every field is nullable and null means "not verified". Nothing is filled by inference.
-- Field-level evidence lives with the field (quote + official https source) because program admission
-- rules are usually published on a different page than the catalog program page.

alter table public.academic_programs
  add column college text,
  add column cip_source_url text,
  add column admission_type text,
  add column admission_details jsonb,
  add column internal_transfer jsonb;

alter table public.academic_programs
  add constraint academic_programs_cip_format check (cip_code is null or cip_code ~ '^[0-9]{2}\.[0-9]{4}$'),
  add constraint academic_programs_cip_source check (cip_code is null or cip_source_url is null or cip_source_url like 'https://%'),
  add constraint academic_programs_admission_type check (admission_type is null or admission_type in ('direct','pre_major','open')),
  add constraint academic_programs_admission_evidence check (admission_type is null or (
    jsonb_typeof(admission_details)='object' and coalesce(btrim(admission_details->>'quote'),'')<>''
    and admission_details->>'source_url' like 'https://%')),
  add constraint academic_programs_internal_transfer_evidence check (internal_transfer is null or (
    jsonb_typeof(internal_transfer->'restricted')='boolean' and coalesce(btrim(internal_transfer->>'quote'),'')<>''
    and internal_transfer->>'source_url' like 'https://%'));

comment on column public.academic_programs.admission_type is
 'direct: first-year students are admitted to the major; pre_major: students start outside the major and must apply or meet published criteria to enter it; open: the institution states students may declare the major without a separate admission. Null: not verified.';
comment on column public.academic_programs.admission_details is
 '{quote, source_url, criteria_text?, gpa_min?, notes?}: the verbatim official statement that sets admission_type.';
comment on column public.academic_programs.internal_transfer is
 '{restricted boolean, quote, source_url, criteria_text?, gpa_min?}: whether enrolled students changing into the major face published limits.';

-- One row per institution and catalog year: what the verified program list covers.
create table public.program_catalogs (
  id uuid primary key default gen_random_uuid(),
  institution_id uuid not null references public.institutions(id) on delete cascade,
  academic_year text not null,
  catalog_url text not null check (catalog_url like 'https://%'),
  catalog_year_label text,
  listed_bachelor_programs integer check (listed_bachelor_programs is null or listed_bachelor_programs >= 0),
  programs_complete boolean,
  completeness_basis text,
  undeclared_policy jsonb,
  source_id uuid not null references public.sources(id),
  verification_status verification_status not null default 'unverified',
  last_verified_at timestamptz,
  notes text,
  unique (institution_id, academic_year),
  constraint program_catalogs_complete_basis check (programs_complete is not true or (
    listed_bachelor_programs is not null and coalesce(btrim(completeness_basis),'')<>'')),
  constraint program_catalogs_undeclared_evidence check (undeclared_policy is null or (
    jsonb_typeof(undeclared_policy->'allowed')='boolean' and coalesce(btrim(undeclared_policy->>'quote'),'')<>''
    and undeclared_policy->>'source_url' like 'https://%'))
);
create index program_catalogs_source_idx on public.program_catalogs(source_id);
comment on table public.program_catalogs is
 'Per institution and academic year: the official catalog program list behind the verified academic_programs rows. programs_complete=true only when every bachelor program on that official list has a verified academic_programs row for the year, so "not offered" may be said; otherwise the UI must say "not in our verified list".';

alter table public.program_catalogs enable row level security;
revoke all on public.program_catalogs from anon, authenticated;
grant select on public.program_catalogs to anon, authenticated;
grant select, insert, update, delete on public.program_catalogs to service_role;
create policy verified_reference_read on public.program_catalogs for select to anon, authenticated
  using (verification_status = 'verified');

-- Major-specific scholarships: structured links, set only when the institution ties the award to the program/field.
alter table public.institutional_awards
  add column program_keys text[],
  add column cip_codes text[];
alter table public.institutional_awards
  add constraint institutional_awards_cip_codes_format check (cip_codes is null or
    array_to_string(cip_codes, ',') ~ '^[0-9]{2}(\.[0-9]{2}([0-9]{2})?)?(,[0-9]{2}(\.[0-9]{2}([0-9]{2})?)?)*$');

-- Read API: program catalog coverage for 1-20 schools in one exact academic year (verified rows only).
create function public.program_catalog_status(p_institution_keys text[], p_academic_year text)
returns jsonb language sql stable security invoker set search_path='' as $function$
 select jsonb_build_object('academic_year', p_academic_year, 'institutions', coalesce(jsonb_agg(jsonb_build_object(
   'institution_key', k.key,
   'catalog', (select to_jsonb(c)-'id'-'institution_id'-'source_id'||jsonb_build_object('source_url', s.canonical_url)
               from public.program_catalogs c join public.institutions i on i.id=c.institution_id
               join public.sources s on s.id=c.source_id
               where i.institution_key=k.key and c.academic_year=p_academic_year and c.verification_status='verified'
               and s.authority<>'secondary'),
   'verified_programs', (select count(*) from public.academic_programs p join public.institutions i on i.id=p.institution_id
               where i.institution_key=k.key and p.academic_year=p_academic_year and p.verification_status='verified')
  ) order by k.ord), '[]'::jsonb))
 from unnest(p_institution_keys) with ordinality k(key, ord)
 where p_academic_year is not null and cardinality(p_institution_keys) between 1 and 20;
$function$;
revoke all on function public.program_catalog_status(text[], text) from public;
grant execute on function public.program_catalog_status(text[], text) to anon, authenticated, service_role;
comment on function public.program_catalog_status(text[], text) is
 'CR-14 item 7: per-school program catalog coverage (complete flag, listed bachelor count, undeclared policy) for one exact academic year. Missing catalog = not assessed.';
