import { describe, expect, it } from 'vitest'
import { b64urlToBytes, bytesToB64url, encryptPayload, sendPush, signActionToken, vapidAuthorization, verifyActionToken } from '../../../supabase/functions/_shared/webpush.ts'

const subtle = globalThis.crypto.subtle

async function p256() {
  const k = (await subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits'])) as CryptoKeyPair
  const pub = new Uint8Array(await subtle.exportKey('raw', k.publicKey))
  const jwk = await subtle.exportKey('jwk', k.privateKey)
  return { k, pub, d: jwk.d! }
}

type B = Uint8Array<ArrayBuffer>
async function hkdf(salt: B, ikm: B, info: B, n: number) {
  const key = await subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits'])
  return new Uint8Array(await subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info }, key, n * 8))
}
const enc = new TextEncoder()
const cat = (...a: Uint8Array[]): B => Uint8Array.from(a.flatMap((x) => [...x]))

/** What the browser does on receipt (RFC 8291), written independently of the sender. */
async function decrypt(body: B, ua: Awaited<ReturnType<typeof p256>>, auth: B) {
  const salt = body.slice(0, 16)
  const idlen = body[20]!
  const asPub = body.slice(21, 21 + idlen)
  const cipher = body.slice(21 + idlen)
  const asKey = await subtle.importKey('raw', asPub, { name: 'ECDH', namedCurve: 'P-256' }, false, [])
  const shared = new Uint8Array(await subtle.deriveBits({ name: 'ECDH', public: asKey }, ua.k.privateKey, 256))
  const ikm = await hkdf(auth, shared, cat(enc.encode('WebPush: info\0'), ua.pub, asPub), 32)
  const cek = await hkdf(salt, ikm, enc.encode('Content-Encoding: aes128gcm\0'), 16)
  const nonce = await hkdf(salt, ikm, enc.encode('Content-Encoding: nonce\0'), 12)
  const key = await subtle.importKey('raw', cek, 'AES-GCM', false, ['decrypt'])
  const plain = new Uint8Array(await subtle.decrypt({ name: 'AES-GCM', iv: nonce }, key, cipher))
  expect(plain.at(-1)).toBe(2) // last-record delimiter
  return new TextDecoder().decode(plain.slice(0, -1))
}

describe('web push (VAPID + aes128gcm)', () => {
  it('encrypts so the browser side can decrypt it, with a single 4096-byte record header', async () => {
    const ua = await p256()
    const auth = globalThis.crypto.getRandomValues(new Uint8Array(16))
    const body = await encryptPayload({ endpoint: 'https://push.example/x', p256dh: bytesToB64url(ua.pub), auth: bytesToB64url(auth) }, enc.encode('{"hello":"there"}'))
    expect([...body.slice(16, 20)]).toEqual([0, 0, 16, 0])
    expect(await decrypt(body, ua, auth)).toBe('{"hello":"there"}')
  })

  it('signs a VAPID JWT for the push service origin that verifies with the public key', async () => {
    const v = await p256()
    const header = await vapidAuthorization('https://fcm.googleapis.com/fcm/send/abc', { publicKey: bytesToB64url(v.pub), privateKey: v.d, subject: 'mailto:ops@example.com' }, Date.UTC(2026, 9, 7))
    const m = /^vapid t=([^.]+)\.([^.]+)\.([^,]+), k=(.+)$/.exec(header)!
    expect(JSON.parse(new TextDecoder().decode(b64urlToBytes(m[2]!)))).toEqual({ aud: 'https://fcm.googleapis.com', exp: Date.UTC(2026, 9, 7) / 1000 + 43200, sub: 'mailto:ops@example.com' })
    const pub = await subtle.importKey('raw', v.pub, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['verify'])
    expect(await subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, pub, b64urlToBytes(m[3]!), enc.encode(`${m[1]}.${m[2]}`))).toBe(true)
  })

  it('reports gone subscriptions (404/410) so they stop being used', async () => {
    const ua = await p256()
    const v = await p256()
    const vapid = { publicKey: bytesToB64url(v.pub), privateKey: v.d, subject: 'mailto:a@b.c' }
    const target = { endpoint: 'https://push.example/x', p256dh: bytesToB64url(ua.pub), auth: bytesToB64url(new Uint8Array(16)) }
    const seen: Record<string, string>[] = []
    const fake = (status: number) => (async (_u: string, init: RequestInit) => (seen.push(init.headers as Record<string, string>), new Response(null, { status }))) as unknown as typeof fetch
    expect(await sendPush(target, { a: 1 }, vapid, { fetchImpl: fake(201), topic: 'practice-reminder' })).toEqual({ ok: true, status: 201 })
    expect(seen[0]).toMatchObject({ 'Content-Encoding': 'aes128gcm', TTL: '3600', Topic: 'practice-reminder' })
    expect(await sendPush(target, { a: 1 }, vapid, { fetchImpl: fake(410) })).toEqual({ ok: false, status: 410, gone: true })
    expect(await sendPush(target, { a: 1 }, vapid, { fetchImpl: fake(500) })).toEqual({ ok: false, status: 500, gone: false })
  })

  it('action tokens are signed, expire, and are bound to one delivery', async () => {
    const id = '7d3c6c1e-1f1a-4c2b-9a39-0f6f0c6a1b2c'
    const t = await signActionToken(id, 'secret-1', Date.now() + 60_000)
    expect(await verifyActionToken(t, 'secret-1')).toBe(id)
    expect(await verifyActionToken(t, 'secret-2')).toBeNull()
    expect(await verifyActionToken(t.replace(id, '7d3c6c1e-1f1a-4c2b-9a39-0f6f0c6a1b2d'), 'secret-1')).toBeNull()
    expect(await verifyActionToken(await signActionToken(id, 'secret-1', Date.now() - 1), 'secret-1')).toBeNull()
  })
})
