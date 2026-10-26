import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import { DataError } from '../../lib/data/source'
import type { BenchmarkSummary, Confidence, ExamFamily, PublicQuestion } from '../../lib/data/types'
import { FULL_FORM_READY, PER_SECTION, SECTION_LABEL, SECTION_ORDER, computeMetrics, nextDifficulty, planBenchmark, type BenchmarkKind, type BenchmarkPlan, type BenchmarkRecord, benchmarkSchedule } from '../../lib/engine/benchmark'
import { checkPlanFromCounts, pickCheckItem, type CheckSectionPlan } from '../../lib/engine/freshness'
import type { CheckItem } from '../../lib/data/source'
import { ActiveClock } from '../practice/useAttempt'
import { QuestionView, ConfidenceBar } from '../practice/QuestionView'
import { Button, ButtonLink, ChoiceCard, EmptyState, Notice, PageLoading, ProgressBar } from '../../components/ui'
import { Book, ChevronLeft, Clock, Compass, Flag, X } from '../../components/icons'
import { BenchmarkResults } from './BenchmarkResults'
import { useCatalog } from '../practice/useCatalog'
import { EXAM_NAME } from '../onboarding/options'
import { formatShortDate } from '../../lib/engine/dates'

interface Open {
  question: PublicQuestion
  attemptId: string
  clock: ActiveClock
  answer: string
  changes: number
  skipEvents: number
  returns: number
  firstInteraction: number | null
  shownAt: number
}

type Phase = 'intro' | 'running' | 'break' | 'done'

/** Per section, how many of this run's questions the student had seen before it started. */
function repeatsIn(records: { question_id: string; section: string }[], seen: Set<string>) {
  const m = new Map<string, number>()
  for (const r of records) if (seen.has(r.question_id)) m.set(r.section, (m.get(r.section) ?? 0) + 1)
  return m
}

