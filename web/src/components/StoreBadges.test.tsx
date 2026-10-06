import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import { StoreBadges } from './StoreBadges'

afterEach(() => vi.unstubAllEnvs())

describe('StoreBadges', () => {
  it('links official badge artwork only for configured listings, and marks the other platform coming soon', () => {
    vi.stubEnv('VITE_APP_STORE_URL', 'https://apps.apple.com/us/app/prep-price/id123')
    render(<StoreBadges />)
    const link = screen.getByRole('link', { name: 'Download on the App Store' })
    expect(link).toHaveAttribute('href', 'https://apps.apple.com/us/app/prep-price/id123')
    expect(screen.getByRole('img', { name: 'Download on the App Store' })).toHaveAttribute('src', '/badges/app-store-badge.svg')
    expect(screen.queryByRole('link', { name: /Google Play/ })).not.toBeInTheDocument()
    expect(screen.getByText('Android app coming soon')).toBeInTheDocument()
  })
})
