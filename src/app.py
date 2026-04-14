from __future__ import annotations

import csv
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "reports" / "dashboard_summary_v1.csv"


def read_summary() -> list[dict[str, str]]:
    with SUMMARY_PATH.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def metric_lookup(rows: list[dict[str, str]], metric_name: str, preferred_section: str | None = None) -> dict[str, str] | None:
    for row in rows:
        if row["metric_name"] == metric_name and (
            preferred_section is None or row["dashboard_section"] == preferred_section
        ):
            return row
    return None


def format_metric(metric_name: str, value: str) -> str:
    numeric = float(value)

    if "rate" in metric_name:
        return f"{numeric:.1%}"
    if "debt" in metric_name or "earnings" in metric_name:
        return f"${numeric:,.0f}"
    return f"{numeric:,.0f}"


def section_table(rows: list[dict[str, str]], section: str) -> list[dict[str, str]]:
    section_rows = [row for row in rows if row["dashboard_section"] == section]
    return [
        {
            "Metric": row["metric_name"].replace("_", " ").title(),
            "Value": format_metric(row["metric_name"], row["metric_value"]),
            "Source": row["source_name"],
            "Year": row["reporting_year"],
        }
        for row in section_rows
    ]


st.set_page_config(
    page_title="Student Success Signal Hub",
    page_icon="📊",
    layout="wide",
)

rows = read_summary()

st.title("Student Success Signal Hub")
st.caption(
    "Public-data prototype for higher education benchmark and graduate outcomes reporting."
)

left, right = st.columns([1.6, 1], gap="large")

with left:
    st.subheader("Executive Overview")
    top_metrics = st.columns(4)
    metric_config = [
        ("total_enrollment", "Total Enrollment", "Institution Benchmarks"),
        ("first_year_retention_rate", "Retention Rate", "Institution Benchmarks"),
        ("graduation_rate", "Graduation Rate", "Outcomes Benchmarks"),
        ("median_earnings", "Median Earnings", "Outcomes Benchmarks"),
    ]
    for column, (metric_key, label, section) in zip(top_metrics, metric_config, strict=False):
        row = metric_lookup(rows, metric_key, section)
        if row:
            column.metric(label, format_metric(metric_key, row["metric_value"]), f"{row['source_name']} {row['reporting_year']}")

    st.subheader("Benchmark Snapshot")
    st.dataframe(section_table(rows, "Institution Benchmarks"), use_container_width=True, hide_index=True)

    st.subheader("Outcomes Snapshot")
    st.dataframe(section_table(rows, "Outcomes Benchmarks"), use_container_width=True, hide_index=True)

with right:
    st.subheader("Institution Profile")
    st.dataframe(section_table(rows, "Institution Profile"), use_container_width=True, hide_index=True)

    st.subheader("Project Notes")
    st.markdown(
        """
        - This prototype uses existing public data only.
        - IPEDS, College Scorecard, and IU CDS values may differ slightly because reporting windows and definitions vary.
        - The current dashboard is a Version 1 summary view built from cleaned benchmark tables.
        """
    )

    st.subheader("Next Build Ideas")
    st.markdown(
        """
        - Add trend charts across multiple years
        - Compare IU Bloomington with peer institutions
        - Add filters for source and metric group
        - Expand the reporting context panel with NACE methodology
        """
    )
