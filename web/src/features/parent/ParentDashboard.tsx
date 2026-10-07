import { useState } from 'react'
import { Link, Navigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import type { SkillEstimate, Student } from '../../lib/data/types'
import { ButtonLink, Card, EmptyState, Notice, PageLoading, Pill, ProgressBar } from '../../components/ui'
import { Users } from '../../components/icons'
import { latestEstimate, recentTrend, useStudentOverview, type StudentOverview } from '../student/useStudentOverview'
import { SECTION_LABEL, SECTION_ORDER, benchmarkSchedule, pacingVerdict } from '../../lib/engine/benchmark'
import { addDays, daysBetween, formatShortDate, isoWeekday } from '../../lib/engine/dates'
import { EXAM_NAME } from '../onboarding/options'
import { useCatalog } from '../practice/useCatalog'
import { costPhrase, outlookFor } from './CostOutlook'
import { WeeklyUpdate } from './WeeklyUpdate'
import { GuardianReminderStatus, ReminderSettingsPanel } from '../reminders/Reminders'
import { showRecap, weekRecap, weeklyPlan } from '../../lib/engine/weeklyPlan'
import { Figure, NextSteps, PageHeader, Row, RowList, Section, compactUsd } from '../../components/layout'
import { planSummary, type PlanSummary } from '../../lib/engine/planSummary'
import { schoolLevers } from '../colleges/schoolLevers'
import { useExamPlan } from '../colleges/useExamPlan'
import { useMeritReference } from '../colleges/useMeritReference'
import { useInterests } from '../majors/useInterests'
import { useHomeState } from '../../lib/homeState'
import { labelOf } from '../../lib/engine/interests'
import { meritAwards } from '../../lib/engine/merit'
import { useSavedComparison } from '../colleges/useSavedComparison'
import { parentActions } from '../../lib/engine/actions'

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
  if (o.error)
    return (
      <Notice tone="bad" title="Couldn't load progress">
        {o.error.message}
      </Notice>
    )
  if (!o.data) return null
  return <Panel student={student} o={o.data} onRefresh={o.reload} />
}

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

