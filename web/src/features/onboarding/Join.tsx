import { useEffect, useState, type FormEvent } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { Button, Field, Notice, PageLoading, inputClass } from '../../components/ui'
import { inviteFailure, inviteFailureCopy, parseInviteInput } from '../../lib/invites'
import { StepFrame } from './Stepper'

/** A code the live backend issues (64 hex characters); demo codes are 8 letters and never look like this. */
const LIVE_CODE = /^[0-9a-f]{64}$/i

export function Join() {
  const { source, viewer, loading, refresh, mode, liveAvailable, useLive } = useApp()
  const [params] = useSearchParams()
  const navigate = useNavigate()
  const fromLink = parseInviteInput(params.get('code') ?? '')
  const [code, setCode] = useState(fromLink)
  const [error, setError] = useState<{ title: string; body: string } | null>(null)
  const [busy, setBusy] = useState(false)

  // A real invite link opened in a browser that last used the demo goes to the real backend, never demo storage.
  const switchToLive = liveAvailable && mode === 'demo' && LIVE_CODE.test(fromLink)
  useEffect(() => {
    if (switchToLive) useLive()
  }, [switchToLive]) // eslint-disable-line react-hooks/exhaustive-deps

  if (loading || switchToLive) return <PageLoading />
  if (!viewer) {
    if (mode === 'live') {
      const next = `/join${fromLink ? `?code=${encodeURIComponent(fromLink)}` : ''}`
      return <Navigate to={`/auth?role=student&next=${encodeURIComponent(next)}`} replace />
    }
    return <Navigate to="/" replace />
  }

  const submit = async (e?: FormEvent) => {
    e?.preventDefault()
    setBusy(true)
    setError(null)
    try {
      await source.acceptInvitation(parseInviteInput(code))
      await refresh()
      const ctx = await source.getHouseholdContext()
      navigate(ctx.myStudent ? '/student' : '/parent')
    } catch (err) {
      const raw = err instanceof Error ? err.message : 'That code did not work'
      setError(inviteFailureCopy(inviteFailure(raw), raw, mode === 'demo'))
    } finally {
      setBusy(false)
    }
  }

  return (
    <StepFrame
      step={1}
      total={1}
      title="Join your household"
      subtitle="Enter the code or open the link your parent or guardian shared. Your practice history always stays with you."
      onBack={() => navigate(-1)}
      footer={
        <Button size="lg" block disabled={busy || parseInviteInput(code).length < 6} onClick={() => void submit()}>
          {busy ? 'Joining…' : 'Join'}
        </Button>
      }
    >
      <form onSubmit={submit}>
        {mode === 'demo' && (
          <Notice tone="gold" title="Demo mode" className="mb-4">
            Demo codes only work in this browser.{liveAvailable ? ' To join from another device, use a real account.' : ''}
          </Notice>
        )}
        <Field label="Invite code" htmlFor="code" hint="Paste the whole code or the invite link.">
          <input
            id="code"
            className={`${inputClass} font-mono text-base`}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            autoComplete="one-time-code"
            autoCapitalize="none"
            spellCheck={false}
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
