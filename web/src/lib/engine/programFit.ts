import { INTEREST_AREAS, MAJORS, labelOf, type SavedInterest } from './interests'
import { COURSE_NUMBER, normalizeCode, readTermItems, type PlanTermLike } from './planItems'

const COURSE_ONLY = new RegExp(`^[A-Z]{2,5} ${COURSE_NUMBER}$`)

/**
 * "Keeps my options open": how a school's verified records line up with every interest a student saved.
 *
 * Verified facts only. A program counts as offered when a verified academic_programs record matches the interest
 * (by CIP family when the record has one, else by name; the matched program name is always shown). Program lists
 * are often partial imports, so "not listed" never means "not offered". Admission type, internal-transfer limits,
 * starting undeclared, credit by degree path and switching cost are not modelled by the backend yet (CR-14): they
 * are reported as unverified questions, never answered. Published progression text is quoted, not interpreted.
 */

export interface ProgramRecord {
  program_key?: string | null
  program_name?: string | null
  cip_code?: string | null
  credential_level?: string | null
  program_url?: string | null
  source_url?: string | null
  /** CR-14 (not served yet): how students enter the program. */
  admission_type?: 'direct' | 'pre_major' | 'open' | null
}

interface DegreeRecord {
  program_key?: string | null
  source_url?: string | null
  rule_details?: {
    terms?: PlanTermLike[]
    progression?: string | null
    grade_requirements?: string | null
    prior_credit_notes?: string | null
  } | null
}

interface AwardRecord {
  award_name?: string | null
  major_requirement?: string | null
  source_url?: string | null
}

export interface SchoolDomains {
  academic_programs?: unknown[]
  degree_requirements?: unknown[]
  awards?: unknown[]
}

export type FitStatus = 'verified' | 'not_listed' | 'no_data'

export interface InterestFit {
  interest: SavedInterest
  label: string
  status: FitStatus
  programs: { name: string; url: string | null; key: string | null }[]
  /** Only when the backend states it (CR-14): some matched program requires direct/freshman admission. */
  directAdmission: boolean
  /** Verbatim published rules from the matched programs' degree maps. */
  progression: { program: string; text: string; source: string | null }[]
  priorCredit: { program: string; text: string }[]
  scholarships: { name: string; requirement: string; url: string | null }[]
}

export interface SchoolFit {
  fits: InterestFit[]
  verifiedCount: number
  /** Courses that appear verbatim in the first-year terms of two or more matched programs' published maps. */
  sharedFirstYear: { courses: string[]; programs: string[] } | null
  hasProgramData: boolean
}

function patternsFor(i: SavedInterest): { cip: string[]; match: RegExp[] } {
  if (i.kind === 'major') {
    const m = MAJORS.find((x) => x.key === i.key)
    return { cip: m?.cip ?? [], match: m?.match ?? [] }
  }
  const a = INTEREST_AREAS.find((x) => x.key === i.key)
  return { cip: a?.cip ?? [], match: a?.majors.flatMap((x) => x.match) ?? [] }
}

function matches(p: ProgramRecord, pat: { cip: string[]; match: RegExp[] }): boolean {
  const cip = (p.cip_code ?? '').replace(/\D/g, '').slice(0, 2)
  if (cip) return pat.cip.includes(cip)
  const name = p.program_name ?? ''
  return pat.match.some((r) => r.test(name))
}

const isBachelor = (p: ProgramRecord) => !p.credential_level || /bachelor/i.test(p.credential_level)

