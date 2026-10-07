import type { BenchmarkSummary, Strategy, TrapType } from '../../lib/data/types'
import { SECTION_LABEL, pacingVerdict } from '../../lib/engine/benchmark'
import { compareProgress, type SectionChange } from '../../lib/engine/progressCheck'
import { benchmarkRepeats } from '../../lib/engine/freshness'
import type { AttemptRecord } from '../../lib/data/types'
import { formatShortDate } from '../../lib/engine/dates'
import { formatDuration } from '../../lib/engine/dates'
import { ButtonLink, Card, CardHeader, Notice, Pill, ProgressBar, Ring } from '../../components/ui'
import { Bolt, Clock, Compass, Flag, Target } from '../../components/icons'

const pct = (x: number | null) => (x === null ? '—' : `${Math.round(x * 100)}%`)

export const PACE_COPY = {
  rushed: { label: 'Rushing?', tone: 'warn' as const },
  fast: { label: 'Quick', tone: 'info' as const },
  on_pace: { label: 'On pace', tone: 'go' as const },
  slow: { label: 'Needs speed', tone: 'warn' as const },
  unknown: { label: 'Not enough data', tone: 'neutral' as const },
}

export function BenchmarkResults({
  summary,
  traps,
  standalone = true,
  history = [],
  attempts = [],
  currentRepeats,
}: {
  summary: BenchmarkSummary
  strategies?: Strategy[]
  traps: TrapType[]
  skillName?: (k: string | null) => string | null
  standalone?: boolean
  /** Completed checks before this one, for the comparison with the baseline. */
  history?: BenchmarkSummary[]
  /** The student's answers (all time), to tell which check questions were seen before. */
  attempts?: AttemptRecord[]
  /** For the run just finished, whose attempts aren't in `attempts` yet. */
  currentRepeats?: Map<string, number>
}) {
  const repeatsOf = (b: BenchmarkSummary) => (b.id === summary.id && currentRepeats ? currentRepeats : benchmarkRepeats(b, attempts))
  const comparison = summary.kind === 'initial' ? null : compareProgress(summary, history, repeatsOf)
  const ownRepeats = [...repeatsOf(summary).values()].reduce((n, x) => n + x, 0)
  const m = summary.metrics
  const trapName = (k: string) => traps.find((t) => t.trap_key === k)?.name ?? k.replace(/_/g, ' ')
  const certain = m.calibration.find((c) => c.confidence === 3)
  const guess = m.calibration.find((c) => c.confidence === 1)
  const sections = [...m.sections].sort((a, b) => (a.accuracy ?? 0) - (b.accuracy ?? 0))
  const weakest = sections[0]
  const slowest = [...m.sections].filter((s) => s.pacing_ratio !== null).sort((a, b) => (b.pacing_ratio ?? 0) - (a.pacing_ratio ?? 0))[0]

  return (
    <div className={standalone ? 'mx-auto max-w-3xl px-4 py-8' : ''}>
      {standalone && (
        <div className="anim-rise flex flex-col items-center text-center">
          <Ring value={m.correct} max={Math.max(1, m.answered)} size={160} stroke={14} tone="brand" label={`${m.correct} of ${m.answered} correct`}>
            <div>
              <div className="display text-4xl font-semibold tabular text-ink">{pct(m.accuracy)}</div>
              <div className="text-xs font-semibold text-ink-3">right on these questions</div>
            </div>
          </Ring>
          <h1 className="display mt-5 text-3xl font-semibold text-ink">{summary.kind === 'initial' ? 'Your baseline is set' : 'Progress check complete'}</h1>
          <p className="mt-1 max-w-md text-ink-2">
            {m.correct} of {m.answered} answered correctly{m.skipped ? `, ${m.skipped} left blank` : ''}. Here is what that says about knowledge, pacing and test-taking — separately.
          </p>
        </div>
      )}

      <div className={standalone ? 'mt-8 grid gap-4' : 'grid gap-4'}>
        <ResultLabel />
        {ownRepeats > 0 && (
          <Notice tone="warn" title={`${ownRepeats} ${ownRepeats === 1 ? 'question' : 'questions'} in this check ${ownRepeats === 1 ? 'was' : 'were'} seen before`}>
            There weren't enough new questions left for a fully fresh check. Sections with repeats aren't compared, because answering a question you've seen
            isn't new evidence of improvement.
          </Notice>
        )}
        {comparison?.baseline && <Comparison changes={comparison.sinceBaseline} title={`Since your baseline (${formatShortDate(comparison.baseline.completed_at.slice(0, 10))})`} />}
        {comparison?.sinceLast && comparison.previous && <Comparison changes={comparison.sinceLast} title={`Since your last check (${formatShortDate(comparison.previous.completed_at.slice(0, 10))})`} />}
        <Card>
          <CardHeader title={<span className="flex items-center gap-2"><Target size={18} /> Knowledge by section</span>} subtitle="Share of answered questions you got right, and the hardest level you got right." />
          <div className="grid gap-4 p-5">
            {m.sections.map((s) => (
              <div key={s.section}>
                <div className="mb-1.5 flex items-baseline justify-between gap-2 text-sm">
                  <span className="font-semibold text-ink">{SECTION_LABEL[s.section] ?? s.section}</span>
                  <span className="tabular text-ink-2">
                    {s.correct}/{s.answered} · {pct(s.accuracy)}
                    {s.ceiling_difficulty ? ` · up to level ${s.ceiling_difficulty}` : ''}
                  </span>
                </div>
                <ProgressBar value={s.accuracy ?? 0} label={`${SECTION_LABEL[s.section]} accuracy`} tone={(s.accuracy ?? 0) < 0.6 ? 'warn' : 'go'} />
              </div>
            ))}
          </div>
        </Card>

        <div className="grid gap-4 md:grid-cols-2">
          <Card>
            <CardHeader title={<span className="flex items-center gap-2"><Clock size={18} /> Pacing</span>} subtitle="Your active time compared with test pace (1.0× = exactly on pace)." />
            <ul className="grid gap-3 p-5">
              {m.sections.map((s) => {
                const v = PACE_COPY[pacingVerdict(s.pacing_ratio)]
                return (
                  <li key={s.section} className="flex items-center justify-between gap-2 text-sm">
                    <span className="text-ink">{SECTION_LABEL[s.section] ?? s.section}</span>
                    <span className="flex items-center gap-2">
                      <span className="tabular text-ink-2">{s.pacing_ratio === null ? '—' : `${s.pacing_ratio.toFixed(2)}×`}</span>
                      <Pill tone={v.tone}>{v.label}</Pill>
                    </span>
                  </li>
                )
              })}
              {m.sections.some((s) => pacingVerdict(s.pacing_ratio) === 'rushed') && (
                <li><Notice tone="warn">Some answers came in far faster than anyone can work them. Rushed answers make the baseline less reliable.</Notice></li>
              )}
              {m.median_elapsed_ms !== null && <li className="pt-1 text-xs text-ink-3">Typical time per question: {formatDuration(m.median_elapsed_ms)}</li>}
            </ul>
          </Card>

          <Card>
            <CardHeader title={<span className="flex items-center gap-2"><Compass size={18} /> Confidence</span>} subtitle="How well your sense of certainty matched the result." />
            <div className="grid gap-3 p-5 text-sm">
              <CalRow label="When you said “Certain”" c={certain} />
              <CalRow label="When you said “Fairly sure”" c={m.calibration.find((c) => c.confidence === 2)} />
              <CalRow label="When you were guessing" c={guess} />
              {certain && certain.answered >= 3 && certain.correct / certain.answered < 0.75 && (
                <Notice tone="warn">You were sometimes certain and wrong. Slow down on questions that feel easy — that is where traps live.</Notice>
              )}
            </div>
          </Card>
        </div>

        <Card>
          <CardHeader title={<span className="flex items-center gap-2"><Flag size={18} /> Test-taking habits</span>} />
          <div className="grid grid-cols-3 gap-3 px-5 pt-4">
            <Habit label="Skipped, then returned" value={m.returns} />
            <Habit label="Left blank" value={m.skipped} />
            <Habit label="Changed answers" value={m.answer_changes} />
          </div>
          <div className="p-5">
            {m.traps_fallen.length > 0 ? (
              <>
                <div className="text-sm font-semibold text-ink">Traps that caught you</div>
                <div className="mt-2 flex flex-wrap gap-2">
                  {m.traps_fallen.map((t) => (
                    <Pill key={t.trap} tone="warn">
                      {trapName(t.trap)} ×{t.count}
                    </Pill>
                  ))}
                </div>
              </>
            ) : (
              <p className="text-sm text-ink-3">No repeated trap patterns this time.</p>
            )}
          </div>
        </Card>

        <Card className="border-brand/20 bg-brand-soft">
          <div className="p-5">
            <div className="flex items-center gap-2 font-semibold text-ink">
              <Bolt size={18} /> What happens next
            </div>
            <ul className="mt-2 grid gap-1.5 text-sm text-ink-2">
              {weakest && <li>Daily practice will lead with {SECTION_LABEL[weakest.section] ?? weakest.section}, your lowest-accuracy section.</li>}
              {slowest && pacingVerdict(slowest.pacing_ratio) === 'slow' && <li>{SECTION_LABEL[slowest.section]} is accurate enough to work on speed next.</li>}
              <li>Every practice question updates your skill estimates. A mini benchmark in about 5 weeks will show the change.</li>
            </ul>
            <p className="mt-3 text-xs text-ink-3">
              A scaled score estimate needs a calibrated scoring model, which isn't connected yet. We won't show a number we can't stand behind.
            </p>
          </div>
        </Card>

        {standalone && (
          <ButtonLink to="/student" size="lg" block>
            See today's plan
          </ButtonLink>
        )}
      </div>
    </div>
  )
}

