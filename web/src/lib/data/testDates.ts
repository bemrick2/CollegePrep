import type { ExamFamily } from './types'

/**
 * National test dates as the test makers publish them. Checked 2026-10-07; re-check each term.
 * `projected`: the publisher lists the date as anticipated or subject to change.
 */
export const TEST_DATES_CHECKED = '2026-10-07'

export const TEST_DATE_SOURCES: Record<ExamFamily, string> = {
  act: 'https://www.act.org/content/act/en/products-and-services/the-act/registration/test-dates.html',
  sat: 'https://satsuite.collegeboard.org/sat/register/dates-deadlines',
}

export interface TestDate {
  date: string
  projected: boolean
}

export const TEST_DATES: Record<ExamFamily, TestDate[]> = {
  act: [
    { date: '2026-09-19', projected: false },
    { date: '2026-10-17', projected: false },
    { date: '2026-12-12', projected: false },
    { date: '2027-02-27', projected: false },
    { date: '2027-04-10', projected: false },
    { date: '2027-06-12', projected: false },
    { date: '2027-07-10', projected: false },
    { date: '2027-09-11', projected: true },
    { date: '2027-10-16', projected: true },
    { date: '2027-12-11', projected: true },
  ],
  sat: [
    { date: '2026-10-03', projected: false },
    { date: '2026-11-07', projected: false },
    { date: '2026-12-05', projected: false },
    { date: '2027-03-06', projected: false },
    { date: '2027-05-01', projected: false },
    { date: '2027-06-05', projected: false },
    { date: '2027-08-28', projected: true },
    { date: '2027-09-18', projected: true },
    { date: '2027-10-09', projected: true },
    { date: '2027-11-06', projected: true },
    { date: '2027-12-04', projected: true },
  ],
}

/** Dates still ahead of `today` (local ISO date), soonest first. */
export function upcomingTestDates(exam: ExamFamily, today: string): TestDate[] {
  return TEST_DATES[exam].filter((d) => d.date > today)
}
