import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Route, Routes, useLocation } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import type { DataSource } from '../../lib/data/source'
import { Join } from './Join'

function Where() {
  const l = useLocation()
  return <p data-testid="where">{l.pathname + l.search}</p>
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
  const code = await src.createInvitation(hh, 'student', sid)
  src.switchPersona(DEMO_STUDENT, 'Riley')
  return { src, code, sid }
}

describe('joining with an invite', () => {
  it('a signed-out visitor on the live app is sent to sign-in and comes back with the code', async () => {
    const code = 'ab'.repeat(32)
    at(`/join?code=${code}`, signedOutLive())
    const where = await screen.findByTestId('where')
    const url = new URL(where.textContent!, 'https://x.test')
    expect(url.pathname).toBe('/auth')
    expect(url.searchParams.get('role')).toBe('student')
    expect(url.searchParams.get('next')).toBe(`/join?code=${code}`)
  })

  it('another browser (separate storage) gets "Invalid code" with the demo explanation, not "expired"', async () => {
    const { code } = await parentWithInvite()
    const other = new DemoSource(emptyStore())
    other.switchPersona(DEMO_STUDENT, 'Riley')
    const user = userEvent.setup()
    at(`/join?code=${code}`, other)
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    expect(await screen.findByText('Invalid code')).toBeInTheDocument()
    expect(screen.getByText(/only work in the browser that created them/)).toBeInTheDocument()
    expect(screen.queryByText(/expired/i)).not.toBeInTheDocument()
  })

  it('claims the guardian-created profile once; reuse says "Already used"; a lapsed code says "Expired code"', async () => {
    const { src, code, sid } = await parentWithInvite()
    const user = userEvent.setup()
    const ui = at(`/join?code=${code}`, src)
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    expect(await screen.findByTestId('where')).toHaveTextContent('/student')
    const ctx = await src.getHouseholdContext()
    expect(ctx.myStudent?.id).toBe(sid) // same profile, no duplicate
    expect(ctx.students.filter((s) => s.display_name === 'Riley')).toHaveLength(1)
    ui.unmount()
    await expect(src.acceptInvitation(code)).rejects.toThrow(/already been used/)

    const again = await parentWithInvite()
    ;(again.src as unknown as { s: { invitations: { expires_at: string }[] } }).s.invitations[0]!.expires_at = new Date(Date.now() - 1000).toISOString()
    at(`/join?code=${again.code}`, again.src)
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    expect(await screen.findByText('Expired code')).toBeInTheDocument()
    expect(screen.getByText(/valid for 72 hours/)).toBeInTheDocument()
  })
})
