"""
mod-guide skill — Default canonical-template styler.

Applies Jedida's locked mod-guide template spec to a Google Doc. The spec is
extracted from reference doc `18Q9V4th9BwwNtlLXSncmMpiN591XTV1RzCUAyxym7wI`
and documented in `references/canonical-template-spec.md`.

Phases (in order):
  1. Strip baselineOffset=SUBSCRIPT on every run (md2doc <br> artifact)
  2. Page setup (612 x 792 pt, 72pt margins all sides)
  3. Run-level typography (headings, body, breadcrumb, "Last updated")
  4. HEADING_2 paragraph style (non-bold, 36pt above / 12pt below, 110% line)
  5. NORMAL_TEXT paragraph spaceBelow = 4pt
  6. Table styling — col widths 96 / 715.5 pt, header bg #2D4A3E + white bold,
     body label col bold dark green, body content col #161416, 0.5pt #C7C7C7
     borders, 8pt padding all sides, contentAlignment=TOP
  7. Bullet glyphs — BULLET_DISC_CIRCLE_SQUARE on every bulleted paragraph

Usage:
    uv run --python 3.12 \\
        --with google-api-python-client --with google-auth \\
        --with google-auth-oauthlib --with google-auth-httplib2 \\
        --with requests --with python-dotenv --with markdown --with pillow \\
        ~/.claude/skills/mod-guide/scripts/apply_canonical_template.py <DOC_ID>
"""

import sys

sys.path.insert(0, '/Users/jedidamilton/.claude/plugins/cache/instacart/md2doc/893dc15bd620/skills/md2doc/scripts')
import _env  # noqa: F401
from common.drive import get_docs_service

if len(sys.argv) < 2:
    print("Usage: apply_canonical_template.py <DOC_ID>", file=sys.stderr)
    sys.exit(1)

DOC_ID = sys.argv[1]

# ---------------------------------------------------------------------------
# Canonical spec values (mirrors references/canonical-template-spec.md)
# ---------------------------------------------------------------------------

GREEN = "#2D4A3E"
BLACK_BODY = "#161416"
GRAY_MUTED = "#666666"
GRAY_BORDER = "#C7C7C7"
WHITE = "#FFFFFF"

DM_SANS = "DM Sans"
DM_SERIF = "DM Serif Display"

PAGE_WIDTH_PT = 612
PAGE_HEIGHT_PT = 792
MARGIN_PT = 72

COL0_WIDTH_PT = 96
COL1_WIDTH_PT = 715.5

BORDER_WIDTH_PT = 0.5
CELL_PADDING_PT = 8

NORMAL_TEXT_SPACE_BELOW_PT = 4
H2_SPACE_ABOVE_PT = 36
H2_SPACE_BELOW_PT = 12
H2_LINE_SPACING = 110
NORMAL_LINE_SPACING = 115

BATCH_SIZE = 200


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

docs = get_docs_service()


def hex_to_rgb_color(hex_str):
    h = hex_str.lstrip("#")
    return {
        "color": {
            "rgbColor": {
                "red": int(h[0:2], 16) / 255.0,
                "green": int(h[2:4], 16) / 255.0,
                "blue": int(h[4:6], 16) / 255.0,
            }
        }
    }


def batch_update(reqs, label=""):
    if not reqs:
        return
    for i in range(0, len(reqs), BATCH_SIZE):
        chunk = reqs[i:i + BATCH_SIZE]
        docs.documents().batchUpdate(documentId=DOC_ID, body={"requests": chunk}).execute()
        print(f"  [{label}] applied {len(chunk)} reqs (chunk {i // BATCH_SIZE + 1})")


def fetch():
    return docs.documents().get(documentId=DOC_ID).execute()


def text_run_style_request(start, end, font=None, size=None, bold=None,
                           italic=None, fg=None, bg=None,
                           baseline_offset=None):
    text_style = {}
    fields = []
    if font is not None:
        text_style["weightedFontFamily"] = {"fontFamily": font}
        fields.append("weightedFontFamily")
    if size is not None:
        text_style["fontSize"] = {"magnitude": size, "unit": "PT"}
        fields.append("fontSize")
    if bold is not None:
        text_style["bold"] = bold
        fields.append("bold")
    if italic is not None:
        text_style["italic"] = italic
        fields.append("italic")
    if fg is not None:
        text_style["foregroundColor"] = hex_to_rgb_color(fg)
        fields.append("foregroundColor")
    if bg is not None:
        text_style["backgroundColor"] = hex_to_rgb_color(bg)
        fields.append("backgroundColor")
    if baseline_offset is not None:
        text_style["baselineOffset"] = baseline_offset
        fields.append("baselineOffset")
    return {
        "updateTextStyle": {
            "range": {"startIndex": start, "endIndex": end},
            "textStyle": text_style,
            "fields": ",".join(fields),
        }
    }


