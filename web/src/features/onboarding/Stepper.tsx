import type { ReactNode } from 'react'
import { useNavigate } from 'react-router-dom'
import { Brand } from '../../components/shell'
import { ChevronLeft } from '../../components/icons'
import { ProgressBar } from '../../components/ui'

export function StepFrame({
  step,
  total,
  title,
  subtitle,
  onBack,
  children,
  footer,
}: {
  step: number
  total: number
  title: ReactNode
  subtitle?: ReactNode
  onBack?: () => void
  children: ReactNode
  footer: ReactNode
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
        <ProgressBar value={step} max={total} label={`Step ${step} of ${total}`} className="flex-1" />
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
