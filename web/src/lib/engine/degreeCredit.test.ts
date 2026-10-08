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

  it('calculus and English place into plan courses, but the table publishes no hours for them', () => {
    const r = check([ap('AP Calculus BC', 5), ap('AP English Language & Composition', 4)])
    const calc = r.accepted.find((a) => a.examName === 'AP Calculus BC')!
    expect(calc.status).toBe('applies')
    expect(calc.matched.map((m) => [m.code, m.term])).toEqual([
      ['MATH 147', 1],
      ['MATH 148', 2],
    ])
    expect(r.accepted.find((a) => a.examName.startsWith('AP English'))!.matched[0]).toMatchObject({ code: 'ENGL 101', term: 1 })
    // Applies, but no hours are published, so nothing can be counted in dollars.
    expect(r.applicableHours).toBe(0)
    expect(r.applicableWithoutHours).toBe(2)
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
      { term_index: 1, label: 'Term 1', items: ['MATH 147', 'ENGL 101 or ENGL 131'] },
      { term_index: 2, label: 'Term 2', items: ['MATH 148', 'COSC 202'] },
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
