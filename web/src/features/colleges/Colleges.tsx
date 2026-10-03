import { useEffect, useMemo, useState } from 'react'
import { useApp, useAsync } from '../../lib/app'
import type { CostRecord, InstitutionComparison, InstitutionSearchHit } from '../../lib/data/types'
import { Card, EmptyState, Notice, PageLoading, Pill, Segmented, cx, inputClass } from '../../components/ui'
import { Info, School, X } from '../../components/icons'
import { formatShortDate } from '../../lib/engine/dates'
import { MAX_SAVED_SCHOOLS, readSavedSchools, writeSavedSchools } from '../../lib/savedSchools'

const usd = (n: number | null | undefined) => (n == null ? null : n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }))
const YEARS = ['2026-27', '2025-26']
const MAX = MAX_SAVED_SCHOOLS

const RESIDENCY_LABEL: Record<string, string> = { in_state: 'In-state', out_of_state: 'Out-of-state', not_applicable: 'All students', in_district: 'In-district' }
const RES_ORDER: Record<string, number> = { in_district: 0, in_state: 1, not_applicable: 2, out_of_state: 3 }
const POLICY_LABEL: Record<string, string> = { AP: 'AP', CLEP: 'CLEP', IB: 'IB', cambridge_international: 'Cambridge', dual_enrollment: 'Dual enrollment', statewide_dual_credit: 'Statewide dual credit', industry_certification: 'Industry certification' }
const humanize = (k: string) => { const s = k.replace(/_/g, ' '); return s.charAt(0).toUpperCase() + s.slice(1) }
const CONTROL_LABEL: Record<string, string> = { public: 'Public', private_nonprofit: 'Private nonprofit', private_for_profit: 'Private for-profit' }
const DOMAIN_LABEL: Record<string, string> = {
  costs: 'Cost of attendance',
  admissions_metrics: 'Admissions',
  awards: 'Scholarships',
  credit_policies: 'AP / CLEP / IB credit',
  transfer_policies: 'Transfer credit',
  academic_programs: 'Programs',
  degree_requirements: 'Degree maps',
  appeals: 'Aid appeals',
}


