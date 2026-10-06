/**
 * App store listings. Set at build time once the listings are live:
 *   VITE_APP_STORE_URL=https://apps.apple.com/...   VITE_PLAY_STORE_URL=https://play.google.com/store/apps/details?id=...
 * Unset (or not an official store host) means "coming soon": no badge, no link. Never a placeholder URL.
 *
 * The badge artwork must be the official files (see docs/product/APP_DISTRIBUTION_AND_PAYMENTS.md), placed at
 * public/badges/app-store-badge.svg and public/badges/google-play-badge.png when the listings go live.
 */

export type Store = 'apple' | 'google'

const HOSTS: Record<Store, RegExp> = {
  apple: /^https:\/\/apps\.apple\.com\//,
  google: /^https:\/\/play\.google\.com\/store\/apps\/details\?id=[\w.]+/,
}

export function storeUrl(store: Store, env: Record<string, string | undefined> = import.meta.env as Record<string, string | undefined>): string | null {
  const v = (store === 'apple' ? env.VITE_APP_STORE_URL : env.VITE_PLAY_STORE_URL)?.trim()
  return v && HOSTS[store].test(v) ? v : null
}

/** iPhone/iPad visitors see the App Store first, Android visitors Google Play; both are always offered. */
export function storeOrder(userAgent: string = typeof navigator === 'undefined' ? '' : navigator.userAgent): Store[] {
  if (/android/i.test(userAgent)) return ['google', 'apple']
  return ['apple', 'google']
}

export const BADGE = {
  apple: { src: '/badges/app-store-badge.svg', alt: 'Download on the App Store' },
  google: { src: '/badges/google-play-badge.png', alt: 'Get it on Google Play' },
} as const
