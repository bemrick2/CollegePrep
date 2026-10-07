import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import type { BenchmarkSummary, Confidence, ExamFamily, PublicQuestion } from '../../lib/data/types'
import { SECTION_LABEL, computeMetrics, nextDifficulty, pickNext, planBenchmark, type BenchmarkKind, type BenchmarkPlan, type BenchmarkRecord, benchmarkSchedule } from '../../lib/engine/benchmark'
import { ActiveClock } from '../practice/useAttempt'
import { QuestionView, ConfidenceBar } from '../practice/QuestionView'
import { Button, ButtonLink, ChoiceCard, EmptyState, Notice, PageLoading, ProgressBar } from '../../components/ui'
import { Book, ChevronLeft, Clock, Compass, Flag, X } from '../../components/icons'
import { BenchmarkResults } from './BenchmarkResults'
import { useCatalog } from '../practice/useCatalog'
import { EXAM_NAME } from '../onboarding/options'

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
  const catalog = useCatalog(exam)

  const [kind, setKind] = useState<BenchmarkKind | null>(null)
  const [phase, setPhase] = useState<Phase>('intro')
  const [sectionIdx, setSectionIdx] = useState(0)
  const [current, setCurrent] = useState<Open | null>(null)
  const [records, setRecords] = useState<BenchmarkRecord[]>([])
  const [summary, setSummary] = useState<BenchmarkSummary | null>(null)
  const [error, setError] = useState<string | null>(null)
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
  })

  // The home screen links straight to the kind that is due (?kind=mini|full); otherwise use the schedule.
  const [params] = useSearchParams()
  const asked = params.get('kind')
  const defaultKind: BenchmarkKind =
    (history.data?.length ?? 0) === 0 ? 'initial' : asked === 'mini' || asked === 'full' ? asked : benchmarkSchedule(history.data ?? []).kind === 'full' ? 'full' : 'mini'
  const chosenKind = kind ?? defaultKind
  const bplan: BenchmarkPlan | null = useMemo(() => (pool.data ? planBenchmark(exam, chosenKind, pool.data) : null), [pool.data, exam, chosenKind])
  const section = bplan?.sections[sectionIdx]

  const present = useCallback(
    async (q: PublicQuestion) => {
      if (!student) return
      const attemptId = await source.startAttempt(student.id, q.id, null, run.current.benchmarkId)
      const clock = new ActiveClock()
      clock.start()
      run.current.used.add(q.id)
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
    if (!bplan || !section || !pool.data) return
    const r = run.current
    if (!r.returning && r.served < section.count) {
      // Fresh questions first, so the check measures more than recall; seen ones only when a section runs out.
      const inExam = pool.data.filter((x) => x.exam_family === exam)
      const q = pickNext(inExam.filter((x) => !seenBefore.has(x.id)), section.section, r.target, r.used) ?? pickNext(inExam, section.section, r.target, r.used)
      if (q) return present(q)
    }
    const back = r.skipped.shift()
    if (back) {
      r.returning = true
      return resume(back)
    }
    setCurrent(null)
    setPhase(sectionIdx + 1 >= bplan.sections.length ? 'done' : 'break')
  }, [bplan, section, pool.data, exam, present, resume, sectionIdx, seenBefore])

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
      (saved) => setSummary({ ...saved, metrics: s.metrics }), // show this run's full detail now; history reads the stored copy
      (e: Error) => setError(e.message),
    )
  }, [phase, summary, student, records, chosenKind, exam, source])

  if (!student) return <Navigate to="/student" replace />
  if (plan.loading || pool.loading || history.loading || answered.loading) return <PageLoading />

  if (!bplan || bplan.totalQuestions === 0)
    return (
      <div className="mx-auto max-w-xl p-6">
        <EmptyState icon={<Book size={32} />} title={`No ${EXAM_NAME[exam]} questions are published yet`} action={<ButtonLink to="/student" variant="secondary">Back</ButtonLink>}>
          The benchmark needs a question bank, which hasn't been loaded for this test yet.
        </EmptyState>
      </div>
    )

  const startSection = async (idx: number) => {
    run.current = { ...run.current, used: run.current.used, served: 0, target: 3, skipped: [], returning: false }
    setSectionIdx(idx)
    setPhase('running')
    const sec = bplan.sections[idx]!
    const q = pickNext(pool.data!.filter((x) => x.exam_family === exam), sec.section, 3, run.current.used)
    if (q) await present(q).catch((e: Error) => setError(e.message))
  }

  const finishAttempt = async (opts: { confidence?: Confidence; skipped?: boolean }) => {
    if (!current) return
    setBusy(true)
    setError(null)
    current.clock.pause()
    try {
      if (!opts.skipped) await source.recordEvent(current.attemptId, 'answered', current.answer)
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
      await advance()
    } catch (e) {
      current.clock.start()
      setError(e instanceof Error ? e.message : 'Could not save that answer')
    } finally {
      setBusy(false)
    }
  }

  const skipForNow = async () => {
    if (!current) return
    current.clock.pause()
    try {
      await source.recordEvent(current.attemptId, 'skipped')
    } catch {
      // ignore
    }
    run.current.skipped.push({ ...current, skipEvents: current.skipEvents + 1 })
    await advance()
  }

  if (phase === 'intro') {
    const options: BenchmarkKind[] = (history.data?.length ?? 0) === 0 ? ['initial'] : ['mini', 'full']
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
            {EXAM_NAME[exam]} benchmark · {bplan.totalQuestions} questions · about {bplan.expectedMinutes} minutes. It adapts as you go, so it is shorter than a full test.
          </p>
          {options.length > 1 && (
            <div className="mt-6 grid gap-3">
              {options.map((k) => {
                const p = planBenchmark(exam, k, pool.data!)
                return (
                  <ChoiceCard
                    key={k}
                    selected={chosenKind === k}
                    onClick={() => setKind(k)}
                    title={k === 'mini' ? 'Mini benchmark' : 'Full benchmark'}
                    description={`${p.totalQuestions} questions · ~${p.expectedMinutes} min${k === 'full' ? ' · best before a real test' : ' · every 4–6 weeks'}`}
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
            disabled={busy}
            onClick={async () => {
              run.current.startedAt = new Date().toISOString()
              setBusy(true)
              try {
                run.current.benchmarkId = await source.startBenchmark(student.id, chosenKind, exam)
                void startSection(0)
              } catch (e) {
                setError((e as Error).message)
              } finally {
                setBusy(false)
              }
            }}
          >
            Start {SECTION_LABEL[bplan.sections[0]!.section]}
          </Button>
        </div>
      </div>
    )
  }

  if (phase === 'break') {
    const next = bplan.sections[sectionIdx + 1]!
    const doneSec = bplan.sections[sectionIdx]!
    return (
      <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-md flex-col items-center justify-center px-4 text-center">
        <div className="anim-pop text-5xl" aria-hidden>
          ✓
        </div>
        <h1 className="display mt-4 text-3xl font-semibold text-ink">{SECTION_LABEL[doneSec.section]} done</h1>
        <p className="mt-2 text-ink-2">
          Section {sectionIdx + 2} of {bplan.sections.length} is {SECTION_LABEL[next.section]} ({next.count} questions). Take a breath, stretch, then go.
        </p>
        <ProgressBar value={sectionIdx + 1} max={bplan.sections.length} label="Sections complete" className="mt-6" />
        <Button size="lg" block className="mt-8" onClick={() => void startSection(sectionIdx + 1)}>
          Start {SECTION_LABEL[next.section]}
        </Button>
      </div>
    )
  }

  if (phase === 'done') {
    if (!summary) return <PageLoading />
    return <BenchmarkResults summary={summary} strategies={catalog.strategies} traps={catalog.traps} skillName={catalog.skillName} history={history.data ?? []} attempts={answered.data ?? []} currentRepeats={repeatsIn(records, seenBefore)} />
  }

  const answeredInSection = records.filter((r) => r.section === section?.section).length
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
              {SECTION_LABEL[section!.section]} · section {sectionIdx + 1} of {bplan.sections.length}
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
        {error && <Notice tone="bad" className="mt-4">{error}</Notice>}
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
