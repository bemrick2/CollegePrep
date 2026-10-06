// Pure helpers for the invitation email, shared with the web tests (no Deno APIs here).

const esc = (s: string) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!)

/** The link base must be one of ours: never a client-supplied site, so the email can't point anywhere else. */
export function pickOrigin(requested: string | null | undefined, allowed: string): string | null {
  const list = allowed
    .split(',')
    .map((s) => s.trim().replace(/\/+$/, ''))
    .filter((s) => /^https?:\/\/[^/\s]+$/.test(s))
  if (list.length === 0) return null
  const want = (requested ?? '').trim().replace(/\/+$/, '')
  return list.includes(want) ? want : list[0]!
}

/** The link carries the token in the URL fragment, which browsers never send to a server (so it stays out of
 *  hosting and CDN logs). */
export function joinLink(origin: string, token: string) {
  return `${origin}/join#t=${encodeURIComponent(token)}`
}

export function inviteEmail(i: { origin: string; token: string; inviteCode: string; inviter: string | null; student: string | null; expiresAt: string }) {
  const who = i.inviter?.trim() || 'Your parent or guardian'
  const link = joinLink(i.origin, i.token)
  const until = new Date(i.expiresAt).toUTCString().replace(' GMT', ' UTC')
  const subject = `${who} invited you to Prep & Price`
  const hello = i.student?.trim() ? `Hi ${i.student.trim()},` : 'Hi,'
  const text = [
    'Prep & Price',
    '',
    hello,
    `${who} invited you to join your Prep & Price family.`,
    '',
    `Join Prep & Price: ${link}`,
    '',
    `Invite code: ${i.inviteCode}`,
    `Valid for 72 hours (until ${until}). It works once.`,
    '',
    "You'll create your own account (or sign in) before joining. If you weren't expecting this, you can ignore it.",
  ].join('\n')
  const html = `<!doctype html><html><body style="margin:0;background:#f4f6f8;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#15212b">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:32px 16px"><tr><td align="center">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:520px;background:#ffffff;border:1px solid #e1e6eb;border-radius:12px;padding:32px">
<tr><td style="font-size:18px;font-weight:700;color:#0f5446">Prep &amp; Price</td></tr>
<tr><td style="padding-top:24px;font-size:16px;line-height:1.5">${esc(hello)}<br>${esc(who)} invited you to join your Prep &amp; Price family.</td></tr>
<tr><td style="padding-top:24px"><a href="${esc(link)}" style="display:inline-block;background:#127a59;color:#ffffff;text-decoration:none;font-weight:700;font-size:16px;padding:14px 24px;border-radius:10px">Join Prep &amp; Price</a></td></tr>
<tr><td style="padding-top:24px;font-size:14px;color:#44515d">Or enter this invite code on the Join page:</td></tr>
<tr><td style="padding-top:6px;font-family:Menlo,Consolas,monospace;font-size:22px;font-weight:700;letter-spacing:2px;color:#15212b">Invite code: ${esc(i.inviteCode)}</td></tr>
<tr><td style="padding-top:12px;font-size:14px;color:#44515d">Valid for 72 hours (until ${esc(until)}). It works once.</td></tr>
<tr><td style="padding-top:24px;font-size:12px;color:#56626e">You'll create your own account (or sign in) before joining. If you weren't expecting this, you can ignore it.</td></tr>
</table></td></tr></table></body></html>`
  return { subject, text, html, link }
}