function Panel({ student, o, onRefresh }: { student: Student; o: StudentOverview; onRefresh: () => void }) {
  const { ctx, source } = useApp()
  const exam = o.plan?.exam_family ?? 'act'
  const interestCount = useInterests(student.id).profile.interests.length
  const { homeState } = useHomeState()
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
  const exams = useExamPlan(student.id).exams
  const merit = useMeritReference(student.id)
  const [showAll, setShowAll] = useState(false)
  const weakSkill = (kind: 'knowledge' | 'pacing') =>
    [...o.estimates]
      .filter((e) => (kind === 'knowledge' ? e.knowledge_weak : e.pacing_weak))
      .sort((a, b) => (kind === 'knowledge' ? (a.accuracy ?? 1) - (b.accuracy ?? 1) : (b.pacing_ratio ?? 0) - (a.pacing_ratio ?? 0)))[0]
  const focus = (['knowledge', 'pacing'] as const).flatMap((kind) => {
    const e = weakSkill(kind)
    if (!e) return []
    const skill = catalog.skillName(e.skill_key) ?? e.skill_key
    return [
      {
        section: e.section,
        label: SECTION_LABEL[e.section] ?? e.section,
        kind,
        detail:
          kind === 'knowledge'
            ? `${skill}: ${Math.round((e.accuracy ?? 0) * 100)}% right over ${e.attempts} questions. Daily sessions already lead with it.`
            : `${skill}: about ${(e.pacing_ratio ?? 0).toFixed(1)}× test pace. Sessions now include timed work.`,
      },
    ]
  })
  const official = [...o.scores]
    .filter((x) => x.exam_family === exam && x.composite !== null && (x.score_source === 'official' || x.score_source === 'self_reported'))
    .sort((a, b) => b.test_date.localeCompare(a.test_date))[0]
  const actions = parentActions({
    interestsSaved: interestCount,
    homeStateKnown: !!homeState,
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
    schools: (saved.data ?? [])
      .filter((c) => c.found)
      .map((c) => ({
        name: c.institution?.display_name ?? c.institution_key,
        levers: outlookFor(c).levers,
        awards: meritAwards(c.domains.awards).map((a) => ({ name: a.name, act_min: a.min.act, sat_min: a.min.sat })),
      })),
  })

  // The plan: one headline cost, one opportunity, three next steps.
  const schools = (saved.data ?? []).filter((c) => c.found)
  const rows = schools.map((c) => ({ c, o: outlookFor(c, homeState) }))
  const plan = planSummary(
    rows.map(({ c, o }) => ({
      key: c.institution_key,
      name: o.name,
      level: o.level,
      total: o.degreeTotal,
      comparable: o.comparable,
      levers: schoolLevers(c, exams, exam, merit.reference),
    })),
    saved.primary,
  )

  return (
    <div className="grid grid-cols-1 gap-10">
      <PageHeader
        title={`${name}'s college plan`}
        actions={
          <Link to="/parent/goals" className="rounded-lg border border-line-strong bg-surface px-3 py-2 text-sm font-semibold text-ink hover:bg-surface-2">
            Edit goals
          </Link>
        }
      />

      <div className="grid gap-10 lg:grid-cols-[minmax(0,1.35fr)_minmax(0,1fr)] lg:gap-14">
        <div className="grid content-start gap-8">
          <PlanHeadline plan={plan} residency={rows.find((r) => r.o.key === plan.headline?.key)?.o.residency ?? null} schoolsSaved={schools.length} canChooseTop={saved.canSetPrimary && !saved.primary && schools.length > 1} />
          {plan.opportunity && (
            <div className="border-l-4 border-brand pl-4">
              <h2 className="text-sm font-bold text-brand">Biggest opportunity</h2>
              <p className="mt-1 text-lg font-semibold leading-snug text-ink">
                {plan.opportunity.lever.title} at {plan.opportunity.school}
              </p>
              <p className="mt-1 text-sm text-ink-2">{plan.opportunity.lever.detail}</p>
              <Link to="/colleges/paths" className="mt-2 inline-block text-sm font-semibold text-brand hover:underline">
                See every way to lower the cost
              </Link>
            </div>
          )}
        </div>

        <section aria-labelledby="next-heading">
          <h2 id="next-heading" className="text-[17px] font-bold text-ink">
            What to do next
          </h2>
          <p className="mt-0.5 text-sm text-ink-3">From recorded practice and verified college records.</p>
          <div className="mt-3">
            <NextSteps items={(showAll ? actions : actions.slice(0, 3)).map((a) => ({ key: a.key, title: a.title, detail: a.detail, to: a.to }))} />
          </div>
          {actions.length > 3 && (
            <button type="button" onClick={() => setShowAll((v) => !v)} className="mt-1 text-sm font-semibold text-brand hover:underline">
              {showAll ? 'Show fewer' : `Show ${actions.length - 3} more`}
            </button>
          )}
        </section>
      </div>

      <Section
        id="where-heading"
        title={`Where ${name} might go`}
        action={
          <Link to="/colleges" className="font-semibold text-brand hover:underline">
            Your colleges
          </Link>
        }
      >
        <InterestsLine studentId={student.id} name={name} />
        {schools.length === 0 ? (
          <div className="mt-4 flex flex-wrap items-center gap-3">
            <ButtonLink to="/colleges" variant="brand" size="sm">
              Choose colleges
            </ButtonLink>
            <span className="text-sm text-ink-3">Save the schools {name} might apply to, in any state.</span>
          </div>
        ) : (
          <RowList className="mt-4">
            {rows.map(({ c, o }) => {
              const cp = costPhrase(o)
              return (
                <Row
                  key={c.institution_key}
                  to={`/colleges/${encodeURIComponent(c.institution_key)}`}
                  title={
                    <>
                      {o.name}
                      {c.institution_key === saved.primary && <Pill tone="brand" className="ml-2 align-middle">Top choice</Pill>}
                    </>
                  }
                  meta={[c.institution?.city, c.institution?.state_code].filter(Boolean).join(', ') + (o.level === 'two_year' ? ' · 2-year college' : '')}
                  value={
                    cp.amount && o.comparable ? (
                      <span className="text-right">
                        <span className="block text-lg font-bold tabular text-ink">{cp.amount}</span>
                        <span className="block text-xs text-ink-3">{o.level === 'two_year' ? '2 years' : '4 years'}, before aid</span>
                      </span>
                    ) : (
                      <span className="block max-w-[11rem] text-right text-xs text-ink-3">{o.basis === 'out_of_state_missing' ? 'No out-of-state price' : cp.amount ? 'Set your home state' : 'No verified cost yet'}</span>
                    )
                  }
                />
              )
            })}
          </RowList>
        )}
      </Section>

      {o.history.length > 0 || o.benchmarks.length > 0 ? (
        <WeeklyUpdate
          studentId={student.id}
          name={name}
          plan={weeklyPlan({ today: o.today, weekStart: o.weekStart, tz: o.tz, plan: o.plan, week: o.week, history: o.history, benchmarks: o.benchmarks, estimates: o.estimates })}
          canSetGoals={!!ctx?.memberships.some((m) => m.household_id === student.household_id && m.role === 'guardian' && m.can_set_goals)}
          skillName={catalog.skillName}
          lastPractice={lastDay}
          lastCheck={o.benchmarks.at(-1) ?? null}
          lastWeek={o.lastWeek ? weekRecap({ weekStart: addDays(o.weekStart, -7), tz: o.tz, plan: o.plan, week: o.lastWeek, history: o.history, benchmarks: o.benchmarks, estimates: o.estimates }) : null}
          recapFirst={showRecap(o.today, o.weekStart)}
          hasGoal={!!o.week.goal?.target_questions}
          content={o.content}
          onRefresh={onRefresh}
        />
      ) : null}

      {source.supportsReminders && (
        <Section id="reminders-heading" title="Practice reminders" subtitle={`Friendly nudges on ${name}'s phone or computer`}>
          <div className="grid max-w-2xl gap-4">
            <ReminderSettingsPanel
              studentId={student.id}
              name={name}
              as="guardian"
              canEdit={!!ctx?.memberships.some((m) => m.household_id === student.household_id && m.role === 'guardian' && m.can_set_goals)}
              hasGuardian
              timeZone={o.tz}
            />
            <GuardianReminderStatus studentId={student.id} name={name} />
          </div>
        </Section>
      )}

      <Section
        id="prep-heading"
        title="Test prep"
        subtitle={`What ${name} should work on now`}
        action={
          <Link to="/parent/progress" className="font-semibold text-brand hover:underline">
            Full progress
          </Link>
        }
      >
        {o.history.length === 0 ? (
          <div className="max-w-2xl">
            <h3 className="font-semibold text-ink">Practice hasn't started yet</h3>
            <p className="mt-1 text-sm text-ink-2">
              {linked
                ? `${name} logs in and takes the starting benchmark (about 30 minutes).`
                : `Once ${name} logs in with the invite code, they take a starting benchmark (about 30 minutes).`}{' '}
              After that, this section shows what to work on, pacing and progress toward the{' '}
              {o.plan?.target_score ? `${EXAM_NAME[exam]} ${o.plan.target_score} target` : 'target'}
              {goal ? ` and the ${goal}-question weekly goal` : ''}.
            </p>
            {!linked && (
              <Link to="/parent/household" className="mt-2 inline-flex text-sm font-semibold text-brand hover:underline">
                Get the invite code
              </Link>
            )}
          </div>
        ) : (
          <div className="grid gap-8">
            <div className="grid grid-cols-2 gap-x-6 gap-y-6 sm:grid-cols-4">
              {official ? (
                <Figure size="md" value={String(official.composite)} label={`${official.score_source === 'official' ? 'Official' : 'Self-reported'} ${EXAM_NAME[exam]}`} sub={`Target ${o.plan?.target_score ?? '—'}`} />
              ) : (
                <Figure size="md" value={o.plan?.target_score != null ? String(o.plan.target_score) : '—'} label={`Target ${EXAM_NAME[exam]}`} sub={est ? `Practice estimate ${est.composite}` : 'No score estimate yet (not calibrated)'} />
              )}
              <Figure size="md" value={goal ? `${o.week.questions_submitted}/${goal}` : String(o.week.questions_submitted)} label="This week" sub={goal ? `questions · ${Math.round((100 * o.week.questions_submitted) / goal)}% done` : 'questions · no goal set'} />
              <Figure size="md" value={`${o.streak.current_streak}`} label={`Day streak`} sub={`Longest ${o.streak.longest_streak}`} />
              <Figure
                size="md"
                value={trend.recent.acc === null ? '—' : `${Math.round(trend.recent.acc * 100)}%`}
                label="Accuracy, 7 days"
                sub={trend.prior.acc === null || trend.recent.acc === null ? `${trend.recent.n} answered` : `${trend.recent.acc >= trend.prior.acc ? '▲' : '▼'} from ${Math.round(trend.prior.acc * 100)}%`}
              />
            </div>
            <div>
              <h3 className="text-sm font-bold text-ink">By section</h3>
              <ul className="mt-3 grid gap-3 sm:grid-cols-2 sm:gap-x-10">
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
                      <ProgressBar value={acc ?? 0} label={`${SECTION_LABEL[sec]} accuracy`} tone={acc !== null && acc < 0.6 ? 'warn' : 'brand'} className="h-1.5" />
                    </li>
                  )
                })}
              </ul>
              {o.estimates.filter((e) => e.knowledge_weak).length > 0 && (
                <p className="mt-3 text-sm text-ink-3">
                  Weakest skills:{' '}
                  {o.estimates
                    .filter((e) => e.knowledge_weak)
                    .map((e) => catalog.skillName(e.skill_key))
                    .join(', ')}
                </p>
              )}
            </div>
            <NextBenchmark history={o.benchmarks} />
          </div>
        )}
      </Section>

      <p className="text-xs text-ink-3">
        Last practice: {lastDay ? formatShortDate(lastDay) : 'never'} · Time zone {o.tz}
      </p>
    </div>
  )
}

