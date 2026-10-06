import type { CostLever } from './costLevers'

export interface SchoolPlanInput {
  key: string
  name: string
  level: string | null
  /** Applicable published 4-year total for this family, or null. */
  total: number | null
  /** True only when `total` is the price that applies to the family. */
  comparable: boolean
  levers: CostLever[]
}

export interface PlanSummary {
  /** The school the headline cost is about: the family's top choice if it has an applicable price, else the
   *  lowest applicable 4-year total among saved schools. */
  headline: { key: string; name: string; total: number; why: 'top_choice' | 'lowest' } | null
  /** Why there's no headline number, when there isn't one. */
  missing: 'no_schools' | 'no_four_year' | 'no_applicable_price' | null
  opportunity: { key: string; school: string; lever: CostLever } | null
}

// Score improvement first (the plan's main lever), then credit, then everything else; one opportunity only.
const RANK: Record<string, number> = { 'merit-next:within_reach': 0, 'merit-met:on_track': 1, 'credit:on_track': 2, 'merit-next:stretch': 3, 'credit:available': 4, 'dual:available': 5, 'need:available': 6 }

export function planSummary(schools: SchoolPlanInput[], topChoice: string | null): PlanSummary {
  const four = schools.filter((s) => s.level !== 'two_year')
  const priced = four.filter((s) => s.comparable && s.total != null)
  const top = priced.find((s) => s.key === topChoice)
  const lowest = [...priced].sort((a, b) => a.total! - b.total!)[0]
  const pick = top ?? lowest
  const headline = pick ? { key: pick.key, name: pick.name, total: pick.total!, why: top ? ('top_choice' as const) : ('lowest' as const) } : null
  const missing = headline ? null : schools.length === 0 ? 'no_schools' : four.length === 0 ? 'no_four_year' : 'no_applicable_price'

  // The opportunity favours the headline school, then any other saved four-year school.
  const ordered = pick ? [pick, ...four.filter((s) => s.key !== pick.key)] : four
  let best: PlanSummary['opportunity'] = null
  let bestRank = Infinity
  ordered.forEach((s, i) => {
    for (const l of s.levers) {
      const r = (RANK[`${l.key}:${l.status}`] ?? Infinity) + i * 0.01
      if (r < bestRank) {
        bestRank = r
        best = { key: s.key, school: s.name, lever: l }
      }
    }
  })
  return { headline, missing, opportunity: best }
}
