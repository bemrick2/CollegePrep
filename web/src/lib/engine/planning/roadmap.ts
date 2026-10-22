/**
 * One student, one school, one major: what the school's records say about the exams the family entered, where that
 * credit lands in the major's plan, what it costs, and what isn't on file (#194, docs/product/PLANNING_ENGINE.md).
 *
 * Composition only. Acceptance is examCredit's, plan fit is degreeCredit's (planItems reads every plan format), the
 * applicable price is residency's, savings are costProjection's whole-term rule. Records that aren't `verified` are
 * never used for a fact: they become `missing` lines that say what isn't verified. Nothing is projected forward a
 * year, and no score is predicted.
 */
import type { InstitutionComparison, ProjectionRow } from '../../data/types'
import { degreeCredit, type ExamApplicability } from '../degreeCredit'
import { FAMILY_LABEL, examOptions, matchExam, policyKindOf, type CreditPolicy, type ExamFamily, type ExamMatch, type IbLevel, type PlannedExam } from '../examCredit'
import { termsSaving, type FamilyAid } from '../costProjection'
import { gatedSaving, withheldReason, type CompletionEvidence } from '../earlyCompletion'
import { pickCost } from '../residency'
import { planTerms, type PlanTermLike } from '../planItems'
import type { CostByArrangement, CreditFit, CreditLine, DualEnrollmentFacts, Evidence, ExamOption, LivingArrangement, PlanCourseRow, PlanRow, PlanningProfile, Roadmap, Unknown } from './types'

type Rec = Record<string, unknown>

export interface RoadmapInput {
  comparison: InstitutionComparison
  programKey: string
  /** Which of the major's plans (requirement_key); default the first one printed. */
  planKey?: string | null
  profile: PlanningProfile
  /** The school's cost_projection row (server in live, projectRow in demo). Savings need it. */
  projection?: ProjectionRow | null
  aid?: FamilyAid
  /** Verified records that the student could finish sooner (earlyCompletion.ts). None exist today. */
  completionEvidence?: CompletionEvidence
}

const str = (v: unknown): string | null => (typeof v === 'string' && v.trim() ? v.trim() : null)
const num = (v: unknown): number | null => (typeof v === 'number' && Number.isFinite(v) ? v : null)
const verified = (r: Rec | null | undefined) => r?.verification_status === 'verified'

function evidence(r: Rec | null | undefined, year: string | null, extra: Partial<Evidence> = {}): Evidence {
  return {
    state: verified(r) ? 'verified' : 'missing',
    sourceUrl: str(r?.source_url) ?? str(r?.policy_url),
    verificationStatus: str(r?.verification_status),
    academicYearBasis: str(r?.academic_year_basis),
    lastVerifiedAt: str(r?.last_verified_at),
    publishedYear: year,
    ...extra,
  }
}
/** Why a record isn't a fact yet, in plain words (the record's own status stays in the evidence). */
function notVerifiedWhy(r: Rec): string {
  if (r.verification_status === 'partially_verified' && /unlabeled/.test(String(r.academic_year_basis ?? '')))
    return ': the values were checked, but the page prints no academic year'
  return r.verification_status === 'partially_verified' ? ': some of its values are still being checked' : ''
}
const missing = (text: string, r?: Rec | null, year: string | null = null): Evidence => ({ ...evidence(r ?? null, year), state: 'missing', missing: text })

const ARRANGEMENT_WORDS: Record<LivingArrangement, string> = { on_campus: 'on campus', off_campus: 'off campus', with_family: 'with family' }
const ARRANGEMENT: Record<string, LivingArrangement> = {
  on_campus: 'on_campus',
  off_campus_not_with_family: 'off_campus',
  off_campus: 'off_campus',
  with_parents_or_family: 'with_family',
  with_family: 'with_family',
}