def collect_paragraph_runs(doc):
    out = []

    def walk(elements, in_table=False, in_table_col=None):
        for el in elements:
            if "paragraph" in el:
                p = el["paragraph"]
                nst = p.get("paragraphStyle", {}).get("namedStyleType")
                for re_ in p.get("elements", []):
                    if "textRun" in re_:
                        out.append({
                            "nst": nst,
                            "start": re_["startIndex"],
                            "end": re_["endIndex"],
                            "text": re_["textRun"].get("content", ""),
                            "in_table": in_table,
                            "table_col": in_table_col,
                            "baseline_offset": re_["textRun"].get("textStyle", {}).get("baselineOffset"),
                        })
            if "table" in el:
                for row in el["table"].get("tableRows", []):
                    for ci, cell in enumerate(row.get("tableCells", [])):
                        walk(cell.get("content", []), in_table=True, in_table_col=ci)

    walk(doc.get("body", {}).get("content", []))
    return out


def find_top_level_tables(doc):
    out = []
    for el in doc.get("body", {}).get("content", []):
        if "table" in el:
            out.append({
                "startIndex": el["startIndex"],
                "endIndex": el["endIndex"],
                "table": el["table"],
            })
    return out


# ---------------------------------------------------------------------------
# PHASE 1 — Strip SUBSCRIPT baseline offset (the smoking gun)
# ---------------------------------------------------------------------------
print("=" * 80)
print("PHASE 1: Clear baselineOffset=SUBSCRIPT")
print("=" * 80)

doc = fetch()
runs = collect_paragraph_runs(doc)
sub_reqs = []
for r in runs:
    if r["baseline_offset"] == "SUBSCRIPT":
        sub_reqs.append({
            "updateTextStyle": {
                "range": {"startIndex": r["start"], "endIndex": r["end"]},
                "textStyle": {"baselineOffset": "NONE"},
                "fields": "baselineOffset",
            }
        })
print(f"Found {len(sub_reqs)} SUBSCRIPT runs")
batch_update(sub_reqs, "subscript-clear")


# ---------------------------------------------------------------------------
# PHASE 2 — Page setup (size + margins)
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 2: Page setup")
print("=" * 80)

page_reqs = [{
    "updateDocumentStyle": {
        "documentStyle": {
            "pageSize": {
                "width": {"magnitude": PAGE_WIDTH_PT, "unit": "PT"},
                "height": {"magnitude": PAGE_HEIGHT_PT, "unit": "PT"},
            },
            "marginTop": {"magnitude": MARGIN_PT, "unit": "PT"},
            "marginBottom": {"magnitude": MARGIN_PT, "unit": "PT"},
            "marginLeft": {"magnitude": MARGIN_PT, "unit": "PT"},
            "marginRight": {"magnitude": MARGIN_PT, "unit": "PT"},
        },
        "fields": "pageSize,marginTop,marginBottom,marginLeft,marginRight",
    }
}]
batch_update(page_reqs, "page-setup")


# ---------------------------------------------------------------------------
# PHASE 3 — Run-level typography (headings, body, breadcrumb, last-updated)
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 3: Run-level typography")
print("=" * 80)

doc = fetch()
runs = collect_paragraph_runs(doc)
print(f"Total runs: {len(runs)}")

reqs = []
first_normal_done = False
for r in runs:
    nst = r["nst"]
    text = r["text"]
    s, e = r["start"], r["end"]
    if not text.strip():
        continue

    if nst in ("HEADING_1", "TITLE"):
        reqs.append(text_run_style_request(s, e, font=DM_SERIF, size=26, bold=True, fg=GREEN))
    elif nst == "HEADING_2":
        # Non-bold per the locked spec; paragraph-style bump in Phase 4
        reqs.append(text_run_style_request(s, e, font=DM_SERIF, size=16, bold=False, fg=GREEN))
    elif nst == "HEADING_3":
        reqs.append(text_run_style_request(s, e, font=DM_SERIF, size=14, bold=True, fg=GREEN))
    elif nst == "HEADING_4":
        reqs.append(text_run_style_request(s, e, font=DM_SERIF, size=12, bold=True, fg=GREEN))
    elif nst in ("HEADING_5", "HEADING_6"):
        reqs.append(text_run_style_request(s, e, font=DM_SERIF, size=11, bold=True, fg=GREEN))
    elif nst == "SUBTITLE":
        reqs.append(text_run_style_request(s, e, font=DM_SANS, size=15, bold=False, italic=False, fg=GRAY_MUTED))
    elif nst == "NORMAL_TEXT":
        if r["in_table"]:
            # Table content handled in Phase 6 — skip here so we don't double-write
            continue
        if not first_normal_done and "|" in text:
            # Breadcrumb: italic dark green
            reqs.append(text_run_style_request(s, e, font=DM_SANS, size=10, italic=True, fg=GREEN))
            first_normal_done = True
        elif text.startswith("Last updated"):
            reqs.append(text_run_style_request(s, e, font=DM_SANS, size=10, italic=False, fg=GRAY_MUTED))
        else:
            # Body paragraphs (not in tables)
            reqs.append(text_run_style_request(s, e, font=DM_SANS, size=10, fg=BLACK_BODY))

