# LeadScore Service

A small Python service that scores and enriches inbound leads — modeled loosely on a
LeadSquared-style CRM workflow, with sample data across three verticals: **EdTech**,
**Healthcare**, and **BFSI**.

This repository is the shared working base for the **Advanced Batch — Claude Code
for Senior Engineers** program (LeadSquared × TimesPro). You'll use it across
Day 1 and Day 2, and extend it further through Day 4. It may also become the base
for your capstone.

## What's Here

```
leadscore_service/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── models/
│   │   └── lead.py          # Lead data model (Pydantic)
│   ├── services/
│   │   └── scoring.py       # Scoring logic — INTENTIONALLY INCOMPLETE
│   └── api/
│       └── routes.py        # API routes — one endpoint is a stub
├── data/
│   └── samples/
│       ├── leads_edtech.csv
│       ├── leads_healthcare.csv
│       └── leads_bfsi.csv
├── docs/
│   ├── BRD.md                # Business Requirements Document — Day 1 starting point
│   └── ARCHITECTURE.md       # Short architecture note — Day 1 context exercise
├── tests/
│   └── test_scoring.py       # Starter tests — some pass, some are marked TODO
├── .claude/
│   └── CLAUDE.md             # Project context file for Claude Code
├── requirements.txt
└── README.md                 # You are here
```

## Why It's Incomplete on Purpose

`app/services/scoring.py` and one route in `app/api/routes.py` are deliberately
left unfinished. Day 1's spec-to-code exercise walks you through using
Claude Code — guided by `docs/BRD.md` and the BMAD workflow — to complete them
properly, rather than just asking for "a scoring function."

## Getting Started

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open VS Code in this folder with the Claude Code extension active, and make
sure your Claude API key is configured in your environment before Day 1 begins.

## Domain Note

The three sample data files under `data/samples/` represent the same underlying
lead-scoring problem, applied to three different LeadSquared customer verticals.
Exercises across the program will ask you to work with one, two, or all three —
pay attention to which fields matter differently in each vertical (for example,
`course_interest` in EdTech vs. `policy_type` in BFSI).