/** What these numbers are, and are not. Shown on every benchmark result. */
export function ResultLabel() {
  return (
    <Notice tone="neutral" title="Practice results, not a test score">
      Original practice questions written for Prep & Price and checked for answer accuracy; not official ACT or SAT items. Percent right describes these
      questions only. It isn't converted to an ACT or SAT score, because no scoring model has been checked against real test results.
    </Notice>
  )
}

const VERDICT: Record<SectionChange['verdict'], { label: string; tone: 'go' | 'warn' | 'neutral' }> = {
  up: { label: 'Clear improvement', tone: 'go' },
  down: { label: 'Clear drop', tone: 'warn' },
  within_noise: { label: 'Within normal variation', tone: 'neutral' },
  too_few: { label: 'Too few answers to tell', tone: 'neutral' },
  not_clean: { label: 'Not a clean comparison', tone: 'neutral' },
}

function Comparison({ changes, title }: { changes: SectionChange[]; title: string }) {
  return (
    <Card>
      <CardHeader title={title} subtitle="Different questions each time, a few per section. A change counts as clear only when it's bigger than chance usually produces." />
      <ul className="grid gap-3 p-5 text-sm">
        {changes.map((c) => {
          const v = VERDICT[c.verdict]
          return (
            <li key={c.section} className="flex flex-wrap items-center justify-between gap-2">
              <span className="font-semibold text-ink">{SECTION_LABEL[c.section] ?? c.section}</span>
              <span className="flex flex-wrap items-center gap-2">
                <span className="tabular text-ink-2">
                  {c.then ? `${c.then.correct}/${c.then.answered} → ` : 'Not in that check · '}
                  {c.now.correct}/{c.now.answered}
                  {c.delta != null && c.then ? ` (${c.delta >= 0 ? '+' : '−'}${Math.round(Math.abs(c.delta) * 100)} points)` : ''}
                </span>
                {c.then && <Pill tone={v.tone}>{v.label}</Pill>}
              </span>
              {c.verdict === 'not_clean' && (
                <span className="basis-full text-xs text-ink-3">
                  {c.repeatsNow + c.repeatsThen} {c.repeatsNow + c.repeatsThen === 1 ? 'question was' : 'questions were'} seen before. Recall isn't new evidence, so this change isn't judged.
                </span>
              )}
            </li>
          )
        })}
      </ul>
    </Card>
  )
}

function CalRow({ label, c }: { label: string; c?: { answered: number; correct: number } }) {
  return (
    <div className="flex items-center justify-between gap-2">
      <span className="text-ink-2">{label}</span>
      <span className="font-semibold tabular text-ink">{c && c.answered ? `${c.correct}/${c.answered} right` : '—'}</span>
    </div>
  )
}

function Habit({ label, value }: { label: string; value: number }) {
  return (
    <div className="rounded-xl bg-surface-2 p-3">
      <div className="text-2xl font-semibold tabular text-ink">{value}</div>
      <div className="text-xs text-ink-3">{label}</div>
    </div>
  )
}
