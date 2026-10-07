import { useEffect, useMemo, useRef, useState } from 'react'
import { Link, Navigate, useNavigate } from 'react-router-dom'
import { realName, useApp, useAsync } from '../../lib/app'
import type { ExamFamily, Student, StudentPlan, TestScore } from '../../lib/data/types'
import { browserTimeZone, localDate, weekStartOf } from '../../lib/engine/dates'
import { planBenchmark } from '../../lib/engine/benchmark'
import { contentStatus } from '../../lib/engine/freshness'
import { proposeFirstWeek } from '../../lib/engine/firstWeek'
import { checkScore } from '../../lib/engine/scoreEntry'
import { readHomeState, writeHomeState } from '../../lib/homeState'
import { clearSetupDraft, readSetupDraft, readStudentSetup, writeSetupDraft, writeStudentSetup, type ExamIntent } from '../../lib/setupProfile'
import { Button, Notice, PageLoading } from '../../components/ui'
import { StepFrame } from './Stepper'
import { AboutYou, StartingPoint, TestAndGoal, WeeklyPlanStep, type Role, type StartChoice } from './SetupScreens'
import { SetupResult } from './SetupResult'
import { gradeForGraduationYear } from './options'

/**
 * Setup in at most four short screens: about you, test and goal, starting point, weekly plan. Each question is asked
 * once: anything the account, the household or a guardian already supplied is skipped, and an invited student is
 * asked only what they may save themselves (household plans and goals belong to guardians with set-goals). Answers
 * are kept as a draft in this browser so a reload resumes where it stopped; nothing is written until the last screen.
 */
type Screen = 'about' | 'test' | 'start' | 'plan'

interface Draft {
  role: Role | null
  screen: Screen | null
  name: string
  gradYear: number | null
  homeState: string
  highSchool: string
  intent: ExamIntent | null
  primary: ExamFamily | null
  testDate: string | null | undefined
  target: string
  start: StartChoice | null
  scoreExam: ExamFamily | null
  composite: string
  sections: Record<string, string>
  scoreDate: string
  studyDays: number[]
  minutes: number | null
  weekly: number
  remind: boolean
  remindDays: number
  digest: boolean
  tz: string
  /** Records already created by an earlier, interrupted finish: never created twice. */
  created: { householdId?: string; studentId?: string; scoreSaved?: boolean }
}

const blank = (role: Role | null, name: string): Draft => ({
  role,
  screen: null,
  name,
  gradYear: null,
  homeState: '',
  highSchool: '',
  intent: null,
  primary: null,
  testDate: undefined,
  target: '',
  start: null,
  scoreExam: null,
  composite: '',
  sections: {},
  scoreDate: '',
  studyDays: [],
  minutes: null,
  weekly: 40,
  remind: false,
  remindDays: 3,
  digest: false,
  tz: browserTimeZone(),
  created: {},
})

type Mode = 'new' | 'invited' | 'self'

interface Existing {
  student: Student
  plan: StudentPlan | null
  scores: TestScore[]
  weeklyGoal: number | null
  hasBaseline: boolean
}

export function Setup({ role: routeRole }: { role?: Role }) {
  const { source, viewer, ctx, loading, refresh, setActiveStudentId } = useApp()
  const myStudent = ctx?.myStudent ?? null
  // Fixed once the flow starts: finishing creates the profile, which must not restart or redirect the flow.
  const [finishedHere, setFinishedHere] = useState(false)
  const frozen = useRef<Mode | null>(null)
  const live: Mode = myStudent ? (myStudent.household_id && !myStudent.is_independent ? 'invited' : 'self') : 'new'
  const mode: Mode = frozen.current ?? live
  const isGuardian = !!ctx?.memberships.some((m) => m.role === 'guardian')
  const existing = useAsync<Existing | null>(async () => {
    if (!myStudent) return null
    const tz = myStudent.time_zone ?? ctx?.households.find((h) => h.id === myStudent.household_id)?.time_zone ?? browserTimeZone()
    const [plan, scores, week, benchmarks] = await Promise.all([
      source.getPlan(myStudent.id),
      source.testScores(myStudent.id).catch(() => []),
      source.weeklyProgress(myStudent.id, weekStartOf(localDate(new Date(), tz))).catch(() => null),
      source.listBenchmarks(myStudent.id).catch(() => []),
    ])
    return { student: myStudent, plan, scores, weeklyGoal: week?.goal?.target_questions ?? null, hasBaseline: benchmarks.length > 0 }
  }, [source, myStudent?.id])

  if (!finishedHere && (loading || !ctx || (myStudent && existing.loading))) return <PageLoading />
  if (!viewer) return <Navigate to="/" replace />
  // A guardian who already has a household manages students from Household, not a second setup.
  if (!finishedHere && !frozen.current && !myStudent && isGuardian && !readSetupDraft(viewer.userId)) return <Navigate to="/parent" replace />
  frozen.current = mode
  return (
    <SetupFlow
      mode={mode}
      routeRole={myStudent ? 'student' : (routeRole ?? null)}
      existing={mode === 'new' ? null : (existing.data ?? null)}
      userId={viewer.userId}
      accountName={realName(viewer)}
      onFinished={async (studentId) => {
        setFinishedHere(true)
        if (mode === 'new' && studentId && routeRole !== 'student') setActiveStudentId(studentId)
        await refresh()
      }}
      source={source}
    />
  )
}

