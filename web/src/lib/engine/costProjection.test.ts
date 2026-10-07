import { describe, expect, it } from 'vitest'
import type { InstitutionComparison } from '../data/types'
import { fullProgram, potentialSaving, projectCosts, projectRow, termsSaving } from './costProjection'

// The same fixtures and expected numbers as the CR-4 v2 block in supabase/tests/frontend_contracts.sql.
const V = { verification_status: 'verified', academic_year: '2026-27', source_url: 'https://example.edu/x' }
function school(key: string, level: 'four_year' | 'two_year', domains: Partial<Record<string, Record<string, unknown>[]>>): InstitutionComparison {
  return {
    institution_key: key,
    found: true,
    institution: { institution_key: key, display_name: key, level, state_code: 'TN', verification_status: 'verified' } as never,
    academic_year: '2026-27',
    domains: { costs: [], awards: [], appeals: [], credit_policies: [], transfer_policies: [], ...domains } as never,
    missing_domains: [],
    can_offer_paid_addon: false,
  }
}
const priv = school('contract-private', 'four_year', {
  costs: [{ ...V, residency: 'not_applicable', tuition: 40000, mandatory_fees: 1000, on_campus_food_housing: 12000, books_supplies: 1200, transportation: 1500, personal_misc: 2300, total_cost_of_attendance: 58000 }],
  credit_policies: [{ ...V, policy_kind: 'AP', general_limit_credits: 18 }],
  transfer_policies: [{ ...V, max_transfer_credits: 60, residency_requirement_credits: 100 }],
  awards: [
    { ...V, award_name: 'Merit', award_max: 4000 },
    { ...V, verification_status: 'unverified', award_name: 'Draft', award_max: 9000 },
  ],
})
const four = school('contract-four', 'four_year', {
  costs: [{ ...V, residency: 'in_state', tuition: 9000 }, { ...V, verification_status: 'unverified', residency: 'out_of_state', tuition: 30000 }],
  transfer_policies: [{ ...V, max_transfer_credits: 60 }],
  credit_policies: [
    { ...V, policy_kind: 'dual_enrollment', general_limit_credits: 24 },
    { ...V, policy_kind: 'AP', general_limit_credits: 6 },
  ],
})

describe('cost projection v2 (mirror of the SQL rules)', () => {
  it('uses one published price for everyone and keeps tuition, fees and living costs apart', () => {
    const r = projectRow(priv, '2026-27', { residency: 'in_state', exam_credits: 24 })
    expect(r).toMatchObject({ status: 'ok', baseline_total: 164000, savings_total: 20500 })
    expect(r.cost).toMatchObject({ residency: 'not_applicable', residency_requested: 'in_state' })
    expect(r.cost!.components).toMatchObject({ tuition: 40000, mandatory_fees: 1000, housing_food: 12000, living_and_other: 17000 })
    expect(r.levers![1]).toMatchObject({ accepted_upper_bound: 18, reason: 'bounded_by_verified_limit' })
    expect(r.credit_savings).toMatchObject({ mechanism: 'fewer_terms', billing_structure: 'unknown', terms_saved: 1, remainder_credits: 3 })
    expect(r.credit_savings!.by_component).toEqual({ tuition: 20000, mandatory_fees: 500, living_and_other: null })
    expect(r.not_counted!.awards.map((a) => a.award_name)).toEqual(['Merit'])
    expect(r.not_counted!.loans).toBe('no_data')
  })

  it('bounds all outside credit by the residency rule, and a saved term on full cost includes living costs', () => {
    const r = projectRow(priv, '2026-27', { residency: 'out_of_state', cost_basis: 'cost_of_attendance', exam_credits: 24, prior_credits: 30 })
    expect(r.credit_savings).toMatchObject({ outside_credit_max: 20, credits_counted: 20 })
    expect(r.levers![0]!.accepted_upper_bound + r.levers![1]!.accepted_upper_bound).toBe(20)
    expect(r.savings_total).toBe(29000)
    expect(r.credit_savings!.by_component.living_and_other).toBe(8500)
  })

  it('counts nothing under a full term, and says how much is left over', () => {
    const r = projectRow(priv, '2026-27', { residency: 'in_state', exam_credits: 10 })
    expect(r.levers![1]!.reason).toBe('less_than_one_term')
    expect(r.savings_total).toBe(0)
    expect(r.credit_savings!.remainder_credits).toBe(10)
  })

  it('keeps v1 behaviour: lowest verified transfer cap, AP limit only for exam credit, no unverified prices', () => {
    const r = projectRow(four, '2026-27', { residency: 'in_state', prior_credits: 30 })
    expect(r).toMatchObject({ baseline_total: 36000, savings_total: 4500, optimized_total: 31500 })
    expect(r.levers![0]).toMatchObject({ accepted_upper_bound: 24, terms_saved: 1, counted: true })
    expect(projectRow(four, '2026-27', { residency: 'out_of_state' }).status).toBe('missing_cost')
    const exam = projectRow(four, '2026-27', { residency: 'in_state', exam_credits: 30 })
    expect(exam.levers![1]).toMatchObject({ accepted_upper_bound: 6, reason: 'less_than_one_term' })
    expect(projectRow(four, '2026-27', { residency: 'in_state', prior_credits: 0 }).levers![0]!.reason).toBe('no_prior_credits')
  })

  it('reports unknown schools and missing prices explicitly', () => {
    const res = projectCosts([priv, { ...four, found: false, institution: null }], '2026-27', { residency: 'in_state' })
    expect(res.institutions.map((r) => r.status)).toEqual(['ok', 'unknown_institution'])
    expect(res).toMatchObject({ guaranteed: false, prices_held_constant: true, definition: 'v2' })
    const coaOnly = school('coa-only', 'four_year', { costs: [{ ...V, residency: 'in_state', total_cost_of_attendance: 30000 }] })
    const r = projectRow(coaOnly, '2026-27', { residency: 'in_state' })
    expect(r.status).toBe('missing_cost')
    expect(r.cost!.components.total_cost_of_attendance).toBe(30000)
  })
})

