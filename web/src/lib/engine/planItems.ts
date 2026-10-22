/**
 * One reader for degree-plan items (`rule_details.terms[].items[]`), whatever extractor wrote them (#171). Supported:
 *
 *  - a string: "ENGL 101", "MATH 132 or MATH 141", "Volunteer Core elective (AH, GCUS, GCI or SS)"
 *  - courseleaf_plan/v1: {code, title, credits?, milestone?} or {text, credits?, milestone?}
 *  - courseleaf_plangrid/v1: {code | text, credits?, footnotes?, recommended?, options?: item[]}
 *    ("Complete one of the following:" with its option rows)
 *  - {any_of: item[]} (one of several courses)
 *  - a pipe string (#230): "MGMT 4010 | Total Rewards | 3", "GER Elective | 3", "CIS 2166 | Title" and Oregon's
 *    "WR 122Zor WR 123 | Titles | Milestone | 4". Split here, on the app side only; the stored text is unchanged.
 *  - a row `note` (courseleaf_plantext/v1) and `{text}` rows with no credits (milestones such as "BFA Application")
 *
 * Rows that aren't requirements are kept but marked: an inline heading ("Semester 2", "Sophomore") is `heading`, and
 * a printed subtotal ("Credit Hours | 15") is `subtotal`. Neither is something a student has to take.
 *
 * Nothing is dropped or invented: term, course, title, credits, milestone, footnotes and recommended flags are kept
 * as printed. An option list or any_of is "any one of these". Unknown shapes are kept as their text, never thrown on.
 */

export type RawPlanItem =
  | string
  | {
      code?: string | null
      title?: string | null
      text?: string | null
      credits?: number | string | null
      milestone?: string | null
      footnotes?: string[] | null
      note?: string | null
      recommended?: boolean | null
      /** The printed count of a choice block ("Select two of the following"); never inferred (#230). */
      choose?: number | null
      options?: RawPlanItem[] | null
      any_of?: RawPlanItem[] | null
    }

/**
 * course: one course code. choice: any one of several. text: a printed requirement with no single code (an
 * elective, a milestone, a note row). heading: a label printed among the rows. subtotal: a printed hours total.
 */
export type PlanEntryKind = 'course' | 'choice' | 'text' | 'heading' | 'subtotal'

export interface PlanEntry {
  kind: PlanEntryKind
  /** As printed: the course code (with its title) or the text row. */
  text: string
  /** The course code when the item is one course. */
  code: string | null
  title: string | null
  /** Credits as printed (a number, or a range such as "3-4"); null when the plan prints none. */
  credits: number | string | null
  milestone: string | null
  /** The row's printed note (courseleaf_plantext/v1), as printed. */
  note: string | null
  footnotes: string[]
  recommended: boolean
  /** "Any one of": the item's options (plangrid) or any_of list. Empty for a single requirement. */
  choices: PlanEntry[]
  /** How many of `choices` the requirement takes, when the plan prints it; 1 otherwise. */
  choose: number
}

export interface PlanTermLike {
  term_index?: number
  label?: string
  credit_hours?: string
  items?: RawPlanItem[] | null
}

const str = (v: unknown): string | null => (typeof v === 'string' && v.trim() ? v.trim() : null)

/** A printed credit value: "3", "1.5", ".5", "3-4", "15-16", "2 or 3", "3,4", "6 to 12", "15+". */
const NUM = '(?:\\d+(?:\\.\\d+)?|\\.\\d+)'
const CREDITS = new RegExp(`^${NUM}(?:\\s*(?:[-–,]|or|to)\\s*${NUM})*\\+?$`, 'i')
const ORDINAL = '(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|\\d+(?:st|nd|rd|th))'
const NUMBER_WORD = '(?:\\d+|one|two|three|four|five|six|seven|eight|nine|ten)'
/** Semester-level labels: "Semester 2", "Semester Seven", "Second Semester", "Term 1", "Fall", "Summer Session", "J-term". */
const SEMESTER_HEADING = new RegExp(
  `^(?:${ORDINAL}\\s+(?:semester|term|quarter)|(?:semester|term|quarter)\\s+${NUMBER_WORD}|(?:fall|spring|summer|winter|autumn)(?:\\s+(?:semester|term|quarter|session))?|(?:fall|spring|autumn)\\s*[12]|j-?term|any\\s+quarter|maymester|intersession)$`,
  'i',
)
/** A column header printed as a row: "First Semester | Credits", "Fall | S.H.", "Semester 1 | Credit Hours". */
const HEADER_WORD = /^(?:credits?|credit\s+hours|semester\s+credit\s+hours|hours|s\.?\s?h\.?|units)$/i
/** A short or partial session: whole-term coverage is never checked for it (it isn't a semester of cost). */
const SHORT_TERM = /\b(?:summer|winter|j-?term|intersession|maymester|session|mini)\b|^any\b/i
/** "Spring 1" / "Spring 2" printed under a "Spring" heading: sub-sessions of one semester (SLU), not semesters. */
const SUB_SESSION = /^(?:fall|spring|autumn)\s*[12]$/i
/** Year-level labels: "Freshman", "Sophomore Year", "Year 2", "Year One", "First Year", "4th Year". */
const YEAR_HEADING = /^(?:(?:freshman|sophomore|junior|senior)(?:\s+year)?|year\s+(?:\d+|one|two|three|four|five)|(?:first|second|third|fourth|fifth|\d+(?:st|nd|rd|th))\s+year)$/i
const SUBTOTAL = /^(?:minimum\s+)?(?:total\s+)?(?:(?:semester|term|quarter)\s+)?(?:credit\s+)?(?:hours|credits|units)(?:\s+total)?$/i
/**
 * Exactly one course code. Subjects of 6–8 letters must be capitals ("COMPSCI 250", "ENGLISH 101" at UWM), so a
 * word such as "Language 113" isn't read as a code. COURSE_NUMBER is declared further down.
 */
