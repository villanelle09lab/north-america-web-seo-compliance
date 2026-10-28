#!/usr/bin/env python3
"""
north-america-web-seo-compliance — deliverable generator.

A generic, product-agnostic tool that turns a compliance run into concrete
deliverables. It contains no product- or business-specific content; you fill the
returned structures with your own findings.

Produces:
  1. Master execution checklist as an XLSX workbook (single source of truth).
  2. A styled HTML report, rendered to PDF when a Chromium browser is available.

Usage:
  python3 compliance_workflow.py checklist --out out/checklist.xlsx
  python3 compliance_workflow.py report --rows rows.json --out out/report.pdf

The rows.json format is a JSON array of objects; each key must match one of
MASTER_CHECKLIST_COLUMNS. Unknown keys are ignored.
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
from pathlib import Path

# --------------------------------------------------------------------------- #
# Schema — kept in sync with references/schemas.md
# --------------------------------------------------------------------------- #

MASTER_CHECKLIST_COLUMNS = [
    "Requirement ID",
    "Copy ID",
    "Module or page",
    "Trigger and audience",
    "Jurisdiction",
    "Applicability condition",
    "Evidence class",
    "Compliance or SEO type",
    "Part",
    "Requirement",
    "Mandatory English copy or placeholder",
    "Dynamic variables",
    "UI behavior",
    "Frontend/backend implementation",
    "Operations material",
    "Official source",
    "Competitor evidence",
    "Target current state",
    "Gap",
    "Red flag or non-compliance risk",
    "Priority",
    "Owner",
    "Legal status",
    "QA acceptance",
    "Not-applicable reason",
    "Last verified",
]

PRIORITIES = ("P0", "P1", "P2", "N/A")

LEGAL_STATUSES = (
    "Not reviewed",
    "Counsel question open",
    "Draft for counsel",
    "Counsel approved",
    "Implementation deviates from approved text",
    "Not applicable",
)

PARTS = (
    "技术排版",
    "UI 设计排版",
    "运营排版",
)


def _require_openpyxl() -> None:
    try:
        import openpyxl  # noqa: F401
    except ImportError:  # pragma: no cover
        sys.exit(
            "Missing dependency 'openpyxl'. Install it with: pip install -r requirements.txt"
        )


# --------------------------------------------------------------------------- #
# Checklist (XLSX)
# --------------------------------------------------------------------------- #

def build_checklist_workbook():
    """Return an openpyxl Workbook pre-populated with the checklist schema."""
    import openpyxl
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Master checklist"

    header_fill = PatternFill("solid", fgColor="2B2F3A")
    header_font = Font(color="FFFFFF", bold=True, size=10)
    wrap = Alignment(wrap_text=True, vertical="top")

    for col, name in enumerate(MASTER_CHECKLIST_COLUMNS, start=1):
        cell = ws.cell(row=1, column=col, value=name)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(vertical="center")
        ws.column_dimensions[get_column_letter(col)].width = 18

    # one example row, marked clearly as a sample
    example = {name: "" for name in MASTER_CHECKLIST_COLUMNS}
    example["Requirement ID"] = "SAMPLE-001"
    example["Priority"] = "P0"
    example["Legal status"] = "Not reviewed"
    example["Requirement"] = "Replace with a real, independently testable obligation."
    for col, name in enumerate(MASTER_CHECKLIST_COLUMNS, start=1):
        ws.cell(row=2, column=col, value=example[name]).alignment = wrap

    # data validation for the two controlled vocabularies
    dv_priority = DataValidation(
        type="list", formula1='"' + ",".join(PRIORITIES) + '"', allow_blank=True
    )
    ws.add_data_validation(dv_priority)
    dv_priority.add(f"T2:T1000")

    dv_legal = DataValidation(
        type="list", formula1='"' + ",".join(LEGAL_STATUSES) + '"', allow_blank=True
    )
    ws.add_data_validation(dv_legal)
    dv_legal.add(f"V2:V1000")

    ws.freeze_panes = "A2"
    return wb


def save_checklist(path: Path) -> None:
    _require_openpyxl()
    wb = build_checklist_workbook()
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    print(f"Checklist written: {path}")


# --------------------------------------------------------------------------- #
# Report (HTML -> PDF)
# --------------------------------------------------------------------------- #

REPORT_CSS = """
@page { size: A4 landscape; margin: 12mm 11mm; }
body { font-family: -apple-system, "Segoe UI", Arial, sans-serif; color:#1a1d23;
       font-size:9px; line-height:1.45; margin:0; }
