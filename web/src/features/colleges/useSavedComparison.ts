import { useApp, useAsync } from '../../lib/app'
import type { InstitutionComparison } from '../../lib/data/types'
import { useSavedSchools } from './useSavedSchools'

export const COMPARE_YEAR = '2026-27'

/** Verified comparison records for the household's saved schools. */
export function useSavedComparison(year = COMPARE_YEAR) {
  const { source } = useApp()
  const saved = useSavedSchools()
  const cmp = useAsync(
    () => (saved.keys.length ? source.compareInstitutions(saved.keys, year) : Promise.resolve([] as InstitutionComparison[])),
    [source, saved.keys.join(','), year],
  )
  return { keys: saved.keys, ...cmp, loading: saved.loading || cmp.loading }
}
