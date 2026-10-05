import { useState } from 'react'
import { Navigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { Card, CardHeader, EmptyState, Notice, PageLoading, Pill, ProgressBar, cx } from '../../components/ui'
import { Chart } from '../../components/icons'
import { addDays, formatDuration, formatShortDate, localDate } from '../../lib/engine/dates'
import { SECTION_LABEL, SECTION_ORDER, benchmarkImprovement, pacingVerdict } from '../../lib/engine/benchmark'
import { improvementVerdict } from '../../lib/engine/improving'
import { ImprovingCard } from '../../components/ImprovingCard'
import { recentTrend, useStudentOverview, type StudentOverview } from '../student/useStudentOverview'
import { useCatalog } from '../practice/useCatalog'
import { BenchmarkResults, PACE_COPY } from '../benchmark/BenchmarkResults'
import type { SkillEstimate } from '../../lib/data/types'
import { PracticeIndicators } from '../../components/PracticeIndicators'
import { BenchmarkStatus } from '../../components/BenchmarkStatus'
import { achievements } from '../../lib/engine/gamify'
import { Trophy } from '../../components/icons'

export function StudentProgressPage() {
  const { ctx } = useApp()
  if (!ctx?.myStudent) return <Navigate to="/student" replace />
  return <Progress studentId={ctx.myStudent.id} heading="Your progress" />
}

export function ParentProgressPage() {
  const { activeStudent } = useApp()
  if (!activeStudent) return <Navigate to="/parent" replace />
  return <Progress studentId={activeStudent.id} heading={`${activeStudent.display_name}'s progress`} who={activeStudent.display_name} />
}

export function Progress({ studentId, heading, who }: { studentId: string; heading: string; who?: string }) {
  const o = useStudentOverview(studentId)
  if (o.loading && !o.data) return <PageLoading />
  if (o.error) return <Notice tone="bad">{o.error.message}</Notice>
  if (!o.data) return null
  return <Body o={o.data} heading={heading} who={who} />
}

function Body({ o, heading, who }: { o: StudentOverview; heading: string; who?: string }) {
  const exam = o.plan?.exam_family ?? 'act'
  const catalog = useCatalog(exam)
  const answered = o.history.filter((a) => !a.skipped)
  const [openBench, setOpenBench] = useState<string | null>(null)

  if (answered.length === 0 && o.benchmarks.length === 0)
    return (
      <div>
        <h1 className="display text-[28px] font-semibold text-ink">{heading}</h1>
        <Card className="mt-4">
          <EmptyState icon={<Chart size={32} />} title="No practice yet">
            Progress appears after the first benchmark or practice session.
          </EmptyState>
        </Card>
      </div>
    )

  const weeks = Array.from({ length: 8 }, (_, i) => addDays(o.weekStart, -7 * (7 - i)))
  const weekly = weeks.map((w) => {
    const rs = answered.filter((a) => {
      const d = localDate(a.submitted_at, o.tz)
      return d >= w && d < addDays(w, 7)
    })
    return { week: w, n: rs.length, acc: rs.length ? rs.filter((a) => a.is_correct).length / rs.length : null }
  })

  const bySection = new Map<string, SkillEstimate[]>()
  for (const e of o.estimates) bySection.set(e.section, [...(bySection.get(e.section) ?? []), e])
  const sections = [...SECTION_ORDER[exam].filter((s) => bySection.has(s)), ...[...bySection.keys()].filter((s) => !SECTION_ORDER[exam].includes(s))]

  return (
    <div className="grid grid-cols-1 gap-4">
      <h1 className="display text-[28px] font-semibold text-ink">{heading}</h1>

      <ImprovingCard v={improvementVerdict(benchmarkImprovement(o.benchmarks), recentTrend(o.history, o.today, o.tz))} title={who ? `Is ${who} improving?` : 'Am I improving?'} />

      <PracticeIndicators history={o.history} who={who} showTrend />

      <Card>
        <CardHeader title="Last 8 weeks" subtitle="Bars: questions answered. Dots: accuracy." />
        <WeeklyChart data={weekly} />
      </Card>

      <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
        <MiniStat label="Answered this week" value={String(o.week.questions_submitted)} />
        <MiniStat label="Accuracy this week" value={o.week.accuracy === null ? '—' : `${Math.round(o.week.accuracy * 100)}%`} />
        <MiniStat label="Typical time / question" value={o.week.median_elapsed_ms === null ? '—' : formatDuration(o.week.median_elapsed_ms)} />
        <MiniStat label="Longest streak" value={`${o.streak.longest_streak} days`} />
      </div>

      <Card>
        <CardHeader title="Skill mastery" subtitle="From the last 30 answers per skill. Flags need at least 5 answers." />
        <div className="grid gap-5 p-5">
          {sections.map((sec) => {
            const list = [...bySection.get(sec)!].sort((a, b) => Number(!!b.knowledge_weak) - Number(!!a.knowledge_weak) || Number(!!b.pacing_weak) - Number(!!a.pacing_weak))
            const toBuild = list.filter((e) => e.knowledge_weak || e.pacing_weak).length
            const solid = list.filter((e) => e.knowledge_weak === false && !e.pacing_weak).length
            return (
            <details key={sec} open={toBuild > 0} className="group">
              <summary className="mb-2 flex cursor-pointer list-none items-center justify-between gap-2">
                <h3 className="text-xs font-bold uppercase tracking-wide text-ink-3">{SECTION_LABEL[sec] ?? sec}</h3>
                <span className="text-xs text-ink-3">
                  {toBuild > 0 && <span className="font-semibold text-warn">{toBuild} to build · </span>}
                  {solid} solid · <span className="text-brand group-open:hidden">show</span><span className="hidden text-brand group-open:inline">hide</span>
                </span>
              </summary>
              <ul className="grid grid-cols-1 gap-2">
                {list.map((e) => {
                  const pv = PACE_COPY[pacingVerdict(e.pacing_ratio)]
                  const status = e.knowledge_weak === null ? { label: 'Need more data', tone: 'neutral' as const } : e.knowledge_weak ? { label: 'Build knowledge', tone: 'warn' as const } : e.pacing_weak ? { label: 'Build speed', tone: 'info' as const } : { label: 'Solid', tone: 'go' as const }
                  return (
                    <li key={e.skill_id} className="grid grid-cols-[1fr_auto] items-center gap-x-3 gap-y-1.5 rounded-xl bg-surface-2 px-3 py-2.5 sm:grid-cols-[minmax(0,1.3fr)_minmax(0,1fr)_auto_auto]">
                      <span className="line-clamp-2 text-sm font-semibold leading-snug text-ink">{catalog.skillName(e.skill_key)}</span>
                      <Pill tone={status.tone} className="sm:order-4">
                        {status.label}
                      </Pill>
                      <span className="flex items-center gap-2 sm:order-2">
                        <ProgressBar value={e.accuracy ?? 0} label={`${catalog.skillName(e.skill_key)} accuracy`} tone={e.knowledge_weak ? 'warn' : 'go'} className="h-2" />
                        <span className="w-10 text-right text-xs tabular text-ink-2">{Math.round((e.accuracy ?? 0) * 100)}%</span>
                      </span>
                      <span className="text-right text-xs text-ink-3 tabular sm:order-3">
                        {e.attempts} ans · <span title={pv.label}>{e.pacing_ratio === null ? '—' : `${e.pacing_ratio.toFixed(1)}×`}</span>
                      </span>
                    </li>
                  )
                })}
              </ul>
            </details>
            )
          })}
          {sections.length === 0 && <p className="text-sm text-ink-3">No skill data yet.</p>}
        </div>
      </Card>

      <Card>
        <CardHeader title="Test-taking this week" subtitle="Habits that move scores without new knowledge" />
        <div className="grid grid-cols-2 gap-3 p-5 sm:grid-cols-4">
          <MiniStat label="Skipped then returned" value={String(o.week.returns)} flat />
          <MiniStat label="Answer changes" value={String(o.week.answer_changes)} flat />
          <MiniStat label="Hints used" value={String(o.week.hints_used)} flat />
          <MiniStat label="Avg confidence" value={o.week.avg_confidence === null ? '—' : `${o.week.avg_confidence.toFixed(1)} / 3`} flat />
        </div>
      </Card>

      <BenchmarkStatus history={o.benchmarks} forGuardian={!!who} />

      <Milestones o={o} />

      <Card>
        <CardHeader title="Benchmark history" />
        <ul className="divide-y divide-line">
          {o.benchmarks.length === 0 && <li className="px-5 py-4 text-sm text-ink-3">No benchmarks yet.</li>}
          {[...o.benchmarks].reverse().map((b) => (
            <li key={b.id}>
              <button className="flex w-full items-center gap-3 px-5 py-4 text-left hover:bg-surface-2" aria-expanded={openBench === b.id} onClick={() => setOpenBench(openBench === b.id ? null : b.id)}>
                <span className="min-w-0 flex-1">
                  <span className="block font-semibold capitalize text-ink">{b.kind} benchmark</span>
                  <span className="text-xs text-ink-3">{formatShortDate(b.completed_at)} · {b.metrics.answered} answered</span>
                </span>
                <span className="text-lg font-semibold tabular text-ink">{b.metrics.accuracy === null ? '—' : `${Math.round(b.metrics.accuracy * 100)}%`}</span>
              </button>
              {openBench === b.id && (
                <div className="bg-surface-2 p-4">
                  <BenchmarkResults summary={b} traps={catalog.traps} standalone={false} />
                </div>
              )}
            </li>
          ))}
        </ul>
      </Card>

      {o.scores.length > 0 && (
        <Card>
          <CardHeader title="Scores" subtitle="Official, self-reported and practice estimates are kept separate." />
          <ul className="divide-y divide-line">
            {[...o.scores].sort((a, b) => b.test_date.localeCompare(a.test_date)).map((s) => (
              <li key={s.id} className="flex items-center justify-between gap-3 px-5 py-3 text-sm">
                <span>
                  <span className="font-semibold uppercase text-ink">{s.exam_family}</span> <span className="text-ink-3">· {formatShortDate(s.test_date)}</span>
                </span>
                <span className="flex items-center gap-2">
                  <Pill tone={s.score_source === 'official' ? 'go' : s.score_source === 'self_reported' ? 'info' : 'neutral'}>
                    {s.score_source === 'official' ? 'Official' : s.score_source === 'self_reported' ? 'Self-reported' : 'Practice estimate'}
                  </Pill>
                  <span className="text-lg font-semibold tabular text-ink">{s.composite ?? '—'}</span>
                </span>
              </li>
            ))}
          </ul>
        </Card>
      )}
    </div>
  )
}

function Milestones({ o }: { o: StudentOverview }) {
  const list = achievements({ attempts: o.history, benchmarks: o.benchmarks, longestStreak: o.streak.longest_streak, goalsMet: o.goalsMet })
  const earned = list.filter((a) => a.earned)
  const next = list.filter((a) => !a.earned).sort((a, b) => b.progress / b.goal - a.progress / a.goal).slice(0, 2)
  return (
    <Card>
      <CardHeader title={<span className="flex items-center gap-2"><Trophy size={18} /> Milestones</span>} subtitle={`${earned.length} of ${list.length} earned`} />
      <div className="grid gap-4 p-5 pt-3">
        {earned.length > 0 && (
          <ul className="flex flex-wrap gap-1.5">
            {earned.map((a) => (
              <li key={a.key} title={a.description}>
                <Pill tone="gold">{a.title}</Pill>
              </li>
            ))}
          </ul>
        )}
        {next.length > 0 && (
          <ul className="grid gap-3">
            {next.map((a) => (
              <li key={a.key}>
                <div className="mb-1 flex justify-between gap-2 text-sm">
                  <span className="text-ink-2">
                    <span className="font-semibold text-ink">{a.title}</span> · {a.description}
                  </span>
                  <span className="tabular text-ink-3">
                    {a.progress}/{a.goal}
                  </span>
                </div>
                <ProgressBar value={a.progress} max={a.goal} tone="gold" label={`${a.title} progress`} className="h-1.5" />
              </li>
            ))}
          </ul>
        )}
      </div>
    </Card>
  )
}

function MiniStat({ label, value, flat }: { label: string; value: string; flat?: boolean }) {
  return (
    <div className={cx('rounded-2xl p-4', flat ? 'bg-surface-2' : 'border border-line bg-surface shadow-card')}>
      <div className="text-xl font-semibold tabular text-ink">{value}</div>
      <div className="mt-0.5 text-xs text-ink-3">{label}</div>
    </div>
  )
}

function WeeklyChart({ data }: { data: { week: string; n: number; acc: number | null }[] }) {
  const W = 640
  const H = 180
  const pad = { l: 28, r: 28, t: 12, b: 26 }
  const maxN = Math.max(10, ...data.map((d) => d.n))
  const bw = (W - pad.l - pad.r) / data.length
  const y = (n: number) => pad.t + (H - pad.t - pad.b) * (1 - n / maxN)
  const ya = (a: number) => pad.t + (H - pad.t - pad.b) * (1 - a)
  const pts = data.map((d, i) => (d.acc === null ? null : { x: pad.l + bw * i + bw / 2, y: ya(d.acc), a: d.acc }))
  const line = pts.filter(Boolean) as { x: number; y: number; a: number }[]
  return (
    <div className="px-3 pb-4 pt-2">
      <svg viewBox={`0 0 ${W} ${H}`} className="h-auto w-full" role="img" aria-label={data.map((d) => `Week of ${formatShortDate(d.week)}: ${d.n} answered${d.acc === null ? '' : `, ${Math.round(d.acc * 100)}% correct`}`).join('; ')}>
        {[0, 0.5, 1].map((t) => (
          <g key={t}>
            <line x1={pad.l} x2={W - pad.r} y1={ya(t)} y2={ya(t)} stroke="var(--line)" strokeDasharray={t === 0 ? undefined : '3 4'} />
            <text x={W - pad.r + 4} y={ya(t) + 4} fontSize="10" fill="var(--ink-3)">
              {Math.round(t * 100)}%
            </text>
          </g>
        ))}
        {data.map((d, i) => (
          <g key={d.week}>
            <rect x={pad.l + bw * i + bw * 0.22} width={bw * 0.56} y={y(d.n)} height={Math.max(0, H - pad.b - y(d.n))} rx={4} fill="var(--brand-soft)" stroke="var(--brand)" strokeOpacity={0.25} />
            <text x={pad.l + bw * i + bw / 2} y={H - 8} fontSize="10" textAnchor="middle" fill="var(--ink-3)">
              {formatShortDate(d.week)}
            </text>
            {d.n > 0 && (
              <text x={pad.l + bw * i + bw / 2} y={y(d.n) - 4} fontSize="10" textAnchor="middle" fill="var(--ink-2)" fontWeight={600}>
                {d.n}
              </text>
            )}
          </g>
        ))}
        {line.length > 1 && <polyline points={line.map((p) => `${p.x},${p.y}`).join(' ')} fill="none" stroke="var(--go)" strokeWidth={2.5} strokeLinejoin="round" />}
        {line.map((p, i) => (
          <circle key={i} cx={p.x} cy={p.y} r={4} fill="var(--surface)" stroke="var(--go)" strokeWidth={2.5} />
        ))}
      </svg>
    </div>
  )
}
