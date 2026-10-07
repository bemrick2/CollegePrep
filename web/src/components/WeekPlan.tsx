import { useState } from 'react'
import { useApp, useAsync } from '../lib/app'
import { addDays, formatShortDate } from '../lib/engine/dates'
import { PACE_LABEL, suggestionReason, type WeekRecap, type WeeklyPlan } from '../lib/engine/weeklyPlan'
import type { ContentStatus } from '../lib/engine/freshness'
import { SECTION_LABEL } from '../lib/engine/benchmark'
import { Button, Notice, Pill, cx } from './ui'
import { Link } from 'react-router-dom'

const CHECK_LABEL = { initial: 'Starting benchmark', mini: 'Mini benchmark', full: 'Full benchmark' } as const

/** Mon-Sun: practised, missed, today and the day a progress check is due. */
export function WeekStrip({ plan, className, label = "This week's practice days" }: { plan: Pick<WeeklyPlan, 'days'>; className?: string; label?: string }) {
  return (
    <ol className={cx('grid grid-cols-7 gap-1', className)} aria-label={label}>
      {plan.days.map((d) => {
        const done = d.status === 'done' || d.status === 'today_done'
        const today = d.status === 'today' || d.status === 'today_done'
        const state = done ? `practised, ${d.answered} answered` : d.status === 'missed' ? 'missed' : today ? 'today, not yet' : 'upcoming'
        return (
          <li key={d.date} className="flex flex-col items-center gap-1">
            <span className={cx('text-[11px] font-semibold', today ? 'text-ink' : 'text-ink-3')}>{d.label}</span>
            <span
              role="img"
              aria-label={`${d.label}: ${state}${d.check ? `; ${CHECK_LABEL[d.check].toLowerCase()} due` : ''}`}
              className={cx(
                'grid h-7 w-7 place-items-center rounded-full text-[11px] font-bold tabular',
                done ? 'bg-go text-white' : d.status === 'missed' ? 'bg-surface-3 text-ink-3' : today ? 'border-2 border-go text-go-strong dark:text-go' : 'border border-line text-ink-3',
              )}
            >
              {done ? d.answered : ''}
            </span>
            <span className={cx('h-1.5 w-1.5 rounded-full', d.check ? 'bg-gold' : 'bg-transparent')} aria-hidden />
          </li>
        )
      })}
    </ol>
  )
}

export function paceSentence(plan: WeeklyPlan): string {
  if (plan.pace === 'no_goal') return 'No weekly goal yet.'
  if (plan.pace === 'met') return `${plan.done} of ${plan.target} questions. Goal met.`
  const rest = plan.perDayToFinish ? ` About ${plan.perDayToFinish} a day finishes it.` : ''
  return `${plan.done} of ${plan.target} questions; ${plan.expectedByToday} by today is on pace.${rest}`
}

export function PacePill({ plan }: { plan: WeeklyPlan }) {
  const tone = plan.pace === 'behind' ? 'warn' : plan.pace === 'no_goal' ? 'neutral' : 'go'
  return <Pill tone={tone}>{PACE_LABEL[plan.pace]}</Pill>
}

export function checkSentence(plan: WeeklyPlan, who: 'you' | string): string {
  if (plan.needsBaseline) return `The starting benchmark comes first. It sets the baseline the plan depends on.`
  const what = CHECK_LABEL[plan.check.kind]
  if (plan.check.overdueDays > 0) return `${what} was due ${plan.check.overdueDays} ${plan.check.overdueDays === 1 ? 'day' : 'days'} ago.`
  if (plan.check.thisWeek) return `${what} due ${formatShortDate(plan.check.dueDate)}. It shows what changed since the last one.`
  return `Next progress check (${what.toLowerCase()}) ${formatShortDate(plan.check.dueDate)}. ${who === 'you' ? 'Keep practising until then.' : ''}`.trim()
}

