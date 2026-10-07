// Lives outside src/ because it uses Node APIs (crypto, child_process, https).
//
// End-to-end check of practice reminders (CR-27) against the local disposable backend with the reference SQL:
// the real edge functions under Deno (push sender, "Remind me later" action, parent email sender), a fake HTTPS
// push service that decrypts what it receives the way a browser would, and a fake mail endpoint for Resend.
// Skipped unless LOCAL_BACKEND_URL and DENO_BIN are set (scripts/local/live_stack.sh test).
import { execFileSync, spawn, type ChildProcess } from 'node:child_process'
import { createHmac, webcrypto } from 'node:crypto'
import { mkdtempSync, readFileSync } from 'node:fs'
import { createServer as createHttps, type Server as HttpsServer } from 'node:https'
import { createServer, type Server } from 'node:http'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { createClient } from '@supabase/supabase-js'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { LiveSource } from '../../src/lib/data/live/liveSource'
import { DEFAULT_REMINDERS, localParts, type ReminderSettings } from '../../../supabase/functions/_shared/reminders.ts'

const URL_ = process.env.LOCAL_BACKEND_URL
const DENO = process.env.DENO_BIN
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000000a5'
const STUDENT = '00000000-0000-4000-a000-000000000053'
const ADULT = '00000000-0000-4000-a000-000000000054'
const OUTSIDER = '00000000-0000-4000-a000-000000000099'
const TZ = 'America/Chicago'
const PORTS = { sender: 54341, action: 54342, digest: 54343, mail: 54344, push: 54345 }
const subtle = webcrypto.subtle as unknown as SubtleCrypto

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(claims: Record<string, unknown>) {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ aud: 'authenticated', iat: now, exp: now + 3600, ...claims })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
async function as(sub: string) {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt({ sub, role: 'authenticated' }), refresh_token: 'local' })
  if (error) throw error
  return new LiveSource(sb, { weeklyDigest: true, reminders: true })
}
const u8 = (b: ArrayBuffer | Uint8Array) => new Uint8Array(b instanceof Uint8Array ? b : b)
const b64u = (b: Uint8Array) => Buffer.from(b).toString('base64url')

async function p256() {
  const k = (await subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits'])) as CryptoKeyPair
  return { k, pub: u8(await subtle.exportKey('raw', k.publicKey)), d: (await subtle.exportKey('jwk', k.privateKey)).d! }
}
async function hkdf(salt: Uint8Array, ikm: Uint8Array, info: Uint8Array, n: number) {
  const key = await subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits'])
  return u8(await subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info }, key, n * 8))
}
const te = new TextEncoder()
/** A browser's side of RFC 8291. */
async function decrypt(body: Uint8Array, ua: Awaited<ReturnType<typeof p256>>, auth: Uint8Array) {
  const salt = body.slice(0, 16)
  const n = body[20]!
  const asPub = body.slice(21, 21 + n)
  const asKey = await subtle.importKey('raw', asPub, { name: 'ECDH', namedCurve: 'P-256' }, false, [])
  const shared = u8(await subtle.deriveBits({ name: 'ECDH', public: asKey }, ua.k.privateKey, 256))
  const ikm = await hkdf(auth, shared, Uint8Array.from([...te.encode('WebPush: info\0'), ...ua.pub, ...asPub]), 32)
  const cek = await hkdf(salt, ikm, te.encode('Content-Encoding: aes128gcm\0'), 16)
  const nonce = await hkdf(salt, ikm, te.encode('Content-Encoding: nonce\0'), 12)
  const key = await subtle.importKey('raw', cek, 'AES-GCM', false, ['decrypt'])
  const plain = u8(await subtle.decrypt({ name: 'AES-GCM', iv: nonce }, key, body.slice(21 + n)))
  return JSON.parse(new TextDecoder().decode(plain.slice(0, -1)))
}

/** The current local quarter-hour as "HH:MM", and quiet hours placed six hours away from it. */
function slotNow() {
  const { minutes } = localParts(new Date(), TZ)
  const q = minutes - (minutes % 15)
  const hhmm = (m: number) => `${String(Math.floor(((m + 1440) % 1440) / 60)).padStart(2, '0')}:${String(((m + 1440) % 1440) % 60).padStart(2, '0')}`
  return { slot: hhmm(q), quietStart: hhmm(q + 360), quietEnd: hhmm(q + 375) }
}

