import { Link, Navigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import type { SkillEstimate, Student } from '../../lib/data/types'
import { ButtonLink, Card, CardHeader, EmptyState, Notice, PageLoading, Pill, ProgressBar, cx } from '../../components/ui'
import { ArrowRight, Compass, Flame, Info, Target, Users } from '../../components/icons'
import { latestEstimate, recentTrend, useStudentOverview, type StudentOverview } from '../student/useStudentOverview'
import { SECTION_LABEL, SECTION_ORDER, benchmarkSchedule, pacingVerdict } from '../../lib/engine/benchmark'
import { daysBetween, formatShortDate, isoWeekday } from '../../lib/engine/dates'
import { EXAM_NAME } from '../onboarding/options'
import { useCatalog } from '../practice/useCatalog'
import { CostOutlook, outlookFor } from './CostOutlook'
import { PrimaryTarget } from './PrimaryTarget'
import { useInterests } from '../majors/useInterests'
import { meritAwards } from '../../lib/engine/merit'
import { useSavedComparison } from '../colleges/useSavedComparison'
import { parentActions, type ParentAction } from '../../lib/engine/actions'
import { PracticeIndicators } from '../../components/PracticeIndicators'
import { BenchmarkStatus } from '../../components/BenchmarkStatus'


export function ParentDashboard() {
  const { ctx, activeStudent } = useApp()
  if (!ctx) return <PageLoading />
  if (ctx.students.length === 0)
    return (
      <Card>
        <EmptyState icon={<Users size={32} />} title="Add your first student" action={<ButtonLink to="/onboarding/parent">Set up household</ButtonLink>}>
          Your dashboard fills in once a student is added and starts practising.
        </EmptyState>
      </Card>
    )
  if (!activeStudent) return <Navigate to="/parent" replace />
  return <StudentPanel student={activeStudent} />
}

function StudentPanel({ student }: { student: Student }) {
  const o = useStudentOverview(student.id)
  if (o.loading && !o.data) return <PageLoading />
  if (o.error) return <Notice tone="bad" title="Couldn't load progress">{o.error.message}</Notice>
  if (!o.data) return null
  return <Panel student={student} o={o.data} />
}

type Action = ParentAction

function sectionRollup(estimates: SkillEstimate[]) {
  const m = new Map<string, { n: number; c: number; paces: number[]; flagged: boolean }>()
  for (const e of estimates) {
    const r = m.get(e.section) ?? { n: 0, c: 0, paces: [], flagged: false }
    r.n += e.attempts
    r.c += e.correct
    if (e.pacing_ratio !== null) r.paces.push(e.pacing_ratio)
    r.flagged ||= e.knowledge_weak !== null
    m.set(e.section, r)
  }
  return m
}

function Panel({ student, o }: { student: Student; o: StudentOverview }) {
  const exam = o.plan?.exam_family ?? 'act'
  const interestCount = useInterests(student.id).profile.interests.length
  const catalog = useCatalog(exam)
  const est = latestEstimate(o.scores, exam)[0]
  const goal = o.week.goal?.target_questions ?? null
  const trend = recentTrend(o.history, o.today, o.tz)
  const rollup = sectionRollup(o.estimates)
  const lastDay = o.streak.last_practice_day
  const idleDays = lastDay ? daysBetween(lastDay, o.today) : null
  const linked = !!student.linked_user_id
  const name = student.display_name

  // Expected pace through the week: weekday/7 of the goal.
  const dayOfWeek = isoWeekday(o.today)
  const expectedByNow = goal ? Math.round((goal * dayOfWeek) / 7) : null
  const behind = goal !== null && expectedByNow !== null && o.week.questions_submitted < expectedByNow * 0.8

  const saved = useSavedComparison()
  const weakSkill = (kind: 'knowledge' | 'pacing') =>
    [...o.estimates]
      .filter((e) => (kind === 'knowledge' ? e.knowledge_weak : e.pacing_weak))
      .sort((a, b) => (kind === 'knowledge' ? (a.accuracy ?? 1) - (b.accuracy ?? 1) : (b.pacing_ratio ?? 0) - (a.pacing_ratio ?? 0)))[0]
  const focus = (['knowledge', 'pacing'] as const).flatMap((kind) => {
    const e = weakSkill(kind)
    if (!e) return []
    const skill = catalog.skillName(e.skill_key) ?? e.skill_key
    return [{
      section: e.section,
      label: SECTION_LABEL[e.section] ?? e.section,
      kind,
      detail: kind === 'knowledge' ? `${skill}: ${Math.round((e.accuracy ?? 0) * 100)}% right over ${e.attempts} questions. Daily sessions already lead with it.` : `${skill}: about ${(e.pacing_ratio ?? 0).toFixed(1)}× test pace. Sessions now include timed work.`,
    }]
  })
  const official = [...o.scores].filter((x) => x.exam_family === exam && x.composite !== null && x.score_source !== 'practice_estimate').sort((a, b) => b.test_date.localeCompare(a.test_date))[0]
  const actions = parentActions({
    interestsSaved: interestCount,
    name,
    exam,
    linked,
    benchmarks: o.benchmarks.length,
    schedule: benchmarkSchedule(o.benchmarks),
    focus,
    behind: behind && goal !== null && expectedByNow !== null ? { done: o.week.questions_submitted, goal, expected: expectedByNow } : null,
    idleDays,
    goals: o.plan?.goals ?? [],
    targetScore: o.plan?.target_score ?? null,
    officialScore: official ? { composite: official.composite!, selfReported: official.score_source === 'self_reported' } : null,
    schools: (saved.data ?? []).filter((c) => c.found).map((c) => ({
      name: c.institution?.display_name ?? c.institution_key,
      levers: outlookFor(c).levers,
      awards: meritAwards(c.domains.awards).map((a) => ({ name: a.name, act_min: a.min.act, sat_min: a.min.sat })),
    })),
  })

  return (
    <div className="grid grid-cols-1 gap-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">Overview</p>
          <h1 className="display text-[30px] font-semibold leading-tight text-ink md:text-[36px]">How {name} is doing</h1>
        </div>
        <div className="flex gap-2">
          <Link to="/parent/goals" className="rounded-lg border border-line-strong bg-surface px-3 py-2 text-sm font-semibold text-ink hover:bg-surface-2">
            Edit goals
          </Link>
          <Link to="/parent/progress" className="rounded-lg bg-brand px-3 py-2 text-sm font-semibold text-brand-ink hover:bg-brand-2">
            Full progress
          </Link>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
        {official ? (
          <Kpi
            label={`${official.score_source === 'official' ? 'Official' : 'Self-reported'} ${EXAM_NAME[exam]}`}
            value={String(official.composite)}
            sub={`${formatShortDate(official.test_date)} · target ${o.plan?.target_score ?? '—'}`}
            icon={<Target size={18} />}
          />
        ) : (
          <Kpi
            label={`Target ${EXAM_NAME[exam]}`}
            value={o.plan?.target_score != null ? String(o.plan.target_score) : '—'}
            sub={est ? `Practice estimate ${est.composite}` : 'No score estimate yet (not calibrated)'}
            icon={<Target size={18} />}
          />
        )}
        <Kpi label="Weekly goal" value={goal ? `${o.week.questions_submitted}/${goal}` : String(o.week.questions_submitted)} sub={goal ? `questions · ${Math.round((100 * o.week.questions_submitted) / goal)}% done` : 'questions · no goal set'} icon={<Compass size={18} />} bar={goal ? o.week.questions_submitted / goal : undefined} />
        <Kpi label="Streak" value={`${o.streak.current_streak} days`} sub={`Longest ${o.streak.longest_streak}`} icon={<Flame size={18} />} />
        <Kpi
          label="Accuracy, 7 days"
          value={trend.recent.acc === null ? '—' : `${Math.round(trend.recent.acc * 100)}%`}
          sub={trend.prior.acc === null || trend.recent.acc === null ? `${trend.recent.n} answered` : `${trend.recent.acc >= trend.prior.acc ? '▲' : '▼'} from ${Math.round(trend.prior.acc * 100)}%`}
          icon={<Info size={18} />}
        />
      </div>


      <div className="grid grid-cols-1 gap-5 lg:grid-cols-[1.25fr_1fr]">
        <Card>
          <CardHeader title="What to do next" subtitle="Based on recorded practice and verified college records." />
          <ol className="grid gap-2 p-5 pt-3">
            {actions.slice(0, 6).map((a, i) => (
              <li key={a.key}>
                <ActionRow a={a} n={i + 1} />
              </li>
            ))}
          </ol>
        </Card>

        <Card>
          <CardHeader title="By section" subtitle="Knowledge and pacing, from recent practice" />
          <ul className="grid gap-3 p-5 pt-3">
            {SECTION_ORDER[exam].map((sec) => {
              const r = rollup.get(sec)
              const acc = r && r.n ? r.c / r.n : null
              const pace = r?.paces.length ? r.paces.reduce((a, b) => a + b, 0) / r.paces.length : null
              const pv = pacingVerdict(pace)
              return (
                <li key={sec} className="grid gap-1.5">
                  <div className="flex items-center justify-between gap-2 text-sm">
                    <span className="font-semibold text-ink">{SECTION_LABEL[sec]}</span>
                    <span className="flex items-center gap-1.5">
                      {acc === null || (r && r.n < 5) ? (
                        <Pill>Not enough data</Pill>
                      ) : (
                        <>
                          <Pill tone={acc >= 0.75 ? 'go' : acc >= 0.6 ? 'brand' : 'warn'}>{acc >= 0.75 ? 'Strong' : acc >= 0.6 ? 'Developing' : 'Needs work'}</Pill>
                          {pv === 'slow' && <Pill tone="warn">Pacing</Pill>}
                        </>
                      )}
                    </span>
                  </div>
                  <ProgressBar value={acc ?? 0} label={`${SECTION_LABEL[sec]} accuracy`} tone={acc !== null && acc < 0.6 ? 'warn' : 'brand'} className="h-2" />
                </li>
              )
            })}
          </ul>
          {o.estimates.filter((e) => e.knowledge_weak).length > 0 && (
            <div className="border-t border-line px-5 py-3 text-xs text-ink-3">
              Weakest skills: {o.estimates.filter((e) => e.knowledge_weak).map((e) => catalog.skillName(e.skill_key)).join(', ')}
            </div>
          )}
        </Card>
      </div>

      <PrimaryTarget student={student} />

      <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
        <PracticeIndicators history={o.history} who={name} />
        <BenchmarkStatus history={o.benchmarks} forGuardian />
      </div>

      <CostOutlook showAlternative={!!o.plan?.goals.includes('lower_cost')} />

      <p className="text-xs text-ink-3">
        Last practice: {lastDay ? formatShortDate(lastDay) : 'never'} · Time zone {o.tz}
      </p>
    </div>
  )
}

function Kpi({ label, value, sub, icon, bar }: { label: string; value: string; sub: string; icon: React.ReactNode; bar?: number }) {
  return (
    <Card className="p-4">
      <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wide text-ink-3">
        <span className="text-brand">{icon}</span>
        {label}
      </div>
      <div className="display mt-2 text-[32px] font-semibold leading-none tabular text-ink">{value}</div>
      {bar !== undefined && <ProgressBar value={bar} label={label} tone="brand" className="mt-3 h-1.5" />}
      <div className="mt-2 text-xs text-ink-3">{sub}</div>
    </Card>
  )
}

function ActionRow({ a, n }: { a: Action; n: number }) {
  const dot = { go: 'bg-go', warn: 'bg-warn', info: 'bg-info', brand: 'bg-brand' }[a.tone]
  const body = (
    <div className="flex items-start gap-3 rounded-xl px-3 py-3 transition-colors hover:bg-surface-2">
      <span className={cx('mt-1.5 h-2 w-2 shrink-0 rounded-full', dot)} aria-hidden />
      <span className="min-w-0 flex-1">
        <span className="block text-sm font-semibold text-ink">
          <span className="sr-only">{n}. </span>
          {a.title}
        </span>
        <span className="block text-sm text-ink-3">{a.detail}</span>
      </span>
      {a.to && <ArrowRight size={18} className="mt-0.5 shrink-0 text-ink-3" />}
    </div>
  )
  return a.to ? <Link to={a.to}>{body}</Link> : body
}

