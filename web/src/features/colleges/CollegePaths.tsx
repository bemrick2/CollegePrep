import { useMemo, useState } from 'react'
import { useApp } from '../../lib/app'
import { BASIS_LABEL, meritAwards, type ReferenceScore } from '../../lib/engine/merit'
import { useMeritReference } from './useMeritReference'
import { useInterests } from '../majors/useInterests'
import { SchoolFitRow } from '../majors/SchoolFitRow'
import { CollegesTabs } from './CollegesTabs'
import { HomeStateControl } from './HomeStateControl'
import { useHomeState } from '../../lib/homeState'
import type { SavedInterest } from '../../lib/engine/interests'
import { Link } from 'react-router-dom'
import { schoolLevers } from './schoolLevers'
import { CostLeverList } from './CostLeverList'
import type { InstitutionComparison } from '../../lib/data/types'
import {
  HOURS_PER_SEMESTER,
  examOptions,
  summarizeSchool,
  type CreditPolicy,
  type ExamFamily,
  type ExamMatch,
  type PlannedExam,
} from '../../lib/engine/examCredit'
import { formatShortDate } from '../../lib/engine/dates'
import { costPhrase, outlookFor } from '../parent/CostOutlook'
import { useSavedComparison, COMPARE_YEAR } from './useSavedComparison'
import { useExamPlan } from './useExamPlan'
import { Book, Check, Clock, Sparkle, Trophy, Wallet, Info, School, X } from '../../components/icons'
import { ButtonLink, Card, EmptyState, Notice, PageLoading, Pill, cx, inputClass } from '../../components/ui'

const usd = (n: number) =>
  n.toLocaleString(undefined, {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  })
const SCORE_RANGE: Record<ExamFamily, [number, number]> = {
  AP: [1, 5],
  CLEP: [20, 80],
}


const policiesOf = (c: InstitutionComparison) => (c.domains.credit_policies ?? []) as unknown as CreditPolicy[]

/**
 * College paths: ways to finish a degree at the four-year schools the family saved, built only from each school's
 * verified published policies. Exam credit is matched to the school's own equivalency table; no time or money saved
 * is estimated, and no transfer is implied unless a verified transfer policy is on file.
 */
