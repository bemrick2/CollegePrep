# Acceptance scenarios

These tests run the real UI against verified records captured from the live backend, so a product question can be checked end to end once research data supports it.

1. Capture the records (publishable key only):
   ```
   VITE_SUPABASE_URL=… VITE_SUPABASE_PUBLISHABLE_KEY=… node scripts/capture-comparison.mjs --name tn-or --year 2026-27 --states TN,OR
   ```
2. Run `npm test -- acceptance`. A scenario is skipped until its fixture exists.

The tests assert product rules (residency-correct prices, four-year schools first, interest fit stated only from verified programs, no invented totals), not specific numbers, and print a summary table for review.

## Scenario: Tennessee 8th grader, engineering, Tennessee and Oregon, four-year, minimize total cost

Fixture: `fixtures/tn-or.json`. What becomes meaningful as research deepens:

- **CR-14** (program `cip_code`, `admission_type`, coverage flag): "has engineering" moves from name matching to classification, and "requires freshman admission" appears.
- **CR-11** (numeric merit criteria): tiered awards can be compared with the target.
- **CR-15** (household home state): the home state syncs across devices.
