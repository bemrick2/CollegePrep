import { Link } from 'react-router-dom'
import type { BenchmarkSummary } from '../lib/data/types'
import { benchmarkSchedule } from '../lib/engine/benchmark'
import { formatShortDate } from '../lib/engine/dates'
import { ArrowRight, Compass } from './icons'
import { Card, CardHeader, Pill, cx } from './ui'

const KIND_LABEL = { initial: 'Starting benchmark', mini: 'Mini benchmark', full: 'Full benchmark' } as const
const KIND_LENGTH = { initial: 'About 30 minutes', mini: 'About 15 minutes', full: 'About an hour · best before a real test' } as const

/**
 * Benchmark cadence: what is due next. Benchmarks are separate from daily practice: they count toward streak and XP,
 * but never mark today's practice done. What changed between checks is shown only by the comparison that requires
 * like-for-like checks on fresh questions ('Am I improving?', engine/improving.ts), never as raw deltas here.
 */
export function BenchmarkStatus({ history, forGuardian = false, today = new Date() }: { history: BenchmarkSummary[]; forGuardian?: boolean; today?: Date }) {
  const next = benchmarkSchedule(history, today)
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

        {history.length >= 2 ? (
          <p className="text-ink-3">
            How the last checks compare is shown under “Am I improving?”. A change is judged only between like checks on questions not seen before.
          </p>
        ) : history.length === 1 ? (
          <p className="text-ink-3">A comparison is possible after the next benchmark, if it uses questions not seen before.</p>
        ) : null}
      </div>
    </Card>
  )
}
