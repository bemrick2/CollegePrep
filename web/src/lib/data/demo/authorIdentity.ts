/**
 * Author identities (question_import/v2; docs/product/QUESTION_IMPORT_CONTRACT.md).
 *
 * An author is either an AI model, recorded explicitly, or a person with a stable identity id (`au-…`) in
 * identities.json. When the same person is also a reviewer, the identity carries their reviewer id, so author/reviewer
 * separation is decided by id, not by how a name is spelled. Names stay display fields.
 *
 * identities.json ships EMPTY. Only the owner, or an active content lead, records a person's identity, and nothing in
 * this repository creates one. An author known only by a name (a question_import/v1 line, or a name in the ledger)
 * is UNRESOLVED: it is never treated as a verified identity, and an item with any unresolved author is never eligible.
 */
import registry from './identities.json'
import { authorized, canonicalPerson, isAuthor, REVIEWERS, type ReviewerRegistry } from './reviewerRegistry'

export interface Identity {
  /** Stable and never reused: `au-` then lowercase letters, digits or hyphens. */
  id: string
  display_name: string
  /** Other names this person writes under (display and fail-closed matching only). */
  aliases: string[]
  /** Their reviewer id, when this person is also in the reviewer registry. */
  reviewer_id?: string
  /**
   * Reviewer ids of different people whose recorded names match this identity's. Without it, a reviewer whose names
   * match this identity but who isn't its linked reviewer is a problem (a link is probably missing or wrong).
   */
  distinct_from?: string[]
  /** "owner", or an active content lead's reviewer id. */
  recorded_by: string
  recorded_on: string
}

export interface IdentityRegistry {
  contract: 'author_identity_registry/v1'
  identities: Record<string, Identity>
}

export const IDENTITIES = registry as unknown as IdentityRegistry
export const emptyIdentities = (): IdentityRegistry => ({ contract: 'author_identity_registry/v1', identities: {} })

/** How a line or ledger entry names its author. */
export type AuthorIdentity = { kind: 'ai'; model: string } | { kind: 'person'; identity_id: string }

export const IDENTITY_ID = /^au-[a-z0-9][a-z0-9-]{1,62}$/
const ID = IDENTITY_ID
/** The bank's recorded AI drafting name; a person's identity may not use it. */
const AI_NAME = 'AI (Claude)'

/** The recorded identity with this id, if any (own keys only: never "constructor" or another built-in). */
export const identityOf = (reg: IdentityRegistry, id: unknown): Identity | undefined =>
  typeof id === 'string' && ID.test(id) && Object.hasOwn(reg?.identities ?? {}, id) ? reg.identities[id] : undefined
export const AI_MODEL = /^[A-Za-z0-9][A-Za-z0-9._:/-]{1,80}$/

