import type { DataSource, DevicePermission, DevicePlatform } from './data/source'

/**
 * This browser as a reminder device. What the app can know, and when:
 * - the notification permission and push subscription, read when the app opens (and right after the student
 *   allows notifications). Turning notifications off in phone or browser settings while the app is closed is not
 *   visible until the app is opened again on that device, so nothing here claims immediate detection;
 * - "blocked" (the device setting) is never confused with "off" (the family's in-app choice).
 */

const DEVICE_KEY = 'pp-device-id'
export const VAPID_PUBLIC_KEY: string = (import.meta.env.VITE_VAPID_PUBLIC_KEY as string | undefined) ?? ''

export function deviceId(): string {
  try {
    const have = localStorage.getItem(DEVICE_KEY)
    if (have) return have
    const id = crypto.randomUUID()
    localStorage.setItem(DEVICE_KEY, id)
    return id
  } catch {
    return crypto.randomUUID()
  }
}

export function devicePlatform(ua = typeof navigator === 'undefined' ? '' : navigator.userAgent, touch = typeof navigator !== 'undefined' && navigator.maxTouchPoints > 1): DevicePlatform {
  if (/iPhone|iPad|iPod/.test(ua) || (/Macintosh/.test(ua) && touch)) return 'ios'
  if (/Android/.test(ua)) return 'android'
  if (/Windows|Macintosh|Linux|CrOS/.test(ua)) return 'desktop'
  return 'other'
}

export interface DeviceSupport {
  /** Notifications and push both exist in this browser. */
  push: boolean
  platform: DevicePlatform
  /** iPhone/iPad: web push only works after "Add to Home Screen", opened from there. */
  needsHomeScreen: boolean
  /** The app has a push key configured (VITE_VAPID_PUBLIC_KEY). */
  configured: boolean
}

export function deviceSupport(): DeviceSupport {
  const platform = devicePlatform()
  const hasApi = typeof window !== 'undefined' && 'Notification' in window && 'serviceWorker' in navigator && 'PushManager' in window
  const standalone = typeof window !== 'undefined' && (window.matchMedia?.('(display-mode: standalone)').matches || (navigator as unknown as { standalone?: boolean }).standalone === true)
  return { push: hasApi, platform, needsHomeScreen: platform === 'ios' && !standalone, configured: !!VAPID_PUBLIC_KEY }
}

export interface DeviceState {
  permission: DevicePermission
  subscription: PushSubscriptionJSON | null
}

/** Reads this browser's state now. Never prompts. */
export async function readDeviceState(): Promise<DeviceState> {
  const s = deviceSupport()
  if (!s.push) return { permission: 'unsupported', subscription: null }
  const permission = Notification.permission as DevicePermission
  let subscription: PushSubscriptionJSON | null = null
  try {
    const reg = await navigator.serviceWorker.getRegistration('/')
    const sub = await reg?.pushManager.getSubscription()
    subscription = sub ? sub.toJSON() : null
  } catch {
    subscription = null
  }
  return { permission, subscription: permission === 'granted' ? subscription : null }
}

function keyBytes(b64url: string): Uint8Array<ArrayBuffer> {
  const b = atob(b64url.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((b64url.length + 3) % 4))
  return Uint8Array.from(b, (c) => c.charCodeAt(0))
}

/** Asks for permission (call from a tap) and subscribes. Returns the resulting state, whatever the answer. */
export async function enableOnThisDevice(): Promise<DeviceState> {
  const s = deviceSupport()
  if (!s.push || !s.configured) return readDeviceState()
  const answer = await Notification.requestPermission()
  if (answer !== 'granted') return { permission: answer as DevicePermission, subscription: null }
  const reg = await navigator.serviceWorker.register('/sw.js', { scope: '/' })
  await navigator.serviceWorker.ready
  const sub = (await reg.pushManager.getSubscription()) ?? (await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: keyBytes(VAPID_PUBLIC_KEY) }))
  return { permission: 'granted', subscription: sub.toJSON() }
}

export async function reportDevice(source: DataSource, state: DeviceState): Promise<void> {
  await source.reportNotificationDevice({ deviceId: deviceId(), permission: state.permission, subscription: state.subscription, platform: devicePlatform() })
}

export const PLATFORM_NAME: Record<DevicePlatform, string> = { ios: 'iPhone or iPad', android: 'Android phone', desktop: 'Computer', other: 'Device' }
