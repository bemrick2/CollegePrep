import { useApp, useAsync } from '../../lib/app'
import type { InstitutionComparison } from '../../lib/data/types'
import { readSavedSchools } from '../../lib/savedSchools'

export const COMPARE_YEAR = '2026-27'

/** Verified comparison records for the household's saved schools. */
export function useSavedComparison(year = COMPARE_YEAR) {
  const { source } = useApp()
  const keys = readSavedSchools()
  return { keys, ...useAsync(() => (keys.length ? source.compareInstitutions(keys, year) : Promise.resolve([] as InstitutionComparison[])), [source, keys.join(','), year]) }
}
