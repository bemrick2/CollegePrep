import type { AttemptRecord, BenchmarkSummary, ExamFamily } from '../data/types'
import type { PoolStatus } from '../data/source'
import { MINI_PER_SECTION, PER_SECTION } from './benchmark'

/**
 * Fresh questions, repeats and the reserved assessment pool, per student (CR-23, #218 B1).
 *
 *  - Reserved (assessment pool): questions that only progress checks use. Practice never shows them and never lends
 *    them out, whatever else is left. The set is fixed, not "whatever is still unseen".
 *  - Fresh: a question this student has never been shown.
 *  - Seen before (repeat): any question shown earlier. Repeats are allowed in practice (review helps learning) and
 *    count toward the weekly goal, but they are never used as evidence of improvement: the recent trend uses
 *    first answers only, and a progress-check section that contains repeats is not compared.
 *
 * When the reserved pool is too small for a check (checkPlan):
 *  1. unseen reserved questions first;
 *  2. then reserved repeats; the section is flagged and gets no verdict;
 *  3. a section with fewer reserved questions than the check asks for is shortened, and says so;
 *  4. a section with no reserved questions is not measured;
 *  5. practice questions are never used to fill a check.
 *
 * Where the pool comes from: a question's `pool` when the source provides one (the CR-23 column). Until then the
 * reserve is assigned here, deterministically (mid-difficulty first, then id), RESERVED_PER_SECTION per section.
 * That assignment is fixed only while the bank is: publishing or retiring a question can move it, which is why the
 * server column (CR-23) replaces it. When the column arrives, the migration must seed the reserve before the client
 * reads `pool`: once any question carries a mark, unmarked questions count as practice.
 */
export type QuestionPool = 'practice' | 'assessment'

export interface Q {
  id: string
  section: string
  exam_family: ExamFamily
  difficulty?: number | null
  pool?: QuestionPool | null
}

/**
 * Reserved questions per section when the source doesn't mark them. Configurable; the default is one mini check's
 * worth (ACT 3/4/3/3, SAT 4/4), because today's bank is small. The planning target for the bank workstream is in
 * lib/contentTarget.ts.
 */
export const RESERVED_PER_SECTION: Readonly<Record<ExamFamily, Readonly<Record<string, number>>>> = Object.freeze({
  act: Object.freeze({ ...MINI_PER_SECTION.act }),
  sat: Object.freeze({ ...MINI_PER_SECTION.sat }),
})

export interface SectionContent {
  section: string
  total: number
  seen: number
  unseen: number
  /** Reserved for progress checks (never practice). */
  reserved: number
  /** Reserved questions this student hasn't seen yet. */
  reservedUnseen: number
  /** Same as `reserved`; the name screens used before CR-23. */
  heldForCheck: number
  /** Fresh practice questions left. */
  freshForPractice: number
}

export interface ContentStatus {
  exam: ExamFamily
  /** False when the source hides reserved items and couldn't give their counts: reserved figures are then unknown. */
  reserveKnown: boolean
  sections: SectionContent[]
  freshForPractice: number
  /** Every section's practice is review only. */
  practiceAllReview: boolean
  /** Sections with no fresh practice left. */
  reviewOnlySections: string[]
  /** The next mini check can't be fully fresh in these sections. */
  checkShortSections: string[]
}

const nearMiddle = (a: Q, b: Q) => Math.abs((a.difficulty ?? 3) - 3) - Math.abs((b.difficulty ?? 3) - 3) || (a.id < b.id ? -1 : 1)

/** The reserved assessment pool for one exam: the source's marks when it has them, otherwise the fixed assignment. */
export function reservedIds(exam: ExamFamily, pool: Q[], perSection: Readonly<Record<string, number>> = RESERVED_PER_SECTION[exam]): Set<string> {
  const mine = pool.filter((q) => q.exam_family === exam)
  if (mine.some((q) => q.pool != null)) return new Set(mine.filter((q) => q.pool === 'assessment').map((q) => q.id))
  const held = new Set<string>()
  const bySection = new Map<string, Q[]>()
  for (const q of mine) bySection.set(q.section, [...(bySection.get(q.section) ?? []), q])
  for (const [section, qs] of bySection)
    qs.sort(nearMiddle)
      .slice(0, perSection[section] ?? 0)
      .forEach((q) => held.add(q.id))
  return held
}

/** The reserved pool as counts (what the server's assessment_pool_status returns), from questions the source can see. */
export function poolStatusOf(exam: ExamFamily, pool: Q[], seen: Set<string>): PoolStatus[] {
  const reserved = reservedIds(exam, pool)
  const by = new Map<string, PoolStatus>()
  for (const q of pool)
    if (q.exam_family === exam && reserved.has(q.id)) {
      const x = by.get(q.section) ?? { section: q.section, reserved: 0, unseen: 0 }
      x.reserved++
      if (!seen.has(q.id)) x.unseen++
      by.set(q.section, x)
    }
  return [...by.values()]
}

/**
 * `counts`: the reserved pool as the server counts it (assessment_pool_status). Pass it when the source hides reserved
 * content (live); null means the server couldn't say, so reserved figures are unknown. Omit it when `pool` holds every
 * question (demo, tests).
 */
