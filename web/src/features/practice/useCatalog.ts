import { useApp, useAsync } from '../../lib/app'
import type { ExamFamily } from '../../lib/data/types'

export function useCatalog(exam: ExamFamily | null | undefined) {
  const { source } = useApp()
  const { data } = useAsync(() => (exam ? source.catalog(exam) : Promise.resolve({ skills: [], strategies: [], traps: [] })), [source, exam])
  const skills = data?.skills ?? []
  return {
    skills,
    strategies: data?.strategies ?? [],
    traps: data?.traps ?? [],
    skill: (key: string | null | undefined) => (key ? (skills.find((s) => s.skill_key === key) ?? null) : null),
    /** Strategies that apply to a section; falls back to none when the catalog has no section data. */
    strategiesFor: (section: string | null | undefined) => (data?.strategies ?? []).filter((s) => !!section && !!s.sections?.includes(section)),
    skillName: (key: string | null | undefined) => (key ? (skills.find((s) => s.skill_key === key)?.name ?? humanize(key)) : null),
  }
}

export function humanize(key: string): string {
  const s = key.replace(/^(act|sat)_/, '').replace(/_/g, ' ')
  return s.charAt(0).toUpperCase() + s.slice(1)
}
