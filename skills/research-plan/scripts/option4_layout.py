#!/usr/bin/env python3
"""Build and verify the exact Option 4 — Leadership Google Docs layout.

Checks while drafting:
    option4_layout.py timeline TIMELINE.md   # Step 3: the Gantt grid is well formed and every label fits
    option4_layout.py lint APPROVED.md       # Step 4: layout failures plus content-rule flags

Pipeline:
    option4_layout.py manifest APPROVED.md manifest.json
    option4_layout.py normalize imported-doc.json manifest.json normalize-batch.json \
        --required-revision-id IMPORTED_REVISION_ID
    # Apply batch and re-fetch the document.
    option4_layout.py format normalized-doc.json manifest.json format-batch.json \
        --required-revision-id NORMALIZED_REVISION_ID
    # Apply batch and re-fetch the document.
    option4_layout.py verify final-doc.json manifest.json

Applying a batch through gws, which has no request-body file option:
    option4_layout.py send BATCH.json --document-id DOC_ID --response response.json

The Research Timeline is a Gantt grid. In Markdown it is a table headed
`Phase | Activity | <one column per week>`; a Phase cell reads `Phase N: Name`
and a blank Phase cell continues the phase above (the Doc merges it); a week
cell is blank or `[target]`, `[spillover]`, or `[event]`, optionally followed
by a short note (`[target] Human raters`).

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
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CONTRACT_PATH = SKILL_DIR / "references" / "option4-style-contract.json"
TAB_ID_FALLBACK = "t.0"
SECTIONS = (
    "Key Information",
    "Project Details",
    "Deliverables & Next Steps",
    "Appendix",
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
APPENDIX_ROWS = ("Appendix", "Additional UXR documents", "Resources from XFN")
# Labels that keep NORMAL_TEXT plus direct bold, as in the reference; every other label is HEADING_5.
PLAIN_BOLD_LABELS = ("Topic", "TL;DR summary of findings")
# Gantt week-cell status tokens and the contract color each one fills.
STATUS_COLORS = {"target": "status_target", "spillover": "status_spillover", "event": "status_event"}
STATUS_CELL = re.compile(r"^\[(?P<status>[^\]]*)\](?:\s+(?P<note>\S.*))?$")
LIST_ITEM = re.compile(r"^(?P<indent>(?: |&nbsp;)*)(?P<marker>-|\d+\.)\s+(?P<body>\S.*)$", re.DOTALL)
# The simulated-study banner; the contract's warning.variants holds every accepted banner.
WARNING = "⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable."
# Files whose hashes a manifest records, so a skill update mid-run is caught.
SKILL_FILES = ("scripts/option4_layout.py", "references/option4-style-contract.json")
GWS_FALLBACK_PATH = Path.home() / ".config" / "gohan" / "bin" / "gws"


class ContractError(ValueError):
    """Raised when the document cannot satisfy the Option 4 contract."""


def load_contract() -> dict[str, Any]:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    page = contract["page"]
    usable_width = round(page["width_pt"] - page["margins_pt"]["left"] - page["margins_pt"]["right"], 3)
    overview = contract["overview_table"]
    overview_total = round(sum(overview["column_widths_pt"]), 3)
    if overview_total != overview["total_width_pt"]:
        raise ContractError("Option 4 overview table-width tokens are internally inconsistent")
    if round(overview_total - usable_width, 3) != overview["intentional_text_area_overflow_pt"]:
        raise ContractError("Option 4 intentional table overflow token is inconsistent")
    if tuple(overview["section_rows"]) != SECTIONS:
        raise ContractError("Option 4 section bands must be the four Title Case bands in order")
    timeline = contract["timeline_table"]
    widths = timeline["column_widths_pt"]
    if round(widths["phase"] + widths["activity"] + timeline["max_week_columns"] * widths["week"], 3) != timeline["max_total_width_pt"]:
        raise ContractError("Option 4 timeline widths must add up to the maximum grid width")
    statuses = timeline["week_cells"]["statuses"]
    if set(statuses) != set(STATUS_COLORS) or any(
        statuses[status] != contract["colors"][key] for status, key in STATUS_COLORS.items()
    ):
        raise ContractError("Option 4 timeline status fills must match the status colors")
    if set(timeline["legend"]["swatches"].values()) != set(STATUS_COLORS):
        raise ContractError("Option 4 timeline legend must name every status")
    bold = contract["font_metrics"]["dm_sans_bold"]
    regular = contract["font_metrics"]["dm_sans_regular"]
    if (
        bold["bold"] is not True
        or regular["bold"] is not False
        or bold["size_pt"] != regular["size_pt"]
        or bold["units_per_em"] != regular["units_per_em"]
        or set(bold["advance_widths"]) != set(regular["advance_widths"])
    ):
        raise ContractError("Option 4 font-width tokens are inconsistent")
    for name, role in contract["typography"].items():
        named = contract["named_styles"].get(role.get("named_style", ""))
        if named and name != "section_band" and any(
            role[key] != named[key] for key in ("font", "size_pt", "bold", "color")
        ):
            raise ContractError(f"Option 4 typography {name!r} disagrees with its named style")
    variants = contract["warning"]["variants"]
    if set(variants) != {"simulated", "test_run"} or variants["simulated"] != WARNING:
        raise ContractError("Option 4 warning variants must be exactly simulated and test_run")
    return contract


def skill_files_digest() -> dict[str, str]:
    return {
        name: hashlib.sha256((SKILL_DIR / name).read_bytes()).hexdigest()
        for name in SKILL_FILES
    }


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
    if manifest.get("skill_files_sha256") != skill_files_digest():
        raise ContractError(
            "Skill files changed since this manifest was generated — rerun manifest "
            "(and don't update the skill mid-run)"
        )


def text_width_pt(text: str, font: dict[str, Any]) -> float:
    """Printed width of text in one DM Sans weight, from the contract's advance widths."""
    widths = font["advance_widths"]
    units = sum(widths.get(char, font["unknown_character_width"]) for char in text)
    return units * font["size_pt"] / font["units_per_em"]


def wrapped_lines(text: str, max_width_pt: float, font: dict[str, Any]) -> tuple[int, list[str]]:
    """Greedy word wrap: the line count and any word too wide to fit on a line by itself."""
    words = text.split()
    too_wide = [word for word in words if text_width_pt(word, font) > max_width_pt]
    lines = 0
    current = ""
    for word in words:
        candidate = f"{current} {word}" if current else word
        if current and text_width_pt(candidate, font) > max_width_pt:
            lines += 1
            current = word
        else:
            current = candidate
    if current:
        lines += 1
    return lines, too_wide


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



def _strip_wrapping_italics(value: str) -> str:
    stripped = value.strip()
    if len(stripped) >= 2 and stripped.startswith("*") and stripped.endswith("*"):
        return stripped[1:-1].strip()
    return stripped



def split_cell_items(raw: str, contract: dict[str, Any] | None = None) -> tuple[str | None, list[dict[str, Any]]]:
    """Return a cell's list kind (None, "BULLET", or "NUMBER") and its items.

    A list cell starts with `- ` or `1. `; `<br>` separates items, and two leading spaces
    (or `&nbsp;`) per level after a `<br>` nest an item one level deeper.
    """
    lists = (contract or load_contract())["lists"]
    value = raw.strip()
    if not value:
        return None, []
    if not LIST_ITEM.match(value):
        return None, [dict(parse_inline(value), level=0)]
    kinds: set[str] = set()
    items: list[dict[str, Any]] = []
    for chunk in re.split(r"<br\s*/?>|\n", value):
        if not chunk.strip():
            continue
        match = LIST_ITEM.match(chunk)
        if not match:
            raise ContractError(
                f"Each list item in a cell starts with '- ' or '1. ' after its <br>: {chunk.strip()!r}"
            )
        indent = match.group("indent").count(" ") + match.group("indent").count("&nbsp;")
        level = indent // lists["markdown_indent_spaces_per_level"]
        previous = items[-1]["level"] if items else -1
        if level > previous + 1 or level > lists["max_nesting_level"]:
            raise ContractError(
                f"List item nests more than one level below the item above it: {match.group('body')[:60]!r}"
            )
        kinds.add("BULLET" if match.group("marker") == "-" else "NUMBER")
        items.append(dict(parse_inline(match.group("body")), level=level))
    if len(kinds) > 1:
        raise ContractError("A cell's list uses '- ' bullets or '1. ' numbers, not both")
    return kinds.pop(), items


def timeline_cell_paragraphs(timeline: dict[str, Any]) -> list[list[list[str]]]:
    """The paragraphs each Doc grid cell holds once normalized: rows × cells × paragraphs."""
    grid: list[list[list[str]]] = [[["Phase"], ["Activity"], *[[week] for week in timeline["weeks"]]]]
    for index, row in enumerate(timeline["rows"]):
        phase = timeline["phases"][row["phase"]]
        phase_cell = [f"Phase {phase['number']}:", phase["name"]] if phase["start_row"] == index else [""]
        grid.append([phase_cell, [row["activity"]], *[[cell["note"]] for cell in row["cells"]]])
    return grid


def timeline_measurements(timeline: dict[str, Any], contract: dict[str, Any]) -> list[tuple[bool, str, str]]:
    """(fits, report line, kind) for every label in the grid, measured against its column."""
    spec = contract["timeline_table"]
    widths = spec["column_widths_pt"]
    bold = contract["font_metrics"]["dm_sans_bold"]
    regular = contract["font_metrics"]["dm_sans_regular"]
    week_width = round(widths["week"] - 2 * spec["header_row"]["week_cells"]["padding_pt"], 3)
    padding = spec["body_rows"]["padding_pt"]
    phase_width = round(widths["phase"] - 2 * padding, 3)
    activity_width = round(widths["activity"] - 2 * padding, 3)
    note_width = round(widths["week"] - 2 * padding, 3)
    results: list[tuple[bool, str, str]] = []
    for week in timeline["weeks"]:
        width = text_width_pt(week, bold)
        results.append((width <= week_width, f"week {week!r} — {width:.1f}/{week_width:g}pt", "week"))
    for phase in timeline["phases"]:
        width = text_width_pt(phase["name"], bold)
        span = phase["rows"]
        where = f"{span} rows, merged" if span > 1 else "1 row"
        results.append((
            width <= phase_width,
            f"Phase {phase['number']}: {phase['name']} — {width:.1f}/{phase_width:g}pt ({where})",
            "phase",
        ))
    for row in timeline["rows"]:
        lines, too_wide = wrapped_lines(row["activity"], activity_width, regular)
        fits = lines <= spec["activity_column"]["max_lines"] and not too_wide
        results.append((fits, f"activity {row['activity']!r} — {lines} line(s) at {activity_width:g}pt", "activity"))
        for week, cell in zip(timeline["weeks"], row["cells"]):
            if not cell["note"]:
                continue
            lines, too_wide = wrapped_lines(cell["note"], note_width, regular)
            fits = lines <= spec["week_cells"]["note_max_lines"] and not too_wide
            results.append((
                fits,
                f"note {cell['note']!r} ({row['activity']}, {week}) — {lines} line(s) at {note_width:g}pt",
                "note",
            ))
    return results


