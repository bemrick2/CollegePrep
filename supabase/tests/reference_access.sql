-- Disposable fixtures only; never counted as school coverage.
begin;
do $$ begin
 if has_schema_privilege('anon','ingestion','USAGE') then raise exception 'Private ingestion schema exposed'; end if;
end $$;
insert into public.sources(id,canonical_url,authority) values
('00000000-0000-0000-0000-000000000001','https://example.edu/appeal','institution');
insert into public.institutions(id,ipeds_name,display_name,state_code,verification_status) values
('00000000-0000-0000-0000-000000000002','Test College','Test College','TN','verified'),
('00000000-0000-0000-0000-000000000003','Unverified College','Unverified College','TN','unverified');
insert into public.appeal_policies(institution_id,academic_year,appeal_kind,offered,source_id,policy_url,verification_status,last_verified_at)
values ('00000000-0000-0000-0000-000000000002','2026-27','financial_aid_appeal',true,
'00000000-0000-0000-0000-000000000001','https://example.edu/appeal','verified',current_date);
insert into public.institutional_awards(institution_id,award_name,award_type,academic_year,source_id)
values ('00000000-0000-0000-0000-000000000002','Fixture award','merit','2026-27','00000000-0000-0000-0000-000000000001');
do $$ begin
 if exists(select 1 from public.institutional_awards where full_tuition is not null or full_ride is not null) then raise exception 'Missing award flags became guessed negatives'; end if;
end $$;
do $$ begin
 if (select can_offer_negotiation_addon from public.institution_negotiation_addon_eligibility_by_year where academic_year='2026-27') then
  raise exception 'Generic appeal wrongly enables paid feature'; end if;
end $$;
update public.appeal_policies set qualifies_for_paid_addon=true,qualifying_path_evidence='Fixture: published incoming award review process';
do $$ begin
 if not (select can_offer_negotiation_addon from public.institution_negotiation_addon_eligibility_by_year where academic_year='2026-27') then
  raise exception 'Verified documented path not enabled'; end if;
 if exists(select 1 from public.institution_negotiation_addon_eligibility_by_year where academic_year='2027-28' and can_offer_negotiation_addon) then
  raise exception 'Year isolation failed'; end if;
 if (select can_offer_negotiation_addon from public.institution_negotiation_addon_eligibility) then
  raise exception 'Unscoped legacy gate must fail closed'; end if;
end $$;
update public.appeal_policies set last_verified_at=current_date-366;
do $$ begin
 if (select can_offer_negotiation_addon from public.institution_negotiation_addon_eligibility_by_year) then raise exception 'Stale path enabled'; end if;
end $$;
update public.appeal_policies set last_verified_at=current_date+1;
do $$ begin
 if (select can_offer_negotiation_addon from public.institution_negotiation_addon_eligibility_by_year) then raise exception 'Future verification enabled'; end if;
end $$;
update public.appeal_policies set last_verified_at=null;
do $$ begin
 if (select can_offer_negotiation_addon from public.institution_negotiation_addon_eligibility_by_year) then raise exception 'Missing verification enabled'; end if;
end $$;
-- Degree requirements: verified-only reads through the provenance view; full payload kept in rule_details.
insert into public.academic_programs(id,institution_id,program_key,academic_year,program_name,source_id,verification_status,last_verified_at)
values ('00000000-0000-0000-0000-000000000004','00000000-0000-0000-0000-000000000002','fixture-bs','2026-27','Fixture BS',
'00000000-0000-0000-0000-000000000001','verified',current_date);
insert into public.degree_requirements(program_id,academic_year,requirement_key,requirement_kind,minimum_credits,rule_details,source_id,verification_status,last_verified_at)
values ('00000000-0000-0000-0000-000000000004','2026-27','fixture-bs','program_plan',120,'{"semester_plan":[]}',
'00000000-0000-0000-0000-000000000001','verified',current_date),
('00000000-0000-0000-0000-000000000004','2026-27','fixture-bs-draft','program_plan',null,'{}',
'00000000-0000-0000-0000-000000000001','unverified',null);
insert into public.transfer_policies(institution_id,academic_year,policy_url,min_grade,source_id,verification_status)
values ('00000000-0000-0000-0000-000000000002','2026-27','https://example.edu/transfer','D-','00000000-0000-0000-0000-000000000001','partially_verified');
-- Retention-type appeals can be stored but can never be flagged as a paid add-on path.
do $$ begin
 begin
  insert into public.appeal_policies(institution_id,academic_year,appeal_kind,offered,source_id,policy_url,verification_status,last_verified_at,qualifies_for_paid_addon,qualifying_path_evidence)
  values ('00000000-0000-0000-0000-000000000002','2026-27','scholarship_retention_appeal',true,'00000000-0000-0000-0000-000000000001','https://example.edu/appeal','verified',current_date,true,'retention only');
  raise exception 'Retention appeal accepted as paid add-on path';
 exception when check_violation then null;
 end;
end $$;
set local role anon;
do $$ begin
 if (select count(*) from public.degree_requirements_with_provenance)<>1 then raise exception 'Degree requirement RLS failed'; end if;
 if (select count(*) from public.transfer_policies_with_provenance)<>0 then raise exception 'Unverified transfer policy exposed'; end if;
 if has_table_privilege(current_user,'public.degree_requirements','INSERT') then raise exception 'Client can write degree requirements'; end if;
end $$;
do $$ begin
 if (select count(*) from public.institutions)<>1 then raise exception 'RLS exposes unverified institution'; end if;
 if has_table_privilege(current_user,'public.institutions','INSERT') or has_table_privilege(current_user,'public.institutions','UPDATE') or has_table_privilege(current_user,'public.institutions','DELETE') then raise exception 'Client write privilege exists'; end if;
 if has_table_privilege(current_user,'public.data_verification_runs','SELECT') then raise exception 'Internal verification runs exposed'; end if;
end $$;
reset role;
set local role authenticated;
do $$ begin
 if (select count(*) from public.institutions)<>1 then raise exception 'Authenticated RLS failed'; end if;
 if has_table_privilege(current_user,'public.appeal_policies','UPDATE') then raise exception 'Authenticated gate mutation possible'; end if;
end $$;
reset role;
rollback;
