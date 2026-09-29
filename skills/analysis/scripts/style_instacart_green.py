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
import json, sys

# --- Palette (from anthropic-skills:instacart-brand) ---
KALE = "#003D29"; LIME = "#0AAD0A"; CARROT = "#FF7009"; CASHEW = "#FAF1E5"
POMEGRANATE = "#BA0239"; OCHRE = "#B45F06"; WHITE = "#FFFFFF"; BLACK = "#000000"
QUOTE = "#333333"; SANS = "DM Sans"
TURMERIC = "#ECAA01"  # RETIRED 2026-09-28 (old "Bottom line" callout) — do not use by default
TAB = "t.0"

OPS: list[dict] = []

def _ft(s, e, **k): OPS.append({"type": "format_text", "start_index": s, "end_index": e, "tab_id": TAB, **k})
def _ps(s, e, **k): OPS.append({"type": "update_paragraph_style", "start_index": s, "end_index": e, "tab_id": TAB, **k})
def _cell(tsi, r, c, bg): OPS.append({"type": "update_table_cell_style", "table_start_index": tsi, "row_index": r, "column_index": c, "row_span": 1, "column_span": 1, "background_color": bg, "tab_id": TAB})
def _colw(tsi, cols, w): OPS.append({"type": "update_table_column_properties", "table_start_index": tsi, "column_indices": cols, "width": w, "width_type": "FIXED_WIDTH", "tab_id": TAB})

# --- Building blocks. (s, e) = paragraph start/end from inspect; te = e-1 (text, no newline). ---

def base_font(doc_start=1, doc_end=None):
    """Set DM Sans 10 black over the whole body first; overrides come after."""
    _ft(doc_start, doc_end, font_family=SANS, font_size=10, text_color=BLACK)

def masthead(breadcrumb, title, subtitle=None, author=None):
    """Each arg is (s, e) of that paragraph (author line accepts None)."""
    s, e = breadcrumb; _ft(s, e - 1, font_family=SANS, font_size=8, italic=True, text_color=KALE)
    s, e = title;      _ft(s, e - 1, font_family=SANS, font_size=18, bold=True, text_color=KALE)
    if subtitle: s, e = subtitle; _ft(s, e - 1, font_family=SANS, font_size=10, text_color=KALE)
    if author:   s, e = author;   _ft(s, e - 1, font_family=SANS, font_size=12, bold=True, text_color=LIME)

def band(s, e):
    """Thin Kale section band for a HEADING_2 paragraph. line_spacing=1 is load-bearing."""
    _ft(s, e - 1, font_family=SANS, font_size=12, bold=True, text_color=WHITE)
    _ps(s, e, shading_color=KALE, line_spacing=1, space_above=0, space_below=0)

def table_header(table_start_index, header_text_ranges):
    """header_text_ranges: list of (text_start, text_end) for each header cell (== [s+1, e-1])."""
    for c in range(len(header_text_ranges)): _cell(table_start_index, 0, c, CASHEW)
    for s, e in header_text_ranges: _ft(s, e, font_family=SANS, font_size=10, bold=True, text_color=KALE)

def column_widths(table_start_index, widths):
    """widths: list of pt per column, in order (should sum to ~468 for portrait letter)."""
    for i, w in enumerate(widths): _colw(table_start_index, [i], w)

def status(text_start, text_end, positive=True):
    _ft(text_start, text_end, bold=True, text_color=(LIME if positive else POMEGRANATE))

def priority(text_start, text_end, level):
    _ft(text_start, text_end, bold=True, text_color=(POMEGRANATE if str(level).upper() == "P0" else CARROT))

def finding_subheading(s, e):
    """A finding's ### sub-heading: Kale bold 13, NOT shaded, white space above."""
    _ft(s, e - 1, font_family=SANS, font_size=13, bold=True, text_color=KALE)
    _ps(s, e, space_above=10, space_below=2)

def finding_label(text_start, label_len):
    """The Ochre run-in label at the start of an Analysis/Recommendation/Quote line.
    label_len = len('Analysis')=8 / len('Recommendation')=14 / len('Quote')=5."""
    _ft(text_start, text_start + label_len, bold=True, text_color=OCHRE)

def quote_body(text_start, text_end):
    """Italic #333 for the verbatim quote text after 'Quote — '."""
    _ft(text_start, text_end, italic=True, text_color=QUOTE)

def evidence_line(label_range, quote_range, tone="pos"):
    """LEGACY (pre-v2 '›' evidence lines). tone: 'pos'->Lime, 'caution'->Carrot, 'neg'->Pomegranate."""
    color = {"pos": LIME, "caution": CARROT, "neg": POMEGRANATE}[tone]
    ls, le = label_range; _ft(ls, le, bold=True, text_color=color)
    qs, qe = quote_range; _ft(qs, qe, italic=True, text_color=QUOTE)

def appendix_label(text_start, text_end):
    _ft(text_start, text_end, bold=True, text_color=KALE)

def footer(s, e):
    _ft(s, e - 1, font_family=SANS, font_size=9, italic=True, text_color=KALE)

def dump():
    print(json.dumps(OPS, ensure_ascii=False))

if __name__ == "__main__":
    sys.stderr.write(
        "This is a helper library, not a turnkey CLI. Import it, call the builders with\n"
        "indices from inspect_doc_structure + debug_table_structure, then `dump()` the OPS\n"
        "list into batch_update_doc. See ../references/instacart-green-analysis-style.md.\n"
    )
