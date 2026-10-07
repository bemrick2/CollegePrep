import { describe, expect, it } from 'vitest'
import uafData from './__fixtures__/uaf-2026-27.json'
import { codesInText, entryCodes, readPlanItem, readTermItems, type PlanTermLike } from './planItems'
import { degreeCredit } from './degreeCredit'
import { examKey, summarizeSchool, type CreditPolicy } from './examCredit'
import { schoolFit } from './programFit'

const uaf = uafData as unknown as { domains: { degree_requirements: { program_key: string; requirement_key: string; rule_details: { terms: PlanTermLike[] } }[]; academic_programs: unknown[] } }
const plans = uaf.domains.degree_requirements

describe('reading plan items in every stored format (#171)', () => {
  it('strings, courseleaf_plan/v1, courseleaf_plangrid/v1 and any_of, keeping course, credits and notes', () => {
    expect(readPlanItem('MATH 132 or MATH 141')).toMatchObject({ text: 'MATH 132 or MATH 141', code: null, credits: null, choices: [] })
    // courseleaf_plan/v1 (NJIT, Oregon)
    expect(readPlanItem({ code: 'AD 150', credits: 3, title: 'Color and Composition' })).toMatchObject({ text: 'AD 150 Color and Composition', code: 'AD 150', title: 'Color and Composition', credits: 3 })
    expect(readPlanItem({ code: 'ACTG 450', credits: 4, milestone: 'Attend Meet the Firms', title: 'Advanced Financial Accounting' })).toMatchObject({ code: 'ACTG 450', credits: 4, milestone: 'Attend Meet the Firms' })
    expect(readPlanItem({ credits: 4, milestone: 'Consider using electives toward a minor', text: 'Elective course' })).toMatchObject({ text: 'Elective course', code: null, credits: 4 })
    // A text row printed with credits only stays a row (credits kept) rather than vanishing.
    expect(readPlanItem({ credits: 2, text: '' })).toMatchObject({ text: '', credits: 2 })
    expect(readPlanItem({ text: '' })).toBeNull()
    // courseleaf_plangrid/v1 (UAF): footnotes, recommended options, "complete one of"
    expect(readPlanItem({ code: 'CHEM F105X', credits: 4, footnotes: ['7'] })).toMatchObject({ code: 'CHEM F105X', credits: 4, footnotes: ['7'] })
    const choice = readPlanItem({ credits: 3, footnotes: ['1'], options: [{ code: 'WRTG F211X' }, { code: 'WRTG F212X', recommended: true }], text: 'Complete one of the following:' })!
    expect(choice).toMatchObject({ text: 'Complete one of the following:', credits: 3, footnotes: ['1'] })
    expect(choice.choices.map((c) => [c.code, c.recommended])).toEqual([['WRTG F211X', false], ['WRTG F212X', true]])
    expect(entryCodes(choice)).toEqual(['WRTG F211X', 'WRTG F212X'])
    // any_of (UTC)
    const any = readPlanItem({ any_of: [{ code: 'MATH 1530', title: 'Introductory Statistics', credits: 3 }, { code: 'DATA 2130', title: 'Statistics for Business', credits: 3 }] })!
    expect(any.text).toBe('MATH 1530 Introductory Statistics or DATA 2130 Statistics for Business')
    expect(entryCodes(any)).toEqual(['MATH 1530', 'DATA 2130'])
    // Anything unrecognised is skipped, never thrown on.
    expect(readPlanItem(42)).toBeNull()
    expect(readPlanItem(null)).toBeNull()
  })

  it('course codes as UAF prints them, subjects carried forward', () => {
    expect(codesInText('COM F121X, F131X, or F141X')).toEqual(['COM F121X', 'COM F131X', 'COM F141X'])
    expect(codesInText('EF 142 or EF 151 or EF 157')).toEqual(['EF 142', 'EF 151', 'EF 157'])
    expect(codesInText('CPSC 4995R Thesis')).toEqual(['CPSC 4995R'])
    expect(codesInText('Degree Requirement - Alaska Native-themed')).toEqual([])
  })

  it('every stored UAF roadmap reads in full: no item lost, credits as printed', () => {
    let raw = 0
    let read = 0
    for (const p of plans)
      for (const t of p.rule_details.terms) {
        raw += (t.items ?? []).filter((x) => (typeof x === 'string' ? x.trim() !== '' : !!x && Object.values(x as object).some((v) => v !== '' && v != null))).length
        read += readTermItems(t).length
      }
    expect(plans.length).toBe(140)
    expect(read).toBe(raw)
    const me = plans.find((p) => p.requirement_key === 'roadmap-aerospace-concentration')!
    const fall = readTermItems(me.rule_details.terms[0]!)
    expect(fall.map((e) => [e.code ?? e.text, e.credits])).toEqual([
      ['CHEM F105X', 4],
      ['COM F121X, F131X, or F141X', 3],
      ['ES F100X', 3],
      ['MATH F251X', 4],
      ['WRTG F111X', 3],
    ])
  })
})

describe('the two modules that read plans', () => {
  it('degree credit matches UAF course codes, with an option list as any-of, and keeps the plan credits', () => {
    // A synthetic equivalency table (UAF publishes none yet) to exercise matching against a real UAF roadmap.
    const policies: CreditPolicy[] = [
      {
        policy_kind: 'AP',
        equivalencies: [
          { exam_or_course_code: 'AP-CALCAB', exam_or_course_name: 'AP Calculus AB', minimum_score: '4', institution_course_equivalent: 'MATH F251X', credits_awarded: 4 },
          { exam_or_course_code: 'AP-ENGLANG', exam_or_course_name: 'AP English Language and Composition', minimum_score: '4', institution_course_equivalent: 'WRTG F212X', credits_awarded: 3 },
        ],
      },
    ]
    const plan = plans.find((p) => p.requirement_key === 'roadmap-aerospace-concentration')!.rule_details.terms
    const exams = [
      { family: 'AP' as const, key: examKey('AP', 'AP Calculus AB'), name: 'AP Calculus AB', score: 5 },
      { family: 'AP' as const, key: examKey('AP', 'AP English Language and Composition'), name: 'AP English Language and Composition', score: 4 },
    ]
    const r = degreeCredit(summarizeSchool(policies, exams).matches, plan)
    const calc = r.accepted.find((a) => a.examName.includes('Calculus'))!
    expect(calc).toMatchObject({ status: 'applies', course: 'MATH F251X' })
    expect(calc.matched[0]).toMatchObject({ code: 'MATH F251X', term: 1, label: 'First Year Fall', credits: 4 })
    const wrtg = r.accepted.find((a) => a.examName.includes('English'))!
    expect(wrtg.status).toBe('applies')
    expect(wrtg.matched[0]).toMatchObject({ code: 'WRTG F212X', term: 2, credits: 3 })
  })

  it('program fit finds first-year courses shared by UAF engineering roadmaps', () => {
    const fit = schoolFit(uaf.domains as never, [
      { kind: 'major', key: 'mechanical-eng' },
      { kind: 'major', key: 'electrical-eng' },
    ])
    expect(fit.verifiedCount).toBe(2)
    expect(fit.sharedFirstYear?.courses).toEqual(expect.arrayContaining(['MATH F251X', 'CHEM F105X']))
    expect(fit.sharedFirstYear?.courses.every((c) => /^[A-Z]{2,5} F?\d{3,4}[A-Z]?$/.test(c))).toBe(true)
  })
})
