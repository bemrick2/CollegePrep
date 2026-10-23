// #194: the planning engine on the stored Tennessee pilot records (data/institutions), for a fictional 9th grader
// interested in business. Reads the repository's files with Node's fs; nothing is imported or promoted.
import { readdirSync, readFileSync, existsSync } from 'node:fs'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { buildRoadmap } from '../src/lib/engine/planning/roadmap'
import { examKey, type PlannedExam } from '../src/lib/engine/examCredit'
import { projectRow } from '../src/lib/engine/costProjection'
import type { InstitutionComparison } from '../src/lib/data/types'
import type { PlanningProfile } from '../src/lib/engine/planning/types'

const ROOT = join(__dirname, '../../data')
type Rec = Record<string, unknown>
const DOMAINS = ['costs', 'awards', 'appeals', 'credit_policies', 'academic_programs', 'transfer_policies', 'admissions_metrics', 'degree_requirements']

function domainRecords(school: string, domain: string, year: string): Rec[] {
  const dir = join(ROOT, 'institutions', school, domain)
  if (!existsSync(dir)) return []
  // The record year (or the nearest file) the comparison serves: exact year first, as compare_institutions does.
  const files = readdirSync(dir).filter((f) => f.endsWith('.json'))
  const f = files.find((x) => x === `${year}.json`) ?? (domain === 'awards' ? files.sort().at(-1) : undefined)
  if (!f) return []
  const d = JSON.parse(readFileSync(join(dir, f), 'utf8'))
  return ((d.records ?? []) as Rec[]).map((r) => ({ academic_year: d.academic_year, ...r }))
}

function identity(school: string, unitid: string): Rec {
  const own = join(ROOT, 'institutions', school, 'institution.json')
  if (existsSync(own)) return JSON.parse(readFileSync(own, 'utf8'))
  const csv = readFileSync(join(ROOT, 'national/ipeds/2023-24/TN/institutions.csv'), 'utf8').trim().split('\n')
  const head = csv[0]!.split(',')
  const row = csv.find((l) => l.split(',')[2] === unitid)!.split(',')
  return Object.fromEntries(head.map((h, i) => [h, row[i]]))
}

function comparison(school: string, unitid: string, year = '2026-27'): InstitutionComparison {
  const domains = Object.fromEntries(DOMAINS.map((d) => [d, domainRecords(school, d, year)]))
  return { institution_key: school, found: true, institution: identity(school, unitid) as never, academic_year: year, domains: domains as never, missing_domains: [], can_offer_paid_addon: false }
}

/** Test-only: what Research's #191 would change (records marked verified in memory). Never written anywhere. */
function asIfVerified(c: InstitutionComparison, domains: string[]): InstitutionComparison {
  const d = Object.fromEntries(Object.entries(c.domains).map(([k, rs]) => [k, domains.includes(k) ? (rs as Rec[]).map((r) => ({ ...r, verification_status: 'verified' })) : rs]))
  return { ...c, domains: d as never }
}

const ap = (name: string, score: number | null): PlannedExam => ({ family: 'AP', key: examKey('AP', name), name, score })
const persona: PlanningProfile = {
  gradeLevel: 9,
  graduationYear: 2030,
  homeState: 'TN',
  interests: [{ kind: 'area', key: 'business' } as never],
  exams: [ap('AP Microeconomics', 3), ap('AP Macroeconomics', 3), ap('AP English Language and Composition', 4), ap('AP Calculus AB', 3), ap('AP Statistics', 3)],
  livingArrangement: null,
}
const have = existsSync(join(ROOT, 'institutions/utc')) && existsSync(join(ROOT, 'institutions/utk'))

