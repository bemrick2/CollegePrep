import { useCallback, useEffect, useState } from 'react'
import { useApp } from '../../lib/app'
import { MAX_SAVED_SCHOOLS, readSavedSchools, writeSavedSchools } from '../../lib/savedSchools'

/**
 * The household's saved schools (CR-9). Live: household_saved_schools via save/remove RPCs, so the list follows
 * the family across devices and reaches the student. A student with no household keeps the list in this browser.
 */
export function useSavedSchools() {
  const { source, ctx, activeStudent } = useApp()
  const householdId = activeStudent?.household_id ?? ctx?.myStudent?.household_id ?? ctx?.households[0]?.id ?? null
  const [keys, setKeys] = useState<string[]>(() => (householdId ? [] : readSavedSchools()))
  const [loading, setLoading] = useState(!!householdId)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let live = true
    if (!householdId) {
      setKeys(readSavedSchools())
      setLoading(false)
      return
    }
    setLoading(true)
    source.savedSchools(householdId).then(
      (k) => live && (setKeys(k), setLoading(false)),
      (e: Error) => live && (setError(e.message), setLoading(false)),
    )
    return () => {
      live = false
    }
  }, [source, householdId])

  const add = useCallback(
    async (key: string) => {
      if (keys.includes(key) || keys.length >= MAX_SAVED_SCHOOLS) return
      const next = [...keys, key]
      setKeys(next)
      setError(null)
      try {
        if (householdId) await source.saveSchool(householdId, key)
        else writeSavedSchools(next)
      } catch (e) {
        setKeys(keys)
        setError((e as Error).message)
      }
    },
    [keys, householdId, source],
  )

  const remove = useCallback(
    async (key: string) => {
      const next = keys.filter((k) => k !== key)
      setKeys(next)
      setError(null)
      try {
        if (householdId) await source.removeSchool(householdId, key)
        else writeSavedSchools(next)
      } catch (e) {
        setKeys(keys)
        setError((e as Error).message)
      }
    },
    [keys, householdId, source],
  )

  return { keys, add, remove, loading, error, max: MAX_SAVED_SCHOOLS }
}
