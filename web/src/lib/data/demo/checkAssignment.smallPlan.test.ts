import { describe, expect, it, vi } from 'vitest'

// TEST SETUP: the demo's reserve is exactly one mini check, so every reserved item is always assigned. To show that
// unassigned reserved items are refused and unlisted, this file shrinks the mini-check plan to 1 item per section
// (as the local server test shrinks practice_benchmark_plan). Nothing else changes.
vi.mock('../../engine/benchmark', async (orig) => {
  const m = await orig<typeof import('../../engine/benchmark')>()
  const mini = (r: Record<string, number>) => Object.fromEntries(Object.keys(r).map((k) => [k, 1]))
  return { ...m, PER_SECTION: { act: { ...m.PER_SECTION.act, mini: mini(m.PER_SECTION.act.mini) }, sat: { ...m.PER_SECTION.sat, mini: mini(m.PER_SECTION.sat.mini) } } }
})

// The setup file's imports load demoSource first; reload it so it sees the smaller plan.
vi.resetModules()
const { DemoSource, DEMO_STUDENT } = await import('./demoSource')
const { emptyStore } = await import('./store')
const { QUESTIONS } = await import('./fixtures')
const { practiceExclusions } = await import('../../engine/freshness')

describe('demo progress checks (#263) with a check smaller than the reserve', () => {
  it('lists only the assigned items and refuses the rest of the reserve; the next check draws the unseen ones first', async () => {
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Ava')
    const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
    const reserved = practiceExclusions('sat', QUESTIONS)
    const bm = await src.startBenchmark(sid, 'mini', 'sat')
    const items = await src.benchmarkQuestions(bm, sid)
    expect(items).toHaveLength(2) // one per section
    const assigned = new Set(items.map((i) => i.question.id))
    const rest = [...reserved].filter((id) => !assigned.has(id))
    expect(rest.length).toBe(reserved.size - 2)
    for (const id of rest) await expect(src.startAttempt(sid, id, null, bm)).rejects.toThrow('This question is not part of this progress check')
    // Exposure is the assignment: the pool now counts these two as seen, though none was answered.
    const pool = await src.assessmentPoolStatus(sid, 'sat')
    expect(pool!.reduce((n, s) => n + s.reserved - s.unseen, 0)).toBe(2)
  })
})
