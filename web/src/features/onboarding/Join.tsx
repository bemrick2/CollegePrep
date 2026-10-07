import { useEffect, useState, type FormEvent } from 'react'
import { Navigate, useLocation, useNavigate, useSearchParams } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { Button, Field, Notice, PageLoading, inputClass } from '../../components/ui'
import { LINK_TOKEN, clearPendingInvite, inviteFailure, inviteFailureCopy, parseInviteInput, readPendingInvite, savePendingInvite } from '../../lib/invites'
import { StepFrame } from './Stepper'

/** Outcomes that settle an invitation for good: forget a stored link once one of these comes back. */
const FINAL = new Set(['invalid', 'expired', 'used', 'revoked', 'already_member', 'already_linked'])

export function Join() {
  const { source, viewer, loading, refresh, mode, liveAvailable, useLive } = useApp()
  const [params] = useSearchParams()
  const { hash } = useLocation()
  const navigate = useNavigate()
  // The emailed link carries its token in the fragment (#t=…); older links used ?code=. A link opened before
  // signing in is remembered in this browser until the account exists.
  const fromUrl = parseInviteInput(hash.startsWith('#t=') ? hash : params.get('code') ?? '')
  const [token] = useState(() => fromUrl || readPendingInvite() || '')
  const linked = token !== '' && !/^[A-Za-z0-9]{5}-?[A-Za-z0-9]{5}$/.test(token)
  const [code, setCode] = useState(linked ? '' : token)
  const [error, setError] = useState<{ title: string; body: string } | null>(null)
  const [busy, setBusy] = useState(false)

  // A real invite link opened in a browser that last used the demo goes to the real backend, never demo storage.
  const switchToLive = liveAvailable && mode === 'demo' && LINK_TOKEN.test(token)
  useEffect(() => {
    if (switchToLive) useLive()
  }, [switchToLive]) // eslint-disable-line react-hooks/exhaustive-deps

  if (loading || switchToLive) return <PageLoading />
  if (!viewer) {
    if (mode === 'live') {
      // Keep the link token out of URLs and logs: hold it in this browser while the student signs up/confirms.
      if (linked) savePendingInvite(token)
      return <Navigate to="/auth?role=student&next=%2Fjoin" replace />
    }
    return <Navigate to="/" replace />
  }

  const value = code.trim() ? parseInviteInput(code) : linked ? token : ''
  const submit = async (e?: FormEvent) => {
    e?.preventDefault()
    setBusy(true)
    setError(null)
    try {
      await source.acceptInvitation(value)
      clearPendingInvite()
      await refresh()
      const ctx = await source.getHouseholdContext()
      // A joined student finishes setup with only what the guardian didn't already supply.
      navigate(ctx.myStudent ? '/onboarding/student' : '/parent')
    } catch (err) {
      const raw = err instanceof Error ? err.message : 'That code did not work'
      const kind = inviteFailure(raw)
      if (FINAL.has(kind) && value === token) clearPendingInvite()
      setError(inviteFailureCopy(kind, raw, mode === 'demo'))
    } finally {
      setBusy(false)
    }
  }

  return (
    <StepFrame
      step={1}
      total={1}
      title="Join your household"
      subtitle="Your parent or guardian invited you. Your practice history always stays with you."
      onBack={() => navigate(-1)}
      footer={
        <Button size="lg" block disabled={busy || value.length < 10} onClick={() => void submit()}>
          {busy ? 'Joining…' : 'Join'}
        </Button>
      }
    >
      <form onSubmit={submit}>
        {mode === 'demo' && (
          <Notice tone="gold" title="Demo mode" className="mb-4">
            Demo invitations only work in this browser.{liveAvailable ? ' To join from another device, use a real account.' : ''}
          </Notice>
        )}
        {linked && !code.trim() && (
          <Notice tone="info" title="Invitation attached" className="mb-4">
            Your invitation link is ready. Select Join to connect your account.
          </Notice>
        )}
        <Field label={linked ? 'Or enter an invite code' : 'Invite code'} htmlFor="code" hint="Looks like K7M4P-9Q2TX. Not case-sensitive.">
          <input
            id="code"
            className={`${inputClass} font-mono text-lg uppercase tracking-[0.1em]`}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            autoComplete="one-time-code"
            autoCapitalize="characters"
            spellCheck={false}
            placeholder="XXXXX-XXXXX"
          />
        </Field>
        {error && (
          <Notice tone="bad" title={error.title} className="mt-4">
            {error.body}
          </Notice>
        )}
      </form>
    </StepFrame>
  )
}
