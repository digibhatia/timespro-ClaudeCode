# Project Context — LeadScore Service

## What This Project Is
A Python (FastAPI) service that scores and enriches inbound leads across three
customer verticals: EdTech, Healthcare, and BFSI. Built as the shared working
repository for the Advanced Batch training program (LeadSquared × TimesPro).

## Tech Stack
- Python 3.11+
- FastAPI for the API layer
- Pydantic for data models
- Pytest for testing
- No database yet — sample data is read from CSV files under `data/samples/`

## Conventions
- Follow PEP 8. Use type hints on all function signatures.
- Business logic lives in `app/services/`, never directly in `app/api/routes.py`.
- Every new function needs at least one corresponding test in `tests/`.
- Docstrings use Google style.

## Current State
- `app/models/lead.py` — complete. Defines the `Lead` and `ScoredLead` models.
- `app/services/scoring.py` — INCOMPLETE. The `score_lead()` function has a stub
  implementation that only returns a placeholder score. This is intentional —
  it's the subject of the Day 1 hands-on exercise.
- `app/api/routes.py` — mostly complete. The `/leads/{lead_id}/score` endpoint is
  a stub returning a 501, pending the scoring logic above.
- `tests/test_scoring.py` — a few tests pass against the placeholder; several are
  marked with `# TODO` and will fail until scoring is implemented properly.

## Domain Notes
- EdTech leads: prioritize `course_interest` match and `enquiry_recency`.
- Healthcare leads: prioritize `appointment_type` and `urgency_flag`; treat any
  field that looks like patient-identifying information as sensitive — do not
  log it or print it during debugging.
- BFSI leads: prioritize `policy_type` and `income_bracket`; treat `income_bracket`
  and any account-number-like field as sensitive.

## Human-in-the-Loop Reminder
This is a training repository. Nothing here should be treated as production-ready
without review. When Claude Code proposes a change, read the diff before
accepting it — especially anything touching the scoring weights or the handling
of the fields marked sensitive above.
