import type { AttemptRecord } from '../data/types'
import { RUSHED_BELOW } from './benchmark'

/** Practice window and minimum evidence for the three home-screen scores. */
export const SCORE_WINDOW_DAYS = 28
export const MIN_FOR_SCORE = 10

export interface Score {
  /** 0-100, or null until there is enough evidence. */
  value: number | null
  /** Attempts the score is based on. */
  n: number
}

export interface ThreeScores {
  knowledge: Score
  pacing: Score
  strategy: Score
}

const pct = (num: number, den: number) => Math.round((100 * num) / den)

/**
 * Knowledge: share of answered questions right.
 * Pacing: share of timed answers within test pace that were not rushed (at least RUSHED_BELOW of expected time).
 * Strategy (test-taking habits): mean of (a) how often "Certain" answers were right and (b) how often correct
 * answers needed no hint. Each part needs MIN_FOR_SCORE attempts; the score uses the parts that qualify.
 */
export function threeScores(history: AttemptRecord[], now: Date = new Date()): ThreeScores {
  const until = now.getTime()
  const since = until - SCORE_WINDOW_DAYS * 86_400_000
  const answered = history.filter((a) => {
    const t = new Date(a.submitted_at).getTime()
    return !a.skipped && a.is_correct !== null && t >= since && t <= until
  })

  const knowledge: Score = { n: answered.length, value: answered.length >= MIN_FOR_SCORE ? pct(answered.filter((a) => a.is_correct).length, answered.length) : null }

  const timed = answered.filter((a) => a.expected_time_seconds && a.expected_time_seconds > 0)
  const onPace = timed.filter((a) => {
    const r = a.elapsed_ms / (a.expected_time_seconds! * 1000)
    return r <= 1 && r >= RUSHED_BELOW
  }).length
  const pacing: Score = { n: timed.length, value: timed.length >= MIN_FOR_SCORE ? pct(onPace, timed.length) : null }

  const certain = answered.filter((a) => a.confidence === 3)
  const correct = answered.filter((a) => a.is_correct)
  const parts: number[] = []
  if (certain.length >= MIN_FOR_SCORE) parts.push(certain.filter((a) => a.is_correct).length / certain.length)
  if (correct.length >= MIN_FOR_SCORE) parts.push(correct.filter((a) => a.hint_count === 0).length / correct.length)
  const strategy: Score = {
    n: Math.max(certain.length, correct.length),
    value: parts.length ? Math.round((100 * parts.reduce((s, x) => s + x, 0)) / parts.length) : null,
  }
  return { knowledge, pacing, strategy }
}

/** The same indicators for the previous window, for "change vs the 4 weeks before". */
export function priorScores(history: AttemptRecord[], now: Date = new Date()): ThreeScores {
  return threeScores(history, new Date(now.getTime() - SCORE_WINDOW_DAYS * 86_400_000))
}
