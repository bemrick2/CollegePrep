import { useState } from 'react'
import { useApp } from '../../lib/app'
import { Button, Notice } from '../../components/ui'
import { INVITE_TTL_HOURS, formatInviteCode, inviteExpiry, inviteLink } from '../../lib/invites'

/**
 * A freshly created invitation. People see the short invite code; the long link token only ever travels inside
 * the copied link. Neither can be shown again later (the backend keeps digests), so a new invite replaces it.
 */
export function InviteCode({ token, inviteCode, expiresAt }: { token: string; inviteCode?: string | null; expiresAt?: string | null }) {
  const { mode, liveAvailable } = useApp()
  const [copied, setCopied] = useState<'code' | 'link' | null>(null)
  const [fallbackExpiry] = useState(() => inviteExpiry(new Date()))
  const expires = expiresAt ? new Date(expiresAt) : fallbackExpiry
  const link = inviteLink(token)
  const code = inviteCode ? formatInviteCode(inviteCode) : null
  const copy = async (what: 'code' | 'link') => {
    try {
      await navigator.clipboard.writeText(what === 'code' && code ? code : link)
      setCopied(what)
      setTimeout(() => setCopied(null), 2000)
    } catch {
      // Clipboard blocked; the code is visible to copy by hand.
    }
  }
  return (
    <div className="grid gap-3">
      <div className="rounded-2xl border-2 border-dashed border-line-strong bg-surface p-5 text-center">
        {code && (
          <>
            <div className="text-sm font-semibold text-ink-3">Invite code</div>
            <div className="mt-2 font-mono text-3xl font-bold tracking-[0.12em] text-ink" aria-live="polite" data-testid="invite-code">
              {code}
            </div>
          </>
        )}
        <p className={code ? 'mt-2 text-sm text-ink-2' : 'text-sm text-ink-2'}>
          Works once. Valid for {INVITE_TTL_HOURS} hours, until{' '}
          <time dateTime={expires.toISOString()}>{expires.toLocaleString(undefined, { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' })}</time>.
        </p>
        <div className="mt-4 flex flex-wrap justify-center gap-2">
          <Button variant="brand" size="sm" onClick={() => void copy('link')}>
            {copied === 'link' ? 'Link copied' : 'Copy invite link'}
          </Button>
          {code && (
            <Button variant="secondary" size="sm" onClick={() => void copy('code')}>
              {copied === 'code' ? 'Code copied' : 'Copy invite code'}
            </Button>
          )}
        </div>
      </div>
      {mode === 'demo' && (
        <Notice tone="gold" title="Demo code">
          This invitation is stored only in this browser, so it won't work on another device or in a private window.
          {liveAvailable ? ' Create real accounts to test with two devices.' : ''}
        </Notice>
      )}
    </div>
  )
}
