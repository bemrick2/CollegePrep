import { useApp, useAsync } from '../../lib/app'
import { referenceScore, type ReferenceScore } from '../../lib/engine/merit'

/** The exam and the score merit criteria may be compared with for a student: official, self-reported (labelled)
 *  or target. Never a practice estimate. */
export function useMeritReference(studentId: string | null | undefined): { exam: 'act' | 'sat'; reference: ReferenceScore | null; goals: string[] } {
  const { source } = useApp()
  const facts = useAsync(async () => (studentId ? Promise.all([source.getPlan(studentId), source.testScores(studentId)]) : null), [source, studentId])
  const exam = facts.data?.[0]?.exam_family ?? 'act'
  return {
    exam,
    reference: facts.data ? referenceScore(facts.data[1], exam, facts.data[0]?.target_score ?? null) : null,
    goals: facts.data?.[0]?.goals ?? [],
  }
}