function PlanHeadline({ plan, residency, schoolsSaved, canChooseTop }: { plan: PlanSummary; residency: string | null; schoolsSaved: number; canChooseTop: boolean }) {
  if (!plan.headline)
    return (
      <div>
        <Figure size="xl" tone="muted" value="—" label="Four-year cost" />
        <p className="mt-2 max-w-md text-sm text-ink-2">
          {plan.missing === 'no_schools' ? (
            <>
              <Link to="/colleges" className="font-semibold text-brand hover:underline">Save colleges</Link> to see what a four-year degree would cost your family at published prices.
            </>
          ) : plan.missing === 'no_four_year' ? (
            'None of your saved schools is a four-year college yet.'
          ) : (
            <>
              None of your saved schools has a published price that applies to you yet. <Link to="/colleges" className="font-semibold text-brand hover:underline">Set your home state</Link> or add schools.
            </>
          )}
        </p>
      </div>
    )
  return (
    <div>
      <Figure
        size="xl"
        value={compactUsd(plan.headline.total)}
        label={`Four-year cost at ${plan.headline.name}`}
        sub={`${plan.headline.total.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })} published ${residency === 'out_of_state' ? 'out-of-state ' : residency === 'in_state' || residency === 'in_district' ? 'in-state ' : ''}cost of attendance, before aid · ${plan.headline.why === 'top_choice' ? 'your top choice' : `lowest of ${schoolsSaved === 1 ? 'your saved school' : `your ${schoolsSaved} saved schools`}`}`}
      />
      {canChooseTop && (
        <p className="mt-2 text-sm text-ink-3">
          <Link to="/colleges/paths" className="font-semibold text-brand hover:underline">Mark a top choice</Link> to plan around the school {`they`} most want.
        </p>
      )}
    </div>
  )
}

