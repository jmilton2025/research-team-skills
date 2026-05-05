"""
mod-guide skill — Custom-reference styler.

Reads a user-supplied reference Google Doc, extracts its visual styling spec
(page setup, headings, body, table cell styles, bullet glyphs), and applies
that spec to a target mod guide.

This mirrors the phases of `apply_canonical_template.py` exactly — the only
difference is that values are sourced from the reference doc instead of
locked canonical constants.

Usage:
    uv run --python 3.12 \\
        --with google-api-python-client --with google-auth \\
        --with google-auth-oauthlib --with google-auth-httplib2 \\
        --with requests --with python-dotenv --with markdown --with pillow \\
        ~/.claude/skills/mod-guide/scripts/apply_custom_template.py \\
        <TARGET_DOC_ID> <REF_DOC_ID>
"""

import sys

sys.path.insert(0, '/Users/jedidamilton/.claude/plugins/cache/instacart/md2doc/893dc15bd620/skills/md2doc/scripts')
import _env  # noqa: F401
from common.drive import get_docs_service

if len(sys.argv) < 3:
    print("Usage: apply_custom_template.py <TARGET_DOC_ID> <REF_DOC_ID>", file=sys.stderr)
    sys.exit(1)

TARGET_ID = sys.argv[1]
REF_ID = sys.argv[2]

BATCH_SIZE = 200

# Sensible fallbacks if the reference doc doesn't define a particular value
DEFAULT_BODY_FONT = "DM Sans"
DEFAULT_HEADING_FONT = "DM Serif Display"
DEFAULT_GREEN = "#2D4A3E"
DEFAULT_BORDER = "#C7C7C7"
DEFAULT_BLACK = "#161416"
DEFAULT_WHITE = "#FFFFFF"


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


def rgb_color_to_hex(rgb_color):
    """Inverse — read the API color obj and return a hex string, or None."""
    if not rgb_color:
        return None
    inner = rgb_color.get("color", {}).get("rgbColor", {})
    if not inner:
        # Some places nest it differently
        inner = rgb_color.get("rgbColor", {})
    if not inner:
        return None
    r = int(round(inner.get("red", 0) * 255))
    g = int(round(inner.get("green", 0) * 255))
    b = int(round(inner.get("blue", 0) * 255))
    return f"#{r:02X}{g:02X}{b:02X}"


def batch_update(doc_id, reqs, label=""):
    if not reqs:
        return
    for i in range(0, len(reqs), BATCH_SIZE):
        chunk = reqs[i:i + BATCH_SIZE]
        docs.documents().batchUpdate(documentId=doc_id, body={"requests": chunk}).execute()
        print(f"  [{label}] applied {len(chunk)} reqs (chunk {i // BATCH_SIZE + 1})")


def fetch(doc_id):
    return docs.documents().get(documentId=doc_id).execute()


def text_run_style_request(start, end, font=None, size=None, bold=None,
                           italic=None, fg=None, baseline_offset=None):
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


# ---------------------------------------------------------------------------
# REFERENCE EXTRACTION
# ---------------------------------------------------------------------------

def first_text_run_in_doc(doc, predicate):
    """Walk doc and return the first textRun where predicate(paragraph, run) is True."""
    def walk(elements, in_table=False):
        for el in elements:
            if "paragraph" in el:
                p = el["paragraph"]
                for re_ in p.get("elements", []):
                    if "textRun" in re_ and predicate(p, re_, in_table):
                        return re_
            if "table" in el:
                for row in el["table"].get("tableRows", []):
                    for cell in row.get("tableCells", []):
                        r = walk(cell.get("content", []), in_table=True)
                        if r is not None:
                            return r
        return None

    return walk(doc.get("body", {}).get("content", []))


def extract_run_style(doc, namedStyleType, in_table=None):
    """Find first run where paragraph has the given namedStyleType.
    Return (font, size, bold, italic, fg_hex) or all-None if not found."""

    def pred(p, re_, in_t):
        if p.get("paragraphStyle", {}).get("namedStyleType") != namedStyleType:
            return False
        if in_table is True and not in_t:
            return False
        if in_table is False and in_t:
            return False
        # Skip empty runs
        return bool(re_["textRun"].get("content", "").strip())

    run = first_text_run_in_doc(doc, pred)
    if not run:
        return None
    ts = run["textRun"].get("textStyle", {})
    font = ts.get("weightedFontFamily", {}).get("fontFamily")
    size = ts.get("fontSize", {}).get("magnitude")
    bold = ts.get("bold")
    italic = ts.get("italic")
    fg = rgb_color_to_hex(ts.get("foregroundColor")) if ts.get("foregroundColor") else None
    return {
        "font": font,
        "size": size,
        "bold": bold,
        "italic": italic,
        "fg": fg,
    }


