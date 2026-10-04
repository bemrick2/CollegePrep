import { Link } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { labelOf } from '../../lib/engine/interests'
import { UNVERIFIED_QUESTIONS } from '../../lib/engine/programFit'
import { useSavedComparison, COMPARE_YEAR } from '../colleges/useSavedComparison'
import { CollegesTabs } from '../colleges/CollegesTabs'
import { SchoolFitRow } from './SchoolFitRow'
import { CertaintyChoice, InterestPicker } from './InterestPicker'
import { useInterests } from './useInterests'
import { ArrowRight, Info, School, Sparkle, X } from '../../components/icons'
import { Card, CardHeader, cx } from '../../components/ui'

/**
 * Explore majors: certainty, saved interests (no ranking unless the student picks a focus), and how each saved
 * school's verified records cover them. Changes apply everywhere at once; onboarding never has to be repeated.
 */
export function ExploreMajors() {
  const { activeStudent, viewer } = useApp()
  const sid = activeStudent?.id
  const it = useInterests(sid)
  const isStudent = !!viewer && activeStudent?.linked_user_id === viewer.userId
  const who = isStudent ? 'you' : (activeStudent?.display_name ?? 'your student')
  const cmp = useSavedComparison(COMPARE_YEAR)
  const schools = (cmp.data ?? []).filter((c) => c.found && c.institution?.level !== 'two_year')
  const { profile } = it

  return (
    <div className="grid grid-cols-1 gap-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">Colleges & cost</p>
          <h1 className="display text-[30px] font-semibold leading-tight text-ink md:text-[36px]">Explore majors</h1>
          <p className="mt-1 max-w-2xl text-sm text-ink-2">
            Save interests as {who === 'you' ? 'you' : who} explore{who === 'you' ? '' : 's'}. No single major is required, and nothing is ranked unless {who === 'you' ? 'you choose' : 'they choose'} a focus.
          </p>
        </div>
        <CollegesTabs />
      </div>

      <Card className="p-5">
        <h2 className="font-semibold text-ink">{who === 'you' ? 'How sure are you about a major?' : `How sure is ${who} about a major?`}</h2>
        <div className="mt-3">
          <CertaintyChoice compact value={profile.certainty} onChange={it.setCertainty} who={who} />
        </div>
      </Card>

      <Card>
        <CardHeader title="Saved interests" subtitle={profile.interests.length ? 'Not ranked. Mark one as a focus only if you want to.' : undefined} />
        <div className="p-5 pt-3">
          {profile.interests.length === 0 ? (
            <p className="text-sm text-ink-3">Nothing saved yet. Not sure is fine — add broad areas whenever something sounds interesting.</p>
          ) : (
            <ul className="flex flex-wrap gap-2">
              {profile.interests.map((i) => (
                <li key={`${i.kind}:${i.key}`} className={cx('flex items-center gap-1 rounded-full border py-1 pl-3 pr-1 text-sm', i.focus ? 'border-brand bg-brand-soft' : 'border-line bg-surface')}>
                  <span className="font-semibold text-ink">{labelOf(i)}</span>
                  {i.kind === 'area' && <span className="text-xs text-ink-3">· area</span>}
                  <button
                    type="button"
                    onClick={() => it.setFocus(i)}
                    aria-pressed={!!i.focus}
                    aria-label={i.focus ? `Remove focus from ${labelOf(i)}` : `Make ${labelOf(i)} the focus`}
                    title={i.focus ? 'Focus (tap to clear)' : 'Make this the focus (optional)'}
                    className={cx('grid h-7 w-7 place-items-center rounded-full', i.focus ? 'text-brand' : 'text-ink-3 hover:bg-surface-2 hover:text-ink')}
                  >
                    <Sparkle size={14} />
                  </button>
                  <button type="button" onClick={() => it.toggle(i)} aria-label={`Remove ${labelOf(i)}`} className="grid h-7 w-7 place-items-center rounded-full text-ink-3 hover:bg-surface-2 hover:text-ink">
                    <X size={14} />
                  </button>
                </li>
              ))}
            </ul>
          )}
          <p className="mt-3 text-xs text-ink-3">Saved on this device for now.</p>
        </div>
      </Card>

      <Card className="p-5">
        <h2 className="font-semibold text-ink">Add interests</h2>
        <div className="mt-3">
          <InterestPicker value={profile} onToggle={it.toggle} />
        </div>
      </Card>

      <Card>
        <CardHeader title={<span className="flex items-center gap-2"><School size={18} /> Keeps options open?</span>} subtitle="How each saved four-year school's verified records cover every saved interest" />
        <div className="grid gap-4 p-5 pt-3">
          {cmp.keys.length === 0 ? (
            <p className="text-sm text-ink-3">
              <Link to="/colleges" className="font-semibold text-brand hover:underline">Save schools</Link> to see which of them offer programs in these interests.
            </p>
          ) : profile.interests.length === 0 ? (
            <p className="text-sm text-ink-3">Save an interest above, even a broad area, to see how each school covers it.</p>
          ) : cmp.loading && !cmp.data ? (
            <p className="text-sm text-ink-3">Loading verified programs…</p>
          ) : (
            schools.map((c) => <SchoolFitRow key={c.institution_key} name={c.institution?.display_name ?? c.institution_key} domains={c.domains} interests={profile.interests} />)
          )}
          <details className="rounded-2xl border border-line p-4 text-sm">
            <summary className="cursor-pointer font-semibold text-ink">Not verified yet — questions to ask each school</summary>
            <ul className="mt-2 grid list-disc gap-1 pl-5 text-ink-2">
              {UNVERIFIED_QUESTIONS.map((q) => (
                <li key={q}>{q}</li>
              ))}
            </ul>
            <p className="mt-2 text-xs text-ink-3">We'll answer these from published records once they're verified, never by guessing.</p>
          </details>
          <p className="flex gap-2 text-xs text-ink-3">
            <Info size={14} className="mt-0.5 shrink-0" />
            “Verified program” means the school's own published records list it; we show the program name we matched. Program lists we've imported are often partial, so “not in our verified list” doesn't mean a school doesn't offer it.
          </p>
          <Link to="/colleges/paths" className="inline-flex items-center gap-1 text-sm font-semibold text-brand hover:underline">
            See costs and credit on College paths <ArrowRight size={16} />
          </Link>
        </div>
      </Card>
    </div>
  )
}

