import type { InstitutionComparison } from '../../lib/data/types'
import { costLevers, type CostLever } from '../../lib/engine/costLevers'
import { summarizeSchool, type CreditPolicy, type PlannedExam } from '../../lib/engine/examCredit'
import type { ReferenceScore } from '../../lib/engine/merit'

/** Cost levers for one compared school, from its verified domains. */
export function schoolLevers(c: InstitutionComparison, exams: PlannedExam[], exam: 'act' | 'sat', reference: ReferenceScore | null): CostLever[] {
  const policies = (c.domains.credit_policies ?? []) as unknown as CreditPolicy[]
  return costLevers({
    awards: c.domains.awards,
    creditPolicies: policies,
    appeals: c.domains.appeals as LeverAppeal[] | undefined,
    credit: exams.length ? summarizeSchool(policies, exams) : null,
    exam,
    reference,
    netPriceUrl: c.institution?.net_price_calculator_url ?? null,
  })
}

type LeverAppeal = { offered?: boolean | null; policy_url?: string | null; source_url?: string | null }
