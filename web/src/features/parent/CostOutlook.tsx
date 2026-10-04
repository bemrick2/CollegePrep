import { Link } from 'react-router-dom'
import type { CostRecord, InstitutionComparison } from '../../lib/data/types'
import { useSavedComparison, COMPARE_YEAR } from '../colleges/useSavedComparison'
import { ArrowRight, Info, School, Wallet } from '../../components/icons'
import { ButtonLink, Card, CardHeader, Pill } from '../../components/ui'

const YEAR = COMPARE_YEAR
const YEARS: Partial<Record<string, number>> = { two_year: 2, four_year: 4 }
const usd = (n: number) => n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })
const RES_ORDER: Record<string, number> = { in_district: 0, in_state: 1, not_applicable: 2, out_of_state: 3 }
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
}

/** Only verified, published figures: the cheapest-residency cost of attendance x years, and the savings
 *  opportunities the school's own verified records list. No savings are estimated. */
export function outlookFor(c: InstitutionComparison): SchoolOutlook {
  const costs = [...((c.domains.costs ?? []) as unknown as CostRecord[])]
    .filter((x) => x.total_cost_of_attendance != null)
    .sort((a, b) => (RES_ORDER[a.residency] ?? 9) - (RES_ORDER[b.residency] ?? 9))
  const cost = costs[0] ?? null
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
  }
}

/**
 * The outlook leads with four-year options. A community-college start is an optional alternative: shown only
 * when the family asked for the lowest-cost route (goal "lower_cost") and has a two-year school saved, collapsed,
 * and labelled as an example scenario until a verified transfer/articulation path exists for the pair.
 */
export function CostOutlook({ showAlternative = false }: { showAlternative?: boolean }) {
  const cmp = useSavedComparison(YEAR)
  const keys = cmp.keys
  const rows = (cmp.data ?? [])
    .filter((c) => c.found)
    .map(outlookFor)
    .sort((a, b) => (a.level === 'two_year' ? 1 : 0) - (b.level === 'two_year' ? 1 : 0) || Number(b.key === cmp.primary) - Number(a.key === cmp.primary))
  const four = rows.filter((r) => r.level === 'four_year' && r.degreeTotal != null).sort((a, b) => a.degreeTotal! - b.degreeTotal!)
  const low = four[0]
  const high = four[four.length - 1]
  const two = rows.filter((r) => r.level === 'two_year' && r.annual != null).sort((a, b) => a.annual! - b.annual!)[0]
  // A transfer path is shown only as published prices for each leg, with the transfer itself flagged as unverified.
  const target = four[four.length - 1]
  const path =
    two && target && target.annual != null
      ? { start: two, finish: target, total: Math.round(two.annual! * 2 + target.annual * 2), direct: target.degreeTotal! }
      : null

  return (
    <Card className="overflow-hidden">
      <CardHeader
        title={<span className="flex items-center gap-2"><Wallet size={18} /> College cost outlook</span>}
        subtitle={`Published ${YEAR} cost of attendance for the schools you're comparing`}
      />
      {keys.length === 0 ? (
        <div className="grid gap-4 p-5 md:grid-cols-[1fr_auto] md:items-center">
          <p className="text-sm text-ink-2">Pick up to four schools to see their verified costs and the credit and scholarship options each one publishes.</p>
          <ButtonLink to="/colleges" variant="brand">
            <School size={18} /> Choose schools
          </ButtonLink>
        </div>
      ) : cmp.loading ? (
        <div className="p-5 text-sm text-ink-3">Loading verified costs…</div>
      ) : (
        <div className="grid gap-5 p-5">
          {low && high && low !== high && (
            <div className="rounded-2xl bg-go-soft p-4">
              <div className="text-xs font-semibold uppercase tracking-wide text-go">Biggest difference between your 4-year schools</div>
              <p className="mt-1 text-ink">
                <span className="font-semibold">{low.name}</span> costs{' '}
                <span className="display text-2xl font-semibold tabular text-go">{usd(high.degreeTotal! - low.degreeTotal!)}</span> less than{' '}
                <span className="font-semibold">{high.name}</span> over 4 years at published prices.
              </p>
            </div>
          )}
          <ul className="grid gap-3">
            {rows.map((r) => (
              <li key={r.key} className="rounded-2xl border border-line p-4">
                <div className="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1">
                  <span className="font-semibold text-ink">
                    {r.name}
                    {r.key === cmp.primary && <Pill tone="brand" className="ml-2 align-middle">Primary target</Pill>}
                  </span>
                  {r.degreeTotal != null ? (
                    <span className="display text-xl font-semibold tabular text-ink">{usd(r.degreeTotal)}</span>
                  ) : r.annual != null ? (
                    <span className="display text-xl font-semibold tabular text-ink">
                      {usd(r.annual)}
                      <span className="text-sm font-normal text-ink-3"> /yr</span>
                    </span>
                  ) : (
                    <span className="text-sm text-ink-3">No verified total yet</span>
                  )}
                </div>
                {r.annual != null && (
                  <p className="mt-0.5 text-xs text-ink-3">
                    {usd(r.annual)} a year, {RES_LABEL[r.residency ?? ''] ?? r.residency}
                    {r.level ? ` × ${YEARS[r.level]} years (${r.level === 'two_year' ? '2-year college' : '4-year degree'})` : ''}
                    {r.sourceUrl && (
                      <>
                        {' · '}
                        <a href={r.sourceUrl} target="_blank" rel="noreferrer" className="underline-offset-2 hover:underline">source</a>
                      </>
                    )}
                  </p>
                )}
                <div className="mt-2 flex flex-wrap gap-1.5">
                  {r.levers.map((l) => (
                    <Pill key={l} tone="go">{l}</Pill>
                  ))}
                  {r.meritAwards > 0 && <Pill tone="gold">{r.meritAwards} merit award{r.meritAwards === 1 ? '' : 's'}</Pill>}
                  {r.levers.length === 0 && r.meritAwards === 0 && <span className="text-xs text-ink-3">No verified credit or scholarship records yet</span>}
                </div>
              </li>
            ))}
          </ul>
          {showAlternative && path && path.total < path.direct && (
            <details className="group rounded-2xl border border-line bg-surface-2 p-4">
              <summary className="cursor-pointer list-none text-sm font-semibold text-ink">
                Alternative lower-cost path <span className="font-normal text-ink-3">· example scenario</span>
              </summary>
              <p className="mt-2 text-sm text-ink-2">
                2 years at {path.start.name}, then 2 at {path.finish.name}: <span className="font-semibold tabular text-ink">{usd(path.total)}</span> at published prices,
                vs {usd(path.direct)} for 4 years at {path.finish.name}.
              </p>
              <p className="mt-1.5 text-xs text-ink-3">
                Potential path — transfer agreement not yet verified. It is not a recommendation, and credits may not all transfer or count toward the same degree.
              </p>
            </details>
          )}
          <p className="flex gap-2 text-xs text-ink-3">
            <Info size={14} className="mt-0.5 shrink-0" />
            Sticker prices before grants and scholarships, at {YEAR} prices. Savings from credit and scholarships aren't estimated until we can source them.
          </p>
          <Link to="/colleges" className="inline-flex items-center gap-1 text-sm font-semibold text-brand hover:underline">
            Compare schools side by side <ArrowRight size={16} />
          </Link>
        </div>
      )}
    </Card>
  )
}
