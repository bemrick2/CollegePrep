import { useState } from 'react'
import { CERTAINTY_OPTIONS, INTEREST_AREAS, MAX_INTERESTS, type InterestProfile, type MajorCertainty, type SavedInterest } from '../../lib/engine/interests'
import { ChoiceCard, cx } from '../../components/ui'
import { Check } from '../../components/icons'

const same = (a: SavedInterest, b: SavedInterest) => a.kind === b.kind && a.key === b.key

export function CertaintyChoice({ value, onChange, who = 'you', compact = false }: { value: MajorCertainty | null; onChange: (c: MajorCertainty) => void; who?: string; compact?: boolean }) {
  if (compact)
    return (
      <div role="radiogroup" aria-label={who === 'you' ? 'How sure are you about a major?' : `How sure is ${who} about a major?`} className="flex flex-wrap gap-2">
        {CERTAINTY_OPTIONS.map((o) => (
          <button
            key={o.value}
            type="button"
            role="radio"
            aria-checked={value === o.value}
            onClick={() => onChange(o.value)}
            className={cx('rounded-full border px-3 py-1.5 text-sm font-semibold', value === o.value ? 'border-go bg-go-soft text-ink' : 'border-line-strong bg-surface text-ink-2 hover:bg-surface-2')}
          >
            {o.label}
          </button>
        ))}
      </div>
    )
  return (
    <div role="radiogroup" aria-label={who === 'you' ? 'How sure are you about a major?' : `How sure is ${who} about a major?`} className="grid gap-2">
      {CERTAINTY_OPTIONS.map((o) => (
        <ChoiceCard key={o.value} selected={value === o.value} onClick={() => onChange(o.value)} title={o.label} description={o.hint} />
      ))}
    </div>
  )
}

function Chip({ on, onClick, children, small, disclosure }: { on: boolean; onClick: () => void; children: React.ReactNode; small?: boolean; disclosure?: boolean }) {
  return (
    <button
      type="button"
      aria-pressed={disclosure ? undefined : on}
      aria-expanded={disclosure ? on : undefined}
      onClick={onClick}
      className={cx(
        'inline-flex items-center gap-1 rounded-full border font-semibold transition-colors',
        small ? 'px-2.5 py-1 text-xs' : 'px-3 py-1.5 text-sm',
        on ? (disclosure ? 'border-brand bg-surface text-ink' : 'border-go bg-go-soft text-ink') : 'border-line-strong bg-surface text-ink-2 hover:bg-surface-2',
      )}
    >
      {on && !disclosure && <Check size={small ? 12 : 14} />}
      {children}
    </button>
  )
}

/**
 * Broad areas first; each area opens its common majors. Areas alone are a complete answer for an undecided
 * student. This is an exploration list, not any school's catalog.
 */
export function InterestPicker({ value, onToggle }: { value: InterestProfile; onToggle: (i: SavedInterest) => void }) {
  const has = (i: SavedInterest) => value.interests.some((x) => same(x, i))
  const [open, setOpen] = useState<string | null>(() => INTEREST_AREAS.find((a) => a.majors.some((m) => has({ kind: 'major', key: m.key })))?.key ?? null)
  const full = value.interests.length >= MAX_INTERESTS
  const showMajors = value.certainty !== 'unsure'

  return (
    <div className="grid gap-3">
      <div className="flex flex-wrap gap-2">
        {INTEREST_AREAS.map((a) => {
          const i: SavedInterest = { kind: 'area', key: a.key }
          const picked = has(i)
          const majorsPicked = a.majors.filter((m) => has({ kind: 'major', key: m.key })).length
          const count = majorsPicked + (picked ? 1 : 0)
          return showMajors ? (
            <Chip key={a.key} disclosure on={open === a.key} onClick={() => setOpen(open === a.key ? null : a.key)}>
              {a.label}
              {count > 0 && <span className="ml-0.5 rounded-full bg-go px-1.5 text-[10px] text-white">{count}</span>}
            </Chip>
          ) : (
            <Chip key={a.key} on={picked} onClick={() => (picked || !full) && onToggle(i)}>
              {a.label}
            </Chip>
          )
        })}
      </div>
      {showMajors && (
        <div className="rounded-2xl bg-surface-2 p-3">
          {open ? (
            <>
              <div className="text-xs font-semibold text-ink-3">Possible majors in {INTEREST_AREAS.find((a) => a.key === open)!.label}</div>
              <div className="mt-2 flex flex-wrap gap-1.5">
                <Chip small on={has({ kind: 'area', key: open })} onClick={() => (has({ kind: 'area', key: open }) || !full) && onToggle({ kind: 'area', key: open })}>
                  Anything in {INTEREST_AREAS.find((a) => a.key === open)!.label}
                </Chip>
                {INTEREST_AREAS.find((a) => a.key === open)!.majors.map((m) => {
                  const i: SavedInterest = { kind: 'major', key: m.key }
                  return (
                    <Chip key={m.key} small on={has(i)} onClick={() => (has(i) || !full) && onToggle(i)}>
                      {m.label}
                    </Chip>
                  )
                })}
              </div>
            </>
          ) : (
            <p className="text-xs text-ink-3">Tap an area to see possible majors in it.</p>
          )}
        </div>
      )}
      <p className="text-xs text-ink-3">
        {value.interests.length} saved{full ? ` (up to ${MAX_INTERESTS})` : ''}. This is our exploration list, not a school's catalog — each school's own programs are checked separately.
      </p>
    </div>
  )
}