export function Benchmark() {
  const { source, ctx } = useApp()
  const student = ctx?.myStudent ?? null
  const navigate = useNavigate()
  const plan = useAsync(() => (student ? source.getPlan(student.id) : Promise.resolve(null)), [source, student?.id])
  const history = useAsync(() => (student ? source.listBenchmarks(student.id) : Promise.resolve([])), [source, student?.id])
  const exam: ExamFamily = plan.data?.exam_family ?? 'act'
  const pool = useAsync(() => source.publishedQuestions(exam), [source, exam])
  // Everything this student has answered, for fresh-first selection and for marking repeats in the results.
  const answered = useAsync(() => (student ? source.attemptHistory(student.id, '1970-01-01T00:00:00Z') : Promise.resolve([])), [source, student?.id])
  const seenBefore = useMemo(() => new Set((answered.data ?? []).map((a) => a.question_id)), [answered.data])
  // CR-23: a check uses the reserved assessment pool only, never practice questions. Its content stays hidden until the
  // check opens, so before that the plan comes from counts (assessment_pool_status); null = the source can't say.
  const poolStatus = useAsync(() => (student ? source.assessmentPoolStatus(student.id, exam) : Promise.resolve(null)), [source, student?.id, exam])
  // #279: what the server will open now, and the student's live check (resumed, never replaced by fresh questions).
  const checkOpts = useAsync(() => (student ? source.benchmarkOptions(student.id, exam) : Promise.resolve(null)), [source, student?.id, exam])
  const openCheck = checkOpts.data?.open ?? null
  const openProgress = useAsync(() => (student && openCheck ? source.benchmarkProgress(openCheck.id, student.id) : Promise.resolve(null)), [source, student?.id, openCheck?.id])
  // The open check's own reserved items (benchmark_questions), once it has started.
  const [items, setItems] = useState<CheckItem[] | null>(null)
  const catalog = useCatalog(exam)

  const [kind, setKind] = useState<BenchmarkKind | null>(null)
  const [phase, setPhase] = useState<Phase>('intro')
  const [sectionIdx, setSectionIdx] = useState(0)
  const [current, setCurrent] = useState<Open | null>(null)
  const [records, setRecords] = useState<BenchmarkRecord[]>([])
  const [summary, setSummary] = useState<BenchmarkSummary | null>(null)
  const [error, setError] = useState<string | null>(null)
  // After an answer is saved, a failure to move on must not resubmit it: `stalled` offers "Continue" (advance only),
  // and `ended` means the server closed the check (expired), so only a new check can follow.
  const [stalled, setStalled] = useState(false)
  const [ended, setEnded] = useState(false)
  const [busy, setBusy] = useState(false)

  // Mutable run state that doesn't drive rendering directly.
  const run = useRef({
    used: new Set<string>(),
    served: 0,
    target: 3,
    skipped: [] as Open[],
    returning: false,
    startedAt: '',
    benchmarkId: null as string | null,
    items: [] as CheckItem[],
    plan: null as BenchmarkPlan | null,
    /** Attempts the server has saved: never submitted, skipped or resumed again. */
    submitted: new Set<string>(),
    /** Answers saved by the server whose reply was lost: this run's own record lacks them. */
    lostReplies: 0,
    /** A resumed check: answers from before the reload aren't in this run's record, so the server's metrics are shown. */
    resumed: false,
    /** Per section, items already used before a resume (they count toward the section's length). */
    usedBefore: {} as Record<string, number>,
  })
  // One action at a time (answer, skip, continue, next section): a double tap or a slow network can't run two.
  const lock = useRef(false)
  const exclusive = async (fn: () => Promise<void>) => {
    if (lock.current) return
    lock.current = true
    setBusy(true)
    try {
      await fn()
    } finally {
      lock.current = false
      setBusy(false)
    }
  }
  /** The server closed this check (expired, or no longer open): only a new check can follow. Other 22023s aren't. */
  const checkEnded = (e: unknown) => e instanceof DataError && e.code === 'invalid' && /expired|start a new one|not an open benchmark/i.test(e.message)
  const alreadySaved = (e: unknown) => e instanceof DataError && /already submitted/i.test(e.message)

  // The home screen links straight to the kind that is due (?kind=mini|full); otherwise use the schedule.
  const [params] = useSearchParams()
  const asked = params.get('kind')
  const scheduled: BenchmarkKind =
    (history.data?.length ?? 0) === 0 ? 'initial' : asked === 'mini' || (asked === 'full' && FULL_FORM_READY) ? asked : benchmarkSchedule(history.data ?? []).kind === 'full' ? 'full' : 'mini'
  // The kinds the server will open now (#279). Without that answer (an older source), the history decides, as before.
  const o = checkOpts.data
  const allowed: BenchmarkKind[] = o
    ? [...(o.initialAllowed ? (['initial'] as const) : []), ...(o.miniAllowed ? (['mini'] as const) : []), ...(o.fullAllowed && FULL_FORM_READY ? (['full'] as const) : [])]
    : (history.data?.length ?? 0) === 0 ? ['initial'] : FULL_FORM_READY ? ['mini', 'full'] : ['mini']
  const defaultKind: BenchmarkKind = openCheck ? openCheck.kind : allowed.includes(scheduled) ? scheduled : (allowed[0] ?? scheduled)
  const chosenKind = kind ?? defaultKind
  const wanted = (k: BenchmarkKind) => Object.fromEntries(SECTION_ORDER[exam].map((sec) => [sec, PER_SECTION[exam][k][sec] ?? 0]))
  // What the reserved pool allows, per section: fresh, with repeats (no verdict), shortened, or not measured.
  const poolPlan: CheckSectionPlan[] | null = useMemo(
    () => (poolStatus.data ? checkPlanFromCounts(wanted(chosenKind), poolStatus.data) : null),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [poolStatus.data, exam, chosenKind],
  )
  // Before the check opens: its size from the counts (time from practice questions' expected times, as an estimate).
  const avgSecs = useMemo(() => {
    const t = (pool.data ?? []).map((q) => q.expected_time_seconds ?? 60)
    return t.length ? t.reduce((a, b) => a + b, 0) / t.length : 60
  }, [pool.data])
  const planOf = (p: CheckSectionPlan[]): BenchmarkPlan => {
    const sections = p.filter((x) => x.count > 0).map((x) => ({ section: x.section, count: x.count }))
    const total = sections.reduce((n, x) => n + x.count, 0)
    return { exam, kind: chosenKind, sections, totalQuestions: total, expectedMinutes: Math.round((total * avgSecs * 1.3) / 60) }
  }
  const bplan: BenchmarkPlan | null = items ? run.current.plan : poolPlan ? planOf(poolPlan) : null
  const section = bplan?.sections[sectionIdx]

  const present = useCallback(
    async (q: PublicQuestion) => {
      if (!student) return
      // Claimed before the request, so a second advance can't pick the same question while this one is in flight.
      run.current.used.add(q.id)
      let attemptId: string
      try {
        attemptId = await source.startAttempt(student.id, q.id, null, run.current.benchmarkId)
      } catch (e) {
        // "Used once" means the server already started it (a lost reply): keep it used, or Continue would pick it again.
        // It also counts toward the section's length, as the server holds that (unanswered) attempt.
        if (e instanceof DataError && /used once/i.test(e.message)) run.current.served++
        else run.current.used.delete(q.id)
        throw e
      }
      const clock = new ActiveClock()
      clock.start()
      run.current.served++
      setCurrent({ question: q, attemptId, clock, answer: '', changes: 0, skipEvents: 0, returns: 0, firstInteraction: null, shownAt: performance.now() })
    },
    [source, student],
  )

  const resume = useCallback(
    async (o: Open) => {
      try {
        await source.recordEvent(o.attemptId, 'returned')
      } catch {
        // ignore
      }
      o.clock.start()
      setCurrent({ ...o, returns: o.returns + 1 })
    },
    [source],
  )

  /** Decides what comes next within the section, or ends it. */
  const advance = useCallback(async () => {
    if (!bplan || !section) return
    const r = run.current
    if (!r.returning && r.served < section.count) {
      // From this check's own reserved items: unseen first, so the check measures more than recall; repeats only when
      // the section's unseen ones run out (that section then gets no verdict). Never a practice question.
      const next = pickCheckItem(r.items, section.section, r.target, r.used)
      if (next) return present(next.question)
    }
    let back = r.skipped.shift()
    while (back && r.submitted.has(back.attemptId)) back = r.skipped.shift()
    if (back) {
      r.returning = true
      return resume(back)
    }
    setCurrent(null)
    setPhase(sectionIdx + 1 >= bplan.sections.length ? 'done' : 'break')
  }, [bplan, section, present, resume, sectionIdx])

  // When the run ends, save the summary.
  useEffect(() => {
    if (phase !== 'done' || summary || !student) return
    const s: BenchmarkSummary = {
      id: `bm-${Date.now()}`,
      kind: chosenKind,
      exam_family: exam,
      started_at: run.current.startedAt,
      completed_at: new Date().toISOString(),
      attempt_ids: records.map((x) => x.attempt_id),
      metrics: computeMetrics(records),
    }
    const id = run.current.benchmarkId
    const done = id ? source.completeBenchmark(student.id, id, s) : Promise.resolve(s)
    done.then(
      // Show this run's full detail now (history reads the stored copy). If a reply was lost, this screen's own record
      // is missing an answer the server has, so the server's metrics are shown instead.
      (saved) => setSummary(run.current.lostReplies > 0 || run.current.resumed ? saved : { ...saved, metrics: s.metrics }),
      (e: Error) => setError(e.message),
    )
  }, [phase, summary, student, records, chosenKind, exam, source])

  if (!student) return <Navigate to="/student" replace />
  if (plan.loading || pool.loading || history.loading || answered.loading || poolStatus.loading || checkOpts.loading || openProgress.loading) return <PageLoading />

  // Known to be empty (counts, or the open check's items): no check can be taken.
  if (bplan && bplan.totalQuestions === 0)
    return (
      <div className="mx-auto max-w-xl p-6">
        <EmptyState
          icon={<Book size={32} />}
          title={pool.data?.length ? `No ${EXAM_NAME[exam]} progress-check questions yet` : `No ${EXAM_NAME[exam]} questions are published yet`}
          action={<ButtonLink to="/student" variant="secondary">Back</ButtonLink>}
        >
          {pool.data?.length
            ? 'Progress checks use their own questions, kept out of practice, so a result measures more than memory. None are available for this test yet, so no check can be taken.'
            : "The benchmark needs a question bank, which hasn't been loaded for this test yet."}
        </EmptyState>
      </div>
    )

  const startSection = (idx: number) =>
    exclusive(async () => {
      const served = run.current.usedBefore[run.current.plan!.sections[idx]!.section] ?? 0
      run.current = { ...run.current, used: run.current.used, served, target: 3, skipped: [], returning: false }
      setSectionIdx(idx)
      setPhase('running')
      setError(null)
      setStalled(false)
      const sec = run.current.plan!.sections[idx]!
      const next = pickCheckItem(run.current.items, sec.section, 3, run.current.used)
      // The break screen is where a check most often passes its 4 hours: an expired check says so here too.
      if (next) await present(next.question).catch(onMoveError)
    })

  /** After an answer is saved, a failure only affects what comes next: say so, and never send the answer again. */
  const onMoveError = (e: unknown) => {
    if (checkEnded(e)) setEnded(true)
    else {
      setError(e instanceof Error ? e.message : 'Could not load the next question')
      setStalled(true)
    }
  }

  const finishAttempt = (opts: { confidence?: Confidence; skipped?: boolean }) => exclusive(() => submitCurrent(opts))

  const submitCurrent = async (opts: { confidence?: Confidence; skipped?: boolean }) => {
    if (!current || run.current.submitted.has(current.attemptId)) return
    setError(null)
    current.clock.pause()
    try {
      // The event is a log entry: on a retry after a lost reply it can be refused, and that mustn't block the answer.
      if (!opts.skipped) await source.recordEvent(current.attemptId, 'answered', current.answer).catch(() => undefined)
      const res = await source.submitAttempt(current.attemptId, {
        answer: opts.skipped ? null : current.answer,
        activeMs: current.clock.ms,
        firstInteractionMs: current.firstInteraction ?? undefined,
        confidence: opts.confidence,
        skipped: opts.skipped,
      })
      const q = current.question
      setRecords((rs) => [
        ...rs,
        {
          question_id: q.id,
          attempt_id: current.attemptId,
          section: q.section,
          difficulty: q.difficulty,
          skill_key: q.primary_skill_key,
          expected_time_seconds: q.expected_time_seconds,
          answer: opts.skipped ? null : current.answer,
          is_correct: res.is_correct,
          skipped: res.skipped,
          elapsed_ms: res.elapsed_ms,
          active_ms: current.clock.ms,
          confidence: opts.confidence ?? null,
          strategy_key: null,
          skip_events: current.skipEvents,
          returns: current.returns,
          answer_changes: current.changes,
          trap: res.is_correct === false ? (res.distractors.find((d) => d.choice === current.answer)?.trap ?? null) : null,
        },
      ])
      if (!run.current.returning) run.current.target = nextDifficulty(run.current.target, res.is_correct)
    } catch (e) {
      // The server already has it (the reply was lost on the way back): treat it as saved and move on.
      if (alreadySaved(e)) {
        run.current.submitted.add(current.attemptId)
        run.current.lostReplies++
        setCurrent(null)
        await moveOnNow()
        return
      }
      if (checkEnded(e)) {
        setEnded(true)
        return
      }
      current.clock.start()
      setError(e instanceof Error ? e.message : 'Could not save that answer')
      return
    }
    // Saved. From here a failure only affects what comes next; the answer is never sent again.
    run.current.submitted.add(current.attemptId)
    setCurrent(null)
    await moveOnNow()
  }

  const moveOnNow = async () => {
    setError(null)
    setStalled(false)
    try {
      await advance()
    } catch (e) {
      onMoveError(e)
    }
  }
  const moveOn = () => exclusive(moveOnNow)

  const skipForNow = () =>
    exclusive(async () => {
      if (!current || run.current.submitted.has(current.attemptId)) return
      const open = current
      open.clock.pause()
      try {
        await source.recordEvent(open.attemptId, 'skipped')
      } catch {
        // ignore
      }
      if (!run.current.skipped.some((x) => x.attemptId === open.attemptId)) run.current.skipped.push({ ...open, skipEvents: open.skipEvents + 1 })
      setCurrent(null)
      await moveOnNow()
    })

  /** Resumes the student's live check (#279): the same check and assignment, from the first section with items left. */
  const resumeOpen = async () => {
    if (!openCheck || lock.current) return
    lock.current = true
    setBusy(true)
    let begin: number | null = null
    try {
      const id = openCheck.id
      const [list, prog] = await Promise.all([source.benchmarkQuestions(id, student.id, exam), source.benchmarkProgress(id, student.id)])
      const sections = SECTION_ORDER[exam].flatMap((sec) => {
        const p = prog.find((x) => x.section === sec)
        return p && p.assigned > 0 ? [{ section: sec, count: p.assigned }] : []
      })
      const total = sections.reduce((n, x) => n + x.count, 0)
      run.current.benchmarkId = id
      run.current.startedAt = openCheck.startedAt || new Date().toISOString()
      run.current.resumed = true
      run.current.usedBefore = Object.fromEntries(prog.map((p) => [p.section, p.used]))
      run.current.items = list
      run.current.plan = { exam, kind: openCheck.kind, sections, totalQuestions: total, expectedMinutes: Math.round((total * avgSecs * 1.3) / 60) }
      setKind(openCheck.kind)
      setItems(list)
      const idx = sections.findIndex((x) => (run.current.usedBefore[x.section] ?? 0) < x.count)
      begin = idx
    } catch (e) {
      setError((e as Error).message)
    } finally {
      lock.current = false
      setBusy(false)
    }
    if (begin === -1) setPhase('done')
    else if (begin !== null) void startSection(begin)
  }

  if (phase === 'intro' && openCheck) {
    const left = (openProgress.data ?? []).reduce((n, p) => n + Math.max(0, p.assigned - p.used), 0)
    return (
      <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-xl flex-col px-4">
        <div className="flex h-16 items-center">
          <button onClick={() => navigate('/student')} className="grid h-10 w-10 place-items-center rounded-full text-ink-2 hover:bg-surface-2" aria-label="Back">
            <ChevronLeft />
          </button>
        </div>
        <div className="anim-rise flex-1">
          <span className="grid h-14 w-14 place-items-center rounded-2xl bg-brand-soft text-brand">
            <Compass size={28} />
          </span>
          <h1 className="display mt-4 text-[32px] font-semibold leading-tight text-ink">Your progress check is still open</h1>
          <p className="mt-2 text-ink-2">
            Pick up where you left off: {left === 1 ? '1 question is' : `${left} questions are`} left. Questions you were already shown stay used, and no new
            ones are added.
          </p>
          {error && (
            <Notice tone="bad" title="The check couldn't continue" className="mt-4">
              {error}
            </Notice>
          )}
        </div>
        <div className="sticky bottom-0 -mx-4 border-t border-line bg-bg/95 px-4 py-4 pb-[max(1rem,env(safe-area-inset-bottom))]">
          <Button size="lg" block disabled={busy} onClick={() => void resumeOpen()}>
            Resume the check
          </Button>
        </div>
      </div>
    )
  }

  if (phase === 'intro') {
    const options = allowed
    const blockedUntil = !options.length && o?.miniOpensOn ? o.miniOpensOn : null
    return (
      <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-xl flex-col px-4">
        <div className="flex h-16 items-center">
          <button onClick={() => navigate('/student')} className="grid h-10 w-10 place-items-center rounded-full text-ink-2 hover:bg-surface-2" aria-label="Back">
            <ChevronLeft />
          </button>
        </div>
        <div className="anim-rise flex-1">
          <span className="grid h-14 w-14 place-items-center rounded-2xl bg-brand-soft text-brand">
            <Compass size={28} />
          </span>
          <h1 className="display mt-4 text-[32px] font-semibold leading-tight text-ink">
            {chosenKind === 'initial' ? "Let's find your starting point" : 'Check how far you have come'}
          </h1>
          <p className="mt-2 text-ink-2">
            {bplan
              ? `${EXAM_NAME[exam]} benchmark · ${bplan.totalQuestions} questions · about ${bplan.expectedMinutes} minutes. It adapts as you go, so it is shorter than a full test.`
              : `${EXAM_NAME[exam]} benchmark. Its length is set when it starts, from the questions set aside for checks. It adapts as you go, so it is shorter than a full test.`}
          </p>
          {chosenKind === 'mini' && !FULL_FORM_READY && (
            <p className="mt-2 text-sm text-ink-3">
              A full-length check isn't available yet. It needs its own set of questions that never appear in practice, and those haven't been written.
            </p>
          )}
          {poolPlan && options.length > 0 && <PoolNotice plan={poolPlan} />}
          {!options.length && (
            <Notice tone="warn" title={blockedUntil ? `Your next progress check opens on ${formatShortDate(blockedUntil)}` : 'No progress check can be started right now'} className="mt-4">
              Checks are spaced out so each one has questions you haven't seen. Practice in the meantime counts toward the next one.
            </Notice>
          )}
          {error && (
            <Notice tone="bad" title="The check didn't start" className="mt-4">
              {error}
            </Notice>
          )}
          {options.length > 1 && (
            <div className="mt-6 grid gap-3">
              {options.map((k) => {
                const p = poolStatus.data ? planOf(checkPlanFromCounts(wanted(k), poolStatus.data)) : null
                return (
                  <ChoiceCard
                    key={k}
                    selected={chosenKind === k}
                    onClick={() => setKind(k)}
                    title={k === 'mini' ? 'Mini benchmark' : 'Full benchmark'}
                    description={`${p ? `${p.totalQuestions} questions · ~${p.expectedMinutes} min` : 'Length set when it starts'}${k === 'full' ? ' · best before a real test' : ' · every 4–6 weeks'}`}
                  />
                )
              })}
            </div>
          )}
          <ul className="mt-6 grid gap-3 text-sm text-ink-2">
            <Rule icon={<Clock size={18} />} text="Work at a test-day pace, but don't rush. We measure speed separately from knowledge." />
            <Rule icon={<Flag size={18} />} text="Stuck? Skip it. Skipped questions come back at the end of each section." />
            <Rule icon={<Compass size={18} />} text="After each answer, tell us how sure you are. That shows whether to trust your instincts." />
            <Rule icon={<X size={18} />} text="No hints or explanations during the benchmark. You'll get a full breakdown at the end." />
          </ul>
        </div>
        <div className="sticky bottom-0 -mx-4 border-t border-line bg-bg/95 px-4 py-4 pb-[max(1rem,env(safe-area-inset-bottom))]">
          <Button
            size="lg"
            block
            disabled={busy || !options.includes(chosenKind)}
            onClick={async () => {
              // Under the same lock as every other action, so a double tap can't open two checks.
              if (lock.current) return
              lock.current = true
              run.current.startedAt = new Date().toISOString()
              setBusy(true)
              let begin = false
              try {
                const id = await source.startBenchmark(student.id, chosenKind, exam)
                run.current.benchmarkId = id
                // The check's own reserved items, now readable; its plan is sized from them.
                const list = await source.benchmarkQuestions(id, student.id, exam)
                run.current.items = list
                run.current.plan = planBenchmark(exam, chosenKind, list.map((i) => i.question))
                setItems(list)
                begin = run.current.plan.totalQuestions > 0
              } catch (e) {
                setError((e as Error).message)
                // The server's answer wins (e.g. a check opened on another device): read it again.
                checkOpts.reload()
              } finally {
                lock.current = false
                setBusy(false)
              }
              if (begin) void startSection(0)
            }}
          >
            {bplan?.sections[0] ? `Start ${SECTION_LABEL[bplan.sections[0].section]}` : 'Start the check'}
          </Button>
        </div>
      </div>
    )
  }

  if (phase === 'break') {
    const bp = run.current.plan!
    const next = bp.sections[sectionIdx + 1]!
    const doneSec = bp.sections[sectionIdx]!
    return (
      <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-md flex-col items-center justify-center px-4 text-center">
        <div className="anim-pop text-5xl" aria-hidden>
          ✓
        </div>
        <h1 className="display mt-4 text-3xl font-semibold text-ink">{SECTION_LABEL[doneSec.section]} done</h1>
        <p className="mt-2 text-ink-2">
          Section {sectionIdx + 2} of {bp.sections.length} is {SECTION_LABEL[next.section]} ({next.count} questions). Take a breath, stretch, then go.
        </p>
        <ProgressBar value={sectionIdx + 1} max={bp.sections.length} label="Sections complete" className="mt-6" />
        <Button size="lg" block className="mt-8" onClick={() => void startSection(sectionIdx + 1)}>
          Start {SECTION_LABEL[next.section]}
        </Button>
      </div>
    )
  }

  if (phase === 'done') {
    if (!summary) return <PageLoading />
    return <BenchmarkResults summary={summary} strategies={catalog.strategies} traps={catalog.traps} skillName={catalog.skillName} history={history.data ?? []} attempts={answered.data ?? []} currentRepeats={repeatsIn(records, new Set([...seenBefore, ...(items ?? []).filter((i) => i.seen_before).map((i) => i.question.id)]))} />
  }

  // A resumed section counts the questions used before the reload (answered or shown), as the server does.
  const answeredInSection = records.filter((r) => r.section === section?.section).length + (section ? (run.current.usedBefore[section.section] ?? 0) : 0)
  return (
    <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-5xl flex-col px-4">
      <div className="flex h-16 items-center gap-3">
        <button
          onClick={() => {
            if (confirm('Leave the benchmark? Answers so far are saved, but you will need to start a new benchmark for results.')) navigate('/student')
          }}
          className="grid h-10 w-10 place-items-center rounded-full text-ink-2 hover:bg-surface-2"
          aria-label="Leave benchmark"
        >
          <X />
        </button>
        <div className="flex-1">
          <div className="mb-1 flex justify-between text-xs font-semibold text-ink-3">
            <span>
              {SECTION_LABEL[section!.section]} · section {sectionIdx + 1} of {(run.current.plan ?? bplan)!.sections.length}
            </span>
            <span className="tabular">
              {Math.min(answeredInSection + 1, section!.count)} / {section!.count}
            </span>
          </div>
          <ProgressBar value={answeredInSection} max={section!.count} label="Section progress" tone="brand" />
        </div>
      </div>
      {run.current.returning && current && <Notice tone="gold" className="mb-4">Back to a question you skipped. Answer it now or leave it blank.</Notice>}
      <div className="flex-1 pb-6">
        {current && (
          <QuestionView
            question={current.question}
            answer={current.answer}
            onChoose={(a) =>
              setCurrent((c) =>
                c && {
                  ...c,
                  answer: a,
                  changes: c.answer && c.answer !== a ? c.changes + 1 : c.changes,
                  firstInteraction: c.firstInteraction ?? Math.floor(performance.now() - c.shownAt),
                },
              )
            }
          />
        )}
        {ended ? (
          <Notice tone="warn" title="This progress check has ended" className="mt-4">
            <p>Your answers so far are saved, but this check can't continue (checks close 4 hours after they start). Start a new check for a result.</p>
            <Button className="mt-3" onClick={() => navigate(0)}>
              Start a new check
            </Button>
          </Notice>
        ) : (
          error && (
            <Notice tone="bad" className="mt-4">
              <p>{error}</p>
              {stalled && (
                <Button variant="secondary" className="mt-3" disabled={busy} onClick={() => void moveOn()}>
                  Continue
                </Button>
              )}
            </Notice>
          )
        )}
      </div>
      <div className="sticky bottom-0 -mx-4 border-t border-line bg-bg/95 px-4 py-4 pb-[max(1rem,env(safe-area-inset-bottom))] backdrop-blur">
        <div className="mx-auto grid max-w-xl gap-3">
          {current?.answer ? (
            <ConfidenceBar disabled={busy} onPick={(c) => void finishAttempt({ confidence: c })} />
          ) : (
            <p className="py-2 text-center text-sm text-ink-3">{current && current.question.answer_format !== 'choice' ? 'Type your answer' : 'Choose an answer'}</p>
          )}
          <button
            disabled={busy || !current}
            onClick={() => void (run.current.returning ? finishAttempt({ skipped: true }) : skipForNow())}
            className="text-sm font-semibold text-ink-3 hover:text-ink disabled:opacity-40"
          >
            {run.current.returning ? 'Leave it blank' : 'Skip for now'}
          </button>
        </div>
      </div>
    </div>
  )
}