batch_update(reqs, "typography")


# ---------------------------------------------------------------------------
# PHASE 4 — HEADING_2 paragraph style (non-bold, 36pt above / 12pt below)
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 4: HEADING_2 paragraph style")
print("=" * 80)

doc = fetch()
h2_ranges = []
for el in doc.get("body", {}).get("content", []):
    if "paragraph" in el:
        p = el["paragraph"]
        if p.get("paragraphStyle", {}).get("namedStyleType") == "HEADING_2":
            h2_ranges.append((el["startIndex"], el["endIndex"]))

print(f"Found {len(h2_ranges)} HEADING_2 paragraphs")

reqs = []
for s, e in h2_ranges:
    reqs.append({
        "updateParagraphStyle": {
            "range": {"startIndex": s, "endIndex": e},
            "paragraphStyle": {
                "lineSpacing": H2_LINE_SPACING,
                "spaceAbove": {"magnitude": H2_SPACE_ABOVE_PT, "unit": "PT"},
                "spaceBelow": {"magnitude": H2_SPACE_BELOW_PT, "unit": "PT"},
            },
            "fields": "lineSpacing,spaceAbove,spaceBelow",
        }
    })
batch_update(reqs, "h2-style")


# ---------------------------------------------------------------------------
# PHASE 5 — NORMAL_TEXT paragraph spaceBelow=4pt + lineSpacing=115
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 5: NORMAL_TEXT paragraph spacing")
print("=" * 80)

doc = fetch()
nt_ranges = []
for el in doc.get("body", {}).get("content", []):
    if "paragraph" in el:
        p = el["paragraph"]
        if p.get("paragraphStyle", {}).get("namedStyleType") == "NORMAL_TEXT":
            nt_ranges.append((el["startIndex"], el["endIndex"]))

print(f"Found {len(nt_ranges)} NORMAL_TEXT paragraphs")

reqs = []
for s, e in nt_ranges:
    reqs.append({
        "updateParagraphStyle": {
            "range": {"startIndex": s, "endIndex": e},
            "paragraphStyle": {
                "lineSpacing": NORMAL_LINE_SPACING,
                "spaceBelow": {"magnitude": NORMAL_TEXT_SPACE_BELOW_PT, "unit": "PT"},
            },
            "fields": "lineSpacing,spaceBelow",
        }
    })
batch_update(reqs, "normal-text-spacing")


# ---------------------------------------------------------------------------
# PHASE 6 — Table styling: col widths, cell bg, borders, padding,
# header row text, label col text, content col text, contentAlignment=TOP
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 6: Table styling")
print("=" * 80)

doc = fetch()
tables_info = find_top_level_tables(doc)
print(f"Found {len(tables_info)} top-level tables")

# 6a — Column widths
width_reqs = []
for ti_info in tables_info:
    t = ti_info["table"]
    table_start = ti_info["startIndex"]
    n_cols = t.get("columns", 0) or (len(t["tableRows"][0]["tableCells"]) if t.get("tableRows") else 0)
    if n_cols != 2:
        print(f"  Skipping table at idx {table_start}: {n_cols} cols")
        continue
    for ci, w in enumerate([COL0_WIDTH_PT, COL1_WIDTH_PT]):
        width_reqs.append({
            "updateTableColumnProperties": {
                "tableStartLocation": {"index": table_start},
                "columnIndices": [ci],
                "tableColumnProperties": {
                    "widthType": "FIXED_WIDTH",
                    "width": {"magnitude": w, "unit": "PT"},
                },
                "fields": "widthType,width",
            }
        })
batch_update(width_reqs, "col-widths")


