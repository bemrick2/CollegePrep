// Calendar helpers. Dates are ISO yyyy-mm-dd strings in a given IANA time zone.

export function browserTimeZone(): string {
  try {
    return Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC'
  } catch {
    return 'UTC'
  }
}

export function localDate(at: Date | string, timeZone: string): string {
  const d = typeof at === 'string' ? new Date(at) : at
  // en-CA formats as yyyy-mm-dd.
  return new Intl.DateTimeFormat('en-CA', { timeZone, year: 'numeric', month: '2-digit', day: '2-digit' }).format(d)
}

export function addDays(iso: string, days: number): string {
  const [y, m, d] = iso.split('-').map(Number) as [number, number, number]
  const t = new Date(Date.UTC(y, m - 1, d + days))
  return t.toISOString().slice(0, 10)
}

export function isoWeekday(iso: string): number {
  const [y, m, d] = iso.split('-').map(Number) as [number, number, number]
  const wd = new Date(Date.UTC(y, m - 1, d)).getUTCDay()
  return wd === 0 ? 7 : wd
}

/** Monday of the week containing the given local date. */
export function weekStartOf(iso: string): string {
  return addDays(iso, 1 - isoWeekday(iso))
}

export function daysBetween(a: string, b: string): number {
  const [y1, m1, d1] = a.split('-').map(Number) as [number, number, number]
  const [y2, m2, d2] = b.split('-').map(Number) as [number, number, number]
  return Math.round((Date.UTC(y2, m2 - 1, d2) - Date.UTC(y1, m1 - 1, d1)) / 86_400_000)
}

export function median(values: number[]): number | null {
  if (values.length === 0) return null
  const s = [...values].sort((x, y) => x - y)
  const mid = Math.floor(s.length / 2)
  // percentile_cont(0.5): mean of the two middle values for even counts.
  return s.length % 2 ? s[mid]! : (s[mid - 1]! + s[mid]!) / 2
}

export function formatDuration(ms: number): string {
  const total = Math.round(ms / 1000)
  const m = Math.floor(total / 60)
  const s = total % 60
  return m > 0 ? `${m}m ${s.toString().padStart(2, '0')}s` : `${s}s`
}

export function formatShortDate(iso: string): string {
  const [y, m, d] = iso.slice(0, 10).split('-').map(Number) as [number, number, number]
  return new Date(Date.UTC(y, m - 1, d)).toLocaleDateString(undefined, { month: 'short', day: 'numeric', timeZone: 'UTC' })
}
