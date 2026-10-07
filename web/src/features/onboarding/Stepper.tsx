import type { ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'
import { Brand } from '../../components/shell'
import { ChevronLeft } from '../../components/icons'
import { ProgressBar, cx } from '../../components/ui'
import { SUPPORTED_LANGUAGES } from './options'

/** Outside the step count. Appears only when the app is written in more than one language (today: English only). */
function LanguageControl() {
  if (SUPPORTED_LANGUAGES.length < 2) return null
  return (
    <select aria-label="Language" className={cx('h-9 rounded-lg border border-line bg-surface px-2 text-sm')} defaultValue="en">
      {SUPPORTED_LANGUAGES.map((l) => (
        <option key={l.code} value={l.code}>
          {l.name}
        </option>
      ))}
    </select>
  )
}

export function StepFrame({
  step,
  total,
  title,
  subtitle,
  onBack,
  children,
  footer,
  hideProgress,
}: {
  step: number
  total: number
  title: ReactNode
  subtitle?: ReactNode
  onBack?: () => void
  children: ReactNode
  footer: ReactNode
  /** A result page after the steps: no step count. */
  hideProgress?: boolean
}) {
  const navigate = useNavigate()
  return (
    <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-xl flex-col px-4">
      <div className="flex h-16 items-center gap-3">
        <button
          onClick={onBack ?? (() => navigate('/'))}
          className="grid h-10 w-10 place-items-center rounded-full text-ink-2 hover:bg-surface-2"
          aria-label="Back"
        >
          <ChevronLeft />
        </button>
        {hideProgress ? <span className="flex-1" /> : <ProgressBar value={step} max={total} label={`Step ${step} of ${total}`} className="flex-1" />}
        {!hideProgress && total > 1 && (
          <span className="text-xs font-semibold text-ink-3 tabular" aria-hidden>
            {step} of {total}
          </span>
        )}
        <LanguageControl />
        <span className="hidden sm:block">
          <Brand />
        </span>
      </div>
      <div className="anim-rise flex-1 pb-6 pt-4" key={step}>
        <h1 className="display text-[30px] font-semibold leading-tight text-ink md:text-[34px]">{title}</h1>
        {subtitle && <p className="mt-2 text-ink-2">{subtitle}</p>}
        <div className="mt-6">{children}</div>
      </div>
      <div className="sticky bottom-0 -mx-4 border-t border-line bg-bg/95 px-4 py-4 pb-[max(1rem,env(safe-area-inset-bottom))] backdrop-blur">{footer}</div>
    </div>
  )
}
