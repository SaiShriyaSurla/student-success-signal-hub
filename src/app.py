from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd
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


def metric_label(metric_name: str) -> str:
    labels = {
        "total_enrollment": "Total Enrollment",
        "first_year_retention_rate": "First-Year Retention Rate",
        "admissions_rate": "Admissions Rate",
        "degrees_awarded_total": "Degrees Awarded",
        "undergraduate_enrollment": "Undergraduate Enrollment",
        "graduation_rate": "Graduation Rate",
        "graduation_rate_ipeds": "Graduation Rate (IPEDS)",
        "median_earnings": "Median Earnings",
        "median_grad_debt": "Median Graduate Debt",
        "graduate_enrollment": "Graduate Enrollment",
        "total_all_students": "Total All Students",
        "degrees_conferred": "Degrees Conferred",
        "bachelors_degrees": "Bachelor's Degrees",
        "retention_rate": "Retention Rate",
        "six_year_graduation_rate": "Six-Year Graduation Rate",
    }
    return labels.get(metric_name, metric_name.replace("_", " ").title())


def metric_value(rows: list[dict[str, str]], metric_name: str, preferred_section: str | None = None) -> float | None:
    row = metric_lookup(rows, metric_name, preferred_section)
    if row is None:
        return None
    return float(row["metric_value"])


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
            "Metric": metric_label(row["metric_name"]),
            "Value": format_metric(row["metric_name"], row["metric_value"]),
            "Source": row["source_name"],
            "Year": row["reporting_year"],
        }
        for row in section_rows
    ]


def build_enrollment_mix(rows: list[dict[str, str]]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Group": "Undergraduate",
                "Students": metric_value(rows, "undergraduate_enrollment", "Institution Profile") or 0,
            },
            {
                "Group": "Graduate",
                "Students": metric_value(rows, "graduate_enrollment", "Institution Profile") or 0,
            },
        ]
    )


def build_outcomes_chart(rows: list[dict[str, str]]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Metric": "Median Earnings",
                "Value": metric_value(rows, "median_earnings", "Outcomes Benchmarks") or 0,
            },
            {
                "Metric": "Median Graduate Debt",
                "Value": metric_value(rows, "median_grad_debt", "Outcomes Benchmarks") or 0,
            },
        ]
    )


def build_rate_comparison(rows: list[dict[str, str]]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Metric": "Retention",
                "IPEDS / Scorecard": metric_value(rows, "first_year_retention_rate", "Institution Benchmarks") or 0,
                "IU CDS": metric_value(rows, "retention_rate", "Institution Profile") or 0,
            },
            {
                "Metric": "Graduation",
                "IPEDS / Scorecard": metric_value(rows, "graduation_rate", "Outcomes Benchmarks") or 0,
                "IU CDS": metric_value(rows, "six_year_graduation_rate", "Institution Profile") or 0,
            },
            {
                "Metric": "Admissions",
                "IPEDS / Scorecard": metric_value(rows, "admissions_rate", "Institution Benchmarks") or 0,
                "IU CDS": metric_value(rows, "admissions_rate", "Institution Profile") or 0,
            },
        ]
    )


st.set_page_config(
    page_title="Student Success Signal Hub",
    page_icon="SS",
    layout="wide",
)

rows = read_summary()
enrollment_mix = build_enrollment_mix(rows)
outcomes_chart = build_outcomes_chart(rows)
rate_comparison = build_rate_comparison(rows)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(184, 208, 255, 0.35), transparent 28%),
            linear-gradient(180deg, #f4f7fb 0%, #ffffff 48%, #f7f8f4 100%);
    }
    .hero {
        padding: 1.4rem 1.6rem;
        border-radius: 22px;
        background: linear-gradient(135deg, #0f3d3e 0%, #164f52 55%, #c9792b 100%);
        color: #f7f4ef;
        box-shadow: 0 18px 60px rgba(15, 61, 62, 0.18);
        margin-bottom: 1rem;
    }
    .hero h1 {
        margin: 0 0 0.35rem 0;
        font-size: 2.4rem;
        line-height: 1.05;
    }
    .hero p {
        margin: 0;
        max-width: 880px;
        font-size: 1rem;
    }
    .context-card {
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(15, 61, 62, 0.08);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 0.84rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #6e6d63;
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>Student Success Signal Hub</h1>
        <p>
            A public-data dashboard prototype for higher education business analysis,
            combining institutional benchmarks, graduate outcomes context, and IU Bloomington
            profile data into one leadership-ready reporting view.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.6, 1], gap="large")

with left:
    st.markdown('<div class="section-title">Executive Overview</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="context-card">
        This prototype answers a simple analyst question:
        <strong>What do public data sources say about IU Bloomington's scale, retention,
        completion, and post-college outcomes?</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )
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

    st.markdown('<div class="section-title">Benchmark Snapshot</div>', unsafe_allow_html=True)
    st.dataframe(section_table(rows, "Institution Benchmarks"), use_container_width=True, hide_index=True)

    chart_left, chart_right = st.columns(2, gap="large")
    with chart_left:
        st.markdown('<div class="section-title">Enrollment Mix</div>', unsafe_allow_html=True)
        st.bar_chart(enrollment_mix.set_index("Group"), color="#1f6f78")

    with chart_right:
        st.markdown('<div class="section-title">Outcomes Comparison</div>', unsafe_allow_html=True)
        st.bar_chart(outcomes_chart.set_index("Metric"), color="#c9792b")

    st.markdown('<div class="section-title">Outcomes Snapshot</div>', unsafe_allow_html=True)
    st.dataframe(section_table(rows, "Outcomes Benchmarks"), use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">Cross-Source Rate Comparison</div>', unsafe_allow_html=True)
    st.bar_chart(rate_comparison.set_index("Metric"), color=["#164f52", "#d98b3b"])

    st.markdown('<div class="section-title">Analyst Takeaways</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="context-card">
        <strong>Retention and graduation are both strong in the current pull.</strong> The benchmark view
        shows a retention rate around 91% and a graduation rate around 80%, while outcomes data adds
        earnings and debt context to the student success story.
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown('<div class="section-title">Institution Profile</div>', unsafe_allow_html=True)
    st.dataframe(section_table(rows, "Institution Profile"), use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">Project Notes</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="context-card">
        - This prototype uses existing public data only.
        - IPEDS, College Scorecard, and IU CDS values may differ slightly because reporting windows and definitions vary.
        - The current dashboard is a Version 1 summary view built from cleaned benchmark tables.
        </div>
        """
        ,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Next Build Ideas</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="context-card">
        - Add trend charts across multiple years
        - Compare IU Bloomington with peer institutions
        - Add filters for source and metric group
        - Expand the reporting context panel with NACE methodology
        </div>
        """
        ,
        unsafe_allow_html=True,
    )
