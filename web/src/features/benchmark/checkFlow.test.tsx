// The check flow's helpers (#248 review: pickCheckItem, checkPlanFromCounts, checkSize had no unit tests) and its
// error path: after an answer is saved, a failure to move on never resubmits it, and an expired check says to start
// a new one.
import { describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
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
    expect(screen.getByRole('button', { name: 'Start a new check' })).toBeInTheDocument()
    expect(src.submits).toBe(1)
    // Nothing on screen can send the saved answer again.
    expect(screen.queryByRole('button', { name: 'Fairly sure' })).not.toBeInTheDocument()
  }, 30_000)
})
