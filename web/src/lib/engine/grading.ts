import type { AnswerFormat } from '../data/types'

// Mirrors public.parse_numeric_answer / grade_answer.

export function parseNumericAnswer(raw: string): number | null {
  const s = raw.trim()
  if (/^[-+]?(\d+(\.\d*)?|\.\d+)$/.test(s)) return Number(s)
  const frac = /^([-+]?\d+)\s*\/\s*([-+]?\d+)$/.exec(s)
  if (frac) {
    const den = Number(frac[2])
    if (den === 0) return null
    return Number(frac[1]) / den
  }
  return null
}

export function gradeAnswer(format: AnswerFormat, accepted: string[], given: string): boolean {
  const g = given.trim()
  switch (format) {
    case 'choice':
      return accepted.some((a) => a.trim() === g)
    case 'numeric': {
      const v = parseNumericAnswer(g)
      if (v === null) return false
      return accepted.some((a) => {
        const x = parseNumericAnswer(a)
        return x !== null && Math.abs(x - v) < 1e-9
      })
    }
    case 'text':
      return accepted.some((a) => a.trim().toLowerCase() === g.toLowerCase())
  }
}
