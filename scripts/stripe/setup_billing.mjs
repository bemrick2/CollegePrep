#!/usr/bin/env node
// One-time (idempotent) Stripe setup for Prep & Price, run by the account owner in their own terminal against
// the Prep & Price Stripe account. Never paste keys into chat or commit them.
//
//   export STRIPE_SECRET_KEY=sk_test_...        # test mode first; later sk_live_... for live
//   node scripts/stripe/setup_billing.mjs \
//     --monthly-cents 1499 --annual-cents 11900 --currency usd \
//     --site-url https://YOUR-SITE \
//     --webhook-url https://<project-ref>.supabase.co/functions/v1/stripe-webhook
//
// Creates (or reuses): the "Prep & Price Family Plan" product, monthly and annual prices with lookup keys
// pp_family_monthly / pp_family_annual, a Customer Portal configuration, and the webhook endpoint. Re-running
// with a new amount creates a new price and moves the lookup key to it (existing subscribers keep their price).
// The webhook signing secret is printed ONCE: put it straight into the Supabase secret STRIPE_WEBHOOK_SECRET.
const key = process.env.STRIPE_SECRET_KEY
const arg = (k) => {
  const i = process.argv.indexOf(`--${k}`)
  return i > 0 ? process.argv[i + 1] : undefined
}
if (!key) fail('Set STRIPE_SECRET_KEY in your shell (not in a file you commit).')
const monthly = Number(arg('monthly-cents'))
const annual = Number(arg('annual-cents'))
const currency = (arg('currency') ?? 'usd').toLowerCase()
const site = arg('site-url')
const webhookUrl = arg('webhook-url')
if (!Number.isInteger(monthly) || monthly <= 0 || !Number.isInteger(annual) || annual <= 0) fail('Pass --monthly-cents and --annual-cents (whole cents, e.g. 1499). Prices are your decision.')
if (!site?.startsWith('https://')) fail('Pass --site-url https://… (where Checkout and the portal return to).')
if (!webhookUrl?.startsWith('https://')) fail('Pass --webhook-url https://<project-ref>.supabase.co/functions/v1/stripe-webhook')

const EVENTS = [
  'checkout.session.completed',
  'customer.subscription.created',
  'customer.subscription.updated',
  'customer.subscription.deleted',
  'customer.subscription.paused',
  'customer.subscription.resumed',
  'invoice.paid',
  'invoice.payment_failed',
  'invoice.payment_action_required',
]

function fail(m) {
  console.error(m)
  process.exit(1)
}

function form(obj, prefix = '', out = new URLSearchParams()) {
  for (const [k, v] of Object.entries(obj)) {
    const name = prefix ? `${prefix}[${k}]` : k
    if (v === undefined) continue
    if (Array.isArray(v)) v.forEach((x, i) => (typeof x === 'object' ? form(x, `${name}[${i}]`, out) : out.append(`${name}[${i}]`, String(x))))
    else if (v && typeof v === 'object') form(v, name, out)
    else out.append(name, String(v))
  }
  return out
}

async function api(method, path, body) {
  const r = await fetch(`https://api.stripe.com/v1/${path}`, {
    method,
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/x-www-form-urlencoded' },
    body: body ? form(body) : undefined,
  })
  const j = await r.json()
  if (!r.ok) fail(`${method} ${path}: ${j.error?.message ?? r.status}`)
  return j
}

const mode = key.startsWith('sk_live') || key.startsWith('rk_live') ? 'LIVE' : 'TEST'
console.log(`Stripe ${mode} mode. Check the dashboard shows the Prep & Price account before continuing.`)

// Product: reuse the one our prices point at; product search is eventually consistent, so it is only a fallback.
const priced = (await api('GET', 'prices?lookup_keys[]=pp_family_monthly&lookup_keys[]=pp_family_annual')).data[0]
const found = priced ? { data: [await api('GET', `products/${priced.product}`)] } : await api('GET', `products/search?query=${encodeURIComponent("metadata['pp_plan']:'family'")}`)
const product =
  found.data[0] ??
  (await api('POST', 'products', {
    name: 'Prep & Price Family Plan',
    description: 'ACT/SAT practice and college cost planning for one household (parents and students).',
    metadata: { pp_plan: 'family' },
  }))
console.log(`Product ${product.id}`)

// Prices by lookup key
async function ensurePrice(lookup, amount, interval) {
  const existing = (await api('GET', `prices?lookup_keys[]=${lookup}&active=true`)).data[0]
  if (existing && existing.unit_amount === amount && existing.currency === currency && existing.recurring?.interval === interval) return existing
  const p = await api('POST', 'prices', {
    product: product.id,
    unit_amount: amount,
    currency,
    recurring: { interval },
    lookup_key: lookup,
    transfer_lookup_key: true,
    tax_behavior: 'exclusive',
    metadata: { pp_plan: 'family' },
  })
  if (existing) await api('POST', `prices/${existing.id}`, { active: false })
  return p
}
const pm = await ensurePrice('pp_family_monthly', monthly, 'month')
const pa = await ensurePrice('pp_family_annual', annual, 'year')
console.log(`Prices ${pm.id} (monthly) ${pa.id} (annual)`)

// Customer Portal configuration: update payment method, see invoices, switch monthly/annual, cancel at period end.
const mine = (await api('GET', 'billing_portal/configurations?limit=100')).data.find((c) => c.metadata?.pp_portal === 'family')
const portal = await api('POST', mine ? `billing_portal/configurations/${mine.id}` : 'billing_portal/configurations', {
  metadata: { pp_portal: 'family' },
  business_profile: { headline: 'Prep & Price billing' },
  default_return_url: `${site.replace(/\/$/, '')}/parent/household`,
  features: {
    customer_update: { enabled: true, allowed_updates: ['email', 'address'] },
    invoice_history: { enabled: true },
    payment_method_update: { enabled: true },
    subscription_cancel: { enabled: true, mode: 'at_period_end' },
    subscription_update: {
      enabled: true,
      default_allowed_updates: ['price'],
      proration_behavior: 'create_prorations',
      products: [{ product: product.id, prices: [pm.id, pa.id] }],
    },
  },
})
console.log(`Portal configuration ${portal.id}  ->  set Supabase secret STRIPE_PORTAL_CONFIGURATION_ID=${portal.id}`)

// Webhook endpoint
const hooks = (await api('GET', 'webhook_endpoints?limit=100')).data.filter((h) => h.url === webhookUrl)
if (hooks.length) {
  await api('POST', `webhook_endpoints/${hooks[0].id}`, { enabled_events: EVENTS })
  console.log(`Webhook ${hooks[0].id} already exists; events updated. Its signing secret is in the Stripe dashboard (Developers → Webhooks).`)
} else {
  const h = await api('POST', 'webhook_endpoints', { url: webhookUrl, enabled_events: EVENTS, description: 'Prep & Price household entitlement' })
  console.log(`Webhook ${h.id} created.`)
  console.log(`Signing secret (shown once): ${h.secret}`)
  console.log('Put it straight into the Supabase Edge Function secret STRIPE_WEBHOOK_SECRET. Do not paste it anywhere else.')
}
