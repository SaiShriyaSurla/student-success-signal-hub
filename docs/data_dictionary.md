# Data Dictionary

## Purpose

This document defines the fields used in the Version 1 analytical tables for Student Success Signal Hub.

## `institution_benchmarks`

### `benchmark_record_id`
- Description: Unique identifier for each benchmark row
- Type: string
- Example: `bench_ipeds_2023_retention`

### `source_name`
- Description: Public source from which the metric was collected
- Type: string
- Allowed values: `IPEDS`, `College Scorecard`, `IU CDS`

### `institution_name`
- Description: Institution name associated with the metric
- Type: string
- Example: `Indiana University Bloomington`

### `institution_id`
- Description: Cross-source institution identifier when available
- Type: string
- Example: `151351`

### `reporting_year`
- Description: Year associated with the metric
- Type: integer
- Example: `2023`

### `metric_name`
- Description: Name of the reported metric
- Type: string
- Allowed values:
  - `total_enrollment`
  - `first_year_retention_rate`
  - `graduation_rate`
  - `degrees_awarded_total`
  - `admissions_rate`

### `metric_value`
- Description: Value of the metric
- Type: number or string
- Example: `0.87`

### `metric_group`
- Description: High-level category for the metric
- Type: string
- Allowed values:
  - `enrollment`
  - `retention`
  - `graduation`
  - `completions`
  - `admissions`

### `source_url`
- Description: URL for the source or download location
- Type: string

### `notes`
- Description: Optional note for interpretation or assumptions
- Type: string

## `outcomes_benchmarks`

### `outcome_benchmark_id`
- Description: Unique identifier for each outcomes benchmark row
- Type: string
- Example: `outcome_scorecard_2023_earnings`

### `source_name`
- Description: Source for the outcome metric or methodology
- Type: string
- Allowed values: `College Scorecard`, `NACE`

### `institution_name`
- Description: Institution name when the metric applies to a specific institution
- Type: string

### `reporting_year`
- Description: Year associated with the metric
- Type: integer

### `metric_name`
- Description: Name of the post-college outcome metric
- Type: string
- Allowed values:
  - `completion_rate`
  - `median_earnings`
  - `median_debt`
  - `knowledge_rate_definition`

### `metric_value`
- Description: Value or text definition for the metric
- Type: number or string

### `metric_group`
- Description: Category of the metric
- Type: string
- Allowed values:
  - `completion`
  - `earnings`
  - `debt`
  - `methodology`

### `population_scope`
- Description: Scope of the metric or definition
- Type: string
- Allowed values:
  - `institution`
  - `cohort`
  - `national_definition`

### `source_url`
- Description: Source or reference URL
- Type: string

### `notes`
- Description: Optional interpretation note
- Type: string

## `institution_profile`

### `profile_record_id`
- Description: Unique identifier for each profile row
- Type: string
- Example: `profile_iucds_2023_undergrad`

### `source_name`
- Description: Source for the institution profile metric
- Type: string
- Allowed values: `IU CDS`

### `institution_name`
- Description: Institution name
- Type: string

### `reporting_year`
- Description: Year associated with the profile metric
- Type: integer

### `profile_metric_name`
- Description: Name of the institution profile metric
- Type: string
- Allowed values:
  - `undergraduate_enrollment`
  - `degrees_conferred`
  - `persistence_context`
  - `admissions_context`

### `profile_metric_value`
- Description: Value of the institution profile metric
- Type: number or string

### `metric_group`
- Description: Category of the profile metric
- Type: string
- Allowed values:
  - `enrollment`
  - `completions`
  - `persistence`
  - `admissions`

### `source_url`
- Description: Source or reference URL
- Type: string

### `notes`
- Description: Optional note for interpretation
- Type: string

## `reporting_context`

### `context_record_id`
- Description: Unique identifier for each context row
- Type: string
- Example: `context_nace_knowledge_rate`

### `context_type`
- Description: Type of explanatory context
- Type: string
- Allowed values:
  - `kpi_definition`
  - `methodology_note`
  - `process_note`
  - `dashboard_annotation`

### `context_name`
- Description: Short label for the context item
- Type: string
- Example: `knowledge_rate_definition`

### `context_value`
- Description: Definition or explanatory text
- Type: string

### `source_name`
- Description: Source of the context item
- Type: string
- Allowed values:
  - `NACE`
  - `IU Placement Exams`
  - `Project`

### `source_url`
- Description: Reference URL
- Type: string

### `applies_to_metric_group`
- Description: Metric group supported by the context item
- Type: string
- Allowed values:
  - `retention`
  - `graduation`
  - `outcomes`
  - `placement_context`
  - `admissions`

### `notes`
- Description: Optional implementation note
- Type: string
