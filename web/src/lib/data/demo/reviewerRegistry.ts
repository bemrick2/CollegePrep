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
  /**
   * Ids of other entries the owner has confirmed are different people despite sharing a name (two people named
   * "Maria Garcia"). Without it, entries sharing a name are treated as one person. Nobody is asked to change their name.
   */
  distinct_from?: string[]
}

export interface ReviewerRegistry {
  contract: 'reviewer_registry/v1'
  reviewers: Record<string, Reviewer>
}

export const REVIEWERS = registry as unknown as ReviewerRegistry
export const emptyReviewers = (): ReviewerRegistry => ({ contract: 'reviewer_registry/v1', reviewers: {} })

const ID = /^rv-[a-z0-9][a-z0-9-]{1,62}$/
const ROLES: ReviewRole[] = ['rights', 'solver', 'auditor', 'fairness', 'copyedit', 'approver', 'content_lead']

/**
 * Whether an entry's appointment chain reaches the owner through active content leads only, without a loop.
 * "owner" appoints; every link above an entry must be an active, distinct content lead.
 */
function chainReachesOwner(reg: ReviewerRegistry, r: Reviewer): boolean {
  const visited = new Set<string>([r.id])
  let cur = r
  while (cur.appointed_by !== 'owner') {
    const by = reg.reviewers[cur.appointed_by]
    if (!by || by.revoked || !by.roles.includes('content_lead') || visited.has(by.id)) return false
    visited.add(by.id)
    cur = by
  }
  return true
}

/**
 * Every problem with the registry itself; an empty list means it can be used. A registry with any problem is not used
 * at all: no sign-off counts against it (editorialState), so a loop, a broken chain or one person under two ids can't
 * quietly approve anything.
 */
export function registryProblems(reg: ReviewerRegistry): string[] {
  const out: string[] = []
  if (reg?.contract !== 'reviewer_registry/v1') out.push('not a reviewer_registry/v1 file')
  const entries = Object.values(reg?.reviewers ?? {})
  for (const [key, r] of Object.entries(reg?.reviewers ?? {})) {
    if (r.id !== key) out.push(`${key}: id ${r.id} doesn't match its key`)
    if (!ID.test(r.id ?? '')) out.push(`${key}: id must look like rv-<letters-digits>`)
    if (!r.display_name?.trim()) out.push(`${key}: display_name required`)
    if (!Array.isArray(r.aliases)) out.push(`${key}: aliases must be a list`)
    if (!Array.isArray(r.roles) || !r.roles.length || r.roles.some((x) => !ROLES.includes(x))) out.push(`${key}: roles must be some of ${ROLES.join(', ')}`)
    if (r.appointed_by === r.id) out.push(`${key}: can't appoint themselves`)
    else if (!r.revoked && !chainReachesOwner(reg, r)) out.push(`${key}: appointed_by must lead to "owner" through active content leads, with no loop`)
    if (!r.appointed_on?.trim()) out.push(`${key}: appointed_on required`)
    // One person, one id: a name or alias shared by two entries means one person under two ids (two "independent"
    // solvers), unless both entries declare each other distinct_from (confirmed different people with one name).
    if (Array.isArray(r.aliases))
      for (const o of entries)
        if (o.id < r.id && Array.isArray(o.aliases) && samePerson(r, o)) out.push(`${key}: shares a recorded name with ${o.id}; one person has one id (or record both in each other's distinct_from)`)
    for (const d of r.distinct_from ?? []) if (!reg.reviewers[d]) out.push(`${key}: distinct_from names unknown id ${d}`)
  }
  return out
}

/**
 * The reviewer behind an id, if active, authorized for `role`, and appointed through a chain of active content leads
 * that reaches the owner (any revoked link, broken link or loop disqualifies everyone below it).
 */
export function authorized(reg: ReviewerRegistry, id: string | undefined, role: ReviewRole): Reviewer | null {
  const r = id ? reg.reviewers[id] : undefined
  if (!r || r.revoked || !r.roles.includes(role)) return null
  return chainReachesOwner(reg, r) ? r : null
}

/**
 * A name as written, for telling people apart: accents, case, punctuation and spacing ignored, word order kept, so
 * "Li Wang" and "Wang Li" are different people while "Sam Solver" and "sam solver." are not.
 */
export const personKey = (s: string) =>
  s.normalize('NFKD').replace(/\p{M}|\p{Cf}/gu, '').replace(/ß/g, 'ss').normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ' ').trim()
const keysOf = (r: Reviewer) => new Set([r.display_name, ...(Array.isArray(r.aliases) ? r.aliases : [])].map(personKey).filter(Boolean))
const declaredDistinct = (a: Reviewer, b: Reviewer) => !!(a.distinct_from?.includes(b.id) && b.distinct_from?.includes(a.id))

/** Whether two entries are one person: the same id, or a shared recorded name not declared distinct by the owner. */
export function samePerson(a: Reviewer, b: Reviewer): boolean {
  if (a.id === b.id) return true
  if (declaredDistinct(a, b)) return false
  const names = keysOf(a)
  for (const n of keysOf(b)) if (names.has(n)) return true
  return false
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
