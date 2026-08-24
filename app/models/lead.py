"""Data models for LeadScore Service."""

from typing import Optional
from pydantic import BaseModel, Field


class Lead(BaseModel):
    """A single inbound lead record, before scoring.

    Fields are intentionally optional where real-world data is often missing —
    the scoring logic is required to handle missing fields gracefully rather
    than assuming they are always present.
    """

    lead_id: str
    vertical: str = Field(description="One of: edtech, healthcare, bfsi")
    name: Optional[str] = None
    email: Optional[str] = None
    enquiry_recency_days: Optional[int] = Field(
        default=None, description="Days since the lead's last enquiry activity"
    )

    # EdTech-specific fields
    course_interest: Optional[str] = None

    # Healthcare-specific fields
    appointment_type: Optional[str] = None
    urgency_flag: Optional[bool] = None

    # BFSI-specific fields
    policy_type: Optional[str] = None
    income_bracket: Optional[str] = None


class ScoredLead(BaseModel):
    """A lead with a computed score and an explanation of what drove it."""

    lead_id: str
    score: int = Field(ge=0, le=100)
    top_factors: list[str] = Field(
        default_factory=list,
        description="Short, human-readable list of the top factors behind the score",
    )
