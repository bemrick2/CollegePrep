import type {
  AwardListing,
  CostAssumptions,
  CostComponents,
  CostProjectionResult,
  CreditCap,
  CreditLever,
  InstitutionComparison,
  ProjectionRow,
} from '../data/types'

/**
 * The demo's copy of `cost_projection` v2 (supabase/migrations/20261007120000_cost_projection_v2.sql), run over the
 * same verified records `compare_institutions` returns. Live mode always uses the server; the local end-to-end test
 * checks the two agree. Any rule change goes in both places.
 */
type Rec = Record<string, unknown>
const num = (v: unknown): number | null => (v == null || v === '' ? null : Number(v))
const round2 = (n: number) => Math.round(n * 100) / 100
const EXAM_KINDS = ['AP', 'IB', 'CLEP', 'cambridge_international']

export function projectRow(c: InstitutionComparison, year: string, a: CostAssumptions): ProjectionRow {
  const inst = c.institution
  if (!c.found || !inst || (inst as unknown as Rec).verification_status !== 'verified')
    return { institution_key: c.institution_key, status: 'unknown_institution' }
  const basis = a.cost_basis ?? 'tuition_and_fees'
  const cpt = a.credits_per_term ?? 15
  const tpy = a.terms_per_year ?? 2
  const prior = a.prior_credits ?? 0
  const exam = a.exam_credits ?? 0
  const verified = (d: string) => ((c.domains[d as keyof typeof c.domains] ?? []) as Rec[]).filter((r) => r.verification_status === 'verified' && (r.academic_year == null || r.academic_year === year))

  const costs = verified('costs')
  const cost = costs.find((r) => r.residency === a.residency) ?? costs.find((r) => r.residency === 'not_applicable') ?? null
  const tuition = num(cost?.tuition)
  const fees = num(cost?.mandatory_fees)
  const coa = num(cost?.total_cost_of_attendance)
  const room = num(cost?.room)
  const board = num(cost?.board)
  const living = coa != null && tuition != null && fees != null ? coa - tuition - fees : null
  const components: CostComponents | null = cost
    ? {
        tuition,
        mandatory_fees: fees,
        housing_food: num(cost.on_campus_food_housing) ?? (room != null || board != null ? (room ?? 0) + (board ?? 0) : null),
        books_supplies: num(cost.books_supplies),
        transportation: num(cost.transportation),
        personal_misc: num(cost.personal_misc),
        other_expenses: num(cost.on_campus_other_expenses),
        total_cost_of_attendance: coa,
        living_and_other: living,
      }
    : null
  const annual = !cost ? null : basis === 'cost_of_attendance' ? coa : tuition == null ? null : tuition + (fees ?? 0)
  const years = a.years ?? (inst.level === 'four_year' ? 4 : inst.level === 'two_year' ? 2 : null)
  const head = { institution_key: inst.institution_key, display_name: inst.display_name, level: inst.level ?? null }
  const costOut = cost
    ? {
        basis,
        residency: String(cost.residency),
        residency_requested: a.residency,
        components: components!,
        source_url: (cost.source_url as string | null) ?? null,
        last_verified_at: (cost.last_verified_at as string | null) ?? null,
      }
    : null
  const notCounted = {
    awards: verified('awards').map((w) => w as unknown as AwardListing).sort((x, y) => x.award_name.localeCompare(y.award_name)),
    state_aid: [], // compare_institutions does not carry state programs; the server lists them
    appeals: verified('appeals')
      .filter((p) => p.offered)
      .map((p) => ({ appeal_kind: String(p.appeal_kind), process_summary: (p.process_summary as string | null) ?? null, policy_url: (p.policy_url as string | null) ?? null })),
    loans: 'no_data' as const,
  }
  if (annual == null || years == null) return { ...head, status: annual == null ? 'missing_cost' : 'missing_years', cost: costOut, not_counted: notCounted }
  const baseline = annual * years

  const policies = verified('credit_policies')
  const transfers = verified('transfer_policies')
  const caps: CreditCap[] = [
    ...transfers.filter((t) => num(t.max_transfer_credits) != null).map((t) => ({ kind: 'transfer_max_credits', credits: num(t.max_transfer_credits)!, source_url: (t.source_url as string) ?? null })),
    ...policies
      .filter((p) => p.policy_kind === 'dual_enrollment' && num(p.general_limit_credits) != null)
      .map((p) => ({ kind: 'dual_enrollment_limit', credits: num(p.general_limit_credits)!, source_url: (p.source_url as string) ?? null })),
  ].sort((x, y) => x.kind.localeCompare(y.kind))
  const examCaps: CreditCap[] = policies
    .filter((p) => EXAM_KINDS.includes(String(p.policy_kind)) && num(p.general_limit_credits) != null)
    .map((p) => ({ kind: `${p.policy_kind}_limit`, credits: num(p.general_limit_credits)!, source_url: (p.source_url as string) ?? null }))
    .sort((x, y) => x.kind.localeCompare(y.kind))
  const minOf = (xs: number[]) => (xs.length ? Math.min(...xs) : null)
  const cap = minOf(caps.map((x) => x.credits))
  const examCap = minOf(examCaps.map((x) => x.credits))
  const resReq = minOf(
    [...transfers.map((t) => num(t.residency_requirement_credits)), ...policies.map((p) => num(p.residency_credit_requirement))].filter((x): x is number => x != null),
  )
  const outsideMax = resReq == null ? null : Math.max(years * tpy * cpt - resReq, 0)

  let priorOk = prior === 0 || cap == null ? 0 : Math.min(prior, cap)
  const priorReason = prior === 0 ? 'no_prior_credits' : cap == null ? 'no_verified_cap' : 'bounded_by_verified_cap'
  let examOk = exam === 0 ? 0 : Math.min(exam, examCap ?? exam)
  const examReason = exam === 0 ? 'no_exam_credits' : examCap == null ? 'from_school_table' : 'bounded_by_verified_limit'
  let total = priorOk + examOk
  if (outsideMax != null && total > outsideMax) {
    priorOk = round2((priorOk * outsideMax) / total)
    examOk = outsideMax - priorOk
    total = outsideMax
  }
  const maxTerms = years * tpy - 1
  const termsFor = (credits: number) => Math.min(Math.floor(credits / cpt), maxTerms)
  const terms = termsFor(total)
  const savings = round2((terms * annual) / tpy)
  const lever = (kind: CreditLever['kind'], requested: number, ok: number, leverCaps: CreditCap[], reason: CreditLever['reason']): CreditLever => ({
    kind,
    requested_credits: requested,
    accepted_upper_bound: ok,
    caps: leverCaps,
    terms_saved: termsFor(ok),
    savings: round2((termsFor(ok) * annual) / tpy),
    counted: Math.floor(ok / cpt) > 0,
    reason: requested > 0 && Math.floor(ok / cpt) === 0 && (reason === 'bounded_by_verified_cap' || kind === 'exam_credits') ? 'less_than_one_term' : reason,
    requires_confirmation: true,
  })
  return {
    ...head,
    status: 'ok',
    cost: { ...costOut!, annual, tuition, mandatory_fees: fees, total_cost_of_attendance: coa },
    years,
    years_source: a.years == null ? 'level_default' : 'assumption',
    baseline_total: baseline,
    levers: [lever('prior_credits', prior, priorOk, caps, priorReason), lever('exam_credits', exam, examOk, examCaps, examReason)],
    credit_savings: {
      certainty: 'potential',
      assumes: ['counted_credit_applies_to_the_degree', 'schedule_allows_finishing_early'],
      mechanism: 'fewer_terms',
      billing_structure: 'unknown',
      credits_counted: total,
      residency_requirement_credits: resReq,
      outside_credit_max: outsideMax,
      terms_saved: terms,
      remainder_credits: total - terms * cpt,
      by_component: {
        tuition: tuition == null ? null : round2((terms * tuition) / tpy),
        mandatory_fees: fees == null ? null : round2((terms * fees) / tpy),
        living_and_other: basis === 'cost_of_attendance' && living != null ? round2((terms * living) / tpy) : null,
      },
      requires_confirmation: true,
    },
    optimized_total: baseline - savings,
    savings_total: savings,
    not_counted: notCounted,
  }
}

