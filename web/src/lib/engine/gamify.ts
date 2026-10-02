import type { AttemptRecord, BenchmarkSummary } from '../data/types'

// XP and achievements are derived from recorded attempts, so they can never
// disagree with the progress data. They are not persisted server-side yet
// (contract request CR-6); recomputing is cheap and deterministic.

export const XP_CORRECT = 10
export const XP_ANSWERED = 4
export const XP_ON_PACE_BONUS = 2
export const XP_PER_LEVEL = 250

export function xpFor(a: Pick<AttemptRecord, 'skipped' | 'is_correct' | 'elapsed_ms' | 'expected_time_seconds'>): number {
  if (a.skipped) return 0
  let xp = a.is_correct ? XP_CORRECT : XP_ANSWERED
  if (a.is_correct && a.expected_time_seconds && a.elapsed_ms <= a.expected_time_seconds * 1000) xp += XP_ON_PACE_BONUS
  return xp
}

export function totalXp(attempts: AttemptRecord[]): number {
  return attempts.reduce((s, a) => s + xpFor(a), 0)
}

export function levelOf(xp: number): { level: number; into: number; span: number } {
  return { level: Math.floor(xp / XP_PER_LEVEL) + 1, into: xp % XP_PER_LEVEL, span: XP_PER_LEVEL }
}

export interface Achievement {
  key: string
  title: string
  description: string
  earned: boolean
  progress: number
  goal: number
}

function longestCorrectRun(attempts: AttemptRecord[]): number {
  let best = 0
  let run = 0
  for (const a of [...attempts].sort((x, y) => x.submitted_at.localeCompare(y.submitted_at))) {
    if (a.skipped) continue
    run = a.is_correct ? run + 1 : 0
    best = Math.max(best, run)
  }
  return best
}

export function achievements(input: { attempts: AttemptRecord[]; benchmarks: BenchmarkSummary[]; longestStreak: number; goalsMet: number }): Achievement[] {
  const answered = input.attempts.filter((a) => !a.skipped)
  const onPace = answered.filter((a) => a.is_correct && a.expected_time_seconds && a.elapsed_ms <= a.expected_time_seconds * 1000).length
  const make = (key: string, title: string, description: string, progress: number, goal: number): Achievement => ({
    key,
    title,
    description,
    progress: Math.min(progress, goal),
    goal,
    earned: progress >= goal,
  })
  return [
    make('baseline', 'Baseline set', 'Finish your first benchmark', input.benchmarks.length, 1),
    make('streak_3', 'Three-day run', 'Practise three days in a row', input.longestStreak, 3),
    make('streak_7', 'Full week', 'Practise seven days in a row', input.longestStreak, 7),
    make('century', 'Hundred club', 'Answer 100 questions', answered.length, 100),
    make('hot_hand', 'Hot hand', 'Get 8 right in a row', longestCorrectRun(input.attempts), 8),
    make('pace_setter', 'Pace setter', 'Answer 25 correctly within test pace', onPace, 25),
    make('goal_met', 'Goal met', 'Hit a weekly question goal', input.goalsMet, 1),
  ]
}
