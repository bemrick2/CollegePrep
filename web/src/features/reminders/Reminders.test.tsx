import { beforeEach, describe, expect, it, vi } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'

function renderAt(path: string, source: DemoSource) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <AppProvider source={source}>
        <App />
      </AppProvider>
    </MemoryRouter>,
  )
}

async function family() {
  const src = new DemoSource(emptyStore())
  src.switchPersona(DEMO_PARENT, 'Jordan')
  const hh = await src.createHousehold('Home', 'America/Chicago')
  const sid = await src.addStudent(hh, 'Riley', 2028, 11)
  await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: ['raise_score'], daily_minutes: 10 })
  const inv = await src.createStudentInvitation(hh, sid)
  src.switchPersona(DEMO_STUDENT, 'Riley')
  await src.acceptInvitation(inv.inviteCode)
  return { src, sid }
}

beforeEach(() => localStorage.clear())

describe('practice reminders', () => {
  it('a linked student is told their parent will be notified before turning reminders off; snoozing notifies nobody', async () => {
    const user = userEvent.setup()
    const { src, sid } = await family()
    renderAt('/student/reminders', src)
    const toggle = await screen.findByRole('switch')
    expect(toggle).not.toBeChecked()
    await user.click(toggle)
    expect(await screen.findByText('Practice reminders are on.')).toBeInTheDocument()
    expect(await screen.findByText(/Next possible reminder:/)).toBeInTheDocument()
    // The device can't show notifications in this test browser: said plainly, not as "off".
    expect(screen.getByText("This browser can't show notifications.")).toBeInTheDocument()

    await user.click(screen.getByRole('switch'))
    const dialog = screen.getByRole('alertdialog', { name: 'Turn off practice reminders?' })
    expect(within(dialog).getByText('Your parent will be notified that you turned off practice reminders.')).toBeInTheDocument()
    await user.click(within(dialog).getByRole('button', { name: 'Remind me later' }))
    expect(await screen.findByText(/Reminders pause until .+\. Nobody is notified\./)).toBeInTheDocument()
    expect(screen.getByRole('switch')).toBeChecked()
    expect(await src.reminderHistory(sid)).toEqual([expect.objectContaining({ enabled: true, by: 'student', notifyGuardians: false })])

    await user.click(screen.getByRole('switch'))
    await user.click(within(screen.getByRole('alertdialog')).getByRole('button', { name: 'Turn off reminders' }))
    expect(await screen.findByText('Practice reminders are off. Your parent would be notified (the demo sends no email).')).toBeInTheDocument()
    expect((await src.reminderHistory(sid))[0]).toMatchObject({ enabled: false, by: 'student', notifyGuardians: true, emailedToMeAt: null })
  }, 30_000)

  it('the guardian sees the change and that nothing was emailed, plus each device as of its last app open', async () => {
    const { src, sid } = await family()
    await src.saveReminderSettings(sid, { ...(await src.reminderSettings(sid)), enabled: true })
    await src.reportNotificationDevice({ deviceId: 'dev-1', permission: 'denied', subscription: null, platform: 'ios' })
    await src.saveReminderSettings(sid, { ...(await src.reminderSettings(sid)), enabled: false })
    src.switchPersona(DEMO_PARENT, 'Jordan')
    renderAt('/parent', src)
    expect(await screen.findByText(/Riley turned off practice reminders on .+\. Shown here only: the demo never sends email\./, {}, { timeout: 8000 })).toBeInTheDocument()
    expect(screen.getByText(/iPhone or iPad: notifications blocked in device settings/)).toBeInTheDocument()
    expect(screen.getByText(/Turning notifications off in phone settings shows up only after that/)).toBeInTheDocument()
  }, 30_000)

  it('a student outside a household turns reminders off with no parent notice', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Alex')
    const me = await src.createSelfStudentProfile({ displayName: 'Alex', graduationYear: 2027, gradeLevel: 12, independent: false, timeZone: 'UTC' })
    await src.saveReminderSettings(me, { ...(await src.reminderSettings(me)), enabled: true })
    renderAt('/student/reminders', src)
    await user.click(await screen.findByRole('switch'))
    expect(screen.queryByRole('alertdialog')).not.toBeInTheDocument()
    expect(await screen.findByText('Practice reminders are off.')).toBeInTheDocument()
    expect((await src.reminderHistory(me))[0]).toMatchObject({ enabled: false, notifyGuardians: false })
  }, 30_000)

  it('a reminder tap opens a short session', async () => {
    const { src } = await family()
    const start = vi.spyOn(src, 'startSession')
    renderAt('/student/practice?quick=1&r=abc', src)
    await vi.waitFor(() => expect(start).toHaveBeenCalled(), { timeout: 5000 })
    expect(start.mock.calls[0]![1]).toBe(5)
  }, 30_000)
})
