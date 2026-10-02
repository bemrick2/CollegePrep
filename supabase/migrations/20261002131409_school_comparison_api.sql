-- Public reference RPC uses caller permissions, explicit years, and verified data.
create function public.compare_institutions(p_institution_keys text[],p_academic_year text)
returns jsonb language plpgsql stable security invoker set search_path='' as $function$
declare
 key text; pair text[]; institution jsonb; v_institution_id uuid;
 domains jsonb; items jsonb; missing jsonb; results jsonb='[]'::jsonb;
 paid boolean; statement text;
begin
 if p_academic_year is null or btrim(p_academic_year)='' or length(p_academic_year)>40 then
  raise exception 'academic_year is required (maximum 40 characters)' using errcode='22023';
 end if;
 if p_institution_keys is null or cardinality(p_institution_keys) not between 1 and 20
 or array_ndims(p_institution_keys)<>1
 or exists(select 1 from unnest(p_institution_keys) k where k is null or btrim(k)='' or length(k)>200)
 or (select count(distinct k) from unnest(p_institution_keys) k)<>cardinality(p_institution_keys) then
  raise exception 'Provide 1 to 20 distinct nonempty institution keys' using errcode='22023';
 end if;
 foreach key in array p_institution_keys loop
  institution=null; v_institution_id=null; domains='{}'::jsonb; missing='[]'::jsonb; paid=false;
  select i.id,to_jsonb(i)-'id'-'source_id'||jsonb_build_object('source_url',s.canonical_url)
  into v_institution_id,institution from public.institutions i join public.sources s on s.id=i.source_id
  where i.institution_key=key and i.verification_status='verified' and s.authority<>'secondary';
  foreach pair slice 1 in array array[
   ['costs','institution_costs'],['admissions_metrics','admissions_metrics'],
   ['awards','institutional_awards'],['credit_policies','credit_policies'],
   ['transfer_policies','transfer_policies'],['academic_programs','academic_programs'],
   ['degree_requirements','degree_requirements'],['appeals','appeal_policies']
  ] loop
   if pair[1]='degree_requirements' then
    select coalesce(jsonb_agg(to_jsonb(d)-'id'-'source_id'-'program_id'||
     jsonb_build_object('source_url',s.canonical_url,'program_key',p.program_key)
     order by p.program_key,d.requirement_key),'[]'::jsonb) into items
    from public.degree_requirements d join public.academic_programs p on p.id=d.program_id
    join public.sources s on s.id=d.source_id
    where p.institution_id=v_institution_id and p.academic_year=p_academic_year
    and d.academic_year=p_academic_year and p.verification_status='verified'
    and d.verification_status='verified' and s.authority<>'secondary';
   elsif pair[1]='credit_policies' then
    select coalesce(jsonb_agg(to_jsonb(r)-'id'-'source_id'-'institution_id'||
     jsonb_build_object('source_url',s.canonical_url,'equivalencies',(
      select coalesce(jsonb_agg(to_jsonb(e)-'id'-'credit_policy_id'
       order by e.exam_or_course_code,e.minimum_score,e.institution_course_equivalent),'[]'::jsonb)
      from public.credit_equivalencies e where e.credit_policy_id=r.id))
     order by r.policy_kind),'[]'::jsonb) into items
    from public.credit_policies r join public.sources s on s.id=r.source_id
    where r.institution_id=v_institution_id and r.academic_year=p_academic_year
    and r.verification_status='verified' and s.authority<>'secondary';
   else
    -- Table identifiers are fixed above; caller values are bound parameters.
    statement=format('select coalesce(jsonb_agg(to_jsonb(r)-''id''-''source_id''-''institution_id''||jsonb_build_object(''source_url'',s.canonical_url) order by r.id),''[]''::jsonb) from public.%I r join public.sources s on s.id=r.source_id where r.institution_id=$1 and r.academic_year=$2 and r.verification_status=''verified'' and s.authority<>''secondary''',pair[2]);
    execute statement into items using v_institution_id,p_academic_year;
   end if;
   domains=domains||jsonb_build_object(pair[1],items);
   if jsonb_array_length(items)=0 then missing=missing||jsonb_build_array(pair[1]); end if;
  end loop;
  select coalesce(bool_or(e.can_offer_negotiation_addon),false) into paid
   from public.institution_negotiation_addon_eligibility_by_year e
   where e.institution_id=v_institution_id and e.academic_year=p_academic_year;
  results=results||jsonb_build_array(jsonb_build_object('institution_key',key,
   'found',institution is not null,'institution',institution,'academic_year',p_academic_year,
   'domains',domains,'missing_domains',missing,'can_offer_paid_addon',paid));
 end loop;
 return jsonb_build_object('academic_year',p_academic_year,'institutions',results);
end $function$;
revoke all on function public.compare_institutions(text[],text) from public;
grant execute on function public.compare_institutions(text[],text) to anon,authenticated,service_role;
comment on function public.compare_institutions(text[],text) is
 'Compare 1-20 schools for one exact academic year. Unknown schools and missing domains are explicit; no historical fallback or inferred aid eligibility.';
