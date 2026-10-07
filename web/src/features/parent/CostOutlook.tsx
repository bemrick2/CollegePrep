import { Link } from 'react-router-dom'
import type { CostRecord, InstitutionComparison } from '../../lib/data/types'
import { useSavedComparison, COMPARE_YEAR } from '../colleges/useSavedComparison'
import { pickCost, stateName, type ResidencyBasis } from '../../lib/engine/residency'
import { useHomeState } from '../../lib/homeState'
import { X } from '../../components/icons'
import { Pill } from '../../components/ui'

const YEAR = COMPARE_YEAR
const YEARS: Partial<Record<string, number>> = { two_year: 2, four_year: 4 }
const usd = (n: number) => n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })
const RES_LABEL: Record<string, string> = { in_district: 'in-district', in_state: 'in-state', not_applicable: 'all students', out_of_state: 'out-of-state' }
const LEVER_LABEL: Record<string, string> = { AP: 'AP credit', CLEP: 'CLEP credit', IB: 'IB credit', dual_enrollment: 'Dual enrollment', statewide_dual_credit: 'Statewide dual credit' }

export interface SchoolOutlook {
  key: string
  name: string
  annual: number | null
  residency: string | null
  level: 'two_year' | 'four_year' | 'less_than_two_year' | null
  /** Published annual cost x years to degree; null when the level is unknown (no guessing). */
  degreeTotal: number | null
  sourceUrl: string | null
  levers: string[]
  meritAwards: number
  /** How the price was chosen for this family (home state is a user-entered assumption). */
  basis: ResidencyBasis
  /** True only when this is the price that applies to the family (or the same for everyone). Only comparable
   *  rows enter cost ranking, differences or path math. */
  comparable: boolean
  /** The school's state, for "if you're a resident of …" wording when the home state is unknown. */
  schoolState: string | null
}

/**
 * Only verified, published figures. The price is the one that applies to the family's (stated) home state:
 * in-state for a home-state school, out-of-state otherwise. When that price isn't published there is no number
 * (never a substitute); when the home state is unknown, a public school's in-state price is kept but marked
 * not comparable. No savings are estimated.
 */
export function outlookFor(c: InstitutionComparison, homeState: string | null = null): SchoolOutlook {
  const picked = pickCost((c.domains.costs ?? []) as unknown as CostRecord[], c.institution?.state_code, homeState)
  const basis = picked.basis
  const cost = basis === 'out_of_state_missing' ? null : picked.cost
  const level = c.institution?.level ?? null
  const kinds = new Set(((c.domains.credit_policies ?? []) as { policy_kind?: string }[]).map((p) => p.policy_kind ?? ''))
  return {
    key: c.institution_key,
    name: c.institution?.display_name ?? c.institution_key,
    annual: cost?.total_cost_of_attendance ?? null,
    residency: cost?.residency ?? null,
    level,
    degreeTotal: cost?.total_cost_of_attendance != null && level && YEARS[level] ? Math.round(cost.total_cost_of_attendance * YEARS[level]!) : null,
    sourceUrl: cost?.source_url ?? null,
    levers: Object.keys(LEVER_LABEL).filter((k) => kinds.has(k)).map((k) => LEVER_LABEL[k]!),
    meritAwards: ((c.domains.awards ?? []) as { award_type?: string }[]).filter((a) => (a.award_type ?? '').includes('merit')).length,
    basis,
    comparable: cost?.total_cost_of_attendance != null && (basis === 'matched' || cost.residency === 'not_applicable'),
    schoolState: c.institution?.state_code ?? null,
  }
}

/** One wording for a school's applicable 4-year price, used everywhere a cost is shown. */
export function costPhrase(o: SchoolOutlook): { amount: string | null; label: string; note: string | null } {
  const res = o.residency === 'out_of_state' ? 'out-of-state ' : o.residency === 'in_state' || o.residency === 'in_district' ? 'in-state ' : ''
  if (o.basis === 'out_of_state_missing')
    return { amount: null, label: `No published out-of-state price for ${YEAR}`, note: 'We don’t substitute the in-state price, so this school is left out of cost comparisons.' }
  if (o.degreeTotal == null) return { amount: null, label: `No verified ${YEAR} cost of attendance yet`, note: null }
  const years = o.level ? YEARS[o.level] : 4
  return {
    amount: usd(o.degreeTotal),
    label: `published ${res}cost of attendance over ${years} years, before aid`,
    note: o.comparable ? null : `Applies if you live in ${stateName(o.schoolState) || 'its state'}; set your home state to compare it.`,
  }
}

/**
 * The outlook leads with four-year options. A community-college start is an optional alternative: shown only
 * when the family asked for the lowest-cost route (goal "lower_cost") and has a two-year school saved, collapsed,
 * and labelled as an example scenario until a verified transfer/articulation path exists for the pair.
 */
