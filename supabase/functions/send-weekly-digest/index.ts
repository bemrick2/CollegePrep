// Sends parent accountability emails: the Monday weekly summary (mode "weekly"), the inactivity alert
// (mode "inactivity", meant to run daily) and the notice that a linked student turned practice reminders off
// (mode "reminders_off", CR-27; meant to run every 15 minutes). Called by a scheduler, never by a browser.
//
// Unlike the invitation function, there is no signed-in user here, so this uses the service-role key. It reads
// only through the CR-22 functions (weekly_digest_payload, inactivity_alert_payload), which are service-role only and
// run the dashboard's own RPCs as each guardian, so recipients and numbers follow the database's permission rules.
//
// Idempotent: each email is recorded (mark_parent_email_sent) before sending; a failed send removes the record so
// the next run retries. A retried run never sends the same week's summary or the same alert twice.
// Logs carry counts and failure kinds only, never addresses or content.
//
// Secrets: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY (provided by Supabase), DIGEST_CRON_SECRET (the scheduler's
// shared secret), RESEND_API_KEY; optional DIGEST_FROM_EMAIL, APP_ORIGINS, RESEND_API_URL (local testing only).
import { createClient } from 'npm:@supabase/supabase-js@2'
import { inactivityEmail, lastCompletedWeekStart, remindersOffEmail, weeklyDigestEmail, type DigestRecipient, type InactivityAlert, type RemindersOffNotice } from './digest.ts'

// Temporary Prep & Price sender (owner decision 2026-10-06 for invitations); DIGEST_FROM_EMAIL overrides it.
const DEFAULT_FROM = 'Prep & Price <invites@mail.getcimiento.com>'
const DEFAULT_ORIGIN = 'https://college-optimizer-staging.netlify.app'

const json = (status: number, body: unknown) => new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } })

function sameSecret(a: string, b: string) {
  if (!a || !b || a.length !== b.length) return false
  let d = 0
  for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i)
  return d === 0
}

interface Body {
  mode?: 'weekly' | 'inactivity' | 'reminders_off'
  /** Monday to summarize; defaults to the last completed week. */
  week_start?: string
  /** Compose without recording or sending; returns subjects and text (no addresses). */
  dry_run?: boolean
}

Deno.serve(async (req) => {
  if (req.method !== 'POST') return json(405, { error: 'method_not_allowed' })
  const secret = Deno.env.get('DIGEST_CRON_SECRET') ?? ''
  const given = (req.headers.get('x-digest-secret') ?? '').trim()
  if (!sameSecret(given, secret)) return json(401, { error: 'unauthorized' })

  let body: Body
  try {
    body = await req.json()
  } catch {
    body = {}
  }
  const mode = body.mode ?? 'weekly'
  if (mode !== 'weekly' && mode !== 'inactivity' && mode !== 'reminders_off') return json(400, { error: 'mode must be weekly, inactivity or reminders_off' })
  const week = body.week_start ?? lastCompletedWeekStart(new Date())
  if (mode === 'weekly' && !/^\d{4}-\d{2}-\d{2}$/.test(week)) return json(400, { error: 'week_start must be YYYY-MM-DD' })

  const sb = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!, { auth: { persistSession: false } })
  const origin = (Deno.env.get('APP_ORIGINS') || DEFAULT_ORIGIN).split(',')[0]!.trim().replace(/\/+$/, '')

  // Build the emails.
  type Out = { user_id: string; to: string; kind: 'weekly_digest' | 'inactivity' | 'reminders_off'; period: string; subject: string; html: string; text: string }
  const out: Out[] = []
  if (mode === 'weekly') {
    const { data, error } = await sb.rpc('weekly_digest_payload', { p_week_start: week })
    if (error) {
      console.error('digest: payload failed', error.code)
      return json(500, { error: 'payload_failed' })
    }
    for (const r of (data ?? []) as DigestRecipient[]) {
      const m = weeklyDigestEmail(r, origin)
      out.push({ user_id: r.user_id, to: r.email, kind: 'weekly_digest', period: week, ...m })
    }
  } else if (mode === 'reminders_off') {
    const { data, error } = await sb.rpc('reminder_opt_out_payload')
    if (error) {
      console.error('digest: reminders_off payload failed', error.code)
      return json(500, { error: 'payload_failed' })
    }
    for (const n of (data ?? []) as (RemindersOffNotice & { period_key: string })[]) {
      const m = remindersOffEmail(n, origin)
      out.push({ user_id: n.user_id, to: n.email, kind: 'reminders_off', period: n.period_key, ...m })
    }
  } else {
    const { data, error } = await sb.rpc('inactivity_alert_payload')
    if (error) {
      console.error('digest: inactivity payload failed', error.code)
      return json(500, { error: 'payload_failed' })
    }
    for (const a of (data ?? []) as (InactivityAlert & { period_key: string })[]) {
      const m = inactivityEmail(a, origin)
      out.push({ user_id: a.user_id, to: a.email, kind: 'inactivity', period: a.period_key, ...m })
    }
  }

  if (body.dry_run) return json(200, { mode, week_start: mode === 'weekly' ? week : null, dry_run: true, count: out.length, emails: out.map((e) => ({ user_id: e.user_id, subject: e.subject, text: e.text })) })

  const key = Deno.env.get('RESEND_API_KEY')
  if (!key) {
    console.error('digest: not configured')
    return json(200, { mode, sent: 0, failed: 0, skipped: out.length, reason: 'not_configured' })
  }
  const from = Deno.env.get('DIGEST_FROM_EMAIL') || DEFAULT_FROM
  const url = Deno.env.get('RESEND_API_URL') || 'https://api.resend.com/emails'
  let sent = 0
  let failed = 0
  let already = 0
  for (const e of out) {
    const mark = await sb.rpc('mark_parent_email_sent', { p_user: e.user_id, p_kind: e.kind, p_period_key: e.period })
    if (mark.error) {
      failed++
      console.error('digest: mark failed', mark.error.code)
      continue
    }
    if (mark.data !== true) {
      already++
      continue
    }
    let ok = false
    try {
      const r = await fetch(url, {
        method: 'POST',
        headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json', 'Idempotency-Key': `${e.kind}:${e.user_id}:${e.period}` },
        body: JSON.stringify({ from, to: [e.to], subject: e.subject, html: e.html, text: e.text }),
      })
      ok = r.ok
      if (!ok) console.error('digest: provider status', r.status)
    } catch {
      console.error('digest: provider unreachable')
    }
    if (ok) sent++
    else {
      failed++
      // Let the next run retry this one.
      await sb.from('parent_email_deliveries').delete().match({ user_id: e.user_id, kind: e.kind, period_key: e.period })
    }
  }
  console.log(`digest: mode=${mode} candidates=${out.length} sent=${sent} already=${already} failed=${failed}`)
  return json(200, { mode, week_start: mode === 'weekly' ? week : null, candidates: out.length, sent, already, failed })
})
