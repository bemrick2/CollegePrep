import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { DemoSource, DEMO_PARENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import type { InviteSendResult } from '../../lib/data/source'
import { StudentInvite } from './StudentInvite'
import { inviteEmail, pickOrigin } from '../../../../supabase/functions/send-household-invitation/email'

async function setup(send?: (r: InviteSendResult) => InviteSendResult) {
  const src = new DemoSource(emptyStore())
  src.switchPersona(DEMO_PARENT, 'Jordan')
  const hh = await src.createHousehold('Home', 'America/Chicago')
  const sid = await src.addStudent(hh, 'Riley', null, 8)
  if (send) {
    const real = src.sendStudentInvitation.bind(src)
    src.sendStudentInvitation = async (i) => send(await real(i))
  }
  render(
    <MemoryRouter>
      <AppProvider source={src}>
        <StudentInvite householdId={hh} student={{ id: sid, display_name: 'Riley' }} />
      </AppProvider>
    </MemoryRouter>,
  )
  return { src, hh, sid, user: userEvent.setup() }
}

describe('emailing a student invitation', () => {
  it('sends, and a replacement revokes the old invitation without adding a student', async () => {
    const { src, hh, sid, user } = await setup((r) => ({ ...r, emailed: true, reason: undefined }))
    await user.type(screen.getByLabelText('Recipient email'), 'riley@example.com')
    await user.click(screen.getByRole('button', { name: 'Send invitation' }))
    expect(await screen.findByText('Invitation sent')).toBeInTheDocument()
    expect(screen.getByText(/We emailed riley@example.com/)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Send invitation' }))
    await screen.findByText('Invitation sent')
    const invites = (await src.listInvitations(hh)).filter((i) => i.student_id === sid)
    expect(invites).toHaveLength(2)
    expect(invites.filter((i) => !i.revoked_at)).toHaveLength(1)
    const ctx = await src.getHouseholdContext()
    expect(ctx.students).toHaveLength(1)
    // The recipient email is the invitation's, not the student's.
    expect(JSON.stringify(ctx.students[0])).not.toContain('riley@example.com')
  })

  it('an email failure keeps the invitation usable and offers copy and retry', async () => {
    const { user } = await setup((r) => ({ ...r, emailed: false, reason: 'provider' }))
    await user.type(screen.getByLabelText('Recipient email'), 'riley@example.com')
    await user.click(screen.getByRole('button', { name: 'Send invitation' }))
    expect(await screen.findByText("We couldn't send the email")).toBeInTheDocument()
    expect(screen.getByText(/The invitation still works/)).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Copy invite link' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Copy invite code' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Try sending again' })).toBeEnabled()
  })

  it('revoking an outstanding invitation makes its code unusable', async () => {
    const { src, user } = await setup()
    await user.type(screen.getByLabelText('Recipient email'), 'riley@example.com')
    await user.click(screen.getByRole('button', { name: 'Send invitation' }))
    const code = (await screen.findByTestId('invite-code')).textContent!
    await user.click(screen.getByRole('button', { name: 'Revoke this invitation' }))
    expect(await screen.findByRole('button', { name: /Copy invite link or code instead/ })).toBeInTheDocument()
    await expect(src.acceptInvitation(code)).rejects.toThrow(/revoked/)
  })
})

describe('invitation email content', () => {
  it('links to our own site with the code attached, shows the code and 72 hours, and escapes names', () => {
    const code = 'f'.repeat(64)
    const m = inviteEmail({ origin: 'https://app.test', code, inviter: '<b>Jordan</b>', student: 'Riley', expiresAt: '2026-10-09T10:00:00Z' })
    expect(m.link).toBe(`https://app.test/join?code=${code}`)
    expect(m.html).toContain(`href="https://app.test/join?code=${code}"`)
    expect(m.html).toContain('Join Prep &amp; Price')
    expect(m.html).toContain('&lt;b&gt;Jordan&lt;/b&gt; invited you to join your Prep &amp; Price family.')
    expect(m.text).toContain(`Invite code: ${code}`)
    expect(m.text).toMatch(/Valid for 72 hours/)
    expect(m.subject).toBe('<b>Jordan</b> invited you to Prep & Price')
  })

  it('never uses an origin outside the allowlist', () => {
    const allowed = 'https://college-optimizer-staging.netlify.app, https://prepandprice.com/'
    expect(pickOrigin('https://evil.example', allowed)).toBe('https://college-optimizer-staging.netlify.app')
    expect(pickOrigin('https://prepandprice.com', allowed)).toBe('https://prepandprice.com')
    expect(pickOrigin(null, '')).toBeNull()
  })
})
