// Builds src/lib/data/demo/questionReviews.json from review outputs, pinning each approval to the item's content hash.
//
//   npx vite-node scripts/local/recordReviews.ts <review-dir>
//
// <review-dir> holds JSON arrays written by the reviewers:
//   solver_a.json, solver_b.json  blind solves of every item: [{id, answer}]
//   audit.json                    key and explanation audit: [{id, verdict, key_correct, problems}]
//   re_blind.json, re_audit.json  optional: blind solve + audit of items revised after the first pass
//   resolutions.json              optional: [{id, note}] for disagreements settled by working the item by hand
// An item is approved only if its latest audit approves it, the key is correct, and every blind solve matched
// the key or a recorded resolution explains the mismatch.
import { existsSync, readFileSync, writeFileSync } from 'node:fs'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { contentHash, type QuestionReview } from '../../src/lib/data/demo/questionReview'

const dir = process.argv[2]
if (!dir) throw new Error('usage: recordReviews.ts <review-dir>')
const load = <T>(f: string): T[] => (existsSync(`${dir}/${f}`) ? (JSON.parse(readFileSync(`${dir}/${f}`, 'utf8')) as T[]) : [])
type Solve = { id: string; answer: string }
type Audit = { id: string; verdict: 'approve' | 'fix' | 'reject'; key_correct: boolean; problems: string[] }
const byId = <T extends { id: string }>(xs: T[]) => new Map(xs.map((x) => [x.id, x]))
const a = byId(load<Solve>('solver_a.json'))
const b = byId(load<Solve>('solver_b.json'))
const audit = byId(load<Audit>('audit.json'))
const reBlind = byId(load<Solve>('re_blind.json'))
const reAudit = byId(load<Audit>('re_audit.json'))
const resolved = byId(load<{ id: string; note: string }>('resolutions.json'))

const num = (s: string) => {
  const t = String(s).replace(/[\s$]/g, '').replace(/\(.*\)$/, '')
  const m = t.match(/^(-?\d+)\/(\d+)$/)
  return m ? Number(m[1]) / Number(m[2]) : Number(t)
}
function matches(q: (typeof QUESTIONS)[number], ans: string | undefined) {
  if (ans == null) return false
  if (q.answer_format === 'choice') return String(ans).trim().toUpperCase() === q.accepted_answers[0]
  const v = num(ans)
  return q.accepted_answers.some((k) => Math.abs(num(k) - v) < 0.0006)
}

const today = new Date().toISOString().slice(0, 10)
const items: Record<string, QuestionReview> = {}
for (const q of QUESTIONS) {
  const revised = reAudit.has(q.id)
  const solves = revised ? [reBlind.get(q.id)] : [a.get(q.id), b.get(q.id)]
  const hits = solves.filter((s) => matches(q, s?.answer)).length
  const au = revised ? reAudit.get(q.id) : audit.get(q.id)
  const res = resolved.get(q.id)
  const ok = au?.verdict === 'approve' && au.key_correct && (hits === solves.length || !!res)
  const notes = [revised ? 'Revised after the first audit; re-reviewed.' : null, res?.note ?? null, ...(au?.problems ?? []).map((p) => `Audit: ${p}`)].filter(Boolean).join(' ')
  items[q.id] = {
    status: ok ? 'approved' : au?.verdict === 'reject' ? 'rejected' : 'changes_needed',
    hash: contentHash(q),
    reviewed_at: today,
    blind_solves: [hits, solves.length],
    audit: au?.verdict ?? 'fix',
    notes: notes || null,
  }
}
const out = {
  method: 'Two independent blind solves (no key, no explanations) of every item, plus an audit of key, numeric answer forms, distractors, hints and explanations. Items revised after the audit get a fresh blind solve and audit. Disagreements are worked by hand and recorded.',
  reviewer: 'AI reviewers in separate contexts (Claude), coordinated by the Design workstream',
  human_reviewed: false,
  items,
}
writeFileSync('src/lib/data/demo/questionReviews.json', JSON.stringify(out, null, 1) + '\n')
const n = (s: string) => Object.values(items).filter((i) => i.status === s).length
console.log(`approved ${n('approved')}, changes_needed ${n('changes_needed')}, rejected ${n('rejected')}`)
