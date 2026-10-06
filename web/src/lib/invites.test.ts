import { describe, expect, it } from 'vitest'
import { INVITE_TTL_HOURS, clearPendingInvite, formatInviteCode, inviteExpiry, inviteFailure, inviteFailureCopy, inviteLink, parseInviteInput, readPendingInvite, savePendingInvite } from './invites'
import { initialMode } from './app'

describe('invitations', () => {
  it('names each backend failure separately (accept_household_invitation messages)', () => {
    expect(inviteFailure('Invalid invitation code')).toBe('invalid')
    expect(inviteFailure('Invitation has expired')).toBe('expired')
    expect(inviteFailure('Invitation has already been used')).toBe('used')
    expect(inviteFailure('Invitation has been revoked')).toBe('revoked')
    expect(inviteFailure('Too many invite code attempts; try again in 15 minutes')).toBe('rate_limited')
    expect(inviteFailure('You are already a member of this household')).toBe('already_member')
    expect(inviteFailure('This student profile is already linked to another account')).toBe('already_linked')
    expect(inviteFailure('Authentication required')).toBe('signed_out')
    const titles = (['invalid', 'expired', 'used', 'revoked', 'rate_limited'] as const).map((k) => inviteFailureCopy(k, '', false).title)
    expect(new Set(titles).size).toBe(5)
    expect(inviteFailureCopy('invalid', '', true).body).toMatch(/only work in the browser that created them/)
  })

  it('accepts an invite code, a bare token, or a pasted link (fragment or the older query form)', () => {
    const token = 'a'.repeat(64)
    expect(parseInviteInput(`  ${token} `)).toBe(token)
    expect(parseInviteInput(inviteLink(token, 'https://staging.example'))).toBe(token)
    expect(parseInviteInput(`https://x.test/join?code=${token}`)).toBe(token)
    expect(inviteLink(token, 'https://x.test')).toBe(`https://x.test/join#t=${token}`)
    expect(parseInviteInput(' k7m4p-9q2tx ')).toBe('k7m4p-9q2tx')
    expect(formatInviteCode('k7m4p9q2tx')).toBe('K7M4P-9Q2TX')
  })

  it('remembers an invite link across sign-up and email confirmation, for 72 hours at most', () => {
    const token = 'b'.repeat(64)
    savePendingInvite(token, 0)
    expect(readPendingInvite(1000)).toBe(token)
    expect(readPendingInvite(INVITE_TTL_HOURS * 3_600_000 + 1)).toBeNull()
    savePendingInvite(token)
    clearPendingInvite()
    expect(readPendingInvite()).toBeNull()
  })

  it('states the requested lifetime', () => {
    const t = new Date('2026-10-06T10:00:00Z')
    expect(INVITE_TTL_HOURS).toBe(72)
    expect(inviteExpiry(t).toISOString()).toBe('2026-10-09T10:00:00.000Z')
  })

  it('a fresh browser uses the real backend whenever one is configured (regression: second-device invite)', () => {
    expect(initialMode(true, null)).toBe('live') // new browser / private window
    expect(initialMode(true, 'live')).toBe('live')
    expect(initialMode(true, 'demo')).toBe('demo') // only an explicit demo choice stays in demo
    expect(initialMode(false, null)).toBe('demo')
    expect(initialMode(false, 'live')).toBe('demo')
  })
})