def extract_paragraph_style(doc, namedStyleType):
    """Return spaceAbove/spaceBelow/lineSpacing of first matching paragraph."""
    for el in doc.get("body", {}).get("content", []):
        if "paragraph" in el:
            p = el["paragraph"]
            ps = p.get("paragraphStyle", {})
            if ps.get("namedStyleType") == namedStyleType:
                return {
                    "spaceAbove": ps.get("spaceAbove", {}).get("magnitude"),
                    "spaceBelow": ps.get("spaceBelow", {}).get("magnitude"),
                    "lineSpacing": ps.get("lineSpacing"),
                }
    return None


def extract_page_setup(doc):
    ds = doc.get("documentStyle", {})
    page = ds.get("pageSize", {})
    return {
        "width": page.get("width", {}).get("magnitude", 612),
        "height": page.get("height", {}).get("magnitude", 792),
        "marginTop": ds.get("marginTop", {}).get("magnitude", 72),
        "marginBottom": ds.get("marginBottom", {}).get("magnitude", 72),
        "marginLeft": ds.get("marginLeft", {}).get("magnitude", 72),
        "marginRight": ds.get("marginRight", {}).get("magnitude", 72),
    }


def extract_table_spec(doc):
    """Find the first 2-col table and extract its spec."""
    for el in doc.get("body", {}).get("content", []):
        if "table" not in el:
            continue
        t = el["table"]
        rows = t.get("tableRows", [])
        n_cols = t.get("columns", 0) or (len(rows[0]["tableCells"]) if rows else 0)
        if n_cols != 2:
            continue

        # Column widths (from table style)
        col_widths = []
        ts_cols = t.get("tableStyle", {}).get("tableColumnProperties", [])
        for cp in ts_cols:
            w = cp.get("width", {}).get("magnitude")
            col_widths.append(w)

        spec = {
            "col_widths": col_widths if len(col_widths) == 2 else [96, 715.5],
        }

        # Header cell (row 0, col 0)
        if rows:
            header_cell = rows[0]["tableCells"][0] if rows[0].get("tableCells") else None
            if header_cell:
                cs = header_cell.get("tableCellStyle", {})
                spec["header_bg"] = rgb_color_to_hex(cs.get("backgroundColor"))
                spec["padding_top"] = cs.get("paddingTop", {}).get("magnitude")
                spec["padding_bottom"] = cs.get("paddingBottom", {}).get("magnitude")
                spec["padding_left"] = cs.get("paddingLeft", {}).get("magnitude")
                spec["padding_right"] = cs.get("paddingRight", {}).get("magnitude")
                bt = cs.get("borderTop", {})
                spec["border_color"] = rgb_color_to_hex(bt.get("color"))
                spec["border_width"] = bt.get("width", {}).get("magnitude")
                spec["border_dash"] = bt.get("dashStyle")
                # Header text run
                for c_el in header_cell.get("content", []):
                    if "paragraph" in c_el:
                        for re_ in c_el["paragraph"].get("elements", []):
                            if "textRun" in re_ and re_["textRun"].get("content", "").strip():
                                hts = re_["textRun"].get("textStyle", {})
                                spec["header_text_font"] = hts.get("weightedFontFamily", {}).get("fontFamily")
                                spec["header_text_size"] = hts.get("fontSize", {}).get("magnitude")
                                spec["header_text_bold"] = hts.get("bold")
                                spec["header_text_color"] = rgb_color_to_hex(hts.get("foregroundColor"))
                                break
                        if "header_text_font" in spec:
                            break

        # Body label cell (row 1, col 0) — if any body row exists
        if len(rows) >= 2:
            label_cell = rows[1]["tableCells"][0] if rows[1].get("tableCells") else None
            if label_cell:
                for c_el in label_cell.get("content", []):
                    if "paragraph" in c_el:
                        for re_ in c_el["paragraph"].get("elements", []):
                            if "textRun" in re_ and re_["textRun"].get("content", "").strip():
                                lts = re_["textRun"].get("textStyle", {})
                                spec["label_font"] = lts.get("weightedFontFamily", {}).get("fontFamily")
                                spec["label_size"] = lts.get("fontSize", {}).get("magnitude")
                                spec["label_bold"] = lts.get("bold")
                                spec["label_color"] = rgb_color_to_hex(lts.get("foregroundColor"))
                                break
                        if "label_font" in spec:
                            break

            # Body content cell (row 1, col 1)
            if len(rows[1].get("tableCells", [])) >= 2:
                content_cell = rows[1]["tableCells"][1]
                for c_el in content_cell.get("content", []):
                    if "paragraph" in c_el:
                        for re_ in c_el["paragraph"].get("elements", []):
                            if "textRun" in re_ and re_["textRun"].get("content", "").strip():
                                cts = re_["textRun"].get("textStyle", {})
                                spec["content_font"] = cts.get("weightedFontFamily", {}).get("fontFamily")
                                spec["content_size"] = cts.get("fontSize", {}).get("magnitude")
                                spec["content_color"] = rgb_color_to_hex(cts.get("foregroundColor"))
                                break
                        if "content_font" in spec:
                            break
        return spec
    return None


