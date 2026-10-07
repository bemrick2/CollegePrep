// Pure helpers for parent accountability emails: the Monday weekly summary and the inactivity alert.
// Shared with the web app (its in-app preview and tests import this file), so the preview is exactly what is sent.
// No Deno APIs and no imports here.
//
// Content rules: practice results are labelled as practice on original questions; no ACT/SAT score, estimate or
// prediction appears anywhere; nothing is said that the data does not show.

/** One student's last completed week, from weekly_digest_payload (CR-22). */
export interface DigestStudent {
  student_id: string
  student_name: string
  /** Monday of the summarized week, in the household's time zone. */
  week_start: string
  goal_questions: number | null
  /** Answers submitted that week, as on the dashboard (student_weekly_progress; benchmark answers count as practice). */
  questions_submitted: number
  days_practised: number
  last_practice_at: string | null
  /** Up to three skills flagged by student_skill_estimates. */
  focus: { skill_name: string; section: string; reason: 'knowledge' | 'pacing'; accuracy: number | null; pacing_ratio: number | null }[]
  last_check: { kind: 'initial' | 'mini' | 'full'; completed_at: string } | null
  /** Present only when this guardian turned on the alert and the threshold is reached. */
  inactivity: { threshold_days: number; days_inactive: number | null } | null
}

export interface DigestRecipient {
  user_id: string
  email: string
  guardian_name: string | null
  time_zone: string
  students: DigestStudent[]
}

export interface InactivityAlert {
  user_id: string
  email: string
  guardian_name: string | null
  student_name: string
  threshold_days: number
  days_inactive: number | null
  last_practice_at: string | null
  time_zone: string
}

const esc = (s: string) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!)
const SECTION: Record<string, string> = { english: 'English', math: 'Math', reading: 'Reading', science: 'Science', reading_writing: 'Reading and Writing' }
const CHECK: Record<string, string> = { initial: 'Starting benchmark', mini: 'Mini benchmark', full: 'Full benchmark' }
const plural = (n: number, one: string, many = `${one}s`) => `${n} ${n === 1 ? one : many}`

/** "Oct 5" in the household's time zone; dates are YYYY-MM-DD (noon UTC avoids day shifts) or ISO timestamps. */
export function shortDate(iso: string, timeZone: string) {
  const d = /^\d{4}-\d{2}-\d{2}$/.test(iso) ? new Date(`${iso}T12:00:00Z`) : new Date(iso)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: /^\d{4}-\d{2}-\d{2}$/.test(iso) ? 'UTC' : timeZone })
}

/** inProgress: the week isn't over (the in-app preview), so an unmet goal is not called missed. */
export function weekLine(s: DigestStudent, inProgress = false): string {
  const days = `practised on ${plural(s.days_practised, 'day')} of 7${inProgress ? ' so far' : ''}`
  if (s.goal_questions == null) return `${plural(s.questions_submitted, 'practice question')}, ${days}. No weekly goal was set.`
  const met = s.questions_submitted >= s.goal_questions
  return `${s.questions_submitted} of ${s.goal_questions} practice questions (${met ? 'goal met' : inProgress ? 'week in progress' : 'goal not met'}), ${days}.`
}

export function focusLines(s: DigestStudent): string[] {
  return s.focus.slice(0, 3).map((f) =>
    f.reason === 'knowledge'
      ? `${f.skill_name} (${SECTION[f.section] ?? f.section}): ${f.accuracy == null ? 'accuracy low' : `${Math.round(f.accuracy * 100)}% right`} in practice`
      : `${f.skill_name} (${SECTION[f.section] ?? f.section}): answering at ${f.pacing_ratio == null ? 'a slow' : `${f.pacing_ratio.toFixed(1)}×`} test pace`,
  )
}

export function inactivityLine(s: DigestStudent, timeZone: string): string | null {
  if (!s.inactivity) return null
  if (!s.last_practice_at) return `${s.student_name} hasn't practised yet.`
  return `${s.student_name} hasn't practised since ${shortDate(s.last_practice_at, timeZone)}${s.inactivity.days_inactive != null ? ` (${plural(s.inactivity.days_inactive, 'day')})` : ''}.`
}

