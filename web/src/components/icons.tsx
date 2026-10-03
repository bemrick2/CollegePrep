import type { SVGProps } from 'react'

type P = SVGProps<SVGSVGElement> & { size?: number }

function Base({ size = 20, children, ...rest }: P & { children: React.ReactNode }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" aria-hidden {...rest}>
      {children}
    </svg>
  )
}

export const Flame = (p: P) => (
  <Base {...p}>
    <path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-2 .8-3.4 2-4.5.2 1.6 1 2.5 2 2.5-.5-3 .1-5.6 1-8Z" />
  </Base>
)
export const Target = (p: P) => (
  <Base {...p}>
    <circle cx="12" cy="12" r="9" />
    <circle cx="12" cy="12" r="5" />
    <circle cx="12" cy="12" r="1" />
  </Base>
)
export const Check = (p: P) => (
  <Base {...p}>
    <path d="m5 12.5 4.5 4.5L19 7.5" />
  </Base>
)
export const X = (p: P) => (
  <Base {...p}>
    <path d="M6 6l12 12M18 6 6 18" />
  </Base>
)
export const Clock = (p: P) => (
  <Base {...p}>
    <circle cx="12" cy="12" r="9" />
    <path d="M12 7v5l3 2" />
  </Base>
)
export const Home = (p: P) => (
  <Base {...p}>
    <path d="M4 10.5 12 4l8 6.5V20a1 1 0 0 1-1 1h-4.5v-6h-5v6H5a1 1 0 0 1-1-1z" />
  </Base>
)
export const Bolt = (p: P) => (
  <Base {...p}>
    <path d="M13 3 5 13.5h6L10 21l8-10.5h-6z" />
  </Base>
)
export const Chart = (p: P) => (
  <Base {...p}>
    <path d="M4 20V10M10 20V4M16 20v-7M22 20H2" />
  </Base>
)
export const School = (p: P) => (
  <Base {...p}>
    <path d="m2 9 10-5 10 5-10 5z" />
    <path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5" />
  </Base>
)
export const Lightbulb = (p: P) => (
  <Base {...p}>
    <path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3Z" />
  </Base>
)
export const Compass = (p: P) => (
  <Base {...p}>
    <circle cx="12" cy="12" r="9" />
    <path d="m15.5 8.5-2 5-5 2 2-5z" />
  </Base>
)
export const ArrowRight = (p: P) => (
  <Base {...p}>
    <path d="M5 12h14M13 6l6 6-6 6" />
  </Base>
)
export const ChevronLeft = (p: P) => (
  <Base {...p}>
    <path d="m15 6-6 6 6 6" />
  </Base>
)
export const ChevronRight = (p: P) => (
  <Base {...p}>
    <path d="m9 6 6 6-6 6" />
  </Base>
)
export const Users = (p: P) => (
  <Base {...p}>
    <circle cx="9" cy="8" r="3.5" />
    <path d="M2.5 20c.6-3.4 3.3-5.5 6.5-5.5s5.9 2.1 6.5 5.5" />
    <path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.8c2 .7 3.2 2.5 3.5 5.2" />
  </Base>
)
export const Wallet = (p: P) => (
  <Base {...p}>
    <path d="M3 7a2 2 0 0 1 2-2h12v4" />
    <rect x="3" y="7" width="18" height="13" rx="2" />
    <path d="M16 13.5h2" />
  </Base>
)
export const Shield = (p: P) => (
  <Base {...p}>
    <path d="M12 3 4.5 6v6c0 4.5 3.2 7.8 7.5 9 4.3-1.2 7.5-4.5 7.5-9V6z" />
    <path d="m9 12 2 2 4-4" />
  </Base>
)
export const Trophy = (p: P) => (
  <Base {...p}>
    <path d="M8 4h8v5a4 4 0 0 1-8 0z" />
    <path d="M8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4M12 13v4M8.5 21h7M10 17h4v4h-4z" />
  </Base>
)
export const Sparkle = (p: P) => (
  <Base {...p}>
    <path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6" />
  </Base>
)
export const Flag = (p: P) => (
  <Base {...p}>
    <path d="M5 21V4M5 4h11l-2 4 2 4H5" />
  </Base>
)
export const Book = (p: P) => (
  <Base {...p}>
    <path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z" />
    <path d="M4 19V5M19 19v2H6" />
  </Base>
)
export const Gauge = (p: P) => (
  <Base {...p}>
    <path d="M4 17a8 8 0 1 1 16 0" />
    <path d="m12 17 4-6" />
  </Base>
)
export const Info = (p: P) => (
  <Base {...p}>
    <circle cx="12" cy="12" r="9" />
    <path d="M12 11v5M12 8h.01" />
  </Base>
)
export const Logo = ({ size = 28 }: { size?: number }) => (
  <svg width={size} height={size} viewBox="0 0 32 32" aria-hidden>
    <rect width="32" height="32" rx="8" fill="var(--brand)" />
    <path d="M9 22V10h6.5a4 4 0 0 1 0 8H9" fill="none" stroke="var(--gold)" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
    <circle cx="22.5" cy="21.5" r="2.5" fill="var(--gold)" />
  </svg>
)
