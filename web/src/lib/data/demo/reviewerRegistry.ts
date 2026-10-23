/**
 * Authorized reviewers (docs/product/QUESTION_REVIEW_WORKFLOW.md). Identity is a stable reviewer id, never a name.
 *
 * A sign-off counts only when its `reviewer_id` is an active entry here that is authorized for that stage. A name is
 * a display field: it is never used to decide who someone is, so nobody is refused, or let through, because of what
 * their name looks like. A real reviewer named "Claude …" is entered here like anyone else.
 *
 * Names still matter in one direction only: an author may not review their own item. Authors are recorded as names
 * (the import contract's `author`, the ledger's `author`), so a reviewer whose display name or any recorded alias
 * matches an author name counts as that author. That can only block a sign-off, never allow one.
 *
 * reviewers.json ships EMPTY. Only the owner, or a content lead the owner appointed, adds a reviewer; nothing in this
 * repository appoints anyone or records an approval.
 */
import registry from './reviewers.json'
import type { Stage } from './editorialLedger'

/**
 * Canonical form of a name, used ONLY to stop an author reviewing their own item (never as identity): accents,
 * case, spacing, punctuation, invisible characters, bracketed asides and word order are ignored, so "José Writer",
 * "jose writer" and "Writer, José" match. Merging names can only block a sign-off.
 */
export const canonicalPerson = (s: string) =>
  s
    .normalize('NFKD')
    .replace(/\p{M}|\p{Cf}/gu, '')
    .replace(/ß/g, 'ss')
    .normalize('NFKC')
    .replace(/\([^)]*\)|\[[^\]]*\]/g, ' ')
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, ' ')
    .trim()
    .split(' ')
    .filter(Boolean)
    .sort()
    .join(' ')

export type ReviewRole = 'rights' | 'solver' | 'auditor' | 'fairness' | 'copyedit' | 'approver' | 'content_lead'

/** The role a sign-off at each stage needs. */
export const STAGE_ROLE: Record<Exclude<Stage, 2>, ReviewRole> = { 3: 'rights', 4: 'solver', 5: 'auditor', 6: 'fairness', 7: 'copyedit', 8: 'approver' }

export interface Reviewer {
  /** Stable and never reused: `rv-` then lowercase letters, digits or hyphens. */
  id: string
  /** Display only. */
  display_name: string
  /** Other names this person has been recorded under (display and author matching only, never identity). */
  aliases: string[]
  roles: ReviewRole[]
  /** "owner", or the id of an active reviewer with the content_lead role. */
  appointed_by: string
  appointed_on: string
  /** Set when the person may no longer review. Their sign-offs then stop counting. */
  revoked?: { on: string; by: string; reason: string }
}

export interface ReviewerRegistry {
  contract: 'reviewer_registry/v1'
  reviewers: Record<string, Reviewer>
}

export const REVIEWERS = registry as unknown as ReviewerRegistry
export const emptyReviewers = (): ReviewerRegistry => ({ contract: 'reviewer_registry/v1', reviewers: {} })

const ID = /^rv-[a-z0-9][a-z0-9-]{1,62}$/
const ROLES: ReviewRole[] = ['rights', 'solver', 'auditor', 'fairness', 'copyedit', 'approver', 'content_lead']

/** Every problem with the registry itself; an empty list means it can be used. */
export function registryProblems(reg: ReviewerRegistry): string[] {
  const out: string[] = []
  if (reg.contract !== 'reviewer_registry/v1') out.push('not a reviewer_registry/v1 file')
  for (const [key, r] of Object.entries(reg.reviewers ?? {})) {
    if (r.id !== key) out.push(`${key}: id ${r.id} doesn't match its key`)
    if (!ID.test(r.id)) out.push(`${key}: id must look like rv-<letters-digits>`)
    if (!r.display_name?.trim()) out.push(`${key}: display_name required`)
    if (!Array.isArray(r.aliases)) out.push(`${key}: aliases must be a list`)
    if (!Array.isArray(r.roles) || !r.roles.length || r.roles.some((x) => !ROLES.includes(x))) out.push(`${key}: roles must be some of ${ROLES.join(', ')}`)
    if (r.appointed_by !== 'owner') {
      const by = reg.reviewers[r.appointed_by]
      if (!by || by.revoked || !by.roles.includes('content_lead')) out.push(`${key}: appointed_by must be "owner" or an active content lead's id`)
      if (r.appointed_by === r.id) out.push(`${key}: can't appoint themselves`)
    }
    if (!r.appointed_on?.trim()) out.push(`${key}: appointed_on required`)
  }
  return out
}

/** The reviewer behind an id, if active and authorized for `role`. */
export function authorized(reg: ReviewerRegistry, id: string | undefined, role: ReviewRole): Reviewer | null {
  const r = id ? reg.reviewers[id] : undefined
  if (!r || r.revoked || !r.roles.includes(role)) return null
  // An entry appointed by a lead who is no longer valid doesn't count either.
  if (r.appointed_by !== 'owner') {
    const by = reg.reviewers[r.appointed_by]
    if (!by || by.revoked || !by.roles.includes('content_lead') || by.id === r.id) return null
  }
  return r
}

/** Every name a reviewer is known by, canonical. */
export const namesOf = (r: Reviewer) => new Set([r.display_name, ...r.aliases].map(canonicalPerson).filter(Boolean))

/**
 * Whether a reviewer is one of the authors. Authors are names (or "ai:<model>"/the AI default, which no reviewer can
 * be). Matching any recorded name of the reviewer, canonically, counts: fail-closed.
 */
export function isAuthor(r: Reviewer, authors: Iterable<string>): boolean {
  const names = namesOf(r)
  for (const a of authors) if (names.has(canonicalPerson(a))) return true
  return false
}
