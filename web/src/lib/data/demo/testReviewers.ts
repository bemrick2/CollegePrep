/**
 * TEST ONLY. Fictional reviewers for unit tests of the editorial ledger and candidate registry. These people don't
 * exist, nobody is appointed by this file, and it is never read by the app or by any script that records sign-offs:
 * the real registry is reviewers.json, which ships empty.
 */
import type { Reviewer, ReviewerRegistry, ReviewRole } from './reviewerRegistry'

const ALL: ReviewRole[] = ['rights', 'solver', 'auditor', 'fairness', 'copyedit', 'approver', 'content_lead']

/** Display name → roles. Ids are derived: rv-test-<slug>. */
const PEOPLE: [string, ReviewRole[], string[]?][] = [
  ['Lee Rights', ['rights']],
  ['Sam Solver', ['solver', 'auditor']],
  ['Ana Solver', ['solver']],
  ['Kim Fair', ['fairness']],
  ['Ed Copy', ['copyedit']],
  ['Pat Lead', ['approver', 'content_lead']],
  ['Jo Writer', ALL, ['J. Writer', 'Jojo Writer']],
  ['José Writer', ALL],
  ['Dana Author', ALL],
  // Real people can have any name: this one is a person like any other.
  ['Claude Debussy', ['solver', 'approver', 'content_lead']],
  ['Ai Nguyen', ['solver']],
]

export const testId = (name: string) => `rv-test-${name.normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')}`

export function testReviewers(extra: Partial<Record<string, Partial<Reviewer>>> = {}): ReviewerRegistry {
  const reviewers: Record<string, Reviewer> = {}
  for (const [name, roles, aliases] of PEOPLE) {
    const id = testId(name)
    reviewers[id] = { id, display_name: name, aliases: aliases ?? [], roles, appointed_by: 'owner', appointed_on: '2026-10-23', ...(extra[id] ?? {}) }
  }
  return { contract: 'reviewer_registry/v1', reviewers }
}

// ---------------------------------------------------------------------------------------------------------------------
// TEST ONLY: fictional author identities (question_import/v2). Nobody's identity is recorded by this file; the real
// registry is identities.json, which ships empty.

import type { Identity, IdentityRegistry } from './authorIdentity'

/** Authors who are not reviewers in the test registry. */
const AUTHOR_ONLY = ['Ed Editor', 'Someone Else']

export const testIdentityId = (name: string) => `au-test-${testId(name).slice('rv-test-'.length)}`

/** Every test person gets an identity linked to their test reviewer id; author-only people get one with no link. */
export function testIdentities(extra: Record<string, Partial<Identity>> = {}): IdentityRegistry {
  const identities: Record<string, Identity> = {}
  for (const [name] of PEOPLE) {
    const id = testIdentityId(name)
    identities[id] = { id, display_name: name, aliases: [], reviewer_id: testId(name), recorded_by: 'owner', recorded_on: '2026-10-26', ...(extra[id] ?? {}) }
  }
  for (const name of AUTHOR_ONLY) {
    const id = testIdentityId(name)
    identities[id] = { id, display_name: name, aliases: [], recorded_by: 'owner', recorded_on: '2026-10-26', ...(extra[id] ?? {}) }
  }
  for (const [id, x] of Object.entries(extra)) if (!identities[id]) identities[id] = { id, display_name: id, aliases: [], recorded_by: 'owner', recorded_on: '2026-10-26', ...x } as Identity
  return { contract: 'author_identity_registry/v1', identities }
}