export function CollegePaths() {
  const { activeStudent, viewer } = useApp()
  const cmp = useSavedComparison(COMPARE_YEAR)
  const plan = useExamPlan(activeStudent?.id)
  const { exam: examFamily, reference: ref } = useMeritReference(activeStudent?.id)
  const interests = useInterests(activeStudent?.id).profile.interests
  const schools = (cmp.data ?? []).filter((c) => c.found)
  // The family's primary target (CR-12), when set, leads.
  const four = schools
    .filter((c) => c.institution?.level !== 'two_year')
    .sort((a, b) => Number(b.institution_key === cmp.primary) - Number(a.institution_key === cmp.primary))
  const two = schools.filter((c) => c.institution?.level === 'two_year')
  const options = useMemo(() => examOptions(four.map(policiesOf)), [cmp.data])
  const isStudent = !!viewer && activeStudent?.linked_user_id === viewer.userId
  const who = isStudent ? 'you' : (activeStudent?.display_name ?? 'your student')

  return (
    <div className="grid grid-cols-1 gap-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">Colleges & cost</p>
          <h1 className="display text-[30px] font-semibold leading-tight text-ink md:text-[36px]">College paths</h1>
          <p className="mt-1 max-w-2xl text-sm text-ink-2">
            Ways to finish a degree at the schools you saved, from each school's verified, published policies. Credit only counts where a school's own table
            lists it.
          </p>
        </div>
        <CollegesTabs />
      </div>

      {cmp.keys.length === 0 ? (
        <Card>
          <EmptyState icon={<School size={32} />} title="Save schools first" action={<ButtonLink to="/colleges">Choose schools</ButtonLink>}>
            Paths compare the four-year schools you've saved: the standard four years, exam credit and dual enrollment.
          </EmptyState>
        </Card>
      ) : cmp.loading && !cmp.data ? (
        <PageLoading />
      ) : cmp.error ? (
        <Notice tone="bad">{cmp.error.message}</Notice>
      ) : (
        <>
          <HomeStateControl />
          <ExamPlanner who={who} options={options} plan={plan} />
          {four.length === 0 ? (
            <Notice tone="neutral">None of your saved schools is a four-year college yet. Add one on the Compare tab.</Notice>
          ) : (
            <>
              {cmp.canSetPrimary && !cmp.primary && four.length > 1 && (
                <p className="text-sm text-ink-2">
                  Mark the school {who === 'you' ? 'you most want' : `${who} most wants`} to attend as the{' '}
                  <span className="font-semibold text-ink">primary target</span>. The overview then focuses on its path.
                </p>
              )}
              <div className={cx('grid grid-cols-1 items-start gap-4', four.length > 1 && 'lg:grid-cols-2')}>
                {four.map((c) => (
                  <PathCard
                    key={c.institution_key}
                    c={c}
                    exams={plan.exams}
                    interests={interests}
                    exam={examFamily}
                    reference={ref}
                    primary={cmp.primary === c.institution_key}
                    anyPrimary={!!cmp.primary}
                    onPrimary={cmp.canSetPrimary ? (on) => void cmp.setPrimary(on ? c.institution_key : null) : undefined}
                  />
                ))}
              </div>
            </>
          )}
          {two.length > 0 && (
            <p className="flex gap-2 text-xs text-ink-3">
              <Info size={14} className="mt-0.5 shrink-0" />
              {two.map((c) => c.institution?.display_name).join(', ')} {two.length === 1 ? 'is a 2-year college' : 'are 2-year colleges'}. A transfer route
              appears here only once a verified transfer agreement is on file.
            </p>
          )}
          <Notice tone="neutral" title="How to read this">
            Exam credit is matched to each school's published table for {COMPARE_YEAR}; whether a course counts toward a specific major is the school's
            decision. We don't estimate semesters or money saved: many schools charge a flat full-time rate, and credit shortens a degree only when it covers
            required courses.
          </Notice>
        </>
      )}
    </div>
  )
}

function ExamPlanner({
  who,
  options,
  plan,
}: {
  who: string
  options: { family: ExamFamily; key: string; name: string }[]
  plan: ReturnType<typeof useExamPlan>
}) {
  const [pick, setPick] = useState('')
  const available = options.filter((o) => !plan.exams.some((e) => e.key === o.key))
  const add = (key: string) => {
    const o = options.find((x) => x.key === key)
    if (o) plan.add({ family: o.family, key: o.key, name: o.name, score: null })
    setPick('')
  }
  const possessive = who === 'you' ? 'your' : `${who}'s`

  return (
    <Card className="p-5 lg:max-w-3xl">
      <div className="flex items-center gap-2">
        <Book size={18} />
        <h2 className="font-semibold text-ink">{who === 'you' ? 'Your' : `${possessive.charAt(0).toUpperCase()}${possessive.slice(1)}`} AP and CLEP exams</h2>
      </div>
      <p className="mt-1 text-sm text-ink-2">Add exams {who} took or plan to take. Leave the score as “Planned” to see what each school requires.</p>

      {plan.exams.length > 0 && (
        <ul className="mt-4 grid gap-2">
          {plan.exams.map((e) => (
            <ExamRow key={e.key} exam={e} onScore={(s) => plan.setScore(e.key, s)} onRemove={() => plan.remove(e.key)} />
          ))}
        </ul>
      )}

      {options.length === 0 ? (
        <p className="mt-4 text-sm text-ink-3">None of your saved four-year schools has a verified AP or CLEP table yet.</p>
      ) : (
        <div className="mt-4">
          <label htmlFor="add-exam" className="text-sm font-semibold text-ink">
            Add an exam
          </label>
          <select
            id="add-exam"
            className={cx(inputClass, 'mt-1.5')}
            value={pick}
            onChange={(e) => add(e.target.value)}
            disabled={plan.exams.length >= plan.max}
          >
            <option value="">Choose an exam…</option>
            {(['AP', 'CLEP'] as ExamFamily[]).map((f) => (
              <optgroup key={f} label={f}>
                {available
                  .filter((o) => o.family === f)
                  .map((o) => (
                    <option key={o.key} value={o.key}>
                      {o.name}
                    </option>
                  ))}
              </optgroup>
            ))}
          </select>
          <p className="mt-1.5 text-xs text-ink-3">Exams listed by your saved schools' published tables. Saved on this device for now.</p>
        </div>
      )}
    </Card>
  )
}

