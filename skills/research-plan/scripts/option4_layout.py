#!/usr/bin/env python3
"""Build and verify the exact Option 4 — Leadership Google Docs layout.

Pipeline:
    option4_layout.py manifest APPROVED.md manifest.json
    option4_layout.py normalize imported-doc.json manifest.json normalize-batch.json \
        --required-revision-id IMPORTED_REVISION_ID
    # Apply batch and re-fetch the document.
    option4_layout.py format normalized-doc.json manifest.json format-batch.json \
        --required-revision-id NORMALIZED_REVISION_ID
    # Apply batch and re-fetch the document.
    option4_layout.py verify final-doc.json manifest.json

The script only uses the Python standard library. Batch files use the native
Google Docs API request schema and can be applied through any equivalent
write-capable integration. Normalize and format inputs must carry the fresh
document `revisionId`; a supplied `--required-revision-id` must match it.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONTRACT_PATH = SKILL_DIR / "references" / "option4-style-contract.json"
TAB_ID_FALLBACK = "t.0"
SECTIONS = (
    "KEY INFORMATION",
    "PROJECT DETAILS",
    "DELIVERABLES & NEXT STEPS",
    "APPENDIX",
)
RACI_ROLES = ("Responsible", "Accountable", "Consulted", "Informed")
KEY_INFORMATION_ROWS = (
    "Background",
    "Existing insights",
    "Objectives",
    "Key research questions",
    "Hypotheses",
    "What decisions will be made with this research?",
)
PROJECT_CORE_ROWS = (
    "Method & approach",
    "What does success look like?",
    "Dependencies & guardrails",
)
DELIVERABLE_ROWS = ("Deliverables", "Timeline", "Next steps")
WARNING = "⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable."


class ContractError(ValueError):
    """Raised when the document cannot satisfy the Option 4 contract."""


def load_contract() -> dict[str, Any]:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    table_total = round(sum(contract["tables"]["column_widths_pt"]), 3)
    usable_width = round(
        contract["page"]["width_pt"]
        - contract["page"]["margins_pt"]["left"]
        - contract["page"]["margins_pt"]["right"],
        3,
    )
    if table_total != contract["tables"]["total_width_pt"]:
        raise ContractError("Option 4 table-width tokens are internally inconsistent")
    if round(table_total - usable_width, 3) != contract["tables"]["intentional_text_area_overflow_pt"]:
        raise ContractError("Option 4 intentional table overflow token is inconsistent")
    return contract


def manifest_digest(manifest: dict[str, Any]) -> str:
    payload = {key: value for key, value in manifest.items() if key != "manifest_sha256"}
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def validate_manifest(manifest: dict[str, Any]) -> None:
    contract = load_contract()
    if manifest.get("contract") != contract["name"]:
        raise ContractError("Manifest is not for the Option 4 — Leadership contract")
    if manifest.get("contract_version") != contract["version"]:
        raise ContractError("Manifest contract version is stale")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest.get("markdown_sha256", "")):
        raise ContractError("Manifest is missing its approved-Markdown SHA-256")
    if manifest.get("manifest_sha256") != manifest_digest(manifest):
        raise ContractError("Manifest content has changed since approved Markdown was parsed")


def parse_inline(markdown: str) -> dict[str, Any]:
    """Parse the small inline Markdown subset used by research plans."""
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
                # Pair this "[" with its own balanced "]"; a literal bracket earlier in
                # the line must not borrow the "](" of a later link.
                close = -1
                depth = 0
                cursor = i
                while cursor < len(value):
                    if value[cursor] == "\\":
                        cursor += 2
                        continue
                    if value[cursor] == "[":
                        depth += 1
                    elif value[cursor] == "]":
                        depth -= 1
                        if depth == 0:
                            close = cursor
                            break
                    cursor += 1
                if close >= 0 and value.startswith("](", close):
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


def table_after(lines: list[str], heading_index: int) -> tuple[list[list[str]], int]:
    start = next(
        (i for i in range(heading_index + 1, len(lines)) if lines[i].strip().startswith("|")),
        None,
    )
    if start is None:
        raise ContractError(f"No table found after {lines[heading_index]!r}")
    raw_rows: list[list[str]] = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw_rows.append(split_markdown_row(lines[i]))
        i += 1
    return raw_rows, i


def split_cell_items(raw: str) -> tuple[bool, list[dict[str, Any]]]:
    value = raw.strip()
    bulleted = value.startswith("- ")
    if bulleted:
        value = value[2:]
        chunks = re.split(r"(?:<br\s*/?>\s*|\n)-\s+", value)
    elif value:
        chunks = [value]
    else:
        chunks = []
    return bulleted, [parse_inline(chunk) for chunk in chunks if chunk.strip()]


def _strip_wrapping_italics(value: str) -> str:
    stripped = value.strip()
    if len(stripped) >= 2 and stripped.startswith("*") and stripped.endswith("*"):
        return stripped[1:-1].strip()
    return stripped


def parse_markdown(markdown: str) -> dict[str, Any]:
    """Parse an approved Option 4 intermediate Markdown document."""
    lines = markdown.splitlines()
    nonempty = [i for i, line in enumerate(lines) if line.strip() and not line.lstrip().startswith("<!--")]
    if not nonempty:
        raise ContractError("Approved Markdown is empty")

    timeline_heading = next((i for i, line in enumerate(lines) if line.strip() == "# Research Timeline"), None)
    overview_heading = next((i for i, line in enumerate(lines) if line.strip() == "# Project Plan Overview"), None)
    if timeline_heading is None or overview_heading is None or timeline_heading >= overview_heading:
        raise ContractError("Markdown must contain Research Timeline before Project Plan Overview")

    title_index = next(
        (
            i
            for i in range(timeline_heading)
            if lines[i].startswith("# ") and lines[i].strip() not in ("# Research Timeline", "# Project Plan Overview")
        ),
        None,
    )
    if title_index is None:
        raise ContractError("Missing research-plan title")
    breadcrumb_index = next((i for i in nonempty if i < title_index), None)
    if breadcrumb_index is None:
        raise ContractError("Missing breadcrumb before title")

    updated_index = next((i for i in range(title_index + 1, timeline_heading) if lines[i].strip().startswith("Last updated:")), None)
    if updated_index is None:
        raise ContractError("Missing Last updated line")

    raci: list[dict[str, Any]] = []
    raci_indices: list[int] = []
    raci_pattern = re.compile(r"^-\s+\*\*(Responsible|Accountable|Consulted|Informed):\*\*\s*(.*)$")
    for i in range(updated_index + 1, timeline_heading):
        match = raci_pattern.match(lines[i].strip())
        if match:
            role, remainder = match.groups()
            item = parse_inline(f"**{role}:** {remainder}")
            item["role"] = role
            raci.append(item)
            raci_indices.append(i)
    if [item["role"] for item in raci] != list(RACI_ROLES):
        raise ContractError("RACI must contain Responsible, Accountable, Consulted, and Informed in order")

    warning_index = next(
        (
            i
            for i in range(updated_index + 1, timeline_heading)
            if parse_inline(lines[i].strip().removeprefix(">").strip())["text"] == WARNING
        ),
        None,
    )
    notes: list[dict[str, Any]] = []
    after_opening = (warning_index if warning_index is not None else raci_indices[-1]) + 1
    for i in range(after_opening, timeline_heading):
        value = lines[i].strip()
        if value and value != "---":
            notes.append(parse_inline(_strip_wrapping_italics(value)))

    timeline_rows_raw, timeline_end = table_after(lines, timeline_heading)
    if len(timeline_rows_raw) < 2 or not is_separator_row(timeline_rows_raw[1]):
        raise ContractError("Research Timeline must be a Markdown table with a separator row")
    timeline_rows = timeline_rows_raw[:1] + timeline_rows_raw[2:]
    if len(timeline_rows) != 5 or any(len(row) != 2 for row in timeline_rows):
        raise ContractError("Research Timeline must contain one header plus four milestone rows")
    timeline = [[parse_inline(cell) for cell in row] for row in timeline_rows]
    table_contract = load_contract()["tables"]
    expected_header = table_contract["timeline_header"]
    if [cell["text"] for cell in timeline[0]] != expected_header:
        raise ContractError(
            f"Research Timeline header must be {' | '.join(expected_header)!r}"
        )
    label_pattern = re.compile(table_contract["timeline_left_label_pattern"])
    left_maximum = table_contract["timeline_left_cell_max_characters"]
    right_maximum = table_contract["timeline_right_cell_max_characters"]
    for row in timeline[1:]:
        if not label_pattern.match(row[0]["text"]):
            raise ContractError(
                "Leadership timeline label must start with its timing, as in "
                f"'Week 1: Setup & rubric': {row[0]['text']!r}"
            )
        if len(row[0]["text"]) > left_maximum:
            raise ContractError(
                f"Leadership timeline label exceeds {left_maximum} characters: {row[0]['text']!r}"
            )
        if len(row[1]["text"]) > right_maximum:
            raise ContractError(
                f"Leadership timeline milestone exceeds {right_maximum} characters: {row[1]['text']!r}"
            )

    timeline_note = None
    for i in range(timeline_end, overview_heading):
        value = lines[i].strip()
        if value and value != "---":
            timeline_note = parse_inline(_strip_wrapping_italics(value))
            break
    if timeline_note is None:
        raise ContractError("Missing one-sentence timing note after Research Timeline")

    overview_rows_raw, _ = table_after(lines, overview_heading)
    if len(overview_rows_raw) < 3 or not is_separator_row(overview_rows_raw[1]):
        raise ContractError("Project Plan Overview must be a Markdown table with a conversion header")
    if len(overview_rows_raw[0]) != 2:
        raise ContractError("Project Plan Overview must have two columns")

    rows: list[dict[str, Any]] = []
    for cells in overview_rows_raw[2:]:
        if len(cells) != 2:
            raise ContractError(f"Overview row must have two cells: {cells!r}")
        label = parse_inline(cells[0])["text"]
        bulleted, items = split_cell_items(cells[1])
        rows.append(
            {
                "label": label,
                "items": items,
                "bulleted": bulleted,
                "section": label in SECTIONS,
            }
        )

    labels = [row["label"] for row in rows]
    if len(labels) != len(set(labels)):
        raise ContractError("Project Plan Overview contains a duplicate row label")
    section_positions = [labels.index(section) if section in labels else -1 for section in SECTIONS]
    if any(position < 0 for position in section_positions) or section_positions != sorted(section_positions):
        raise ContractError("The four Option 4 section rows are missing or out of order")
    key_index, project_index, deliverable_index, appendix_index = section_positions
    if labels[:key_index] != ["Topic", "TL;DR summary of findings"]:
        raise ContractError("Topic and TL;DR summary of findings must be the first two overview rows")
    if labels[key_index + 1 : project_index] != list(KEY_INFORMATION_ROWS):
        raise ContractError("Key Information rows are missing or out of canonical order")
    project_rows = labels[project_index + 1 : deliverable_index]
    if not project_rows or project_rows[0] != PROJECT_CORE_ROWS[0]:
        raise ContractError("Project Details must begin with Method & approach")
    if project_rows[-2:] != list(PROJECT_CORE_ROWS[1:]):
        raise ContractError(
            "Project Details must end with What does success look like? and Dependencies & guardrails"
        )
    if any(row not in project_rows for row in PROJECT_CORE_ROWS):
        raise ContractError("Project Details is missing a core row")
    if labels[deliverable_index + 1 : appendix_index] != list(DELIVERABLE_ROWS):
        raise ContractError("Deliverables & Next Steps rows are missing or out of canonical order")
    if labels[appendix_index:] != ["APPENDIX", "Additional UXR documents", "Resources from XFN"]:
        raise ContractError("Appendix must end with exactly the two approved document rows")
    for row in rows:
        if row["section"] and row["items"]:
            raise ContractError(f"Section row {row['label']!r} must not contain body content")
        if not row["section"] and not row["items"]:
            raise ContractError(f"Overview row {row['label']!r} must contain approved content")

    manifest = {
        "contract": "Option 4 — Leadership",
        "contract_version": load_contract()["version"],
        "markdown_sha256": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "top": {
            "breadcrumb": parse_inline(lines[breadcrumb_index].strip()),
            "title": parse_inline(lines[title_index][2:].strip()),
            "updated": parse_inline(lines[updated_index].strip()),
            "raci": raci,
            "warning": WARNING if warning_index is not None else None,
            "notes": notes,
        },
        "timeline": timeline,
        "timeline_note": timeline_note,
        "rows": rows,
    }
    manifest["manifest_sha256"] = manifest_digest(manifest)
    return manifest


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
        raise ContractError("Option 4 formatter requires one active content tab")
    tab_id = tabs[0].get("tabProperties", {}).get("tabId", TAB_ID_FALLBACK)
    return tab_id, tabs[0]["documentTab"]


def doc_tables(tab: dict[str, Any]) -> list[dict[str, Any]]:
    return [element for element in tab["body"]["content"] if "table" in element]


def output_label(label: str) -> str:
    if label == "Topic":
        return "TOPIC"
    if label == "TL;DR summary of findings":
        return "TL;DR SUMMARY OF FINDINGS"
    return label


def normalized_visible_items(cell: dict[str, Any]) -> list[str]:
    """Return importer-independent visible paragraphs for manifest binding."""
    values: list[str] = []
    for element in cell_paragraphs(cell):
        content = paragraph_text(element["paragraph"]).replace("<br>", "\n")
        for line in content.splitlines():
            line = re.sub(r"^(?:[-*•]\s+|\d+[.)]\s+)", "", line.strip())
            line = re.sub(r"\s+", " ", line)
            if line:
                values.append(line)
    return values


def replace_target(targets: list[tuple[int, list[dict[str, Any]]]], tab_id: str, start: int, end: int, value: str) -> None:
    operations: list[dict[str, Any]] = []
    if end > start:
        operations.append(
            {
                "deleteContentRange": {
                    "range": {"startIndex": start, "endIndex": end, "tabId": tab_id}
                }
            }
        )
    if value:
        operations.append(
            {
                "insertText": {
                    "location": {"index": start, "tabId": tab_id},
                    "text": value,
                }
            }
        )
    targets.append((start, operations))


def _batch_payload(
    requests: list[dict[str, Any]],
    required_revision_id: str | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {"requests": requests}
    if required_revision_id is None:
        return payload
    if not isinstance(required_revision_id, str) or not required_revision_id.strip():
        raise ContractError("Required revision ID must be a non-empty string")
    payload["writeControl"] = {"requiredRevisionId": required_revision_id.strip()}
    return payload


def resolve_required_revision_id(
    doc: dict[str, Any],
    supplied_revision_id: str | None,
    *,
    require: bool = False,
) -> str | None:
    snapshot_revision_id = doc.get("revisionId")
    if snapshot_revision_id is not None:
        if not isinstance(snapshot_revision_id, str) or not snapshot_revision_id.strip():
            raise ContractError("Document snapshot revision ID must be a non-empty string")
        snapshot_revision_id = snapshot_revision_id.strip()
    elif require:
        raise ContractError(
            "Document snapshot revision ID is missing; fetch a fresh document snapshot before generating a write batch"
        )

    if supplied_revision_id is not None:
        if not isinstance(supplied_revision_id, str) or not supplied_revision_id.strip():
            raise ContractError("Required revision ID must be a non-empty string")
        resolved = supplied_revision_id.strip()
        if snapshot_revision_id is not None and resolved != snapshot_revision_id:
            raise ContractError(
                "Supplied revision ID does not match the input document snapshot"
            )
    else:
        resolved = snapshot_revision_id

    return resolved


def build_normalize_requests(
    doc: dict[str, Any],
    manifest: dict[str, Any],
    *,
    required_revision_id: str | None = None,
) -> dict[str, Any]:
    """Rebuild imported table-cell text and remove the Markdown conversion header."""
    validate_manifest(manifest)
    resolved_revision_id = resolve_required_revision_id(
        doc,
        required_revision_id,
        require=True,
    )
    tab_id, tab = get_tab(doc)
    tables = doc_tables(tab)
    if len(tables) != 2:
        raise ContractError(f"Expected two tables; found {len(tables)}")
    timeline_table, overview_table = tables
    timeline_rows = timeline_table["table"]["tableRows"]
    if len(timeline_rows) != 5:
        raise ContractError("Timeline table must contain five rows")

    expected_overview = len(manifest["rows"])
    actual_overview = len(overview_table["table"]["tableRows"])
    has_conversion_header = actual_overview == expected_overview + 1
    if actual_overview not in (expected_overview, expected_overview + 1):
        raise ContractError(
            f"Overview table row count {actual_overview} does not match {expected_overview} approved rows"
        )
    row_offset = 1 if has_conversion_header else 0
    if has_conversion_header:
        header_cells = overview_table["table"]["tableRows"][0]["tableCells"]
        header_text = [
            paragraph_text(cell_paragraphs(cell)[0]["paragraph"]).strip()
            for cell in header_cells
        ]
        if header_text != ["Section / element", "Approved content"]:
            raise ContractError(f"Unexpected overview conversion header: {header_text!r}")
    targets: list[tuple[int, list[dict[str, Any]]]] = []

    # Do not rewrite content before the overview table in this batch. A length
    # change there would invalidate the overview tableStartLocation used by the
    # structural operations below. The import must preserve timeline text.
    for row, manifest_row in zip(timeline_rows, manifest["timeline"]):
        if len(row["tableCells"]) != 2:
            raise ContractError("Timeline rows must keep two physical cells")
        for cell, item in zip(row["tableCells"], manifest_row):
            actual = "\n".join(
                paragraph_text(paragraph["paragraph"]).strip()
                for paragraph in cell_paragraphs(cell)
                if paragraph_text(paragraph["paragraph"]).strip()
            )
            if actual != item["text"]:
                raise ContractError(
                    "Imported leadership timeline text differs from approved Markdown; "
                    "re-import it before normalization"
                )

    raw_overview_rows = overview_table["table"]["tableRows"]
    for row, source in zip(raw_overview_rows[row_offset:], manifest["rows"]):
        if not row["tableCells"]:
            raise ContractError("Overview row has no cells")
        left = row["tableCells"][0]
        imported_labels = normalized_visible_items(left)
        approved_labels = {source["label"].casefold(), output_label(source["label"]).casefold()}
        if len(imported_labels) != 1 or imported_labels[0].casefold() not in approved_labels:
            raise ContractError(
                f"Imported overview label differs from manifest: {imported_labels!r} vs {source['label']!r}"
            )
        if len(row["tableCells"]) >= 2:
            imported_items = normalized_visible_items(row["tableCells"][1])
            approved_items = [re.sub(r"\s+", " ", item["text"].strip()) for item in source["items"]]
            if imported_items != approved_items:
                raise ContractError(
                    f"Imported content for {source['label']!r} differs from approved manifest"
                )
        elif not source["section"]:
            raise ContractError(f"Non-section row {source['label']!r} is physically merged")
        left_ps = cell_paragraphs(left)
        replace_target(
            targets,
            tab_id,
            left_ps[0]["startIndex"],
            left_ps[-1]["endIndex"] - 1,
            output_label(source["label"]),
        )
        if len(row["tableCells"]) >= 2:
            right = row["tableCells"][1]
            right_ps = cell_paragraphs(right)
            replace_target(
                targets,
                tab_id,
                right_ps[0]["startIndex"],
                right_ps[-1]["endIndex"] - 1,
                "\n".join(item["text"] for item in source["items"]),
            )

    requests: list[dict[str, Any]] = []
    for _, operations in sorted(targets, key=lambda pair: pair[0], reverse=True):
        requests.extend(operations)

    table_start = overview_table["startIndex"]
    if has_conversion_header:
        requests.append(
            {
                "deleteTableRow": {
                    "tableCellLocation": {
                        "tableStartLocation": {"index": table_start, "tabId": tab_id},
                        "rowIndex": 0,
                        "columnIndex": 0,
                    }
                }
            }
        )

    for index, source in enumerate(manifest["rows"]):
        raw_index = index + row_offset
        row = raw_overview_rows[raw_index]
        merged = len(row["tableCells"]) == 1 or row["tableCells"][0].get("tableCellStyle", {}).get("columnSpan", 1) > 1
        if source["section"] and merged:
            requests.append(
                {
                    "unmergeTableCells": {
                        "tableRange": {
                            "tableCellLocation": {
                                "tableStartLocation": {"index": table_start, "tabId": tab_id},
                                "rowIndex": index,
                                "columnIndex": 0,
                            },
                            "rowSpan": 1,
                            "columnSpan": 2,
                        }
                    }
                }
            )

    return _batch_payload(requests, resolved_revision_id)


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


def update_cell(tab_id: str, table_start: int, row: int, col: int, style: dict[str, Any], fields: str, *, row_span: int = 1, col_span: int = 1) -> dict[str, Any]:
    return {
        "updateTableCellStyle": {
            "tableRange": cell_range(tab_id, table_start, row, col, row_span, col_span),
            "tableCellStyle": style,
            "fields": fields,
        }
    }


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


def find_paragraph(body: list[dict[str, Any]], exact: str) -> dict[str, Any]:
    for element in body:
        if "paragraph" in element and paragraph_text(element["paragraph"]).strip() == exact:
            return element
    raise ContractError(f"Paragraph not found: {exact!r}")


def utf16_offset(text: str, character_offset: int) -> int:
    """Convert a Python character offset to the UTF-16 units used by Docs indices."""
    return len(text[:character_offset].encode("utf-16-le")) // 2


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


def build_format_requests(
    doc: dict[str, Any],
    manifest: dict[str, Any],
    *,
    required_revision_id: str | None = None,
) -> dict[str, Any]:
    """Generate exact Option 4 formatting requests for a normalized document."""
    validate_manifest(manifest)
    resolved_revision_id = resolve_required_revision_id(
        doc,
        required_revision_id,
        require=True,
    )
    contract = load_contract()
    tab_id, tab = get_tab(doc)
    body = tab["body"]["content"]
    tables = doc_tables(tab)
    if len(tables) != 2:
        raise ContractError("Formatting requires exactly the timeline and overview tables")
    timeline, overview = tables
    if len(timeline["table"]["tableRows"]) != 5:
        raise ContractError("Timeline must have five rows before formatting")
    if len(overview["table"]["tableRows"]) != len(manifest["rows"]):
        raise ContractError("Normalize the overview table before formatting")

    colors = {name: hex_color(value) for name, value in contract["colors"].items()}
    spacing = contract["spacing"]
    requests: list[dict[str, Any]] = []

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
                    # useCustomHeaderFooterMargins is output-only; Docs derives it from these values.
                },
                "fields": "documentFormat.documentMode,flipPageOrientation,pageSize,marginTop,marginBottom,marginLeft,marginRight,marginHeader,marginFooter",
                "tabId": tab_id,
            }
        }
    )

    top = manifest["top"]
    breadcrumb = find_paragraph(body, top["breadcrumb"]["text"])
    title = find_paragraph(body, top["title"]["text"])
    updated = find_paragraph(body, top["updated"]["text"])
    research_heading = find_paragraph(body, "Research Timeline")
    timeline_note = find_paragraph(body, manifest["timeline_note"]["text"])
    overview_heading = find_paragraph(body, "Project Plan Overview")

    font, size, bold, italic, color = _text_style(contract, "breadcrumb")
    style_paragraph(
        requests, tab_id, breadcrumb, font=font, size=size, bold=bold, italic=italic,
        color=color, named_style="SUBTITLE", line_spacing=115,
        space_below=spacing["breadcrumb_space_below_pt"], keep_next=True,
    )
    font, size, bold, italic, color = _text_style(contract, "title")
    style_paragraph(
        requests, tab_id, title, font=font, size=size, bold=bold, italic=italic,
        color=color, named_style="TITLE", line_spacing=115,
        space_below=spacing["title_space_below_pt"], keep_next=True,
    )
    body_font, body_size, _, _, body_color = _text_style(contract, "body")
    style_paragraph(
        requests, tab_id, updated, font=body_font, size=body_size, color=body_color,
        space_above=12, space_below=12,
    )

    raci_elements: list[dict[str, Any]] = []
    for item in top["raci"]:
        element = find_paragraph(body, item["text"])
        raci_elements.append(element)
        style_paragraph(
            requests, tab_id, element, font=body_font, size=body_size, color=body_color,
            space_above=12, space_below=12,
            indent_start=spacing["raci_indent_start_pt"],
            indent_first=spacing["raci_indent_first_line_pt"],
        )
        apply_inline_styles(requests, tab_id, element, item, link_color=body_color)
    raci_start, raci_end = raci_elements[0]["startIndex"], raci_elements[-1]["endIndex"]
    requests.append(
        {
            "createParagraphBullets": {
                "range": docs_range(tab_id, raci_start, raci_end),
                "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
            }
        }
    )
    # Bullet creation can reset indents; make the approved RACI geometry the final operation.
    requests.append(
        update_paragraph(
            tab_id,
            raci_start,
            raci_end,
            {
                "indentStart": {"magnitude": spacing["raci_indent_start_pt"], "unit": "PT"},
                "indentFirstLine": {
                    "magnitude": spacing["raci_indent_first_line_pt"], "unit": "PT"
                },
                "lineSpacing": 115,
                "spaceAbove": {"magnitude": 12, "unit": "PT"},
                "spaceBelow": {"magnitude": 12, "unit": "PT"},
            },
            "indentStart,indentFirstLine,lineSpacing,spaceAbove,spaceBelow",
        )
    )

    if top.get("warning"):
        warning = find_paragraph(body, top["warning"])
        style_paragraph(
            requests, tab_id, warning,
            font=contract["warning"]["font"], size=contract["warning"]["size_pt"],
            bold=contract["warning"]["bold"], color=hex_color(contract["warning"]["foreground"]),
            space_above=6, space_below=8, keep_next=True,
        )
        requests.append(
            update_paragraph(
                tab_id, warning["startIndex"], warning["endIndex"],
                {"shading": {"backgroundColor": hex_color(contract["warning"]["background"])}},
                "shading",
            )
        )

    note_font, note_size, note_bold, note_italic, note_color = _text_style(contract, "context_note")
    for item in top.get("notes", []):
        element = find_paragraph(body, item["text"])
        style_paragraph(
            requests, tab_id, element, font=note_font, size=note_size,
            bold=note_bold, italic=note_italic, color=note_color, space_below=8,
        )
        apply_inline_styles(requests, tab_id, element, item, link_color=note_color)

    heading_font, heading_size, heading_bold, heading_italic, heading_color = _text_style(contract, "heading")
    for heading in (research_heading, overview_heading):
        style_paragraph(
            requests, tab_id, heading, font=heading_font, size=heading_size,
            bold=heading_bold, italic=heading_italic, color=heading_color,
            named_style="HEADING_1", line_spacing=115,
            space_above=spacing["heading_space_above_pt"],
            space_below=spacing["heading_space_below_pt"], keep_next=True,
        )
    style_paragraph(
        requests, tab_id, timeline_note, font=body_font, size=body_size,
        italic=True, color=body_color,
    )
    apply_inline_styles(
        requests, tab_id, timeline_note, manifest["timeline_note"], link_color=body_color
    )

    # Leadership timeline table.
    timeline_start = timeline["startIndex"]
    padding = {"magnitude": contract["tables"]["cell_padding_pt"], "unit": "PT"}
    table_base_style = {
        "backgroundColor": colors["white"],
        "paddingTop": padding,
        "paddingBottom": padding,
        "paddingLeft": padding,
        "paddingRight": padding,
    }
    requests.append(
        update_cell(
            tab_id, timeline_start, 0, 0,
            table_base_style,
            "backgroundColor,paddingTop,paddingBottom,paddingLeft,paddingRight",
            row_span=5, col_span=2,
        )
    )
    requests.append(
        update_cell(
            tab_id, timeline_start, 0, 0,
            {"backgroundColor": colors["dark_green"]}, "backgroundColor",
            col_span=2,
        )
    )
    for row_index in range(1, 5):
        requests.append(
            update_cell(
                tab_id, timeline_start, row_index, 0,
                {"backgroundColor": colors["gray_cell"]}, "backgroundColor",
            )
        )
    requests.append(
        {
            "pinTableHeaderRows": {
                "tableStartLocation": {"index": timeline_start, "tabId": tab_id},
                "pinnedHeaderRowsCount": 1,
            }
        }
    )
    for row_index, (row, manifest_row) in enumerate(zip(timeline["table"]["tableRows"], manifest["timeline"])):
        for col_index, (cell, item) in enumerate(zip(row["tableCells"], manifest_row)):
            elements = [element for element in cell_paragraphs(cell) if paragraph_text(element["paragraph"]).strip()]
            if len(elements) != 1:
                raise ContractError("Each normalized timeline cell must contain one paragraph")
            element = elements[0]
            style_paragraph(
                requests, tab_id, element, font=body_font, size=body_size,
                bold=(row_index == 0 or col_index == 0),
                color=(colors["white"] if row_index == 0 else body_color),
                line_spacing=spacing["table_line_spacing_percent"],
            )
            apply_inline_styles(
                requests,
                tab_id,
                element,
                item,
                link_color=(colors["white"] if row_index == 0 else body_color),
            )

    # Project Plan Overview table.
    overview_start = overview["startIndex"]
    overview_rows = overview["table"]["tableRows"]
    requests.append(
        update_cell(
            tab_id, overview_start, 0, 0,
            table_base_style,
            "backgroundColor,paddingTop,paddingBottom,paddingLeft,paddingRight",
            row_span=len(overview_rows), col_span=2,
        )
    )
    section_font, section_size, section_bold, section_italic, section_color = _text_style(contract, "section_band")
    for row_index, (row, source) in enumerate(zip(overview_rows, manifest["rows"])):
        if len(row["tableCells"]) != 2:
            raise ContractError(f"Row {row_index} must keep two physical cells")
        left, right = row["tableCells"]
        left_elements = [element for element in cell_paragraphs(left) if paragraph_text(element["paragraph"]).strip()]
        right_elements = [element for element in cell_paragraphs(right) if paragraph_text(element["paragraph"]).strip()]
        if len(left_elements) != 1:
            raise ContractError(f"Row {row_index} label cell must contain one paragraph")

        if source["section"]:
            requests.append(
                update_cell(
                    tab_id, overview_start, row_index, 0,
                    {"backgroundColor": colors["dark_green"]}, "backgroundColor", col_span=2,
                )
            )
            style_paragraph(
                requests, tab_id, left_elements[0], font=section_font, size=section_size,
                bold=section_bold, italic=section_italic, color=section_color,
                named_style="HEADING_4", line_spacing=100,
            )
            for element in cell_paragraphs(right):
                requests.append(
                    update_paragraph(
                        tab_id, element["startIndex"], element["endIndex"],
                        {
                            "lineSpacing": 100,
                            "spaceAbove": {"magnitude": 0, "unit": "PT"},
                            "spaceBelow": {"magnitude": 0, "unit": "PT"},
                        },
                        "lineSpacing,spaceAbove,spaceBelow",
                    )
                )
            continue

        style_paragraph(
            requests, tab_id, left_elements[0], font=body_font, size=body_size,
            bold=True, color=body_color,
        )
        if len(right_elements) != len(source["items"]):
            raise ContractError(
                f"Row {source['label']!r} has {len(right_elements)} paragraphs; expected {len(source['items'])}"
            )
        for element, item in zip(right_elements, source["items"]):
            if paragraph_text(element["paragraph"]).rstrip("\n") != item["text"]:
                raise ContractError(f"Normalized content mismatch in {source['label']!r}")
            style_paragraph(
                requests, tab_id, element, font=body_font, size=body_size,
                color=body_color,
            )
            apply_inline_styles(requests, tab_id, element, item, link_color=body_color)
        if source["bulleted"] and right_elements:
            requests.append(
                {
                    "createParagraphBullets": {
                        "range": docs_range(
                            tab_id, right_elements[0]["startIndex"], right_elements[-1]["endIndex"]
                        ),
                        "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                    }
                }
            )
            requests.append(
                update_paragraph(
                    tab_id, right_elements[0]["startIndex"], right_elements[-1]["endIndex"],
                    {
                        "indentStart": {
                            "magnitude": spacing["cell_bullet_indent_start_pt"], "unit": "PT"
                        },
                        "indentFirstLine": {
                            "magnitude": spacing["cell_bullet_indent_first_line_pt"], "unit": "PT"
                        },
                        "lineSpacing": 115,
                        "spaceAbove": {"magnitude": 0, "unit": "PT"},
                        "spaceBelow": {"magnitude": 0, "unit": "PT"},
                    },
                    "indentStart,indentFirstLine,lineSpacing,spaceAbove,spaceBelow",
                )
            )

    for table_start in (timeline_start, overview_start):
        for column_index, width in enumerate(contract["tables"]["column_widths_pt"]):
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

    return _batch_payload(requests, resolved_revision_id)


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
    # Google named styles inherit unspecified values from NORMAL_TEXT.
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


def _assert_text_style(
    element: dict[str, Any], named: dict[str, dict[str, Any]], expected: dict[str, Any]
) -> None:
    style = _effective_style(element["paragraph"], _first_run(element), named)
    if style.get("weightedFontFamily", {}).get("fontFamily") != expected["font"]:
        raise ContractError(f"Wrong font for {paragraph_text(element['paragraph']).strip()!r}")
    if style.get("fontSize", {}).get("magnitude") != expected["size_pt"]:
        raise ContractError(f"Wrong font size for {paragraph_text(element['paragraph']).strip()!r}")
    if style.get("bold", False) != expected.get("bold", False):
        raise ContractError(f"Wrong bold style for {paragraph_text(element['paragraph']).strip()!r}")
    if style.get("italic", False) != expected.get("italic", False):
        raise ContractError(f"Wrong italic style for {paragraph_text(element['paragraph']).strip()!r}")
    if _rgb(style.get("foregroundColor"), default_black=True) != _hex_tuple(expected["color"]):
        raise ContractError(f"Wrong text color for {paragraph_text(element['paragraph']).strip()!r}")


def _assert_base_text_style(
    element: dict[str, Any], named: dict[str, dict[str, Any]], expected: dict[str, Any]
) -> None:
    """Check font, size, and color across every visible run, allowing approved inline emphasis."""
    for child in element["paragraph"].get("elements", []):
        run = child.get("textRun") or child.get("person")
        if run is None or ("textRun" in child and not run.get("content", "").rstrip("\n")):
            continue
        style = _effective_style(element["paragraph"], run, named)
        if style.get("weightedFontFamily", {}).get("fontFamily") != expected["font"]:
            raise ContractError(f"Wrong run font in {paragraph_text(element['paragraph']).strip()!r}")
        if style.get("fontSize", {}).get("magnitude") != expected["size_pt"]:
            raise ContractError(f"Wrong run font size in {paragraph_text(element['paragraph']).strip()!r}")
        if _rgb(style.get("foregroundColor"), default_black=True) != _hex_tuple(expected["color"]):
            raise ContractError(f"Wrong run color in {paragraph_text(element['paragraph']).strip()!r}")


def _assert_inline_exact(
    element: dict[str, Any], item: dict[str, Any], named: dict[str, dict[str, Any]],
    *, base_bold: bool = False, base_italic: bool = False,
) -> None:
    """Require approved bold/italic/link spans and reject unapproved extra emphasis."""
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
        run = child.get("textRun") or child.get("person")
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
    element: dict[str, Any], *, line_spacing: int, space_above: float = 0,
    space_below: float = 0, keep_next: bool | None = None,
    indent_start: float | None = None, indent_first: float | None = None,
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


def verify_document(doc: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    """Validate content and every machine-checkable Option 4 visual invariant."""
    validate_manifest(manifest)
    contract = load_contract()
    _, tab = get_tab(doc)
    body = tab["body"]["content"]
    named = _named_text_styles(tab)
    tables = doc_tables(tab)
    if len(tables) != 2:
        raise ContractError("Final document must contain exactly two tables")
    timeline, overview = tables
    if [len(timeline["table"]["tableRows"]), len(overview["table"]["tableRows"])] != [5, len(manifest["rows"])]:
        raise ContractError("Final table row counts do not match the Option 4 manifest")

    top = manifest["top"]
    expected_sequence = [
        top["breadcrumb"]["text"],
        top["title"]["text"],
        top["updated"]["text"],
        *[item["text"] for item in top["raci"]],
        *([top["warning"]] if top.get("warning") else []),
        *[item["text"] for item in top.get("notes", [])],
        "Research Timeline",
        "<TABLE>",
        manifest["timeline_note"]["text"],
        "<RULE>",
        "Project Plan Overview",
        "<TABLE>",
    ]
    actual_sequence: list[str] = []
    for element in body:
        if "table" in element:
            actual_sequence.append("<TABLE>")
        elif "paragraph" in element:
            if any("horizontalRule" in child for child in element["paragraph"].get("elements", [])):
                actual_sequence.append("<RULE>")
                continue
            text = paragraph_text(element["paragraph"]).strip()
            if text:
                actual_sequence.append(text)
    if actual_sequence != expected_sequence:
        raise ContractError("Opening, timeline, or overview hierarchy does not match the approved manifest")

    document_style = tab.get("documentStyle", {})
    if document_style.get("documentFormat", {}).get("documentMode") != contract["page"]["document_mode"]:
        raise ContractError(f"Document mode is not {contract['page']['document_mode']}")
    if bool(document_style.get("useCustomHeaderFooterMargins", False)) != contract["page"]["use_custom_header_footer_margins"]:
        raise ContractError("Custom header/footer margins are not enabled")
    margins = contract["page"]["margins_pt"]
    for key, expected in (
        ("marginTop", margins["top"]),
        ("marginBottom", margins["bottom"]),
        ("marginLeft", margins["left"]),
        ("marginRight", margins["right"]),
        ("marginHeader", contract["page"]["header_margin_pt"]),
        ("marginFooter", contract["page"]["footer_margin_pt"]),
    ):
        if document_style.get(key, {}).get("magnitude") != expected:
            raise ContractError(f"{key} is not {expected}pt")
    width = document_style.get("pageSize", {}).get("width", {}).get("magnitude")
    height = document_style.get("pageSize", {}).get("height", {}).get("magnitude")
    if document_style.get("flipPageOrientation"):
        width, height = height, width
    if (width, height) != (contract["page"]["width_pt"], contract["page"]["height_pt"]):
        raise ContractError(f"Page is not landscape letter: {(width, height)}")

    for table in tables:
        properties = table["table"].get("tableStyle", {}).get("tableColumnProperties", [])
        actual_widths = [item.get("width", {}).get("magnitude") for item in properties]
        if actual_widths != contract["tables"]["column_widths_pt"]:
            raise ContractError(f"Wrong table widths: {actual_widths}")
        for row in table["table"]["tableRows"]:
            for cell in row["tableCells"]:
                _assert_cell_padding(cell, contract["tables"]["cell_padding_pt"])

    breadcrumb = find_paragraph(body, top["breadcrumb"]["text"])
    title = find_paragraph(body, top["title"]["text"])
    updated = find_paragraph(body, top["updated"]["text"])
    research_heading = find_paragraph(body, "Research Timeline")
    overview_heading = find_paragraph(body, "Project Plan Overview")
    timeline_note = find_paragraph(body, manifest["timeline_note"]["text"])
    _assert_text_style(breadcrumb, named, contract["typography"]["breadcrumb"])
    _assert_text_style(title, named, contract["typography"]["title"])
    _assert_text_style(updated, named, contract["typography"]["body"])
    _assert_text_style(research_heading, named, contract["typography"]["heading"])
    _assert_text_style(overview_heading, named, contract["typography"]["heading"])
    for element, item, style_name in (
        (breadcrumb, top["breadcrumb"], "breadcrumb"),
        (title, top["title"], "title"),
        (updated, top["updated"], "body"),
    ):
        expected = contract["typography"][style_name]
        _assert_base_text_style(element, named, expected)
        _assert_inline_exact(
            element, item, named,
            base_bold=expected.get("bold", False),
            base_italic=expected.get("italic", False),
        )
    for element, text in ((research_heading, "Research Timeline"), (overview_heading, "Project Plan Overview")):
        _assert_base_text_style(element, named, contract["typography"]["heading"])
        _assert_inline_exact(
            element,
            {"text": text, "bold": [], "italic": [], "links": []},
            named,
            base_bold=True,
        )
    note_expected = dict(contract["typography"]["body"])
    note_expected["italic"] = True
    _assert_text_style(timeline_note, named, note_expected)
    _assert_paragraph_metrics(
        breadcrumb, line_spacing=115,
        space_below=contract["spacing"]["breadcrumb_space_below_pt"], keep_next=True,
    )
    _assert_paragraph_metrics(
        title, line_spacing=115,
        space_below=contract["spacing"]["title_space_below_pt"], keep_next=True,
    )
    _assert_paragraph_metrics(updated, line_spacing=115, space_above=12, space_below=12)
    for heading in (research_heading, overview_heading):
        _assert_paragraph_metrics(
            heading, line_spacing=115,
            space_above=contract["spacing"]["heading_space_above_pt"],
            space_below=contract["spacing"]["heading_space_below_pt"], keep_next=True,
        )
    _assert_paragraph_metrics(timeline_note, line_spacing=115)
    _assert_base_text_style(timeline_note, named, contract["typography"]["body"])
    _assert_inline_exact(timeline_note, manifest["timeline_note"], named, base_italic=True)

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
        expected = {
            "font": contract["warning"]["font"],
            "size_pt": contract["warning"]["size_pt"],
            "bold": contract["warning"]["bold"],
            "color": contract["warning"]["foreground"],
        }
        _assert_text_style(warning, named, expected)
        _assert_base_text_style(warning, named, expected)
        _assert_inline_exact(
            warning,
            {"text": top["warning"], "bold": [], "italic": [], "links": []},
            named,
            base_bold=True,
        )
        _assert_paragraph_metrics(warning, line_spacing=115, space_above=6, space_below=8, keep_next=True)
        shading = warning["paragraph"].get("paragraphStyle", {}).get("shading", {}).get("backgroundColor")
        if _rgb(shading) != _hex_tuple(contract["warning"]["background"]):
            raise ContractError("Mock warning does not use full-paragraph pale-yellow shading")

    for item in top.get("notes", []):
        element = find_paragraph(body, item["text"])
        _assert_base_text_style(element, named, contract["typography"]["context_note"])
        _assert_inline_exact(element, item, named, base_italic=True)
        _assert_paragraph_metrics(element, line_spacing=115, space_below=8)

    # Leadership timeline content and treatment.
    timeline_rows = timeline["table"]["tableRows"]
    for row_index, (row, source_row) in enumerate(zip(timeline_rows, manifest["timeline"])):
        if len(row["tableCells"]) != 2:
            raise ContractError("Timeline rows must keep two cells")
        actual = [paragraph_text(cell_paragraphs(cell)[0]["paragraph"]).strip() for cell in row["tableCells"]]
        if actual != [item["text"] for item in source_row]:
            raise ContractError(f"Timeline content mismatch in row {row_index}")
        for col_index, (cell, item) in enumerate(zip(row["tableCells"], source_row)):
            background = _rgb(cell.get("tableCellStyle", {}).get("backgroundColor"))
            expected_background = (
                _hex_tuple(contract["colors"]["dark_green"])
                if row_index == 0
                else _hex_tuple(contract["colors"]["gray_cell"])
                if col_index == 0
                else _hex_tuple(contract["colors"]["white"])
            )
            if background != expected_background:
                raise ContractError(f"Timeline background mismatch at {row_index},{col_index}")
            elements = [
                element for element in cell_paragraphs(cell)
                if paragraph_text(element["paragraph"]).strip()
            ]
            if len(elements) != 1:
                raise ContractError(f"Timeline cell {row_index},{col_index} must contain one paragraph")
            if "bullet" in elements[0]["paragraph"]:
                raise ContractError(f"Timeline cell {row_index},{col_index} has an unexpected bullet")
            expected_style = dict(contract["typography"]["body"])
            expected_style["bold"] = row_index == 0 or col_index == 0
            if row_index == 0:
                expected_style["color"] = contract["colors"]["white"]
            _assert_text_style(elements[0], named, expected_style)
            _assert_base_text_style(elements[0], named, expected_style)
            _assert_inline_exact(
                elements[0], item, named, base_bold=(row_index == 0 or col_index == 0)
            )
            _assert_paragraph_metrics(
                elements[0], line_spacing=contract["spacing"]["table_line_spacing_percent"]
            )
    if not timeline_rows[0].get("tableRowStyle", {}).get("tableHeader", False):
        raise ContractError("Timeline header row is not pinned/repeating")

    # Main overview content and treatment.
    overview_rows = overview["table"]["tableRows"]
    for row_index, (row, source) in enumerate(zip(overview_rows, manifest["rows"])):
        if len(row["tableCells"]) != 2:
            raise ContractError(f"Overview row {row_index} is merged; Option 4 requires two cells")
        if any(cell.get("tableCellStyle", {}).get("columnSpan", 1) != 1 for cell in row["tableCells"]):
            raise ContractError(f"Overview row {row_index} has a physical column span")
        left, right = row["tableCells"]
        label = paragraph_text(cell_paragraphs(left)[0]["paragraph"]).strip()
        if label != output_label(source["label"]):
            raise ContractError(f"Overview label mismatch: {label!r}")
        expected_background = _hex_tuple(
            contract["colors"]["dark_green"] if source["section"] else contract["colors"]["white"]
        )
        if any(_rgb(cell.get("tableCellStyle", {}).get("backgroundColor")) != expected_background for cell in row["tableCells"]):
            raise ContractError(f"Overview background mismatch in row {row_index}")
        left_element = cell_paragraphs(left)[0]
        if "bullet" in left_element["paragraph"]:
            raise ContractError(f"Overview label {source['label']!r} has an unexpected bullet")
        if source["section"]:
            _assert_text_style(left_element, named, contract["typography"]["section_band"])
            _assert_base_text_style(left_element, named, contract["typography"]["section_band"])
            _assert_inline_exact(
                left_element,
                {"text": source["label"], "bold": [], "italic": [], "links": []},
                named,
                base_bold=True,
            )
            _assert_paragraph_metrics(
                left_element, line_spacing=contract["spacing"]["table_line_spacing_percent"]
            )
            right_section_elements = cell_paragraphs(right)
            if len(right_section_elements) != 1:
                raise ContractError(f"Section band {source['label']!r} must keep one empty right paragraph")
            if any(paragraph_text(element["paragraph"]).strip() for element in right_section_elements):
                raise ContractError(f"Section band {source['label']!r} must have an empty right cell")
            _assert_paragraph_metrics(
                right_section_elements[0],
                line_spacing=contract["spacing"]["table_line_spacing_percent"],
            )
            continue

        label_style = dict(contract["typography"]["body"])
        label_style["bold"] = True
        _assert_text_style(left_element, named, label_style)
        _assert_base_text_style(left_element, named, label_style)
        _assert_inline_exact(
            left_element,
            {"text": output_label(source["label"]), "bold": [], "italic": [], "links": []},
            named,
            base_bold=True,
        )
        _assert_paragraph_metrics(left_element, line_spacing=115)
        right_elements = [element for element in cell_paragraphs(right) if paragraph_text(element["paragraph"]).strip()]
        if [paragraph_text(element["paragraph"]).rstrip("\n") for element in right_elements] != [item["text"] for item in source["items"]]:
            raise ContractError(f"Overview content mismatch in {source['label']!r}")
        if source["bulleted"] and any("bullet" not in element["paragraph"] for element in right_elements):
            raise ContractError(f"Overview row {source['label']!r} is missing native bullets")
        if not source["bulleted"] and any("bullet" in element["paragraph"] for element in right_elements):
            raise ContractError(f"Overview row {source['label']!r} has unexpected bullets")
        for element, item in zip(right_elements, source["items"]):
            _assert_base_text_style(element, named, contract["typography"]["body"])
            _assert_inline_exact(element, item, named)
            if source["bulleted"]:
                _assert_paragraph_metrics(
                    element, line_spacing=115,
                    indent_start=contract["spacing"]["cell_bullet_indent_start_pt"],
                    indent_first=contract["spacing"]["cell_bullet_indent_first_line_pt"],
                )
            else:
                _assert_paragraph_metrics(element, line_spacing=115)

    labels = [row["label"] for row in manifest["rows"]]
    appendix_index = labels.index("APPENDIX")
    if labels[appendix_index:] != ["APPENDIX", "Additional UXR documents", "Resources from XFN"]:
        raise ContractError("Appendix contains an unsupported row")

    return [
        "Option 4 page geometry and typography",
        "leadership timeline content, colors, widths, and repeating header",
        "Project Plan Overview order, two-cell section bands, and white body cells",
        "native RACI and table bullets",
        "approved emphasis and active links",
    ]


def write_json(path: str | Path, value: dict[str, Any]) -> None:
    target = Path(path)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.",
        suffix=".tmp",
        dir=target.parent,
    )
    temporary = Path(temporary_name)
    try:
        stream = os.fdopen(descriptor, "w", encoding="utf-8")
        descriptor = -1
        with stream:
            os.chmod(temporary, 0o600)
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
    except BaseException:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def read_json_object(path: str | Path, label: str) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"{label} JSON root must be an object")
    return value


def cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True)

    manifest = subparsers.add_parser("manifest", help="Parse approved Markdown into a build manifest")
    manifest.add_argument("markdown")
    manifest.add_argument("output")

    normalize = subparsers.add_parser("normalize", help="Generate cleanup/population requests after import")
    normalize.add_argument("document_json")
    normalize.add_argument("manifest_json")
    normalize.add_argument("output")
    normalize.add_argument(
        "--required-revision-id",
        help="bind the batch to the freshly fetched Google Docs revision",
    )

    format_parser = subparsers.add_parser("format", help="Generate exact Option 4 formatting requests")
    format_parser.add_argument("document_json")
    format_parser.add_argument("manifest_json")
    format_parser.add_argument("output")
    format_parser.add_argument(
        "--required-revision-id",
        help="bind the batch to the freshly fetched Google Docs revision",
    )

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
        print(f"PASS: parsed {len(value['rows'])} overview rows and four leadership milestones")
        return 0

    doc = read_json_object(args.document_json, "Document")
    manifest = read_json_object(args.manifest_json, "Manifest")
    if args.command == "normalize":
        required_revision_id = resolve_required_revision_id(
            doc,
            args.required_revision_id,
            require=True,
        )
        payload = build_normalize_requests(
            doc,
            manifest,
            required_revision_id=required_revision_id,
        )
        write_json(args.output, payload)
        print(f"PASS: generated {len(payload['requests'])} normalization requests")
        return 0
    if args.command == "format":
        required_revision_id = resolve_required_revision_id(
            doc,
            args.required_revision_id,
            require=True,
        )
        payload = build_format_requests(
            doc,
            manifest,
            required_revision_id=required_revision_id,
        )
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
    except (
        ContractError,
        KeyError,
        IndexError,
        StopIteration,
        AttributeError,
        TypeError,
        OSError,
        UnicodeError,
        json.JSONDecodeError,
    ) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
