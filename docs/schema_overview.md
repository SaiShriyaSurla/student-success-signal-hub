# First-Pass Schema Overview

## Purpose

This document defines the initial version of the core project tables for Student Success Signal Hub. The schema is intentionally compact so the project stays focused while still supporting realistic analytics and operational reporting.

## Core Tables

The first version of the project will include seven tables:

- `students`
- `placement_exams`
- `advising_engagement`
- `experiential_learning`
- `career_outcomes`
- `institution_benchmarks`
- `data_quality_issues`

## 1. `students`

Purpose:
Create a core student dimension used to connect placement, engagement, and outcomes records.

Initial fields:

- `student_id`: unique synthetic student identifier
- `cohort_year`: entering cohort year
- `graduation_term`: expected or actual graduation term
- `major`: primary academic program
- `class_level`: first-year, sophomore, junior, senior, alumni
- `first_gen_flag`: indicates first-generation status
- `residency_status`: in-state, out-of-state, international
- `urm_flag`: indicates underrepresented minority grouping for analysis
- `pell_eligible_flag`: optional socioeconomic proxy
- `created_at`: synthetic record creation timestamp

## 2. `placement_exams`

Purpose:
Track placement activity, exam attempts, outcomes, and follow-up needs.

Initial fields:

- `placement_record_id`: unique placement event identifier
- `student_id`: foreign key to `students`
- `placement_exam_type`: math, language, writing, other
- `placement_required_flag`: indicates whether exam is required
- `attempt_count`: total attempts for the record
- `score`: exam score
- `placement_level`: resulting placement category
- `placement_status`: not_started, scheduled, completed, waived, incomplete
- `exam_date`: date of most recent exam event
- `accommodation_flag`: indicates accommodation support may be involved
- `follow_up_needed_flag`: identifies records requiring staff follow-up
- `source_system`: placeholder source label for operational realism

## 3. `advising_engagement`

Purpose:
Track advising and support interactions connected to student progression.

Initial fields:

- `advising_event_id`: unique engagement identifier
- `student_id`: foreign key to `students`
- `engagement_date`: date of interaction
- `engagement_type`: appointment, orientation, workshop, outreach, referral
- `engagement_status`: completed, canceled, no_show, pending
- `staff_unit`: advising, career services, placement administration, other
- `topic_category`: registration, placement, academic planning, career planning, support services
- `follow_up_required_flag`: indicates whether additional action is needed
- `follow_up_completed_flag`: indicates whether follow-up occurred

## 4. `experiential_learning`

Purpose:
Track participation in experiences that may connect to student engagement and outcomes.

Initial fields:

- `experience_id`: unique experiential learning identifier
- `student_id`: foreign key to `students`
- `experience_type`: internship, research, service_learning, study_abroad, campus_employment
- `start_date`: experience start date
- `end_date`: experience end date
- `experience_status`: planned, active, completed, withdrawn
- `paid_flag`: indicates whether the experience was paid when relevant
- `credit_bearing_flag`: indicates academic credit linkage
- `verified_flag`: indicates whether participation was verified

## 5. `career_outcomes`

Purpose:
Track first-destination and graduate outcomes data using NACE-aligned logic.

Initial fields:

- `outcome_record_id`: unique outcome identifier
- `student_id`: foreign key to `students`
- `graduation_term`: graduation term associated with the outcome
- `outcome_status`: employed_full_time, employed_part_time, continuing_education, seeking, volunteering, military, not_seeking, unknown
- `employment_sector`: optional high-level employer category
- `salary_band`: grouped salary range when known
- `knowledge_source`: survey, institutional_data, linkedin, faculty_report, employer_confirmation, unknown
- `verified_flag`: indicates whether the outcome has been confirmed
- `outcome_collection_date`: date outcome was captured
- `knowledge_rate_included_flag`: indicates inclusion in knowledge rate calculations

## 6. `institution_benchmarks`

Purpose:
Store aggregate public metrics used to contextualize the synthetic operational data.

Initial fields:

- `benchmark_record_id`: unique benchmark row identifier
- `source_name`: IPEDS, College Scorecard, IU CDS
- `institution_name`: institution label
- `reporting_year`: reporting year
- `metric_name`: name of the benchmark metric
- `metric_value`: numeric or text metric value
- `metric_group`: enrollment, retention, graduation, outcomes, admissions
- `source_url`: documentation or download location
- `notes`: optional interpretation notes

## 7. `data_quality_issues`

Purpose:
Track validation failures, incomplete records, and issues that need manual review.

Initial fields:

- `issue_id`: unique issue identifier
- `table_name`: affected table
- `record_id`: identifier of the affected record
- `issue_type`: missing_value, duplicate_record, invalid_category, invalid_date, conflicting_data, stale_record
- `issue_severity`: low, medium, high
- `issue_status`: open, under_review, resolved
- `detected_date`: date issue was detected
- `resolution_date`: date issue was resolved, if applicable
- `issue_description`: short explanation of the problem

## Relationship Summary

- `students` is the central table
- `placement_exams`, `advising_engagement`, `experiential_learning`, and `career_outcomes` all join to `students` by `student_id`
- `data_quality_issues` can reference records from any operational table
- `institution_benchmarks` remains mostly separate and supports aggregate context rather than student-level joins

## Design Principles

- keep the schema small enough for a polished first version
- include enough operational detail to support realistic reporting
- preserve room for missing data and edge cases
- use fields that are easy to explain in an interview

## Recommended Next Step

The next step is to turn this overview into a more detailed data dictionary and create the repository folders that will hold raw, synthetic, and processed data.