export function projectCosts(comparisons: InstitutionComparison[], year: string, a: CostAssumptions): CostProjectionResult {
  return {
    academic_year: year,
    assumptions: {
      residency: a.residency,
      cost_basis: a.cost_basis ?? 'tuition_and_fees',
      years: a.years ?? null,
      prior_credits: a.prior_credits ?? 0,
      exam_credits: a.exam_credits ?? 0,
      credits_per_term: a.credits_per_term ?? 15,
      terms_per_year: a.terms_per_year ?? 2,
    },
    prices_held_constant: true,
    guaranteed: false,
    definition: 'v2',
    institutions: comparisons.map((c) => projectRow(c, year, a)),
  }
}

/** Money the family entered (from an award letter or their own plan). Never comes from research data. */
export interface FamilyAid {
  /** Grants and scholarships already offered, per academic year. Free money: lowers the price. */
  grantsPerYear: number | null
  /** Planned borrowing per academic year. Not a saving: repaid later, with interest (not modelled). */
  loansPerYear: number | null
  /** Living costs outside the school's academic-year budget (summer, breaks, a 12-month lease), per year. */
  yearRoundLivingPerYear?: number | null
}

const pos = (n: number | null | undefined) => Math.max(n ?? 0, 0)

export interface FullProgram {
  /** Years in the program with no credit assumed: the school's usual length or the family's assumption. */
  years: number
  /** The school's published academic-year price x years. */
  published: number
  /** The family's year-round living number x years (0 when not entered). */
  yearRound: number
  grants: number
  netPrice: number
  borrowed: number
  paidWithoutLoans: number
  loansCapped: boolean
}

