import { describe, expect, it, beforeEach } from 'vitest'
import { act, renderHook, waitFor } from '@testing-library/react'
import type { ReactNode } from 'react'
import { AppProvider } from '../../lib/app'
import { DemoSource } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import { DataError } from '../../lib/data/source'
import { examKey, type PlannedExam } from '../../lib/engine/examCredit'
import { useExamPlan } from './useExamPlan'

/** A source with CR-10: AP and CLEP go to the "account"; anything else has no catalog key ('not_found'). */
class AccountPlan extends DemoSource {
  byStudent: Record<string, PlannedExam[]> = {}
  gate: Promise<void> | null = null
  limit = 20
  override readonly supportsExamPlan = true
  get account() {
    return this.byStudent.s1 ?? []
  }
  set account(v: PlannedExam[]) {
    this.byStudent.s1 = v
  }
  override async examPlan(id: string) {
    return [...(this.byStudent[id] ?? [])]
  }
  override async saveExamPlanEntry(id: string, e: PlannedExam) {
    if (e.family !== 'AP' && e.family !== 'CLEP') throw new DataError('no key', 'not_found')
    if (this.gate) await this.gate
    const cur = this.byStudent[id] ?? []
    if (!cur.some((x) => x.key === e.key) && cur.length >= this.limit) throw new DataError("A student's exam plan holds up to 20 exams", 'invalid')
    this.byStudent[id] = [...cur.filter((x) => x.key !== e.key), e]
  }
  override async removeExamPlanEntry(id: string, key: string) {
    this.byStudent[id] = (this.byStudent[id] ?? []).filter((x) => x.key !== key)
  }
}
const ap = (name: string, score: number | null): PlannedExam => ({ family: 'AP', key: examKey('AP', name), name, score })
const ib: PlannedExam = { family: 'IB', key: examKey('IB', 'Economics'), name: 'IB Economics', score: null, level: 'SL' }
const stored = () => JSON.parse(localStorage.getItem('pp-exam-plan:s1') ?? '[]') as PlannedExam[]
const hook = (src: DemoSource, canEdit = true) =>
  renderHook(() => useExamPlan('s1', canEdit), { wrapper: ({ children }: { children: ReactNode }) => <AppProvider source={src}>{children}</AppProvider> })