def timeline_problems(timeline: dict[str, Any], contract: dict[str, Any]) -> list[str]:
    """Labels that would not fit their grid column; a wrapped label makes rows taller than the reference."""
    spec = contract["timeline_table"]
    widths = spec["column_widths_pt"]
    padding = spec["body_rows"]["padding_pt"]
    limits = {
        "week": (
            f"Timeline week label would wrap; a week column fits "
            f"{widths['week'] - 2 * spec['header_row']['week_cells']['padding_pt']:g}pt on one line. "
            "Use a short date such as 'Nov. 3' or 'Week 3'"
        ),
        "phase": (
            f"Timeline phase name would wrap; the Phase column fits {widths['phase'] - 2 * padding:g}pt "
            "on one line. Shorten the name after the colon"
        ),
        "activity": (
            f"Timeline activity name doesn't fit; the Activity column holds "
            f"{spec['activity_column']['max_lines']} lines of {widths['activity'] - 2 * padding:g}pt "
            "with no word split. Use a shorter name"
        ),
        "note": (
            f"Timeline week note doesn't fit; a week cell holds {spec['week_cells']['note_max_lines']} lines "
            f"of {widths['week'] - 2 * padding:g}pt with no word split. Use one or two short words"
        ),
    }
    failing: dict[str, list[str]] = {}
    for fits, line, kind in timeline_measurements(timeline, contract):
        if not fits:
            failing.setdefault(kind, []).append(line)
    return [f"{limits[kind]}: {', '.join(lines)}" for kind, lines in failing.items()]


def timeline_report(timeline: dict[str, Any], contract: dict[str, Any]) -> list[str]:
    """One line per grid label with its measured fit, for the researcher-facing check."""
    return [f"{'OK  ' if fits else 'WRAP'} {line}" for fits, line, _ in timeline_measurements(timeline, contract)]


def parse_timeline_table(
    lines: list[str], heading_index: int, contract: dict[str, Any]
) -> tuple[dict[str, Any], int, list[str]]:
    """Parse the Gantt grid that follows heading_index (-1 for a bare table).

    Raises for a table that can't be read as a grid; returns every token, merge, and
    width problem so a researcher sees them all at once.
    """
    spec = contract["timeline_table"]
    if not any(line.strip().startswith("|") for line in lines[heading_index + 1 :]):
        raise ContractError("No Research Timeline table found")
    raw_rows, end = table_after(lines, heading_index)
    if len(raw_rows) < 3 or not is_separator_row(raw_rows[1]):
        raise ContractError(
            "Research Timeline must be a Markdown table with a header, a separator row, and at least one activity row"
        )
    header = [parse_inline(cell)["text"].strip() for cell in raw_rows[0]]
    if header[:2] != spec["header"]:
        raise ContractError(
            "Research Timeline header must start with 'Phase | Activity', then one column per week: "
            f"{' | '.join(header)!r}"
        )
    weeks = header[2:]
    if not weeks:
        raise ContractError("Research Timeline needs at least one week column")
    if len(weeks) > spec["max_week_columns"]:
        raise ContractError(
            f"Research Timeline has {len(weeks)} week columns; the grid holds {spec['max_week_columns']}. "
            f"For a longer study, replace a run of middle weeks with one '{spec['filler_label']}' column"
        )
    body = raw_rows[2:]
    for row in body:
        if len(row) != len(header):
            raise ContractError(
                f"Research Timeline row has {len(row)} cells; the header has {len(header)}: {row!r}"
            )

    problems: list[str] = []
    filler = spec["filler_label"]
    fillers = [index for index, week in enumerate(weeks) if week == filler]
    if len(fillers) > 1:
        problems.append(f"Use at most one '{filler}' filler column")
    if fillers and fillers[0] in (0, len(weeks) - 1):
        problems.append(f"The '{filler}' column stands for skipped middle weeks, so it can't be the first or last week")
    named_weeks = [week for week in weeks if week != filler]
    if any(not week for week in weeks):
        problems.append("Every week column needs a label, such as 'Nov. 3'")
    elif len(set(named_weeks)) != len(named_weeks):
        problems.append("Week labels must be unique")

    label_pattern = re.compile(spec["phase_column"]["label_pattern"])
    phases: list[dict[str, Any]] = []
    rows: list[dict[str, Any]] = []
    source: list[list[str]] = [header]
    for index, cells in enumerate(body):
        parsed = [parse_inline(cell) for cell in cells]
        source.append([item["text"].strip() for item in parsed])
        phase_item, activity_item = parsed[0], parsed[1]
        phase_text = phase_item["text"].strip()
        if phase_item["italic"] or phase_item["links"] or activity_item["bold"] or activity_item["italic"] or activity_item["links"]:
            problems.append(f"Phase and Activity cells take plain text (the Phase cell may be bold): row {index + 1}")
        if phase_text:
            match = label_pattern.match(phase_text)
            expected = len(phases) + 1
            if not match:
                problems.append(
                    f"Phase cell must read 'Phase {expected}: Name' (leave it blank to continue the phase above): {phase_text!r}"
                )
                name = phase_text
            else:
                name = match.group(2).strip()
                if int(match.group(1)) != expected:
                    problems.append(f"Phases are numbered in order: expected 'Phase {expected}:', found {phase_text!r}")
            phases.append({"number": expected, "name": name, "start_row": index, "rows": 1})
        elif not phases:
            problems.append("The first activity row needs a Phase cell: 'Phase 1: Name'")
            phases.append({"number": 1, "name": "", "start_row": index, "rows": 1})
        else:
            phases[-1]["rows"] += 1
        activity = activity_item["text"].strip()
        if not activity:
            problems.append(f"Row {index + 1} needs an activity name")
        week_cells: list[dict[str, Any]] = []
        for week, item in zip(weeks, parsed[2:]):
            text = item["text"].strip()
            match = STATUS_CELL.match(text)
            if not text:
                week_cells.append({"status": None, "note": ""})
            elif match and match.group("status") in STATUS_COLORS and not (item["bold"] or item["italic"] or item["links"]):
                week_cells.append({"status": match.group("status"), "note": (match.group("note") or "").strip()})
            else:
                problems.append(
                    f"Week cell {week!r} for {activity or 'row ' + str(index + 1)!r} must be blank or start with "
                    f"[target], [spillover], or [event], plus an optional short plain note: {text!r}"
                )
                week_cells.append({"status": None, "note": ""})
        rows.append({"phase": len(phases) - 1, "activity": activity, "cells": week_cells})

    for column, week in enumerate(weeks):
        statuses = [row["cells"][column]["status"] for row in rows]
        if "event" in statuses and any(status != "event" for status in statuses):
            problems.append(
                f"[event] marks a fixed event for the whole week, so every row in {week!r} must be [event]"
            )
    timeline = {"weeks": weeks, "phases": phases, "rows": rows, "source": source}
    problems.extend(timeline_problems(timeline, contract))
    return timeline, end, problems


