// #230: the plan reader against representative stored plans (Deep Dive's list), read straight from data/.
import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { describe, expect, it } from 'vitest'
import { codesInText, entryCodes, isHeadingTerm, planTerms, readPlanItem, type PlanTermLike } from '../src/lib/engine/planItems'
import { degreeCredit } from '../src/lib/engine/degreeCredit'
import { buildRoadmap } from '../src/lib/engine/planning/roadmap'

type Rec = { program_key: string; requirement_key: string; requirement_kind: string; verification_status: string; rule_details: { source_section?: string; rule_text?: string; terms: PlanTermLike[] } }
const data = (inst: string): Rec[] => JSON.parse(readFileSync(resolve(__dirname, `../../data/institutions/${inst}/degree_requirements/2026-27.json`), 'utf8')).records
const plan = (inst: string, program: string, key?: string) => {
  const r = data(inst).find((x) => x.requirement_kind === 'program_plan' && x.program_key.includes(program) && (!key || x.requirement_key === key))
  if (!r) throw new Error(`no plan ${inst}/${program}`)
  return r
}

describe('item shapes (#230)', () => {
  it('splits pipe strings into code, title and credits, as printed', () => {
    expect(readPlanItem('MGMT 4010 | Total Rewards | 3')).toMatchObject({ kind: 'course', code: 'MGMT 4010', title: 'Total Rewards', credits: 3 })
    expect(readPlanItem('GER Elective | 3')).toMatchObject({ kind: 'text', code: null, text: 'GER Elective', credits: 3 })
    expect(readPlanItem('CIS 2166 | Mathematical Concepts in Computing II')).toMatchObject({ code: 'CIS 2166', title: 'Mathematical Concepts in Computing II', credits: null })
    expect(readPlanItem('1st semester L&S Language Other than English | 3-5')).toMatchObject({ kind: 'text', credits: '3-5' })
    expect(readPlanItem('Applied Lessons | 1.5')).toMatchObject({ credits: '1.5' })
    // Oregon's four parts: codes | titles | milestone | credits.
    const or = readPlanItem('WR 122Zor WR 123 | Composition II or College Composition III | Complete writing requirement | 4')!
    expect(or).toMatchObject({ kind: 'text', code: null, title: 'Composition II or College Composition III', milestone: 'Complete writing requirement', credits: 4 })
    expect(entryCodes(or)).toEqual(['WR 122Z', 'WR 123'])
  })

  it('finds both codes in joined alternatives printed without a space', () => {
    expect(codesInText('INM 101or VOK 101')).toEqual(['INM 101', 'VOK 101'])
    expect(codesInText('MATH 1113and MATH 1114')).toEqual(['MATH 1113', 'MATH 1114'])
    // A trailing letter is still part of the number.
    expect(codesInText('CPSC 4995R Thesis')).toEqual(['CPSC 4995R'])
  })

  it('keeps row notes and milestone rows; marks inline headings and printed subtotals', () => {
    expect(readPlanItem({ credits: 3, note: 'Complete any elective course.', text: 'EHS 120 Total Credits (Elective or Other Degree Requirement)' })).toMatchObject({ kind: 'text', note: 'Complete any elective course.', credits: 3 })
    expect(readPlanItem({ text: 'BFA Application' })).toMatchObject({ kind: 'text', text: 'BFA Application', credits: null })
    expect(readPlanItem('Semester 2')!.kind).toBe('heading')
    expect(readPlanItem('Sophomore')!.kind).toBe('heading')
    expect(readPlanItem('Credit Hours | 15')).toMatchObject({ kind: 'subtotal', credits: 15 })
    expect(readPlanItem('Semester Credit Hours | 15-16')).toMatchObject({ kind: 'subtotal', credits: '15-16' })
    // Only exact subtotal wording: a requirement that mentions credits stays a requirement.
    expect(readPlanItem('Upper-division business elective courses | 8')!.kind).toBe('text')
  })
})

