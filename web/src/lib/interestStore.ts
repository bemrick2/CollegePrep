import { MAX_INTERESTS, type InterestProfile, type SavedInterest } from './engine/interests'

/**
 * The student's major certainty and saved interests. Kept in this browser until the backend stores them
 * (contract request CR-13); nothing here is sent anywhere.
 */
const KEY = (studentId: string) => `pp-interests:${studentId}`
export const EMPTY_PROFILE: InterestProfile = { certainty: null, interests: [] }

export function readInterests(studentId: string | null | undefined): InterestProfile {
  if (!studentId) return EMPTY_PROFILE
  try {
    const v = JSON.parse(localStorage.getItem(KEY(studentId)) ?? 'null') as InterestProfile | null
    if (!v || typeof v !== 'object') return EMPTY_PROFILE
    const interests = (Array.isArray(v.interests) ? v.interests : []).filter((i: SavedInterest) => i && (i.kind === 'area' || i.kind === 'major') && typeof i.key === 'string')
    return { certainty: ['unsure', 'few', 'sure'].includes(v.certainty as string) ? v.certainty : null, interests: interests.slice(0, MAX_INTERESTS) }
  } catch {
    return EMPTY_PROFILE
  }
}

export function writeInterests(studentId: string, p: InterestProfile) {
  try {
    localStorage.setItem(KEY(studentId), JSON.stringify({ certainty: p.certainty, interests: p.interests.slice(0, MAX_INTERESTS) }))
  } catch {
    /* storage unavailable: kept in memory for this page */
  }
}

/** Sample family: Maya is weighing three directions and hasn't ranked them. */
export const SAMPLE_INTERESTS: InterestProfile = {
  certainty: 'few',
  interests: [
    { kind: 'major', key: 'computer-science' },
    { kind: 'major', key: 'mechanical-eng' },
    { kind: 'major', key: 'finance' },
  ],
}
