import type { FixtureQuestion } from './fixtures'
import { contentHash } from './questionReview'
import ledger from './editorialLedger.json'

/**
 * The human editorial review (docs/product/CONTENT_PLAN.md §5, stages 2–8), recorded in the repository so review can
 * start while the database is paused. One sign-off per person per stage, each pinned to the item's content hash:
 * any edit to what a student sees voids every sign-off made before it, and the item goes back to stage 4.
 *
 * This ledger doesn't change what is served. The AI review gate (questionReview.ts) still decides that, and nothing
 * here claims a human review that the ledger doesn't show. Once every stage passes and a named approver signs, an
 * item is `humanApproved`; switching the serving gate to require it is an owner decision (launch checklist A2).
 *
 * Items with no ledger entry were drafted and reviewed by AI and enter at stage 3 (they are not grandfathered).
 */

export type Stage = 2 | 3 | 4 | 5 | 6 | 7 | 8
export const STAGE_NAME: Record<Stage, string> = {
  2: 'Draft',
  3: 'Rights check',
  4: 'Blind solve ×2',
  5: 'Content audit',
  6: 'Fairness and sensitivity',
  7: 'Copy edit and accessibility',
  8: 'Approve',
}

export interface SignOff {
  stage: Stage
  /** A named person. Never "AI", a team name or a role. */
  by: string
  date: string
  result: 'pass' | 'fail'
  /** contentHash(q) when signed. */
  hash: string
  /** Stage 3: the license or source basis ("original", "public domain: <source>", "CC BY 4.0: <attribution>"). */
  license?: string
  /** Stage 4: the answer given without the key, and the time taken. */
  answer?: string
  seconds?: number
  note?: string
}

export interface LedgerEntry {
  /** Who drafted the item: a person, or "AI (Claude)" for the existing bank. */
  author: string
  signoffs: SignOff[]
}

export interface Ledger {
  items: Record<string, LedgerEntry>
}

export const EDITORIAL_LEDGER = ledger as unknown as Ledger
export const AI_AUTHOR = 'AI (Claude)'
const ALLOWED_LICENSE = /^(original|public domain|federal|cc by(-sa)? \d)/i
/**
 * One canonical form for comparing reviewer names, so variants of one name count as one person: Unicode-normalized,
 * invisible characters and bracketed asides removed, punctuation ignored, case folded, and word order ignored.
 * "Jo  Writer", "Jo Writer.", "Jo-Writer", "Writer, Jo" and "Jo Writer (author)" are all "jo writer". This errs toward
 * merging names, which can only block a sign-off, never let an author through. Look-alike letters from another script
 * are refused by isNotAPerson. Initials ("J. Writer") still need the content lead's check against the reviewer list.
 */
export const canonicalPerson = (s: string) =>
  s
    .normalize('NFKC')
    .replace(/\p{Cf}/gu, '')
    .replace(/\([^)]*\)|\[[^\]]*\]/g, ' ')
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, ' ')
    .trim()
    .split(' ')
    .filter(Boolean)
    .sort()
    .join(' ')

/** Whole names that are a tool, a role or a placeholder, not a person. */
const NOT_A_PERSON_WHOLE = new Set([
  'ai', 'a i', 'claude', 'anthropic', 'gpt', 'chatgpt', 'openai', 'gemini', 'bard', 'copilot', 'llama', 'mistral', 'opus', 'sonnet', 'haiku',
  'assistant', 'bot', 'llm', 'model', 'system', 'team', 'staff', 'reviewer', 'solver', 'auditor', 'lead', 'content lead', 'editor', 'author',
  'admin', 'tbd', 'todo', 'unknown', 'na', 'n a', 'none', 'anonymous', 'anon', 'test', 'intake', 'the content lead', 'the reviewer', 'the team',
])
/** First words that only a tool or a group uses ("Claude Opus", "GPT 5", "Team Rights"). */
const NOT_A_PERSON_FIRST = /^(claude|anthropic|chatgpt|gpt|openai|gemini|copilot|assistant|llm|team|the)\b/
const SCRIPTS = [/\p{Script=Latin}/u, /\p{Script=Cyrillic}/u, /\p{Script=Greek}/u]
/**
 * A screen, not proof of identity: refuses obvious non-people (AI tools, roles, teams, placeholders) and names mixing
 * Latin, Cyrillic or Greek letters (look-alike spoofs). Real names such as "Ai Nguyen" or "Na Young Kim" pass. The
 * content lead still checks every name against the people actually doing the review.
 */
