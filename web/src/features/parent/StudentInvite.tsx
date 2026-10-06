import { useEffect, useState, type FormEvent } from 'react'
import { useApp } from '../../lib/app'
import type { InvitationSummary, InviteSendResult } from '../../lib/data/source'
import { Button, Field, Notice, inputClass } from '../../components/ui'
import { InviteCode } from '../onboarding/InviteCode'
import { INVITE_TTL_HOURS } from '../../lib/invites'

const when = (iso: string) => new Date(iso).toLocaleString(undefined, { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' })

const FAIL_COPY: Record<NonNullable<InviteSendResult['reason']>, string> = {
  not_configured: 'Email sending isn’t set up yet.',
  provider: 'The email service didn’t accept the message.',
  rejected: '',
  demo: '',
}

/**
 * Invite one guardian-created student to their own login, by email (sent server-side) or by link/code.
 * The plain code is only ever held in this page's memory; the backend keeps a hash.
 */
export function StudentInvite({
  householdId,
  student,
  onInvitesChanged,
  onTryDemo,
  showTitle = true,
}: {
  householdId: string
  student: { id: string; display_name: string }
  onInvitesChanged?: () => void
  /** Demo only: switch to the student persona and open the link in this browser. */
  onTryDemo?: (code: string) => void
  /** Off where the page title already says who is being invited. */
  showTitle?: boolean
}) {
  const { source, mode } = useApp()
  const [email, setEmail] = useState('')
  const [code, setCode] = useState<string | null>(null)
  const [currentId, setCurrentId] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const [result, setResult] = useState<{ kind: 'sent' | 'failed' | 'demo'; to: string; detail?: string } | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [invites, setInvites] = useState<InvitationSummary[]>([])
  const [tick, setTick] = useState(0)

  useEffect(() => {
    let alive = true
    source
      .listInvitations(householdId)
      .then((all) => alive && setInvites(all.filter((i) => i.student_id === student.id)))
      .catch(() => alive && setInvites([]))
    return () => {
      alive = false
    }
  }, [source, householdId, student.id, tick])

  const now = new Date().toISOString()
  const outstanding = invites.find((i) => !i.accepted_at && !i.revoked_at && i.expires_at > now)
  const lastExpired = !outstanding && invites.find((i) => !i.accepted_at && !i.revoked_at && i.expires_at <= now)
  const changed = () => {
    setTick((t) => t + 1)
    onInvitesChanged?.()
  }

  const send = async (e?: FormEvent, resendCode?: string) => {
    e?.preventDefault()
    setBusy(true)
    setError(null)
    setResult(null)
    const to = email.trim()
    try {
      const r = await source.sendStudentInvitation({ householdId, studentId: student.id, email: to, code: resendCode })
      if (r.code) setCode(r.code)
      if (r.invitationId) setCurrentId(r.invitationId)
      if (r.emailed) setResult({ kind: 'sent', to })
      else if (r.reason === 'demo') setResult({ kind: 'demo', to })
      else setResult({ kind: 'failed', to, detail: r.reason === 'rejected' ? r.error : FAIL_COPY[r.reason ?? 'provider'] })
      changed()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Could not create the invitation')
    } finally {
      setBusy(false)
    }
  }

  const linkOnly = async () => {
    setBusy(true)
    setError(null)
    setResult(null)
    try {
      // A new link replaces any outstanding one, as an emailed replacement does.
      for (const i of invites) if (!i.accepted_at && !i.revoked_at && i.expires_at > new Date().toISOString()) await source.revokeInvitation(i.id)
      setCode(await source.createInvitation(householdId, 'student', student.id))
      changed()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Could not create the invitation')
    } finally {
      setBusy(false)
    }
  }

  const revoke = async (id: string) => {
    setError(null)
    try {
      await source.revokeInvitation(id)
      setCode(null)
      setCurrentId(null)
      setResult(null)
      changed()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Could not revoke the invitation')
    }
  }

  const inputId = `invite-email-${student.id}`
  return (
    <section aria-label={`Invite ${student.display_name}`} className="grid gap-3">
      {showTitle && <h3 className="font-semibold text-ink">Invite {student.display_name}</h3>}
      <form onSubmit={(e) => void send(e)} className="grid gap-2 sm:grid-cols-[1fr_auto] sm:items-end">
        <Field label="Recipient email" htmlFor={inputId}>
          <input id={inputId} type="email" autoComplete="off" className={inputClass} value={email} onChange={(e) => setEmail(e.target.value)} placeholder="their own email" />
        </Field>
        <Button type="submit" className="h-12" disabled={busy || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.trim())}>
          {busy ? 'Sending…' : 'Send invitation'}
        </Button>
      </form>
      <p className="text-xs text-ink-3">
        Used only to send this invitation. It isn’t added to {student.display_name}’s profile, and they still create their own account. Works once, valid for{' '}
        {INVITE_TTL_HOURS} hours.
      </p>

      {result?.kind === 'sent' && (
        <Notice tone="info" title="Invitation sent">
          We emailed {result.to}. The link works once and is valid for {INVITE_TTL_HOURS} hours.
        </Notice>
      )}
      {result?.kind === 'demo' && (
        <Notice tone="gold" title="Demo mode doesn’t send email">
          The invitation was created. Copy the link below to try it in this browser.
        </Notice>
      )}
      {result?.kind === 'failed' && (
        <Notice tone="bad" title="We couldn't send the email">
          {result.detail ? `${result.detail} ` : ''}
          {code ? 'The invitation still works: copy the link below and send it yourself, or try again.' : 'Try again, or create a link to share yourself.'}
          {code && (
            <div className="mt-2">
              <Button size="sm" variant="secondary" disabled={busy || !email.trim()} onClick={() => void send(undefined, code)}>
                Try sending again
              </Button>
            </div>
          )}
        </Notice>
      )}
      {error && <Notice tone="bad">{error}</Notice>}

      {code ? (
        <>
          <InviteCode code={code} />
          {mode === 'demo' && onTryDemo && (
            <Button variant="secondary" onClick={() => onTryDemo(code)}>
              Try it as {student.display_name} (demo)
            </Button>
          )}
        </>
      ) : (
        <div className="flex flex-wrap items-center gap-x-4 gap-y-2 text-sm">
          <button type="button" className="font-semibold text-brand hover:underline disabled:opacity-50" disabled={busy} onClick={() => void linkOnly()}>
            {outstanding ? 'Create a new link to copy' : 'Copy invite link or code instead'}
          </button>
        </div>
      )}

      {outstanding && !code && (
        <div className="flex flex-wrap items-center justify-between gap-2 rounded-lg bg-surface-2 px-3 py-2 text-sm">
          <span className="text-ink-2">
            Invitation outstanding{outstanding.recipient_email ? ` for ${outstanding.recipient_email}` : ''}, valid until {when(outstanding.expires_at)}.
          </span>
          <button type="button" className="font-semibold text-bad hover:underline" onClick={() => void revoke(outstanding.id)}>
            Revoke invitation
          </button>
        </div>
      )}
      {code && (currentId ?? outstanding?.id) && (
        <button type="button" className="justify-self-start text-sm font-semibold text-bad hover:underline" onClick={() => void revoke((currentId ?? outstanding!.id)!)}>
          Revoke this invitation
        </button>
      )}
      {lastExpired && !code && (
        <p className="text-sm text-ink-3">
          The last invitation{lastExpired.recipient_email ? ` to ${lastExpired.recipient_email}` : ''} expired {when(lastExpired.expires_at)}. Send a new one above.
        </p>
      )}
      {mode === 'demo' && !code && <p className="text-xs text-ink-3">Demo mode: invitations stay in this browser and no email is sent.</p>}
    </section>
  )
}
