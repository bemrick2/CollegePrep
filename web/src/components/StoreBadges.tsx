import { useState } from 'react'
import { BADGE, storeOrder, storeUrl, type Store } from '../lib/storeLinks'
import { cx } from './ui'

const NAME: Record<Store, string> = { apple: 'iPhone', google: 'Android' }

/**
 * Official store badges, linked to the live listings. Until a listing URL is configured, nothing pretends to be a
 * badge: a plain "coming soon" line is shown instead. Badges keep clear space of at least a quarter of their height.
 */
export function StoreBadges({ className, align = 'start' }: { className?: string; align?: 'start' | 'center' }) {
  const order = storeOrder()
  const live = order.map((s) => ({ s, url: storeUrl(s) })).filter((x): x is { s: Store; url: string } => !!x.url)
  if (live.length === 0)
    return (
      <p className={cx('text-sm text-ink-3', align === 'center' && 'text-center', className)}>
        Apps for iPhone and Android are coming soon. Use the same account there once they're out.
      </p>
    )
  const missing = order.filter((s) => !live.some((x) => x.s === s))
  return (
    // Negative margin offsets the badges' own clear space so they line up with surrounding text.
    <div className={cx('-mx-2.5 flex flex-wrap items-center', align === 'center' && 'justify-center', className)}>
      {live.map(({ s, url }) => (
        <Badge key={s} store={s} url={url} />
      ))}
      {missing.length > 0 && <span className="m-2.5 text-xs text-ink-3">{missing.map((s) => NAME[s]).join(' and ')} app coming soon</span>}
    </div>
  )
}

function Badge({ store, url }: { store: Store; url: string }) {
  const [broken, setBroken] = useState(false)
  const b = BADGE[store]
  return (
    // Clear space: 10px around a 40px-tall badge (one quarter of its height).
    <a href={url} target="_blank" rel="noopener noreferrer" className="m-2.5 inline-flex rounded-lg focus-visible:outline-2 focus-visible:outline-offset-2">
      {broken ? (
        <span className="rounded-lg border border-line-strong px-3 py-2 text-sm font-semibold text-ink">{b.alt}</span>
      ) : (
        <img src={b.src} alt={b.alt} height={40} className="h-10 w-auto" onError={() => setBroken(true)} />
      )}
    </a>
  )
}