export function FocusList({ plan, skillName }: { plan: WeeklyPlan; skillName: (key: string) => string | null | undefined }) {
  if (plan.focus.length === 0)
    return <p className="text-sm text-ink-3">No weak skills flagged yet. Skills are flagged after about five answers each.</p>
  return (
    <ul className="grid gap-1.5 text-sm">
      {plan.focus.map((f) => (
        <li key={f.skillKey} className="flex flex-wrap items-baseline gap-x-2">
          <span className="font-semibold text-ink">{skillName(f.skillKey) ?? f.skillKey}</span>
          <span className="text-ink-3">
            {SECTION_LABEL[f.section] ?? f.section},{' '}
            {f.why === 'knowledge' ? `${Math.round((f.accuracy ?? 0) * 100)}% right` : `${(f.pacingRatio ?? 0).toFixed(1)}× test pace`}
          </span>
        </li>
      ))}
    </ul>
  )
}

/**
 * The backend's suggestion for next week's question goal, with a one-tap way to set it. Only guardians with the
 * set-goals permission (or a student without a household) can set goals; others see the suggestion.
 */
export function NextWeekGoal({ studentId, weekStart, canSet, name }: { studentId: string; weekStart: string; canSet: boolean; name?: string }) {
  const { source } = useApp()
  const s = useAsync(() => source.suggestNextWeekGoal(studentId), [source, studentId])
  const [state, setState] = useState<'idle' | 'busy' | 'saved' | { error: string }>('idle')
  if (s.loading || s.error || !s.data) return null
  const sug = s.data
  const next = sug.weekStart || addDays(weekStart, 7)
  const set = async () => {
    if (sug.targetQuestions == null) return
    setState('busy')
    try {
      await source.setWeeklyGoal(studentId, next, sug.targetQuestions, null)
      setState('saved')
    } catch (e) {
      setState({ error: e instanceof Error ? e.message : 'Could not set the goal' })
    }
  }
  return (
    <div className="grid gap-2">
      <p className="text-sm text-ink-2">
        {sug.targetQuestions != null ? (
          <>
            Suggested for the week of {formatShortDate(next)}: <span className="font-semibold text-ink">{sug.targetQuestions} questions</span>.{' '}
          </>
        ) : null}
        {suggestionReason(sug)}
      </p>
      {sug.targetQuestions != null &&
        (state === 'saved' ? (
          <p className="text-sm font-semibold text-go-strong dark:text-go">Next week's goal is set to {sug.targetQuestions}.</p>
        ) : canSet ? (
          <div>
            <Button size="sm" variant="secondary" disabled={state === 'busy'} onClick={() => void set()}>
              Set next week to {sug.targetQuestions}
            </Button>
          </div>
        ) : (
          <p className="text-xs text-ink-3">{name ? `${name}'s parent or guardian sets the goal.` : 'Your parent or guardian sets the weekly goal.'}</p>
        ))}
      {typeof state === 'object' && <p className="text-sm text-bad">{state.error}</p>}
    </div>
  )
}

export function recapSentence(r: WeekRecap): string {
  const days = `Practised ${r.daysPractised} of 7 days.`
  if (r.met == null) return `${r.done} ${r.done === 1 ? 'question' : 'questions'}; no goal was set. ${days}`
  return r.met ? `Goal met: ${r.done} of ${r.target} questions. ${days}` : `${r.done} of ${r.target} questions, ${r.shortBy} short of the goal. ${days}`
}

/** The finished week, shown at the start of the next one. Recorded practice only. */
export function LastWeekRecap({ recap, className, compact = false }: { recap: WeekRecap; className?: string; compact?: boolean }) {
  return (
    <section className={className} aria-label="Last week">
      <h3 className="text-sm font-bold text-ink">Last week <span className="font-normal text-ink-3">(week of {formatShortDate(recap.weekStart)})</span></h3>
      <p className="mt-1 flex flex-wrap items-center gap-2 text-sm text-ink-2">
        {recap.met != null && <Pill tone={recap.met ? 'go' : 'warn'}>{recap.met ? 'Goal met' : 'Short of goal'}</Pill>}
        {recapSentence(recap)}
      </p>
      {!compact && <WeekStrip plan={recap} label="Last week's practice days" className="mt-3 max-w-sm" />}
    </section>
  )
}

/**
 * When the new week has no goal yet: whoever may set goals can carry last week's forward in one tap; everyone else
 * is told who sets it. Never set automatically.
 */
