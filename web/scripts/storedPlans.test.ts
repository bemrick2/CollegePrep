// Lives outside src/ because it reads the repository's stored records with Node's fs.
//
// #171: every stored degree plan (data/institutions/*/degree_requirements) goes through the shared plan reader and
// the two modules that read plans, whatever extractor wrote its items. Runs in the normal suite.
import { readdirSync, readFileSync, existsSync } from 'node:fs'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { readTermItems, entryCodes, type PlanTermLike } from '../src/lib/engine/planItems'
import { degreeCredit } from '../src/lib/engine/degreeCredit'
import { examKey, summarizeSchool, type CreditPolicy } from '../src/lib/engine/examCredit'
import { schoolFit } from '../src/lib/engine/programFit'
import { MAJORS } from '../src/lib/engine/interests'

const ROOT = join(__dirname, '../../data/institutions')
type Rec = { program_key?: string; rule_details?: { terms?: PlanTermLike[] } }
const read = (school: string, domain: string): Rec[] => {
  const dir = join(ROOT, school, domain)
  if (!existsSync(dir)) return []
  return readdirSync(dir)
    .filter((f) => f.endsWith('.json'))
    .flatMap((f) => {
      const d = JSON.parse(readFileSync(join(dir, f), 'utf8'))
      return (Array.isArray(d) ? d : d.records ?? []) as Rec[]
    })
}
const schools = existsSync(ROOT) ? readdirSync(ROOT).filter((s) => existsSync(join(ROOT, s, 'degree_requirements'))) : []

describe.skipIf(!schools.length)('every stored degree plan reads (#171)', () => {
  it('no item lost or thrown on, in any format; both plan readers run on every school', () => {
    let raw = 0
    let objects = 0
    let read_ = 0
    const withObjects = new Set<string>()
    const interests = MAJORS.slice(0, 60).map((m) => ({ kind: 'major' as const, key: m.key }))
    for (const s of schools) {
      const plans = read(s, 'degree_requirements')
      for (const p of plans)
        for (const t of p.rule_details?.terms ?? []) {
          for (const it of t.items ?? []) {
            if (typeof it === 'object' && it) {
              objects++
              withObjects.add(s)
            }
            const empty = typeof it === 'string' ? !it.trim() : !it || Object.values(it).every((v) => v === '' || v == null)
            if (!empty) raw++
          }
          const entries = readTermItems(t)
          read_ += entries.length
          for (const e of entries) entryCodes(e)
        }
      for (const p of plans) if (p.rule_details?.terms?.length) expect(() => degreeCredit([], p.rule_details!.terms!)).not.toThrow()
      expect(() => schoolFit({ degree_requirements: plans, academic_programs: read(s, 'academic_programs') }, interests)).not.toThrow()
    }
    expect(read_).toBe(raw)
    // At the time of writing: about 100,000 items, a third of them objects, at 30 schools.
    expect(objects).toBeGreaterThan(20_000)
    expect(withObjects.size).toBeGreaterThanOrEqual(28)
  }, 60_000)
})

type Plan = Rec & { requirement_kind?: string; rule_details?: { terms?: PlanTermLike[] } }
describe.skipIf(!schools.includes('utc'))('UTC Clear Path alternatives printed in titles (#192)', () => {
  // Stored files, not a fixture; tables are read as published (their verification status is not this test's subject).
  const policies = read('utc', 'credit_policies') as unknown as CreditPolicy[]
  const plan = (k: string) => (read('utc', 'degree_requirements') as Plan[]).find((r) => r.program_key === k && r.requirement_kind === 'program_plan')!.rule_details!.terms!
  const calc = [{ family: 'AP' as const, key: examKey('AP', 'AP Calculus AB'), name: 'AP Calculus AB', score: 3 }]

  it('Management: the math row is "MATH 1130 or MATH 1830"; AP Calculus AB (MATH 1950) still does not apply', () => {
    const row = readTermItems(plan('management-b-s-b-a')[0]!).find((e) => e.code === 'MATH 1130')!
    expect(entryCodes(row)).toEqual(['MATH 1130', 'MATH 1830'])
    expect(degreeCredit(summarizeSchool(policies, calc).matches, plan('management-b-s-b-a')).accepted[0]).toMatchObject({ course: 'MATH 1950', status: 'not_in_plan' })
  })

  it('General Biology lists MATH 1950 among the options, so the same credit applies there', () => {
    const r = degreeCredit(summarizeSchool(policies, calc).matches, plan('biology-general-biology-b-s'))
    expect(r.accepted[0]).toMatchObject({ course: 'MATH 1950', status: 'applies' })
    expect(r.accepted[0]!.matched[0]).toMatchObject({ code: 'MATH 1950', term: 2 })
  })
})

describe.skipIf(!schools.includes('utk'))('stored IB and Statewide Dual Credit tables (#197)', () => {
  it('UTK IB and SDC rows match; UTC IB minimums printed as "SL & HL" are read-the-criteria, never credit', () => {
    const utk = read('utk', 'credit_policies') as unknown as CreditPolicy[]
    const econ = { family: 'IB' as const, key: examKey('IB', 'Economics'), name: 'IB Economics', score: 5, level: 'SL' as const }
    expect(summarizeSchool(utk, [econ]).matches[0]).toMatchObject({ status: 'qualifies' })
    const bus = { family: 'SDC' as const, key: examKey('SDC', 'Introduction to Business'), name: 'Statewide Dual Credit Introduction to Business', score: 80 }
    expect(summarizeSchool(utk, [bus]).matches[0]!.earned[0]).toMatchObject({ course: 'BUAD LD (3 credits)', credits: 3 })
    const utc = read('utc', 'credit_policies') as unknown as CreditPolicy[]
    expect(summarizeSchool(utc, [{ ...econ, level: 'HL', score: 7 }]).matches[0]!.status).toBe('read_criteria')
  })
})
