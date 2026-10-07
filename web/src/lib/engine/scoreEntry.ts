import type { ExamFamily } from '../data/types'

/**
 * Checks a score the family types in from a real test report or a full-length practice test. Nothing here estimates
 * or fills in a score: blank stays blank, and "haven't tested" is a complete answer.
 */

export const SECTION_FIELDS: Record<ExamFamily, { key: string; label: string; min: number; max: number; step: number }[]> = {
  act: [
    { key: 'english', label: 'English', min: 1, max: 36, step: 1 },
    { key: 'math', label: 'Math', min: 1, max: 36, step: 1 },
    { key: 'reading', label: 'Reading', min: 1, max: 36, step: 1 },
    { key: 'science', label: 'Science', min: 1, max: 36, step: 1 },
  ],
  sat: [
    { key: 'reading_writing', label: 'Reading and Writing', min: 200, max: 800, step: 10 },
    { key: 'math', label: 'Math', min: 200, max: 800, step: 10 },
  ],
}

export const COMPOSITE_RANGE: Record<ExamFamily, { min: number; max: number; step: number; label: string }> = {
  act: { min: 1, max: 36, step: 1, label: 'Composite (1–36)' },
  sat: { min: 400, max: 1600, step: 10, label: 'Total (400–1600)' },
}

export interface ScoreDraft {
  exam: ExamFamily
  composite: string
  sections: Record<string, string>
  testDate: string
}

export interface ScoreCheck {
  ok: boolean
  errors: Partial<Record<'composite' | 'testDate' | string, string>>
  /** Only the sections that were filled in. */
  sections: Record<string, number>
  composite: number | null
}

function inRange(raw: string, r: { min: number; max: number; step: number }): number | 'bad' | null {
  const t = raw.trim()
  if (!t) return null
  if (!/^\d+$/.test(t)) return 'bad'
  const n = Number(t)
  if (n < r.min || n > r.max || n % r.step !== 0) return 'bad'
  return n
}

export function checkScore(d: ScoreDraft, today: string): ScoreCheck {
  const errors: ScoreCheck['errors'] = {}
  const range = COMPOSITE_RANGE[d.exam]
  const c = inRange(d.composite, range)
  if (c === null) errors.composite = 'Enter the score from the report.'
  else if (c === 'bad') errors.composite = d.exam === 'act' ? 'An ACT composite is a whole number from 1 to 36.' : 'An SAT total is 400 to 1600, in steps of 10.'
  const sections: Record<string, number> = {}
  for (const f of SECTION_FIELDS[d.exam]) {
    const v = inRange(d.sections[f.key] ?? '', f)
    if (v === 'bad') errors[f.key] = d.exam === 'act' ? '1 to 36' : '200 to 800, in steps of 10'
    else if (v !== null) sections[f.key] = v
  }
  // The SAT total is exactly the sum of its two sections; a mismatch means a typo somewhere.
  if (d.exam === 'sat' && typeof c === 'number' && sections.reading_writing && sections.math && sections.reading_writing + sections.math !== c)
    errors.composite = `Reading and Writing plus Math is ${sections.reading_writing + sections.math}, not ${c}. Check the report.`
  if (!/^\d{4}-\d{2}-\d{2}$/.test(d.testDate)) errors.testDate = 'Enter the test date.'
  else if (d.testDate > today) errors.testDate = "That date hasn't happened yet."
  return { ok: Object.keys(errors).length === 0, errors, sections, composite: typeof c === 'number' ? c : null }
}
