// Shared, strict argument parsing for the editorial scripts: an unrecognised flag or a missing value is an error,
// never a silent fall-back to every item or to the repository's files.
export function parseArgs(argv: string[], flags: string[], usage: string): { positional: string[]; opts: Record<string, string> } {
  const positional: string[] = []
  const opts: Record<string, string> = {}
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i]!
    if (a.startsWith('-')) {
      if (!flags.includes(a)) throw new Error(`unrecognised argument ${a}. ${usage}`)
      const v = argv[i + 1]
      if (!v || v.startsWith('-')) throw new Error(`${a} needs a value. ${usage}`)
      if (a in opts) throw new Error(`${a} given twice. ${usage}`)
      opts[a] = v
      i++
    } else positional.push(a)
  }
  return { positional, opts }
}