describe('representative stored plans (#230)', () => {
  it('UWM Computer Science: year rows are headings, 8 real terms, credits as printed', () => {
    const p = plan('uwm', 'computer-science')
    const terms = planTerms(p.rule_details.terms)
    expect(p.rule_details.terms.filter(isHeadingTerm).length).toBeGreaterThan(0)
    expect(terms.every((t) => t.entries.length > 0)).toBe(true)
    expect(terms.length).toBe(p.rule_details.terms.filter((t) => !isHeadingTerm(t)).length)
    expect(terms[0]).toMatchObject({ number: 1, group: 'Year 1', creditHours: '14' })
    expect(terms[0]!.entries[0]).toMatchObject({ code: 'COMPSCI 250', title: 'Introductory Computer Programming', credits: 4 })
  })

  it('West Chester Jazz Performance: 8 terms, not 12; decimal hours and joined applied-lesson codes kept', () => {
    const p = plan('wcupa', 'jazz')
    expect(p.rule_details.terms.length).toBe(12)
    const terms = planTerms(p.rule_details.terms)
    expect(terms.length).toBe(8)
    expect(terms.map((t) => t.group)).toEqual(['Year One', 'Year One', 'Year Two', 'Year Two', 'Year Three', 'Year Three', 'Year Four', 'Year Four'])
    expect(terms[1]!.creditHours).toBe('13.5')
    const applied = terms[0]!.entries.find((e) => e.text.startsWith('INM 131'))!
    expect(entryCodes(applied)).toEqual(expect.arrayContaining(['INM 131', 'VOK 131']))
    expect(terms.some((t) => t.multiTerm)).toBe(false)
  })

  it('Texas A&M Agribusiness: First Year rows are headings; every course code and title kept', () => {
    const p = plan('tamu', 'agribusiness')
    const terms = planTerms(p.rule_details.terms)
    expect(terms[0]).toMatchObject({ label: 'Fall', group: 'First Year' })
    expect(terms[0]!.entries[0]).toMatchObject({ code: 'AGEC 105', credits: 3 })
    expect(terms[0]!.entries.find((e) => e.text.startsWith('American History'))).toMatchObject({ kind: 'text', credits: 3 })
  })

  it('UNL Finance: four titled plans, each named by its source_section, and a picker can choose one', () => {
    const recs = data('admissions').filter((r) => r.program_key === 'finance-bachelor-of-science-in-business-administration' && r.requirement_kind === 'program_plan')
    expect(recs.length).toBe(4)
    expect(recs.map((r) => r.rule_details.source_section)).toEqual(expect.arrayContaining(['Finance - General', 'Finance - Investments']))
    const comparison = { institution_key: 'unl', found: true, institution: { display_name: 'UNL' }, academic_year: '2026-27', domains: { degree_requirements: recs, academic_programs: [], credit_policies: [] }, missing_domains: [], can_offer_paid_addon: false }
    const profile = { gradeLevel: null, graduationYear: null, homeState: null, interests: [], exams: [], livingArrangement: null }
    const first = buildRoadmap({ comparison: comparison as never, programKey: recs[0]!.program_key, profile })
    expect(first.plans.map((x) => x.title)).toEqual(recs.map((r) => r.rule_details.source_section))
    expect(first.plan.value?.title).toBe(recs[0]!.rule_details.source_section)
    const inv = buildRoadmap({ comparison: comparison as never, programKey: recs[0]!.program_key, planKey: 'plan-finance-investments', profile })
    expect(inv.planKey).toBe('plan-finance-investments')
    expect(inv.plan.value?.title).toBe('Finance - Investments')
    expect(inv.plan.value?.terms.every((t) => t.rows.length > 0)).toBe(true)
  })

  it('UNL Advertising: notes and milestone rows survive, and every stored row is read', () => {
    const p = plan('admissions', 'advertising-public-relations-bachelor-of-journalism')
    const raw = p.rule_details.terms.flatMap((t) => t.items ?? []).length
    const read = planTerms(p.rule_details.terms).flatMap((t) => t.entries).length
    expect(read).toBe(raw)
  })
})

