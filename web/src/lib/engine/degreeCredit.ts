import type { ExamMatch } from './examCredit'
import { COURSE_NUMBER, entryCodes, readTermItems, scanCodes, type PlanTermLike } from './planItems'

/**
 * Three different questions about credit a student brings, answered only from verified records:
 *
 *  1. Accepted: the school's own published table awards credit for the score (examCredit.ts).
 *  2. Applies: the awarded course appears in the selected major's verified term-by-term degree plan.
 *  3. Removes a term: every item of a whole plan term is covered by awarded courses.
 *
 * (2) and (3) are checked course code by course code. Anything we cannot show (no plan on file, elective-only
 * credit, a course the school assigns from several options) is reported as unknown, never assumed.
 */

/** "MATH 147-148", "PHYS 102 or 222 or 231", "BIOL 101-102 and BIOL 160" -> required groups of alternatives. */
export function parseEquivalent(text: string | null | undefined): { groups: string[][]; elective: boolean } {
  const t = (text ?? '').toUpperCase()
  const groups: string[][] = []
  for (const part of t.split(/\s+AND\s+|;|,(?![^(]*\))/)) {
    let subject: string | null = null
    const alts: string[] = []
    const range: string[] = []
    const re = new RegExp(`(?:\\b(?!OR\\b|AND\\b|WITH\\b)([A-Z]{2,5}))?\\s*(${COURSE_NUMBER})\\b(?:\\s*[-–]\\s*(${COURSE_NUMBER})\\b)?`, 'g')
    for (const m of part.matchAll(re)) {
      if (m[1]) subject = m[1]
      if (!subject) continue
      if (m[3]) range.push(`${subject} ${m[2]}`, `${subject} ${m[3]}`)
      else alts.push(`${subject} ${m[2]}`)
    }
    // A range (101-102) means both courses; "A or B" means one of them.
    for (const r of range) groups.push([r])
    if (alts.length) {
      if (/\bOR\b|\//.test(part)) groups.push(alts)
      else for (const a of alts) groups.push([a])
    }
  }
  return { groups, elective: groups.length === 0 && /\b(LD|UD|ELECTIVE|ELEC)\b/.test(t) }
}

/** A plan term as stored; items may be strings or structured entries (see planItems.ts). */
export type PlanTerm = PlanTermLike

interface PlanItem {
  term: number
  label: string
  text: string
  /** As printed; null when the plan prints none. */
  credits: number | string | null
  /** Any one of these codes satisfies the item. */
  any: string[]
  /** Or all codes of one of these combinations ("CHEM 102+103"). */
  combos: string[][]
}

function planItems(terms: PlanTerm[]): PlanItem[] {
  return terms.flatMap((t, i) =>
    readTermItems(t).map((e) => {
      const base = { term: t.term_index ?? i + 1, label: t.label ?? `Term ${t.term_index ?? i + 1}`, text: e.choices.length ? `${e.text} ${e.choices.map((c) => c.text).join(' / ')}` : e.text, credits: e.credits }
      // A structured course, or a choice among options: any one of its codes.
      if (e.code || e.choices.length) return { ...base, any: entryCodes(e), combos: [] }
      // Free text: "A or B" is any one; "CHEM 102+103" is a combination that counts only when all were awarded.
      const combos: string[][] = []
      const any: string[] = []
      let subject: string | null = null
      for (const seg of e.text.toUpperCase().split(/[,/]|\bOR\b/)) {
        const scan = scanCodes(seg, subject)
        subject = scan.subject
        const codes = scan.codes
        if (seg.includes('+') && codes.length > 1) combos.push(codes)
        else any.push(...codes)
      }
      return { ...base, any, combos }
    }),
  )
}

export type Applicability = 'applies' | 'partly' | 'elective_only' | 'not_in_plan' | 'school_assigns' | 'no_course'

export interface ExamApplicability {
  examName: string
  course: string | null
  /** Credit hours from the school's table; null when not published. */
  hours: number | null
  status: Applicability
  /** Where the credit lands in the plan; credits are the plan item's, as printed. */
  matched: { code: string; term: number; label: string; item: string; credits: number | string | null }[]
}

export interface DegreeCreditResult {
  /** Exams whose score earns credit in the school's table. */
  accepted: ExamApplicability[]
  /** Hours accepted per the table (published hours only). */
  acceptedHours: number
  /** Hours for exams whose every awarded course is in the plan (published hours only). */
  applicableHours: number
  /** Exams that apply but whose table row publishes no hours. */
  applicableWithoutHours: number
  /** Plan terms whose every item is covered by awarded courses. */
  coveredTerms: { term: number; label: string }[]
}

/**
 * Checks earned exam credit against one program's verified plan. `matches` comes from summarizeSchool/matchExam;
 * only 'qualifies' rows count. Each plan item is used once.
 */
export function degreeCredit(matches: ExamMatch[], terms: PlanTerm[]): DegreeCreditResult {
  const items = planItems(terms)
  const used = new Set<PlanItem>()
  const earnedCodes = new Set<string>()
  const accepted: ExamApplicability[] = []

  /** Matches one published course equivalent against the plan, recording into `taken`. */
  const evaluate = (course: string | null, taken: Set<PlanItem>) => {
    const { groups, elective } = parseEquivalent(course)
    const matched: ExamApplicability['matched'] = []
    const codes: string[] = []
    if (!groups.length) return { status: (elective ? 'elective_only' : 'no_course') as Applicability, matched, codes }
    let anyAssigned = false
    let hit = 0
    for (const g of groups) {
      if (g.length > 1) {
        // The school assigns one of several courses: it applies only if every option fits the same item.
        const fit = items.find((it) => !taken.has(it) && g.every((c) => it.any.includes(c)))
        if (fit) {
          taken.add(fit)
          matched.push({ code: g.join(' or '), term: fit.term, label: fit.label, item: fit.text, credits: fit.credits })
          hit++
        } else anyAssigned = true
        continue
      }
      const code = g[0]!
      codes.push(code)
      const it = items.find((x) => !taken.has(x) && x.any.includes(code))
      if (it) {
        taken.add(it)
        matched.push({ code, term: it.term, label: it.label, item: it.text, credits: it.credits })
        hit++
      }
    }
    const status: Applicability = hit === groups.length ? 'applies' : hit > 0 ? 'partly' : anyAssigned ? 'school_assigns' : 'not_in_plan'
    return { status, matched, codes }
  }

  for (const m of matches.filter((x) => x.status === 'qualifies')) {
    const known = m.earned.map((t) => t.credits).filter((c): c is number => c != null)
    const hours = known.length === m.earned.length && known.length ? Math.min(...known) : null
    const courses = [...new Set(m.earned.map((t) => t.course))]
    if (courses.length > 1) {
      // Several rows at the same score with different courses (often by program or admit term): which one
      // applies to this student isn't on file. It applies only if every row does.
      const all = courses.map((c) => evaluate(c, new Set(used)))
      if (!all.every((r) => r.status === 'applies')) {
        accepted.push({ examName: m.exam.name, course: courses.join('; or '), hours, status: 'school_assigns', matched: [] })
        continue
      }
    }
    const r = evaluate(courses[0] ?? null, used)
    for (const c of r.codes) earnedCodes.add(c)
    accepted.push({ examName: m.exam.name, course: courses[0] ?? null, hours, status: r.status, matched: r.matched })
  }

  // Combination items ("CHEM 102+103") count when every course of one combination was awarded.
  for (const it of items)
    if (!used.has(it) && it.combos.some((c) => c.every((code) => earnedCodes.has(code)))) used.add(it)

  const byTerm = new Map<number, PlanItem[]>()
  for (const it of items) byTerm.set(it.term, [...(byTerm.get(it.term) ?? []), it])
  const coveredTerms = [...byTerm.entries()].filter(([, its]) => its.length > 0 && its.every((x) => used.has(x))).map(([term, its]) => ({ term, label: its[0]!.label }))

  return {
    accepted,
    acceptedHours: accepted.reduce((s, a) => s + (a.hours ?? 0), 0),
    applicableHours: accepted.filter((a) => a.status === 'applies').reduce((s, a) => s + (a.hours ?? 0), 0),
    applicableWithoutHours: accepted.filter((a) => a.status === 'applies' && a.hours == null).length,
    coveredTerms,
  }
}
