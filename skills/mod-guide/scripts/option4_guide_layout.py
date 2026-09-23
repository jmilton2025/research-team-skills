#!/usr/bin/env python3
"""Build and verify the Option 4 — Leadership layout for a MODERATION GUIDE.

This is the opt-in "leadership design" path for /mod-guide. The default
mod-guide deliverable is native Google Docs; this formatter reproduces the same
clean, edited "leadership" look that /research-plan's Option 4 pipeline produces,
adapted to a moderation guide's structure (breadcrumb -> title -> RACI ->
parameters table -> Pre-Session Checklist -> Consent script -> Phase sections ->
Post-Session Debrief).

Pipeline (same four stages as the research-plan formatter):
    option4_guide_layout.py manifest APPROVED.md manifest.json
    option4_guide_layout.py normalize imported-doc.json manifest.json normalize-batch.json
    # Apply the normalize batch and re-fetch the document.
    option4_guide_layout.py format normalized-doc.json manifest.json format-batch.json
    # Apply the format batch and re-fetch the document.
    option4_guide_layout.py verify final-doc.json manifest.json

The script only uses the Python standard library. Batch files use the native
Google Docs API request schema and can be applied through any write-capable
integration (the MCP batch_update_doc tool, gws, etc.). No live API call is made
by this script; every stage operates on JSON, so the whole pipeline is testable
offline against fixtures.

The contract loaded here is skills/mod-guide/references/option4-guide-style.json.
Its page/colors/typography/warning/spacing tokens are copied verbatim from
research-plan's option4-style-contract.json so the finished look matches; the
structure and table geometry are moderation-guide-specific.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONTRACT_PATH = SKILL_DIR / "references" / "option4-guide-style.json"
TAB_ID_FALLBACK = "t.0"

RACI_ROLES = ("Responsible", "Accountable", "Consulted", "Informed")

# Exact TEST ARTIFACT copy, verbatim from
# references/output-status-and-labeling-conventions.md. Do not paraphrase.
WARNING = (
    "⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. "
    "Do not file or share as real research."
)

# The guide MUST end at Post-Session Debrief (SKILL.md lines 488, 688).
TERMINAL_BAND = "POST-SESSION DEBRIEF"

# Bands that carry a fixed, non-phase label.
FIXED_BAND_LABELS = (
    "PRE-SESSION CHECKLIST",
    "CONSENT + RECORDING SCRIPT — READ VERBATIM",
    "POST-SESSION DEBRIEF",
)

BULLET_PRESET = "BULLET_DISC_CIRCLE_SQUARE"
NUMBERED_PRESET = "NUMBERED_DECIMAL_ALPHA_ROMAN"


class ContractError(ValueError):
    """Raised when the document cannot satisfy the Option 4 mod-guide contract."""


# ---------------------------------------------------------------------------
# Contract loading + manifest integrity
# ---------------------------------------------------------------------------


def load_contract() -> dict[str, Any]:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    usable_width = round(
        contract["page"]["width_pt"]
        - contract["page"]["margins_pt"]["left"]
        - contract["page"]["margins_pt"]["right"],
        3,
    )
    # Each table kind's widths must sum to its total, and the shared overflow
    # token must equal (total width - usable text area). This is the same
    # internal-consistency self-check the research-plan contract performs.
    for kind, spec in contract["tables"]["kinds"].items():
        widths_total = round(sum(spec["column_widths_pt"]), 3)
        if widths_total != spec["total_width_pt"]:
            raise ContractError(f"Table kind {kind!r} column widths are internally inconsistent")
        if widths_total != contract["tables"]["total_width_pt"]:
            raise ContractError(f"Table kind {kind!r} total width does not match the shared table width")
        overflow = round(widths_total - usable_width, 3)
        if overflow != contract["tables"]["intentional_text_area_overflow_pt"]:
            raise ContractError(f"Table kind {kind!r} intentional overflow token is inconsistent")
    return contract


def manifest_digest(manifest: dict[str, Any]) -> str:
    payload = {key: value for key, value in manifest.items() if key != "manifest_sha256"}
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def validate_manifest(manifest: dict[str, Any]) -> None:
    contract = load_contract()
    if manifest.get("contract") != contract["name"]:
        raise ContractError("Manifest is not for the Option 4 — Leadership (Moderation Guide) contract")
    if manifest.get("contract_version") != contract["version"]:
        raise ContractError("Manifest contract version is stale")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest.get("markdown_sha256", "")):
        raise ContractError("Manifest is missing its approved-Markdown SHA-256")
    if manifest.get("manifest_sha256") != manifest_digest(manifest):
        raise ContractError("Manifest content has changed since approved Markdown was parsed")


# ---------------------------------------------------------------------------
# Inline + table markdown parsing
# ---------------------------------------------------------------------------


def parse_inline(markdown: str) -> dict[str, Any]:
    """Parse the small inline Markdown subset used by moderation guides.

    Returns {"text", "bold", "italic", "links"} where bold/italic are lists of
    [start, end] character offsets into text and links carry start/end/url.
    """
    source = html.unescape(markdown.strip())
    plain: list[str] = []
    bold: list[list[int]] = []
    italic: list[list[int]] = []
    links: list[dict[str, Any]] = []

    def length() -> int:
        return sum(len(part) for part in plain)

    def walk(value: str) -> None:
        i = 0
        while i < len(value):
            if value.startswith("**", i):
                end = value.find("**", i + 2)
                if end >= 0:
                    start_plain = length()
                    walk(value[i + 2 : end])
                    bold.append([start_plain, length()])
                    i = end + 2
                    continue
            if value.startswith("*", i):
                end = value.find("*", i + 1)
                if end >= 0:
                    start_plain = length()
                    walk(value[i + 1 : end])
                    italic.append([start_plain, length()])
                    i = end + 1
                    continue
            if value.startswith("`", i):
                end = value.find("`", i + 1)
                if end >= 0:
                    plain.append(value[i + 1 : end])
                    i = end + 1
                    continue
            if value.startswith("[", i):
                close = value.find("](", i + 1)
                if close >= 0:
                    depth = 1
                    close_url = -1
                    cursor = close + 2
                    while cursor < len(value):
                        if value[cursor] == "\\":
                            cursor += 2
                            continue
                        if value[cursor] == "(":
                            depth += 1
                        elif value[cursor] == ")":
                            depth -= 1
                            if depth == 0:
                                close_url = cursor
                                break
                        cursor += 1
                    if close_url >= 0:
                        start_plain = length()
                        walk(value[i + 1 : close])
                        links.append(
                            {
                                "start": start_plain,
                                "end": length(),
                                "url": value[close + 2 : close_url],
                            }
                        )
                        i = close_url + 1
                        continue
            if value.startswith("\\|", i):
                plain.append("|")
                i += 2
                continue
            plain.append(value[i])
            i += 1

    walk(source)
    return {
        "text": "".join(plain),
        "bold": sorted(bold),
        "italic": sorted(italic),
        "links": links,
    }


def split_markdown_row(line: str) -> list[str]:
    """Split a simple Markdown table row while honoring escaped pipes."""
    value = line.strip()
    if not value.startswith("|") or not value.endswith("|"):
        raise ContractError(f"Not a Markdown table row: {line!r}")
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in value[1:-1]:
        if escaped:
            current.append("\\" + char if char != "|" else "\\|")
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def _strip_wrapping_emphasis(value: str) -> str:
    stripped = value.strip()
    for marker in ("**", "*"):
        if len(stripped) >= 2 * len(marker) and stripped.startswith(marker) and stripped.endswith(marker):
            return stripped[len(marker) : -len(marker)].strip()
    return stripped


# ---------------------------------------------------------------------------
# parse_markdown -> manifest
# ---------------------------------------------------------------------------


def _table_rows(lines: list[str], start: int) -> tuple[list[list[str]], int]:
    raw_rows: list[list[str]] = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw_rows.append(split_markdown_row(lines[i]))
        i += 1
    return raw_rows, i


def _content_rows(raw_rows: list[list[str]], conversion_header: list[str]) -> list[dict[str, Any]]:
    """Drop the separator row and the conversion header, return content rows."""
    if len(raw_rows) < 2 or not is_separator_row(raw_rows[1]):
        raise ContractError("Table must have a header row and a Markdown separator row")
    header = [parse_inline(cell)["text"] for cell in raw_rows[0]]
    if header != conversion_header:
        raise ContractError(f"Unexpected table conversion header: {header!r} (want {conversion_header})")
    rows: list[dict[str, Any]] = []
    for cells in raw_rows[2:]:
        if len(cells) != 2:
            raise ContractError(f"Table row must have two cells: {cells!r}")
        rows.append({"label": parse_inline(cells[0])["text"], "content": parse_inline(cells[1])})
    if not rows:
        raise ContractError("Table has no content rows")
    return rows


def _parse_section_blocks(lines: list[str], band_label: str) -> list[dict[str, Any]]:
    """Parse the ordered blocks inside one ## section (prose/list/table/sub-phase)."""
    blocks: list[dict[str, Any]] = []
    i = 0
    is_core = "CORE" in band_label
    is_consent = band_label.startswith("CONSENT")
    is_checklist_section = band_label == "PRE-SESSION CHECKLIST"
    is_debrief_section = band_label == TERMINAL_BAND

    def table_kind() -> str:
        return "consent" if is_consent else "question"

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped == "---":
            i += 1
            continue
        if stripped.startswith("### "):
            heading = parse_inline(stripped[4:].strip())
            j = i + 1
            sub_lines: list[str] = []
            while j < len(lines) and not lines[j].strip().startswith("### "):
                sub_lines.append(lines[j])
                j += 1
            sub_blocks = _parse_section_blocks(sub_lines, band_label)
            blocks.append({"type": "sub_phase", "heading": heading, "blocks": sub_blocks})
            i = j
            continue
        if stripped.startswith("|"):
            raw_rows, i = _table_rows(lines, i)
            kind = table_kind()
            header = {"consent": ["Cue", "Read aloud"], "question": ["#", "Ask"]}[kind]
            blocks.append({"type": "table", "kind": kind, "rows": _content_rows(raw_rows, header)})
            continue
        if re.match(r"^\d+[.)]\s+", stripped):
            items: list[dict[str, Any]] = []
            while i < len(lines) and re.match(r"^\d+[.)]\s+", lines[i].strip()):
                text = re.sub(r"^\d+[.)]\s+", "", lines[i].strip())
                items.append(parse_inline(text))
                i += 1
            kind = "debrief" if is_debrief_section else "numbered"
            blocks.append({"type": "list", "kind": kind, "items": items})
            continue
        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                text = re.sub(r"^[-*]\s+", "", lines[i].strip())
                items.append(parse_inline(text))
                i += 1
            if is_checklist_section:
                kind = "checklist"
            elif is_core:
                kind = "silent_tagging"
            else:
                kind = "checklist"
            blocks.append({"type": "list", "kind": kind, "items": items})
            continue
        # Prose paragraph (including >-blockquote moderator reminders).
        text = stripped[1:].strip() if stripped.startswith(">") else stripped
        blocks.append({"type": "prose", "inline": parse_inline(text)})
        i += 1
    return blocks


