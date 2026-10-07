import { describe, expect, it } from 'vitest'
import { fcmAccessToken, sendFcm } from '../../../supabase/functions/_shared/fcm.ts'

const subtle = globalThis.crypto.subtle
async function serviceAccount() {
  const k = (await subtle.generateKey({ name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]), hash: 'SHA-256' }, true, ['sign', 'verify'])) as CryptoKeyPair
  const pkcs8 = new Uint8Array(await subtle.exportKey('pkcs8', k.privateKey))
  const pem = `-----BEGIN PRIVATE KEY-----\n${btoa(String.fromCharCode(...pkcs8)).replace(/(.{64})/g, '$1\n')}\n-----END PRIVATE KEY-----\n`
  return { k, sa: { project_id: 'prep-and-price', client_email: 'sender@prep-and-price.iam.gserviceaccount.com', private_key: pem, token_uri: 'https://oauth.example/token' } }
}
const b64 = (s: string) => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((s.length + 3) % 4)), (c) => c.charCodeAt(0))

describe('FCM HTTP v1 (native apps)', () => {
  it('gets an access token with a signed service-account JWT', async () => {
    const { k, sa } = await serviceAccount()
    let assertion = ''
    const fake = (async (url: string, init: RequestInit) => {
      expect(url).toBe('https://oauth.example/token')
      assertion = new URLSearchParams(String(init.body)).get('assertion')!
      return new Response(JSON.stringify({ access_token: 'ya29.test' }), { status: 200 })
    }) as unknown as typeof fetch
    expect(await fcmAccessToken(sa, fake, Date.UTC(2026, 9, 7))).toBe('ya29.test')
    const [h, c, sig] = assertion.split('.')
    expect(JSON.parse(new TextDecoder().decode(b64(c!)))).toMatchObject({ iss: sa.client_email, scope: 'https://www.googleapis.com/auth/firebase.messaging', aud: 'https://oauth.example/token' })
    expect(await subtle.verify('RSASSA-PKCS1-v1_5', k.publicKey, b64(sig!), new TextEncoder().encode(`${h}.${c}`))).toBe(true)
  })

  it('sends one collapsing reminder with the tap path and snooze token; an uninstalled app is reported gone', async () => {
    const sent: { url: string; body: Record<string, unknown> }[] = []
    const ok = (async (url: string, init: RequestInit) => (sent.push({ url, body: JSON.parse(String(init.body)) }), new Response('{}', { status: 200 }))) as unknown as typeof fetch
    const msg = { title: 'Prep & Price', body: 'Got a few minutes? Try a quick practice session.', path: '/student/practice?quick=1&r=abc', deliveryId: 'abc', snoozeToken: 't', snoozeEndpoint: 'https://fn.example/practice-reminder-action' }
    expect(await sendFcm('prep-and-price', 'ya29', 'tok-123456789012345678901', msg, { fetchImpl: ok, nowSeconds: 1000 })).toEqual({ ok: true, status: 200 })
    expect(sent[0]!.url).toBe('https://fcm.googleapis.com/v1/projects/prep-and-price/messages:send')
    expect(sent[0]!.body).toMatchObject({
      message: {
        token: 'tok-123456789012345678901',
        notification: { title: 'Prep & Price', body: msg.body },
        data: { path: msg.path, delivery_id: 'abc', snooze_token: 't' },
        android: { collapse_key: 'practice-reminder', ttl: '3600s' },
        apns: { headers: { 'apns-collapse-id': 'practice-reminder', 'apns-expiration': '4600' }, payload: { aps: { category: 'PRACTICE_REMINDER' } } },
      },
    })
    const gone = (async () => new Response(JSON.stringify({ error: { status: 'NOT_FOUND', details: [{ errorCode: 'UNREGISTERED' }] } }), { status: 404 })) as unknown as typeof fetch
    expect(await sendFcm('p', 'a', 'tok-123456789012345678901', msg, { fetchImpl: gone })).toEqual({ ok: false, status: 404, gone: true })
    const busy = (async () => new Response('{}', { status: 503 })) as unknown as typeof fetch
    expect(await sendFcm('p', 'a', 'tok-123456789012345678901', msg, { fetchImpl: busy })).toEqual({ ok: false, status: 503, gone: false })
  })
})
