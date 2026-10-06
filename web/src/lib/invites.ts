/**
 * Household invitations: one lifetime, one link format and one set of error messages for every screen.
 * The backend (create/accept_household_invitation) owns the rules; this only names them for people.
 */

/** Requested explicitly on every create so "valid for 72 hours" is a promise, not a default we hope holds. */
export const INVITE_TTL_HOURS = 72

export type InviteFailure = 'invalid' | 'expired' | 'used' | 'revoked' | 'already_member' | 'already_linked' | 'needs_profile' | 'signed_out' | 'other'

/** Classify the backend's (or demo's) error text. Matches the messages raised by accept_household_invitation. */
export function inviteFailure(message: string): InviteFailure {
  const m = message.toLowerCase()
  if (m.includes('already been used')) return 'used'
  if (m.includes('revoked')) return 'revoked'
  if (m.includes('expired')) return 'expired'
  if (m.includes('invalid invitation')) return 'invalid'
  if (m.includes('already a member')) return 'already_member'
  if (m.includes('already linked')) return 'already_linked'
  if (m.includes('create your student profile') || m.includes('leave your current household')) return 'needs_profile'
  if (m.includes('authentication required')) return 'signed_out'
  return 'other'
}

export function inviteFailureCopy(kind: InviteFailure, raw: string, demo: boolean): { title: string; body: string } {
  switch (kind) {
    case 'invalid':
      return demo
        ? { title: 'Invalid invitation', body: 'Demo codes only work in the browser that created them. To test with two devices, use real accounts (sign in) instead of the demo.' }
        : { title: 'Invalid invitation', body: 'We couldn’t find that code. Check that it was copied in full, or ask your parent or guardian for a new one.' }
    case 'expired':
      return { title: 'Invitation expired', body: `Codes are valid for ${INVITE_TTL_HOURS} hours. Ask your parent or guardian to create a new one.` }
    case 'used':
      return { title: 'Invitation already used', body: 'Each invitation works once, and this one has been used. If that wasn’t you, ask for a new one.' }
    case 'revoked':
      return { title: 'Invitation cancelled', body: 'Your parent or guardian cancelled this invitation or sent a newer one. Use the latest email, or ask for a new invitation.' }
    case 'already_member':
      return { title: 'Already joined', body: 'Your account is already part of this household.' }
    case 'already_linked':
      return { title: 'Profile already linked', body: raw }
    case 'needs_profile':
      return { title: 'One step first', body: raw }
    case 'signed_out':
      return { title: 'Sign in first', body: 'Sign in or create your account, then enter the code.' }
    default:
      return { title: 'That code didn’t work', body: raw }
  }
}

/** Accepts a bare code or a pasted invite link (…/join?code=…). */
export function parseInviteInput(input: string): string {
  const t = input.trim()
  const m = /[?&]code=([^&#\s]+)/.exec(t)
  return (m ? decodeURIComponent(m[1]!) : t).trim()
}

export function inviteLink(code: string, origin = typeof window !== 'undefined' ? window.location.origin : ''): string {
  return `${origin}/join?code=${encodeURIComponent(code)}`
}

export function inviteExpiry(createdAt: Date, hours = INVITE_TTL_HOURS): Date {
  return new Date(createdAt.getTime() + hours * 3_600_000)
}