function ExamRow({ exam, onScore, onRemove }: { exam: PlannedExam; onScore: (s: number | null) => void; onRemove: () => void }) {
  const [lo, hi] = SCORE_RANGE[exam.family]
  const scores = exam.family === 'AP' ? [1, 2, 3, 4, 5] : null
  return (
    <li className="flex items-center gap-2 rounded-xl border border-line p-2 pl-3">
      <span className="min-w-0 flex-1 text-sm font-semibold text-ink">{exam.name}</span>
      {scores ? (
        <select
          aria-label={`${exam.name} score`}
          className="rounded-lg border border-line-strong bg-surface px-2 py-1.5 text-sm"
          value={exam.score ?? ''}
          onChange={(e) => onScore(e.target.value ? Number(e.target.value) : null)}
        >
          <option value="">Planned</option>
          {scores.map((s) => (
            <option key={s} value={s}>
              Score {s}
            </option>
          ))}
        </select>
      ) : (
        <input
          aria-label={`${exam.name} score`}
          inputMode="numeric"
          placeholder="Planned"
          className="w-24 rounded-lg border border-line-strong bg-surface px-2 py-1.5 text-sm"
          value={exam.score ?? ''}
          onChange={(e) => {
            const n = Number(e.target.value)
            onScore(e.target.value === '' || Number.isNaN(n) ? null : Math.max(lo, Math.min(hi, Math.round(n))))
          }}
        />
      )}
      <button
        onClick={onRemove}
        aria-label={`Remove ${exam.name}`}
        className="grid h-8 w-8 shrink-0 place-items-center rounded-full text-ink-3 hover:bg-surface-2 hover:text-ink"
      >
        <X size={16} />
      </button>
    </li>
  )
}

