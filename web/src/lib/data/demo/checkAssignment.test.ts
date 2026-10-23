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
    const bm = await src.startBenchmark(sid, 'mini', 'act')
    const items = await src.benchmarkQuestions(bm, sid)
    for (const [section, n] of Object.entries(PER_SECTION.act.mini)) {
      const inReserve = QUESTIONS.filter((q) => RESERVED_ACT.has(q.id) && q.section === section).length
      expect(items.filter((i) => i.question.section === section)).toHaveLength(Math.min(n, inReserve))
    }
    expect(items.every((i) => RESERVED_ACT.has(i.question.id) && !i.seen_before)).toBe(true)
    // Resuming returns the same check and the same items.
    expect(await src.startBenchmark(sid, 'mini', 'act')).toBe(bm)
    expect((await src.benchmarkQuestions(bm, sid)).map((i) => i.question.id)).toEqual(items.map((i) => i.question.id))
  })

  it('refuses an item that isn’t assigned to the check, and a used one', async () => {
    const { src, sid } = await student()
    const bm = await src.startBenchmark(sid, 'mini', 'sat')
    const assigned = new Set((await src.benchmarkQuestions(bm, sid)).map((i) => i.question.id))
    const unassigned = [...RESERVED_SAT].find((id) => !assigned.has(id))
    if (unassigned) await expect(src.startAttempt(sid, unassigned, null, bm)).rejects.toThrow('This question is not part of this progress check')
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
    const bm1 = await src.startBenchmark(sid, 'mini', 'act')
    const first = await src.benchmarkQuestions(bm1, sid)
    const before = await src.assessmentPoolStatus(sid, 'act')
    // Nothing answered; the check expires.
    vi.setSystemTime(new Date('2026-10-23T17:00:00Z'))
    const bm2 = await src.startBenchmark(sid, 'mini', 'act')
    expect(bm2).not.toBe(bm1)
    const second = await src.benchmarkQuestions(bm2, sid)
    // The reserve is exactly one mini check, so the second check is all repeats, every one of them never answered.
    expect(second.map((i) => i.question.id).sort()).toEqual(first.map((i) => i.question.id).sort())
    expect(second.every((i) => i.seen_before)).toBe(true)
    expect(before!.every((s) => s.unseen === 0)).toBe(true) // exposure counted from assignment, not from answers
  })
})
