import { useCallback, useEffect, useState } from 'react'
import type { PlannedExam } from '../../lib/engine/examCredit'

/**
 * The student's AP/CLEP exams (taken with a score, or planned). Kept on this device until the backend stores
 * them (contract request CR-10); nothing here is sent anywhere.
 */
const KEY = (studentId: string) => `pp-exam-plan:${studentId}`
const MAX = 20

function read(studentId: string | undefined): PlannedExam[] {
  if (!studentId) return []
  try {
    const v = JSON.parse(localStorage.getItem(KEY(studentId)) ?? '[]')
    return Array.isArray(v) ? (v as PlannedExam[]).filter((e) => e && typeof e.key === 'string').slice(0, MAX) : []
  } catch {
    return []
  }
}

export function useExamPlan(studentId: string | undefined) {
  const [exams, setExams] = useState<PlannedExam[]>(() => read(studentId))
  useEffect(() => setExams(read(studentId)), [studentId])

  const write = useCallback(
    (next: PlannedExam[]) => {
      setExams(next)
      if (!studentId) return
      try {
        localStorage.setItem(KEY(studentId), JSON.stringify(next))
      } catch {
        /* storage unavailable: keep in memory */
      }
    },
    [studentId],
  )

  return {
    exams,
    add: (e: PlannedExam) => !exams.some((x) => x.key === e.key) && exams.length < MAX && write([...exams, e]),
    setScore: (key: string, score: number | null) => write(exams.map((x) => (x.key === key ? { ...x, score } : x))),
    remove: (key: string) => write(exams.filter((x) => x.key !== key)),
    max: MAX,
  }
}
