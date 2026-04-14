# Metric Extraction Notes

## Version 1 IU Bloomington Metrics

The first processed metrics file is:

- `data/processed/iu_bloomington_metrics_v1.csv`

## Extraction Rules Used

- `institution_name` and `unitid` were taken from `hd2024.csv`
- `total_enrollment` was taken from `effy2024.csv` field `EFYTOTLT`
- `undergraduate_enrollment` was taken from College Scorecard field `UGDS`
- `first_year_retention_rate` was taken from `ef2024d.csv` field `RET_PCF`
- `graduation_rate` was taken from College Scorecard field `C150_4`
- `graduation_rate_ipeds` was computed from `gr2024.csv` using:
  - adjusted cohort = `8051`
  - graduates within the measured period = `6458`
  - rate = `6458 / 8051 = 0.8021`
- `degrees_awarded_total` was computed from `c2024_a.csv` as the sum of `CTOTALT` where:
  - `UNITID = 151351`
  - `MAJORNUM = 1`
- `admissions_rate` was taken from College Scorecard field `ADM_RATE`
- `median_earnings` was taken from College Scorecard field `MD_EARN_WNE_P10`
- `median_grad_debt` was taken from College Scorecard field `GRAD_DEBT_MDN`

## Important Notes

- Some values differ slightly across public sources because the files measure different populations or time windows.
- For example, IU CDS enrollment values and IPEDS/Scorecard enrollment values are not identical because they are based on different reporting definitions.
- For Version 1, this is acceptable as long as each metric is clearly sourced and documented.

## Recommended Next Step

The next step is to convert these metrics into the project tables defined in the schema and begin building a cleaned benchmark dataset for dashboard use.