def parse_markdown(markdown: str) -> dict[str, Any]:
    """Parse an approved Option 4 moderation-guide intermediate Markdown document."""
    lines = markdown.splitlines()
    nonempty = [
        i
        for i, line in enumerate(lines)
        if line.strip() and not line.lstrip().startswith("<!--")
    ]
    if not nonempty:
        raise ContractError("Approved Markdown is empty")

    title_index = next(
        (i for i in nonempty if lines[i].lstrip().startswith("# ")),
        None,
    )
    if title_index is None:
        raise ContractError("Missing moderation-guide title (a single '# ' heading)")

    breadcrumb_index = next((i for i in nonempty if i < title_index), None)
    if breadcrumb_index is None:
        raise ContractError("Missing breadcrumb before the title")

    updated_index = next(
        (i for i in range(title_index + 1, len(lines)) if lines[i].strip().startswith("Last updated:")),
        None,
    )
    if updated_index is None:
        raise ContractError("Missing 'Last updated:' line")

    # Optional bold phase subtitle between the title and the date line.
    phase_subtitle = None
    for i in range(title_index + 1, updated_index):
        value = lines[i].strip()
        if value.startswith("**") and value.endswith("**") and len(value) > 4:
            phase_subtitle = parse_inline(value)
            break

    # RACI bullets.
    raci: list[dict[str, Any]] = []
    raci_pattern = re.compile(r"^-\s+\*\*(Responsible|Accountable|Consulted|Informed):\*\*\s*(.*)$")
    for i in range(updated_index + 1, len(lines)):
        if lines[i].strip().startswith("##") or lines[i].strip().startswith("|"):
            break
        match = raci_pattern.match(lines[i].strip())
        if match:
            role, remainder = match.groups()
            item = parse_inline(f"**{role}:** {remainder}")
            item["role"] = role
            raci.append(item)
    if [item["role"] for item in raci] != list(RACI_ROLES):
        raise ContractError("RACI must contain Responsible, Accountable, Consulted, and Informed in order")

    # Optional TEST ARTIFACT warning.
    warning = None
    for i in range(updated_index + 1, len(lines)):
        if lines[i].strip().startswith("##"):
            break
        value = lines[i].strip()
        if not value:
            continue
        candidate = value[1:].strip() if value.startswith(">") else value
        if parse_inline(candidate)["text"] == WARNING:
            warning = WARNING
            break

    # Parameters table: the first Markdown table, which precedes the first '## '.
    first_heading = next((i for i in range(len(lines)) if lines[i].strip().startswith("## ")), len(lines))
    param_start = next(
        (i for i in range(updated_index + 1, first_heading) if lines[i].strip().startswith("|")),
        None,
    )
    if param_start is None:
        raise ContractError("Missing the Parameters table before the first phase heading")
    param_raw, _ = _table_rows(lines, param_start)
    parameters = {"kind": "parameters", "rows": _content_rows(param_raw, ["Parameter", "Detail"])}

    # Sections: every '## ' heading and the blocks beneath it.
    heading_indices = [i for i in range(len(lines)) if lines[i].strip().startswith("## ")]
    if not heading_indices:
        raise ContractError("A moderation guide must contain at least one '## ' section heading")
    sections: list[dict[str, Any]] = []
    for order, start in enumerate(heading_indices):
        end = heading_indices[order + 1] if order + 1 < len(heading_indices) else len(lines)
        source_label = lines[start].strip()[3:].strip()
        band_label = source_label.upper()
        blocks = _parse_section_blocks(lines[start + 1 : end], band_label)
        sections.append({"band_label": band_label, "source_label": source_label, "blocks": blocks})

    # Guide-specific structural guarantees.
    band_labels = [section["band_label"] for section in sections]
    required = ["PRE-SESSION CHECKLIST", "CONSENT + RECORDING SCRIPT — READ VERBATIM"]
    for label in required:
        if label not in band_labels:
            raise ContractError(f"Missing required section: {label}")
    if band_labels[-1] != TERMINAL_BAND:
        raise ContractError(f"The guide must end at {TERMINAL_BAND!r}; last section is {band_labels[-1]!r}")
    if any(label.startswith("PHASE") for label in band_labels) is False:
        raise ContractError("A moderation guide must contain at least one PHASE section")
    # No forbidden trailing sections may follow the debrief.
    for forbidden in ("MASTER PROBE BANK", "BIAS MITIGATION CHECKLIST", "SELF-CRITIQUE AUDIT"):
        if forbidden in band_labels:
            raise ContractError(f"{forbidden} must not appear inside the guide document")

    study_type = None
    for row in parameters["rows"]:
        if row["label"].casefold() == "study type":
            study_type = row["content"]["text"]
    has_stimulus = any(label.startswith("PHASE 3") for label in band_labels)

    manifest = {
        "contract": load_contract()["name"],
        "contract_version": load_contract()["version"],
        "markdown_sha256": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "document_meta": {
            "is_test_artifact": warning is not None,
            "has_phase_subtitle": phase_subtitle is not None,
            "has_stimulus_phase": has_stimulus,
            "study_type": study_type,
        },
        "top": {
            "breadcrumb": parse_inline(_strip_wrapping_emphasis(lines[breadcrumb_index].strip())),
            "title": parse_inline(lines[title_index].lstrip()[2:].strip()),
            "phase_subtitle": phase_subtitle,
            "date": parse_inline(lines[updated_index].strip()),
            "raci": raci,
            "warning": warning,
        },
        "parameters": parameters,
        "sections": sections,
    }
    manifest["manifest_sha256"] = manifest_digest(manifest)
    return manifest


