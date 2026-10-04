import type { SavedInterest } from '../../lib/engine/interests'
import { fitSentence, schoolFit, type InterestFit } from '../../lib/engine/programFit'
import { Pill, cx } from '../../components/ui'

const STATUS = {
  verified: { tone: 'go' as const, label: 'Verified program' },
  not_listed: { tone: 'neutral' as const, label: 'Not in our verified list' },
  no_data: { tone: 'neutral' as const, label: 'Programs not verified yet' },
}

export function SchoolFitRow({ name, domains, interests, compact = false }: { name: string; domains: Record<string, unknown[] | undefined>; interests: SavedInterest[]; compact?: boolean }) {
  const fit = schoolFit(domains, interests)
  const sentence = fitSentence(name, fit)
  return (
    <div className={cx(!compact && 'rounded-2xl bg-surface-2 p-4')}>
      {!compact && <h3 className="font-semibold text-ink">{name}</h3>}
      {sentence && <p className={cx('text-sm text-ink-2', !compact && 'mt-0.5')}>{sentence}</p>}
      {fit.hasProgramData && (
        <ul className="mt-2 grid grid-cols-1 gap-1.5">
          {fit.fits.map((f) => (
            <FitLine key={`${f.interest.kind}:${f.interest.key}`} f={f} />
          ))}
        </ul>
      )}
      {fit.sharedFirstYear && fit.sharedFirstYear.courses.length > 0 && (
        <p className="mt-2 text-xs text-ink-2">
          Shared first-year courses in the published maps: {fit.sharedFirstYear.courses.join(', ')}.
        </p>
      )}
    </div>
  )
}

function FitLine({ f }: { f: InterestFit }) {
  const s = STATUS[f.status]
  return (
    <li className="min-w-0 text-sm">
      <div className="flex flex-wrap items-center gap-1.5">
        <span className="font-semibold text-ink">{f.label}</span>
        <Pill tone={s.tone}>{s.label}</Pill>
        {f.directAdmission && <Pill tone="warn">Freshman admission required</Pill>}
      </div>
      {f.programs.length > 0 && (
        <p className="mt-0.5 text-xs text-ink-2">
          {f.programs.slice(0, 2).map((p, n) => (
            <span key={p.name}>
              {n > 0 && ' · '}
              {p.url ? (
                <a href={p.url} target="_blank" rel="noreferrer" className="hover:underline">{p.name}</a>
              ) : (
                p.name
              )}
            </span>
          ))}
          {f.programs.length > 2 && ` · +${f.programs.length - 2} more`}
        </p>
      )}
      {f.progression.map((r) => (
        <p key={r.program} className="mt-1 border-l-2 border-line-strong pl-2 text-xs text-ink-2">
          Published rule: “{r.text}”
        </p>
      ))}
      {f.scholarships.map((a) => (
        <p key={a.name} className="mt-1 text-xs text-ink-2">
          Scholarship tied to this field: {a.url ? <a href={a.url} target="_blank" rel="noreferrer" className="font-semibold hover:underline">{a.name}</a> : a.name} ({a.requirement})
        </p>
      ))}
    </li>
  )
}

