import { useState } from 'react'
import { Button } from '../../components/ui'

export function InviteCode({ code }: { code: string }) {
  const [copied, setCopied] = useState(false)
  return (
    <div className="rounded-2xl border-2 border-dashed border-line-strong bg-surface p-5 text-center">
      <div className="text-xs font-semibold uppercase tracking-wide text-ink-3">Invite code</div>
      <div className="mt-2 font-mono text-3xl font-bold tracking-[0.2em] text-ink" aria-live="polite">
        {code}
      </div>
      <Button
        variant="secondary"
        size="sm"
        className="mt-4"
        onClick={async () => {
          try {
            await navigator.clipboard.writeText(code)
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
          } catch {
            // Clipboard blocked; the code is visible to copy by hand.
          }
        }}
      >
        {copied ? 'Copied' : 'Copy code'}
      </Button>
    </div>
  )
}
