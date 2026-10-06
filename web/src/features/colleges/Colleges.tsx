import { useEffect, useMemo, useState } from 'react'
import { useApp, useAsync } from '../../lib/app'
import type { InstitutionSearchHit } from '../../lib/data/types'
import { Notice, inputClass } from '../../components/ui'
import { MAX_SAVED_SCHOOLS } from '../../lib/savedSchools'
import { useSavedSchools } from './useSavedSchools'
import { COMPARE_YEAR } from './useSavedComparison'
import { CostOutlook } from '../parent/CostOutlook'
import { PageHeader, Section } from '../../components/layout'
import { CollegesTabs } from './CollegesTabs'
import { HomeStateControl } from './HomeStateControl'
import { useHomeState } from '../../lib/homeState'
import { stateName } from '../../lib/engine/residency'
import { useMeritReference } from './useMeritReference'

const MAX = MAX_SAVED_SCHOOLS

/** Colleges home: the saved list with the price that applies to the family, then adding schools. */
export function Colleges() {
  const { source, mode, activeStudent } = useApp()
  const merit = useMeritReference(activeStudent?.id)
  const year = COMPARE_YEAR
  const who = activeStudent?.display_name ?? 'your student'
  const saved = useSavedSchools()
  const keys = saved.keys
  const [query, setQuery] = useState('')

  // Suggestions: schools with at least one verified record for the selected year (CR-7).
  const suggestions = useAsync(() => source.verifiedSchools(year), [source, year])
  const [debounced, setDebounced] = useState('')
  useEffect(() => {
    const t = setTimeout(() => setDebounced(query), 250)
    return () => clearTimeout(t)
  }, [query])
  const [stateFilter, setStateFilter] = useState('')
  const results = useAsync(
    () => (debounced.trim().length >= 2 ? source.searchInstitutions(debounced, stateFilter || undefined) : Promise.resolve([] as InstitutionSearchHit[])),
    [source, debounced, stateFilter],
  )

  const add = (k: string) => {
    void saved.add(k)
    setQuery('')
  }

  const [showAll, setShowAll] = useState(false)
  const { homeState } = useHomeState()
  const states = useMemo(() => [...new Set((suggestions.data ?? []).map((x) => x.state_code).filter((x): x is string => !!x))].sort(), [suggestions.data])
  // Four-year schools with a verified cost record first: the main path is direct admission to a four-year college.
  const featuredAll = useMemo(
    () =>
      [...(suggestions.data ?? [])]
        .filter((x) => !stateFilter || x.state_code === stateFilter)
        .sort(
          (a, b) =>
            Number(b.level === 'four_year') - Number(a.level === 'four_year') ||
            Number(b.state_code === homeState) - Number(a.state_code === homeState) ||
            Number(!!b.domains?.includes('costs')) - Number(!!a.domains?.includes('costs')) ||
            a.display_name.localeCompare(b.display_name),
        ),
    [suggestions.data, stateFilter, homeState],
  )
  const featured = showAll ? featuredAll : featuredAll.slice(0, 12)

  return (
    <div className="grid grid-cols-1 gap-10">
      <PageHeader kicker="Colleges & cost" title="Your colleges" actions={<CollegesTabs />}>
        The schools {who} might apply to, with the published price that applies to your family. Open one for the full picture.
      </PageHeader>

      {keys.length > 0 && (
        <Section divider={false} title="Saved schools" subtitle={`${keys.length} of ${MAX} saved · ${COMPARE_YEAR} published prices`} action={<HomeStateControl />}>
          <CostOutlook showAlternative={merit.goals.includes('lower_cost')} />
        </Section>
      )}

      <Section divider={keys.length > 0} title={keys.length ? 'Add a school' : 'Start with the schools you might apply to'} subtitle="Search any college, or pick one with verified records.">
        <div className="grid gap-3">
        <label htmlFor="school-search" className="text-sm font-semibold text-ink">
          Add a school{' '}
          <span className="font-normal text-ink-3">
            ({keys.length}/{MAX})
          </span>
        </label>
        <div className="relative mt-1.5">
          <input
            id="school-search"
            className={inputClass}
            placeholder="Search by name"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={keys.length >= MAX}
            autoComplete="off"
            role="combobox"
            aria-expanded={!!results.data?.length}
            aria-controls="school-results"
          />
          {results.data && results.data.length > 0 && query.trim().length >= 2 && (
            <ul
              id="school-results"
              role="listbox"
              className="absolute z-20 mt-1 max-h-72 w-full overflow-auto rounded-xl border border-line bg-surface shadow-lift"
            >
              {results.data.map((r) => (
                <li key={r.institution_key} role="option" aria-selected={false}>
                  <button
                    className="flex w-full items-center justify-between gap-2 px-4 py-2.5 text-left text-sm hover:bg-surface-2"
                    onClick={() => add(r.institution_key)}
                  >
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
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="text-xs font-semibold text-ink-3">Schools with verified {year} records</div>
              {states.length > 1 && (
                <select
                  aria-label="Filter by state"
                  value={stateFilter}
                  onChange={(e) => setStateFilter(e.target.value)}
                  className="h-8 rounded-lg border border-line-strong bg-surface px-2 text-xs font-semibold"
                >
                  <option value="">All states ({states.length})</option>
                  {states.map((st) => (
                    <option key={st} value={st}>
                      {stateName(st)}
                    </option>
                  ))}
                </select>
              )}
            </div>
            <div className="mt-2 flex flex-wrap gap-1.5">
              {featured
                .filter((f) => !keys.includes(f.institution_key))
                .map((f) => (
                  <button
                    key={f.institution_key}
                    disabled={keys.length >= MAX}
                    onClick={() => add(f.institution_key)}
                    className="rounded-full border border-line-strong bg-surface px-3 py-1 text-xs font-semibold text-ink-2 hover:bg-surface-2 disabled:opacity-40"
                  >
                    + {f.display_name}
                  </button>
                ))}
              {featuredAll.length > 12 && (
                <button onClick={() => setShowAll((v) => !v)} className="px-2 py-1 text-xs font-semibold text-brand hover:underline">
                  {showAll ? 'Show fewer' : `Show all ${featuredAll.length}`}
                </button>
              )}
            </div>
          </div>
        )}
        {keys.length === 0 && <HomeStateControl className="mt-3" />}
        {saved.error && (
          <Notice tone="bad" className="mt-3">
            {saved.error}
          </Notice>
        )}
        {mode === 'demo' && (
          <p className="mt-3 text-xs text-ink-3">Demo uses a snapshot of verified records captured 2 Oct 2026. Signed-in accounts read the live database.</p>
        )}
        </div>
      </Section>
    </div>
  )
}
