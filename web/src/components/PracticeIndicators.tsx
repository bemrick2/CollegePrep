import { useState } from 'react'
import type { AttemptRecord } from '../lib/data/types'
import { MIN_FOR_SCORE, SCORE_WINDOW_DAYS, threeScores, type ThreeScores } from '../lib/engine/scores'
import { Clock, Compass, Info, Target } from './icons'
import { Card, CardHeader, ProgressBar, cx } from './ui'

const SCORE_HELP: Record<keyof ThreeScores, { label: string; help: string; icon: React.ReactNode }> = {
  knowledge: { label: 'Knowledge', help: 'How often you answer correctly on the skills you have practised.', icon: <Target size={16} /> },
  pacing: { label: 'Pacing', help: 'How often you answer within test timing without rushing (faster than about a third of the expected time counts as rushing).', icon: <Clock size={16} /> },
  strategy: {
    label: 'Strategy',
    help: 'How well your test-taking habits work: answers you mark "Certain" are right, and right answers come without hints. Trap avoidance is added once wrong-answer choices are tracked.',
    icon: <Compass size={16} />,
  },
}

/** Three practice indicators (0-100) so a student can see whether to study, speed up, or change how they test.
 *  They are not ACT/SAT scores and are labelled that way everywhere they appear. */
export function PracticeIndicators({ history, title = 'Practice indicators' }: { history: AttemptRecord[]; title?: string }) {
  const s = threeScores(history)
  const [open, setOpen] = useState<keyof ThreeScores | null>(null)
  const keys = Object.keys(SCORE_HELP) as (keyof ThreeScores)[]
  return (
    <Card>
      <CardHeader title={title} subtitle={`Not ACT/SAT scores · 0–100 from your last ${SCORE_WINDOW_DAYS} days of practice`} />
      <ul className="grid grid-cols-3 gap-2 px-5 pt-3">
        {keys.map((k) => {
          const v = s[k].value
          const meta = SCORE_HELP[k]
          return (
            <li key={k}>
              <button
                type="button"
                onClick={() => setOpen((o) => (o === k ? null : k))}
                aria-expanded={open === k}
                aria-controls="indicator-help"
                className={cx('w-full rounded-2xl p-3 text-left transition', open === k ? 'bg-surface-3 ring-2 ring-line-strong' : 'bg-surface-2 hover:bg-surface-3')}
              >
                <div className="flex items-center gap-1 text-[13px] font-semibold text-ink-2">
                  <span className="hidden sm:inline">{meta.icon}</span> {meta.label}
                  <Info size={12} className="ml-auto text-ink-3" />
                </div>
                {v === null ? (
                  <div className="mt-1 text-sm text-ink-3">
                    <span className="display text-2xl font-semibold text-ink-3">—</span>
                    <span className="block text-[11px] leading-tight">{Math.max(0, MIN_FOR_SCORE - s[k].n)} more answers</span>
                  </div>
                ) : (
                  <>
                    <div className={cx('display mt-1 text-3xl font-semibold tabular', v >= 75 ? 'text-go' : v >= 50 ? 'text-ink' : 'text-warn')}>{v}</div>
                    <ProgressBar value={v} max={100} tone={v >= 75 ? 'go' : 'gold'} label={`${meta.label} practice indicator ${v} of 100`} className="mt-1.5 h-1.5" />
                  </>
                )}
              </button>
            </li>
          )
        })}
      </ul>
      <div id="indicator-help" aria-live="polite" className="px-5 pb-5 pt-3 text-sm text-ink-2">
        {open ? (
          <p>
            <span className="font-semibold text-ink">{SCORE_HELP[open].label}: </span>
            {SCORE_HELP[open].help} Based on {s[open].n} answer{s[open].n === 1 ? '' : 's'}; treat small changes as noise.
          </p>
        ) : (
          <p className="text-xs text-ink-3">Tap an indicator to see what it measures.</p>
        )}
      </div>
    </Card>
  )
}

