# First-Pass Schema Overview

## Purpose

This document defines the initial version of the core project tables for Student Success Signal Hub. The schema is intentionally compact so the project stays focused while still supporting realistic analytics, institutional benchmarking, and business-facing reporting using existing public datasets only.

## Core Tables

The first version of the project will include four analytical tables:

- `institution_benchmarks`
- `outcomes_benchmarks`
- `institution_profile`
- `reporting_context`

## 1. `institution_benchmarks`

Purpose:
Store multi-year public benchmark metrics for institutional performance and student success trends.

Initial fields:

- `benchmark_record_id`: unique benchmark row identifier
- `source_name`: IPEDS, College Scorecard, IU CDS
- `institution_name`: institution label
- `institution_id`: optional cross-source institution identifier
- `reporting_year`: reporting year
- `metric_name`: name of the benchmark metric
- `metric_value`: numeric or text metric value
- `metric_group`: enrollment, retention, graduation, completions, admissions
- `source_url`: documentation or download location
- `notes`: optional interpretation notes

## 2. `outcomes_benchmarks`

Purpose:
Store public post-college outcomes metrics and the definitions needed to interpret them.

Initial fields:

- `outcome_benchmark_id`: unique row identifier
- `source_name`: College Scorecard, NACE
- `institution_name`: institution label when applicable
- `reporting_year`: reporting year
- `metric_name`: median_earnings, median_debt, completion_rate, knowledge_rate_definition, other
- `metric_value`: numeric or text metric value
- `metric_group`: earnings, debt, completion, methodology
- `population_scope`: institution, cohort, national_definition
- `source_url`: documentation or download location
- `notes`: optional interpretation notes

## 3. `institution_profile`

Purpose:
Store institution-specific context used to frame the dashboard and case study.

Initial fields:

- `profile_record_id`: unique row identifier
- `source_name`: IU CDS
- `institution_name`: institution label
- `reporting_year`: reporting year
- `profile_metric_name`: undergraduate_enrollment, degrees_conferred, persistence_context, admissions_context
- `profile_metric_value`: numeric or text metric value
- `metric_group`: enrollment, completions, persistence, admissions
- `source_url`: documentation or download location
- `notes`: optional interpretation notes

## 4. `reporting_context`

Purpose:
Store business-analysis context that supports KPI definitions, methodology notes, and institutional process framing.

Initial fields:

- `context_record_id`: unique row identifier
- `context_type`: kpi_definition, methodology_note, process_note, dashboard_annotation
- `context_name`: short label for the item
- `context_value`: definition, explanation, or note text
- `source_name`: NACE, IU Placement Exams, project-defined
- `source_url`: documentation or reference link
- `applies_to_metric_group`: retention, graduation, outcomes, placement_context, admissions
- `notes`: optional implementation note

## Relationship Summary

- `institution_benchmarks` is the main fact-style table for institutional trend analysis
- `outcomes_benchmarks` complements it with public post-college outcomes context
- `institution_profile` provides institution-specific framing for the case study and dashboard
- `reporting_context` supports business-facing explanations of KPI logic and methodology

## Design Principles

- keep the schema small enough for a polished first version
- use only existing public datasets and official methodology sources
- preserve clear traceability back to the source
- use fields that are easy to explain in an interview

## Recommended Next Step

The next step is to create the detailed data dictionary and pull the first public benchmark files into `data/raw`.
