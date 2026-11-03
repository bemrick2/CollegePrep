// Regression (2026-11-03 owner direction): a plan row whose alternatives exist only in its printed wording (an
// "unresolved or row") never receives credit automatically, so it can't make a requirement, a whole term, coverage or
// a saving look met. Showing the wording verbatim is not enough on its own; these tests check the engine itself.
// Each case has a control: the same courses stored as a reviewed structure (any_of) are filled, so the test would
// catch the engine silently placing nothing at all.
import { describe, expect, it } from 'vitest'
import { degreeCredit, type PlanTerm } from './degreeCredit'
import { readPlanItem, rowMarks, titleAlternatives, unresolvedAlternatives } from './planItems'

const award = (...courses: string[]) => courses.map((course) => ({ status: 'qualifies', exam: { name: `Exam for ${course}` }, earned: [{ course, credits: 3, minimumText: '3' }] }) as never)
/** One regular full-time semester: the row under test plus a course the student also has credit for. */
const term = (row: unknown): PlanTerm[] => [{ term_index: 1, label: 'Fall', credit_hours: '15', items: [{ code: 'HIST 1110', credits: 3 }, row as never] }]

// The printed shapes on file (verified plans, 2026-11-03 scan after the #302 review: 4,983 such rows).
const UNRESOLVED: [string, string, string[]][] = [
  ['A or B', 'MATH 1710 or MATH 1730', ['MATH 1710']],
  ['a three-way list', 'MATH 132 or MATH 141 or MATH 147', ['MATH 147']],
  ['a placement condition (UTC Management, footnote *)', 'Elective (ENGL 1010 or 1011)*', ['ENGL 1010']],
  ['a joined "or" (Oregon)', 'INM 101or VOK 101', ['VOK 101']],
  ['a slash', 'ENGL 221/MODL 221', ['MODL 221']],
  ['a comma list with a carried subject (UAF)', 'WRTG F211X, F212X, F213X, or F214X', ['WRTG F212X']],
  ['a level, not a course', 'ART 3700 level or higher Art History Elective', ['ART 3700']],
  // Comma lists with no "or" (#302 review): "any one" can't be read from them.
  ['a "two from" comma list (OK State)', 'Students should complete two courses from: CHEM 3353, CHEM 3363, and CHEM 4333', ['CHEM 3353']],
  ['a timing note (OK State)', 'SC 2183, MC 2003, and MC 2023 can be taken as late as junior fall.', ['SC 2183']],
  ['a survey list (UO)', 'One major survey course (JPN 305, 306, 307, 315)', ['JPN 306']],
]