const LABEL = 'Practice results on original Prep & Price questions. They are not an ACT or SAT score and are not converted to one.'
const WHY = 'You get this because you turned on the weekly summary in Prep & Price. Turn it off on the parent dashboard.'

export function weeklyDigestEmail(r: DigestRecipient, origin: string, opts: { inProgress?: boolean } = {}) {
  const hello = r.guardian_name?.trim() ? `Hi ${r.guardian_name.trim().split(/\s+/)[0]},` : 'Hi,'
  const one = r.students.length === 1 ? r.students[0]! : null
  const week = r.students[0] ? shortDate(r.students[0].week_start, r.time_zone) : ''
  const subject = one ? `${one.student_name}'s week on Prep & Price: ${one.goal_questions != null ? `${one.questions_submitted} of ${one.goal_questions} questions` : `${plural(one.questions_submitted, 'question')}`}` : `Your family's week on Prep & Price (week of ${week})`
  const link = `${origin}/parent`

  const blocks = r.students.map((s) => {
    const lines = [inactivityLine(s, r.time_zone), weekLine(s, opts.inProgress)].filter((x): x is string => !!x)
    const focus = focusLines(s)
    const check = s.last_check ? `Last progress check: ${CHECK[s.last_check.kind] ?? s.last_check.kind}, ${shortDate(s.last_check.completed_at, r.time_zone)}.` : 'No starting benchmark yet. It comes first: the weekly plan depends on it.'
    return { s, lines, focus, check }
  })

  const text = [
    'Prep & Price',
    '',
    hello,
    `Here is the week of ${week}.`,
    ...blocks.flatMap((b) => [
      '',
      b.s.student_name,
      ...b.lines,
      ...(b.focus.length ? ['Working on:', ...b.focus.map((f) => `- ${f}`)] : ['No weak skills flagged yet (skills are flagged after about five answers each).']),
      b.check,
    ]),
    '',
    `Open the parent dashboard: ${link}`,
    '',
    LABEL,
    WHY,
  ].join('\n')

  const p = (s: string, style = '') => `<tr><td style="padding-top:8px;font-size:15px;line-height:1.5;${style}">${esc(s)}</td></tr>`
  const studentHtml = blocks
    .map(
      (b) => `<tr><td style="padding-top:24px;font-size:17px;font-weight:700;color:#15212b">${esc(b.s.student_name)}</td></tr>
${b.lines.map((l, i) => p(l, i === 0 && b.s.inactivity ? 'color:#8a4b00;font-weight:600' : '')).join('\n')}
${b.focus.length ? `<tr><td style="padding-top:8px;font-size:15px;line-height:1.5">Working on:<ul style="margin:4px 0 0 18px;padding:0">${b.focus.map((f) => `<li>${esc(f)}</li>`).join('')}</ul></td></tr>` : p('No weak skills flagged yet (skills are flagged after about five answers each).', 'color:#56626e')}
${p(b.check, 'color:#44515d')}`,
    )
    .join('\n')
  const html = `<!doctype html><html><body style="margin:0;background:#f4f6f8;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#15212b">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:32px 16px"><tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#ffffff;border:1px solid #e1e6eb;border-radius:12px;padding:32px">
<tr><td style="font-size:18px;font-weight:700;color:#0f5446">Prep &amp; Price</td></tr>
${p(hello, 'padding-top:20px')}
${p(`Here is the week of ${week}.`)}
${studentHtml}
<tr><td style="padding-top:24px"><a href="${esc(link)}" style="display:inline-block;background:#127a59;color:#ffffff;text-decoration:none;font-weight:700;font-size:15px;padding:12px 20px;border-radius:10px">Open the parent dashboard</a></td></tr>
<tr><td style="padding-top:24px;font-size:12px;color:#56626e">${esc(LABEL)}<br>${esc(WHY)}</td></tr>
</table></td></tr></table></body></html>`
  return { subject, text, html }
}