describe('full program and potential savings from family-entered aid', () => {
  const row = projectRow(priv, '2026-27', { residency: 'in_state', exam_credits: 24 }) // 164,000 for 4 years; 1 potential term

  it('prices the full program with no credit assumed, grants and loans over every year', () => {
    const f = fullProgram(row, { grantsPerYear: 10000, loansPerYear: 5500 })!
    expect(f).toMatchObject({ years: 4, published: 164000, yearRound: 0, grants: 40000, netPrice: 124000, borrowed: 22000, paidWithoutLoans: 102000 })
  })

  it('adds the family\'s year-round living number separately from the academic-year budget', () => {
    const f = fullProgram(row, { grantsPerYear: null, loansPerYear: null, yearRoundLivingPerYear: 3000 })!
    expect(f).toMatchObject({ published: 164000, yearRound: 12000, netPrice: 176000 })
  })

  it('a potential saving gives up the grants for the terms not attended', () => {
    const p = potentialSaving(row, { grantsPerYear: 10000, loansPerYear: null })!
    expect(p).toEqual({ terms: 1, gross: 20500, lostGrants: 5000, net: 15500 })
    expect(row.credit_savings).toMatchObject({ certainty: 'potential', assumes: ['counted_credit_applies_to_the_degree', 'schedule_allows_finishing_early', 'exam_credit_total_entered_by_family'] })
    expect(row.totals_certainty).toBe('potential')
    expect(projectRow(priv, '2026-27', { residency: 'in_state' }).credit_savings!.assumes).not.toContain('exam_credit_total_entered_by_family')
  })

  it('whole covered plan terms use the same rule, and always leave a term to attend', () => {
    expect(termsSaving(row, 1, { grantsPerYear: 0, loansPerYear: null })).toEqual({ terms: 1, gross: 20500, lostGrants: 0, net: 20500 })
    expect(termsSaving(row, 20, { grantsPerYear: 0, loansPerYear: null })!.terms).toBe(7)
  })

  it('never goes below zero, caps borrowing, and has no answer without a price', () => {
    const f = fullProgram(row, { grantsPerYear: 100000, loansPerYear: 9000 })!
    expect(f).toMatchObject({ netPrice: 0, borrowed: 0, loansCapped: true })
    expect(fullProgram({ institution_key: 'x', status: 'missing_cost' }, { grantsPerYear: 1, loansPerYear: 1 })).toBeNull()
    expect(potentialSaving(projectRow(priv, '2026-27', { residency: 'in_state' }), { grantsPerYear: 1, loansPerYear: null })).toBeNull()
  })
})
