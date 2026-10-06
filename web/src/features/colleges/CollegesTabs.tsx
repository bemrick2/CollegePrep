import { NavLink } from 'react-router-dom'
import { cx } from '../../components/ui'

export function CollegesTabs() {
  const tab = ({ isActive }: { isActive: boolean }) =>
    cx('shrink-0 whitespace-nowrap rounded-full px-4 py-1.5 text-sm font-semibold', isActive ? 'bg-ink text-surface' : 'text-ink-2 hover:bg-surface-2')
  return (
    <nav aria-label="Colleges views" className="-mx-1 flex max-w-full gap-1 overflow-x-auto px-1">
      <NavLink to="/colleges" end className={tab}>
        Your colleges
      </NavLink>
      <NavLink to="/colleges/compare" className={tab}>
        Compare
      </NavLink>
      <NavLink to="/colleges/paths" className={tab}>
        Paths
      </NavLink>
      <NavLink to="/colleges/majors" className={tab}>
        Majors
      </NavLink>
    </nav>
  )
}