h1 { font-size:18px; margin:0 0 2px; }
.sub { color:#5b616e; font-size:10px; margin-bottom:12px; }
table { border-collapse:collapse; width:100%; }
th,td { border:1px solid #e2e4ea; padding:4px 5px; text-align:left;
        vertical-align:top; word-break:break-word; font-size:7.5px; }
th { background:#2b2f3a; color:#fff; white-space:nowrap; }
tr:nth-child(even) td { background:#fafafc; }
.badge { display:inline-block; border-radius:3px; padding:0 5px; font-size:7px;
         font-weight:600; white-space:nowrap; }
.b-p0 { background:#fde8e8; color:#b91c1c; }
.b-p1 { background:#fdf1dd; color:#9a5b00; }
.b-counsel { background:#fdf1dd; color:#9a5b00; }
.b-draft { background:#e3ecfb; color:#1d4ed8; }
.foot { margin-top:12px; color:#8a90a0; font-size:7.5px; text-align:center; }
"""


def _badge(value: str) -> str:
    value = (value or "").strip()
    cls = ""
    if value == "P0":
        cls = "b-p0"
    elif value == "P1":
        cls = "b-p1"
    elif value in ("Counsel question open", "Draft for counsel"):
        cls = "b-draft" if value == "Draft for counsel" else "b-counsel"
    if not cls:
        return html.escape(value)
    return f'<span class="badge {cls}">{html.escape(value)}</span>'


def build_report_html(rows, title: str = "Compliance Execution Checklist") -> str:
    parts = [
        "<!doctype html><html><head><meta charset='utf-8'><style>",
        REPORT_CSS,
        "</style></head><body>",
        f"<h1>{html.escape(title)}</h1>",
        '<div class="sub">Generated by north-america-web-seo-compliance</div>',
        "<table><thead><tr>",
    ]
    parts += [f"<th>{html.escape(c)}</th>" for c in MASTER_CHECKLIST_COLUMNS]
    parts.append("</tr></thead><tbody>")
    for row in rows:
        parts.append("<tr>")
        for c in MASTER_CHECKLIST_COLUMNS:
            value = row.get(c, "") if isinstance(row, dict) else ""
            if c == "Priority":
                cell = _badge(value)
            elif c == "Legal status":
                cell = _badge(value)
            else:
                cell = html.escape(str(value))
            parts.append(f"<td>{cell}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    parts.append(
        '<div class="foot">Not a substitute for licensed legal advice.</div>'
    )
    parts.append("</body></html>")
    return "".join(parts)


def _find_chromium() -> str | None:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("chrome"),
    ]
    for cand in candidates:
        if cand and Path(cand).exists():
            return cand
    return None


def save_report(rows, out: Path, title: str) -> None:
    html_text = build_report_html(rows, title)
    out.parent.mkdir(parents=True, exist_ok=True)

    target = out if out.suffix.lower() == ".pdf" else out.with_suffix(".pdf")
    html_path = target.with_suffix(".html")
    html_path.write_text(html_text, encoding="utf-8")

    chromium = _find_chromium()
    if chromium:
        subprocess.run(
            [
                chromium,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={target}",
                f"file://{html_path.resolve()}",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"Report written: {target}")
    else:
        print(f"Report written as HTML (no Chromium found for PDF): {html_path}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("checklist", help="Generate the master checklist XLSX")
    p_check.add_argument("--out", type=Path, required=True)

    p_report = sub.add_parser("report", help="Render a report from JSON rows")
    p_report.add_argument("--rows", type=Path, required=True)
    p_report.add_argument("--out", type=Path, required=True)
    p_report.add_argument("--title", default="Compliance Execution Checklist")
    p_report.add_argument("--part", help="Filter rows to one part (技术排版 / UI 设计排版 / 运营排版)")

    args = parser.parse_args(argv)

    if args.command == "checklist":
        save_checklist(args.out)
        return 0

    rows = json.loads(Path(args.rows).read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        sys.exit("rows.json must contain a JSON array")
    if args.part:
        rows = [r for r in rows if isinstance(r, dict) and r.get("Part") == args.part]
    save_report(rows, args.out, args.title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
