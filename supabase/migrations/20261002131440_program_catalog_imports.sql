-- Stable program identities preserve separate annual catalogs and unknown flags.
alter table public.academic_programs add column program_key text;
alter table public.academic_programs alter column active drop not null;
alter table public.academic_programs alter column active drop default;
alter table public.academic_programs add constraint academic_programs_version_key
 unique(institution_id,program_key,academic_year);
alter table public.academic_programs add constraint academic_programs_import_provenance
 check (program_key is null or (btrim(program_key)<>'' and academic_year is not null and source_id is not null and last_verified_at is not null));
create index academic_programs_source_idx on public.academic_programs(source_id);
create index transfer_policies_source_idx on public.transfer_policies(source_id);
create index degree_requirements_source_idx on public.degree_requirements(source_id);
comment on column public.academic_programs.program_key is
 'Repository program identifier, stable across academic years and display-name revisions.';