function PathCard({
  c,
  exams,
  interests,
  exam,
  reference,
  primary = false,
  anyPrimary = false,
  onPrimary,
}: {
  c: InstitutionComparison
  exams: PlannedExam[]
  interests: SavedInterest[]
  exam: 'act' | 'sat'
  reference: ReferenceScore | null
  primary?: boolean
  anyPrimary?: boolean
  /** Present only where a primary target can be stored (CR-12). */
  onPrimary?: (on: boolean) => void
}) {
  const policies = policiesOf(c)
  const { homeState } = useHomeState()
  const outlook = outlookFor(c, homeState)
  const credit = summarizeSchool(policies, exams)
  const ap = policies.find((p) => p.policy_kind === 'AP') ?? policies.find((p) => p.policy_kind === 'CLEP')
  const dual = policies.find((p) => p.policy_kind === 'dual_enrollment')
  const statewide = policies.find((p) => p.policy_kind === 'statewide_dual_credit')
  const transfer = (
    (c.domains.transfer_policies ?? []) as {
      policy_url?: string
      source_url?: string
    }[]
  )[0]
  const name = outlook.name
  const semesters = Math.floor(credit.publishedHours / HOURS_PER_SEMESTER)
  const levers = schoolLevers(c, exams, exam, reference)

  return (
    <Card as="article" className={cx('min-w-0 overflow-hidden', primary && 'ring-2 ring-brand')}>
      <div className="flex flex-wrap items-start justify-between gap-2 border-b border-line p-5">
        <div className="min-w-0">
          {primary && <div className="mb-1 text-xs font-bold uppercase tracking-wide text-brand">Primary target</div>}
          <h2 className="display text-xl font-semibold leading-tight text-ink">{name}</h2>
          <p className="mt-0.5 text-sm text-ink-3">{[c.institution?.city, c.institution?.state_code].filter(Boolean).join(', ')}</p>
        </div>
        {onPrimary && (
          <button
            onClick={() => onPrimary(!primary)}
            aria-pressed={primary}
            className={cx(
              'rounded-full border px-3 py-1 text-xs font-semibold',
              primary ? 'border-line text-ink-2 hover:bg-surface-2' : 'border-brand text-brand hover:bg-brand-soft',
            )}
          >
            {primary ? 'Clear primary' : 'Make primary target'}
          </button>
        )}
      </div>
      <ol className="grid grid-cols-1 divide-y divide-line">
        <Route icon={<Clock size={16} />} title="Standard path" tag="4 years · 8 semesters">
          {(() => {
            const c = costPhrase(outlook)
            return (
              <>
                <p className={c.amount ? undefined : 'text-ink-3'}>
                  {c.amount && <span className="font-semibold tabular text-ink">{c.amount} </span>}
                  {c.amount ? c.label : c.label + '.'}
                </p>
                {c.note && <p className="mt-1 text-xs text-warn">{c.note}</p>}
              </>
            )
          })()}
        </Route>

        <Route icon={<Sparkle size={16} />} title="Your interests">
          {interests.length ? (
            <SchoolFitRow compact name={name} domains={c.domains} interests={interests} />
          ) : (
            <p className="text-ink-3">
              <Link to="/colleges/majors" className="font-semibold text-brand hover:underline">Add interests</Link> to see which of them {name} offers. Not sure yet is fine.
            </p>
          )}
        </Route>

        <Route icon={<Wallet size={16} />} title="Ways to lower this cost">
          <CostLeverList levers={levers} max={primary ? undefined : 3} expandable />
          <p className="mt-2 text-xs text-ink-3">
            From {name}'s verified records. Awards may not combine and aid depends on family finances, so no total is estimated.
          </p>
        </Route>

        <li>
          <details open={primary || !anyPrimary} className="group">
            <summary className="cursor-pointer list-none px-5 py-3 text-sm font-semibold text-brand hover:bg-surface-2">
              <span className="group-open:hidden">Show scholarship, exam-credit and dual-enrollment details</span>
              <span className="hidden group-open:inline">Hide details</span>
            </summary>
            <ol className="grid grid-cols-1 divide-y divide-line border-t border-line">
              <MeritRoute c={c} exam={exam} reference={reference} />

              {!credit.hasTable && !dual && !statewide ? (
                <Route icon={<Book size={16} />} title="Exam credit and dual enrollment">
                  <p className="text-ink-3">No verified AP, CLEP or dual-enrollment policy yet. Check {name}'s site.</p>
                </Route>
              ) : (
                <>
                  <Route icon={<Book size={16} />} title="With exam credit" source={ap?.policy_url ?? ap?.source_url} verified={ap?.last_verified_at}>
                    {!credit.hasTable ? (
                      <p className="text-ink-3">No verified AP or CLEP credit table yet. Check the school's site.</p>
                    ) : exams.length === 0 ? (
                      <p className="text-ink-3">Add exams above to see what {name} awards.</p>
                    ) : (
                      <>
                        <p>
                          {credit.courses > 0 ? (
                            <>
                              <span className="font-semibold text-ink">
                                {credit.courses} of {exams.length}
                              </span>{' '}
                              exams earn credit at the listed scores
                              {credit.publishedHours > 0 && (
                                <>
                                  {' '}
                                  · <span className="font-semibold tabular text-ink">{credit.publishedHours}</span> published credit hours
                                </>
                              )}
                              {credit.coursesWithoutHours > 0 && <> · {credit.coursesWithoutHours} with hours not listed</>}.
                            </>
                          ) : (
                            <>
                              None of the listed scores earns credit yet
                              {exams.some((e) => e.score == null) ? ' — planned exams show the score needed' : ''}.
                            </>
                          )}
                        </p>
                        {semesters > 0 && (
                          <p className="mt-1 text-xs text-ink-3">
                            That's about {semesters} semester
                            {semesters === 1 ? '' : 's'} of hours, which can shorten the degree only if the courses count toward its requirements.
                          </p>
                        )}
                        <ul className="mt-3 grid gap-2">
                          {credit.matches.map((m) => (
                            <MatchRow key={m.exam.key} m={m} />
                          ))}
                        </ul>
                      </>
                    )}
                  </Route>

                  <Route
                    icon={<School size={16} />}
                    title="Dual enrollment in high school"
                    source={dual?.policy_url ?? dual?.source_url}
                    verified={dual?.last_verified_at}
                  >
                    {dual || statewide ? (
                      <div className="flex flex-wrap gap-1.5">
                        {dual && <Pill tone="go">Verified dual-enrollment policy</Pill>}
                        {statewide && (
                          <Pill tone="go">
                            Statewide dual credit
                            {statewide.equivalency_count ? ` · ${statewide.equivalency_count} courses` : ''}
                          </Pill>
                        )}
                        <p className="w-full text-xs text-ink-3">
                          Read the policy for GPA and eligibility rules; how credit from another college counts depends on its transfer evaluation.
                        </p>
                      </div>
                    ) : (
                      <p className="text-ink-3">No verified dual-enrollment policy yet.</p>
                    )}
                  </Route>
                </>
              )}

              {transfer && (
                <Route icon={<Check size={16} />} title="Transfer credit" source={transfer.policy_url ?? transfer.source_url}>
                  <p>A verified transfer-credit policy is on file. Course-by-course transfer still depends on the school's evaluation.</p>
                </Route>
              )}
            </ol>
          </details>
        </li>
      </ol>
    </Card>
  )
}