export function CostOutlook({ showAlternative = false }: { showAlternative?: boolean }) {
  const cmp = useSavedComparison(YEAR)
  const { homeState } = useHomeState()
  const rows = (cmp.data ?? [])
    .filter((c) => c.found)
    .map((c) => outlookFor(c, homeState))
    .sort((a, b) => (a.level === 'two_year' ? 1 : 0) - (b.level === 'two_year' ? 1 : 0) || Number(b.key === cmp.primary) - Number(a.key === cmp.primary))
  const four = rows.filter((r) => r.level === 'four_year' && r.degreeTotal != null && r.comparable).sort((a, b) => a.degreeTotal! - b.degreeTotal!)
  const low = four[0]
  const high = four[four.length - 1]
  const two = rows.filter((r) => r.level === 'two_year' && r.annual != null && r.comparable).sort((a, b) => a.annual! - b.annual!)[0]
  // A transfer path is shown only as published prices for each leg, with the transfer itself flagged as unverified.
  const target = four[four.length - 1]
  const path =
    two && target && target.annual != null ? { start: two, finish: target, total: Math.round(two.annual! * 2 + target.annual * 2), direct: target.degreeTotal! } : null

  if (cmp.keys.length === 0) return null
  if (cmp.loading && !cmp.data) return <p className="text-sm text-ink-3">Loading verified costs…</p>

  return (
    <div className="grid gap-6">
      {low && high && low !== high && (
        <div className="grid gap-1">
          <div className="figure text-[36px] text-ink md:text-[44px]">{usd(high.degreeTotal! - low.degreeTotal!)}</div>
          <p className="text-[15px] text-ink-2">
            Biggest difference between your 4-year schools: <span className="font-semibold text-ink">{low.name}</span> costs that much less than{' '}
            <span className="font-semibold text-ink">{high.name}</span> over 4 years at published prices.
          </p>
        </div>
      )}
      {rows.some((r) => r.level === 'four_year' && !r.comparable) && four.length < 2 && (
        <p className="text-sm text-ink-3">Cost differences appear once at least two 4-year schools have the price that applies to you.</p>
      )}
      <ul className="divide-y divide-line border-y border-line">
        {rows.map((r) => (
          <li key={r.key} className="flex flex-wrap items-start justify-between gap-x-6 gap-y-2 py-4">
            <div className="min-w-0 flex-1">
              <Link to={`/colleges/${encodeURIComponent(r.key)}`} className="font-semibold text-ink hover:underline">
                {r.name}
              </Link>
              {r.key === cmp.primary && <Pill tone="brand" className="ml-2 align-middle">Top choice</Pill>}
              {r.annual != null && (
                <p className="mt-0.5 text-sm text-ink-3">
                  {usd(r.annual)} a year, {RES_LABEL[r.residency ?? ''] ?? r.residency}
                  {!r.comparable && r.basis === 'assumed_in_state' ? ' (if in-state)' : ''}
                  {r.level ? ` × ${YEARS[r.level]} years` : ''}
                  {r.sourceUrl && (
                    <>
                      {' · '}
                      <a href={r.sourceUrl} target="_blank" rel="noreferrer" className="underline-offset-2 hover:underline">source</a>
                    </>
                  )}
                </p>
              )}
              {r.basis === 'out_of_state_missing' && (
                <p className="mt-0.5 text-sm text-ink-3">{r.name} publishes only an in-state price for {YEAR}. We don't substitute it, so this school is left out of the cost comparison.</p>
              )}
              {!r.comparable && r.basis === 'assumed_in_state' && r.annual != null && (
                <p className="mt-0.5 text-sm text-warn">Shown if you live in {stateName(r.schoolState) || 'its state'}. Set your home state to include it in the comparison.</p>
              )}
              <p className="mt-1 text-sm text-ink-2">
                {[...r.levers, r.meritAwards > 0 ? `${r.meritAwards} merit award${r.meritAwards === 1 ? '' : 's'}` : null].filter(Boolean).join(' · ') || <span className="text-ink-3">No verified credit or scholarship records yet</span>}
              </p>
            </div>
            <div className="flex items-start gap-3">
              <div className="text-right">
                {r.degreeTotal != null ? (
                  <span className="text-xl font-bold tabular text-ink">{usd(r.degreeTotal)}</span>
                ) : r.basis === 'out_of_state_missing' ? (
                  <span className="text-sm text-ink-3">No out-of-state price published</span>
                ) : (
                  <span className="text-sm text-ink-3">No verified total yet</span>
                )}
              </div>
              <button type="button" onClick={() => void cmp.remove(r.key)} aria-label={`Remove ${r.name}`} className="grid h-8 w-8 place-items-center rounded-full text-ink-3 hover:bg-surface-2 hover:text-ink">
                <X size={16} />
              </button>
            </div>
          </li>
        ))}
      </ul>
      {showAlternative && path && path.total < path.direct && (
        <details className="group rounded-xl border border-line bg-surface p-4">
          <summary className="cursor-pointer list-none text-sm font-semibold text-ink">
            Alternative lower-cost path <span className="font-normal text-ink-3">· example scenario</span>
          </summary>
          <p className="mt-2 text-sm text-ink-2">
            2 years at {path.start.name}, then 2 at {path.finish.name}: <span className="font-semibold tabular text-ink">{usd(path.total)}</span> at published prices, vs{' '}
            {usd(path.direct)} for 4 years at {path.finish.name}.
          </p>
          <p className="mt-1.5 text-xs text-ink-3">
            Potential path — transfer agreement not yet verified. It is not a recommendation, and credits may not all transfer or count toward the same degree.
          </p>
        </details>
      )}
      <p className="text-xs text-ink-3">
        Sticker prices before grants and scholarships, at {YEAR} prices.{' '}
        <Link to="/colleges/savings" className="font-semibold text-go-strong underline dark:text-go">
          See cost & savings
        </Link>{' '}
        for tuition, fees and living costs apart, credit each school's rules allow, and your own grant and loan numbers.
      </p>
    </div>
  )
}
