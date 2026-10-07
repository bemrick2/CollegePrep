import type { AttemptRecord, BenchmarkSummary, SkillEstimate, StudentPlan, WeeklyProgress } from '../data/types'
import { addDays, localDate } from './dates'
import { benchmarkAttemptIds, benchmarkSchedule, type BenchmarkKind } from './benchmark'

/**
 * The student's week, built only from recorded data: the weekly goal (set by the student or a guardian), the daily
 * session length, the skills the backend flags as weak, and the benchmark schedule. Nothing here predicts a score.
 *
 * Practice is daily, so the goal is spread evenly over the seven days of the student's local week; "on track" uses
 * the same rule the parent dashboard has always used (goal × days so far ÷ 7, with 20% slack).
 */

export type DayStatus = 'done' | 'today' | 'today_done' | 'missed' | 'upcoming'

export interface PlanDay {
  date: string
  /** Mon … Sun */
  label: string
  status: DayStatus
  /** Practice answers submitted that day (benchmark answers excluded). */
  answered: number
  /** A progress check (benchmark) falls due this day. */
  check: BenchmarkKind | null
}

export interface FocusSkill {
  skillKey: string
  section: string
  why: 'knowledge' | 'pacing'
  accuracy: number | null
  pacingRatio: number | null
}

export interface WeeklyPlan {
  weekStart: string
  days: PlanDay[]
  minutesPerSession: number
  target: number | null
  done: number
  /** Questions expected by the end of today to stay on pace; null without a goal. */
  expectedByToday: number | null
  pace: 'met' | 'ahead' | 'on_track' | 'behind' | 'no_goal'
  /** Questions per remaining day (today included unless already practised) to finish the goal. */
  perDayToFinish: number | null
  daysPractised: number
  focus: FocusSkill[]
  check: { kind: BenchmarkKind; dueDate: string; overdueDays: number; thisWeek: boolean }
  /** No baseline yet: the plan is "take the benchmark", nothing else is personalised. */
  needsBaseline: boolean
}

const LABELS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

export interface WeeklyPlanInput {
  today: string
  weekStart: string
  tz: string
  plan: StudentPlan | null
  week: WeeklyProgress
  history: AttemptRecord[]
  benchmarks: BenchmarkSummary[]
  estimates: SkillEstimate[]
  /** Clock for the benchmark schedule (tests). */
  now?: Date
}

export function weeklyPlan(i: WeeklyPlanInput): WeeklyPlan {
  const benchIds = benchmarkAttemptIds(i.benchmarks)
  const answeredOn = new Map<string, number>()
  for (const a of i.history) {
    if (a.skipped || benchIds.has(a.id)) continue
    const d = localDate(a.submitted_at, i.tz)
    answeredOn.set(d, (answeredOn.get(d) ?? 0) + 1)
  }
  const schedule = benchmarkSchedule(i.benchmarks, i.now ?? new Date())
  const weekEnd = addDays(i.weekStart, 6)
  const checkDate = schedule.overdueDays > 0 || schedule.dueDate < i.today ? i.today : schedule.dueDate
  const days: PlanDay[] = LABELS.map((label, n) => {
    const date = addDays(i.weekStart, n)
    const answered = answeredOn.get(date) ?? 0
    const status: DayStatus =
      date < i.today ? (answered > 0 ? 'done' : 'missed') : date === i.today ? (answered > 0 ? 'today_done' : 'today') : 'upcoming'
    return { date, label, status, answered, check: i.benchmarks.length > 0 && date === checkDate ? schedule.kind : null }
  })

  const target = i.week.goal?.target_questions ?? null
  const done = i.week.questions_submitted
  const dayIndex = Math.max(0, Math.min(6, days.findIndex((d) => d.date === i.today)))
  const expectedByToday = target ? Math.round((target * (dayIndex + 1)) / 7) : null
  const practisedToday = (answeredOn.get(i.today) ?? 0) > 0
  const daysLeft = 7 - dayIndex - (practisedToday ? 1 : 0)
  const pace: WeeklyPlan['pace'] = !target
    ? 'no_goal'
    : done >= target
      ? 'met'
      : done >= (expectedByToday ?? 0) * 1.15
        ? 'ahead'
        : done >= (expectedByToday ?? 0) * 0.8
          ? 'on_track'
          : 'behind'
  const perDayToFinish = target && done < target ? Math.ceil((target - done) / Math.max(1, daysLeft)) : target ? 0 : null

  // Weakest first: knowledge gaps by accuracy, then pacing by how far over test pace. At most three.
  const knowledge = i.estimates.filter((e) => e.knowledge_weak).sort((a, b) => (a.accuracy ?? 1) - (b.accuracy ?? 1))
  const pacing = i.estimates.filter((e) => e.pacing_weak && !e.knowledge_weak).sort((a, b) => (b.pacing_ratio ?? 0) - (a.pacing_ratio ?? 0))
  const focus: FocusSkill[] = [
    ...knowledge.map((e) => ({ skillKey: e.skill_key, section: e.section, why: 'knowledge' as const, accuracy: e.accuracy, pacingRatio: e.pacing_ratio })),
    ...pacing.map((e) => ({ skillKey: e.skill_key, section: e.section, why: 'pacing' as const, accuracy: e.accuracy, pacingRatio: e.pacing_ratio })),
  ].slice(0, 3)

  return {
    weekStart: i.weekStart,
    days,
    minutesPerSession: i.plan?.daily_minutes ?? 10,
    target,
    done,
    expectedByToday,
    pace,
    perDayToFinish,
    daysPractised: days.filter((d) => d.answered > 0).length,
    focus,
    check: { kind: schedule.kind, dueDate: schedule.dueDate, overdueDays: schedule.overdueDays, thisWeek: schedule.dueDate <= weekEnd },
    needsBaseline: i.benchmarks.length === 0,
  }
}

