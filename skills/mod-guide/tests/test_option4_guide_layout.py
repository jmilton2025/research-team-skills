#!/usr/bin/env python3
"""Offline regression tests for the STRUCTURE-AGNOSTIC Option 4 moderation-guide
Google Docs contract.

Run with either:
    python3 skills/mod-guide/tests/test_option4_guide_layout.py
    python3 -m pytest skills/mod-guide/tests/test_option4_guide_layout.py

No Google Docs API call is made. Every test builds a synthetic raw-Docs JSON tree
in Python and exercises the same parse/normalize/format/verify code paths the live
pipeline uses. Two fixtures are covered — an Interview / IDI guide and a
Prototype / Usability guide — because the formatter must handle both shapes.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

TEST_DIR = Path(__file__).resolve().parent
SKILL_DIR = TEST_DIR.parent
STYLE_PATH = SKILL_DIR / "references" / "option4-guide-style.json"
SCRIPT_PATH = SKILL_DIR / "scripts" / "option4_guide_layout.py"
INTERVIEW_FIXTURE = TEST_DIR / "fixtures" / "mock-interview-guide.md"
PROTOTYPE_FIXTURE = TEST_DIR / "fixtures" / "mock-prototype-guide.md"


def load_module():
    spec = importlib.util.spec_from_file_location("option4_guide_layout", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Synthetic raw-Docs JSON builders.
# ---------------------------------------------------------------------------


def paragraph(text: str, start: int, *, bullet: bool = False) -> tuple[dict, int]:
    content = text + "\n"
    utf16_units = len(content.encode("utf-16-le")) // 2
    value = {
        "startIndex": start,
        "endIndex": start + utf16_units,
        "paragraph": {
            "elements": [
                {
                    "startIndex": start,
                    "endIndex": start + utf16_units,
                    "textRun": {"content": content, "textStyle": {}},
                }
            ],
            "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
        },
    }
    if bullet:
        value["paragraph"]["bullet"] = {"listId": "fixture-list"}
    return value, value["endIndex"]


def horizontal_rule(start: int) -> tuple[dict, int]:
    value = {
        "startIndex": start,
        "endIndex": start + 2,
        "paragraph": {
            "elements": [
                {"startIndex": start, "endIndex": start + 1, "horizontalRule": {"textStyle": {}}},
                {"startIndex": start + 1, "endIndex": start + 2, "textRun": {"content": "\n", "textStyle": {}}},
            ],
            "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
        },
    }
    return value, value["endIndex"]


def table(rows: list[list[str]], start: int) -> tuple[dict, int]:
    cursor = start + 1
    table_rows = []
    for values in rows:
        cells = []
        for value in values:
            content = []
            cell_start = cursor
            for paragraph_value in value.split("\n"):
                item, cursor = paragraph(paragraph_value, cursor)
                content.append(item)
            cells.append(
                {
                    "startIndex": cell_start,
                    "endIndex": content[-1]["endIndex"],
                    "content": content,
                    "tableCellStyle": {"columnSpan": 1, "rowSpan": 1},
                }
            )
        table_rows.append(
            {
                "startIndex": cells[0]["startIndex"],
                "endIndex": cells[-1]["endIndex"],
                "tableCells": cells,
                "tableRowStyle": {"tableHeader": False},
            }
        )
    value = {
        "startIndex": start,
        "endIndex": cursor + 1,
        "table": {"tableRows": table_rows, "tableStyle": {"tableColumnProperties": []}},
    }
    return value, value["endIndex"]


def _table_value_rows(spec: dict) -> list[list[str]]:
    return [[cell["text"] for cell in row["cells"]] for row in spec["rows"]]


def synthetic_document(module, manifest: dict, *, imported: bool) -> dict:
    """Build a raw one-tab Docs JSON tree from a manifest.

    imported=True reproduces the just-imported doc: title-case band headings, a
    conversion header row on every table, and native ``---`` rules. imported=False
    reproduces the normalized doc: UPPERCASE bands, no conversion headers, no rules.
    """
    cursor = 1
    body = [{"startIndex": 0, "endIndex": 1, "sectionBreak": {"sectionStyle": {}}}]

    def add_paragraph(text: str) -> None:
        nonlocal cursor
        item, cursor = paragraph(text, cursor)
        body.append(item)

    def add_rule() -> None:
        nonlocal cursor
        item, cursor = horizontal_rule(cursor)
        body.append(item)

    def add_table(spec: dict) -> None:
        nonlocal cursor
        rows = _table_value_rows(spec)
        if imported:
            rows = [list(spec["header"])] + rows
        item, cursor = table(rows, cursor)
        body.append(item)

    def add_blocks(blocks: list[dict]) -> None:
        for block in blocks:
            if block["type"] == "prose":
                add_paragraph(block["inline"]["text"])
            elif block["type"] == "list":
                for entry in block["items"]:
                    add_paragraph(entry["inline"]["text"])
            elif block["type"] == "table":
                add_table(block)
            elif block["type"] == "sub_phase":
                add_paragraph(block["heading"]["text"])
                add_blocks(block["blocks"])

    top = manifest["top"]
    for pre in top["pre_title"]:
        add_paragraph(pre["text"])
    add_paragraph(top["title"]["text"])
    for item in top["items"]:
        if item.get("type") == "table":
            add_table(item)
            if imported:
                add_rule()
        elif item.get("role") == "raci":
            add_paragraph(item["inline"]["text"])
        elif item.get("role") == "list":
            for entry in item["items"]:
                add_paragraph(entry["inline"]["text"])
        elif item.get("role") == "warning":
            add_paragraph(item["text"])
        else:
            add_paragraph(item["inline"]["text"])

    for section in manifest["sections"]:
        add_paragraph(section["source_label"] if imported else section["band_label"])
        add_blocks(section["blocks"])
        if imported:
            add_rule()

    return {
        "tabs": [
            {
                "tabProperties": {"tabId": "t.0"},
                "documentTab": {
                    "body": {"content": body},
                    "documentStyle": {},
                    "namedStyles": {"styles": []},
                },
            }
        ]
    }


def formatted_document(module, manifest: dict) -> dict:
    """Build a fully styled normalized doc that the visual verifier must accept."""
    doc = synthetic_document(module, manifest, imported=False)
    contract = module.load_contract()
    tab = doc["tabs"][0]["documentTab"]
    body = tab["body"]["content"]
    colors = contract["colors"]
    spacing = contract["spacing"]
    page = contract["page"]

    tab["documentStyle"] = {
        "documentFormat": {"documentMode": page["document_mode"]},
        "pageSize": {
            "width": {"magnitude": page["width_pt"], "unit": "PT"},
            "height": {"magnitude": page["height_pt"], "unit": "PT"},
        },
        **{
            f"margin{name.title()}": {"magnitude": value, "unit": "PT"}
            for name, value in page["margins_pt"].items()
        },
        "marginHeader": {"magnitude": page["header_margin_pt"], "unit": "PT"},
        "marginFooter": {"magnitude": page["footer_margin_pt"], "unit": "PT"},
        "useCustomHeaderFooterMargins": page["use_custom_header_footer_margins"],
    }
    tab["namedStyles"] = {
        "styles": [
            {
                "namedStyleType": "NORMAL_TEXT",
                "textStyle": {
                    "weightedFontFamily": {"fontFamily": "DM Sans", "weight": 400},
                    "fontSize": {"magnitude": 10, "unit": "PT"},
                    "bold": False,
                    "italic": False,
                    "foregroundColor": module.hex_color(colors["black"]),
                },
            }
        ]
    }

    def pstyle(
        *, line: int, above: float = 0, below: float = 0, keep: bool = False,
        named: str = "NORMAL_TEXT", indent_start: float | None = None,
        indent_first: float | None = None, shading: str | None = None,
    ) -> dict:
        value = {
            "namedStyleType": named,
            "lineSpacing": line,
            "spaceAbove": {"magnitude": above, "unit": "PT"},
            "spaceBelow": {"magnitude": below, "unit": "PT"},
            "keepWithNext": keep,
        }
        if indent_start is not None:
            value["indentStart"] = {"magnitude": indent_start, "unit": "PT"}
        if indent_first is not None:
            value["indentFirstLine"] = {"magnitude": indent_first, "unit": "PT"}
        if shading is not None:
            value["shading"] = {"backgroundColor": module.hex_color(shading)}
        return value

    def style_element(
        element: dict, item: dict, style: dict, paragraph_style: dict,
        *, base_bold: bool = False, base_italic: bool = False, bullet: bool = False,
    ) -> None:
        text = item["text"]
        boundaries = {0, len(text)}
        for key in ("bold", "italic"):
            for start, end in item.get(key, []):
                boundaries.update((start, end))
        for link in item.get("links", []):
            boundaries.update((link["start"], link["end"]))
        ordered = sorted(boundaries)
        runs = []
        cursor = element["startIndex"]
        for index, (start, end) in enumerate(zip(ordered, ordered[1:])):
            if end <= start:
                continue
            content = text[start:end]
            if index == len(ordered) - 2:
                content += "\n"
            units = len(content.encode("utf-16-le")) // 2
            bold = base_bold or any(a <= start and end <= b for a, b in item.get("bold", []))
            italic = base_italic or any(a <= start and end <= b for a, b in item.get("italic", []))
            text_style = {
                "weightedFontFamily": {"fontFamily": style["font"], "weight": 400},
                "fontSize": {"magnitude": style["size_pt"], "unit": "PT"},
                "bold": bold,
                "italic": italic,
                "foregroundColor": module.hex_color(style["color"]),
            }
            link = next(
                (v for v in item.get("links", []) if v["start"] <= start and end <= v["end"]),
                None,
            )
            if link:
                text_style["link"] = {"url": link["url"]}
                text_style["underline"] = True
            runs.append(
                {
                    "startIndex": cursor,
                    "endIndex": cursor + units,
                    "textRun": {"content": content, "textStyle": text_style},
                }
            )
            cursor += units
        element["endIndex"] = cursor
        element["paragraph"]["elements"] = runs
        element["paragraph"]["paragraphStyle"] = paragraph_style
        if bullet:
            element["paragraph"]["bullet"] = {"listId": "fixture-list"}
        else:
            element["paragraph"].pop("bullet", None)

    def plain(text: str) -> dict:
        return {"text": text, "bold": [], "italic": [], "links": []}

    step = spacing.get("list_indent_level_step_pt", 18)

    def style_list_items(items: list[dict]) -> None:
        for entry in items:
            level = entry["level"]
            style_element(
                module.find_paragraph(body, entry["inline"]["text"]), entry["inline"],
                contract["typography"]["body"],
                pstyle(
                    line=115,
                    indent_start=spacing["list_indent_start_pt"] + level * step,
                    indent_first=spacing["list_indent_first_line_pt"] + level * step,
                ),
                bullet=True,
            )

    top = manifest["top"]
    for pre in top["pre_title"]:
        style_element(
            module.find_paragraph(body, pre["text"]), pre, contract["typography"]["breadcrumb"],
            pstyle(line=115, below=spacing["breadcrumb_space_below_pt"], keep=True, named="SUBTITLE"),
            base_bold=True,
        )
    style_element(
        module.find_paragraph(body, top["title"]["text"]), top["title"],
        contract["typography"]["title"],
        pstyle(line=115, below=spacing["title_space_below_pt"], keep=True, named="TITLE"),
        base_bold=True,
    )

    for item in top["items"]:
        role = item.get("role")
        if item.get("type") == "table":
            continue
        if role == "raci":
            style_element(
                module.find_paragraph(body, item["inline"]["text"]), item["inline"],
                contract["typography"]["body"],
                pstyle(
                    line=115, above=12, below=12,
                    indent_start=spacing["raci_indent_start_pt"],
                    indent_first=spacing["raci_indent_first_line_pt"],
                ),
                bullet=True,
            )
        elif role == "list":
            style_list_items(item["items"])
        elif role == "warning":
            warning_style = {
                "font": contract["warning"]["font"],
                "size_pt": contract["warning"]["size_pt"],
                "color": contract["warning"]["foreground"],
            }
            style_element(
                module.find_paragraph(body, item["text"]), plain(item["text"]), warning_style,
                pstyle(line=115, above=6, below=8, keep=True, shading=contract["warning"]["background"]),
                base_bold=True,
            )
        elif role == "phase_subtitle":
            style_element(
                module.find_paragraph(body, item["inline"]["text"]), item["inline"],
                contract["typography"]["phase_subtitle"],
                pstyle(line=115, below=spacing["phase_subtitle_space_below_pt"], keep=True),
                base_bold=True,
            )
        elif role == "breadcrumb":
            style_element(
                module.find_paragraph(body, item["inline"]["text"]), item["inline"],
                contract["typography"]["breadcrumb"],
                pstyle(line=115, below=spacing["breadcrumb_space_below_pt"], keep=True),
                base_bold=True,
            )
        elif role == "context_note":
            style_element(
                module.find_paragraph(body, item["inline"]["text"]), item["inline"],
                contract["typography"]["context_note"], pstyle(line=115, above=6, below=8),
                base_italic=True,
            )
        else:  # body
            style_element(
                module.find_paragraph(body, item["inline"]["text"]), item["inline"],
                contract["typography"]["body"], pstyle(line=115),
            )

    def style_blocks(blocks: list[dict]) -> None:
        for block in blocks:
            if block["type"] == "prose":
                style_element(
                    module.find_paragraph(body, block["inline"]["text"]), block["inline"],
                    contract["typography"]["body"], pstyle(line=115),
                )
            elif block["type"] == "list":
                style_list_items(block["items"])
            elif block["type"] == "sub_phase":
                style_element(
                    module.find_paragraph(body, block["heading"]["text"]), block["heading"],
                    contract["typography"]["sub_phase_heading"],
                    pstyle(
                        line=115, above=spacing["sub_phase_space_above_pt"],
                        below=spacing["sub_phase_space_below_pt"], keep=True, named="HEADING_3",
                    ),
                    base_bold=True,
                )
                style_blocks(block["blocks"])

    for section in manifest["sections"]:
        style_element(
            module.find_paragraph(body, section["band_label"]), plain(section["band_label"]),
            contract["typography"]["section_band"],
            pstyle(
                line=115, above=spacing["band_space_above_pt"],
                below=spacing["band_space_below_pt"], keep=True, named="HEADING_2",
                shading=contract["colors"]["dark_green"],
            ),
            base_bold=True,
        )
        style_blocks(section["blocks"])

    # Tables: widths, backgrounds, padding, and per-cell text styling.
    tables = module.doc_tables(tab)
    specs = module.manifest_tables(manifest)
    cell_padding = {"magnitude": contract["tables"]["cell_padding_pt"], "unit": "PT"}
    for table_element, spec in zip(tables, specs):
        widths = module.table_column_widths(contract, spec["ncols"], spec["header"][0])
        table_element["table"]["tableStyle"] = {
            "tableColumnProperties": [
                {"width": {"magnitude": width, "unit": "PT"}, "widthType": "FIXED_WIDTH"}
                for width in widths
            ]
        }
        label_bg = (
            contract["tables"]["top_matter_label_background"]
            if spec.get("gray_label")
            else contract["tables"]["section_label_background"]
        )
        content_bg = contract["tables"]["body_cell_background"]
        for row, source in zip(table_element["table"]["tableRows"], spec["rows"]):
            for col_index, cell in enumerate(row["tableCells"]):
                cell["tableCellStyle"].update(
                    {
                        "backgroundColor": module.hex_color(label_bg if col_index == 0 else content_bg),
                        "paddingTop": cell_padding, "paddingBottom": cell_padding,
                        "paddingLeft": cell_padding, "paddingRight": cell_padding,
                    }
                )
                style = (
                    contract["tables"]["label_column_text"]
                    if col_index == 0
                    else contract["tables"]["content_column_text"]
                )
                style_element(
                    module.cell_paragraphs(cell)[0], source["cells"][col_index], style,
                    pstyle(line=contract["spacing"]["table_line_spacing_percent"]),
                    base_bold=(col_index == 0 and bool(spec.get("first_col_bold"))),
                )
    return doc


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class Option4GuideContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.interview = cls.module.parse_markdown(INTERVIEW_FIXTURE.read_text(encoding="utf-8"))
        cls.prototype = cls.module.parse_markdown(PROTOTYPE_FIXTURE.read_text(encoding="utf-8"))

    # -- Contract ---------------------------------------------------------

    def test_machine_readable_contract_is_exact(self) -> None:
        contract = json.loads(STYLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(contract["name"], "Option 4 — Leadership (Moderation Guide)")
        self.assertTrue(contract["structure_agnostic"])
        self.assertEqual(contract["page"]["document_mode"], "PAGELESS")
        self.assertEqual(contract["page"]["orientation"], "LANDSCAPE")
        self.assertTrue(contract["page"]["use_custom_header_footer_margins"])
        self.assertEqual(contract["page"]["margins_pt"], {"top": 72, "bottom": 72, "left": 72, "right": 72})
        self.assertEqual(contract["colors"]["dark_green"], "#003D29")
        self.assertEqual(contract["colors"]["warning_background"], "#FFF2CC")
        self.assertEqual(contract["structure"]["native_horizontal_rules"], 0)
        # Generic table tokens (no more per-kind fixed widths).
        self.assertEqual(contract["tables"]["total_width_pt"], 698.4)
        self.assertEqual(contract["tables"]["narrow_first_column_pt"], 90)
        self.assertEqual(contract["tables"]["label_first_column_pt"], 144)
        self.assertEqual(contract["tables"]["narrow_first_column_trigger"], "#")
        self.assertEqual(contract["tables"]["top_matter_label_background"], "#D9D9D9")
        self.assertEqual(contract["tables"]["section_label_background"], "#FFFFFF")
        self.assertNotIn("kinds", contract["tables"])

    def test_contract_self_check_passes(self) -> None:
        contract = self.module.load_contract()
        self.assertEqual(contract["tables"]["total_width_pt"], 698.4)

    def test_table_column_widths_are_inferred_generically(self) -> None:
        c = self.module.load_contract()
        # Narrow first column when the first header cell is '#'.
        self.assertEqual(self.module.table_column_widths(c, 2, "#"), [90, 608.4])
        # Label width otherwise, for 2-col and 3-col tables.
        self.assertEqual(self.module.table_column_widths(c, 2, "Parameter"), [144, 554.4])
        self.assertEqual(self.module.table_column_widths(c, 2, "Cue"), [144, 554.4])
        self.assertEqual(self.module.table_column_widths(c, 3, "Date & Time"), [144, 277.2, 277.2])
        # Every distribution still sums to the shared total.
        for widths in (
            self.module.table_column_widths(c, 2, "#"),
            self.module.table_column_widths(c, 3, "Description"),
        ):
            self.assertEqual(round(sum(widths), 1), 698.4)

    # -- Parsing (both shapes) -------------------------------------------

    def test_interview_fixture_parses(self) -> None:
        m = self.interview
        self.assertEqual(m["contract"], "Option 4 — Leadership (Moderation Guide)")
        self.assertEqual(m["top"]["pre_title"][0]["text"], "MOCK EXPERT INTERVIEWS")
        self.assertEqual(m["top"]["title"]["text"], "Discussion Guide")
        roles = [it.get("role") or it.get("type") for it in m["top"]["items"]]
        # Two-tier header: the italic period line is a breadcrumb-level top item.
        self.assertEqual(roles[0], "breadcrumb")
        # Extended RACI: seven ownership rows with varied labels.
        raci_labels = [it["label"] for it in m["top"]["items"] if it.get("role") == "raci"]
        self.assertEqual(
            raci_labels,
            ["Responsible", "Accountable", "Consulted", "Contributor", "External", "Informed", "Session Summaries"],
        )
        self.assertTrue(m["document_meta"]["is_test_artifact"])
        self.assertEqual(m["document_meta"]["study_type"], "1:1 in-depth interview (IDI), blinded")
        self.assertEqual(len(m["sections"]), 10)
        self.assertEqual(len(self.module.manifest_tables(m)), 3)
        # Body is prose bullets with indented probes (a nested list).
        landscape = next(s for s in m["sections"] if s["band_label"] == "CURRENT LANDSCAPE")
        nested = next(b for b in landscape["blocks"] if b["type"] == "list")
        self.assertEqual(max(entry["level"] for entry in nested["items"]), 1)

    def test_prototype_fixture_parses(self) -> None:
        m = self.prototype
        self.assertEqual(m["top"]["pre_title"][0]["text"], "UX Research | Discussion Guide | Round 4 · Q3 2026")
        roles = [it.get("role") for it in m["top"]["items"]]
        self.assertIn("phase_subtitle", roles)
        self.assertIn("context_note", roles)
        self.assertIn("body", roles)  # the "Links:" run-in line
        self.assertFalse(m["document_meta"]["is_test_artifact"])  # no warning in this fixture
        self.assertEqual(len(m["sections"]), 8)
        self.assertEqual(len(self.module.manifest_tables(m)), 7)
        # Prototype tasks live under ### Flow sub-phases with '#|Ask / Do' tables.
        tasks = next(s for s in m["sections"] if s["band_label"] == "PROTOTYPE TASKS")
        subs = [b for b in tasks["blocks"] if b["type"] == "sub_phase"]
        self.assertEqual(len(subs), 2)
        flow_table = next(b for b in subs[0]["blocks"] if b["type"] == "table")
        self.assertEqual(flow_table["header"], ["#", "Ask / Do"])
        # A 3-col Timeline table sits in the vendor back-matter.
        comms = next(s for s in m["sections"] if s["band_label"] == "COMMUNICATION & DELIVERABLES")
        timeline = next(b for b in comms["blocks"] if b["type"] == "table")
        self.assertEqual(timeline["ncols"], 3)

    def test_structure_agnostic_parser_has_no_terminal_or_forbidden_section_gate(self) -> None:
        # The old formatter rejected any guide that did not end at Post-Session
        # Debrief or that carried a "Master Probe Bank" trailing section. Both
        # now parse cleanly — the visual pass no longer owns those content rules.
        source = INTERVIEW_FIXTURE.read_text(encoding="utf-8")
        with_extra = source + "\n\n## Master Probe Bank\n\nExtra probes for later.\n"
        m = self.module.parse_markdown(with_extra)
        self.assertEqual(m["sections"][-1]["band_label"], "MASTER PROBE BANK")
        # A guide that ends on a table (Participants Log) rather than the debrief.
        self.assertEqual(self.interview["sections"][-1]["band_label"], "PARKING LOT — FUTURE QUESTIONS")

    def test_inline_parser_decodes_entities_and_utf16_indices(self) -> None:
        item = self.module.parse_inline(
            "A &amp; B with **bold** and [link](https://example.com/a_(b)?x=1&amp;y=2)"
        )
        self.assertEqual(item["text"], "A & B with bold and link")
        link = item["links"][0]
        self.assertEqual(item["text"][link["start"]:link["end"]], "link")
        self.assertEqual(link["url"], "https://example.com/a_(b)?x=1&y=2")
        emoji = self.module.parse_inline("☐ tag")
        self.assertEqual(self.module.utf16_offset(emoji["text"], 1), 1)

    def test_pipeline_rejects_stale_or_tampered_manifest(self) -> None:
        for manifest in (self.interview, self.prototype):
            stale = json.loads(json.dumps(manifest))
            stale["contract_version"] = "1900-01-01"
            with self.assertRaises(self.module.ContractError):
                self.module.build_format_requests(
                    synthetic_document(self.module, manifest, imported=False), stale
                )
            tampered = json.loads(json.dumps(manifest))
            tampered["top"]["title"]["text"] = "Different approved title"
            with self.assertRaises(self.module.ContractError):
                self.module.build_format_requests(
                    synthetic_document(self.module, manifest, imported=False), tampered
                )

    # -- Normalize (both shapes) -----------------------------------------

    def test_normalizer_uppercases_bands_drops_headers_and_rules(self) -> None:
        for manifest in (self.interview, self.prototype):
            doc = synthetic_document(self.module, manifest, imported=True)
            payload = self.module.build_normalize_requests(doc, manifest)
            request_types = [next(iter(request)) for request in payload["requests"]]
            self.assertIn("deleteTableRow", request_types)      # conversion headers removed
            self.assertIn("deleteContentRange", request_types)  # rules + band text replaced
            self.assertIn("insertText", request_types)          # uppercased band labels
            # One deleteTableRow per table.
            self.assertEqual(request_types.count("deleteTableRow"), len(self.module.manifest_tables(manifest)))

    def test_normalizer_binds_imported_content_to_manifest(self) -> None:
        manifest = self.prototype
        doc = synthetic_document(self.module, manifest, imported=True)
        # Corrupt a 3-col Timeline content cell (row 1 = first content row).
        timeline = self.module.doc_tables(doc["tabs"][0]["documentTab"])[-1]
        cell = self.module.cell_paragraphs(timeline["table"]["tableRows"][1]["tableCells"][2])[0]
        cell["paragraph"]["elements"][0]["textRun"]["content"] = "Tampered date\n"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(doc, manifest)

    # -- Format (both shapes) --------------------------------------------

    def test_formatter_emits_every_required_operation_family(self) -> None:
        for manifest in (self.interview, self.prototype):
            doc = synthetic_document(self.module, manifest, imported=False)
            payload = self.module.build_format_requests(doc, manifest)
            request_types = [next(iter(request)) for request in payload["requests"]]
            for operation in (
                "updateDocumentStyle",
                "updateTableColumnProperties",
                "updateTableCellStyle",
                "createParagraphBullets",
                "updateParagraphStyle",
                "updateTextStyle",
            ):
                self.assertIn(operation, request_types)

            document_style = next(
                request["updateDocumentStyle"]["documentStyle"]
                for request in payload["requests"]
                if "updateDocumentStyle" in request
            )
            self.assertEqual(document_style["documentFormat"]["documentMode"], "PAGELESS")
            self.assertFalse(document_style["flipPageOrientation"])
            self.assertNotIn("useCustomHeaderFooterMargins", document_style)
            self.assertEqual(document_style["pageSize"]["width"]["magnitude"], 792)
            self.assertEqual(document_style["pageSize"]["height"]["magnitude"], 612)

            # Every H2 band gets dark-green full-paragraph shading — one per section.
            shadings = [
                request["updateParagraphStyle"]["paragraphStyle"]["shading"]["backgroundColor"]
                for request in payload["requests"]
                if "updateParagraphStyle" in request
                and "shading" in request["updateParagraphStyle"].get("paragraphStyle", {})
            ]
            self.assertGreaterEqual(
                shadings.count(self.module.hex_color("#003D29")), len(manifest["sections"])
            )

    def test_formatter_uses_both_bullet_and_numbered_presets(self) -> None:
        # The interview fixture has both prose-bullet lists and a numbered debrief.
        doc = synthetic_document(self.module, self.interview, imported=False)
        payload = self.module.build_format_requests(doc, self.interview)
        presets = [
            request["createParagraphBullets"]["bulletPreset"]
            for request in payload["requests"]
            if "createParagraphBullets" in request
        ]
        self.assertIn(self.module.NUMBERED_PRESET, presets)
        self.assertIn(self.module.BULLET_PRESET, presets)

    # -- Verify (both shapes) --------------------------------------------

    def test_verifier_accepts_both_formatted_docs(self) -> None:
        for manifest in (self.interview, self.prototype):
            doc = formatted_document(self.module, manifest)
            checks = self.module.verify_document(doc, manifest)
            self.assertEqual(len(checks), 5)

    def test_verifier_accepts_a_table_after_the_debrief(self) -> None:
        # This is the whole point of the rework: the old verifier rejected any
        # table after Post-Session Debrief. Both fixtures place one there.
        for manifest in (self.interview, self.prototype):
            seq = self.module.expected_sequence(manifest)
            debrief = seq.index("POST-SESSION DEBRIEF")
            self.assertIn("<TABLE>", seq[debrief + 1:], "fixture should have a table after the debrief")
            # And the fully styled doc still verifies clean.
            self.module.verify_document(formatted_document(self.module, manifest), manifest)

    def test_verifier_rejects_visual_drift(self) -> None:
        # A section band that loses its dark-green shading.
        drifted = formatted_document(self.module, self.prototype)
        body = drifted["tabs"][0]["documentTab"]["body"]["content"]
        band = self.module.find_paragraph(body, "WRAP-UP")
        band["paragraph"]["paragraphStyle"].pop("shading")
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(drifted, self.prototype)

        # A parameters label cell background turns red.
        drifted2 = formatted_document(self.module, self.prototype)
        param_table = self.module.doc_tables(drifted2["tabs"][0]["documentTab"])[0]
        param_table["table"]["tableRows"][0]["tableCells"][0]["tableCellStyle"]["backgroundColor"] = (
            self.module.hex_color("#FF0000")
        )
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(drifted2, self.prototype)

    def test_verifier_rejects_wrong_table_column_widths(self) -> None:
        doc = formatted_document(self.module, self.prototype)
        # Break the 3-col Timeline table's widths.
        timeline = self.module.doc_tables(doc["tabs"][0]["documentTab"])[-1]
        timeline["table"]["tableStyle"]["tableColumnProperties"][0]["width"]["magnitude"] = 200
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(doc, self.prototype)

    def test_verifier_rejects_debrief_rendered_as_non_list(self) -> None:
        doc = formatted_document(self.module, self.interview)
        body = doc["tabs"][0]["documentTab"]["body"]["content"]
        debrief_item = self.module.find_paragraph(body, "Top three themes heard, in one line each.")
        debrief_item["paragraph"].pop("bullet")
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(doc, self.interview)

    def test_verifier_rejects_surviving_horizontal_rule(self) -> None:
        doc = formatted_document(self.module, self.prototype)
        body = doc["tabs"][0]["documentTab"]["body"]["content"]
        rule, _ = horizontal_rule(body[-1]["endIndex"])
        body.append(rule)
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(doc, self.prototype)

    def test_layout_tool_exposes_required_pipeline(self) -> None:
        for name in ("parse_markdown", "build_normalize_requests", "build_format_requests", "verify_document"):
            self.assertTrue(callable(getattr(self.module, name, None)), name)


if __name__ == "__main__":
    unittest.main()
