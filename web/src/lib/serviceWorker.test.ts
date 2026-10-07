import swSource from '../../public/sw.js?raw'
import { describe, expect, it } from 'vitest'

/** Loads public/sw.js with a fake service-worker global and returns its handlers and helpers. */
function loadWorker() {
  const listeners: Record<string, (e: unknown) => void> = {}
  const shown: { title: string; options: Record<string, unknown> }[] = []
  const opened: string[] = []
  const posted: { url: string; body: string }[] = []
  const self = {
    location: { origin: 'https://app.example' },
    addEventListener: (t: string, f: (e: unknown) => void) => (listeners[t] = f),
    skipWaiting: () => {},
    registration: { showNotification: (title: string, options: Record<string, unknown>) => (shown.push({ title, options }), Promise.resolve()) },
    clients: { claim: () => Promise.resolve(), matchAll: () => Promise.resolve([]), openWindow: (u: string) => (opened.push(u), Promise.resolve()) },
  }
  const module = { exports: {} as { reminderNotification: (d: unknown) => { title: string; options: Record<string, unknown> }; safeUrl: (u: string) => string } }
  const fetch = (url: string, init: { body: string }) => (posted.push({ url, body: init.body }), Promise.resolve({}))
  new Function('self', 'module', 'fetch', swSource)(self, module, fetch)
  const wait: Promise<unknown>[] = []
  const fire = (type: string, e: Record<string, unknown>) => listeners[type]!({ ...e, waitUntil: (p: Promise<unknown>) => wait.push(p) })
  return { fire, shown, opened, posted, wait, ...module.exports }
}

const payload = { title: 'Prep & Price', body: 'Got a few minutes? Try a quick practice session.', url: 'https://app.example/student/practice?quick=1&r=abc', snooze: { endpoint: 'https://fn.example/practice-reminder-action', token: 't0k' } }

describe('service worker', () => {
  it('shows the reminder with Start and Remind me later', async () => {
    const w = loadWorker()
    w.fire('push', { data: { json: () => payload } })
    await Promise.all(w.wait)
    expect(w.shown[0]).toMatchObject({ title: 'Prep & Price', options: { body: 'Got a few minutes? Try a quick practice session.', tag: 'practice-reminder' } })
    expect((w.shown[0]!.options.actions as { title: string }[]).map((a) => a.title)).toEqual(['Start', 'Remind me later'])
  })

  it('a tap opens the short session; "Remind me later" posts only the token and opens nothing', async () => {
    const w = loadWorker()
    const n = w.reminderNotification(payload)
    w.fire('notificationclick', { action: '', notification: { data: n.options.data, close: () => {} } })
    w.fire('notificationclick', { action: 'later', notification: { data: n.options.data, close: () => {} } })
    await Promise.all(w.wait)
    expect(w.opened).toEqual(['/student/practice?quick=1&r=abc'])
    expect(w.posted).toEqual([{ url: 'https://fn.example/practice-reminder-action', body: '{"token":"t0k"}' }])
  })

  it('never opens another site from a payload', () => {
    const w = loadWorker()
    expect(w.safeUrl('https://evil.example/x')).toBe('/student/practice?quick=1')
    expect(w.safeUrl('/student/practice?quick=1&r=1')).toBe('/student/practice?quick=1&r=1')
  })
})
