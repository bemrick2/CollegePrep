// The silent "verify device" push (20261103010000_device_claims.sql). When a login reports a device another login
// holds, the database records a claim; this push carries the claim's nonce to the HELD device's stored endpoint or
// token. Only the app running on that device can read it and return it with confirm_device_claim(nonce).
//
// Pure helpers plus the sending loop, with the network calls injected, so Deno tests run offline. No titles, bodies or
// names: the push says nothing to anyone who sees it, and logs carry counts only, never nonces, endpoints or tokens.

/** One challenge, as issue_device_claim_challenges returns it (service role only). */
export interface DeviceChallenge {
  claim_id: string
  nonce: string
  expires_at: string
  device: { id: string; channel: 'webpush' | 'fcm'; endpoint: string | null; p256dh: string | null; auth: string | null; token: string | null }
}

export const VERIFY_TYPE = 'verify-device'
/** A claim lives 10 minutes; the push is useless after that. */
export const VERIFY_TTL_SECONDS = 600

/** Web push payload (encrypted for the device). The service worker must hand the nonce to the app, see CR-27. */
export function verifyWebPayload(c: DeviceChallenge): { type: string; nonce: string; claim: string } {
  return { type: VERIFY_TYPE, nonce: c.nonce, claim: c.claim_id }
}

/** FCM HTTP v1 message: data only (no notification block), background on iOS, so nothing is shown. */
export function verifyFcmMessage(c: DeviceChallenge, nowSeconds = Math.floor(Date.now() / 1000)) {
  return {
    message: {
      token: c.device.token!,
      data: { type: VERIFY_TYPE, nonce: c.nonce, claim: c.claim_id },
      android: { priority: 'HIGH', ttl: `${VERIFY_TTL_SECONDS}s`, collapse_key: VERIFY_TYPE },
      apns: {
        headers: { 'apns-push-type': 'background', 'apns-priority': '5', 'apns-expiration': String(nowSeconds + VERIFY_TTL_SECONDS) },
        payload: { aps: { 'content-available': 1 } },
      },
    },
  }
}

export type SendResult = { ok: boolean; status: number; gone?: boolean }

export interface VerifyDeps {
  sendWeb: (target: { endpoint: string; p256dh: string; auth: string }, payload: ReturnType<typeof verifyWebPayload>) => Promise<SendResult>
  sendFcm: (message: ReturnType<typeof verifyFcmMessage>) => Promise<SendResult>
  /** The push service said the subscription is gone: retire_notification_device. */
  retire: (deviceId: string) => Promise<void>
}

export interface VerifySummary {
  challenges: number
  sent: number
  failed: number
  gone: number
  skipped: number
}

/** Sends one silent push per challenge, to the held device only. */
export async function sendVerifications(challenges: DeviceChallenge[], deps: VerifyDeps, nowSeconds?: number): Promise<VerifySummary> {
  const out: VerifySummary = { challenges: challenges.length, sent: 0, failed: 0, gone: 0, skipped: 0 }
  for (const c of challenges) {
    let r: SendResult | null = null
    try {
      if (c.device.channel === 'webpush' && c.device.endpoint && c.device.p256dh && c.device.auth) {
        r = await deps.sendWeb({ endpoint: c.device.endpoint, p256dh: c.device.p256dh, auth: c.device.auth }, verifyWebPayload(c))
      } else if (c.device.channel === 'fcm' && c.device.token) {
        r = await deps.sendFcm(verifyFcmMessage(c, nowSeconds))
      }
    } catch {
      r = { ok: false, status: 0 }
    }
    if (!r) out.skipped++
    else if (r.ok) out.sent++
    else {
      out.failed++
      if (r.gone) {
        out.gone++
        await deps.retire(c.device.id)
      }
    }
  }
  return out
}

/** POST an FCM HTTP v1 message (verifyFcmMessage). */
export async function postFcm(projectId: string, accessToken: string, message: ReturnType<typeof verifyFcmMessage>, opts: { fetchImpl?: typeof fetch; apiBase?: string } = {}): Promise<SendResult> {
  const base = (opts.apiBase ?? 'https://fcm.googleapis.com').replace(/\/+$/, '')
  const res = await (opts.fetchImpl ?? fetch)(`${base}/v1/projects/${encodeURIComponent(projectId)}/messages:send`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(message),
  })
  let code = ''
  if (!res.ok) {
    try {
      const j = (await res.json()) as { error?: { status?: string; details?: { errorCode?: string }[] } }
      code = j.error?.details?.find((d) => d.errorCode)?.errorCode ?? j.error?.status ?? ''
    } catch {
      /* no body */
    }
  } else await res.body?.cancel().catch(() => {})
  return res.ok ? { ok: true, status: res.status } : { ok: false, status: res.status, gone: res.status === 404 || code === 'UNREGISTERED' }
}

export interface HandlerDeps {
  /** The signed-in caller's user id from the Authorization header, or null. */
  userId: (authorization: string) => Promise<string | null>
  /** issue_device_claim_challenges(p_claimant): null = every pending claim (scheduler). */
  issue: (claimant: string | null) => Promise<DeviceChallenge[]>
  verify: VerifyDeps
  /** Scheduler secret (VERIFY_CRON_SECRET); empty disables the scheduler mode. */
  cronSecret: string
  /** False when neither VAPID nor FCM is configured: nothing is issued, so no nonce is spent. */
  configured: boolean
}

function sameSecret(a: string, b: string) {
  if (!a || !b || a.length !== b.length) return false
  let d = 0
  for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i)
  return d === 0
}

const reply = (status: number, body: unknown) => new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } })

/**
 * POST only. Two callers:
 * - the app, right after report_notification_device returned 'verification_pending', with its own session: challenges
 *   for that login's claims only;
 * - a scheduler with x-verify-secret: every pending claim (a retry when the app's call was lost).
 * The response has counts only.
 */
export async function handleVerify(req: Request, deps: HandlerDeps): Promise<Response> {
  if (req.method !== 'POST') return reply(405, { error: 'method_not_allowed' })
  let claimant: string | null
  const secret = (req.headers.get('x-verify-secret') ?? '').trim()
  if (secret) {
    if (!sameSecret(secret, deps.cronSecret)) return reply(401, { error: 'unauthorized' })
    claimant = null
  } else {
    const auth = req.headers.get('Authorization') ?? ''
    claimant = auth ? await deps.userId(auth) : null
    if (!claimant) return reply(401, { error: 'unauthorized' })
  }
  if (!deps.configured) return reply(200, { challenges: 0, sent: 0, failed: 0, gone: 0, skipped: 0, reason: 'not_configured' })
  let challenges: DeviceChallenge[]
  try {
    challenges = await deps.issue(claimant)
  } catch {
    return reply(500, { error: 'issue_failed' })
  }
  const summary = await sendVerifications(challenges, deps.verify)
  return reply(200, summary)
}
