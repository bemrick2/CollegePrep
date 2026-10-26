import type { FixtureQuestion } from './fixtures'
import { contentHash } from './questionReview'
import ledger from './editorialLedger.json'
import { authorized, canonicalPerson, isAuthor, registryProblems, REVIEWERS, samePerson, STAGE_ROLE, type Reviewer, type ReviewerRegistry } from './reviewerRegistry'
import { IDENTITIES, resolveAuthors, type AuthorIdentity, type IdentityRegistry } from './authorIdentity'

export { canonicalPerson }

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
  /** The signer's stable id in the reviewer registry (reviewerRegistry.ts). This, not the name, is who signed. */
  reviewer_id: string
  /** The name as written on the sheet. Display only. */
  by: string
  date: string
  result: 'pass' | 'fail'
  /** contentHash(q) when signed. */
  hash: string
  /**
   * Stage 3, imported items: the rights version signed (questionCandidates rights_hash: the content plus author,
   * origin, license and source). A rights or author change makes a new rights_hash, so an earlier rights check stops
   * counting and a re-check of the new version counts at once, the same day or any day.
   */
  rights_hash?: string
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
  /** Every author ever recorded for the item, append-only. Each stays excluded from stages 4, 6 and 8. */
  authors?: string[]
  /**
   * The identity behind each recorded author name (import contract v2 / stage 2 with an identity). A human name with
   * no record here is unresolved: the item is never human-approved while any author is unresolved.
   */
  author_records?: { name: string; identity: AuthorIdentity }[]
  signoffs: SignOff[]
}

export interface Ledger {
  items: Record<string, LedgerEntry>
}

export const EDITORIAL_LEDGER = ledger as unknown as Ledger
export const AI_AUTHOR = 'AI (Claude)'
const ALLOWED_LICENSE = /^(original|public domain|federal|cc by(-sa)? \d)/i

/** A sign-off date must be a real calendar date written YYYY-MM-DD. Dates are a record, never an ordering rule. */
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

export interface EditorialOptions {
  reviewers?: ReviewerRegistry
  /** Every author name of the item (all versions). Default: the ledger entry's author, else the AI default. */
  authors?: string[]
  /** When set, a rights check counts only if it signed exactly this rights version. */
  rightsHash?: string
  /**
   * Rights versions making the same claims as the current one (same content, author, origin, license and source).
   * A stage-3 fail recorded against any of them keeps blocking: a resubmission that changes nothing about the claims
   * never clears a rights fail.
   */
  sameClaims?: string[]
  /** Today (YYYY-MM-DD). A pass dated after tomorrow doesn't count. Default: the current date. */
  today?: string
  /**
   * Imported items: their authors' resolution, worked out from the import (every version). When given, it replaces the
   * ledger-based resolution used for the app's bank.
   */
  authorship?: { resolved: boolean; unresolved: string[]; reviewerIds: string[]; names: string[] }
  identities?: IdentityRegistry
}

/**
 * The app bank's authors, resolved from the ledger. Stage 2 records an author under its identity key ("au-…" or
 * "ai:<model>") in `authors`, with a matching entry in `author_records`. Only those keys resolve, and only when the
 * record agrees with its key. "AI (Claude)" (the bank's recorded AI drafting) is explicit AI authorship. Any other name
 * is a legacy name: it stays unresolved, whatever identity happens to share its display name.
 */
export function ledgerAuthorship(entry: LedgerEntry | undefined, identities: IdentityRegistry = IDENTITIES, reviewers: ReviewerRegistry = REVIEWERS) {
  const records = entry?.author_records ?? []
  const keyOf = (i: AuthorIdentity | null | undefined) => (i?.kind === 'ai' ? `ai:${i.model}` : i?.kind === 'person' ? i.identity_id : null)
  const identityFor = (name: string): AuthorIdentity | null => {
    if (/^(au-|ai:)/.test(name)) return records.find((r) => r.name === name && keyOf(r.identity) === name)?.identity ?? null
    return name === AI_AUTHOR ? { kind: 'ai', model: 'claude' } : null
  }
  return resolveAuthors(
    ledgerAuthors(entry).map((name) => ({ name, identity: identityFor(name) })),
    identities,
    reviewers,
  )
}

/** Every author name recorded for an item in the ledger: the current one and every earlier one. */
export const ledgerAuthors = (entry: LedgerEntry | undefined) => [...new Set([...(entry?.authors ?? []), entry?.author ?? AI_AUTHOR])]

