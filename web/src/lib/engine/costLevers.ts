import { meritAwards, BASIS_LABEL, type ReferenceScore } from './merit'
import type { SchoolCreditSummary } from './examCredit'

/**
 * "Ways to lower this cost" for one school, built only from that school's verified records: merit awards with a
 * plainly published single test minimum, the school's own exam-credit table, verified dual-enrollment policy,
 * need-based/access programs it publishes, and its published aid-appeal process. Nothing is summed into a dollar
 * saving: awards may not stack, credit may not shorten the degree, and need-based aid depends on family finances.
 */

export type LeverStatus = 'on_track' | 'within_reach' | 'stretch' | 'available' | 'check'

export interface CostLever {
  key: string
  status: LeverStatus
  title: string
  detail: string
  href?: string | null
}

/** Points of a single published minimum still counted as "within reach" (ACT composite / SAT total). */
export const REACH = { act: 2, sat: 60 } as const
const EXAM = { act: 'ACT', sat: 'SAT' } as const
// Score-driven levers lead (the main path is raising the score at the schools the student wants), then credit.
const KEY_ORDER = ['merit-met', 'merit-next', 'merit-target', 'credit', 'dual', 'merit-other', 'need', 'appeal', 'npc']

export interface LeverInput {
  awards?: unknown[]
  creditPolicies?: { policy_kind: string; policy_url?: string | null; source_url?: string | null }[]
  appeals?: { offered?: boolean | null; appeal_kind?: string | null; policy_url?: string | null; source_url?: string | null }[]
  credit: SchoolCreditSummary | null
  exam: 'act' | 'sat'
  reference: ReferenceScore | null
  netPriceUrl?: string | null
}

interface NeedAward {
  award_name?: string | null
  award_type?: string | null
  source_url?: string | null
}

export function costLevers(i: LeverInput): CostLever[] {
  const out: CostLever[] = []
  const exam = EXAM[i.exam]

  // Merit: single published minimums only (CR-11 pending); tiered or GPA-only awards are pointed to, not scored.
  const merits = meritAwards(i.awards)
  const scored = merits.filter((m) => m.min[i.exam] != null)
  const unscored = merits.length - scored.length
  if (scored.length && i.reference) {
    const ref = i.reference.value
    const met = scored.filter((m) => m.min[i.exam]! <= ref)
    const above = scored.filter((m) => m.min[i.exam]! > ref).sort((a, b) => a.min[i.exam]! - b.min[i.exam]!)
    const basis = BASIS_LABEL[i.reference.basis]
    if (met.length)
      out.push({
        key: 'merit-met',
        status: 'on_track',
        title: `${met.length} merit award${met.length === 1 ? '' : 's'} with a published ${exam} minimum the ${basis} meets`,
        detail: `${met.map((m) => m.name).slice(0, 3).join(', ')}${met.length > 3 ? '…' : ''}. GPA, deadlines and other criteria still apply — not an eligibility decision.`,
        href: met[0]!.sourceUrl,
      })
    const next = above[0]
    if (next) {
      const gap = next.min[i.exam]! - ref
      const sameMin = above.filter((m) => m.min[i.exam] === next.min[i.exam])
      out.push({
        key: 'merit-next',
        status: gap <= REACH[i.exam] ? 'within_reach' : 'stretch',
        title: `${gap} more ${exam} point${gap === 1 ? '' : 's'} reaches ${sameMin.length > 1 ? `${sameMin.length} merit awards` : next.name} (${exam} ${next.min[i.exam]}+)`,
        detail: `${(next.amountText ?? (next.amountMax != null ? `Up to $${next.amountMax.toLocaleString()}` : 'Amount not published')).replace(/\.\s*$/, '')}. Compared with the ${basis} of ${ref}; published criteria only.`,
        href: next.sourceUrl,
      })
    }
  } else if (scored.length) {
    out.push({ key: 'merit-target', status: 'check', title: `Set a target ${exam} score`, detail: `${scored.length} merit award${scored.length === 1 ? '' : 's'} here publish an ${exam} minimum; a target shows the gap.` })
  }
  if (unscored > 0)
    out.push({ key: 'merit-other', status: 'check', title: `${unscored} more merit award${unscored === 1 ? '' : 's'} with GPA-only or tiered criteria`, detail: 'Read each award’s published criteria; we only compare single published test minimums.' })

  // Exam credit from the school's own table.
  const hasTable = (i.creditPolicies ?? []).some((p) => ['AP', 'CLEP', 'IB'].includes(p.policy_kind))
  if (i.credit && i.credit.courses > 0)
    out.push({
      key: 'credit',
      status: 'on_track',
      title: `Listed exams earn credit for ${i.credit.courses} course${i.credit.courses === 1 ? '' : 's'}`,
      detail: `${i.credit.publishedHours ? `${i.credit.publishedHours} published credit hours` : 'Credit hours not all published'}. Shortens the degree only if the courses count toward its requirements.`,
    })
  else if (hasTable)
    out.push({ key: 'credit', status: 'available', title: 'AP, CLEP or IB credit from a verified table', detail: 'Add exams on College paths to see the score each needs and the course it counts as.' })

  const dual = (i.creditPolicies ?? []).find((p) => p.policy_kind === 'dual_enrollment' || p.policy_kind === 'statewide_dual_credit')
  if (dual)
    out.push({ key: 'dual', status: 'available', title: 'Dual enrollment in high school', detail: 'Verified policy published. Read its GPA and eligibility rules before enrolling.', href: dual.policy_url ?? dual.source_url })

  // Need-based and access programs the school publishes; eligibility depends on family circumstances.
  const need = ((i.awards ?? []) as NeedAward[]).filter((a) => /need|access/.test(a.award_type ?? ''))
  if (need.length)
    out.push({
      key: 'need',
      status: 'available',
      title: `${need.length} need-based or access program${need.length === 1 ? '' : 's'}`,
      detail: `${need.map((a) => a.award_name).filter(Boolean).slice(0, 3).join(', ')}. Eligibility depends on family income and other published criteria.`,
      href: need[0]!.source_url,
    })

  const appeal = (i.appeals ?? []).find((a) => a.offered)
  if (appeal)
    out.push({ key: 'appeal', status: 'available', title: 'Published financial-aid appeal process', detail: 'If family circumstances change, the school lists how to ask for a review.', href: appeal.policy_url ?? appeal.source_url })

  if (i.netPriceUrl) out.push({ key: 'npc', status: 'check', title: 'Estimate your net price', detail: 'The school’s net price calculator estimates cost after grants for your family.', href: i.netPriceUrl })

  return out.sort((a, b) => KEY_ORDER.indexOf(a.key) - KEY_ORDER.indexOf(b.key))
}