def extract_bullet_preset(doc):
    """Return the first bullet preset we can infer from the reference doc."""
    lists = doc.get("lists", {})
    for lid, lobj in lists.items():
        nls = lobj.get("listProperties", {}).get("nestingLevels", [])
        if nls:
            glyph0 = nls[0].get("glyphSymbol")
            if glyph0:
                return "BULLET_DISC_CIRCLE_SQUARE"
    return "BULLET_DISC_CIRCLE_SQUARE"


# ---------------------------------------------------------------------------
# Build runtime spec from reference doc
# ---------------------------------------------------------------------------

print("=" * 80)
print("EXTRACTING SPEC FROM REFERENCE")
print("=" * 80)
print(f"Ref doc: {REF_ID}")
ref = fetch(REF_ID)

page_spec = extract_page_setup(ref)
print(f"Page: {page_spec['width']}x{page_spec['height']}, margins T{page_spec['marginTop']} B{page_spec['marginBottom']} L{page_spec['marginLeft']} R{page_spec['marginRight']}")

# Headings: try TITLE/HEADING_1/2/3/4
heading_specs = {}
for nst in ["TITLE", "HEADING_1", "HEADING_2", "HEADING_3", "HEADING_4"]:
    s = extract_run_style(ref, nst, in_table=False)
    if s:
        heading_specs[nst] = s
        print(f"{nst}: {s}")

normal_run_spec = extract_run_style(ref, "NORMAL_TEXT", in_table=False)
print(f"NORMAL_TEXT: {normal_run_spec}")

normal_para_spec = extract_paragraph_style(ref, "NORMAL_TEXT")
h2_para_spec = extract_paragraph_style(ref, "HEADING_2")
print(f"NORMAL_TEXT para: {normal_para_spec}")
print(f"HEADING_2 para: {h2_para_spec}")

table_spec = extract_table_spec(ref)
print(f"Table: {table_spec}")

bullet_preset = extract_bullet_preset(ref)
print(f"Bullets: {bullet_preset}")


# ---------------------------------------------------------------------------
# PHASE 1 — Strip SUBSCRIPT in target
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 1: Clear SUBSCRIPT in target")
print("=" * 80)

target = fetch(TARGET_ID)


def collect_subscript_ranges(doc):
    ranges = []

    def walk(elements):
        for el in elements:
            if "paragraph" in el:
                for re_ in el["paragraph"].get("elements", []):
                    if "textRun" in re_:
                        bo = re_["textRun"].get("textStyle", {}).get("baselineOffset")
                        if bo == "SUBSCRIPT":
                            ranges.append((re_["startIndex"], re_["endIndex"]))
            if "table" in el:
                for row in el["table"].get("tableRows", []):
                    for cell in row.get("tableCells", []):
                        walk(cell.get("content", []))

    walk(doc.get("body", {}).get("content", []))
    return ranges


sub_ranges = collect_subscript_ranges(target)
sub_reqs = [
    {
        "updateTextStyle": {
            "range": {"startIndex": s, "endIndex": e},
            "textStyle": {"baselineOffset": "NONE"},
            "fields": "baselineOffset",
        }
    }
    for s, e in sub_ranges
]
print(f"Found {len(sub_reqs)} SUBSCRIPT runs")
batch_update(TARGET_ID, sub_reqs, "subscript-clear")