export function schoolFit(d: SchoolDomains, interests: SavedInterest[]): SchoolFit {
  const programs = ((d.academic_programs ?? []) as ProgramRecord[]).filter(isBachelor)
  const degrees = (d.degree_requirements ?? []) as DegreeRecord[]
  const awards = (d.awards ?? []) as AwardRecord[]
  const hasProgramData = programs.length > 0

  const fits: InterestFit[] = interests.map((interest) => {
    const pat = patternsFor(interest)
    const found = programs.filter((p) => matches(p, pat))
    const keys = new Set(found.map((p) => p.program_key).filter(Boolean))
    const maps = degrees.filter((r) => r.program_key && keys.has(r.program_key))
    const nameOf = (k?: string | null) => found.find((p) => p.program_key === k)?.program_name ?? k ?? 'Program'
    return {
      interest,
      label: labelOf(interest),
      status: found.length ? 'verified' : hasProgramData ? 'not_listed' : 'no_data',
      programs: found.map((p) => ({ name: p.program_name ?? 'Program', url: p.program_url ?? p.source_url ?? null, key: p.program_key ?? null })),
      directAdmission: found.some((p) => p.admission_type === 'direct'),
      progression: maps.filter((r) => r.rule_details?.progression).map((r) => ({ program: nameOf(r.program_key), text: r.rule_details!.progression!, source: r.source_url ?? null })),
      priorCredit: maps.filter((r) => r.rule_details?.prior_credit_notes).map((r) => ({ program: nameOf(r.program_key), text: r.rule_details!.prior_credit_notes! })),
      scholarships: awards
        .filter((a) => a.major_requirement && pat.match.some((r) => r.test(a.major_requirement!)))
        .map((a) => ({ name: a.award_name ?? 'Scholarship', requirement: a.major_requirement!, url: a.source_url ?? null })),
    }
  })

  // Shared first-year courses: only from published maps, only exact item text, only across distinct programs.
  const firstYear = new Map<string, Set<string>>()
  const mapped = new Set<string>()
  for (const f of fits)
    for (const p of f.programs) {
      if (!p.key || mapped.has(p.key)) continue
      const map = degrees.find((r) => r.program_key === p.key)
      const items = (map?.rule_details?.terms ?? []).filter((t) => (t.term_index ?? 99) <= 2).flatMap(readTermItems)
      if (!items.length) continue
      mapped.add(p.key)
      // One named course per item: a structured course's code, or a text item that is exactly a course. Choices
      // ("complete one of") and electives aren't a shared course.
      const courses = items.flatMap((e) => (e.choices.length ? [] : e.code ? [e.code] : COURSE_ONLY.test(e.text) ? [normalizeCode(e.text)] : []))
      for (const c of new Set(courses)) firstYear.set(c, (firstYear.get(c) ?? new Set()).add(p.name))
    }
  const shared = [...firstYear.entries()].filter(([, ps]) => ps.size >= 2)
  const sharedFirstYear = mapped.size >= 2 ? { courses: shared.map(([c]) => c), programs: [...new Set(shared.flatMap(([, ps]) => [...ps]))] } : null

  return { fits, verifiedCount: fits.filter((f) => f.status === 'verified').length, sharedFirstYear, hasProgramData }
}

/** Questions the backend cannot answer yet (CR-14). Shown as a checklist, never answered by inference. */
export const UNVERIFIED_QUESTIONS = [
  'Does the major require direct (freshman) admission?',
  'Can you transfer into it after starting at the school, and is that restricted?',
  'Can you start undeclared or exploratory?',
  'How do AP, CLEP, IB and dual-enrollment credits apply to each major?',
  'What would changing majors cost in time or money?',
]

/** One-sentence summary in the student's terms, from verified facts only. */
export function fitSentence(school: string, fit: SchoolFit): string | null {
  const n = fit.fits.length
  if (!n) return null
  if (!fit.hasProgramData) return `We haven't verified ${school}'s program list yet.`
  const found = fit.fits.filter((f) => f.status === 'verified').map((f) => f.label)
  const missing = fit.fits.filter((f) => f.status !== 'verified').map((f) => f.label)
  const list = (xs: string[]) => (xs.length <= 1 ? (xs[0] ?? '') : `${xs.slice(0, -1).join(', ')} and ${xs[xs.length - 1]}`)
  if (!found.length) return `None of your interests is in the verified programs we have for ${school} yet (that list is partial).`
  const direct = fit.fits.filter((f) => f.directAdmission).map((f) => f.label)
  const but = direct.length ? `, but ${list(direct)} ${direct.length === 1 ? 'requires' : 'require'} freshman admission` : ''
  if (!missing.length) return `${school} has verified programs for ${n === 1 ? 'your interest' : n === 2 ? 'both of your interests' : `all ${n} of your interests`}${but}.`
  return `${school} has verified programs for ${list(found)}${but}; ${list(missing)} ${missing.length === 1 ? "isn't" : "aren't"} in our verified list yet.`
}
