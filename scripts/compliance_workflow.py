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

The rows.json format is a JSON array of objects; each key should match a
phase-sheet column (see PHASE_SHEETS), and a "Part" value routes the row to
its sheet (see SHEET_PART). Unknown keys are ignored.
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
# Schema — kept in sync with references/schemas.md "Master execution work order"
# The deliverable is three phase sheets, each with its own tailored columns.
# --------------------------------------------------------------------------- #

PHASE_SHEETS = [
    {
        "name": "1 开发",
        "title": "1 开发处理（无需 UI 出稿）",
        "collab": "后端 / 前端 / 运维 / SEO 技术实现。P0 = 上线阻断。最后一列 = 对参考文件的修正。",
        "columns": [
            "编号", "优先级", "模块", "事项", "具体需求（做什么）",
            "合规/SEO 依据", "验收标准", "对参考文件的修正/备注",
        ],
    },
    {
        "name": "2 UI+开发",
        "title": "2 UI + 开发一起处理",
        "collab": "先由 UI 出组件、状态、响应式和无障碍方案，再交开发实现；文案按 C-xx 引用运营表。",
        "columns": [
            "编号", "优先级", "模块", "事项", "具体需求（做什么）",
            "对参考文件的修正/备注",
        ],
    },
    {
        "name": "3 运营文案",
        "title": "3 运营准备文案与资料",
        "collab": "英文基线仅为草稿，最终以法务审定为准。政策正文由运营备料、法务起草定稿。",
        "columns": [
            "编号", "优先级", "类型", "文案/资料", "需要写什么（要点）",
            "建议英文基线", "展示位置",
        ],
    },
]

# phase sheet name -> part tag (for filtering rows into the right sheet)
SHEET_PART = {
    "1 开发": "技术排版",
    "2 UI+开发": "UI 设计排版",
    "3 运营文案": "运营排版",
}

# Flat union of all sheet columns, used by the report view only.
REPORT_COLUMNS = ["编号", "优先级", "模块/类型", "事项/文案", "具体需求/要点", "建议英文基线", "依据", "验收标准", "展示位置", "对参考文件的修正/备注"]

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
    """Return an openpyxl Workbook with three phase sheets, per schemas.md."""
    import openpyxl
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    wb = openpyxl.Workbook()

    header_fill = PatternFill("solid", fgColor="2B2F3A")
    header_font = Font(color="FFFFFF", bold=True, size=10)
    title_font = Font(bold=True, size=12)
    collab_font = Font(color="5B616E", size=9, italic=True)
    wrap = Alignment(wrap_text=True, vertical="top")

    for idx, sheet in enumerate(PHASE_SHEETS):
        ws = wb.active if idx == 0 else wb.create_sheet()
        ws.title = sheet["name"]
        columns = sheet["columns"]
        ncol = len(columns)

        # Row 1: title (merged)
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncol)
        ws.cell(row=1, column=1, value=sheet["title"]).font = title_font

        # Row 2: collaboration note (merged)
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncol)
        note = ws.cell(row=2, column=1, value=sheet["collab"])
        note.font = collab_font
        note.alignment = wrap
        ws.row_dimensions[2].height = 30

        # Row 3: column headers
        for col, name in enumerate(columns, start=1):
            cell = ws.cell(row=3, column=col, value=name)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            ws.column_dimensions[get_column_letter(col)].width = 24

        # Row 4: sample row, clearly marked
        ws.cell(row=4, column=1, value="SAMPLE-001").alignment = wrap
        if len(columns) >= 2 and columns[1] == "优先级":
            ws.cell(row=4, column=2, value="P0").alignment = wrap
            dv = DataValidation(
                type="list", formula1='"' + ",".join(PRIORITIES) + '"', allow_blank=True
            )
            ws.add_data_validation(dv)
            dv.add("B4:B1000")

        ws.freeze_panes = "A4"

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
h2 { font-size:12px; margin:14px 0 4px; }
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
    from collections import defaultdict

    part_to_sheet = {v: k for k, v in SHEET_PART.items()}
    grouped = defaultdict(list)
    for row in rows:
        if not isinstance(row, dict):
            continue
        grouped[part_to_sheet.get(row.get("Part", ""), "其他")].append(row)

    parts = [
        "<!doctype html><html><head><meta charset='utf-8'><style>",
        REPORT_CSS,
        "</style></head><body>",
        f"<h1>{html.escape(title)}</h1>",
        '<div class="sub">Generated by north-america-web-seo-compliance</div>',
    ]

    for sheet in PHASE_SHEETS:
        name = sheet["name"]
        columns = sheet["columns"]
        sheet_rows = grouped.get(name, [])
        parts.append(f"<h2>{html.escape(name)}</h2>")
        parts.append("<table><thead><tr>")
        parts += [f"<th>{html.escape(c)}</th>" for c in columns]
        parts.append("</tr></thead><tbody>")
        for row in sheet_rows:
            parts.append("<tr>")
            for c in columns:
                value = row.get(c, "")
                cell = _badge(value) if c == "优先级" else html.escape(str(value))
                parts.append(f"<td>{cell}</td>")
            parts.append("</tr>")
        parts.append("</tbody></table>")

    other = grouped.get("其他", [])
    if other:
        parts.append("<h2>其他</h2>")
        parts.append("<table><thead><tr>")
        parts += [f"<th>{html.escape(c)}</th>" for c in REPORT_COLUMNS]
        parts.append("</tr></thead><tbody>")
        for row in other:
            parts.append("<tr>")
            for c in REPORT_COLUMNS:
                parts.append(f"<td>{html.escape(str(row.get(c, '')))}</td>")
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
