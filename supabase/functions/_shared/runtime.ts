// Edge-function runtime helpers: Stripe and Supabase clients, CORS, JSON responses, caller identity.
// Secrets come only from the function environment (Supabase Edge Function secrets), never from the client.
import Stripe from 'npm:stripe@17'
import { createClient, type SupabaseClient } from 'npm:@supabase/supabase-js@2'
import { siteUrl } from './billing.ts'

export function env(name: string): string {
  const v = Deno.env.get(name)
  if (!v) throw new Error(`Missing secret ${name}`)
  return v
}

export const stripe = () =>
  new Stripe(env('STRIPE_SECRET_KEY'), { httpClient: Stripe.createFetchHttpClient(), appInfo: { name: 'Prep & Price' } })

/** Service-role client: bypasses RLS; used only after the caller's permission has been checked. */
export const admin = (): SupabaseClient => createClient(env('SUPABASE_URL'), env('SUPABASE_SERVICE_ROLE_KEY'), { auth: { persistSession: false } })

export const site = () => siteUrl(Deno.env.get('SITE_URL'))

export function cors(req: Request): Record<string, string> {
  const origin = req.headers.get('Origin') ?? ''
  let allowed = ''
  try {
    allowed = site()
  } catch {
    /* SITE_URL missing: no cross-origin access */
  }
  return {
    'Access-Control-Allow-Origin': origin && origin === allowed ? origin : allowed,
    'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    Vary: 'Origin',
  }
}

export function json(req: Request, body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json', ...cors(req) } })
}

/** The signed-in caller, from the Authorization header the Supabase client sends. */
export async function caller(req: Request): Promise<{ id: string; email: string | null } | null> {
  const auth = req.headers.get('Authorization')
  if (!auth) return null
  const client = createClient(env('SUPABASE_URL'), env('SUPABASE_ANON_KEY'), { global: { headers: { Authorization: auth } }, auth: { persistSession: false } })
  const { data } = await client.auth.getUser()
  return data.user ? { id: data.user.id, email: data.user.email ?? null } : null
}

/** Guardians with the manage_billing flag may buy or manage the household plan. */
export async function canManageBilling(db: SupabaseClient, householdId: string, userId: string): Promise<boolean> {
  const { data } = await db
    .from('household_members')
    .select('user_id')
    .eq('household_id', householdId)
    .eq('user_id', userId)
    .eq('role', 'guardian')
    .eq('can_manage_billing', true)
    .maybeSingle()
  return !!data
}
