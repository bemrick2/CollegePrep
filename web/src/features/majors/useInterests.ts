import { useCallback, useEffect, useState } from 'react'
import { useApp } from '../../lib/app'
import type { InterestProfile, MajorCertainty, SavedInterest } from '../../lib/engine/interests'
import { MAX_INTERESTS } from '../../lib/engine/interests'
import { EMPTY_PROFILE, readInterests } from '../../lib/interestStore'

const same = (a: SavedInterest, b: SavedInterest) => a.kind === b.kind && a.key === b.key
const EVENT = 'pp-interests'
/** Last known profile per student, so every screen shows the same answer without refetching. */
const cache = new Map<string, InterestProfile>()

/**
 * A student's interests (CR-13), from the data source: this browser in the demo, the household's account when
 * signed in. Every change is saved at once and shared by all screens.
 */
export function useInterests(studentId: string | null | undefined) {
  const { source } = useApp()
  const initial = () => (!studentId ? EMPTY_PROFILE : (cache.get(studentId) ?? (source.mode === 'demo' ? readInterests(studentId) : EMPTY_PROFILE)))
  const [profile, setProfile] = useState<InterestProfile>(initial)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    setProfile(initial())
    if (!studentId) return
    let live = true
    source.interests(studentId).then(
      (p) => {
        if (!live) return
        cache.set(studentId, p)
        setProfile(p)
      },
      () => undefined, // keep what we have; the screens work without interests
    )
    const onChange = () => cache.has(studentId) && setProfile(cache.get(studentId)!)
    window.addEventListener(EVENT, onChange)
    return () => {
      live = false
      window.removeEventListener(EVENT, onChange)
    }
  }, [studentId, source])

  const save = useCallback(
    (next: InterestProfile) => {
      if (!studentId) return setProfile(next)
      const before = cache.get(studentId) ?? profile
      cache.set(studentId, next)
      setProfile(next)
      setError(null)
      window.dispatchEvent(new Event(EVENT))
      source.saveInterests(studentId, next).catch((e: unknown) => {
        cache.set(studentId, before)
        setProfile(before)
        setError(e instanceof Error ? e.message : 'Could not save your interests')
        window.dispatchEvent(new Event(EVENT))
      })
    },
    [studentId, source, profile],
  )

  return {
    profile,
    error,
    max: MAX_INTERESTS,
    setCertainty: (c: MajorCertainty) => save({ ...profile, certainty: c }),
    has: (i: SavedInterest) => profile.interests.some((x) => same(x, i)),
    toggle: (i: SavedInterest) =>
      save({
        ...profile,
        interests: profile.interests.some((x) => same(x, i))
          ? profile.interests.filter((x) => !same(x, i))
          : profile.interests.length < MAX_INTERESTS
            ? [...profile.interests, { kind: i.kind, key: i.key }]
            : profile.interests,
      }),
    /** Focus is optional and exclusive; choosing it again clears it. */
    setFocus: (i: SavedInterest) => save({ ...profile, interests: profile.interests.map((x) => ({ ...x, focus: same(x, i) ? !x.focus : false })) }),
    replace: save,
  }
}

/** Test hook: forget cached profiles between renders of a fresh app. */
export function resetInterestCache() {
  cache.clear()
}
