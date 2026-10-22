// CR-23 on the demo source: checks use only reserved questions, practice never does, and the check says when the
// reserved pool is too small.
import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT, loadFixtures } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import { checkQuestions, practiceExclusions } from '../../lib/engine/freshness'

async function family() {
  const src = new DemoSource(emptyStore())
  src.switchPersona(DEMO_PARENT, 'Jordan')
  const hh = await src.createHousehold('Home', 'America/Chicago')
  const sid = await src.addStudent(hh, 'Riley', 2028, 11)
  await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 10 })
  const inv = await src.createStudentInvitation(hh, sid)
  src.switchPersona(DEMO_STUDENT, 'Riley')
  await src.acceptInvitation(inv.inviteCode)
  return { src, sid }
}

describe('reserved assessment pool (CR-23) on the demo source', () => {
  it('practice sessions never include a reserved question, and a practice attempt on one is refused', async () => {
    const { src, sid } = await family()
    const F = await loadFixtures()
    const reserved = practiceExclusions('act', F.QUESTIONS)
    expect(reserved.size).toBeGreaterThan(0)
    for (let i = 0; i < 3; i++) {
      const s = await src.startSession(sid, 30, 'act')
      for (const it of s.items) expect(reserved.has(it.question.id)).toBe(false)
    }
    // With every practice question already answered, sessions are review of practice items and still never reserved.
    for (const q of F.QUESTIONS.filter((x) => x.exam_family === 'act' && !reserved.has(x.id))) {
      const a = await src.startAttempt(sid, q.id, null)
      await src.submitAttempt(a, { answer: q.accepted_answers[0]!, activeMs: 30_000 })
    }
    const review = await src.startSession(sid, 30, 'act')
    expect(review.items.length).toBeGreaterThan(0)
    for (const it of review.items) expect([reserved.has(it.question.id), it.seen_before]).toEqual([false, true])
    const one = [...reserved][0]!
    // The server refuses with 22023, which LiveSource maps to 'invalid'.
    await expect(src.startAttempt(sid, one, null)).rejects.toMatchObject({ code: 'invalid' })
  })

  it('a check attempt accepts reserved questions only', async () => {
    const { src, sid } = await family()
    const F = await loadFixtures()
    const reserved = checkQuestions('act', F.QUESTIONS)
    const practice = F.QUESTIONS.find((q) => q.exam_family === 'act' && !reserved.some((r) => r.id === q.id))!
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    await expect(src.startAttempt(sid, practice.id, null, bm)).rejects.toMatchObject({ code: 'invalid' })
    await expect(src.startAttempt(sid, reserved[0]!.id, null, bm)).resolves.toBeTruthy()
  })

  it('a second start of the same check resumes it; a completed check is closed', async () => {
    const { src, sid } = await family()
    const bm = await src.startBenchmark(sid, 'mini', 'act')
    expect(await src.startBenchmark(sid, 'mini', 'act')).toBe(bm)
    expect(await src.startBenchmark(sid, 'initial', 'act')).not.toBe(bm)
    const items = await src.benchmarkQuestions(bm, sid)
    const sat = (await loadFixtures()).QUESTIONS.find((q) => q.exam_family === 'sat' && checkQuestions('sat', [q]).length)
    if (sat) await expect(src.startAttempt(sid, sat.id, null, bm)).rejects.toMatchObject({ code: 'invalid' })  // another exam's reserved item
    await src.completeBenchmark(sid, bm, { id: bm, kind: 'mini', exam_family: 'act' } as never)
    await expect(src.benchmarkQuestions(bm, sid)).rejects.toMatchObject({ code: 'forbidden' })
    await expect(src.startAttempt(sid, items[0]!.question.id, null, bm)).rejects.toMatchObject({ code: 'invalid' })
    expect(await src.startBenchmark(sid, 'mini', 'act')).not.toBe(bm)
  })

  it('the starting check says it is shorter than usual when the reserve is smaller than the check', async () => {
    const { src } = await family()
    render(
      <MemoryRouter initialEntries={['/student/benchmark']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText('This check is limited by the questions set aside for checks', {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.getByText(/Shorter than usual:/)).toBeInTheDocument()
  }, 30_000)
})