describe('unresolved "or" rows are never filled by credit', () => {
  for (const [name, row, earned] of UNRESOLVED) {
    it(`${name}: “${row}”`, () => {
      const e = readPlanItem(row)!
      expect(unresolvedAlternatives(e)).toBe(true)
      const r = degreeCredit(award('HIST 1110', ...earned), term(row))
      const exam = r.accepted.find((a) => a.course === earned[0])!
      // No placement: nothing matched, reported as named among alternatives, never "applies".
      expect(exam.matched).toEqual([])
      expect(exam.status).toBe('printed_alternative')
      expect(exam.named?.map((n) => n.item)).toEqual([e.text])
      // No requirement, term, coverage or applicable hours follow from it.
      expect(r.coveredTerms).toEqual([])
      expect(r.applicableHours).toBe(3) // HIST 1110 only
    })
  }

  it('control: the same alternatives stored as a reviewed structure (any_of) are filled and can cover the term', () => {
    const structured = { any_of: [{ code: 'ENGL 1010' }, { code: 'ENGL 1011' }], credits: '1-4' }
    expect(unresolvedAlternatives(readPlanItem(structured)!)).toBe(false)
    const r = degreeCredit(award('HIST 1110', 'ENGL 1010'), term(structured))
    expect(r.accepted.find((a) => a.course === 'ENGL 1010')).toMatchObject({ status: 'applies', matched: [expect.objectContaining({ code: 'ENGL 1010' })] })
    expect(r.coveredTerms).toEqual([{ term: 1, label: 'Fall' }])
  })

  it('a course awarded in a combination never fills an unresolved row either', () => {
    const r = degreeCredit(award('ENGL 1010 & ENGL 1020'), [{ term_index: 1, label: 'Fall', credit_hours: '15', items: [{ code: 'ENGL 1020', credits: 3 }, 'Elective (ENGL 1010 or 1011)*'] }])
    expect(r.accepted[0]).toMatchObject({ status: 'partly', matched: [expect.objectContaining({ code: 'ENGL 1020' })], named: [expect.objectContaining({ code: 'ENGL 1010', item: 'Elective (ENGL 1010 or 1011)*' })] })
    expect(r.coveredTerms).toEqual([])
  })

  it('a coded row: only its own code is filled; alternatives printed in its title are named, never placed (UTC Clear Path)', () => {
    const row = { code: 'MATH 1130', credits: '3-4', title: 'College Algebra, MATH 1830: Calculus for Mgt., Life, and Social Sciences, or MATH 1950: Calculus w/ Analytic Geometry 1' }
    const alt = degreeCredit(award('HIST 1110', 'MATH 1950'), term(row))
    expect(alt.accepted.find((a) => a.course === 'MATH 1950')).toMatchObject({ status: 'printed_alternative', matched: [], named: [expect.objectContaining({ code: 'MATH 1950' })] })
    expect(alt.coveredTerms).toEqual([])
    expect(alt.applicableHours).toBe(3)
    // Control: the row's own code.
    const own = degreeCredit(award('HIST 1110', 'MATH 1130'), term(row))
    expect(own.accepted.find((a) => a.course === 'MATH 1130')).toMatchObject({ status: 'applies' })
    expect(own.coveredTerms).toEqual([{ term: 1, label: 'Fall' }])
  })

  it('an excluded course is never read as an alternative (JSU, OK State)', () => {
    expect(titleAlternatives('MS 112', 'Precalculus Algebra (or higher excluding MS 204 Mathematics for Business)')).toEqual([])
    expect(titleAlternatives('MATH 1483', 'Mathematical Functions (or Higher, except 1493)')).toEqual([])
  })

  it('a choice option whose alternatives exist only in its wording is never completed; a reviewed option is', () => {
    const block = { text: 'Select one of the following:', options: [{ text: 'ENGL 103 Writing or ENGL 104 Writing Honors' }, { code: 'ENGL 110' }] }
    const r = degreeCredit(award('HIST 1110', 'ENGL 104'), term(block))
    expect(r.accepted.find((a) => a.course === 'ENGL 104')).toMatchObject({ status: 'printed_alternative', matched: [] })
    expect(r.coveredTerms).toEqual([])
    // The same printed option inside any_of, and a school-assigned group that names exactly that option's courses.
    expect(degreeCredit(award('HIST 1110', 'ENGL 104'), term({ any_of: [{ text: 'ENGL 1010 or ENGL 104' }, { code: 'ENGL 110' }] })).coveredTerms).toEqual([])
    expect(degreeCredit(award('HIST 1110', 'ENGL 103 or ENGL 104'), term(block)).coveredTerms).toEqual([])
    // Control: the reviewed option.
    expect(degreeCredit(award('HIST 1110', 'ENGL 110'), term(block)).coveredTerms).toEqual([{ term: 1, label: 'Fall' }])
  })

  it('a course placed in its own row is not also reported as named among alternatives', () => {
    const r = degreeCredit(award('ENGL 1010'), [{ term_index: 1, label: 'Fall', credit_hours: '15', items: [{ code: 'ENGL 1010', credits: 3 }, 'Elective (ENGL 1010 or 1011)*'] }])
    expect(r.accepted[0]).toMatchObject({ status: 'applies' })
    expect(r.accepted[0]!.named).toBeUndefined()
  })

  it('a plain combination in free text counts only when every course is awarded', () => {
    expect(unresolvedAlternatives(readPlanItem('ENGL 1010 and ENGL 1020')!)).toBe(false)
    expect(degreeCredit(award('HIST 1110', 'ENGL 1010'), term('ENGL 1010 and ENGL 1020')).coveredTerms).toEqual([])
    expect(degreeCredit(award('HIST 1110', 'ENGL 1010', 'ENGL 1020'), term('ENGL 1010 and ENGL 1020')).coveredTerms).toEqual([{ term: 1, label: 'Fall' }])
  })

  it('rows that are not unresolved alternatives are unaffected: a single code, a combination, a heading', () => {
    expect(unresolvedAlternatives(readPlanItem('ENGL 1020')!)).toBe(false)
    expect(unresolvedAlternatives(readPlanItem('BIOL 1113& BIOL 1111')!)).toBe(false)
    expect(unresolvedAlternatives(readPlanItem('Semester Two')!)).toBe(false)
  })
})

