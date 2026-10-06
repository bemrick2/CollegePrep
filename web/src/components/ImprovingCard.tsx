import type { Verdict } from '../lib/engine/improving'
import { Card, cx } from './ui'

/** One-line answer to "Am I improving?" with its basis. Practice accuracy, never an ACT/SAT score. */
export function ImprovingCard({ v, title = 'Am I improving?' }: { v: Verdict; title?: string }) {
  return (
    <Card className={cx('p-4', v.tone === 'go' && 'border-go/40', v.tone === 'warn' && 'border-warn/40')}>
      <div className="text-xs font-semibold uppercase tracking-wide text-ink-3">{title}</div>
      <div className={cx('mt-1 font-semibold', v.tone === 'go' ? 'text-go-strong dark:text-go' : v.tone === 'warn' ? 'text-warn' : 'text-ink')}>{v.headline}</div>
      <p className="mt-0.5 text-sm text-ink-2">{v.detail}</p>
    </Card>
  )
}
