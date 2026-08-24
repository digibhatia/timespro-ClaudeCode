"""Tests for app.services.scoring.

Some of these pass against the current placeholder implementation.
Others are marked TODO and will only pass once scoring is implemented
properly, per docs/BRD.md. This is expected on Day 1 — do not "fix" the
tests to make them pass without implementing the real logic.
"""

import pytest

from app.models.lead import Lead
from app.services.scoring import score_lead


def test_score_is_within_bounds():
    """This should already pass — the placeholder returns a valid range."""
    lead = Lead(lead_id="L1", vertical="edtech", course_interest="Data Science")
    result = score_lead(lead)
    assert 0 <= result.score <= 100


def test_score_lead_returns_correct_id():
    """This should already pass."""
    lead = Lead(lead_id="L42", vertical="bfsi")
    result = score_lead(lead)
    assert result.lead_id == "L42"


# --- The following are TODO: implement scoring properly to pass these ---


@pytest.mark.skip(reason="TODO: implement vertical-aware scoring (BRD requirement 2)")
def test_edtech_lead_with_course_match_scores_higher():
    strong_match = Lead(
        lead_id="L1", vertical="edtech",
        course_interest="Data Science", enquiry_recency_days=1,
    )
    weak_match = Lead(
        lead_id="L2", vertical="edtech",
        course_interest=None, enquiry_recency_days=60,
    )
    assert score_lead(strong_match).score > score_lead(weak_match).score


@pytest.mark.skip(reason="TODO: implement vertical-aware scoring (BRD requirement 2)")
def test_healthcare_urgent_lead_scores_higher():
    urgent = Lead(lead_id="H1", vertical="healthcare", urgency_flag=True)
    routine = Lead(lead_id="H2", vertical="healthcare", urgency_flag=False)
    assert score_lead(urgent).score > score_lead(routine).score


@pytest.mark.skip(reason="TODO: implement explainability (BRD requirement 3)")
def test_score_includes_meaningful_top_factors():
    lead = Lead(lead_id="B1", vertical="bfsi", policy_type="term_life", income_bracket="high")
    result = score_lead(lead)
    assert result.top_factors != ["not yet implemented"]
    assert len(result.top_factors) > 0


@pytest.mark.skip(reason="TODO: handle missing fields gracefully (BRD requirement 4)")
def test_missing_fields_do_not_crash_and_score_lower():
    incomplete = Lead(lead_id="E1", vertical="edtech")  # no course_interest, no recency
    complete = Lead(
        lead_id="E2", vertical="edtech",
        course_interest="MBA", enquiry_recency_days=2,
    )
    incomplete_result = score_lead(incomplete)
    complete_result = score_lead(complete)
    assert incomplete_result.score <= complete_result.score
    assert any("missing" in factor.lower() for factor in incomplete_result.top_factors)
