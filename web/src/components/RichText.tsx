import { Fragment } from 'react'

/**
 * Plain question text with one convention: [bracketed words] are the
 * underlined portion an English item asks about. Numeric markers such as
 * [3] are sentence numbers and render as-is.
 */
export function RichText({ text }: { text: string }) {
  const parts = text.split(/(\[[^\]]+\])/g)
  return (
    <>
      {parts.map((p, i) => {
        const m = /^\[([^\]]+)\]$/.exec(p)
        if (m && !/^\d+$/.test(m[1]!))
          return (
            <span key={i} className="underline decoration-2 underline-offset-4 decoration-info">
              <span className="sr-only">underlined: </span>
              {m[1]}
            </span>
          )
        if (m) return <sup key={i} className="mr-0.5 text-[0.7em] font-semibold text-ink-3">{m[1]}</sup>
        return <Fragment key={i}>{p}</Fragment>
      })}
    </>
  )
}
