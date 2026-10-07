import type { ExamFamily } from '../../lib/data/types'

export const GOAL_OPTIONS = [
  { key: 'raise_score', label: 'Raise my test score', description: 'Steady practice toward a target' },
  { key: 'merit', label: 'Qualify for merit aid', description: 'Scores often drive scholarship tiers' },
  { key: 'college_credit', label: 'Earn college credit early', description: 'AP, CLEP and dual enrollment' },
  { key: 'lower_cost', label: 'Lower the total cost', description: 'Compare real prices and paths' },
  { key: 'explore', label: 'Explore colleges', description: 'Find schools that fit' },
] as const

export const GRADES = [6, 7, 8, 9, 10, 11, 12]

export function gradeLabel(g: number | null): string {
  if (g === null) return 'Grade not set'
  return `${g}th grade`
}

/** The spring graduation year for a student currently in the given grade. */
export function graduationYearFor(grade: number, now = new Date()): number {
  const schoolYearEnd = now.getMonth() >= 6 ? now.getFullYear() + 1 : now.getFullYear()
  return schoolYearEnd + (12 - grade)
}

export const SCORE_RANGE: Record<ExamFamily, { min: number; max: number; step: number; default: number }> = {
  act: { min: 12, max: 36, step: 1, default: 26 },
  sat: { min: 800, max: 1600, step: 10, default: 1250 },
}

export const EXAM_NAME: Record<ExamFamily, string> = { act: 'ACT', sat: 'SAT' }

export function timeZones(): string[] {
  try {
    return (Intl as unknown as { supportedValuesOf(k: string): string[] }).supportedValuesOf('timeZone')
  } catch {
    return ['UTC', 'America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles']
  }
}

/** Inverse of graduationYearFor: the grade this school year for a given graduation year (null outside 6–12). */
export function gradeForGraduationYear(year: number, now = new Date()): number | null {
  const schoolYearEnd = now.getMonth() >= 6 ? now.getFullYear() + 1 : now.getFullYear()
  const g = 12 - (year - schoolYearEnd)
  return g >= 6 && g <= 12 ? g : null
}

/** Graduation years for students in grades 12 down to 6 this school year. */
export function graduationYears(now = new Date()): number[] {
  return GRADES.slice().reverse().map((g) => graduationYearFor(g, now))
}

/** Languages the app is actually written in. A language control appears only when there is a choice. */
export const SUPPORTED_LANGUAGES = [{ code: 'en', name: 'English' }] as const

/** Session lengths. Short ones lead; 20 and 30 need CR-26 on the backend (daily_minutes 5–30). */
export const SHORT_SESSIONS = [5, 10, 15] as const
export const LONG_SESSIONS = [20, 30] as const

/** The existing weekly question goal presets. */
export const WEEKLY_GOALS = [
  { value: 20, label: '20 · light' },
  { value: 40, label: '40 · steady' },
  { value: 60, label: '60 · intense' },
] as const
