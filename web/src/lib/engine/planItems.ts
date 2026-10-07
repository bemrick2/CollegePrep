/**
 * One reader for degree-plan items (`rule_details.terms[].items[]`), whatever extractor wrote them (#171). Supported:
 *
 *  - a string: "ENGL 101", "MATH 132 or MATH 141", "Volunteer Core elective (AH, GCUS, GCI or SS)"
 *  - courseleaf_plan/v1: {code, title, credits?, milestone?} or {text, credits?, milestone?}
 *  - courseleaf_plangrid/v1: {code | text, credits?, footnotes?, recommended?, options?: item[]}
 *    ("Complete one of the following:" with its option rows)
 *  - {any_of: item[]} (one of several courses)
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
      recommended?: boolean | null
      options?: RawPlanItem[] | null
      any_of?: RawPlanItem[] | null
    }

export interface PlanEntry {
  /** As printed: the course code (with its title) or the text row. */
  text: string
  /** The course code when the item is one course. */
  code: string | null
  title: string | null
  /** Credits as printed (a number, or a range such as "3-4"); null when the plan prints none. */
  credits: number | string | null
  milestone: string | null
  footnotes: string[]
  recommended: boolean
  /** "Any one of": the item's options (plangrid) or any_of list. Empty for a single requirement. */
  choices: PlanEntry[]
}

export interface PlanTermLike {
  term_index?: number
  label?: string
  credit_hours?: string
  items?: RawPlanItem[] | null
}

const str = (v: unknown): string | null => (typeof v === 'string' && v.trim() ? v.trim() : null)

export function readPlanItem(raw: unknown): PlanEntry | null {
  if (typeof raw === 'string') {
    const t = raw.trim()
    return t ? { text: t, code: null, title: null, credits: null, milestone: null, footnotes: [], recommended: false, choices: [] } : null
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
  return {
    text,
    code: code ? normalizeCode(code) : null,
    title,
    credits,
    milestone: str(o.milestone),
    footnotes: Array.isArray(o.footnotes) ? o.footnotes.filter((f): f is string => typeof f === 'string') : [],
    recommended: o.recommended === true,
    choices,
  }
}

/** The readable items of one term, in order. */
export function readTermItems(term: PlanTermLike): PlanEntry[] {
  return (Array.isArray(term.items) ? term.items : []).map(readPlanItem).filter((x): x is PlanEntry => !!x)
}

/**
 * Course codes as catalogs print them: subject (2–5 letters) and number, including UAF's "F" campus prefix and
 * attribute suffixes ("MATH F251X", "CPSC 4995R", "ENGL 101"). A bare number after a code inherits its subject
 * ("COM F121X, F131X, or F141X").
 */
export const COURSE_NUMBER = 'F?\\d{3,4}[A-Z]?'
const CODE_IN_TEXT = new RegExp(`(?:\\b(?!OR\\b|AND\\b|WITH\\b)([A-Z]{2,5})\\s*)?(${COURSE_NUMBER})\\b`, 'g')

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

/**
 * The course codes that satisfy an entry, "any one of": its own code, codes printed in its text, and every
 * choice's codes. A choice rule's own text ("Complete one of the following:") contributes none.
 */
export function entryCodes(e: PlanEntry): string[] {
  const own = e.code ? [e.code] : codesInText(e.text)
  return [...new Set([...own, ...e.choices.flatMap(entryCodes)])]
}