describe.skipIf(!have)('planning roadmap on the stored Tennessee pilot records (#194)', () => {
  it('UTC Management today: the plan is on file but not verified (a printed note isn’t captured, 2026-10-23), so it isn’t shown and no credit is placed in it', () => {
    const r = buildRoadmap({ comparison: comparison('utc', '221740'), programKey: 'management-b-s-b-a', profile: persona })
    expect(r.status).toBe('blocked')
    expect(r.target.programName).toBe('Management, B.S.B.A.')
    expect(r.plan.value).toBeNull()
    expect(r.plan.evidence).toMatchObject({ state: 'missing', verificationStatus: 'partially_verified', notesCapture: 'incomplete', missing: 'Plan on file but not verified.' })
    // Never "no plan": the plan exists, and the reason it isn't shown is stated.
    expect(r.unknowns.find((u) => u.topic === 'plan')?.text).toMatch(/plan for this major is on file but not yet verified: its course rows were checked, but a note printed with it, which can change what it requires, isn’t captured yet/)
    expect(r.credit.every((x) => x.acceptance.value === null && x.rows.length === 0)).toBe(true)
    expect(r.options).toEqual([])
    // #206: cost verified from the raw 2026-27 PDF; shown as published, by living arrangement.
    expect(r.cost.evidence).toMatchObject({ state: 'verified', publishedYear: '2026-27' })
    expect(r.cost.value).toEqual(
      expect.arrayContaining([
        { arrangement: 'on_campus', annual: 30340 },
        { arrangement: 'off_campus', annual: 29936 },
        { arrangement: 'with_family', annual: 23736 },
      ]),
    )
    expect(r.coverage.value).toBeNull()
    expect(r.savings.value).toBeNull()
    expect(r.unknowns.map((u) => u.text)).toEqual(
      expect.arrayContaining([
        expect.stringMatching(/AP credit table is on file but not yet verified: the values were checked, but the page prints no academic year/),
        expect.stringMatching(/dual-enrollment policy is on file but not yet verified/),
        expect.stringMatching(/No verified plan for a saved major is on file, so no time or money saved is shown/),
      ]),
    )
    expect(r.unknowns.some((u) => u.topic === 'cost')).toBe(false)
  })

  it('the plan reason wording covers every unverified plan: notes missing with or without reviewed rows, and other statuses', () => {
    const withPlan = (patch: Rec) => {
      const c = comparison('utc', '221740')
      const reqs = (c.domains.degree_requirements as Rec[]).map((r) => (r.program_key === 'management-b-s-b-a' && r.requirement_kind === 'program_plan' ? { ...r, ...patch } : r))
      return buildRoadmap({ comparison: { ...c, domains: { ...c.domains, degree_requirements: reqs } as never }, programKey: 'management-b-s-b-a', profile: persona })
    }
    const why = (r: ReturnType<typeof withPlan>) => r.unknowns.find((u) => u.topic === 'plan')?.text ?? ''
    expect(why(withPlan({ captured_rows_reviewed: false }))).toMatch(/not yet verified: a note printed with it, which can change what it requires, isn’t captured yet/)
    for (const status of ['unverified', 'stale']) {
      const r = withPlan({ verification_status: status, notes_capture: undefined })
      expect(r).toMatchObject({ status: 'blocked', plan: { value: null, evidence: { verificationStatus: status, missing: 'Plan on file but not verified.' } } })
    }
  })

  // Scenario, not today's data: the plan's note captured and its replacement reviewed (#218), and #191's tables verified.
  it('UTC Management once its plan note is captured and reviewed and #191 verifies the tables and cost: 12 hours fill named rows, two exams accepted but not in plan, no timeline', () => {
    const c = asIfVerified(comparison('utc', '221740'), ['credit_policies', 'costs', 'degree_requirements'])
    const r = buildRoadmap({ comparison: c, programKey: 'management-b-s-b-a', profile: persona, projection: projectRow(c, '2026-27', { residency: 'in_state', cost_basis: 'cost_of_attendance' }) })
    expect(r.status).toBe('ready')
    const by = Object.fromEntries(r.credit.map((x) => [x.exam.name, x]))
    expect(by['AP Microeconomics']).toMatchObject({ fit: 'applies', rows: [expect.objectContaining({ term: 3 })] })
    expect(by['AP Macroeconomics']).toMatchObject({ fit: 'applies', rows: [expect.objectContaining({ term: 4 })] })
    expect(by['AP English Language and Composition']!.rows.map((x) => x.term)).toEqual([1, 2])
    expect(by['AP Calculus AB']).toMatchObject({ fit: 'accepted_not_in_plan', hours: { value: 4 } })
    expect(by['AP Statistics']!.fit).toBe('accepted_not_in_plan')
    expect(r.credit.filter((x) => x.fit === 'applies').reduce((s, x) => s + (x.hours.value ?? 0), 0)).toBe(12)
    expect(r.unknowns.map((u) => u.text)).toEqual(expect.arrayContaining([expect.stringMatching(/awards MATH 1950 for AP Calculus AB, but this major's plan lists other courses/)]))
    // Coverage and savings: no whole term covered, so none shown.
    expect(r.coverage.value).toBeNull()
    expect(r.savings.value).toBeNull()
    // Cost by arrangement, as published, labelled with its year.
    expect(r.cost.value).toEqual(
      expect.arrayContaining([
        { arrangement: 'on_campus', annual: 30340 },
        { arrangement: 'off_campus', annual: 29936 },
        { arrangement: 'with_family', annual: 23736 },
      ]),
    )
    expect(r.cost.evidence.publishedYear).toBe('2026-27')
    // Dual enrollment as published: grades 11-12, 3.0 GPA; no course list.
    expect(r.dualEnrollment.value).toMatchObject({ grades: ['11', '12'], minHsGpa: 3, stateGrantAccepted: true })
    // Options: every exam whose course fills a Management row, e.g. CLEP College Algebra -> MATH 1130 (term 1).
    expect(r.options.find((o) => o.examName === 'CLEP College Algebra')).toMatchObject({ course: 'MATH 1130', rows: [expect.objectContaining({ term: 1 })] })
    expect(r.options.every((o) => o.rows.length > 0 && o.evidence.state === 'verified')).toBe(true)
  })

  it('UTK: credit tables partially verified (academic year unconfirmed, owner-approved 2026-10-22) and no business plan on file, so the roadmap is blocked', () => {
    const r = buildRoadmap({ comparison: comparison('utk', '221759'), programKey: 'management-bsba', profile: persona })
    expect(r.status).toBe('blocked')
    expect(r.plan.value).toBeNull()
    const micro = r.credit.find((x) => x.exam.name === 'AP Microeconomics')!
    // The table is kept and shown as on file, but not as a fact: its academic year is unconfirmed. Not rejected.
    expect(micro.acceptance.value).toBeNull()
    expect(micro.acceptance.evidence).toMatchObject({ state: 'missing', verificationStatus: 'partially_verified' })
    const why = r.unknowns.map((u) => u.text).find((t) => /AP credit table/.test(t))!
    expect(why).toMatch(/on file but not yet verified: the values were checked, but the page prints no academic year/)
    expect(why).not.toMatch(/reject|discontinu|no longer/i)
    // Its own fit, so no screen reading `fit` can say "No credit at this score" for a table that just isn't verified.
    expect(micro.fit).toBe('not_verified')
    expect(micro.hours.value).toBeNull()
    expect(r.cost.value?.length).toBeGreaterThan(0)
    expect(r.options).toEqual([])
    expect(r.unknowns[0]!.text).toMatch(/no term-by-term plan on file for this major/)
  })
})

describe.skipIf(!have)('UTC cost breakdown as printed (#206)', () => {
  it('one "Enrollment Fees" line is shown as printed, never split; out of state adds the printed out-of-state tuition', async () => {
    const { printedTuitionLines } = await import('../src/features/colleges/CollegeDetail')
    const [inState, outState] = ['in_state', 'out_of_state'].map((r) => domainRecords('utc', 'costs', '2026-27').find((c) => c.residency === r)!)
    expect(printedTuitionLines(inState as never)).toEqual([{ label: 'Tuition and fees (one line, as printed)', amount: 11084 }])
    expect(printedTuitionLines(outState as never)).toEqual([
      { label: 'Tuition and fees (one line, as printed)', amount: 11084 },
      { label: 'Out-of-state tuition', amount: 8306 },
    ])
    // UTK prints tuition and fees apart, so the normal two lines apply.
    expect(printedTuitionLines(domainRecords('utk', 'costs', '2026-27')[0] as never)).toBeNull()
  })
})
