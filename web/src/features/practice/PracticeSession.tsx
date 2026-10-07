import { useEffect, useMemo, useState } from 'react'
import { Link, Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import type { Confidence, PracticeSession as Session } from '../../lib/data/types'
import { ButtonLink, EmptyState, Notice, PageLoading, ProgressBar, Ring } from '../../components/ui'
import { Book, Compass, Flame, Lightbulb, Sparkle, X } from '../../components/icons'
import { QuestionView, ConfidenceBar } from './QuestionView'
import { Feedback } from './Feedback'
import { useAttempt } from './useAttempt'
import { useCatalog } from './useCatalog'
import { RUSHED_BELOW } from '../../lib/engine/benchmark'
import { QUICK_SESSION_MINUTES } from '../../../../supabase/functions/_shared/reminders.ts'
import { xpFor } from '../../lib/engine/gamify'
import { formatDuration, localDate, weekStartOf } from '../../lib/engine/dates'

interface Outcome {
  /** Shown to this student before: counts toward the goal, not fresh evidence. */
  seenBefore: boolean
  correct: boolean | null
  elapsed_ms: number
  expected: number | null
  skill: string | null
}

const REASON_LABEL: Record<string, string> = {
  weak_knowledge: 'Building a weak skill',
  weak_pacing: 'Working on speed',
  new_skill: 'Something new',
  review: 'Keeping it sharp',
  untagged: 'Mixed practice',
}

export function PracticeSession() {
  const { source, ctx } = useApp()
  const student = ctx?.myStudent ?? null
  const navigate = useNavigate()
  const [params] = useSearchParams()
  const quick = params.get('quick') === '1'
  const reminderId = params.get('r')
  const plan = useAsync(() => (student ? source.getPlan(student.id) : Promise.resolve(null)), [source, student?.id])
  const exam = plan.data?.exam_family ?? 'act'
  const [session, setSession] = useState<Session | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [index, setIndex] = useState(0)
  const [outcomes, setOutcomes] = useState<Outcome[]>([])
  const [done, setDone] = useState(false)
  const catalog = useCatalog(exam)

  useEffect(() => {
    if (!student || plan.loading || session) return
    // A reminder tap opens a short session (?quick=1); ?r= records that the reminder was opened.
    const minutes = quick ? QUICK_SESSION_MINUTES : Math.min(source.supportsAccountSetup ? 30 : 15, Math.max(5, plan.data?.daily_minutes ?? 10))
    if (reminderId) void source.markReminderOpened(reminderId).catch(() => {})
    source.startSession(student.id, minutes, exam).then(setSession, (e: Error) => setError(e.message))
    // Start once per mount.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [student?.id, plan.loading])

  const item = session?.items[index] ?? null
  const question = useMemo(() => item?.question ?? null, [item])
  const attempt = useAttempt(student?.id ?? '', done ? null : question, session?.id ?? null)
  const [remember, setRemember] = useState<string | null>(null)
  const [aiNote, setAiNote] = useState<string | null>(null)
  const [help, setHelp] = useState<{ concept: boolean; strategy: boolean }>({ concept: false, strategy: false })

  useEffect(() => {
    setRemember(null)
    setAiNote(null)
    setHelp({ concept: false, strategy: false })
  }, [question?.id])

  if (!student) return <Navigate to="/student" replace />
  if (error) return <div className="mx-auto max-w-xl p-6"><Notice tone="bad" title="Could not start a session">{error}</Notice></div>
  if (!session) return <PageLoading />

  if (session.items.length === 0)
    return (
      <div className="mx-auto max-w-xl p-6">
        <EmptyState
          icon={<Book size={32} />}
          title="No practice questions are published yet"
          action={<ButtonLink to="/student" variant="secondary">Back to today</ButtonLink>}
        >
          Your account works, but the question bank hasn't been loaded for this test. Check back soon.
        </EmptyState>
      </div>
    )

  const finish = async () => {
    setDone(true)
    try {
      await source.endSession(session.id)
    } catch {
      // The session may already be closed; the summary still shows.
    }
  }

  if (done) return <SessionSummary outcomes={outcomes} studentId={student.id} skillName={catalog.skillName} />

  const onPick = async (confidence: Confidence) => {
    const r = await attempt.submit({ confidence })
    if (!r || !question) return
    setOutcomes((o) => [...o, { seenBefore: !!item?.seen_before, correct: r.result.is_correct, elapsed_ms: r.result.elapsed_ms, expected: question.expected_time_seconds, skill: question.primary_skill_key }])
    setRemember(r.result.remember_text ?? (await source.rememberThis(question.id)))
  }

  const next = () => {
    if (index + 1 >= session.items.length) void finish()
    else setIndex((i) => i + 1)
  }

  // "Teach me" and "Test strategy" before answering never reveal the answer: they show the skill's primer and the
  // strategies for this section. The request is still recorded (request_ai_help) so help use is measured, and a
  // tutor reply appears only if the backend tutor is switched on.
  const askHelp = async (mode: 'concept' | 'strategy') => {
    if (!attempt.state.attemptId) return
    setHelp((h) => ({ ...h, [mode]: true }))
    const r = await source.requestAiHelp(attempt.state.attemptId, mode)
    const haveStatic = mode === 'concept' ? !!catalog.skill(question?.primary_skill_key)?.concept_summary : catalog.strategiesFor(question?.section).length > 0
    if (r.status !== 'disabled') setAiNote('Your tutor request is queued. The explanation will appear here when it is ready.')
    else if (!haveStatic) setAiNote("The AI tutor isn't switched on yet. Try a hint — after you answer you'll get the full explanation.")
  }

  const total = session.items.length
  const { state } = attempt
  const streakish = outcomes.slice().reverse().findIndex((o) => !o.correct)
  const run = streakish === -1 ? outcomes.length : streakish

  return (
    <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-5xl flex-col px-4">
      <h1 className="sr-only">Practice · question {index + 1} of {total}</h1>
      <div className="flex h-16 items-center gap-3">
        <button
          onClick={() => {
            if (outcomes.length === 0 || confirm('End this session? Answers so far are saved.')) {
              if (outcomes.length) void finish()
              else navigate('/student')
            }
          }}
          className="grid h-10 w-10 place-items-center rounded-full text-ink-2 hover:bg-surface-2"
          aria-label="End session"
        >
          <X />
        </button>
        <ProgressBar value={index + (state.result ? 1 : 0)} max={total} label={`Question ${index + 1} of ${total}`} className="h-3 flex-1" />
        <span className="flex items-center gap-1 text-sm font-bold text-gold-ink tabular dark:text-gold">
          <Flame size={18} /> {run}<span className="sr-only"> correct in a row</span>
        </span>
      </div>

      <div className="flex-1 pb-6">
        {item && (
          <p className="mb-3 text-xs font-semibold text-go">
            {REASON_LABEL[item.reason] ?? 'Practice'} · {index + 1} of {total}
            {item.seen_before && (
              <span className="ml-2 rounded-full bg-surface-2 px-2 py-0.5 font-semibold text-ink-3" title="You've answered this question before. It counts toward your goal as review, not as a new result.">
                Seen before
              </span>
            )}
          </p>
        )}
        {question && <QuestionView question={question} answer={state.answer} onChoose={attempt.choose} result={state.result} skillName={catalog.skillName(question.primary_skill_key)} />}

        {!state.result && (
          <div className="mt-5 flex flex-wrap gap-2">
            <button
              onClick={() => void attempt.hint()}
              disabled={!state.attemptId || state.hintsLeft === 0}
              className="flex items-center gap-1.5 rounded-full border border-line-strong bg-surface px-3 py-1.5 text-sm font-semibold text-ink-2 hover:text-ink disabled:opacity-40"
            >
              <Lightbulb size={16} /> {state.hints.length ? 'Another hint' : 'Hint'}
            </button>
            <HelpButton icon={<Sparkle size={16} />} label="Teach me" active={help.concept} disabled={!state.attemptId} onClick={() => void askHelp('concept')} />
            <HelpButton icon={<Compass size={16} />} label="Test strategy" active={help.strategy} disabled={!state.attemptId} onClick={() => void askHelp('strategy')} />
          </div>
        )}
        {!state.result && help.concept && question && catalog.skill(question.primary_skill_key)?.concept_summary && (
          <div className="anim-rise mt-3 rounded-2xl border border-line bg-surface px-4 py-3 text-sm text-ink" role="note" aria-label="Concept">
            <div className="mb-1 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wide text-go">
              <Book size={14} /> {catalog.skillName(question.primary_skill_key)}
            </div>
            {catalog.skill(question.primary_skill_key)?.concept_summary}
          </div>
        )}
        {!state.result && help.strategy && question && catalog.strategiesFor(question.section).length > 0 && (
          <div className="anim-rise mt-3 rounded-2xl border border-line bg-surface px-4 py-3 text-sm text-ink" role="note" aria-label="Test strategies">
            <div className="mb-2 flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wide text-go">
              <Compass size={14} /> Strategies that work here
            </div>
            <ul className="grid gap-2">
              {catalog.strategiesFor(question.section).slice(0, 3).map((st) => (
                <li key={st.strategy_key}>
                  <span className="font-semibold">{st.name}.</span> <span className="text-ink-2">{st.description}</span>
                </li>
              ))}
            </ul>
            <p className="mt-2 text-xs text-ink-3">After you answer you'll see which one is fastest for this question.</p>
          </div>
        )}
        {state.hints.map((h, i) => (
          <div key={i} className="anim-rise mt-3 flex gap-2 rounded-2xl bg-gold-soft px-4 py-3 text-sm text-ink">
            <Lightbulb size={18} className="shrink-0 text-gold-ink" />
            <span>
              <span className="font-semibold">Hint {i + 1}: </span>
              {h}
            </span>
          </div>
        ))}
        {state.hintsLeft === 0 && state.hints.length > 0 && <p className="mt-2 text-xs text-ink-3">That's every hint for this one.</p>}
        {aiNote && <Notice className="mt-3">{aiNote}</Notice>}
        {state.error && <Notice tone="bad" className="mt-3">{state.error}</Notice>}

        {state.result && question && (
          <div className="mt-6">
            <Feedback
              result={state.result}
              chosen={state.answer || null}
              expectedSeconds={question.expected_time_seconds}
              remember={remember}
              strategies={catalog.strategies}
              traps={catalog.traps}
              onContinue={next}
              continueLabel={index + 1 >= total ? 'Finish' : 'Continue'}
            />
          </div>
        )}
      </div>

      {!state.result && (
        <div className="sticky bottom-0 -mx-4 border-t border-line bg-bg/95 px-4 py-4 pb-[max(1rem,env(safe-area-inset-bottom))] backdrop-blur">
          <div className="mx-auto max-w-xl">
            {state.answer ? (
              <ConfidenceBar disabled={state.busy || !state.attemptId} onPick={(c) => void onPick(c)} />
            ) : (
              <p className="py-4 text-center text-sm text-ink-3">{question && question.answer_format !== 'choice' ? 'Type your answer' : 'Choose an answer'}</p>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

function SessionSummary({ outcomes, studentId, skillName }: { outcomes: Outcome[]; studentId: string; skillName: (k: string) => string | null }) {
  const { source, ctx } = useApp()
  const tz = ctx?.myStudent?.time_zone ?? ctx?.households[0]?.time_zone ?? 'UTC'
  const week = useAsync(() => source.weeklyProgress(studentId, weekStartOf(localDate(new Date(), tz))), [source, studentId])
  const correct = outcomes.filter((o) => o.correct).length
  const time = outcomes.reduce((s, o) => s + o.elapsed_ms, 0)
  const xp = outcomes.reduce(
    (s, o) => s + xpFor({ skipped: o.correct === null, is_correct: o.correct, elapsed_ms: o.elapsed_ms, expected_time_seconds: o.expected }),
    0,
  )
  const goal = week.data?.goal?.target_questions
  const doneQs = week.data?.questions_submitted ?? 0
  // What this session worked on, per skill, and how many answers came in at test pace.
  const bySkill = [...outcomes.reduce((m, o) => (o.skill && o.correct !== null ? m.set(o.skill, [...(m.get(o.skill) ?? []), o]) : m), new Map<string, Outcome[]>())]
  const timed = outcomes.filter((o) => o.correct !== null && o.expected)
  const ratio = (o: Outcome) => o.elapsed_ms / (o.expected! * 1000)
  const onPace = timed.filter((o) => ratio(o) <= 1 && ratio(o) >= RUSHED_BELOW).length
  const rushed = timed.filter((o) => ratio(o) < RUSHED_BELOW).length
  return (
    <div className="mx-auto flex min-h-[calc(100dvh-28px)] max-w-md flex-col items-center justify-center px-4 py-10 text-center">
      <div className="anim-pop">
        <Ring value={correct} max={Math.max(1, outcomes.length)} size={168} stroke={14} label={`${correct} of ${outcomes.length} correct`}>
          <div>
            <div className="display text-5xl font-semibold tabular text-ink">
              {correct}/{outcomes.length}
            </div>
            <div className="text-xs font-semibold uppercase tracking-wide text-ink-3">correct</div>
          </div>
        </Ring>
      </div>
      <h1 className="display mt-6 text-3xl font-semibold text-ink">Session complete</h1>
      <p className="mt-1 text-ink-2">{formatDuration(time)} of focused practice.</p>
      <div className="mt-6 grid w-full grid-cols-3 gap-3">
        <SummaryTile label="XP" value={`+${xp}`} tone="gold" />
        <SummaryTile label="Streak" value={week.data ? `${week.data.streak.current}d` : '—'} tone="gold" />
        <SummaryTile label="This week" value={goal ? `${doneQs}/${goal}` : String(doneQs)} />
      </div>
      {bySkill.length > 0 && (
        <div className="mt-4 w-full rounded-2xl border border-line bg-surface p-4 text-left">
          <div className="text-xs font-semibold uppercase tracking-wide text-ink-3">What you worked on</div>
          <ul className="mt-2 grid gap-1.5 text-sm">
            {bySkill.map(([k, os]) => (
              <li key={k} className="flex items-center justify-between gap-3">
                <span className="min-w-0 truncate text-ink">{skillName(k) ?? k}</span>
                <span className="shrink-0 font-semibold tabular text-ink-2">
                  {os.filter((o) => o.correct).length}/{os.length}
                </span>
              </li>
            ))}
          </ul>
          {timed.length > 0 && (
            <p className="mt-2 text-xs text-ink-3">
              {onPace} of {timed.length} at test pace{rushed ? ` · ${rushed} too fast to count — slow down a little` : ''}. These feed your skills and indicators; benchmarks show bigger changes.
            </p>
          )}
        </div>
      )}
      {goal && doneQs >= goal && <Notice tone="gold" className="mt-4 w-full">Weekly goal reached. Anything extra this week is a bonus.</Notice>}
      {outcomes.some((o) => o.seenBefore) && (
        <p className="mt-4 w-full text-left text-sm text-ink-2">
          {outcomes.filter((o) => !o.seenBefore).length} new, {outcomes.filter((o) => o.seenBefore).length} seen before. Questions you've seen before count toward your
          goal as review; only new ones count as evidence of improvement.
        </p>
      )}
      <p className="mt-4 w-full text-left text-xs text-ink-3">
        Practice result on original Prep & Price questions, checked for answer accuracy. Not official ACT or SAT items, and not converted to a test score.
      </p>
      <div className="mt-8 grid w-full gap-3">
        <ButtonLink to="/student" size="lg" block>
          Done
        </ButtonLink>
        <Link to="/student/progress" className="text-sm font-semibold text-ink-2 hover:text-ink">
          See my progress
        </Link>
      </div>
    </div>
  )
}

function HelpButton({ icon, label, active, disabled, onClick }: { icon: React.ReactNode; label: string; active: boolean; disabled: boolean; onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      aria-pressed={active}
      className={
        'flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-sm font-semibold disabled:opacity-40 ' +
        (active ? 'border-go bg-go-soft text-ink' : 'border-line-strong bg-surface text-ink-2 hover:text-ink')
      }
    >
      {icon} {label}
    </button>
  )
}

function SummaryTile({ label, value, tone }: { label: string; value: string; tone?: 'gold' }) {
  return (
    <div className="rounded-2xl border border-line bg-surface p-3">
      <div className={tone === 'gold' ? 'text-xl font-bold tabular text-gold-ink dark:text-gold' : 'text-xl font-bold tabular text-ink'}>{value}</div>
      <div className="text-xs font-semibold uppercase tracking-wide text-ink-3">{label}</div>
    </div>
  )
}

