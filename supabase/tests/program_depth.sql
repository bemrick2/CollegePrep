-- CR-14 program-depth fields. Synthetic fixtures; everything is rolled back.
begin;
insert into public.sources(id,canonical_url,authority) values
 ('20000000-0000-0000-0000-000000000001','https://example.edu/program-depth-test','institution');
insert into public.institutions(id,institution_key,ipeds_name,display_name,state_code,source_id,verification_status,last_verified_at,identity_academic_year)
values ('20000000-0000-0000-0000-000000000002','program-depth-test','Fixture','Fixture','TN','20000000-0000-0000-0000-000000000001','verified',current_date,'2023-24');
insert into public.academic_programs(institution_id,program_key,program_name,academic_year,source_id,verification_status,last_verified_at,
  cip_code,cip_source_url,admission_type,admission_details,internal_transfer) values
 ('20000000-0000-0000-0000-000000000002','mechanical-engineering-bs','Mechanical Engineering, BS','2026-27','20000000-0000-0000-0000-000000000001','verified',current_date,
  '14.1901','https://example.edu/inventory','direct',
  '{"quote":"First-year students who meet the criteria are admitted directly to the college.","source_url":"https://example.edu/admit","gpa_min":3.0}',
  '{"restricted":true,"quote":"Changing into the major requires a 2.8 GPA.","source_url":"https://example.edu/change","gpa_min":2.8}'),
 ('20000000-0000-0000-0000-000000000002','history-ba','History, BA','2026-27','20000000-0000-0000-0000-000000000001','verified',current_date,
  null,null,null,null,null);
insert into public.program_catalogs(institution_id,academic_year,catalog_url,listed_bachelor_programs,programs_complete,completeness_basis,undeclared_policy,source_id,verification_status,last_verified_at)
values ('20000000-0000-0000-0000-000000000002','2026-27','https://example.edu/catalog',2,true,'Every program on the 2026-2027 Programs A-Z list has a verified record.',
  '{"allowed":true,"quote":"Students may begin as Exploratory.","source_url":"https://example.edu/exploratory"}',
  '20000000-0000-0000-0000-000000000001','verified',current_date),
 ('20000000-0000-0000-0000-000000000002','2025-26','https://example.edu/catalog-old',null,null,null,null,'20000000-0000-0000-0000-000000000001','unverified',current_date);

-- Constraints: a field without its evidence, or an unsupported value, is refused.
do $test$ begin
 begin
  insert into public.academic_programs(institution_id,program_key,program_name,academic_year,source_id,verification_status,admission_type)
  values ('20000000-0000-0000-0000-000000000002','x1','X','2026-27','20000000-0000-0000-0000-000000000001','verified','direct');
  raise exception 'admission_type without evidence accepted';
 exception when check_violation then null; end;
 begin
  insert into public.academic_programs(institution_id,program_key,program_name,academic_year,source_id,verification_status,admission_type,admission_details)
  values ('20000000-0000-0000-0000-000000000002','x2','X','2026-27','20000000-0000-0000-0000-000000000001','verified','competitive','{"quote":"q","source_url":"https://e.edu"}');
  raise exception 'unknown admission_type accepted';
 exception when check_violation then null; end;
 begin
  insert into public.academic_programs(institution_id,program_key,program_name,academic_year,source_id,verification_status,cip_code)
  values ('20000000-0000-0000-0000-000000000002','x3','X','2026-27','20000000-0000-0000-0000-000000000001','verified','14');
  raise exception 'malformed CIP accepted';
 exception when check_violation then null; end;
 begin
  insert into public.academic_programs(institution_id,program_key,program_name,academic_year,source_id,verification_status,internal_transfer)
  values ('20000000-0000-0000-0000-000000000002','x4','X','2026-27','20000000-0000-0000-0000-000000000001','verified','{"restricted":"yes","quote":"q","source_url":"https://e.edu"}');
  raise exception 'non-boolean internal_transfer.restricted accepted';
 exception when check_violation then null; end;
 begin
  insert into public.program_catalogs(institution_id,academic_year,catalog_url,programs_complete,source_id)
  values ('20000000-0000-0000-0000-000000000002','2024-25','https://example.edu/c',true,'20000000-0000-0000-0000-000000000001');
  raise exception 'programs_complete without count and basis accepted';
 exception when check_violation then null; end;
 begin
  insert into public.institutional_awards(institution_id,award_name,award_type,academic_year,source_id,cip_codes)
  values ('20000000-0000-0000-0000-000000000002','Bad','merit','2026-27','20000000-0000-0000-0000-000000000001',array['engineering']);
  raise exception 'malformed award CIP accepted';
 exception when check_violation then null; end;
end $test$;

set local role anon;
do $test$
declare r jsonb; school jsonb; cmp jsonb;
begin
 r=public.program_catalog_status(array['program-depth-test','unknown'],'2026-27');
 school=r->'institutions'->0;
 if not (school->'catalog'->>'programs_complete')::boolean then raise exception 'Verified completeness missing'; end if;
 if school->'catalog'->>'source_url'<>'https://example.edu/program-depth-test' then raise exception 'Catalog provenance lost'; end if;
 if school->'catalog'->'undeclared_policy'->>'quote' is null then raise exception 'Undeclared evidence lost'; end if;
 if (school->>'verified_programs')::int<>2 then raise exception 'Verified program count wrong'; end if;
 if r->'institutions'->1->'catalog'<>'null'::jsonb then raise exception 'Unknown school invented a catalog'; end if;
 if public.program_catalog_status(array['program-depth-test'],'2025-26')->'institutions'->0->'catalog'<>'null'::jsonb then raise exception 'Unverified catalog exposed'; end if;
 -- CR-14 fields reach the comparison RPC with their evidence
 cmp=public.compare_institutions(array['program-depth-test'],'2026-27')->'institutions'->0->'domains'->'academic_programs';
 if not exists(select 1 from jsonb_array_elements(cmp) p where p->>'admission_type'='direct' and p->'admission_details'->>'source_url'='https://example.edu/admit'
   and p->>'cip_code'='14.1901' and (p->'internal_transfer'->>'restricted')::boolean) then raise exception 'CR-14 fields missing from comparison'; end if;
 if exists(select 1 from jsonb_array_elements(cmp) p where p->>'program_key'='history-ba' and (p->>'admission_type' is not null or p->>'cip_code' is not null)) then
  raise exception 'Unknown fields were filled'; end if;
 begin
  insert into public.program_catalogs(institution_id,academic_year,catalog_url,source_id) values ('20000000-0000-0000-0000-000000000002','2023-24','https://e.edu','20000000-0000-0000-0000-000000000001');
  raise exception 'Anonymous write accepted';
 exception when insufficient_privilege then null; end;
 if (select prosecdef from pg_proc where oid='public.program_catalog_status(text[],text)'::regprocedure) then raise exception 'RPC bypasses caller permissions'; end if;
end $test$;
rollback;
