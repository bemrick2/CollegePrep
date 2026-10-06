import type { InstitutionComparison } from '../../lib/data/types'
import type { ReferenceScore } from '../../lib/engine/merit'
import { formatShortDate } from '../../lib/engine/dates'

export const POLICY_LABEL: Record<string, string> = {
  AP: 'AP',
  CLEP: 'CLEP',
  IB: 'IB',
  cambridge_international: 'Cambridge',
  dual_enrollment: 'Dual enrollment',
  statewide_dual_credit: 'Statewide dual credit',
  industry_certification: 'Industry certification',
}
export const CONTROL_LABEL: Record<string, string> = { public: 'Public', private_nonprofit: 'Private nonprofit', private_for_profit: 'Private for-profit' }
export const LEVEL_LABEL: Record<string, string> = { four_year: '4-year', two_year: '2-year', less_than_two_year: 'Less than 2-year' }
export const DOMAIN_LABEL: Record<string, string> = {
  costs: 'Cost of attendance',
  admissions_metrics: 'Admissions',
  awards: 'Scholarships',
  credit_policies: 'AP / CLEP / IB credit',
  transfer_policies: 'Transfer credit',
  academic_programs: 'Programs',
  degree_requirements: 'Degree maps',
  appeals: 'Aid appeals',
}
export const humanize = (k: string) => {
  const s = k.replace(/_/g, ' ')
  return s.charAt(0).toUpperCase() + s.slice(1)
}

export interface AcademicFit {
  lo: number
  hi: number
  where: 'below' | 'within' | 'above'
  value: number
  whose: string
}

/** Where the target or official score sits against the published middle 50% of admitted students.
 *  A comparison of two numbers, never an admission prediction. */
export function academicFit(c: InstitutionComparison, exam: 'act' | 'sat', reference: ReferenceScore | null): AcademicFit | null {
  const adm = (c.domains.admissions_metrics?.[0] ?? null) as Record<string, number | null> | null
  const lo = adm?.[`${exam}_25`] ?? null
  const hi = adm?.[`${exam}_75`] ?? null
  if (!reference || lo == null || hi == null) return null
  const v = reference.value
  return { lo, hi, value: v, where: v < lo ? 'below' : v > hi ? 'above' : 'within', whose: reference.basis === 'target' ? 'Target' : reference.basis === 'official' ? 'Official score' : 'Self-reported score' }
}

export function RangeNote({ fit, exam }: { fit: AcademicFit; exam: 'act' | 'sat' }) {
  return (
    <p className="text-sm text-ink-2">
      {fit.whose} {fit.value} is <span className="font-semibold text-ink">{fit.where}</span> the middle 50% ({fit.lo}–{fit.hi} {exam.toUpperCase()}). Not an admission prediction.
    </p>
  )
}

export function SourceLink({ href, verified }: { href?: string | null; verified?: string | null }) {
  if (!href) return null
  return (
    <a href={href} target="_blank" rel="noreferrer" className="text-xs font-semibold text-ink-3 hover:text-ink hover:underline">
      Source{verified ? `, verified ${formatShortDate(verified)}` : ''}
    </a>
  )
}

export function Missing({ what = 'record' }: { what?: string }) {
  return <p className="text-sm text-ink-3">No verified {what} yet. That doesn't mean it doesn't exist.</p>
}
