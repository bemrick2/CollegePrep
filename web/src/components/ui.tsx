import { forwardRef, type ButtonHTMLAttributes, type HTMLAttributes, type ReactNode } from 'react'
import { Link, type LinkProps } from 'react-router-dom'

export function cx(...parts: (string | false | null | undefined)[]) {
  return parts.filter(Boolean).join(' ')
}

type Variant = 'go' | 'brand' | 'secondary' | 'ghost' | 'danger'
type Size = 'sm' | 'md' | 'lg'

const variants: Record<Variant, string> = {
  go: 'bg-go text-white hover:bg-go-strong shadow-[0_2px_0_0_var(--go-strong)] active:translate-y-px active:shadow-none dark:text-bg',
  brand: 'bg-brand text-brand-ink hover:bg-brand-2',
  secondary: 'bg-surface text-ink border border-line-strong hover:bg-surface-2',
  ghost: 'text-ink-2 hover:bg-surface-2 hover:text-ink',
  danger: 'bg-bad text-white hover:opacity-90',
}
const sizes: Record<Size, string> = {
  sm: 'h-9 px-3 text-sm rounded-lg gap-1.5',
  md: 'h-11 px-4 text-[15px] rounded-xl gap-2',
  lg: 'h-14 px-6 text-base rounded-2xl gap-2',
}

export function buttonClass(variant: Variant = 'go', size: Size = 'md', block = false) {
  return cx(
    'inline-flex items-center justify-center font-semibold transition-colors duration-150 select-none disabled:opacity-50 disabled:pointer-events-none',
    variants[variant],
    sizes[size],
    block && 'w-full',
  )
}

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant
  size?: Size
  block?: boolean
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { variant = 'go', size = 'md', block, className, type = 'button', ...rest },
  ref,
) {
  return <button ref={ref} type={type} className={cx(buttonClass(variant, size, block), className)} {...rest} />
})

export function ButtonLink({ variant = 'go', size = 'md', block, className, ...rest }: LinkProps & { variant?: Variant; size?: Size; block?: boolean }) {
  return <Link className={cx(buttonClass(variant, size, block), className)} {...rest} />
}

export function Card({ className, as: As = 'section', ...rest }: HTMLAttributes<HTMLElement> & { as?: 'section' | 'div' | 'article' }) {
  // Cards are for things you act on or that must stand apart; most content sits directly on the page.
  return <As className={cx('rounded-xl border border-line bg-surface', className)} {...rest} />
}

export function CardHeader({ title, subtitle, action, id }: { title: ReactNode; subtitle?: ReactNode; action?: ReactNode; id?: string }) {
  return (
    <div className="flex items-start justify-between gap-3 px-5 pt-5">
      <div className="min-w-0">
        <h2 id={id} className="text-[15px] font-semibold text-ink">
          {title}
        </h2>
        {subtitle && <p className="mt-0.5 text-sm text-ink-3">{subtitle}</p>}
      </div>
      {action}
    </div>
  )
}

type Tone = 'neutral' | 'go' | 'gold' | 'bad' | 'warn' | 'info' | 'brand'
const tones: Record<Tone, string> = {
  neutral: 'bg-surface-2 text-ink-2',
  go: 'bg-go-soft text-go-strong dark:text-go',
  gold: 'bg-gold-soft text-gold-ink',
  bad: 'bg-bad-soft text-bad',
  warn: 'bg-warn-soft text-warn',
  info: 'bg-info-soft text-info',
  brand: 'bg-brand-soft text-brand',
}

export function Pill({ tone = 'neutral', className, children }: { tone?: Tone; className?: string; children: ReactNode }) {
  return <span className={cx('inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-xs font-semibold', tones[tone], className)}>{children}</span>
}

export function ProgressBar({ value, max = 1, tone = 'go', label, className }: { value: number; max?: number; tone?: 'go' | 'gold' | 'brand' | 'bad' | 'warn'; label: string; className?: string }) {
  const pct = max > 0 ? Math.max(0, Math.min(1, value / max)) : 0
  const color = { go: 'bg-go', gold: 'bg-gold', brand: 'bg-brand', bad: 'bg-bad', warn: 'bg-warn' }[tone]
  return (
    <div
      role="progressbar"
      aria-label={label}
      aria-valuemin={0}
      aria-valuemax={max}
      aria-valuenow={Math.round(value)}
      className={cx('h-2.5 w-full overflow-hidden rounded-full bg-surface-3', className)}
    >
      <div className={cx('h-full rounded-full transition-[width] duration-500 ease-out', color)} style={{ width: `${pct * 100}%` }} />
    </div>
  )
}

export function Ring({
  value,
  max = 1,
  size = 120,
  stroke = 12,
  tone = 'go',
  children,
  label,
}: {
  value: number
  max?: number
  size?: number
  stroke?: number
  tone?: 'go' | 'gold' | 'brand'
  children?: ReactNode
  label: string
}) {
  const r = (size - stroke) / 2
  const c = 2 * Math.PI * r
  const pct = max > 0 ? Math.max(0, Math.min(1, value / max)) : 0
  const color = { go: 'var(--go)', gold: 'var(--gold)', brand: 'var(--brand)' }[tone]
  return (
    <div className="relative inline-grid place-items-center" style={{ width: size, height: size }} role="img" aria-label={label}>
      <svg width={size} height={size} className="-rotate-90" aria-hidden>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="var(--surface-3)" strokeWidth={stroke} />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={color}
          strokeWidth={stroke}
          strokeLinecap="round"
          strokeDasharray={c}
          strokeDashoffset={c * (1 - pct)}
          style={{ transition: 'stroke-dashoffset 600ms ease-out' }}
        />
      </svg>
      <div className="absolute inset-0 grid place-items-center text-center">{children}</div>
    </div>
  )
}

