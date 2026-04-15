# Student Success Signal Hub

Student Success Signal Hub is a higher education analytics portfolio project built to reflect the kind of work an Academic Placement and Analytics Specialist or Business Analyst might do in a university setting.

The project uses public datasets and official methodology sources to build a leadership-ready dashboard focused on institutional scale, retention, graduation, admissions, and post-college outcomes. It is designed to show business analysis thinking, data sourcing discipline, documentation quality, and dashboard storytelling in a single project.

## Project Goal

The goal of this project is to answer a practical higher education reporting question:

How can a university combine public benchmark data and institutional profile data into a single reporting view that supports student success strategy and graduate outcomes storytelling?

## What This Project Demonstrates

- sourcing and validating public higher education data
- translating business questions into KPIs
- documenting data definitions and assumptions
- structuring raw data into analysis-ready tables
- building a clean dashboard prototype for stakeholder review

## Data Sources

This project uses existing public sources only.

- IPEDS / NCES for enrollment, retention, graduation, and completions
- College Scorecard for admissions, completion, earnings, and debt context
- Indiana University Common Data Set for institution-specific profile metrics
- NACE First-Destination standards for methodology context

## Version 1 Metrics

The first version of the dashboard includes:

- total enrollment
- undergraduate enrollment
- first-year retention rate
- graduation rate
- degrees awarded
- admissions rate
- median earnings
- median graduate debt

## Dashboard Prototype

The first dashboard prototype is built in Streamlit and reads from the cleaned project tables.

Main files:

- [src/app.py](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/src/app.py)
- [reports/dashboard_summary_v1.csv](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/reports/dashboard_summary_v1.csv)

The dashboard currently includes:

- executive KPI cards
- benchmark and outcomes tables
- institution profile metrics
- visual comparisons for enrollment mix, outcomes, and cross-source rates

## Screenshots

### Enrollment and Outcomes Analysis

![Enrollment and outcomes analysis](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/enrollment-outcome-analysis.png)

This view highlights the dashboard's benchmark snapshot, enrollment mix, outcomes comparison, and project notes.

### Institution Profile

![Institution profile](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/instituition-profile.png)

This view shows the institution-specific profile metrics drawn from IU CDS, including enrollment, degrees conferred, retention, graduation, and admissions context.

### Cross-Source Comparison

![Cross-source comparison](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/cross-source-comparison.png)

This view emphasizes one of the main analyst takeaways: comparing public metrics across IPEDS, College Scorecard, and IU CDS requires clear documentation of source definitions and reporting windows.

## How To Run

Using the local virtual environment:

```bash
./.venv/bin/streamlit run src/app.py
```

If the virtual environment is not set up yet:

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./.venv/bin/streamlit run src/app.py
```

## Repository Highlights

- `data/raw`: downloaded public source files
- `data/processed`: cleaned metrics and schema-aligned benchmark tables
- `docs`: business analysis, schema, and source strategy documentation
- `reports`: dashboard-ready summary outputs
- `src`: data preparation and dashboard code

## Key Project Outputs

- [data/processed/institution_benchmarks_v1.csv](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/data/processed/institution_benchmarks_v1.csv)
- [data/processed/outcomes_benchmarks_v1.csv](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/data/processed/outcomes_benchmarks_v1.csv)
- [data/processed/institution_profile_v1.csv](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/data/processed/institution_profile_v1.csv)
- [reports/dashboard_summary_v1.md](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/reports/dashboard_summary_v1.md)

## Documentation

Supporting project docs:

- [docs/project_scope.md](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/docs/project_scope.md)
- [docs/data_source_strategy.md](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/docs/data_source_strategy.md)
- [docs/schema_overview.md](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/docs/schema_overview.md)
- [docs/data_dictionary.md](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/docs/data_dictionary.md)
- [docs/metrics_plan.md](/Users/saishriyasurla/Desktop/Projects/student-success-signal-hub/docs/metrics_plan.md)

## Next Improvements

- add multi-year trends
- add peer institution comparison
- expand the methodology section
- capture dashboard screenshots for portfolio use
- write resume bullets and a short case study summary