/** The next benchmark as one line with a date, not a card. */
function NextBenchmark({ history }: { history: StudentOverview['benchmarks'] }) {
  const next = benchmarkSchedule(history)
  const kind = next.kind === 'initial' ? 'Starting benchmark' : next.kind === 'full' ? 'Full benchmark' : 'Mini benchmark'
  return (
    <p className="text-sm text-ink-2">
      <span className="font-semibold text-ink">{kind}</span>{' '}
      {next.inDays === 0 ? (next.overdueDays > 0 ? `was due ${next.overdueDays} day${next.overdueDays === 1 ? '' : 's'} ago` : 'is due now') : `is due ${formatShortDate(next.dueDate)}`}.{' '}
      {history.length} taken so far.
    </p>
  )
}

function InterestsLine({ studentId, name }: { studentId: string; name: string }) {
  const { profile } = useInterests(studentId)
  const labels = profile.interests.map(labelOf)
  return (
    <p className="text-sm text-ink-2">
      {labels.length ? (
        <>
          {name} is considering <span className="font-semibold text-ink">{labels.join(', ')}</span>
          {profile.interests.some((i) => i.focus) ? '' : ' (not ranked)'}.{' '}
        </>
      ) : (
        <>{name} hasn't saved any study interests yet; not sure is fine. </>
      )}
      <Link to="/colleges/majors" className="font-semibold text-brand hover:underline">
        Explore majors
      </Link>
    </p>
  )
}

