import '@testing-library/jest-dom/vitest'
import { afterEach } from 'vitest'
import { cleanup, configure } from '@testing-library/react'
import { resetInterestCache } from '../features/majors/useInterests'

// Lazy routes and demo-store reads can exceed the 1s default when the whole suite runs in parallel (CI).
configure({ asyncUtilTimeout: 5000 })

afterEach(() => {
  cleanup()
  localStorage.clear()
  resetInterestCache()
})