# ---------------------------------------------------------------------------
# PHASE 2 — Page setup from ref
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 2: Page setup")
print("=" * 80)
page_reqs = [{
    "updateDocumentStyle": {
        "documentStyle": {
            "pageSize": {
                "width": {"magnitude": page_spec["width"], "unit": "PT"},
                "height": {"magnitude": page_spec["height"], "unit": "PT"},
            },
            "marginTop": {"magnitude": page_spec["marginTop"], "unit": "PT"},
            "marginBottom": {"magnitude": page_spec["marginBottom"], "unit": "PT"},
            "marginLeft": {"magnitude": page_spec["marginLeft"], "unit": "PT"},
            "marginRight": {"magnitude": page_spec["marginRight"], "unit": "PT"},
        },
        "fields": "pageSize,marginTop,marginBottom,marginLeft,marginRight",
    }
}]
batch_update(TARGET_ID, page_reqs, "page-setup")


# ---------------------------------------------------------------------------
# PHASE 3 — Run-level typography from ref
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 3: Run-level typography")
print("=" * 80)

target = fetch(TARGET_ID)


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
                        })
            if "table" in el:
                for row in el["table"].get("tableRows", []):
                    for ci, cell in enumerate(row.get("tableCells", [])):
                        walk(cell.get("content", []), in_table=True, in_table_col=ci)

    walk(doc.get("body", {}).get("content", []))
    return out


runs = collect_paragraph_runs(target)
print(f"Total runs: {len(runs)}")

reqs = []
first_normal_done = False
body_font = (normal_run_spec or {}).get("font") or DEFAULT_BODY_FONT
body_size = (normal_run_spec or {}).get("size") or 10
body_color = (normal_run_spec or {}).get("fg") or DEFAULT_BLACK


def hreq(s, e, hspec, fallback_size):
    if not hspec:
        return None
    return text_run_style_request(
        s, e,
        font=hspec.get("font") or DEFAULT_HEADING_FONT,
        size=hspec.get("size") or fallback_size,
        bold=hspec.get("bold") if hspec.get("bold") is not None else None,
        italic=hspec.get("italic") if hspec.get("italic") is not None else None,
        fg=hspec.get("fg") or DEFAULT_GREEN,
    )


for r in runs:
    nst = r["nst"]
    text = r["text"]
    s, e = r["start"], r["end"]
    if not text.strip():
        continue
    if r["in_table"]:
        # Handled in Phase 6
        continue

    if nst in ("HEADING_1", "TITLE"):
        req = hreq(s, e, heading_specs.get(nst) or heading_specs.get("HEADING_1") or heading_specs.get("TITLE"), 26)
        if req:
            reqs.append(req)
    elif nst == "HEADING_2":
        req = hreq(s, e, heading_specs.get("HEADING_2"), 16)
        if req:
            reqs.append(req)
    elif nst == "HEADING_3":
        req = hreq(s, e, heading_specs.get("HEADING_3"), 14)
        if req:
            reqs.append(req)
    elif nst == "HEADING_4":
        req = hreq(s, e, heading_specs.get("HEADING_4"), 12)
        if req:
            reqs.append(req)
    elif nst == "NORMAL_TEXT":
        if not first_normal_done and "|" in text:
            # Breadcrumb heuristic
            reqs.append(text_run_style_request(s, e, font=body_font, size=body_size, italic=True, fg=DEFAULT_GREEN))
            first_normal_done = True
        elif text.startswith("Last updated"):
            reqs.append(text_run_style_request(s, e, font=body_font, size=body_size, italic=False, fg="#666666"))
        else:
            reqs.append(text_run_style_request(s, e, font=body_font, size=body_size, fg=body_color))

batch_update(TARGET_ID, reqs, "typography")


# ---------------------------------------------------------------------------
# PHASE 4 — HEADING_2 paragraph style
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 4: HEADING_2 paragraph style")
print("=" * 80)

target = fetch(TARGET_ID)
h2_ranges = []
for el in target.get("body", {}).get("content", []):
    if "paragraph" in el:
        if el["paragraph"].get("paragraphStyle", {}).get("namedStyleType") == "HEADING_2":
            h2_ranges.append((el["startIndex"], el["endIndex"]))
print(f"Found {len(h2_ranges)} HEADING_2 paragraphs")