export function editorialState(q: FixtureQuestion, rec: Ledger = EDITORIAL_LEDGER, opts: EditorialOptions = {}): EditorialState {
  const reviewers = opts.reviewers ?? REVIEWERS
  const entry = rec.items[q.id]
  const authorship = opts.authorship ?? ledgerAuthorship(entry, opts.identities ?? IDENTITIES, reviewers)
  const authors = [...new Set([...(opts.authors ?? []), ...ledgerAuthors(entry), ...authorship.names])]
  const authorIds = new Set(authorship.reviewerIds)
  const hash = contentHash(q)
  const all = entry?.signoffs ?? []
  const problems: string[] = []
  const stale = all.filter((s) => s.hash !== hash)
  if (stale.length) problems.push(`${stale.length} sign-off(s) were for earlier content and no longer count`)
  // A registry with any problem (a loop, a broken chain, one person under two ids) is not used: no pass counts.
  const registryOk = registryProblems(reviewers).length === 0
  if (!registryOk) problems.push('the reviewer registry has problems (see registryProblems); no sign-off counts until it is fixed')
  const today = opts.today ?? new Date().toISOString().slice(0, 10)
  const tomorrow = new Date(Date.parse(`${today}T00:00:00Z`) + 86400000).toISOString().slice(0, 10)
  for (const s of all) if (s.hash === hash && !isIsoDate(s.date)) problems.push(`stage ${s.stage}: date "${s.date}" is not YYYY-MM-DD; a pass with it doesn't count`)
  for (const s of all) if (s.hash === hash && isIsoDate(s.date) && s.date > tomorrow) problems.push(`stage ${s.stage}: dated ${s.date}, in the future; a pass with it doesn't count`)

  // A pass counts only from an active reviewer authorized for that stage, with a valid date that isn't in the future.
  // A recorded FAIL on this content always blocks, whoever recorded it and whatever its date: fail-closed until the
  // item is revised. (Stage 3 of an imported item: a fail for a different rights version doesn't block this one.)
  const current = all.filter((s) => s.hash === hash)
  const signer = (s: SignOff): Reviewer | null => (s.stage === 2 || !registryOk ? null : authorized(reviewers, s.reviewer_id, STAGE_ROLE[s.stage as Exclude<Stage, 2>]))
  for (const s of current)
    if (s.result === 'pass' && s.stage !== 2 && registryOk && !signer(s))
      problems.push(`stage ${s.stage}: ${s.reviewer_id ? `reviewer ${s.reviewer_id}` : `"${s.by}" (no reviewer id)`} is not an active reviewer authorized for ${STAGE_ROLE[s.stage as Exclude<Stage, 2>]}; it doesn't count`)
  const passes = (st: Stage) => current.filter((s) => s.stage === st && s.result === 'pass' && isIsoDate(s.date) && s.date <= tomorrow && signer(s))
  // An author is excluded by id (an identity linked to their reviewer id) and, fail-closed, by any recorded name.
  const notAuthor = (s: SignOff) => !authorIds.has(signer(s)!.id) && !isAuthor(signer(s)!, authors)

  const checks: Record<Exclude<Stage, 2>, () => string | null> = {
    3: () => {
      const ok = passes(3).filter((x) => opts.rightsHash === undefined || x.rights_hash === opts.rightsHash)
      if (!ok.length) return passes(3).length ? 'rights check was for an earlier rights version (author, origin, license or source changed); check the current one' : 'needs a rights check'
      return ok.some((x) => x.license && ALLOWED_LICENSE.test(x.license)) ? null : 'rights check has no allowed license recorded'
    },
    4: () => {
      const solves = passes(4).filter(notAuthor)
      // Distinct people, not distinct ids: entries sharing any recorded name count as one person.
      const people: Reviewer[] = []
      for (const s of solves) {
        const r = signer(s)!
        if (!people.some((p) => samePerson(p, r))) people.push(r)
      }
      if (people.length < 2) return `needs ${2 - people.length} more blind solve(s) by an authorized solver other than the author`
      const wrong = solves.filter((s) => !q.accepted_answers.some((a) => a.trim().toLowerCase() === (s.answer ?? '').trim().toLowerCase()))
      return wrong.length ? `blind solve by ${wrong.map((s) => s.reviewer_id).join(', ')} did not match the key` : null
    },
    5: () => (passes(5).length ? null : 'needs a content audit by an authorized auditor'),
    6: () => (passes(6).some(notAuthor) ? null : 'needs a fairness review by an authorized reviewer other than the author'),
    7: () => (passes(7).length ? null : 'needs a copy edit and accessibility check by an authorized editor'),
    8: () => (passes(8).some(notAuthor) ? null : 'needs approval by an authorized approver who is not the author'),
  }
  let passed: Stage = 2
  for (const st of [3, 4, 5, 6, 7, 8] as const) {
    const failed = current.filter((s) => s.stage === st && s.result === 'fail' && (st !== 3 || opts.rightsHash === undefined || !s.rights_hash || s.rights_hash === opts.rightsHash || (opts.sameClaims ?? []).includes(s.rights_hash)))
    const why = failed.length ? `stage ${st} failed: ${failed.map((s) => s.note ?? s.reviewer_id ?? s.by).join('; ')}` : checks[st]()
    if (why) {
      problems.push(why)
      return { passed, next: st, humanApproved: false, problems }
    }
    passed = st
  }
  // Every stage passed, but approval also needs every author resolved (an AI model or a recorded identity).
  if (!authorship.resolved) {
    problems.push(...authorship.unresolved, 'not approved until every author has a recorded identity (next: 2 means authorship)')
    return { passed, next: 2, humanApproved: false, problems }
  }
  return { passed, next: null, humanApproved: true, problems }
}
