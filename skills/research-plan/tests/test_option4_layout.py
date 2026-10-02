#!/usr/bin/env python3
"""Regression tests for the exact Option 4 Leadership Google Docs contract."""

from __future__ import annotations

from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

TEST_DIR = Path(__file__).resolve().parent
SKILL_DIR = TEST_DIR.parent
STYLE_PATH = SKILL_DIR / "references" / "option4-style-contract.json"
SCRIPT_PATH = SKILL_DIR / "scripts" / "option4_layout.py"
FIXTURE_PATH = TEST_DIR / "fixtures" / "leadership-plan.md"


def load_module():
    spec = importlib.util.spec_from_file_location("option4_layout", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def table(rows: list[list[str]], start: int, *, header: bool = False) -> tuple[dict, int]:
    cursor = start + 1
    table_rows = []
    for row_index, values in enumerate(rows):
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
                "tableRowStyle": {"tableHeader": bool(header and row_index == 0)},
            }
        )
    value = {
        "startIndex": start,
        "endIndex": cursor + 1,
        "table": {
            "tableRows": table_rows,
            "tableStyle": {"tableColumnProperties": []},
        },
    }
    return value, value["endIndex"]


def synthetic_document(manifest: dict, *, conversion_header: bool) -> dict:
    cursor = 1
    body = [{"startIndex": 0, "endIndex": 1, "sectionBreak": {"sectionStyle": {}}}]

    opening = [
        manifest["top"]["breadcrumb"]["text"],
        manifest["top"]["title"]["text"],
        manifest["top"]["updated"]["text"],
        *[item["text"] for item in manifest["top"]["raci"]],
    ]
    if manifest["top"].get("warning"):
        opening.append(manifest["top"]["warning"])
    opening.extend(item["text"] for item in manifest["top"].get("notes", []))
    opening.append("Research Timeline")
    for value in opening:
        item, cursor = paragraph(value, cursor)
        body.append(item)

    timeline_rows = [[cell["text"] for cell in row] for row in manifest["timeline"]]
    timeline, cursor = table(timeline_rows, cursor, header=True)
    body.append(timeline)

    item, cursor = paragraph(manifest["timeline_note"]["text"], cursor)
    body.append(item)
    body.append(
        {
            "startIndex": cursor,
            "endIndex": cursor + 2,
            "paragraph": {
                "elements": [
                    {"startIndex": cursor, "endIndex": cursor + 1, "horizontalRule": {"textStyle": {}}},
                    {
                        "startIndex": cursor + 1,
                        "endIndex": cursor + 2,
                        "textRun": {"content": "\n", "textStyle": {}},
                    },
                ],
                "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
            },
        }
    )
    cursor += 2
    item, cursor = paragraph("Project Plan Overview", cursor)
    body.append(item)

    overview_rows = []
    if conversion_header:
        overview_rows.append(["Section / element", "Approved content"])
    for row in manifest["rows"]:
        overview_rows.append(
            [
                {"Topic": "TOPIC", "TL;DR summary of findings": "TL;DR SUMMARY OF FINDINGS"}.get(
                    row["label"], row["label"]
                ),
                "\n".join(item["text"] for item in row["items"]),
            ]
        )
    overview, cursor = table(overview_rows, cursor)
    body.append(overview)

    return {
        "revisionId": "fixture-revision",
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
    """Create a compact, fully styled raw-Docs fixture for verifier regression tests."""
    doc = synthetic_document(manifest, conversion_header=False)
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
                (
                    value for value in item.get("links", [])
                    if value["start"] <= start and end <= value["end"]
                ),
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

    top = manifest["top"]
    breadcrumb = module.find_paragraph(body, top["breadcrumb"]["text"])
    title = module.find_paragraph(body, top["title"]["text"])
    updated = module.find_paragraph(body, top["updated"]["text"])
    style_element(
        breadcrumb, top["breadcrumb"], contract["typography"]["breadcrumb"],
        pstyle(line=115, below=spacing["breadcrumb_space_below_pt"], keep=True, named="SUBTITLE"),
        base_bold=True,
    )
    style_element(
        title, top["title"], contract["typography"]["title"],
        pstyle(line=115, below=spacing["title_space_below_pt"], keep=True, named="TITLE"),
        base_bold=True,
    )
    style_element(updated, top["updated"], contract["typography"]["body"], pstyle(line=115, above=12, below=12))
    for item in top["raci"]:
        style_element(
            module.find_paragraph(body, item["text"]), item, contract["typography"]["body"],
            pstyle(
                line=115, above=12, below=12,
                indent_start=spacing["raci_indent_start_pt"],
                indent_first=spacing["raci_indent_first_line_pt"],
            ),
            bullet=True,
        )
    if top.get("warning"):
        warning_style = {
            "font": contract["warning"]["font"],
            "size_pt": contract["warning"]["size_pt"],
            "color": contract["warning"]["foreground"],
        }
        style_element(
            module.find_paragraph(body, top["warning"]),
            {"text": top["warning"], "bold": [], "italic": [], "links": []},
            warning_style,
            pstyle(line=115, above=6, below=8, keep=True, shading=contract["warning"]["background"]),
            base_bold=True,
        )
    for item in top.get("notes", []):
        style_element(
            module.find_paragraph(body, item["text"]), item, contract["typography"]["context_note"],
            pstyle(line=115, below=8), base_italic=True,
        )
    for text in ("Research Timeline", "Project Plan Overview"):
        style_element(
            module.find_paragraph(body, text),
            {"text": text, "bold": [], "italic": [], "links": []},
            contract["typography"]["heading"],
            pstyle(
                line=115, above=spacing["heading_space_above_pt"],
                below=spacing["heading_space_below_pt"], keep=True, named="HEADING_1",
            ),
            base_bold=True,
        )
    style_element(
        module.find_paragraph(body, manifest["timeline_note"]["text"]),
        manifest["timeline_note"], contract["typography"]["body"],
        pstyle(line=115), base_italic=True,
    )

    tables = module.doc_tables(tab)
    widths = contract["tables"]["column_widths_pt"]
    cell_padding = {"magnitude": contract["tables"]["cell_padding_pt"], "unit": "PT"}
    for value in tables:
        value["table"]["tableStyle"] = {
            "tableColumnProperties": [
                {"width": {"magnitude": width, "unit": "PT"}, "widthType": "FIXED_WIDTH"}
                for width in widths
            ]
        }
        for row in value["table"]["tableRows"]:
            for cell in row["tableCells"]:
                cell["tableCellStyle"].update(
                    {
                        "paddingTop": cell_padding,
                        "paddingBottom": cell_padding,
                        "paddingLeft": cell_padding,
                        "paddingRight": cell_padding,
                    }
                )

    timeline = tables[0]
    for row_index, (row, source_row) in enumerate(zip(timeline["table"]["tableRows"], manifest["timeline"])):
        row["tableRowStyle"]["tableHeader"] = row_index == 0
        for col_index, (cell, item) in enumerate(zip(row["tableCells"], source_row)):
            color = (
                colors["dark_green"] if row_index == 0
                else colors["gray_cell"] if col_index == 0
                else colors["white"]
            )
            cell["tableCellStyle"]["backgroundColor"] = module.hex_color(color)
            body_style = dict(contract["typography"]["body"])
            if row_index == 0:
                body_style["color"] = colors["white"]
            style_element(
                module.cell_paragraphs(cell)[0], item, body_style,
                pstyle(line=spacing["table_line_spacing_percent"]),
                base_bold=(row_index == 0 or col_index == 0),
            )

    overview = tables[1]
    for row, source in zip(overview["table"]["tableRows"], manifest["rows"]):
        left, right = row["tableCells"]
        background = colors["dark_green"] if source["section"] else colors["white"]
        for cell in row["tableCells"]:
            cell["tableCellStyle"]["backgroundColor"] = module.hex_color(background)
            cell["tableCellStyle"]["columnSpan"] = 1
        if source["section"]:
            style_element(
                module.cell_paragraphs(left)[0],
                {"text": source["label"], "bold": [], "italic": [], "links": []},
                contract["typography"]["section_band"],
                pstyle(line=spacing["table_line_spacing_percent"], named="HEADING_4"),
                base_bold=True,
            )
            module.cell_paragraphs(right)[0]["paragraph"]["paragraphStyle"] = pstyle(
                line=spacing["table_line_spacing_percent"]
            )
            continue
        style_element(
            module.cell_paragraphs(left)[0],
            {
                "text": module.output_label(source["label"]),
                "bold": [], "italic": [], "links": [],
            },
            contract["typography"]["body"], pstyle(line=115), base_bold=True,
        )
        elements = module.cell_paragraphs(right)
        for element, item in zip(elements, source["items"]):
            style_element(
                element, item, contract["typography"]["body"],
                pstyle(
                    line=115,
                    indent_start=(spacing["cell_bullet_indent_start_pt"] if source["bulleted"] else None),
                    indent_first=(spacing["cell_bullet_indent_first_line_pt"] if source["bulleted"] else None),
                ),
                bullet=source["bulleted"],
            )
    return doc


class Option4ContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.manifest = cls.module.parse_markdown(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_machine_readable_contract_is_exact(self) -> None:
        contract = json.loads(STYLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(contract["name"], "Option 4 — Leadership")
        self.assertEqual(contract["page"]["document_mode"], "PAGELESS")
        self.assertEqual(contract["page"]["orientation"], "LANDSCAPE")
        self.assertTrue(contract["page"]["use_custom_header_footer_margins"])
        self.assertEqual(
            contract["page"]["margins_pt"],
            {"top": 72, "bottom": 72, "left": 72, "right": 72},
        )
        self.assertEqual(contract["structure"]["native_horizontal_rules"], 1)
        self.assertEqual(contract["structure"]["top_level_tables"], 2)
        self.assertEqual(contract["colors"]["dark_green"], "#003D29")
        self.assertEqual(contract["colors"]["warning_background"], "#FFF2CC")
        self.assertEqual(
            contract["typography"]["title"],
            {"font": "DM Serif Display", "size_pt": 26, "bold": True, "color": "#003D29"},
        )
        self.assertEqual(
            contract["typography"]["body"],
            {"font": "DM Sans", "size_pt": 10, "color": "#000000"},
        )
        self.assertEqual(contract["tables"]["column_widths_pt"], [144, 554.4])
        self.assertEqual(contract["tables"]["total_width_pt"], 698.4)
        self.assertEqual(contract["tables"]["intentional_text_area_overflow_pt"], 50.4)
        self.assertEqual(contract["tables"]["cell_padding_pt"], 5)
        self.assertEqual(contract["tables"]["timeline_rows"], 5)
        self.assertEqual(contract["tables"]["timeline_header"], ["Timing", "Leadership milestone"])
        self.assertEqual(contract["tables"]["timeline_left_cell_max_characters"], 24)
        self.assertEqual(contract["tables"]["timeline_right_cell_max_characters"], 160)
        self.assertEqual(
            contract["tables"]["overview_section_rows"],
            ["KEY INFORMATION", "PROJECT DETAILS", "DELIVERABLES & NEXT STEPS", "APPENDIX"],
        )

    def test_fixture_parses_into_option4_manifest(self) -> None:
        self.assertEqual(self.manifest["contract"], "Option 4 — Leadership")
        self.assertEqual(len(self.manifest["timeline"]), 5)
        self.assertEqual(
            [cell["text"] for cell in self.manifest["timeline"][0]],
            ["Timing", "Leadership milestone"],
        )
        self.assertEqual(max(len(row[0]["text"]) for row in self.manifest["timeline"][1:]), 24)
        self.assertEqual(len(self.manifest["rows"]), 22)
        self.assertEqual(
            [row["label"] for row in self.manifest["rows"] if row["section"]],
            ["KEY INFORMATION", "PROJECT DETAILS", "DELIVERABLES & NEXT STEPS", "APPENDIX"],
        )
        self.assertTrue(next(row for row in self.manifest["rows"] if row["label"] == "Background")["bulleted"])
        self.assertEqual(
            self.manifest["top"]["warning"],
            "⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.",
        )

    def test_pipeline_rejects_stale_or_tampered_manifest(self) -> None:
        stale = json.loads(json.dumps(self.manifest))
        stale["contract_version"] = "1900-01-01"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(
                synthetic_document(self.manifest, conversion_header=True), stale
            )

        tampered = json.loads(json.dumps(self.manifest))
        tampered["top"]["title"]["text"] = "Different approved title"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(
                synthetic_document(self.manifest, conversion_header=True), tampered
            )

    def test_manifest_rejects_missing_required_row_but_allows_optional_sample_omission(self) -> None:
        source = FIXTURE_PATH.read_text(encoding="utf-8")
        without_background = "\n".join(
            line for line in source.splitlines() if not line.startswith("| **Background** |")
        )
        with self.assertRaises(self.module.ContractError):
            self.module.parse_markdown(without_background)

        without_sample = "\n".join(
            line for line in source.splitlines() if not line.startswith("| **Sample & evaluators** |")
        )
        manifest = self.module.parse_markdown(without_sample)
        self.assertNotIn("Sample & evaluators", [row["label"] for row in manifest["rows"]])

    def test_manifest_rejects_oversized_leadership_label(self) -> None:
        source = FIXTURE_PATH.read_text(encoding="utf-8").replace(
            "Week 1: Setup & rubric",
            "Week 1: Setup, rubric & sample",
            1,
        )
        with self.assertRaisesRegex(self.module.ContractError, "exceeds 24 characters"):
            self.module.parse_markdown(source)

    def test_manifest_rejects_leadership_label_without_timing(self) -> None:
        source = FIXTURE_PATH.read_text(encoding="utf-8").replace(
            "Week 1: Setup & rubric",
            "Before fieldwork",
            1,
        )
        with self.assertRaisesRegex(self.module.ContractError, "must start with its timing"):
            self.module.parse_markdown(source)

    def test_manifest_rejects_noncanonical_timeline_header(self) -> None:
        source = FIXTURE_PATH.read_text(encoding="utf-8").replace(
            "| Timing | Leadership milestone |",
            "| Milestone | Leadership milestone |",
            1,
        )
        with self.assertRaisesRegex(self.module.ContractError, "header must be"):
            self.module.parse_markdown(source)

    def test_inline_parser_decodes_entities_before_ranges_and_balances_url_parentheses(self) -> None:
        item = self.module.parse_inline(
            "A &amp; B with **bold** and [link](https://example.com/a_(b)?x=1&amp;y=2)"
        )
        self.assertEqual(item["text"], "A & B with bold and link")
        bold_start, bold_end = item["bold"][0]
        self.assertEqual(item["text"][bold_start:bold_end], "bold")
        link = item["links"][0]
        self.assertEqual(item["text"][link["start"]:link["end"]], "link")
        self.assertEqual(link["url"], "https://example.com/a_(b)?x=1&y=2")

    def test_inline_parser_keeps_literal_brackets_before_a_real_link(self) -> None:
        item = self.module.parse_inline(
            "“I wish [the page] loaded faster” — from the [example study](https://example.com/study)"
        )
        self.assertEqual(item["text"], "“I wish [the page] loaded faster” — from the example study")
        self.assertEqual(len(item["links"]), 1)
        link = item["links"][0]
        self.assertEqual(item["text"][link["start"]:link["end"]], "example study")
        self.assertEqual(link["url"], "https://example.com/study")

        nested = self.module.parse_inline("See [the [draft] plan](https://example.com/p) today")
        self.assertEqual(nested["text"], "See the [draft] plan today")
        link = nested["links"][0]
        self.assertEqual(nested["text"][link["start"]:link["end"]], "the [draft] plan")

    def test_inline_ranges_use_google_docs_utf16_indices(self) -> None:
        item = self.module.parse_inline("⚠️ Read [source](https://example.com)")
        element = {"startIndex": 10}
        requests = []
        self.module.apply_inline_styles(requests, "t.0", element, item)
        link_request = next(request["updateTextStyle"] for request in requests if "updateTextStyle" in request)
        link = item["links"][0]
        self.assertEqual(
            link_request["range"]["startIndex"],
            10 + self.module.utf16_offset(item["text"], link["start"]),
        )
        self.assertEqual(
            link_request["range"]["endIndex"],
            10 + self.module.utf16_offset(item["text"], link["end"]),
        )

    def test_verifier_rejects_unapproved_extra_emphasis(self) -> None:
        element, _ = paragraph("Plain text", 1)
        element["paragraph"]["elements"][0]["textRun"]["textStyle"] = {"bold": True}
        with self.assertRaises(self.module.ContractError):
            self.module._assert_inline_exact(
                element,
                self.module.parse_inline("Plain text"),
                {"NORMAL_TEXT": {}},
            )

    def test_normalizer_removes_conversion_header_and_rebuilds_cells(self) -> None:
        doc = synthetic_document(self.manifest, conversion_header=True)
        payload = self.module.build_normalize_requests(doc, self.manifest)
        self.assertEqual(
            payload["writeControl"],
            {"requiredRevisionId": "fixture-revision"},
        )
        request_types = [next(iter(request)) for request in payload["requests"]]
        self.assertIn("deleteTableRow", request_types)
        self.assertIn("deleteContentRange", request_types)
        self.assertIn("insertText", request_types)

    def test_mutating_payloads_bind_the_required_revision_id(self) -> None:
        normalize_doc = synthetic_document(self.manifest, conversion_header=True)
        normalize_doc["revisionId"] = "revision-normalize"
        normalize = self.module.build_normalize_requests(
            normalize_doc,
            self.manifest,
            required_revision_id="revision-normalize",
        )
        self.assertEqual(
            normalize["writeControl"],
            {"requiredRevisionId": "revision-normalize"},
        )

        format_doc = synthetic_document(self.manifest, conversion_header=False)
        format_doc["revisionId"] = "revision-format"
        formatted = self.module.build_format_requests(
            format_doc,
            self.manifest,
            required_revision_id="revision-format",
        )
        self.assertEqual(
            formatted["writeControl"],
            {"requiredRevisionId": "revision-format"},
        )

    def test_mutating_payloads_reject_blank_revision_ids(self) -> None:
        normalize_doc = synthetic_document(self.manifest, conversion_header=True)
        with self.assertRaisesRegex(self.module.ContractError, "revision ID"):
            self.module.build_normalize_requests(
                normalize_doc,
                self.manifest,
                required_revision_id="   ",
            )

    def test_mutating_payloads_reject_revision_mismatch_with_input_snapshot(self) -> None:
        normalize_doc = synthetic_document(self.manifest, conversion_header=True)
        normalize_doc["revisionId"] = "snapshot-revision"
        with self.assertRaisesRegex(self.module.ContractError, "does not match"):
            self.module.build_normalize_requests(
                normalize_doc,
                self.manifest,
                required_revision_id="different-revision",
            )

    def test_mutating_payloads_require_a_snapshot_revision_even_with_an_override(self) -> None:
        normalize_doc = synthetic_document(self.manifest, conversion_header=True)
        normalize_doc.pop("revisionId", None)
        for supplied in (None, "unbound-revision"):
            with self.subTest(supplied=supplied):
                with self.assertRaisesRegex(
                    self.module.ContractError,
                    "snapshot revision ID",
                ):
                    self.module.build_normalize_requests(
                        normalize_doc,
                        self.manifest,
                        required_revision_id=supplied,
                    )

    def test_cli_exposes_revision_binding_for_each_mutating_batch(self) -> None:
        for command in ("normalize", "format"):
            with self.subTest(command=command):
                args = self.module.cli().parse_args(
                    [
                        command,
                        "document.json",
                        "manifest.json",
                        "batch.json",
                        "--required-revision-id",
                        "revision-123",
                    ]
                )
                self.assertEqual(args.required_revision_id, "revision-123")

    def test_cli_requires_revision_from_flag_or_fresh_document(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document_path = root / "document.json"
            manifest_path = root / "manifest.json"
            output_path = root / "batch.json"
            document = synthetic_document(self.manifest, conversion_header=True)
            document.pop("revisionId")
            document_path.write_text(json.dumps(document), encoding="utf-8")
            manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")

            with self.assertRaisesRegex(self.module.ContractError, "revision ID"):
                self.module.main(
                    [
                        "normalize",
                        str(document_path),
                        str(manifest_path),
                        str(output_path),
                    ]
                )
            self.assertFalse(output_path.exists())

            document["revisionId"] = "revision-from-document"
            document_path.write_text(json.dumps(document), encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                result = self.module.main(
                    [
                        "normalize",
                        str(document_path),
                        str(manifest_path),
                        str(output_path),
                    ]
                )
            self.assertEqual(result, 0)
            payload = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(
                payload["writeControl"],
                {"requiredRevisionId": "revision-from-document"},
            )

    def test_normalizer_binds_imported_overview_content_to_manifest(self) -> None:
        doc = synthetic_document(self.manifest, conversion_header=True)
        overview = self.module.doc_tables(doc["tabs"][0]["documentTab"])[1]
        labels = [row["label"] for row in self.manifest["rows"]]
        background_row = overview["table"]["tableRows"][labels.index("Background") + 1]
        first = self.module.cell_paragraphs(background_row["tableCells"][1])[0]
        first["paragraph"]["elements"][0]["textRun"]["content"] = "Different content\n"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(doc, self.manifest)

    def test_normalizer_blocks_timeline_rewrites_that_would_stale_table_indices(self) -> None:
        doc = synthetic_document(self.manifest, conversion_header=True)
        timeline = self.module.doc_tables(doc["tabs"][0]["documentTab"])[0]
        first = self.module.cell_paragraphs(timeline["table"]["tableRows"][1]["tableCells"][0])[0]
        first["paragraph"]["elements"][0]["textRun"]["content"] = "Changed before table\n"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(doc, self.manifest)

    def test_normalizer_restores_two_cells_for_section_bands(self) -> None:
        doc = synthetic_document(self.manifest, conversion_header=True)
        body = doc["tabs"][0]["documentTab"]["body"]["content"]
        overview = [element for element in body if "table" in element][1]
        section_row = overview["table"]["tableRows"][3]  # conversion header + Topic + TL;DR + section
        section_row["tableCells"] = section_row["tableCells"][:1]
        section_row["tableCells"][0]["tableCellStyle"]["columnSpan"] = 2
        payload = self.module.build_normalize_requests(doc, self.manifest)
        unmerge = [request for request in payload["requests"] if "unmergeTableCells" in request]
        self.assertEqual(len(unmerge), 1)
        self.assertEqual(unmerge[0]["unmergeTableCells"]["tableRange"]["columnSpan"], 2)

    def test_formatter_emits_every_required_operation_family(self) -> None:
        doc = synthetic_document(self.manifest, conversion_header=False)
        payload = self.module.build_format_requests(doc, self.manifest)
        self.assertEqual(
            payload["writeControl"],
            {"requiredRevisionId": "fixture-revision"},
        )
        request_types = [next(iter(request)) for request in payload["requests"]]
        for operation in (
            "updateDocumentStyle",
            "pinTableHeaderRows",
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
        base_cell_update = next(
            request["updateTableCellStyle"]
            for request in payload["requests"]
            if "updateTableCellStyle" in request
            and "paddingTop" in request["updateTableCellStyle"]["tableCellStyle"]
        )
        self.assertEqual(
            base_cell_update["tableCellStyle"]["paddingTop"],
            {"magnitude": 5, "unit": "PT"},
        )
        link_styles = [
            request["updateTextStyle"]["textStyle"]
            for request in payload["requests"]
            if "updateTextStyle" in request
            and "link" in request["updateTextStyle"].get("textStyle", {})
        ]
        self.assertTrue(link_styles)
        self.assertTrue(all("foregroundColor" in style for style in link_styles))

    def test_hard_verifier_accepts_complete_option4_doc_and_rejects_visual_drift(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        checks = self.module.verify_document(doc, self.manifest)
        self.assertEqual(len(checks), 5)

        drifted = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(drifted["tabs"][0]["documentTab"])[1]
        overview["table"]["tableRows"][0]["tableCells"][0]["tableCellStyle"]["backgroundColor"] = self.module.hex_color("#FF0000")
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(drifted, self.manifest)

    def test_verifier_rejects_later_run_typography_drift_in_timeline(self) -> None:
        def corrupt_second_run(element: dict) -> None:
            run = element["paragraph"]["elements"][0]
            content = run["textRun"]["content"]
            split = max(1, (len(content) - 1) // 2)
            start = run["startIndex"]
            first = json.loads(json.dumps(run))
            second = json.loads(json.dumps(run))
            first["textRun"]["content"] = content[:split]
            first["endIndex"] = start + split
            second["textRun"]["content"] = content[split:]
            second["startIndex"] = start + split
            second["textRun"]["textStyle"]["fontSize"] = {"magnitude": 99, "unit": "PT"}
            element["paragraph"]["elements"] = [first, second]

        note_doc = formatted_document(self.module, self.manifest)
        note_body = note_doc["tabs"][0]["documentTab"]["body"]["content"]
        corrupt_second_run(
            self.module.find_paragraph(note_body, self.manifest["timeline_note"]["text"])
        )
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(note_doc, self.manifest)

        cell_doc = formatted_document(self.module, self.manifest)
        timeline = self.module.doc_tables(cell_doc["tabs"][0]["documentTab"])[0]
        timeline_cell = self.module.cell_paragraphs(
            timeline["table"]["tableRows"][1]["tableCells"][1]
        )[0]
        corrupt_second_run(timeline_cell)
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(cell_doc, self.manifest)

    def test_layout_tool_exposes_required_pipeline(self) -> None:
        for name in (
            "parse_markdown",
            "build_normalize_requests",
            "build_format_requests",
            "verify_document",
        ):
            self.assertTrue(callable(getattr(self.module, name, None)), name)

    def test_write_json_is_atomic_private_and_cleans_up_after_replace_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "payload.json"
            self.module.write_json(output, {"secret": "value"})
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), {"secret": "value"})
            self.assertEqual(os.stat(output).st_mode & 0o777, 0o600)

            output.write_text("original", encoding="utf-8")
            with mock.patch.object(self.module.os, "replace", side_effect=OSError("replace failed")):
                with self.assertRaisesRegex(OSError, "replace failed"):
                    self.module.write_json(output, {"secret": "replacement"})
            self.assertEqual(output.read_text(encoding="utf-8"), "original")
            self.assertEqual([output], list(Path(directory).iterdir()))

    def test_cli_reports_bad_input_without_traceback_or_partial_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            missing = root / "missing-doc.json"
            manifest = root / "manifest.json"
            output = root / "batch.json"
            manifest.write_text(json.dumps(self.manifest), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    "normalize",
                    str(missing),
                    str(manifest),
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse(output.exists())

            malformed = root / "malformed-doc.json"
            malformed.write_text("{not json", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    "normalize",
                    str(malformed),
                    str(manifest),
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse(output.exists())

            wrong_shape = root / "wrong-shape-doc.json"
            wrong_shape.write_text("[]", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_PATH),
                    "normalize",
                    str(wrong_shape),
                    str(manifest),
                    str(output),
                    "--required-revision-id",
                    "revision-123",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL:", result.stderr)
            self.assertIn("JSON root must be an object", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse(output.exists())

    def test_skill_has_no_visual_downgrade_path(self) -> None:
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        rules = (SKILL_DIR / "references" / "content-rules.md").read_text(encoding="utf-8")
        for text in (skill, rules):
            self.assertIn("Option 4 — Leadership", text)
            self.assertIn("DM Serif Display", text)
            self.assertIn("DM Sans", text)
            self.assertIn("Research Timeline", text)
            self.assertIn("Project Plan Overview", text)
            self.assertIn("block completion", text.lower())
        self.assertNotIn("portable Leadership layout", skill)
        self.assertNotIn("portable leadership layout", rules.lower())


if __name__ == "__main__":
    unittest.main()