reqs = []
if h2_para_spec:
    para_style = {}
    fields = []
    if h2_para_spec.get("lineSpacing"):
        para_style["lineSpacing"] = h2_para_spec["lineSpacing"]
        fields.append("lineSpacing")
    if h2_para_spec.get("spaceAbove") is not None:
        para_style["spaceAbove"] = {"magnitude": h2_para_spec["spaceAbove"], "unit": "PT"}
        fields.append("spaceAbove")
    if h2_para_spec.get("spaceBelow") is not None:
        para_style["spaceBelow"] = {"magnitude": h2_para_spec["spaceBelow"], "unit": "PT"}
        fields.append("spaceBelow")
    if fields:
        for s, e in h2_ranges:
            reqs.append({
                "updateParagraphStyle": {
                    "range": {"startIndex": s, "endIndex": e},
                    "paragraphStyle": para_style,
                    "fields": ",".join(fields),
                }
            })
batch_update(TARGET_ID, reqs, "h2-style")


# ---------------------------------------------------------------------------
# PHASE 5 — NORMAL_TEXT paragraph spacing
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 5: NORMAL_TEXT paragraph spacing")
print("=" * 80)

target = fetch(TARGET_ID)
nt_ranges = []
for el in target.get("body", {}).get("content", []):
    if "paragraph" in el:
        if el["paragraph"].get("paragraphStyle", {}).get("namedStyleType") == "NORMAL_TEXT":
            nt_ranges.append((el["startIndex"], el["endIndex"]))
print(f"Found {len(nt_ranges)} NORMAL_TEXT paragraphs")

reqs = []
if normal_para_spec:
    para_style = {}
    fields = []
    if normal_para_spec.get("lineSpacing"):
        para_style["lineSpacing"] = normal_para_spec["lineSpacing"]
        fields.append("lineSpacing")
    if normal_para_spec.get("spaceBelow") is not None:
        para_style["spaceBelow"] = {"magnitude": normal_para_spec["spaceBelow"], "unit": "PT"}
        fields.append("spaceBelow")
    if fields:
        for s, e in nt_ranges:
            reqs.append({
                "updateParagraphStyle": {
                    "range": {"startIndex": s, "endIndex": e},
                    "paragraphStyle": para_style,
                    "fields": ",".join(fields),
                }
            })
batch_update(TARGET_ID, reqs, "normal-text-spacing")


# ---------------------------------------------------------------------------
# PHASE 6 — Table styling from ref
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 6: Table styling")
print("=" * 80)

if not table_spec:
    print("  No 2-col table found in ref — skipping table styling")
