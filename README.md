# Student Success Signal Hub

Student Success Signal Hub is a portfolio project designed to mirror the work of a higher education business analyst supporting student success, institutional reporting, and graduate outcomes analysis.

The project uses existing public higher education datasets and official reporting standards to build a realistic benchmark and outcomes analytics environment. The goal is to show how integrated reporting can support leadership decision-making, performance monitoring, and institutional storytelling across the student lifecycle.

## Project Foundation

The initial project framing for Phase 1 lives in [docs/project_scope.md](docs/project_scope.md). It defines:

- the business problem
- the target stakeholders
- the primary reporting questions
- the success criteria for the project

Phase 2 planning documents now live in:

- [docs/data_source_strategy.md](docs/data_source_strategy.md)
- [docs/schema_overview.md](docs/schema_overview.md)
- [docs/metrics_plan.md](docs/metrics_plan.md)

## Planned Scope

The project is expected to include:

- public benchmark and institutional context data
- public graduate outcomes and post-college context data
- data cleaning and validation workflows
- KPI reporting for enrollment, retention, completion, and outcomes
- dashboard views for leadership and institutional research use cases
- business analyst artifacts such as requirements, definitions, and process documentation

## Repository Structure

- `data/raw`: downloaded public source files before cleaning
- `data/external`: reference extracts and curated public data inputs
- `data/processed`: cleaned and analytics-ready outputs
- `docs`: scope, source strategy, schema, and business analysis documentation
- `reports`: exported summaries, screenshots, and portfolio artifacts
- `src`: future ingestion, transformation, validation, and dashboard code
- `tests`: future data quality and transformation tests

## Dashboard Prototype

The first dashboard prototype is a Streamlit app:

- `src/app.py`

Install the dependency and run it locally:

```bash
pip install -r requirements.txt
streamlit run src/app.py
```
