// Tests the shared Stripe edge-function logic (supabase/functions/_shared/billing.ts).
import { describe, expect, it } from 'vitest'
import { HANDLED_EVENTS, isLookupKey, planKeyFor, siteUrl, subscriptionIdFromEvent, subscriptionRow } from '../../../../supabase/functions/_shared/billing'

const sub = (over: Record<string, unknown> = {}) => ({
  id: 'sub_123',
  status: 'active',
  customer: 'cus_9',
  livemode: true,
  cancel_at_period_end: false,
  metadata: { household_id: 'hh-1', owner_user_id: 'user-1' },
  items: { data: [{ price: { id: 'price_1', lookup_key: 'pp_family_annual' }, current_period_start: 1790000000, current_period_end: 1821536000 }] },
  ...over,
})

describe('Stripe billing logic', () => {
  it('maps lookup keys to plans and rejects anything else', () => {
    expect(planKeyFor('pp_family_monthly')).toBe('family')
    expect(planKeyFor('pp_family_annual')).toBe('family')
    expect(planKeyFor('price_123')).toBeNull()
    expect(isLookupKey('pp_family_annual')).toBe(true)
    expect(isLookupKey('pp_free')).toBe(false)
  })

  it('derives the row from the subscription state, period from the item on newer API versions', () => {
    const r = subscriptionRow(sub())
    expect(r).toMatchObject({ household_id: 'hh-1', owner_user_id: 'user-1', plan_key: 'family', status: 'active', provider_customer_id: 'cus_9', environment: 'production' })
    expect(r.current_period_end).toBe(new Date(1821536000 * 1000).toISOString())
    expect(subscriptionRow(sub({ current_period_end: 1800000000 })).current_period_end).toBe(new Date(1800000000 * 1000).toISOString())
    expect(subscriptionRow(sub({ livemode: false })).environment).toBe('sandbox')
    expect(() => subscriptionRow(sub({ status: 'mystery' }))).toThrow(/Unknown Stripe subscription status/)
  })

  it('finds the subscription for every handled event shape', () => {
    expect(subscriptionIdFromEvent({ type: 'checkout.session.completed', data: { object: { mode: 'subscription', subscription: 'sub_a' } } })).toBe('sub_a')
    expect(subscriptionIdFromEvent({ type: 'checkout.session.completed', data: { object: { mode: 'payment' } } })).toBeNull()
    expect(subscriptionIdFromEvent({ type: 'customer.subscription.deleted', data: { object: { id: 'sub_b' } } })).toBe('sub_b')
    expect(subscriptionIdFromEvent({ type: 'invoice.paid', data: { object: { subscription: 'sub_c' } } })).toBe('sub_c')
    expect(subscriptionIdFromEvent({ type: 'invoice.payment_failed', data: { object: { parent: { subscription_details: { subscription: 'sub_d' } } } } })).toBe('sub_d')
    for (const t of ['customer.subscription.created', 'customer.subscription.updated', 'invoice.paid', 'invoice.payment_failed']) expect(HANDLED_EVENTS.has(t)).toBe(true)
  })

  it('redirects only to our own https origin', () => {
    expect(siteUrl('https://prepandprice.example/path')).toBe('https://prepandprice.example')
    expect(() => siteUrl('http://evil.example')).toThrow()
  })
})
