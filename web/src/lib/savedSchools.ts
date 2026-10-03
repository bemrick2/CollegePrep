/** Schools the household is comparing. Kept in the browser until the backend models saved schools (CR-9). */
export const SAVED_SCHOOLS_KEY = 'pp-compare'
export const MAX_SAVED_SCHOOLS = 4

export function readSavedSchools(): string[] {
  try {
    const v = JSON.parse(localStorage.getItem(SAVED_SCHOOLS_KEY) ?? '[]')
    return Array.isArray(v) ? v.filter((x): x is string => typeof x === 'string').slice(0, MAX_SAVED_SCHOOLS) : []
  } catch {
    return []
  }
}

export function writeSavedSchools(keys: string[]) {
  try {
    localStorage.setItem(SAVED_SCHOOLS_KEY, JSON.stringify(keys.slice(0, MAX_SAVED_SCHOOLS)))
  } catch {
    // Private mode or blocked storage: the list lives for this page only.
  }
}

/** Sample family: three four-year schools with verified 2026-27 cost of attendance in the demo snapshot. */
export const SAMPLE_SCHOOLS = ['utk', 'ipeds-221847', 'ipeds-219976']