def parse_legend(item: dict[str, Any], timeline: dict[str, Any], contract: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    """Find the Green / Yellow / Red swatch words in the timing note."""
    legend = contract["timeline_table"]["legend"]
    text = item["text"]
    pattern = re.compile(
        r"^(?P<caveat>\S.*?)" + re.escape(legend["suffix"])
        + r"(?:" + re.escape(legend["event_suffix"]) + r"(?P<event>[^;]*\S))?\.?$",
        re.DOTALL,
    )
    match = pattern.match(text)
    uses_event = any(cell["status"] == "event" for row in timeline["rows"] for cell in row["cells"])
    expected = f"'<caveat>{legend['suffix']}'" + (f" plus '{legend['event_suffix']}<fixed event>'" if uses_event else "")
    if not match:
        return [], [f"The timing note under the timeline must end with the legend {expected}: {text!r}"]
    problems: list[str] = []
    if uses_event and not match.group("event"):
        problems.append(f"The grid marks [event] weeks, so the legend must end with '{legend['event_suffix']}<fixed event>'")
    if match.group("event") and not uses_event:
        problems.append(f"The legend names a fixed event, but no week is marked [event]; drop '{legend['event_suffix'].strip()} …'")
    swatches: list[dict[str, Any]] = []
    cursor = match.end("caveat")
    for word, status in legend["swatches"].items():
        if status == "event" and not match.group("event"):
            continue
        start = text.index(word, cursor)
        swatches.append({"start": start, "end": start + len(word), "status": status})
        cursor = start + len(word)
    return swatches, problems


def find_warning_banner(lines: list[str], start: int, end: int, contract: dict[str, Any]) -> tuple[int | None, str | None]:
    """Locate the one approved warning banner between start and end; reject an unknown or repeated one."""
    variants = contract["warning"]["variants"]
    found: list[tuple[int, str]] = []
    for i in range(start, end):
        text = parse_inline(lines[i].strip().removeprefix(">").strip())["text"]
        if text in variants.values():
            found.append((i, text))
        elif text.startswith("⚠"):
            raise ContractError(
                "Unrecognized warning banner; use exactly one of: "
                + " | ".join(repr(value) for value in variants.values())
                + f". Found: {text!r}"
            )
    if len(found) > 1:
        raise ContractError("Use one warning banner, not more than one")
    return found[0] if found else (None, None)


def parse_markdown(markdown: str) -> dict[str, Any]:
    """Parse an approved Option 4 intermediate Markdown document."""
    manifest, problems = _parse(markdown)
    if problems:
        raise ContractError("\n".join(problems))
    return manifest


def _parse(markdown: str) -> tuple[dict[str, Any], list[str]]:
    """Parse approved Markdown; structural errors raise, timeline and rule problems are returned."""
    contract = load_contract()
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

    problems: list[str] = []
    warning_index, warning = find_warning_banner(lines, updated_index + 1, timeline_heading, contract)
    notes: list[dict[str, Any]] = []
    after_opening = (warning_index if warning_index is not None else raci_indices[-1]) + 1
    rule_lines = [i for i in range(after_opening, timeline_heading) if lines[i].strip() == "---"]
    for i in range(after_opening, timeline_heading):
        value = lines[i].strip()
        if value and value != "---":
            if rule_lines and i > rule_lines[-1]:
                raise ContractError(f"Nothing but the rule goes between the opening and Research Timeline: {value!r}")
            notes.append(parse_inline(_strip_wrapping_italics(value)))
    if len(rule_lines) != 1:
        problems.append("Put one '---' rule line, with a blank line above it, right before '# Research Timeline'")

    timeline, timeline_end, timeline_issues = parse_timeline_table(lines, timeline_heading, contract)
    problems.extend(timeline_issues)

    timeline_note = None
    note_rules = 0
    for i in range(timeline_end, overview_heading):
        value = lines[i].strip()
        if value == "---":
            note_rules += 1
        elif value:
            if timeline_note is not None or note_rules:
                raise ContractError(f"Only the timing note and one rule go between the timeline and Project Plan Overview: {value!r}")
            timeline_note = parse_inline(_strip_wrapping_italics(value))
    if timeline_note is None:
        raise ContractError("Missing the timing note and legend after Research Timeline")
    if note_rules != 1:
        problems.append("Put one '---' rule line, with a blank line above it, right before '# Project Plan Overview'")
    swatches, legend_issues = parse_legend(timeline_note, timeline, contract)
    timeline_note["swatches"] = swatches
    problems.extend(legend_issues)

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
        list_kind, items = split_cell_items(cells[1], contract)
        rows.append(
            {
                "label": label,
                "items": items,
                "list": list_kind,
                "bulleted": list_kind is not None,
                "section": label in SECTIONS,
            }
        )

    labels = [row["label"] for row in rows]
    if len(labels) != len(set(labels)):
        raise ContractError("Project Plan Overview contains a duplicate row label")
    retired = [label for label in labels if label.upper() == label and label.title() in SECTIONS]
    if retired:
        raise ContractError(f"Section bands are Title Case now: write {retired[0].title()!r}, not {retired[0]!r}")
    section_positions = [labels.index(section) if section in labels else -1 for section in SECTIONS]
    if any(position < 0 for position in section_positions) or section_positions != sorted(section_positions):
        raise ContractError("The four Option 4 section rows are missing or out of order")
    key_index, project_index, deliverable_index, appendix_index = section_positions
    if labels[:key_index] != list(PLAIN_BOLD_LABELS):
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
    if labels[appendix_index:] != list(APPENDIX_ROWS):
        raise ContractError("Appendix must end with exactly the two approved document rows")
    for row in rows:
        if row["section"] and row["items"]:
            raise ContractError(f"Section row {row['label']!r} must not contain body content")
        if not row["section"] and not row["items"]:
            raise ContractError(f"Overview row {row['label']!r} must contain approved content")

    manifest = {
        "contract": "Option 4 — Leadership",
        "contract_version": contract["version"],
        "markdown_sha256": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "skill_files_sha256": skill_files_digest(),
        "top": {
            "breadcrumb": parse_inline(lines[breadcrumb_index].strip()),
            "title": parse_inline(lines[title_index][2:].strip()),
            "updated": parse_inline(lines[updated_index].strip()),
            "raci": raci,
            "warning": warning,
            "notes": notes,
        },
        "timeline": timeline,
        "timeline_note": timeline_note,
        "rows": rows,
    }
    manifest["manifest_sha256"] = manifest_digest(manifest)
    return manifest, problems


QUOTE_PATTERN = re.compile(r"“([^”]+)”|\"([^\"]+)\"")
QUOTE_MINIMUM_WORDS = 4


def _plan_items(manifest: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    items = [("Opening note", note) for note in manifest["top"]["notes"]]
    timeline = manifest["timeline"]
    items += [("Research Timeline", {"text": phase["name"]}) for phase in timeline["phases"]]
    items += [("Research Timeline", {"text": row["activity"]}) for row in timeline["rows"]]
    items += [
        ("Research Timeline", {"text": cell["note"]})
        for row in timeline["rows"] for cell in row["cells"] if cell["note"]
    ]
    items.append(("Timing note", manifest["timeline_note"]))
    items += [(row["label"], item) for row in manifest["rows"] for item in row["items"]]
    return items


def lint_markdown(markdown: str) -> tuple[list[str], list[str], list[str]]:
    """Return layout failures, content-rule flags to fix or accept, and quotes to confirm."""
    manifest, failures = _parse(markdown)
    rows = {row["label"]: row for row in manifest["rows"]}
    flags: list[str] = []

    background = rows["Background"]["items"]
    if not 3 <= len(background) <= 6:
        flags.append(f"Background has {len(background)} bullets; the rule is 3–6.")
    first = background[0] if background else {"text": "", "bold": []}
    lead = next((first["text"][start:end] for start, end in first["bold"] if start == 0), "")
    if not lead.strip().lower().startswith("why now"):
        flags.append("Background must open with a bullet whose bold lead-in is **Why now**.")
    if "Strategic fit" not in first["text"]:
        flags.append(
            "The Why now bullet must end with **Strategic fit:** — the priority a source names, "
            "or [TBD — fill in] (the H2 / OKR priority this supports)."
        )

    hypotheses = rows["Hypotheses"]["items"]
    empty_state = len(hypotheses) == 1 and "No hypotheses confirmed at planning time" in hypotheses[0]["text"]
    if not empty_state:
        for item in hypotheses:
            if "(Researcher hypothesis" not in item["text"] and "(Stakeholder assumption" not in item["text"]:
                flags.append(
                    "Hypothesis has no origin label — add *(Researcher hypothesis, inferred from …)* "
                    f"or *(Stakeholder assumption, stated by …)*: {item['text'][:90]!r}"
                )

    quotes: list[str] = []
    for where, item in _plan_items(manifest):
        for match in QUOTE_PATTERN.finditer(item["text"]):
            quote = match.group(1) or match.group(2)
            if len(quote.split()) >= QUOTE_MINIMUM_WORDS:
                quotes.append(f"{where}: “{quote}”")
    return failures, flags, quotes


SEND_TIMEOUT_SECONDS = 600
# macOS caps a command line plus environment at 1 MiB; leave room for the environment.
SEND_MAXIMUM_BODY_BYTES = 900_000
DOCUMENT_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{20,}")


def resolve_gws(explicit: str | None) -> str:
    if explicit:
        candidate = Path(explicit).expanduser()
        if not (candidate.is_file() and os.access(candidate, os.X_OK)):
            raise ContractError(f"--gws is not an executable file: {candidate}")
        return str(candidate)
    found = shutil.which("gws")
    if found:
        return found
    if GWS_FALLBACK_PATH.is_file() and os.access(GWS_FALLBACK_PATH, os.X_OK):
        return str(GWS_FALLBACK_PATH)
    raise ContractError(
        "gws not found on PATH or at ~/.config/gohan/bin/gws; pass --gws PATH, "
        "or apply the batch through a connector tool that takes native, revision-bound Google Docs requests"
    )


def send_batch(batch_path: str | Path, document_id: str, response_path: str | Path, gws: str | None = None) -> dict[str, Any]:
    """Apply one revision-bound batch through gws without a shell, then save its reply privately.

    gws reads the request body only from a process argument. This keeps the body out of the
    shell, shell history, and the chat transcript; it still sits in gws's process arguments
    while gws runs, which is why the safety reference asks for one-time approval.
    """
    if not DOCUMENT_ID_PATTERN.fullmatch(document_id):
        raise ContractError("--document-id must be the ID from the Doc URL (letters, digits, - and _)")
    batch = read_json_object(batch_path, "Batch")
    requests = batch.get("requests")
    if not isinstance(requests, list) or not requests:
        raise ContractError("Batch must contain a non-empty requests list")
    write_control = batch.get("writeControl")
    if not isinstance(write_control, dict) or not str(write_control.get("requiredRevisionId") or "").strip():
        raise ContractError("Batch is not bound to a revision; regenerate it from a freshly fetched Doc")
    body = json.dumps(batch, separators=(",", ":"))
    if len(body.encode("utf-8")) > SEND_MAXIMUM_BODY_BYTES:
        raise ContractError(
            f"Batch is too large to hand to gws ({len(body.encode('utf-8'))} bytes); "
            "apply it through a connector tool that takes native, revision-bound Google Docs requests"
        )
    command = [
        resolve_gws(gws),
        "docs",
        "documents",
        "batchUpdate",
        "--params",
        json.dumps({"documentId": document_id}),
        "--json",
        body,
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=SEND_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired as error:
        raise ContractError(
            "gws did not answer in time, so the outcome is unknown. Re-fetch the Doc and check its "
            "revision before anything else; do not resend this batch"
        ) from error
    record: dict[str, Any] = {"returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    try:
        reply = json.loads(result.stdout)
    except ValueError:
        reply = None
    if isinstance(reply, dict):
        record["response"] = reply
    write_json(response_path, record)
    if result.returncode != 0:
        raise ContractError(
            f"gws batchUpdate failed (exit {result.returncode}); details saved to {response_path}. "
            "Re-fetch the Doc before deciding what to do next; do not resend this batch"
        )
    if "response" not in record:
        raise ContractError(
            f"gws exited 0 but its reply was not a JSON object; saved to {response_path}. "
            "Re-fetch the Doc and verify the expected post-state; do not resend this batch"
        )
    return record["response"]



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
    """The label as the Doc shows it: the approved Markdown label, unchanged."""
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


def top_level_blocks(tab: dict[str, Any]) -> list[dict[str, Any]]:
    """Classify each body element as a table, a rule paragraph, an empty paragraph, or text."""
    blocks: list[dict[str, Any]] = []
    for element in tab["body"]["content"]:
        if "table" in element:
            blocks.append({"kind": "table", "element": element, "text": None})
        elif "paragraph" in element:
            paragraph = element["paragraph"]
            if any("horizontalRule" in child for child in paragraph.get("elements", [])):
                kind = "rule"
            elif paragraph_text(paragraph).strip():
                kind = "text"
            else:
                kind = "empty"
            blocks.append({"kind": kind, "element": element, "text": paragraph_text(paragraph).strip()})
    return blocks


def expected_layout(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Every visible top-level block in order, with the empty spacer paragraphs wanted before it."""
    top = manifest["top"]
    opening = [
        ("breadcrumb", top["breadcrumb"]["text"]),
        ("title", top["title"]["text"]),
        ("updated", top["updated"]["text"]),
        *[("raci", item["text"]) for item in top["raci"]],
        *([("warning", top["warning"])] if top.get("warning") else []),
        *[("note", item["text"]) for item in top.get("notes", [])],
    ]
    layout = [{"role": role, "kind": "text", "text": text, "spacers": 0} for role, text in opening]
    layout += [
        {"role": "rule", "kind": "rule", "text": None, "spacers": 1},
        {"role": "heading", "kind": "text", "text": "Research Timeline", "spacers": 0},
        {"role": "timeline", "kind": "table", "text": None, "spacers": 1},
        {"role": "legend", "kind": "text", "text": manifest["timeline_note"]["text"], "spacers": 0},
        {"role": "rule", "kind": "rule", "text": None, "spacers": 1},
        {"role": "heading", "kind": "text", "text": "Project Plan Overview", "spacers": 0},
        {"role": "overview", "kind": "table", "text": None, "spacers": 1},
    ]
    return layout


def match_layout(tab: dict[str, Any], manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Pair each expected block with the Doc's block and the empty paragraphs just before it."""
    layout = expected_layout(manifest)
    matched: list[dict[str, Any]] = []
    pending: list[dict[str, Any]] = []
    for block in top_level_blocks(tab):
        if block["kind"] == "empty":
            pending.append(block)
            continue
        found = block["text"] or f"<{block['kind']}>"
        if len(matched) == len(layout):
            raise ContractError(f"Unexpected content after the Project Plan Overview table: {found!r}")
        expected = layout[len(matched)]
        if block["kind"] != expected["kind"] or (expected["text"] is not None and block["text"] != expected["text"]):
            raise ContractError(
                "Opening, rules, timeline, or overview hierarchy does not match the approved manifest: "
                f"expected {expected['text'] or '<' + expected['kind'] + '>'!r}, found {found!r}"
            )
        matched.append(dict(expected, block=block, empties=pending))
        pending = []
    if len(matched) != len(layout):
        missing = layout[len(matched)]
        raise ContractError(
            "Opening, rules, timeline, or overview hierarchy does not match the approved manifest: "
            f"missing {missing['text'] or '<' + missing['kind'] + '>'!r}"
        )
    return matched


def _trim_trailing_empty(texts: list[str]) -> list[str]:
    trimmed = list(texts) or [""]
    while len(trimmed) > 1 and trimmed[-1] == "":
        trimmed.pop()
    return trimmed


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



def _cell_replacement(
    targets: list[tuple[int, list[dict[str, Any]]]], tab_id: str, cell: dict[str, Any], value: str
) -> None:
    """Rebuild a cell's text as value, one paragraph per line; skip a cell that already holds it."""
    paragraphs = cell_paragraphs(cell)
    current = "\n".join(paragraph_text(element["paragraph"]).rstrip("\n") for element in paragraphs)
    if current == value:
        return
    replace_target(targets, tab_id, paragraphs[0]["startIndex"], paragraphs[-1]["endIndex"] - 1, value)


def _descending(targets: list[tuple[int, list[dict[str, Any]]]]) -> list[dict[str, Any]]:
    requests: list[dict[str, Any]] = []
    for _, operations in sorted(targets, key=lambda pair: pair[0], reverse=True):
        requests.extend(operations)
    return requests


def build_normalize_requests(
    doc: dict[str, Any],
    manifest: dict[str, Any],
    *,
    required_revision_id: str | None = None,
) -> dict[str, Any]:
    """Rebuild imported cell text, remove the conversion header, merge the grid and bands, and fix spacers.

    One native batch can only use indices from the fetched snapshot, so the operations run
    from the end of the document toward the start: overview text, its structure, the spacer
    paragraphs after the timeline, the timeline's text and merges, then the spacers before it.
    """
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
    layout = match_layout(tab, manifest)

    timeline = manifest["timeline"]
    grid_rows = timeline_table["table"]["tableRows"]
    columns = 2 + len(timeline["weeks"])
    if len(grid_rows) != 1 + len(timeline["rows"]) or any(len(row["tableCells"]) != columns for row in grid_rows):
        raise ContractError(
            f"Timeline table must be {1 + len(timeline['rows'])} rows × {columns} columns, as approved"
        )
    for row_index, (row, source_row) in enumerate(zip(grid_rows, timeline["source"])):
        for column, (cell, expected) in enumerate(zip(row["tableCells"], source_row)):
            actual = re.sub(r"\s+", " ", " ".join(normalized_visible_items(cell))).strip()
            if actual != re.sub(r"\s+", " ", expected).strip():
                raise ContractError(
                    f"Imported timeline grid text differs from approved Markdown at row {row_index}, "
                    f"column {column}; re-import it before normalization"
                )

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

    overview_targets: list[tuple[int, list[dict[str, Any]]]] = []
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
        _cell_replacement(overview_targets, tab_id, left, output_label(source["label"]))
        if len(row["tableCells"]) >= 2:
            # Leading tabs set each item's nesting level when format creates the native list.
            value = "\n".join("\t" * item["level"] + item["text"] for item in source["items"])
            _cell_replacement(overview_targets, tab_id, row["tableCells"][1], value)

    requests = _descending(overview_targets)
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
        row = raw_overview_rows[index + row_offset]
        merged = len(row["tableCells"]) == 1 or row["tableCells"][0].get("tableCellStyle", {}).get("columnSpan", 1) > 1
        if source["section"] and not merged:
            requests.append({"mergeTableCells": {"tableRange": cell_range(tab_id, table_start, index, 0, 1, 2)}})

    # Spacer paragraphs: one empty paragraph before each rule and between each H1 and its table.
    timeline_start = timeline_table["startIndex"]
    late: list[tuple[int, list[dict[str, Any]]]] = []
    early: list[tuple[int, list[dict[str, Any]]]] = []
    previous: dict[str, Any] | None = None
    for entry in layout:
        empties, wanted = entry["empties"], entry["spacers"]
        operations: list[tuple[int, dict[str, Any]]] = []
        for extra in empties[: max(0, len(empties) - wanted)]:
            element = extra["element"]
            operations.append((
                element["startIndex"],
                {"deleteContentRange": {"range": docs_range(tab_id, element["startIndex"], element["endIndex"])}},
            ))
        if len(empties) < wanted:
            if entry["kind"] == "rule":
                index = entry["block"]["element"]["startIndex"]
            elif previous is not None and previous["kind"] == "text":
                index = previous["block"]["element"]["endIndex"] - 1
            else:
                raise ContractError("A table must follow its heading")
            operations.append((index, {"insertText": {"location": {"index": index, "tabId": tab_id}, "text": "\n"}}))
        for position, operation in operations:
            (late if position > timeline_start else early).append((position, [operation]))
        previous = entry
    requests.extend(_descending(late))

    timeline_targets: list[tuple[int, list[dict[str, Any]]]] = []
    for row, expected_row in zip(grid_rows, timeline_cell_paragraphs(timeline)):
        for cell, paragraphs in zip(row["tableCells"], expected_row):
            _cell_replacement(timeline_targets, tab_id, cell, "\n".join(paragraphs))
    requests.extend(_descending(timeline_targets))
    for phase in timeline["phases"]:
        head = grid_rows[phase["start_row"] + 1]["tableCells"][0].get("tableCellStyle", {})
        if phase["rows"] > 1 and head.get("rowSpan", 1) != phase["rows"]:
            requests.append(
                {"mergeTableCells": {"tableRange": cell_range(tab_id, timeline_start, phase["start_row"] + 1, 0, phase["rows"], 1)}}
            )
    requests.extend(_descending(early))
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


def update_rows(tab_id: str, table_start: int, rows: list[int], min_height: float) -> dict[str, Any]:
    return {
        "updateTableRowStyle": {
            "tableStartLocation": {"index": table_start, "tabId": tab_id},
            "rowIndices": rows,
            "tableRowStyle": {"minRowHeight": {"magnitude": min_height, "unit": "PT"}},
            "fields": "minRowHeight",
        }
    }


def table_columns(tab_id: str, table_start: int, widths: list[float]) -> list[dict[str, Any]]:
    return [
        {
            "updateTableColumnProperties": {
                "tableStartLocation": {"index": table_start, "tabId": tab_id},
                "columnIndices": [column],
                "tableColumnProperties": {
                    "widthType": "FIXED_WIDTH",
                    "width": {"magnitude": width, "unit": "PT"},
                },
                "fields": "widthType,width",
            }
        }
        for column, width in enumerate(widths)
    ]


def _pt(value: float) -> dict[str, Any]:
    return {"magnitude": value, "unit": "PT"}


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
    keep_together: bool | None = None,
    alignment: str | None = None,
    indent_start: float | None = None,
    indent_first: float | None = None,
) -> None:
    start, end = element["startIndex"], element["endIndex"]
    paragraph_style: dict[str, Any] = {
        "namedStyleType": named_style,
        "lineSpacing": line_spacing,
        "spaceAbove": _pt(space_above),
        "spaceBelow": _pt(space_below),
        "keepWithNext": keep_next,
    }
    paragraph_fields = "namedStyleType,lineSpacing,spaceAbove,spaceBelow,keepWithNext"
    for key, value in (
        ("keepLinesTogether", keep_together),
        ("alignment", alignment),
        ("indentStart", None if indent_start is None else _pt(indent_start)),
        ("indentFirstLine", None if indent_first is None else _pt(indent_first)),
    ):
        if value is not None:
            paragraph_style[key] = value
            paragraph_fields += f",{key}"

    # Named styles can clear direct overrides. Paragraph first; exact text style second.
    requests.append(update_paragraph(tab_id, start, end, paragraph_style, paragraph_fields))
    # An empty paragraph has no text to style, so style its paragraph mark; its size sets the line height.
    text_start, text_end = (start, end - 1) if end - 1 > start else (start, end)
    requests.append(
        update_text(
            tab_id,
            text_start,
            text_end,
            {
                "weightedFontFamily": {"fontFamily": font, "weight": 400},
                "fontSize": _pt(size),
                "bold": bold,
                "italic": italic,
                "underline": False,
                "foregroundColor": color,
            },
            # backgroundColor is listed but unset, which clears any highlight.
            "weightedFontFamily,fontSize,bold,italic,underline,foregroundColor,backgroundColor",
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
    offset: int = 0,
    swatch_colors: dict[str, dict[str, Any]] | None = None,
) -> None:
    """Apply approved bold, italic, links, and legend swatches; offset skips leading list tabs."""
    base = element["startIndex"] + offset
    text = item.get("text", "")

    def span(start: int, end: int) -> tuple[int, int]:
        return base + utf16_offset(text, start), base + utf16_offset(text, end)

    for start, end in item.get("bold", []):
        if end > start:
            requests.append(update_text(tab_id, *span(start, end), {"bold": True}, "bold"))
    for start, end in item.get("italic", []):
        if end > start:
            requests.append(update_text(tab_id, *span(start, end), {"italic": True}, "italic"))
    for link in item.get("links", []):
        if link["end"] > link["start"]:
            link_style: dict[str, Any] = {"link": {"url": link["url"]}, "underline": True}
            fields = "link,underline"
            if link_color is not None:
                link_style["foregroundColor"] = link_color
                fields += ",foregroundColor"
            requests.append(update_text(tab_id, *span(link["start"], link["end"]), link_style, fields))
    for swatch in item.get("swatches", []):
        if swatch_colors is None:
            raise ContractError("Legend swatches need their status colors")
        requests.append(
            update_text(
                tab_id, *span(swatch["start"], swatch["end"]),
                {"backgroundColor": swatch_colors[swatch["status"]]}, "backgroundColor",
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


def _named_metrics(contract: dict[str, Any], named_style: str) -> dict[str, Any]:
    style = contract["named_styles"][named_style]
    return {
        "named_style": named_style,
        "line_spacing": style["line_spacing_percent"],
        "space_above": style["space_above_pt"],
        "space_below": style["space_below_pt"],
        "keep_next": style["keep_with_next"],
        "keep_together": style["keep_lines_together"],
    }


def _defer_cell_cleanup(
    deferred: list[tuple[int, list[dict[str, Any]]]], tab_id: str, elements: list[dict[str, Any]], kept: int
) -> None:
    """Delete empty paragraphs left after a cell's content (a merge appends them), keeping the cell's last mark."""
    if len(elements) > kept:
        start = elements[kept - 1]["endIndex"] - 1
        end = elements[-1]["endIndex"] - 1
        deferred.append((start, [{"deleteContentRange": {"range": docs_range(tab_id, start, end)}}]))


def _matched_cell(elements: list[dict[str, Any]], expected: list[str], where: str) -> int:
    """How many of a cell's paragraphs hold its approved content; trailing empty paragraphs may follow."""
    texts = _trim_trailing_empty([paragraph_text(element["paragraph"]).rstrip("\n") for element in elements])
    wanted = _trim_trailing_empty(expected)
    if texts != wanted:
        raise ContractError(f"Normalized {where} differs from the manifest; run normalize first")
    return len(wanted)


def build_format_requests(
    doc: dict[str, Any],
    manifest: dict[str, Any],
    *,
    required_revision_id: str | None = None,
) -> dict[str, Any]:
    """Generate exact Option 4 formatting requests for a normalized document.

    Style operations use the snapshot's indices. Operations that change text (native list
    creation consumes leading tabs, and empty trailing paragraphs are deleted) come last,
    from the highest index to the lowest, so no earlier operation sees a shifted index.
    """
    validate_manifest(manifest)
    resolved_revision_id = resolve_required_revision_id(
        doc,
        required_revision_id,
        require=True,
    )
    contract = load_contract()
    tab_id, tab = get_tab(doc)
    tables = doc_tables(tab)
    if len(tables) != 2:
        raise ContractError("Formatting requires exactly the timeline and overview tables")
    layout = match_layout(tab, manifest)
    if any(len(entry["empties"]) != entry["spacers"] for entry in layout):
        raise ContractError("Spacer paragraphs around the rules and tables are not normalized; run normalize first")
    timeline_element, overview_element = tables
    timeline = manifest["timeline"]
    grid_rows = timeline_element["table"]["tableRows"]
    weeks = len(timeline["weeks"])
    if len(grid_rows) != 1 + len(timeline["rows"]) or any(len(row["tableCells"]) != 2 + weeks for row in grid_rows):
        raise ContractError("Timeline grid does not match the approved rows and weeks")
    for phase in timeline["phases"]:
        head = grid_rows[phase["start_row"] + 1]["tableCells"][0].get("tableCellStyle", {})
        if head.get("rowSpan", 1) != phase["rows"]:
            raise ContractError(f"Phase {phase['number']} is not merged across its rows; run normalize first")
    if len(overview_element["table"]["tableRows"]) != len(manifest["rows"]):
        raise ContractError("Normalize the overview table before formatting")

    colors = {name: hex_color(value) for name, value in contract["colors"].items()}
    link_color = colors["link_blue"]
    spacing = contract["spacing"]
    lists = contract["lists"]
    requests: list[dict[str, Any]] = []
    deferred: list[tuple[int, list[dict[str, Any]]]] = []

    page = contract["page"]
    requests.append(
        {
            "updateDocumentStyle": {
                "documentStyle": {
                    "documentFormat": {"documentMode": page["document_mode"]},
                    "flipPageOrientation": False,
                    "pageSize": {
                        "width": _pt(page["width_pt"]),
                        "height": _pt(page["height_pt"]),
                    },
                    "marginTop": _pt(page["margins_pt"]["top"]),
                    "marginBottom": _pt(page["margins_pt"]["bottom"]),
                    "marginLeft": _pt(page["margins_pt"]["left"]),
                    "marginRight": _pt(page["margins_pt"]["right"]),
                    "marginHeader": _pt(page["header_margin_pt"]),
                    "marginFooter": _pt(page["footer_margin_pt"]),
                    # useCustomHeaderFooterMargins is output-only; Docs derives it from these values.
                },
                "fields": "documentFormat.documentMode,flipPageOrientation,pageSize,marginTop,marginBottom,marginLeft,marginRight,marginHeader,marginFooter",
                "tabId": tab_id,
            }
        }
    )

    top = manifest["top"]
    blocks = {role: [entry["block"]["element"] for entry in layout if entry["role"] == role] for role in (
        "breadcrumb", "title", "updated", "raci", "warning", "note", "rule", "heading", "legend",
    )}
    body_font, body_size, _, _, body_color = _text_style(contract, "body")

    font, size, bold, italic, color = _text_style(contract, "breadcrumb")
    style_paragraph(
        requests, tab_id, blocks["breadcrumb"][0], font=font, size=size, bold=bold, italic=italic,
        color=color, **_named_metrics(contract, "SUBTITLE"),
    )
    apply_inline_styles(requests, tab_id, blocks["breadcrumb"][0], top["breadcrumb"], link_color=link_color)
    font, size, bold, italic, color = _text_style(contract, "title")
    style_paragraph(
        requests, tab_id, blocks["title"][0], font=font, size=size, bold=bold, italic=italic,
        color=color, **_named_metrics(contract, "TITLE"),
    )
    apply_inline_styles(requests, tab_id, blocks["title"][0], top["title"], link_color=link_color)
    style_paragraph(
        requests, tab_id, blocks["updated"][0], font=body_font, size=body_size, color=body_color,
        space_above=spacing["updated_space_above_pt"], space_below=spacing["updated_space_below_pt"],
    )
    apply_inline_styles(requests, tab_id, blocks["updated"][0], top["updated"], link_color=link_color)

    raci_elements = blocks["raci"]
    for element, item in zip(raci_elements, top["raci"]):
        style_paragraph(
            requests, tab_id, element, font=body_font, size=body_size, color=body_color,
            space_above=spacing["raci_space_above_pt"], space_below=spacing["raci_space_below_pt"],
            indent_start=spacing["raci_indent_start_pt"],
            indent_first=spacing["raci_indent_first_line_pt"],
        )
        apply_inline_styles(requests, tab_id, element, item, link_color=link_color)
    raci_start, raci_end = raci_elements[0]["startIndex"], raci_elements[-1]["endIndex"]
    requests.append(
        {
            "createParagraphBullets": {
                "range": docs_range(tab_id, raci_start, raci_end),
                "bulletPreset": lists["bullet_preset"],
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
                "indentStart": _pt(spacing["raci_indent_start_pt"]),
                "indentFirstLine": _pt(spacing["raci_indent_first_line_pt"]),
                "lineSpacing": spacing["line_spacing_percent"],
                "spaceAbove": _pt(spacing["raci_space_above_pt"]),
                "spaceBelow": _pt(spacing["raci_space_below_pt"]),
            },
            "indentStart,indentFirstLine,lineSpacing,spaceAbove,spaceBelow",
        )
    )

    if top.get("warning"):
        warning = blocks["warning"][0]
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
    for element, item in zip(blocks["note"], top.get("notes", [])):
        style_paragraph(
            requests, tab_id, element, font=note_font, size=note_size,
            bold=note_bold, italic=note_italic, color=note_color, space_below=8,
        )
        apply_inline_styles(requests, tab_id, element, item, link_color=link_color)

    # Spacer paragraphs and the two native rules: plain NORMAL_TEXT at the body size.
    for entry in layout:
        for spacer in entry["empties"]:
            style_paragraph(
                requests, tab_id, spacer["element"], font=body_font, size=body_size, color=body_color,
            )
    for rule in blocks["rule"]:
        requests.append(
            update_paragraph(
                tab_id, rule["startIndex"], rule["endIndex"],
                {"namedStyleType": "NORMAL_TEXT", "lineSpacing": spacing["line_spacing_percent"],
                 "spaceAbove": _pt(0), "spaceBelow": _pt(0), "keepWithNext": False},
                "namedStyleType,lineSpacing,spaceAbove,spaceBelow,keepWithNext",
            )
        )
        requests.append(
            update_text(
                tab_id, rule["endIndex"] - 1, rule["endIndex"],
                {"weightedFontFamily": {"fontFamily": body_font, "weight": 400}, "fontSize": _pt(body_size)},
                "weightedFontFamily,fontSize",
            )
        )

    heading_font, heading_size, heading_bold, heading_italic, heading_color = _text_style(contract, "heading")
    for heading in blocks["heading"]:
        style_paragraph(
            requests, tab_id, heading, font=heading_font, size=heading_size,
            bold=heading_bold, italic=heading_italic, color=heading_color,
            **_named_metrics(contract, "HEADING_1"),
        )

    legend = blocks["legend"][0]
    legend_font, legend_size, legend_bold, legend_italic, legend_color = _text_style(contract, "timeline_legend")
    style_paragraph(
        requests, tab_id, legend, font=legend_font, size=legend_size,
        bold=legend_bold, italic=legend_italic, color=legend_color,
    )
    apply_inline_styles(
        requests, tab_id, legend, manifest["timeline_note"], link_color=link_color,
        swatch_colors={status: colors[key] for status, key in STATUS_COLORS.items()},
    )

    # Research Timeline: the Gantt grid.
    spec = contract["timeline_table"]
    grid_start = timeline_element["startIndex"]
    body_rows = len(timeline["rows"])

    def padding(value: float) -> dict[str, Any]:
        return {key: _pt(value) for key in ("paddingTop", "paddingBottom", "paddingLeft", "paddingRight")}

    padding_fields = "paddingTop,paddingBottom,paddingLeft,paddingRight"
    requests.append(
        update_cell(
            tab_id, grid_start, 0, 0,
            {"backgroundColor": hex_color(spec["week_cells"]["default_background"]),
             **padding(spec["body_rows"]["padding_pt"]), "contentAlignment": spec["body_rows"]["content_alignment"]},
            f"backgroundColor,{padding_fields},contentAlignment",
            row_span=1 + body_rows, col_span=2 + weeks,
        )
    )
    requests.append(
        update_cell(
            tab_id, grid_start, 0, 0, {"backgroundColor": hex_color(spec["header_row"]["background"])},
            "backgroundColor", col_span=2 + weeks,
        )
    )
    week_header = spec["header_row"]["week_cells"]
    requests.append(
        update_cell(
            tab_id, grid_start, 0, 2,
            {**padding(week_header["padding_pt"]), "contentAlignment": week_header["content_alignment"]},
            f"{padding_fields},contentAlignment", col_span=weeks,
        )
    )
    requests.append(
        update_cell(
            tab_id, grid_start, 1, 0, {"backgroundColor": hex_color(spec["phase_column"]["background"])},
            "backgroundColor", row_span=body_rows, col_span=2,
        )
    )
    statuses = spec["week_cells"]["statuses"]
    for row_index, row in enumerate(timeline["rows"]):
        for column, cell in enumerate(row["cells"]):
            if cell["status"]:
                requests.append(
                    update_cell(
                        tab_id, grid_start, row_index + 1, column + 2,
                        {"backgroundColor": hex_color(statuses[cell["status"]])}, "backgroundColor",
                    )
                )
    requests.append(update_rows(tab_id, grid_start, [0], spec["header_row"]["min_row_height_pt"]))
    requests.append(update_rows(tab_id, grid_start, list(range(1, 1 + body_rows)), spec["body_rows"]["min_row_height_pt"]))
    requests.append(
        {"pinTableHeaderRows": {"tableStartLocation": {"index": grid_start, "tabId": tab_id}, "pinnedHeaderRowsCount": 0}}
    )
    header_text = spec["header_row"]["text"]
    for row_index, (row, expected_row) in enumerate(zip(grid_rows, timeline_cell_paragraphs(timeline))):
        for column, (cell, expected) in enumerate(zip(row["tableCells"], expected_row)):
            elements = cell_paragraphs(cell)
            kept = _matched_cell(elements, expected, f"timeline cell {row_index},{column}")
            if row_index == 0:
                cell_bold, cell_color = header_text["bold"], hex_color(header_text["color"])
                metrics = spec["header_row"]["week_cells" if column >= 2 else "label_cells"]
            else:
                cell_bold, cell_color = column == 0, body_color
                metrics = spec["body_rows"]
            for element in elements:
                style_paragraph(
                    requests, tab_id, element, font=body_font, size=body_size, bold=cell_bold,
                    color=cell_color, line_spacing=metrics["line_spacing_percent"],
                    alignment=metrics["alignment"],
                )
            _defer_cell_cleanup(deferred, tab_id, elements, kept)

    # Project Plan Overview.
    overview = contract["overview_table"]
    overview_start = overview_element["startIndex"]
    overview_rows = overview_element["table"]["tableRows"]
    border = {
        "color": hex_color(overview["border"]["color"]),
        "width": _pt(overview["border"]["width_pt"]),
        "dashStyle": overview["border"]["dash_style"],
    }
    borders = {key: border for key in ("borderTop", "borderBottom", "borderLeft", "borderRight")}
    requests.append(
        update_cell(
            tab_id, overview_start, 0, 0,
            {"backgroundColor": hex_color(overview["body_cell_background"]), **padding(overview["cell_padding_pt"]),
             "contentAlignment": overview["content_alignment"], **borders},
            f"backgroundColor,{padding_fields},contentAlignment,borderTop,borderBottom,borderLeft,borderRight",
            row_span=len(overview_rows), col_span=2,
        )
    )
    requests.append(update_rows(tab_id, overview_start, list(range(len(overview_rows))), overview["min_row_height_pt"]))
    requests.append(
        {"pinTableHeaderRows": {"tableStartLocation": {"index": overview_start, "tabId": tab_id}, "pinnedHeaderRowsCount": 0}}
    )
    band = overview["section_band"]
    section_font, section_size, section_bold, section_italic, section_color = _text_style(contract, "section_band")
    label_font, label_size, label_bold, _, label_color = _text_style(contract, "label")
    for row_index, (row, source) in enumerate(zip(overview_rows, manifest["rows"])):
        if len(row["tableCells"]) != 2:
            raise ContractError(f"Row {row_index} must keep its two cells")
        left, right = row["tableCells"]
        left_elements = cell_paragraphs(left)
        label = output_label(source["label"])
        kept = _matched_cell(left_elements, [label], f"label {label!r}")
        if source["section"]:
            if left.get("tableCellStyle", {}).get("columnSpan", 1) != band["column_span"]:
                raise ContractError(f"Section band {label!r} is not merged; run normalize first")
            requests.append(
                update_cell(
                    tab_id, overview_start, row_index, 0, {"backgroundColor": hex_color(band["background"])},
                    "backgroundColor", col_span=2,
                )
            )
            for element in left_elements:
                style_paragraph(
                    requests, tab_id, element, font=section_font, size=section_size,
                    bold=section_bold, italic=section_italic, color=section_color,
                    **_named_metrics(contract, band["named_style"]),
                )
            _defer_cell_cleanup(deferred, tab_id, left_elements, kept)
            continue

        named_label = "NORMAL_TEXT" if source["label"] in overview["plain_bold_labels"] else overview["label_named_style"]
        for element in left_elements:
            style_paragraph(
                requests, tab_id, element, font=label_font, size=label_size, bold=label_bold,
                color=label_color, **_named_metrics(contract, named_label),
            )
        _defer_cell_cleanup(deferred, tab_id, left_elements, kept)

        right_elements = cell_paragraphs(right)
        texts = _trim_trailing_empty([paragraph_text(element["paragraph"]).rstrip("\n") for element in right_elements])
        tabbed = ["\t" * item["level"] + item["text"] for item in source["items"]]
        plain = [item["text"] for item in source["items"]]
        nested = any(item["level"] for item in source["items"])
        if texts == tabbed:
            fresh = True
        elif texts == plain and all(
            (element["paragraph"].get("bullet", {}).get("nestingLevel", 0) == item["level"] and "bullet" in element["paragraph"])
            for element, item in zip(right_elements, source["items"])
        ):
            fresh = False
        else:
            raise ContractError(f"Normalized content mismatch in {source['label']!r}; run normalize first")
        kept_elements = right_elements[: len(source["items"])]
        for element, item in zip(right_elements, source["items"]):
            style_paragraph(
                requests, tab_id, element, font=body_font, size=body_size, color=body_color,
                line_spacing=overview["line_spacing_percent"],
            )
            apply_inline_styles(
                requests, tab_id, element, item, link_color=link_color,
                offset=item["level"] if fresh else 0,
            )
        for element in right_elements[len(source["items"]) :]:
            style_paragraph(
                requests, tab_id, element, font=body_font, size=body_size, color=body_color,
                line_spacing=overview["line_spacing_percent"],
            )
        _defer_cell_cleanup(deferred, tab_id, right_elements, len(source["items"]))
        if source["list"]:
            operations: list[dict[str, Any]] = []
            if fresh or not nested:
                preset = lists["bullet_preset"] if source["list"] == "BULLET" else lists["number_preset"]
                operations.append(
                    {
                        "createParagraphBullets": {
                            "range": docs_range(tab_id, kept_elements[0]["startIndex"], kept_elements[-1]["endIndex"]),
                            "bulletPreset": preset,
                        }
                    }
                )
            # createParagraphBullets consumes each paragraph's leading tabs, so later paragraphs move up.
            shift = 0
            for element, item in zip(kept_elements, source["items"]):
                tabs = item["level"] if fresh else 0
                indent = lists["indent_step_pt"] * (item["level"] + 1)
                operations.append(
                    update_paragraph(
                        tab_id, element["startIndex"] - shift, element["endIndex"] - shift - tabs,
                        {
                            "indentStart": _pt(indent),
                            "indentFirstLine": _pt(indent - lists["first_line_hang_pt"]),
                            "lineSpacing": overview["line_spacing_percent"],
                            "spaceAbove": _pt(0),
                            "spaceBelow": _pt(0),
                        },
                        "indentStart,indentFirstLine,lineSpacing,spaceAbove,spaceBelow",
                    )
                )
                shift += tabs
            deferred.append((kept_elements[0]["startIndex"], operations))

    timeline_widths = [spec["column_widths_pt"]["phase"], spec["column_widths_pt"]["activity"]]
    timeline_widths += [spec["column_widths_pt"]["week"]] * weeks
    requests.extend(table_columns(tab_id, grid_start, timeline_widths))
    requests.extend(table_columns(tab_id, overview_start, overview["column_widths_pt"]))

    for _, operations in sorted(deferred, key=lambda pair: pair[0], reverse=True):
        requests.extend(operations)
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


def _label(element: dict[str, Any]) -> str:
    return paragraph_text(element["paragraph"]).strip()


def _assert_named_style(element: dict[str, Any], expected: str) -> None:
    actual = element["paragraph"].get("paragraphStyle", {}).get("namedStyleType", "NORMAL_TEXT")
    if actual != expected:
        raise ContractError(f"{_label(element)!r} uses {actual}; expected {expected}")


def _assert_text_style(
    element: dict[str, Any], named: dict[str, dict[str, Any]], expected: dict[str, Any]
) -> None:
    style = _effective_style(element["paragraph"], _first_run(element), named)
    if style.get("weightedFontFamily", {}).get("fontFamily") != expected["font"]:
        raise ContractError(f"Wrong font for {_label(element)!r}")
    if style.get("fontSize", {}).get("magnitude") != expected["size_pt"]:
        raise ContractError(f"Wrong font size for {_label(element)!r}")
    if style.get("bold", False) != expected.get("bold", False):
        raise ContractError(f"Wrong bold style for {_label(element)!r}")
    if style.get("italic", False) != expected.get("italic", False):
        raise ContractError(f"Wrong italic style for {_label(element)!r}")
    if _rgb(style.get("foregroundColor"), default_black=True) != _hex_tuple(expected["color"]):
        raise ContractError(f"Wrong text color for {_label(element)!r}")


def _assert_base_text_style(
    element: dict[str, Any], named: dict[str, dict[str, Any]], expected: dict[str, Any],
    link_color: str = "#1155CC",
) -> None:
    """Check font, size, and color across every visible run; linked runs use the link color."""
    for child in element["paragraph"].get("elements", []):
        run = child.get("textRun") or child.get("person")
        if run is None or ("textRun" in child and not run.get("content", "").rstrip("\n")):
            continue
        style = _effective_style(element["paragraph"], run, named)
        if style.get("weightedFontFamily", {}).get("fontFamily") != expected["font"]:
            raise ContractError(f"Wrong run font in {_label(element)!r}")
        if style.get("fontSize", {}).get("magnitude") != expected["size_pt"]:
            raise ContractError(f"Wrong run font size in {_label(element)!r}")
        color = link_color if (style.get("link") or {}).get("url") else expected["color"]
        if _rgb(style.get("foregroundColor"), default_black=True) != _hex_tuple(color):
            raise ContractError(f"Wrong run color in {_label(element)!r}")


def _assert_inline_exact(
    element: dict[str, Any], item: dict[str, Any], named: dict[str, dict[str, Any]],
    *, base_bold: bool = False, base_italic: bool = False,
    swatch_colors: dict[str, str] | None = None,
) -> None:
    """Require approved bold/italic/link/swatch spans and reject unapproved emphasis or highlights."""
    text = item.get("text", "")
    units = utf16_offset(text, len(text))
    expected_bold = [base_bold] * units
    expected_italic = [base_italic] * units
    expected_links: list[str | None] = [None] * units
    expected_backgrounds: list[tuple[int, int, int] | None] = [None] * units

    def span(start: int, end: int) -> slice:
        return slice(utf16_offset(text, start), utf16_offset(text, end))

    for start, end in item.get("bold", []):
        piece = span(start, end)
        expected_bold[piece] = [True] * (piece.stop - piece.start)
    for start, end in item.get("italic", []):
        piece = span(start, end)
        expected_italic[piece] = [True] * (piece.stop - piece.start)
    for link in item.get("links", []):
        piece = span(link["start"], link["end"])
        expected_links[piece] = [link["url"]] * (piece.stop - piece.start)
    for swatch in item.get("swatches", []):
        piece = span(swatch["start"], swatch["end"])
        expected_backgrounds[piece] = [_hex_tuple((swatch_colors or {})[swatch["status"]])] * (piece.stop - piece.start)

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
        actual_underline = bool(style.get("underline", False))
        actual_background = _rgb(style.get("backgroundColor"))
        for offset in range(start, end):
            if actual_bold != expected_bold[offset]:
                raise ContractError(f"Inline bold mismatch in {text!r}")
            if actual_italic != expected_italic[offset]:
                raise ContractError(f"Inline italic mismatch in {text!r}")
            if actual_link != expected_links[offset]:
                raise ContractError(f"Inline link mismatch in {text!r}")
            if actual_underline != (expected_links[offset] is not None):
                raise ContractError(f"Underline mismatch in {text!r}; only links are underlined")
            if actual_background != expected_backgrounds[offset]:
                raise ContractError(f"Text highlight mismatch in {text!r}; only legend swatches carry a background")
            covered[offset] = True
    if units and not all(covered):
        raise ContractError(f"Inline style coverage is incomplete in {text!r}")


def _magnitude(style: dict[str, Any], key: str, default: float = 0) -> float:
    return style.get(key, {}).get("magnitude", default)


def _assert_cell_box(cell: dict[str, Any], *, padding: float, alignment: str, where: str) -> None:
    # Google Docs omits the default 5pt padding and TOP alignment from read responses.
    style = cell.get("tableCellStyle", {})
    for key in ("paddingTop", "paddingBottom", "paddingLeft", "paddingRight"):
        if _magnitude(style, key, 5) != padding:
            raise ContractError(f"Wrong {key} in {where}: {_magnitude(style, key, 5)}pt")
    if style.get("contentAlignment", "TOP") != alignment:
        raise ContractError(f"Wrong vertical alignment in {where}")


def _assert_paragraph_metrics(
    element: dict[str, Any], *, line_spacing: int, space_above: float = 0,
    space_below: float = 0, keep_next: bool | None = None,
    indent_start: float | None = None, indent_first: float | None = None,
    alignment: str | None = None,
) -> None:
    style = element["paragraph"].get("paragraphStyle", {})
    text = _label(element)
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
    if alignment is not None and style.get("alignment", "START") != alignment:
        raise ContractError(f"Wrong alignment for {text!r}")


def _assert_role(
    element: dict[str, Any], named: dict[str, dict[str, Any]], contract: dict[str, Any],
    named_style: str, text_style: dict[str, Any], item: dict[str, Any] | None = None,
) -> None:
    """A paragraph that stands in for a reference named style: its type, metrics, and text."""
    metrics = contract["named_styles"][named_style]
    _assert_named_style(element, named_style)
    _assert_text_style(element, named, text_style)
    _assert_base_text_style(element, named, text_style)
    _assert_inline_exact(
        element, item or {"text": _label(element), "bold": [], "italic": [], "links": []}, named,
        base_bold=text_style.get("bold", False), base_italic=text_style.get("italic", False),
    )
    _assert_paragraph_metrics(
        element, line_spacing=metrics["line_spacing_percent"], space_above=metrics["space_above_pt"],
        space_below=metrics["space_below_pt"], keep_next=metrics["keep_with_next"],
    )
    if bool(element["paragraph"].get("paragraphStyle", {}).get("keepLinesTogether", False)) != metrics["keep_lines_together"]:
        raise ContractError(f"Wrong keep-lines-together setting for {_label(element)!r}")


def _assert_spacer(element: dict[str, Any], named: dict[str, dict[str, Any]], contract: dict[str, Any], what: str) -> None:
    if "bullet" in element["paragraph"]:
        raise ContractError(f"{what} has a bullet")
    _assert_named_style(element, "NORMAL_TEXT")
    _assert_paragraph_metrics(element, line_spacing=contract["spacing"]["line_spacing_percent"], keep_next=False)
    runs = [child["textRun"] for child in element["paragraph"].get("elements", []) if "textRun" in child]
    size = _effective_style(element["paragraph"], runs[-1], named).get("fontSize", {}).get("magnitude") if runs else None
    if size != contract["typography"]["body"]["size_pt"]:
        raise ContractError(f"{what} is {size}pt; spacer lines use the {contract['typography']['body']['size_pt']}pt body size")


def _assert_list_glyph(
    element: dict[str, Any], lists: dict[str, Any], contract: dict[str, Any], kind: str, level: int, where: str
) -> None:
    """A native list paragraph at the approved level, with ● ○ ■ bullets or 1. / 1.1. numbers."""
    bullet = element["paragraph"].get("bullet")
    if bullet is None:
        raise ContractError(f"{where} is missing its native list paragraph")
    if bullet.get("nestingLevel", 0) != level:
        raise ContractError(f"{where} sits at list level {bullet.get('nestingLevel', 0)}; expected {level}")
    levels = lists.get(bullet.get("listId"), {}).get("listProperties", {}).get("nestingLevels", [])
    if level >= len(levels):
        raise ContractError(f"{where} uses a list without level {level}")
    definition = levels[level]
    if kind == "BULLET":
        glyphs = contract["lists"]["bullet_glyphs"]
        if definition.get("glyphSymbol") != glyphs[level % len(glyphs)]:
            raise ContractError(f"{where} uses glyph {definition.get('glyphSymbol')!r}; expected {glyphs[level % len(glyphs)]!r}")
    else:
        expected_format = "".join(f"%{index}." for index in range(level + 1))
        if definition.get("glyphType") != contract["lists"]["number_glyph_type"] or definition.get("glyphFormat") != expected_format:
            raise ContractError(f"{where} must be numbered {expected_format!r} with DECIMAL glyphs")


def _assert_list_item(
    element: dict[str, Any], lists: dict[str, Any], contract: dict[str, Any], kind: str, level: int, where: str
) -> None:
    _assert_list_glyph(element, lists, contract, kind, level, where)
    indent = contract["lists"]["indent_step_pt"] * (level + 1)
    _assert_paragraph_metrics(
        element, line_spacing=contract["overview_table"]["line_spacing_percent"],
        indent_start=indent, indent_first=indent - contract["lists"]["first_line_hang_pt"],
    )


def _row_height(row: dict[str, Any]) -> float:
    return _magnitude(row.get("tableRowStyle", {}), "minRowHeight")


def _assert_widths(table: dict[str, Any], expected: list[float], name: str) -> None:
    properties = table["table"].get("tableStyle", {}).get("tableColumnProperties", [])
    actual = [item.get("width", {}).get("magnitude") for item in properties]
    if actual != expected or any(item.get("widthType") != "FIXED_WIDTH" for item in properties):
        raise ContractError(f"Wrong {name} table widths: {actual}")


def _verify_timeline(
    element: dict[str, Any], manifest: dict[str, Any], contract: dict[str, Any], named: dict[str, dict[str, Any]]
) -> None:
    spec = contract["timeline_table"]
    timeline = manifest["timeline"]
    rows = element["table"]["tableRows"]
    weeks = len(timeline["weeks"])
    if len(rows) != 1 + len(timeline["rows"]) or any(len(row["tableCells"]) != 2 + weeks for row in rows):
        raise ContractError("Timeline grid does not match the approved rows and weeks")
    widths = spec["column_widths_pt"]
    _assert_widths(element, [widths["phase"], widths["activity"], *[widths["week"]] * weeks], "timeline")
    if rows[0].get("tableRowStyle", {}).get("tableHeader", False):
        raise ContractError("Timeline header row must not be pinned")
    if _row_height(rows[0]) != spec["header_row"]["min_row_height_pt"]:
        raise ContractError("Timeline header row has a minimum height")
    if any(_row_height(row) != spec["body_rows"]["min_row_height_pt"] for row in rows[1:]):
        raise ContractError(f"Timeline activity rows must have a {spec['body_rows']['min_row_height_pt']}pt minimum height")
    header_text = dict(spec["header_row"]["text"])
    body = contract["typography"]["body"]
    statuses = spec["week_cells"]["statuses"]
    heads = {phase["start_row"]: phase for phase in timeline["phases"]}
    for row_index, (row, expected_row) in enumerate(zip(rows, timeline_cell_paragraphs(timeline))):
        for column, (cell, expected) in enumerate(zip(row["tableCells"], expected_row)):
            where = f"timeline cell {row_index},{column}"
            style = cell.get("tableCellStyle", {})
            if style.get("columnSpan", 1) != 1:
                raise ContractError(f"{where} spans columns; only Phase cells merge, and only down")
            if row_index == 0:
                background = spec["header_row"]["background"]
                metrics = spec["header_row"]["week_cells" if column >= 2 else "label_cells"]
                text_style = header_text
            else:
                source = timeline["rows"][row_index - 1]
                if column == 0:
                    phase = heads.get(row_index - 1)
                    span = phase["rows"] if phase else 1
                    if style.get("rowSpan", 1) != span:
                        raise ContractError(
                            f"Phase cell in timeline row {row_index} spans {style.get('rowSpan', 1)} rows; expected {span}"
                        )
                background = (
                    spec["phase_column"]["background"] if column < 2
                    else statuses.get(source["cells"][column - 2]["status"], spec["week_cells"]["default_background"])
                )
                metrics = spec["body_rows"]
                text_style = dict(body, bold=column == 0)
            if _rgb(style.get("backgroundColor")) != _hex_tuple(background):
                raise ContractError(f"Timeline background mismatch at {row_index},{column}")
            _assert_cell_box(cell, padding=metrics["padding_pt"], alignment=metrics["content_alignment"], where=where)
            elements = cell_paragraphs(cell)
            if [paragraph_text(item["paragraph"]).rstrip("\n") for item in elements] != expected:
                raise ContractError(f"Timeline content mismatch in {where}")
            for paragraph in elements:
                if "bullet" in paragraph["paragraph"]:
                    raise ContractError(f"{where} has an unexpected bullet")
                if not _label(paragraph):
                    continue
                _assert_text_style(paragraph, named, text_style)
                _assert_base_text_style(paragraph, named, text_style)
                _assert_inline_exact(
                    paragraph, {"text": paragraph_text(paragraph["paragraph"]).rstrip("\n"), "bold": [], "italic": [], "links": []},
                    named, base_bold=text_style.get("bold", False),
                )
                _assert_paragraph_metrics(
                    paragraph, line_spacing=metrics["line_spacing_percent"], alignment=metrics["alignment"],
                )


def _verify_overview(
    element: dict[str, Any], manifest: dict[str, Any], contract: dict[str, Any],
    named: dict[str, dict[str, Any]], lists: dict[str, Any],
) -> None:
    overview = contract["overview_table"]
    rows = element["table"]["tableRows"]
    if len(rows) != len(manifest["rows"]):
        raise ContractError("Overview row count does not match the Option 4 manifest")
    _assert_widths(element, overview["column_widths_pt"], "overview")
    if rows[0].get("tableRowStyle", {}).get("tableHeader", False):
        raise ContractError("Overview first row must not be pinned")
    border = overview["border"]
    band = overview["section_band"]
    body = contract["typography"]["body"]
    for row_index, (row, source) in enumerate(zip(rows, manifest["rows"])):
        label = output_label(source["label"])
        if _row_height(row) != overview["min_row_height_pt"]:
            raise ContractError(f"Overview row {label!r} must have a {overview['min_row_height_pt']}pt minimum height")
        if len(row["tableCells"]) != 2:
            raise ContractError(f"Overview row {label!r} must report its two cells")
        left, right = row["tableCells"]
        for cell in row["tableCells"]:
            style = cell.get("tableCellStyle", {})
            _assert_cell_box(cell, padding=overview["cell_padding_pt"], alignment=overview["content_alignment"], where=f"row {label!r}")
            for side in ("borderTop", "borderBottom", "borderLeft", "borderRight"):
                value = style.get(side, {})
                if (
                    _magnitude(value, "width", -1) != border["width_pt"]
                    or value.get("dashStyle") != border["dash_style"]
                    or _rgb(value.get("color"), default_black=True) != _hex_tuple(border["color"])
                ):
                    raise ContractError(f"Overview row {label!r} needs {border['width_pt']}pt solid black borders on every side")
        span = left.get("tableCellStyle", {}).get("columnSpan", 1)
        if source["section"]:
            if span != band["column_span"]:
                raise ContractError(f"Section band {label!r} must be one merged cell (columnSpan {band['column_span']})")
            if any(_rgb(cell.get("tableCellStyle", {}).get("backgroundColor")) != _hex_tuple(band["background"]) for cell in row["tableCells"]):
                raise ContractError(f"Overview background mismatch in band {label!r}")
            elements = cell_paragraphs(left)
            if [_label(item) for item in elements] != [label]:
                raise ContractError(f"Section band {label!r} must hold exactly its Title Case name")
            if any(_label(item) for item in cell_paragraphs(right)):
                raise ContractError(f"Section band {label!r} has text in its covered cell")
            section_style = contract["typography"]["section_band"]
            _assert_role(elements[0], named, contract, band["named_style"], section_style)
            continue
        if span != 1:
            raise ContractError(f"Overview row {label!r} is merged; only section bands merge")
        if any(_rgb(cell.get("tableCellStyle", {}).get("backgroundColor")) != _hex_tuple(overview["body_cell_background"]) for cell in row["tableCells"]):
            raise ContractError(f"Overview background mismatch in row {label!r}")
        left_elements = cell_paragraphs(left)
        if [_label(item) for item in left_elements] != [label] or "bullet" in left_elements[0]["paragraph"]:
            raise ContractError(f"Overview label mismatch: {[_label(item) for item in left_elements]!r}")
        named_label = "NORMAL_TEXT" if source["label"] in overview["plain_bold_labels"] else overview["label_named_style"]
        label_style = contract["typography"]["label"]
        if named_label == "NORMAL_TEXT":
            _assert_named_style(left_elements[0], "NORMAL_TEXT")
            _assert_text_style(left_elements[0], named, label_style)
            _assert_base_text_style(left_elements[0], named, label_style)
            _assert_inline_exact(left_elements[0], {"text": label, "bold": [], "italic": [], "links": []}, named, base_bold=True)
            _assert_paragraph_metrics(left_elements[0], line_spacing=overview["line_spacing_percent"], keep_next=False)
        else:
            _assert_role(left_elements[0], named, contract, named_label, label_style)
        right_elements = cell_paragraphs(right)
        if [paragraph_text(item["paragraph"]).rstrip("\n") for item in right_elements] != [item["text"] for item in source["items"]]:
            raise ContractError(f"Overview content mismatch in {source['label']!r}")
        for paragraph, item in zip(right_elements, source["items"]):
            _assert_base_text_style(paragraph, named, body)
            _assert_inline_exact(paragraph, item, named)
            if source["list"]:
                _assert_list_item(paragraph, lists, contract, source["list"], item["level"], f"{source['label']!r} item")
            else:
                if "bullet" in paragraph["paragraph"]:
                    raise ContractError(f"Overview row {source['label']!r} has unexpected bullets")
                _assert_paragraph_metrics(paragraph, line_spacing=overview["line_spacing_percent"])


def verify_document(doc: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    """Validate content and every machine-checkable Option 4 visual invariant."""
    validate_manifest(manifest)
    contract = load_contract()
    _, tab = get_tab(doc)
    named = _named_text_styles(tab)
    lists = tab.get("lists", {})
    tables = doc_tables(tab)
    if len(tables) != contract["structure"]["top_level_tables"]:
        raise ContractError("Final document must contain exactly two tables")
    layout = match_layout(tab, manifest)
    for entry in layout:
        if len(entry["empties"]) != entry["spacers"]:
            where = entry["text"] or ("the rule" if entry["kind"] == "rule" else f"the {entry['role']} table")
            raise ContractError(
                f"Expected {entry['spacers']} empty spacer paragraph(s) before {where!r}; found {len(entry['empties'])}"
            )
    blocks = {role: [entry["block"]["element"] for entry in layout if entry["role"] == role] for role in (
        "breadcrumb", "title", "updated", "raci", "warning", "note", "rule", "heading", "legend",
    )}
    if len(blocks["rule"]) != contract["structure"]["native_horizontal_rules"]:
        raise ContractError("Final document must contain exactly two native horizontal rules")

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

    top = manifest["top"]
    typography = contract["typography"]
    spacing = contract["spacing"]
    _assert_role(blocks["breadcrumb"][0], named, contract, "SUBTITLE", typography["breadcrumb"], top["breadcrumb"])
    _assert_role(blocks["title"][0], named, contract, "TITLE", typography["title"], top["title"])
    for heading in blocks["heading"]:
        _assert_role(heading, named, contract, "HEADING_1", typography["heading"])
    updated = blocks["updated"][0]
    _assert_named_style(updated, "NORMAL_TEXT")
    _assert_text_style(updated, named, typography["body"])
    _assert_base_text_style(updated, named, typography["body"])
    _assert_inline_exact(updated, top["updated"], named)
    _assert_paragraph_metrics(
        updated, line_spacing=spacing["line_spacing_percent"],
        space_above=spacing["updated_space_above_pt"], space_below=spacing["updated_space_below_pt"],
    )

    for element, item in zip(blocks["raci"], top["raci"]):
        if "bullet" not in element["paragraph"]:
            raise ContractError(f"RACI item is not a native bullet: {item['role']}")
        _assert_list_glyph(element, lists, contract, "BULLET", 0, f"RACI {item['role']}")
        _assert_base_text_style(element, named, typography["body"])
        _assert_inline_exact(element, item, named)
        _assert_paragraph_metrics(
            element, line_spacing=spacing["line_spacing_percent"],
            space_above=spacing["raci_space_above_pt"], space_below=spacing["raci_space_below_pt"],
            indent_start=spacing["raci_indent_start_pt"], indent_first=spacing["raci_indent_first_line_pt"],
        )

    if top.get("warning"):
        warning = blocks["warning"][0]
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
            raise ContractError("Warning banner does not use full-paragraph pale-yellow shading")

    for element, item in zip(blocks["note"], top.get("notes", [])):
        _assert_base_text_style(element, named, typography["context_note"])
        _assert_inline_exact(element, item, named, base_italic=True)
        _assert_paragraph_metrics(element, line_spacing=115, space_below=8)

    for entry in layout:
        for spacer in entry["empties"]:
            _assert_spacer(spacer["element"], named, contract, f"Spacer before {entry['text'] or entry['role']!r}")
    for rule in blocks["rule"]:
        _assert_spacer(rule, named, contract, "Horizontal-rule paragraph")

    legend = blocks["legend"][0]
    legend_style = typography["timeline_legend"]
    _assert_named_style(legend, "NORMAL_TEXT")
    _assert_text_style(legend, named, legend_style)
    _assert_base_text_style(legend, named, legend_style)
    _assert_inline_exact(
        legend, manifest["timeline_note"], named, base_italic=True,
        swatch_colors=contract["timeline_table"]["week_cells"]["statuses"],
    )
    _assert_paragraph_metrics(legend, line_spacing=spacing["line_spacing_percent"])

    timeline_element, overview_element = tables
    _verify_timeline(timeline_element, manifest, contract, named)
    _verify_overview(overview_element, manifest, contract, named, lists)

    return [
        "Option 4 page geometry and named-style typography",
        "two native rules and their spacer paragraphs",
        "Gantt timeline grid: widths, phase merges, status fills, and legend swatches",
        "Project Plan Overview order, merged section bands, labels, borders, and row heights",
        "native ● ○ ■ bullets and DECIMAL numbered lists",
        "approved emphasis and #1155CC links, with no stray highlights",
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

    timeline = subparsers.add_parser(
        "timeline", help="Check that a draft Gantt timeline grid is well formed and every label fits its column"
    )
    timeline.add_argument("markdown", help="a file holding the draft timeline table, or the whole plan")

    lint = subparsers.add_parser(
        "lint", help="Check assembled Markdown for layout failures and content-rule gaps"
    )
    lint.add_argument("markdown")

    manifest = subparsers.add_parser("manifest", help="Parse approved Markdown into a build manifest")
    manifest.add_argument("markdown")
    manifest.add_argument("output")

    send = subparsers.add_parser(
        "send", help="Apply one revision-bound batch through gws without a shell"
    )
    send.add_argument("batch_json")
    send.add_argument("--document-id", required=True)
    send.add_argument("--response", required=True, help="private file for gws's reply")
    send.add_argument("--gws", help="path to gws (default: PATH, then ~/.config/gohan/bin/gws)")

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
    if args.command == "timeline":
        lines = Path(args.markdown).read_text(encoding="utf-8").splitlines()
        heading = next((i for i, line in enumerate(lines) if line.strip() == "# Research Timeline"), -1)
        contract = load_contract()
        grid, _, problems = parse_timeline_table(lines, heading, contract)
        for line in timeline_report(grid, contract):
            print(line)
        for problem in problems:
            print(f"FAIL: {problem}")
        if problems:
            return 1
        print(
            f"PASS: the {len(grid['rows'])}-row, {len(grid['weeks'])}-week grid is well formed "
            "and every label fits its column"
        )
        return 0
    if args.command == "lint":
        failures, flags, quotes = lint_markdown(Path(args.markdown).read_text(encoding="utf-8"))
        for failure in failures:
            print(f"FAIL: {failure}")
        for flag in flags:
            print(f"FIX OR ACCEPT: {flag}")
        for quote in quotes:
            print(
                f"CONFIRM QUOTE: {quote} — keep the quote marks only if this is word for word in the "
                "cited source artifact; otherwise paraphrase"
            )
        if not (failures or flags or quotes):
            print("PASS: no layout failures, content-rule gaps, or quotes to confirm")
        else:
            print(
                f"lint: {len(failures)} layout failure(s), {len(flags)} to fix or accept, "
                f"{len(quotes)} quote(s) to confirm"
            )
        return 1 if failures else 0
    if args.command == "send":
        reply = send_batch(args.batch_json, args.document_id, args.response, args.gws)
        revision = (reply.get("writeControl") or {}).get("requiredRevisionId", "unavailable")
        print(f"PASS: batch applied; new revision {revision}; reply saved to {args.response}")
        return 0
    if args.command == "manifest":
        markdown = Path(args.markdown).read_text(encoding="utf-8")
        value = parse_markdown(markdown)
        write_json(args.output, value)
        grid = value["timeline"]
        print(
            f"PASS: parsed {len(value['rows'])} overview rows and a {len(grid['rows'])}-row, "
            f"{len(grid['weeks'])}-week timeline grid in {len(grid['phases'])} phase(s)"
        )
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
        for line in str(error).splitlines() or [repr(error)]:
            print(f"FAIL: {line}", file=sys.stderr)
        raise SystemExit(1)
