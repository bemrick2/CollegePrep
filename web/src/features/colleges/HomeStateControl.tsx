import { useHomeState } from '../../lib/homeState'
import { US_STATES } from '../../lib/engine/residency'
import { cx } from '../../components/ui'

/**
 * The family's home state, marked as their answer (not verified). It decides in-state vs out-of-state prices.
 */
export function HomeStateControl({ className }: { className?: string }) {
  const { homeState, setHomeState, scope } = useHomeState()
  if (!scope) return null
  return (
    <div className={cx('flex flex-wrap items-center gap-x-2 gap-y-1 text-sm', className)}>
      <label htmlFor="home-state" className="font-semibold text-ink">
        Home state
      </label>
      <select
        id="home-state"
        value={homeState ?? ''}
        onChange={(e) => setHomeState(e.target.value || null)}
        className="h-9 rounded-lg border border-line-strong bg-surface px-2 text-sm font-semibold"
      >
        <option value="">Not set</option>
        {US_STATES.map(([c, n]) => (
          <option key={c} value={c}>
            {n}
          </option>
        ))}
      </select>
      <span className="text-xs text-ink-3">
        {homeState ? 'Your answer. It picks in-state or out-of-state prices; each school decides residency.' : 'Not set: in-state prices are shown and marked as assumed.'}
      </span>
    </div>
  )
}
