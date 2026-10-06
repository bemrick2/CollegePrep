import { describe, expect, it } from 'vitest'
import { storeOrder, storeUrl } from './storeLinks'

describe('store links', () => {
  it('only accepts official store URLs; anything else is "coming soon"', () => {
    expect(storeUrl('apple', {})).toBeNull()
    expect(storeUrl('apple', { VITE_APP_STORE_URL: 'https://example.com/app' })).toBeNull()
    expect(storeUrl('apple', { VITE_APP_STORE_URL: 'https://apps.apple.com/us/app/prep-price/id123' })).toBe('https://apps.apple.com/us/app/prep-price/id123')
    expect(storeUrl('google', { VITE_PLAY_STORE_URL: 'https://play.google.com/store/apps/details?id=com.prepandprice.app' })).toMatch(/^https:\/\/play\.google\.com/)
    expect(storeUrl('google', { VITE_PLAY_STORE_URL: '#' })).toBeNull()
  })
  it('orders by device but always offers both', () => {
    expect(storeOrder('Mozilla/5.0 (Linux; Android 15; Pixel 9)')).toEqual(['google', 'apple'])
    expect(storeOrder('Mozilla/5.0 (iPhone; CPU iPhone OS 19_0 like Mac OS X)')).toEqual(['apple', 'google'])
    expect(storeOrder('')).toEqual(['apple', 'google'])
  })
})
