# Initial Metrics Plan

## Purpose

This document defines the first set of metrics Student Success Signal Hub should include, where each metric comes from, and why it matters to the portfolio story.

The guiding principle is to keep the first version compact, credible, and fully supported by existing public data.

## Recommended Dashboard Sections

- Enrollment and student profile
- Retention and graduation trends
- Completions and degree output
- Post-college outcomes and earnings context
- Reporting notes and KPI definitions

## Priority Metrics

### 1. Total Enrollment

- Source: IPEDS or IU CDS
- Why it matters:
  - establishes institutional scale
  - gives context for all other student success metrics
- Planned table:
  - `institution_benchmarks`

### 2. Undergraduate Enrollment

- Source: IU Common Data Set
- Why it matters:
  - ties the project more directly to the undergraduate focus in the target role
- Planned table:
  - `institution_profile`

### 3. First-Year Retention Rate

- Source: IPEDS
- Why it matters:
  - one of the clearest public student success indicators
  - useful for leadership reporting and trend analysis
- Planned table:
  - `institution_benchmarks`

### 4. Graduation Rate

- Source: IPEDS
- Why it matters:
  - core institutional performance metric
  - aligns naturally with assessment and student success reporting
- Planned table:
  - `institution_benchmarks`

### 5. Degrees Awarded Total

- Source: IPEDS or IU CDS
- Why it matters:
  - provides outcome volume and completion context
- Planned table:
  - `institution_benchmarks`
  - `institution_profile`

### 6. Completion Rate

- Source: College Scorecard
- Why it matters:
  - connects institutional performance with public accountability data
- Planned table:
  - `outcomes_benchmarks`

### 7. Median Earnings After Attendance

- Source: College Scorecard
- Why it matters:
  - connects education outcomes to workforce results
  - makes the dashboard more relevant to career outcomes storytelling
- Planned table:
  - `outcomes_benchmarks`

### 8. Median Debt

- Source: College Scorecard
- Why it matters:
  - balances the earnings story with student cost and repayment context
- Planned table:
  - `outcomes_benchmarks`

### 9. Admissions Rate

- Source: IPEDS or IU CDS
- Why it matters:
  - provides useful institutional profile context
  - helps frame cohort scale and selectivity
- Planned table:
  - `institution_benchmarks`
  - `institution_profile`

### 10. Knowledge Rate Definition

- Source: NACE standards
- Why it matters:
  - adds business-analysis value even if the project does not include first-destination microdata
  - shows understanding of graduate outcomes methodology
- Planned table:
  - `reporting_context`

## Recommended Version 1 Metric Set

To keep the first build manageable, the project should start with these eight metrics:

- total_enrollment
- undergraduate_enrollment
- first_year_retention_rate
- graduation_rate
- degrees_awarded_total
- completion_rate
- median_earnings
- median_debt

## Nice-to-Have Metrics for Version 2

- admissions_rate
- transfer_in_count
- completions_by_award_level
- repayment_rate
- earnings_by_program if an appropriate public source is easy to use
- additional NACE methodology notes for the case study

## Recommended Next Step

The next step is to create a data dictionary and a source pull checklist so each metric is mapped to a file, a field name, and a target table.
