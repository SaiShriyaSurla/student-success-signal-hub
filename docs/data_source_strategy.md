# Phase 2 Data Source Strategy

## Purpose

This document defines which public sources will be used in Student Success Signal Hub, what each source contributes, and which project tables will rely on real public data versus synthetic operational data.

The goal is to make the project transparent, realistic, and easy to explain in a portfolio or interview setting.

## Data Approach

The project will use a hybrid data strategy:

- real public data for institutional benchmarks, definitions, and reporting context
- synthetic student-level data for operational workflows that would normally be private or protected

This approach reflects how higher education analytics work often combines official aggregate reporting with internal operational systems that are not publicly accessible.

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
  - guide assumptions for cohort sizes and student distributions in synthetic data
- Project tables supported:
  - `institution_benchmarks`
  - synthetic modeling assumptions for `students`
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
  - model the synthetic placement process realistically
  - ensure fields and statuses reflect believable operational workflows
- Project tables supported:
  - `placement_exams`
  - `data_quality_issues`
- Likely fields informed by this source:
  - placement_exam_type
  - placement_required_flag
  - placement_status
  - exam_window
  - follow_up_needed_flag

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

### Real Public Data

The following project data should come directly or indirectly from public sources:

- institution benchmark metrics
- outcome reporting methodology
- placement process context
- assumptions for realistic cohort sizing and distributions

### Synthetic Operational Data

The following project data should be generated:

- student-level records
- placement attempts and scores
- advising interactions
- experiential learning participation
- first-destination outreach records
- verification workflow details
- data quality exception records

## Table-by-Table Source Strategy

### `institution_benchmarks`

- Primary source type: Real public data
- Sources:
  - IPEDS
  - College Scorecard
  - IU Common Data Set
- Notes:
  - this table will anchor institutional context and multi-year reporting

### `students`

- Primary source type: Synthetic
- Sources informing design:
  - IU Common Data Set
  - IPEDS
- Notes:
  - student demographics and cohort distributions should be modeled using realistic institutional proportions where possible

### `placement_exams`

- Primary source type: Synthetic
- Sources informing design:
  - IU Placement Exams page
- Notes:
  - workflows should include incomplete records, multiple attempts, and follow-up flags

### `advising_engagement`

- Primary source type: Synthetic
- Sources informing design:
  - project business questions and realistic student success workflows
- Notes:
  - should include both completed and missed or canceled interactions

### `experiential_learning`

- Primary source type: Synthetic
- Sources informing design:
  - career readiness and student engagement assumptions
- Notes:
  - can include internships, research, service learning, and campus involvement markers

### `career_outcomes`

- Primary source type: Synthetic with real methodology
- Sources informing design:
  - NACE standards
  - College Scorecard context
- Notes:
  - should include missing and unverified cases to support knowledge rate reporting

### `data_quality_issues`

- Primary source type: Synthetic
- Sources informing design:
  - realistic reporting and validation failure cases
- Notes:
  - should track issue type, severity, status, and resolution context

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

- aggregate benchmark data comes from official public sources
- student-level operational data is synthetic
- synthetic datasets were intentionally modeled to reflect real university workflows, reporting categories, and data quality issues

## Recommended Next Step

The next step is to finalize the first-pass schema for the core tables and then create the repository folders where raw, synthetic, and processed data will live.