export function contentStatus(exam: ExamFamily, pool: Q[], seen: Set<string>, counts?: PoolStatus[] | null): ContentStatus {
  const reserved = reservedIds(exam, pool)
  const known = counts !== null
  const res = counts ?? (counts === undefined ? poolStatusOf(exam, pool, seen) : [])
  const mine = pool.filter((q) => q.exam_family === exam)
  const names = [...new Set([...mine.map((q) => q.section), ...res.map((x) => x.section)])]
  const sections = names.map((section) => {
    const practice = mine.filter((q) => q.section === section && !reserved.has(q.id))
    const r = res.find((x) => x.section === section) ?? { reserved: 0, unseen: 0 }
    const practiceSeen = practice.filter((q) => seen.has(q.id)).length
    return {
      section,
      total: practice.length + r.reserved,
      seen: practiceSeen + (r.reserved - r.unseen),
      unseen: practice.length - practiceSeen + r.unseen,
      reserved: r.reserved,
      reservedUnseen: r.unseen,
      heldForCheck: r.reserved,
      freshForPractice: practice.length - practiceSeen,
    }
  })
  return {
    exam,
    reserveKnown: known,
    sections,
    freshForPractice: sections.reduce((n, s) => n + s.freshForPractice, 0),
    practiceAllReview: sections.length > 0 && sections.every((s) => s.freshForPractice === 0),
    reviewOnlySections: sections.filter((s) => s.freshForPractice === 0).map((s) => s.section),
    checkShortSections: known ? sections.filter((s) => s.reservedUnseen < (MINI_PER_SECTION[exam][s.section] ?? 0)).map((s) => s.section) : [],
  }
}

/** Practice never uses the reserved pool, whether or not the student has seen those questions. */
export function practiceExclusions(exam: ExamFamily, pool: Q[], _seen?: Set<string>): Set<string> {
  return reservedIds(exam, pool)
}

/** The questions a progress check may use: the reserved pool only. */
export function checkQuestions<T extends Q>(exam: ExamFamily, pool: T[]): T[] {
  const ids = reservedIds(exam, pool)
  return pool.filter((q) => ids.has(q.id))
}

/**
 * The next question a check shows in a section: an unseen reserved question nearest the target difficulty, else a
 * reserved repeat (the section then gets no verdict). Never a practice question; null when the section's reserve is
 * used up in this run.
 */
export function nextCheckQuestion<T extends Q>(exam: ExamFamily, pool: T[], section: string, target: number, used: Set<string>, seen: Set<string>): T | null {
  const reserved = checkQuestions(exam, pool).filter((q) => q.section === section && !used.has(q.id))
  const nearest = (qs: T[]) =>
    qs.reduce<T | null>((best, q) => {
      if (!best) return q
      const d = Math.abs((q.difficulty ?? 3) - target)
      const bd = Math.abs((best.difficulty ?? 3) - target)
      return d < bd || (d === bd && q.id < best.id) ? q : best
    }, null)
  return nearest(reserved.filter((q) => !seen.has(q.id))) ?? nearest(reserved)
}

export interface CheckSectionPlan {
  section: string
  /** What the check asks for in this section. */
  wanted: number
  /** What it will use: never more than the reserved questions in the section. */
  count: number
  unseen: number
  /** Reserved repeats it will need. Any repeat means the section gets no verdict. */
  repeats: number
  status: 'fresh' | 'with_repeats' | 'not_measured'
  /** Fewer reserved questions than asked for: the section is shorter. */
  shortened: boolean
}

/** What a check can be, per section, from the reserved pool alone (rules 1–5 above). */
export function checkPlan(exam: ExamFamily, wantedPerSection: Record<string, number>, pool: Q[], seen: Set<string>): CheckSectionPlan[] {
  return checkPlanFromCounts(wantedPerSection, poolStatusOf(exam, pool, seen))
}

/** The same plan from counts only (the server hides reserved content until a check opens). */
export function checkPlanFromCounts(wantedPerSection: Record<string, number>, counts: PoolStatus[]): CheckSectionPlan[] {
  return Object.entries(wantedPerSection).map(([section, wanted]) => {
    const c = counts.find((x) => x.section === section) ?? { reserved: 0, unseen: 0 }
    const count = Math.min(wanted, c.reserved)
    const unseen = Math.min(count, c.unseen)
    const repeats = count - unseen
    return { section, wanted, count, unseen, repeats, status: count === 0 ? 'not_measured' : repeats > 0 ? 'with_repeats' : 'fresh', shortened: count > 0 && count < wanted }
  })
}

/**
 * The next question an open check shows in a section, from the check's own reserved items (the server's
 * benchmark_questions): unseen first, nearest the target difficulty, then repeats. Never anything else.
 */
export function pickCheckItem<T extends { question: Q; seen_before: boolean }>(items: T[], section: string, target: number, used: Set<string>): T | null {
  const open = items.filter((i) => i.question.section === section && !used.has(i.question.id))
  const nearest = (xs: T[]) =>
    xs.reduce<T | null>((best, x) => {
      if (!best) return x
      const d = Math.abs((x.question.difficulty ?? 3) - target)
      const bd = Math.abs((best.question.difficulty ?? 3) - target)
      return d < bd || (d === bd && x.question.id < best.question.id) ? x : best
    }, null)
  return nearest(open.filter((i) => !i.seen_before)) ?? nearest(open)
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

/** A check's size from the reserved pool's counts: per section the check's length or the reserve, whichever is smaller.
 *  Minutes are an estimate from `secondsPerQuestion` (1.3x for students new to the format, as planBenchmark). */
export function checkSize(exam: ExamFamily, kind: keyof (typeof PER_SECTION)['act'], counts: PoolStatus[], secondsPerQuestion = 60): { questions: number; minutes: number } {
  const questions = Object.entries(PER_SECTION[exam][kind]).reduce((n, [section, want]) => n + Math.min(want, counts.find((c) => c.section === section)?.reserved ?? 0), 0)
  return { questions, minutes: Math.round((questions * secondsPerQuestion * 1.3) / 60) }
}
