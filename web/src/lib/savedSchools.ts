/** Schools the household is comparing. Kept in the browser until the backend models saved schools (CR-9). */
export const SAVED_SCHOOLS_KEY = 'pp-compare'
/** Six fits two states' worth of options on the comparison; the backend allows eight. */
export const MAX_SAVED_SCHOOLS = 6

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

/** Demo only: the household's primary target school (CR-12 pending in live mode). */
export const PRIMARY_SCHOOL_KEY = 'pp-primary'

export function readPrimarySchool(): string | null {
  try {
    const v = localStorage.getItem(PRIMARY_SCHOOL_KEY)
    return v && readSavedSchools().includes(v) ? v : null
  } catch {
    return null
  }
}

export function writePrimarySchool(key: string | null) {
  try {
    if (key) localStorage.setItem(PRIMARY_SCHOOL_KEY, key)
    else localStorage.removeItem(PRIMARY_SCHOOL_KEY)
  } catch {
    // Storage blocked: no primary this session.
  }
}

/** Sample family: three four-year schools with verified 2026-27 cost of attendance in the demo snapshot. */
export const SAMPLE_SCHOOLS = ['utk', 'ipeds-221847', 'ipeds-219976']
