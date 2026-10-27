# Combined-bank reconciliation (Claude workstream)

- `baseline/` holds the user-supplied combined screening ZIP exactly as received (sha256 in `SHA256SUMS`). It is never modified.
- `tools/reconcile_combined.py` merges that baseline with this workstream's current append-only banks by question ID and normalized content hash, and writes `reconciled/` (combined bank, summary, report). Re-run it after every change.
- `reviews/` holds fresh, version-bound review results made after the baseline (blind solves without keys); each result names the content hash it reviewed.
- `overlays.json` holds proposed repairs or adjudications for records owned by other workstreams. Their source files are not edited.
- `progress.json` is the durable tracker for this reconciliation and the follow-up work.

Nothing here is imported, deployed, published, human-approved, rights-cleared, or student-calibrated.