const SINGLE_CODE = /^(?:[A-Z]{2,8}|[A-Za-z]{2,5})\s*F?\d{3,4}[A-Z]?$/

const entry = (e: Partial<PlanEntry> & Pick<PlanEntry, 'text'>): PlanEntry => ({
  kind: 'text',
  code: null,
  title: null,
  credits: null,
  milestone: null,
  note: null,
  footnotes: [],
  recommended: false,
  choices: [],
  choose: 1,
  ...e,
})

/** Credits as printed: an integer as a number (as the structured formats store it), anything else as the string. */
const printedCredits = (c: string): number | string => (/^\d+$/.test(c) ? Number(c) : c)

function readPipe(raw: string): PlanEntry | null {
  const parts = raw.split('|').map((x) => x.trim())
  if (parts.every((x) => !x)) return null
  // A column header row: the semester's name plus "Credits".
  if (parts.length === 2 && HEADER_WORD.test(parts[1]!) && (SEMESTER_HEADING.test(parts[0]!) || YEAR_HEADING.test(parts[0]!))) return entry({ kind: 'heading', text: parts[0]! })
  const last = parts[parts.length - 1]!
  const credits = CREDITS.test(last) ? printedCredits(last) : null
  const rest = credits !== null ? parts.slice(0, -1) : parts
  const [first = '', title = null, milestone = null] = rest.filter((x, i) => x !== '' || i === 0)
  if (rest.length === 1 || !title) {
    if (SINGLE_CODE.test(first)) return entry({ kind: 'course', text: normalizeCode(first), code: normalizeCode(first), credits })
    const kind = credits !== null && SUBTOTAL.test(first) ? 'subtotal' : 'text'
    return entry({ kind, text: first, credits })
  }
  // "CODE | Title": one course. "WR 122Zor WR 123 | ...", "BIOL 1113& BIOL 1111 | ...", "ACCT 3xx/4xx | ...": the
  // first part names several courses (or a placeholder), so it stays text and its codes are read from it.
  const code = SINGLE_CODE.test(first) ? normalizeCode(first) : null
  return entry({ kind: code ? 'course' : 'text', text: `${code ?? first} ${title}`, code, title, credits, milestone: milestone || null })
}

export function readPlanItem(raw: unknown): PlanEntry | null {
  if (typeof raw === 'string') {
    const t = raw.trim()
    if (!t) return null
    if (t.includes('|')) return readPipe(t)
    if (SEMESTER_HEADING.test(t) || YEAR_HEADING.test(t)) return entry({ kind: 'heading', text: t })
    return entry({ text: t })
  }
  if (!raw || typeof raw !== 'object') return null
  const o = raw as Exclude<RawPlanItem, string>
  const list = Array.isArray(o.options) ? o.options : Array.isArray(o.any_of) ? o.any_of : []
  const choices = list.map(readPlanItem).filter((x): x is PlanEntry => !!x)
  const code = str(o.code)
  const title = str(o.title)
  const own = code ? (title ? `${code} ${title}` : code) : str(o.text)
  const text = own ?? (choices.length ? choices.map((c) => c.text).join(' or ') : '')
  const credits = typeof o.credits === 'number' || (typeof o.credits === 'string' && o.credits.trim()) ? o.credits : null
  // A row printed with credits only (Oregon) is kept with its credits; only a row with nothing in it is skipped.
  if (!text && !choices.length && credits === null) return null
  const kind: PlanEntryKind = code ? 'course' : choices.length ? 'choice' : credits !== null && SUBTOTAL.test(text) ? 'subtotal' : 'text'
  return entry({
    kind,
    text,
    code: code ? normalizeCode(code) : null,
    title,
    credits,
    milestone: str(o.milestone),
    note: str(o.note),
    footnotes: Array.isArray(o.footnotes) ? o.footnotes.filter((f): f is string => typeof f === 'string') : [],
    recommended: o.recommended === true,
    choices,
    choose: choices.length && Number.isInteger(o.choose) && (o.choose as number) > 1 && (o.choose as number) <= choices.length ? (o.choose as number) : 1,
  })
}