function SetupFlow(p: {
  mode: Mode
  routeRole: Role | null
  existing: Existing | null
  userId: string
  accountName: string
  onFinished: (studentId: string | null) => Promise<void>
  source: ReturnType<typeof useApp>['source']
}) {
  const { source, existing, mode } = p
  const navigate = useNavigate()
  const stored = useMemo(() => readStudentSetup(existing?.student.id), [existing?.student.id])
  const [d, setD] = useState<Draft>(() => {
    const saved = readSetupDraft<Draft>(p.userId)
    const base = blank(p.routeRole, mode === 'new' && p.routeRole === 'parent' ? '' : p.accountName)
    const merged = saved ? { ...base, ...saved, role: p.routeRole ?? saved.role } : base
    if (existing?.plan) {
      merged.primary ??= existing.plan.exam_family
      merged.minutes ??= existing.plan.daily_minutes
    }
    return merged
  })
  const [finished, setFinished] = useState<{ studentId: string; householdId: string | null } | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const [showErrors, setShowErrors] = useState(false)
  const set = (patch: Partial<Draft>) => setD((x) => ({ ...x, ...patch }))
  const today = localDate(new Date(), d.tz)

  // Who may save what: a household plan and its goals belong to guardians with set-goals.
  const canPlan = mode !== 'invited'
  const nameKnown = mode !== 'new' || (d.role === 'student' && !!p.accountName)
  const homeKnown = mode !== 'new'

  const screens: Screen[] = useMemo(() => {
    if (mode === 'new') return ['about', 'test', 'start', 'plan']
    const out: Screen[] = []
    if (mode === 'self' && existing && existing.student.graduation_year == null) out.push('about')
    if (canPlan && !existing?.plan) out.push('test')
    if (!(existing?.scores.length || stored.startingPointDone)) out.push('start')
    if (canPlan && (!existing?.plan || !stored.studyDays?.length)) out.push('plan')
    return out
  }, [mode, existing, canPlan, stored])
  const screen: Screen | null = d.screen && screens.includes(d.screen) ? d.screen : (screens[0] ?? null)
  const index = screen ? screens.indexOf(screen) : -1

  // Resume: keep the draft (never the result) in this browser after every change.
  const done = useRef(false)
  useEffect(() => {
    if (!done.current) writeSetupDraft(p.userId, { ...d, screen })
  }, [d, screen, p.userId])

  const exam: ExamFamily = d.primary ?? (d.intent === 'act' || d.intent === 'sat' ? d.intent : null) ?? existing?.plan?.exam_family ?? 'act'
  const scoreExam: ExamFamily = d.scoreExam ?? exam
  const pool = useAsync(() => source.publishedQuestions(exam), [source, exam])
  const baseline = pool.data && pool.data.length ? planBenchmark(exam, 'initial', pool.data) : null
  const secondsPerQuestion = useMemo(() => {
    const t = (pool.data ?? []).map((q) => q.expected_time_seconds).filter((x): x is number => typeof x === 'number' && x > 0)
    return t.length ? t.reduce((a, b) => a + b, 0) / t.length : null
  }, [pool.data])
  const fresh = pool.data ? contentStatus(exam, pool.data, new Set()).freshForPractice : null
  const needsBaseline = !existing?.hasBaseline
  const week = d.studyDays.length && d.minutes
    ? proposeFirstWeek({
        today,
        studyDays: d.studyDays,
        minutesPerSession: d.minutes,
        weeklyQuestions: d.weekly,
        needsBaseline,
        baseline: baseline ? { questions: baseline.totalQuestions, minutes: baseline.expectedMinutes } : null,
        secondsPerQuestion,
        freshAvailable: existing?.hasBaseline ? null : fresh,
      })
    : null

  const who = d.role === 'parent' ? d.name.trim() || 'your student' : 'you'
  const score = checkScore({ exam: scoreExam, composite: d.composite, sections: d.sections, testDate: d.scoreDate }, today)
  const target = parseTarget(d.target, exam)
  const valid: Record<Screen, boolean> = {
    about: !!d.role && (nameKnown || !!d.name.trim()) && d.gradYear !== null,
    test: !!d.intent && (d.intent === 'act' || d.intent === 'sat' || !!d.primary) && (d.intent === 'undecided' || d.testDate !== undefined) && target.ok,
    start: !!d.start && (d.start === 'none' || d.start === 'unknown' || score.ok),
    plan: d.studyDays.length > 0 && !!d.minutes,
  }

  if (finished || !screen)
    return (
      <SetupResult
        role={d.role ?? 'student'}
        name={mode === 'new' ? d.name.trim() : (existing?.student.display_name ?? d.name)}
        studentId={finished?.studentId ?? existing?.student.id ?? null}
        householdId={finished?.householdId ?? existing?.student.household_id ?? null}
        exam={exam}
        weekly={canPlan ? d.weekly : existing?.weeklyGoal ?? null}
        minutes={canPlan ? d.minutes : existing?.plan?.daily_minutes ?? null}
        studyDays={canPlan ? d.studyDays : stored.studyDays ?? []}
        target={canPlan ? target.value : existing?.plan?.target_score ?? null}
        setByGuardian={!canPlan}
        week={week}
        baseline={baseline ? { questions: baseline.totalQuestions, minutes: baseline.expectedMinutes } : null}
        needsBaseline={needsBaseline}
        onContinue={() => navigate(d.role === 'parent' ? '/parent' : '/student')}
      />
    )

  const finish = async () => {
    setBusy(true)
    setError(null)
    const created = { ...d.created }
    try {
      let sid = existing?.student.id ?? created.studentId ?? null
      let hid = existing?.student.household_id ?? created.householdId ?? null
      const grade = d.gradYear ? gradeForGraduationYear(d.gradYear) : null
      if (mode === 'new' && d.role === 'parent') {
        hid ??= created.householdId = await source.createHousehold(p.accountName ? `${p.accountName}'s household` : 'Our household', d.tz)
        sid ??= created.studentId = await source.addStudent(hid, d.name.trim(), d.gradYear, grade)
        if (d.homeState) writeHomeState(hid, d.homeState)
      } else if (mode === 'new') {
        sid ??= created.studentId = await source.createSelfStudentProfile({ displayName: d.name.trim(), graduationYear: d.gradYear, gradeLevel: grade, independent: false, timeZone: d.tz })
        if (d.homeState) writeHomeState(sid, d.homeState)
      }
      set({ created })
      if (!sid) throw new Error('No student profile to save to')
      if (canPlan && (screens.includes('test') || screens.includes('plan'))) {
        await source.savePlan(sid, {
          exam_family: exam,
          target_score: screens.includes('test') ? target.value : (existing?.plan?.target_score ?? null),
          goals: existing?.plan?.goals ?? ['raise_score'],
          daily_minutes: d.minutes ?? existing?.plan?.daily_minutes ?? 10,
        })
        if (screens.includes('plan')) await source.setWeeklyGoal(sid, weekStartOf(today), d.weekly, null)
      }
      if (screens.includes('start') && d.start === 'official' && !created.scoreSaved) {
        await source.addTestScore(sid, { exam_family: scoreExam, test_date: d.scoreDate, composite: score.composite!, section_scores: score.sections })
        created.scoreSaved = true
        set({ created })
      }
      writeStudentSetup(sid, {
        ...(screens.includes('test') ? { examIntent: d.intent ?? undefined, plannedTestDate: d.intent === 'undecided' ? null : (d.testDate ?? null) } : {}),
        ...(screens.includes('plan') ? { studyDays: [...d.studyDays].sort() } : {}),
        ...(screens.includes('about') && d.highSchool.trim() ? { highSchool: d.highSchool.trim() } : {}),
        ...(screens.includes('start')
          ? {
              startingPointDone: true,
              practiceScore: d.start === 'practice' ? { exam: scoreExam, testDate: d.scoreDate, composite: score.composite!, sections: score.sections } : (stored.practiceScore ?? null),
            }
          : {}),
      })
      if (d.role === 'parent' && (d.remind || d.digest)) {
        await source.setAlertPreference(sid, { enabled: d.remind, inactivityDays: d.remindDays, ...(source.supportsWeeklyDigest ? { weeklyDigest: d.digest } : {}) })
      }
      done.current = true
      clearSetupDraft(p.userId)
      await p.onFinished(sid)
      setFinished({ studentId: sid, householdId: hid })
    } catch (e) {
      set({ created })
      setError(e instanceof Error ? e.message : 'Could not finish setup')
    } finally {
      setBusy(false)
    }
  }

  const next = () => {
    if (!valid[screen]) {
      setShowErrors(true)
      return
    }
    setShowErrors(false)
    const after = screens[index + 1]
    if (after) set({ screen: after })
    else void finish()
  }
  const back = index > 0 ? () => set({ screen: screens[index - 1]! }) : undefined
  const last = index === screens.length - 1
  const titles: Record<Screen, string> = {
    about: mode === 'new' && !d.role ? "Let's get you set up" : 'About you',
    test: 'Test and goal',
    start: 'Starting point',
    plan: 'Weekly plan',
  }
  const examsForScore: ExamFamily[] = d.intent === 'both' ? ['act', 'sat'] : [exam]

  return (
    <StepFrame
      step={index + 1}
      total={screens.length}
      title={titles[screen]}
      subtitle={screen === 'about' && mode === 'new' ? 'Four short screens. Anything you skip can be added later.' : undefined}
      onBack={back}
      footer={
        <div className="grid gap-3">
          {error && <Notice tone="bad">{error}</Notice>}
          {showErrors && !valid[screen] && <p className="text-sm text-bad">{missingLine(screen)}</p>}
          <Button size="lg" block disabled={busy} onClick={next}>
            {busy ? 'Saving…' : last ? (screen === 'plan' ? 'Accept this plan' : 'Finish') : 'Continue'}
          </Button>
          {screen === 'about' && mode === 'new' && d.role !== 'parent' && (
            <Link to="/join" className="text-center text-sm font-semibold text-ink-2 hover:text-ink">
              I have an invite code from a parent
            </Link>
          )}
        </div>
      }
    >
      {screen === 'about' && (
        <AboutYou
          role={d.role}
          onRole={mode === 'new' && !p.routeRole ? (r) => set({ role: r, name: r === 'parent' ? '' : p.accountName }) : null}
          name={nameKnown ? null : d.name}
          onName={(v) => set({ name: v })}
          gradYear={d.gradYear}
          onGradYear={(y) => set({ gradYear: y })}
          homeState={homeKnown || readHomeState(existing?.student.household_id ?? existing?.student.id) ? null : d.homeState}
          onHomeState={(v) => set({ homeState: v })}
          highSchool={d.highSchool}
          onHighSchool={(v) => set({ highSchool: v })}
        />
      )}
      {screen === 'test' && (
        <TestAndGoal
          who={who}
          intent={d.intent}
          onIntent={(v) => set({ intent: v, primary: v === 'act' || v === 'sat' ? v : null, testDate: undefined, target: '' })}
          primary={d.intent === 'act' || d.intent === 'sat' ? d.intent : d.primary}
          onPrimary={(v) => set({ primary: v, testDate: undefined, target: '' })}
          testDate={d.testDate}
          onTestDate={(v) => set({ testDate: v })}
          target={d.target}
          onTarget={(v) => set({ target: v })}
          targetError={showErrors || d.target.length >= (exam === 'act' ? 2 : 4) ? target.error : null}
          today={today}
        />
      )}
      {screen === 'start' && (
        <StartingPoint
          who={who}
          exams={examsForScore}
          exam={scoreExam}
          onExam={(e) => set({ scoreExam: e, composite: '', sections: {} })}
          choice={d.start}
          onChoice={(c) => set({ start: c })}
          composite={d.composite}
          onComposite={(v) => set({ composite: v })}
          sections={d.sections}
          onSection={(k, v) => set({ sections: { ...d.sections, [k]: v } })}
          testDate={d.scoreDate}
          onTestDate={(v) => set({ scoreDate: v })}
          check={score}
          showErrors={showErrors}
          today={today}
        />
      )}
      {screen === 'plan' && (
        <WeeklyPlanStep
          who={who}
          studyDays={d.studyDays}
          onToggleDay={(n) => set({ studyDays: d.studyDays.includes(n) ? d.studyDays.filter((x) => x !== n) : [...d.studyDays, n] })}
          minutes={d.minutes}
          onMinutes={(m) => set({ minutes: m })}
          weekly={d.weekly}
          onWeekly={(n) => set({ weekly: n })}
          tz={d.tz}
          onTz={(tz) => set({ tz })}
          exam={exam}
          preview={week}
          reminders={
            d.role === 'parent' ? (
              <ParentReminders name={who} d={d} set={set} digest={source.supportsWeeklyDigest} demo={source.mode === 'demo'} />
            ) : null
          }
        />
      )}
    </StepFrame>
  )
}

