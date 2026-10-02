# Prep & Price — web app

The student and parent front end for CollegePrep. It uses React 19, TypeScript, Vite and Tailwind CSS v4, and talks directly to the CollegePrep Supabase project through its documented RPCs.

```sh
cd web
npm ci
npm run dev        # http://localhost:5173
npm test           # unit + component tests (vitest, jsdom)
npm run typecheck
npm run build
```

## Two data sources, one interface

`src/lib/data/source.ts` defines everything the UI reads or writes. It has two implementations:

- **`LiveSource`** (`src/lib/data/live`)
  - Supabase Auth, RLS-filtered table reads and the RPCs in `docs/HOUSEHOLD_PRACTICE.md` and `docs/BACKEND.md`: `create_household`, `start_practice_session`, `submit_practice_attempt`, `student_weekly_progress`, `compare_institutions` and the rest.
  - Enabled when `VITE_SUPABASE_URL` and `VITE_SUPABASE_PUBLISHABLE_KEY` are set; see `.env.example`.
  - Use only the publishable key.
- **`DemoSource`** (`src/lib/data/demo`)
  - Reproduces the same backend rules in the browser:
    - grading
    - skill estimates and the knowledge/pacing thresholds
    - the v1 recommender order
    - streaks in local time
    - only the student's own login can practise
    - answers stay hidden until submit
  - Runs on original fixture questions (`fixtures.ts`, 58 items).
  - Uses a dated snapshot of real verified comparison records (`comparison-snapshot.json`, captured 2026-10-02).
  - Loads lazily, so live users never download it.

The pure rules live in `src/lib/engine` and are unit-tested against the SQL definitions. When the backend changes a threshold, update `analytics.ts` and the tests.

Data that the backend doesn't model yet is kept in the browser:

- planning preferences
- benchmark summaries

The live source returns "unavailable" for cost projections. Each gap has a contract request in [`docs/frontend/CONTRACT_REQUESTS.md`](../docs/frontend/CONTRACT_REQUESTS.md).

## Screens

| Route | Screen |
|---|---|
| `/` | Landing: parent-led or student-led entry, sample family |
| `/onboarding/parent` | Household → student → goals → invite code |
| `/onboarding/student` | Name and grade → test and target → goals → benchmark |
| `/join` | Accept an invite code |
| `/student` | Today's plan, weekly goal, score vs target, weak skills, XP, benchmarks |
| `/student/practice` | Adaptive session: hint, teach-me, confidence-to-submit, feedback (teach / strategy / other answers / remember this) |
| `/student/benchmark` | Section-by-section staircase benchmark with skip-and-return, then results that separate knowledge, pacing, confidence and habits |
| `/student/progress`, `/parent/progress` | 8-week chart, skill mastery, habits, benchmark history, scores by source |
| `/parent` | KPIs, next best actions, sections, cost outlook |
| `/parent/household` | Students, invite codes, guardians |
| `/colleges` | Verified comparison by academic year: cost of attendance, admissions, scholarships, exam credit, appeals, sticker cost × years |

## Principles enforced in code

- **No invented data.**
  - Missing domains render as "No verified record yet".
  - Score estimates appear only when the backend writes them.
  - Demo financials carry an "Illustrative example" banner.
- **Practice estimates are never shown as official scores.**
- **Accessibility.**
  - Shell screens have a skip link. Progress bars and rings are labelled, and answers can be chosen by keyboard (1–4 or A–D).
  - Pages respect `prefers-reduced-motion` and support a dark theme through tokens.
  - Layouts work at 375px wide with no horizontal scroll.
