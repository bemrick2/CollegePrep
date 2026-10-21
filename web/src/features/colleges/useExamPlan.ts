import { useCallback, useEffect, useRef, useState } from 'react'
import { useApp } from '../../lib/app'
import type { IbLevel, PlannedExam } from '../../lib/engine/examCredit'

/**
 * The student's credit exams (AP, CLEP, IB, Statewide Dual Credit), taken with a score or planned.
 *
 * Where the backend has CR-10 (`source.supportsExamPlan`), AP and CLEP exams whose printed name is in the canonical
 * catalog live on the account, so they follow the family to every device. Everything else (IB, Statewide Dual
 * Credit, a name the catalog doesn't list) stays on this device, and `onDevice` names those entries so the screen can
 * say so. Device entries that can move are moved once the account plan has loaded (when this viewer may edit).
 * Without CR-10 the whole plan stays on this device, as before.
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
const noKey = (e: unknown) => (e as { code?: string }).code === 'not_found'

/** `canEdit`: whether this viewer may change the plan (the linked student, or a guardian who can set goals). */
export function useExamPlan(studentId: string | undefined, canEdit = true) {
  const { source } = useApp()
  const onAccount = source.supportsExamPlan
  const [local, setLocalState] = useState<PlannedExam[]>(() => read(studentId))
  const [remote, setRemote] = useState<PlannedExam[]>([])
  const [ready, setReady] = useState(!onAccount)
  const [error, setError] = useState<string | null>(null)
  const sid = useRef(studentId)
  sid.current = studentId

  // Always from the latest list, and stored from that same list: an await in between can't bring back a stale copy.
  const updateLocal = useCallback((f: (prev: PlannedExam[]) => PlannedExam[]) => {
    setLocalState((prev) => {
      const next = f(prev)
      writeLocal(sid.current, next)
      return next
    })
  }, [])

  const saveToAccount = useCallback(
    async (e: PlannedExam): Promise<'account' | 'device' | 'error'> => {
      if (!onAccount || !studentId) return 'device'
      // A save that finishes after the screen switched to another student must not touch that student's lists.
      const stillHere = () => sid.current === studentId
      try {
        await source.saveExamPlanEntry(studentId, e)
        if (!stillHere()) return 'error'
        setRemote((r) => [...r.filter((x) => x.key !== e.key), e])
        updateLocal((prev) => prev.filter((x) => x.key !== e.key))
        return 'account'
      } catch (err) {
        if (!stillHere()) return 'error'
        if (noKey(err)) return 'device'
        setError((err as Error).message)
        return 'error'
      }
    },
    [onAccount, studentId, source, updateLocal],
  )

  useEffect(() => {
    setLocalState(read(studentId))
    setRemote([])
    setError(null)
    setReady(!onAccount)
    if (!onAccount || !studentId) return
    let live = true
    source.examPlan(studentId).then(
      async (r) => {
        if (!live) return
        setRemote(r)
        // Move device entries the account can hold BEFORE enabling edits, so an edit can't race the move.
        if (canEdit) {
          const acc = new Map(r.map((x) => [x.key, x]))
          for (const e of read(studentId)) {
            if (!live) return
            const there = acc.get(e.key)
            // The account's entry wins, unless it's only "planned" and this device has a score.
            if (there && !(there.score == null && e.score != null)) updateLocal((prev) => prev.filter((x) => x.key !== e.key))
            else await saveToAccount(e)
          }
        }
        if (live) setReady(true)
      },
      // Without the account plan nothing can be edited safely (a save could overwrite a score we couldn't read).
      (e: Error) => live && setError(e.message),
    )
    return () => {
      live = false
    }
    // saveToAccount is stable for a given student and source.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [studentId, onAccount, source, canEdit])

  const remoteKeys = new Set(remote.map((e) => e.key))
  // An exam on the account and also on this device is shown once, from the account.
  const exams = [...remote, ...local.filter((e) => !remoteKeys.has(e.key))].slice(0, MAX)

  const save = async (e: PlannedExam) => {
    setError(null)
    if ((await saveToAccount(e)) !== 'device') return
    updateLocal((prev) => (prev.some((x) => x.key === e.key) ? prev.map((x) => (x.key === e.key ? e : x)) : [...prev, e]))
  }

  return {
    exams,
    /** Keys kept on this device only (not on the account). */
    onDevice: new Set(local.filter((e) => !remoteKeys.has(e.key)).map((e) => e.key)),
    onAccount,
    /** False until the account plan has loaded: adding before then could overwrite a saved score. */
    ready,
    canEdit,
    error,
    add: (e: PlannedExam) => {
      if (!ready || !canEdit || exams.some((x) => x.key === e.key) || exams.length >= MAX) return false
      void save(e)
      return true
    },
    setScore: (key: string, score: number | null) => {
      const e = exams.find((x) => x.key === key)
      if (e && ready && canEdit) void save({ ...e, score })
    },
    setLevel: (key: string, level: IbLevel | null) => {
      const e = exams.find((x) => x.key === key)
      if (e && ready && canEdit) void save({ ...e, level })
    },
    remove: (key: string) => {
      if (!canEdit || !ready) return
      setError(null)
      if (remoteKeys.has(key) && studentId)
        void source.removeExamPlanEntry(studentId, key).then(
          () => sid.current === studentId && setRemote((r) => r.filter((x) => x.key !== key)),
          (err: Error) => sid.current === studentId && setError(err.message),
        )
      updateLocal((prev) => prev.filter((x) => x.key !== key))
    },
    max: MAX,
  }
}