function ParentReminders({ name, d, set, digest, demo }: { name: string; d: Draft; set: (p: Partial<Draft>) => void; digest: boolean; demo: boolean }) {
  return (
    <section aria-labelledby="q-remind">
      <h2 id="q-remind" className="mb-2 text-[15px] font-semibold text-ink">
        Updates for you (optional)
      </h2>
      <label className="flex items-start gap-3 text-sm text-ink-2">
        <input type="checkbox" className="mt-0.5 h-4 w-4 accent-[var(--go)]" checked={d.remind} onChange={(e) => set({ remind: e.target.checked })} />
        <span>
          Tell me when {name} goes{' '}
          <select
            aria-label="Days without practice"
            className="mx-1 inline-block h-8 rounded-lg border border-line-strong bg-surface px-2 align-middle text-sm text-ink"
            value={d.remindDays}
            onChange={(e) => set({ remindDays: Number(e.target.value) })}
          >
            {[2, 3, 4, 5, 7].map((n) => (
              <option key={n}>{n}</option>
            ))}
          </select>{' '}
          days without practice.
        </span>
      </label>
      {digest && (
        <label className="mt-2 flex items-start gap-3 text-sm text-ink-2">
          <input type="checkbox" className="mt-0.5 h-4 w-4 accent-[var(--go)]" checked={d.digest} onChange={(e) => set({ digest: e.target.checked })} />
          <span>Email me a summary of {name}'s week on Mondays.</span>
        </label>
      )}
      <p className="mt-1 text-xs text-ink-3">
        {demo ? 'Demo: choices are kept, but no email is sent.' : digest ? 'Emails go out only once sending is switched on; until then updates show on your dashboard.' : 'For now alerts show on your dashboard; email delivery comes later.'}
      </p>
    </section>
  )
}

function missingLine(s: Screen): string {
  return {
    about: 'Choose who is setting up, add a first name and pick a graduation year.',
    test: 'Choose a test, a test date (or "Not sure yet"), and check the goal score.',
    start: 'Choose an answer. If there is a score, check the highlighted fields.',
    plan: 'Pick at least one study day and a session length.',
  }[s]
}

function parseTarget(raw: string, exam: ExamFamily): { ok: boolean; value: number | null; error: string | null } {
  if (!raw.trim()) return { ok: true, value: null, error: null }
  const n = Number(raw)
  if (exam === 'act') return n >= 1 && n <= 36 ? { ok: true, value: n, error: null } : { ok: false, value: null, error: 'An ACT goal is 1 to 36.' }
  return n >= 400 && n <= 1600 && n % 10 === 0 ? { ok: true, value: n, error: null } : { ok: false, value: null, error: 'An SAT goal is 400 to 1600, in steps of 10.' }
}
