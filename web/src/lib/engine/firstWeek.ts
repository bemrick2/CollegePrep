import { addDays, isoWeekday, weekStartOf } from './dates'

/**
 * The week a family sees before accepting a plan in setup. It applies the existing weekly-goal rules unchanged: the
 * goal is a number of questions for the local Monday–Sunday week, set for the current week, and progress-check
 * answers count toward it like any other practice. Study days and session length only decide how the remaining
 * questions are spread; they never change the goal. Nothing here predicts a score.
 */

export const WEEKDAY_LABEL = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] as const

export interface FirstWeekInput {
  today: string
  /** ISO weekdays, 1 = Monday … 7 = Sunday. */
  studyDays: number[]
  minutesPerSession: number
  weeklyQuestions: number
  /** No starting check yet: it comes first, today. */
  needsBaseline: boolean
  /** Questions and minutes in the starting check, from the real plan for this exam (null while loading). */
  baseline: { questions: number; minutes: number } | null
  /** Mean expected seconds per published practice question for this exam; null when unknown. */
  secondsPerQuestion: number | null
  /** New practice questions this student hasn't seen; null when unknown. */
  freshAvailable: number | null
}

export interface FirstWeekDay {
  date: string
  label: string
  isToday: boolean
  study: boolean
  check: { questions: number; minutes: number } | null
  /** Practice questions planned that day (0 on rest days). */
  questions: number
  /** Planned questions need noticeably more time than one session. */
  overSession: boolean
}

export interface FirstWeek {
  weekStart: string
  weekEnd: string
  days: FirstWeekDay[]
  /** The single thing to do next. */
  next: { kind: 'check'; date: string; minutes: number | null } | { kind: 'practice'; date: string; questions: number; minutes: number } | { kind: 'none_this_week'; nextStudyDay: string | null }
  /** Questions per study day in a full week. */
  fullWeekPerDay: number
  minutesCommitted: number
  /** Typical minutes the weekly goal takes, from published question times; null when unknown. */
  minutesNeeded: number | null
  shortOfTime: boolean
  /** Questions this week's remaining study days are planned to cover (check included). */
  plannedThisWeek: number
  /** This week can't reach the goal with the days left (the goal still counts the whole week). */
  partialWeek: boolean
  freshShort: boolean
}

export function proposeFirstWeek(i: FirstWeekInput): FirstWeek {
  const weekStart = weekStartOf(i.today)
  const days = new Set(i.studyDays.filter((d) => d >= 1 && d <= 7))
  const check = i.needsBaseline ? (i.baseline ?? { questions: 0, minutes: 0 }) : null
  const remaining = Array.from({ length: 7 }, (_, n) => addDays(weekStart, n)).filter((d) => d >= i.today)
  const practiceDays = remaining.filter((d) => days.has(isoWeekday(d)) && !(check && d === i.today))
  const need = Math.max(0, i.weeklyQuestions - (check?.questions ?? 0))
  const perDay = practiceDays.length ? Math.ceil(need / practiceDays.length) : 0
  const sessionQuestions = i.secondsPerQuestion ? (i.minutesPerSession * 60) / i.secondsPerQuestion : null

  const out: FirstWeekDay[] = remaining.map((date) => {
    const study = days.has(isoWeekday(date))
    const questions = practiceDays.includes(date) ? perDay : 0
    return {
      date,
      label: WEEKDAY_LABEL[isoWeekday(date) - 1]!,
      isToday: date === i.today,
      study,
      check: check && date === i.today ? check : null,
      questions,
      overSession: sessionQuestions !== null && questions > sessionQuestions * 1.25,
    }
  })

  const plannedThisWeek = (check?.questions ?? 0) + perDay * practiceDays.length
  const minutesCommitted = days.size * i.minutesPerSession
  const minutesNeeded = i.secondsPerQuestion ? Math.round((i.weeklyQuestions * i.secondsPerQuestion) / 60) : null
  const firstPractice = out.find((d) => d.questions > 0)
  const nextStudyDay = [...days].length ? addDays(weekStart, 7 + Math.min(...days) - 1) : null
  const next: FirstWeek['next'] = check
    ? { kind: 'check', date: i.today, minutes: i.baseline?.minutes ?? null }
    : firstPractice
      ? { kind: 'practice', date: firstPractice.date, questions: firstPractice.questions, minutes: i.minutesPerSession }
      : { kind: 'none_this_week', nextStudyDay }

  return {
    weekStart,
    weekEnd: addDays(weekStart, 6),
    days: out,
    next,
    fullWeekPerDay: days.size ? Math.ceil(i.weeklyQuestions / days.size) : 0,
    minutesCommitted,
    minutesNeeded,
    shortOfTime: minutesNeeded !== null && minutesNeeded > minutesCommitted,
    plannedThisWeek: Math.min(plannedThisWeek, Math.max(plannedThisWeek, 0)),
    partialWeek: practiceDays.length === 0 ? (check?.questions ?? 0) < i.weeklyQuestions : out.some((d) => d.overSession),
    freshShort: i.freshAvailable !== null && i.freshAvailable < i.weeklyQuestions,
  }
}