else:
    target = fetch(TARGET_ID)

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

    tables_info = find_top_level_tables(target)
    print(f"Found {len(tables_info)} top-level tables in target")

    # 6a — Column widths
    width_reqs = []
    col_widths = table_spec.get("col_widths") or [96, 715.5]
    for ti_info in tables_info:
        t = ti_info["table"]
        n_cols = t.get("columns", 0) or (len(t["tableRows"][0]["tableCells"]) if t.get("tableRows") else 0)
        if n_cols != 2:
            continue
        for ci, w in enumerate(col_widths):
            if w is None:
                continue
            width_reqs.append({
                "updateTableColumnProperties": {
                    "tableStartLocation": {"index": ti_info["startIndex"]},
                    "columnIndices": [ci],
                    "tableColumnProperties": {
                        "widthType": "FIXED_WIDTH",
                        "width": {"magnitude": w, "unit": "PT"},
                    },
                    "fields": "widthType,width",
                }
            })
    batch_update(TARGET_ID, width_reqs, "col-widths")

    # 6b — Cell-level styling
    target = fetch(TARGET_ID)
    tables_info = find_top_level_tables(target)
    cell_reqs = []
    header_bg = table_spec.get("header_bg") or DEFAULT_GREEN
    border_color = table_spec.get("border_color") or DEFAULT_BORDER
    border_width = table_spec.get("border_width") or 0.5
    border_dash = table_spec.get("border_dash") or "SOLID"
    pt_top = table_spec.get("padding_top") or 8
    pt_bot = table_spec.get("padding_bottom") or 8
    pt_left = table_spec.get("padding_left") or 8
    pt_right = table_spec.get("padding_right") or 8

    for ti_info in tables_info:
        t = ti_info["table"]
        rows = t.get("tableRows", [])
        n_cols = t.get("columns", 0) or (len(rows[0]["tableCells"]) if rows else 0)
        if n_cols != 2:
            continue
        for ri, row in enumerate(rows):
            is_header = (ri == 0)
            bg = header_bg if is_header else DEFAULT_WHITE
            for ci, cell in enumerate(row.get("tableCells", [])):
                cell_reqs.append({
                    "updateTableCellStyle": {
                        "tableRange": {
                            "tableCellLocation": {
                                "tableStartLocation": {"index": ti_info["startIndex"]},
                                "rowIndex": ri,
                                "columnIndex": ci,
                            },
                            "rowSpan": 1,
                            "columnSpan": 1,
                        },
                        "tableCellStyle": {
                            "backgroundColor": hex_to_rgb_color(bg),
                            "contentAlignment": "TOP",
                            "paddingTop": {"magnitude": pt_top, "unit": "PT"},
                            "paddingBottom": {"magnitude": pt_bot, "unit": "PT"},
                            "paddingLeft": {"magnitude": pt_left, "unit": "PT"},
                            "paddingRight": {"magnitude": pt_right, "unit": "PT"},
                            "borderTop": {
                                "color": hex_to_rgb_color(border_color),
                                "width": {"magnitude": border_width, "unit": "PT"},
                                "dashStyle": border_dash,
                            },
                            "borderBottom": {
                                "color": hex_to_rgb_color(border_color),
                                "width": {"magnitude": border_width, "unit": "PT"},
                                "dashStyle": border_dash,
                            },
                            "borderLeft": {
                                "color": hex_to_rgb_color(border_color),
                                "width": {"magnitude": border_width, "unit": "PT"},
                                "dashStyle": border_dash,
                            },
                            "borderRight": {
                                "color": hex_to_rgb_color(border_color),
                                "width": {"magnitude": border_width, "unit": "PT"},
                                "dashStyle": border_dash,
                            },
                        },
                        "fields": "backgroundColor,contentAlignment,paddingTop,paddingBottom,paddingLeft,paddingRight,borderTop,borderBottom,borderLeft,borderRight",
                    }
                })
    batch_update(TARGET_ID, cell_reqs, "cell-style")

    # 6c — Cell text styling (header / label / content)
    target = fetch(TARGET_ID)
    tables_info = find_top_level_tables(target)
    text_reqs = []
    h_font = table_spec.get("header_text_font") or DEFAULT_BODY_FONT
    h_size = table_spec.get("header_text_size") or 10
    h_bold = table_spec.get("header_text_bold") if table_spec.get("header_text_bold") is not None else True
    h_color = table_spec.get("header_text_color") or DEFAULT_WHITE
    l_font = table_spec.get("label_font") or DEFAULT_BODY_FONT
    l_size = table_spec.get("label_size") or 10
    l_bold = table_spec.get("label_bold") if table_spec.get("label_bold") is not None else True
    l_color = table_spec.get("label_color") or DEFAULT_GREEN
    c_font = table_spec.get("content_font") or DEFAULT_BODY_FONT
    c_size = table_spec.get("content_size") or 10
    c_color = table_spec.get("content_color") or DEFAULT_BLACK

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
                                s, e, font=h_font, size=h_size, bold=h_bold, fg=h_color
                            ))
                        elif ci == 0:
                            text_reqs.append(text_run_style_request(
                                s, e, font=l_font, size=l_size, bold=l_bold, fg=l_color
                            ))
                        else:
                            text_reqs.append(text_run_style_request(
                                s, e, font=c_font, size=c_size, fg=c_color
                            ))
    batch_update(TARGET_ID, text_reqs, "cell-text")


# ---------------------------------------------------------------------------
# PHASE 7 — Bullet glyphs
# ---------------------------------------------------------------------------
print()
print("=" * 80)
print("PHASE 7: Bullet glyph normalization")
print("=" * 80)

target = fetch(TARGET_ID)
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


walk_bulleted(target.get("body", {}).get("content", []), bulleted)
print(f"Found {len(bulleted)} bulleted paragraphs")
bullet_reqs = [
    {
        "createParagraphBullets": {
            "range": {"startIndex": b["start"], "endIndex": b["end"]},
            "bulletPreset": bullet_preset,
        }
    }
    for b in bulleted
]
batch_update(TARGET_ID, bullet_reqs, "bullets")


print()
print("=" * 80)
print("DONE")
print("=" * 80)
print(f"Target doc URL: https://docs.google.com/document/d/{TARGET_ID}/edit")
print(f"Source ref doc: https://docs.google.com/document/d/{REF_ID}/edit")
