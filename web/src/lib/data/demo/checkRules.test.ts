import { afterEach, describe, expect, it, vi } from 'vitest'
import { DemoSource, DEMO_STUDENT } from './demoSource'
import { emptyStore, type DemoStore } from './store'
import { QUESTIONS } from './fixtures'

// The demo mirrors the proposed #279 contract (comments 6421822021 and 6422427834): a live check is resumed whatever
// was answered, a different kind is refused while one is open, `full` is refused, `initial` is once, and a `mini`
// needs an earlier check and a week since the last one started.
async function student(store: DemoStore = emptyStore()) {
  const src = new DemoSource(store)
  src.switchPersona(DEMO_STUDENT, 'Ava')
  const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
  return { src, sid, store }
}
const answer = async (src: DemoSource, sid: string, bm: string, id: string) => {
  const a = await src.startAttempt(sid, id, null, bm)
  await src.submitAttempt(a, { answer: QUESTIONS.find((q) => q.id === id)!.accepted_answers[0]!, activeMs: 5 })
}
afterEach(() => vi.useRealTimers())

describe('demo check rules (#279 proposed contract)', () => {
  it('first: only the starting check; full and mini are refused', async () => {
    const { src, sid } = await student()
    expect(await src.benchmarkOptions(sid, 'act')).toEqual({ initialAllowed: true, miniAllowed: false, miniOpensOn: null, fullAllowed: false, open: null })
    await expect(src.startBenchmark(sid, 'full', 'act')).rejects.toThrow("A full progress check isn't available yet")
    await expect(src.startBenchmark(sid, 'mini', 'act')).rejects.toThrow('Take the starting check first')
  })

  it('a partly answered check is resumed after a reload, with the same assignment and its progress; another kind is refused', async () => {
    const { src, sid, store } = await student()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    const items = await src.benchmarkQuestions(bm, sid)
    await answer(src, sid, bm, items[0]!.question.id)
    // A reload: a new source over the saved store.
    const again = new DemoSource(JSON.parse(JSON.stringify(store)))
    again.switchPersona(DEMO_STUDENT, 'Ava')
    expect((await again.benchmarkOptions(sid, 'act')).open).toMatchObject({ id: bm, kind: 'initial' })
    expect(await again.startBenchmark(sid, 'initial', 'act')).toBe(bm)
    await expect(again.startBenchmark(sid, 'mini', 'act')).rejects.toThrow('A progress check is already open')
    const left = await again.benchmarkQuestions(bm, sid)
    expect(left.map((i) => i.question.id)).toEqual(items.slice(1).map((i) => i.question.id))
    const prog = await again.benchmarkProgress(bm, sid)
    expect(prog.reduce((n, p) => n + p.assigned, 0)).toBe(items.length)
    expect(prog.reduce((n, p) => n + p.used, 0)).toBe(1)
  })

  it('initial once; a mini opens a week after the last check started, even after an unanswered, expired one', async () => {
    vi.useFakeTimers({ toFake: ['Date'] })
    vi.setSystemTime(new Date('2026-10-26T12:00:00Z'))
    const { src, sid } = await student()
    await src.startBenchmark(sid, 'initial', 'act') // never answered
    vi.setSystemTime(new Date('2026-10-26T17:00:00Z')) // expired
    expect(await src.benchmarkOptions(sid, 'act')).toEqual({ initialAllowed: false, miniAllowed: false, miniOpensOn: '2026-11-02', fullAllowed: false, open: null })
    await expect(src.startBenchmark(sid, 'initial', 'act')).rejects.toThrow('The starting check has already been taken')
    await expect(src.startBenchmark(sid, 'mini', 'act')).rejects.toThrow('The next progress check opens on 2026-11-02')
    vi.setSystemTime(new Date('2026-11-02T12:00:00Z'))
    expect((await src.benchmarkOptions(sid, 'act')).miniAllowed).toBe(true)
    await expect(src.startBenchmark(sid, 'mini', 'act')).resolves.toBeTruthy()
  })

  it('exams are separate: an open ACT check doesn’t block or count toward SAT', async () => {
    const { src, sid } = await student()
    await src.startBenchmark(sid, 'initial', 'act')
    expect(await src.benchmarkOptions(sid, 'sat')).toMatchObject({ initialAllowed: true, open: null })
  })
})
