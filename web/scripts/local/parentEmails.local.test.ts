// Lives outside src/ because it uses Node APIs (crypto, process, child_process, http).
//
// End-to-end check of parent accountability emails: the real edge function (supabase/functions/send-weekly-digest)
// running under Deno, against the local disposable backend with the CR-22 reference SQL, and a fake mail endpoint
// standing in for Resend. Skipped unless LOCAL_BACKEND_URL and DENO_BIN are set:
//
//   DENO_BIN=$(command -v deno) scripts/local/live_stack.sh test
import { spawn, type ChildProcess } from 'node:child_process'
import { createHmac } from 'node:crypto'
import { createServer, type Server } from 'node:http'
import { createClient } from '@supabase/supabase-js'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { LiveSource } from '../../src/lib/data/live/liveSource'

const URL_ = process.env.LOCAL_BACKEND_URL
const DENO = process.env.DENO_BIN
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000000a3'
const OTHER_PARENT = '00000000-0000-4000-a000-0000000000a4'
const STUDENT = '00000000-0000-4000-a000-000000000052'
const CRON = 'local-digest-secret'
const FN_PORT = 54331
const MAIL_PORT = 54332

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
  return new LiveSource(sb, { weeklyDigest: true })
}
const monday = (d = new Date()) => {
  const x = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()))
  x.setUTCDate(x.getUTCDate() - ((x.getUTCDay() + 6) % 7))
  return x.toISOString().slice(0, 10)
}
const pause = () => new Promise((r) => setTimeout(r, 25))

