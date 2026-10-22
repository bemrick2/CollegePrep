import type { ExamMatch } from './examCredit'
import { COURSE_NUMBER, entryCodes, isRequirement, planTerms, scanCodes, type PlanEntry, type PlanTermLike } from './planItems'

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
  // "LD", "UD", "Elective", and placeholder numbers such as "BUS 1XXX", "ARTH 1XX" or "ELEC 1XXX" are elective credit.
  return { groups, elective: groups.length === 0 && /\b(LD|UD|ELECTIVE|ELEC)\b|\b[A-Z]{2,5}\s*\d{0,3}X{1,3}\b/.test(t) }
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
  /**
   * "Select two of the following" (#230): done only when `n` different options are fully awarded. Each option is the
   * codes that satisfy it (all of them, e.g. a lecture and its lab), and no code counts for two options or two rows.
   */
  pick: { options: Option[]; n: number } | null
  /** The term is a regular full-time semester (planTerms' notChecked is null); only such terms can be "covered". */
  checked: boolean
}

/**
 * One option of a choice block, as the courses it needs: each inner list is one requirement, met by any one of its
 * codes. A combination ("CHEM 101 & CHEM 101L") needs every course, so each is its own requirement; anything else
 * ("ENGL 221/MODL 221", "BA F454 or F421", a nested any_of) is one requirement with its alternatives.
 */
type Option = string[][]
function optionOf(o: PlanEntry): Option {
  const codes = entryCodes(o)
  if (!codes.length) return []
  return !o.code && /[+&]|\bAND\b/i.test(o.text) ? codes.map((c) => [c]) : [codes]
}
/** The block's printed count, or one written in its text ("Complete two of the following:") when none is stored. */
const NUMBER: Record<string, number> = { two: 2, three: 3, four: 4, five: 5 }
function printedCount(e: PlanEntry): number {
  if (e.choose > 1) return e.choose
  const m = /\b(?:complete|select|choose|take)\s+(two|three|four|five|[2-5])\b/i.exec(e.text)
  return m ? (NUMBER[m[1]!.toLowerCase()] ?? Number(m[1])) : 1
}

