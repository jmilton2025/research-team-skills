#!/usr/bin/env python3
"""Offline regression tests for the Option 4 moderation-guide Google Docs contract.

Run with either:
    python3 skills/mod-guide/tests/test_option4_guide_layout.py
    python3 -m pytest skills/mod-guide/tests/test_option4_guide_layout.py

No Google Docs API call is made. Every test builds a synthetic raw-Docs JSON tree
in Python and exercises the same parse/normalize/format/verify code paths the live
pipeline uses.
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
FIXTURE_PATH = TEST_DIR / "fixtures" / "mock-moderation-guide.md"


def load_module():
    spec = importlib.util.spec_from_file_location("option4_guide_layout", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Synthetic raw-Docs JSON builders (mirror the research-plan test harness).
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


CONVERSION_HEADERS = {
    "parameters": ["Parameter", "Detail"],
    "consent": ["Cue", "Read aloud"],
    "question": ["#", "Ask"],
}


def _table_value_rows(spec: dict) -> list[list[str]]:
    return [[row["label"], row["content"]["text"]] for row in spec["rows"]]


def synthetic_document(module, manifest: dict, *, imported: bool) -> dict:
    """Build a raw one-tab Docs JSON tree.

    imported=True reproduces the just-imported doc: title-case band headings,
    a conversion header row on every table, and native ``---`` rules between
    sections. imported=False reproduces the normalized doc: UPPERCASE bands, no
    conversion headers, no rules.
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
            rows = [CONVERSION_HEADERS[spec["kind"]]] + rows
        item, cursor = table(rows, cursor)
        body.append(item)

    top = manifest["top"]
    add_paragraph(top["breadcrumb"]["text"])
    add_paragraph(top["title"]["text"])
    if top.get("phase_subtitle"):
        add_paragraph(top["phase_subtitle"]["text"])
    add_paragraph(top["date"]["text"])
    for item in top["raci"]:
        add_paragraph(item["text"])
    if top.get("warning"):
        add_paragraph(top["warning"])

    add_table(manifest["parameters"])
    if imported:
        add_rule()

    def add_blocks(blocks: list[dict]) -> None:
        for block in blocks:
            if block["type"] == "prose":
                add_paragraph(block["inline"]["text"])
            elif block["type"] == "list":
                for entry in block["items"]:
                    add_paragraph(entry["text"])
            elif block["type"] == "table":
                add_table(block)
            elif block["type"] == "sub_phase":
                add_paragraph(block["heading"]["text"])
                add_blocks(block["blocks"])

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
    """Build a fully styled normalized doc that the hard verifier must accept."""
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

    top = manifest["top"]
    style_element(
        module.find_paragraph(body, top["breadcrumb"]["text"]), top["breadcrumb"],
        contract["typography"]["breadcrumb"],
        pstyle(line=115, below=spacing["breadcrumb_space_below_pt"], keep=True, named="SUBTITLE"),
        base_bold=True,
    )
    style_element(
        module.find_paragraph(body, top["title"]["text"]), top["title"],
        contract["typography"]["title"],
        pstyle(line=115, below=spacing["title_space_below_pt"], keep=True, named="TITLE"),
        base_bold=True,
    )
    if top.get("phase_subtitle"):
        style_element(
            module.find_paragraph(body, top["phase_subtitle"]["text"]), top["phase_subtitle"],
            contract["typography"]["phase_subtitle"],
            pstyle(line=115, below=spacing["phase_subtitle_space_below_pt"], keep=True),
            base_bold=True,
        )
    style_element(
        module.find_paragraph(body, top["date"]["text"]), top["date"],
        contract["typography"]["context_note"], pstyle(line=115, above=6, below=8),
        base_italic=True,
    )
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
            module.find_paragraph(body, top["warning"]), plain(top["warning"]), warning_style,
            pstyle(line=115, above=6, below=8, keep=True, shading=contract["warning"]["background"]),
            base_bold=True,
        )

    def style_blocks(blocks: list[dict]) -> None:
        for block in blocks:
            if block["type"] == "prose":
                style_element(
                    module.find_paragraph(body, block["inline"]["text"]), block["inline"],
                    contract["typography"]["body"], pstyle(line=115),
                )
            elif block["type"] == "list":
                for entry in block["items"]:
                    style_element(
                        module.find_paragraph(body, entry["text"]), entry, contract["typography"]["body"],
                        pstyle(
                            line=115,
                            indent_start=spacing["list_indent_start_pt"],
                            indent_first=spacing["list_indent_first_line_pt"],
                        ),
                        bullet=True,
                    )
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

    # Tables: backgrounds, padding, widths, and cell text styling per kind.
    tables = module.doc_tables(tab)
    specs = module.manifest_tables(manifest)
    cell_padding = {"magnitude": contract["tables"]["cell_padding_pt"], "unit": "PT"}
    for table_element, spec in zip(tables, specs):
        kind_spec = contract["tables"]["kinds"][spec["kind"]]
        table_element["table"]["tableStyle"] = {
            "tableColumnProperties": [
                {"width": {"magnitude": width, "unit": "PT"}, "widthType": "FIXED_WIDTH"}
                for width in kind_spec["column_widths_pt"]
            ]
        }
        label_bg = kind_spec["label_column_background"]
        content_bg = contract["tables"]["body_cell_background"]
        for row, source in zip(table_element["table"]["tableRows"], spec["rows"]):
            left, right = row["tableCells"]
            left["tableCellStyle"].update(
                {
                    "backgroundColor": module.hex_color(label_bg),
                    "paddingTop": cell_padding, "paddingBottom": cell_padding,
                    "paddingLeft": cell_padding, "paddingRight": cell_padding,
                }
            )
            right["tableCellStyle"].update(
                {
                    "backgroundColor": module.hex_color(content_bg),
                    "paddingTop": cell_padding, "paddingBottom": cell_padding,
                    "paddingLeft": cell_padding, "paddingRight": cell_padding,
                }
            )
            style_element(
                module.cell_paragraphs(left)[0], plain(source["label"]),
                kind_spec["label_column_text"],
                pstyle(line=contract["spacing"]["table_line_spacing_percent"]),
                base_bold=kind_spec["label_column_text"].get("bold", False),
            )
            style_element(
                module.cell_paragraphs(right)[0], source["content"],
                kind_spec["content_column_text"],
                pstyle(line=contract["spacing"]["table_line_spacing_percent"]),
                base_bold=kind_spec["content_column_text"].get("bold", False),
            )
    return doc


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class Option4GuideContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.manifest = cls.module.parse_markdown(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_machine_readable_contract_is_exact(self) -> None:
        contract = json.loads(STYLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(contract["name"], "Option 4 — Leadership (Moderation Guide)")
        self.assertEqual(contract["page"]["document_mode"], "PAGELESS")
        self.assertEqual(contract["page"]["orientation"], "LANDSCAPE")
        self.assertTrue(contract["page"]["use_custom_header_footer_margins"])
        self.assertEqual(contract["page"]["margins_pt"], {"top": 72, "bottom": 72, "left": 72, "right": 72})
        self.assertEqual(contract["colors"]["dark_green"], "#003D29")
        self.assertEqual(contract["colors"]["warning_background"], "#FFF2CC")
        self.assertEqual(contract["structure"]["native_horizontal_rules"], 0)
        self.assertEqual(contract["structure"]["ends_at"], "Post-Session Debrief")
        self.assertEqual(contract["tables"]["kinds"]["parameters"]["column_widths_pt"], [144, 554.4])
        self.assertEqual(contract["tables"]["kinds"]["question"]["column_widths_pt"], [90, 608.4])
        self.assertEqual(contract["tables"]["kinds"]["parameters"]["label_column_background"], "#D9D9D9")
        self.assertEqual(contract["tables"]["kinds"]["consent"]["label_column_background"], "#FFFFFF")

    def test_contract_self_check_passes(self) -> None:
        # load_contract() raises ContractError on any internal geometry inconsistency.
        contract = self.module.load_contract()
        self.assertEqual(contract["tables"]["total_width_pt"], 698.4)

    def test_fixture_parses_into_manifest(self) -> None:
        m = self.manifest
        self.assertEqual(m["contract"], "Option 4 — Leadership (Moderation Guide)")
        self.assertEqual(len(m["sections"]), 7)
        self.assertEqual(len(self.module.manifest_tables(m)), 8)
        self.assertEqual([s["band_label"] for s in m["sections"]][-1], "POST-SESSION DEBRIEF")
        self.assertTrue(m["document_meta"]["is_test_artifact"])
        self.assertTrue(m["document_meta"]["has_phase_subtitle"])
        self.assertTrue(m["document_meta"]["has_stimulus_phase"])
        self.assertEqual(m["document_meta"]["study_type"], "In-Depth Interview (IDI)")
        self.assertEqual(
            m["top"]["warning"],
            "⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. "
            "Do not file or share as real research.",
        )
        # Core phase carries silent-tagging bullets and three sub-phases.
        core = next(s for s in m["sections"] if "CORE" in s["band_label"])
        self.assertEqual(sum(1 for b in core["blocks"] if b["type"] == "sub_phase"), 3)
        self.assertTrue(any(b["type"] == "list" and b["kind"] == "silent_tagging" for b in core["blocks"]))

    def test_manifest_rejects_guide_not_ending_at_debrief(self) -> None:
        source = FIXTURE_PATH.read_text(encoding="utf-8")
        broken = source.replace("## Post-Session Debrief", "## Extra Trailing Section")
        with self.assertRaises(self.module.ContractError):
            self.module.parse_markdown(broken)

    def test_manifest_rejects_forbidden_trailing_section(self) -> None:
        source = FIXTURE_PATH.read_text(encoding="utf-8")
        injected = source + "\n\n## Master Probe Bank\n\nExtra probes.\n"
        with self.assertRaises(self.module.ContractError):
            self.module.parse_markdown(injected)

    def test_pipeline_rejects_stale_or_tampered_manifest(self) -> None:
        stale = json.loads(json.dumps(self.manifest))
        stale["contract_version"] = "1900-01-01"
        with self.assertRaises(self.module.ContractError):
            self.module.build_format_requests(
                synthetic_document(self.module, self.manifest, imported=False), stale
            )
        tampered = json.loads(json.dumps(self.manifest))
        tampered["top"]["title"]["text"] = "Different approved title"
        with self.assertRaises(self.module.ContractError):
            self.module.build_format_requests(
                synthetic_document(self.module, self.manifest, imported=False), tampered
            )

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

    def test_normalizer_uppercases_bands_drops_headers_and_rules(self) -> None:
        doc = synthetic_document(self.module, self.manifest, imported=True)
        payload = self.module.build_normalize_requests(doc, self.manifest)
        request_types = [next(iter(request)) for request in payload["requests"]]
        self.assertIn("deleteTableRow", request_types)      # conversion headers removed
        self.assertIn("deleteContentRange", request_types)  # rules + band text replaced
        self.assertIn("insertText", request_types)          # uppercased band labels
        # One deleteTableRow per table (8) and the band uppercasing covers 7 sections.
        self.assertEqual(request_types.count("deleteTableRow"), 8)

    def test_normalizer_binds_imported_content_to_manifest(self) -> None:
        doc = synthetic_document(self.module, self.manifest, imported=True)
        table = self.module.doc_tables(doc["tabs"][0]["documentTab"])[0]  # parameters
        # Corrupt a content cell (row 1 because row 0 is the conversion header).
        cell = self.module.cell_paragraphs(table["table"]["tableRows"][1]["tableCells"][1])[0]
        cell["paragraph"]["elements"][0]["textRun"]["content"] = "Tampered value\n"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(doc, self.manifest)

    def test_formatter_emits_every_required_operation_family(self) -> None:
        doc = synthetic_document(self.module, self.manifest, imported=False)
        payload = self.module.build_format_requests(doc, self.manifest)
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

        # A section band paragraph must receive dark-green full-paragraph shading.
        shadings = [
            request["updateParagraphStyle"]["paragraphStyle"]["shading"]["backgroundColor"]
            for request in payload["requests"]
            if "updateParagraphStyle" in request
            and "shading" in request["updateParagraphStyle"].get("paragraphStyle", {})
        ]
        self.assertIn(self.module.hex_color("#003D29"), shadings)
        # Numbered debrief list uses the numbered preset.
        presets = [
            request["createParagraphBullets"]["bulletPreset"]
            for request in payload["requests"]
            if "createParagraphBullets" in request
        ]
        self.assertIn(self.module.NUMBERED_PRESET, presets)
        self.assertIn(self.module.BULLET_PRESET, presets)

    def test_hard_verifier_accepts_complete_doc_and_rejects_visual_drift(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        checks = self.module.verify_document(doc, self.manifest)
        self.assertEqual(len(checks), 5)

        # Drift 1: a section band loses its dark-green shading.
        drifted = formatted_document(self.module, self.manifest)
        body = drifted["tabs"][0]["documentTab"]["body"]["content"]
        band = self.module.find_paragraph(body, "PRE-SESSION CHECKLIST")
        band["paragraph"]["paragraphStyle"].pop("shading")
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(drifted, self.manifest)

        # Drift 2: a parameters label cell background turns red.
        drifted2 = formatted_document(self.module, self.manifest)
        param_table = self.module.doc_tables(drifted2["tabs"][0]["documentTab"])[0]
        param_table["table"]["tableRows"][0]["tableCells"][0]["tableCellStyle"]["backgroundColor"] = (
            self.module.hex_color("#FF0000")
        )
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(drifted2, self.manifest)

    def test_verifier_rejects_probe_text_leaking_into_a_table_cell(self) -> None:
        # Guide-specific rule: tables contain ONLY the label and the question text.
        doc = formatted_document(self.module, self.manifest)
        question_table = self.module.doc_tables(doc["tabs"][0]["documentTab"])[2]  # Phase 1 Ask table
        cell = self.module.cell_paragraphs(question_table["table"]["tableRows"][0]["tableCells"][1])[0]
        run = cell["paragraph"]["elements"][0]
        run["textRun"]["content"] = "Probe: echo their last phrase (watch-for note)\n"
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(doc, self.manifest)

    def test_verifier_rejects_debrief_rendered_as_non_list(self) -> None:
        # Lists must be native list paragraphs, not plain paragraphs or a table.
        doc = formatted_document(self.module, self.manifest)
        body = doc["tabs"][0]["documentTab"]["body"]["content"]
        debrief_item = self.module.find_paragraph(
            body, "Planning style: ☐ Written · ☐ Mental · ☐ Improvised · ☐ Mixed"
        )
        debrief_item["paragraph"].pop("bullet")
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(doc, self.manifest)

    def test_verifier_rejects_surviving_horizontal_rule(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        body = doc["tabs"][0]["documentTab"]["body"]["content"]
        last_end = body[-1]["endIndex"]
        rule, _ = horizontal_rule(last_end)
        body.append(rule)
        with self.assertRaises(self.module.ContractError):
            self.module.verify_document(doc, self.manifest)

    def test_layout_tool_exposes_required_pipeline(self) -> None:
        for name in ("parse_markdown", "build_normalize_requests", "build_format_requests", "verify_document"):
            self.assertTrue(callable(getattr(self.module, name, None)), name)


if __name__ == "__main__":
    unittest.main()
