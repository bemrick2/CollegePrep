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

export const PER_SECTION: Record<ExamFamily, Record<BenchmarkKind, Record<string, number>>> = {
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


// ---------------------------------------------------------------------------
// Cadence and improvement
// ---------------------------------------------------------------------------

/** Mini benchmark every ~5 weeks (4–6), full every ~10 weeks (8–12) or before a real test. */
export const MINI_EVERY_DAYS = 35
export const FULL_EVERY_DAYS = 70

/**
 * A full check needs its own full-length set of questions, held out of practice entirely. None exists yet: a "full"
 * plan would take every question in the bank, mostly ones the student has already practised. Until a held-out form
 * is authored (docs/product/CONTENT_PLAN.md §2), every later check is a mini.
 */
export const FULL_FORM_READY = false

export interface BenchmarkSchedule {
  kind: BenchmarkKind
  inDays: number
  /** Local calendar date the next benchmark becomes due (ISO yyyy-mm-dd). */
  dueDate: string
  overdueDays: number
}

export function benchmarkSchedule(history: BenchmarkSummary[], today: Date = new Date(), fullReady: boolean = FULL_FORM_READY): BenchmarkSchedule {
  const iso = (d: Date) => d.toISOString().slice(0, 10)
  if (history.length === 0) return { kind: 'initial', inDays: 0, dueDate: iso(today), overdueDays: 0 }
  const byDate = [...history].sort((a, b) => b.completed_at.localeCompare(a.completed_at))
  const last = byDate[0]!
  const lastBroad = byDate.find((b) => b.kind !== 'mini') ?? last
  const days = (s: string) => Math.floor((today.getTime() - new Date(s).getTime()) / 86_400_000)
  const sinceBroad = days(lastBroad.completed_at)
  const sinceLast = days(last.completed_at)
  const kind: BenchmarkKind = fullReady && sinceBroad >= FULL_EVERY_DAYS ? 'full' : 'mini'
  const remaining = kind === 'full' ? FULL_EVERY_DAYS - sinceBroad : MINI_EVERY_DAYS - sinceLast
  const due = new Date(today.getTime() + Math.max(0, remaining) * 86_400_000)
  return { kind, inDays: Math.max(0, remaining), dueDate: iso(due), overdueDays: Math.max(0, -remaining) }
}

/** Back-compat wrapper used by older screens. */
export function nextBenchmarkDue(history: BenchmarkSummary[], today: Date = new Date()): { kind: BenchmarkKind; inDays: number } {
  const s = benchmarkSchedule(history, today)
  return { kind: s.kind, inDays: s.inDays }
}

export interface BenchmarkChange {
  from: BenchmarkSummary
  to: BenchmarkSummary
  /** Accuracy change in percentage points; null when either side has no answers. */
  accuracyPts: number | null
  /** Change in median time vs expected (negative = faster). */
  pacingDelta: number | null
  sections: { section: string; accuracyPts: number | null; ceilingDelta: number | null }[]
}

/** Latest benchmark vs the one before. Adaptive benchmarks change difficulty, so the hardest level answered
 *  correctly (ceiling) is reported next to accuracy; neither is an official score change. */
export function benchmarkImprovement(history: BenchmarkSummary[]): BenchmarkChange | null {
  const byDate = [...history].sort((a, b) => a.completed_at.localeCompare(b.completed_at))
  if (byDate.length < 2) return null
  const to = byDate[byDate.length - 1]!
  const from = byDate[byDate.length - 2]!
  const pts = (a: number | null, b: number | null) => (a === null || b === null ? null : Math.round((b - a) * 100))
  const sections = to.metrics.sections.map((s) => {
    const p = from.metrics.sections.find((x) => x.section === s.section)
    return {
      section: s.section,
      accuracyPts: pts(p?.accuracy ?? null, s.accuracy),
      ceilingDelta: p?.ceiling_difficulty != null && s.ceiling_difficulty != null ? s.ceiling_difficulty - p.ceiling_difficulty : null,
    }
  })
  return {
    from,
    to,
    accuracyPts: pts(from.metrics.accuracy, to.metrics.accuracy),
    pacingDelta:
      from.metrics.pacing_ratio === null || to.metrics.pacing_ratio === null ? null : Math.round((to.metrics.pacing_ratio - from.metrics.pacing_ratio) * 100) / 100,
    sections,
  }
}

/** Attempt ids that belong to benchmarks, so benchmark work never counts as (or replaces) daily practice. */
export function benchmarkAttemptIds(history: BenchmarkSummary[]): Set<string> {
  return new Set(history.flatMap((b) => b.attempt_ids))
}

/** Questions per section in a mini progress check: what is held back from practice for the next check. */
export const MINI_PER_SECTION: Record<ExamFamily, Record<string, number>> = { act: PER_SECTION.act.mini, sat: PER_SECTION.sat.mini }
