import { Link, Navigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { ButtonLink, Card, CardHeader, Notice, PageLoading, Pill, ProgressBar, Ring, cx } from '../../components/ui'
import { Bolt, Compass, Flame, Target, Trophy } from '../../components/icons'
import { PracticeIndicators } from '../../components/PracticeIndicators'
import { BenchmarkStatus } from '../../components/BenchmarkStatus'
import { addDays, localDate } from '../../lib/engine/dates'
import { benchmarkAttemptIds, SECTION_LABEL } from '../../lib/engine/benchmark'
import { achievements, levelOf, totalXp } from '../../lib/engine/gamify'
import { latestEstimate, recentTrend, useStudentOverview, type StudentOverview } from './useStudentOverview'
import { useCatalog } from '../practice/useCatalog'
import { EXAM_NAME } from '../onboarding/options'

export function StudentHome() {
  const { ctx } = useApp()
  const student = ctx?.myStudent
  const o = useStudentOverview(student?.id)
  if (!student) return <Navigate to="/start" replace />
  if (o.loading && !o.data) return <PageLoading />
  if (o.error) return <Notice tone="bad" title="Couldn't load your plan">{o.error.message}</Notice>
  if (!o.data) return null
  return <HomeBody name={student.display_name} o={o.data} />
}

function HomeBody({ name, o }: { name: string; o: StudentOverview }) {
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
  const focus = [...weakK, ...weakP].slice(0, 2)
  const estimates = latestEstimate(o.scores, exam)
  const est = estimates[0]
  const prevEst = estimates[1]
  const trend = recentTrend(o.history, o.today, o.tz)
  const badges = achievements({ attempts: o.history, benchmarks: o.benchmarks, longestStreak: o.streak.longest_streak, goalsMet: o.goalsMet })
  const goal = o.week.goal?.target_questions ?? null
  const hour = new Date().getHours()
  const hello = hour < 12 ? 'Good morning' : hour < 18 ? 'Good afternoon' : 'Good evening'

  return (
    <div className="grid grid-cols-1 gap-4">
      <div className="flex items-center justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">{hello},</p>
          <h1 className="display text-[28px] font-semibold leading-tight text-ink">{name}</h1>
        </div>
        <div className="flex items-center gap-2">
          <span className={cx('flex items-center gap-1 rounded-full px-3 py-1.5 text-sm font-bold tabular', o.streak.current_streak > 0 ? 'bg-gold-soft text-gold-ink' : 'bg-surface-2 text-ink-3')} title={`${o.streak.current_streak} day streak`}>
            <Flame size={18} /> {o.streak.current_streak}<span className="sr-only"> day streak</span>
          </span>
          <span className="rounded-full bg-brand-soft px-3 py-1.5 text-sm font-bold text-brand">
            Lv {lvl.level}
          </span>
        </div>
      </div>

      {/* The one thing to do now. */}
      {o.benchmarks.length === 0 ? (
        <HeroCard
          eyebrow="Start here"
          title="Take your benchmark"
          body={`About 25 minutes. It finds your strengths and gaps so every session after this is about ${minutes} minutes and aimed at what matters.`}
          cta="Start benchmark"
          to="/student/benchmark"
          icon={<Compass size={28} />}
        />
      ) : practicedToday ? (
        <HeroCard
          eyebrow="Today"
          title="Done for today"
          body={o.streak.current_streak > 1 ? `${o.streak.current_streak} days in a row. Come back tomorrow to keep it going — or take a bonus round now.` : 'Nice. Come back tomorrow to start a streak — or take a bonus round now.'}
          cta="Bonus round"
          to="/student/practice"
          variant="quiet"
          icon={<Trophy size={28} />}
        />
      ) : (
        <HeroCard
          eyebrow="Today's plan"
          title={`About ${minutes} minutes`}
          body={
            focus.length
              ? `Focus: ${focus.map((f) => catalog.skillName(f.skill_key)).join(' and ')}${weakP.length && focus.some((f) => f.pacing_weak) ? ' (speed)' : ''}.`
              : 'A short mixed set, aimed at the skills with the least data so far.'
          }
          cta="Start"
          to="/student/practice"
          icon={<Bolt size={28} />}
          streakNote={o.streak.current_streak > 0 ? `Keep your ${o.streak.current_streak}-day streak alive` : undefined}
        />
      )}

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        <Card>
          <CardHeader title="This week" subtitle={goal ? `${o.week.questions_submitted} of ${goal} questions` : `${o.week.questions_submitted} questions`} />
          <div className="flex items-center gap-4 p-5 pt-3">
            <Ring value={o.week.questions_submitted} max={goal ?? Math.max(1, o.week.questions_submitted)} size={80} stroke={9} label="Weekly goal progress">
              <span className="text-lg font-bold tabular text-ink">{goal ? `${Math.min(100, Math.round((100 * o.week.questions_submitted) / goal))}%` : o.week.questions_submitted}</span>
            </Ring>
            <WeekDots o={o} />
          </div>
        </Card>

        <Card>
          <CardHeader title={`${EXAM_NAME[exam]} score`} subtitle={o.plan?.target_score ? `Target ${o.plan.target_score}` : 'No target set'} />
          <div className="p-5 pt-3">
            {est ? (
              <>
                <div className="flex items-baseline gap-2">
                  <span className="display text-5xl font-semibold tabular text-ink">{est.composite}</span>
                  {prevEst?.composite != null && est.composite! > prevEst.composite && <Pill tone="go">+{est.composite! - prevEst.composite}</Pill>}
                  {o.plan?.target_score && est.composite! < o.plan.target_score && <span className="text-sm text-ink-3">{o.plan.target_score - est.composite!} to go</span>}
                </div>
                <p className="mt-1 text-xs text-ink-3">Practice estimate — not an official score.</p>
              </>
            ) : (
              <>
                <div className="display text-5xl font-semibold text-ink-3">—</div>
                <p className="mt-1 text-xs text-ink-3">No score estimate yet: turning practice into an {EXAM_NAME[exam]} score needs a calibrated question bank, and we won't guess. Your practice indicators and benchmarks show where you stand.</p>
              </>
            )}
          </div>
        </Card>
      </div>

      <PracticeIndicators history={o.history} />

      <Card>
        <CardHeader
          title="Skills to work on"
          subtitle="Knowledge and speed are tracked separately"
          action={
            <Link to="/student/progress" className="shrink-0 whitespace-nowrap text-sm font-semibold text-go hover:underline">
              All skills
            </Link>
          }
        />
        <div className="grid grid-cols-1 gap-2 p-5 pt-3">
          {weakK.length === 0 && weakP.length === 0 ? (
            <p className="text-sm text-ink-3">
              {o.estimates.some((e) => e.knowledge_weak !== null) ? 'No weak skills flagged right now. Nice.' : 'Skills get flagged after about five answers each. Keep practising.'}
            </p>
          ) : (
            <>
              {weakK.slice(0, 3).map((e) => (
                <SkillRow key={e.skill_id} name={catalog.skillName(e.skill_key) ?? e.skill_key} section={e.section} tag="Knowledge" tone="warn" value={e.accuracy ?? 0} detail={`${Math.round((e.accuracy ?? 0) * 100)}% right`} />
              ))}
              {weakP.slice(0, 2).map((e) => (
                <SkillRow key={e.skill_id} name={catalog.skillName(e.skill_key) ?? e.skill_key} section={e.section} tag="Speed" tone="info" value={e.accuracy ?? 0} detail={`${e.pacing_ratio?.toFixed(1)}× test pace`} />
              ))}
            </>
          )}
        </div>
      </Card>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        <Card>
          <CardHeader title="Momentum" />
          <div className="grid gap-3 p-5 pt-3 text-sm">
            <div>
              <div className="mb-1 flex justify-between">
                <span className="font-semibold text-ink">Level {lvl.level}</span>
                <span className="tabular text-ink-3">
                  {lvl.into}/{lvl.span} XP
                </span>
              </div>
              <ProgressBar value={lvl.into} max={lvl.span} tone="gold" label="XP to next level" />
            </div>
            {trend.recent.acc !== null && trend.prior.acc !== null && trend.recent.n >= 5 && trend.prior.n >= 5 && (
              <p className="text-ink-2">
                Accuracy this week{' '}
                <span className={cx('font-semibold', trend.recent.acc >= trend.prior.acc ? 'text-go' : 'text-warn')}>
                  {Math.round(trend.recent.acc * 100)}%
                </span>{' '}
                vs {Math.round(trend.prior.acc * 100)}% the week before.
              </p>
            )}
            <div className="flex flex-wrap gap-1.5">
              {badges.filter((b) => b.earned).map((b) => (
                <Pill key={b.key} tone="gold">
                  <Trophy size={12} /> {b.title}
                </Pill>
              ))}
              {(() => {
                const next = badges.find((b) => !b.earned)
                return next ? (
                  <span className="text-xs text-ink-3">
                    Next: {next.title} ({next.progress}/{next.goal})
                  </span>
                ) : null
              })()}
            </div>
          </div>
        </Card>

        <BenchmarkStatus history={o.benchmarks} />
      </div>
      {!o.plan && (
        <Notice tone="gold" title="Set your test and target">
          <Link className="font-semibold underline" to="/student/goals">
            Choose ACT or SAT and a target score
          </Link>{' '}
          so practice matches your test.
        </Notice>
      )}
    </div>
  )
}

function HeroCard({ eyebrow, title, body, cta, to, icon, variant = 'go', streakNote }: { eyebrow: string; title: string; body: string; cta: string; to: string; icon: React.ReactNode; variant?: 'go' | 'quiet'; streakNote?: string }) {
  return (
    <section
      className={cx(
        'anim-rise relative overflow-hidden rounded-3xl p-6',
        variant === 'go' ? 'bg-hero text-hero-ink' : 'border border-line bg-surface text-ink',
      )}
      aria-labelledby="hero-title"
    >
      <div className="flex items-start gap-4">
        <div className="min-w-0 flex-1">
          <p className={cx('text-xs font-bold uppercase tracking-[0.14em]', variant === 'go' ? 'text-gold' : 'text-go')}>{eyebrow}</p>
          <h2 id="hero-title" className="display mt-1 text-[30px] font-semibold leading-tight">
            {title}
          </h2>
          <p className={cx('mt-2 text-[15px]', variant === 'go' ? 'opacity-85' : 'text-ink-2')}>{body}</p>
        </div>
        <span className={cx('grid h-14 w-14 shrink-0 place-items-center rounded-2xl', variant === 'go' ? 'bg-white/10 text-gold' : 'bg-gold-soft text-gold-ink')}>{icon}</span>
      </div>
      <ButtonLink to={to} size="lg" block className="mt-5" variant={variant === 'go' ? 'go' : 'secondary'}>
        {cta}
      </ButtonLink>
      {streakNote && (
        <p className="mt-3 flex items-center justify-center gap-1 text-xs font-semibold text-gold">
          <Flame size={14} /> {streakNote}
        </p>
      )}
    </section>
  )
}

function WeekDots({ o }: { o: StudentOverview }) {
  const days = Array.from({ length: 7 }, (_, i) => addDays(o.weekStart, i))
  const practiced = new Set(o.history.filter((a) => !a.skipped).map((a) => localDate(a.submitted_at, o.tz)))
  return (
    <ol className="grid min-w-0 flex-1 grid-cols-7 gap-0.5" aria-label="Days practised this week">
      {days.map((d, i) => {
        const done = practiced.has(d)
        const isToday = d === o.today
        return (
          <li key={d} className="flex flex-col items-center gap-1">
            <span className={cx('text-[11px] font-semibold', isToday ? 'text-ink' : 'text-ink-3')}>{'MTWTFSS'[i]}</span>
            <span
              className={cx('grid h-6 w-6 place-items-center rounded-full text-[11px]', done ? 'bg-gold text-white' : isToday ? 'border-2 border-gold' : 'bg-surface-3')}
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

function SkillRow({ name, section, tag, tone, value, detail }: { name: string; section: string; tag: string; tone: 'warn' | 'info'; value: number; detail: string }) {
  return (
    <div className="flex items-center gap-3 rounded-xl bg-surface-2 px-3 py-2.5">
      <Target size={18} className={tone === 'warn' ? 'text-warn' : 'text-info'} />
      <div className="min-w-0 flex-1">
        <div className="line-clamp-2 text-sm font-semibold leading-snug text-ink">{name}</div>
        <div className="text-xs text-ink-3">
          {SECTION_LABEL[section] ?? section} · {detail}
        </div>
      </div>
      <Pill tone={tone}>{tag}</Pill>
      <span className="sr-only">{Math.round(value * 100)}%</span>
    </div>
  )
}
