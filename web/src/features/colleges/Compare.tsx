import { useEffect, useState, type ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { useApp } from '../../lib/app'
import type { InstitutionComparison } from '../../lib/data/types'
import { Notice, PageLoading, Pill, cx } from '../../components/ui'
import { PageHeader } from '../../components/layout'
import { X } from '../../components/icons'
import { useHomeState } from '../../lib/homeState'
import { meritAwards, type ReferenceScore } from '../../lib/engine/merit'
import { fitSentence, schoolFit } from '../../lib/engine/programFit'
import type { SavedInterest } from '../../lib/engine/interests'
import type { PlannedExam } from '../../lib/engine/examCredit'
import { costPhrase, outlookFor } from '../parent/CostOutlook'
import { useInterests } from '../majors/useInterests'
import { useSavedComparison } from './useSavedComparison'
import { useMeritReference } from './useMeritReference'
import { useExamPlan } from './useExamPlan'
import { schoolLevers } from './schoolLevers'
import { CollegesTabs } from './CollegesTabs'
import { HomeStateControl } from './HomeStateControl'
import { CONTROL_LABEL, DOMAIN_LABEL, POLICY_LABEL, academicFit, humanize } from './schoolBits'

/** How many items a variable-length row previews; the detail page shows everything. */
export const PREVIEW = 3
const LEVER_ORDER: Record<string, number> = { on_track: 0, within_reach: 1, stretch: 2, available: 3, check: 4 }
const usd = (n: number) => n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })

type School = InstitutionComparison & { institution: NonNullable<InstitutionComparison['institution']> }

interface Ctx {
  homeState: string | null
  exam: 'act' | 'sat'
  reference: ReferenceScore | null
  interests: SavedInterest[]
  exams: PlannedExam[]
  primary: string | null
}

const detailPath = (c: School, hash = '') => `/colleges/${encodeURIComponent(c.institution_key)}${hash}`

function NoRecord({ what = 'record' }: { what?: string }) {
  return <p className="text-sm text-ink-3">No verified {what} yet.</p>
}

function More({ c, n, noun, hash }: { c: School; n: number; noun: string; hash: string }) {
  return (
    <Link to={detailPath(c, hash)} className="mt-2 inline-block text-sm font-semibold text-brand hover:underline">
      View all {n} {noun}
    </Link>
  )
}

/**
 * The scholarships most useful for comparing: merit awards with a single published test minimum (nearest first),
 * then other merit awards, then everything else. Never reordered by amount, which schools publish unevenly.
 */
export function scholarshipPreview(c: InstitutionComparison, exam: 'act' | 'sat') {
  const raw = (c.domains.awards ?? []) as Record<string, unknown>[]
  const merit = meritAwards(c.domains.awards)
  const scored = merit.filter((m) => m.min[exam] != null).sort((a, b) => a.min[exam]! - b.min[exam]!)
  const seen = new Set<string>()
  const items: { name: string; detail: string; min: number | null; href: string | null }[] = []
  const push = (name: string, detail: string, min: number | null, href: string | null) => {
    if (seen.has(name)) return
    seen.add(name)
    items.push({ name, detail, min, href })
  }
  for (const m of [...scored, ...merit.filter((m) => m.min[exam] == null)])
    push(m.name, m.amountText ?? (m.amountMax != null ? `Up to ${usd(m.amountMax)}` : 'Amount not published'), m.min[exam] ?? null, m.sourceUrl)
  for (const a of raw)
    push(
      String(a.award_name ?? 'Unnamed award'),
      a.award_amount_text ? String(a.award_amount_text) : typeof a.award_max === 'number' ? `Up to ${usd(a.award_max)}` : 'Amount not published',
      null,
      a.source_url ? String(a.source_url) : null,
    )
  return { total: Math.max(raw.length, items.length), items, merit: merit.length, scored: scored.length }
}

interface RowDef {
  key: string
  label: string
  hint?: string
  cell: (c: School, x: Ctx) => ReactNode
}