function fitOf(a: ExamApplicability | undefined, hasPlan: boolean): CreditFit {
  if (!a) return 'none'
  if (!hasPlan) return 'unknown'
  switch (a.status) {
    case 'applies':
      return 'applies'
    case 'partly':
      return 'partly'
    case 'not_in_plan':
      return 'accepted_not_in_plan'
    case 'elective_only':
      return 'elective_only'
    default:
      return 'unknown'
  }
}

/** `numberOf` turns the stored term_index into the term's number as shown (year headings aren't numbered). */
const rowsOf = (a: ExamApplicability | undefined, numberOf: (termIndex: number) => number): PlanRow[] =>
  (a?.matched ?? []).map((m) => ({ term: numberOf(m.term), label: m.label, item: m.item, credits: m.credits }))

export function buildRoadmap({ comparison: c, programKey, planKey = null, completionEvidence = {}, profile, projection = null, aid = { grantsPerYear: null, loansPerYear: null } }: RoadmapInput): Roadmap {
  const domain = (d: string) => ((c.domains as Record<string, Rec[] | undefined>)[d] ?? []) as Rec[]
  const inst = str(c.institution?.display_name) ?? c.institution_key
  const program = domain('academic_programs').find((p) => p.program_key === programKey) ?? null
  const unknowns: Unknown[] = []
  const unknown = (topic: Unknown['topic'], text: string) => unknowns.some((u) => u.text === text) || unknowns.push({ topic, text })

  // Plan: the major's verified term-by-term plan, and its printed total.
  const reqs = domain('degree_requirements').filter((r) => r.program_key === programKey)
  // A major can have several plans (tracks, concentrations; up to 12 per program). Each is named by its printed
  // title, source_section, so the family can pick the one they mean.
  const planRecs = reqs.filter((r) => r.requirement_kind === 'program_plan')
  const plans = planRecs.map((r) => ({ key: String(r.requirement_key ?? ''), title: str((r.rule_details as Rec | undefined)?.source_section) }))
  const planRec = planRecs.find((r) => planKey != null && r.requirement_key === planKey) ?? planRecs[0] ?? null
  const planDetails = (planRec?.rule_details ?? null) as { catalog_year?: string; source_section?: string; rule_text?: string; terms?: PlanTermLike[] } | null
  const catalogYear = str(planDetails?.catalog_year) ?? str(planRec?.academic_year)
  const terms = verified(planRec) ? (planDetails?.terms ?? []) : []
  const termViews = planTerms(terms)
  const hasPlan = termViews.length > 0
  const numberOf = (termIndex: number) => termViews.find((t) => t.termIndex === termIndex)?.number ?? termIndex
  const totalRec = reqs.find((r) => r.requirement_kind === 'total_credits' && verified(r)) ?? null
  if (!planRec) unknown('plan', `${inst} has no term-by-term plan on file for this major, so credit can be shown as accepted but not where it counts.`)
  else if (!hasPlan) unknown('plan', `${inst}'s plan for this major is on file but not yet verified${notVerifiedWhy(planRec)}.`)

  // Credit: each planned exam against the school's verified table for its family.
  const policies = domain('credit_policies')
  // Every exam-credit table the school has on file, whether or not the family entered exams for it.
  const examTables = policies.filter((p) => (['AP', 'CLEP', 'IB', 'SDC'] as ExamFamily[]).some((f) => policyKindOf(f) === p.policy_kind))
  if (!examTables.length) unknown('credit', `No exam-credit table (AP, CLEP, IB or Statewide Dual Credit) is on file for ${inst}.`)
  for (const t of examTables.filter((x) => !verified(x))) {
    const fam = (['AP', 'CLEP', 'IB', 'SDC'] as ExamFamily[]).find((f) => policyKindOf(f) === t.policy_kind)!
    unknown('credit', `${inst}'s ${FAMILY_LABEL[fam]} credit table is on file but not yet verified${notVerifiedWhy(t)}.`)
  }
  const verifiedPolicies = policies.filter(verified) as unknown as CreditPolicy[]
  const tableFor = (f: ExamFamily) => policies.find((p) => p.policy_kind === policyKindOf(f)) ?? null
  const verifiedTable = (f: ExamFamily) => (verified(tableFor(f)) ? tableFor(f) : null)
  const tableYear = (r: Rec | null) => str(r?.academic_year) ?? c.academic_year

  const matches = profile.exams.map((e): { exam: PlannedExam; m: ExamMatch | null } => ({ exam: e, m: verifiedTable(e.family) ? matchExam(verifiedPolicies, e) : null }))
  const qualifying = matches.filter((x) => x.m?.status === 'qualifies').map((x) => x.m!)
  const dc = degreeCredit(qualifying, terms)
  const accepted = new Map(qualifying.map((m, i) => [m, dc.accepted[i]]))

  const credit: CreditLine[] = matches.map(({ exam, m }) => {
    const t = tableFor(exam.family)
    const label = FAMILY_LABEL[exam.family]
    if (!m) {
      const text = t ? `${inst}'s ${label} credit table is on file but not yet verified${notVerifiedWhy(t)}.` : `No ${label} credit table is on file for ${inst}.`
      unknown('credit', text)
      return { exam, acceptance: { value: null, evidence: missing(text, t, tableYear(t)) }, fit: 'none', rows: [], hours: { value: null, evidence: missing(text, t) } }
    }
    const a = accepted.get(m)
    const fit = fitOf(a, hasPlan)
    if (a && fit === 'accepted_not_in_plan')
      unknown('credit', `${inst} awards ${a.course} for ${exam.name}, but this major's plan lists other courses. Whether ${a.course} can substitute isn't published in the records on file.`)
    if (a && a.status === 'school_assigns') unknown('credit', `For ${exam.name}, ${inst} lists more than one course (${a.course}); which one a student gets isn't on file.`)
    if (a && a.hours == null) unknown('credit', `${inst}'s table lists no credit hours for ${exam.name}.`)
    const ev = evidence(t, tableYear(t))
    return {
      exam,
      acceptance: { value: m, evidence: ev },
      fit,
      rows: rowsOf(a, numberOf),
      hours: a ? (a.hours != null ? { value: a.hours, evidence: ev } : { value: null, evidence: missing(`No hours listed for ${exam.name}.`, t) }) : { value: null, evidence: ev },
    }
  })

  // Options: exams in each verified table whose course fills a row of the verified plan, at each published minimum.
  const options: ExamOption[] = []
  if (hasPlan)
    for (const p of verifiedPolicies) {
      const fam = (['AP', 'CLEP', 'IB', 'SDC'] as ExamFamily[]).find((f) => policyKindOf(f) === p.policy_kind)
      if (!fam) continue
      for (const o of examOptions([[p]])) {
        const levels: (IbLevel | null)[] = fam === 'IB' ? ['SL', 'HL'] : [null]
        for (const level of levels) {
          const base: PlannedExam = { family: fam, key: o.key, name: o.name, score: null, level }
          const mins = [...new Set(matchExam([p], base).thresholds.filter((t) => t.min != null && (!t.levels || (level && t.levels.includes(level)))).map((t) => t.min!))]
          for (const min of mins.sort((x, y) => x - y)) {
            const m = matchExam([p], { ...base, score: min })
            if (m.status !== 'qualifies') continue
            const a = degreeCredit([m], terms).accepted[0]
            if (!a || (a.status !== 'applies' && a.status !== 'partly')) continue
            if (options.some((x) => x.examName === o.name && x.course === a.course && x.level !== level)) continue
            options.push({ family: fam, examName: o.name, minimumText: m.earned[0]!.minimumText, level, course: a.course ?? '', rows: rowsOf(a, numberOf), hours: a.hours, evidence: evidence(p as unknown as Rec, tableYear(p as unknown as Rec)) })
          }
        }
      }
    }
  options.sort((x, y) => (x.rows[0]?.term ?? 99) - (y.rows[0]?.term ?? 99) || x.examName.localeCompare(y.examName))

  // Dual enrollment: eligibility as published. No course equivalencies are on file for any pilot school.
  const deRec = policies.find((p) => p.policy_kind === 'dual_enrollment') ?? null
  const de = (deRec?.dual_enrollment ?? null) as Rec | null
  let dualEnrollment: Roadmap['dualEnrollment']
  if (deRec && verified(deRec) && de) {
    const tiers = (Array.isArray(de.eligibility_tiers) ? de.eligibility_tiers : []) as Rec[]
    const charges = (Array.isArray(de.per_credit_hour_charges) ? de.per_credit_hour_charges : []) as Rec[]
    const facts: DualEnrollmentFacts = {
      grades: [...new Set(tiers.flatMap((t) => (Array.isArray(t.grades) ? (t.grades as string[]) : [])))],
      minHsGpa: num(de.min_hs_gpa),
      altMinAct: num(de.alt_min_act),
      perCreditCharge: charges.length === 1 ? num(charges[0]!.amount) : null,
      stateGrantAccepted: typeof de.state_grant_accepted === 'boolean' ? de.state_grant_accepted : null,
    }
    dualEnrollment = { value: facts, evidence: evidence(deRec, tableYear(deRec)) }
  } else {
    const text = deRec ? `${inst}'s dual-enrollment policy is on file but not yet verified${notVerifiedWhy(deRec)}.` : `No dual-enrollment policy is on file for ${inst}.`
    dualEnrollment = { value: null, evidence: missing(text, deRec) }
    unknown('dual_enrollment', text)
  }
  if (!((deRec?.equivalencies as unknown[] | undefined) ?? []).length)
    unknown('dual_enrollment', `Which dual-enrollment courses ${inst} counts toward this major isn't on file.`)

  // Cost: the verified price that applies to the family, by living arrangement, as published.
  const costRecs = domain('costs')
  const pick = pickCost(costRecs.filter(verified) as unknown as { residency: string; total_cost_of_attendance?: number | null }[], str(c.institution?.state_code), profile.homeState)
  const chosen = pick.cost as unknown as Rec | null
  let cost: Roadmap['cost']
  if (chosen) {
    const byArr: CostByArrangement[] = ((Array.isArray(chosen.living_arrangements) ? chosen.living_arrangements : []) as Rec[])
      .map((l) => ({ arrangement: ARRANGEMENT[String(l.arrangement)], annual: num(l.total_cost_of_attendance) }))
      .filter((l): l is CostByArrangement => !!l.arrangement && l.annual != null)
    const basis =
      pick.basis === 'assumed_in_state'
        ? 'In-state price shown: home state not entered.'
        : pick.basis === 'out_of_state_missing'
          ? 'The school publishes no out-of-state price; the in-state price shown is not this family’s.'
          : undefined
    cost = byArr.length
      ? { value: byArr, evidence: evidence(chosen, str(chosen.academic_year) ?? c.academic_year, basis ? { method: basis } : {}) }
      : { value: null, evidence: missing(`${inst}'s published cost has no breakdown by living arrangement.`, chosen) }
    if (!byArr.length) unknown('cost', `${inst}'s published cost has no breakdown by living arrangement.`)
    else
      for (const a of ['on_campus', 'off_campus', 'with_family'] as LivingArrangement[])
        if (!byArr.some((x) => x.arrangement === a)) unknown('cost', `${inst} doesn't publish a price for living ${ARRANGEMENT_WORDS[a]}.`)
  } else {
    const anyCost = costRecs[0] ?? null
    const text = anyCost ? `${inst}'s cost of attendance is on file but not yet verified${notVerifiedWhy(anyCost)}.` : `No cost of attendance is on file for ${inst}.`
    cost = { value: null, evidence: missing(text, anyCost) }
    unknown('cost', text)
  }

  // Timeline and savings: whole plan terms only.
  const termList = termViews.map((t) => ({
    term: t.number,
    label: t.label,
    group: t.group,
    creditHours: t.creditHours,
    rows: t.entries.map(
      (e): PlanCourseRow => ({ kind: e.kind as PlanCourseRow['kind'], code: e.code, title: e.title, text: e.text, credits: e.credits, note: e.note, milestone: e.milestone, options: e.choices.map((x) => x.text), choose: e.choose }),
    ),
    covered: dc.coveredTerms.some((x) => x.term === t.termIndex),
    notChecked: t.notChecked,
  }))
  const skipped = new Set(termList.map((t) => t.notChecked).filter(Boolean))
  if (skipped.has('multi_term')) unknown('timeline', `${inst}'s plan prints some years as one block, so whether credit covers a whole term isn't checked for those years.`)
  if (skipped.has('short_term')) unknown('timeline', 'Summer and other short sessions are never counted as a covered term.')
  if (skipped.has('quarter_calendar')) unknown('timeline', `${inst}'s plan uses quarters; whole-term coverage is checked only for semester plans.`)
  if (skipped.has('hours')) unknown('timeline', 'Terms with fewer than 12 printed credit hours, or none printed, are never counted as a covered term.')
  const covered = dc.coveredTerms.length
  const coverage: Roadmap['coverage'] =
    hasPlan && covered > 0
      ? {
          value: { termsCovered: covered, termsInPlan: termList.length },
          evidence: {
            ...evidence(planRec, catalogYear),
            state: 'estimate',
            method: 'Whole regular semesters (12 or more printed hours) whose every course is covered by credit the school awards. This is credit coverage, not a shorter degree.',
          },
        }
      : { value: null, evidence: missing(hasPlan ? 'No whole plan term is covered by this credit.' : 'No verified plan, so coverage can’t be checked.', planRec, catalogYear) }

  // Time or money saved needs more than coverage: records showing the student could really finish sooner.
  const { early, saving } = gatedSaving(covered, () => (projection ? termsSaving(projection, covered, aid) : null), completionEvidence, {
    institutionKey: c.institution_key,
    planKey: planRec ? String(planRec.requirement_key ?? '') || null : null,
    terms: dc.coveredTerms.map((t) => t.term),
  })
  const savings: Roadmap['savings'] = saving
    ? { value: saving, evidence: { ...evidence(planRec, c.academic_year), state: 'estimate', method: 'Potential only: the published price of the terms no longer needed, held at this year’s price, minus grants entered for those terms.' } }
    : { value: null, evidence: missing(early.supported ? `No verified cost projection for ${inst}.` : withheldReason(early, hasPlan ? covered : -1), null, c.academic_year) }
  if (!saving) unknown('timeline', savings.evidence.missing!)

  const allCreditVerified = credit.every((x) => x.acceptance.evidence.state === 'verified') && examTables.length > 0 && examTables.every(verified)
  return {
    target: { institutionKey: c.institution_key, programKey, programName: str(program?.program_name), programVerified: verified(program), institutionName: str(c.institution?.display_name) },
    status: !hasPlan ? 'blocked' : allCreditVerified && cost.value ? 'ready' : 'partial',
    plan: hasPlan
      ? {
          value: { catalogYear, title: str(planDetails?.source_section), terms: termList, totalCredits: num(totalRec?.minimum_credits), totalText: /\btotal\b.*\d/i.test(str(planDetails?.rule_text) ?? '') ? str(planDetails?.rule_text) : null },
          evidence: evidence(planRec, catalogYear),
        }
      : { value: null, evidence: missing(planRec ? 'Plan on file but not verified.' : 'No plan on file.', planRec, catalogYear) },
    plans,
    planKey: planRec ? String(planRec.requirement_key ?? '') || null : null,
    credit,
    options,
    dualEnrollment,
    cost,
    savings,
    coverage,
    earlyCompletion: early,
    unknowns,
  }
}
