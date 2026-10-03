import type { BenchmarkMetrics, BenchmarkSummary, Confidence, ExamFamily, PublicQuestion, SectionMetrics } from '../data/types'
import { median } from './dates'
import { PACING_WEAK_ABOVE } from './analytics'

// Benchmark design: section by section, as on the real tests, with a simple
// difficulty staircase inside each section (start at 3, +1 after a correct
// answer, -1 after a wrong one). Skipped questions come back at the end of
// their section. This is a v1 heuristic, not a calibrated adaptive test.

export type BenchmarkKind = BenchmarkSummary['kind']

export const SECTION_ORDER: Record<ExamFamily, string[]> = {
  act: ['english', 'math', 'reading', 'science'],
  sat: ['reading_writing', 'math'],
}

export const SECTION_LABEL: Record<string, string> = {
  english: 'English',
  math: 'Math',
  reading: 'Reading',
  science: 'Science',
  reading_writing: 'Reading & Writing',
}

const PER_SECTION: Record<ExamFamily, Record<BenchmarkKind, Record<string, number>>> = {
  act: {
    initial: { english: 7, math: 8, reading: 6, science: 6 },
    mini: { english: 3, math: 4, reading: 3, science: 3 },
    full: { english: 99, math: 99, reading: 99, science: 99 },
  },
  sat: {
    initial: { reading_writing: 9, math: 9 },
    mini: { reading_writing: 4, math: 4 },
    full: { reading_writing: 99, math: 99 },
  },
}

export interface BenchmarkPlan {
  exam: ExamFamily
  kind: BenchmarkKind
  sections: { section: string; count: number }[]
  totalQuestions: number
  expectedMinutes: number
}

export function planBenchmark(exam: ExamFamily, kind: BenchmarkKind, pool: PublicQuestion[]): BenchmarkPlan {
  const sections = SECTION_ORDER[exam]
    .map((section) => {
      const available = pool.filter((q) => q.exam_family === exam && q.section === section)
      return { section, count: Math.min(PER_SECTION[exam][kind][section] ?? 0, available.length), available }
    })
    .filter((s) => s.count > 0)
  const expectedSeconds = sections.reduce((sum, s) => {
    const avg = s.available.reduce((t, q) => t + (q.expected_time_seconds ?? 60), 0) / s.available.length
    return sum + avg * s.count
  }, 0)
  return {
    exam,
    kind,
    sections: sections.map(({ section, count }) => ({ section, count })),
    totalQuestions: sections.reduce((n, s) => n + s.count, 0),
    // Students new to the format run slower than the expected pace; budget 1.3x.
    expectedMinutes: Math.round((expectedSeconds * 1.3) / 60),
  }
}

/** Picks the unseen question in the section closest to the target difficulty. */
export function pickNext(pool: PublicQuestion[], section: string, targetDifficulty: number, used: Set<string>): PublicQuestion | null {
  const candidates = pool.filter((q) => q.section === section && !used.has(q.id))
  if (candidates.length === 0) return null
  return candidates.reduce((best, q) => {
    const d = Math.abs((q.difficulty ?? 3) - targetDifficulty)
    const bd = Math.abs((best.difficulty ?? 3) - targetDifficulty)
    return d < bd || (d === bd && q.id < best.id) ? q : best
  })
}

export function nextDifficulty(current: number, correct: boolean | null): number {
  if (correct === null) return current
  return Math.max(1, Math.min(5, current + (correct ? 1 : -1)))
}

export interface BenchmarkRecord {
  question_id: string
  attempt_id: string
  section: string
  difficulty: number | null
  skill_key: string | null
  expected_time_seconds: number | null
  answer: string | null
  is_correct: boolean | null
  skipped: boolean
  elapsed_ms: number
  active_ms: number
  confidence: Confidence | null
  strategy_key: string | null
  skip_events: number
  returns: number
  answer_changes: number
  trap: string | null
}

