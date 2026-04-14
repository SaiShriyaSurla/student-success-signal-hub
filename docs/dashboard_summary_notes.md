# Dashboard Summary Notes

## Purpose

The dashboard summary script loads the processed benchmark tables and creates one flattened output that is easier to use for an initial dashboard or visual prototype.

## Script

- `src/build_dashboard_summary.py`

## Outputs

- `reports/dashboard_summary_v1.csv`
- `reports/dashboard_summary_v1.md`

## Why This Step Matters

- it validates that the processed tables can be loaded together
- it creates one simple dataset for the first dashboard mockup
- it gives a quick stakeholder-friendly summary before any frontend work starts

## Recommended Next Step

Use the generated summary file to create either:

- a simple notebook chart
- a Streamlit prototype
- or a Power BI / Tableau mock dashboard
