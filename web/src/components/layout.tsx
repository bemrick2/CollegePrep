import type { ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { cx } from './ui'

/**
 * Page structure for the redesign: one answer first, then sections separated by space and a hairline, not cards.
 * Typography and figures carry hierarchy; color is reserved for meaning (good, caution, plan).
 */

export function PageHeader({ kicker, title, children, actions }: { kicker?: ReactNode; title: ReactNode; children?: ReactNode; actions?: ReactNode }) {
  return (
    <header className="flex flex-wrap items-end justify-between gap-x-6 gap-y-3">
      <div className="min-w-0">
        {kicker && <p className="text-sm font-medium text-ink-3">{kicker}</p>}
        <h1 className="display mt-0.5 text-[28px] leading-tight text-ink md:text-[34px]">{title}</h1>
        {children && <div className="mt-1.5 max-w-2xl text-[15px] text-ink-2">{children}</div>}
      </div>
      {actions && <div className="flex min-w-0 max-w-full flex-wrap items-center gap-2">{actions}</div>}
    </header>
  )
}

export function Section({
  title,
  subtitle,
  action,
  children,
  className,
  id,
  divider = true,
}: {
  title?: ReactNode
  subtitle?: ReactNode
  action?: ReactNode
  children: ReactNode
  className?: string
  id?: string
  divider?: boolean
}) {
  return (
    <section aria-labelledby={title && id ? id : undefined} className={cx(divider && 'border-t border-line pt-6', className)}>
      {(title || action) && (
        <div className="mb-3 flex flex-wrap items-baseline justify-between gap-x-4 gap-y-2">
          <div className="min-w-0">
            {title && (
              <h2 id={id} className="text-[17px] font-bold text-ink">
                {title}
              </h2>
            )}
            {subtitle && <p className="mt-0.5 text-sm text-ink-3">{subtitle}</p>}
          </div>
          {action && <div className="min-w-0 max-w-full text-sm">{action}</div>}
        </div>
      )}
      {children}
    </section>
  )
}

/** A number that answers the screen's question. */
export function Figure({ value, label, sub, size = 'lg', tone }: { value: ReactNode; label: ReactNode; sub?: ReactNode; size?: 'xl' | 'lg' | 'md'; tone?: 'go' | 'warn' | 'muted' }) {
  return (
    <div className="min-w-0">
      <div
        className={cx(
          'figure',
          size === 'xl' ? 'text-[52px] md:text-[64px]' : size === 'lg' ? 'text-[36px] md:text-[40px]' : 'text-[26px]',
          tone === 'go' ? 'text-go-strong dark:text-go' : tone === 'warn' ? 'text-warn' : tone === 'muted' ? 'text-ink-3' : 'text-ink',
        )}
      >
        {value}
      </div>
      <div className={cx('font-semibold text-ink', size === 'xl' ? 'mt-2 text-base' : 'mt-1.5 text-sm')}>{label}</div>
      {sub && <div className="mt-0.5 text-sm text-ink-3">{sub}</div>}
    </div>
  )
}

export function RowList({ children, className }: { children: ReactNode; className?: string }) {
  return <ul className={cx('divide-y divide-line border-y border-line', className)}>{children}</ul>
}

/** A list row: title and meta on the left, a value on the right; the whole row links when `to` is given. */
export function Row({ title, meta, value, to, children }: { title: ReactNode; meta?: ReactNode; value?: ReactNode; to?: string; children?: ReactNode }) {
  const body = (
    <div className="flex items-center justify-between gap-4 py-3.5">
      <div className="min-w-0">
        <div className={cx('font-semibold text-ink', to && 'group-hover:underline')}>{title}</div>
        {meta && <div className="mt-0.5 text-sm text-ink-3">{meta}</div>}
        {children}
      </div>
      {value !== undefined && <div className="shrink-0 text-right">{value}</div>}
    </div>
  )
  return <li>{to ? <Link to={to} className="group block rounded-sm">{body}</Link> : body}</li>
}

/** A short ordered step list for "what to do next". */
export function NextSteps({ items }: { items: { key: string; title: ReactNode; detail?: ReactNode; to?: string }[] }) {
  return (
    <ol className="grid gap-1">
      {items.map((a, i) => {
        const body = (
          <div className="flex gap-3 py-2.5">
            <span className="mt-0.5 grid h-6 w-6 shrink-0 place-items-center rounded-full bg-brand-soft text-xs font-bold text-brand" aria-hidden>
              {i + 1}
            </span>
            <div className="min-w-0">
              <div className={cx('font-semibold text-ink', a.to && 'group-hover:underline')}>{a.title}</div>
              {a.detail && <div className="mt-0.5 text-sm text-ink-2">{a.detail}</div>}
            </div>
          </div>
        )
        return <li key={a.key}>{a.to ? <Link to={a.to} className="group block rounded-sm">{body}</Link> : body}</li>
      })}
    </ol>
  )
}

export const compactUsd = (n: number) =>
  n >= 100_000 ? `$${Math.round(n / 1000)}K` : n >= 10_000 ? `$${(n / 1000).toFixed(1).replace(/\.0$/, '')}K` : n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })
