import { Link } from 'react-router-dom'
import type { BenchmarkSummary } from '../lib/data/types'
import { SECTION_LABEL, benchmarkImprovement, benchmarkSchedule } from '../lib/engine/benchmark'
import { formatShortDate } from '../lib/engine/dates'
import { ArrowRight, Compass } from './icons'
import { Card, CardHeader, Pill, cx } from './ui'

const KIND_LABEL = { initial: 'Starting benchmark', mini: 'Mini benchmark', full: 'Full benchmark' } as const
const KIND_LENGTH = { initial: 'About 30 minutes', mini: 'About 15 minutes', full: 'About an hour · best before a real test' } as const

function Delta({ pts, unit = ' pts', invert = false }: { pts: number | null; unit?: string; invert?: boolean }) {
  if (pts === null) return <span className="text-ink-3">—</span>
  const good = invert ? pts < 0 : pts > 0
  const flat = pts === 0
  return (
    <span className={cx('font-semibold tabular', flat ? 'text-ink-2' : good ? 'text-go' : 'text-warn')}>
      {pts > 0 ? '+' : ''}
      {pts}
      {unit}
    </span>
  )
}

/**
 * Benchmark cadence: what is due next and what changed since the last one. Benchmarks are separate from daily
 * practice: they count toward streak and XP, but never mark today's practice done.
 */
export function BenchmarkStatus({ history, forGuardian = false, today = new Date() }: { history: BenchmarkSummary[]; forGuardian?: boolean; today?: Date }) {
  const next = benchmarkSchedule(history, today)
  const change = benchmarkImprovement(history)
  const last = [...history].sort((a, b) => b.completed_at.localeCompare(a.completed_at))[0]
  const due = next.inDays === 0
  const who = forGuardian ? 'They' : 'You'

  return (
    <Card>
      <CardHeader
        title={<span className="flex items-center gap-2"><Compass size={18} /> Benchmarks</span>}
        subtitle={history.length ? `${history.length} taken · last ${formatShortDate(last!.completed_at)}` : 'Not taken yet'}
      />
      <div className="grid gap-4 p-5 pt-3 text-sm">
        <div className={cx('rounded-2xl p-4', due ? 'bg-brand-soft' : 'bg-surface-2')}>
          <div className="flex flex-wrap items-center gap-2">
            <span className="font-semibold text-ink">{KIND_LABEL[next.kind]}</span>
            {due ? <Pill tone="brand">{next.overdueDays > 0 ? `Due ${next.overdueDays} day${next.overdueDays === 1 ? '' : 's'} ago` : 'Due now'}</Pill> : <Pill>In {next.inDays} days · {formatShortDate(next.dueDate)}</Pill>}
          </div>
          <p className="mt-1 text-ink-2">
            {KIND_LENGTH[next.kind]}. {next.kind === 'initial' ? `${who} get a starting point for knowledge, pacing and habits.` : `It shows what changed. Daily practice still counts that day.`}
          </p>
          {due && !forGuardian && (
            <Link to={`/student/benchmark${next.kind === 'initial' ? '' : `?kind=${next.kind}`}`} className="mt-2 inline-flex items-center gap-1 font-semibold text-brand hover:underline">
              Start the {next.kind === 'full' ? 'full' : next.kind === 'mini' ? 'mini' : ''} benchmark <ArrowRight size={16} />
            </Link>
          )}
        </div>

        {change ? (
          <div>
            <div className="font-semibold text-ink">Since the previous benchmark ({formatShortDate(change.from.completed_at)})</div>
            <dl className="mt-2 grid grid-cols-2 gap-2">
              <div className="rounded-xl border border-line p-3">
                <dt className="text-xs text-ink-3">Accuracy</dt>
                <dd className="mt-0.5 text-lg"><Delta pts={change.accuracyPts} /></dd>
              </div>
              <div className="rounded-xl border border-line p-3">
                <dt className="text-xs text-ink-3">Time vs test pace</dt>
                <dd className="mt-0.5 text-lg"><Delta pts={change.pacingDelta} unit="×" invert /></dd>
              </div>
            </dl>
            <ul className="mt-2 flex flex-wrap gap-1.5">
              {change.sections.map((s) => (
                <li key={s.section} className="rounded-full bg-surface-2 px-2.5 py-1 text-xs">
                  {SECTION_LABEL[s.section] ?? s.section} <Delta pts={s.accuracyPts} />
                  {s.ceilingDelta !== null && s.ceilingDelta > 0 && <span className="text-go"> · harder level</span>}
                </li>
              ))}
            </ul>
            <p className="mt-2 text-xs text-ink-3">Benchmarks adapt to the student, so question difficulty varies. Treat changes as a guide, not an official score change.</p>
          </div>
        ) : history.length === 1 ? (
          <p className="text-ink-3">Improvement shows after the next benchmark.</p>
        ) : null}
      </div>
    </Card>
  )
}
