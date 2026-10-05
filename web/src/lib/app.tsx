import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from 'react'
import type { DataSource } from './data/source'
import type { HouseholdContext, Student, Viewer } from './data/types'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from './data/demo/demoSource'
import { LiveSource } from './data/live/liveSource'
import { supabase } from './supabase'
import { clearStore } from './data/demo/store'

type Mode = 'demo' | 'live'

interface AppState {
  source: DataSource
  mode: Mode
  liveAvailable: boolean
  viewer: Viewer | null
  ctx: HouseholdContext | null
  loading: boolean
  /** The student a guardian is currently looking at. */
  activeStudent: Student | null
  setActiveStudentId: (id: string) => void
  refresh: () => Promise<void>
  useLive: () => void
  startDemo: (persona: 'parent' | 'student', withSample: boolean) => Promise<void>
  switchDemoPersona: (persona: 'parent' | 'student') => Promise<void>
  resetDemo: () => Promise<void>
  signOut: () => Promise<void>
}

const AppContext = createContext<AppState | null>(null)
const MODE_KEY = 'pp-mode'
const ACTIVE_KEY = 'pp-active-student'

function readMode(): Mode {
  try {
    return localStorage.getItem(MODE_KEY) === 'live' && supabase ? 'live' : 'demo'
  } catch {
    return 'demo'
  }
}

export function AppProvider({ children, source: injected }: { children: ReactNode; source?: DataSource }) {
  const [mode, setMode] = useState<Mode>(injected?.mode ?? readMode())
  const source = useMemo<DataSource>(() => injected ?? (mode === 'live' && supabase ? new LiveSource(supabase) : new DemoSource()), [mode, injected])
  const [viewer, setViewer] = useState<Viewer | null>(null)
  const [ctx, setCtx] = useState<HouseholdContext | null>(null)
  const [loading, setLoading] = useState(true)
  const [activeId, setActiveId] = useState<string | null>(() => {
    try {
      return localStorage.getItem(ACTIVE_KEY)
    } catch {
      return null
    }
  })

  const refresh = useCallback(async () => {
    try {
      const v = await source.getViewer()
      setViewer(v)
      setCtx(v ? await source.getHouseholdContext() : null)
    } catch {
      setViewer(null)
      setCtx(null)
    } finally {
      setLoading(false)
    }
  }, [source])

  useEffect(() => {
    setLoading(true)
    void refresh()
    if (mode === 'live' && supabase) {
      const { data } = supabase.auth.onAuthStateChange(() => void refresh())
      return () => data.subscription.unsubscribe()
    }
  }, [refresh, mode])

  const persistMode = (m: Mode) => {
    try {
      localStorage.setItem(MODE_KEY, m)
    } catch {
      // ignore
    }
    setMode(m)
  }

  const setActiveStudentId = (id: string) => {
    setActiveId(id)
    try {
      localStorage.setItem(ACTIVE_KEY, id)
    } catch {
      // ignore
    }
  }

  const demo = () => (source instanceof DemoSource ? source : null)

  const startDemo = async (persona: 'parent' | 'student', withSample: boolean) => {
    persistMode('demo')
    const d = source instanceof DemoSource ? source : new DemoSource()
    if (withSample) {
      const { sampleFamily } = await import('./data/demo/seed')
      d.replaceStore(sampleFamily(persona))
      const { SAMPLE_SCHOOLS, readSavedSchools, writeSavedSchools } = await import('./savedSchools')
      if (readSavedSchools().length === 0) writeSavedSchools(SAMPLE_SCHOOLS)
      const { SAMPLE_INTERESTS, readInterests, writeInterests } = await import('./interestStore')
      for (const st of d.sampleStudentIds()) if (readInterests(st).certainty === null) writeInterests(st, SAMPLE_INTERESTS)
      // The sample family lives in Tennessee (their answer, like any family's).
      const { readHomeState, writeHomeState } = await import('./homeState')
      for (const h of d.sampleHouseholdIds()) if (!readHomeState(h)) writeHomeState(h, 'TN')
    }
    else {
      d.reset()
      d.switchPersona(persona === 'parent' ? DEMO_PARENT : DEMO_STUDENT, persona === 'parent' ? 'Parent (demo)' : 'Student (demo)')
    }
    if (d === source) await refresh()
  }

  const switchDemoPersona = async (persona: 'parent' | 'student') => {
    demo()?.switchPersona(persona === 'parent' ? DEMO_PARENT : DEMO_STUDENT, persona === 'parent' ? 'Parent (demo)' : 'Student (demo)')
    await refresh()
  }

  const resetDemo = async () => {
    clearStore()
    demo()?.reset()
    await refresh()
  }

  const signOut = async () => {
    await source.signOut()
    await refresh()
  }

  const students = ctx?.students ?? []
  const activeStudent = students.find((s) => s.id === activeId) ?? (ctx?.myStudent && viewer && ctx.myStudent.linked_user_id === viewer.userId ? ctx.myStudent : students[0]) ?? null

  const value: AppState = {
    source,
    mode,
    liveAvailable: supabase !== null,
    viewer,
    ctx,
    loading,
    activeStudent,
    setActiveStudentId,
    refresh,
    useLive: () => persistMode('live'),
    startDemo,
    switchDemoPersona,
    resetDemo,
    signOut,
  }
  return <AppContext.Provider value={value}>{children}</AppContext.Provider>
}

export function useApp(): AppState {
  const v = useContext(AppContext)
  if (!v) throw new Error('useApp outside AppProvider')
  return v
}

/** Where a signed-in viewer belongs. */
/** A person's real name for prefilling forms; demo placeholders such as "Student (demo)" are not names. */
export function realName(viewer: Viewer | null): string {
  const n = viewer?.displayName?.trim() ?? ''
  return /\(demo\)$/i.test(n) ? '' : n
}

export function homePathFor(viewer: Viewer | null, ctx: HouseholdContext | null): string {
  if (!viewer) return '/'
  if (ctx?.myStudent) return '/student'
  if (ctx?.memberships.some((m) => m.role === 'guardian')) return '/parent'
  return '/start'
}

/** Small async-data hook with reload. */
export function useAsync<T>(fn: () => Promise<T>, deps: unknown[]): { data: T | undefined; error: Error | null; loading: boolean; reload: () => void } {
  const [state, setState] = useState<{ data: T | undefined; error: Error | null; loading: boolean }>({ data: undefined, error: null, loading: true })
  const [tick, setTick] = useState(0)
  useEffect(() => {
    let alive = true
    setState((s) => ({ ...s, loading: true }))
    fn().then(
      (data) => alive && setState({ data, error: null, loading: false }),
      (error: Error) => alive && setState({ data: undefined, error, loading: false }),
    )
    return () => {
      alive = false
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [...deps, tick])
  return { ...state, reload: () => setTick((t) => t + 1) }
}