describe.skipIf(!URL_ || !DENO)('practice reminders: push sender, snooze action, guardian notice', () => {
  const procs: ChildProcess[] = []
  let mail: Server
  let push: HttpsServer
  const inbox: { to: string[]; subject: string; text: string }[] = []
  const pushes: { path: string; headers: Record<string, unknown>; body: Buffer }[] = []
  let pushStatus = 201
  let parent: LiveSource
  let student: LiveSource
  let studentId = ''
  let ua: Awaited<ReturnType<typeof p256>>
  const authSecret = new Uint8Array(16).map((_, i) => i + 1)
  const deviceId = '5f0f8a1e-4b6a-4a8e-9a55-2d7f3c1b0a01'
  // The chosen time is the current quarter hour; re-read right before each send so a slow start can't miss it.
  let cur = slotNow()
  const freshSlot = async () => {
    const left = 15 * 60_000 - (Date.now() % (15 * 60_000))
    if (left < 45_000) await new Promise((r) => setTimeout(r, left + 1000))
    cur = slotNow()
  }
  const settings = (over: Partial<ReminderSettings> = {}): ReminderSettings => ({ ...DEFAULT_REMINDERS, enabled: true, times: [cur.slot], quietStart: cur.quietStart, quietEnd: cur.quietEnd, schoolStart: null, schoolEnd: null, ...over })
  const cron = (port: number, header: string, secret: string, body: unknown = {}) =>
    fetch(`http://127.0.0.1:${port}`, { method: 'POST', headers: { [header]: secret, 'Content-Type': 'application/json' }, body: JSON.stringify(body) }).then(async (r) => ({ status: r.status, body: (await r.json()) as Record<string, unknown> }))
  const sendReminders = () => cron(PORTS.sender, 'x-reminder-secret', 'local-reminder-secret')
  const sendNotices = () => cron(PORTS.digest, 'x-digest-secret', 'local-digest-secret', { mode: 'reminders_off' })

  beforeAll(async () => {
    const dir = mkdtempSync(join(tmpdir(), 'pp-push-'))
    execFileSync('openssl', ['req', '-x509', '-newkey', 'ec', '-pkeyopt', 'ec_paramgen_curve:prime256v1', '-nodes', '-keyout', join(dir, 'k.pem'), '-out', join(dir, 'c.pem'), '-days', '1', '-subj', '/CN=127.0.0.1'], { stdio: 'ignore' })
    push = createHttps({ key: readFileSync(join(dir, 'k.pem')), cert: readFileSync(join(dir, 'c.pem')) }, (req, res) => {
      const chunks: Buffer[] = []
      req.on('data', (c) => chunks.push(c))
      req.on('end', () => {
        pushes.push({ path: req.url ?? '', headers: req.headers, body: Buffer.concat(chunks) })
        res.writeHead(pushStatus).end()
      })
    }).listen(PORTS.push, '127.0.0.1')
    mail = createServer((req, res) => {
      let raw = ''
      req.on('data', (c) => (raw += c))
      req.on('end', () => {
        const m = JSON.parse(raw)
        inbox.push({ to: m.to, subject: m.subject, text: m.text })
        res.writeHead(200, { 'content-type': 'application/json' }).end('{"id":"local"}')
      })
    }).listen(PORTS.mail, '127.0.0.1')

    const vapid = await p256()
    const env = {
      ...process.env,
      SUPABASE_URL: URL_!,
      SUPABASE_SERVICE_ROLE_KEY: jwt({ sub: 'service', role: 'service_role' }),
      APP_ORIGINS: 'https://app.local.test',
      REMINDER_CRON_SECRET: 'local-reminder-secret',
      REMINDER_ACTION_SECRET: 'local-action-secret',
      VAPID_PUBLIC_KEY: b64u(vapid.pub),
      VAPID_PRIVATE_KEY: vapid.d,
      VAPID_SUBJECT: 'mailto:ops@local.test',
      DIGEST_CRON_SECRET: 'local-digest-secret',
      RESEND_API_KEY: 'local-test-key',
      RESEND_API_URL: `http://127.0.0.1:${PORTS.mail}/emails`,
    }
    const run = (fn: string, port: number, extra: string[] = []) => {
      const p = spawn(DENO!, ['run', '--allow-net', '--allow-env', '--allow-read', ...extra, `../supabase/functions/${fn}/index.ts`], { env: { ...env, DENO_SERVE_ADDRESS: `tcp:127.0.0.1:${port}` }, stdio: ['ignore', 'pipe', 'pipe'] })
      procs.push(p)
    }
    run('send-practice-reminders', PORTS.sender, ['--unsafely-ignore-certificate-errors=127.0.0.1'])
    run('practice-reminder-action', PORTS.action)
    run('send-weekly-digest', PORTS.digest)
    for (const port of [PORTS.sender, PORTS.action, PORTS.digest])
      for (let i = 0; i < 300; i++) {
        try {
          await fetch(`http://127.0.0.1:${port}`, { method: 'GET' })
          break
        } catch {
          await new Promise((r) => setTimeout(r, 200))
        }
      }

    parent = await as(PARENT)
    const hh = await parent.createHousehold('Reminder family', TZ)
    studentId = await parent.addStudent(hh, 'Riley', 2028, 11)
    const inv = await parent.createStudentInvitation(hh, studentId)
    student = await as(STUDENT)
    await student.acceptInvitation(inv.inviteCode!)
    ua = await p256()
  }, 120_000)

  afterAll(() => {
    for (const p of procs) p.kill()
    mail?.close()
    push?.close()
  })

  it('only the family can read or change reminders', async () => {
    const outsider = await as(OUTSIDER)
    await expect(outsider.reminderSettings(studentId)).resolves.toMatchObject({ enabled: false }) // no row is visible
    await expect(outsider.saveReminderSettings(studentId, settings())).rejects.toThrow()
    await expect(outsider.studentDevices(studentId)).rejects.toThrow()
  })

  it('devices report permission when the app opens; families see the state, never endpoints or keys', async () => {
    await student.reportNotificationDevice({ deviceId, permission: 'granted', platform: 'android', subscription: { endpoint: `https://127.0.0.1:${PORTS.push}/sub/one`, keys: { p256dh: b64u(ua.pub), auth: b64u(authSecret) } } })
    await student.reportNotificationDevice({ deviceId: '5f0f8a1e-4b6a-4a8e-9a55-2d7f3c1b0a02', permission: 'denied', platform: 'ios', subscription: null })
    const devices = await parent.studentDevices(studentId)
    expect(devices.map((d) => [d.permission, d.platform, d.canReceive])).toEqual(expect.arrayContaining([['granted', 'android', true], ['denied', 'ios', false]]))
    expect(JSON.stringify(devices)).not.toContain('sub/one')
    // A device id belongs to the login that first reported it.
    await expect(parent.reportNotificationDevice({ deviceId, permission: 'denied', platform: 'desktop', subscription: null })).rejects.toThrow()
  })

  it('a guardian turns reminders on; at the chosen time one push goes out, encrypted, then the daily limit holds', async () => {
    await freshSlot()
    expect(await parent.saveReminderSettings(studentId, settings())).toEqual({ guardiansNotified: false })
    expect(await student.reminderSettings(studentId)).toMatchObject({ enabled: true, times: [cur.slot] })
    const first = await sendReminders()
    expect(first.body).toMatchObject({ sent: 1, failed: 0 })
    expect(pushes).toHaveLength(1)
    expect(pushes[0]!.headers).toMatchObject({ 'content-encoding': 'aes128gcm', ttl: '3600', topic: 'practice-reminder' })
    expect(String(pushes[0]!.headers.authorization)).toMatch(/^vapid t=.+, k=/)
    const payload = await decrypt(new Uint8Array(pushes[0]!.body), ua, authSecret)
    expect(payload).toMatchObject({ title: 'Prep & Price', body: 'Got a few minutes? Try a quick practice session.', tag: 'practice-reminder' })
    expect(payload.url).toMatch(/^https:\/\/app\.local\.test\/student\/practice\?quick=1&r=[0-9a-f-]{36}$/)
    const latest = await student.latestReminder(studentId)
    expect(payload.url).toContain(latest!.id)

    const again = await sendReminders()
    expect(again.body).toMatchObject({ sent: 0 })
    expect((again.body.reasons as Record<string, number>).daily_limit).toBeGreaterThanOrEqual(1)
    expect(pushes).toHaveLength(1)

    // Tapping "Remind me later" on the notification: the signed token works once, and tells nobody.
    const tap = () => fetch(`http://127.0.0.1:${PORTS.action}`, { method: 'POST', headers: { 'Content-Type': 'application/json', Origin: 'https://app.local.test' }, body: JSON.stringify({ token: payload.snooze.token }) }).then((r) => r.json())
    expect((await tap()).snoozed_until).toBeTruthy()
    expect((await tap()).snoozed_until).toBeNull()
    expect((await fetch(`http://127.0.0.1:${PORTS.action}`, { method: 'POST', body: JSON.stringify({ token: payload.snooze.token.slice(0, -2) + 'xx' }) })).status).toBe(400)
    expect((await student.reminderSettings(studentId)).snoozedUntil).toBeTruthy()
    expect(await student.reminderHistory(studentId)).toEqual([expect.objectContaining({ enabled: true, by: 'guardian', notifyGuardians: false })])
    await student.markReminderOpened(latest!.id)
    expect((await student.latestReminder(studentId))!.openedAt).toBeTruthy()
  }, 70_000)

  it('snoozing in the app never notifies; the student turning reminders off emails each guardian once, recorded', async () => {
    await student.snoozeReminders(studentId, 60)
    expect((await sendNotices()).body).toMatchObject({ candidates: 0, sent: 0 })

    expect(await student.saveReminderSettings(studentId, settings({ enabled: false }))).toEqual({ guardiansNotified: true })
    const [off] = await parent.reminderHistory(studentId)
    expect(off).toMatchObject({ enabled: false, by: 'student', notifyGuardians: true, emailedToMeAt: null })

    expect((await sendNotices()).body).toMatchObject({ candidates: 1, sent: 1, failed: 0 })
    expect(inbox).toEqual([expect.objectContaining({ to: ['parent5@local.test'], subject: 'Riley turned off practice reminders' })])
    expect(inbox[0]!.text).toContain("Snoozing a reminder doesn't send this.")
    expect((await sendNotices()).body).toMatchObject({ candidates: 0, sent: 0 })
    expect((await parent.reminderHistory(studentId))[0]!.emailedToMeAt).toBeTruthy()

    // Back on and off again within a day: recorded, not emailed again.
    await student.saveReminderSettings(studentId, settings())
    expect(await student.saveReminderSettings(studentId, settings({ enabled: false }))).toEqual({ guardiansNotified: false })
    expect((await sendNotices()).body).toMatchObject({ candidates: 0 })
    // A guardian turning them off tells nobody either.
    await parent.saveReminderSettings(studentId, settings())
    expect(await parent.saveReminderSettings(studentId, settings({ enabled: false }))).toEqual({ guardiansNotified: false })
    expect(inbox).toHaveLength(1)
  })

  it('an independent adult is never reported; a subscription the push service drops is retired', async () => {
    const adult = await as(ADULT)
    const me = await adult.createSelfStudentProfile({ displayName: 'Alex', graduationYear: null, gradeLevel: null, independent: true, timeZone: TZ })
    const k = await p256()
    await adult.reportNotificationDevice({ deviceId: '5f0f8a1e-4b6a-4a8e-9a55-2d7f3c1b0a03', permission: 'granted', platform: 'desktop', subscription: { endpoint: `https://127.0.0.1:${PORTS.push}/sub/adult`, keys: { p256dh: b64u(k.pub), auth: b64u(authSecret) } } })
    await freshSlot()
    await adult.saveReminderSettings(me, settings())
    pushStatus = 410
    const r = await sendReminders()
    pushStatus = 201
    expect(r.body).toMatchObject({ gone: 1 })
    expect((await adult.studentDevices(me))[0]).toMatchObject({ permission: 'granted', canReceive: false })
    expect(await adult.saveReminderSettings(me, settings({ enabled: false }))).toEqual({ guardiansNotified: false })
    expect((await sendNotices()).body).toMatchObject({ candidates: 0 })
    expect(inbox).toHaveLength(1)
  }, 70_000)
})
