import { useApp, useAsync } from '../../lib/app'
import type { AttemptRecord, BenchmarkSummary, SkillEstimate, Streak, StudentPlan, TestScore, WeeklyProgress } from '../../lib/data/types'
import { addDays, localDate, weekStartOf } from '../../lib/engine/dates'

export interface StudentOverview {
  tz: string
  today: string
  weekStart: string
  plan: StudentPlan | null
  week: WeeklyProgress
  streak: Streak
  estimates: SkillEstimate[]
  scores: TestScore[]
  benchmarks: BenchmarkSummary[]
  history: AttemptRecord[]
  goalsMet: number
  /** The previous week's progress (Monday weekStart - 7), for the recap. */
  lastWeek: WeeklyProgress | null
}

/** Everything the student home, progress page and parent dashboard read about one student. */
export function useStudentOverview(studentId: string | null | undefined) {
  const { source, ctx } = useApp()
  const student = ctx?.students.find((s) => s.id === studentId) ?? ctx?.myStudent ?? null
  const household = ctx?.households.find((h) => h.id === student?.household_id)
  const tz = student?.time_zone ?? household?.time_zone ?? 'UTC'
  return useAsync<StudentOverview | null>(async () => {
    if (!studentId) return null
    const today = localDate(new Date(), tz)
    const weekStart = weekStartOf(today)
    const since = new Date(Date.now() - 70 * 86_400_000).toISOString()
    const pastWeeks = [1, 2, 3, 4].map((w) => addDays(weekStart, -7 * w))
    const [plan, week, streak, estimates, scores, benchmarks, history, past] = await Promise.all([
      source.getPlan(studentId),
      source.weeklyProgress(studentId, weekStart),
      source.streak(studentId),
      source.skillEstimates(studentId),
      source.testScores(studentId),
      source.listBenchmarks(studentId),
      source.attemptHistory(studentId, since),
      Promise.all(pastWeeks.map((w) => source.weeklyProgress(studentId, w).catch(() => null))),
    ])
    const goalsMet = [week, ...past].filter((w) => w?.goal?.target_questions && w.questions_submitted >= w.goal.target_questions).length
    return { tz, today, weekStart, plan, week, streak, estimates, scores, benchmarks, history, goalsMet, lastWeek: past[0] ?? null }
  }, [source, studentId, tz])
}

/**
 * Practice score estimates are never shown. No scoring model has been validated against real test results
 * (CR-3), so a practice "composite" would be an uncalibrated ACT/SAT prediction. Any practice_estimate row the
 * backend returns is ignored until a validated calibration exists; official and self-reported scores are separate.
 */
export const PRACTICE_ESTIMATES_VALIDATED = false

export function latestEstimate(scores: TestScore[], exam: string) {
  if (!PRACTICE_ESTIMATES_VALIDATED) return []
  return [...scores]
    .filter((s) => s.score_source === 'practice_estimate' && s.exam_family === exam && s.composite !== null)
    .sort((a, b) => b.test_date.localeCompare(a.test_date))
}

/** Accuracy over the last 7 days vs the 7 before, from answered attempts. */
export function recentTrend(history: AttemptRecord[], today: string, tz: string) {
  const bucket = (from: number, to: number) => {
    const rs = history.filter((a) => {
      if (a.skipped) return false
      const d = localDate(a.submitted_at, tz)
      return d > addDays(today, -to) && d <= addDays(today, -from)
    })
    return { n: rs.length, acc: rs.length ? rs.filter((a) => a.is_correct).length / rs.length : null }
  }
  return { recent: bucket(0, 7), prior: bucket(7, 14) }
}
