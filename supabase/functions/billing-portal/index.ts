// POST { household_id } -> { url } of the Stripe Customer Portal for the household's web subscription.
import { billingEnvironment, admin, canManageBilling, caller, cors, json, site, stripe } from '../_shared/runtime.ts'

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response(null, { headers: cors(req) })
  if (req.method !== 'POST') return json(req, { error: 'POST only' }, 405)
  const user = await caller(req)
  if (!user) return json(req, { error: 'Sign in first.' }, 401)
  const body = await req.json().catch(() => ({}))
  const householdId = typeof body.household_id === 'string' ? body.household_id : ''
  const environment = billingEnvironment()
  const db = admin()
  if (!householdId || !(await canManageBilling(db, householdId, user.id))) return json(req, { error: 'Only a guardian who manages billing can open billing.' }, 403)
  const { data: customer } = await db.from('billing_customers').select('provider_customer_id').eq('household_id', householdId).eq('provider', 'stripe').eq('environment', environment).maybeSingle()
  if (!customer) return json(req, { error: 'This household has no web billing yet.' }, 404)
  const configuration = Deno.env.get('STRIPE_PORTAL_CONFIGURATION_ID') || undefined
  const session = await stripe().billingPortal.sessions.create({ customer: customer.provider_customer_id, return_url: `${site()}/parent/household`, configuration })
  return json(req, { url: session.url })
})
