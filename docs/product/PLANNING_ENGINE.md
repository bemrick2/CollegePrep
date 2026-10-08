# Planning engine: design and data structures

Companion to `COLLEGE_PLANNING_PILOT.md` (the audit, gaps and MVP). Tracking issue: #198. Written 2026-10-08.

**Supabase status:** the hosted project is paused on purpose, and the owner has no date to reactivate it. Everything
in milestones P1–P4 below runs on the stored records in `data/` and in the browser. Only P5 and P6 need Supabase,
and they're deferred until the owner decides (`SUPABASE_DEFERRED.md`).

## 1. Principles (enforced by tests, not by convention)

1. **Records decide; the engine composes.** The engine reads the same `InstitutionComparison` shape that
   `compare_institutions` and the demo snapshot return. It reuses the existing pure modules and never re-implements
   their rules:
   - `examCredit`: acceptance of AP, CLEP, IB and Statewide Dual Credit.
   - `planItems` and `degreeCredit`: where credit lands in a plan.
   - `costProjection`: `termsSaving` and `potentialSaving`.
   - `residency`: which price applies.
   - `merit`: published single test minimums.
2. **Every output line carries its evidence.** The line has a state, and if the evidence is missing, the line says what's missing.

   | State | Shown as | Allowed source |
   |---|---|---|
   | `verified` | A fact, with source, review date and published year | A record whose `verification_status` is `verified` |
   | `estimate` | Labeled, with how it was computed | Arithmetic over verified values only (a sum of published hours, whole-term savings). Never a projection to a future year |
   | `missing` | "Not published" or "not on file", plus the exact item | Any gap, including `partially_verified` records |
   | `family` | "Your answer" | Values the family typed (scores, planned exams, home state) |
3. **Never invented.** The engine never invents an equivalency, prerequisite, requirement, award amount, saving or substitution. If no record says it, the line is `missing`.
4. **No ACT/SAT score predictions.** Merit lines compare a published minimum with an official, self-reported or target score, and they're labeled with which one was used. The engine never estimates a future score.
5. **Year honesty.** Every value carries the year it was published (catalog 2026-27, award 2027-28). A 9th grader in 2026 enters around 2030; the engine says so and never adjusts for inflation or later catalogs.

## 2. Data structures

These live in `web/src/lib/engine/planning/types.ts`. All of them are plain values, so they work the same in the demo, in live mode and in tests.

```ts
/** What the family told us. Every field is optional, and every value is labelled as the family's answer. */
interface PlanningProfile {
  gradeLevel: number | null            // students.grade_level (exists)
  graduationYear: number | null        // students.graduation_year (exists)
  homeState: string | null             // CR-15: browser today
  interests: SavedInterest[]           // CR-13: live
  exams: PlannedExam[]                 // CR-10: device today (AP, CLEP, IB with level, SDC)
  livingArrangement: LivingArrangement | null   // 'on_campus' | 'off_campus' | 'with_family'
  hsCourses: HsCourseEntry[]           // CR-28 proposal: device-only in the pilot
}

interface HsCourseEntry {
  name: string                          // as the family types it; never matched to a college course by us
  kind: 'ap' | 'ib' | 'dual_enrollment' | 'statewide_dual_credit' | 'honors' | 'standard'
  gradeLevel: number | null
  status: 'planned' | 'in_progress' | 'completed'
  institutionKey?: string | null        // dual enrollment: where the course is taken
}

interface PlanningTarget { institutionKey: string; programKey: string }

interface Evidence {
  state: 'verified' | 'estimate' | 'missing' | 'family'
  sourceUrl: string | null
  verificationStatus: string | null     // as stored
  lastVerifiedAt: string | null
  publishedYear: string | null          // catalog_year, academic_year
  method?: string                       // estimate: how it was computed, in words
  missing?: string                      // missing: what exactly isn't on file
}
interface Line<T> { value: T | null; evidence: Evidence }

interface Roadmap {
  target: PlanningTarget & { programName: string | null; institutionName: string | null }
  /** blocked: no verified plan for this major, so only acceptance can be shown. */
  status: 'ready' | 'partial' | 'blocked'
  plan: Line<{ catalogYear: string; terms: TermCoverage[]; totalCredits: number | null }>
  credit: CreditLine[]                  // one per planned exam
  /** Exams in this school's verified table whose course is in this major's verified plan: the data-backed "consider". */
  options: ExamOption[]
  dualEnrollment: Line<{ grades: string[]; minHsGpa: number | null; altMinAct: number | null; perCreditCharge: number | null }>
  cost: Line<{ arrangement: LivingArrangement; annual: number }>[]
  savings: Line<PotentialSaving>        // whole plan terms covered only (until CR-17)
  timeline: Line<{ termsCovered: number; termsInPlan: number }>   // value null unless termsCovered > 0
  unknowns: Unknown[]                   // generated from every `missing` line, deduplicated
}

interface CreditLine {
  exam: PlannedExam
  acceptance: Line<ExamMatch>           // examCredit
  /** applies: fills a named plan row. accepted_not_in_plan: credit awarded, plan lists other courses.
   *  elective_only / unknown as degreeCredit reports them. */
  fit: 'applies' | 'accepted_not_in_plan' | 'elective_only' | 'unknown' | 'none'
  rows: { term: number; label: string; item: string; credits: number | string | null }[]
  hours: Line<number>                   // published hours, or missing (UTK rows have none)
}

interface ExamOption {
  family: ExamFamily; examName: string; minimumText: string
  course: string; term: number; item: string
  evidence: Evidence
}

interface TermCoverage { term: number; label: string; items: number; coveredItems: number; covered: boolean }
interface Unknown { topic: 'credit' | 'plan' | 'cost' | 'aid' | 'dual_enrollment' | 'timeline'; text: string; ask?: string /* issue */ }
```

