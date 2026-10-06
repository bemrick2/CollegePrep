import { describe, expect, it } from 'vitest'
import { signupConfirmationUrl } from './authRedirect'

describe('signup confirmation redirects', () => {
  it('returns staging users to staging and preserves the parent onboarding choice', () => {
    expect(signupConfirmationUrl('https://college-optimizer-staging.netlify.app', false, 'parent'))
      .toBe('https://college-optimizer-staging.netlify.app/auth?role=parent')
  })
  it('uses the actual production origin without carrying a staging URL', () => {
    expect(signupConfirmationUrl('https://prepandprice.com', false, null)).toBe('https://prepandprice.com/auth')
  })
  it('permits localhost only in local development', () => {
    expect(signupConfirmationUrl('http://localhost:5173', true, 'student')).toBe('http://localhost:5173/auth?role=student')
    expect(() => signupConfirmationUrl('http://localhost:5173', false, null)).toThrow()
  })
  it('rejects insecure deployed origins and ignores arbitrary return destinations', () => {
    expect(() => signupConfirmationUrl('http://prepandprice.com', false, null)).toThrow()
    expect(signupConfirmationUrl('https://prepandprice.com', false, 'https://evil.example')).toBe('https://prepandprice.com/auth')
  })
})
