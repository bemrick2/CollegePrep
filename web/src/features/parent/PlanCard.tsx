import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import type { BillingPlan, Entitlement } from '../../lib/data/types'
import { formatShortDate } from '../../lib/engine/dates'
import { redirectTo } from '../../lib/redirect'
import { Button, Card, CardHeader, Notice, Pill, cx } from '../../components/ui'

const money = (p: BillingPlan) =>
  p.unit_amount == null ? '' : (p.unit_amount / 100).toLocaleString(undefined, { style: 'currency', currency: p.currency.toUpperCase(), maximumFractionDigits: p.unit_amount % 100 ? 2 : 0 })

/**
 * The household plan (CR-16). Shows only what the backend entitlement says; buying happens on Stripe Checkout
 * and managing on the Stripe Customer Portal (web) or the store (Apple). Hidden entirely when billing is off.
 */
export function PlanCard({ householdId }: { householdId: string }) {
  const { source } = useApp()
  const [params] = useSearchParams()
  const returned = params.get('billing')
  const [poll, setPoll] = useState(0)
  const ent = useAsync(() => source.entitlement(householdId), [source, householdId, poll])
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // After Checkout, Stripe confirms by webhook a moment later: re-read the entitlement for up to ~30 s.
  useEffect(() => {
    if (returned !== 'success' || ent.data?.active || poll >= 15) return
    const t = setTimeout(() => setPoll((n) => n + 1), 2000)
    return () => clearTimeout(t)
  }, [returned, ent.data?.active, poll])

  if (!source.supportsBilling) return null

  const go = async (fn: () => Promise<string>) => {
    setBusy(true)
    setError(null)
    try {
      redirectTo(await fn())
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Billing is unavailable right now')
      setBusy(false)
    }
  }

  const e = ent.data
  return (
    <Card>
      <CardHeader title="Family plan" subtitle="One plan covers every parent and student in the household, on the web and in the apps." />
      <div className="grid gap-3 p-5 pt-3 text-sm">
        {returned === 'success' && !e?.active && (
          <Notice tone="info">Thanks. Your plan turns on as soon as Stripe confirms the payment, usually within seconds.{poll >= 15 ? ' Refresh in a minute if it still hasn’t.' : ''}</Notice>
        )}
        {returned === 'canceled' && !e?.active && <Notice tone="neutral">Checkout was canceled. You weren’t charged.</Notice>}
        {error && <Notice tone="bad">{error}</Notice>}
        {ent.loading && !e ? (
          <p className="text-ink-3">Checking your plan…</p>
        ) : ent.error ? (
          <Notice tone="bad">{ent.error.message}</Notice>
        ) : e?.active ? (
          <ActivePlan e={e} busy={busy} onManage={() => void go(() => source.billingPortalUrl(householdId))}  />
        ) : e?.can_manage_billing ? (
          <ChoosePlan busy={busy} onCheckout={(lk) => void go(() => source.startCheckout(householdId, lk))} />
        ) : (
          <p className="text-ink-2">No plan yet. Ask the guardian who manages billing to choose one.</p>
        )}
      </div>
    </Card>
  )
}

function ActivePlan({ e, busy, onManage }: { e: Entitlement; busy: boolean; onManage: () => void }) {
  return (
    <>
      <div className="flex flex-wrap items-center gap-2">
        <span className="font-semibold text-ink">Active</span>
        {e.in_grace ? <Pill tone="warn">Payment retrying</Pill> : <Pill tone="go">{e.status === 'trialing' ? 'Trial' : 'Paid'}</Pill>}
        {e.current_period_end && (
          <span className="text-ink-3">
            {e.cancel_at_period_end ? 'Ends' : 'Renews'} {formatShortDate(e.current_period_end)}
          </span>
        )}
      </div>
      {e.in_grace && <p className="text-warn">The last payment didn’t go through. Access continues while it retries; update the payment method to keep it.</p>}
      {e.managed_by === 'web' ? (
        <Button variant="secondary" disabled={busy} onClick={onManage} className="justify-self-start">
          {busy ? 'Opening…' : 'Manage billing'}
        </Button>
      ) : e.managed_by === 'apple' ? (
        <p className="text-ink-2">Billed through Apple. Change or cancel it in your iPhone’s Settings → your name → Subscriptions.</p>
      ) : e.managed_by === 'google' ? (
        <p className="text-ink-2">Billed through Google Play. Change or cancel it in the Play Store under Payments & subscriptions.</p>
      ) : (
        <p className="text-ink-3">Managed by the guardian who pays for it.</p>
      )}
    </>
  )
}

function ChoosePlan({ busy, onCheckout }: { busy: boolean; onCheckout: (lookupKey: string) => void }) {
  const { source } = useApp()
  const plans = useAsync(() => source.billingPlans(), [source])
  const list = [...(plans.data ?? [])].sort((a, b) => (a.interval === 'year' ? 1 : 0) - (b.interval === 'year' ? 1 : 0))
  const [pick, setPick] = useState<string | null>(null)
  const chosen = pick ?? list[0]?.lookup_key ?? null
  if (plans.loading && !plans.data) return <p className="text-ink-3">Loading plans…</p>
  if (plans.error || list.length === 0) return <p className="text-ink-3">Plans aren’t available right now. Please try again later.</p>
  return (
    <>
      <div role="radiogroup" aria-label="Billing period" className="grid gap-2 sm:grid-cols-2">
        {list.map((p) => (
          <button
            key={p.lookup_key}
            type="button"
            role="radio"
            aria-checked={chosen === p.lookup_key}
            onClick={() => setPick(p.lookup_key)}
            className={cx('rounded-2xl border-2 p-4 text-left', chosen === p.lookup_key ? 'border-go bg-go-soft' : 'border-line bg-surface hover:border-line-strong')}
          >
            <span className="block font-semibold text-ink">{p.interval === 'year' ? 'Annual' : 'Monthly'}</span>
            <span className="mt-0.5 block text-ink-2">
              {money(p)} / {p.interval === 'year' ? 'year' : 'month'}
            </span>
          </button>
        ))}
      </div>
      <Button disabled={busy || !chosen} onClick={() => chosen && onCheckout(chosen)} className="justify-self-start">
        {busy ? 'Opening checkout…' : 'Continue to secure checkout'}
      </Button>
      <p className="text-xs text-ink-3">Payment happens on Stripe’s secure checkout page. You can change or cancel anytime from Manage billing.</p>
    </>
  )
}