Input records use the stored shapes unchanged:
- `credit_policies[].equivalencies[]`
- `degree_requirements[]` with `rule_details.terms[].items[]` (all formats via `planItems`)
- `costs[].living_arrangements[]`
- `awards[]`
- `academic_programs[]`

No new record type is needed for slice 1.

## 3. Rules the engine applies

| Output | Rule | Source modules |
|---|---|---|
| Acceptance | The school's own table at the student's score (IB: and level). Minimums printed in words show "read the criteria" | `examCredit` |
| Fit | The awarded course code appears in a row of the major's verified plan, including alternatives printed in titles (#192) | `degreeCredit`, `planItems` |
| Options ("consider") | For every exam in the verified table: run the fit check at the table's lowest qualifying score. List only exams whose course fills a plan row. Ordered by plan term | `degreeCredit` |
| Hours | The published `credits_awarded`. A sum of published hours is an `estimate` with that method stated. Null hours are `missing` | `examCredit` |
| Timeline | Whole plan terms where every item is covered. Otherwise the value is null and the reason is listed | `degreeCredit.coveredTerms` |
| Savings | `termsSaving` over the verified cost for the chosen living arrangement. "Potential", net of grants the family entered. Never from hours alone (CR-17) | `costProjection` |
| Cost | `living_arrangements[]` from a verified cost record, as published, labeled with its year | new reader; data exists |
| Dual enrollment | Eligibility fields as published. No course equivalencies until a verified table exists | `credit_policies.dual_enrollment` |
| Merit | Single published minimums only. Tiers and ranges show "read the criteria" | `merit` |

`partially_verified` records are never used for verified lines. They become `missing` lines that say which item is
unverified. For example, UTC's AP table shows as: "UTC's AP table is on file but not yet verified (#191)".

## 4. Milestones

These are created as GitHub milestones.

| Milestone | Contents | Needs Supabase? |
|---|---|---|
| **P1: Engine (no database)** | #192 (done), #197, #194 | No |
| **P2: Pilot view, demo only** | #195 behind `VITE_PLANNING_PILOT`, off everywhere | No |
| **P3: Slice 1 data (UTC Management)** | #191: Research verifies and answers from files | No |
| **P4: Expansion data** | #193: UTK plans and hours, MTSU, dual enrollment, TN pathways and HS requirements | No |
| **P5: Account storage** | #196: CR-28 planning profile, CR-10 exam-plan wiring, CR-15 home state | **Yes: deferred** |
| **P6: Live pilot** | Import verified records to hosted; set the flag in a deployed environment | **Yes, plus a deploy: deferred** |

Exit criteria for showing the pilot outside the local demo are in `COLLEGE_PLANNING_PILOT.md` §4.
