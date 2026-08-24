# Architecture Note — LeadScore Service (v0.1)

A short, deliberately partial architecture note. Part of Day 1's Architecture &
Context Management exercise is to extend this document using Claude Code before
touching the scoring implementation.

## Current Layers

- **API layer** (`app/api/routes.py`) — thin FastAPI routes, no business logic.
- **Model layer** (`app/models/lead.py`) — Pydantic models for `Lead` and
  `ScoredLead`.
- **Service layer** (`app/services/scoring.py`) — where scoring logic belongs.
  Currently a stub.

## Data Flow (Current)

```
CSV sample data --> Lead model --> [scoring.py: NOT YET IMPLEMENTED] --> API response
```

## Open Questions (for the Day 1 exercise)

- Should vertical-specific scoring weights live in code, in a config file, or in
  a small rules table? Consider maintainability as the number of verticals grows.
- How should the "explainability" factors (Requirement 3 in the BRD) be
  represented in the `ScoredLead` model?
- What's the right way to keep this pure and side-effect-free while still being
  easy to extend later with real data sources?

Use Claude Code to reason through these questions and propose an updated
architecture before writing the implementation — this is the Day 1 workflow.
