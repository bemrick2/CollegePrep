import type { ReactNode } from 'react'
import type { ExamFamily } from '../../lib/data/types'
import { Field, Notice, Segmented, cx, inputClass } from '../../components/ui'
import { US_STATES } from '../../lib/engine/residency'
import { daysBetween, formatShortDate } from '../../lib/engine/dates'
import { upcomingTestDates } from '../../lib/data/testDates'
import { COMPOSITE_RANGE, SECTION_FIELDS, type ScoreCheck } from '../../lib/engine/scoreEntry'
import { WEEKDAY_LABEL, type FirstWeek } from '../../lib/engine/firstWeek'
import type { ExamIntent } from '../../lib/setupProfile'
import { EXAM_NAME, LONG_SESSIONS, SHORT_SESSIONS, WEEKLY_GOALS, graduationYears, timeZones } from './options'

/** One tappable option in a grid; aria-pressed carries the state. */
export function Chip({ selected, onClick, children, className, sub, dense }: { selected: boolean; onClick: () => void; children: ReactNode; className?: string; sub?: ReactNode; dense?: boolean }) {
  return (
    <button
      type="button"
      aria-pressed={selected}
      onClick={onClick}
      className={cx(
        dense ? 'min-h-12 rounded-xl border-2 px-0 py-2 text-center text-[13px] font-semibold transition-colors sm:text-sm' : 'min-h-12 rounded-xl border-2 px-3 py-2 text-center text-[15px] font-semibold transition-colors',
        selected ? 'border-go bg-go-soft text-ink' : 'border-line bg-surface text-ink-2 hover:border-line-strong',
        className,
      )}
    >
      {children}
      {sub && <span className="block text-xs font-normal text-ink-3">{sub}</span>}
    </button>
  )
}

function Question({ id, children, hint }: { id: string; children: ReactNode; hint?: ReactNode }) {
  return (
    <div className="mb-2">
      <h2 id={id} className="text-[15px] font-semibold text-ink">
        {children}
      </h2>
      {hint && <p className="mt-0.5 text-sm text-ink-3">{hint}</p>}
    </div>
  )
}

export type Role = 'parent' | 'student'

// ---------------------------------------------------------------------------------------------------------------
// 1. About you
// ---------------------------------------------------------------------------------------------------------------

export function AboutYou(p: {
  role: Role | null
  onRole: ((r: Role) => void) | null
  /** null: the name is already known from the account and isn't asked. */
  name: string | null
  onName: (v: string) => void
  gradYear: number | null
  onGradYear: (y: number) => void
  homeState: string | null
  onHomeState: (v: string) => void
}) {
  const parentView = p.role === 'parent'
  return (
    <div className="grid gap-7">
      {p.onRole && (
        <section aria-labelledby="q-role">
          <Question id="q-role">Who's setting up?</Question>
          <div className="grid grid-cols-2 gap-2">
            <Chip selected={p.role === 'student'} onClick={() => p.onRole!('student')}>
              I'm a student
            </Chip>
            <Chip selected={p.role === 'parent'} onClick={() => p.onRole!('parent')}>
              I'm a parent or guardian
            </Chip>
          </div>
        </section>
      )}
      {p.role && (
        <>
          {p.name !== null && (
            <Field label={p.role === 'parent' ? "Your student's first name" : 'Your first name'} htmlFor="setup-name">
              <input id="setup-name" className={inputClass} value={p.name} onChange={(e) => p.onName(e.target.value)} autoComplete={p.role === 'parent' ? 'off' : 'given-name'} />
            </Field>
          )}
          <section aria-labelledby="q-grad">
            <Question id="q-grad" hint="We store the graduation year and grade, never a date of birth.">
              {parentView ? 'What year does your student graduate?' : 'What year do you graduate?'}
            </Question>
            <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
              {graduationYears().map((y) => (
                <Chip key={y} selected={p.gradYear === y} onClick={() => p.onGradYear(y)}>
                  Class of {y}
                </Chip>
              ))}
            </div>
          </section>
          {p.homeState !== null && (
            <Field label="Home state (optional)" htmlFor="setup-state" hint="Picks in-state or out-of-state college prices. Change it any time.">
              <select id="setup-state" className={inputClass} value={p.homeState} onChange={(e) => p.onHomeState(e.target.value)}>
                <option value="">Prefer not to say</option>
                {US_STATES.map(([c, n]) => (
                  <option key={c} value={c}>
                    {n}
                  </option>
                ))}
              </select>
            </Field>
          )}
        </>
      )}
    </div>
  )
}

// ---------------------------------------------------------------------------------------------------------------
// 2. Test and goal
// ---------------------------------------------------------------------------------------------------------------

