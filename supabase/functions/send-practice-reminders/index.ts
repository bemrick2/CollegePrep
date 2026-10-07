// Sends practice reminders as web push notifications. Called by a scheduler every 15 minutes, never by a browser.
//
// The database lists students with reminders on and at least one device that allowed notifications
// (practice_reminder_candidates, service role only). The shared rules (../_shared/reminders.ts, the same code the
// app uses) decide whether this run is a reminder time for each: chosen times and days, quiet hours, school hours,
// daily and weekly limits, snoozes, and no reminder once today's planned practice (or the week's goal) is done.
// One reminder goes to one device. Each reminder is claimed in the database before anything is sent
// (claim_practice_reminder, unique per student and reminder key), so overlapping runs, retries and several devices
// never produce a second notification. The device is the one the student opened most recently (deliveryOrder);
// others are tried only if the push service rejects it. Browsers get web push; the native apps get FCM.
//
// Logs carry counts and status codes only, never endpoints, keys or names.
//
// Secrets: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, REMINDER_CRON_SECRET (scheduler), VAPID_PUBLIC_KEY,
// VAPID_PRIVATE_KEY, VAPID_SUBJECT, REMINDER_ACTION_SECRET (signs "Remind me later"); optional APP_ORIGINS;
// FCM_SERVICE_ACCOUNT (JSON) once the native apps exist. FCM_API_URL is for local tests only.
// ALLOW_TEST_CLOCK=true (local tests only) lets the body set "now".
import { createClient } from 'npm:@supabase/supabase-js@2'
import { deliveryOrder, reminderDecision, reminderKey, reminderMessage, SNOOZE_MINUTES, type PushChannel, type ReminderContext, type ReminderSettings } from '../_shared/reminders.ts'
import { sendPush, signActionToken, type Vapid } from '../_shared/webpush.ts'
import { fcmAccessToken, sendFcm, type ServiceAccount } from '../_shared/fcm.ts'

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
  devices: { id: string; channel: PushChannel; checkedAt: string; endpoint: string | null; p256dh: string | null; auth: string | null; token: string | null }[]
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
  let sa: ServiceAccount | null = null
  try {
    sa = Deno.env.get('FCM_SERVICE_ACCOUNT') ? (JSON.parse(Deno.env.get('FCM_SERVICE_ACCOUNT')!) as ServiceAccount) : null
  } catch {
    console.error('reminders: FCM_SERVICE_ACCOUNT is not valid JSON')
  }
  let fcmToken: string | null = null
  const fcm = async () => (fcmToken ??= sa ? await fcmAccessToken(sa) : null)
  if (!body.dry_run && (!actionSecret || ((!vapid.publicKey || !vapid.privateKey || !vapid.subject) && !sa))) {
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
    const id = crypto.randomUUID()
    const key = reminderKey(d.slot!, now, c.time_zone, c.settings.snoozedUntil)
    const claim = await sb.rpc('claim_practice_reminder', { p_id: id, p_student: c.student_id, p_key: key, p_slot: d.slot, p_at: now.toISOString() })
    if (claim.error || claim.data !== true) {
      if (claim.error) console.error('reminders: claim failed', claim.error.code)
      else reasons.already_sent = (reasons.already_sent ?? 0) + 1
      continue
    }
    const token = await signActionToken(id, actionSecret, now.getTime() + 24 * 3600_000)
    const path = `/student/practice?quick=1&r=${id}`
    const snoozeEndpoint = `${supabaseUrl}/functions/v1/practice-reminder-action`
    let outcome: 'sent' | 'failed' | 'gone' = 'failed'
    let used: { id: string; channel: PushChannel } | null = null
    for (const dev of deliveryOrder(c.devices)) {
      used = { id: dev.id, channel: dev.channel }
      let r: { ok: boolean; gone?: boolean; status: number } | null = null
      try {
        if (dev.channel === 'webpush' && dev.endpoint && dev.p256dh && dev.auth && vapid.privateKey) {
          r = await sendPush({ endpoint: dev.endpoint, p256dh: dev.p256dh, auth: dev.auth }, { title: 'Prep & Price', body: message, url: `${origin}${path}`, tag: 'practice-reminder', snooze: { endpoint: snoozeEndpoint, token, minutes: SNOOZE_MINUTES } }, vapid, { ttlSeconds: 3600, topic: 'practice-reminder' })
        } else if (dev.channel === 'fcm' && dev.token && sa) {
          const at = await fcm()
          if (at) r = await sendFcm(sa.project_id, at, dev.token, { title: 'Prep & Price', body: message, path, deliveryId: id, snoozeToken: token, snoozeEndpoint }, { apiBase: Deno.env.get('FCM_API_URL') ?? undefined })
        }
      } catch {
        console.error('reminders: push service unreachable')
      }
      if (r?.ok) {
        outcome = 'sent'
        break
      }
      if (r && !r.ok) console.error('reminders: push status', r.status)
      if (r?.gone) {
        gone++
        await sb.rpc('retire_notification_device', { p_device: dev.id })
      }
      // Not delivered: try the next device. Only one can succeed, because the loop stops at the first.
    }
    if (outcome === 'sent') sent++
    else failed++
    const fin = await sb.rpc('finish_practice_reminder', { p_id: id, p_device: used?.id ?? null, p_channel: used?.channel ?? null, p_status: outcome })
    if (fin.error) console.error('reminders: finish failed', fin.error.code)
  }
  console.log(`reminders: candidates=${(data ?? []).length} due=${due.length} sent=${sent} gone=${gone} failed=${failed}`)
  return json(200, { candidates: (data ?? []).length, due: body.dry_run ? due : due.length, sent, gone, failed, reasons })
})