function planItems(terms: PlanTerm[]): PlanItem[] {
  // Heading terms have no rows; inline headings and printed subtotals aren't requirements (#230).
  return planTerms(terms).flatMap((t) =>
    t.entries.filter(isRequirement).map((e) => {
      const base = { term: t.termIndex, label: t.label, checked: t.notChecked === null, text: e.choices.length ? `${e.text} ${e.choices.map((c) => c.text).join(' / ')}` : e.text, credits: e.credits }
      // A structured course, or a choice among options: any one of its codes.
      // Any choice block ("any one of", "choose N of"): done only when N whole options are awarded with unused courses.
      if (e.choices.length) return { ...base, any: [], combos: [], pick: { options: e.choices.map(optionOf).filter((o) => o.length > 0), n: printedCount(e) } }
      if (e.code || e.choices.length) return { ...base, any: entryCodes(e), combos: [], pick: null }
      // Free text: "A or B" is any one; "CHEM 102+103", "BIOL 1113& BIOL 1111" and "A and B" are combinations that
      // count only when all were awarded.
      const combos: string[][] = []
      const any: string[] = []
      let subject: string | null = null
      for (const seg of e.text.toUpperCase().split(/[,/]|\bOR\b|(?<=\d[A-Z]?)OR\b/)) {
        const scan = scanCodes(seg, subject)
        subject = scan.subject
        const codes = scan.codes
        if (/[+&]|\bAND\b/.test(seg) && codes.length > 1) combos.push(codes)
        else any.push(...codes)
      }
      return { ...base, any, combos, pick: null }
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
  const claimedCodes = new Set<string>()
  const accepted: ExamApplicability[] = []

  /** Matches one published course equivalent against the plan, recording into `taken`. */
  const evaluate = (course: string | null, taken: Set<PlanItem>) => {
    const { groups, elective } = parseEquivalent(course)
    const matched: ExamApplicability['matched'] = []
    const codes: string[] = []
    /** Awarded codes that filled a single row: they can't count again for a combination or a choice block. */
    const claimed: string[] = []
    if (!groups.length) return { status: (elective ? 'elective_only' : 'no_course') as Applicability, matched, codes, claimed }
    let anyAssigned = false
    let hit = 0
    for (const g of groups) {
      if (g.length > 1) {
        // The school assigns one of several courses: it applies only if every option fits the same item.
        // A one-of-several choice row fits too, when every course in the group alone satisfies one of its options.
        const fits = (it: PlanItem) =>
          g.every((c) => it.any.includes(c)) || (!!it.pick && it.pick.n === 1 && g.every((c) => it.pick!.options.some((o) => o.length === 1 && o[0]!.includes(c))))
        const fit = items.find((it) => !taken.has(it) && fits(it))
        if (fit) {
          taken.add(fit)
          matched.push({ code: g.join(' or '), term: fit.term, label: fit.label, item: fit.text, credits: fit.credits })
          hit++
        } else anyAssigned = true
        continue
      }
      const code = g[0]!
      codes.push(code)
      // A course already used by another exam's row fills no second row (two exams awarding the same course).
      const it = claimedCodes.has(code) ? undefined : items.find((x) => !taken.has(x) && x.any.includes(code))
      if (it) {
        taken.add(it)
        claimed.push(code)
        matched.push({ code, term: it.term, label: it.label, item: it.text, credits: it.credits })
        hit++
        continue
      }
      // Part of a combination row ("PHYS 2325& PHYS 2125"): the course is in the plan. The row itself counts as
      // done only when every course of the combination is awarded (checked after all exams), so it isn't taken here.
      const combo = items.find((x) => !taken.has(x) && (x.combos.some((c) => c.includes(code)) || !!x.pick?.options.some((o) => o.some((req) => req.includes(code)))))
      if (combo) {
        matched.push({ code, term: combo.term, label: combo.label, item: combo.text, credits: combo.credits })
        hit++
      }
    }
    const status: Applicability = hit === groups.length ? 'applies' : hit > 0 ? 'partly' : anyAssigned ? 'school_assigns' : 'not_in_plan'
    return { status, matched, codes, claimed }
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
    for (const c of r.claimed) claimedCodes.add(c)
    accepted.push({ examName: m.exam.name, course: courses[0] ?? null, hours, status: r.status, matched: r.matched })
  }

  // Awarded courses not already used by a single row. Each one fills at most one combination or one choice option,
  // so one course is never counted twice (#268 review).
  const free = new Set([...earnedCodes].filter((c) => !claimedCodes.has(c)))
  // Combination items ("CHEM 102+103") count when every course of one combination was awarded and is still free.
  for (const it of items) {
    if (used.has(it)) continue
    const combo = it.combos.find((c) => c.every((code) => free.has(code)))
    if (combo) {
      used.add(it)
      for (const code of combo) free.delete(code)
    }
  }
  // "Select N of the following": done only when N different options are fully awarded with free courses.
  for (const it of items) {
    if (used.has(it) || !it.pick) continue
    const take: string[] = []
    let n = 0
    for (const o of it.pick.options) {
      if (n >= it.pick.n) break
      // Each requirement of the option takes one free course not already taken for this block.
      const chosen: string[] = []
      for (const req of o) {
        const c = req.find((code) => free.has(code) && !take.includes(code) && !chosen.includes(code))
        if (!c) break
        chosen.push(c)
      }
      if (chosen.length === o.length) {
        take.push(...chosen)
        n++
      }
    }
    if (n >= it.pick.n) {
      used.add(it)
      for (const code of take) free.delete(code)
    }
  }

  const byTerm = new Map<number, PlanItem[]>()
  for (const it of items) byTerm.set(it.term, [...(byTerm.get(it.term) ?? []), it])
  const coveredTerms = [...byTerm.entries()].filter(([, its]) => its.length > 0 && its[0]!.checked && its.every((x) => used.has(x))).map(([term, its]) => ({ term, label: its[0]!.label }))

  return {
    accepted,
    acceptedHours: accepted.reduce((s, a) => s + (a.hours ?? 0), 0),
    applicableHours: accepted.filter((a) => a.status === 'applies').reduce((s, a) => s + (a.hours ?? 0), 0),
    applicableWithoutHours: accepted.filter((a) => a.status === 'applies' && a.hours == null).length,
    coveredTerms,
  }
}
