#!/usr/bin/env python3
"""Op-builders for the Instacart Green analysis-deliverable style.

Emits operations for the connected `batch_update_doc` MCP tool (NOT native
Google Docs API requests). Import these helpers and call them with the indices
you read from `inspect_doc_structure` (paragraphs) and `debug_table_structure`
(table cells), then pass the collected `OPS` list to batch_update_doc.

Cell text range convention: for a cell whose debug range is [s, e],
format its text with start=s+1 (== insertion_index) and end=e-1.

Why the funny line_spacing: the batch_update_doc tool multiplies `line_spacing`
by 100 to get the Google Docs API percentage. Pass 1 for single spacing.
Passing 100 stores 10000 (=100x) and turns a section band into a giant block.

See ../references/instacart-green-analysis-style.md for the full contract.
Stdlib only. No live API calls — everything returns/prints JSON.
"""
from __future__ import annotations

import json
import sys

# --- Palette (from anthropic-skills:instacart-brand) ---
KALE = "#003D29"; LIME = "#0AAD0A"; CARROT = "#FF7009"; CASHEW = "#FAF1E5"
POMEGRANATE = "#BA0239"; OCHRE = "#B45F06"; WHITE = "#FFFFFF"; BLACK = "#000000"
QUOTE = "#333333"; GRAY = "#666666"; SANS = "DM Sans"
TURMERIC = "#ECAA01"  # RETIRED 2026-09-28 (old "Bottom line" callout) — do not use by default
DEFAULT_TAB_ID = "t.0"
TAB = DEFAULT_TAB_ID  # Backward-compatible default; pass tab_id for non-default tabs.

PRIORITY_COLORS = {
    "P0": POMEGRANATE,
    "P1": CARROT,
    "P2": GRAY,
    "GUARDRAIL": KALE,
}

OPS: list[dict] = []

def _tab(tab_id):
    return TAB if tab_id is None else tab_id


def normal_line_spacing(backend="custom_mcp"):
    """Return normal single spacing in the selected adapter's units.

    The custom MCP accepts a multiplier (1 == single spacing). The raw Google
    Docs API accepts a percentage (100 == single spacing).
    """
    values = {"custom_mcp": 1, "docs_api": 100}
    try:
        return values[backend]
    except KeyError as exc:
        raise ValueError("backend must be 'custom_mcp' or 'docs_api'") from exc


def priority_color(level):
    """Return the house-style color for P0/P1/P2/Guardrail."""
    normalized = str(level).strip().upper()
    try:
        return PRIORITY_COLORS[normalized]
    except KeyError as exc:
        allowed = ", ".join(PRIORITY_COLORS)
        raise ValueError(f"unknown priority {level!r}; expected one of {allowed}") from exc


def _ft(s, e, *, tab_id=None, **k):
    OPS.append({"type": "format_text", "start_index": s, "end_index": e, "tab_id": _tab(tab_id), **k})


def _ps(s, e, *, tab_id=None, **k):
    OPS.append({"type": "update_paragraph_style", "start_index": s, "end_index": e, "tab_id": _tab(tab_id), **k})


def _cell(tsi, r, c, bg, *, tab_id=None):
    OPS.append({"type": "update_table_cell_style", "table_start_index": tsi, "row_index": r, "column_index": c, "row_span": 1, "column_span": 1, "background_color": bg, "tab_id": _tab(tab_id)})


def _colw(tsi, cols, w, *, tab_id=None):
    OPS.append({"type": "update_table_column_properties", "table_start_index": tsi, "column_indices": cols, "width": w, "width_type": "FIXED_WIDTH", "tab_id": _tab(tab_id)})

# --- Building blocks. (s, e) = paragraph start/end from inspect; te = e-1 (text, no newline). ---

def base_font(doc_start=1, doc_end=None, *, tab_id=None):
    """Set DM Sans 10 black over the whole body first; overrides come after."""
    _ft(doc_start, doc_end, tab_id=tab_id, font_family=SANS, font_size=10, text_color=BLACK)

