"""Lead scoring logic.

STATUS: INTENTIONALLY INCOMPLETE.

This is the starting point for the Day 1 hands-on exercise. See
docs/BRD.md for the full requirements and docs/ARCHITECTURE.md for the
open architectural questions to resolve first.

Do not just ask Claude Code to "finish this function." The point of the
exercise is to go BRD -> architecture -> implementation plan -> code,
using the Specification-Driven Development (BMAD) workflow introduced
in Module 3.
"""

from app.models.lead import Lead, ScoredLead


def score_lead(lead: Lead) -> ScoredLead:
    """Score a single lead.

    TODO (Day 1 exercise): this placeholder does not meet the BRD
    requirements. Specifically, it is not vertical-aware, it is not
    explainable, and it does not handle missing fields gracefully.
    Replace this implementation following the plan you build in the
    Day 1 exercise.
    """
    # Placeholder: every lead gets the same score, with no reasoning.
    # This satisfies nothing in the BRD except "returns a number."
    return ScoredLead(lead_id=lead.lead_id, score=50, top_factors=["not yet implemented"])
