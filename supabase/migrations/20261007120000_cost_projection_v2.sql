-- CR-4 v2 (issue #37): cost_projection, same signature, definition 'v2'.
--
-- Changes from v1 (20261006180000_cost_projection.sql), all still verified, exact-year data only:
--  * Residency: when no verified price exists for the requested residency, a verified 'not_applicable' row
--    (one published price for every student, as most private schools publish) is used. cost.residency says which
--    row was used; this is the school's own price, not a substitute.
--  * cost.components lists every published part of the price (tuition, fees, housing and food, books, transportation,
--    personal, other) so tuition, fees and living costs are never blended. living_and_other is COA minus tuition and
--    fees, only when all three are published.
--  * A second credit lever, exam_credits: AP/IB/CLEP/Cambridge credit the family computed from this school's own
--    published equivalency table (the client does the score lookup on the same verified records). Bounded by the
--    lowest verified exam-credit limit when one exists; no transfer cap is needed because the school's own table
--    is the policy. prior_credits (credit brought from elsewhere) keeps the v1 rule: counted only under a verified cap.
--  * Both are bounded by a verified residency requirement (credits that must be earned at the school), measured
--    against the projection's own credit total (years x terms x credits per term).
--  * credit_savings is a potential saving, never a confirmed shorter degree: certainty 'potential', and assumes
--    lists what it takes for granted (the counted credit applies to the degree; the schedule lets the student
--    finish early). Whether credit applies to a given major is checked by the client against the verified degree
--    plan, when one is on file. credit_savings explains the mechanism. Savings come only from fewer billed terms when the student finishes
--    early; billing_structure is 'unknown' because no flat-rate or per-credit tuition data exists, and credits short
--    of a full term (remainder_credits) are not counted. Each lever's terms_saved/savings are what it would save on
--    its own; the row totals use the combined credits.
--  * Awards, state aid and appeals stay under not_counted (amounts listed, never subtracted). No loan data exists.
create or replace function public.cost_projection(
  p_student uuid,
  p_institution_keys text[],
  p_academic_year text,
  p_assumptions jsonb default '{}'::jsonb
) returns jsonb
language plpgsql stable security invoker set search_path = '' as $$
declare
  a jsonb := coalesce(p_assumptions, '{}'::jsonb);
  v_residency text; v_basis text; v_years numeric; v_prior numeric; v_exam numeric; v_cpt numeric; v_tpy numeric;
  k text; inst record; cost record; v_annual numeric; v_years_used numeric; v_baseline numeric; v_living numeric;
  v_caps jsonb; v_cap numeric; v_exam_caps jsonb; v_exam_cap numeric; v_res_req numeric; v_outside_max numeric;
  v_prior_ok numeric; v_exam_ok numeric; v_total numeric; v_max_terms numeric; v_terms numeric; v_savings numeric;
  v_prior_reason text; v_exam_reason text; v_components jsonb; v_lever_prior jsonb; v_lever_exam jsonb;
  v_not jsonb; v_rows jsonb := '[]'::jsonb;
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
       where x not in ('residency', 'cost_basis', 'years', 'prior_credits', 'exam_credits', 'credits_per_term', 'terms_per_year')) then
    raise exception 'assumptions accepts only residency, cost_basis, years, prior_credits, exam_credits, credits_per_term, terms_per_year'
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
    v_exam := coalesce((a->>'exam_credits')::numeric, 0);
    v_cpt := coalesce((a->>'credits_per_term')::numeric, 15);
    v_tpy := coalesce((a->>'terms_per_year')::numeric, 2);
  exception when invalid_text_representation then raise exception 'numeric assumptions must be numbers' using errcode = '22023'; end;
  if (v_years is not null and (v_years <> trunc(v_years) or v_years not between 1 and 6))
     or v_prior < 0 or v_prior > 90 or v_exam < 0 or v_exam > 90 or v_cpt not between 6 and 21 or v_tpy not in (2, 3) then
    raise exception 'years 1-6 (whole), prior_credits and exam_credits 0-90, credits_per_term 6-21, terms_per_year 2 or 3'
      using errcode = '22023';
  end if;

  foreach k in array p_institution_keys loop
    select i.id, i.institution_key, i.display_name, i.state_code, i.level into inst
    from public.institutions i join public.sources s on s.id = i.source_id
    where i.institution_key = k and i.verification_status = 'verified' and s.authority <> 'secondary';
    if not found then
      v_rows := v_rows || jsonb_build_array(jsonb_build_object('institution_key', k, 'status', 'unknown_institution'));
      continue;
    end if;

    -- The requested residency first; otherwise the school's single price for everyone.
    select c.*, s.canonical_url into cost
    from public.institution_costs c join public.sources s on s.id = c.source_id
    where c.institution_id = inst.id and c.academic_year = p_academic_year and c.verification_status = 'verified'
      and c.residency in (v_residency, 'not_applicable')
    order by (c.residency = v_residency) desc
    limit 1;
    v_annual := case when cost.id is null then null
                     when v_basis = 'cost_of_attendance' then cost.total_cost_of_attendance
                     when cost.tuition is null then null
                     else cost.tuition + coalesce(cost.mandatory_fees, 0) end;
    v_years_used := coalesce(v_years, case inst.level when 'four_year' then 4 when 'two_year' then 2 end);
    v_living := case when cost.total_cost_of_attendance is not null and cost.tuition is not null and cost.mandatory_fees is not null
                     then cost.total_cost_of_attendance - cost.tuition - cost.mandatory_fees end;
    v_components := case when cost.id is null then null else jsonb_build_object(
      'tuition', cost.tuition, 'mandatory_fees', cost.mandatory_fees,
      'housing_food', coalesce(cost.on_campus_food_housing,
                               case when cost.room is not null or cost.board is not null then coalesce(cost.room, 0) + coalesce(cost.board, 0) end),
      'books_supplies', cost.books_supplies, 'transportation', cost.transportation, 'personal_misc', cost.personal_misc,
      'other_expenses', cost.on_campus_other_expenses, 'total_cost_of_attendance', cost.total_cost_of_attendance,
      'living_and_other', v_living) end;

    -- Listed only. Nothing here asserts eligibility or is subtracted.
    v_not := jsonb_build_object(
      'awards', coalesce((select jsonb_agg(jsonb_build_object('award_name', w.award_name, 'award_type', w.award_type,
          'award_amount_text', w.award_amount_text, 'award_min', w.award_min, 'award_max', w.award_max,
          'full_tuition', w.full_tuition, 'full_ride', w.full_ride,
          'automatic_consideration', w.automatic_consideration, 'separate_application', w.separate_application,
          'eligibility_summary', w.eligibility_summary, 'renewable', w.renewable, 'source_url', s.canonical_url)
          order by w.award_name)
        from public.institutional_awards w join public.sources s on s.id = w.source_id
        where w.institution_id = inst.id and w.academic_year = p_academic_year and w.verification_status = 'verified'), '[]'::jsonb),
      'state_aid', coalesce((select jsonb_agg(jsonb_build_object('program_name', g.program_name, 'program_type', g.program_type,
          'award_amount_text', g.award_amount_text, 'award_min', g.award_min, 'award_max', g.award_max,
          'eligibility_summary', g.eligibility_summary, 'official_url', g.official_url, 'source_url', s.canonical_url)
          order by g.program_name)
        from public.state_aid_programs g join public.sources s on s.id = g.source_id
        where g.state_code = inst.state_code and g.academic_year = p_academic_year and g.verification_status = 'verified'), '[]'::jsonb),
      'appeals', coalesce((select jsonb_agg(jsonb_build_object('appeal_kind', ap.appeal_kind, 'process_summary', ap.process_summary,
          'policy_url', ap.policy_url) order by ap.appeal_kind)
        from public.appeal_policies ap
        where ap.institution_id = inst.id and ap.academic_year = p_academic_year and ap.verification_status = 'verified'
          and ap.offered), '[]'::jsonb),
      'loans', 'no_data');

    if v_annual is null or v_years_used is null then
      v_rows := v_rows || jsonb_build_array(jsonb_build_object(
        'institution_key', inst.institution_key, 'display_name', inst.display_name, 'level', inst.level,
        'status', case when v_annual is null then 'missing_cost' else 'missing_years' end,
        'cost', case when cost.id is null then null else jsonb_build_object('basis', v_basis, 'residency', cost.residency,
          'residency_requested', v_residency, 'components', v_components, 'source_url', cost.canonical_url,
          'last_verified_at', cost.last_verified_at) end,
        'not_counted', v_not));
      continue;
    end if;
    v_baseline := v_annual * v_years_used;

    -- Verified caps on credit brought from elsewhere (v1 rule).
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

    -- Verified limits on exam credit (any exam kind the school publishes a limit for).
    select coalesce(jsonb_agg(x order by x->>'kind'), '[]'::jsonb) into v_exam_caps from (
      select jsonb_build_object('kind', r.policy_kind || '_limit', 'credits', r.general_limit_credits, 'source_url', s.canonical_url) x
      from public.credit_policies r join public.sources s on s.id = r.source_id
      where r.institution_id = inst.id and r.academic_year = p_academic_year and r.verification_status = 'verified'
        and r.policy_kind in ('AP', 'IB', 'CLEP', 'cambridge_international') and r.general_limit_credits is not null
    ) caps;
    select min((c->>'credits')::numeric) into v_exam_cap from jsonb_array_elements(v_exam_caps) c;

    -- Credits that must be earned at the school, against this projection's own credit total.
    select min(x) into v_res_req from (
      select t.residency_requirement_credits x from public.transfer_policies t
      where t.institution_id = inst.id and t.academic_year = p_academic_year and t.verification_status = 'verified'
      union all
      select r.residency_credit_requirement from public.credit_policies r
      where r.institution_id = inst.id and r.academic_year = p_academic_year and r.verification_status = 'verified'
    ) req where x is not null;
    v_outside_max := case when v_res_req is null then null else greatest(v_years_used * v_tpy * v_cpt - v_res_req, 0) end;

    v_prior_ok := case when v_prior = 0 or v_cap is null then 0 else least(v_prior, v_cap) end;
    v_prior_reason := case when v_prior = 0 then 'no_prior_credits' when v_cap is null then 'no_verified_cap' else 'bounded_by_verified_cap' end;
    v_exam_ok := case when v_exam = 0 then 0 else least(v_exam, coalesce(v_exam_cap, v_exam)) end;
    v_exam_reason := case when v_exam = 0 then 'no_exam_credits' when v_exam_cap is null then 'from_school_table'
                          else 'bounded_by_verified_limit' end;
    v_total := v_prior_ok + v_exam_ok;
    if v_outside_max is not null and v_total > v_outside_max then
      -- The residency rule bounds the total; each lever keeps its share of what is left.
      v_prior_ok := round(v_prior_ok * v_outside_max / v_total, 2);
      v_exam_ok := v_outside_max - v_prior_ok;
      v_total := v_outside_max;
    end if;

    -- At least one term is always left to attend.
    v_max_terms := v_years_used * v_tpy - 1;
    v_terms := least(floor(v_total / v_cpt), v_max_terms);
    v_savings := round(v_terms * v_annual / v_tpy, 2);

    v_lever_prior := jsonb_build_object('kind', 'prior_credits', 'requested_credits', v_prior,
      'accepted_upper_bound', v_prior_ok, 'caps', v_caps,
      'terms_saved', least(floor(v_prior_ok / v_cpt), v_max_terms),
      'savings', round(least(floor(v_prior_ok / v_cpt), v_max_terms) * v_annual / v_tpy, 2),
      'counted', floor(v_prior_ok / v_cpt) > 0, 'reason',
        case when v_prior_reason = 'bounded_by_verified_cap' and floor(v_prior_ok / v_cpt) = 0 then 'less_than_one_term' else v_prior_reason end,
      'requires_confirmation', true);
    v_lever_exam := jsonb_build_object('kind', 'exam_credits', 'requested_credits', v_exam,
      'accepted_upper_bound', v_exam_ok, 'caps', v_exam_caps,
      'terms_saved', least(floor(v_exam_ok / v_cpt), v_max_terms),
      'savings', round(least(floor(v_exam_ok / v_cpt), v_max_terms) * v_annual / v_tpy, 2),
      'counted', floor(v_exam_ok / v_cpt) > 0, 'reason',
        case when v_exam > 0 and floor(v_exam_ok / v_cpt) = 0 then 'less_than_one_term' else v_exam_reason end,
      'requires_confirmation', true);

    v_rows := v_rows || jsonb_build_array(jsonb_build_object(
      'institution_key', inst.institution_key, 'display_name', inst.display_name, 'level', inst.level,
      'status', 'ok',
      'cost', jsonb_build_object('basis', v_basis, 'residency', cost.residency, 'residency_requested', v_residency,
        'annual', v_annual, 'tuition', cost.tuition, 'mandatory_fees', cost.mandatory_fees,
        'total_cost_of_attendance', cost.total_cost_of_attendance, 'components', v_components,
        'source_url', cost.canonical_url, 'last_verified_at', cost.last_verified_at),
      'years', v_years_used, 'years_source', case when v_years is null then 'level_default' else 'assumption' end,
      'baseline_total', v_baseline,
      'levers', jsonb_build_array(v_lever_prior, v_lever_exam),
      'credit_savings', jsonb_build_object('certainty', 'potential',
        'assumes', jsonb_build_array('counted_credit_applies_to_the_degree', 'schedule_allows_finishing_early'),
        'mechanism', 'fewer_terms', 'billing_structure', 'unknown',
        'credits_counted', v_total, 'residency_requirement_credits', v_res_req, 'outside_credit_max', v_outside_max,
        'terms_saved', v_terms, 'remainder_credits', v_total - v_terms * v_cpt,
        'by_component', jsonb_build_object(
          'tuition', case when cost.tuition is null then null else round(v_terms * cost.tuition / v_tpy, 2) end,
          'mandatory_fees', case when cost.mandatory_fees is null then null else round(v_terms * cost.mandatory_fees / v_tpy, 2) end,
          'living_and_other', case when v_basis = 'cost_of_attendance' and v_living is not null
                                   then round(v_terms * v_living / v_tpy, 2) end),
        'requires_confirmation', true),
      'optimized_total', v_baseline - v_savings,
      'savings_total', v_savings,
      'not_counted', v_not));
  end loop;

  return jsonb_build_object(
    'academic_year', p_academic_year,
    'assumptions', jsonb_build_object('residency', v_residency, 'cost_basis', v_basis, 'years', v_years,
      'prior_credits', v_prior, 'exam_credits', v_exam, 'credits_per_term', v_cpt, 'terms_per_year', v_tpy),
    'prices_held_constant', true,
    'guaranteed', false,
    'definition', 'v2',
    'institutions', v_rows);
end $$;

revoke all on function public.cost_projection(uuid, text[], text, jsonb) from public, anon;
grant execute on function public.cost_projection(uuid, text[], text, jsonb) to authenticated, service_role;
comment on function public.cost_projection(uuid, text[], text, jsonb) is
  'CR-4 v2: verified exact-year cost of attendance by component, with credit counted only from the school''s own exam table or under a verified transfer cap, saved as fewer billed terms. Awards and state aid are listed, never subtracted.';
