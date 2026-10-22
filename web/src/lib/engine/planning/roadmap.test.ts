import { describe, expect, it } from 'vitest'
import { buildRoadmap } from './roadmap'
import { examKey } from '../examCredit'
import type { InstitutionComparison, ProjectionRow } from '../../data/types'
import type { PlanningProfile } from './types'

const plan = (status = 'verified') => ({
  program_key: 'biz',
  requirement_key: 'biz-plan',
  requirement_kind: 'program_plan',
  verification_status: status,
  source_url: 'https://example.edu/plan.pdf',
  rule_details: {
    catalog_year: '2026-2027',
    terms: [
      { term_index: 1, label: 'Fall 1', credit_hours: '15', items: [{ code: 'ECON 101', credits: 3 }, { code: 'ENGL 101', credits: 3 }] },
      { term_index: 2, label: 'Spring 1', credit_hours: '15', items: [{ code: 'ACCT 201', credits: 3 }] },
    ],
  },
})
const school = (planStatus = 'verified', tableStatus = 'verified'): InstitutionComparison => ({
  institution_key: 'x',
  found: true,
  institution: { display_name: 'Example U', state_code: 'TN', verification_status: 'verified' } as never,
  academic_year: '2026-27',
  missing_domains: [],
  can_offer_paid_addon: false,
  domains: {
    academic_programs: [{ program_key: 'biz', program_name: 'Business, B.S.', verification_status: 'verified' }],
    degree_requirements: [plan(planStatus), { program_key: 'biz', requirement_kind: 'total_credits', minimum_credits: 120, verification_status: 'verified' }],
    credit_policies: [
      {
        policy_kind: 'AP',
        verification_status: tableStatus,
        source_url: 'https://example.edu/ap',
        equivalencies: [
          { exam_or_course_code: 'AP-MI', exam_or_course_name: 'AP Microeconomics', minimum_score: '3', institution_course_equivalent: 'ECON 101', credits_awarded: 3 },
          { exam_or_course_code: 'AP-EL', exam_or_course_name: 'AP English Language', minimum_score: '4', institution_course_equivalent: 'ENGL 101', credits_awarded: 3 },
          { exam_or_course_code: 'AP-AR', exam_or_course_name: 'AP Art History', minimum_score: '3', institution_course_equivalent: 'ARTH 1XX', credits_awarded: 3 },
        ],
      },
    ],
    costs: [{ residency: 'in_state', total_cost_of_attendance: 30000, verification_status: 'verified', living_arrangements: [{ arrangement: 'on_campus', total_cost_of_attendance: 30000 }] }],
  } as never,
})
const profile = (exams: [string, number][]): PlanningProfile => ({
  gradeLevel: 9,
  graduationYear: 2030,
  homeState: 'TN',
  interests: [],
  livingArrangement: null,
  exams: exams.map(([name, score]) => ({ family: 'AP', key: examKey('AP', name), name, score })),
})
const projection = { institution_key: 'x', status: 'ok', years: 4, cost: { annual: 30000 } } as unknown as ProjectionRow