/** Something the student has to complete (not an inline heading or a printed subtotal). */
export const isRequirement = (e: PlanEntry) => e.kind !== 'heading' && e.kind !== 'subtotal'

/** The readable items of one term, in order. */
export function readTermItems(term: PlanTermLike): PlanEntry[] {
  return (Array.isArray(term.items) ? term.items : []).map(readPlanItem).filter((x): x is PlanEntry => !!x)
}

/** A term printed as a group heading only: no items and no credit hours ("Freshman", "Year One", #230). */
export function isHeadingTerm(term: PlanTermLike): boolean {
  const items = Array.isArray(term.items) ? term.items : []
  return !items.some((x) => readPlanItem(x)) && !(typeof term.credit_hours === 'string' && term.credit_hours.trim())
}

export type NotCheckedReason = 'multi_term' | 'short_term' | 'quarter_calendar' | 'hours'

export interface PlanTermView {
  /** 1, 2, 3… over real terms only (heading terms are not numbered). */
  number: number
  /** The stored term_index (or position), which credit matches refer to. */
  termIndex: number
  label: string
  /** The year heading printed above this term, when the plan has one. */
  group: string | null
  /** As printed: the term's credit_hours. Never summed by the app, and printed subtotal rows are left as rows. */
  creditHours: string | number | null
  entries: PlanEntry[]
  /** The term holds more than one semester (a year printed as one block, or several semester headings in its rows). */
  multiTerm: boolean
  /**
   * Why "this whole term is covered" isn't checked for this term, or null when it is. A covered term is valued as a
   * semester of cost, so only a regular full-time semester qualifies: never a year block, a summer or short session,
   * a quarter (the cost model counts semesters), or a term whose printed hours are under 12 or not printed.
   */
  notChecked: NotCheckedReason | null
}

const lowest = (v: unknown): number | null => {
  if (typeof v === 'number') return v
  const m = typeof v === 'string' ? /\d+(?:\.\d+)?|\.\d+/.exec(v) : null
  return m ? Number(m[0]) : null
}
const FULL_TIME = 12

/**
 * The plan's terms as the student would read them: heading terms become the `group` of the terms under them and are
 * not counted; every other term keeps its rows exactly as read.
 */
export function planTerms(terms: PlanTermLike[]): PlanTermView[] {
  const out: PlanTermView[] = []
  let group: string | null = null
  // Quarter calendars: a winter term with rows, or any term or inline heading naming a quarter.
  const quarter = terms.some(
    (t) =>
      (/\bquarter\b/i.test(t.label ?? '') || (/\bwinter\b/i.test(t.label ?? '') && !isHeadingTerm(t))) ||
      readTermItems(t).some((e) => e.kind === 'heading' && /\bquarter\b/i.test(e.text)),
  )
  terms.forEach((t, i) => {
    let label = (typeof t.label === 'string' && t.label.trim()) || `Term ${t.term_index ?? i + 1}`
    if (isHeadingTerm(t)) {
      group = label
      return
    }
    let entries = readTermItems(t)
    let termGroup = group
    const semesterHeads = entries.filter((e) => e.kind === 'heading' && SEMESTER_HEADING.test(e.text))
    // "First Year" whose rows start with its only semester heading ("Fall Semester | Credits"): that semester.
    if (YEAR_HEADING.test(label) && semesterHeads.length === 1 && entries[0] === semesterHeads[0]) {
      termGroup = label
      label = semesterHeads[0]!.text
      entries = entries.slice(1)
    }
    const multiTerm = entries.some((e) => e.kind === 'heading' && SEMESTER_HEADING.test(e.text)) || YEAR_HEADING.test(label) || entries.filter((e) => e.kind === 'subtotal' && !/^(?:total|minimum)\b/i.test(e.text)).length > 1
    const hours = typeof t.credit_hours === 'string' && t.credit_hours.trim() ? t.credit_hours.trim() : null
    // Printed hours, or else the rows' printed credits (each at its lowest); used only to tell a full-time term.
    const reqs = entries.filter(isRequirement)
    const rowHours = reqs.every((e) => lowest(e.credits) != null) ? reqs.reduce((n, e) => n + lowest(e.credits)!, 0) : null
    const termHours = hours != null ? lowest(hours) : rowHours
    const notChecked: NotCheckedReason | null = multiTerm
      ? 'multi_term'
      : SHORT_TERM.test(label) || (SUB_SESSION.test(label) && /^(?:fall|spring|autumn)\b/i.test(termGroup ?? ''))
        ? 'short_term'
        : quarter
          ? 'quarter_calendar'
          : termHours == null || termHours < FULL_TIME
            ? 'hours'
            : null
    out.push({ number: out.length + 1, termIndex: t.term_index ?? i + 1, label, group: termGroup, creditHours: hours, entries, multiTerm, notChecked })
  })
  return out
}

