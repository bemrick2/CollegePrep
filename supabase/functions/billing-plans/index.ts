// GET: the household plan's active prices, by lookup key, for the website's plan picker. Public data only.
import { PLAN_LOOKUP_KEYS } from '../_shared/billing.ts'
import { cors, json, stripe } from '../_shared/runtime.ts'

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response(null, { headers: cors(req) })
  try {
    const prices = await stripe().prices.list({ lookup_keys: [...PLAN_LOOKUP_KEYS], active: true, expand: ['data.product'] })
    return json(req, {
      plans: prices.data.map((p) => ({
        lookup_key: p.lookup_key,
        unit_amount: p.unit_amount,
        currency: p.currency,
        interval: p.recurring?.interval ?? null,
        product_name: typeof p.product === 'object' && p.product && 'name' in p.product ? p.product.name : null,
      })),
    })
  } catch (e) {
    console.error(e)
    return json(req, { error: 'Plans are unavailable right now.' }, 503)
  }
})
