// Deno tests for the verify-device push path: `deno test supabase/functions/`. Offline: every network call is a fake.
import { handleVerify, postFcm, sendVerifications, verifyFcmMessage, verifyWebPayload, VERIFY_TYPE, type DeviceChallenge, type HandlerDeps, type VerifyDeps } from '../_shared/deviceVerify.ts'
import { bytesToB64url, sendPush, type Vapid } from '../_shared/webpush.ts'

function eq(got: unknown, want: unknown, msg: string) {
  if (JSON.stringify(got) !== JSON.stringify(want)) throw new Error(`${msg}: got ${JSON.stringify(got)}, want ${JSON.stringify(want)}`)
}
function ok(v: unknown, msg: string) {
  if (!v) throw new Error(msg)
}

const NONCE = 'a'.repeat(64)
const web: DeviceChallenge = { claim_id: 'c-web', nonce: NONCE, expires_at: '2026-11-03T12:10:00Z', device: { id: 'd-web', channel: 'webpush', endpoint: 'https://fcm.googleapis.com/fcm/send/held', p256dh: 'P', auth: 'A', token: null } }
const app: DeviceChallenge = { claim_id: 'c-app', nonce: 'b'.repeat(64), expires_at: '2026-11-03T12:10:00Z', device: { id: 'd-app', channel: 'fcm', endpoint: null, p256dh: null, auth: null, token: 'held-install-token-0000001' } }

function fakeVerify(results: Record<string, { ok: boolean; status: number; gone?: boolean } | Error> = {}) {
  const calls: { kind: string; to: string; body: unknown }[] = []
  const retired: string[] = []
  const deps: VerifyDeps = {
    sendWeb: (target, payload) => {
      calls.push({ kind: 'web', to: target.endpoint, body: payload })
      const r = results[target.endpoint] ?? { ok: true, status: 201 }
      return r instanceof Error ? Promise.reject(r) : Promise.resolve(r)
    },
    sendFcm: (m) => {
      calls.push({ kind: 'fcm', to: m.message.token, body: m })
      const r = results[m.message.token] ?? { ok: true, status: 200 }
      return r instanceof Error ? Promise.reject(r) : Promise.resolve(r)
    },
    retire: (id) => {
      retired.push(id)
      return Promise.resolve()
    },
  }
  return { deps, calls, retired }
}

Deno.test('the web push carries the nonce and nothing to show', () => {
  eq(verifyWebPayload(web), { type: VERIFY_TYPE, nonce: NONCE, claim: 'c-web' }, 'payload')
  ok(!('title' in verifyWebPayload(web)) && !('body' in verifyWebPayload(web)), 'no title or body')
})

Deno.test('the FCM message is data only, background on iOS, and expires with the claim', () => {
  const m = verifyFcmMessage(app, 1_000)
  eq(m.message.token, 'held-install-token-0000001', 'to the held install')
  eq(m.message.data, { type: VERIFY_TYPE, nonce: 'b'.repeat(64), claim: 'c-app' }, 'data')
  ok(!('notification' in m.message), 'no notification block')
  eq(m.message.apns.headers['apns-push-type'], 'background', 'iOS background')
  eq(m.message.apns.payload.aps['content-available'], 1, 'content-available')
  eq(m.message.apns.headers['apns-expiration'], '1600', 'expires after 10 minutes')
  eq(m.message.android.ttl, '600s', 'Android TTL')
})

Deno.test('one push per challenge, each to the held device only', async () => {
  const f = fakeVerify()
  const s = await sendVerifications([web, app], f.deps)
  eq(s, { challenges: 2, sent: 2, failed: 0, gone: 0, skipped: 0 }, 'summary')
  eq(f.calls.map((c) => [c.kind, c.to]), [['web', 'https://fcm.googleapis.com/fcm/send/held'], ['fcm', 'held-install-token-0000001']], 'targets')
})

Deno.test('a gone subscription is retired; other failures and errors are counted, not retried', async () => {
  const f = fakeVerify({ 'https://fcm.googleapis.com/fcm/send/held': { ok: false, status: 410, gone: true }, 'held-install-token-0000001': new Error('network') })
  const s = await sendVerifications([web, app], f.deps)
  eq(s, { challenges: 2, sent: 0, failed: 2, gone: 1, skipped: 0 }, 'summary')
  eq(f.retired, ['d-web'], 'retired')
})

Deno.test('a challenge without a usable target is skipped', async () => {
  const f = fakeVerify()
  const s = await sendVerifications([{ ...web, device: { ...web.device, p256dh: null } }, { ...app, device: { ...app.device, token: null } }], f.deps)
  eq(s, { challenges: 2, sent: 0, failed: 0, gone: 0, skipped: 2 }, 'summary')
  eq(f.calls.length, 0, 'nothing sent')
})