describe('footnote marks on a row', () => {
  const e = (t: string) => readPlanItem(t)!
  it('cites each note in a combined mark, longest marker first; a mark with no note is reported', () => {
    expect(rowMarks(e('Elective (ENGL 1010 or 1011)*'), ['*'])).toEqual({ cited: ['*'], unexplained: [] })
    expect(rowMarks(e('BUS 2000**+'), ['*', '**', '+'])).toEqual({ cited: ['**', '+'], unexplained: [] })
    expect(rowMarks(e('COMM 2310 Multimedia Journalism* or COMM 2330'), ['*'])).toEqual({ cited: ['*'], unexplained: [] })
    expect(rowMarks(e('Political Science Elective**'), ['*'])).toEqual({ cited: [], unexplained: ['**'] })
    // Right after a digit "**" may be a wildcard ("3**"), so no claim is made either way.
    expect(rowMarks(e('POLS 1010**'), ['*'])).toEqual({ cited: [], unexplained: [] })
    expect(rowMarks(e('Business Elective*+'), ['*'])).toEqual({ cited: ['*'], unexplained: ['+'] })
    expect(rowMarks(e('Political Science Elective†'), ['*'])).toEqual({ cited: [], unexplained: ['†'] })
    // Digit markers count only when the row lists them (UAF), never guessed from text.
    expect(rowMarks(readPlanItem({ code: 'CHEM F105X', footnotes: ['7'] })!, ['7'])).toEqual({ cited: ['7'], unexplained: [] })
    expect(rowMarks(e('MATH 1910 3'), ['3'])).toEqual({ cited: [], unexplained: [] })
    // A symbol that is part of the wording is not a mark.
    expect(rowMarks(e('DSGN 1529 Design + 2D Drawing'), ['*'])).toEqual({ cited: [], unexplained: [] })
    expect(rowMarks(e('History and Humanities GER 300+ level'), ['*'])).toEqual({ cited: [], unexplained: [] })
    expect(rowMarks(e('CSE 130 Introduction to C and C++ Programming'), ['*', '+'])).toEqual({ cited: [], unexplained: [] })
    expect(rowMarks(e('SOC Elective (2** or 3**)'), ['*'])).toEqual({ cited: [], unexplained: [] })
    // A plan that prints no footnotes: no symbol is read as a mark.
    expect(rowMarks(e('Elective (ENGL 1010 or 1011)*'), [])).toEqual({ cited: [], unexplained: [] })
    // Right after a digit, an exact marker is still a citation ("MATH 1910*").
    expect(rowMarks(e('MATH 1910*'), ['*'])).toEqual({ cited: ['*'], unexplained: [] })
    // A mark set off by a space: read at the end of the row or before "or"/"and", only when wholly known (#302 review).
    expect(rowMarks(e('MKTG 311 Marketing (or other approved courses) **'), ['**'])).toEqual({ cited: ['**'], unexplained: [] })
    expect(rowMarks(e('MATH 225 Survey of Calculus *'), ['*'])).toEqual({ cited: ['*'], unexplained: [] })
    expect(rowMarks(e('CS 250 Programming * or CS 251'), ['*'])).toEqual({ cited: ['*'], unexplained: [] })
    expect(rowMarks(e('Humanities Elective †'), ['*'])).toEqual({ cited: [], unexplained: ['†'] })
    expect(rowMarks(e('DSGN 1529 Design + 2D Drawing'), ['+'])).toEqual({ cited: [], unexplained: [] })
    // Footnotes recorded on an option (UAF).
    expect(rowMarks(readPlanItem({ text: 'Select one:', options: [{ code: 'BA F454', footnotes: ['4'] }, { code: 'BA F421' }] })!, ['4'])).toEqual({ cited: ['4'], unexplained: [] })
  })
})
