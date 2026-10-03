import { describe, expect, it } from 'vitest'
import { parentActions, type ActionInput } from './actions'

const base: ActionInput = {
  name: 'Maya', exam: 'act', linked: true, benchmarks: 1,
  schedule: { kind: 'mini', inDays: 10, dueDate: '2026-10-12', overdueDays: 0 },
  focus: [{ section: 'math', label: 'Math', kind: 'knowledge', detail: 'Linear equations: 44% right.' }],
  behind: null, idleDays: 0, goals: ['merit'], targetScore: 27, officialScore: null,
  schools: [
    { name: 'CBU', levers: [], awards: [{ name: 'Platinum', act_min: 27 }, { name: 'Silver', act_min: 24 }] },
    { name: 'UTK', levers: ['AP credit', 'CLEP credit', 'Dual enrollment'], awards: [] },
  ],
}

describe('parentActions', () => {
  it('leads with the weakest section and a benchmark when due', () => {
    const a = parentActions({ ...base, schedule: { ...base.schedule, inDays: 0, overdueDays: 3 } })
    expect(a.map((x) => x.key).slice(0, 2)).toEqual(['bench', 'focus-math'])
    expect(a[1]!.title).toBe('Focus on ACT Math this week')
  })

  it('compares merit thresholds with the target, never a practice estimate, and never claims eligibility', () => {
    const merit = parentActions({ ...base, targetScore: 25 }).find((x) => x.key === 'merit')!
    expect(merit.title).toBe('CBU: Platinum lists ACT 27+')
    expect(merit.detail).toMatch(/2 above the target of 25/)
    expect(merit.detail).toMatch(/not an eligibility decision/)
    const official = parentActions({ ...base, officialScore: { composite: 28, selfReported: true } }).find((x) => x.key === 'merit')!
    expect(official.detail).toMatch(/self-reported score \(unverified\) of 28 meets/)
    expect(parentActions({ ...base, targetScore: null }).some((x) => x.key === 'merit')).toBe(false)
  })

  it('shows verified credit and dual-enrollment actions only from school records', () => {
    const a = parentActions({ ...base, goals: ['college_credit'] }, 10)
    expect(a.find((x) => x.key === 'credit')!.title).toBe("Review UTK's verified AP and CLEP credit")
    expect(a.find((x) => x.key === 'dual')!.title).toBe('Check its verified dual-enrollment policy')
    expect(a.some((x) => x.key === 'dual')).toBe(true)
    const none = parentActions({ ...base, goals: ['college_credit'], schools: [{ name: 'X', levers: [], awards: [] }] }, 10)
    expect(none.some((x) => x.key === 'credit' || x.key === 'dual')).toBe(false)
  })

  it('asks for target colleges when none are saved, and caps the list', () => {
    const a = parentActions({ ...base, schools: [] })
    expect(a.at(-1)!.key).toBe('schools')
    expect(parentActions({ ...base, linked: false, behind: { done: 1, goal: 40, expected: 20 } }, 3)).toHaveLength(3)
  })
})
