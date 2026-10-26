import { afterEach, describe, expect, it, vi } from 'vitest'
import { DemoSource, DEMO_STUDENT } from './demoSource'
import { emptyStore } from './store'
import { QUESTIONS } from './fixtures'
import { practiceExclusions } from '../../engine/freshness'
import { PER_SECTION } from '../../engine/benchmark'

// The demo mirrors #263 (server-assigned check items, assignment counts as exposure), as the local server tests
// (scripts/local/checkAssignment.local.test.ts) check on the real server.
const RESERVED_ACT = practiceExclusions('act', QUESTIONS)
const RESERVED_SAT = practiceExclusions('sat', QUESTIONS)

async function student() {
  const src = new DemoSource(emptyStore())
  src.switchPersona(DEMO_STUDENT, 'Ava')
  const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
  return { src, sid }
}
const answer = async (src: DemoSource, sid: string, bm: string, id: string) => {
  const a = await src.startAttempt(sid, id, null, bm)
  await src.submitAttempt(a, { answer: QUESTIONS.find((q) => q.id === id)!.accepted_answers[0]!, activeMs: 5 })
}

afterEach(() => vi.useRealTimers())

describe('demo progress checks mirror #263: items are assigned once, at start', () => {
  it('assigns the plan size per section from the reserve, unseen first, and lists nothing else', async () => {
    const { src, sid } = await student()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    const items = await src.benchmarkQuestions(bm, sid)
    for (const [section, n] of Object.entries(PER_SECTION.act.initial)) {
      const inReserve = QUESTIONS.filter((q) => RESERVED_ACT.has(q.id) && q.section === section).length
      expect(items.filter((i) => i.question.section === section)).toHaveLength(Math.min(n, inReserve))
    }
    expect(items.every((i) => RESERVED_ACT.has(i.question.id) && !i.seen_before)).toBe(true)
    // Resuming returns the same check and the same items.
    expect(await src.startBenchmark(sid, 'initial', 'act')).toBe(bm)
    expect((await src.benchmarkQuestions(bm, sid)).map((i) => i.question.id)).toEqual(items.map((i) => i.question.id))
  })

  it('refuses an item that isn’t assigned to the check, and a used one', async () => {
    const { src, sid } = await student()
    const bm = await src.startBenchmark(sid, 'initial', 'sat')
    const assigned = new Set((await src.benchmarkQuestions(bm, sid)).map((i) => i.question.id))
    // (The demo reserve is exactly one mini check, so every reserved item is assigned here; refusing unassigned items
    // is covered by checkAssignment.smallPlan.test.ts.)
    expect(assigned).toEqual(RESERVED_SAT)
    const first = [...assigned][0]!
    await answer(src, sid, bm, first)
    await expect(src.startAttempt(sid, first, null, bm)).rejects.toThrow('A question is used once per progress check')
    const act = [...RESERVED_ACT][0]!
    await expect(src.startAttempt(sid, act, null, bm)).rejects.toThrow(/its own exam version/)
  })

  it('an assigned item counts as seen even if the check is abandoned unanswered', async () => {
    vi.useFakeTimers({ toFake: ['Date'] })
    vi.setSystemTime(new Date('2026-10-23T12:00:00Z'))
    const { src, sid } = await student()
    const bm1 = await src.startBenchmark(sid, 'initial', 'act')
    const first = await src.benchmarkQuestions(bm1, sid)
    const before = await src.assessmentPoolStatus(sid, 'act')
    // Nothing answered; the check expires.
    vi.setSystemTime(new Date('2026-11-20T12:00:00Z')) // 28 days later: the next check opens
    const bm2 = await src.startBenchmark(sid, 'mini', 'act')
    expect(bm2).not.toBe(bm1)
    const second = await src.benchmarkQuestions(bm2, sid)
    // The reserve is exactly one mini check, so the second check is all repeats, every one of them never answered.
    expect(second.map((i) => i.question.id).sort()).toEqual(first.map((i) => i.question.id).sort())
    expect(second.every((i) => i.seen_before)).toBe(true)
    expect(before!.every((s) => s.unseen === 0)).toBe(true) // exposure counted from assignment, not from answers
  })

  it('exposure survives a reload of the demo, as the server keeps assignment rows', async () => {
    vi.useFakeTimers({ toFake: ['Date'] })
    vi.setSystemTime(new Date('2026-10-23T12:00:00Z'))
    const store = emptyStore()
    const src = new DemoSource(store)
    src.switchPersona(DEMO_STUDENT, 'Ava')
    const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
    await src.startBenchmark(sid, 'initial', 'act') // assigned, never answered
    vi.setSystemTime(new Date('2026-11-20T12:00:00Z'))
    const reloaded = new DemoSource(JSON.parse(JSON.stringify(store)))
    reloaded.switchPersona(DEMO_STUDENT, 'Ava')
    expect((await reloaded.assessmentPoolStatus(sid, 'act'))!.every((s) => s.unseen === 0)).toBe(true)
    const bm = await reloaded.startBenchmark(sid, 'mini', 'act')
    expect((await reloaded.benchmarkQuestions(bm, sid)).every((i) => i.seen_before)).toBe(true)
  })
})

