import { describe, expect, it } from 'vitest'
import { fitSentence, schoolFit } from './programFit'
import type { SavedInterest } from './interests'

const cs: SavedInterest = { kind: 'major', key: 'computer-science' }
const fin: SavedInterest = { kind: 'major', key: 'finance' }
const eng: SavedInterest = { kind: 'area', key: 'engineering' }
const utk = {
  academic_programs: [{ program_key: 'computer-science-bs', program_name: 'Computer Science Major, BS in Computer Science', credential_level: 'bachelor' }],
  degree_requirements: [
    {
      program_key: 'computer-science-bs',
      rule_details: {
        terms: [{ term_index: 1, items: ['ENGL 101', 'COSC 103', 'MATH 132 or MATH 141 or MATH 147'] }],
        progression: 'Progression to upper-division departmental programs is competitive and space-limited.',
      },
    },
  ],
  awards: [{ award_name: 'Haslam Business Scholars', major_requirement: 'Finance or accounting majors' }],
}

describe('schoolFit', () => {
  it('reports verified programs, quotes progression rules, and never treats a partial list as "not offered"', () => {
    const f = schoolFit(utk, [cs, fin, eng])
    expect(f.fits.map((x) => x.status)).toEqual(['verified', 'not_listed', 'verified'])
    expect(f.fits[0]!.progression[0]!.text).toMatch(/competitive and space-limited/)
    expect(f.fits[1]!.scholarships[0]!.name).toBe('Haslam Business Scholars')
    expect(fitSentence('UTK', f)).toBe("UTK has verified programs for Computer science and Engineering & technology; Finance isn't in our verified list yet.")
  })

  it('says nothing about programs when the school has no program data', () => {
    const f = schoolFit({}, [cs])
    expect(f.fits[0]!.status).toBe('no_data')
    expect(fitSentence('Lipscomb', f)).toBe("We haven't verified Lipscomb's program list yet.")
  })

  it('names direct admission only when the backend states it', () => {
    const withAdmission = { academic_programs: [...utk.academic_programs, { program_key: 'me-bs', program_name: 'Mechanical Engineering, BS', admission_type: 'direct' as const }] }
    const f = schoolFit(withAdmission, [{ kind: 'major', key: 'mechanical-eng' }, cs])
    expect(fitSentence('UTK', f)).toBe('UTK has verified programs for both of your interests, but Mechanical engineering requires freshman admission.')
  })

  it('finds shared first-year courses only across two published maps', () => {
    expect(schoolFit(utk, [cs]).sharedFirstYear).toBeNull()
    const two = {
      academic_programs: [...utk.academic_programs, { program_key: 'math-bs', program_name: 'Mathematics, BS' }],
      degree_requirements: [...utk.degree_requirements, { program_key: 'math-bs', rule_details: { terms: [{ term_index: 1, items: ['ENGL 101', 'MATH 141'] }] } }],
    }
    expect(schoolFit(two, [cs, { kind: 'major', key: 'mathematics' }]).sharedFirstYear!.courses).toEqual(['ENGL 101'])
  })
})
