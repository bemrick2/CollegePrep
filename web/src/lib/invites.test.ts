import { describe, expect, it } from 'vitest'
import { INVITE_TTL_HOURS, inviteExpiry, inviteFailure, inviteFailureCopy, inviteLink, parseInviteInput } from './invites'
import { initialMode } from './app'

describe('invitations', () => {
  it('names each backend failure separately (accept_household_invitation messages)', () => {
    expect(inviteFailure('Invalid invitation code')).toBe('invalid')
    expect(inviteFailure('Invitation has expired')).toBe('expired')
    expect(inviteFailure('Invitation has already been used')).toBe('used')
    expect(inviteFailure('Invitation has been revoked')).toBe('revoked')
    expect(inviteFailure('You are already a member of this household')).toBe('already_member')
    expect(inviteFailure('This student profile is already linked to another account')).toBe('already_linked')
    expect(inviteFailure('Authentication required')).toBe('signed_out')
    const titles = (['invalid', 'expired', 'used', 'revoked'] as const).map((k) => inviteFailureCopy(k, '', false).title)
    expect(new Set(titles).size).toBe(4)
    expect(inviteFailureCopy('invalid', '', true).body).toMatch(/only work in the browser that created them/)
  })

  it('accepts a bare code or a pasted invite link', () => {
    const code = 'a'.repeat(64)
    expect(parseInviteInput(`  ${code} `)).toBe(code)
    expect(parseInviteInput(inviteLink(code, 'https://staging.example'))).toBe(code)
    expect(inviteLink(code, 'https://x.test')).toBe(`https://x.test/join?code=${code}`)
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