describe('useExamPlan (CR-10)', () => {
  beforeEach(() => localStorage.clear())

  it('without CR-10 the plan stays on this device', async () => {
    const { result } = hook(new DemoSource(emptyStore()))
    act(() => void result.current.add(ap('AP Calculus AB', null)))
    await waitFor(() => expect(result.current.exams).toHaveLength(1))
    expect(result.current.onAccount).toBe(false)
    expect(stored()).toHaveLength(1)
  })

  it('device AP/CLEP entries move to the account once it loads; IB stays on the device and is named as such', async () => {
    localStorage.setItem('pp-exam-plan:s1', JSON.stringify([ap('AP Microeconomics', 3), ib]))
    const src = new AccountPlan(emptyStore())
    const { result } = hook(src)
    await waitFor(() => expect(src.account).toEqual([ap('AP Microeconomics', 3)]))
    await waitFor(() => expect([...result.current.onDevice]).toEqual([ib.key]))
    expect(stored()).toEqual([ib])
    act(() => result.current.remove(examKey('AP', 'Microeconomics')))
    await waitFor(() => expect(src.account).toEqual([]))
  })

  it('a save in flight never brings back a stale device list (an exam added meanwhile survives)', async () => {
    const src = new AccountPlan(emptyStore())
    const { result } = hook(src)
    await waitFor(() => expect(result.current.ready).toBe(true))
    let open!: () => void
    src.gate = new Promise((r) => (open = r))
    act(() => void result.current.add(ap('AP Statistics', 4)))
    act(() => void result.current.add(ib))
    await waitFor(() => expect(stored()).toEqual([ib]))
    await act(async () => open())
    await waitFor(() => expect(src.account.map((e) => e.key)).toEqual([examKey('AP', 'Statistics')]))
    expect(stored()).toEqual([ib])
    expect(result.current.exams.map((e) => e.key).sort()).toEqual([examKey('AP', 'Statistics'), ib.key].sort())
  })

  it('edits wait until device entries have moved; a device score beats a planned account entry', async () => {
    localStorage.setItem('pp-exam-plan:s1', JSON.stringify([ap('AP Biology', 3), ap('AP Chemistry', 2)]))
    const src = new AccountPlan(emptyStore())
    src.account = [ap('AP Biology', null)]
    let open!: () => void
    src.gate = new Promise((r) => (open = r))
    const { result } = hook(src)
    await waitFor(() => expect(result.current.exams).toHaveLength(2))
    // Still moving: edits are refused rather than raced.
    expect(result.current.ready).toBe(false)
    expect(result.current.add(ap('AP Physics 1', null))).toBe(false)
    act(() => result.current.remove(examKey('AP', 'Chemistry')))
    act(() => result.current.setScore(examKey('AP', 'Chemistry'), 5))
    // Both were refused: nothing changed on screen or on the device while moving.
    expect(result.current.exams.map((e) => [e.key, e.score])).toEqual([
      [examKey('AP', 'Biology'), null],
      [examKey('AP', 'Chemistry'), 2],
    ])
    await act(async () => open())
    await waitFor(() => expect(result.current.ready).toBe(true))
    expect(src.account.sort((a, b) => a.key.localeCompare(b.key))).toEqual([ap('AP Biology', 3), ap('AP Chemistry', 2)])
    expect(stored()).toEqual([])
    act(() => result.current.remove(examKey('AP', 'Chemistry')))
    await waitFor(() => expect(src.account).toEqual([ap('AP Biology', 3)]))
  })

  it('a save that finishes after switching student never lands on the other student', async () => {
    const src = new AccountPlan(emptyStore())
    src.byStudent.s2 = [ap('AP Chemistry', 4)]
    let open!: () => void
    const wrap = ({ children }: { children: ReactNode }) => <AppProvider source={src}>{children}</AppProvider>
    const { result, rerender } = renderHook(({ id }) => useExamPlan(id, true), { wrapper: wrap, initialProps: { id: 's1' } })
    await waitFor(() => expect(result.current.ready).toBe(true))
    src.gate = new Promise((r) => (open = r))
    act(() => void result.current.add(ap('AP Biology', 3)))
    src.gate = null
    rerender({ id: 's2' })
    await waitFor(() => expect(result.current.exams.map((e) => e.key)).toEqual([examKey('AP', 'Chemistry')]))
    await act(async () => open())
    await new Promise((r) => setTimeout(r, 50))
    // s1's exam was saved to s1, and s2's screen never shows it.
    expect(src.byStudent.s1).toEqual([ap('AP Biology', 3)])
    expect(result.current.exams.map((e) => e.key)).toEqual([examKey('AP', 'Chemistry')])
  })

  it('if the account plan cannot load, nothing is editable and the error is shown', async () => {
    const src = new AccountPlan(emptyStore())
    src.examPlan = async () => Promise.reject(new Error('offline'))
    const { result } = hook(src)
    await waitFor(() => expect(result.current.error).toBe('offline'))
    expect(result.current.ready).toBe(false)
    expect(result.current.add(ap('AP Biology', null))).toBe(false)
  })

  it('a real error (the 20-exam limit) is shown, not silently kept on the device', async () => {
    const src = new AccountPlan(emptyStore())
    src.limit = 0
    const { result } = hook(src)
    await waitFor(() => expect(result.current.ready).toBe(true))
    act(() => void result.current.add(ap('AP Biology', null)))
    await waitFor(() => expect(result.current.error).toMatch(/up to 20 exams/))
    expect(stored()).toEqual([])
  })

  it('a viewer who may not edit changes nothing, and nothing is moved for them', async () => {
    localStorage.setItem('pp-exam-plan:s1', JSON.stringify([ap('AP Microeconomics', 3)]))
    const src = new AccountPlan(emptyStore())
    const { result } = hook(src, false)
    await waitFor(() => expect(result.current.ready).toBe(true))
    expect(result.current.add(ap('AP Biology', null))).toBe(false)
    act(() => result.current.setScore(examKey('AP', 'Microeconomics'), 5))
    act(() => result.current.remove(examKey('AP', 'Microeconomics')))
    expect(src.account).toEqual([])
    expect(stored()).toEqual([ap('AP Microeconomics', 3)])
  })
})
