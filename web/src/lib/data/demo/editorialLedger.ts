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
const NOT_A_PERSON = /^(ai\b|claude|gpt|model|team|reviewer|content lead|editor|tbd|unknown)/i

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
  for (const s of all) if (NOT_A_PERSON.test(s.by.trim())) problems.push(`stage ${s.stage}: "${s.by}" is not a named person`)
  const stale = all.filter((s) => s.hash !== hash)
  if (stale.length) problems.push(`${stale.length} sign-off(s) were for earlier content and no longer count`)
  const current = all.filter((s) => s.hash === hash && !NOT_A_PERSON.test(s.by.trim()))
  const at = (st: Stage) => current.filter((s) => s.stage === st)
  const person = (s: string) => s.trim().toLowerCase()
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