export const PACE_LABEL: Record<WeeklyPlan['pace'], string> = {
  met: 'Goal met',
  ahead: 'Ahead',
  on_track: 'On track',
  behind: 'Behind',
  no_goal: 'No goal set',
}

/** The backend's next-week suggestion (suggest_next_week_goal), as the app shows it. */
export interface NextWeekSuggestion {
  weekStart: string
  targetQuestions: number | null
  basis: 'history' | 'insufficient_history'
  weeksConsidered: number
  completion: number | null
}

export function suggestionReason(s: NextWeekSuggestion): string {
  if (s.basis === 'insufficient_history' || s.targetQuestions == null)
    return 'Not enough finished weeks yet to suggest a change; two weeks with a goal are needed.'
  const pct = s.completion != null ? Math.round(s.completion * 100) : null
  return pct == null
    ? `Based on the last ${s.weeksConsidered} weeks.`
    : pct >= 100
      ? `Recent weeks averaged ${pct}% of the goal, so the suggestion steps up about 10%.`
      : pct >= 70
        ? `Recent weeks averaged ${pct}% of the goal, so the suggestion holds steady.`
        : `Recent weeks averaged ${pct}% of the goal, so the suggestion eases off about 15%.`
}

/**
 * The same rule as the backend's suggest_next_week_goal (v1), for the demo: look at up to four previous weeks that
 * had a question goal; with at least two, scale the latest goal by completion (>=100%: +10%, >=70%: same,
 * otherwise -15%), clamped to 5-200.
 */
export function suggestNextWeek(weekStart: string, past: { target: number | null; done: number }[]): NextWeekSuggestion {
  const withGoal = past.filter((w): w is { target: number; done: number } => w.target != null && w.target > 0)
  if (withGoal.length < 2) return { weekStart, targetQuestions: null, basis: 'insufficient_history', weeksConsidered: past.length, completion: null }
  const completion = withGoal.reduce((n, w) => n + Math.min(w.done / w.target, 1.5), 0) / withGoal.length
  const base = withGoal[0]!.target
  const factor = completion >= 1 ? 1.1 : completion >= 0.7 ? 1 : 0.85
  return {
    weekStart,
    targetQuestions: Math.min(200, Math.max(5, Math.round(base * factor))),
    basis: 'history',
    weeksConsidered: past.length,
    completion: Math.round(completion * 1000) / 1000,
  }
}

/** A finished week, for the "Last week" recap on Monday. Same counting rules as the live plan. */
export interface WeekRecap {
  weekStart: string
  target: number | null
  done: number
  /** null without a goal. */
  met: boolean | null
  shortBy: number | null
  daysPractised: number
  days: PlanDay[]
}

export function weekRecap(i: Omit<WeeklyPlanInput, 'today' | 'now'>): WeekRecap {
  const sunday = addDays(i.weekStart, 6)
  const p = weeklyPlan({ ...i, today: sunday, now: new Date(`${addDays(i.weekStart, 7)}T00:00:00Z`) })
  // On a finished week, "today" (Sunday) is just another day.
  const days = p.days.map((d) => ({ ...d, status: d.status === 'today_done' ? ('done' as const) : d.status === 'today' ? ('missed' as const) : d.status, check: null }))
  const met = p.target == null ? null : p.done >= p.target
  return { weekStart: i.weekStart, target: p.target, done: p.done, met, shortBy: met === false ? p.target! - p.done : null, daysPractised: days.filter((d) => d.status === 'done').length, days }
}

/** The recap leads at the start of a week (Monday to Wednesday), then steps aside for the current week. */
export const showRecap = (today: string, weekStart: string) => today >= weekStart && today <= addDays(weekStart, 2)