describe('planning roadmap (#194)', () => {
  it('a whole covered term is credit coverage only: no time or money saving without records that the student could finish sooner', () => {
    const r = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection, aid: { grantsPerYear: 4000, loansPerYear: null } })
    expect(r.status).toBe('ready')
    expect(r.plan.value!.terms.map((t) => t.covered)).toEqual([true, false])
    expect(r.coverage).toMatchObject({ value: { termsCovered: 1, termsInPlan: 2 }, evidence: { state: 'estimate' } })
    expect(r.coverage.evidence.method).toMatch(/not a shorter degree/)
    // Withheld: prerequisites, availability, sequencing and remaining requirements aren't shown by any record.
    expect(r.earlyCompletion).toEqual({ supported: false, missing: ['prerequisites', 'course_availability', 'sequencing', 'remaining_requirements'] })
    expect(r.savings.value).toBeNull()
    expect(r.savings.evidence.missing).toMatch(/prerequisites.*offered.*order.*graduation requirement/s)
  })

  it('a saving appears only when every completion condition is shown by a verified record', () => {
    const ok = { verified: true as const, sourceUrl: 'https://example.edu/catalog', institutionKey: 'x', planKey: 'biz-plan', terms: [1] }
    const partial = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection, completionEvidence: { prerequisites: ok, course_availability: ok, sequencing: ok } })
    expect(partial.savings.value).toBeNull()
    expect(partial.earlyCompletion.missing).toEqual(['remaining_requirements'])
    const full = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection, aid: { grantsPerYear: 4000, loansPerYear: null }, completionEvidence: { prerequisites: ok, course_availability: ok, sequencing: ok, remaining_requirements: ok } })
    expect(full.savings.value).toMatchObject({ terms: 1, gross: 15000, lostGrants: 2000, net: 13000 })
    // Evidence without a source is not evidence.
    const noSource = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection, completionEvidence: { prerequisites: ok, course_availability: ok, sequencing: ok, remaining_requirements: { ...ok, sourceUrl: '' } } })
    expect(noSource.savings.value).toBeNull()
    // Evidence for another plan of the major is not evidence for this one.
    const otherPlan = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection, completionEvidence: { prerequisites: { ...ok, planKey: 'x' }, course_availability: ok, sequencing: ok, remaining_requirements: ok } })
    expect(otherPlan.savings.value).toBeNull()
    expect(noSource.savings.value).toBeNull()
  })

  it('elective-only and below-minimum credit never fill a row', () => {
    const r = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([['AP Art History', 5], ['AP English Language', 3]]), projection })
    expect(r.credit.map((c) => c.fit)).toEqual(['elective_only', 'none'])
    expect(r.coverage.value).toBeNull()
    expect(r.savings.value).toBeNull()
  })

  it('records not verified are missing lines, never facts', () => {
    const blocked = buildRoadmap({ comparison: school('partially_verified'), programKey: 'biz', profile: profile([['AP Microeconomics', 5]]) })
    expect(blocked.status).toBe('blocked')
    expect(blocked.credit[0]).toMatchObject({ fit: 'unknown', acceptance: { evidence: { state: 'verified' } } })
    expect(blocked.unknowns[0]!.text).toMatch(/plan for this major is on file but not yet verified/)
    const noTable = buildRoadmap({ comparison: school('verified', 'partially_verified'), programKey: 'biz', profile: profile([['AP Microeconomics', 5]]) })
    expect(noTable.status).toBe('partial')
    expect(noTable.credit[0]!.acceptance).toMatchObject({ value: null, evidence: { state: 'missing' } })
    expect(noTable.options).toEqual([])
  })

  it('options list each exam whose course fills a plan row, at its published minimum', () => {
    const r = buildRoadmap({ comparison: school(), programKey: 'biz', profile: profile([]) })
    expect(r.options.map((o) => [o.examName, o.minimumText, o.course, o.rows[0]!.term])).toEqual([
      ['AP English Language', '4', 'ENGL 101', 1],
      ['AP Microeconomics', '3', 'ECON 101', 1],
    ])
  })

  it('a school with no exam-credit table on file is never "ready", and says so', () => {
    const c = school()
    ;(c.domains as unknown as Record<string, unknown[]>).credit_policies = []
    const r = buildRoadmap({ comparison: c, programKey: 'biz', profile: profile([]) })
    expect(r.status).toBe('partial')
    expect(r.unknowns.map((u) => u.text)).toContain('No exam-credit table (AP, CLEP, IB or Statewide Dual Credit) is on file for Example U.')
  })

  it('#230: year headings are not terms, and credit rows use the term numbers shown on the plan', () => {
    const c = school()
    const recs = (c.domains as unknown as { degree_requirements: { rule_details?: { terms: unknown[] } }[] }).degree_requirements
    recs[0]!.rule_details!.terms = [{ term_index: 1, label: 'Year One', items: [] }, ...(recs[0]!.rule_details!.terms as object[]).map((t, i) => ({ ...t, term_index: i + 2 }))]
    const r = buildRoadmap({ comparison: c, programKey: 'biz', profile: profile([['AP Microeconomics', 4]]), projection })
    expect(r.plan.value!.terms.map((t) => [t.term, t.label, t.group])).toEqual([[1, 'Fall 1', 'Year One'], [2, 'Spring 1', 'Year One']])
    expect(r.credit[0]!.rows.map((x) => x.term)).toEqual([1])
  })

  it('#230: a summer term, or a term under 12 printed hours, is never a term saved', () => {
    const c = school()
    const recs = (c.domains as unknown as { degree_requirements: { rule_details?: { terms: { label: string; credit_hours?: string }[] } }[] }).degree_requirements
    const terms = recs[0]!.rule_details!.terms
    terms[0] = { ...terms[0]!, label: 'Summer' }
    const summer = buildRoadmap({ comparison: c, programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection })
    expect(summer.plan.value!.terms[0]).toMatchObject({ covered: false, notChecked: 'short_term' })
    expect(summer.savings.value).toBeNull()
    terms[0] = { ...terms[0]!, label: 'Fall 1', credit_hours: '6' }
    const light = buildRoadmap({ comparison: c, programKey: 'biz', profile: profile([['AP Microeconomics', 4], ['AP English Language', 4]]), projection })
    expect(light.plan.value!.terms[0]).toMatchObject({ covered: false, notChecked: 'hours' })
    expect(light.savings.value).toBeNull()
  })
})