describe('term counts and coverage (#230)', () => {
  it('a year printed as one block is never reported as one covered term', () => {
    const terms: PlanTermLike[] = [{ term_index: 1, label: 'First Year', items: ['First Semester', { code: 'ENGL 101', credits: 3 }, 'Second Semester', { code: 'ENGL 102', credits: 3 }] }]
    expect(planTerms(terms)[0]!.multiTerm).toBe(true)
    const m = { status: 'qualifies', exam: { name: 'AP English' }, earned: [{ course: 'ENGL 101 and ENGL 102', credits: 6, minimumText: '4' }] }
    const r = degreeCredit([m as never], terms)
    expect(r.accepted[0]!.status).toBe('applies')
    expect(r.coveredTerms).toEqual([])
  })

  it('a heading term is not a term to cover, and inline subtotals are not requirements', () => {
    const terms: PlanTermLike[] = [
      { term_index: 1, label: 'Year One', items: [] },
      { term_index: 2, label: 'Fall', credit_hours: '15', items: [{ code: 'ENGL 101', credits: 3 }, 'Credit Hours | 15'] },
    ]
    const m = { status: 'qualifies', exam: { name: 'AP English' }, earned: [{ course: 'ENGL 101', credits: 3, minimumText: '4' }] }
    expect(degreeCredit([m as never], terms).coveredTerms).toEqual([{ term: 2, label: 'Fall' }])
  })

  it('an ampersand combination counts only when both courses were awarded', () => {
    const terms: PlanTermLike[] = [{ term_index: 1, label: 'Fall', items: ['BIOL 1113& BIOL 1111 | Introductory Biology and Laboratory | 4'] }]
    const one = { status: 'qualifies', exam: { name: 'AP Biology' }, earned: [{ course: 'BIOL 1113', credits: 3, minimumText: '3' }] }
    expect(degreeCredit([one as never], terms).coveredTerms).toEqual([])
  })

  it('a combination row: the exam fills a course in the plan, but the row is done only when every course is awarded', () => {
    const terms: PlanTermLike[] = [{ term_index: 1, label: 'Fall', credit_hours: '15', items: ['PHYS 2325& PHYS 2125 | University Physics I and Lab | 4'] }]
    const one = { status: 'qualifies', exam: { name: 'AP Physics C: Mechanics' }, earned: [{ course: 'PHYS 2325', credits: 3, minimumText: '4' }] }
    const r = degreeCredit([one as never], terms)
    expect(r.accepted[0]!.status).toBe('applies')
    expect(r.coveredTerms).toEqual([])
  })
})