function Route({
  icon,
  title,
  tag,
  source,
  verified,
  children,
}: {
  icon: React.ReactNode
  title: string
  tag?: string
  source?: string | null
  verified?: string | null
  children: React.ReactNode
}) {
  return (
    <li className="p-5 text-sm text-ink-2">
      <div className="mb-1.5 flex flex-wrap items-center gap-x-2 gap-y-1">
        <span className="grid h-7 w-7 place-items-center rounded-full bg-surface-2 text-ink-2" aria-hidden>
          {icon}
        </span>
        <h3 className="font-semibold text-ink">{title}</h3>
        {tag && <Pill>{tag}</Pill>}
        {source && (
          <a href={source} target="_blank" rel="noreferrer" className="ml-auto text-[11px] font-semibold text-ink-3 hover:text-ink hover:underline">
            Source{verified ? ` · ${formatShortDate(verified)}` : ''} ↗
          </a>
        )}
      </div>
      <div className="min-w-0 pl-9">{children}</div>
    </li>
  )
}

function MatchRow({ m }: { m: ExamMatch }) {
  const rows = m.status === 'qualifies' ? m.earned : m.thresholds.filter((t) => t.min === m.lowest)
  const course = rows
    .map((t) => t.course)
    .filter(Boolean)
    .join(' / ')
  const hours = rows.length && rows.every((t) => t.credits != null) ? Math.min(...rows.map((t) => t.credits!)) : null
  const status: Record<ExamMatch['status'], { tone: 'go' | 'warn' | 'neutral'; label: string }> = {
    qualifies: { tone: 'go', label: `Your ${m.exam.score} earns credit` },
    below: {
      tone: 'warn',
      label: `Needs ${m.lowest}+ (yours: ${m.exam.score})`,
    },
    planned: { tone: 'neutral', label: `Needs ${m.lowest}+` },
    not_awarded: { tone: 'neutral', label: 'No credit at any score' },
    not_listed: { tone: 'neutral', label: 'Not in the published table' },
    no_table: { tone: 'neutral', label: 'No table' },
  }
  const s = status[m.status]
  return (
    <li className="rounded-xl bg-surface-2 p-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <span className="font-semibold text-ink">{m.exam.name}</span>
        <Pill tone={s.tone}>{s.label}</Pill>
      </div>
      {course && m.status !== 'not_awarded' && (
        <p className="mt-1 text-xs text-ink-2">
          {m.status === 'qualifies' ? 'Counts as' : 'Would count as'} {course}
          {hours != null ? ` · ${hours} hrs` : ' · hours not listed'}
        </p>
      )}
      {m.status === 'not_listed' && <p className="mt-1 text-xs text-ink-3">Ask the school; the table may use a different exam name.</p>}
    </li>
  )
}

