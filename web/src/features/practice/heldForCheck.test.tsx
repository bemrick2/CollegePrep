import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import type { PracticeSession } from '../../lib/data/types'

/** The server picked only reserved assessment questions (dropped by the client), so nothing is left to practise. */
class AllHeld extends DemoSource {
  override async startSession(): Promise<PracticeSession> {
    return { id: 's-1', target_minutes: 5, items: [], held_for_check: 4 }
  }
}

describe('practice when only reserved assessment questions are left', () => {
  it('says why, and points to the check, instead of "no questions published"', async () => {
    const src = new AllHeld(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', 2028, 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 5 })
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    await src.acceptInvitation(inv.inviteCode)
    render(
      <MemoryRouter initialEntries={['/student/practice?quick=1']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText('The questions left are set aside for progress checks', {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Go to progress checks' })).toHaveAttribute('href', '/student/benchmark')
    expect(screen.queryByText('No practice questions are published yet')).not.toBeInTheDocument()
  }, 30_000)
})
