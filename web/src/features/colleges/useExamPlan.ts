import { useCallback, useEffect, useState } from 'react'
import { useApp } from '../../lib/app'
import type { IbLevel, PlannedExam } from '../../lib/engine/examCredit'

/**
 * The student's credit exams (AP, CLEP, IB, Statewide Dual Credit), taken with a score or planned.
 *
 * Where the backend has CR-10 (`source.supportsExamPlan`), AP and CLEP exams with a canonical key live on the
 * account, so they follow the family to every device; everything else (IB, Statewide Dual Credit, a name the catalog
 * doesn't have) stays on this device. Otherwise the whole plan stays on this device, as before. `onDevice` says which
 * entries would not follow the family to another device.
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
function writeLocal(studentId: string | undefined, exams: PlannedExam[]) {
  if (!studentId) return
  try {
    localStorage.setItem(KEY(studentId), JSON.stringify(exams))
  } catch {
    /* storage unavailable: keep in memory */
  }
}

export function useExamPlan(studentId: string | undefined) {
  const { source } = useApp()
  const onAccount = source.supportsExamPlan
  const [local, setLocal] = useState<PlannedExam[]>(() => read(studentId))
  const [remote, setRemote] = useState<PlannedExam[]>([])
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    setLocal(read(studentId))
    setRemote([])
    if (!onAccount || !studentId) return
    let live = true
    source.examPlan(studentId).then(
      (r) => live && setRemote(r),
      (e: Error) => live && setError(e.message),
    )
    return () => {
      live = false
    }
  }, [studentId, onAccount, source])

  const remoteKeys = new Set(remote.map((e) => e.key))
  // An exam saved to the account and also left on this device from before is shown once, from the account.
  const exams = [...remote, ...local.filter((e) => !remoteKeys.has(e.key))].slice(0, MAX)
  const setLocalAndStore = useCallback(
    (next: PlannedExam[]) => {
      setLocal(next)
      writeLocal(studentId, next)
    },
    [studentId],
  )

  const save = async (e: PlannedExam) => {
    setError(null)
    if (onAccount && studentId) {
      try {
        await source.saveExamPlanEntry(studentId, e)
        setRemote((r) => [...r.filter((x) => x.key !== e.key), e])
        // Moved to the account: drop any device copy.
        if (local.some((x) => x.key === e.key)) setLocalAndStore(local.filter((x) => x.key !== e.key))
        return
      } catch (err) {
        if ((err as { code?: string }).code !== 'invalid') {
          setError((err as Error).message)
          return
        }
      }
    }
    setLocalAndStore(local.some((x) => x.key === e.key) ? local.map((x) => (x.key === e.key ? e : x)) : [...local, e])
  }

  return {
    exams,
    /** Keys kept on this device only (not on the account). */
    onDevice: new Set(local.filter((e) => !remoteKeys.has(e.key)).map((e) => e.key)),
    onAccount,
    error,
    add: (e: PlannedExam) => {
      if (exams.some((x) => x.key === e.key) || exams.length >= MAX) return false
      void save(e)
      return true
    },
    setScore: (key: string, score: number | null) => {
      const e = exams.find((x) => x.key === key)
      if (e) void save({ ...e, score })
    },
    setLevel: (key: string, level: IbLevel | null) => {
      const e = exams.find((x) => x.key === key)
      if (e) void save({ ...e, level })
    },
    remove: (key: string) => {
      if (remoteKeys.has(key) && studentId)
        void source.removeExamPlanEntry(studentId, key).then(
          () => setRemote((r) => r.filter((x) => x.key !== key)),
          (err: Error) => setError(err.message),
        )
      if (local.some((x) => x.key === key)) setLocalAndStore(local.filter((x) => x.key !== key))
    },
    max: MAX,
  }
}