const ROWS: RowDef[] = [
  {
    key: 'cost',
    label: 'Cost of attendance',
    hint: 'Published, for your family, before aid',
    cell: (c, x) => {
      const o = outlookFor(c, x.homeState)
      const cp = costPhrase(o)
      return cp.amount ? (
        <>
          <div className="figure text-[26px] text-ink">{cp.amount}</div>
          <p className="mt-1 text-sm text-ink-3">{cp.label}</p>
          {o.annual != null && <p className="text-sm text-ink-3">{usd(o.annual)} a year</p>}
          {cp.note && <p className="mt-1 text-sm text-warn">{cp.note}</p>}
        </>
      ) : (
        <>
          <div className="figure text-[26px] text-ink-3">—</div>
          <p className="mt-1 text-sm text-ink-3">{cp.label}</p>
          {cp.note && <p className="mt-1 text-sm text-warn">{cp.note}</p>}
        </>
      )
    },
  },
  {
    key: 'admissions',
    label: 'Admissions',
    hint: 'Middle 50% of admitted students',
    cell: (c, x) => {
      const adm = (c.domains.admissions_metrics?.[0] ?? null) as Record<string, number | null> | null
      if (!adm) return <NoRecord what="admissions data" />
      const fit = academicFit(c, x.exam, x.reference)
      const range = (e: 'act' | 'sat') => (adm[`${e}_25`] != null ? `${adm[`${e}_25`]}–${adm[`${e}_75`]}` : '—')
      const rate = typeof adm.admit_rate === 'number' ? `${Math.round(adm.admit_rate <= 1 ? adm.admit_rate * 100 : adm.admit_rate)}%` : '—'
      return (
        <>
          <dl className="grid grid-cols-3 gap-2 text-sm">
            {[
              ['ACT', range('act')],
              ['SAT', range('sat')],
              ['Admit rate', rate],
            ].map(([k, v]) => (
              <div key={k}>
                <dt className="text-ink-3">{k}</dt>
                <dd className="font-semibold tabular text-ink">{v}</dd>
              </div>
            ))}
          </dl>
          {fit && (
            <p className="mt-2 text-sm text-ink-2">
              {fit.whose} {fit.value} is <span className="font-semibold text-ink">{fit.where}</span> the middle 50%. Not an admission prediction.
            </p>
          )}
        </>
      )
    },
  },
  {
    key: 'scholarships',
    label: 'Scholarships',
    hint: `First ${PREVIEW}: published test minimums first`,
    cell: (c, x) => {
      const p = scholarshipPreview(c, x.exam)
      if (p.total === 0) return <NoRecord what="scholarships" />
      const E = x.exam.toUpperCase()
      return (
        <>
          <p className="text-sm text-ink-2">
            <span className="font-semibold text-ink">{p.total} verified</span>
            {p.merit > 0 && `, ${p.scored} with a published ${E} minimum`}
          </p>
          <ul className="mt-2 grid gap-2">
            {p.items.slice(0, PREVIEW).map((a) => (
              <li key={a.name} className="min-w-0 text-sm">
                <div className="flex items-baseline gap-2">
                  <span className="min-w-0 truncate font-semibold text-ink" title={a.name}>
                    {a.name}
                  </span>
                  {a.min != null && (
                    <Pill tone="gold" className="shrink-0">
                      {E} {a.min}+
                    </Pill>
                  )}
                </div>
                <div className="truncate text-ink-3" title={a.detail}>
                  {a.detail}
                </div>
              </li>
            ))}
          </ul>
          {p.total > PREVIEW && <More c={c} n={p.total} noun="scholarships" hash="#awards-heading" />}
        </>
      )
    },
  },
  {
    key: 'credit',
    label: 'Exam credit',
    hint: 'AP, IB, CLEP and dual enrollment',
    cell: (c) => {
      const policies = (c.domains.credit_policies ?? []) as { policy_kind?: string; equivalency_count?: number | null }[]
      if (policies.length === 0) return <NoRecord what="credit policy" />
      const shown = policies.slice(0, 4)
      return (
        <>
          <ul className="flex flex-wrap gap-1.5">
            {shown.map((p, i) => (
              <li key={i}>
                <Pill tone="brand">{POLICY_LABEL[String(p.policy_kind)] ?? humanize(String(p.policy_kind))}</Pill>
              </li>
            ))}
          </ul>
          {policies.length > shown.length && <More c={c} n={policies.length} noun="credit policies" hash="#credit-heading" />}
        </>
      )
    },
  },
  {
    key: 'lower',
    label: 'Best way to lower the cost',
    hint: 'Strongest verified lever. Nothing is added up.',
    cell: (c, x) => {
      const levers = [...schoolLevers(c, x.exams, x.exam, x.reference)].sort((a, b) => (LEVER_ORDER[a.status] ?? 9) - (LEVER_ORDER[b.status] ?? 9))
      if (levers.length === 0) return <NoRecord what="cost levers" />
      return (
        <>
          <p className="line-clamp-2 text-sm font-semibold text-ink">{levers[0]!.title}</p>
          <p className="mt-0.5 line-clamp-2 text-sm text-ink-3">{levers[0]!.detail}</p>
          {levers.length > 1 && <More c={c} n={levers.length} noun="ways" hash="#lower-heading" />}
        </>
      )
    },
  },
  {
    key: 'appeals',
    label: 'Financial-aid appeals',
    cell: (c) => {
      const appeals = (c.domains.appeals ?? []) as { appeal_kind?: string; offered?: boolean | null }[]
      if (appeals.length === 0) return <NoRecord what="appeal process" />
      const offered = appeals.filter((a) => a.offered)
      return (
        <>
          <p className="text-sm text-ink-2">
            <span className="font-semibold text-ink">{offered.length}</span> published {offered.length === 1 ? 'route' : 'routes'}
          </p>
          <ul className="mt-1 grid gap-0.5 text-sm text-ink-3">
            {offered.slice(0, PREVIEW).map((a, i) => (
              <li key={i} className="truncate">
                {humanize(String(a.appeal_kind))}
              </li>
            ))}
          </ul>
          {offered.length > PREVIEW && <More c={c} n={offered.length} noun="appeal routes" hash="#appeals-heading" />}
        </>
      )
    },
  },
  {
    key: 'programs',
    label: 'Programs & majors',
    hint: 'Against saved interests, verified programs only',
    cell: (c, x) => {
      if (x.interests.length === 0)
        return (
          <p className="text-sm text-ink-3">
            <Link to="/colleges/majors" className="font-semibold text-brand hover:underline">
              Save interests
            </Link>{' '}
            to compare programs.
          </p>
        )
      const f = schoolFit(c.domains, x.interests)
      return <p className="line-clamp-4 text-sm text-ink-2">{fitSentence(c.institution.display_name, f) ?? 'No verified program list yet.'}</p>
    },
  },
  {
    key: 'unverified',
    label: 'Not verified yet',
    cell: (c) =>
      c.missing_domains.length ? (
        <p className="text-sm text-ink-3">{c.missing_domains.map((d) => DOMAIN_LABEL[d] ?? d).join(', ')}</p>
      ) : (
        <p className="text-sm text-ink-3">Every record type we track is verified for {c.academic_year}.</p>
      ),
  },
]

