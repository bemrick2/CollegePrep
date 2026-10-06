/** Full-page navigation to an external URL (Stripe Checkout or the Customer Portal). Separate for tests. */
export function redirectTo(url: string) {
  window.location.assign(url)
}