export function inactivityEmail(a: InactivityAlert, origin: string) {
  const hello = a.guardian_name?.trim() ? `Hi ${a.guardian_name.trim().split(/\s+/)[0]},` : 'Hi,'
  const since = a.last_practice_at ? `since ${shortDate(a.last_practice_at, a.time_zone)}` : 'yet'
  const subject = `${a.student_name} hasn't practised ${a.last_practice_at ? `in ${plural(a.days_inactive ?? a.threshold_days, 'day')}` : 'yet'}`
  const body = `${a.student_name} hasn't practised ${since}. You asked to hear after ${plural(a.threshold_days, 'day')} without practice.`
  const link = `${origin}/parent`
  const why = `You get this because you turned on this alert in Prep & Price. Change it on the parent dashboard. You'll get it once per stretch without practice.`
  const text = ['Prep & Price', '', hello, body, '', `Open the parent dashboard: ${link}`, '', why].join('\n')
  const html = `<!doctype html><html><body style="margin:0;background:#f4f6f8;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#15212b">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:32px 16px"><tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background:#ffffff;border:1px solid #e1e6eb;border-radius:12px;padding:32px">
<tr><td style="font-size:18px;font-weight:700;color:#0f5446">Prep &amp; Price</td></tr>
<tr><td style="padding-top:20px;font-size:15px;line-height:1.5">${esc(hello)}<br>${esc(body)}</td></tr>
<tr><td style="padding-top:24px"><a href="${esc(link)}" style="display:inline-block;background:#127a59;color:#ffffff;text-decoration:none;font-weight:700;font-size:15px;padding:12px 20px;border-radius:10px">Open the parent dashboard</a></td></tr>
<tr><td style="padding-top:24px;font-size:12px;color:#56626e">${esc(why)}</td></tr>
</table></td></tr></table></body></html>`
  return { subject, text, html }
}

/** Monday of the last completed week (UTC). The payload RPC resolves each household's own week from it. */
export function lastCompletedWeekStart(now: Date): string {
  const d = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()))
  const dow = (d.getUTCDay() + 6) % 7 // Monday = 0
  d.setUTCDate(d.getUTCDate() - dow - 7)
  return d.toISOString().slice(0, 10)
}

/** A linked student turned practice reminders off in the app (CR-27). One email per guardian per change. */
export interface RemindersOffNotice {
  user_id: string
  email: string
  guardian_name: string | null
  student_name: string
  changed_at: string
  time_zone: string
}

export function remindersOffEmail(n: RemindersOffNotice, origin: string) {
  const hello = n.guardian_name?.trim() ? `Hi ${n.guardian_name.trim().split(/\s+/)[0]},` : 'Hi,'
  const when = new Date(n.changed_at).toLocaleString('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', timeZone: n.time_zone })
  const subject = `${n.student_name} turned off practice reminders`
  const body = `${n.student_name} turned off practice reminders in Prep & Price on ${when}. Practice itself isn't affected: ${n.student_name} can still practise any time, and progress still shows on your dashboard.`
  const link = `${origin}/parent`
  const why = `You get this because you're a guardian in ${n.student_name}'s household. ${n.student_name} was told you'd be notified. Snoozing a reminder doesn't send this.`
  const text = ['Prep & Price', '', hello, body, '', `Open the parent dashboard: ${link}`, '', why].join('\n')
  const html = `<!doctype html><html><body style="margin:0;background:#f4f6f8;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#15212b">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:32px 16px"><tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background:#ffffff;border:1px solid #e1e6eb;border-radius:12px;padding:32px">
<tr><td style="font-size:18px;font-weight:700;color:#0f5446">Prep &amp; Price</td></tr>
<tr><td style="padding-top:20px;font-size:15px;line-height:1.5">${esc(hello)}<br>${esc(body)}</td></tr>
<tr><td style="padding-top:24px"><a href="${esc(link)}" style="display:inline-block;background:#127a59;color:#ffffff;text-decoration:none;font-weight:700;font-size:15px;padding:12px 20px;border-radius:10px">Open the parent dashboard</a></td></tr>
<tr><td style="padding-top:24px;font-size:12px;color:#56626e">${esc(why)}</td></tr>
</table></td></tr></table></body></html>`
  return { subject, text, html }
}
