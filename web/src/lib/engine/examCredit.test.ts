import { describe, expect, it } from 'vitest'
import { examKey, examOptions, matchExam, minScore, summarizeSchool, type CreditPolicy, type PlannedExam } from './examCredit'

const utk: CreditPolicy[] = [
  {
    policy_kind: 'AP',
    equivalencies: [
      { exam_or_course_code: 'AP-CALCAB', exam_or_course_name: 'AP Calculus AB', minimum_score: '3', institution_course_equivalent: 'MATH 125', credits_awarded: null },
      { exam_or_course_code: 'AP-CALCAB', exam_or_course_name: 'AP Calculus AB', minimum_score: '4', institution_course_equivalent: 'MATH 141', credits_awarded: 4 },
      { exam_or_course_code: 'AP-USH', exam_or_course_name: 'AP American History', minimum_score: '4 or 5', institution_course_equivalent: 'HIUS 221-222', credits_awarded: 6 },
      { exam_or_course_code: 'AP-ITAL', exam_or_course_name: 'AP Italian', minimum_score: 'N/A', institution_course_equivalent: null },
      { exam_or_course_code: 'AP-PCM', exam_or_course_name: 'AP Physics C - Mechanics', minimum_score: '4', institution_course_equivalent: 'PHYS 135', credits_awarded: 4 },
      { exam_or_course_code: 'AP-PCM', exam_or_course_name: 'AP Physics C - Mechanics', minimum_score: '4', institution_course_equivalent: 'PHYS 137', credits_awarded: 4 },
    ],
  },
  { policy_kind: 'dual_enrollment', equivalencies: [] },
]
const other: CreditPolicy[] = [
  { policy_kind: 'AP', equivalencies: [{ exam_or_course_code: 'AP-UNITED-STATES-HISTORY', exam_or_course_name: 'AP United States History', minimum_score: '3, 4, or 5', institution_course_equivalent: 'HIST 2010', credits_awarded: 3 }] },
]
const exam = (name: string, score: number | null): PlannedExam => ({ family: 'AP', key: examKey('AP', name), name, score })

describe('exam credit', () => {
  it('parses published minimums', () => {
    expect(minScore('4 or 5')).toBe(4)
    expect(minScore('3, 4, or 5')).toBe(3)
    expect(minScore('75%')).toBe(75)
    expect(minScore('N/A')).toBeNull()
  })

  it('matches the same exam across schools whose names differ', () => {
    expect(examKey('AP', 'AP American History')).toBe(examKey('AP', 'AP United States History'))
    expect(examKey('AP', 'AP English Language & Composition')).toBe(examKey('AP', 'English Language and Composition'))
    const opts = examOptions([utk, other])
    expect(opts.filter((o) => o.key === examKey('AP', 'US History'))).toHaveLength(1)
  })

  it('uses the highest threshold the score meets', () => {
    const m = matchExam(utk, exam('AP Calculus AB', 4))
    expect(m.status).toBe('qualifies')
    expect(m.earned.map((t) => t.course)).toEqual(['MATH 141'])
    expect(matchExam(utk, exam('AP Calculus AB', 2)).status).toBe('below')
    expect(matchExam(utk, exam('AP Calculus AB', null))).toMatchObject({ status: 'planned', lowest: 3 })
  })

  it('distinguishes no credit, not listed and no table', () => {
    expect(matchExam(utk, exam('AP Italian', 5)).status).toBe('not_awarded')
    expect(matchExam(utk, exam('AP Seminar', 5)).status).toBe('not_listed')
    expect(matchExam([], exam('AP Calculus AB', 5)).status).toBe('no_table')
  })

  it('counts each exam once and only published hours', () => {
    const s = summarizeSchool(utk, [exam('AP Calculus AB', 3), exam('AP Physics C: Mechanics', 5), exam('AP US History', 5), exam('AP Italian', 5)])
    expect(s.courses).toBe(3)
    expect(s.publishedHours).toBe(10)
    expect(s.coursesWithoutHours).toBe(1)
    expect(s.hasTable).toBe(true)
  })
})