function useWide(query = '(min-width: 768px)') {
  const get = () => (typeof window === 'undefined' || !window.matchMedia ? true : window.matchMedia(query).matches)
  const [wide, setWide] = useState(get)
  useEffect(() => {
    if (!window.matchMedia) return
    const m = window.matchMedia(query)
    const on = () => setWide(m.matches)
    m.addEventListener('change', on)
    return () => m.removeEventListener('change', on)
  }, [query])
  return wide
}

/**
 * Side-by-side comparison: one row per question, the same height across every school (a table row), so the eye
 * moves straight across. Variable-length rows preview a fixed number of items; the detail page has the rest.
 */
export function Compare() {
  const { activeStudent } = useApp()
  const cmp = useSavedComparison()
  const { homeState } = useHomeState()
  const merit = useMeritReference(activeStudent?.id)
  const interests = useInterests(activeStudent?.id).profile.interests
  const exams = useExamPlan(activeStudent?.id).exams
  const wide = useWide()
  const [pick, setPick] = useState(0)

  const header = (
    <PageHeader kicker="Colleges & cost" title="Compare your colleges" actions={<CollegesTabs />}>
      The same questions, side by side, from verified records only. Open a school for everything.
    </PageHeader>
  )
  if (cmp.loading && !cmp.data) return <PageLoading />
  if (cmp.error)
    return (
      <div className="grid gap-8">
        {header}
        <Notice tone="bad">{cmp.error.message}</Notice>
      </div>
    )

  const schools = (cmp.data ?? []).filter((c): c is School => c.found && !!c.institution)
  const x: Ctx = { homeState, exam: merit.exam, reference: merit.reference, interests, exams, primary: cmp.primary }
  if (schools.length < 2)
    return (
      <div className="grid gap-8">
        {header}
        <p className="max-w-xl text-[15px] text-ink-2">
          {schools.length === 0 ? 'Save at least two schools to compare them.' : 'Save one more school to compare.'}{' '}
          <Link to="/colleges" className="font-semibold text-brand hover:underline">
            Add a school
          </Link>
        </p>
      </div>
    )

  const head = (c: School) => (
    <div className="flex items-start justify-between gap-2">
      <div className="min-w-0">
        <Link to={detailPath(c)} className="display text-[19px] leading-tight text-ink hover:underline">
          {c.institution.display_name}
        </Link>
        <p className="mt-0.5 text-sm text-ink-3">
          {[[c.institution.city, c.institution.state_code].filter(Boolean).join(', '), c.institution.control && CONTROL_LABEL[c.institution.control]].filter(Boolean).join(', ')}
        </p>
        {cmp.primary === c.institution_key && (
          <Pill tone="brand" className="mt-1.5">
            Top choice
          </Pill>
        )}
      </div>
      <button
        onClick={() => void cmp.remove(c.institution_key)}
        className="grid h-8 w-8 shrink-0 place-items-center rounded-full text-ink-3 hover:bg-surface-2 hover:text-ink"
        aria-label={`Remove ${c.institution.display_name}`}
      >
        <X size={16} />
      </button>
    </div>
  )

  return (
    <div className="grid grid-cols-1 gap-8">
      {header}
      <div className="flex flex-wrap items-center justify-between gap-3">
        <HomeStateControl />
        <span className="text-sm text-ink-3">{cmp.data?.[0]?.academic_year ?? ''} published records</span>
      </div>

      {wide ? (
        <table className="w-full table-fixed border-collapse" aria-label="College comparison">
          <colgroup>
            <col className="w-44" />
            {schools.map((c) => (
              <col key={c.institution_key} />
            ))}
          </colgroup>
          <thead>
            <tr>
              <td />
              {schools.map((c) => (
                <th key={c.institution_key} scope="col" className="px-4 pb-4 text-left align-bottom font-normal">
                  {head(c)}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {ROWS.map((r) => (
              <tr key={r.key} data-row={r.key}>
                <th scope="row" className="border-t border-line py-4 pr-4 text-left align-top font-normal">
                  <span className="block text-sm font-bold text-ink">{r.label}</span>
                  {r.hint && <span className="mt-0.5 block text-xs text-ink-3">{r.hint}</span>}
                </th>
                {schools.map((c) => (
                  <td key={c.institution_key} className="min-w-0 border-t border-line px-4 py-4 align-top">
                    {r.cell(c, x)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <MobileCompare schools={schools} pick={Math.min(pick, schools.length - 1)} onPick={setPick} head={head} x={x} />
      )}
    </div>
  )
}

/** Phones: one school at a time, the same rows in the same order, so switching schools keeps your place. */
function MobileCompare({ schools, pick, onPick, head, x }: { schools: School[]; pick: number; onPick: (i: number) => void; head: (c: School) => ReactNode; x: Ctx }) {
  const c = schools[pick]!
  return (
    <div>
      <div role="group" aria-label="Choose a school" className="-mx-4 flex gap-2 overflow-x-auto px-4 pb-1">
        {schools.map((s, i) => (
          <button
            key={s.institution_key}
            aria-pressed={i === pick}
            onClick={() => onPick(i)}
            className={cx('shrink-0 rounded-full border px-3 py-1.5 text-sm font-semibold', i === pick ? 'border-ink bg-ink text-surface' : 'border-line text-ink-2')}
          >
            {s.institution.display_name}
          </button>
        ))}
      </div>
      <div className="mt-5">{head(c)}</div>
      <dl className="mt-4">
        {ROWS.map((r) => (
          <div key={r.key} className="border-t border-line py-4" data-row={r.key}>
            <dt className="mb-2 text-sm font-bold text-ink">{r.label}</dt>
            <dd className="min-w-0">{r.cell(c, x)}</dd>
          </div>
        ))}
      </dl>
    </div>
  )
}
