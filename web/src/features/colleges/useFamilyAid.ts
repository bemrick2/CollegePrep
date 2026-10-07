import { useCallback, useEffect, useState } from 'react'
import type { FamilyAid } from '../../lib/engine/costProjection'

/**
 * Numbers the family types in for the savings view: grants or scholarships they have actually been offered and
 * planned borrowing (per school), and credit the student will bring from elsewhere. Their own figures, never
 * research data. Kept on this device; no backend stores them yet.
 */
export interface FamilyEntries {
  /** Dual-enrollment or transfer credit from outside the school. */
  otherCredits: number
  bySchool: Record<string, FamilyAid>
}

const KEY = (studentId: string) => `pp-family-aid:${studentId}`
const EMPTY: FamilyEntries = { otherCredits: 0, bySchool: {} }
const clamp = (n: unknown, max: number) => (typeof n === 'number' && Number.isFinite(n) ? Math.min(Math.max(Math.round(n), 0), max) : null)

function read(studentId: string | undefined): FamilyEntries {
  if (!studentId) return EMPTY
  try {
    const v = JSON.parse(localStorage.getItem(KEY(studentId)) ?? 'null') as Partial<FamilyEntries> | null
    if (!v || typeof v !== 'object') return EMPTY
    const bySchool: Record<string, FamilyAid> = {}
    for (const [k, a] of Object.entries(v.bySchool ?? {}))
      if (a && typeof a === 'object') bySchool[k] = { grantsPerYear: clamp(a.grantsPerYear, 500_000), loansPerYear: clamp(a.loansPerYear, 500_000) }
    return { otherCredits: clamp(v.otherCredits, 90) ?? 0, bySchool }
  } catch {
    return EMPTY
  }
}

export function useFamilyAid(studentId: string | undefined) {
  const [entries, setEntries] = useState<FamilyEntries>(() => read(studentId))
  useEffect(() => setEntries(read(studentId)), [studentId])
  const write = useCallback(
    (next: FamilyEntries) => {
      setEntries(next)
      if (!studentId) return
      try {
        localStorage.setItem(KEY(studentId), JSON.stringify(next))
      } catch {
        /* storage unavailable: keep in memory */
      }
    },
    [studentId],
  )
  return {
    entries,
    aidFor: (key: string): FamilyAid => entries.bySchool[key] ?? { grantsPerYear: null, loansPerYear: null },
    setAid: (key: string, aid: Partial<FamilyAid>) =>
      write({ ...entries, bySchool: { ...entries.bySchool, [key]: { ...(entries.bySchool[key] ?? { grantsPerYear: null, loansPerYear: null }), ...aid } } }),
    setOtherCredits: (n: number) => write({ ...entries, otherCredits: clamp(n, 90) ?? 0 }),
  }
}
