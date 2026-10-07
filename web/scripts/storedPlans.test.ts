// Lives outside src/ because it reads the repository's stored records with Node's fs.
//
// #171: every stored degree plan (data/institutions/*/degree_requirements) goes through the shared plan reader and
// the two modules that read plans, whatever extractor wrote its items. Runs in the normal suite.
import { readdirSync, readFileSync, existsSync } from 'node:fs'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { readTermItems, entryCodes, type PlanTermLike } from '../src/lib/engine/planItems'
import { degreeCredit } from '../src/lib/engine/degreeCredit'
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
