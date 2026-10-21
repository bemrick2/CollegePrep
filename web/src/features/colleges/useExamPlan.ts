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

// If the browser can't store (private mode, full storage), the plan still lives for this page session, per student:
// once a write fails for a student, that student's list is read from memory from then on.
const memory = new Map<string, PlannedExam[]>()

function read(studentId: string | undefined): PlannedExam[] {
  if (!studentId) return []
  if (memory.has(studentId)) return memory.get(studentId)!
  try {
    const raw = localStorage.getItem(KEY(studentId))
    if (raw == null) return []
    const v = JSON.parse(raw)
    return Array.isArray(v) ? (v as PlannedExam[]).filter((e) => e && typeof e.key === 'string').slice(0, MAX) : []
  } catch {
    return []
  }
}
function writeLocal(studentId: string | undefined, exams: PlannedExam[]) {
  if (!studentId) return
  if (memory.has(studentId)) {
    memory.set(studentId, exams)
    return
  }
  try {
    localStorage.setItem(KEY(studentId), JSON.stringify(exams))
  } catch {
    memory.set(studentId, exams) // storage unavailable: kept for this page session
  }
}
/** Tests only: forget the in-memory fallback. */
export function resetExamPlanMemory() {
  memory.clear()
}
const noKey = (e: unknown) => (e as { code?: string }).code === 'not_found'

/** `canEdit`: whether this viewer may change the plan (the linked student, or a guardian who can set goals). */
export function useExamPlan(studentId: string | undefined, canEdit = true) {
  const { source } = useApp()
  const onAccount = source.supportsExamPlan
  const [local, setLocalState] = useState<PlannedExam[]>(() => read(studentId))
  // Which student `local` and `remote` belong to: until the effect has loaded the new student, nothing is shown or
  // editable, so a stale list from the previous student can't be acted on.
  const [loadedFor, setLoadedFor] = useState(studentId)
  const [remote, setRemote] = useState<PlannedExam[]>([])
  const [ready, setReady] = useState(!onAccount)
  const [error, setError] = useState<string | null>(null)
  const sid = useRef(studentId)
  sid.current = studentId

  /**
   * Changes one student's device list. Every write names the student it belongs to (the one the action started
   * for), reads that student's latest stored list, and stores the result there; the screen is updated only if that
   * student is still the one shown. A save that settles after a student switch can never land on the other student.
   */
  const updateLocal = useCallback((target: string | undefined, f: (prev: PlannedExam[]) => PlannedExam[]) => {
    if (!target) return
    const next = f(read(target))
    writeLocal(target, next)
    if (sid.current === target) setLocalState(next)
  }, [])

  const saveToAccount = useCallback(
    async (e: PlannedExam): Promise<'account' | 'device' | 'error'> => {
      if (!onAccount || !studentId) return 'device'
      // A save that finishes after the screen switched to another student must not touch that student's lists.
      const stillHere = () => sid.current === studentId
      try {
        await source.saveExamPlanEntry(studentId, e)
        // Saved to this student's account: drop this student's device copy, whoever is on screen now.
        updateLocal(studentId, (prev) => prev.filter((x) => x.key !== e.key))
        if (stillHere()) setRemote((r) => [...r.filter((x) => x.key !== e.key), e])
        return 'account'
      } catch (err) {
        if (noKey(err)) return 'device'
        // Still on screen: say so (the 20-exam limit, a network error). Switched away: keep the answer on this
        // student's device, so it isn't lost; it moves to the account on their next load.
        if (!stillHere()) return 'device'
        setError((err as Error).message)
        return 'error'
      }
    },
    [onAccount, studentId, source, updateLocal],
  )

  useEffect(() => {
    setLocalState(read(studentId))
    setLoadedFor(studentId)
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
            if (there && !(there.score == null && e.score != null)) updateLocal(studentId, (prev) => prev.filter((x) => x.key !== e.key))
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

  const current = loadedFor === studentId
  const remoteKeys = new Set(remote.map((e) => e.key))
  // An exam on the account and also on this device is shown once, from the account.
  const exams = current ? [...remote, ...local.filter((e) => !remoteKeys.has(e.key))].slice(0, MAX) : []
  const editable = current && ready && canEdit

  const save = async (e: PlannedExam) => {
    // Bound now: the student this answer is for, even if the screen switches while it saves.
    const target = studentId
    setError(null)
    if ((await saveToAccount(e)) !== 'device') return
    updateLocal(target, (prev) => (prev.some((x) => x.key === e.key) ? prev.map((x) => (x.key === e.key ? e : x)) : [...prev, e]))
  }

  return {
    exams,
    /** Keys kept on this device only (not on the account). */
    onDevice: new Set(current ? local.filter((e) => !remoteKeys.has(e.key)).map((e) => e.key) : []),
    onAccount,
    /** False until the account plan has loaded: adding before then could overwrite a saved score. */
    ready: ready && current,
    canEdit,
    error,
    add: (e: PlannedExam) => {
      if (!editable || exams.some((x) => x.key === e.key) || exams.length >= MAX) return false
      void save(e)
      return true
    },
    setScore: (key: string, score: number | null) => {
      const e = exams.find((x) => x.key === key)
      if (e && editable) void save({ ...e, score })
    },
    setLevel: (key: string, level: IbLevel | null) => {
      const e = exams.find((x) => x.key === key)
      if (e && editable) void save({ ...e, level })
    },
    remove: (key: string) => {
      if (!editable) return
      setError(null)
      if (remoteKeys.has(key) && studentId)
        void source.removeExamPlanEntry(studentId, key).then(
          () => sid.current === studentId && setRemote((r) => r.filter((x) => x.key !== key)),
          (err: Error) => sid.current === studentId && setError(err.message),
        )
      updateLocal(studentId, (prev) => prev.filter((x) => x.key !== key))
    },
    max: MAX,
  }
}
