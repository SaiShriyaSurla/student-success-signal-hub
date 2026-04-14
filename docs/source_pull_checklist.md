# Source Pull Checklist

## Purpose

This checklist maps the initial Version 1 metrics to their sources, target tables, and download or extraction actions.

## Version 1 Metrics

- `total_enrollment`
- `undergraduate_enrollment`
- `first_year_retention_rate`
- `graduation_rate`
- `degrees_awarded_total`
- `completion_rate`
- `median_earnings`
- `median_debt`

## Pull Checklist

### 1. IPEDS

- Source URL: https://nces.ed.gov/ipeds/datacenter/Data.aspx
- Metrics to pull:
  - `total_enrollment`
  - `first_year_retention_rate`
  - `graduation_rate`
  - `degrees_awarded_total`
- Target table:
  - `institution_benchmarks`
- Output destination:
  - `data/raw/ipeds/`
- Notes:
  - capture multiple years if available
  - save any metadata or field descriptions used during extraction

### 2. College Scorecard

- Source URL: https://collegescorecard.ed.gov/data/
- Metrics to pull:
  - `completion_rate`
  - `median_earnings`
  - `median_debt`
- Target table:
  - `outcomes_benchmarks`
- Output destination:
  - `data/raw/college_scorecard/`
- Notes:
  - confirm the institution identifier used for Indiana University Bloomington
  - keep a note of the original column names

### 3. Indiana University Common Data Set

- Source URL: https://usss.iu.edu/common-data-set/
- Metrics to pull:
  - `undergraduate_enrollment`
  - `degrees_conferred`
  - optional admissions or persistence context
- Target table:
  - `institution_profile`
  - `institution_benchmarks`
- Output destination:
  - `data/raw/iu_cds/`
- Notes:
  - store downloaded PDFs or exported reference files
  - record the exact section/page used for each metric

### 4. NACE First-Destination Standards

- Source URL: https://www.naceweb.org/job-market/graduate-outcomes/first-destination/development-of-the-first-destination-survey-standards-and-protocols/
- Context items to pull:
  - `knowledge_rate_definition`
  - any concise methodology notes relevant to dashboard interpretation
- Target table:
  - `reporting_context`
  - `outcomes_benchmarks`
- Output destination:
  - `data/raw/nace/`
- Notes:
  - capture only short, relevant reference notes
  - avoid copying long passages

## Folder Preparation

Create or confirm these source folders before downloading:

- `data/raw/ipeds/`
- `data/raw/college_scorecard/`
- `data/raw/iu_cds/`
- `data/raw/nace/`

## Done Criteria

The initial source pull is complete when:

- each Version 1 metric has a confirmed source
- the raw files are stored in the correct folder
- the original source URL is documented
- any unclear field mappings are noted for cleaning later
