-- Synthetic reference fixtures and all assertions are rolled back.
begin;
insert into public.sources(id,canonical_url,authority) values
 ('10000000-0000-0000-0000-000000000001','https://example.edu/comparison-test','institution');
insert into public.institutions(id,institution_key,ipeds_name,display_name,state_code,source_id,verification_status,last_verified_at,identity_academic_year)
values ('10000000-0000-0000-0000-000000000002','comparison-test','Fixture','Fixture','TN','10000000-0000-0000-0000-000000000001','verified',current_date,'2023-24'),
 ('10000000-0000-0000-0000-000000000003','comparison-unverified','Hidden','Hidden','TN','10000000-0000-0000-0000-000000000001','unverified',current_date,'2023-24');
insert into public.institution_costs(institution_id,academic_year,residency,tuition,source_id,verification_status,last_verified_at) values
 ('10000000-0000-0000-0000-000000000002','2023-24','in_state',1000,'10000000-0000-0000-0000-000000000001','verified',current_date),
 ('10000000-0000-0000-0000-000000000002','2026-27','in_state',2000,'10000000-0000-0000-0000-000000000001','unverified',current_date);
insert into public.appeal_policies(institution_id,academic_year,appeal_kind,offered,policy_url,source_id,verification_status,last_verified_at,qualifies_for_paid_addon,qualifying_path_evidence) values
 ('10000000-0000-0000-0000-000000000002','2026-27','merit_reconsideration',true,'https://example.edu/comparison-test','10000000-0000-0000-0000-000000000001','verified',current_date,true,'Explicit documented merit reconsideration fixture');
insert into public.academic_programs(id,institution_id,program_key,program_name,academic_year,source_id,verification_status,last_verified_at) values
 ('10000000-0000-0000-0000-000000000004','10000000-0000-0000-0000-000000000002','biology','Biology','2026-27','10000000-0000-0000-0000-000000000001','verified',current_date);
insert into public.degree_requirements(program_id,academic_year,requirement_key,requirement_kind,minimum_credits,source_id,verification_status,last_verified_at) values
 ('10000000-0000-0000-0000-000000000004','2026-27','major','major',40,'10000000-0000-0000-0000-000000000001','verified',current_date);
insert into public.credit_policies(id,institution_id,policy_kind,academic_year,policy_url,source_id,verification_status,last_verified_at) values
 ('10000000-0000-0000-0000-000000000005','10000000-0000-0000-0000-000000000002','AP','2026-27','https://example.edu/comparison-test','10000000-0000-0000-0000-000000000001','verified',current_date);
insert into public.credit_equivalencies(credit_policy_id,exam_or_course_code,minimum_score,credits_awarded) values
 ('10000000-0000-0000-0000-000000000005','BIO','4',4);

set local role anon;
do $test$
declare r jsonb; old jsonb; school jsonb;
begin
 r=public.compare_institutions(array['comparison-test','unknown','comparison-unverified'],'2026-27');
 school=r->'institutions'->0;
 if not (school->>'found')::boolean then raise exception 'Verified identity missing'; end if;
 if jsonb_array_length(school->'domains'->'costs')<>0 or not (school->'missing_domains' ? 'costs') then raise exception 'Historical or unverified costs leaked'; end if;
 if not (school->>'can_offer_paid_addon')::boolean then raise exception 'Documented matching-year appeal denied'; end if;
 if school->'domains'->'degree_requirements'->0->>'program_key'<>'biology' then raise exception 'Program dependency missing'; end if;
 if school->'domains'->'degree_requirements'->0->>'source_url'<>'https://example.edu/comparison-test' then raise exception 'Source provenance lost'; end if;
 if school->'domains'->'credit_policies'->0->'equivalencies'->0->>'exam_or_course_code'<>'BIO' then raise exception 'Equivalencies lost'; end if;
 if (r->'institutions'->1->>'found')::boolean or (r->'institutions'->2->>'found')::boolean then raise exception 'Unknown or unverified identity leaked'; end if;
 old=public.compare_institutions(array['comparison-test'],'2023-24')->'institutions'->0;
 if (old->>'can_offer_paid_addon')::boolean or old->'domains'->'costs'->0->>'tuition'<>'1000' then raise exception 'Annual isolation failed'; end if;
 if (select prosecdef from pg_proc where oid='public.compare_institutions(text[],text)'::regprocedure) then raise exception 'RPC bypasses caller permissions'; end if;
 begin
  perform public.compare_institutions(array['comparison-test'],null);
  raise exception 'Missing year accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.compare_institutions(array['comparison-test','comparison-test'],'2026-27');
  raise exception 'Duplicate keys accepted';
 exception when invalid_parameter_value then null; end;
 begin
  perform public.compare_institutions(array(select n::text from generate_series(1,21) n),'2026-27');
  raise exception 'Unbounded request accepted';
 exception when invalid_parameter_value then null; end;
end $test$;
reset role;
set local role authenticated;
do $test$ begin
 if not (public.compare_institutions(array['comparison-test'],'2026-27')->'institutions'->0->>'found')::boolean then raise exception 'Authenticated read failed'; end if;
 if has_schema_privilege(current_user,'ingestion','usage') or has_table_privilege(current_user,'public.academic_programs','insert') then raise exception 'Client can modify reference data'; end if;
end $test$;
reset role;
rollback;
