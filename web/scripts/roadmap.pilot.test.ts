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
  it('UTC Management today: plan verified; credit table and cost not yet verified, so they are listed as missing, never shown', () => {
    const r = buildRoadmap({ comparison: comparison('utc', '221740'), programKey: 'management-b-s-b-a', profile: persona })
    expect(r.status).toBe('partial')
    expect(r.target.programName).toBe('Management, B.S.B.A.')
    expect(r.plan.evidence.state).toBe('verified')
    expect(r.plan.value).toMatchObject({ catalogYear: '2026-2027', totalCredits: 120 })
    expect(r.plan.value!.terms).toHaveLength(8)
    expect(r.credit.every((x) => x.acceptance.value === null && x.acceptance.evidence.state === 'missing')).toBe(true)
    expect(r.options).toEqual([])
    expect(r.cost.value).toBeNull()
    expect(r.savings.value).toBeNull()
    expect(r.unknowns.map((u) => u.text)).toEqual(
      expect.arrayContaining([
        expect.stringMatching(/AP credit table is on file but not verified \(partially_verified\)/),
        expect.stringMatching(/cost of attendance is on file but not verified/),
        expect.stringMatching(/dual-enrollment policy is on file but not verified/),
      ]),
    )
  })

  it('UTC Management once #191 verifies the tables and cost: 12 hours fill named rows, two exams accepted but not in plan, no timeline', () => {
    const c = asIfVerified(comparison('utc', '221740'), ['credit_policies', 'costs'])
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
    // Timeline and savings: no whole term covered, so none shown.
    expect(r.timeline.value).toBeNull()
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

  it('UTK: credit tables and cost verified, but no business plan on file, so the roadmap is blocked; hours missing on every row', () => {
    const r = buildRoadmap({ comparison: comparison('utk', '221759'), programKey: 'management-bsba', profile: persona })
    expect(r.status).toBe('blocked')
    expect(r.plan.value).toBeNull()
    const micro = r.credit.find((x) => x.exam.name === 'AP Microeconomics')!
    expect(micro.acceptance.evidence.state).toBe('verified')
    expect(micro.acceptance.value!.status).toBe('qualifies')
    expect(micro.fit).toBe('unknown')
    expect(micro.hours.value).toBeNull()
    expect(r.cost.value?.length).toBeGreaterThan(0)
    expect(r.options).toEqual([])
    expect(r.unknowns[0]!.text).toMatch(/no term-by-term plan on file for this major/)
  })
})
