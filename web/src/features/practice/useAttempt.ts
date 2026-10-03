import { useCallback, useEffect, useRef, useState } from 'react'
import type { Confidence, PublicQuestion, SubmitResult } from '../../lib/data/types'
import { useApp } from '../../lib/app'

/**
 * Measures active time (tab visible and not paused) for one attempt.
 * Server time stays authoritative; active_ms is the client's honest
 * complement and is always <= the server's elapsed time.
 */
export class ActiveClock {
  private total = 0
  private since: number | null = null
  constructor(private now: () => number = () => performance.now()) {}
  start() {
    if (this.since === null) this.since = this.now()
  }
  pause() {
    if (this.since !== null) {
      this.total += this.now() - this.since
      this.since = null
    }
  }
  get ms() {
    return Math.floor(this.total + (this.since !== null ? this.now() - this.since : 0))
  }
}

export interface AttemptState {
  attemptId: string | null
  answer: string
  changes: number
  skipEvents: number
  returns: number
  hints: string[]
  hintsLeft: number | null
  result: SubmitResult | null
  error: string | null
  busy: boolean
}

export function useAttempt(studentId: string, question: PublicQuestion | null, sessionId: string | null) {
  const { source } = useApp()
  const clock = useRef(new ActiveClock())
  const firstInteraction = useRef<number | null>(null)
  const startedAt = useRef(0)
  const [s, set] = useState<AttemptState>(blank())

  // Start an attempt whenever the question changes.
  useEffect(() => {
    if (!question) return
    let alive = true
    set(blank())
    clock.current = new ActiveClock()
    firstInteraction.current = null
    source.startAttempt(studentId, question.id, sessionId).then(
      (id) => {
        if (!alive) return
        startedAt.current = performance.now()
        if (document.visibilityState === 'visible') clock.current.start()
        set((x) => ({ ...x, attemptId: id }))
      },
      (e: Error) => alive && set((x) => ({ ...x, error: e.message })),
    )
    return () => {
      alive = false
    }
  }, [question, studentId, sessionId, source])

  useEffect(() => {
    const onVis = () => (document.visibilityState === 'visible' ? clock.current.start() : clock.current.pause())
    document.addEventListener('visibilitychange', onVis)
    return () => document.removeEventListener('visibilitychange', onVis)
  }, [])

  const choose = useCallback(
    (answer: string) => {
      if (firstInteraction.current === null && startedAt.current) firstInteraction.current = Math.floor(performance.now() - startedAt.current)
      set((x) => ({ ...x, answer, changes: x.answer && x.answer !== answer ? x.changes + 1 : x.changes }))
    },
    [],
  )

  /** Logs the selection; called when the student commits to an answer. */
  const logAnswer = useCallback(async () => {
    if (!s.attemptId || !s.answer.trim()) return
    try {
      await source.recordEvent(s.attemptId, 'answered', s.answer)
    } catch {
      // Non-fatal: the submit still records the final answer.
    }
  }, [s.attemptId, s.answer, source])

  const submit = useCallback(
    async (opts: { confidence?: Confidence; strategyKey?: string; skipped?: boolean } = {}) => {
      if (!s.attemptId) return null
      set((x) => ({ ...x, busy: true, error: null }))
      clock.current.pause()
      try {
        if (!opts.skipped) await logAnswer()
        const result = await source.submitAttempt(s.attemptId, {
          answer: opts.skipped ? null : s.answer,
          activeMs: clock.current.ms,
          firstInteractionMs: firstInteraction.current ?? undefined,
          confidence: opts.confidence,
          strategyKey: opts.strategyKey,
          skipped: opts.skipped,
        })
        set((x) => ({ ...x, result, busy: false }))
        return { result, activeMs: clock.current.ms }
      } catch (e) {
        clock.current.start()
        set((x) => ({ ...x, busy: false, error: e instanceof Error ? e.message : 'Could not submit' }))
        return null
      }
    },
    [s.attemptId, s.answer, source, logAnswer],
  )

  /** Skip for now: the attempt stays open and the clock pauses until the student returns. */
  const skipForNow = useCallback(async () => {
    if (!s.attemptId) return
    clock.current.pause()
    set((x) => ({ ...x, skipEvents: x.skipEvents + 1 }))
    try {
      await source.recordEvent(s.attemptId, 'skipped')
    } catch {
      // ignore
    }
  }, [s.attemptId, source])

  const hint = useCallback(async () => {
    if (!s.attemptId) return
    try {
      const h = await source.requestHint(s.attemptId)
      set((x) => ({ ...x, hints: [...x.hints, h.hint], hintsLeft: h.remaining }))
    } catch (e) {
      set((x) => ({ ...x, hintsLeft: 0, error: e instanceof Error && /No more hints/.test(e.message) ? null : (e as Error).message }))
    }
  }, [s.attemptId, source])

  return { state: s, choose, submit, skipForNow, hint, clock: clock.current, firstInteraction }
}

function blank(): AttemptState {
  return { attemptId: null, answer: '', changes: 0, skipEvents: 0, returns: 0, hints: [], hintsLeft: null, result: null, error: null, busy: false }
}