export const isNotAPerson = (s: string) => {
  const raw = s.normalize('NFKC').replace(/\p{Cf}/gu, '').trim()
  if (/^ai\s*:/i.test(raw) || /^ai\s*\(/i.test(raw)) return true
  if (SCRIPTS.filter((re) => re.test(raw)).length > 1) return true
  const inOrder = raw.toLowerCase().replace(/\([^)]*\)|\[[^\]]*\]/g, ' ').replace(/[^\p{L}\p{N}]+/gu, ' ').trim()
  return !inOrder || NOT_A_PERSON_WHOLE.has(inOrder) || NOT_A_PERSON_WHOLE.has(inOrder.replace(/ /g, '')) || NOT_A_PERSON_FIRST.test(inOrder)
}

/** A sign-off date must be a real calendar date written YYYY-MM-DD; anything else doesn't count. */
export const isIsoDate = (d: string) => {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) return false
  const t = new Date(`${d}T00:00:00Z`)
  return !Number.isNaN(t.getTime()) && t.toISOString().slice(0, 10) === d
}

export interface EditorialState {
  /** The last stage passed in order (2 = drafted only). */
  passed: Stage
  /** The next stage the item needs; null once approved. */
  next: Stage | null
  humanApproved: boolean
  /** Why the next stage isn't passed yet, or what is wrong with the record. */
  problems: string[]
}

export function editorialState(q: FixtureQuestion, rec: Ledger = EDITORIAL_LEDGER): EditorialState {
  const entry = rec.items[q.id]
  const author = entry?.author ?? AI_AUTHOR
  const hash = contentHash(q)
  const all = entry?.signoffs ?? []
  const problems: string[] = []
  for (const s of all) if (isNotAPerson(s.by)) problems.push(`stage ${s.stage}: "${s.by}" is not a named person`)
  for (const s of all) if (!isIsoDate(s.date)) problems.push(`stage ${s.stage}: date "${s.date}" is not YYYY-MM-DD and doesn't count`)
  const stale = all.filter((s) => s.hash !== hash)
  if (stale.length) problems.push(`${stale.length} sign-off(s) were for earlier content and no longer count`)
  const current = all.filter((s) => s.hash === hash && !isNotAPerson(s.by) && isIsoDate(s.date))
  const at = (st: Stage) => current.filter((s) => s.stage === st)
  const person = canonicalPerson
  const notAuthor = (s: SignOff) => person(s.by) !== person(author)

  const checks: Record<Exclude<Stage, 2>, () => string | null> = {
    3: () => {
      const s = at(3).find((x) => x.result === 'pass')
      if (!s) return 'needs a rights check'
      return s.license && ALLOWED_LICENSE.test(s.license) ? null : 'rights check has no allowed license recorded'
    },
    4: () => {
      const solves = at(4).filter(notAuthor)
      const people = new Set(solves.map((s) => person(s.by)))
      if (people.size < 2) return `needs ${2 - people.size} more blind solve(s) by someone other than the author`
      const wrong = solves.filter((s) => !q.accepted_answers.some((a) => a.trim().toLowerCase() === (s.answer ?? '').trim().toLowerCase()))
      return wrong.length ? `blind solve by ${wrong.map((s) => s.by).join(', ')} did not match the key` : null
    },
    5: () => (at(5).some((s) => s.result === 'pass') ? null : 'needs a content audit'),
    6: () => (at(6).some((s) => s.result === 'pass' && notAuthor(s)) ? null : 'needs a fairness review by someone other than the author'),
    7: () => (at(7).some((s) => s.result === 'pass') ? null : 'needs a copy edit and accessibility check'),
    8: () => (at(8).some((s) => s.result === 'pass' && notAuthor(s)) ? null : 'needs approval by a named content lead who is not the author'),
  }
  let passed: Stage = 2
  for (const st of [3, 4, 5, 6, 7, 8] as const) {
    const failed = at(st).filter((s) => s.result === 'fail')
    const why = failed.length ? `stage ${st} failed: ${failed.map((s) => s.note ?? s.by).join('; ')}` : checks[st]()
    if (why) {
      problems.push(why)
      return { passed, next: st, humanApproved: false, problems }
    }
    passed = st
  }
  return { passed, next: null, humanApproved: true, problems }
}
