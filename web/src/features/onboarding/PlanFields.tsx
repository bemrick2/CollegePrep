import type { ExamFamily } from '../../lib/data/types'
import { ChoiceCard, Segmented, cx } from '../../components/ui'
import { EXAM_NAME, GOAL_OPTIONS, SCORE_RANGE } from './options'

export interface PlanDraft {
  exam: ExamFamily
  target: number | null
  goals: string[]
  weeklyQuestions: number
}

export const defaultPlanDraft = (): PlanDraft => ({ exam: 'act', target: SCORE_RANGE.act.default, goals: ['raise_score'], weeklyQuestions: 40 })

export function ExamAndTarget({ value, onChange, who }: { value: PlanDraft; onChange: (v: PlanDraft) => void; who: 'student' | 'parent' }) {
  const range = SCORE_RANGE[value.exam]
  return (
    <div className="grid gap-6">
      <div>
        <div className="mb-2 text-sm font-semibold text-ink">Which test?</div>
        <div className="grid grid-cols-2 gap-3">
          {(['act', 'sat'] as ExamFamily[]).map((e) => (
            <ChoiceCard
              key={e}
              selected={value.exam === e}
              onClick={() => onChange({ ...value, exam: e, target: SCORE_RANGE[e].default })}
              title={EXAM_NAME[e]}
              description={e === 'act' ? 'Scored 1–36' : 'Scored 400–1600'}
            />
          ))}
        </div>
        <p className="mt-2 text-xs text-ink-3">Not sure? Start with either — you can switch later, and the benchmark helps you decide.</p>
      </div>
      <div>
        <div className="flex items-baseline justify-between">
          <label htmlFor="target" className="text-sm font-semibold text-ink">
            {who === 'student' ? 'Your target score' : 'Target score'}
          </label>
          <span className="display text-3xl font-semibold tabular text-ink">{value.target ?? '—'}</span>
        </div>
        <input
          id="target"
          type="range"
          min={range.min}
          max={range.max}
          step={range.step}
          value={value.target ?? range.default}
          onChange={(e) => onChange({ ...value, target: Number(e.target.value) })}
          className="mt-3 w-full accent-[var(--go)]"
        />
        <div className="mt-1 flex justify-between text-xs text-ink-3 tabular">
          <span>{range.min}</span>
          <button type="button" className="font-semibold underline-offset-2 hover:underline" onClick={() => onChange({ ...value, target: null })}>
            Not sure yet
          </button>
          <span>{range.max}</span>
        </div>
      </div>
    </div>
  )
}

export function GoalsAndPace({ value, onChange }: { value: PlanDraft; onChange: (v: PlanDraft) => void }) {
  const toggle = (k: string) => onChange({ ...value, goals: value.goals.includes(k) ? value.goals.filter((g) => g !== k) : [...value.goals, k] })
  return (
    <div className="grid gap-6">
      <div>
        <div className="mb-2 text-sm font-semibold text-ink">What matters most? Pick any.</div>
        <div className="grid gap-2">
          {GOAL_OPTIONS.map((g) => (
            <button
              type="button"
              key={g.key}
              aria-pressed={value.goals.includes(g.key)}
              onClick={() => toggle(g.key)}
              className={cx(
                'flex items-center justify-between gap-3 rounded-xl border-2 px-4 py-3 text-left transition-colors',
                value.goals.includes(g.key) ? 'border-go bg-go-soft' : 'border-line bg-surface hover:border-line-strong',
              )}
            >
              <span>
                <span className="block font-semibold text-ink">{g.label}</span>
                <span className="block text-sm text-ink-3">{g.description}</span>
              </span>
              <span
                aria-hidden
                className={cx('grid h-6 w-6 shrink-0 place-items-center rounded-md border-2 text-xs font-bold', value.goals.includes(g.key) ? 'border-go bg-go text-white' : 'border-line-strong')}
              >
                {value.goals.includes(g.key) ? '✓' : ''}
              </span>
            </button>
          ))}
        </div>
      </div>
      <div>
        <div className="mb-2 text-sm font-semibold text-ink">Weekly question goal</div>
        <Segmented
          label="Weekly question goal"
          value={value.weeklyQuestions}
          onChange={(n) => onChange({ ...value, weeklyQuestions: n })}
          options={[
            { value: 20, label: '20 · light' },
            { value: 40, label: '40 · steady' },
            { value: 60, label: '60 · intense' },
          ]}
        />
        <p className="mt-2 text-xs text-ink-3">40 a week is about 9 minutes a day, five days a week.</p>
      </div>
    </div>
  )
}
