import { describe, expect, it, beforeEach } from 'vitest'
import { act, renderHook, waitFor } from '@testing-library/react'
import type { ReactNode } from 'react'
import { AppProvider } from '../../lib/app'
import { DemoSource } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import { DataError } from '../../lib/data/source'
import { examKey, type PlannedExam } from '../../lib/engine/examCredit'
import { useExamPlan } from './useExamPlan'

/** A source with CR-10: AP and CLEP go to the "account"; anything else is refused as 'invalid'. */
class AccountPlan extends DemoSource {
  account: PlannedExam[] = []
  override readonly supportsExamPlan = true
  override async examPlan() {
    return [...this.account]
  }
  override async saveExamPlanEntry(_s: string, e: PlannedExam) {
    if (e.family !== 'AP' && e.family !== 'CLEP') throw new DataError('no key', 'invalid')
    this.account = [...this.account.filter((x) => x.key !== e.key), e]
  }
  override async removeExamPlanEntry(_s: string, key: string) {
    this.account = this.account.filter((x) => x.key !== key)
  }
}
const ap = (name: string, score: number | null): PlannedExam => ({ family: 'AP', key: examKey('AP', name), name, score })

describe('useExamPlan (CR-10)', () => {
  beforeEach(() => localStorage.clear())

  it('without CR-10 the plan stays on this device', async () => {
    const src = new DemoSource(emptyStore())
    const wrap = ({ children }: { children: ReactNode }) => <AppProvider source={src}>{children}</AppProvider>
    const { result } = renderHook(() => useExamPlan('s1'), { wrapper: wrap })
    act(() => void result.current.add(ap('AP Calculus AB', null)))
    await waitFor(() => expect(result.current.exams).toHaveLength(1))
    expect(result.current.onAccount).toBe(false)
    expect(JSON.parse(localStorage.getItem('pp-exam-plan:s1')!)).toHaveLength(1)
  })

  it('with CR-10, AP and CLEP go to the account (and leave the device); IB stays on the device', async () => {
    localStorage.setItem('pp-exam-plan:s1', JSON.stringify([ap('AP Microeconomics', 3)]))
    const src = new AccountPlan(emptyStore())
    const wrap = ({ children }: { children: ReactNode }) => <AppProvider source={src}>{children}</AppProvider>
    const { result } = renderHook(() => useExamPlan('s1'), { wrapper: wrap })
    expect(result.current.onDevice.has(examKey('AP', 'Microeconomics'))).toBe(true)
    // Re-saving a device exam (a score change) moves it to the account.
    act(() => result.current.setScore(examKey('AP', 'Microeconomics'), 4))
    await waitFor(() => expect(src.account).toEqual([{ ...ap('AP Microeconomics', 4) }]))
    await waitFor(() => expect(result.current.onDevice.size).toBe(0))
    act(() => void result.current.add({ family: 'IB', key: examKey('IB', 'Economics'), name: 'IB Economics', score: null, level: 'SL' }))
    await waitFor(() => expect(result.current.onDevice.has(examKey('IB', 'Economics'))).toBe(true))
    expect(result.current.exams.map((e) => e.key).sort()).toEqual([examKey('AP', 'Microeconomics'), examKey('IB', 'Economics')].sort())
    act(() => result.current.remove(examKey('AP', 'Microeconomics')))
    await waitFor(() => expect(src.account).toEqual([]))
  })
})
