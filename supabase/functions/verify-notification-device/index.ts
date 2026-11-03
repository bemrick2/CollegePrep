// Sends the silent "verify device" push for pending device claims (20261103010000_device_claims.sql). Called by the
// app right after report_notification_device returns 'verification_pending' (with the app's own session), and by a
// scheduler with x-verify-secret as a retry. The nonce goes to the device the other login holds; the app on that
// device returns it with confirm_device_claim. See ../_shared/deviceVerify.ts.
//
// Logs carry counts and status codes only, never nonces, endpoints, tokens or names.
//
// Secrets: SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY, VAPID_PUBLIC_KEY, VAPID_PRIVATE_KEY,
// VAPID_SUBJECT; FCM_SERVICE_ACCOUNT for the native apps; VERIFY_CRON_SECRET for the scheduler. FCM_API_URL is for local
// tests only. Not deployed while hosted is held.
import { createClient } from 'npm:@supabase/supabase-js@2'
import { handleVerify, postFcm, type DeviceChallenge } from '../_shared/deviceVerify.ts'
import { sendPush, type Vapid } from '../_shared/webpush.ts'
import { fcmAccessToken, type ServiceAccount } from '../_shared/fcm.ts'

Deno.serve(async (req) => {
  const url = Deno.env.get('SUPABASE_URL') ?? ''
  const service = createClient(url, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '', { auth: { persistSession: false } })
  const vapid: Vapid = { publicKey: Deno.env.get('VAPID_PUBLIC_KEY') ?? '', privateKey: Deno.env.get('VAPID_PRIVATE_KEY') ?? '', subject: Deno.env.get('VAPID_SUBJECT') ?? '' }
  let sa: ServiceAccount | null = null
  try {
    sa = Deno.env.get('FCM_SERVICE_ACCOUNT') ? (JSON.parse(Deno.env.get('FCM_SERVICE_ACCOUNT')!) as ServiceAccount) : null
  } catch {
    console.error('verify: FCM_SERVICE_ACCOUNT is not valid JSON')
  }
  const webReady = !!(vapid.publicKey && vapid.privateKey && vapid.subject)
  let fcmToken: string | null = null
  const res = await handleVerify(req, {
    cronSecret: Deno.env.get('VERIFY_CRON_SECRET') ?? '',
    configured: webReady || !!sa,
    userId: async (authorization) => {
      const client = createClient(url, Deno.env.get('SUPABASE_ANON_KEY') ?? '', { global: { headers: { Authorization: authorization } }, auth: { persistSession: false } })
      const { data } = await client.auth.getUser()
      return data.user?.id ?? null
    },
    issue: async (claimant) => {
      const { data, error } = await service.rpc('issue_device_claim_challenges', { p_claimant: claimant })
      if (error) {
        console.error('verify: issue failed', error.code)
        throw new Error('issue_failed')
      }
      return (data ?? []) as DeviceChallenge[]
    },
    verify: {
      sendWeb: async (target, payload) =>
        webReady ? await sendPush(target, payload, vapid, { ttlSeconds: 600, topic: 'verify-device' }) : { ok: false, status: 0 },
      sendFcm: async (message) => {
        if (!sa) return { ok: false, status: 0 }
        fcmToken ??= await fcmAccessToken(sa)
        return await postFcm(sa.project_id, fcmToken, message, { apiBase: Deno.env.get('FCM_API_URL') ?? undefined })
      },
      retire: async (deviceId) => {
        await service.rpc('retire_notification_device', { p_device: deviceId })
      },
    },
  })
  if (res.status === 200) {
    const body = await res.clone().json()
    console.log(`verify: challenges=${body.challenges} sent=${body.sent} failed=${body.failed} gone=${body.gone}`)
  }
  return res
})
