// Web Push sending with Web Crypto only (works in Deno edge functions and Node 20+): VAPID authentication
// (RFC 8292) and aes128gcm message encryption (RFC 8291 / RFC 8188). No third-party push library.
//
// Keys use the common web-push format: the VAPID public key is the uncompressed P-256 point (65 bytes) and the
// private key the 32-byte scalar, both base64url. Generate them once (scripts/local/vapid_keys.mjs) and keep the
// private key only in function secrets.

export interface PushTarget {
  endpoint: string
  /** Browser's ECDH public key (base64url, 65 bytes). */
  p256dh: string
  /** Browser's auth secret (base64url, 16 bytes). */
  auth: string
}

export interface Vapid {
  publicKey: string
  privateKey: string
  /** mailto: or https: contact for the push service operator. */
  subject: string
}

export type PushResult = { ok: true; status: number } | { ok: false; status: number; gone: boolean }

const enc = new TextEncoder()
/** Bytes backed by a plain ArrayBuffer, as Web Crypto's BufferSource requires. */
type Bytes = Uint8Array<ArrayBuffer>

export function b64urlToBytes(s: string): Bytes {
  const b = atob(s.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((s.length + 3) % 4))
  return Uint8Array.from(b, (c) => c.charCodeAt(0))
}

export function bytesToB64url(b: Uint8Array): string {
  let s = ''
  for (const x of b) s += String.fromCharCode(x)
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function concat(...parts: Uint8Array[]): Bytes {
  const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0))
  let o = 0
  for (const p of parts) {
    out.set(p, o)
    o += p.length
  }
  return out
}

async function hkdf(salt: Bytes, ikm: Bytes, info: Bytes, length: number): Promise<Bytes> {
  const key = await crypto.subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits'])
  return new Uint8Array(await crypto.subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info }, key, length * 8))
}

/** VAPID JWT, signed ES256 (raw r||s, as JWS requires). */
export async function vapidAuthorization(endpoint: string, v: Vapid, now = Date.now()): Promise<string> {
  const pub = b64urlToBytes(v.publicKey)
  if (pub.length !== 65 || pub[0] !== 4) throw new Error('VAPID public key must be an uncompressed P-256 point')
  const jwk = { kty: 'EC', crv: 'P-256', d: v.privateKey, x: bytesToB64url(pub.slice(1, 33)), y: bytesToB64url(pub.slice(33, 65)), ext: true }
  const key = await crypto.subtle.importKey('jwk', jwk, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign'])
  const aud = new URL(endpoint).origin
  const header = bytesToB64url(enc.encode(JSON.stringify({ typ: 'JWT', alg: 'ES256' })))
  const claims = bytesToB64url(enc.encode(JSON.stringify({ aud, exp: Math.floor(now / 1000) + 12 * 3600, sub: v.subject })))
  const sig = new Uint8Array(await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, key, enc.encode(`${header}.${claims}`)))
  return `vapid t=${header}.${claims}.${bytesToB64url(sig)}, k=${v.publicKey}`
}

/** aes128gcm body for one record (RFC 8291 §4). */
export async function encryptPayload(target: PushTarget, payload: Uint8Array): Promise<Bytes> {
  const uaPublic = b64urlToBytes(target.p256dh)
  const authSecret = b64urlToBytes(target.auth)
  const as = (await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits'])) as CryptoKeyPair
  const asPublic = new Uint8Array(await crypto.subtle.exportKey('raw', as.publicKey))
  const uaKey = await crypto.subtle.importKey('raw', uaPublic, { name: 'ECDH', namedCurve: 'P-256' }, false, [])
  const shared = new Uint8Array(await crypto.subtle.deriveBits({ name: 'ECDH', public: uaKey }, as.privateKey, 256))
  const ikm = await hkdf(authSecret, shared, concat(enc.encode('WebPush: info\0'), uaPublic, asPublic), 32)
  const salt = crypto.getRandomValues(new Uint8Array(16))
  const cek = await hkdf(salt, ikm, enc.encode('Content-Encoding: aes128gcm\0'), 16)
  const nonce = await hkdf(salt, ikm, enc.encode('Content-Encoding: nonce\0'), 12)
  const key = await crypto.subtle.importKey('raw', cek, 'AES-GCM', false, ['encrypt'])
  const cipher = new Uint8Array(await crypto.subtle.encrypt({ name: 'AES-GCM', iv: nonce }, key, concat(payload, new Uint8Array([2]))))
  const rs = new Uint8Array([0, 0, 16, 0]) // 4096
  return concat(salt, rs, new Uint8Array([asPublic.length]), asPublic, cipher)
}

/**
 * Sends one push. TTL bounds how long the push service keeps an undelivered reminder; Topic makes a newer reminder
 * replace an older undelivered one instead of piling up.
 */
export async function sendPush(target: PushTarget, data: unknown, v: Vapid, opts: { ttlSeconds?: number; topic?: string; fetchImpl?: typeof fetch } = {}): Promise<PushResult> {
  const body = await encryptPayload(target, enc.encode(JSON.stringify(data)))
  const res = await (opts.fetchImpl ?? fetch)(target.endpoint, {
    method: 'POST',
    headers: {
      Authorization: await vapidAuthorization(target.endpoint, v),
      'Content-Encoding': 'aes128gcm',
      'Content-Type': 'application/octet-stream',
      TTL: String(opts.ttlSeconds ?? 3600),
      Urgency: 'normal',
      ...(opts.topic ? { Topic: opts.topic } : {}),
    },
    body,
  })
  await res.body?.cancel().catch(() => {})
  if (res.status >= 200 && res.status < 300) return { ok: true, status: res.status }
  return { ok: false, status: res.status, gone: res.status === 404 || res.status === 410 }
}

/** HMAC-signed, expiring token for a notification action, so the service worker needs no sign-in. */
export async function signActionToken(deliveryId: string, secret: string, expiresAt: number): Promise<string> {
  const msg = `${deliveryId}.${expiresAt}`
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign'])
  return `${msg}.${bytesToB64url(new Uint8Array(await crypto.subtle.sign('HMAC', key, enc.encode(msg))))}`
}

export async function verifyActionToken(token: string, secret: string, now = Date.now()): Promise<string | null> {
  const m = /^([0-9a-f-]{36})\.(\d{10,13})\.([A-Za-z0-9_-]{43})$/.exec(token)
  if (!m || !secret) return null
  if (Number(m[2]) < now) return null
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['verify'])
  const ok = await crypto.subtle.verify('HMAC', key, b64urlToBytes(m[3]!), enc.encode(`${m[1]}.${m[2]}`))
  return ok ? m[1]! : null
}