def masthead(breadcrumb, title, subtitle=None, author=None, *, tab_id=None):
    """Each arg is (s, e) of that paragraph (author line accepts None)."""
    s, e = breadcrumb; _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=8, italic=True, text_color=KALE)
    s, e = title;      _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=18, bold=True, text_color=KALE)
    if subtitle: s, e = subtitle; _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=10, text_color=KALE)
    if author:   s, e = author;   _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=12, bold=True, text_color=LIME)

def band(s, e, *, tab_id=None):
    """Thin Kale section band for a HEADING_2 paragraph. line_spacing=1 is load-bearing."""
    _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=12, bold=True, text_color=WHITE)
    _ps(s, e, tab_id=tab_id, shading_color=KALE, line_spacing=normal_line_spacing("custom_mcp"), space_above=0, space_below=0)

def table_header(table_start_index, header_text_ranges, *, tab_id=None):
    """header_text_ranges: list of (text_start, text_end) for each header cell (== [s+1, e-1])."""
    for c in range(len(header_text_ranges)): _cell(table_start_index, 0, c, CASHEW, tab_id=tab_id)
    for s, e in header_text_ranges: _ft(s, e, tab_id=tab_id, font_family=SANS, font_size=10, bold=True, text_color=KALE)

def column_widths(table_start_index, widths, *, tab_id=None):
    """widths: list of pt per column, in order (should sum to ~468 for portrait letter)."""
    for i, w in enumerate(widths): _colw(table_start_index, [i], w, tab_id=tab_id)

def status(text_start, text_end, positive=True, *, tab_id=None):
    _ft(text_start, text_end, tab_id=tab_id, bold=True, text_color=(LIME if positive else POMEGRANATE))

def priority(text_start, text_end, level, *, tab_id=None):
    _ft(text_start, text_end, tab_id=tab_id, bold=True, text_color=priority_color(level))

def finding_subheading(s, e, *, tab_id=None):
    """A finding's ### sub-heading: Kale bold 13, NOT shaded, white space above."""
    _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=13, bold=True, text_color=KALE)
    _ps(s, e, tab_id=tab_id, space_above=10, space_below=2)

def finding_label(text_start, label_len, *, tab_id=None):
    """Format an Ochre finding run-in label (for example Analysis or Confidence).

    Pass the exact label length without the following separator.
    """
    _ft(text_start, text_start + label_len, tab_id=tab_id, bold=True, text_color=OCHRE)

def quote_body(text_start, text_end, *, tab_id=None):
    """Italic #333 for the verbatim quote text after 'Quote — '."""
    _ft(text_start, text_end, tab_id=tab_id, italic=True, text_color=QUOTE)

def evidence_line(label_range, quote_range, tone="pos", *, tab_id=None):
    """LEGACY (pre-v2 '›' evidence lines). tone: 'pos'->Lime, 'caution'->Carrot, 'neg'->Pomegranate."""
    color = {"pos": LIME, "caution": CARROT, "neg": POMEGRANATE}[tone]
    ls, le = label_range; _ft(ls, le, tab_id=tab_id, bold=True, text_color=color)
    qs, qe = quote_range; _ft(qs, qe, tab_id=tab_id, italic=True, text_color=QUOTE)

def appendix_label(text_start, text_end, *, tab_id=None):
    _ft(text_start, text_end, tab_id=tab_id, bold=True, text_color=KALE)

def footer(s, e, *, tab_id=None):
    _ft(s, e - 1, tab_id=tab_id, font_family=SANS, font_size=9, italic=True, text_color=KALE)

def dump():
    print(json.dumps(OPS, ensure_ascii=False))

if __name__ == "__main__":
    sys.stderr.write(
        "This is a helper library, not a turnkey CLI. Import it, call the builders with\n"
        "indices from inspect_doc_structure + debug_table_structure, then `dump()` the OPS\n"
        "list into batch_update_doc. See ../references/instacart-green-analysis-style.md.\n"
    )
