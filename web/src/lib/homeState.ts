import { useEffect, useState } from 'react'
import { useApp } from './app'

/**
 * The family's home state: a user-entered assumption used to choose in-state or out-of-state published prices.
 * Kept in this browser until households store it (contract request CR-15).
 */
const KEY = (scope: string) => `pp-home-state:${scope}`
const EVENT = 'pp-home-state'

export function readHomeState(scope: string | null | undefined): string | null {
  if (!scope) return null
  try {
    return localStorage.getItem(KEY(scope))
  } catch {
    return null
  }
}

export function writeHomeState(scope: string, state: string | null) {
  try {
    if (state) localStorage.setItem(KEY(scope), state)
    else localStorage.removeItem(KEY(scope))
    window.dispatchEvent(new Event(EVENT))
  } catch {
    /* storage unavailable */
  }
}

/** Scope: the household when there is one, else the student's own profile. */
export function useHomeState() {
  const { ctx, activeStudent } = useApp()
  const scope = activeStudent?.household_id ?? ctx?.myStudent?.household_id ?? ctx?.households[0]?.id ?? ctx?.myStudent?.id ?? activeStudent?.id ?? null
  const [state, setState] = useState(() => readHomeState(scope))
  useEffect(() => {
    setState(readHomeState(scope))
    const on = () => setState(readHomeState(scope))
    window.addEventListener(EVENT, on)
    return () => window.removeEventListener(EVENT, on)
  }, [scope])
  return { homeState: state, setHomeState: (s: string | null) => scope && writeHomeState(scope, s), scope }
}
