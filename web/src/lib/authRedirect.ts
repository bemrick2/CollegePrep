/** Email confirmations return to the deployment that started signup, never a hardcoded local URL. */
export function signupConfirmationUrl(origin: string, localDevelopment: boolean, role: string | null): string {
  const base = new URL(origin)
  const local = ['localhost', '127.0.0.1', '[::1]'].includes(base.hostname)
  if (local ? !localDevelopment : base.protocol !== 'https:') {
    throw new Error('Account confirmation requires HTTPS outside local development.')
  }
  const url = new URL('/auth', base.origin)
  if (role === 'parent' || role === 'student') url.searchParams.set('role', role)
  return url.toString()
}
