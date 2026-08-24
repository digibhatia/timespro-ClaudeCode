# Business Requirements Document — Lead Scoring Logic

**Status:** Draft, pending implementation
**Owner:** Product (sample, for training purposes)
**Used in:** Day 1 hands-on exercise — Specification-Driven Development (BMAD)

## 1. Background

LeadScore Service currently accepts a `Lead` record but does not yet compute a
meaningful score. Sales and account teams need a fast, explainable score (0–100)
to triage inbound leads across our EdTech, Healthcare, and BFSI verticals.

## 2. Problem Statement

Without a working score, every lead is treated identically regardless of intent
signals, urgency, or fit — teams are manually re-reading raw lead data to decide
who to contact first. This is slow and inconsistent across reps.

## 3. Requirements

1. `score_lead(lead: Lead) -> ScoredLead` must return a score between 0 and 100.
2. The scoring logic must be **vertical-aware**: EdTech, Healthcare, and BFSI
   leads should weight different fields (see Domain Notes in `CLAUDE.md`).
3. The score must be **explainable** — `ScoredLead` should include a short list
   of the top factors that contributed to the score, not just the number.
4. Leads missing key fields should not crash the service — they should score
   lower and note the missing field as a contributing factor.
5. The scoring function must be pure (no side effects, no network calls) so it
   can be tested deterministically.

## 4. Out of Scope (for this exercise)

- Persisting scores to a database.
- Any UI or notification when a score changes.
- Real-time re-scoring on data updates.

## 5. Acceptance Criteria

- All tests in `tests/test_scoring.py` pass, including the ones currently
  marked `# TODO`.
- The `/leads/{lead_id}/score` endpoint returns a real score instead of a 501.
- Running the service against all three sample CSVs produces sensible,
  differentiated scores — not the same score for every lead.

## 6. Suggested Approach (non-binding)

This is intentionally left open for the Day 1 exercise. You will use Claude Code
to go from this BRD to an implementation plan (architecture) before writing any
code — that is the point of the Specification-Driven Development workflow.