/**
 * Course codes as catalogs print them: subject (2–5 letters) and number, including UAF's "F" campus prefix and
 * attribute suffixes ("MATH F251X", "CPSC 4995R", "ENGL 101"). A bare number after a code inherits its subject
 * ("COM F121X, F131X, or F141X").
 */
export const COURSE_NUMBER = 'F?\\d{3,4}[A-Z]?'
// The number ends at a word boundary, or where "or"/"and" was printed without a space ("INM 101or VOK 101", #230).
const CODE_IN_TEXT = new RegExp(`(?:\\b(?!OR\\b|AND\\b|WITH\\b)([A-Z]{2,5})\\s*)?(${COURSE_NUMBER})(?:\\b|(?=(?:OR|AND)\\b))`, 'g')

export function normalizeCode(code: string): string {
  const m = new RegExp(`^\\s*([A-Za-z]{2,5})\\s*(${COURSE_NUMBER})\\s*$`, 'i').exec(code.toUpperCase())
  return m ? `${m[1]} ${m[2]}` : code.trim().toUpperCase().replace(/\s+/g, ' ')
}

/** Codes found in free text, subjects carried forward (from `subject` when the text continues an earlier part). */
export function codesInText(text: string, subject: string | null = null): string[] {
  return scanCodes(text, subject).codes
}

export function scanCodes(text: string, subject: string | null = null): { codes: string[]; subject: string | null } {
  const codes: string[] = []
  for (const m of text.toUpperCase().matchAll(CODE_IN_TEXT)) {
    if (m[1]) subject = m[1]
    if (subject) codes.push(`${subject} ${m[2]}`)
  }
  return { codes, subject }
}

const TITLE_CODE = `[A-Z]{2,5}\\s*${COURSE_NUMBER}`
/** UTC Clear Path: "College Algebra or MATH 1830: Calculus…", "Int'l Economics, FIN 4120: Int'l Finance, or MKT 3180: …". */
const LISTED_ALTERNATIVE = new RegExp(`(?:,|\\bOR)\\s*(${TITLE_CODE})\\s*:`, 'g')
/** "College Algebra (or MATH 103M)", "(or PHIL 225, PHIL 321, or PHIL 323)". */
const PAREN_ALTERNATIVE = /\(OR\s+([^()]*)\)/g
/** Wording that makes a printed course something other than a plain alternative: a prerequisite, a condition, a
 *  combination, advice. Such titles add nothing (the item stays its own code), so credit is never over-applied. */
const NOT_AN_ALTERNATIVE = /\b(pre-?req|co-?req|only|if|not|instead|recommended|encouraged|substitut|either)\b/i
const PAREN_COMBINATION = /\band\b/i

/**
 * Alternatives a catalog printed inside a course's title (#192). Only two unambiguous shapes are read: a list of
 * "CODE: Title" entries joined by commas and "or", and a parenthesis that starts with "(or ". Anything else (a
 * prerequisite, "only if", "and either", "400-level course") is left alone: missing an alternative under-reports
 * applicable credit, guessing one would over-report it.
 */
export function titleAlternatives(code: string | null, title: string | null): string[] {
  if (!title || NOT_AN_ALTERNATIVE.test(title)) return []
  const t = title.toUpperCase()
  const out: string[] = []
  for (const m of t.matchAll(LISTED_ALTERNATIVE)) out.push(normalizeCode(m[1]!))
  for (const m of t.matchAll(PAREN_ALTERNATIVE)) {
    if (PAREN_COMBINATION.test(m[1]!) || /\d-LEVEL/.test(m[1]!)) continue
    out.push(...scanCodes(m[1]!, code ? normalizeCode(code).split(' ')[0]! : null).codes)
  }
  return out.filter((c) => c !== code)
}

/**
 * The course codes that satisfy an entry, "any one of": its own code (and alternatives printed in its title), codes
 * printed in its text, and every choice's codes. A choice rule's own text ("Complete one of the following:")
 * contributes none.
 */
export function entryCodes(e: PlanEntry): string[] {
  const own = e.code ? [e.code, ...titleAlternatives(e.code, e.title)] : codesInText(e.text)
  return [...new Set([...own, ...e.choices.flatMap(entryCodes)])]
}