export function ThisWeekGoal({
  studentId,
  weekStart,
  lastGoal,
  canSet,
  name,
  goalsPath,
  onSet,
}: {
  studentId: string
  weekStart: string
  lastGoal: number | null
  canSet: boolean
  /** The student's name when a guardian is looking. */
  name?: string
  goalsPath: string
  onSet: () => void
}) {
  const { source } = useApp()
  const [state, setState] = useState<'idle' | 'busy' | { error: string }>('idle')
  const set = async (n: number) => {
    setState('busy')
    try {
      await source.setWeeklyGoal(studentId, weekStart, n, null)
      onSet()
    } catch (e) {
      setState({ error: e instanceof Error ? e.message : 'Could not set the goal' })
    }
  }
  return (
    <Notice tone="gold" title="No goal for this week yet">
      {canSet ? (
        lastGoal ? (
          <div className="flex flex-wrap items-center gap-3">
            <span>Last week's goal was {lastGoal} questions.</span>
            <Button size="sm" variant="secondary" disabled={state === 'busy'} onClick={() => void set(lastGoal)}>
              Use {lastGoal} again this week
            </Button>
          </div>
        ) : (
          <span>
            Pick a weekly goal on{' '}
            <Link to={goalsPath} className="font-semibold underline">
              Goals
            </Link>
            .
          </span>
        )
      ) : (
        <span>{name ? `${name}'s parent or guardian sets the weekly goal.` : 'Your parent or guardian sets the weekly goal.'}</span>
      )}
      {typeof state === 'object' && <p className="mt-1 text-bad">{state.error}</p>}
    </Notice>
  )
}

const EXAM = { act: 'ACT', sat: 'SAT' } as const
const list = (xs: string[]) => (xs.length <= 1 ? (xs[0] ?? '') : `${xs.slice(0, -1).join(', ')} and ${xs.at(-1)}`)
/** Below this many fresh practice questions, say how many are left. */
export const LOW_FRESH = 15

/**
 * Says plainly when fresh practice runs low or out. Repeats still count toward the weekly goal (review helps), but
 * they are not new evidence of improvement, and the goal is never lowered to hide the shortage.
 */
export function FreshContentNotice({ content, name }: { content: ContentStatus | null; name?: string }) {
  if (!content) return null
  const you = name ?? 'You'
  const sec = (keys: string[]) => list(keys.map((k) => SECTION_LABEL[k] ?? k))
  const checkShort = content.checkShortSections.length ? (
    <p className="mt-1">
      The next progress check can't be fully fresh in {sec(content.checkShortSections)}. Sections with questions seen before won't be compared.
    </p>
  ) : null
  if (content.practiceAllReview)
    return (
      <Notice tone="warn" title="No new practice questions left">
        <p>
          {you}
          {name ? ' has' : "'ve"} answered every {EXAM[content.exam]} practice question we have. Practice now repeats questions as review. Review counts toward the weekly
          goal and helps memory, but it isn't new evidence of improvement, so trends and progress checks leave it out. More questions are needed; until they arrive,
          practice is review.
        </p>
        {checkShort}
      </Notice>
    )
  if (content.reviewOnlySections.length)
    return (
      <Notice tone="info" title={`No new ${sec(content.reviewOnlySections)} questions left`}>
        <p>
          Practice in {content.reviewOnlySections.length === 1 ? 'that section' : 'those sections'} is review: it counts toward the goal, not as new evidence of improvement.
          {content.freshForPractice > 0 ? ` ${content.freshForPractice} new questions remain in other sections.` : ''}
        </p>
        {checkShort}
      </Notice>
    )
  if (content.freshForPractice < LOW_FRESH)
    return (
      <Notice tone="info" title={`${content.freshForPractice} new practice ${content.freshForPractice === 1 ? 'question' : 'questions'} left`}>
        <p>After that, practice repeats questions already seen, as review. A few new questions in each section are kept for the next progress check.</p>
        {checkShort}
      </Notice>
    )
  return checkShort ? <Notice tone="info">{checkShort}</Notice> : null
}