Deno.test('the web push is really encrypted for the held browser, with a 10-minute TTL', async () => {
  const ua = (await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits'])) as CryptoKeyPair
  const vk = (await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign'])) as CryptoKeyPair
  const vapid: Vapid = { publicKey: bytesToB64url(new Uint8Array(await crypto.subtle.exportKey('raw', vk.publicKey))), privateKey: (await crypto.subtle.exportKey('jwk', vk.privateKey)).d!, subject: 'mailto:ops@local.test' }
  const target = { endpoint: 'https://fcm.googleapis.com/fcm/send/held', p256dh: bytesToB64url(new Uint8Array(await crypto.subtle.exportKey('raw', ua.publicKey))), auth: bytesToB64url(new Uint8Array(16).fill(7)) }
  const seen: { url: string; headers: Headers; body: Uint8Array }[] = []
  const fetchImpl = (async (url: string, init: RequestInit) => {
    seen.push({ url, headers: new Headers(init.headers), body: new Uint8Array(init.body as ArrayBuffer) })
    return new Response(null, { status: 201 })
  }) as unknown as typeof fetch
  const r = await sendPush(target, verifyWebPayload(web), vapid, { ttlSeconds: 600, topic: 'verify-device', fetchImpl })
  ok(r.ok, 'sent')
  eq(seen[0]!.url, target.endpoint, 'to the held endpoint')
  eq([seen[0]!.headers.get('content-encoding'), seen[0]!.headers.get('ttl'), seen[0]!.headers.get('topic')], ['aes128gcm', '600', 'verify-device'], 'headers')
  ok(!new TextDecoder().decode(seen[0]!.body).includes(NONCE), 'the nonce is not readable on the wire')
})

Deno.test('postFcm: UNREGISTERED is gone; success is ok', async () => {
  const gone = (async () => new Response(JSON.stringify({ error: { status: 'NOT_FOUND', details: [{ errorCode: 'UNREGISTERED' }] } }), { status: 404 })) as unknown as typeof fetch
  eq(await postFcm('p', 't', verifyFcmMessage(app), { fetchImpl: gone }), { ok: false, status: 404, gone: true }, 'gone')
  let url = ''
  const fine = (async (u: string) => {
    url = u
    return new Response('{}', { status: 200 })
  }) as unknown as typeof fetch
  eq(await postFcm('proj', 't', verifyFcmMessage(app), { fetchImpl: fine, apiBase: 'http://127.0.0.1:1' }), { ok: true, status: 200 }, 'ok')
  eq(url, 'http://127.0.0.1:1/v1/projects/proj/messages:send', 'url')
})

function handlerDeps(over: Partial<HandlerDeps> = {}) {
  const issued: (string | null)[] = []
  const f = fakeVerify()
  const deps: HandlerDeps = {
    cronSecret: 'cron-secret-value',
    configured: true,
    userId: (a) => Promise.resolve(a === 'Bearer user-jwt' ? 'user-1' : null),
    issue: (c) => {
      issued.push(c)
      return Promise.resolve([web])
    },
    verify: f.deps,
    ...over,
  }
  return { deps, issued, calls: f.calls }
}
const post = (headers: Record<string, string>) => new Request('http://local/verify', { method: 'POST', headers })

Deno.test("the app call challenges only the caller's own claims", async () => {
  const h = handlerDeps()
  const r = await handleVerify(post({ Authorization: 'Bearer user-jwt' }), h.deps)
  eq(r.status, 200, 'status')
  eq(h.issued, ['user-1'], 'claimant')
  const body = await r.json()
  eq(body, { challenges: 1, sent: 1, failed: 0, gone: 0, skipped: 0 }, 'counts only')
  ok(!JSON.stringify(body).includes(NONCE), 'the nonce never comes back to the caller')
})

Deno.test('the scheduler call needs the secret and challenges every pending claim', async () => {
  const h = handlerDeps()
  eq((await handleVerify(post({ 'x-verify-secret': 'wrong' }), h.deps)).status, 401, 'wrong secret')
  eq((await handleVerify(post({ 'x-verify-secret': 'cron-secret-value' }), h.deps)).status, 200, 'right secret')
  eq(h.issued, [null], 'all claims')
  const off = handlerDeps({ cronSecret: '' })
  eq((await handleVerify(post({ 'x-verify-secret': 'anything' }), off.deps)).status, 401, 'no scheduler without a configured secret')
})

Deno.test('no session, a bad session, or GET: refused, and nothing is issued', async () => {
  const h = handlerDeps()
  eq((await handleVerify(post({}), h.deps)).status, 401, 'no session')
  eq((await handleVerify(post({ Authorization: 'Bearer forged' }), h.deps)).status, 401, 'bad session')
  eq((await handleVerify(new Request('http://local/verify'), h.deps)).status, 405, 'GET')
  eq(h.issued, [], 'nothing issued')
})

Deno.test('not configured: no nonce is issued (none would be wasted)', async () => {
  const h = handlerDeps({ configured: false })
  const r = await handleVerify(post({ Authorization: 'Bearer user-jwt' }), h.deps)
  eq([r.status, (await r.json()).reason], [200, 'not_configured'], 'reply')
  eq(h.issued, [], 'nothing issued')
})

// A browser's side of RFC 8291: decrypt with the subscription's private key and auth secret, or throw.
async function browserDecrypt(body: Uint8Array, priv: CryptoKey, pub: Uint8Array, auth: Uint8Array): Promise<unknown> {
  const te = new TextEncoder()
  const hkdf = async (salt: Uint8Array, ikm: Uint8Array, info: Uint8Array, n: number) =>
    new Uint8Array(await crypto.subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info }, await crypto.subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits']), n * 8))
  const salt = body.slice(0, 16)
  const n = body[20]!
  const asPub = body.slice(21, 21 + n)
  const shared = new Uint8Array(await crypto.subtle.deriveBits({ name: 'ECDH', public: await crypto.subtle.importKey('raw', asPub, { name: 'ECDH', namedCurve: 'P-256' }, false, []) }, priv, 256))
  const ikm = await hkdf(auth, shared, Uint8Array.from([...te.encode('WebPush: info\0'), ...pub, ...asPub]), 32)
  const cek = await hkdf(salt, ikm, te.encode('Content-Encoding: aes128gcm\0'), 16)
  const iv = await hkdf(salt, ikm, te.encode('Content-Encoding: nonce\0'), 12)
  const plain = new Uint8Array(await crypto.subtle.decrypt({ name: 'AES-GCM', iv }, await crypto.subtle.importKey('raw', cek, 'AES-GCM', false, ['decrypt']), body.slice(21 + n)))
  return JSON.parse(new TextDecoder().decode(plain.slice(0, -1)))
}

async function browser() {
  const k = (await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits'])) as CryptoKeyPair
  const pub = new Uint8Array(await crypto.subtle.exportKey('raw', k.publicKey))
  const auth = crypto.getRandomValues(new Uint8Array(16))
  return { k, pub, auth, p256dh: bytesToB64url(pub), authB64: bytesToB64url(auth) }
}

async function canRead(body: Uint8Array, b: Awaited<ReturnType<typeof browser>>): Promise<boolean> {
  try {
    await browserDecrypt(body, b.k.privateKey, b.pub, b.auth)
    return true
  } catch {
    return false
  }
}

Deno.test("the challenge is readable only with the keys it was encrypted to: the claimant's real browser, never a squatter's", async () => {
  const vk = (await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign'])) as CryptoKeyPair
  const vapid: Vapid = { publicKey: bytesToB64url(new Uint8Array(await crypto.subtle.exportKey('raw', vk.publicKey))), privateKey: (await crypto.subtle.exportKey('jwk', vk.privateKey)).d!, subject: 'mailto:ops@local.test' }
  const real = await browser() // the browser that really holds the endpoint's subscription, re-reporting it
  const squatter = await browser() // keys someone else registered or presented for the same endpoint
  const sent: { url: string; body: Uint8Array }[] = []
  const fetchImpl = (async (url: string, init: RequestInit) => {
    sent.push({ url, body: new Uint8Array(init.body as ArrayBuffer) })
    return new Response(null, { status: 201 })
  }) as unknown as typeof fetch
  const deps: VerifyDeps = { sendWeb: (t, p) => sendPush(t, p, vapid, { fetchImpl }), sendFcm: () => Promise.resolve({ ok: true, status: 200 }), retire: () => Promise.resolve() }
  // The database returns the held endpoint with the CLAIMANT's keys; the sender encrypts to exactly those.
  const asIssued = (claimant: Awaited<ReturnType<typeof browser>>): DeviceChallenge => ({ ...web, device: { ...web.device, p256dh: claimant.p256dh, auth: claimant.authB64 } })
  await sendVerifications([asIssued(real)], deps)
  eq(sent[0]!.url, web.device.endpoint, 'sent to the held endpoint')
  eq(await browserDecrypt(sent[0]!.body, real.k.privateKey, real.pub, real.auth), verifyWebPayload(web), 'the real browser reads its own claim')
  ok(!(await canRead(sent[0]!.body, squatter)), "a squatter's keys cannot read the real browser's challenge")
  // Turned around: an attacker presents its own keys for someone else's endpoint. The push is encrypted to the
  // attacker's keys but delivered to that endpoint, i.e. to the real browser, which cannot decrypt it.
  await sendVerifications([asIssued(squatter)], deps)
  eq(sent[1]!.url, web.device.endpoint, 'still sent only to the held endpoint')
  ok(!(await canRead(sent[1]!.body, real)), "the endpoint's real browser cannot read a challenge encrypted to someone else's keys")
})
