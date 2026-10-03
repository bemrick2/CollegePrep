import { useEffect, useRef } from 'react'
import type { Confidence, PublicQuestion, SubmitResult } from '../../lib/data/types'
import { cx } from '../../components/ui'
import { Check, X } from '../../components/icons'
import { SECTION_LABEL } from '../../lib/engine/benchmark'
import { RichText } from '../../components/RichText'

export function QuestionView({
  question,
  answer,
  onChoose,
  result,
  skillName,
  autoFocus = true,
}: {
  question: PublicQuestion
  answer: string
  onChoose: (a: string) => void
  result?: SubmitResult | null
  skillName?: string | null
  autoFocus?: boolean
}) {
  const locked = !!result
  const accepted = result?.accepted_answers ?? []
  const headingRef = useRef<HTMLHeadingElement>(null)

  useEffect(() => {
    if (autoFocus) headingRef.current?.focus()
  }, [question.id, autoFocus])

  // Number keys 1-4 / letters pick a choice on desktop.
  useEffect(() => {
    if (locked || question.answer_format !== 'choice') return
    const onKey = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement || e.metaKey || e.ctrlKey) return
      const idx = /^[1-9]$/.test(e.key) ? Number(e.key) - 1 : e.key.length === 1 ? e.key.toUpperCase().charCodeAt(0) - 65 : -1
      const c = question.choices[idx]
      if (c) onChoose(c.key)
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [question, locked, onChoose])

  return (
    <div className={cx('grid gap-5', question.passage && 'lg:grid-cols-2 lg:gap-8')}>
      {question.passage && (
        <div className="max-h-[38dvh] overflow-y-auto rounded-2xl border border-line bg-surface p-4 text-[15px] leading-relaxed text-ink-2 lg:max-h-[65dvh]" tabIndex={0} aria-label="Passage">
          <p className="whitespace-pre-line"><RichText text={question.passage} /></p>
        </div>
      )}
      <div>
        <div className="mb-2 flex flex-wrap items-center gap-2 text-xs font-semibold uppercase tracking-wide text-ink-3">
          <span>{SECTION_LABEL[question.section] ?? question.section}</span>
          {skillName && (
            <>
              <span aria-hidden>·</span>
              <span className="normal-case tracking-normal">{skillName}</span>
            </>
          )}
        </div>
        <h2 ref={headingRef} tabIndex={-1} className="whitespace-pre-line text-[18px] font-medium leading-relaxed text-ink outline-none md:text-[19px]">
          <RichText text={question.stem} />
        </h2>

        {question.answer_format === 'choice' ? (
          <div role="radiogroup" aria-label="Answer choices" className="mt-5 grid gap-2.5">
            {question.choices.map((c, i) => {
              const selected = answer === c.key
              const isRight = locked && accepted.includes(c.key)
              const isWrongPick = locked && selected && !isRight
              return (
                <button
                  key={c.key}
                  type="button"
                  role="radio"
                  aria-checked={selected}
                  disabled={locked}
                  onClick={() => onChoose(c.key)}
                  className={cx(
                    'group flex min-h-14 w-full items-center gap-3 rounded-2xl border-2 px-4 py-3 text-left text-[16px] transition-all',
                    !locked && !selected && 'border-line bg-surface hover:border-line-strong active:scale-[0.99]',
                    !locked && selected && 'border-info bg-info-soft',
                    isRight && 'border-go bg-go-soft',
                    isWrongPick && 'anim-shake border-bad bg-bad-soft',
                    locked && !isRight && !isWrongPick && 'border-line bg-surface opacity-60',
                  )}
                >
                  <span
                    aria-hidden
                    className={cx(
                      'grid h-8 w-8 shrink-0 place-items-center rounded-lg border-2 text-sm font-bold',
                      isRight ? 'border-go bg-go text-white' : isWrongPick ? 'border-bad bg-bad text-white' : selected ? 'border-info bg-info text-white' : 'border-line-strong text-ink-2',
                    )}
                  >
                    {isRight ? <Check size={16} /> : isWrongPick ? <X size={16} /> : c.key}
                  </span>
                  <span className="text-ink">{c.text}</span>
                  <span className="sr-only">{i < 9 ? `(press ${i + 1})` : ''}</span>
                </button>
              )
            })}
          </div>
        ) : (
          <div className="mt-5">
            <label htmlFor={`ans-${question.id}`} className="text-sm font-semibold text-ink">
              Your answer
            </label>
            <input
              id={`ans-${question.id}`}
              inputMode="decimal"
              autoComplete="off"
              disabled={locked}
              value={answer}
              onChange={(e) => onChoose(e.target.value.replace(/[^0-9./-]/g, ''))}
              placeholder="e.g. 3/4 or 0.75"
              className={cx(
                'mt-1.5 block h-14 w-full max-w-xs rounded-2xl border-2 bg-surface px-4 text-xl font-semibold tabular text-ink focus:outline-none',
                locked ? (result?.is_correct ? 'border-go' : 'border-bad') : 'border-line-strong focus:border-info',
              )}
            />
            {locked && !result?.is_correct && (
              <p className="mt-2 text-sm text-ink-2">
                Accepted: <span className="font-semibold text-ink">{accepted.join(' or ')}</span>
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  )
}

export const CONFIDENCE_LABEL: Record<Confidence, string> = { 1: 'Guessing', 2: 'Fairly sure', 3: 'Certain' }

/** Picking a confidence level submits the answer: one tap, and we learn calibration. */
export function ConfidenceBar({ disabled, onPick }: { disabled: boolean; onPick: (c: Confidence) => void }) {
  return (
    <div>
      <div className="mb-2 text-center text-xs font-semibold uppercase tracking-wide text-ink-3" id="conf-label">
        How sure are you?
      </div>
      <div className="grid grid-cols-3 gap-2" role="group" aria-labelledby="conf-label">
        {([1, 2, 3] as Confidence[]).map((c) => (
          <button
            key={c}
            type="button"
            disabled={disabled}
            onClick={() => onPick(c)}
            className={cx(
              'h-14 rounded-2xl text-[15px] font-semibold transition active:translate-y-px disabled:opacity-40',
              c === 3 ? 'bg-go text-white shadow-[0_2px_0_0_var(--go-strong)] hover:bg-go-strong dark:text-bg' : 'border-2 border-line-strong bg-surface text-ink hover:bg-surface-2',
            )}
          >
            {CONFIDENCE_LABEL[c]}
          </button>
        ))}
      </div>
    </div>
  )
}