export function Colleges() {
  const { source, mode } = useApp()
  const [year, setYear] = useState(YEARS[0]!)
  const [keys, setKeys] = useState<string[]>(readSavedSchools)
  const [query, setQuery] = useState('')
  const [years, setYearsInSchool] = useState(4)

  useEffect(() => {
    writeSavedSchools(keys)
  }, [keys])

  const suggestions = useAsync(() => source.searchInstitutions(''), [source])
  const [debounced, setDebounced] = useState('')
  useEffect(() => {
    const t = setTimeout(() => setDebounced(query), 250)
    return () => clearTimeout(t)
  }, [query])
  const results = useAsync(() => (debounced.trim().length >= 2 ? source.searchInstitutions(debounced) : Promise.resolve([] as InstitutionSearchHit[])), [source, debounced])
  const cmp = useAsync(() => (keys.length ? source.compareInstitutions(keys, year) : Promise.resolve([] as InstitutionComparison[])), [source, keys.join(','), year])

  const add = (k: string) => {
    setKeys((ks) => (ks.includes(k) || ks.length >= MAX ? ks : [...ks, k]))
    setQuery('')
  }

  const featured = useMemo(() => (mode === 'demo' ? (suggestions.data ?? []) : []), [mode, suggestions.data])

  return (
    <div className="grid grid-cols-1 gap-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">Colleges & cost</p>
          <h1 className="display text-[30px] font-semibold leading-tight text-ink md:text-[36px]">Compare schools</h1>
          <p className="mt-1 max-w-2xl text-sm text-ink-2">Only verified records from official sources, for one academic year at a time. Blank means we haven't verified it yet — not that it doesn't exist.</p>
        </div>
        <Segmented label="Academic year" value={year} onChange={setYear} options={YEARS.map((y) => ({ value: y, label: y }))} />
      </div>

      <Card className="p-4">
        <label htmlFor="school-search" className="text-sm font-semibold text-ink">
          Add a school <span className="font-normal text-ink-3">({keys.length}/{MAX})</span>
        </label>
        <div className="relative mt-1.5">
          <input id="school-search" className={inputClass} placeholder="Search by name" value={query} onChange={(e) => setQuery(e.target.value)} disabled={keys.length >= MAX} autoComplete="off" role="combobox" aria-expanded={!!results.data?.length} aria-controls="school-results" />
          {results.data && results.data.length > 0 && query.trim().length >= 2 && (
            <ul id="school-results" role="listbox" className="absolute z-20 mt-1 max-h-72 w-full overflow-auto rounded-xl border border-line bg-surface shadow-lift">
              {results.data.map((r) => (
                <li key={r.institution_key} role="option" aria-selected={false}>
                  <button className="flex w-full items-center justify-between gap-2 px-4 py-2.5 text-left text-sm hover:bg-surface-2" onClick={() => add(r.institution_key)}>
                    <span className="font-semibold text-ink">{r.display_name}</span>
                    <span className="text-ink-3">{[r.city, r.state_code].filter(Boolean).join(', ')}</span>
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
        {featured.length > 0 && (
          <div className="mt-3">
            <div className="text-xs font-semibold text-ink-3">Schools with verified {YEARS[0]} records so far</div>
            <div className="mt-2 flex flex-wrap gap-1.5">
              {featured
                .filter((f) => !keys.includes(f.institution_key))
                .map((f) => (
                  <button key={f.institution_key} disabled={keys.length >= MAX} onClick={() => add(f.institution_key)} className="rounded-full border border-line-strong bg-surface px-3 py-1 text-xs font-semibold text-ink-2 hover:bg-surface-2 disabled:opacity-40">
                    + {f.display_name}
                  </button>
                ))}
            </div>
          </div>
        )}
        {mode === 'demo' && <p className="mt-3 text-xs text-ink-3">Demo uses a snapshot of verified records captured 2 Oct 2026. Signed-in accounts read the live database.</p>}
      </Card>

      {keys.length === 0 ? (
        <Card>
          <EmptyState icon={<School size={32} />} title="Pick up to four schools">
            You'll see verified cost of attendance, scholarships, credit policies and aid-appeal options side by side.
          </EmptyState>
        </Card>
      ) : cmp.loading && !cmp.data ? (
        <PageLoading />
      ) : cmp.error ? (
        <Notice tone="bad">{cmp.error.message}</Notice>
      ) : (
        <>
          <div className="flex flex-wrap items-center gap-3 text-sm">
            <span className="font-semibold text-ink">Years to degree</span>
            <Segmented label="Years to degree" value={years} onChange={setYearsInSchool} options={[3, 3.5, 4, 5].map((y) => ({ value: y, label: String(y) }))} />
            <span className="text-xs text-ink-3">AP, CLEP and dual-enrollment credit can shorten time to degree.</span>
          </div>
          <div className={cx('grid gap-4', keys.length > 1 && 'md:grid-cols-2', keys.length === 3 && 'xl:grid-cols-3', keys.length >= 4 && 'xl:grid-cols-4', 'items-start')}>
            {cmp.data!.map((c) => (
              <SchoolColumn key={c.institution_key} c={c} years={years} onRemove={() => setKeys((ks) => ks.filter((k) => k !== c.institution_key))} />
            ))}
          </div>
          <Notice tone="neutral" title="How to read this">
            Totals are each school's published cost of attendance multiplied by years to degree, at {year} prices. They are sticker prices: before grants, scholarships and future price changes. Net price depends on your family's finances — use each school's net price calculator.
          </Notice>
        </>
      )}
    </div>
  )
}

function SchoolColumn({ c, years, onRemove }: { c: InstitutionComparison; years: number; onRemove: () => void }) {
  const inst = c.institution
  const costs = [...((c.domains.costs ?? []) as unknown as CostRecord[])].sort((a, b) => (RES_ORDER[a.residency] ?? 9) - (RES_ORDER[b.residency] ?? 9))
  const awards = (c.domains.awards ?? []) as Record<string, unknown>[]
  const credit = (c.domains.credit_policies ?? []) as Record<string, unknown>[]
  const adm = (c.domains.admissions_metrics?.[0] ?? null) as Record<string, number | string | null> | null
  const appeals = (c.domains.appeals ?? []) as Record<string, unknown>[]
  const [residency, setResidency] = useState(costs.find((x) => x.residency === 'in_state')?.residency ?? costs[0]?.residency ?? '')
  const cost = costs.find((x) => x.residency === residency) ?? costs[0]

  return (
    <Card as="article" className="flex flex-col">
      <div className="flex items-start gap-3 border-b border-line p-5">
        <div className="min-w-0 flex-1">
          <h2 className="display text-xl font-semibold leading-tight text-ink">{inst?.display_name ?? c.institution_key}</h2>
          <p className="mt-0.5 text-sm text-ink-3">{inst ? [inst.city, inst.state_code, inst.control && CONTROL_LABEL[inst.control]].filter(Boolean).join(' · ') : 'Not found'}</p>
        </div>
        <button onClick={onRemove} className="grid h-8 w-8 place-items-center rounded-full text-ink-3 hover:bg-surface-2 hover:text-ink" aria-label={`Remove ${inst?.display_name ?? c.institution_key}`}>
          <X size={16} />
        </button>
      </div>

      {!c.found ? (
        <div className="p-5 text-sm text-ink-3">No verified identity for this school.</div>
      ) : (
        <div className="grid flex-1 gap-0 divide-y divide-line">
          <Section title="Cost of attendance" source={cost?.source_url} verified={cost?.last_verified_at}>
            {costs.length === 0 ? (
              <Missing />
            ) : (
              <>
                {costs.length > 1 && (
                  <div className="mb-3">
                    <Segmented label="Residency" value={residency} onChange={setResidency} options={costs.map((x) => ({ value: x.residency, label: RESIDENCY_LABEL[x.residency] ?? x.residency }))} />
                  </div>
                )}
                {cost && (
                  <>
                    <div className="flex items-baseline justify-between gap-2">
                      <span className="text-sm text-ink-2">Per year</span>
                      <span className="display text-2xl font-semibold tabular text-ink">{usd(cost.total_cost_of_attendance) ?? <span className="text-base text-ink-3">Total not published</span>}</span>
                    </div>
                    {cost.total_cost_of_attendance != null && (
                      <div className="mt-1 flex items-baseline justify-between gap-2">
                        <span className="text-sm text-ink-2">{years} years, sticker</span>
                        <span className="text-lg font-semibold tabular text-brand">{usd(Math.round(cost.total_cost_of_attendance * years))}</span>
                      </div>
                    )}
                    <dl className="mt-3 grid grid-cols-2 gap-x-4 gap-y-1 text-xs">
                      <Row k="Tuition" v={cost.tuition} />
                      <Row k="Fees" v={cost.mandatory_fees} />
                      <Row k="Housing & food" v={cost.on_campus_food_housing ?? (cost.room != null && cost.board != null ? cost.room + cost.board : null)} />
                      <Row k="Books" v={cost.books_supplies} />
                      <Row k="Transport" v={cost.transportation} />
                      <Row k="Personal" v={cost.personal_misc} />
                    </dl>
                  </>
                )}
              </>
            )}
          </Section>

          <Section title="Admissions (middle 50%)" source={adm?.source_url as string | undefined} verified={adm?.last_verified_at as string | undefined}>
            {!adm ? (
              <Missing />
            ) : (
              <dl className="grid grid-cols-2 gap-x-4 gap-y-1 text-sm">
                <Row k="ACT" text={adm.act_25 != null ? `${adm.act_25}–${adm.act_75}` : null} />
                <Row k="SAT" text={adm.sat_25 != null ? `${adm.sat_25}–${adm.sat_75}` : null} />
                <Row k="Admit rate" text={typeof adm.admit_rate === 'number' ? `${Math.round(adm.admit_rate <= 1 ? adm.admit_rate * 100 : adm.admit_rate)}%` : null} />
              </dl>
            )}
          </Section>

          <Section title="Scholarships" count={awards.length}>
            {awards.length === 0 ? (
              <Missing />
            ) : (
              <ul className="grid gap-2">
                {awards.slice(0, 5).map((a, i) => (
                  <li key={i} className="text-sm">
                    <a href={String(a.source_url)} target="_blank" rel="noreferrer" className="font-semibold text-ink hover:underline">
                      {String(a.award_name)}
                    </a>
                    <p className="line-clamp-2 text-xs text-ink-3">{a.award_amount_text ? String(a.award_amount_text) : usd(a.award_max as number) ?? 'Amount not published'}</p>
                  </li>
                ))}
                {awards.length > 5 && <li className="text-xs text-ink-3">+{awards.length - 5} more verified awards</li>}
              </ul>
            )}
          </Section>

          <Section title="Exam credit" count={credit.length}>
            {credit.length === 0 ? (
              <Missing />
            ) : (
              <div className="flex flex-wrap gap-1.5">
                {credit.map((p, i) => (
                  <a key={i} href={String(p.policy_url ?? p.source_url)} target="_blank" rel="noreferrer">
                    <Pill tone="brand">
                      {POLICY_LABEL[String(p.policy_kind)] ?? humanize(String(p.policy_kind))}
                      {typeof p.equivalency_count === 'number' && p.equivalency_count > 0 ? ` · ${p.equivalency_count} exams` : ''}
                    </Pill>
                  </a>
                ))}
              </div>
            )}
          </Section>

          <Section title="Financial-aid appeals" count={appeals.length}>
            {appeals.length === 0 ? (
              <Missing />
            ) : (
              <ul className="grid gap-1 text-sm">
                {appeals.slice(0, 4).map((a, i) => (
                  <li key={i} className="flex items-center gap-2">
                    <span className={cx('h-1.5 w-1.5 rounded-full', a.offered ? 'bg-go' : 'bg-ink-3')} aria-hidden />
                    <span className="text-ink-2">{humanize(String(a.appeal_kind))}</span>
                  </li>
                ))}
              </ul>
            )}
          </Section>

          {c.missing_domains.length > 0 && (
            <div className="p-5 text-xs text-ink-3">
              <Info size={14} className="mr-1 inline" /> Not yet verified for {c.academic_year}: {c.missing_domains.map((d) => DOMAIN_LABEL[d] ?? d).join(', ')}.
            </div>
          )}
          {inst?.net_price_calculator_url && (
            <a href={inst.net_price_calculator_url} target="_blank" rel="noreferrer" className="block p-5 text-sm font-semibold text-brand hover:underline">
              Net price calculator ↗
            </a>
          )}
        </div>
      )}
    </Card>
  )
}

function Section({ title, children, source, verified, count }: { title: string; children: React.ReactNode; source?: string | null; verified?: string | null; count?: number }) {
  return (
    <section className="p-5">
      <div className="mb-2 flex items-baseline justify-between gap-2">
        <h3 className="text-xs font-bold uppercase tracking-wide text-ink-3">
          {title}
          {count ? ` · ${count}` : ''}
        </h3>
        {source && (
          <a href={source} target="_blank" rel="noreferrer" className="text-[11px] font-semibold text-ink-3 hover:text-ink hover:underline" title={verified ? `Verified ${formatShortDate(verified)}` : undefined}>
            Source{verified ? ` · ${formatShortDate(verified)}` : ''} ↗
          </a>
        )}
      </div>
      {children}
    </section>
  )
}

function Row({ k, v, text }: { k: string; v?: number | null; text?: string | null }) {
  const val = text !== undefined ? text : usd(v)
  return (
    <>
      <dt className="text-ink-3">{k}</dt>
      <dd className={cx('text-right tabular', val ? 'font-semibold text-ink' : 'text-ink-3')}>{val ?? '—'}</dd>
    </>
  )
}

function Missing() {
  return <p className="text-sm italic text-ink-3">No verified record yet</p>
}