export function computeMetrics(records: BenchmarkRecord[]): BenchmarkMetrics {
  const answered = records.filter((r) => !r.skipped)
  const correct = answered.filter((r) => r.is_correct).length
  const paceOf = (rs: BenchmarkRecord[]) =>
    median(rs.filter((r) => r.expected_time_seconds).map((r) => r.active_ms / (r.expected_time_seconds! * 1000)))

  const sections: SectionMetrics[] = [...new Set(records.map((r) => r.section))].map((section) => {
    const rs = records.filter((r) => r.section === section)
    const ans = rs.filter((r) => !r.skipped)
    const ok = ans.filter((r) => r.is_correct)
    const pace = paceOf(ans)
    return {
      section,
      answered: ans.length,
      correct: ok.length,
      skipped: rs.length - ans.length,
      accuracy: ans.length ? ok.length / ans.length : null,
      pacing_ratio: pace === null ? null : Math.round(pace * 100) / 100,
      ceiling_difficulty: ok.length ? Math.max(...ok.map((r) => r.difficulty ?? 0)) : null,
    }
  })

  const calibration = ([1, 2, 3] as Confidence[]).map((confidence) => {
    const rs = answered.filter((r) => r.confidence === confidence)
    return { confidence, answered: rs.length, correct: rs.filter((r) => r.is_correct).length }
  })

  const strategyMap = new Map<string, { answered: number; correct: number }>()
  for (const r of answered) {
    if (!r.strategy_key) continue
    const e = strategyMap.get(r.strategy_key) ?? { answered: 0, correct: 0 }
    e.answered++
    if (r.is_correct) e.correct++
    strategyMap.set(r.strategy_key, e)
  }
  const trapMap = new Map<string, number>()
  for (const r of answered) if (!r.is_correct && r.trap) trapMap.set(r.trap, (trapMap.get(r.trap) ?? 0) + 1)

  const pace = paceOf(answered)
  return {
    answered: answered.length,
    correct,
    skipped: records.length - answered.length,
    skip_events: records.reduce((s, r) => s + r.skip_events, 0),
    returns: records.reduce((s, r) => s + r.returns, 0),
    answer_changes: records.reduce((s, r) => s + r.answer_changes, 0),
    accuracy: answered.length ? correct / answered.length : null,
    median_elapsed_ms: median(answered.map((r) => r.active_ms)),
    pacing_ratio: pace === null ? null : Math.round(pace * 100) / 100,
    calibration,
    strategy_use: [...strategyMap.entries()].map(([strategy_key, v]) => ({ strategy_key, ...v })),
    traps_fallen: [...trapMap.entries()].map(([trap, count]) => ({ trap, count })).sort((a, b) => b.count - a.count),
    sections,
  }
}

/** Below this ratio an answer is too fast to have been worked through. */
export const RUSHED_BELOW = 0.3

export type PacingVerdict = 'rushed' | 'fast' | 'on_pace' | 'slow' | 'unknown'

export function pacingVerdict(ratio: number | null): PacingVerdict {
  if (ratio === null) return 'unknown'
  if (ratio > PACING_WEAK_ABOVE) return 'slow'
  if (ratio < RUSHED_BELOW) return 'rushed'
  if (ratio < 0.6) return 'fast'
  return 'on_pace'
}

/** Days until the next suggested benchmark: mini every ~5 weeks, full every ~10. */
export function nextBenchmarkDue(history: BenchmarkSummary[], today: Date = new Date()): { kind: BenchmarkKind; inDays: number } {
  if (history.length === 0) return { kind: 'initial', inDays: 0 }
  const last = [...history].sort((a, b) => b.completed_at.localeCompare(a.completed_at))[0]!
  const lastFull = history.filter((b) => b.kind !== 'mini').sort((a, b) => b.completed_at.localeCompare(a.completed_at))[0]
  const days = (iso: string) => Math.floor((today.getTime() - new Date(iso).getTime()) / 86_400_000)
  if (lastFull && days(lastFull.completed_at) >= 70) return { kind: 'full', inDays: 0 }
  return { kind: 'mini', inDays: Math.max(0, 35 - days(last.completed_at)) }
}
