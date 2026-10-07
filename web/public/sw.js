/* Prep & Price service worker: shows practice reminders and handles taps. No caching, no fetch handling.
 *
 * Push payload (send-practice-reminders): { title, body, url, tag, snooze: { endpoint, token, minutes } }.
 * - Tapping the notification (or "Start") opens a short practice session (url has ?quick=1).
 * - "Remind me later" posts the signed token to the action endpoint; it snoozes once and tells nobody.
 * Action buttons aren't shown by every browser (iPhone and Safari show none); there, the app offers
 * "Remind me later" on the home screen instead.
 */
self.addEventListener('install', () => self.skipWaiting())
self.addEventListener('activate', (event) => event.waitUntil(self.clients.claim()))

function reminderNotification(data) {
  const d = data && typeof data === 'object' ? data : {}
  return {
    title: typeof d.title === 'string' ? d.title : 'Prep & Price',
    options: {
      body: typeof d.body === 'string' ? d.body : 'Got a few minutes? Try a quick practice session.',
      tag: 'practice-reminder',
      renotify: false,
      icon: '/icon-192.png',
      badge: '/icon-192.png',
      data: { url: typeof d.url === 'string' ? d.url : '/student/practice?quick=1', snooze: d.snooze || null },
      actions: [
        { action: 'start', title: 'Start' },
        ...(d.snooze ? [{ action: 'later', title: 'Remind me later' }] : []),
      ],
    },
  }
}

/** Only same-origin app paths are opened, whatever the payload says. */
function safeUrl(url) {
  try {
    const u = new URL(url, self.location.origin)
    return u.origin === self.location.origin ? u.pathname + u.search : '/student/practice?quick=1'
  } catch {
    return '/student/practice?quick=1'
  }
}

self.addEventListener('push', (event) => {
  let data = null
  try {
    data = event.data ? event.data.json() : null
  } catch {
    data = null
  }
  const n = reminderNotification(data)
  event.waitUntil(self.registration.showNotification(n.title, n.options))
})

self.addEventListener('notificationclick', (event) => {
  const data = event.notification.data || {}
  event.notification.close()
  if (event.action === 'later' && data.snooze && data.snooze.endpoint && data.snooze.token) {
    event.waitUntil(
      fetch(data.snooze.endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ token: data.snooze.token }) }).catch(() => undefined),
    )
    return
  }
  const target = safeUrl(data.url)
  event.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((wins) => {
      for (const w of wins) {
        if (new URL(w.url).origin === self.location.origin && 'navigate' in w) return w.navigate(target).then((c) => (c || w).focus())
      }
      return self.clients.openWindow(target)
    }),
  )
})

if (typeof module !== 'undefined') module.exports = { reminderNotification, safeUrl }
