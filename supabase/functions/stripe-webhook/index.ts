// Stripe webhook: verify the signature, record the event exactly once, then set the household's subscription
// row from the subscription's CURRENT state in Stripe (retrieved fresh), so duplicate, delayed or out-of-order
// deliveries all converge on the same result. Deploy with JWT verification off (Stripe signs instead).
import Stripe from 'npm:stripe@17'
import { HANDLED_EVENTS, subscriptionIdFromEvent, subscriptionRow } from '../_shared/billing.ts'
import { admin, env, stripe } from '../_shared/runtime.ts'

const ok = (body: unknown = { received: true }) => new Response(JSON.stringify(body), { status: 200, headers: { 'Content-Type': 'application/json' } })

Deno.serve(async (req) => {
  if (req.method !== 'POST') return new Response('POST only', { status: 405 })
  const signature = req.headers.get('Stripe-Signature')
  const raw = await req.text()
  const s = stripe()
  let event: Stripe.Event
  try {
    event = await s.webhooks.constructEventAsync(raw, signature ?? '', env('STRIPE_WEBHOOK_SECRET'), undefined, Stripe.createSubtleCryptoProvider())
  } catch {
    return new Response('Bad signature', { status: 400 })
  }

  const db = admin()
  const subId = subscriptionIdFromEvent(event)
  const { data: inserted } = await db
    .from('billing_events')
    .upsert({ provider: 'stripe', event_id: event.id, event_type: event.type, provider_subscription_id: subId, payload: event }, { onConflict: 'provider,event_id', ignoreDuplicates: true })
    .select('id')
  if (!inserted?.length) {
    const { data: prior } = await db.from('billing_events').select('processed_at').eq('provider', 'stripe').eq('event_id', event.id).single()
    if (prior?.processed_at) return ok({ received: true, duplicate: true })
  }
  const done = (patch: Record<string, unknown>) => db.from('billing_events').update({ processed_at: new Date().toISOString(), ...patch }).eq('provider', 'stripe').eq('event_id', event.id)

  if (!HANDLED_EVENTS.has(event.type) || !subId) {
    await done({})
    return ok()
  }

  try {
    const sub = await s.subscriptions.retrieve(subId, { expand: ['items.data.price'] })
    const row = subscriptionRow(sub)
    if (!row.household_id || !row.owner_user_id || !row.plan_key) {
      // Not ours to fix by retrying (e.g. a subscription created outside our checkout): record and acknowledge.
      await done({ error: 'Subscription lacks household or owner metadata, or a Prep & Price price lookup key' })
      return ok({ received: true, ignored: true })
    }
    const { data: hh } = await db.from('households').select('id').eq('id', row.household_id).maybeSingle()
    if (!hh) {
      await done({ household_id: row.household_id, error: 'Unknown household' })
      return ok({ received: true, ignored: true })
    }
    const { data: existing } = await db.from('subscriptions').select('last_event_at').eq('provider_subscription_id', row.provider_subscription_id).maybeSingle()
    const eventAt = new Date(event.created * 1000).toISOString()
    const lastEventAt = existing?.last_event_at && existing.last_event_at > eventAt ? existing.last_event_at : eventAt
    const { error } = await db
      .from('subscriptions')
      .upsert({ ...row, owner_user_id: row.owner_user_id, last_event_at: lastEventAt, updated_at: new Date().toISOString() }, { onConflict: 'provider_subscription_id' })
    if (error) throw error
    await done({ household_id: row.household_id, error: null })
    return ok()
  } catch (e) {
    // Transient (Stripe or database): leave unprocessed so Stripe's retry runs it again.
    console.error(e)
    await db.from('billing_events').update({ error: String((e as Error).message ?? e) }).eq('provider', 'stripe').eq('event_id', event.id)
    return new Response('Retry later', { status: 500 })
  }
})
