/**
 * Which published cost of attendance applies to this family: an in-state price when the school is in the family's
 * home state, an out-of-state price otherwise. The home state is a user-entered assumption (the family tells us);
 * whether a student actually qualifies as a resident is decided by each state's and school's residency rules.
 */

export type ResidencyBasis =
  /** Home state known and the matching published price exists. */
  | 'matched'
  /** Home state unknown: the in-state (or all-students) price is shown and labelled as assumed. */
  | 'assumed_in_state'
  /** Out-of-state family, but the school publishes no out-of-state price; the price shown is not theirs. */
  | 'out_of_state_missing'

export interface CostLike {
  residency: string
  total_cost_of_attendance?: number | null
}

const ORDER_IN = ['in_state', 'in_district', 'not_applicable', 'out_of_state']
const ORDER_OUT = ['out_of_state', 'not_applicable']

export function pickCost<T extends CostLike>(costs: T[], schoolState: string | null | undefined, homeState: string | null | undefined): { cost: T | null; basis: ResidencyBasis } {
  const usable = costs.filter((c) => c.total_cost_of_attendance != null)
  const by = (order: string[]) => order.map((r) => usable.find((c) => c.residency === r)).find(Boolean) ?? null
  if (!usable.length) return { cost: null, basis: homeState ? 'matched' : 'assumed_in_state' }
  if (!homeState || !schoolState) return { cost: by(ORDER_IN), basis: homeState ? 'matched' : 'assumed_in_state' }
  if (homeState === schoolState) return { cost: by(ORDER_IN), basis: 'matched' }
  const out = by(ORDER_OUT)
  return out ? { cost: out, basis: 'matched' } : { cost: by(ORDER_IN), basis: 'out_of_state_missing' }
}

export const US_STATES: [string, string][] = [
  ['AL', 'Alabama'], ['AK', 'Alaska'], ['AZ', 'Arizona'], ['AR', 'Arkansas'], ['CA', 'California'], ['CO', 'Colorado'], ['CT', 'Connecticut'],
  ['DE', 'Delaware'], ['DC', 'District of Columbia'], ['FL', 'Florida'], ['GA', 'Georgia'], ['HI', 'Hawaii'], ['ID', 'Idaho'], ['IL', 'Illinois'],
  ['IN', 'Indiana'], ['IA', 'Iowa'], ['KS', 'Kansas'], ['KY', 'Kentucky'], ['LA', 'Louisiana'], ['ME', 'Maine'], ['MD', 'Maryland'],
  ['MA', 'Massachusetts'], ['MI', 'Michigan'], ['MN', 'Minnesota'], ['MS', 'Mississippi'], ['MO', 'Missouri'], ['MT', 'Montana'], ['NE', 'Nebraska'],
  ['NV', 'Nevada'], ['NH', 'New Hampshire'], ['NJ', 'New Jersey'], ['NM', 'New Mexico'], ['NY', 'New York'], ['NC', 'North Carolina'],
  ['ND', 'North Dakota'], ['OH', 'Ohio'], ['OK', 'Oklahoma'], ['OR', 'Oregon'], ['PA', 'Pennsylvania'], ['RI', 'Rhode Island'],
  ['SC', 'South Carolina'], ['SD', 'South Dakota'], ['TN', 'Tennessee'], ['TX', 'Texas'], ['UT', 'Utah'], ['VT', 'Vermont'], ['VA', 'Virginia'],
  ['WA', 'Washington'], ['WV', 'West Virginia'], ['WI', 'Wisconsin'], ['WY', 'Wyoming'],
]
export const stateName = (code: string | null | undefined) => US_STATES.find(([c]) => c === code)?.[1] ?? code ?? ''
