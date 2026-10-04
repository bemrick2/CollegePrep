import { useCallback, useEffect, useState } from 'react'
import type { InterestProfile, MajorCertainty, SavedInterest } from '../../lib/engine/interests'
import { MAX_INTERESTS } from '../../lib/engine/interests'
import { readInterests, writeInterests } from '../../lib/interestStore'

const same = (a: SavedInterest, b: SavedInterest) => a.kind === b.kind && a.key === b.key

/** Live view of a student's interests; every change is saved at once and shared by all screens on this device. */
export function useInterests(studentId: string | null | undefined) {
  const [profile, setProfile] = useState<InterestProfile>(() => readInterests(studentId))
  useEffect(() => {
    setProfile(readInterests(studentId))
    const onChange = () => setProfile(readInterests(studentId))
    window.addEventListener('pp-interests', onChange)
    return () => window.removeEventListener('pp-interests', onChange)
  }, [studentId])

  const save = useCallback(
    (next: InterestProfile) => {
      setProfile(next)
      if (!studentId) return
      writeInterests(studentId, next)
      window.dispatchEvent(new Event('pp-interests'))
    },
    [studentId],
  )

  return {
    profile,
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