describe('review findings on stored plans (#242)', () => {
  it('UNO Geology: the 5-credit Summer term is never a covered term', () => {
    const p = plan('unomaha', 'geology')
    const summer = planTerms(p.rule_details.terms).find((t) => /^summer/i.test(t.label))!
    expect(summer.notChecked).toBe('short_term')
    const m = { status: 'qualifies', exam: { name: 'CLEP Calculus' }, earned: [{ course: 'MATH 1950', credits: 5, minimumText: '50' }] }
    expect(degreeCredit([m as never], p.rule_details.terms).coveredTerms).toEqual([])
  })

  it('a quarter-calendar plan (Oregon) never reports a covered term', () => {
    const p = data('uoregon').find((r) => r.requirement_kind === 'program_plan' && r.rule_details.terms.some((t) => /winter/i.test(t.label ?? '')))!
    expect(planTerms(p.rule_details.terms).every((t) => t.notChecked !== null)).toBe(true)
  })

  it('a "First Year" term whose rows start with its one semester header is that semester, not a year block', () => {
    const t = planTerms([{ term_index: 1, label: 'First Year', items: ['Fall Semester | Semester Credit Hours', 'ENGL 1101 | Composition | 3'] }])[0]!
    expect(t).toMatchObject({ label: 'Fall Semester', group: 'First Year', multiTerm: false })
    expect(planTerms([{ term_index: 1, label: 'Year 2', items: ['Hours | 14', 'Semester 2', 'MATH 2413 | Calculus | 4'] }])[0]!.multiTerm).toBe(true)
  })

  it('credit formats as printed, and odd rows', () => {
    expect(readPlanItem('CORE 1000 | Ignite First Year Seminar | 2 or 3')).toMatchObject({ code: 'CORE 1000', credits: '2 or 3', milestone: null })
    expect(readPlanItem('Select 15+ Credits | 15+')).toMatchObject({ text: 'Select 15+ Credits', credits: '15+' })
    expect(readPlanItem('Elective | .5')!.credits).toBe('.5')
    expect(readPlanItem('|')).toBeNull()
    expect(readPlanItem('Total Units | 120')!.kind).toBe('subtotal')
    expect(readPlanItem('Language 113 | 4')!.code).toBeNull()
    expect(readPlanItem('Semester Seven')!.kind).toBe('heading')
  })

  it('splits joined "or" in free text for credit too', () => {
    const terms: PlanTermLike[] = [{ term_index: 1, label: 'Fall', credit_hours: '15', items: ['INM 101or VOK 101'] }]
    const m = { status: 'qualifies', exam: { name: 'X' }, earned: [{ course: 'VOK 101', credits: 1, minimumText: '3' }] }
    expect(degreeCredit([m as never], terms).coveredTerms).toEqual([{ term: 1, label: 'Fall' }])
  })

  it('a plan-total row in the last semester does not make it a year block (JSU)', () => {
    const t = planTerms([{ term_index: 8, label: 'Spring', items: ['BIOL 4990 | Senior Seminar | 3', 'Hours | 12', 'Total Hours | 120'] }])[0]!
    expect(t.multiTerm).toBe(false)
  })

  it('a quarter label inside a longer heading still marks a quarter calendar (EOU)', () => {
    const ts = planTerms([
      { term_index: 1, label: 'TYPICAL THIRD YEAR CURRICULUM — Fall', items: [{ code: 'BA 303', credits: 4 }, { code: 'BA 312', credits: 4 }, { code: 'BA 321', credits: 4 }] },
      { term_index: 2, label: 'TYPICAL THIRD YEAR CURRICULUM — Winter', items: [{ code: 'BA 304', credits: 4 }, { code: 'BA 313', credits: 4 }, { code: 'BA 322', credits: 4 }] },
    ])
    expect(ts.map((t) => t.notChecked)).toEqual(['quarter_calendar', 'short_term'])
  })

  it('a printed "choose N" block: shown with its count, done only when N listed courses are awarded (Deep Dive, #230)', () => {
    const block = { choose: 2, text: 'Select two of the following:', credits: 6, options: [{ code: 'ANTH 376' }, { code: 'BIOL 350' }, { code: 'STAT 201' }] }
    expect(readPlanItem(block)).toMatchObject({ kind: 'choice', choose: 2, credits: 6 })
    expect(readPlanItem({ ...block, choose: 9 })!.choose).toBe(1) // a count larger than the options isn't trusted
    expect(readPlanItem({ ...block, choose: undefined })!.choose).toBe(1)
    const terms: PlanTermLike[] = [{ term_index: 1, label: 'Fall', credit_hours: '15', items: [block] }]
    const exam = (course: string) => ({ status: 'qualifies', exam: { name: course }, earned: [{ course, credits: 3, minimumText: '3' }] })
    const one = degreeCredit([exam('BIOL 350') as never], terms)
    expect(one.accepted[0]!.status).toBe('applies')
    expect(one.coveredTerms).toEqual([])
    expect(degreeCredit([exam('BIOL 350') as never, exam('STAT 201') as never], terms).coveredTerms).toEqual([{ term: 1, label: 'Fall' }])
  })
})

