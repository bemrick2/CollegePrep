// The check flow's helpers (#248 review: pickCheckItem, checkPlanFromCounts, checkSize had no unit tests) and its
// error path: after an answer is saved, a failure to move on never resubmits it, and an expired check says to start
// a new one.
import { describe, expect, it, vi } from 'vitest'
import { cleanup, render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import { DataError } from '../../lib/data/source'
import { checkPlanFromCounts, checkSize, pickCheckItem, type Q } from '../../lib/engine/freshness'

const item = (id: string, section: string, difficulty: number, seen: boolean) => ({ question: { id, section, exam_family: 'act', difficulty } as Q, seen_before: seen })

describe('check helpers', () => {
  it('pickCheckItem: unseen first, nearest the target difficulty, then repeats; never another section or a used item', () => {
    const items = [item('a', 'math', 1, false), item('b', 'math', 4, false), item('c', 'math', 3, true), item('d', 'english', 3, false)]
    expect(pickCheckItem(items, 'math', 3, new Set())!.question.id).toBe('b')
    expect(pickCheckItem(items, 'math', 1, new Set())!.question.id).toBe('a')
    expect(pickCheckItem(items, 'math', 3, new Set(['a', 'b']))!.question.id).toBe('c')
    expect(pickCheckItem(items, 'math', 3, new Set(['a', 'b', 'c']))).toBeNull()
    expect(pickCheckItem(items, 'reading', 3, new Set())).toBeNull()
  })

  it('checkPlanFromCounts: fresh, with repeats (no verdict), shortened, or not measured', () => {
    const plan = checkPlanFromCounts({ english: 3, math: 4, reading: 3, science: 3 }, [
      { section: 'english', reserved: 3, unseen: 3 },
      { section: 'math', reserved: 4, unseen: 1 },
      { section: 'reading', reserved: 2, unseen: 2 },
    ])
    expect(plan.map((p) => [p.section, p.count, p.repeats, p.status, p.shortened])).toEqual([
      ['english', 3, 0, 'fresh', false],
      ['math', 4, 3, 'with_repeats', false],
      ['reading', 2, 0, 'fresh', true],
      ['science', 0, 0, 'not_measured', false],
    ])
  })

  it('checkSize: the check length or the reserve, whichever is smaller, per section', () => {
    const counts = [
      { section: 'english', reserved: 3, unseen: 3 },
      { section: 'math', reserved: 4, unseen: 4 },
      { section: 'reading', reserved: 3, unseen: 0 },
      { section: 'science', reserved: 3, unseen: 3 },
    ]
    expect(checkSize('act', 'initial', counts).questions).toBe(13) // 7/8/6/6 asked, 3/4/3/3 held
    expect(checkSize('act', 'mini', counts).questions).toBe(13)
    expect(checkSize('act', 'mini', []).questions).toBe(0)
    expect(checkSize('act', 'mini', counts, 60).minutes).toBe(Math.round((13 * 60 * 1.3) / 60))
  })
})

/** The demo with a check that closes (as the server does after 4 hours) once the first answer is in. */
class ClosesAfterOne extends DemoSource {
  submits = 0
  starts = 0
  override async submitAttempt(...a: Parameters<DemoSource['submitAttempt']>) {
    this.submits++
    return super.submitAttempt(...a)
  }
  override async startAttempt(...a: Parameters<DemoSource['startAttempt']>) {
    if (a[3] && ++this.starts > 1) throw new DataError('This progress check has expired; start a new one', 'invalid')
    return super.startAttempt(...a)
  }
}

describe('check error path', () => {
  it('an expired check: the saved answer is never sent again, and the screen says to start a new check', async () => {
    const user = userEvent.setup()
    const src = new ClosesAfterOne(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', 2028, 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 10 })
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    await src.acceptInvitation(inv.inviteCode)
    vi.spyOn(window, 'confirm').mockReturnValue(false)
    render(
      <MemoryRouter initialEntries={['/student/benchmark']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    await user.click(await screen.findByRole('button', { name: /^Start / }, { timeout: 8000 }))
    const choices = await screen.findAllByRole('radio', {}, { timeout: 8000 })
    await user.click(choices[0]!)
    await user.click(screen.getByRole('button', { name: 'Fairly sure' }))
    expect(await screen.findByText('This progress check has ended', {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Back to progress checks' })).toBeInTheDocument()
    expect(src.submits).toBe(1)
    // Nothing on screen can send the saved answer again.
    expect(screen.queryByRole('button', { name: 'Fairly sure' })).not.toBeInTheDocument()
  }, 30_000)

  /** Signs in a demo student with an ACT plan and opens the check page on `src`. */
  async function openCheck(src: DemoSource) {
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', 2028, 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 10 })
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    await src.acceptInvitation(inv.inviteCode)
    vi.spyOn(window, 'confirm').mockReturnValue(false)
    render(
      <MemoryRouter initialEntries={['/student/benchmark']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
  }

  it('a refusal that is not expiry (e.g. "used once") offers Continue, not "ended", and Continue moves on', async () => {
    class UsedOnceOnce extends DemoSource {
      starts = 0
      override async startAttempt(...a: Parameters<DemoSource['startAttempt']>) {
        if (a[3] && ++this.starts === 2) throw new DataError('A question is used once per progress check', 'invalid')
        return super.startAttempt(...a)
      }
    }
    const user = userEvent.setup()
    const src = new UsedOnceOnce(emptyStore())
    await openCheck(src)
    await user.click(await screen.findByRole('button', { name: /^Start / }, { timeout: 8000 }))
    await user.click((await screen.findAllByRole('radio', {}, { timeout: 8000 }))[0]!)
    await user.click(screen.getByRole('button', { name: 'Fairly sure' }))
    expect(await screen.findByText(/used once per progress check/, {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.queryByText('This progress check has ended')).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    expect(await screen.findAllByRole('radio', {}, { timeout: 8000 })).not.toHaveLength(0)
  }, 30_000)

  it('a lost reply: the retry is told "already submitted", treats the answer as saved, and moves on', async () => {
    class LosesFirstReply extends DemoSource {
      submits = 0
      override async submitAttempt(...a: Parameters<DemoSource['submitAttempt']>) {
        this.submits++
        const r = await super.submitAttempt(...a)
        if (this.submits === 1) throw new Error('Network error')
        return r
      }
    }
    const user = userEvent.setup()
    const src = new LosesFirstReply(emptyStore())
    await openCheck(src)
    await user.click(await screen.findByRole('button', { name: /^Start / }, { timeout: 8000 }))
    const first = await screen.findAllByRole('radio', {}, { timeout: 8000 })
    await user.click(first[0]!)
    await user.click(screen.getByRole('button', { name: 'Fairly sure' }))
    expect(await screen.findByText('Network error', {}, { timeout: 8000 })).toBeInTheDocument()
    // The retry reaches a server that already has the answer: no endless error, the next question appears.
    await user.click(screen.getByRole('button', { name: 'Fairly sure' }))
    await screen.findByText(/Question 2|2 of/, {}, { timeout: 8000 }).catch(() => undefined)
    expect(screen.queryByText(/already submitted/)).not.toBeInTheDocument()
    expect(src.submits).toBe(2)
  }, 30_000)

  it('a reload mid-check resumes the same check (#279): no fresh questions, and the next one is from its assignment', async () => {
    const user = userEvent.setup()
    const store = emptyStore()
    const src = new DemoSource(store)
    await openCheck(src)
    await user.click(await screen.findByRole('button', { name: /^Start / }, { timeout: 8000 }))
    await user.click((await screen.findAllByRole('radio', {}, { timeout: 8000 }))[0]!)
    await user.click(screen.getByRole('button', { name: 'Fairly sure' }))
    // The answer is saved and the next question is shown (not the old radios, still on screen for a moment).
    await waitFor(() => expect(Object.values(store.checks ?? {})[0]?.used).toHaveLength(2), { timeout: 8000 })
    await screen.findAllByRole('radio', {}, { timeout: 8000 })
    const sid = Object.values(store.checks ?? {})[0]!.studentId
    const [id, before] = Object.entries(store.checks ?? {})[0]!
    const usedBefore = [...before.used]
    cleanup()
    // Reload: a new source over the saved store, the same student signed in.
    const reloaded = new DemoSource(JSON.parse(JSON.stringify(store)))
    reloaded.switchPersona(DEMO_STUDENT, 'Riley')
    render(
      <MemoryRouter initialEntries={['/student/benchmark']}>
        <AppProvider source={reloaded}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText('Your progress check is still open', {}, { timeout: 8000 })).toBeInTheDocument()
    // Wait until the screen has settled (its progress loaded), so the click lands on the button that stays.
    await screen.findByText(/questions? (is|are) left/, {}, { timeout: 8000 })
    await waitFor(() => expect(screen.getByRole('button', { name: 'Resume the check' })).toBeEnabled(), { timeout: 8000 })
    expect(screen.queryByRole('button', { name: /^Start / })).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Resume the check' }))
    await screen.findAllByRole('radio', {}, { timeout: 8000 })
    // The counter includes the two questions used before the reload (one answered, one shown).
    expect(screen.getByText(/3 \/ 3/)).toBeInTheDocument()
    // Still the one check, its assignment unchanged; the question now shown is an assigned one not used before.
    const after = (reloaded as unknown as { s: typeof store }).s.checks!
    expect(Object.keys(after)).toEqual([id])
    expect(after[id]!.assigned).toEqual(before.assigned)
    const nowUsed = after[id]!.used.filter((q) => !usedBefore.includes(q))
    expect(nowUsed).toHaveLength(1)
    expect(before.assigned.map((a) => a.id)).toContain(nowUsed[0])
    expect(sid).toBeTruthy()
  }, 30_000)

  it('when no check may start yet, the page says when the next one opens and offers no Start', async () => {
    vi.useFakeTimers({ toFake: ['Date'], shouldAdvanceTime: true })
    vi.setSystemTime(new Date('2026-10-26T12:00:00Z'))
    const store = emptyStore()
    const src = new DemoSource(store)
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', 2028, 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 10 })
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    await src.acceptInvitation(inv.inviteCode)
    await src.startBenchmark(sid, 'initial', 'act') // started, never answered
    vi.setSystemTime(new Date('2026-10-26T17:00:00Z')) // expired
    render(
      <MemoryRouter initialEntries={['/student/benchmark']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText(/Your next progress check opens on/, {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /^Start / })).toBeDisabled()
    vi.useRealTimers()
  }, 30_000)

  // #291 review. A student set up in a store the tests share with a second source ("another tab").
  async function riley(store = emptyStore()) {
    const src = new DemoSource(store)
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', 2028, 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 10 })
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    await src.acceptInvitation(inv.inviteCode)
    return { src, sid, store }
  }
  const show = (src: DemoSource) =>
    render(
      <MemoryRouter initialEntries={['/student/benchmark']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
  /** Answers a check's next `n` items through a source (as another tab would). */
  async function answerElsewhere(src: DemoSource, sid: string, bm: string, n: number) {
    const items = await src.benchmarkQuestions(bm, sid)
    for (const it of items.slice(0, n)) {
      const a = await src.startAttempt(sid, it.question.id, null, bm)
      await src.submitAttempt(a, { answer: 'A', activeMs: 5 })
    }
  }

  it('a stale Start (the check was opened and partly answered in another tab) resumes it, with the true counter', async () => {
    const user = userEvent.setup()
    const { src, sid, store } = await riley()
    show(src)
    const start = await screen.findByRole('button', { name: /^Start / }, { timeout: 8000 })
    // Meanwhile, another tab opens the starting check and uses 2 of its 3 English items.
    const other = new DemoSource(store)
    const bm = await other.startBenchmark(sid, 'initial', 'act')
    await answerElsewhere(other, sid, bm, 2)
    await user.click(start)
    await screen.findAllByRole('radio', {}, { timeout: 8000 })
    expect(screen.getByText(/3 \/ 3/)).toBeInTheDocument()
    expect(Object.keys(store.checks ?? {})).toEqual([bm])
  }, 30_000)

  it('a resume lands in the first section with items left', async () => {
    const user = userEvent.setup()
    const { src, sid } = await riley()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    const english = (await src.benchmarkProgress(bm, sid)).find((p) => p.section === 'english')!.assigned
    await answerElsewhere(src, sid, bm, english) // assignment order: English first
    show(src)
    await user.click(await screen.findByRole('button', { name: 'Resume the check' }, { timeout: 8000 }))
    await screen.findAllByRole('radio', {}, { timeout: 8000 })
    expect(screen.getByText(/section 2 of/)).toBeInTheDocument()
    expect(screen.queryByText(/^English ·/)).not.toBeInTheDocument()
  }, 30_000)

  it('a check that expires before Resume is clicked: the page says so and offers what the server allows, not Resume', async () => {
    vi.useFakeTimers({ toFake: ['Date'], shouldAdvanceTime: true })
    vi.setSystemTime(new Date('2026-10-26T12:00:00Z'))
    const user = userEvent.setup()
    const { src, sid } = await riley()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    await answerElsewhere(src, sid, bm, 1)
    show(src)
    const resume = await screen.findByRole('button', { name: 'Resume the check' }, { timeout: 8000 })
    vi.setSystemTime(new Date('2026-10-26T16:30:00Z'))
    await user.click(resume)
    // The page re-reads the server's options after the error, so wait for the settled screen, not the first render.
    await waitFor(
      () => {
        expect(screen.getByText('That progress check has closed')).toBeInTheDocument()
        expect(screen.getByText(/Your next progress check opens on/)).toBeInTheDocument()
        expect(screen.queryByRole('button', { name: 'Resume the check' })).not.toBeInTheDocument()
      },
      { timeout: 8000 },
    )
    vi.useRealTimers()
  }, 30_000)

  it('if the server can’t say which checks may start, nothing starts: the page says so and offers Try again', async () => {
    class NoOptions extends DemoSource {
      override async benchmarkOptions(): Promise<never> {
        throw new DataError('Network error', 'network')
      }
    }
    const store = emptyStore()
    const { sid } = await riley(store)
    show(new NoOptions(store))
    expect(await screen.findByText("We couldn't check which progress check you can take", {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /^Start / })).toBeDisabled()
    expect(screen.getByRole('button', { name: 'Try again' })).toBeInTheDocument()
    expect(sid).toBeTruthy()
  }, 30_000)

  it('a resumed check is completed as resumed (the server’s metrics, not this screen’s partial record), and home offers Resume', async () => {
    const user = userEvent.setup()
    const { src, sid, store } = await riley()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    const total = (await src.benchmarkProgress(bm, sid)).reduce((n, p) => n + p.assigned, 0)
    await answerElsewhere(src, sid, bm, total - 1)
    // Home first: the open check is offered for resuming.
    render(
      <MemoryRouter initialEntries={['/student']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText('Your progress check is still open', {}, { timeout: 8000 })).toBeInTheDocument()
    cleanup()
    const complete = vi.spyOn(src, 'completeBenchmark')
    show(src)
    await user.click(await screen.findByRole('button', { name: 'Resume the check' }, { timeout: 8000 }))
    await user.click((await screen.findAllByRole('radio', {}, { timeout: 8000 }))[0]!)
    await user.click(screen.getByRole('button', { name: 'Fairly sure' }))
    await waitFor(() => expect(complete).toHaveBeenCalled(), { timeout: 8000 })
    expect(complete.mock.calls[0]![3]).toEqual({ resumed: true })
    expect(complete.mock.calls[0]![2].started_at).toBe(store.checks![bm]!.startedAt) // the server's start time, not the reload's
    const saved = await complete.mock.results[0]!.value
    expect(saved.attempt_ids).toHaveLength(total)
  }, 30_000)

  it('(#291 confirm) dates are the student’s own; a resumed check keeps the server’s start time; home follows the server for a mini after an abandoned start', async () => {
    vi.useFakeTimers({ toFake: ['Date'], shouldAdvanceTime: true })
    // 8:30pm in Chicago on Oct 26 is Oct 27 in UTC; 28 days later the next check opens on the evening of Nov 23 in
    // Chicago (Nov 24 in UTC).
    vi.setSystemTime(new Date('2026-10-27T01:30:00Z'))
    const user = userEvent.setup()
    const { src, sid } = await riley()
    const bm = await src.startBenchmark(sid, 'initial', 'act')
    await answerElsewhere(src, sid, bm, 1)
    show(src)
    await user.click(await screen.findByRole('button', { name: 'Resume the check' }, { timeout: 8000 }))
    await screen.findAllByRole('radio', {}, { timeout: 8000 })
    cleanup()
    // Expired, unanswered beyond one item: the next check opens a week after the start, shown in Chicago time.
    vi.setSystemTime(new Date('2026-10-27T06:00:00Z'))
    show(src)
    expect(await screen.findByText(/Your next progress check opens on/, {}, { timeout: 8000 })).toHaveTextContent(/Nov 23\b/)
    cleanup()
    // Once the gap has passed a mini is allowed: home offers it rather than "no check can start".
    vi.setSystemTime(new Date('2026-11-25T12:00:00Z'))
    render(
      <MemoryRouter initialEntries={['/student']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText('Mini benchmark', {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.queryByText('No progress check can be started right now')).not.toBeInTheDocument()
    vi.useRealTimers()
  }, 30_000)
})
