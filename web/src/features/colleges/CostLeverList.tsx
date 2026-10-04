import type { CostLever, LeverStatus } from '../../lib/engine/costLevers'
import { Pill } from '../../components/ui'

const STATUS: Record<LeverStatus, { tone: 'go' | 'gold' | 'brand' | 'neutral'; label: string }> = {
  on_track: { tone: 'go', label: 'On track' },
  within_reach: { tone: 'gold', label: 'Within reach' },
  stretch: { tone: 'neutral', label: 'Stretch' },
  available: { tone: 'brand', label: 'Available' },
  check: { tone: 'neutral', label: 'Check' },
}

/** Ways to lower one school's cost, from its verified records. No lever carries an estimated dollar saving. */
export function CostLeverList({ levers, max }: { levers: CostLever[]; max?: number }) {
  const shown = max ? levers.slice(0, max) : levers
  if (!levers.length) return <p className="text-ink-3">No verified scholarship, credit or aid records here yet.</p>
  return (
    <ul className="grid grid-cols-1 gap-2">
      {shown.map((l) => (
        <li key={l.key} className="min-w-0 rounded-xl border border-line p-3">
          <div className="flex flex-wrap items-start justify-between gap-x-2 gap-y-1">
            {l.href ? (
              <a href={l.href} target="_blank" rel="noreferrer" className="min-w-0 font-semibold text-ink hover:underline">
                {l.title}
              </a>
            ) : (
              <span className="min-w-0 font-semibold text-ink">{l.title}</span>
            )}
            <Pill tone={STATUS[l.status].tone}>{STATUS[l.status].label}</Pill>
          </div>
          <p className="mt-0.5 text-xs text-ink-2">{l.detail}</p>
        </li>
      ))}
      {max && levers.length > max && <li className="text-xs text-ink-3">+{levers.length - max} more on the path</li>}
    </ul>
  )
}
