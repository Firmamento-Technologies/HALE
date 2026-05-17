#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_risk_register.py
======================

Costruisce l'Allegato A.2 — Risk Register v1.0 dello Studio di Fattibilita'
HALE/VTOL di Firmamento Technologies.

Metodologia: NASA NPR 8000.4 (Continuous Risk Management) + FMECA
(MIL-STD-1629A) + FTA (ARP4761) + ISO 31000.

Output:
- RISK-REGISTER-v1.0.xlsx   (multi-sheet, 22 fogli)
- RISK-REGISTER-v1.0-full.csv (tutti i rischi consolidati)
- A2-RISK-REGISTER-REPORT.md  (report narrativo)

Autore: senior risk manager + safety engineer aerospace
Versione: v1.0  (M+3, 2026-05-17)
"""

from __future__ import annotations

import csv
import os
from datetime import date
from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

# ---------------------------------------------------------------------------
# Configurazione globale
# ---------------------------------------------------------------------------
OUT_DIR = Path("/home/user/HALE/studio-di-fattibilita/allegati/A2-Risk-Register")
OUT_DIR.mkdir(parents=True, exist_ok=True)

XLSX_PATH = OUT_DIR / "RISK-REGISTER-v1.0.xlsx"
CSV_PATH = OUT_DIR / "RISK-REGISTER-v1.0-full.csv"
MD_PATH = OUT_DIR / "A2-RISK-REGISTER-REPORT.md"

TODAY = "2026-05-17"
VERSION = "v1.0"

# ---------------------------------------------------------------------------
# Helpers di stile per openpyxl
# ---------------------------------------------------------------------------
THIN = Side(border_style="thin", color="888888")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

FILL_HEADER = PatternFill("solid", fgColor="1F3864")
FILL_SUB = PatternFill("solid", fgColor="D9E1F2")
FILL_RED = PatternFill("solid", fgColor="C00000")
FILL_ORANGE = PatternFill("solid", fgColor="ED7D31")
FILL_YELLOW = PatternFill("solid", fgColor="FFC000")
FILL_GREEN = PatternFill("solid", fgColor="70AD47")
FILL_GREY = PatternFill("solid", fgColor="BFBFBF")

FONT_HEADER = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
FONT_SUB = Font(name="Calibri", size=10, bold=True, color="1F3864")
FONT_BODY = Font(name="Calibri", size=10)
FONT_BODY_BOLD = Font(name="Calibri", size=10, bold=True)
FONT_WHITE_BOLD = Font(name="Calibri", size=10, bold=True, color="FFFFFF")

WRAP = Alignment(wrap_text=True, vertical="top", horizontal="left")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")


def color_for_score(score: int) -> PatternFill:
    """Color coding NASA NPR 8000.4 P x I matrix."""
    if score >= 15:
        return FILL_RED
    if score >= 8:
        return FILL_YELLOW
    if score >= 4:
        return FILL_GREEN
    return PatternFill("solid", fgColor="E2EFDA")


def font_for_score(score: int) -> Font:
    if score >= 15:
        return FONT_WHITE_BOLD
    return FONT_BODY


def status_color(status: str) -> str:
    return {
        "Open": "C00000",
        "Open-Critical": "C00000",
        "Open-High": "ED7D31",
        "Mitigated": "70AD47",
        "Monitor": "FFC000",
        "Closed": "A6A6A6",
        "Showstopper": "C00000",
    }.get(status, "000000")


def write_header(ws, headers, row=1, widths=None):
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=row, column=c, value=h)
        cell.fill = FILL_HEADER
        cell.font = FONT_HEADER
        cell.alignment = CENTER
        cell.border = BORDER
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=row + 1, column=1)


def write_row(ws, row_idx, values, score_col=None, fill_score=True):
    for c, v in enumerate(values, 1):
        cell = ws.cell(row=row_idx, column=c, value=v)
        cell.alignment = WRAP
        cell.font = FONT_BODY
        cell.border = BORDER
    if score_col and fill_score:
        score_val = values[score_col - 1]
        if isinstance(score_val, int):
            ws.cell(row=row_idx, column=score_col).fill = color_for_score(score_val)
            ws.cell(row=row_idx, column=score_col).font = font_for_score(score_val)
            ws.cell(row=row_idx, column=score_col).alignment = CENTER
