"""Program & Degree Deep Dive: targeted, resumable retrieval of official catalog program lists,
program pages, degree maps and program-admission policy pages, plus candidate extraction.

This package is deliberately separate from the national first-pass pipeline (`pipeline/`). It
reuses that pipeline's fetcher, politeness, robots handling, document parsing and extractors by
import only; it never changes them. Runs live in `programs/runs/<STATE>/<run-id>/` and are produced
by `.github/workflows/program-research.yml` on `program-run/**` branches. See programs/README.md.
"""