export function TestAndGoal(p: {
  who: string
  intent: ExamIntent | null
  onIntent: (v: ExamIntent) => void
  primary: ExamFamily | null
  onPrimary: (v: ExamFamily) => void
  /** undefined: not answered; null: "not sure yet". */
  testDate: string | null | undefined
  onTestDate: (v: string | null) => void
  target: string
  onTarget: (v: string) => void
  targetError: string | null
  today: string
}) {
  const exam = p.primary
  const dates = exam ? upcomingTestDates(exam, p.today) : []
  return (
    <div className="grid gap-7">
      <section aria-labelledby="q-test">
        <Question id="q-test">{p.who === 'you' ? 'Which test are you taking?' : `Which test is ${p.who} taking?`}</Question>
        <div className="grid grid-cols-2 gap-2">
          <Chip selected={p.intent === 'act'} onClick={() => p.onIntent('act')} sub="Scored 1–36">
            ACT
          </Chip>
          <Chip selected={p.intent === 'sat'} onClick={() => p.onIntent('sat')} sub="Scored 400–1600">
            SAT
          </Chip>
          <Chip selected={p.intent === 'both'} onClick={() => p.onIntent('both')}>
            Both
          </Chip>
          <Chip selected={p.intent === 'undecided'} onClick={() => p.onIntent('undecided')}>
            Not sure yet
          </Chip>
        </div>
      </section>

      {(p.intent === 'both' || p.intent === 'undecided') && (
        <section aria-labelledby="q-primary">
          <Question id="q-primary" hint={p.intent === 'undecided' ? 'Practice needs one test to start. Switching later keeps your history.' : 'Practice and progress checks follow this one. You can switch any time.'}>
            {p.intent === 'both' ? 'Which one comes first?' : 'Which should practice start with?'}
          </Question>
          <div className="grid grid-cols-2 gap-2">
            {(['act', 'sat'] as ExamFamily[]).map((e) => (
              <Chip key={e} selected={p.primary === e} onClick={() => p.onPrimary(e)}>
                {EXAM_NAME[e]}
              </Chip>
            ))}
          </div>
        </section>
      )}

      {exam && p.intent !== 'undecided' && (
        <section aria-labelledby="q-date">
          <Question id="q-date" hint="National dates as published by the test maker.">
            When is the {EXAM_NAME[exam]}?
          </Question>
          <div className="grid grid-cols-2 gap-2">
            {dates.slice(0, 8).map((d) => (
              <Chip key={d.date} selected={p.testDate === d.date} onClick={() => p.onTestDate(d.date)} sub={d.projected ? 'Projected' : undefined}>
                {new Date(`${d.date}T12:00:00Z`).toLocaleDateString(undefined, { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' })}
              </Chip>
            ))}
            <Chip className="col-span-2" selected={p.testDate === null} onClick={() => p.onTestDate(null)}>
              Not sure yet
            </Chip>
          </div>
          {p.testDate && (
            <p className="mt-2 text-sm text-ink-2">
              That's {daysBetween(p.today, p.testDate)} days away.{' '}
              {dates.find((d) => d.date === p.testDate)?.projected && 'The test maker lists it as projected, so it may move.'}
            </p>
          )}
        </section>
      )}

      {exam && (
        <section aria-labelledby="q-target">
          <Question id="q-target" hint="Optional. It's a goal to aim for, not a prediction. Leave it blank if you're not sure.">
            Goal score
          </Question>
          <div className="flex items-center gap-3">
            <input
              aria-labelledby="q-target"
              inputMode="numeric"
              className={cx(inputClass.replace('w-full', 'w-32'), 'text-center text-xl font-semibold tabular')}
              value={p.target}
              onChange={(e) => p.onTarget(e.target.value.replace(/[^\d]/g, '').slice(0, 4))}
              placeholder="—"
            />
            <span className="text-sm text-ink-3 tabular">
              {COMPOSITE_RANGE[exam].min}–{COMPOSITE_RANGE[exam].max}
              {exam === 'sat' ? ', in steps of 10' : ''}
            </span>
          </div>
          {p.targetError && <p className="mt-1 text-sm text-bad">{p.targetError}</p>}
        </section>
      )}
    </div>
  )
}

// ---------------------------------------------------------------------------------------------------------------
// 3. Starting point
// ---------------------------------------------------------------------------------------------------------------

export type StartChoice = 'official' | 'practice' | 'none' | 'unknown'

export function StartingPoint(p: {
  who: string
  exams: ExamFamily[]
  exam: ExamFamily
  onExam: (e: ExamFamily) => void
  choice: StartChoice | null
  onChoice: (c: StartChoice) => void
  composite: string
  onComposite: (v: string) => void
  sections: Record<string, string>
  onSection: (k: string, v: string) => void
  testDate: string
  onTestDate: (v: string) => void
  check: ScoreCheck | null
  showErrors: boolean
  today: string
}) {
  const you = p.who === 'you'
  const scored = p.choice === 'official' || p.choice === 'practice'
  const err = (k: string) => (p.showErrors ? (p.check?.errors[k] ?? null) : null)
  return (
    <div className="grid gap-7">
      <section aria-labelledby="q-start">
        <Question id="q-start" hint="Only a score from a score report or a full, timed practice test. Please don't guess: the starting benchmark measures where you are.">
          {you ? 'Have you taken a full test before?' : `Has ${p.who} taken a full test before?`}
        </Question>
        <div className="grid gap-2">
          <Chip selected={p.choice === 'official'} onClick={() => p.onChoice('official')} className="text-left">
            Yes, an official test
          </Chip>
          <Chip selected={p.choice === 'practice'} onClick={() => p.onChoice('practice')} className="text-left">
            Yes, a full practice test
          </Chip>
          <div className="grid grid-cols-2 gap-2">
            <Chip selected={p.choice === 'none'} onClick={() => p.onChoice('none')}>
              Not yet
            </Chip>
            <Chip selected={p.choice === 'unknown'} onClick={() => p.onChoice('unknown')}>
              Don't remember the score
            </Chip>
          </div>
        </div>
        {(p.choice === 'none' || p.choice === 'unknown') && (
          <p className="mt-2 text-sm text-ink-2">That's fine. No score is saved, and the starting benchmark shows where {you ? 'you are' : 'they are'}.</p>
        )}
      </section>

      {scored && (
        <section aria-labelledby="q-score" className="grid gap-5">
          {p.exams.length > 1 && (
            <Segmented label="Which test" value={p.exam} onChange={p.onExam} options={p.exams.map((e) => ({ value: e, label: EXAM_NAME[e] }))} />
          )}
          <Field label={`${EXAM_NAME[p.exam]} ${COMPOSITE_RANGE[p.exam].label}`} htmlFor="setup-composite" error={err('composite')}>
            <input id="setup-composite" inputMode="numeric" className={cx(inputClass, 'text-xl font-semibold tabular')} value={p.composite} onChange={(e) => p.onComposite(e.target.value.replace(/[^\d]/g, '').slice(0, 4))} />
          </Field>
          <details className="group rounded-xl border border-line bg-surface p-3">
            <summary className="cursor-pointer text-sm font-semibold text-ink">Section scores (optional)</summary>
            <div className="mt-3 grid grid-cols-2 gap-3">
              {SECTION_FIELDS[p.exam].map((f) => (
                <Field key={f.key} label={f.label} htmlFor={`setup-sec-${f.key}`} error={err(f.key)}>
                  <input id={`setup-sec-${f.key}`} inputMode="numeric" className={cx(inputClass, 'tabular')} value={p.sections[f.key] ?? ''} onChange={(e) => p.onSection(f.key, e.target.value.replace(/[^\d]/g, '').slice(0, 3))} />
                </Field>
              ))}
            </div>
            {p.exam === 'act' && <p className="mt-2 text-xs text-ink-3">Leave Science blank if it wasn't taken.</p>}
          </details>
          <Field label="Test date" htmlFor="setup-score-date" hint={p.choice === 'official' ? 'From the score report.' : 'When the practice test was taken.'} error={err('testDate')}>
            <input id="setup-score-date" type="date" max={p.today} className={inputClass} value={p.testDate} onChange={(e) => p.onTestDate(e.target.value)} />
          </Field>
          <p className="text-xs text-ink-3">
            {p.choice === 'official'
              ? 'Saved as self-reported: we show it as unverified until an official score report is linked.'
              : 'Practice-test scores are kept separately and never used for scholarship comparisons.'}
          </p>
        </section>
      )}
    </div>
  )
}

// ---------------------------------------------------------------------------------------------------------------
// 4. Weekly plan
// ---------------------------------------------------------------------------------------------------------------

export function WeeklyPlanStep(p: {
  who: string
  studyDays: number[]
  onToggleDay: (d: number) => void
  minutes: number | null
  onMinutes: (m: number) => void
  weekly: number
  onWeekly: (n: number) => void
  tz: string
  onTz: (tz: string) => void
  reminders: ReactNode
  preview: FirstWeek | null
  exam: ExamFamily
  /** 20 and 30 minutes, where the backend stores them (CR-26). */
  longSessions: boolean
}) {
  const you = p.who === 'you'
  const w = p.preview
  return (
    <div className="grid gap-7">
      <section aria-labelledby="q-days">
        <Question id="q-days" hint="Pick the days that are realistic most weeks.">
          {you ? 'Which days can you study?' : `Which days can ${p.who} study?`}
        </Question>
        <div className="grid grid-cols-7 gap-1">
          {WEEKDAY_LABEL.map((l, i) => (
            <Chip key={l} selected={p.studyDays.includes(i + 1)} onClick={() => p.onToggleDay(i + 1)} dense>
              {l}
            </Chip>
          ))}
        </div>
      </section>
      <section aria-labelledby="q-min">
        <Question id="q-min" hint="Short sessions are the easiest to keep up. You can always do a bonus round.">
          Minutes per session
        </Question>
        <div className="grid grid-cols-3 gap-2">
          {SHORT_SESSIONS.map((m) => (
            <Chip key={m} selected={p.minutes === m} onClick={() => p.onMinutes(m)} sub={m === 10 ? 'Most students' : undefined}>
              {m} min
            </Chip>
          ))}
        </div>
        {p.longSessions && (
          <div className="mt-2 flex flex-wrap items-center gap-2 text-sm text-ink-3">
            <span>Longer:</span>
            {LONG_SESSIONS.map((m) => (
              <button
                key={m}
                type="button"
                aria-pressed={p.minutes === m}
                onClick={() => p.onMinutes(m)}
                className={cx('h-9 rounded-lg border px-3 font-semibold', p.minutes === m ? 'border-go bg-go-soft text-ink' : 'border-line bg-surface text-ink-2')}
              >
                {m} min
              </button>
            ))}
          </div>
        )}
      </section>
      <section aria-labelledby="q-weekly">
        <Question id="q-weekly" hint="Counted Monday to Sunday. Benchmark answers count too.">
          Weekly question goal
        </Question>
        <div className="grid grid-cols-3 gap-2">
          {WEEKLY_GOALS.map((g) => (
            <Chip key={g.value} selected={p.weekly === g.value} onClick={() => p.onWeekly(g.value)}>
              {g.label}
            </Chip>
          ))}
        </div>
        {w?.shortOfTime && (
          <Notice tone="warn" className="mt-3">
            {p.weekly} {p.exam.toUpperCase()} questions usually take about {w.minutesNeeded} minutes. These days and sessions add up to {w.minutesCommitted}. Add a day, choose
            longer sessions, or pick a smaller goal.
          </Notice>
        )}
        {w?.freshShort && (
          <Notice tone="warn" className="mt-3">
            There aren't {p.weekly} new {p.exam.toUpperCase()} practice questions yet. After the new ones run out, practice repeats questions as review, and the app says so.
          </Notice>
        )}
      </section>
      {p.reminders}
      <details className="text-sm text-ink-2">
        <summary className="cursor-pointer">
          Weeks follow <span className="font-semibold text-ink">{p.tz}</span>
        </summary>
        <select aria-label="Time zone" className={cx(inputClass, 'mt-2')} value={p.tz} onChange={(e) => p.onTz(e.target.value)}>
          {timeZones().map((z) => (
            <option key={z}>{z}</option>
          ))}
        </select>
      </details>
      {w && p.studyDays.length > 0 && p.minutes && <WeekPreview week={w} />}
    </div>
  )
}

export function WeekPreview({ week }: { week: FirstWeek }) {
  return (
    <section aria-labelledby="q-preview" className="rounded-2xl border border-line bg-surface">
      <h2 id="q-preview" className="border-b border-line px-4 py-3 text-[15px] font-semibold text-ink">
        Proposed first week
        <span className="block text-xs font-normal text-ink-3">
          Through Sunday, {formatShortDate(week.weekEnd)}. Then {week.fullWeekPerDay} questions per study day.
        </span>
      </h2>
      <ol className="divide-y divide-line">
        {week.days.map((d) => (
          <li key={d.date} className="flex gap-4 px-4 py-3">
            <div className="w-12 shrink-0 text-center">
              <div className="text-xs text-ink-3">{d.label}</div>
              <div className={cx('text-lg font-semibold tabular', d.isToday ? 'text-go-strong dark:text-go' : 'text-ink')}>{Number(d.date.slice(8))}</div>
            </div>
            <div className="min-w-0 flex-1 text-sm">
              {d.check && (
                <p className="font-semibold text-ink">
                  Starting benchmark
                  <span className="block font-normal text-ink-3">
                    {d.check.questions} questions · about {d.check.minutes} min
                  </span>
                </p>
              )}
              {d.questions > 0 && (
                <p className={cx(d.check && 'mt-2', 'font-semibold text-ink')}>
                  Practice
                  <span className="block font-normal text-ink-3">
                    {d.questions} questions{d.overSession ? ' · longer than one session' : ''}
                  </span>
                </p>
              )}
              {!d.check && d.questions === 0 && <p className="text-ink-3">{d.study ? 'Nothing planned' : 'Rest day'}</p>}
            </div>
          </li>
        ))}
      </ol>
      {week.partialWeek && (
        <p className="border-t border-line px-4 py-3 text-xs text-ink-3">
          This week is already under way, so the days left may not reach the full goal. That's expected. The plan settles in from Monday.
        </p>
      )}
    </section>
  )
}
