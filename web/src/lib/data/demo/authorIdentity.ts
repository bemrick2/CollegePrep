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
import { authorized, canonicalPerson, REVIEWERS, type ReviewerRegistry } from './reviewerRegistry'

export interface Identity {
  /** Stable and never reused: `au-` then lowercase letters, digits or hyphens. */
  id: string
  display_name: string
  /** Other names this person writes under (display and fail-closed matching only). */
  aliases: string[]
  /** Their reviewer id, when this person is also in the reviewer registry. */
  reviewer_id?: string
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

const ID = /^au-[a-z0-9][a-z0-9-]{1,62}$/
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
    if (!x.recorded_on?.trim()) out.push(`${key}: recorded_on required`)
    if (x.recorded_by !== 'owner' && !authorized(reviewers, x.recorded_by, 'content_lead')) out.push(`${key}: recorded_by must be "owner" or an active content lead's reviewer id`)
    if (x.reviewer_id !== undefined) {
      if (!reviewers.reviewers[x.reviewer_id]) out.push(`${key}: reviewer_id ${x.reviewer_id} is not in the reviewer registry`)
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
      const x = usable ? reg.identities[id.identity_id] : undefined
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
