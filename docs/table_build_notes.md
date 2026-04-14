# Table Build Notes

## Purpose

This document explains how the first processed project tables were built from the extracted IU Bloomington metrics.

## Tables Created

- `data/processed/institution_benchmarks_v1.csv`
- `data/processed/outcomes_benchmarks_v1.csv`
- `data/processed/institution_profile_v1.csv`
- `data/processed/reporting_context_v1.csv`

## Mapping Logic

- Enrollment, retention, admissions, and completions benchmark metrics were placed in `institution_benchmarks_v1.csv`
- Graduation, earnings, debt, and related outcome measures were placed in `outcomes_benchmarks_v1.csv`
- IU-specific manually captured CDS values were placed in `institution_profile_v1.csv`
- Methodology and interpretation notes were placed in `reporting_context_v1.csv`

## Important Note

Some metrics intentionally appear in both benchmark and profile contexts because they serve different purposes:

- benchmark tables support cross-source analytics
- profile tables support institution-specific storytelling

## Recommended Next Step

The next step is to preview these tables, validate the structure, and then build a simple analysis notebook or script to load them into a dashboard-friendly format.