describe.skipIf(!URL_ || !DENO)('parent emails: edge function + local backend + fake mail', () => {
  let fn: ChildProcess
  let mail: Server
  const inbox: { to: string[]; subject: string; text: string; key: string | undefined }[] = []
  let mailFails = false
  const week = monday()
  let parentId = ''

  const call = async (body: unknown, secret = CRON) => {
    const r = await fetch(`http://127.0.0.1:${FN_PORT}`, { method: 'POST', headers: { 'x-digest-secret': secret, 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
    return { status: r.status, body: (await r.json()) as Record<string, unknown> }
  }

  beforeAll(async () => {
    mail = createServer((req, res) => {
      let raw = ''
      req.on('data', (c) => (raw += c))
      req.on('end', () => {
        if (mailFails) {
          res.writeHead(500).end()
          return
        }
        const m = JSON.parse(raw)
        inbox.push({ to: m.to, subject: m.subject, text: m.text, key: req.headers['idempotency-key'] as string | undefined })
        res.writeHead(200, { 'content-type': 'application/json' }).end('{"id":"local"}')
      })
    }).listen(MAIL_PORT, '127.0.0.1')

    fn = spawn(DENO!, ['run', '--allow-net', '--allow-env', '--allow-read', '../supabase/functions/send-weekly-digest/index.ts'], {
      env: {
        ...process.env,
        DENO_SERVE_ADDRESS: `tcp:127.0.0.1:${FN_PORT}`,
        SUPABASE_URL: URL_!,
        SUPABASE_SERVICE_ROLE_KEY: jwt({ sub: 'service', role: 'service_role' }),
        DIGEST_CRON_SECRET: CRON,
        RESEND_API_KEY: 'local-test-key',
        RESEND_API_URL: `http://127.0.0.1:${MAIL_PORT}/emails`,
        APP_ORIGINS: 'https://app.local.test',
      },
      stdio: ['ignore', 'pipe', 'pipe'],
    })
    for (let i = 0; i < 300; i++) {
      try {
        await fetch(`http://127.0.0.1:${FN_PORT}`, { method: 'GET' })
        break
      } catch {
        await new Promise((r) => setTimeout(r, 200))
      }
    }

    // A family that opts in: Ana practises, Ben never has; and another family that does not opt in.
    const parent = await as(PARENT)
    parentId = PARENT
    const hh = await parent.createHousehold('Digest family', 'UTC')
    const ana = await parent.addStudent(hh, 'Ana', 2028, 11)
    const ben = await parent.addStudent(hh, 'Ben', 2029, 10)
    await parent.setWeeklyGoal(ana, week, 10, null)
    const inv = await parent.createStudentInvitation(hh, ana)
    const student = await as(STUDENT)
    await student.acceptInvitation(inv.inviteCode!)
    const session = await student.startSession(ana, 10, 'act')
    for (const item of session.items.slice(0, 3)) {
      const a = await student.startAttempt(ana, item.question.id, session.id)
      await pause()
      await student.submitAttempt(a, { answer: 'A', activeMs: 5 })
    }
    await parent.setAlertPreference(ana, { enabled: false, inactivityDays: 3, weeklyDigest: true })
    await parent.setAlertPreference(ben, { enabled: true, inactivityDays: 1, weeklyDigest: true })
    expect(await parent.getAlertPreference(ben)).toEqual({ enabled: true, inactivityDays: 1, weeklyDigest: true })

    const other = await as(OTHER_PARENT)
    const hh2 = await other.createHousehold('Other family', 'UTC')
    const cleo = await other.addStudent(hh2, 'Cleo', 2028, 11)
    await other.setAlertPreference(cleo, { enabled: false, inactivityDays: 3, weeklyDigest: false })
  }, 90_000)

  afterAll(() => {
    fn?.kill()
    mail?.close()
  })

  it('refuses callers without the scheduler secret', async () => {
    expect((await call({ dry_run: true }, 'wrong')).status).toBe(401)
    expect((await call({ dry_run: true }, '')).status).toBe(401)
  })

  it('composes one summary per opted-in guardian with the dashboard numbers (dry run sends nothing)', async () => {
    const r = await call({ mode: 'weekly', week_start: week, dry_run: true })
    expect(r.status).toBe(200)
    const emails = r.body.emails as { user_id: string; subject: string; text: string }[]
    expect(emails.map((e) => e.user_id)).toEqual([parentId])
    const t = emails[0]!.text
    expect(emails[0]!.subject).toMatch(/^Your family's week on Prep & Price/)
    expect(t).toContain('3 of 10 practice questions (goal not met), practised on 1 day of 7.')
    expect(t).toContain("Ben hasn't practised yet.")
    expect(t).toContain('0 practice questions, practised on 0 days of 7. No weekly goal was set.')
    expect(t).toContain('not an ACT or SAT score')
    expect(t).not.toMatch(/@local\.test/)
    expect(inbox).toHaveLength(0)
  })

  it('sends once: a second run for the same week sends nothing', async () => {
    const first = await call({ mode: 'weekly', week_start: week })
    expect(first.body).toMatchObject({ candidates: 1, sent: 1, failed: 0 })
    expect(inbox).toHaveLength(1)
    expect(inbox[0]).toMatchObject({ to: ['parent3@local.test'], key: `weekly_digest:${parentId}:${week}` })
    const again = await call({ mode: 'weekly', week_start: week })
    expect(again.body).toMatchObject({ candidates: 0, sent: 0 })
    expect(inbox).toHaveLength(1)
  })

  it('inactivity alert: a failed send is retried next run, then never repeated for the same stretch', async () => {
    mailFails = true
    const failed = await call({ mode: 'inactivity' })
    expect(failed.body).toMatchObject({ candidates: 1, sent: 0, failed: 1 })
    mailFails = false
    const retried = await call({ mode: 'inactivity' })
    expect(retried.body).toMatchObject({ candidates: 1, sent: 1 })
    expect(inbox.at(-1)).toMatchObject({ to: ['parent3@local.test'], subject: "Ben hasn't practised yet" })
    const again = await call({ mode: 'inactivity' })
    expect(again.body).toMatchObject({ candidates: 0, sent: 0 })
  })
})
