import type {
  BenchmarkSummary,
  Household,
  HouseholdMember,
  Student,
  StudentPlan,
  TestScore,
} from '../types'
import type { EngineAttempt, EngineEvent } from '../../engine/analytics'

export interface DemoUser {
  id: string
  displayName: string
}

export interface DemoInvitation {
  code: string
  household_id: string
  role: 'guardian' | 'student'
  student_id: string | null
  expires_at: string
  accepted_by: string | null
  id?: string
  short_code?: string
  created_at?: string
  accepted_at?: string | null
  recipient_email?: string | null
  revoked_at?: string | null
}

export interface DemoGoal {
  id: string
  student_id: string
  week_start: string
  target_questions: number | null
  target_minutes: number | null
  goal_mode: 'fixed' | 'adaptive'
}

export interface DemoAttempt extends EngineAttempt {
  student_id: string
  session_id: string | null
  selected_answer: string | null
  attempt_number: number
  last_answer: string | null
}

export interface DemoEvent extends EngineEvent {
  student_id: string
}

export interface DemoStore {
  version: 1
  viewerId: string | null
  users: DemoUser[]
  households: Household[]
  members: HouseholdMember[]
  students: Student[]
  invitations: DemoInvitation[]
  goals: DemoGoal[]
  sessions: { id: string; student_id: string; target_minutes: number; started_at: string; ended_at: string | null; question_ids: string[] }[]
  attempts: DemoAttempt[]
  events: DemoEvent[]
  scores: (TestScore & { student_id: string })[]
  plans: Record<string, StudentPlan>
  benchmarks: Record<string, BenchmarkSummary[]>
}

const KEY = 'pp-demo-v1'

export function emptyStore(): DemoStore {
  return {
    version: 1,
    viewerId: null,
    users: [],
    households: [],
    members: [],
    students: [],
    invitations: [],
    goals: [],
    sessions: [],
    attempts: [],
    events: [],
    scores: [],
    plans: {},
    benchmarks: {},
  }
}

export function loadStore(): DemoStore {
  try {
    const raw = localStorage.getItem(KEY)
    if (raw) {
      const parsed = JSON.parse(raw) as DemoStore
      if (parsed.version === 1) return parsed
    }
  } catch {
    // Storage blocked or corrupt: start fresh in memory.
  }
  return emptyStore()
}

export function saveStore(store: DemoStore): void {
  try {
    localStorage.setItem(KEY, JSON.stringify(store))
  } catch {
    // Private mode or quota: the demo keeps working for this tab only.
  }
}

export function clearStore(): void {
  try {
    localStorage.removeItem(KEY)
  } catch {
    // ignore
  }
}

export function uid(prefix = ''): string {
  const c = globalThis.crypto
  const id = c && 'randomUUID' in c ? c.randomUUID() : Math.random().toString(36).slice(2) + Date.now().toString(36)
  return prefix + id
}
