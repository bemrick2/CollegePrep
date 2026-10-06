import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { PlanCard } from './PlanCard'
import type { Entitlement } from '../../lib/data/types'

const state: { source: Record<string, unknown> } = { source: {} }
const redirect = vi.hoisted(() => vi.fn())
vi.mock('../../lib/redirect', () => ({ redirectTo: redirect }))
vi.mock('../../lib/app', async (orig) => {
  const real = (await orig()) as Record<string, unknown>
  return { ...real, useApp: () => ({ source: state.source }) }
})

function withSource(ent: Entitlement, extra: Record<string, unknown> = {}) {
  state.source = {
    supportsBilling: true,
    entitlement: vi.fn().mockResolvedValue(ent),
    billingPlans: vi.fn().mockResolvedValue([
      { lookup_key: 'pp_family_annual', unit_amount: 11900, currency: 'usd', interval: 'year', product_name: 'Family' },
      { lookup_key: 'pp_family_monthly', unit_amount: 1499, currency: 'usd', interval: 'month', product_name: 'Family' },
    ]),
    startCheckout: vi.fn().mockResolvedValue('https://checkout.stripe.com/c/pay/cs_test'),
    billingPortalUrl: vi.fn().mockResolvedValue('https://billing.stripe.com/p/session/x'),
    ...extra,
  }
  return state.source
}
const renderCard = (path = '/parent/household') =>
  render(
    <MemoryRouter initialEntries={[path]}>
      <PlanCard householdId="hh-1" />
    </MemoryRouter>,
  )

afterEach(() => vi.clearAllMocks())

describe('PlanCard', () => {
  it('renders nothing when billing is off (demo, or not configured)', () => {
    withSource({ active: false, status: null, can_manage_billing: true }, { supportsBilling: false })
    const { container } = renderCard()
    expect(container).toBeEmptyDOMElement()
  })

  it('lets a billing guardian pick a period and go to Stripe Checkout', async () => {
    const user = userEvent.setup()
    const src = withSource({ active: false, status: null, can_manage_billing: true })
    renderCard()
    expect(await screen.findByRole('radio', { name: /Monthly\s*\$14\.99 \/ month/ })).toBeInTheDocument()
    await user.click(screen.getByRole('radio', { name: /Annual/ }))
    await user.click(screen.getByRole('button', { name: 'Continue to secure checkout' }))
    expect(src.startCheckout).toHaveBeenCalledWith('hh-1', 'pp_family_annual')
    expect(redirect).toHaveBeenCalledWith('https://checkout.stripe.com/c/pay/cs_test')
  })

  it('never offers a purchase when the household already has access, from any source', async () => {
    withSource({ active: true, status: 'active', plan_key: 'family', current_period_end: '2026-11-06T00:00:00Z', can_manage_billing: true, managed_by: 'apple' })
    renderCard()
    expect(await screen.findByText(/Billed through Apple/)).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: /checkout/i })).not.toBeInTheDocument()
  })

  it('web subscribers manage billing in the Stripe portal; others without billing rights just see access', async () => {
    withSource({ active: true, status: 'active', can_manage_billing: true, managed_by: 'web', current_period_end: '2026-11-06T00:00:00Z' })
    renderCard()
    expect(await screen.findByRole('button', { name: 'Manage billing' })).toBeInTheDocument()
    expect(screen.getByText(/Renews/)).toBeInTheDocument()
  })

  it('a guardian without billing rights is told who can choose a plan', async () => {
    withSource({ active: false, status: null, can_manage_billing: false })
    renderCard()
    expect(await screen.findByText(/Ask the guardian who manages billing/)).toBeInTheDocument()
  })

  it('after checkout, waits for the webhook instead of assuming payment', async () => {
    withSource({ active: false, status: null, can_manage_billing: true })
    renderCard('/parent/household?billing=success')
    expect(await screen.findByText(/turns on as soon as Stripe confirms/)).toBeInTheDocument()
  })
})
