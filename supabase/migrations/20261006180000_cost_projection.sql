-- CR-4 (issue #37): cost_projection(student, institution_keys, academic_year, assumptions).
--
-- Rules this function enforces:
--  * Only verified records for exactly p_academic_year are used. There is no fallback to another year.
--  * Prices are held at that year's published figures. No inflation or escalation is guessed.
--  * The only lever counted in `optimized` is credit the family says the student will bring
--    (assumptions.prior_credits). It is bounded by every verified cap for that year (transfer
--    maximum, dual-enrollment limit). With no verified cap it is not counted. Course-by-course
--    acceptance is never asserted, so the lever is an upper bound that needs the school to confirm.
--  * Awards, state aid and appeal processes are listed under `not_counted`, never added to a total.
--    The list says nothing about scholarship eligibility and does not offer a negotiation add-on.

create function public.cost_projection(
  p_student uuid,
  p_institution_keys text[],
  p_academic_year text,
  p_assumptions jsonb default '{}'::jsonb
) returns jsonb
language plpgsql stable security invoker set search_path = '' as $$
declare
  a jsonb := coalesce(p_assumptions, '{}'::jsonb);
  v_residency text; v_basis text; v_years numeric; v_prior numeric; v_cpt numeric; v_tpy numeric;
  k text; inst record; cost record; v_annual numeric; v_years_used numeric; v_baseline numeric;
  v_caps jsonb; v_cap numeric; v_accepted numeric; v_terms numeric; v_savings numeric; v_counted boolean; v_reason text;
  v_lever jsonb; v_not jsonb; v_row jsonb; v_rows jsonb := '[]'::jsonb;
begin
  if p_student is null or not public.can_view_student(p_student) then
    raise exception 'not allowed to plan for this student' using errcode = '42501';
  end if;
  if p_academic_year is null or p_academic_year !~ '^[0-9]{4}-[0-9]{2}$' then
    raise exception 'academic_year must look like 2026-27' using errcode = '22023';
  end if;
  if p_institution_keys is null or array_ndims(p_institution_keys) <> 1
     or cardinality(p_institution_keys) not between 1 and 8
     or exists (select 1 from unnest(p_institution_keys) x where x is null or btrim(x) = '' or length(x) > 200)
     or (select count(distinct x) from unnest(p_institution_keys) x) <> cardinality(p_institution_keys) then
    raise exception 'Provide 1 to 8 distinct nonempty institution keys' using errcode = '22023';
  end if;
  if jsonb_typeof(a) <> 'object' or exists (select 1 from jsonb_object_keys(a) x
       where x not in ('residency', 'cost_basis', 'years', 'prior_credits', 'credits_per_term', 'terms_per_year')) then
    raise exception 'assumptions accepts only residency, cost_basis, years, prior_credits, credits_per_term, terms_per_year'
      using errcode = '22023';
  end if;

  v_residency := a->>'residency';
  if v_residency is null or v_residency not in ('in_state', 'out_of_state', 'district', 'international') then
    raise exception 'assumptions.residency is required: in_state, out_of_state, district or international' using errcode = '22023';
  end if;
  v_basis := coalesce(a->>'cost_basis', 'tuition_and_fees');
  if v_basis not in ('tuition_and_fees', 'cost_of_attendance') then
    raise exception 'assumptions.cost_basis must be tuition_and_fees or cost_of_attendance' using errcode = '22023';
  end if;
  begin
    v_years := (a->>'years')::numeric;
    v_prior := coalesce((a->>'prior_credits')::numeric, 0);
    v_cpt := coalesce((a->>'credits_per_term')::numeric, 15);
    v_tpy := coalesce((a->>'terms_per_year')::numeric, 2);
  exception when invalid_text_representation then raise exception 'numeric assumptions must be numbers' using errcode = '22023'; end;
  if (v_years is not null and (v_years <> trunc(v_years) or v_years not between 1 and 6))
     or v_prior < 0 or v_prior > 90 or v_cpt not between 6 and 21 or v_tpy not in (2, 3) then
    raise exception 'years 1-6 (whole), prior_credits 0-90, credits_per_term 6-21, terms_per_year 2 or 3' using errcode = '22023';
  end if;

  foreach k in array p_institution_keys loop
    select i.id, i.institution_key, i.display_name, i.state_code, i.level into inst
    from public.institutions i join public.sources s on s.id = i.source_id
    where i.institution_key = k and i.verification_status = 'verified' and s.authority <> 'secondary';
    if not found then
      v_rows := v_rows || jsonb_build_array(jsonb_build_object('institution_key', k, 'status', 'unknown_institution'));
      continue;
    end if;

    select c.*, s.canonical_url into cost
    from public.institution_costs c join public.sources s on s.id = c.source_id
    where c.institution_id = inst.id and c.academic_year = p_academic_year and c.residency = v_residency
      and c.verification_status = 'verified';
    v_annual := case when cost.id is null then null
                     when v_basis = 'cost_of_attendance' then cost.total_cost_of_attendance
                     when cost.tuition is null then null
                     else cost.tuition + coalesce(cost.mandatory_fees, 0) end;
    v_years_used := coalesce(v_years, case inst.level when 'four_year' then 4 when 'two_year' then 2 end);

    -- Listed only. Nothing here asserts eligibility.
    v_not := jsonb_build_object(
      'awards', coalesce((select jsonb_agg(jsonb_build_object('award_name', w.award_name, 'award_type', w.award_type,
          'award_amount_text', w.award_amount_text, 'award_min', w.award_min, 'award_max', w.award_max,
          'automatic_consideration', w.automatic_consideration, 'separate_application', w.separate_application,
          'eligibility_summary', w.eligibility_summary, 'renewable', w.renewable, 'source_url', s.canonical_url)
          order by w.award_name)
        from public.institutional_awards w join public.sources s on s.id = w.source_id
        where w.institution_id = inst.id and w.academic_year = p_academic_year and w.verification_status = 'verified'), '[]'::jsonb),
      'state_aid', coalesce((select jsonb_agg(jsonb_build_object('program_name', g.program_name, 'program_type', g.program_type,
          'award_amount_text', g.award_amount_text, 'eligibility_summary', g.eligibility_summary,
          'official_url', g.official_url, 'source_url', s.canonical_url) order by g.program_name)
        from public.state_aid_programs g join public.sources s on s.id = g.source_id
        where g.state_code = inst.state_code and g.academic_year = p_academic_year and g.verification_status = 'verified'), '[]'::jsonb),
      'appeals', coalesce((select jsonb_agg(jsonb_build_object('appeal_kind', ap.appeal_kind, 'process_summary', ap.process_summary,
          'policy_url', ap.policy_url) order by ap.appeal_kind)
        from public.appeal_policies ap
        where ap.institution_id = inst.id and ap.academic_year = p_academic_year and ap.verification_status = 'verified'
          and ap.offered), '[]'::jsonb));

    if v_annual is null or v_years_used is null then
      v_rows := v_rows || jsonb_build_array(jsonb_build_object(
        'institution_key', inst.institution_key, 'display_name', inst.display_name, 'level', inst.level,
        'status', case when v_annual is null then 'missing_cost' else 'missing_years' end,
        'not_counted', v_not));
      continue;
    end if;
    v_baseline := v_annual * v_years_used;

    -- Verified caps on credit brought in, for exactly this year.
    select coalesce(jsonb_agg(x order by x->>'kind'), '[]'::jsonb) into v_caps from (
      select jsonb_build_object('kind', 'transfer_max_credits', 'credits', t.max_transfer_credits, 'source_url', s.canonical_url) x
      from public.transfer_policies t join public.sources s on s.id = t.source_id
      where t.institution_id = inst.id and t.academic_year = p_academic_year and t.verification_status = 'verified'
        and t.max_transfer_credits is not null
      union all
      select jsonb_build_object('kind', 'dual_enrollment_limit', 'credits', r.general_limit_credits, 'source_url', s.canonical_url)
      from public.credit_policies r join public.sources s on s.id = r.source_id
      where r.institution_id = inst.id and r.academic_year = p_academic_year and r.verification_status = 'verified'
        and r.policy_kind = 'dual_enrollment' and r.general_limit_credits is not null
    ) caps;
    select min((c->>'credits')::numeric) into v_cap from jsonb_array_elements(v_caps) c;

    v_accepted := 0; v_terms := 0; v_savings := 0; v_counted := false;
    if v_prior = 0 then
      v_reason := 'no_prior_credits';
    elsif v_cap is null then
      v_reason := 'no_verified_cap';
    else
      v_accepted := least(v_prior, v_cap);
      -- At least one term is always left to attend.
      v_terms := least(floor(v_accepted / v_cpt), v_years_used * v_tpy - 1);
      v_savings := round(v_terms * v_annual / v_tpy, 2);
      v_counted := v_terms > 0;
      v_reason := case when v_counted then 'bounded_by_verified_cap' else 'less_than_one_term' end;
    end if;
    v_lever := jsonb_build_object('kind', 'prior_credits', 'requested_credits', v_prior,
      'accepted_upper_bound', v_accepted, 'caps', v_caps, 'terms_saved', v_terms, 'savings', v_savings,
      'counted', v_counted, 'reason', v_reason, 'requires_confirmation', true);

    v_rows := v_rows || jsonb_build_array(jsonb_build_object(
      'institution_key', inst.institution_key, 'display_name', inst.display_name, 'level', inst.level,
      'status', 'ok',
      'cost', jsonb_build_object('basis', v_basis, 'residency', v_residency, 'annual', v_annual,
        'tuition', cost.tuition, 'mandatory_fees', cost.mandatory_fees,
        'total_cost_of_attendance', cost.total_cost_of_attendance,
        'source_url', cost.canonical_url, 'last_verified_at', cost.last_verified_at),
      'years', v_years_used, 'years_source', case when v_years is null then 'level_default' else 'assumption' end,
      'baseline_total', v_baseline,
      'levers', jsonb_build_array(v_lever),
      'optimized_total', v_baseline - case when v_counted then v_savings else 0 end,
      'savings_total', case when v_counted then v_savings else 0 end,
      'not_counted', v_not));
  end loop;

  return jsonb_build_object(
    'academic_year', p_academic_year,
    'assumptions', jsonb_build_object('residency', v_residency, 'cost_basis', v_basis, 'years', v_years,
      'prior_credits', v_prior, 'credits_per_term', v_cpt, 'terms_per_year', v_tpy),
    'prices_held_constant', true,
    'guaranteed', false,
    'definition', 'v1',
    'institutions', v_rows);
end $$;

revoke all on function public.cost_projection(uuid, text[], text, jsonb) from public, anon;
grant execute on function public.cost_projection(uuid, text[], text, jsonb) to authenticated, service_role;
comment on function public.cost_projection(uuid, text[], text, jsonb) is
  'CR-4: baseline and optimized cost from verified records for exactly one academic year. Only family-stated prior credits bounded by verified caps are counted; awards, state aid and appeals are listed, never totalled or treated as eligibility.';
