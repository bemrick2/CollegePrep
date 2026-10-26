import { afterEach, describe, expect, it, vi } from 'vitest'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from './demoSource'
import { sampleFamily } from './seed'
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
    expect(await src.benchmarkOptions(sid, 'act')).toEqual({ initialAllowed: true, miniAllowed: false, miniOpensAt: null, fullAllowed: false, open: null, reserveAvailable: true })
    await expect(src.startBenchmark(sid, 'full', 'act')).rejects.toThrow('This kind of progress check is not available for this exam yet')
    await expect(src.startBenchmark(sid, 'mini', 'act')).rejects.toThrow('A repeat progress check comes after a first check for this exam')
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
    await expect(again.startBenchmark(sid, 'mini', 'act')).rejects.toThrow(/progress check is already open for this exam; resume it/)
    const left = await again.benchmarkQuestions(bm, sid)
    expect(left.map((i) => i.question.id)).toEqual(items.slice(1).map((i) => i.question.id))
    const prog = await again.benchmarkProgress(bm, sid)
    expect(prog.reduce((n, p) => n + p.assigned, 0)).toBe(items.length)
    expect(prog.reduce((n, p) => n + p.used, 0)).toBe(1)
  })

  it('initial once; a mini opens 28 days after the last check started, even after an unanswered, expired one', async () => {
    vi.useFakeTimers({ toFake: ['Date'] })
    vi.setSystemTime(new Date('2026-10-26T12:00:00Z'))
    const { src, sid } = await student()
    await src.startBenchmark(sid, 'initial', 'act') // never answered
    vi.setSystemTime(new Date('2026-10-26T17:00:00Z')) // expired
    expect(await src.benchmarkOptions(sid, 'act')).toEqual({ initialAllowed: false, miniAllowed: false, miniOpensAt: '2026-11-23T12:00:00.000Z', fullAllowed: false, open: null, reserveAvailable: true })
    await expect(src.startBenchmark(sid, 'initial', 'act')).rejects.toThrow('An initial progress check is only for a student who has not started one for this exam')
    await expect(src.startBenchmark(sid, 'mini', 'act')).rejects.toThrow('The next progress check opens 28 days after the last one started (on 2026-11-23)')
    vi.setSystemTime(new Date('2026-11-23T12:00:00Z'))
    expect((await src.benchmarkOptions(sid, 'act')).miniAllowed).toBe(true)
    await expect(src.startBenchmark(sid, 'mini', 'act')).resolves.toBeTruthy()
  })

  it('exams are separate: an open ACT check doesn’t block or count toward SAT', async () => {
    const { src, sid } = await student()
    await src.startBenchmark(sid, 'initial', 'act')
    expect(await src.benchmarkOptions(sid, 'sat')).toMatchObject({ initialAllowed: true, open: null })
  })

  it('(#291 review) checks completed before checks were kept count: the sample student has had the starting check', async () => {
    const src = new DemoSource(sampleFamily('student'))
    expect(await src.benchmarkOptions('st-sample-maya', 'act')).toMatchObject({ initialAllowed: false, open: null })
  })

  it('(#291 review) only the linked student reads options and progress, or completes a check; a closed or expired check can’t be completed', async () => {
    vi.useFakeTimers({ toFake: ['Date'] })
    vi.setSystemTime(new Date('2026-10-26T12:00:00Z'))
    const { src, sid } = await student()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    const other = new DemoSource(JSON.parse(JSON.stringify((src as unknown as { s: DemoStore }).s)))
    other.switchPersona(DEMO_PARENT, 'Jordan')
    await expect(other.benchmarkOptions(sid, 'act')).rejects.toThrow()
    await expect(other.benchmarkProgress(bm, sid)).rejects.toThrow()
    const summary = { id: 'x', kind: 'initial', exam_family: 'act', started_at: '', completed_at: '', attempt_ids: [], metrics: {} } as never
    await expect(other.completeBenchmark(sid, bm, summary)).rejects.toThrow()
    await src.completeBenchmark(sid, bm, summary)
    await expect(src.completeBenchmark(sid, bm, summary)).rejects.toThrow(/not an open benchmark/) // once
    vi.setSystemTime(new Date('2026-11-24T12:00:00Z'))
    const late = await src.startBenchmark(sid, 'mini', 'act')
    vi.setSystemTime(new Date('2026-11-24T16:30:00Z'))
    await expect(src.completeBenchmark(sid, late, summary)).rejects.toThrow(/expired/)
  })

  it('(#291 review) a resumed check is completed with metrics from every attempt in it, not only those after the reload', async () => {
    const { src, sid } = await student()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    const items = await src.benchmarkQuestions(bm, sid)
    for (const it of items.slice(0, 3)) await answer(src, sid, bm, it.question.id)
    const empty = { id: 'x', kind: 'initial', exam_family: 'act', started_at: '', completed_at: '', attempt_ids: [], metrics: { answered: 0, sections: [] } } as never
    const saved = await src.completeBenchmark(sid, bm, empty, { resumed: true })
    expect(saved.attempt_ids).toHaveLength(3)
    expect(saved.metrics).toMatchObject({ answered: 3, correct: 3 })
    // Without `resumed`, the client's record is kept as it is (it saw the whole check).
  })

  it('(#291 confirm) a check id of another student is refused even with one’s own id; completion is closed at once (no double save)', async () => {
    const a = await student()
    const bmA = await a.src.startBenchmark(a.sid, 'initial', 'act')
    // A second student, another user, in the same store.
    const bsrc = new DemoSource(a.store)
    bsrc.switchPersona('u-test-bo', 'Bo')
    const b = { src: bsrc, sid: await bsrc.createSelfStudentProfile({ displayName: 'Bo', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' }) }
    await expect(b.src.benchmarkProgress(bmA, b.sid)).rejects.toThrow(/not an open benchmark of this student/)
    await expect(b.src.benchmarkQuestions(bmA, b.sid)).rejects.toThrow()
    const summary = { id: 'x', kind: 'initial', exam_family: 'act', started_at: '', completed_at: '', attempt_ids: [], metrics: {} } as never
    await expect(b.src.completeBenchmark(b.sid, bmA, summary)).rejects.toThrow()
    a.src.switchPersona(DEMO_STUDENT, 'Ava')
    const two = await Promise.allSettled([a.src.completeBenchmark(a.sid, bmA, summary, { resumed: true }), a.src.completeBenchmark(a.sid, bmA, summary, { resumed: true })])
    expect(two.map((r) => r.status).sort()).toEqual(['fulfilled', 'rejected'])
  })
})
