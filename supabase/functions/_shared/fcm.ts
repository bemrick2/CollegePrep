// Firebase Cloud Messaging HTTP v1, for the native iPhone and Android apps (both get FCM tokens; Firebase relays to
// APNs on iOS). Web Crypto only. The service account JSON lives in function secrets (FCM_SERVICE_ACCOUNT), never in
// the client or the repository.

export interface ServiceAccount {
  project_id: string
  client_email: string
  private_key: string
  token_uri?: string
}

export type FcmResult = { ok: true; status: number } | { ok: false; status: number; gone: boolean }

const te = new TextEncoder()
const b64url = (b: Uint8Array) => {
  let s = ''
  for (const x of b) s += String.fromCharCode(x)
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function pemToPkcs8(pem: string): Uint8Array<ArrayBuffer> {
  const body = pem.replace(/-----(BEGIN|END) PRIVATE KEY-----/g, '').replace(/\s+/g, '')
  return Uint8Array.from(atob(body), (c) => c.charCodeAt(0))
}

/** OAuth access token for FCM, from the service account (JWT bearer grant, RS256). */
export async function fcmAccessToken(sa: ServiceAccount, fetchImpl: typeof fetch = fetch, now = Date.now()): Promise<string> {
  const aud = sa.token_uri ?? 'https://oauth2.googleapis.com/token'
  const iat = Math.floor(now / 1000)
  const head = b64url(te.encode(JSON.stringify({ alg: 'RS256', typ: 'JWT' })))
  const claims = b64url(te.encode(JSON.stringify({ iss: sa.client_email, scope: 'https://www.googleapis.com/auth/firebase.messaging', aud, iat, exp: iat + 3600 })))
  const key = await crypto.subtle.importKey('pkcs8', pemToPkcs8(sa.private_key), { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['sign'])
  const sig = new Uint8Array(await crypto.subtle.sign('RSASSA-PKCS1-v1_5', key, te.encode(`${head}.${claims}`)))
  const r = await fetchImpl(aud, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${head}.${claims}.${b64url(sig)}` }).toString(),
  })
  if (!r.ok) throw new Error(`fcm oauth ${r.status}`)
  const j = (await r.json()) as { access_token?: string }
  if (!j.access_token) throw new Error('fcm oauth: no token')
  return j.access_token
}

export interface ReminderPush {
  title: string
  body: string
  /** App path to open on tap (the native app routes it inside the web view). */
  path: string
  deliveryId: string
  snoozeToken: string
  snoozeEndpoint: string
}

/**
 * One reminder to one app install. collapse_key / apns-collapse-id make a newer reminder replace an undelivered
 * older one on that device; the TTL drops it if the phone is offline for over an hour. Category PRACTICE_REMINDER
 * carries the "Start" and "Remind me later" buttons the app registers.
 */
export async function sendFcm(projectId: string, accessToken: string, token: string, m: ReminderPush, opts: { fetchImpl?: typeof fetch; apiBase?: string; nowSeconds?: number } = {}): Promise<FcmResult> {
  const base = (opts.apiBase ?? 'https://fcm.googleapis.com').replace(/\/+$/, '')
  const exp = (opts.nowSeconds ?? Math.floor(Date.now() / 1000)) + 3600
  const res = await (opts.fetchImpl ?? fetch)(`${base}/v1/projects/${encodeURIComponent(projectId)}/messages:send`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: {
        token,
        notification: { title: m.title, body: m.body },
        data: { path: m.path, delivery_id: m.deliveryId, snooze_token: m.snoozeToken, snooze_endpoint: m.snoozeEndpoint },
        android: { collapse_key: 'practice-reminder', ttl: '3600s', priority: 'NORMAL', notification: { tag: 'practice-reminder', channel_id: 'practice_reminders' } },
        apns: { headers: { 'apns-collapse-id': 'practice-reminder', 'apns-expiration': String(exp), 'apns-priority': '5' }, payload: { aps: { category: 'PRACTICE_REMINDER', 'thread-id': 'practice-reminder' } } },
      },
    }),
  })
  if (res.ok) {
    await res.body?.cancel().catch(() => {})
    return { ok: true, status: res.status }
  }
  let code = ''
  try {
    const j = (await res.json()) as { error?: { status?: string; details?: { errorCode?: string }[] } }
    code = j.error?.details?.find((d) => d.errorCode)?.errorCode ?? j.error?.status ?? ''
  } catch {
    /* no body */
  }
  // UNREGISTERED: the app was uninstalled or the token rotated. Retire it; any other error is a failure to retry.
  return { ok: false, status: res.status, gone: res.status === 404 || code === 'UNREGISTERED' }
}
