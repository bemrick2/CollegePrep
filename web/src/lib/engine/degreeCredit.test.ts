import { describe, expect, it } from 'vitest'
import comparison from '../data/demo/comparison-snapshot.json'
import { degreeCredit, parseEquivalent, type PlanTerm } from './degreeCredit'
import { examKey, summarizeSchool, type CreditPolicy, type PlannedExam } from './examCredit'

// UTK's verified records: its AP equivalency table and the Computer Science B.S. term-by-term plan.
const utk = (comparison as unknown as { institutions: { institution_key: string; domains: Record<string, unknown[]> }[] }).institutions.find((i) => i.institution_key === 'utk')!
const policies = utk.domains.credit_policies as unknown as CreditPolicy[]
const plan = (utk.domains.degree_requirements![0] as { rule_details: { terms: PlanTerm[] } }).rule_details.terms
const ap = (name: string, score: number): PlannedExam => ({ family: 'AP', key: examKey('AP', name), name, score })
const check = (exams: PlannedExam[]) => degreeCredit(summarizeSchool(policies, exams).matches, plan)

describe('reading a published course equivalent', () => {
  it('splits ranges, required sets and choices', () => {
    expect(parseEquivalent('MATH 147-148').groups).toEqual([['MATH 147'], ['MATH 148']])
    expect(parseEquivalent('BIOL 101-102 and BIOL 160').groups).toEqual([['BIOL 101'], ['BIOL 102'], ['BIOL 160']])
    expect(['BUS 1XXX', 'ARTH 1XX', 'Elec 1XXX', 'MGT 1XXX (Lower Division)', 'HIST 10XX'].map((t) => parseEquivalent(t).elective)).toEqual([true, true, true, true, true])
    expect(parseEquivalent('MATH 1950').elective).toBe(false)
    expect(parseEquivalent('PHYS 102 or 222 or 231').groups).toEqual([['PHYS 102', 'PHYS 222', 'PHYS 231']])
    expect(parseEquivalent('ART LD (3 credit hours)')).toEqual({ groups: [], elective: true })
  })
})

describe('accepted vs applies to the major vs removes a term (UTK Computer Science)', () => {
  it('accepted is not the same as applies: AP CS A earns COSC 101, which the CS plan does not use', () => {
    const r = check([ap('AP Computer Science A', 4)])
    expect(r.accepted).toEqual([expect.objectContaining({ course: 'COSC 101', status: 'not_in_plan' })])
  })

  it('English places into its plan course; calculus is named only in printed "or" rows, so it is not placed', () => {
    const r = check([ap('AP Calculus BC', 5), ap('AP English Language & Composition', 4)])
    // MATH 147/148 appear only in "MATH 132 or MATH 141 or MATH 147" and "MATH 142 or MATH 148": unresolved rows.
    const calc = r.accepted.find((a) => a.examName === 'AP Calculus BC')!
    expect(calc).toMatchObject({ status: 'printed_alternative', matched: [] })
    expect(calc.named!.map((m) => [m.code, m.term, m.item])).toEqual([
      ['MATH 147', 1, 'MATH 132 or MATH 141 or MATH 147'],
      ['MATH 148', 2, 'MATH 142 or MATH 148'],
    ])
    expect(r.accepted.find((a) => a.examName.startsWith('AP English'))!.matched[0]).toMatchObject({ code: 'ENGL 101', term: 1 })
    // English applies, but no hours are published, so nothing can be counted in dollars.
    expect(r.applicableHours).toBe(0)
    expect(r.applicableWithoutHours).toBe(1)
  })

  it('elective-only credit is accepted with hours but is not shown to apply to the major', () => {
    const r = check([ap('AP Art History', 4)])
    expect(r.accepted[0]).toMatchObject({ status: 'elective_only', hours: 3 })
    expect(r.acceptedHours).toBe(3)
    expect(r.applicableHours).toBe(0)
  })

  it('no plan term is shown as removed unless every one of its items is covered', () => {
    const r = check([ap('AP Calculus BC', 5), ap('AP English Language & Composition', 4), ap('AP Computer Science A', 5), ap('AP Physics C - Mechanics', 5)])
    expect(r.coveredTerms).toEqual([])
  })

  it('a whole covered term is reported (synthetic plan)', () => {
    const terms: PlanTerm[] = [
      { term_index: 1, label: 'Term 1', credit_hours: '15', items: ['MATH 147', { any_of: [{ code: 'ENGL 101' }, { code: 'ENGL 131' }] }] },
      { term_index: 2, label: 'Term 2', credit_hours: '15', items: ['MATH 148', 'COSC 202'] },
    ]
    const r = degreeCredit(summarizeSchool(policies, [ap('AP Calculus BC', 5), ap('AP English Language & Composition', 5)]).matches, terms)
    expect(r.coveredTerms).toEqual([{ term: 1, label: 'Term 1' }])
  })

  it('different courses at the same score depend on which row applies to the student', () => {
    // UTK lists two outcomes for a 4 on Physics C E&M: PHYS 136, or one of PHYS 102/222/231.
    const exams = [ap('AP Physics C - Electricity & Magnetism', 4)]
    const r = degreeCredit(summarizeSchool(policies, exams).matches, [{ term_index: 1, items: ['PHYS 136'] }])
    expect(r.accepted[0]).toMatchObject({ status: 'school_assigns', course: 'PHYS 136; or PHYS 102 or 222 or 231' })
    // A choice the school makes among several courses applies only if every option fits the same plan item.
    const choice = degreeCredit(summarizeSchool(policies, [ap('AP Physics C - Electricity & Magnetism', 5)]).matches, [{ term_index: 1, items: ['PHYS 136'] }])
    expect(choice.accepted[0]!.status).toBe('applies')
  })
})
