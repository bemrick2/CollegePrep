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

describe('IB, Statewide Dual Credit and minimums printed in words (#197)', () => {
  const ib: CreditPolicy[] = [
    {
      policy_kind: 'IB',
      equivalencies: [
        { exam_or_course_code: 'IB-BIO-HL', exam_or_course_name: 'IB Biology (HL)', minimum_score: '5+', institution_course_equivalent: 'BIOL 101-102' },
        { exam_or_course_code: 'IB-ECON', exam_or_course_name: 'IB Economics (SL or HL)', minimum_score: '5+', institution_course_equivalent: 'ECON 211, 213' },
        { exam_or_course_code: 'IB-HIST', exam_or_course_name: 'IB History', minimum_score: 'HL 4', institution_course_equivalent: 'HIST 101' },
        { exam_or_course_code: 'IB-HIST', exam_or_course_name: 'IB History', minimum_score: 'SL 5', institution_course_equivalent: 'HIST 1XX' },
        { exam_or_course_code: 'IB-CHEM', exam_or_course_name: 'IB Chemistry', minimum_score: 'SL & HL', institution_course_equivalent: 'CHEM 1110', notes: 'HL | 5,6, OR 7' },
      ],
    },
    {
      policy_kind: 'statewide_dual_credit',
      equivalencies: [
        { exam_or_course_code: 'SDC-BUS', exam_or_course_name: 'Statewide Dual Credit Introduction to Business', minimum_score: '80%', institution_course_equivalent: 'BUAD LD (3 credits)', credits_awarded: 3 },
      ],
    },
    { policy_kind: 'AP', equivalencies: [{ exam_or_course_code: 'AP-MUS', exam_or_course_name: 'AP Music Theory', minimum_score: 'Subscores', institution_course_equivalent: 'MUS 1XXX' }] },
  ]
  const ibExam = (name: string, score: number | null, level: 'SL' | 'HL' | null): PlannedExam => ({ family: 'IB', key: examKey('IB', name), name, score, level })

  it('one IB subject across level-tagged names', () => {
    expect(examKey('IB', 'IB Biology (HL)')).toBe(examKey('IB', 'Biology'))
    expect(examKey('IB', 'IB Economics (SL or HL)')).toBe('IB:economics')
    expect(examOptions([ib]).filter((o) => o.family === 'IB').map((o) => o.name)).toEqual(['IB Biology', 'IB Chemistry', 'IB Economics', 'IB History'])
  })

  it('matches IB by level and score; a level-specific row never matches an unknown level', () => {
    expect(matchExam(ib, ibExam('Biology', 6, 'HL')).status).toBe('qualifies')
    expect(matchExam(ib, ibExam('Biology', 6, 'SL')).status).toBe('other_level')
    expect(matchExam(ib, ibExam('Biology', 6, null)).status).toBe('needs_level')
    expect(matchExam(ib, ibExam('Economics', 5, 'SL')).status).toBe('qualifies')
    expect(matchExam(ib, ibExam('History', 4, 'HL')).earned.map((t) => t.course)).toEqual(['HIST 101'])
    expect(matchExam(ib, ibExam('History', 4, 'SL'))).toMatchObject({ status: 'below', lowest: 5 })
  })

  it('a minimum printed without a score is "read the criteria", not "no credit"', () => {
    expect(matchExam(ib, ibExam('Chemistry', 7, 'HL')).status).toBe('read_criteria')
    expect(matchExam(ib, exam('AP Music Theory', 5)).status).toBe('read_criteria')
    expect(matchExam(utk, exam('AP Italian', 5)).status).toBe('not_awarded')
  })

  it('Statewide Dual Credit percentages', () => {
    const sdc = (score: number | null): PlannedExam => ({ family: 'SDC', key: examKey('SDC', 'Introduction to Business'), name: 'Statewide Dual Credit Introduction to Business', score })
    expect(matchExam(ib, sdc(85))).toMatchObject({ status: 'qualifies', lowest: 80 })
    expect(matchExam(ib, sdc(79)).status).toBe('below')
    expect(summarizeSchool(ib, [sdc(85)]).publishedHours).toBe(3)
  })
})
