-- Disposable fixtures only; never counted as school coverage.
begin;
insert into public.sources(id,canonical_url,authority) values
('00000000-0000-0000-0000-000000000001','https://example.edu/appeal','institution');
insert into public.institutions(id,ipeds_name,display_name,state_code,verification_status) values
('00000000-0000-0000-0000-000000000002','Test College','Test College','TN','verified'),
('00000000-0000-0000-0000-000000000003','Unverified College','Unverified College','TN','unverified');
insert into public.appeal_policies(institution_id,academic_year,appeal_kind,offered,source_id,policy_url,verification_status,last_verified_at)
values ('00000000-0000-0000-0000-000000000002','2026-27','financial_aid_appeal',true,
'00000000-0000-0000-0000-000000000001','https://example.edu/appeal','verified',current_date);
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
set local role anon;
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
