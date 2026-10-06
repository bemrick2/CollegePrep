// Pure billing logic shared by the Stripe edge functions (no runtime imports, so it is unit-tested from web/).
//
// Plans are identified in Stripe by price lookup keys, never by price ids, so prices can be changed in the
// Stripe dashboard without a deploy. One household plan ("family"), billed monthly or annually.

export const PLAN_LOOKUP_KEYS = ['pp_family_monthly', 'pp_family_annual'] as const
export type LookupKey = (typeof PLAN_LOOKUP_KEYS)[number]

export function isLookupKey(v: unknown): v is LookupKey {
  return typeof v === 'string' && (PLAN_LOOKUP_KEYS as readonly string[]).includes(v)
}

/** Our plan key for a Stripe price lookup key ("pp_family_annual" -> "family"). */
export function planKeyFor(lookupKey: string | null | undefined): string | null {
  const m = /^pp_([a-z0-9]+)_(monthly|annual)$/.exec(lookupKey ?? '')
  return m ? m[1]! : null
}

/** Stripe subscription statuses all exist in our normalised set (see the CR-16 migration). */
const STRIPE_STATUSES = ['trialing', 'active', 'past_due', 'canceled', 'incomplete', 'incomplete_expired', 'unpaid', 'paused'] as const
export type StripeStatus = (typeof STRIPE_STATUSES)[number]
export function normaliseStripeStatus(s: string): StripeStatus {
  if ((STRIPE_STATUSES as readonly string[]).includes(s)) return s as StripeStatus
  throw new Error(`Unknown Stripe subscription status: ${s}`)
}

/** Statuses that grant access (past_due keeps access while Stripe retries the payment). */
export const ACCESS_STATUSES = ['trialing', 'active', 'past_due', 'grace', 'billing_retry']

/** Events that can change a household's entitlement. Everything else is logged and acknowledged. */
export const HANDLED_EVENTS = new Set([
  'checkout.session.completed',
  'customer.subscription.created',
  'customer.subscription.updated',
  'customer.subscription.deleted',
  'customer.subscription.paused',
  'customer.subscription.resumed',
  'invoice.paid',
  'invoice.payment_failed',
  'invoice.payment_action_required',
])

type Obj = Record<string, unknown>
const obj = (v: unknown): Obj => (v && typeof v === 'object' ? (v as Obj) : {})
const str = (v: unknown): string | null => (typeof v === 'string' && v ? v : v && typeof v === 'object' && typeof (v as Obj).id === 'string' ? ((v as Obj).id as string) : null)

/** The subscription an event is about, across the shapes Stripe API versions use. */
export function subscriptionIdFromEvent(event: { type: string; data: { object: unknown } }): string | null {
  const o = obj(event.data.object)
  if (event.type.startsWith('customer.subscription.')) return str(o.id)
  if (event.type === 'checkout.session.completed') return o.mode === 'subscription' ? str(o.subscription) : null
  if (event.type.startsWith('invoice.')) {
    // Older API versions: invoice.subscription. Newer: invoice.parent.subscription_details.subscription.
    return str(o.subscription) ?? str(obj(obj(o.parent).subscription_details).subscription)
  }
  return null
}

export interface SubscriptionRow {
  household_id: string | null
  owner_user_id: string | null
  plan_key: string | null
  status: StripeStatus
  provider: 'stripe'
  provider_customer_id: string | null
  provider_subscription_id: string
  current_period_start: string | null
  current_period_end: string | null
  cancel_at_period_end: boolean
  environment: 'production' | 'sandbox'
}

const iso = (sec: unknown) => (typeof sec === 'number' ? new Date(sec * 1000).toISOString() : null)

/**
 * Our row from a freshly retrieved Stripe subscription. Always derived from the subscription's current state
 * (never from the event payload), so out-of-order or repeated events converge on the same result.
 */
export function subscriptionRow(sub: unknown): SubscriptionRow {
  const s = obj(sub)
  const meta = obj(s.metadata)
  const item = obj((obj(s.items).data as unknown[] | undefined)?.[0])
  const price = obj(item.price)
  return {
    household_id: str(meta.household_id),
    owner_user_id: str(meta.owner_user_id),
    plan_key: planKeyFor(price.lookup_key as string | undefined),
    status: normaliseStripeStatus(String(s.status)),
    provider: 'stripe',
    provider_customer_id: str(s.customer),
    provider_subscription_id: String(s.id),
    // Newer API versions moved the period to the subscription item.
    current_period_start: iso(s.current_period_start ?? item.current_period_start),
    current_period_end: iso(s.current_period_end ?? item.current_period_end),
    cancel_at_period_end: s.cancel_at_period_end === true,
    environment: s.livemode === true ? 'production' : 'sandbox',
  }
}

/** Only redirect back to our own site. */
export function siteUrl(raw: string | undefined): string {
  const u = new URL(raw ?? '')
  if (u.protocol !== 'https:' && u.hostname !== 'localhost') throw new Error('SITE_URL must be https')
  return u.origin
}
