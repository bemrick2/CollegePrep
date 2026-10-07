// Sends practice reminders as web push notifications. Called by a scheduler every 15 minutes, never by a browser.
//
// The database lists students with reminders on and at least one device that allowed notifications
// (practice_reminder_candidates, service role only). The shared rules (../_shared/reminders.ts, the same code the
// app uses) decide whether this run is a reminder time for each: chosen times and days, quiet hours, school hours,
// daily and weekly limits, snoozes, and no reminder once today's planned practice (or the week's goal) is done.
// Every attempt is recorded (record_practice_reminder); a subscription the push service reports gone is retired.
//
// Logs carry counts and status codes only, never endpoints, keys or names.
//
// Secrets: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, REMINDER_CRON_SECRET (scheduler), VAPID_PUBLIC_KEY,
// VAPID_PRIVATE_KEY, VAPID_SUBJECT, REMINDER_ACTION_SECRET (signs "Remind me later"); optional APP_ORIGINS.
// ALLOW_TEST_CLOCK=true (local tests only) lets the body set "now".
import { createClient } from 'npm:@supabase/supabase-js@2'
import { reminderDecision, reminderMessage, SNOOZE_MINUTES, type ReminderContext, type ReminderSettings } from '../_shared/reminders.ts'
import { sendPush, signActionToken, type Vapid } from '../_shared/webpush.ts'

const DEFAULT_ORIGIN = 'https://college-optimizer-staging.netlify.app'
const json = (status: number, body: unknown) => new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } })

function sameSecret(a: string, b: string) {
  if (!a || !b || a.length !== b.length) return false
  let d = 0
  for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i)
  return d === 0
}

interface Candidate {
  student_id: string
  time_zone: string
  settings: ReminderSettings
  context: Omit<ReminderContext, 'now' | 'timeZone'>
  devices: { id: string; endpoint: string; p256dh: string; auth: string }[]
}

Deno.serve(async (req) => {
  if (req.method !== 'POST') return json(405, { error: 'method_not_allowed' })
  if (!sameSecret((req.headers.get('x-reminder-secret') ?? '').trim(), Deno.env.get('REMINDER_CRON_SECRET') ?? '')) return json(401, { error: 'unauthorized' })
  let body: { now?: string; dry_run?: boolean } = {}
  try {
    body = await req.json()
  } catch {
    /* empty body */
  }
  const now = Deno.env.get('ALLOW_TEST_CLOCK') === 'true' && body.now ? new Date(body.now) : new Date()

  const vapid: Vapid = { publicKey: Deno.env.get('VAPID_PUBLIC_KEY') ?? '', privateKey: Deno.env.get('VAPID_PRIVATE_KEY') ?? '', subject: Deno.env.get('VAPID_SUBJECT') ?? '' }
  const actionSecret = Deno.env.get('REMINDER_ACTION_SECRET') ?? ''
  if (!body.dry_run && (!vapid.publicKey || !vapid.privateKey || !vapid.subject || !actionSecret)) {
    console.error('reminders: not configured')
    return json(200, { sent: 0, reason: 'not_configured' })
  }

  const supabaseUrl = Deno.env.get('SUPABASE_URL')!
  const sb = createClient(supabaseUrl, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!, { auth: { persistSession: false } })
  const origin = (Deno.env.get('APP_ORIGINS') || DEFAULT_ORIGIN).split(',')[0]!.trim().replace(/\/+$/, '')

  const { data, error } = await sb.rpc('practice_reminder_candidates', { p_now: now.toISOString() })
  if (error) {
    console.error('reminders: candidates failed', error.code)
    return json(500, { error: 'candidates_failed' })
  }
  const reasons: Record<string, number> = {}
  let sent = 0
  let failed = 0
  let gone = 0
  const due: { student_id: string; slot: string; message: string }[] = []
  for (const c of (data ?? []) as Candidate[]) {
    const d = reminderDecision(c.settings, { ...c.context, now, timeZone: c.time_zone })
    reasons[d.reason] = (reasons[d.reason] ?? 0) + 1
    if (d.reason !== 'send') continue
    const message = reminderMessage(c.context.sentThisWeek)
    due.push({ student_id: c.student_id, slot: d.slot!, message })
    if (body.dry_run) continue
    for (const dev of c.devices) {
      const id = crypto.randomUUID()
      const token = await signActionToken(id, actionSecret, now.getTime() + 24 * 3600_000)
      const payload = {
        title: 'Prep & Price',
        body: message,
        url: `${origin}/student/practice?quick=1&r=${id}`,
        tag: 'practice-reminder',
        snooze: { endpoint: `${supabaseUrl}/functions/v1/practice-reminder-action`, token, minutes: SNOOZE_MINUTES },
      }
      let status: 'sent' | 'failed' | 'gone' = 'failed'
      try {
        const r = await sendPush({ endpoint: dev.endpoint, p256dh: dev.p256dh, auth: dev.auth }, payload, vapid, { ttlSeconds: 3600, topic: 'practice-reminder' })
        status = r.ok ? 'sent' : r.gone ? 'gone' : 'failed'
        if (!r.ok) console.error('reminders: push status', r.status)
      } catch {
        console.error('reminders: push service unreachable')
      }
      if (status === 'sent') sent++
      else if (status === 'gone') gone++
      else failed++
      const rec = await sb.rpc('record_practice_reminder', { p_id: id, p_student: c.student_id, p_device: dev.id, p_slot: d.slot, p_status: status, p_at: now.toISOString() })
      if (rec.error) console.error('reminders: record failed', rec.error.code)
    }
  }
  console.log(`reminders: candidates=${(data ?? []).length} due=${due.length} sent=${sent} gone=${gone} failed=${failed}`)
  return json(200, { candidates: (data ?? []).length, due: body.dry_run ? due : due.length, sent, gone, failed, reasons })
})
