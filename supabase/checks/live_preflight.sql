-- Fails before any live import if the target database lacks the schema the importer needs.
do $preflight$
begin
 if not exists(select 1 from information_schema.schemata where schema_name='ingestion') then
  raise exception 'Preflight: ingestion ledger schema is missing; apply repository migrations first';
 end if;
 if not exists(select 1 from information_schema.columns where table_schema='public' and table_name='academic_programs' and column_name='program_key') then
  raise exception 'Preflight: migration 20261002131440_program_catalog_imports is not applied';
 end if;
 if not exists(select 1 from information_schema.columns where table_schema='public' and table_name='transfer_policies' and column_name='policy_details')
  or not exists(select 1 from pg_constraint where conname='degree_requirements_requirement_kind_check' and pg_get_constraintdef(oid) like '%program_plan%') then
  raise exception 'Preflight: migration 20261002134049_degree_transfer_import_domains is not applied';
 end if;
 if not exists(select 1 from pg_proc where proname='compare_institutions') then
  raise exception 'Preflight: migration 20261002132345_school_comparison_api is not applied';
 end if;
 if not exists(select 1 from information_schema.columns where table_schema='public' and table_name='credit_equivalencies' and column_name='is_current') then
  raise exception 'Preflight: reviewed_policy_domains migration is not applied';
 end if;
end $preflight$;
