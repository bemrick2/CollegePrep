/**
 * Academic interests for exploration. This list is ours, not a school's: it groups common majors under broad
 * areas so an undecided student can start somewhere. Whether a school offers a program is decided only by its
 * verified academic_programs records (see programFit.ts).
 *
 * `cip` is the 2-digit CIP family (NCES Classification of Instructional Programs), used when a verified program
 * carries a CIP code; `match` are name patterns used otherwise (program names vary by school).
 */

export type MajorCertainty = 'unsure' | 'few' | 'sure'

export const CERTAINTY_OPTIONS: { value: MajorCertainty; label: string; hint: string }[] = [
  { value: 'unsure', label: "I'm not sure yet", hint: 'Pick broad interests, or skip. Nothing is locked in.' },
  { value: 'few', label: "I'm considering a few things", hint: 'Save a few possible majors. No need to rank them.' },
  { value: 'sure', label: "I'm pretty sure", hint: "Save the major you're leaning toward. You can add others any time." },
]

export interface MajorOption {
  key: string
  label: string
  cip: string[]
  /** Case-insensitive patterns against a program's name. */
  match: RegExp[]
}

export interface InterestArea {
  key: string
  label: string
  cip: string[]
  majors: MajorOption[]
}

const m = (key: string, label: string, cip: string[], ...match: RegExp[]): MajorOption => ({ key, label, cip, match })

export const INTEREST_AREAS: InterestArea[] = [
  {
    key: 'business',
    label: 'Business',
    cip: ['52'],
    majors: [
      m('finance', 'Finance', ['52'], /\bfinanc/i),
      m('accounting', 'Accounting', ['52'], /\baccount/i),
      m('marketing', 'Marketing', ['52'], /\bmarketing/i),
      m('management', 'Management', ['52'], /\bmanagement\b/i, /business admin/i),
      m('entrepreneurship', 'Entrepreneurship', ['52'], /entrepreneur/i),
    ],
  },
  {
    key: 'engineering',
    label: 'Engineering & technology',
    cip: ['14', '11', '15'],
    majors: [
      m('mechanical-eng', 'Mechanical engineering', ['14'], /mechanical engineering/i),
      m('electrical-eng', 'Electrical engineering', ['14'], /electrical (and computer )?engineering/i),
      m('civil-eng', 'Civil engineering', ['14'], /civil engineering/i),
      m('biomedical-eng', 'Biomedical engineering', ['14'], /biomedical engineering/i),
      m('computer-science', 'Computer science', ['11'], /computer science/i),
      m('information-tech', 'Information technology', ['11'], /information (technology|systems)/i),
    ],
  },
  {
    key: 'health',
    label: 'Health',
    cip: ['51'],
    majors: [
      m('nursing', 'Nursing', ['51'], /\bnursing\b/i),
      m('public-health', 'Public health', ['51'], /public health/i),
      m('kinesiology', 'Kinesiology / exercise science', ['31', '51'], /kinesiology|exercise science/i),
      m('pre-health', 'Pre-med / pre-health (track)', ['26', '51'], /pre-?(med|health|professional)/i),
    ],
  },
  {
    key: 'science',
    label: 'Science',
    cip: ['26', '40', '03'],
    majors: [
      m('biology', 'Biology', ['26'], /\bbiolog/i),
      m('chemistry', 'Chemistry', ['40'], /\bchemistry/i),
      m('physics', 'Physics', ['40'], /\bphysics/i),
      m('environmental', 'Environmental science', ['03'], /environmental (science|studies)/i),
    ],
  },
  {
    key: 'math',
    label: 'Math & data',
    cip: ['27', '30'],
    majors: [m('mathematics', 'Mathematics', ['27'], /\bmathemat/i), m('statistics', 'Statistics / data science', ['27', '30'], /statistic|data science/i)],
  },
  {
    key: 'social',
    label: 'Social sciences',
    cip: ['42', '45'],
    majors: [
      m('psychology', 'Psychology', ['42'], /psycholog/i),
      m('economics', 'Economics', ['45'], /\beconomics/i),
      m('political-science', 'Political science', ['45'], /political science|government/i),
      m('sociology', 'Sociology', ['45'], /sociolog/i),
    ],
  },
  {
    key: 'education',
    label: 'Education',
    cip: ['13'],
    majors: [m('elementary-ed', 'Elementary education', ['13'], /elementary education/i), m('secondary-ed', 'Secondary education', ['13'], /secondary education|teacher/i)],
  },
  {
    key: 'creative',
    label: 'Creative fields',
    cip: ['50'],
    majors: [
      m('art-design', 'Art & design', ['50'], /\b(fine|studio|visual) arts?\b|\bart history\b|graphic design|interior design|industrial design/i),
      m('music', 'Music', ['50'], /\bmusic/i),
      m('film-media', 'Film & media', ['50', '09'], /\bfilm|cinema|media arts/i),
      m('theatre', 'Theatre', ['50'], /theat(re|er)/i),
    ],
  },
  {
    key: 'humanities',
    label: 'Humanities',
    cip: ['23', '54', '38', '16'],
    majors: [
      m('english', 'English', ['23'], /\benglish\b/i),
      m('history', 'History', ['54'], /\bhistory\b/i),
      m('philosophy', 'Philosophy', ['38'], /philosoph/i),
      m('languages', 'World languages', ['16'], /spanish|french|german|chinese|japanese|languages/i),
    ],
  },
  {
    key: 'communication',
    label: 'Communication & media',
    cip: ['09'],
    majors: [m('communication', 'Communication', ['09'], /communication/i), m('journalism', 'Journalism', ['09'], /journalism/i)],
  },
  {
    key: 'public-service',
    label: 'Law & public service',
    cip: ['43', '44'],
    majors: [m('criminal-justice', 'Criminal justice', ['43'], /criminal justice|criminology/i), m('social-work', 'Social work', ['44'], /social work/i)],
  },
]

export const MAJORS: MajorOption[] = INTEREST_AREAS.flatMap((a) => a.majors)
export const areaOf = (majorKey: string) => INTEREST_AREAS.find((a) => a.majors.some((x) => x.key === majorKey))

/** A saved interest: a broad area or a specific major. `focus` is set only when the student chooses one. */
export interface SavedInterest {
  kind: 'area' | 'major'
  key: string
  focus?: boolean
}

export interface InterestProfile {
  certainty: MajorCertainty | null
  interests: SavedInterest[]
}

export const MAX_INTERESTS = 8

export function labelOf(i: SavedInterest): string {
  return i.kind === 'area' ? (INTEREST_AREAS.find((a) => a.key === i.key)?.label ?? i.key) : (MAJORS.find((x) => x.key === i.key)?.label ?? i.key)
}