/**
 * What the full program costs: published academic-year price for every year, plus the family's own year-round
 * living number, minus grants they were offered for every year. No credit is assumed to shorten anything.
 */
export function fullProgram(row: ProjectionRow, aid: FamilyAid): FullProgram | null {
  if (row.status !== 'ok' || row.baseline_total == null || row.years == null) return null
  const years = row.years
  const published = row.baseline_total
  const yearRound = pos(aid.yearRoundLivingPerYear) * years
  const grants = Math.min(pos(aid.grantsPerYear) * years, published + yearRound)
  const net = published + yearRound - grants
  const wantLoans = pos(aid.loansPerYear) * years
  const borrowed = Math.min(wantLoans, net)
  return { years, published, yearRound, grants: round2(grants), netPrice: round2(net), borrowed: round2(borrowed), paidWithoutLoans: round2(net - borrowed), loansCapped: wantLoans > net }
}

export interface PotentialSaving {
  terms: number
  /** Published price of the terms not attended (tuition and fees, plus academic-year living on full cost). */
  gross: number
  /** Grants the family entered for the terms not attended; they are not paid for terms not enrolled. */
  lostGrants: number
  /** gross - lostGrants. Year-round living is not counted: finishing a term early may not remove a summer. */
  net: number
}

/** A saving under the projection's stated assumptions (credit applies, schedule allows). Never a confirmed shorter degree. */
export function potentialSaving(row: ProjectionRow, aid: FamilyAid, termsPerYear = 2): PotentialSaving | null {
  const s = row.credit_savings
  if (row.status !== 'ok' || !s || s.terms_saved <= 0) return null
  const gross = row.savings_total ?? 0
  const lostGrants = round2((pos(aid.grantsPerYear) * s.terms_saved) / termsPerYear)
  return { terms: s.terms_saved, gross, lostGrants, net: round2(Math.max(gross - lostGrants, 0)) }
}

/** The same terms-to-dollars rule, for whole plan terms shown to be covered (degreeCredit coveredTerms). */
export function termsSaving(row: ProjectionRow, terms: number, aid: FamilyAid, termsPerYear = 2): PotentialSaving | null {
  const annual = row.cost?.annual
  if (row.status !== 'ok' || annual == null || terms <= 0 || row.years == null) return null
  const t = Math.min(terms, row.years * termsPerYear - 1)
  const gross = round2((t * annual) / termsPerYear)
  const lostGrants = round2((pos(aid.grantsPerYear) * t) / termsPerYear)
  return { terms: t, gross, lostGrants, net: round2(Math.max(gross - lostGrants, 0)) }
}
