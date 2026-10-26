/**
 * TEST ONLY: NOT A QUESTION BANK, AND NOT THE ORIGINAL, B OR C BANKS (#254).
 *
 * A stand-in import batch for unit tests of intake, review packets and sign-off recording. Each line is an existing
 * app fixture question re-dressed in the import contract's fields; no new question is written here. Ids start with
 * "test-only-". Passing tests on this batch says nothing about the real banks, which have not been delivered.
 */
import { QUESTIONS } from '../data/demo/fixtures'
import { IMPORT_CONTRACT_V2, type ImportedQuestion } from '../questionImport'

export function testOnlyBatch(n = 4, extra: (i: number) => Partial<ImportedQuestion> = () => ({})): ImportedQuestion[] {
  return QUESTIONS.slice(0, n).map((q, i) => {
    const { id, ...content } = q
    return {
      ...content,
      contract: IMPORT_CONTRACT_V2,
      import_id: `test-only-${id}`,
      origin: 'human_original',
      author: 'Jo Writer',
      // TEST ONLY identity (testIdentities in testReviewers.ts); the real identities.json is empty.
      author_identity: { kind: 'person', identity_id: 'au-test-jo-writer' },
      license: 'original-owned',
      source_attribution: null,
      source_url: null,
      requested_pool: i % 2 ? 'assessment' : 'practice',
      ...extra(i),
    }
  })
}
