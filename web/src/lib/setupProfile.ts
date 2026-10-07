import type { ExamFamily } from './data/types'

/**
 * Setup answers the database can't store yet (contract request CR-26), kept in this browser per student until it
 * can. Each is read back by the screens that use it and labelled as the family's answer. Nothing here is a score
 * estimate.
 */
export type ExamIntent = 'act' | 'sat' | 'both' | 'undecided'

export interface PracticeTestScore {
  exam: ExamFamily
  testDate: string
  composite: number
  sections: Record<string, number>
}

export interface StudentSetup {
  examIntent?: ExamIntent
  /** A published national test date (ISO), or null for "not sure yet". */
  plannedTestDate?: string | null
  /** ISO weekdays, 1 = Monday. */
  studyDays?: number[]
  highSchool?: string
  /** A full practice test the family reported. Never used for merit or award comparisons. */
  practiceScore?: PracticeTestScore | null
  /** The family answered the starting-point question (a score, "not yet" or "don't remember"). */
  startingPointDone?: boolean
}

const KEY = (studentId: string) => `pp-setup:${studentId}`

export function readStudentSetup(studentId: string | null | undefined): StudentSetup {
  if (!studentId) return {}
  try {
    const v = JSON.parse(localStorage.getItem(KEY(studentId)) ?? '{}') as unknown
    return v && typeof v === 'object' ? (v as StudentSetup) : {}
  } catch {
    return {}
  }
}

export function writeStudentSetup(studentId: string, patch: StudentSetup) {
  try {
    localStorage.setItem(KEY(studentId), JSON.stringify({ ...readStudentSetup(studentId), ...patch }))
  } catch {
    /* storage unavailable: the answer is used for this visit only */
  }
}

/** An unfinished setup, per signed-in user, so a reload or a later visit resumes where it stopped. */
const DRAFT = (userId: string) => `pp-setup-draft:${userId}`

export function readSetupDraft<T>(userId: string | null | undefined): T | null {
  if (!userId) return null
  try {
    const raw = localStorage.getItem(DRAFT(userId))
    return raw ? (JSON.parse(raw) as T) : null
  } catch {
    return null
  }
}

export function writeSetupDraft(userId: string, draft: unknown) {
  try {
    localStorage.setItem(DRAFT(userId), JSON.stringify(draft))
  } catch {
    /* storage unavailable */
  }
}

export function clearSetupDraft(userId: string) {
  try {
    localStorage.removeItem(DRAFT(userId))
  } catch {
    /* storage unavailable */
  }
}
