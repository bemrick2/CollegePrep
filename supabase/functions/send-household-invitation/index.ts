// Emails a student invitation. Runs as the signed-in guardian (their JWT), so every permission check is the
// database's own: create_student_invitation and prepare_invitation_email refuse anyone who can't manage the
// student. No service-role key is used. Neither the link token nor the invite code is ever logged; failures are
// logged by kind only.
//
// Secrets (Supabase → Edge Functions → Secrets): RESEND_API_KEY, INVITE_FROM_EMAIL ("Prep & Price <invites@…>"),
// APP_ORIGINS (optional: comma-separated allowed site origins, first is the default; defaults to staging).
import { createClient } from 'npm:@supabase/supabase-js@2'
import { inviteEmail, pickOrigin } from './email.ts'

const DEFAULT_ORIGINS = 'https://college-optimizer-staging.netlify.app'

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
}

const json = (status: number, body: unknown) => new Response(JSON.stringify(body), { status, headers: { ...CORS, 'Content-Type': 'application/json' } })

interface Body {
  householdId?: string
  studentId?: string
  email?: string
  /** Resend an invitation the parent already holds instead of creating a new one: its link token and invite code. */
  code?: string
  inviteCode?: string
  origin?: string
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: CORS })
  if (req.method !== 'POST') return json(405, { error: 'method_not_allowed' })
  const auth = req.headers.get('Authorization')
  if (!auth) return json(401, { error: 'Authentication required' })

  let body: Body
  try {
    body = await req.json()
  } catch {
    return json(400, { error: 'Invalid request' })
  }
  const email = (body.email ?? '').trim().toLowerCase()
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || email.length > 320) return json(400, { error: 'Enter a valid email address' })

  const sb = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_ANON_KEY')!, {
    global: { headers: { Authorization: auth } },
    auth: { persistSession: false },
  })

  // 1. The invitation: a new one (replacing that student's earlier outstanding ones), or the one being resent.
  let code = (body.code ?? '').trim().toLowerCase()
  let inviteCode = (body.inviteCode ?? '').trim().toUpperCase()
  if (code && !inviteCode) return json(400, { error: 'Resending needs the invite code too' })
  if (!code) {
    if (!body.householdId || !body.studentId) return json(400, { error: 'Choose the student to invite' })
    const { data, error } = await sb.rpc('create_student_invitation', { p_household: body.householdId, p_student: body.studentId, p_recipient_email: email })
    if (error) return json(error.code === '42501' ? 403 : 400, { error: error.message })
    const row = (data as { code: string; invite_code: string }[])[0]!
    code = row.code
    inviteCode = row.invite_code
  }

  // 2. Check it is still usable and record the send; returns names and expiry, never the hash.
  const prep = await sb.rpc('prepare_invitation_email', { p_code: code, p_recipient_email: email, p_invite_code: inviteCode })
  if (prep.error) {
    // A new invitation exists even if it can't be emailed: hand it back so the parent can copy the link or code.
    return json(200, body.code ? { emailed: false, reason: 'rejected', error: prep.error.message } : { code, inviteCode, emailed: false, reason: 'rejected', error: prep.error.message })
  }
  const row = (prep.data as { invitation_id: string; student_name: string | null; inviter_name: string | null; expires_at: string }[])[0]!
  const result = { code, inviteCode, invitationId: row.invitation_id, expiresAt: row.expires_at }

  // 3. Send. Any failure leaves the invitation valid.
  const key = Deno.env.get('RESEND_API_KEY')
  const from = Deno.env.get('INVITE_FROM_EMAIL')
  if (!key || !from) {
    console.error('invite-email: not configured')
    return json(200, { ...result, emailed: false, reason: 'not_configured' })
  }
  // Staging is the default link base until production origins are configured.
  const origin = pickOrigin(body.origin ?? req.headers.get('Origin'), Deno.env.get('APP_ORIGINS') || DEFAULT_ORIGINS)
  if (!origin) {
    console.error('invite-email: no allowed origin configured')
    return json(200, { ...result, emailed: false, reason: 'not_configured' })
  }
  const msg = inviteEmail({ origin, token: code, inviteCode, inviter: row.inviter_name, student: row.student_name, expiresAt: row.expires_at })
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from, to: [email], subject: msg.subject, html: msg.html, text: msg.text }),
    })
    if (!r.ok) {
      console.error('invite-email: provider status', r.status)
      return json(200, { ...result, emailed: false, reason: 'provider' })
    }
  } catch {
    console.error('invite-email: provider unreachable')
    return json(200, { ...result, emailed: false, reason: 'provider' })
  }
  return json(200, { ...result, emailed: true })
})
