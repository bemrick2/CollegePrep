import { useCallback, useEffect, useState } from 'react'
import { useApp } from '../../lib/app'
import { MAX_SAVED_SCHOOLS, readSavedSchools, writeSavedSchools } from '../../lib/savedSchools'

/**
 * The household's saved schools (CR-9). Live: household_saved_schools via save/remove RPCs, so the list follows
 * the family across devices and reaches the student. A student with no household keeps the list in this browser.
 */
const CHANGED = 'pp-saved-schools'
const announce = () => window.dispatchEvent(new Event(CHANGED))

export function useSavedSchools() {
  const { source, ctx, activeStudent } = useApp()
  const householdId = activeStudent?.household_id ?? ctx?.myStudent?.household_id ?? ctx?.households[0]?.id ?? null
  const [keys, setKeys] = useState<string[]>(() => (householdId ? [] : readSavedSchools()))
  const [loading, setLoading] = useState(!!householdId)
  const [error, setError] = useState<string | null>(null)
  // Primary target (CR-12): only where the source supports it and the family has a household.
  const canSetPrimary = !!householdId && source.supportsPrimarySchool
  const [primary, setPrimaryState] = useState<string | null>(null)

  const [version, setVersion] = useState(0)
  // Every screen's copy of the list stays in step: a change anywhere tells the others to re-read it.
  useEffect(() => {
    const on = () => setVersion((v) => v + 1)
    window.addEventListener(CHANGED, on)
    return () => window.removeEventListener(CHANGED, on)
  }, [])

  useEffect(() => {
    let live = true
    if (!householdId) {
      setKeys(readSavedSchools())
      setLoading(false)
      return
    }
    setLoading(true)
    Promise.all([source.savedSchools(householdId), source.supportsPrimarySchool ? source.primarySchool(householdId) : Promise.resolve(null)]).then(
      ([k, p]) => live && (setKeys(k), setPrimaryState(p && k.includes(p) ? p : null), setLoading(false)),
      (e: Error) => live && (setError(e.message), setLoading(false)),
    )
    return () => {
      live = false
    }
  }, [source, householdId, version])

  const add = useCallback(
    async (key: string) => {
      if (keys.includes(key) || keys.length >= MAX_SAVED_SCHOOLS) return
      const next = [...keys, key]
      setKeys(next)
      setError(null)
      try {
        if (householdId) await source.saveSchool(householdId, key)
        else writeSavedSchools(next)
        announce()
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
        announce()
      } catch (e) {
        setKeys(keys)
        setError((e as Error).message)
      }
    },
    [keys, householdId, source],
  )

  const setPrimary = useCallback(
    async (key: string | null) => {
      if (!canSetPrimary || !householdId) return
      const prev = primary
      setPrimaryState(key)
      setError(null)
      try {
        await source.setPrimarySchool(householdId, key)
        announce()
      } catch (e) {
        setPrimaryState(prev)
        setError((e as Error).message)
      }
    },
    [canSetPrimary, householdId, primary, source],
  )

  return { keys, add, remove, loading, error, max: MAX_SAVED_SCHOOLS, primary: primary && keys.includes(primary) ? primary : null, setPrimary, canSetPrimary }
}
