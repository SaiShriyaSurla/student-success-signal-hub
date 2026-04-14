# Student Success Signal Hub

Student Success Signal Hub is a portfolio project designed to mirror the work of a higher education business analyst supporting placement operations, student engagement, and career outcomes reporting.

The project combines authentic public higher education data with synthetic student-level operational records to simulate a realistic university analytics environment. The goal is to show how integrated reporting can support leadership decision-making, operational follow-up, and data quality improvement across the student lifecycle.

## Project Foundation

The initial project framing for Phase 1 lives in [docs/project_scope.md](docs/project_scope.md). It defines:

- the business problem
- the target stakeholders
- the primary reporting questions
- the success criteria for the project

Phase 2 planning documents now live in:

- [docs/data_source_strategy.md](docs/data_source_strategy.md)
- [docs/schema_overview.md](docs/schema_overview.md)

## Planned Scope

The project is expected to include:

- public benchmark and institutional context data
- synthetic student-level placement, advising, and outcomes records
- data cleaning and validation workflows
- KPI reporting for placement, engagement, and first-destination outcomes
- dashboard views for leadership and operations
- business analyst artifacts such as requirements, definitions, and process documentation

## Repository Structure

- `data/raw`: downloaded public source files before cleaning
- `data/external`: reference extracts and curated public data inputs
- `data/synthetic`: generated student-level operational datasets
- `data/processed`: cleaned and analytics-ready outputs
- `docs`: scope, source strategy, schema, and business analysis documentation
- `reports`: exported summaries, screenshots, and portfolio artifacts
- `src`: future ingestion, transformation, validation, and dashboard code
- `tests`: future data quality and transformation tests