function Rule({ icon, text }: { icon: React.ReactNode; text: string }) {
  return (
    <li className="flex gap-3">
      <span className="mt-0.5 shrink-0 text-brand">{icon}</span>
      <span>{text}</span>
    </li>
  )
}

/** Says, before the check starts, where the reserved pool can't give a fully fresh, full-length section. */
function PoolNotice({ plan }: { plan: CheckSectionPlan[] }) {
  const off = plan.filter((p) => p.status === 'not_measured')
  const repeats = plan.filter((p) => p.status === 'with_repeats')
  const short = plan.filter((p) => p.shortened)
  if (!off.length && !repeats.length && !short.length) return null
  const names = (xs: typeof plan) => xs.map((x) => SECTION_LABEL[x.section] ?? x.section).join(', ')
  return (
    <Notice tone="warn" title="This check is limited by the questions set aside for checks" className="mt-4">
      <ul className="grid list-disc gap-1 pl-5 text-sm">
        {off.length > 0 && <li>Not measured this time: {names(off)}. No check questions are available there.</li>}
        {short.length > 0 && <li>Shorter than usual: {short.map((x) => `${SECTION_LABEL[x.section] ?? x.section} (${x.count} of ${x.wanted})`).join(', ')}.</li>}
        {repeats.length > 0 && (
          <li>
            Includes questions you've seen before: {names(repeats)}. Those sections won't be compared with earlier checks, because a repeat can be remembered.
          </li>
        )}
      </ul>
    </Notice>
  )
}