/** Every problem with the identity registry; an empty list means it can be used. */
export function identityProblems(reg: IdentityRegistry, reviewers: ReviewerRegistry = REVIEWERS): string[] {
  const out: string[] = []
  if (reg?.contract !== 'author_identity_registry/v1') out.push('not an author_identity_registry/v1 file')
  const linked = new Map<string, string>()
  for (const [key, x] of Object.entries(reg?.identities ?? {})) {
    if (x.id !== key) out.push(`${key}: id ${x.id} doesn't match its key`)
    if (!ID.test(x.id ?? '')) out.push(`${key}: id must look like au-<letters-digits>`)
    if (!x.display_name?.trim()) out.push(`${key}: display_name required`)
    if (!Array.isArray(x.aliases)) out.push(`${key}: aliases must be a list`)
    const names = [x.display_name ?? '', ...(Array.isArray(x.aliases) ? x.aliases : [])]
    if (names.some((n) => canonicalPerson(n) && canonicalPerson(n) === canonicalPerson(AI_NAME))) out.push(`${key}: "${AI_NAME}" is the bank's AI drafting name, not a person's`)
    if (x.distinct_from !== undefined && !Array.isArray(x.distinct_from)) out.push(`${key}: distinct_from must be a list of reviewer ids`)
    for (const d of Array.isArray(x.distinct_from) ? x.distinct_from : []) {
      if (typeof d !== 'string' || !Object.hasOwn(reviewers?.reviewers ?? {}, d)) out.push(`${key}: distinct_from ${String(d)} is not a reviewer id in the registry`)
      else if (d === x.reviewer_id) out.push(`${key}: ${d} is this identity's own reviewer, not a different person`)
    }
    for (const rv of Object.values(reviewers?.reviewers ?? {}))
      if (!rv.revoked && rv.id !== x.reviewer_id && !(x.distinct_from ?? []).includes(rv.id) && isAuthor(rv, names.filter(Boolean)))
        out.push(`${key}: reviewer ${rv.id} has a name matching this identity but isn't linked to it; link it (reviewer_id), or record them as different people (distinct_from)`)
    if (!x.recorded_on?.trim()) out.push(`${key}: recorded_on required`)
    if (x.recorded_by !== 'owner' && !authorized(reviewers, x.recorded_by, 'content_lead')) out.push(`${key}: recorded_by must be "owner" or an active content lead's reviewer id`)
    if (x.reviewer_id !== undefined) {
      if (!Object.hasOwn(reviewers?.reviewers ?? {}, x.reviewer_id)) out.push(`${key}: reviewer_id ${x.reviewer_id} is not in the reviewer registry`)
      const other = linked.get(x.reviewer_id)
      if (other) out.push(`${key}: reviewer ${x.reviewer_id} is already linked to ${other}; one reviewer, one identity`)
      linked.set(x.reviewer_id, key)
    }
  }
  return out
}

export interface ResolvedAuthors {
  /** Every author is either an explicit AI model or a recorded identity. */
  resolved: boolean
  /** Why not, one line per unresolved author. */
  unresolved: string[]
  /** Reviewer ids of authors who are also reviewers: excluded from stages 4, 6 and 8 by id. */
  reviewerIds: string[]
  /** Every name the authors are known by (display, aliases, and the names as written), for fail-closed matching. */
  names: string[]
}

/**
 * Resolves the authors of an item. `declared`: each author as recorded, with its identity if one was given. An identity
 * that isn't in the registry is unresolved; so is a bare human name. AI authorship is resolved when it names its model.
 */
export function resolveAuthors(declared: { name: string; identity?: AuthorIdentity | null }[], reg: IdentityRegistry = IDENTITIES, reviewers: ReviewerRegistry = REVIEWERS): ResolvedAuthors {
  const out: ResolvedAuthors = { resolved: true, unresolved: [], reviewerIds: [], names: [] }
  const usable = identityProblems(reg, reviewers).length === 0
  for (const d of declared) {
    out.names.push(d.name)
    const id = d.identity
    if (id?.kind === 'ai') {
      if (!AI_MODEL.test(id.model ?? '')) out.unresolved.push(`author "${d.name}": an AI author must name its model`)
      continue
    }
    if (id?.kind === 'person') {
      const x = usable ? identityOf(reg, id.identity_id) : undefined
      if (!x) {
        out.unresolved.push(`author "${d.name}": identity ${id.identity_id} is not recorded${usable ? '' : ' (the identity registry has problems)'}`)
        continue
      }
      out.names.push(x.display_name, ...x.aliases)
      if (x.reviewer_id) out.reviewerIds.push(x.reviewer_id)
      continue
    }
    out.unresolved.push(`author "${d.name}" is a name only, with no recorded identity; a legacy name is never a verified identity`)
  }
  out.resolved = out.unresolved.length === 0
  out.names = [...new Set(out.names.filter((n) => canonicalPerson(n)))]
  out.reviewerIds = [...new Set(out.reviewerIds)]
  return out
}
