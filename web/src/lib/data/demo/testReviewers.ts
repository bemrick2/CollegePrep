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
