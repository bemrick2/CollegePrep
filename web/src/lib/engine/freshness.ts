import type { AttemptRecord, BenchmarkSummary, ExamFamily } from '../data/types'
import { MINI_PER_SECTION } from './benchmark'

/**
 * Fresh questions, repeats and progress-check questions, per student.
 *
 *  - Fresh: a question this student has never been shown.
 *  - Held for the next check: in each section, the next mini check's worth of fresh questions is kept out of
 *    practice, so a progress check can be answered on questions the student has not seen.
 *  - Seen before (repeat): any question shown earlier. Repeats are allowed in practice (review helps learning) and
 *    count toward the weekly goal, but they are never used as evidence of improvement: the recent trend uses
 *    first answers only, and a progress-check section that contains repeats is not compared.
 */
export interface Q {
  id: string
  section: string
  exam_family: ExamFamily
  difficulty?: number | null
}

export interface SectionContent {
  section: string
  total: number
  seen: number
  unseen: number
  /** Fresh questions kept for the next progress check. */
  heldForCheck: number
  /** Fresh questions practice may still use. */
  freshForPractice: number
}

export interface ContentStatus {
  exam: ExamFamily
  sections: SectionContent[]
  freshForPractice: number
  /** Every section's practice is review only. */
  practiceAllReview: boolean
  /** Sections with no fresh practice left. */
  reviewOnlySections: string[]
  /** The next progress check can't be fully fresh in these sections. */
  checkShortSections: string[]
}

/** Questions held for checks: mid-difficulty first (the check starts at level 3), then by id, for stability. */
function heldIds(pool: Q[], seen: Set<string>, exam: ExamFamily): Set<string> {
  const held = new Set<string>()
  const bySection = new Map<string, Q[]>()
  for (const q of pool) if (q.exam_family === exam && !seen.has(q.id)) bySection.set(q.section, [...(bySection.get(q.section) ?? []), q])
  for (const [section, qs] of bySection) {
    const k = MINI_PER_SECTION[exam][section] ?? 0
    qs.sort((a, b) => Math.abs((a.difficulty ?? 3) - 3) - Math.abs((b.difficulty ?? 3) - 3) || (a.id < b.id ? -1 : 1))
      .slice(0, k)
      .forEach((q) => held.add(q.id))
  }
  return held
}

export function contentStatus(exam: ExamFamily, pool: Q[], seen: Set<string>): ContentStatus {
  const held = heldIds(pool, seen, exam)
  const sections = [...new Set(pool.filter((q) => q.exam_family === exam).map((q) => q.section))].map((section) => {
    const qs = pool.filter((q) => q.exam_family === exam && q.section === section)
    const seenN = qs.filter((q) => seen.has(q.id)).length
    const heldN = qs.filter((q) => held.has(q.id)).length
    return { section, total: qs.length, seen: seenN, unseen: qs.length - seenN, heldForCheck: heldN, freshForPractice: qs.length - seenN - heldN }
  })
  return {
    exam,
    sections,
    freshForPractice: sections.reduce((n, s) => n + s.freshForPractice, 0),
    practiceAllReview: sections.length > 0 && sections.every((s) => s.freshForPractice === 0),
    reviewOnlySections: sections.filter((s) => s.freshForPractice === 0).map((s) => s.section),
    checkShortSections: sections.filter((s) => s.heldForCheck < (MINI_PER_SECTION[exam][s.section] ?? 0)).map((s) => s.section),
  }
}

/** Practice may use everything except the questions held for the next check. */
export function practiceExclusions(exam: ExamFamily, pool: Q[], seen: Set<string>): Set<string> {
  return heldIds(pool, seen, exam)
}

export const seenSet = (attempts: Pick<AttemptRecord, 'question_id'>[]) => new Set(attempts.map((a) => a.question_id))

/** First answers only: an attempt counts as fresh evidence if no earlier attempt at the same question exists. */
export function firstAnswers<T extends Pick<AttemptRecord, 'question_id' | 'submitted_at'>>(attempts: T[]): T[] {
  const first = new Map<string, T>()
  for (const a of attempts) {
    const prev = first.get(a.question_id)
    if (!prev || a.submitted_at < prev.submitted_at) first.set(a.question_id, a)
  }
  const keep = new Set(first.values())
  return attempts.filter((a) => keep.has(a))
}

/** Per section, how many of a benchmark's questions the student had already seen before it started. */
export function benchmarkRepeats(b: BenchmarkSummary, history: Pick<AttemptRecord, 'id' | 'question_id' | 'section' | 'submitted_at'>[]): Map<string, number> {
  const mine = new Set(b.attempt_ids)
  const out = new Map<string, number>()
  for (const a of history) {
    if (!mine.has(a.id)) continue
    const before = history.some((x) => x.question_id === a.question_id && !mine.has(x.id) && x.submitted_at < b.started_at)
    if (before) out.set(a.section, (out.get(a.section) ?? 0) + 1)
  }
  return out
}
