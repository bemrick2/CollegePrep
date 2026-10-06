// POST { household_id, lookup_key } -> { url } of a Stripe Checkout Session for the household plan.
// Only a guardian with manage_billing may start it, and never while the household already has access.
import { ACCESS_STATUSES, isLookupKey } from '../_shared/billing.ts'
import { admin, canManageBilling, caller, cors, json, site, stripe } from '../_shared/runtime.ts'

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response(null, { headers: cors(req) })
  if (req.method !== 'POST') return json(req, { error: 'POST only' }, 405)
  const user = await caller(req)
  if (!user) return json(req, { error: 'Sign in first.' }, 401)
  const body = await req.json().catch(() => ({}))
  const householdId = typeof body.household_id === 'string' ? body.household_id : ''
  if (!householdId || !isLookupKey(body.lookup_key)) return json(req, { error: 'Unknown plan.' }, 400)

  const db = admin()
  if (!(await canManageBilling(db, householdId, user.id))) return json(req, { error: 'Only a guardian who manages billing can choose a plan.' }, 403)

  // No double charge: a household with access from any source (web, Apple, Google) is never sent to checkout.
  const { data: active } = await db
    .from('subscriptions')
    .select('id')
    .eq('household_id', householdId)
    .eq('environment', 'production')
    .in('status', ACCESS_STATUSES)
    .limit(1)
  if (active?.length) return json(req, { error: 'This household already has an active plan.' }, 409)

  const s = stripe()
  const [price] = (await s.prices.list({ lookup_keys: [body.lookup_key], active: true })).data
  if (!price) return json(req, { error: 'That plan is not available yet.' }, 503)

  // One Stripe customer per household, created once (idempotency key guards concurrent first checkouts).
  let { data: customer } = await db.from('billing_customers').select('provider_customer_id').eq('household_id', householdId).eq('provider', 'stripe').maybeSingle()
  if (!customer) {
    const c = await s.customers.create({ email: user.email ?? undefined, metadata: { household_id: householdId } }, { idempotencyKey: `pp-customer-${householdId}` })
    await db.from('billing_customers').upsert({ household_id: householdId, provider: 'stripe', provider_customer_id: c.id, created_by: user.id }, { onConflict: 'household_id,provider', ignoreDuplicates: true })
    ;({ data: customer } = await db.from('billing_customers').select('provider_customer_id').eq('household_id', householdId).eq('provider', 'stripe').single())
  }

  const meta = { household_id: householdId, owner_user_id: user.id }
  const base = site()
  const session = await s.checkout.sessions.create({
    mode: 'subscription',
    customer: customer!.provider_customer_id,
    client_reference_id: householdId,
    line_items: [{ price: price.id, quantity: 1 }],
    subscription_data: { metadata: meta },
    metadata: meta,
    allow_promotion_codes: Deno.env.get('STRIPE_ALLOW_PROMOTION_CODES') === 'true',
    automatic_tax: { enabled: Deno.env.get('STRIPE_AUTOMATIC_TAX') === 'true' },
    ...(Deno.env.get('STRIPE_AUTOMATIC_TAX') === 'true' ? { customer_update: { address: 'auto' as const } } : {}),
    success_url: `${base}/parent/household?billing=success`,
    cancel_url: `${base}/parent/household?billing=canceled`,
  })
  return json(req, { url: session.url })
})
