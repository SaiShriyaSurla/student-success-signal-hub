# Phase 2 Data Source Strategy

## Purpose

This document defines which existing public sources will be used in Student Success Signal Hub, what each source contributes, and how those sources map into the project's analytical tables.

The goal is to make the project transparent, realistic, and easy to explain in a portfolio or interview setting.

## Data Approach

The project will use an existing-datasets-only strategy:

- public institutional datasets for benchmark metrics and multi-year trend analysis
- public methodology sources for KPI definitions and reporting context
- institution-specific public documentation for framing and interpretation

This approach keeps the project fully grounded in real, citable data while avoiding the need to fabricate operational student records.

## Source Inventory

### 1. IPEDS Data Center

- Source type: Real public data
- URL: https://nces.ed.gov/ipeds/datacenter/Data.aspx
- Primary value:
  - institution-level enrollment
  - retention rates
  - graduation rates
  - completions
  - admissions and institutional characteristics
- Planned use:
  - benchmark context for institutional reporting
  - multi-year trends to support leadership-style dashboard views
- Project tables supported:
  - `institution_benchmarks`
- Likely fields to capture:
  - reporting_year
  - institution_name
  - enrollment_total
  - first_year_retention_rate
  - graduation_rate
  - degrees_awarded_total
  - admissions_rate

### 2. College Scorecard Data

- Source type: Real public data
- URL: https://collegescorecard.ed.gov/data/
- Primary value:
  - post-college outcomes context
  - earnings and debt indicators
  - completion-related measures
- Planned use:
  - outcome benchmarking
  - higher-level context connecting student success to post-graduation reporting
- Project tables supported:
  - `institution_benchmarks`
- Likely fields to capture:
  - reporting_year
  - median_earnings
  - median_debt
  - completion_rate
  - institution_id

### 3. Indiana University Common Data Set

- Source type: Real public data
- URL: https://usss.iu.edu/common-data-set/
- Primary value:
  - institution-specific context
  - enrollment and persistence information
  - academic profile and degree conferral context
- Planned use:
  - support institution-specific realism
  - anchor the project in a real institutional context connected to the target role
- Project tables supported:
  - `institution_profile`
  - `institution_benchmarks`
- Likely fields to capture:
  - reporting_year
  - undergraduate_enrollment
  - persistence_metrics
  - degrees_conferred
  - transfer_or_admissions_context

### 4. Indiana University Placement Exams

- Source type: Real public process documentation
- URL: https://college.indiana.edu/undergraduate/admissions/placement-exams/index.html
- Primary value:
  - placement workflow context
  - exam types and operational timing
  - stakeholder process understanding
- Planned use:
  - provide business-process context for how placement supports student success reporting
  - strengthen the project narrative even though placement will not be the main dataset
- Project tables supported:
  - `reporting_context`
- Likely fields informed by this source:
  - placement_process_notes
  - placement_exam_types
  - operational_context

### 5. NACE First-Destination Standards and Protocols

- Source type: Real public methodology
- URL: https://www.naceweb.org/job-market/graduate-outcomes/first-destination/development-of-the-first-destination-survey-standards-and-protocols/
- Primary value:
  - standard outcome definitions
  - reporting categories
  - knowledge rate methodology
  - collection and verification context
- Planned use:
  - define the outcome categories used in the project
  - structure career outcomes KPIs and validation logic
- Project tables supported:
  - `career_outcomes`
  - KPI logic in future analytics views
- Likely fields informed by this source:
  - outcome_status
  - knowledge_source
  - verified_flag
  - continuing_education_flag
  - employment_type

## Real Versus Synthetic Mapping

The following project data should come directly or indirectly from public sources:

- institution benchmark metrics
- graduate outcomes and earnings context
- outcome reporting methodology
- institution-specific reporting context

## Table-by-Table Source Strategy

### `institution_benchmarks`

- Primary source type: Real public data
- Sources:
  - IPEDS
  - College Scorecard
  - IU Common Data Set
- Notes:
  - this table will anchor institutional context and multi-year reporting

### `outcomes_benchmarks`

- Primary source type: Real public data with real methodology
- Sources informing design:
  - NACE standards
  - College Scorecard context
- Notes:
  - this table will summarize post-college outcomes context, definitions, and institution-level measures

### `institution_profile`

- Primary source type: Real public data
- Sources informing design:
  - IU Common Data Set
- Notes:
  - this table will capture institution-specific context such as undergraduate enrollment and degree conferral framing

### `reporting_context`

- Primary source type: Real public documentation
- Sources informing design:
  - NACE standards
  - IU Placement Exams page
- Notes:
  - this table can store KPI definitions, methodology notes, and process context used in the case study and dashboard documentation

## Recommended Initial Public Data Pull

To stay focused, the first version of the project should extract a small, high-value set of public benchmark fields rather than attempting to download and model every available source.

Recommended first pull:

- from IPEDS:
  - enrollment_total
  - first_year_retention_rate
  - graduation_rate
  - degrees_awarded_total
- from College Scorecard:
  - median_earnings
  - median_debt
  - completion_rate
- from IU Common Data Set:
  - undergraduate_enrollment
  - persistence or graduation context
  - degree conferral context

## Documentation Guidance

When this project is presented, it should clearly state:

- all analytical datasets come from existing public sources
- methodology and KPI logic are grounded in official reporting definitions
- institution-specific process context is used to strengthen the business analysis narrative

## Recommended Next Step

The next step is to finalize the metrics plan, then download and organize the first public data files for IPEDS, College Scorecard, and IU Common Data Set.
