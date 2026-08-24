"""API routes for LeadScore Service."""

import csv
from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.models.lead import Lead
from app.services.scoring import score_lead

router = APIRouter()

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "samples"

VERTICAL_FILES = {
    "edtech": "leads_edtech.csv",
    "healthcare": "leads_healthcare.csv",
    "bfsi": "leads_bfsi.csv",
}


def _load_lead(lead_id: str) -> Lead:
    """Look up a single lead by ID across all sample CSVs (helper, complete)."""
    for vertical, filename in VERTICAL_FILES.items():
        path = DATA_DIR / filename
        if not path.exists():
            continue
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("lead_id") == lead_id:
                    row["vertical"] = vertical
                    if "urgency_flag" in row and row["urgency_flag"] != "":
                        row["urgency_flag"] = row["urgency_flag"].lower() == "true"
                    if "enquiry_recency_days" in row and row["enquiry_recency_days"] == "":
                        row["enquiry_recency_days"] = None
                    return Lead(**row)
    raise HTTPException(status_code=404, detail=f"Lead {lead_id} not found")


@router.get("/leads/{lead_id}")
def get_lead(lead_id: str):
    """Fetch a single lead record. Complete — not part of the exercise."""
    return _load_lead(lead_id)


@router.get("/leads/{lead_id}/score")
def get_lead_score(lead_id: str):
    """Score a single lead.

    STATUS: stub. Returns 501 until app/services/scoring.py is implemented
    properly as part of the Day 1 exercise.
    """
    lead = _load_lead(lead_id)
    scored = score_lead(lead)
    if scored.top_factors == ["not yet implemented"]:
        raise HTTPException(
            status_code=501,
            detail="Scoring logic not yet implemented — see docs/BRD.md",
        )
    return scored
