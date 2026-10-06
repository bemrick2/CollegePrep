import { Link, Navigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { ButtonLink, Notice, PageLoading, Pill, ProgressBar, cx } from '../../components/ui'
import { Figure, Row, RowList, Section } from '../../components/layout'
import { Flame, Trophy } from '../../components/icons'
import { useInterests } from '../majors/useInterests'
import { useSavedComparison, COMPARE_YEAR } from '../colleges/useSavedComparison'
import { useMeritReference } from '../colleges/useMeritReference'
import { meritAwards } from '../../lib/engine/merit'
import { addDays, localDate } from '../../lib/engine/dates'
import { benchmarkAttemptIds, benchmarkSchedule, SECTION_LABEL } from '../../lib/engine/benchmark'
import { achievements, levelOf, totalXp } from '../../lib/engine/gamify'
import { latestEstimate, useStudentOverview, type StudentOverview } from './useStudentOverview'
import { useCatalog } from '../practice/useCatalog'
import { EXAM_NAME } from '../onboarding/options'

export function StudentHome() {
  const { ctx } = useApp()
  const student = ctx?.myStudent
  const o = useStudentOverview(student?.id)
  if (!student) return <Navigate to="/start" replace />
  if (o.loading && !o.data) return <PageLoading />
  if (o.error)
    return (
      <Notice tone="bad" title="Couldn't load your plan">
        {o.error.message}
      </Notice>
    )
  if (!o.data) return null
  return <HomeBody name={student.display_name} o={o.data} studentId={student.id} />
}

function HomeBody({ name, o, studentId }: { name: string; o: StudentOverview; studentId: string }) {
  const interests = useInterests(studentId).profile
  const exam = o.plan?.exam_family ?? 'act'
  const catalog = useCatalog(exam)
  const xp = totalXp(o.history)
  const lvl = levelOf(xp)
  // Benchmark answers count toward streak and XP but never mark today's daily practice done.
  const benchIds = benchmarkAttemptIds(o.benchmarks)
  const practicedToday = o.history.some((a) => !a.skipped && !benchIds.has(a.id) && localDate(a.submitted_at, o.tz) === o.today)
  const minutes = o.plan?.daily_minutes ?? 10
  const weakK = o.estimates.filter((e) => e.knowledge_weak)
  const weakP = o.estimates.filter((e) => e.pacing_weak)
  const focus = [...weakK, ...weakP][0]
  const estimates = latestEstimate(o.scores, exam)
  const est = estimates[0]
  const prevEst = estimates[1]
  const badges = achievements({ attempts: o.history, benchmarks: o.benchmarks, longestStreak: o.streak.longest_streak, goalsMet: o.goalsMet })
  const goal = o.week.goal?.target_questions ?? null
  const done = o.week.questions_submitted
  // Before the first benchmark the next step is the only thing on the page.
  const fresh = o.benchmarks.length === 0 && o.history.length === 0
  const schedule = benchmarkSchedule(o.benchmarks)
  const hour = new Date().getHours()
  const hello = hour < 12 ? 'Good morning' : hour < 18 ? 'Good afternoon' : 'Good evening'

  const next =
    o.benchmarks.length === 0
      ? {
          title: 'Your starting benchmark',
          length: 'About 30 minutes',
          cta: 'Start benchmark',
          to: '/student/benchmark',
          detail: `It finds your strengths and gaps, so every session after this is about ${minutes} minutes and aimed at what matters.`,
        }
      : practicedToday
        ? {
            title: 'Done for today',
            length: o.streak.current_streak > 1 ? `${o.streak.current_streak} days in a row. Come back tomorrow to keep it going.` : 'Come back tomorrow to start a streak.',
            cta: 'Bonus round',
            to: '/student/practice',
            detail: null,
          }
        : {
            title: focus ? `${EXAM_NAME[exam]} ${SECTION_LABEL[focus.section] ?? focus.section} — ${catalog.skillName(focus.skill_key) ?? focus.skill_key}` : `${EXAM_NAME[exam]} mixed practice`,
            length: `About ${minutes} minutes`,
            cta: 'Continue',
            to: '/student/practice',
            detail: focus
              ? focus.pacing_weak && !focus.knowledge_weak
                ? 'You know this one; the goal is getting faster.'
                : 'Your weakest skill right now.'
              : 'Aimed at the skills with the least data so far.',
          }

  return (
    <div className="grid grid-cols-1 gap-8">
      <header className="flex items-center justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">{hello},</p>
          <h1 className="display text-[28px] leading-tight text-ink">{name}</h1>
        </div>
        <div className="flex items-center gap-2">
          <span
            className={cx(
              'flex items-center gap-1 rounded-full px-3 py-1.5 text-sm font-bold tabular',
              o.streak.current_streak > 0 ? 'bg-gold-soft text-gold-ink' : 'bg-surface-2 text-ink-3',
            )}
            title={`${o.streak.current_streak} day streak`}
          >
            <Flame size={18} /> {o.streak.current_streak}
            <span className="sr-only"> day streak</span>
          </span>
          {!fresh && <span className="rounded-full bg-brand-soft px-3 py-1.5 text-sm font-bold text-brand">Lv {lvl.level}</span>}
        </div>
      </header>

      <div className={cx('grid grid-cols-1 gap-8', !fresh && 'lg:grid-cols-[minmax(0,1.5fr)_minmax(0,1fr)] lg:gap-12')}>
        {/* The one thing to do now: where the week stands, what's next, why it matters, one button. */}
        <section aria-labelledby="next-title" className="rounded-2xl border border-line bg-surface p-5 md:p-8">
          {!fresh && (
            <div className="border-b border-line pb-5 md:pb-6">
              <p className="text-sm font-semibold text-ink-3">This week</p>
              <p className="mt-1 flex items-baseline gap-2">
                <span className="figure text-[36px] text-ink md:text-[44px]">{goal ? `${done} / ${goal}` : done}</span>
                <span className="text-[15px] font-semibold text-ink-2">questions</span>
              </p>
              {goal ? <ProgressBar className="mt-3" value={done} max={goal} tone="go" label="Weekly goal progress" /> : null}
              <WeekDots o={o} />
            </div>
          )}
          <div className={cx(!fresh && 'pt-5 md:pt-6')}>
            <p className="text-sm font-semibold text-ink-3">{practicedToday ? 'Today' : 'Next up'}</p>
            <h2 id="next-title" className="display mt-1 text-[26px] leading-tight text-ink md:text-[30px]">
              {next.title}
            </h2>
            <p className="mt-1 text-[15px] font-semibold text-ink-2">{next.length}</p>
            {next.detail && <p className="mt-1 text-sm text-ink-3">{next.detail}</p>}
          </div>
          {!fresh && (
            <div className="mt-5 md:mt-6">
              <p className="text-sm font-semibold text-ink-3">Why this matters</p>
              <WhyItMatters studentId={studentId} exam={exam} target={o.plan?.target_score ?? null} />
            </div>
          )}
          <ButtonLink to={next.to} size="lg" block className="mt-6 md:mt-7" variant={practicedToday ? 'secondary' : 'go'}>
            {next.cta}
          </ButtonLink>
        </section>

        {!fresh && (
          <aside className="grid content-start gap-8" aria-label="Your progress">
            {est && (
              <Figure
                size="lg"
                value={est.composite}
                label={`${EXAM_NAME[exam]} practice estimate`}
                sub={
                  <>
                    {prevEst?.composite != null && est.composite! > prevEst.composite && <span className="font-semibold text-go">+{est.composite! - prevEst.composite}. </span>}
                    {o.plan?.target_score ? `Target ${o.plan.target_score}. ` : ''}Not an official score.
                  </>
                }
              />
            )}
            <Section
              id="skills-heading"
              title="Skills to work on"
              action={
                <Link to="/student/progress" className="font-semibold text-brand hover:underline">
                  All skills
                </Link>
              }
            >
              {weakK.length === 0 && weakP.length === 0 ? (
                <p className="text-sm text-ink-3">
                  {o.estimates.some((e) => e.knowledge_weak !== null) ? 'No weak skills flagged right now. Nice.' : 'Skills get flagged after about five answers each. Keep practising.'}
                </p>
              ) : (
                <RowList>
                  {weakK.slice(0, 3).map((e) => (
                    <Row
                      key={e.skill_id}
                      title={catalog.skillName(e.skill_key) ?? e.skill_key}
                      meta={`${SECTION_LABEL[e.section] ?? e.section}, ${Math.round((e.accuracy ?? 0) * 100)}% right`}
                      value={<Pill tone="warn">Knowledge</Pill>}
                    />
                  ))}
                  {weakP.slice(0, 2).map((e) => (
                    <Row
                      key={e.skill_id}
                      title={catalog.skillName(e.skill_key) ?? e.skill_key}
                      meta={`${SECTION_LABEL[e.section] ?? e.section}, ${e.pacing_ratio?.toFixed(1)}× test pace`}
                      value={<Pill tone="info">Speed</Pill>}
                    />
                  ))}
                </RowList>
              )}
            </Section>
            <Section id="momentum-heading" title="Momentum">
              <div className="mb-1 flex justify-between text-sm">
                <span className="font-semibold text-ink">Level {lvl.level}</span>
                <span className="tabular text-ink-3">
                  {lvl.into}/{lvl.span} XP
                </span>
              </div>
              <ProgressBar value={lvl.into} max={lvl.span} tone="gold" label="XP to next level" />
              <div className="mt-3 flex flex-wrap items-center gap-1.5">
                {badges
                  .filter((b) => b.earned)
                  .map((b) => (
                    <Pill key={b.key} tone="gold">
                      <Trophy size={12} /> {b.title}
                    </Pill>
                  ))}
                {(() => {
                  const nb = badges.find((b) => !b.earned)
                  return nb ? (
                    <span className="text-xs text-ink-3">
                      Next: {nb.title} ({nb.progress}/{nb.goal})
                    </span>
                  ) : null
                })()}
              </div>
              <p className="mt-4 text-sm text-ink-2">
                {schedule.inDays === 0 ? (
                  <Link to={`/student/benchmark${schedule.kind === 'initial' ? '' : `?kind=${schedule.kind}`}`} className="font-semibold text-brand hover:underline">
                    {schedule.kind === 'full' ? 'Full' : 'Mini'} benchmark due
                  </Link>
                ) : (
                  `Next ${schedule.kind === 'full' ? 'full' : 'mini'} benchmark in ${schedule.inDays} ${schedule.inDays === 1 ? 'day' : 'days'}.`
                )}{' '}
                <Link to="/student/progress" className="font-semibold text-brand hover:underline">
                  See your progress
                </Link>
              </p>
            </Section>
          </aside>
        )}
      </div>

      {(interests.certainty === null && interests.interests.length === 0) || !o.plan ? (
        <Section>
          <RowList>
            {interests.certainty === null && interests.interests.length === 0 && (
              <Row to="/colleges/majors" title="What might you study?" meta="Not sure is a fine answer. Save a few interests and we'll show which of your colleges offer them." />
            )}
            {!o.plan && <Row to="/student/goals" title="Set your test and target" meta="Choose ACT or SAT and a target score so practice matches your test." />}
          </RowList>
        </Section>
      ) : null}
    </div>
  )
}

function WeekDots({ o }: { o: StudentOverview }) {
  const days = Array.from({ length: 7 }, (_, i) => addDays(o.weekStart, i))
  const practiced = new Set(o.history.filter((a) => !a.skipped).map((a) => localDate(a.submitted_at, o.tz)))
  return (
    <ol className="mt-3 grid max-w-xs grid-cols-7 gap-0.5" aria-label="Days practised this week">
      {days.map((d, i) => {
        const done = practiced.has(d)
        const isToday = d === o.today
        return (
          <li key={d} className="flex flex-col items-center gap-1">
            <span className={cx('text-[11px] font-semibold', isToday ? 'text-ink' : 'text-ink-3')}>{'MTWTFSS'[i]}</span>
            <span
              className={cx(
                'grid h-6 w-6 place-items-center rounded-full text-[11px]',
                done ? 'bg-gold text-white' : isToday ? 'border-2 border-gold' : 'bg-surface-3',
              )}
              role="img"
              aria-label={`${d}: ${done ? 'practised' : 'not practised'}`}
            >
              {done ? <Flame size={12} /> : null}
            </span>
          </li>
        )
      })}
    </ol>
  )
}

/**
 * Why today's practice matters, from verified records only: the nearest published merit minimum at the student's
 * saved schools, compared with their target (or official score). Never a guarantee, never a score estimate.
 */
function WhyItMatters({ studentId, exam, target }: { studentId: string; exam: 'act' | 'sat'; target: number | null }) {
  const cmp = useSavedComparison(COMPARE_YEAR)
  const { reference } = useMeritReference(studentId)
  const label = EXAM_NAME[exam]
  const merits = (cmp.data ?? [])
    .filter((c) => c.found)
    .flatMap((c) => meritAwards(c.domains.awards).map((m) => ({ school: c.institution?.display_name ?? c.institution_key, name: m.name, min: m.min[exam] })))
    .filter((m): m is { school: string; name: string; min: number } => m.min != null)
  const ref = reference?.value ?? null
  const next = ref != null ? merits.filter((m) => m.min > ref).sort((a, b) => a.min - b.min)[0] : undefined
  const met = ref != null ? merits.filter((m) => m.min <= ref).sort((a, b) => b.min - a.min)[0] : undefined
  const sameMin = next ? merits.filter((m) => m.school === next.school && m.min === next.min).length : 0
  const whose = reference?.basis === 'target' ? 'your target' : 'your score'
  return (
    <div className="mt-1 grid gap-1.5">
      <p className="text-[15px] text-ink">
        {cmp.keys.length === 0 ? (
          <>
            <Link to="/colleges" className="font-semibold text-brand hover:underline">
              Save colleges
            </Link>{' '}
            to see which scholarships list the score you're working toward.
          </>
        ) : !target && !reference ? (
          <>
            <Link to="/student/goals" className="font-semibold text-brand hover:underline">
              Set a target
            </Link>{' '}
            to compare it with your colleges' published scholarship minimums.
          </>
        ) : next ? (
          <>
            <span className="font-semibold">
              {next.min - ref!} more {label} {next.min - ref! === 1 ? 'point' : 'points'}
            </span>{' '}
            than {whose} could put you at the published {label} {next.min}+ threshold for {sameMin > 1 ? `${sameMin} merit awards` : next.name} at{' '}
            <span className="font-semibold">{next.school}</span>.
          </>
        ) : met ? (
          <>
            {whose[0]!.toUpperCase() + whose.slice(1)} meets the published {label} minimum for {met.name} at <span className="font-semibold">{met.school}</span>. Other
            criteria apply.
          </>
        ) : (
          <>None of your saved colleges publishes a single {label} minimum for a merit award yet.</>
        )}
      </p>
      <p className="text-xs text-ink-3">
        Published criteria, not an eligibility decision or a guarantee. We don't estimate your {label} score from practice yet.
      </p>
    </div>
  )
}
