#!/usr/bin/env python3
"""apply_jedida_reporting.py — Apply the Jedida Reporting palette + structural
patterns to an existing Google Doc.

This is the Google-Docs-native port of the docx/xlsx Jedida Reporting Skill
(navy/blue palette, RACI strip vibe, full-width nav banners, 2-col tables,
traffic-light colors). The skill itself is calibrated for HITL/pipeline failure
analysis outputs; this script applies the same visual identity to any Google
Doc so we can compare against the doc-styling-1 (forest green) and
doc-styling-3 (forest green V3) variants.

Usage:
    python3 apply_jedida_reporting.py <docId>
    python3 apply_jedida_reporting.py https://docs.google.com/document/d/<docId>/edit

Pipeline (multi-pass, refetch between passes):
    Pass 0: Sanitize     — clear baselineOffset artifacts
    Pass 1: Document     — page margins (45pt = 0.625")
    Pass 2: Named styles — TITLE / HEADING_1..3 / NORMAL_TEXT typography
    Pass 3: H1 cleanup   — Clear any prior NAV background block; H1s render
                           as dark-blue (NAV) text only, no shaded block
                           (v1.0.0–1.1.0 used full-width nav bars; deprecated
                           in v1.2.0 per researcher feedback)
    Pass 4: Tables       — first-col label fill (LBLUE), alternating rows,
                           DGRAY borders; header row gets NAV fill + WHITE text
                           if it looks like a header (single-row label across
                           multiple columns, or first row of multi-row tables).
                           For 2-col label/content tables, fixes col 0 to
                           LABEL_COL_WIDTH_PT so the label column is snug to
                           its words and the content column gets the rest of
                           the page.
    Pass 5: Lead-word    — Content-agnostic auto-bolder. Detects three lead
        bolding            patterns in every paragraph (body + table cells)
                           and re-applies bold + weight=700 to the lead range,
                           overriding any pass-2/pass-4 weight=400 that
                           visually stripped the bold:
                           (a) RACI bullets — "Responsible:" / "Accountable:" /
                               "Consulted:" / "Informed:" → bold through colon
                           (b) Hypothesis bullets — "H1 — Mixed households:"
                               → bold through colon
                           (c) Em-dash lead — "Low recall — Personal Planogram
                               hits..." → bold the lead before " — "
                           Idempotent. Safe to re-run.

Never deletes or inserts text — only styles.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Reuse the doc-styling-3 helpers (gws wrappers, request builders).
HELPERS_DIR = Path.home() / ".claude" / "skills" / "jedi-doc-styling-3" / "scripts"
sys.path.insert(0, str(HELPERS_DIR))

from _helpers import (  # type: ignore  # noqa: E402
    gws_get, gws_batch_update,
    iter_body_content,
    find_paragraphs_by_named_style, find_first_paragraph, find_tables,
    find_subscript_runs, paragraph_text, is_list_paragraph,
    mk_range, mk_location,
    font_run_style, color_bg, clear_baseline,
    update_text_style, update_paragraph_style, update_document_style,
    update_table_cell_style, update_table_column_properties, cell_style_full,
)


# ---------------------------------------------------------------------------
# Pass 5 — Lead-word bolding (content-agnostic auto-bold)
# ---------------------------------------------------------------------------

# RACI bullet — "Responsible:" / "Accountable:" / "Consulted:" / "Informed:"
# Bold through the colon (so the trailing colon stays bold for visual anchor).
RACI_LEAD_RE = re.compile(r"^(Responsible|Accountable|Consulted|Informed):")

# Hypothesis bullet — "H1 — Mixed households:" or "H2 — Aspirational diets:"
# Em-dash OR hyphen tolerated; bold through the colon.
HYPO_LEAD_RE = re.compile(r"^(H\d+\s*[—\-]\s*[^:\n]{1,80}):")

# Em-dash lead bullet — "Low recall — Personal Planogram hits...". Lead phrase
# must start with a capital letter or digit, must NOT contain em-dash or colon
# before the " — " separator. Length cap = 60 chars to avoid eating sentences.
EM_DASH_LEAD_RE = re.compile(r"^([A-Z0-9][^—:\n]{1,60}?)\s+—\s")


# ---------------------------------------------------------------------------
# Palette (from SKILL.md § 1)
# ---------------------------------------------------------------------------

def _hex(h: str) -> dict:
    h = h.lstrip("#")
    return {
        "red":   int(h[0:2], 16) / 255.0,
        "green": int(h[2:4], 16) / 255.0,
        "blue":  int(h[4:6], 16) / 255.0,
    }


class Palette:
    NAV    = _hex("1F4E79")
    BLUE   = _hex("2E74B5")
    LBLUE  = _hex("D6E4F0")
    WHITE  = _hex("FFFFFF")
    LGRAY  = _hex("F5F5F5")
    DGRAY  = _hex("D0D0D0")
    MGRAY  = _hex("737373")
    BLACK  = _hex("000000")


FONT_BODY = "Calibri"

# Page geometry (matches pass1 margins). US Letter = 612pt wide; margins = 45pt
# each side → 522pt of content width. 2-col tables get a fixed narrow label
# column (~14 chars of Calibri 10pt bold) + remaining width on the content col.
PAGE_WIDTH_PT = 612.0
MARGIN_PT = 45.0
CONTENT_WIDTH_PT = PAGE_WIDTH_PT - 2 * MARGIN_PT  # 522
LABEL_COL_WIDTH_PT = 130.0
DATA_COL_WIDTH_PT = CONTENT_WIDTH_PT - LABEL_COL_WIDTH_PT  # 392


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_doc_id(arg: str) -> str:
    m = re.search(r"/document/d/([a-zA-Z0-9_-]+)", arg)
    return m.group(1) if m else arg


# ---------------------------------------------------------------------------
# Pass 0 — sanitize baseline offsets
# ---------------------------------------------------------------------------

def pass0_sanitize(doc_id: str) -> None:
    doc = gws_get(doc_id)
    runs = find_subscript_runs(doc)
    if not runs:
        print("[pass0] no SUBSCRIPT/SUPERSCRIPT artifacts found")
        return
    style, fields = clear_baseline()
    reqs = [update_text_style(s, e, style, fields) for (s, e) in runs]
    gws_batch_update(doc_id, reqs, label="pass0-sanitize")


# ---------------------------------------------------------------------------
# Pass 1 — document margins
# ---------------------------------------------------------------------------

def pass1_document(doc_id: str) -> None:
    # 45pt ~ 0.625" — matches docx skill (900 DXA all sides)
    margins = {
        "marginTop": 45, "marginBottom": 45,
        "marginLeft": 45, "marginRight": 45,
    }
    req = update_document_style(margins)
    gws_batch_update(doc_id, [req], label="pass1-document")


# ---------------------------------------------------------------------------
# Pass 2 — named styles (typography)
# ---------------------------------------------------------------------------

def _para_with_spacing(space_before: float, space_after: float,
                       line_spacing_pct: float = 115,
                       alignment: str | None = None) -> tuple[dict, str]:
    style: dict = {
        "spaceAbove":  {"magnitude": space_before, "unit": "PT"},
        "spaceBelow":  {"magnitude": space_after,  "unit": "PT"},
        "lineSpacing": line_spacing_pct,
    }
    fields = ["spaceAbove", "spaceBelow", "lineSpacing"]
    if alignment:
        style["alignment"] = alignment
        fields.append("alignment")
    return style, ",".join(fields)


def pass2_named_styles(doc_id: str) -> None:
    doc = gws_get(doc_id)
    reqs: list[dict] = []

    # NORMAL_TEXT body — Calibri 10pt black. bold=None preserves inline bold
    # runs (the lead-word pattern: "**Low recall** — ..." stays bold).
    body_text, body_fields = font_run_style(FONT_BODY, 10.0,
                                            color=Palette.BLACK)
    body_para, body_pfields = _para_with_spacing(2, 4, 115)
    for s, e, _ in find_paragraphs_by_named_style(doc, "NORMAL_TEXT"):
        reqs.append(update_text_style(s, e, body_text, body_fields))
        reqs.append(update_paragraph_style(s, e, body_para, body_pfields))

    # TITLE — Calibri 36pt bold NAV
    title_text, title_fields = font_run_style(FONT_BODY, 36.0, bold=True,
                                              color=Palette.NAV, weight=700)
    title_para, title_pfields = _para_with_spacing(0, 6, 110)
    for s, e, _ in find_paragraphs_by_named_style(doc, "TITLE"):
        reqs.append(update_text_style(s, e, title_text, title_fields))
        reqs.append(update_paragraph_style(s, e, title_para, title_pfields))

    # H1 — Calibri 18pt bold NAV (dark blue text only, no background block).
    # Changed from WHITE-on-NAV in v1.2.0 per researcher feedback.
    h1_text, h1_fields = font_run_style(FONT_BODY, 18.0, bold=True,
                                        color=Palette.NAV, weight=700)
    h1_para, h1_pfields = _para_with_spacing(14, 8, 115)
    for s, e, _ in find_paragraphs_by_named_style(doc, "HEADING_1"):
        reqs.append(update_text_style(s, e, h1_text, h1_fields))
        reqs.append(update_paragraph_style(s, e, h1_para, h1_pfields))

    # H2 — Calibri 14pt bold BLUE
    h2_text, h2_fields = font_run_style(FONT_BODY, 14.0, bold=True,
                                        color=Palette.BLUE, weight=700)
    h2_para, h2_pfields = _para_with_spacing(10, 4, 115)
    for s, e, _ in find_paragraphs_by_named_style(doc, "HEADING_2"):
        reqs.append(update_text_style(s, e, h2_text, h2_fields))
        reqs.append(update_paragraph_style(s, e, h2_para, h2_pfields))

    # H3 — Calibri 11pt bold NAV
    h3_text, h3_fields = font_run_style(FONT_BODY, 11.0, bold=True,
                                        color=Palette.NAV, weight=700)
    h3_para, h3_pfields = _para_with_spacing(8, 3, 115)
    for s, e, _ in find_paragraphs_by_named_style(doc, "HEADING_3"):
        reqs.append(update_text_style(s, e, h3_text, h3_fields))
        reqs.append(update_paragraph_style(s, e, h3_para, h3_pfields))

    # H4–H6 — degrade gracefully to bold NAV
    for hstyle, size in (("HEADING_4", 10.5), ("HEADING_5", 10.0),
                         ("HEADING_6", 10.0)):
        ht, hf = font_run_style(FONT_BODY, size, bold=True,
                                color=Palette.NAV, weight=700)
        hp, hpf = _para_with_spacing(6, 2, 115)
        for s, e, _ in find_paragraphs_by_named_style(doc, hstyle):
            reqs.append(update_text_style(s, e, ht, hf))
            reqs.append(update_paragraph_style(s, e, hp, hpf))

    # SUBTITLE (if present) — Calibri 16pt bold BLUE
    sub_text, sub_fields = font_run_style(FONT_BODY, 16.0, bold=True,
                                          color=Palette.BLUE, weight=700)
    sub_para, sub_pfields = _para_with_spacing(4, 8, 115)
    for s, e, _ in find_paragraphs_by_named_style(doc, "SUBTITLE"):
        reqs.append(update_text_style(s, e, sub_text, sub_fields))
        reqs.append(update_paragraph_style(s, e, sub_para, sub_pfields))

    gws_batch_update(doc_id, reqs, label="pass2-named-styles")


# ---------------------------------------------------------------------------
# Pass 3 — H1 nav bars (NAV shading + WHITE text)
# ---------------------------------------------------------------------------

def pass3_h1_cleanup(doc_id: str) -> None:
    """Clear any prior NAV background block on H1s and re-assert NAV text.

    v1.0.0–1.1.0 painted full-width nav bars (WHITE text on NAV background)
    on every H1. v1.2.0 reverts to dark-blue text only. Idempotent: re-running
    on a doc previously styled with nav bars clears the block."""
    doc = gws_get(doc_id)
    reqs: list[dict] = []
    # Set shading explicitly to WHITE to clear any prior NAV fill
    # (Docs API treats `{}` as black — must set explicit WHITE; per
    # reference_docs_api_clear_color_gotcha.md).
    clear_style = {
        "shading":     {"backgroundColor": {"color": {"rgbColor": Palette.WHITE}}},
        "indentStart": {"magnitude": 0, "unit": "PT"},
        "indentEnd":   {"magnitude": 0, "unit": "PT"},
        "spaceAbove":  {"magnitude": 14, "unit": "PT"},
        "spaceBelow":  {"magnitude": 8,  "unit": "PT"},
    }
    fields = "shading,indentStart,indentEnd,spaceAbove,spaceBelow"
    for s, e, _ in find_paragraphs_by_named_style(doc, "HEADING_1"):
        reqs.append(update_paragraph_style(s, e, clear_style, fields))
        # Re-assert NAV text in case prior pass left it WHITE
        text_style, tfields = font_run_style(FONT_BODY, 18.0, bold=True,
                                             color=Palette.NAV, weight=700)
        reqs.append(update_text_style(s, e, text_style, tfields))
    gws_batch_update(doc_id, reqs, label="pass3-h1-cleanup")


# ---------------------------------------------------------------------------
# Pass 4 — Tables (2-col label/content pattern + alternating rows)
# ---------------------------------------------------------------------------

def _table_text_style_for_cell(*, bold: bool | None, color: dict,
                                size: float = 10.0) -> tuple[dict, str]:
    """bold=True for label/header cells; bold=None for data cells (preserves
    inline lead-word bolding inside cell content)."""
    return font_run_style(FONT_BODY, size, bold=bold, color=color,
                          weight=700 if bold else 400)


def _cell_text_range(table: dict, row_idx: int, col_idx: int) -> list[tuple[int, int]]:
    cell = table["tableRows"][row_idx]["tableCells"][col_idx]
    ranges: list[tuple[int, int]] = []
    for content in cell.get("content", []):
        if "paragraph" in content:
            ranges.append((content["startIndex"], content["endIndex"]))
    return ranges


def pass4_tables(doc_id: str) -> None:
    doc = gws_get(doc_id)
    reqs: list[dict] = []

    for table_info in find_tables(doc):
        table_start = table_info["startIndex"]
        rows = table_info["rows"]
        cols = table_info["cols"]
        table = table_info["table"]

        # Detect "header row" — first row of multi-row tables OR any table
        # with a clearly different first row (we always treat first row as
        # header for consistency).
        has_header_row = rows > 1

        # Detect "2-col label/content" — exactly 2 columns
        is_two_col = cols == 2

        # For 2-col tables, fix column widths: narrow label col + wide data col.
        # Set data col first so the label col change doesn't trigger Google
        # Docs' auto-redistribution.
        if is_two_col:
            reqs.append(update_table_column_properties(
                table_start, [1], width_pt=DATA_COL_WIDTH_PT,
                width_type="FIXED_WIDTH",
            ))
            reqs.append(update_table_column_properties(
                table_start, [0], width_pt=LABEL_COL_WIDTH_PT,
                width_type="FIXED_WIDTH",
            ))

        for r in range(rows):
            for c in range(cols):
                # Decide cell fill
                if has_header_row and r == 0:
                    fill = Palette.NAV
                    text_color = Palette.WHITE
                    is_bold = True
                elif is_two_col and c == 0:
                    fill = Palette.LBLUE
                    text_color = Palette.NAV
                    is_bold = True
                else:
                    fill = Palette.WHITE if (r % 2 == 0) else Palette.LGRAY
                    text_color = Palette.BLACK
                    is_bold = None  # preserve inline lead-word bold in data cells

                cell_style, cell_fields = cell_style_full(
                    bg_color=fill,
                    padding_pt=5,
                    border_color=Palette.DGRAY,
                    border_width_pt=0.5,
                    content_alignment="TOP",
                )
                reqs.append(update_table_cell_style(
                    table_start, r, c, cell_style, cell_fields,
                ))

                # Re-style every text run inside the cell
                text_style, text_fields = _table_text_style_for_cell(
                    bold=is_bold, color=text_color, size=10.0,
                )
                for s, e in _cell_text_range(table, r, c):
                    if e > s:
                        reqs.append(update_text_style(s, e, text_style, text_fields))

    gws_batch_update(doc_id, reqs, label="pass4-tables")


# ---------------------------------------------------------------------------
# Pass 5 — Lead-word bolding
# ---------------------------------------------------------------------------

def _first_text_run_start(para: dict) -> int | None:
    """startIndex of the first textRun in this paragraph (where text begins,
    *after* any bullet glyph)."""
    for run in para.get("elements", []):
        if "textRun" in run:
            return run["startIndex"]
    return None


def _bold_range_for_paragraph(para: dict) -> tuple[int, int] | None:
    """Inspect paragraph text. If it matches a lead-word pattern, return the
    absolute (start, end) range in the document to bold. Otherwise None."""
    start = _first_text_run_start(para)
    if start is None:
        return None
    text = paragraph_text(para)
    if not text:
        return None
    # Strip leading whitespace and adjust start offset (rare but defensive).
    stripped = text.lstrip()
    leading_ws = len(text) - len(stripped)
    base = start + leading_ws

    # Check RACI first (most specific), then Hypothesis, then em-dash lead.
    for pattern, include_colon in (
        (RACI_LEAD_RE, True),
        (HYPO_LEAD_RE, True),
        (EM_DASH_LEAD_RE, False),
    ):
        m = pattern.match(stripped)
        if m:
            end_offset = m.end(0) if include_colon else m.end(1)
            return (base, base + end_offset)
    return None


def pass5_lead_word_bolding(doc_id: str) -> None:
    """Walk every paragraph (body + table cells), regex-detect lead-word
    patterns, and re-apply bold + weight=700 to the lead range.

    Why this exists: pass 2 applies `weightedFontFamily.weight=400` across
    NORMAL_TEXT paragraphs, which visually strips inline `**bold**` runs
    even though the structural runs survive. Pass 5 is the safety net —
    it enforces the lead-word bold rule from the markdown structure (the
    runs are split correctly; only the weight needs to be re-asserted)."""
    doc = gws_get(doc_id)
    reqs: list[dict] = []

    def visit_paragraph(para: dict) -> None:
        r = _bold_range_for_paragraph(para)
        if r is None:
            return
        start, end = r
        if end <= start:
            return
        # Re-assert both `bold=True` AND `weightedFontFamily.weight=700`
        # so the bold survives even if some downstream tool re-reads weight.
        style = {
            "bold": True,
            "weightedFontFamily": {"fontFamily": FONT_BODY, "weight": 700},
        }
        fields = "bold,weightedFontFamily"
        reqs.append(update_text_style(start, end, style, fields))

    for el in iter_body_content(doc):
        if "paragraph" in el:
            visit_paragraph(el["paragraph"])
        elif "table" in el:
            for row in el["table"].get("tableRows", []):
                for cell in row.get("tableCells", []):
                    for content in cell.get("content", []):
                        if "paragraph" in content:
                            visit_paragraph(content["paragraph"])

    if not reqs:
        print("[pass5] no lead-word patterns detected")
        return
    gws_batch_update(doc_id, reqs, label=f"pass5-lead-bold ({len(reqs)} ranges)")


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

VERSION = "1.3.0"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    doc_id = parse_doc_id(argv[1])
    print(f"=== Jedida Reporting Google Docs styler (v{VERSION}) ===")
    print(f"Doc:  {doc_id}\n")

    pass0_sanitize(doc_id)
    pass1_document(doc_id)
    pass2_named_styles(doc_id)
    pass3_h1_cleanup(doc_id)
    pass4_tables(doc_id)
    pass5_lead_word_bolding(doc_id)

    print(f"\nDONE. Open: https://docs.google.com/document/d/{doc_id}/edit")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
