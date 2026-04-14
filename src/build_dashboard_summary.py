from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def build_summary_rows() -> list[dict[str, str]]:
    institution_benchmarks = read_csv(PROCESSED_DIR / "institution_benchmarks_v1.csv")
    outcomes_benchmarks = read_csv(PROCESSED_DIR / "outcomes_benchmarks_v1.csv")
    institution_profile = read_csv(PROCESSED_DIR / "institution_profile_v1.csv")

    rows: list[dict[str, str]] = []

    for row in institution_benchmarks:
        rows.append(
            {
                "dashboard_section": "Institution Benchmarks",
                "metric_name": row["metric_name"],
                "metric_value": row["metric_value"],
                "source_name": row["source_name"],
                "reporting_year": row["reporting_year"],
                "notes": row["notes"],
            }
        )

    for row in outcomes_benchmarks:
        rows.append(
            {
                "dashboard_section": "Outcomes Benchmarks",
                "metric_name": row["metric_name"],
                "metric_value": row["metric_value"],
                "source_name": row["source_name"],
                "reporting_year": row["reporting_year"],
                "notes": row["notes"],
            }
        )

    for row in institution_profile:
        rows.append(
            {
                "dashboard_section": "Institution Profile",
                "metric_name": row["profile_metric_name"],
                "metric_value": row["profile_metric_value"],
                "source_name": row["source_name"],
                "reporting_year": row["reporting_year"],
                "notes": row["notes"],
            }
        )

    return rows


def write_summary_csv(rows: list[dict[str, str]], path: Path) -> None:
    fieldnames = [
        "dashboard_section",
        "metric_name",
        "metric_value",
        "source_name",
        "reporting_year",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_summary_markdown(rows: list[dict[str, str]], path: Path) -> None:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["dashboard_section"], []).append(row)

    lines = [
        "# Dashboard Summary v1",
        "",
        "This file is a quick review artifact generated from the processed benchmark tables.",
        "",
    ]

    for section, section_rows in grouped.items():
        lines.append(f"## {section}")
        lines.append("")
        lines.append("| Metric | Value | Source | Year |")
        lines.append("| --- | --- | --- | --- |")
        for row in section_rows:
            lines.append(
                f"| {row['metric_name']} | {row['metric_value']} | "
                f"{row['source_name']} | {row['reporting_year']} |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORTS_DIR.mkdir(exist_ok=True)
    rows = build_summary_rows()
    write_summary_csv(rows, REPORTS_DIR / "dashboard_summary_v1.csv")
    write_summary_markdown(rows, REPORTS_DIR / "dashboard_summary_v1.md")
    print("Generated reports/dashboard_summary_v1.csv")
    print("Generated reports/dashboard_summary_v1.md")


if __name__ == "__main__":
    main()