# 6b — Cell-level styling (bg, padding, borders, contentAlignment)
doc = fetch()
tables_info = find_top_level_tables(doc)
cell_reqs = []
for ti_info in tables_info:
    t = ti_info["table"]
    table_start = ti_info["startIndex"]
    rows = t.get("tableRows", [])
    n_cols = t.get("columns", 0) or (len(rows[0]["tableCells"]) if rows else 0)
    if n_cols != 2:
        continue
    for ri, row in enumerate(rows):
        is_header = (ri == 0)
        bg = GREEN if is_header else WHITE
        for ci, cell in enumerate(row.get("tableCells", [])):
            cell_reqs.append({
                "updateTableCellStyle": {
                    "tableRange": {
                        "tableCellLocation": {
                            "tableStartLocation": {"index": table_start},
                            "rowIndex": ri,
                            "columnIndex": ci,
                        },
                        "rowSpan": 1,
                        "columnSpan": 1,
                    },
                    "tableCellStyle": {
                        "backgroundColor": hex_to_rgb_color(bg),
                        "contentAlignment": "TOP",
                        "paddingTop": {"magnitude": CELL_PADDING_PT, "unit": "PT"},
                        "paddingBottom": {"magnitude": CELL_PADDING_PT, "unit": "PT"},
                        "paddingLeft": {"magnitude": CELL_PADDING_PT, "unit": "PT"},
                        "paddingRight": {"magnitude": CELL_PADDING_PT, "unit": "PT"},
                        "borderTop": {
                            "color": hex_to_rgb_color(GRAY_BORDER),
                            "width": {"magnitude": BORDER_WIDTH_PT, "unit": "PT"},
                            "dashStyle": "SOLID",
                        },
                        "borderBottom": {
                            "color": hex_to_rgb_color(GRAY_BORDER),
                            "width": {"magnitude": BORDER_WIDTH_PT, "unit": "PT"},
                            "dashStyle": "SOLID",
                        },
                        "borderLeft": {
                            "color": hex_to_rgb_color(GRAY_BORDER),
                            "width": {"magnitude": BORDER_WIDTH_PT, "unit": "PT"},
                            "dashStyle": "SOLID",
                        },
                        "borderRight": {
                            "color": hex_to_rgb_color(GRAY_BORDER),
                            "width": {"magnitude": BORDER_WIDTH_PT, "unit": "PT"},
                            "dashStyle": "SOLID",
                        },
                    },
                    "fields": "backgroundColor,contentAlignment,paddingTop,paddingBottom,paddingLeft,paddingRight,borderTop,borderBottom,borderLeft,borderRight",
                }
            })
batch_update(cell_reqs, "cell-style")


# 6c — Cell text styling (header row white bold; label col bold green; content col black)
doc = fetch()
tables_info = find_top_level_tables(doc)
text_reqs = []
for ti_info in tables_info:
    t = ti_info["table"]
    rows = t.get("tableRows", [])
    n_cols = t.get("columns", 0) or (len(rows[0]["tableCells"]) if rows else 0)
    if n_cols != 2:
        continue
    for ri, row in enumerate(rows):
        is_header = (ri == 0)
        for ci, cell in enumerate(row.get("tableCells", [])):
            for el in cell.get("content", []):
                if "paragraph" not in el:
                    continue
                for re_ in el["paragraph"].get("elements", []):
                    if "textRun" not in re_:
                        continue
                    s, e = re_["startIndex"], re_["endIndex"]
                    text = re_["textRun"].get("content", "")
                    if not text:
                        continue
                    if is_header:
                        text_reqs.append(text_run_style_request(
                            s, e, font=DM_SANS, size=10, bold=True, fg=WHITE
                        ))
                    elif ci == 0:
                        text_reqs.append(text_run_style_request(
                            s, e, font=DM_SANS, size=10, bold=True, fg=GREEN
                        ))
                    else:
                        text_reqs.append(text_run_style_request(
                            s, e, font=DM_SANS, size=10, fg=BLACK_BODY
                        ))
batch_update(text_reqs, "cell-text")


# ---------------------------------------------------------------------------
# PHASE 7 — Bullet glyphs: BULLET_DISC_CIRCLE_SQUARE everywhere
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 7: Bullet glyph normalization")
print("=" * 80)

doc = fetch()
bulleted = []


def walk_bulleted(elements, accum):
    for el in elements:
        if "paragraph" in el:
            p = el["paragraph"]
            if p.get("bullet"):
                accum.append({
                    "start": p["elements"][0]["startIndex"] if p.get("elements") else el["startIndex"],
                    "end": el["endIndex"],
                })
        if "table" in el:
            for row in el["table"].get("tableRows", []):
                for cell in row.get("tableCells", []):
                    walk_bulleted(cell.get("content", []), accum)


walk_bulleted(doc.get("body", {}).get("content", []), bulleted)
print(f"Found {len(bulleted)} bulleted paragraphs")

bullet_reqs = []
for b in bulleted:
    bullet_reqs.append({
        "createParagraphBullets": {
            "range": {"startIndex": b["start"], "endIndex": b["end"]},
            "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
        }
    })
batch_update(bullet_reqs, "bullets")


print()
print("=" * 80)
print("DONE")
print("=" * 80)
print(f"Doc URL: https://docs.google.com/document/d/{DOC_ID}/edit")