# ---------------------------------------------------------------------------
# Flat views over the manifest (tables + expected paragraph sequence)
# ---------------------------------------------------------------------------


def manifest_tables(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Every table in document order: parameters, then each section/sub-phase table."""
    tables: list[dict[str, Any]] = [manifest["parameters"]]
    for section in manifest["sections"]:
        for block in section["blocks"]:
            if block["type"] == "table":
                tables.append(block)
            elif block["type"] == "sub_phase":
                for sub in block["blocks"]:
                    if sub["type"] == "table":
                        tables.append(sub)
    return tables


def _iter_block_paragraphs(block: dict[str, Any]) -> list[str]:
    seq: list[str] = []
    if block["type"] == "prose":
        seq.append(block["inline"]["text"])
    elif block["type"] == "list":
        seq.extend(item["text"] for item in block["items"])
    elif block["type"] == "table":
        seq.append("<TABLE>")
    elif block["type"] == "sub_phase":
        seq.append(block["heading"]["text"])
        for sub in block["blocks"]:
            seq.extend(_iter_block_paragraphs(sub))
    return seq


def expected_sequence(manifest: dict[str, Any]) -> list[str]:
    top = manifest["top"]
    seq: list[str] = [top["breadcrumb"]["text"], top["title"]["text"]]
    if top.get("phase_subtitle"):
        seq.append(top["phase_subtitle"]["text"])
    seq.append(top["date"]["text"])
    seq.extend(item["text"] for item in top["raci"])
    if top.get("warning"):
        seq.append(top["warning"])
    seq.append("<TABLE>")  # parameters
    for section in manifest["sections"]:
        seq.append(section["band_label"])
        for block in section["blocks"]:
            seq.extend(_iter_block_paragraphs(block))
    return seq


# ---------------------------------------------------------------------------
# Raw Google Docs JSON helpers
# ---------------------------------------------------------------------------


def paragraph_text(paragraph: dict[str, Any]) -> str:
    return "".join(
        element.get("textRun", {}).get("content", "")
        for element in paragraph.get("elements", [])
    )


def cell_paragraphs(cell: dict[str, Any]) -> list[dict[str, Any]]:
    return [element for element in cell.get("content", []) if "paragraph" in element]


def get_tab(doc: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    tabs = doc.get("tabs", [])
    if len(tabs) != 1:
        raise ContractError("Option 4 mod-guide formatter requires one active content tab")
    tab_id = tabs[0].get("tabProperties", {}).get("tabId", TAB_ID_FALLBACK)
    return tab_id, tabs[0]["documentTab"]


def doc_tables(tab: dict[str, Any]) -> list[dict[str, Any]]:
    return [element for element in tab["body"]["content"] if "table" in element]


def find_paragraph(body: list[dict[str, Any]], exact: str) -> dict[str, Any]:
    for element in body:
        if "paragraph" in element and paragraph_text(element["paragraph"]).strip() == exact:
            return element
    raise ContractError(f"Paragraph not found: {exact!r}")


def utf16_offset(text: str, character_offset: int) -> int:
    """Convert a Python character offset to the UTF-16 units used by Docs indices."""
    return len(text[:character_offset].encode("utf-16-le")) // 2


# ---------------------------------------------------------------------------
# Native Docs request builders
# ---------------------------------------------------------------------------


def hex_color(value: str) -> dict[str, Any]:
    color = value.lstrip("#")
    if len(color) != 6:
        raise ContractError(f"Invalid color: {value}")
    red, green, blue = (int(color[i : i + 2], 16) / 255 for i in (0, 2, 4))
    return {"color": {"rgbColor": {"red": red, "green": green, "blue": blue}}}


def docs_range(tab_id: str, start: int, end: int) -> dict[str, Any]:
    return {"startIndex": start, "endIndex": end, "tabId": tab_id}


def update_text(tab_id: str, start: int, end: int, style: dict[str, Any], fields: str) -> dict[str, Any]:
    return {
        "updateTextStyle": {
            "range": docs_range(tab_id, start, end),
            "textStyle": style,
            "fields": fields,
        }
    }


def update_paragraph(tab_id: str, start: int, end: int, style: dict[str, Any], fields: str) -> dict[str, Any]:
    return {
        "updateParagraphStyle": {
            "range": docs_range(tab_id, start, end),
            "paragraphStyle": style,
            "fields": fields,
        }
    }


def cell_range(tab_id: str, table_start: int, row: int, col: int, row_span: int = 1, col_span: int = 1) -> dict[str, Any]:
    return {
        "tableCellLocation": {
            "tableStartLocation": {"index": table_start, "tabId": tab_id},
            "rowIndex": row,
            "columnIndex": col,
        },
        "rowSpan": row_span,
        "columnSpan": col_span,
    }


def update_cell(
    tab_id: str, table_start: int, row: int, col: int, style: dict[str, Any], fields: str,
    *, row_span: int = 1, col_span: int = 1,
) -> dict[str, Any]:
    return {
        "updateTableCellStyle": {
            "tableRange": cell_range(tab_id, table_start, row, col, row_span, col_span),
            "tableCellStyle": style,
            "fields": fields,
        }
    }


def column_widths_request(tab_id: str, table_start: int, widths: list[float]) -> list[dict[str, Any]]:
    requests: list[dict[str, Any]] = []
    for column_index, width in enumerate(widths):
        requests.append(
            {
                "updateTableColumnProperties": {
                    "tableStartLocation": {"index": table_start, "tabId": tab_id},
                    "columnIndices": [column_index],
                    "tableColumnProperties": {
                        "widthType": "FIXED_WIDTH",
                        "width": {"magnitude": width, "unit": "PT"},
                    },
                    "fields": "widthType,width",
                }
            }
        )
    return requests


def style_paragraph(
    requests: list[dict[str, Any]],
    tab_id: str,
    element: dict[str, Any],
    *,
    font: str,
    size: float,
    color: dict[str, Any],
    bold: bool = False,
    italic: bool = False,
    named_style: str = "NORMAL_TEXT",
    line_spacing: int = 115,
    space_above: float = 0,
    space_below: float = 0,
    keep_next: bool = False,
    indent_start: float | None = None,
    indent_first: float | None = None,
    shading: dict[str, Any] | None = None,
) -> None:
    start, end = element["startIndex"], element["endIndex"]
    paragraph_style: dict[str, Any] = {
        "namedStyleType": named_style,
        "lineSpacing": line_spacing,
        "spaceAbove": {"magnitude": space_above, "unit": "PT"},
        "spaceBelow": {"magnitude": space_below, "unit": "PT"},
        "keepWithNext": keep_next,
    }
    paragraph_fields = "namedStyleType,lineSpacing,spaceAbove,spaceBelow,keepWithNext"
    if indent_start is not None:
        paragraph_style["indentStart"] = {"magnitude": indent_start, "unit": "PT"}
        paragraph_fields += ",indentStart"
    if indent_first is not None:
        paragraph_style["indentFirstLine"] = {"magnitude": indent_first, "unit": "PT"}
        paragraph_fields += ",indentFirstLine"
    if shading is not None:
        paragraph_style["shading"] = {"backgroundColor": shading}
        paragraph_fields += ",shading"

    # Named styles can clear direct overrides. Paragraph first; exact text style second.
    requests.append(update_paragraph(tab_id, start, end, paragraph_style, paragraph_fields))
    requests.append(
        update_text(
            tab_id,
            start,
            end - 1,
            {
                "weightedFontFamily": {"fontFamily": font, "weight": 400},
                "fontSize": {"magnitude": size, "unit": "PT"},
                "bold": bold,
                "italic": italic,
                "foregroundColor": color,
            },
            "weightedFontFamily,fontSize,bold,italic,foregroundColor",
        )
    )


def apply_inline_styles(
    requests: list[dict[str, Any]],
    tab_id: str,
    element: dict[str, Any],
    item: dict[str, Any],
    *,
    link_color: dict[str, Any] | None = None,
) -> None:
    base = element["startIndex"]
    text = item.get("text", "")
    for start, end in item.get("bold", []):
        if end > start:
            requests.append(
                update_text(
                    tab_id,
                    base + utf16_offset(text, start),
                    base + utf16_offset(text, end),
                    {"bold": True},
                    "bold",
                )
            )
    for start, end in item.get("italic", []):
        if end > start:
            requests.append(
                update_text(
                    tab_id,
                    base + utf16_offset(text, start),
                    base + utf16_offset(text, end),
                    {"italic": True},
                    "italic",
                )
            )
    for link in item.get("links", []):
        if link["end"] > link["start"]:
            link_style: dict[str, Any] = {"link": {"url": link["url"]}, "underline": True}
            fields = "link,underline"
            if link_color is not None:
                # Creating a link otherwise adds Google blue after the base text pass.
                link_style["foregroundColor"] = link_color
                fields += ",foregroundColor"
            requests.append(
                update_text(
                    tab_id,
                    base + utf16_offset(text, link["start"]),
                    base + utf16_offset(text, link["end"]),
                    link_style,
                    fields,
                )
            )


def _text_style(contract: dict[str, Any], name: str) -> tuple[str, float, bool, bool, dict[str, Any]]:
    style = contract["typography"][name]
    return (
        style["font"],
        style["size_pt"],
        style.get("bold", False),
        style.get("italic", False),
        hex_color(style["color"]),
    )


# ---------------------------------------------------------------------------
# normalize: rebuild imported cell text, uppercase bands, drop rules + headers
# ---------------------------------------------------------------------------


def _cell_visible_lines(cell: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for element in cell_paragraphs(cell):
        content = paragraph_text(element["paragraph"]).replace("<br>", "\n")
        for line in content.splitlines():
            line = re.sub(r"^(?:[-*•]\s+|\d+[.)]\s+)", "", line.strip())
            line = re.sub(r"\s+", " ", line)
            if line:
                values.append(line)
    return values


def build_normalize_requests(doc: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    """Bind imported content to the manifest and emit cleanup requests.

    Cleanup covers: uppercasing each ## band heading (length-preserving), dropping
    every native horizontal rule the importer created from ``---`` (target: zero
    rules), and deleting each table's conversion header row so the first content
    row becomes the first visible row. Every index-shifting operation is emitted
    in strictly descending document position so earlier (higher) indices stay
    valid as later ones are applied.
    """
    validate_manifest(manifest)
    tab_id, tab = get_tab(doc)
    body = tab["body"]["content"]
    tables = doc_tables(tab)
    manifest_table_specs = manifest_tables(manifest)

    # The imported doc may still carry a conversion header row per table, so its
    # row count is (content rows) or (content rows + 1).
    if len(tables) != len(manifest_table_specs):
        raise ContractError(
            f"Imported table count {len(tables)} does not match {len(manifest_table_specs)} approved tables"
        )

    # Collect (document_position, ops) so we can emit strictly bottom-first.
    edits: list[tuple[int, list[dict[str, Any]]]] = []

    # 1. Uppercase every band heading paragraph (length-preserving replacement).
    for section in manifest["sections"]:
        element = find_paragraph(body, section["source_label"])
        if section["source_label"] != section["band_label"]:
            start = element["startIndex"]
            end = element["endIndex"] - 1  # keep the trailing newline
            ops = [
                {"deleteContentRange": {"range": docs_range(tab_id, start, end)}},
                {"insertText": {"location": {"index": start, "tabId": tab_id}, "text": section["band_label"]}},
            ]
            edits.append((start, ops))

    # 2. Delete any native horizontal rules (want zero).
    for element in body:
        if "paragraph" not in element:
            continue
        if any("horizontalRule" in child for child in element["paragraph"].get("elements", [])):
            edits.append(
                (
                    element["startIndex"],
                    [{"deleteContentRange": {"range": docs_range(tab_id, element["startIndex"], element["endIndex"])}}],
                )
            )

    # 3. Per table: verify content binds to the manifest, then drop the
    #    conversion header row if the importer kept one.
    for table_element, spec in zip(tables, manifest_table_specs):
        rows = table_element["table"]["tableRows"]
        expected = spec["rows"]
        has_header = len(rows) == len(expected) + 1
        if len(rows) not in (len(expected), len(expected) + 1):
            raise ContractError(
                f"Imported {spec['kind']} table has {len(rows)} rows; expected {len(expected)}"
            )
        offset = 1 if has_header else 0
        for row, source in zip(rows[offset:], expected):
            if len(row["tableCells"]) != 2:
                raise ContractError(f"{spec['kind']} table rows must keep two cells")
            label = " ".join(_cell_visible_lines(row["tableCells"][0]))
            content = " ".join(_cell_visible_lines(row["tableCells"][1]))
            want_label = re.sub(r"\s+", " ", source["label"].strip())
            want_content = re.sub(r"\s+", " ", source["content"]["text"].strip())
            if label != want_label or content != want_content:
                raise ContractError(
                    f"Imported {spec['kind']} table content differs from approved manifest: {label!r}"
                )
        if has_header:
            edits.append(
                (
                    table_element["startIndex"],
                    [
                        {
                            "deleteTableRow": {
                                "tableCellLocation": {
                                    "tableStartLocation": {"index": table_element["startIndex"], "tabId": tab_id},
                                    "rowIndex": 0,
                                    "columnIndex": 0,
                                }
                            }
                        }
                    ],
                )
            )

    requests: list[dict[str, Any]] = []
    for _, ops in sorted(edits, key=lambda pair: pair[0], reverse=True):
        requests.extend(ops)
    return {"requests": requests}


# ---------------------------------------------------------------------------
# format: emit the exact Option 4 styling operations
# ---------------------------------------------------------------------------


def _visible_cell_paragraph(cell: dict[str, Any]) -> dict[str, Any]:
    elements = [element for element in cell_paragraphs(cell) if paragraph_text(element["paragraph"]).strip()]
    if len(elements) != 1:
        raise ContractError("Each normalized table cell must contain exactly one non-empty paragraph")
    return elements[0]


def _style_table(
    requests: list[dict[str, Any]],
    tab_id: str,
    table_element: dict[str, Any],
    spec: dict[str, Any],
    contract: dict[str, Any],
    colors: dict[str, dict[str, Any]],
) -> None:
    kind = spec["kind"]
    kind_spec = contract["tables"]["kinds"][kind]
    rows = table_element["table"]["tableRows"]
    if len(rows) != len(spec["rows"]):
        raise ContractError(f"{kind} table has {len(rows)} rows; expected {len(spec['rows'])} (normalize first)")
    table_start = table_element["startIndex"]
    padding = {"magnitude": contract["tables"]["cell_padding_pt"], "unit": "PT"}
    base_style = {
        "backgroundColor": colors["white"],
        "paddingTop": padding,
        "paddingBottom": padding,
        "paddingLeft": padding,
        "paddingRight": padding,
    }
    requests.append(
        update_cell(
            tab_id, table_start, 0, 0, base_style,
            "backgroundColor,paddingTop,paddingBottom,paddingLeft,paddingRight",
            row_span=len(rows), col_span=2,
        )
    )
    label_bg = kind_spec["label_column_background"]
    if label_bg.upper() != contract["colors"]["white"]:
        for row_index in range(len(rows)):
            requests.append(
                update_cell(
                    tab_id, table_start, row_index, 0,
                    {"backgroundColor": hex_color(label_bg)}, "backgroundColor",
                )
            )
    label_style = kind_spec["label_column_text"]
    content_style = kind_spec["content_column_text"]
    for row_index, (row, source) in enumerate(zip(rows, spec["rows"])):
        if len(row["tableCells"]) != 2:
            raise ContractError(f"{kind} table row {row_index} must keep two cells")
        left = _visible_cell_paragraph(row["tableCells"][0])
        right = _visible_cell_paragraph(row["tableCells"][1])
        style_paragraph(
            requests, tab_id, left,
            font=label_style["font"], size=label_style["size_pt"],
            bold=label_style.get("bold", False), color=hex_color(label_style["color"]),
            line_spacing=contract["spacing"]["table_line_spacing_percent"],
        )
        style_paragraph(
            requests, tab_id, right,
            font=content_style["font"], size=content_style["size_pt"],
            bold=content_style.get("bold", False), color=hex_color(content_style["color"]),
            line_spacing=contract["spacing"]["table_line_spacing_percent"],
        )
        apply_inline_styles(requests, tab_id, right, source["content"], link_color=hex_color(content_style["color"]))
    requests.extend(column_widths_request(tab_id, table_start, kind_spec["column_widths_pt"]))


def _style_list(
    requests: list[dict[str, Any]],
    tab_id: str,
    body: list[dict[str, Any]],
    items: list[dict[str, Any]],
    *,
    numbered: bool,
    contract: dict[str, Any],
    body_font: str,
    body_size: float,
    body_color: dict[str, Any],
) -> None:
    spacing = contract["spacing"]
    elements = [find_paragraph(body, item["text"]) for item in items]
    for element, item in zip(elements, items):
        style_paragraph(
            requests, tab_id, element, font=body_font, size=body_size, color=body_color,
            indent_start=spacing["list_indent_start_pt"], indent_first=spacing["list_indent_first_line_pt"],
        )
        apply_inline_styles(requests, tab_id, element, item, link_color=body_color)
    start = elements[0]["startIndex"]
    end = elements[-1]["endIndex"]
    requests.append(
        {
            "createParagraphBullets": {
                "range": docs_range(tab_id, start, end),
                "bulletPreset": NUMBERED_PRESET if numbered else BULLET_PRESET,
            }
        }
    )
    # Bullet creation resets indents; make the approved geometry the final op.
    requests.append(
        update_paragraph(
            tab_id, start, end,
            {
                "indentStart": {"magnitude": spacing["list_indent_start_pt"], "unit": "PT"},
                "indentFirstLine": {"magnitude": spacing["list_indent_first_line_pt"], "unit": "PT"},
                "lineSpacing": 115,
                "spaceAbove": {"magnitude": 0, "unit": "PT"},
                "spaceBelow": {"magnitude": 0, "unit": "PT"},
            },
            "indentStart,indentFirstLine,lineSpacing,spaceAbove,spaceBelow",
        )
    )


def build_format_requests(doc: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    """Generate exact Option 4 formatting requests for a normalized mod-guide doc."""
    validate_manifest(manifest)
    contract = load_contract()
    tab_id, tab = get_tab(doc)
    body = tab["body"]["content"]
    tables = doc_tables(tab)
    manifest_table_specs = manifest_tables(manifest)
    if len(tables) != len(manifest_table_specs):
        raise ContractError(
            f"Normalize the document first: {len(tables)} tables vs {len(manifest_table_specs)} approved"
        )

    colors = {name: hex_color(value) for name, value in contract["colors"].items()}
    spacing = contract["spacing"]
    requests: list[dict[str, Any]] = []

    # 1. Document style (page geometry).
    page = contract["page"]
    requests.append(
        {
            "updateDocumentStyle": {
                "documentStyle": {
                    "documentFormat": {"documentMode": page["document_mode"]},
                    "flipPageOrientation": False,
                    "pageSize": {
                        "width": {"magnitude": page["width_pt"], "unit": "PT"},
                        "height": {"magnitude": page["height_pt"], "unit": "PT"},
                    },
                    "marginTop": {"magnitude": page["margins_pt"]["top"], "unit": "PT"},
                    "marginBottom": {"magnitude": page["margins_pt"]["bottom"], "unit": "PT"},
                    "marginLeft": {"magnitude": page["margins_pt"]["left"], "unit": "PT"},
                    "marginRight": {"magnitude": page["margins_pt"]["right"], "unit": "PT"},
                    "marginHeader": {"magnitude": page["header_margin_pt"], "unit": "PT"},
                    "marginFooter": {"magnitude": page["footer_margin_pt"], "unit": "PT"},
                    # useCustomHeaderFooterMargins is output-only; Docs derives it.
                },
                "fields": "documentFormat.documentMode,flipPageOrientation,pageSize,marginTop,marginBottom,marginLeft,marginRight,marginHeader,marginFooter",
                "tabId": tab_id,
            }
        }
    )

    top = manifest["top"]
    body_font, body_size, _, _, body_color = _text_style(contract, "body")

    # 2. Opening paragraphs in document order.
    breadcrumb = find_paragraph(body, top["breadcrumb"]["text"])
    font, size, bold, italic, color = _text_style(contract, "breadcrumb")
    style_paragraph(
        requests, tab_id, breadcrumb, font=font, size=size, bold=bold, italic=italic, color=color,
        named_style="SUBTITLE", space_below=spacing["breadcrumb_space_below_pt"], keep_next=True,
    )

    title = find_paragraph(body, top["title"]["text"])
    font, size, bold, italic, color = _text_style(contract, "title")
    style_paragraph(
        requests, tab_id, title, font=font, size=size, bold=bold, italic=italic, color=color,
        named_style="TITLE", space_below=spacing["title_space_below_pt"], keep_next=True,
    )

    if top.get("phase_subtitle"):
        subtitle = find_paragraph(body, top["phase_subtitle"]["text"])
        font, size, bold, italic, color = _text_style(contract, "phase_subtitle")
        style_paragraph(
            requests, tab_id, subtitle, font=font, size=size, bold=bold, italic=italic, color=color,
            space_below=spacing["phase_subtitle_space_below_pt"], keep_next=True,
        )

    updated = find_paragraph(body, top["date"]["text"])
    font, size, bold, italic, color = _text_style(contract, "context_note")
    style_paragraph(
        requests, tab_id, updated, font=font, size=size, bold=bold, italic=italic, color=color,
        space_above=6, space_below=8,
    )

    # RACI bullets.
    raci_elements: list[dict[str, Any]] = []
    for item in top["raci"]:
        element = find_paragraph(body, item["text"])
        raci_elements.append(element)
        style_paragraph(
            requests, tab_id, element, font=body_font, size=body_size, color=body_color,
            space_above=12, space_below=12,
            indent_start=spacing["raci_indent_start_pt"], indent_first=spacing["raci_indent_first_line_pt"],
        )
        apply_inline_styles(requests, tab_id, element, item, link_color=body_color)
    raci_start, raci_end = raci_elements[0]["startIndex"], raci_elements[-1]["endIndex"]
    requests.append(
        {"createParagraphBullets": {"range": docs_range(tab_id, raci_start, raci_end), "bulletPreset": BULLET_PRESET}}
    )
    requests.append(
        update_paragraph(
            tab_id, raci_start, raci_end,
            {
                "indentStart": {"magnitude": spacing["raci_indent_start_pt"], "unit": "PT"},
                "indentFirstLine": {"magnitude": spacing["raci_indent_first_line_pt"], "unit": "PT"},
                "lineSpacing": 115,
                "spaceAbove": {"magnitude": 12, "unit": "PT"},
                "spaceBelow": {"magnitude": 12, "unit": "PT"},
            },
            "indentStart,indentFirstLine,lineSpacing,spaceAbove,spaceBelow",
        )
    )

    # Optional TEST ARTIFACT warning with full-paragraph shading.
    if top.get("warning"):
        warning = find_paragraph(body, top["warning"])
        style_paragraph(
            requests, tab_id, warning,
            font=contract["warning"]["font"], size=contract["warning"]["size_pt"],
            bold=contract["warning"]["bold"], color=hex_color(contract["warning"]["foreground"]),
            space_above=6, space_below=8, keep_next=True,
            shading=hex_color(contract["warning"]["background"]),
        )

    # 3. Parameters table.
    _style_table(requests, tab_id, tables[0], manifest["parameters"], contract, colors)

    # 4. Sections (bands, prose, lists, sub-phases, tables). Bind tables by order.
    table_cursor = 1
    section_font, section_size, section_bold, section_italic, section_color = _text_style(contract, "section_band")
    sub_font, sub_size, sub_bold, sub_italic, sub_color = _text_style(contract, "sub_phase_heading")

    def style_prose(element_text: str, inline: dict[str, Any]) -> None:
        element = find_paragraph(body, element_text)
        style_paragraph(requests, tab_id, element, font=body_font, size=body_size, color=body_color)
        apply_inline_styles(requests, tab_id, element, inline, link_color=body_color)

    def style_blocks(blocks: list[dict[str, Any]]) -> None:
        nonlocal table_cursor
        for block in blocks:
            if block["type"] == "prose":
                style_prose(block["inline"]["text"], block["inline"])
            elif block["type"] == "list":
                _style_list(
                    requests, tab_id, body, block["items"],
                    numbered=(block["kind"] == "debrief"),
                    contract=contract, body_font=body_font, body_size=body_size, body_color=body_color,
                )
            elif block["type"] == "table":
                _style_table(requests, tab_id, tables[table_cursor], block, contract, colors)
                table_cursor += 1
            elif block["type"] == "sub_phase":
                heading = find_paragraph(body, block["heading"]["text"])
                style_paragraph(
                    requests, tab_id, heading, font=sub_font, size=sub_size,
                    bold=sub_bold, italic=sub_italic, color=sub_color,
                    named_style="HEADING_3",
                    space_above=spacing["sub_phase_space_above_pt"],
                    space_below=spacing["sub_phase_space_below_pt"], keep_next=True,
                )
                apply_inline_styles(requests, tab_id, heading, block["heading"], link_color=sub_color)
                style_blocks(block["blocks"])

    for section in manifest["sections"]:
        band = find_paragraph(body, section["band_label"])
        style_paragraph(
            requests, tab_id, band, font=section_font, size=section_size,
            bold=section_bold, italic=section_italic, color=section_color,
            named_style="HEADING_2",
            space_above=spacing["band_space_above_pt"], space_below=spacing["band_space_below_pt"],
            keep_next=True, shading=colors["dark_green"],
        )
        style_blocks(section["blocks"])

    return {"requests": requests}


# ---------------------------------------------------------------------------
# Verifier
# ---------------------------------------------------------------------------


def _rgb(value: dict[str, Any] | None, *, default_black: bool = False) -> tuple[int, int, int] | None:
    if not value or "color" not in value:
        return (0, 0, 0) if default_black else None
    raw = value.get("color", {}).get("rgbColor", {})
    if not raw and default_black:
        return (0, 0, 0)
    return tuple(round(255 * raw.get(channel, 0)) for channel in ("red", "green", "blue"))


def _hex_tuple(value: str) -> tuple[int, int, int]:
    raw = value.lstrip("#")
    return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4))


def _named_text_styles(tab: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        item["namedStyleType"]: item.get("textStyle", {})
        for item in tab.get("namedStyles", {}).get("styles", [])
    }


def _effective_style(paragraph: dict[str, Any], run: dict[str, Any], named: dict[str, dict[str, Any]]) -> dict[str, Any]:
    style = dict(named.get("NORMAL_TEXT", {}))
    style.update(named.get(paragraph.get("paragraphStyle", {}).get("namedStyleType", "NORMAL_TEXT"), {}))
    style.update(run.get("textStyle", {}))
    return style


def _first_run(element: dict[str, Any]) -> dict[str, Any]:
    return next(
        child["textRun"]
        for child in element["paragraph"].get("elements", [])
        if "textRun" in child
    )


def _assert_text_style(element: dict[str, Any], named: dict[str, dict[str, Any]], expected: dict[str, Any]) -> None:
    style = _effective_style(element["paragraph"], _first_run(element), named)
    label = paragraph_text(element["paragraph"]).strip()
    if style.get("weightedFontFamily", {}).get("fontFamily") != expected["font"]:
        raise ContractError(f"Wrong font for {label!r}")
    if style.get("fontSize", {}).get("magnitude") != expected["size_pt"]:
        raise ContractError(f"Wrong font size for {label!r}")
    if style.get("bold", False) != expected.get("bold", False):
        raise ContractError(f"Wrong bold style for {label!r}")
    if style.get("italic", False) != expected.get("italic", False):
        raise ContractError(f"Wrong italic style for {label!r}")
    if _rgb(style.get("foregroundColor"), default_black=True) != _hex_tuple(expected["color"]):
        raise ContractError(f"Wrong text color for {label!r}")


def _assert_base_text_style(element: dict[str, Any], named: dict[str, dict[str, Any]], expected: dict[str, Any]) -> None:
    for child in element["paragraph"].get("elements", []):
        run = child.get("textRun")
        if run is None or not run.get("content", "").rstrip("\n"):
            continue
        style = _effective_style(element["paragraph"], run, named)
        label = paragraph_text(element["paragraph"]).strip()
        if style.get("weightedFontFamily", {}).get("fontFamily") != expected["font"]:
            raise ContractError(f"Wrong run font in {label!r}")
        if style.get("fontSize", {}).get("magnitude") != expected["size_pt"]:
            raise ContractError(f"Wrong run font size in {label!r}")
        if _rgb(style.get("foregroundColor"), default_black=True) != _hex_tuple(expected["color"]):
            raise ContractError(f"Wrong run color in {label!r}")


def _assert_inline_exact(
    element: dict[str, Any], item: dict[str, Any], named: dict[str, dict[str, Any]],
    *, base_bold: bool = False, base_italic: bool = False,
) -> None:
    text = item.get("text", "")
    units = utf16_offset(text, len(text))
    expected_bold = [base_bold] * units
    expected_italic = [base_italic] * units
    expected_links: list[str | None] = [None] * units
    for start, end in item.get("bold", []):
        expected_bold[utf16_offset(text, start) : utf16_offset(text, end)] = [True] * (
            utf16_offset(text, end) - utf16_offset(text, start)
        )
    for start, end in item.get("italic", []):
        expected_italic[utf16_offset(text, start) : utf16_offset(text, end)] = [True] * (
            utf16_offset(text, end) - utf16_offset(text, start)
        )
    for link in item.get("links", []):
        start = utf16_offset(text, link["start"])
        end = utf16_offset(text, link["end"])
        expected_links[start:end] = [link["url"]] * (end - start)

    covered = [False] * units
    base = element["startIndex"]
    for child in element["paragraph"].get("elements", []):
        run = child.get("textRun")
        if run is None:
            continue
        start = max(0, child["startIndex"] - base)
        end = min(units, child["endIndex"] - base)
        if end <= start:
            continue
        style = _effective_style(element["paragraph"], run, named)
        actual_bold = bool(style.get("bold", False))
        actual_italic = bool(style.get("italic", False))
        actual_link = (style.get("link") or {}).get("url")
        for offset in range(start, end):
            if actual_bold != expected_bold[offset]:
                raise ContractError(f"Inline bold mismatch in {text!r}")
            if actual_italic != expected_italic[offset]:
                raise ContractError(f"Inline italic mismatch in {text!r}")
            if actual_link != expected_links[offset]:
                raise ContractError(f"Inline link mismatch in {text!r}")
            covered[offset] = True
    if units and not all(covered):
        raise ContractError(f"Inline style coverage is incomplete in {text!r}")


def _magnitude(style: dict[str, Any], key: str, default: float = 0) -> float:
    return style.get(key, {}).get("magnitude", default)


def _assert_cell_padding(cell: dict[str, Any], expected: float) -> None:
    # Google Docs omits the default 5pt padding from read responses.
    style = cell.get("tableCellStyle", {})
    for key in ("paddingTop", "paddingBottom", "paddingLeft", "paddingRight"):
        if _magnitude(style, key, 5) != expected:
            raise ContractError(f"Wrong table cell {key}: {_magnitude(style, key, 5)}pt")


def _assert_paragraph_metrics(
    element: dict[str, Any], *, line_spacing: int, space_above: float = 0, space_below: float = 0,
    keep_next: bool | None = None, indent_start: float | None = None, indent_first: float | None = None,
) -> None:
    style = element["paragraph"].get("paragraphStyle", {})
    text = paragraph_text(element["paragraph"]).strip()
    if style.get("lineSpacing") != line_spacing:
        raise ContractError(f"Wrong line spacing for {text!r}")
    if _magnitude(style, "spaceAbove") != space_above or _magnitude(style, "spaceBelow") != space_below:
        raise ContractError(f"Wrong paragraph spacing for {text!r}")
    if keep_next is not None and bool(style.get("keepWithNext", False)) != keep_next:
        raise ContractError(f"Wrong keep-with-next setting for {text!r}")
    if indent_start is not None and _magnitude(style, "indentStart") != indent_start:
        raise ContractError(f"Wrong start indent for {text!r}")
    if indent_first is not None and _magnitude(style, "indentFirstLine") != indent_first:
        raise ContractError(f"Wrong first-line indent for {text!r}")


def _verify_table(
    table_element: dict[str, Any], spec: dict[str, Any], contract: dict[str, Any],
    named: dict[str, dict[str, Any]],
) -> None:
    kind = spec["kind"]
    kind_spec = contract["tables"]["kinds"][kind]
    rows = table_element["table"]["tableRows"]
    if len(rows) != len(spec["rows"]):
        raise ContractError(f"{kind} table has {len(rows)} rows; expected {len(spec['rows'])}")
    # Column widths per kind.
    properties = table_element["table"].get("tableStyle", {}).get("tableColumnProperties", [])
    actual_widths = [item.get("width", {}).get("magnitude") for item in properties]
    if actual_widths != kind_spec["column_widths_pt"]:
        raise ContractError(f"Wrong {kind} table widths: {actual_widths}")
    label_bg = _hex_tuple(kind_spec["label_column_background"])
    content_bg = _hex_tuple(contract["tables"]["body_cell_background"])
    for row_index, (row, source) in enumerate(zip(rows, spec["rows"])):
        if len(row["tableCells"]) != 2:
            raise ContractError(f"{kind} table row {row_index} must keep two cells")
        left, right = row["tableCells"]
        _assert_cell_padding(left, contract["tables"]["cell_padding_pt"])
        _assert_cell_padding(right, contract["tables"]["cell_padding_pt"])
        if _rgb(left.get("tableCellStyle", {}).get("backgroundColor")) != label_bg:
            raise ContractError(f"Wrong {kind} label background at row {row_index}")
        if _rgb(right.get("tableCellStyle", {}).get("backgroundColor")) != content_bg:
            raise ContractError(f"Wrong {kind} content background at row {row_index}")
        left_p = _visible_cell_paragraph(left)
        right_p = _visible_cell_paragraph(right)
        # Guide-specific rule: tables contain ONLY the label + read-aloud/question.
        if paragraph_text(left_p["paragraph"]).strip() != source["label"]:
            raise ContractError(f"{kind} table label mismatch: {paragraph_text(left_p['paragraph']).strip()!r}")
        if paragraph_text(right_p["paragraph"]).rstrip("\n") != source["content"]["text"]:
            raise ContractError(f"{kind} table content mismatch in row {row_index}")
        if "bullet" in left_p["paragraph"] or "bullet" in right_p["paragraph"]:
            raise ContractError(f"{kind} table row {row_index} must not contain a bullet")
        label_expected = dict(kind_spec["label_column_text"])
        _assert_text_style(left_p, named, label_expected)
        _assert_base_text_style(left_p, named, label_expected)
        content_expected = dict(kind_spec["content_column_text"])
        _assert_base_text_style(right_p, named, content_expected)
        _assert_inline_exact(right_p, source["content"], named)
        _assert_paragraph_metrics(left_p, line_spacing=contract["spacing"]["table_line_spacing_percent"])
        _assert_paragraph_metrics(right_p, line_spacing=contract["spacing"]["table_line_spacing_percent"])


def verify_document(doc: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    """Validate content and every machine-checkable Option 4 mod-guide invariant."""
    validate_manifest(manifest)
    contract = load_contract()
    _, tab = get_tab(doc)
    body = tab["body"]["content"]
    named = _named_text_styles(tab)
    tables = doc_tables(tab)
    manifest_table_specs = manifest_tables(manifest)
    if len(tables) != len(manifest_table_specs):
        raise ContractError(
            f"Final document has {len(tables)} tables; expected {len(manifest_table_specs)}"
        )

    # 1. Element sequence (content + hierarchy). No horizontal rule may survive.
    expected = expected_sequence(manifest)
    actual: list[str] = []
    for element in body:
        if "table" in element:
            actual.append("<TABLE>")
        elif "paragraph" in element:
            if any("horizontalRule" in child for child in element["paragraph"].get("elements", [])):
                raise ContractError("Native horizontal rule found; mod-guide bands replace all rules")
            text = paragraph_text(element["paragraph"]).strip()
            if text:
                actual.append(text)
    if actual != expected:
        raise ContractError("Document hierarchy does not match the approved mod-guide manifest")

    # 2. Guide-specific terminal rule: the guide ends at Post-Session Debrief.
    band_labels = [section["band_label"] for section in manifest["sections"]]
    if band_labels[-1] != TERMINAL_BAND:
        raise ContractError(f"The guide must end at {TERMINAL_BAND!r}")
    debrief_band_index = len(actual) - 1
    # Find the terminal band position in the actual sequence and ensure no table follows.
    terminal_pos = max(i for i, value in enumerate(actual) if value == TERMINAL_BAND)
    if "<TABLE>" in actual[terminal_pos:]:
        raise ContractError("A table appears in the Post-Session Debrief; it must be a numbered list, not a table")
    _ = debrief_band_index

    # 3. Document style.
    document_style = tab.get("documentStyle", {})
    if document_style.get("documentFormat", {}).get("documentMode") != contract["page"]["document_mode"]:
        raise ContractError(f"Document mode is not {contract['page']['document_mode']}")
    if bool(document_style.get("useCustomHeaderFooterMargins", False)) != contract["page"]["use_custom_header_footer_margins"]:
        raise ContractError("Custom header/footer margins are not enabled")
    margins = contract["page"]["margins_pt"]
    for key, value in (
        ("marginTop", margins["top"]),
        ("marginBottom", margins["bottom"]),
        ("marginLeft", margins["left"]),
        ("marginRight", margins["right"]),
        ("marginHeader", contract["page"]["header_margin_pt"]),
        ("marginFooter", contract["page"]["footer_margin_pt"]),
    ):
        if document_style.get(key, {}).get("magnitude") != value:
            raise ContractError(f"{key} is not {value}pt")
    width = document_style.get("pageSize", {}).get("width", {}).get("magnitude")
    height = document_style.get("pageSize", {}).get("height", {}).get("magnitude")
    if document_style.get("flipPageOrientation"):
        width, height = height, width
    if (width, height) != (contract["page"]["width_pt"], contract["page"]["height_pt"]):
        raise ContractError(f"Page is not landscape letter: {(width, height)}")

    # 4. Opening typography.
    top = manifest["top"]
    breadcrumb = find_paragraph(body, top["breadcrumb"]["text"])
    _assert_text_style(breadcrumb, named, contract["typography"]["breadcrumb"])
    _assert_base_text_style(breadcrumb, named, contract["typography"]["breadcrumb"])
    _assert_paragraph_metrics(
        breadcrumb, line_spacing=115, space_below=contract["spacing"]["breadcrumb_space_below_pt"], keep_next=True
    )
    title = find_paragraph(body, top["title"]["text"])
    _assert_text_style(title, named, contract["typography"]["title"])
    _assert_paragraph_metrics(
        title, line_spacing=115, space_below=contract["spacing"]["title_space_below_pt"], keep_next=True
    )
    if top.get("phase_subtitle"):
        subtitle = find_paragraph(body, top["phase_subtitle"]["text"])
        _assert_text_style(subtitle, named, contract["typography"]["phase_subtitle"])
    date = find_paragraph(body, top["date"]["text"])
    _assert_text_style(date, named, contract["typography"]["context_note"])

    for item in top["raci"]:
        element = find_paragraph(body, item["text"])
        if "bullet" not in element["paragraph"]:
            raise ContractError(f"RACI item is not a native bullet: {item['role']}")
        _assert_base_text_style(element, named, contract["typography"]["body"])
        _assert_inline_exact(element, item, named)
        _assert_paragraph_metrics(
            element, line_spacing=115, space_above=12, space_below=12,
            indent_start=contract["spacing"]["raci_indent_start_pt"],
            indent_first=contract["spacing"]["raci_indent_first_line_pt"],
        )

    if top.get("warning"):
        warning = find_paragraph(body, top["warning"])
        expected_warning = {
            "font": contract["warning"]["font"],
            "size_pt": contract["warning"]["size_pt"],
            "bold": contract["warning"]["bold"],
            "color": contract["warning"]["foreground"],
        }
        _assert_text_style(warning, named, expected_warning)
        _assert_base_text_style(warning, named, expected_warning)
        shading = warning["paragraph"].get("paragraphStyle", {}).get("shading", {}).get("backgroundColor")
        if _rgb(shading) != _hex_tuple(contract["warning"]["background"]):
            raise ContractError("TEST ARTIFACT warning does not use full-paragraph pale-yellow shading")

    # 5. Section bands + sub-phase headings + prose + lists.
    def verify_blocks(blocks: list[dict[str, Any]]) -> None:
        for block in blocks:
            if block["type"] == "prose":
                element = find_paragraph(body, block["inline"]["text"])
                if "bullet" in element["paragraph"]:
                    raise ContractError(f"Prose line rendered as a bullet: {block['inline']['text']!r}")
                _assert_base_text_style(element, named, contract["typography"]["body"])
                _assert_inline_exact(element, block["inline"], named)
                _assert_paragraph_metrics(element, line_spacing=115)
            elif block["type"] == "list":
                for item in block["items"]:
                    element = find_paragraph(body, item["text"])
                    if "bullet" not in element["paragraph"]:
                        raise ContractError(f"List item is not a native list paragraph: {item['text']!r}")
                    _assert_base_text_style(element, named, contract["typography"]["body"])
                    _assert_inline_exact(element, item, named)
                    _assert_paragraph_metrics(
                        element, line_spacing=115,
                        indent_start=contract["spacing"]["list_indent_start_pt"],
                        indent_first=contract["spacing"]["list_indent_first_line_pt"],
                    )
            elif block["type"] == "sub_phase":
                heading = find_paragraph(body, block["heading"]["text"])
                _assert_text_style(heading, named, contract["typography"]["sub_phase_heading"])
                _assert_paragraph_metrics(
                    heading, line_spacing=115,
                    space_above=contract["spacing"]["sub_phase_space_above_pt"],
                    space_below=contract["spacing"]["sub_phase_space_below_pt"], keep_next=True,
                )
                verify_blocks(block["blocks"])
            # table blocks are verified separately, by document order, below.

    for section in manifest["sections"]:
        band = find_paragraph(body, section["band_label"])
        _assert_text_style(band, named, contract["typography"]["section_band"])
        _assert_base_text_style(band, named, contract["typography"]["section_band"])
        _assert_paragraph_metrics(
            band, line_spacing=115,
            space_above=contract["spacing"]["band_space_above_pt"],
            space_below=contract["spacing"]["band_space_below_pt"], keep_next=True,
        )
        shading = band["paragraph"].get("paragraphStyle", {}).get("shading", {}).get("backgroundColor")
        if _rgb(shading) != _hex_tuple(contract["colors"]["dark_green"]):
            raise ContractError(f"Section band {section['band_label']!r} is missing its dark-green shading")
        verify_blocks(section["blocks"])

    # 6. Every table, in document order (guide-specific "questions only" binding).
    for table_element, spec in zip(tables, manifest_table_specs):
        _verify_table(table_element, spec, contract, named)

    return [
        "Option 4 page geometry, opening typography, and RACI bullets",
        "dark-green section bands with white serif labels and preserved outline",
        "parameters / consent / question tables with correct widths and label columns",
        "tables contain only labels and read-aloud/question text (no probes or notes)",
        f"guide structure ends at {TERMINAL_BAND} with zero horizontal rules",
    ]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def write_json(path: str | Path, value: dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True)

    manifest = subparsers.add_parser("manifest", help="Parse approved Markdown into a build manifest")
    manifest.add_argument("markdown")
    manifest.add_argument("output")

    normalize = subparsers.add_parser("normalize", help="Generate cleanup/binding requests after import")
    normalize.add_argument("document_json")
    normalize.add_argument("manifest_json")
    normalize.add_argument("output")

    format_parser = subparsers.add_parser("format", help="Generate exact Option 4 formatting requests")
    format_parser.add_argument("document_json")
    format_parser.add_argument("manifest_json")
    format_parser.add_argument("output")

    verify = subparsers.add_parser("verify", help="Verify final content and machine-checkable styling")
    verify.add_argument("document_json")
    verify.add_argument("manifest_json")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = cli().parse_args(argv)
    if args.command == "manifest":
        markdown = Path(args.markdown).read_text(encoding="utf-8")
        value = parse_markdown(markdown)
        write_json(args.output, value)
        print(
            f"PASS: parsed {len(value['sections'])} sections, "
            f"{len(manifest_tables(value))} tables, and four RACI roles"
        )
        return 0

    doc = json.loads(Path(args.document_json).read_text(encoding="utf-8"))
    manifest = json.loads(Path(args.manifest_json).read_text(encoding="utf-8"))
    if args.command == "normalize":
        payload = build_normalize_requests(doc, manifest)
        write_json(args.output, payload)
        print(f"PASS: generated {len(payload['requests'])} normalization requests")
        return 0
    if args.command == "format":
        payload = build_format_requests(doc, manifest)
        write_json(args.output, payload)
        print(f"PASS: generated {len(payload['requests'])} Option 4 formatting requests")
        return 0
    if args.command == "verify":
        checks = verify_document(doc, manifest)
        for check in checks:
            print(f"PASS: {check}")
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ContractError, KeyError, IndexError, StopIteration) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
