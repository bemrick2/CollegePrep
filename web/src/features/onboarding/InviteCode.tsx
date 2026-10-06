import { useState } from 'react'
import { useApp } from '../../lib/app'
import { Button, Notice } from '../../components/ui'
import { INVITE_TTL_HOURS, inviteExpiry, inviteLink } from '../../lib/invites'

/**
 * A freshly created invitation. The plain code exists only in this browser's memory: the backend stores a
 * SHA-256 digest, so the code can't be shown again later (create a new one instead).
 */
export function InviteCode({ code }: { code: string }) {
  const { mode, liveAvailable } = useApp()
  const [copied, setCopied] = useState<'code' | 'link' | null>(null)
  const [expires] = useState(() => inviteExpiry(new Date()))
  const link = inviteLink(code)
  const copy = async (what: 'code' | 'link') => {
    try {
      await navigator.clipboard.writeText(what === 'code' ? code : link)
      setCopied(what)
      setTimeout(() => setCopied(null), 2000)
    } catch {
      // Clipboard blocked; the code is visible to copy by hand.
    }
  }
  const short = code.length <= 12
  return (
    <div className="grid gap-3">
      <div className="rounded-2xl border-2 border-dashed border-line-strong bg-surface p-5 text-center">
        <div className="text-sm font-semibold text-ink-3">Invite code</div>
        <div
          className={short ? 'mt-2 font-mono text-3xl font-bold tracking-[0.2em] text-ink' : 'mt-2 break-all font-mono text-sm font-semibold leading-relaxed text-ink'}
          aria-live="polite"
          data-testid="invite-code"
        >
          {code}
        </div>
        <p className="mt-2 text-sm text-ink-2">
          Works once. Valid for {INVITE_TTL_HOURS} hours, until{' '}
          <time dateTime={expires.toISOString()}>{expires.toLocaleString(undefined, { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' })}</time>.
        </p>
        <div className="mt-4 flex flex-wrap justify-center gap-2">
          <Button variant="brand" size="sm" onClick={() => void copy('link')}>
            {copied === 'link' ? 'Link copied' : 'Copy invite link'}
          </Button>
          <Button variant="secondary" size="sm" onClick={() => void copy('code')}>
            {copied === 'code' ? 'Code copied' : 'Copy invite code'}
          </Button>
        </div>
      </div>
      {mode === 'demo' && (
        <Notice tone="gold" title="Demo code">
          This code is stored only in this browser, so it won't work on another device or in a private window.
          {liveAvailable ? ' Create real accounts to test with two devices.' : ''}
        </Notice>
      )}
    </div>
  )
}
