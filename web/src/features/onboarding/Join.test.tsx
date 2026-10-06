import { beforeEach, describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Route, Routes, useLocation } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import type { DataSource } from '../../lib/data/source'
import { readPendingInvite } from '../../lib/invites'
import { Join } from './Join'

function Where() {
  const l = useLocation()
  return <p data-testid="where">{l.pathname + l.search + l.hash}</p>
}

function at(path: string, source: DataSource) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <AppProvider source={source}>
        <Routes>
          <Route path="/join" element={<Join />} />
          <Route path="*" element={<Where />} />
        </Routes>
      </AppProvider>
    </MemoryRouter>,
  )
}

/** A live-mode source with nobody signed in: what a student's own new browser sees. */
function signedOutLive(): DataSource {
  const s = new DemoSource(emptyStore())
  return Object.assign(Object.create(s) as DataSource, { mode: 'live' as const })
}

async function parentWithInvite() {
  const src = new DemoSource(emptyStore())
  src.switchPersona(DEMO_PARENT, 'Jordan')
  const hh = await src.createHousehold('Home', 'America/Chicago')
  const sid = await src.addStudent(hh, 'Riley', null, 11)
  const inv = await src.createStudentInvitation(hh, sid)
  src.switchPersona(DEMO_STUDENT, 'Riley')
  return { src, hh, sid, ...inv }
}

beforeEach(() => localStorage.clear())

describe('joining with an invite', () => {
  it('a signed-out visitor keeps the link token out of the URL and finds it again after sign-up', async () => {
    const token = 'ab'.repeat(32)
    at(`/join#t=${token}`, signedOutLive())
    const where = await screen.findByTestId('where')
    expect(where.textContent).toBe('/auth?role=student&next=%2Fjoin')
    expect(where.textContent).not.toContain(token)
    expect(readPendingInvite()).toBe(token) // survives the email-confirmation round trip in this browser
  })

  it('an emailed link joins with no typing; the human code joins too, any case', async () => {
    const a = await parentWithInvite()
    const user = userEvent.setup()
    const ui = at(`/join#t=${a.code}`, a.src)
    expect(await screen.findByText('Invitation attached')).toBeInTheDocument()
    expect(screen.queryByDisplayValue(a.code)).not.toBeInTheDocument() // the token is never shown
    await user.click(screen.getByRole('button', { name: 'Join' }))
    expect(await screen.findByTestId('where')).toHaveTextContent('/student')
    ui.unmount()

    const b = await parentWithInvite()
    at('/join', b.src)
    await user.type(await screen.findByLabelText('Invite code'), b.inviteCode.toLowerCase())
    await user.click(screen.getByRole('button', { name: 'Join' }))
    expect(await screen.findByTestId('where')).toHaveTextContent('/student')
    const ctx = await b.src.getHouseholdContext()
    expect(ctx.myStudent?.id).toBe(b.sid)
    expect(ctx.students.filter((s) => s.display_name === 'Riley')).toHaveLength(1)
  })

  it('another browser (separate storage) gets "Invalid invitation" with the demo explanation, not "expired"', async () => {
    const { inviteCode } = await parentWithInvite()
    const other = new DemoSource(emptyStore())
    other.switchPersona(DEMO_STUDENT, 'Riley')
    const user = userEvent.setup()
    at('/join', other)
    await user.type(await screen.findByLabelText('Invite code'), inviteCode)
    await user.click(screen.getByRole('button', { name: 'Join' }))
    expect(await screen.findByText('Invalid invitation')).toBeInTheDocument()
    expect(screen.getByText(/only work in the browser that created them/)).toBeInTheDocument()
    expect(screen.queryByText(/expired/i)).not.toBeInTheDocument()
  })

  it('used, cancelled and expired invitations each say so', async () => {
    const user = userEvent.setup()
    const used = await parentWithInvite()
    await used.src.acceptInvitation(used.inviteCode)
    const u = at(`/join#t=${used.code}`, used.src)
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    expect(await screen.findByText('Invitation already used')).toBeInTheDocument()
    u.unmount()

    // A replacement cancels the earlier invitation.
    const old = await parentWithInvite()
    old.src.switchPersona(DEMO_PARENT, 'Jordan')
    await old.src.createStudentInvitation(old.hh, old.sid)
    old.src.switchPersona(DEMO_STUDENT, 'Riley')
    const r = at('/join', old.src)
    await user.type(await screen.findByLabelText('Invite code'), old.inviteCode)
    await user.click(screen.getByRole('button', { name: 'Join' }))
    expect(await screen.findByText('Invitation cancelled')).toBeInTheDocument()
    r.unmount()

    const lapsed = await parentWithInvite()
    ;(lapsed.src as unknown as { s: { invitations: { expires_at: string }[] } }).s.invitations[0]!.expires_at = new Date(Date.now() - 1000).toISOString()
    at(`/join#t=${lapsed.code}`, lapsed.src)
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    expect(await screen.findByText('Invitation expired')).toBeInTheDocument()
    expect(screen.getByText(/valid for 72 hours/)).toBeInTheDocument()
  })
})