const EXAM_LABEL = { act: 'ACT', sat: 'SAT' } as const

/** Merit scholarships with a plainly published test minimum, compared with an official, self-reported (labelled)
 *  or target score. Never a practice estimate, and never stated as eligibility. */
function MeritRoute({ c, exam, reference }: { c: InstitutionComparison; exam: 'act' | 'sat'; reference: ReferenceScore | null }) {
  const merits = meritAwards(c.domains.awards)
  const scored = merits.filter((m) => m.min[exam] != null).sort((a, b) => a.min[exam]! - b.min[exam]!)
  const other = merits.length - scored.length
  const groups = [...scored.reduce((g, m) => g.set(m.min[exam]!, [...(g.get(m.min[exam]!) ?? []), m]), new Map<number, typeof scored>())]
  const label = EXAM_LABEL[exam]
  if (merits.length === 0)
    return (
      <Route icon={<Trophy size={16} />} title="Merit scholarships">
        <p className="text-ink-3">No verified merit scholarships yet.</p>
      </Route>
    )
  return (
    <Route icon={<Trophy size={16} />} title="Merit scholarships" tag={`${merits.length} verified`}>
      {scored.length > 0 ? (
        <ul className="grid grid-cols-1 gap-2">
          {groups.map(([min, awards]) => {
            const gap = reference ? min - reference.value : null
            return (
              <li key={min} className="rounded-xl bg-surface-2 p-3">
                <div className="flex flex-wrap items-center gap-1.5">
                  <Pill tone="gold">
                    {label} {min}+
                  </Pill>
                  {gap !== null &&
                    (gap <= 0 ? (
                      <Pill tone="go">{reference!.basis === 'target' ? 'Target meets it' : 'Score meets it'}</Pill>
                    ) : (
                      <Pill tone="warn">
                        {gap} above {reference!.basis === 'target' ? 'target' : 'score'}
                      </Pill>
                    ))}
                  <span className="text-xs text-ink-3">
                    {awards.length} award{awards.length === 1 ? '' : 's'}
                  </span>
                </div>
                <ul className="mt-2 grid grid-cols-1 gap-1.5">
                  {awards.map((m) => (
                    <li key={m.name} className="text-xs">
                      {m.sourceUrl ? (
                        <a href={m.sourceUrl} target="_blank" rel="noreferrer" className="font-semibold text-ink hover:underline">
                          {m.name}
                        </a>
                      ) : (
                        <span className="font-semibold text-ink">{m.name}</span>
                      )}
                      <span className="block truncate text-ink-2">
                        {m.amountText ?? (m.amountMax != null ? `Up to ${usd(m.amountMax)}` : 'Amount not published')}
                        {m.gpaText ? ` · GPA: ${m.gpaText}` : ''}
                      </span>
                    </li>
                  ))}
                </ul>
              </li>
            )
          })}
        </ul>
      ) : (
        <p>None states a single {label} minimum; their criteria are GPA-based or tiered.</p>
      )}
      {other > 0 && scored.length > 0 && <p className="mt-2 text-xs text-ink-3">{other} more with GPA-only or tiered criteria — see Compare.</p>}
      <p className="mt-2 text-xs text-ink-3">
        {reference ? `Compared with the ${BASIS_LABEL[reference.basis]} of ${reference.value}. ` : `Set a target ${label} score to see the gap. `}
        Published criteria only — not an eligibility decision; deadlines and other requirements apply.
      </p>
    </Route>
  )
}
