import { useState } from 'react'
import type { Strategy, SubmitResult, TrapType } from '../../lib/data/types'
import { Button, Pill, cx } from '../../components/ui'
import { Bolt, Book, Check, Flag, Lightbulb, X } from '../../components/icons'
import { formatDuration } from '../../lib/engine/dates'

type Tab = 'why' | 'strategy' | 'traps'

export function Feedback({
  result,
  chosen,
  expectedSeconds,
  remember,
  strategies,
  traps,
  onContinue,
  continueLabel = 'Continue',
}: {
  result: SubmitResult
  chosen: string | null
  expectedSeconds: number | null
  remember: string | null
  strategies: Strategy[]
  traps: TrapType[]
  onContinue: () => void
  continueLabel?: string
}) {
  const [tab, setTab] = useState<Tab>('why')
  const ok = result.is_correct === true
  const fastest = result.strategies.find((s) => s.is_fastest) ?? result.strategies[0]
  const strategyName = (k: string) => strategies.find((s) => s.strategy_key === k)?.name ?? k.replace(/_/g, ' ')
  const trapName = (k: string | null) => (k ? (traps.find((t) => t.trap_key === k)?.name ?? k.replace(/_/g, ' ')) : null)
  const myDistractor = result.distractors.find((d) => d.choice === chosen)
  const onPace = expectedSeconds ? result.elapsed_ms <= expectedSeconds * 1000 : null

  const tabs: { key: Tab; label: string; icon: React.ReactNode; show: boolean }[] = [
    { key: 'why', label: 'Teach me', icon: <Book size={16} />, show: !!result.teaching_explanation },
    { key: 'strategy', label: 'Test strategy', icon: <Bolt size={16} />, show: !!(result.strategy_explanation || fastest) },
    { key: 'traps', label: 'Other answers', icon: <Flag size={16} />, show: result.distractors.length > 0 },
  ]
  const visible = tabs.filter((t) => t.show)
  const active = visible.some((t) => t.key === tab) ? tab : visible[0]?.key

  return (
    <div className={cx('anim-rise rounded-3xl border-2 p-5', ok ? 'border-go/40 bg-go-soft' : result.skipped ? 'border-line bg-surface-2' : 'border-bad/30 bg-bad-soft')} aria-live="polite">
      <div className="flex items-center gap-3">
        <span className={cx('grid h-10 w-10 place-items-center rounded-full text-white', ok ? 'bg-go' : result.skipped ? 'bg-ink-3' : 'bg-bad')}>
          {ok ? <Check /> : <X />}
        </span>
        <div className="min-w-0 flex-1">
          <div className="text-lg font-bold text-ink">{ok ? pickPraise(result.elapsed_ms) : result.skipped ? 'Skipped' : 'Not quite'}</div>
          <div className="text-sm text-ink-2">
            {formatDuration(result.elapsed_ms)}
            {onPace !== null && ok && <> · {onPace ? 'within test pace' : `test pace is ${formatDuration(expectedSeconds! * 1000)}`}</>}
          </div>
        </div>
      </div>

      {!ok && myDistractor && (
        <div className="mt-4 rounded-2xl bg-surface p-4">
          <div className="flex flex-wrap items-center gap-2">
            <span className="text-sm font-semibold text-ink">Why {chosen} is tempting</span>
            {myDistractor.trap && <Pill tone="warn">{trapName(myDistractor.trap)}</Pill>}
          </div>
          <p className="mt-1 text-sm text-ink-2">{myDistractor.rationale}</p>
        </div>
      )}

      {visible.length > 0 && (
        <div className="mt-4">
          <div role="tablist" aria-label="Explanation" className="grid auto-cols-fr grid-flow-col gap-1 rounded-full bg-surface p-1">
            {visible.map((t) => (
              <button
                key={t.key}
                role="tab"
                aria-selected={active === t.key}
                onClick={() => setTab(t.key)}
                className={cx('flex min-w-0 items-center justify-center gap-1.5 rounded-full px-2 py-1.5 text-[13px] font-semibold sm:text-sm', active === t.key ? 'bg-ink text-bg' : 'text-ink-2 hover:text-ink')}
              >
                <span className="hidden shrink-0 min-[400px]:inline">{t.icon}</span>
                <span className="truncate">{t.label}</span>
              </button>
            ))}
          </div>
          <div role="tabpanel" className="mt-3 rounded-2xl bg-surface p-4 text-[15px] leading-relaxed text-ink-2">
            {active === 'why' && <p>{result.teaching_explanation}</p>}
            {active === 'strategy' && (
              <div className="grid gap-3">
                {fastest && (
                  <div>
                    <Pill tone="go">Fastest: {strategyName(fastest.strategy_key)}</Pill>
                    {fastest.explanation && <p className="mt-2">{fastest.explanation}</p>}
                  </div>
                )}
                {result.strategy_explanation && result.strategy_explanation !== fastest?.explanation && <p>{result.strategy_explanation}</p>}
              </div>
            )}
            {active === 'traps' && (
              <ul className="grid gap-3">
                {result.distractors.map((d) => (
                  <li key={d.choice} className="flex gap-3">
                    <span className={cx('grid h-7 w-7 shrink-0 place-items-center rounded-lg border-2 text-xs font-bold', d.choice === chosen ? 'border-bad text-bad' : 'border-line-strong text-ink-3')}>{d.choice}</span>
                    <div>
                      {d.trap && <div className="text-xs font-semibold uppercase tracking-wide text-warn">{trapName(d.trap)}</div>}
                      <p>{d.rationale}</p>
                    </div>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      )}

      {remember && (
        <div className="mt-3 flex gap-3 rounded-2xl bg-gold-soft p-4">
          <Lightbulb className="shrink-0 text-gold-ink" />
          <div>
            <div className="text-xs font-bold uppercase tracking-wide text-gold-ink">Remember this</div>
            <p className="mt-0.5 font-medium text-ink">{remember}</p>
          </div>
        </div>
      )}

      <Button size="lg" block className="mt-5" onClick={onContinue} autoFocus>
        {continueLabel}
      </Button>
    </div>
  )
}

function pickPraise(ms: number) {
  const options = ['Nice work', 'Correct', 'Got it', 'Exactly right']
  return options[Math.floor(ms / 997) % options.length]!
}
