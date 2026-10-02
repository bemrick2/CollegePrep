import { describe, expect, it } from 'vitest'
import { QUESTIONS, SKILLS, STRATEGIES, TRAPS } from './fixtures'

const EXPECTED_COUNTS: Record<string, number> = {
  'act/english': 10,
  'act/math': 12,
  'act/reading': 8,
  'act/science': 8,
  'sat/reading_writing': 10,
  'sat/math': 10,
}

const sectionKey = (q: { exam_family: string; section: string }) => `${q.exam_family}/${q.section}`

describe('demo fixtures', () => {
  it('has the expected number of questions per exam and section', () => {
    const counts: Record<string, number> = {}
    for (const q of QUESTIONS) counts[sectionKey(q)] = (counts[sectionKey(q)] ?? 0) + 1
    expect(counts).toEqual(EXPECTED_COUNTS)
  })

  it('uses unique question ids', () => {
    const ids = QUESTIONS.map((q) => q.id)
    expect(new Set(ids).size).toBe(ids.length)
  })

  it('has unique skill keys per exam family, and unique strategy and trap keys', () => {
    for (const fam of ['act', 'sat']) {
      const keys = SKILLS.filter((s) => s.exam_family === fam).map((s) => s.skill_key)
      expect(new Set(keys).size).toBe(keys.length)
    }
    expect(new Set(SKILLS.map((s) => s.id)).size).toBe(SKILLS.length)
    expect(new Set(STRATEGIES.map((s) => s.strategy_key)).size).toBe(STRATEGIES.length)
    expect(new Set(TRAPS.map((t) => t.trap_key)).size).toBe(TRAPS.length)
  })

  it('has well-formed answers and distractors', () => {
    for (const q of QUESTIONS) {
      expect(q.accepted_answers.length, q.id).toBeGreaterThan(0)
      if (q.answer_format === 'choice') {
        const keys = q.choices.map((c) => c.key)
        expect(keys, q.id).toEqual(['A', 'B', 'C', 'D'])
        expect(q.accepted_answers, q.id).toHaveLength(1)
        const answer = q.accepted_answers[0]!
        expect(keys, q.id).toContain(answer)
        const wrong = keys.filter((k) => k !== answer).sort()
        expect(q.distractors.map((d) => d.choice).sort(), q.id).toEqual(wrong)
      } else {
        expect(q.choices, q.id).toEqual([])
        expect(q.distractors, q.id).toEqual([])
      }
    }
  })

  it('resolves skill, trap, and strategy references', () => {
    const trapKeys = new Set(TRAPS.map((t) => t.trap_key))
    const strategyKeys = new Set(STRATEGIES.map((s) => s.strategy_key))
    for (const q of QUESTIONS) {
      const skill = SKILLS.find((s) => s.skill_key === q.primary_skill_key)
      expect(skill, q.id).toBeDefined()
      expect(skill!.exam_family, q.id).toBe(q.exam_family)
      expect(skill!.section, q.id).toBe(q.section)
      for (const d of q.distractors) {
        if (d.trap !== null) expect(trapKeys.has(d.trap), `${q.id} trap ${d.trap}`).toBe(true)
      }
      for (const s of q.strategies) {
        expect(strategyKeys.has(s.strategy_key), `${q.id} strategy ${s.strategy_key}`).toBe(true)
      }
    }
  })

  it('marks exactly one strategy as fastest per question', () => {
    for (const q of QUESTIONS) {
      expect(q.strategies.length, q.id).toBeGreaterThanOrEqual(1)
      expect(q.strategies.length, q.id).toBeLessThanOrEqual(2)
      expect(q.strategies.filter((s) => s.is_fastest), q.id).toHaveLength(1)
    }
  })

  it('covers difficulties 1 through 5 in every section', () => {
    for (const key of Object.keys(EXPECTED_COUNTS)) {
      const diffs = new Set(QUESTIONS.filter((q) => sectionKey(q) === key).map((q) => q.difficulty))
      expect([...diffs].sort(), key).toEqual([1, 2, 3, 4, 5])
    }
  })

  it('includes the required numeric items', () => {
    const numeric = (key: string) =>
      QUESTIONS.filter((q) => sectionKey(q) === key && q.answer_format === 'numeric').length
    expect(numeric('act/math')).toBe(2)
    expect(numeric('sat/math')).toBe(2)
  })

  it('has hints and explanations for every item', () => {
    for (const q of QUESTIONS) {
      expect(q.hints.length, q.id).toBeGreaterThanOrEqual(1)
      expect(q.hints.length, q.id).toBeLessThanOrEqual(2)
      expect(q.teaching_explanation.length, q.id).toBeGreaterThan(0)
      expect(q.strategy_explanation.length, q.id).toBeGreaterThan(0)
      expect(q.remember.split(/\s+/).length, q.id).toBeLessThanOrEqual(16)
    }
  })

  it('gives passages to non-math items and leaves no underline markers behind', () => {
    for (const q of QUESTIONS) {
      if (q.section !== 'math') expect(q.passage, q.id).toBeTruthy()
      if (q.passage) expect(q.passage, q.id).not.toMatch(/\{\{|\}\}/)
    }
  })
})
