import type { ExamFamily } from './data/types'
import { MINI_EVERY_DAYS, PER_SECTION } from './engine/benchmark'

/**
 * Provisional question-bank planning target (docs/product/QUESTION_BANK_RECOMMENDATION.md,
 * docs/product/QUESTION_IMPORT_CONTRACT.md).
 *
 * This is a planning number for the separate question-bank workstream. It is NOT launch approval, and it does not
 * promise that fresh questions will be available to any student. The weekly goal shown to families is never lowered
 * to fit the bank; when the bank runs short, the app says so.
 *
 * Everything here is configurable: change the target, not the formulas.
 */
export interface ContentTarget {
  exam: ExamFamily
  questionsPerWeek: number
  weeks: number
  /** Share of each week deliberately spent on spaced review (repeats), 0–1. */
  plannedReview: number
  /** Extra unique practice items so a student isn't always shown the last few left (0.15 = 15%). */
  headroom: number
  /**
   * Reserved (assessment-only) items per section. Default: the starting benchmark plus every mini check in the
   * period, each with its own unseen items. Override to plan a different reserve.
   */
  reservedPerSection?: Record<string, number>
}

export const PROVISIONAL_TARGET: ContentTarget = { exam: 'act', questionsPerWeek: 40, weeks: 12, plannedReview: 0.25, headroom: 0.15 }

/** Mini checks in the period, on the MINI_EVERY_DAYS cadence after the starting benchmark. */
export function miniChecksIn(weeks: number): number {
  return Math.floor((weeks * 7) / MINI_EVERY_DAYS)
}

export function defaultReservedPerSection(exam: ExamFamily, weeks: number): Record<string, number> {
  const minis = miniChecksIn(weeks)
  const initial = PER_SECTION[exam].initial
  const mini = PER_SECTION[exam].mini
  return Object.fromEntries(Object.keys(initial).map((s) => [s, initial[s]! + minis * (mini[s] ?? 0)]))
}

export interface BankSize {
  practiceShown: number
  practiceUnique: number
  reserved: number
  reservedPerSection: Record<string, number>
  total: number
}

/** Unique items the bank needs for a target. Practice and reserved items are separate; reserved never enter practice. */
export function bankSize(t: ContentTarget = PROVISIONAL_TARGET): BankSize {
  if (t.plannedReview < 0 || t.plannedReview > 1) throw new Error('plannedReview must be between 0 and 1')
  if (!(t.questionsPerWeek > 0) || !(t.weeks > 0) || !(t.headroom >= 0)) throw new Error('questionsPerWeek and weeks must be positive, headroom not negative')
  if (Object.values(t.reservedPerSection ?? {}).some((n) => !(n >= 0))) throw new Error('reservedPerSection values must not be negative')
  const practiceShown = t.questionsPerWeek * t.weeks
  const practiceUnique = Math.ceil(practiceShown * (1 - t.plannedReview) * (1 + t.headroom))
  const reservedPerSection = t.reservedPerSection ?? defaultReservedPerSection(t.exam, t.weeks)
  const reserved = Object.values(reservedPerSection).reduce((a, b) => a + b, 0)
  return { practiceShown, practiceUnique, reserved, reservedPerSection, total: practiceUnique + reserved }
}
