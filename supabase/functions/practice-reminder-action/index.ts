// "Remind me later" from a reminder notification. The service worker has no sign-in, so the notification carries
// a signed, expiring token bound to one delivery (signed by send-practice-reminders). The token works once: it
// snoozes that student's reminders and nothing else. A snooze never notifies a guardian.
//
// Secrets: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, REMINDER_ACTION_SECRET; APP_ORIGINS (allowed CORS origins).
import { createClient } from 'npm:@supabase/supabase-js@2'
import { SNOOZE_MINUTES } from '../_shared/reminders.ts'
import { verifyActionToken } from '../_shared/webpush.ts'

function cors(req: Request): Record<string, string> {
  const origins = (Deno.env.get('APP_ORIGINS') ?? '').split(',').map((o) => o.trim().replace(/\/+$/, '')).filter(Boolean)
  const origin = req.headers.get('Origin') ?? ''
  return {
    'Access-Control-Allow-Origin': origins.includes(origin) ? origin : (origins[0] ?? ''),
    'Access-Control-Allow-Headers': 'content-type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    Vary: 'Origin',
  }
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(req) })
  const reply = (status: number, body: unknown) => new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json', ...cors(req) } })
  if (req.method !== 'POST') return reply(405, { error: 'method_not_allowed' })
  let token = ''
  try {
    token = String(((await req.json()) as { token?: unknown }).token ?? '')
  } catch {
    /* fall through */
  }
  const delivery = await verifyActionToken(token, Deno.env.get('REMINDER_ACTION_SECRET') ?? '')
  if (!delivery) return reply(400, { error: 'invalid_or_expired' })
  const sb = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!, { auth: { persistSession: false } })
  const { data, error } = await sb.rpc('snooze_practice_reminder_delivery', { p_delivery: delivery, p_minutes: SNOOZE_MINUTES })
  if (error) {
    console.error('reminder action: snooze failed', error.code)
    return reply(500, { error: 'snooze_failed' })
  }
  // null: already used, unknown, or reminders were turned off meanwhile. Nothing to do either way.
  return reply(200, { snoozed_until: data ?? null })
})