export function Stat({ label, value, sub, tone }: { label: ReactNode; value: ReactNode; sub?: ReactNode; tone?: 'go' | 'bad' | 'warn' | 'gold' }) {
  const color = tone ? { go: 'text-go', bad: 'text-bad', warn: 'text-warn', gold: 'text-gold-ink' }[tone] : 'text-ink'
  return (
    <div className="min-w-0">
      <div className="text-sm font-medium text-ink-3">{label}</div>
      <div className={cx('mt-1 text-2xl font-semibold tabular', color)}>{value}</div>
      {sub && <div className="mt-0.5 text-xs text-ink-3">{sub}</div>}
    </div>
  )
}

export function Spinner({ label = 'Loading' }: { label?: string }) {
  return (
    <div role="status" className="flex items-center gap-2 text-sm text-ink-3">
      <svg className="h-4 w-4 animate-spin" viewBox="0 0 24 24" aria-hidden>
        <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" fill="none" opacity="0.25" />
        <path d="M22 12a10 10 0 0 0-10-10" stroke="currentColor" strokeWidth="3" fill="none" strokeLinecap="round" />
      </svg>
      <span>{label}…</span>
    </div>
  )
}

export function PageLoading() {
  return (
    <div className="grid min-h-[50dvh] place-items-center">
      <Spinner />
    </div>
  )
}

export function Notice({ tone = 'info', title, children, className }: { tone?: 'info' | 'warn' | 'bad' | 'gold' | 'neutral'; title?: ReactNode; children?: ReactNode; className?: string }) {
  const t = { info: 'bg-info-soft border-info/20', warn: 'bg-warn-soft border-warn/20', bad: 'bg-bad-soft border-bad/20', gold: 'bg-gold-soft border-gold/30', neutral: 'bg-surface-2 border-line' }[tone]
  return (
    <div className={cx('rounded-xl border px-4 py-3 text-sm text-ink-2', t, className)} role={tone === 'bad' ? 'alert' : undefined}>
      {title && <div className="font-semibold text-ink">{title}</div>}
      {children && <div className={title ? 'mt-1' : ''}>{children}</div>}
    </div>
  )
}

export function EmptyState({ icon, title, children, action }: { icon?: ReactNode; title: ReactNode; children?: ReactNode; action?: ReactNode }) {
  return (
    <div className="flex flex-col items-center px-6 py-10 text-center">
      {icon && <div className="mb-3 text-ink-3">{icon}</div>}
      <div className="font-semibold text-ink">{title}</div>
      {children && <div className="mt-1 max-w-sm text-sm text-ink-3">{children}</div>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  )
}

export function Field({ label, hint, error, children, htmlFor }: { label: string; hint?: string; error?: string | null; children: ReactNode; htmlFor: string }) {
  return (
    <div>
      <label htmlFor={htmlFor} className="block text-sm font-semibold text-ink">
        {label}
      </label>
      {hint && <p className="mt-0.5 text-xs text-ink-3">{hint}</p>}
      <div className="mt-1.5">{children}</div>
      {error && (
        <p className="mt-1 text-xs font-medium text-bad" role="alert">
          {error}
        </p>
      )}
    </div>
  )
}

export const inputClass =
  'block h-12 w-full rounded-xl border border-line-strong bg-surface px-3.5 text-[16px] text-ink placeholder:text-ink-3 focus:border-focus focus:outline-none focus:ring-2 focus:ring-info/30'

export function ChoiceCard({
  selected,
  onClick,
  title,
  description,
  icon,
  className,
}: {
  selected: boolean
  onClick: () => void
  title: ReactNode
  description?: ReactNode
  icon?: ReactNode
  className?: string
}) {
  return (
    <button
      type="button"
      aria-pressed={selected}
      onClick={onClick}
      className={cx(
        'flex w-full items-start gap-3 rounded-2xl border-2 p-4 text-left transition-colors',
        selected ? 'border-go bg-go-soft' : 'border-line bg-surface hover:border-line-strong',
        className,
      )}
    >
      {icon && <span className="mt-0.5 shrink-0 text-xl" aria-hidden>{icon}</span>}
      <span className="min-w-0">
        <span className="block font-semibold text-ink">{title}</span>
        {description && <span className="mt-0.5 block text-sm text-ink-3">{description}</span>}
      </span>
    </button>
  )
}

export function Segmented<T extends string | number>({
  value,
  onChange,
  options,
  label,
}: {
  value: T
  onChange: (v: T) => void
  options: { value: T; label: ReactNode }[]
  label: string
}) {
  return (
    <div role="radiogroup" aria-label={label} className="inline-flex rounded-xl bg-surface-2 p-1">
      {options.map((o) => (
        <button
          key={String(o.value)}
          type="button"
          role="radio"
          aria-checked={value === o.value}
          onClick={() => onChange(o.value)}
          className={cx(
            'rounded-lg px-3 py-1.5 text-sm font-semibold transition-colors',
            value === o.value ? 'bg-surface text-ink shadow-card' : 'text-ink-3 hover:text-ink',
          )}
        >
          {o.label}
        </button>
      ))}
    </div>
  )
}
