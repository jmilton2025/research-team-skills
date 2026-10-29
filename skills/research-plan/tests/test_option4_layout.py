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
DOCUMENT_ID = "1AbCdEfGhIjKlMnOpQrStUvWxYz0123456789"
FIXTURE_HEADER = "| Phase | Activity | Nov. 2 | Nov. 9 | Nov. 16 | Nov. 23 | Nov. 30 |"
FIXTURE_LEGEND = (
    "*Note: Timing depends on finalized inputs, evaluator capacity, and decision-owner availability; "
    "Green = target dates; Yellow = possible spillover; Red = US holiday week*"
)


def run_script(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), *args], capture_output=True, text=True, check=False
    )


def fake_gws(directory: Path, *, exit_code: int, reply: dict | None) -> tuple[Path, Path]:
    """A stand-in gws that records its arguments, prints a JSON reply, and exits with exit_code."""
    directory.mkdir(parents=True, exist_ok=True)
    argv_log = directory / "argv.json"
    program = directory / "fake_gws.py"
    program.write_text(
        "import json, sys\n"
        f"open({str(argv_log)!r}, 'w', encoding='utf-8').write(json.dumps(sys.argv[1:]))\n"
        f"print({json.dumps(reply) if reply is not None else 'gws: request failed'!r})\n"
        f"sys.exit({exit_code})\n",
        encoding="utf-8",
    )
    launcher = directory / "gws"
    launcher.write_text(f'#!/bin/sh\nexec "{sys.executable}" "{program}" "$@"\n', encoding="utf-8")
    launcher.chmod(0o700)
    return launcher, argv_log


def load_module():
    spec = importlib.util.spec_from_file_location("option4_layout", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixture() -> str:
    return FIXTURE_PATH.read_text(encoding="utf-8")


def grid_markdown(header: list[str], rows: list[list[str]]) -> list[str]:
    """A bare Markdown Gantt table."""
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return lines


def replace_grid(source: str, header: list[str], rows: list[list[str]], legend: str | None = None) -> str:
    """Swap the fixture's Gantt table (and optionally its legend) for another one."""
    lines = source.splitlines()
    start = lines.index(FIXTURE_HEADER)
    end = start
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    lines[start:end] = grid_markdown(header, rows)
    text = "\n".join(lines) + "\n"
    if legend is not None:
        text = text.replace(FIXTURE_LEGEND, legend, 1)
    return text


PLAIN_LEGEND = (
    "*Note: Timing depends on evaluator capacity; Green = target dates; Yellow = possible spillover*"
)


def plain(text: str) -> dict:
    return {"text": text, "bold": [], "italic": [], "links": []}


def utf16_units(text: str) -> int:
    return len(text.encode("utf-16-le")) // 2


class DocBuilder:
    """Lay out raw Google Docs body JSON with consistent indices."""

    def __init__(self, module) -> None:
        self.module = module
        self.cursor = 1
        self.body: list[dict] = [{"startIndex": 0, "endIndex": 1, "sectionBreak": {"sectionStyle": {}}}]

    def paragraph_at(
        self, start: int, item: dict, *, text_style=None, paragraph_style=None, bullet=None, swatch_colors=None,
        base_bold: bool = False, base_italic: bool = False,
    ) -> dict:
        text = item["text"]
        boundaries = {0, len(text)}
        for key in ("bold", "italic"):
            for begin, end in item.get(key, []):
                boundaries.update((begin, end))
        for span in item.get("links", []) + item.get("swatches", []):
            boundaries.update((span["start"], span["end"]))
        ordered = sorted(boundaries)
        pieces = [(begin, end) for begin, end in zip(ordered, ordered[1:]) if end > begin] or [(0, 0)]
        runs = []
        cursor = start
        for index, (begin, end) in enumerate(pieces):
            content = text[begin:end] + ("\n" if index == len(pieces) - 1 else "")
            style: dict = {}
            if text_style is not None:
                style = {
                    "weightedFontFamily": {"fontFamily": text_style["font"], "weight": 400},
                    "fontSize": {"magnitude": text_style["size_pt"], "unit": "PT"},
                    "bold": base_bold or any(a <= begin and end <= b for a, b in item.get("bold", [])),
                    "italic": base_italic or any(a <= begin and end <= b for a, b in item.get("italic", [])),
                    "foregroundColor": self.module.hex_color(text_style["color"]),
                }
                link = next((span for span in item.get("links", []) if span["start"] <= begin and end <= span["end"]), None)
                if link and end > begin:
                    style.update(link={"url": link["url"]}, underline=True,
                                 foregroundColor=self.module.hex_color("#1155CC"))
                swatch = next((span for span in item.get("swatches", []) if span["start"] <= begin and end <= span["end"]), None)
                if swatch and end > begin:
                    style["backgroundColor"] = self.module.hex_color(swatch_colors[swatch["status"]])
            runs.append({
                "startIndex": cursor,
                "endIndex": cursor + utf16_units(content),
                "textRun": {"content": content, "textStyle": style},
            })
            cursor += utf16_units(content)
        value = {
            "startIndex": start,
            "endIndex": cursor,
            "paragraph": {"elements": runs, "paragraphStyle": paragraph_style or {"namedStyleType": "NORMAL_TEXT"}},
        }
        if bullet is not None:
            value["paragraph"]["bullet"] = bullet
        return value

    def paragraph(self, item: dict, **kwargs) -> dict:
        element = self.paragraph_at(self.cursor, item, **kwargs)
        self.cursor = element["endIndex"]
        self.body.append(element)
        return element

    def rule(self, *, paragraph_style=None, mark_style=None) -> dict:
        start = self.cursor
        style = {}
        if mark_style is not None:
            style = {
                "weightedFontFamily": {"fontFamily": mark_style["font"], "weight": 400},
                "fontSize": {"magnitude": mark_style["size_pt"], "unit": "PT"},
            }
        element = {
            "startIndex": start,
            "endIndex": start + 2,
            "paragraph": {
                "elements": [
                    {"startIndex": start, "endIndex": start + 1, "horizontalRule": {"textStyle": {}}},
                    {"startIndex": start + 1, "endIndex": start + 2, "textRun": {"content": "\n", "textStyle": style}},
                ],
                "paragraphStyle": paragraph_style or {"namedStyleType": "NORMAL_TEXT"},
            },
        }
        self.cursor = start + 2
        self.body.append(element)
        return element

    def table(self, rows: list[list[dict]], *, widths=None, row_styles=None) -> dict:
        """Each cell: {"paragraphs": [(item, kwargs)], "style": tableCellStyle}."""
        start = self.cursor
        cursor = start + 1
        table_rows = []
        for row_index, cells in enumerate(rows):
            built = []
            for cell in cells:
                content = []
                cell_start = cursor
                for item, kwargs in cell["paragraphs"]:
                    element = self.paragraph_at(cursor, item, **kwargs)
                    cursor = element["endIndex"]
                    content.append(element)
                built.append({
                    "startIndex": cell_start,
                    "endIndex": cursor,
                    "content": content,
                    "tableCellStyle": dict({"rowSpan": 1, "columnSpan": 1}, **cell.get("style", {})),
                })
            table_rows.append({
                "startIndex": built[0]["startIndex"],
                "endIndex": built[-1]["endIndex"],
                "tableCells": built,
                "tableRowStyle": (row_styles[row_index] if row_styles else {}),
            })
        element = {
            "startIndex": start,
            "endIndex": cursor + 1,
            "table": {
                "rows": len(rows),
                "columns": len(rows[0]),
                "tableRows": table_rows,
                "tableStyle": {"tableColumnProperties": widths or []},
            },
        }
        self.cursor = cursor + 1
        self.body.append(element)
        return element

    def document(self, *, document_style=None, named_styles=None, lists=None) -> dict:
        return {
            "revisionId": "fixture-revision",
            "tabs": [
                {
                    "tabProperties": {"tabId": "t.0"},
                    "documentTab": {
                        "body": {"content": self.body},
                        "documentStyle": document_style or {},
                        "namedStyles": {"styles": named_styles or []},
                        "lists": lists or {},
                    },
                }
            ],
        }


def synthetic_document(module, manifest: dict, *, conversion_header: bool, spacers: int = 0) -> dict:
    """A raw Doc as the Markdown importer leaves it: cell text as typed, no merges, no styling."""
    builder = DocBuilder(module)
    top = manifest["top"]
    for text in (
        top["breadcrumb"]["text"], top["title"]["text"], top["updated"]["text"],
        *[item["text"] for item in top["raci"]],
        *([top["warning"]] if top.get("warning") else []),
        *[item["text"] for item in top.get("notes", [])],
    ):
        builder.paragraph(plain(text))

    def spacer() -> None:
        for _ in range(spacers):
            builder.paragraph(plain(""))

    def cell(text: str) -> dict:
        return {"paragraphs": [(plain(line), {}) for line in text.split("\n")]}

    spacer()
    builder.rule()
    builder.paragraph(plain("Research Timeline"))
    spacer()
    builder.table([[cell(text) for text in row] for row in manifest["timeline"]["source"]])
    builder.paragraph(plain(manifest["timeline_note"]["text"]))
    spacer()
    builder.rule()
    builder.paragraph(plain("Project Plan Overview"))
    spacer()
    overview_rows = [[cell("Section / element"), cell("Approved content")]] if conversion_header else []
    for row in manifest["rows"]:
        overview_rows.append([cell(row["label"]), cell("\n".join(item["text"] for item in row["items"]))])
    builder.table(overview_rows)
    builder.paragraph(plain(""))
    return builder.document()


def list_definition(glyphs: list[str] | None) -> dict:
    levels = []
    for level in range(9):
        definition = {
            "indentStart": {"magnitude": 36 * (level + 1), "unit": "PT"},
            "indentFirstLine": {"magnitude": 36 * (level + 1) - 18, "unit": "PT"},
        }
        if glyphs:
            definition.update(glyphSymbol=glyphs[level % 3], glyphFormat=f"%{level}")
        else:
            definition.update(glyphType="DECIMAL", glyphFormat="".join(f"%{index}." for index in range(level + 1)))
        levels.append(definition)
    return {"listProperties": {"nestingLevels": levels}}


def shifted(item: dict, units: int) -> dict:
    """The same inline item with `units` leading tabs, as normalize leaves a nested list item."""
    def move(pair):
        return [pair[0] + units, pair[1] + units]
    return {
        "text": "\t" * units + item["text"],
        "bold": [move(pair) for pair in item.get("bold", [])],
        "italic": [move(pair) for pair in item.get("italic", [])],
        "links": [dict(link, start=link["start"] + units, end=link["end"] + units) for link in item.get("links", [])],
    }


def formatted_document(module, manifest: dict, *, pre_bullets: bool = False) -> dict:
    """A compact, fully styled raw-Docs fixture for verifier regression tests.

    With pre_bullets, overview list cells look as normalize leaves them: leading tabs and no bullets.
    """
    contract = module.load_contract()
    colors = contract["colors"]
    typography = contract["typography"]
    spacing = contract["spacing"]
    page = contract["page"]
    hexc = module.hex_color
    builder = DocBuilder(module)

    def pstyle(
        *, line: int = 115, above: float = 0, below: float = 0, keep: bool = False,
        named: str = "NORMAL_TEXT", indent_start: float | None = None,
        indent_first: float | None = None, shading: str | None = None,
        together: bool | None = None, alignment: str | None = None,
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
            value["shading"] = {"backgroundColor": hexc(shading)}
        if together is not None:
            value["keepLinesTogether"] = together
        if alignment is not None:
            value["alignment"] = alignment
        return value

    def named_pstyle(name: str) -> dict:
        metrics = contract["named_styles"][name]
        return pstyle(
            line=metrics["line_spacing_percent"], above=metrics["space_above_pt"], below=metrics["space_below_pt"],
            keep=metrics["keep_with_next"], named=name, together=metrics["keep_lines_together"],
        )

    def spacer() -> None:
        builder.paragraph(plain(""), text_style=typography["body"], paragraph_style=pstyle())

    top = manifest["top"]
    builder.paragraph(top["breadcrumb"], text_style=typography["breadcrumb"], paragraph_style=named_pstyle("SUBTITLE"), base_bold=True)
    builder.paragraph(top["title"], text_style=typography["title"], paragraph_style=named_pstyle("TITLE"), base_bold=True)
    builder.paragraph(top["updated"], text_style=typography["body"], paragraph_style=pstyle(above=12, below=12))
    for item in top["raci"]:
        builder.paragraph(
            item, text_style=typography["body"], bullet={"listId": "raci"},
            paragraph_style=pstyle(above=12, below=12, indent_start=spacing["raci_indent_start_pt"],
                                   indent_first=spacing["raci_indent_first_line_pt"]),
        )
    if top.get("warning"):
        warning_style = {"font": contract["warning"]["font"], "size_pt": contract["warning"]["size_pt"],
                         "color": contract["warning"]["foreground"]}
        builder.paragraph(
            plain(top["warning"]), text_style=warning_style, base_bold=True,
            paragraph_style=pstyle(above=6, below=8, keep=True, shading=contract["warning"]["background"]),
        )
    for item in top.get("notes", []):
        builder.paragraph(item, text_style=typography["context_note"], base_italic=True, paragraph_style=pstyle(below=8))

    spacer()
    builder.rule(paragraph_style=pstyle(), mark_style=typography["body"])
    builder.paragraph(plain("Research Timeline"), text_style=typography["heading"], paragraph_style=named_pstyle("HEADING_1"), base_bold=True)
    spacer()

    spec = contract["timeline_table"]
    timeline = manifest["timeline"]
    padding = lambda value: {key: {"magnitude": value, "unit": "PT"} for key in ("paddingTop", "paddingBottom", "paddingLeft", "paddingRight")}
    header_text = spec["header_row"]["text"]
    body_text = typography["body"]
    grid = module.timeline_cell_paragraphs(timeline)
    heads = {phase["start_row"]: phase for phase in timeline["phases"]}
    grid_rows = []
    for row_index, expected_row in enumerate(grid):
        cells = []
        for column, paragraphs in enumerate(expected_row):
            if row_index == 0:
                metrics = spec["header_row"]["week_cells" if column >= 2 else "label_cells"]
                background, text_style, bold = spec["header_row"]["background"], header_text, True
            else:
                metrics = spec["body_rows"]
                source = timeline["rows"][row_index - 1]
                background = (
                    spec["phase_column"]["background"] if column < 2
                    else spec["week_cells"]["statuses"].get(source["cells"][column - 2]["status"], "#FFFFFF")
                )
                text_style, bold = body_text, column == 0
            style = {
                "backgroundColor": hexc(background), **padding(metrics["padding_pt"]),
                "contentAlignment": metrics["content_alignment"],
            }
            if row_index and column == 0 and (row_index - 1) in heads:
                style["rowSpan"] = heads[row_index - 1]["rows"]
            cells.append({
                "style": style,
                "paragraphs": [
                    (plain(text), {"text_style": text_style, "base_bold": bold,
                                   "paragraph_style": pstyle(line=metrics["line_spacing_percent"], alignment=metrics["alignment"])})
                    for text in paragraphs
                ],
            })
        grid_rows.append(cells)
    widths = spec["column_widths_pt"]
    builder.table(
        grid_rows,
        widths=[{"width": {"magnitude": width, "unit": "PT"}, "widthType": "FIXED_WIDTH"}
                for width in [widths["phase"], widths["activity"], *[widths["week"]] * len(timeline["weeks"])]],
        row_styles=[{"minRowHeight": {"unit": "PT"}, "tableHeader": False}]
        + [{"minRowHeight": {"magnitude": spec["body_rows"]["min_row_height_pt"], "unit": "PT"}}] * len(timeline["rows"]),
    )
    builder.paragraph(
        manifest["timeline_note"], text_style=typography["timeline_legend"], base_italic=True,
        paragraph_style=pstyle(), swatch_colors=spec["week_cells"]["statuses"],
    )
    spacer()
    builder.rule(paragraph_style=pstyle(), mark_style=typography["body"])
    builder.paragraph(plain("Project Plan Overview"), text_style=typography["heading"], paragraph_style=named_pstyle("HEADING_1"), base_bold=True)
    spacer()

    overview = contract["overview_table"]
    border = {"color": hexc("#000000"), "width": {"magnitude": 0.75, "unit": "PT"}, "dashStyle": "SOLID"}
    box = {**padding(5), "contentAlignment": "TOP", **{side: border for side in ("borderTop", "borderBottom", "borderLeft", "borderRight")}}
    overview_rows = []
    for source in manifest["rows"]:
        if source["section"]:
            green = dict(box, backgroundColor=hexc(colors["dark_green"]))
            overview_rows.append([
                {"style": dict(green, columnSpan=2), "paragraphs": [(plain(source["label"]), {
                    "text_style": typography["section_band"], "base_bold": True, "paragraph_style": named_pstyle("HEADING_4")})]},
                {"style": green, "paragraphs": [(plain(""), {"paragraph_style": pstyle()})]},
            ])
            continue
        white = dict(box, backgroundColor=hexc(colors["white"]))
        label_style = pstyle(keep=False) if source["label"] in overview["plain_bold_labels"] else named_pstyle("HEADING_5")
        right = []
        for item in source["items"]:
            kwargs = {"text_style": body_text}
            if source["list"] and pre_bullets:
                right.append((shifted(item, item["level"]), dict(kwargs, paragraph_style=pstyle())))
                continue
            if source["list"]:
                indent = 36 * (item["level"] + 1)
                bullet = {"listId": "bullets" if source["list"] == "BULLET" else "numbers"}
                if item["level"]:
                    bullet["nestingLevel"] = item["level"]
                kwargs.update(bullet=bullet, paragraph_style=pstyle(indent_start=indent, indent_first=indent - 18))
            else:
                kwargs["paragraph_style"] = pstyle()
            right.append((item, kwargs))
        overview_rows.append([
            {"style": white, "paragraphs": [(plain(source["label"]), {
                "text_style": typography["label"], "base_bold": True, "paragraph_style": label_style})]},
            {"style": white, "paragraphs": right},
        ])
    builder.table(
        overview_rows,
        widths=[{"width": {"magnitude": width, "unit": "PT"}, "widthType": "FIXED_WIDTH"} for width in overview["column_widths_pt"]],
        row_styles=[{"minRowHeight": {"magnitude": overview["min_row_height_pt"], "unit": "PT"}}] * len(overview_rows),
    )
    builder.paragraph(plain(""))
    return builder.document(
        document_style={
            "documentFormat": {"documentMode": page["document_mode"]},
            "pageSize": {
                "width": {"magnitude": page["width_pt"], "unit": "PT"},
                "height": {"magnitude": page["height_pt"], "unit": "PT"},
            },
            **{f"margin{name.title()}": {"magnitude": value, "unit": "PT"} for name, value in page["margins_pt"].items()},
            "marginHeader": {"magnitude": page["header_margin_pt"], "unit": "PT"},
            "marginFooter": {"magnitude": page["footer_margin_pt"], "unit": "PT"},
            "useCustomHeaderFooterMargins": page["use_custom_header_footer_margins"],
        },
        named_styles=[{
            "namedStyleType": "NORMAL_TEXT",
            "textStyle": {
                "weightedFontFamily": {"fontFamily": "DM Sans", "weight": 400},
                "fontSize": {"magnitude": 10, "unit": "PT"},
                "bold": False, "italic": False, "underline": False, "backgroundColor": {},
                "foregroundColor": hexc(colors["black"]),
            },
        }],
        lists={"raci": list_definition(["●", "○", "■"]), "bullets": list_definition(["●", "○", "■"]),
               "numbers": list_definition(None)},
    )


def tab_of(doc: dict) -> dict:
    return doc["tabs"][0]["documentTab"]


def request_types(payload: dict) -> list[str]:
    return [next(iter(request)) for request in payload["requests"]]


class Option4ContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.manifest = cls.module.parse_markdown(fixture())

    def manifest_for(self, source: str) -> dict:
        return self.module.parse_markdown(source)

    def assert_verify_fails(self, doc: dict, pattern: str, manifest: dict | None = None) -> None:
        with self.assertRaisesRegex(self.module.ContractError, pattern):
            self.module.verify_document(doc, manifest or self.manifest)

    # Contract tokens -------------------------------------------------------------------------

    def test_machine_readable_contract_is_exact(self) -> None:
        contract = json.loads(STYLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(contract["name"], "Option 4 — Leadership")
        self.assertEqual(contract["version"], "2026-10-29")
        self.assertEqual(contract["reference"], "the approved International retailer research plan (Q3 2025)")
        self.assertNotIn("1K7I", STYLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(contract["page"]["document_mode"], "PAGELESS")
        self.assertEqual(contract["page"]["orientation"], "LANDSCAPE")
        self.assertTrue(contract["page"]["use_custom_header_footer_margins"])
        self.assertEqual(contract["page"]["margins_pt"], {"top": 72, "bottom": 72, "left": 72, "right": 72})
        self.assertEqual(contract["structure"]["native_horizontal_rules"], 2)
        self.assertEqual(contract["structure"]["top_level_tables"], 2)
        colors = contract["colors"]
        for key, value in {
            "dark_green": "#003D29", "warning_background": "#FFF2CC", "gray_cell": "#D9D9D9",
            "link_blue": "#1155CC", "status_target": "#D9EAD3", "status_spillover": "#FFF2CC",
            "status_event": "#F4CCCC", "border_black": "#000000",
        }.items():
            self.assertEqual(colors[key], value, key)
        named = contract["named_styles"]
        self.assertEqual(
            {name: (style["font"], style["size_pt"], style["bold"], style["color"], style["space_above_pt"], style["space_below_pt"])
             for name, style in named.items() if name != "NORMAL_TEXT"},
            {
                "TITLE": ("DM Serif Display", 26, True, "#003D29", 0, 3),
                "SUBTITLE": ("DM Serif Display", 16, True, "#666666", 0, 16),
                "HEADING_1": ("DM Serif Display", 20, True, "#000000", 20, 6),
                "HEADING_4": ("DM Serif Display", 14, True, "#003D29", 14, 4),
                "HEADING_5": ("DM Sans", 10, True, "#000000", 0, 0),
            },
        )
        self.assertEqual(contract["typography"]["section_band"]["color"], "#FFFFFF")
        self.assertEqual(contract["typography"]["timeline_legend"], {"font": "DM Sans", "size_pt": 10, "italic": True, "color": "#000000"})
        timeline = contract["timeline_table"]
        self.assertEqual(timeline["header"], ["Phase", "Activity"])
        self.assertEqual(timeline["column_widths_pt"], {"phase": 180, "activity": 72, "week": 54})
        self.assertEqual((timeline["max_week_columns"], timeline["max_total_width_pt"]), (12, 900))
        self.assertEqual(timeline["filler_label"], "…")
        self.assertFalse(timeline["header_row"]["pinned"])
        self.assertEqual(timeline["header_row"]["text"], {"font": "DM Sans", "size_pt": 10, "bold": True, "color": "#FFFFFF"})
        self.assertEqual(
            (timeline["header_row"]["week_cells"]["padding_pt"], timeline["header_row"]["week_cells"]["content_alignment"],
             timeline["header_row"]["week_cells"]["alignment"]),
            (2, "BOTTOM", "END"),
        )
        self.assertEqual(
            (timeline["body_rows"]["min_row_height_pt"], timeline["body_rows"]["padding_pt"], timeline["body_rows"]["line_spacing_percent"]),
            (20, 5, 100),
        )
        self.assertEqual(timeline["week_cells"]["statuses"], {"target": "#D9EAD3", "spillover": "#FFF2CC", "event": "#F4CCCC"})
        overview = contract["overview_table"]
        self.assertEqual(overview["column_widths_pt"], [144, 554.4])
        self.assertEqual((overview["total_width_pt"], overview["intentional_text_area_overflow_pt"]), (698.4, 50.4))
        self.assertEqual(overview["min_row_height_pt"], 25.75)
        self.assertEqual(overview["border"], {"color": "#000000", "width_pt": 0.75, "dash_style": "SOLID"})
        self.assertEqual(overview["section_rows"], ["Key Information", "Project Details", "Deliverables & Next Steps", "Appendix"])
        self.assertEqual(overview["section_band"]["column_span"], 2)
        self.assertEqual(overview["label_named_style"], "HEADING_5")
        self.assertEqual(contract["lists"]["bullet_glyphs"], ["●", "○", "■"])
        self.assertEqual((contract["lists"]["indent_step_pt"], contract["lists"]["first_line_hang_pt"]), (36, 18))
        self.assertEqual(contract["lists"]["number_preset"], "NUMBERED_DECIMAL_NESTED")
        bold = contract["font_metrics"]["dm_sans_bold"]
        regular = contract["font_metrics"]["dm_sans_regular"]
        self.assertEqual(bold["unknown_character_width"], max(bold["advance_widths"].values()))
        self.assertEqual(regular["unknown_character_width"], max(regular["advance_widths"].values()))
        self.assertEqual(set(bold["advance_widths"]), set(regular["advance_widths"]))
        self.assertEqual(
            contract["warning"]["variants"],
            {
                "simulated": "⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.",
                "test_run": "⚠️ TEST RUN — real, authorized inputs, created to test the workflow. Not a stakeholder deliverable.",
            },
        )
        self.module.load_contract()

    # Markdown parsing ------------------------------------------------------------------------

    def test_fixture_parses_into_option4_manifest(self) -> None:
        manifest = self.manifest
        self.assertEqual(manifest["contract"], "Option 4 — Leadership")
        timeline = manifest["timeline"]
        self.assertEqual(timeline["weeks"], ["Nov. 2", "Nov. 9", "Nov. 16", "Nov. 23", "Nov. 30"])
        self.assertEqual(
            [(phase["number"], phase["name"], phase["start_row"], phase["rows"]) for phase in timeline["phases"]],
            [(1, "Setup & calibration", 0, 2), (2, "Validation & decision", 2, 2)],
        )
        self.assertEqual([row["activity"] for row in timeline["rows"]], ["Rubric & sample", "Calibration", "Blind validation", "Readout"])
        self.assertEqual(
            [cell["status"] for cell in timeline["rows"][1]["cells"]],
            [None, "target", "target", "event", "spillover"],
        )
        self.assertEqual(timeline["rows"][1]["cells"][1]["note"], "Human raters")
        self.assertEqual(len(manifest["rows"]), 22)
        self.assertEqual(
            [row["label"] for row in manifest["rows"] if row["section"]],
            ["Key Information", "Project Details", "Deliverables & Next Steps", "Appendix"],
        )
        rows = {row["label"]: row for row in manifest["rows"]}
        self.assertTrue(rows["Background"]["bulleted"])
        self.assertEqual(rows["Background"]["list"], "BULLET")
        self.assertEqual([item["level"] for item in rows["Method & approach"]["items"]], [0, 0, 1, 0])
        self.assertIsNone(rows["What does success look like?"]["list"])
        self.assertEqual(manifest["top"]["warning"], "⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.")
        note = manifest["timeline_note"]
        self.assertEqual(
            [(note["text"][swatch["start"]:swatch["end"]], swatch["status"]) for swatch in note["swatches"]],
            [("Green", "target"), ("Yellow", "spillover"), ("Red", "event")],
        )
        self.assertEqual(set(manifest["skill_files_sha256"]), set(self.module.SKILL_FILES))

    def test_gantt_grid_cells_become_doc_paragraphs(self) -> None:
        grid = self.module.timeline_cell_paragraphs(self.manifest["timeline"])
        self.assertEqual(grid[0], [["Phase"], ["Activity"], ["Nov. 2"], ["Nov. 9"], ["Nov. 16"], ["Nov. 23"], ["Nov. 30"]])
        self.assertEqual(grid[1][0], ["Phase 1:", "Setup & calibration"])
        self.assertEqual(grid[2][0], [""])  # covered by the Phase 1 merge
        self.assertEqual(grid[2][1:4], [["Calibration"], [""], ["Human raters"]])
        self.assertEqual(grid[3][0], ["Phase 2:", "Validation & decision"])
        self.assertEqual(grid[4][-1], ["Decision"])

    def test_gantt_accepts_twelve_weeks_with_a_filler_and_rejects_thirteen(self) -> None:
        weeks = ["Jul. 28", "Aug. 4", "Aug. 11", "Aug. 18", "Aug. 25", "Sep. 1", "Sep. 8", "Sep. 15", "Sep. 22", "Sep. 29", "…", "Dec. 8"]
        rows = [["**Phase 1:** Discovery", "Plan", *["[target]"] + [""] * 11],
                ["", "Readout", *[""] * 10 + ["[spillover]", "[target]"]]]
        source = replace_grid(fixture(), ["Phase", "Activity", *weeks], rows, PLAIN_LEGEND)
        manifest = self.module.parse_markdown(source)
        self.assertEqual(len(manifest["timeline"]["weeks"]), 12)
        contract = self.module.load_contract()
        widths = contract["timeline_table"]["column_widths_pt"]
        self.assertEqual(widths["phase"] + widths["activity"] + 12 * widths["week"], 900)

        thirteen = replace_grid(fixture(), ["Phase", "Activity", *weeks, "Dec. 15"],
                                [row + [""] for row in rows], PLAIN_LEGEND)
        with self.assertRaisesRegex(self.module.ContractError, r"13 week columns.*holds 12.*'…' column"):
            self.module.parse_markdown(thirteen)

        named = [week for week in weeks if week != "…"]
        for bad, pattern in (
            (["…", *named], "can't be the first or last week"),
            ([*named, "…"], "can't be the first or last week"),
            ([*named[:5], "…", *named[5:9], "…", named[9]], "at most one '…' filler column"),
        ):
            with self.subTest(filler=bad):
                with self.assertRaisesRegex(self.module.ContractError, pattern):
                    self.module.parse_markdown(replace_grid(fixture(), ["Phase", "Activity", *bad], rows, PLAIN_LEGEND))

    def test_gantt_rejects_malformed_phases_tokens_and_events(self) -> None:
        header = ["Phase", "Activity", "Week 1", "Week 2"]
        legend = PLAIN_LEGEND
        cases = {
            "first activity row needs a Phase cell": [["", "Plan", "[target]", ""]],
            "Phases are numbered in order": [["Phase 1: Setup", "Plan", "[target]", ""], ["Phase 3: Wrap", "Readout", "", "[target]"]],
            r"must read 'Phase 1: Name'": [["Setup", "Plan", "[target]", ""]],
            r"must be blank or start with \[target\], \[spillover\], or \[event\]": [["Phase 1: Setup", "Plan", "[done]", ""]],
            "needs an activity name": [["Phase 1: Setup", "", "[target]", ""]],
        }
        for pattern, rows in cases.items():
            with self.subTest(pattern=pattern):
                with self.assertRaisesRegex(self.module.ContractError, pattern):
                    self.module.parse_markdown(replace_grid(fixture(), header, rows, legend))
        note_without_status = [["Phase 1: Setup", "Plan", "Internal SMEs", ""]]
        with self.assertRaisesRegex(self.module.ContractError, "must be blank or start with"):
            self.module.parse_markdown(replace_grid(fixture(), header, note_without_status, legend))

        partial_event = [["Phase 1: Setup", "Plan", "[event]", ""], ["", "Readout", "[target]", "[target]"]]
        with self.assertRaisesRegex(self.module.ContractError, r"every row in 'Week 1' must be \[event\]"):
            self.module.parse_markdown(replace_grid(fixture(), header, partial_event, legend + ""))

        with self.assertRaisesRegex(self.module.ContractError, "header must start with 'Phase \\| Activity'"):
            self.module.parse_markdown(fixture().replace("| Phase | Activity |", "| Timing | Leadership milestone |", 1))
        with self.assertRaisesRegex(self.module.ContractError, "row has 6 cells; the header has 7"):
            self.module.parse_markdown(fixture().replace("| [event] | [spillover] |", "| [event] |", 1))

    def test_gantt_measures_every_label_against_its_column(self) -> None:
        header = ["Phase", "Activity", "September 29", "Week 2"]
        rows = [
            ["Phase 1: Stakeholder interviews and synthesis readiness", "Recruit, screen, and schedule participants", "[target] Internal subject-matter experts", ""],
        ]
        with self.assertRaises(self.module.ContractError) as raised:
            self.module.parse_markdown(replace_grid(fixture(), header, rows, PLAIN_LEGEND))
        message = str(raised.exception)
        self.assertIn("week label would wrap; a week column fits 50pt", message)
        self.assertIn("'September 29'", message)
        self.assertIn("phase name would wrap; the Phase column fits 170pt", message)
        self.assertIn("activity name doesn't fit; the Activity column holds 2 lines of 62pt", message)
        self.assertIn("week note doesn't fit; a week cell holds 2 lines of 44pt", message)

        contract = self.module.load_contract()
        bold = contract["font_metrics"]["dm_sans_bold"]
        self.assertAlmostEqual(
            self.module.text_width_pt("Nov. 30", bold),
            sum(bold["advance_widths"][char] for char in "Nov. 30") * 10 / 1000,
        )
        regular = contract["font_metrics"]["dm_sans_regular"]
        self.assertEqual(self.module.wrapped_lines("Internal SMEs", 44, regular), (2, []))
        self.assertEqual(self.module.wrapped_lines("Decision", 44, regular), (1, []))
        lines, too_wide = self.module.wrapped_lines("Subject-matter", 44, regular)
        self.assertEqual(too_wide, ["Subject-matter"])

    def test_legend_swatches_follow_the_grid(self) -> None:
        header = ["Phase", "Activity", "Week 1", "Week 2"]
        rows = [["Phase 1: Setup", "Plan", "[target]", "[spillover]"]]
        manifest = self.module.parse_markdown(replace_grid(fixture(), header, rows, PLAIN_LEGEND))
        self.assertEqual([swatch["status"] for swatch in manifest["timeline_note"]["swatches"]], ["target", "spillover"])

        with self.assertRaisesRegex(self.module.ContractError, "legend names a fixed event, but no week is marked"):
            self.module.parse_markdown(replace_grid(fixture(), header, rows))
        event_rows = [["Phase 1: Setup", "Plan", "[target]", "[event]"]]
        with self.assertRaisesRegex(self.module.ContractError, "must end with '; Red = <fixed event>'"):
            self.module.parse_markdown(replace_grid(fixture(), header, event_rows, PLAIN_LEGEND))
        with self.assertRaisesRegex(self.module.ContractError, "must end with the legend"):
            self.module.parse_markdown(fixture().replace(FIXTURE_LEGEND, "*Timing depends on finalized inputs.*", 1))

    def test_two_rules_are_required_in_markdown(self) -> None:
        source = fixture()
        first = source.replace("\n---\n\n# Research Timeline", "\n# Research Timeline", 1)
        failures = self.module.lint_markdown(first)[0]
        self.assertTrue(any("right before '# Research Timeline'" in failure for failure in failures))
        second = source.replace("\n---\n\n# Project Plan Overview", "\n# Project Plan Overview", 1)
        failures = self.module.lint_markdown(second)[0]
        self.assertTrue(any("right before '# Project Plan Overview'" in failure for failure in failures))

    def test_section_bands_are_title_case(self) -> None:
        with self.assertRaisesRegex(self.module.ContractError, "Title Case now: write 'Key Information'"):
            self.module.parse_markdown(fixture().replace("| **Key Information** |", "| **KEY INFORMATION** |", 1))

    def test_cell_lists_support_nesting_and_numbers(self) -> None:
        kind, items = self.module.split_cell_items("1. **First** step<br>  1. Sub-step<br>    1. Detail<br>2. Second step")
        self.assertEqual(kind, "NUMBER")
        self.assertEqual([(item["text"], item["level"]) for item in items],
                         [("First step", 0), ("Sub-step", 1), ("Detail", 2), ("Second step", 0)])
        self.assertEqual(self.module.split_cell_items("- One<br>&nbsp;&nbsp;- Two")[1][1]["level"], 1)
        self.assertEqual(self.module.split_cell_items("Just a sentence."), (None, [dict(self.module.parse_inline("Just a sentence."), level=0)]))
        with self.assertRaisesRegex(self.module.ContractError, "not both"):
            self.module.split_cell_items("- One<br>1. Two")
        with self.assertRaisesRegex(self.module.ContractError, "more than one level"):
            self.module.split_cell_items("- One<br>    - Too deep")
        with self.assertRaisesRegex(self.module.ContractError, "starts with '- ' or '1. '"):
            self.module.split_cell_items("- One<br>Two")

    def test_pipeline_rejects_stale_or_tampered_manifest(self) -> None:
        stale = json.loads(json.dumps(self.manifest))
        stale["contract_version"] = "1900-01-01"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(synthetic_document(self.module, self.manifest, conversion_header=True), stale)

        tampered = json.loads(json.dumps(self.manifest))
        tampered["top"]["title"]["text"] = "Different approved title"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(synthetic_document(self.module, self.manifest, conversion_header=True), tampered)

    def test_manifest_rejects_missing_required_row_but_allows_optional_sample_omission(self) -> None:
        source = fixture()
        without_background = "\n".join(line for line in source.splitlines() if not line.startswith("| **Background** |"))
        with self.assertRaises(self.module.ContractError):
            self.module.parse_markdown(without_background)

        without_sample = "\n".join(line for line in source.splitlines() if not line.startswith("| **Sample & evaluators** |"))
        manifest = self.module.parse_markdown(without_sample)
        self.assertNotIn("Sample & evaluators", [row["label"] for row in manifest["rows"]])

    def test_manifest_accepts_either_approved_warning_banner_or_none(self) -> None:
        source = fixture()
        simulated = "⚠️ **TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.**"
        test_run = "⚠️ TEST RUN — real, authorized inputs, created to test the workflow. Not a stakeholder deliverable."
        manifest = self.module.parse_markdown(source.replace(simulated, f"**{test_run}**", 1))
        self.assertEqual(manifest["top"]["warning"], test_run)
        doc = formatted_document(self.module, manifest)
        self.assertEqual(len(self.module.verify_document(doc, manifest)), 6)

        real = "\n".join(line for line in source.splitlines() if "TEST ARTIFACT" not in line)
        real_manifest = self.module.parse_markdown(real)
        self.assertIsNone(real_manifest["top"]["warning"])
        self.assertEqual(len(self.module.verify_document(formatted_document(self.module, real_manifest), real_manifest)), 6)

    def test_manifest_rejects_unknown_or_repeated_warning_banner(self) -> None:
        source = fixture()
        banner = "> ⚠️ **TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.**"
        unknown = source.replace(banner, "> ⚠️ **TEST — demo only.**", 1)
        with self.assertRaisesRegex(self.module.ContractError, "Unrecognized warning banner"):
            self.module.parse_markdown(unknown)
        repeated = source.replace(banner, banner + "\n\n" + banner, 1)
        with self.assertRaisesRegex(self.module.ContractError, "one warning banner"):
            self.module.parse_markdown(repeated)

    def test_pipeline_rejects_manifest_built_by_different_skill_files(self) -> None:
        drifted = json.loads(json.dumps(self.manifest))
        drifted["skill_files_sha256"]["scripts/option4_layout.py"] = "0" * 64
        drifted["manifest_sha256"] = self.module.manifest_digest(drifted)
        with self.assertRaisesRegex(self.module.ContractError, "Skill files changed since this manifest"):
            self.module.build_normalize_requests(synthetic_document(self.module, self.manifest, conversion_header=True), drifted)
        changed = {name: "f" * 64 for name in self.module.SKILL_FILES}
        with mock.patch.object(self.module, "skill_files_digest", return_value=changed):
            with self.assertRaisesRegex(self.module.ContractError, "Skill files changed"):
                self.module.verify_document(formatted_document(self.module, self.manifest), self.manifest)

    # lint, timeline, send --------------------------------------------------------------------

    def test_lint_passes_fixture_and_flags_content_rule_gaps(self) -> None:
        source = fixture()
        failures, flags, quotes = self.module.lint_markdown(source)
        self.assertEqual((failures, flags), ([], []))
        self.assertEqual(quotes, ["Existing insights: “Verbatim evidence from the source.”"])

        no_why_now = source.replace("**Why now** —", "**Context** —", 1)
        self.assertTrue(any("Why now" in flag for flag in self.module.lint_markdown(no_why_now)[1]))

        no_fit = source.replace("**Strategic fit:** [TBD — fill in] (the H2 / OKR priority this supports).", "", 1)
        self.assertTrue(any("Strategic fit" in flag for flag in self.module.lint_markdown(no_fit)[1]))

        extra = "".join(f"<br>- **Fact {n}** — Another sourced fact." for n in range(4))
        too_many = source.replace("independent human judgment. |", f"independent human judgment.{extra} |", 1)
        self.assertIn("Background has 7 bullets; the rule is 3–6.", self.module.lint_markdown(too_many)[1])

        unlabeled = source.replace(
            " *(Stakeholder assumption, stated by the decision owner in the product requirements document.)*", "", 1
        )
        self.assertTrue(any("no origin label" in flag for flag in self.module.lint_markdown(unlabeled)[1]))

        hypotheses_row = next(line for line in source.splitlines() if line.startswith("| **Hypotheses** |"))
        empty = source.replace(hypotheses_row, "| **Hypotheses** | No hypotheses confirmed at planning time. |", 1)
        self.assertEqual(self.module.lint_markdown(empty)[1], [])

        short = source.replace("“Verbatim evidence from the source.”", "“two words”", 1)
        self.assertEqual(self.module.lint_markdown(short)[2], [])

        quoted_note = source.replace("[target] Human raters", "[target] “Human raters agree here”", 1)
        self.assertIn("Research Timeline: “Human raters agree here”", self.module.lint_markdown(quoted_note)[2])

    def test_lint_cli_exits_nonzero_only_for_layout_failures(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            plan = Path(directory) / "APPROVED.md"
            plan.write_text(fixture(), encoding="utf-8")
            result = run_script("lint", str(plan))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("CONFIRM QUOTE: Existing insights: “Verbatim evidence from the source.”", result.stdout)

            plan.write_text(fixture().replace("| Nov. 30 |", "| November 30 |", 1), encoding="utf-8")
            result = run_script("lint", str(plan))
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL: Timeline week label would wrap", result.stdout)
            self.assertIn("CONFIRM QUOTE:", result.stdout)
            self.assertNotIn("Traceback", result.stderr)

    def test_timeline_cli_checks_a_bare_draft_table(self) -> None:
        lines = fixture().splitlines()
        start = lines.index(FIXTURE_HEADER)
        draft = "\n".join(lines[start:start + 6]) + "\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "TIMELINE.md"
            path.write_text(draft, encoding="utf-8")
            result = run_script("timeline", str(path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.count("OK   week"), 5)
            self.assertIn("OK   Phase 1: Setup & calibration", result.stdout)
            self.assertIn("(2 rows, merged)", result.stdout)
            self.assertIn("OK   note 'Human raters' (Calibration, Nov. 9)", result.stdout)
            self.assertIn("PASS: the 4-row, 5-week grid is well formed and every label fits its column", result.stdout)

            path.write_text(draft.replace("| Nov. 30 |", "| November 30 |"), encoding="utf-8")
            result = run_script("timeline", str(path))
            self.assertEqual(result.returncode, 1)
            self.assertIn("WRAP week 'November 30'", result.stdout)
            self.assertIn("FAIL: Timeline week label would wrap", result.stdout)

            path.write_text(draft.replace("[target] Human raters", "[done]"), encoding="utf-8")
            result = run_script("timeline", str(path))
            self.assertEqual(result.returncode, 1)
            self.assertIn("must be blank or start with [target]", result.stdout)

            path.write_text(draft.replace("| Phase | Activity |", "| When | Activity |"), encoding="utf-8")
            result = run_script("timeline", str(path))
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL: Research Timeline header must start with 'Phase | Activity'", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_send_passes_the_body_as_one_argument_and_saves_the_reply_privately(self) -> None:
        batch = {
            "requests": [{"insertText": {"location": {"index": 1}, "text": "approved text"}}],
            "writeControl": {"requiredRevisionId": "rev-1"},
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            gws, argv_log = fake_gws(root, exit_code=0, reply={"writeControl": {"requiredRevisionId": "rev-2"}})
            batch_path = root / "batch.json"
            batch_path.write_text(json.dumps(batch), encoding="utf-8")
            response = root / "response.json"
            result = run_script(
                "send", str(batch_path), "--document-id", DOCUMENT_ID, "--response", str(response), "--gws", str(gws)
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("new revision rev-2", result.stdout)
            self.assertNotIn("approved text", result.stdout + result.stderr)
            argv = json.loads(argv_log.read_text(encoding="utf-8"))
            self.assertEqual(argv[:4], ["docs", "documents", "batchUpdate", "--params"])
            self.assertEqual(json.loads(argv[4]), {"documentId": DOCUMENT_ID})
            self.assertEqual(argv[5], "--json")
            self.assertEqual(json.loads(argv[6]), batch)
            self.assertEqual(len(argv), 7)
            self.assertEqual(os.stat(response).st_mode & 0o777, 0o600)
            self.assertEqual(json.loads(response.read_text(encoding="utf-8"))["returncode"], 0)

    def test_send_refuses_unbound_batches_and_reports_gws_failure_without_resending(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            response = root / "response.json"
            unbound = root / "unbound.json"
            unbound.write_text(json.dumps({"requests": [{"insertText": {}}]}), encoding="utf-8")
            gws, argv_log = fake_gws(root, exit_code=0, reply={})
            result = run_script(
                "send", str(unbound), "--document-id", DOCUMENT_ID, "--response", str(response), "--gws", str(gws)
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("not bound to a revision", result.stderr)
            self.assertFalse(argv_log.exists())

            bound = root / "bound.json"
            bound.write_text(
                json.dumps({"requests": [{"insertText": {}}], "writeControl": {"requiredRevisionId": "rev-1"}}),
                encoding="utf-8",
            )
            result = run_script(
                "send", str(bound), "--document-id", "not a doc id", "--response", str(response), "--gws", str(gws)
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("--document-id", result.stderr)

            failing, _ = fake_gws(root / "failing", exit_code=3, reply=None)
            result = run_script(
                "send", str(bound), "--document-id", DOCUMENT_ID, "--response", str(response), "--gws", str(failing)
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("gws batchUpdate failed (exit 3)", result.stderr)
            self.assertIn("do not resend", result.stderr)
            self.assertNotIn("PASS", result.stdout)
            self.assertEqual(json.loads(response.read_text(encoding="utf-8"))["returncode"], 3)
            self.assertNotIn("Traceback", result.stderr)

    # Inline parsing --------------------------------------------------------------------------

    def test_inline_parser_decodes_entities_before_ranges_and_balances_url_parentheses(self) -> None:
        item = self.module.parse_inline("A &amp; B with **bold** and [link](https://example.com/a_(b)?x=1&amp;y=2)")
        self.assertEqual(item["text"], "A & B with bold and link")
        bold_start, bold_end = item["bold"][0]
        self.assertEqual(item["text"][bold_start:bold_end], "bold")
        link = item["links"][0]
        self.assertEqual(item["text"][link["start"]:link["end"]], "link")
        self.assertEqual(link["url"], "https://example.com/a_(b)?x=1&y=2")

    def test_inline_parser_keeps_literal_brackets_before_a_real_link(self) -> None:
        item = self.module.parse_inline("“I wish [the page] loaded faster” — from the [example study](https://example.com/study)")
        self.assertEqual(item["text"], "“I wish [the page] loaded faster” — from the example study")
        self.assertEqual(len(item["links"]), 1)
        link = item["links"][0]
        self.assertEqual(item["text"][link["start"]:link["end"]], "example study")
        self.assertEqual(link["url"], "https://example.com/study")
        nested = self.module.parse_inline("See [the [draft] plan](https://example.com/p) today")
        self.assertEqual(nested["text"], "See the [draft] plan today")
        link = nested["links"][0]
        self.assertEqual(nested["text"][link["start"]:link["end"]], "the [draft] plan")
        self.assertEqual(self.module.parse_inline("[target] Human raters")["text"], "[target] Human raters")

    def test_inline_ranges_use_google_docs_utf16_indices(self) -> None:
        item = self.module.parse_inline("⚠️ Read [source](https://example.com)")
        element = {"startIndex": 10}
        requests = []
        self.module.apply_inline_styles(requests, "t.0", element, item)
        link_request = next(request["updateTextStyle"] for request in requests if "updateTextStyle" in request)
        link = item["links"][0]
        self.assertEqual(link_request["range"]["startIndex"], 10 + self.module.utf16_offset(item["text"], link["start"]))
        self.assertEqual(link_request["range"]["endIndex"], 10 + self.module.utf16_offset(item["text"], link["end"]))

    def test_verifier_rejects_unapproved_extra_emphasis(self) -> None:
        builder = DocBuilder(self.module)
        element = builder.paragraph(plain("Plain text"))
        element["paragraph"]["elements"][0]["textRun"]["textStyle"] = {"bold": True}
        with self.assertRaises(self.module.ContractError):
            self.module._assert_inline_exact(element, self.module.parse_inline("Plain text"), {"NORMAL_TEXT": {}})

    # normalize --------------------------------------------------------------------------------

    def test_normalizer_removes_conversion_header_and_rebuilds_cells(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        payload = self.module.build_normalize_requests(doc, self.manifest)
        self.assertEqual(payload["writeControl"], {"requiredRevisionId": "fixture-revision"})
        types = request_types(payload)
        for operation in ("deleteTableRow", "deleteContentRange", "insertText", "mergeTableCells"):
            self.assertIn(operation, types)
        self.assertNotIn("unmergeTableCells", types)
        inserted = [request["insertText"]["text"] for request in payload["requests"] if "insertText" in request]
        self.assertIn("Phase 1:\nSetup & calibration", inserted)
        self.assertIn("Human raters", inserted)
        self.assertFalse(any("[target]" in text or "[event]" in text for text in inserted))
        self.assertIn("Calibrate the rubric with an initial human-review round.\nDiagnose disagreements and refine only "
                      "evidence-supported gaps.\n\tSend every split decision to adjudication before refining.\nRun a "
                      "separate blind validation before the adoption decision.", inserted)

    def test_normalizer_merges_section_bands_and_phase_cells(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        timeline_table, overview_table = self.module.doc_tables(tab_of(doc))
        payload = self.module.build_normalize_requests(doc, self.manifest)
        merges = [request["mergeTableCells"]["tableRange"] for request in payload["requests"] if "mergeTableCells" in request]
        band_merges = [merge for merge in merges if merge["tableCellLocation"]["tableStartLocation"]["index"] == overview_table["startIndex"]]
        labels = [row["label"] for row in self.manifest["rows"]]
        self.assertEqual(
            sorted(merge["tableCellLocation"]["rowIndex"] for merge in band_merges),
            [labels.index(section) for section in self.module.SECTIONS],
        )
        self.assertTrue(all((merge["rowSpan"], merge["columnSpan"]) == (1, 2) for merge in band_merges))
        phase_merges = [merge for merge in merges if merge["tableCellLocation"]["tableStartLocation"]["index"] == timeline_table["startIndex"]]
        self.assertEqual(
            [(merge["tableCellLocation"]["rowIndex"], merge["tableCellLocation"]["columnIndex"], merge["rowSpan"], merge["columnSpan"])
             for merge in phase_merges],
            [(1, 0, 2, 1), (3, 0, 2, 1)],
        )

    def test_normalizer_inserts_missing_spacers_and_removes_extras(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        tab = tab_of(doc)
        blocks = self.module.top_level_blocks(tab)
        rules = [block["element"] for block in blocks if block["kind"] == "rule"]
        headings = [block["element"] for block in blocks if block["text"] in ("Research Timeline", "Project Plan Overview")]
        payload = self.module.build_normalize_requests(doc, self.manifest)
        spacer_inserts = sorted(
            request["insertText"]["location"]["index"] for request in payload["requests"]
            if "insertText" in request and request["insertText"]["text"] == "\n"
        )
        self.assertEqual(
            spacer_inserts,
            sorted([rule["startIndex"] for rule in rules] + [heading["endIndex"] - 1 for heading in headings]),
        )

        tidy = synthetic_document(self.module, self.manifest, conversion_header=True, spacers=1)
        payload = self.module.build_normalize_requests(tidy, self.manifest)
        self.assertFalse(any("insertText" in request and request["insertText"]["text"] == "\n" for request in payload["requests"]))

        crowded = synthetic_document(self.module, self.manifest, conversion_header=True, spacers=2)
        empties = [block["element"] for block in self.module.top_level_blocks(tab_of(crowded)) if block["kind"] == "empty"]
        payload = self.module.build_normalize_requests(crowded, self.manifest)
        deleted = {
            request["deleteContentRange"]["range"]["startIndex"] for request in payload["requests"] if "deleteContentRange" in request
        }
        # Four gaps hold two spacers each; the first of each pair goes.
        self.assertTrue({empties[index]["startIndex"] for index in (0, 2, 4, 6)} <= deleted)
        self.assertFalse({empties[index]["startIndex"] for index in (1, 3, 5, 7)} & deleted)

    def test_normalizer_orders_writes_from_the_end_of_the_document(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        timeline_table, overview_table = self.module.doc_tables(tab_of(doc))
        payload = self.module.build_normalize_requests(doc, self.manifest)

        def position(request: dict) -> int:
            body = next(iter(request.values()))
            if "range" in body:
                return body["range"]["startIndex"]
            if "location" in body:
                return body["location"]["index"]
            location = body.get("tableCellLocation") or body["tableRange"]["tableCellLocation"]
            return location["tableStartLocation"]["index"]

        positions = [position(request) for request in payload["requests"]]
        # Every write lands at or before the writes that preceded it, so no snapshot index goes stale.
        overview_done = max(index for index, value in enumerate(positions) if value >= overview_table["startIndex"])
        self.assertTrue(all(value < overview_table["startIndex"] for value in positions[overview_done + 1:]))
        timeline_done = max(index for index, value in enumerate(positions) if value >= timeline_table["startIndex"])
        self.assertTrue(all(value < timeline_table["startIndex"] for value in positions[timeline_done + 1:]))

    def test_mutating_payloads_bind_the_required_revision_id(self) -> None:
        normalize_doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        normalize_doc["revisionId"] = "revision-normalize"
        normalize = self.module.build_normalize_requests(normalize_doc, self.manifest, required_revision_id="revision-normalize")
        self.assertEqual(normalize["writeControl"], {"requiredRevisionId": "revision-normalize"})

        format_doc = formatted_document(self.module, self.manifest)
        format_doc["revisionId"] = "revision-format"
        formatted = self.module.build_format_requests(format_doc, self.manifest, required_revision_id="revision-format")
        self.assertEqual(formatted["writeControl"], {"requiredRevisionId": "revision-format"})

    def test_mutating_payloads_reject_blank_revision_ids(self) -> None:
        normalize_doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        with self.assertRaisesRegex(self.module.ContractError, "revision ID"):
            self.module.build_normalize_requests(normalize_doc, self.manifest, required_revision_id="   ")

    def test_mutating_payloads_reject_revision_mismatch_with_input_snapshot(self) -> None:
        normalize_doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        normalize_doc["revisionId"] = "snapshot-revision"
        with self.assertRaisesRegex(self.module.ContractError, "does not match"):
            self.module.build_normalize_requests(normalize_doc, self.manifest, required_revision_id="different-revision")

    def test_mutating_payloads_require_a_snapshot_revision_even_with_an_override(self) -> None:
        normalize_doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        normalize_doc.pop("revisionId", None)
        for supplied in (None, "unbound-revision"):
            with self.subTest(supplied=supplied):
                with self.assertRaisesRegex(self.module.ContractError, "snapshot revision ID"):
                    self.module.build_normalize_requests(normalize_doc, self.manifest, required_revision_id=supplied)

    def test_cli_exposes_revision_binding_for_each_mutating_batch(self) -> None:
        for command in ("normalize", "format"):
            with self.subTest(command=command):
                args = self.module.cli().parse_args(
                    [command, "document.json", "manifest.json", "batch.json", "--required-revision-id", "revision-123"]
                )
                self.assertEqual(args.required_revision_id, "revision-123")

    def test_cli_requires_revision_from_flag_or_fresh_document(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document_path = root / "document.json"
            manifest_path = root / "manifest.json"
            output_path = root / "batch.json"
            document = synthetic_document(self.module, self.manifest, conversion_header=True)
            document.pop("revisionId")
            document_path.write_text(json.dumps(document), encoding="utf-8")
            manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")

            with self.assertRaisesRegex(self.module.ContractError, "revision ID"):
                self.module.main(["normalize", str(document_path), str(manifest_path), str(output_path)])
            self.assertFalse(output_path.exists())

            document["revisionId"] = "revision-from-document"
            document_path.write_text(json.dumps(document), encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                result = self.module.main(["normalize", str(document_path), str(manifest_path), str(output_path)])
            self.assertEqual(result, 0)
            payload = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["writeControl"], {"requiredRevisionId": "revision-from-document"})

    def test_cli_runs_normalize_format_and_verify_on_synthetic_docs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plan = root / "APPROVED.md"
            plan.write_text(fixture(), encoding="utf-8")
            manifest_path = root / "manifest.json"
            result = run_script("manifest", str(plan), str(manifest_path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PASS: parsed 22 overview rows and a 4-row, 5-week timeline grid in 2 phase(s)", result.stdout)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for name, doc, command in (
                ("imported", synthetic_document(self.module, manifest, conversion_header=True), "normalize"),
                ("normalized", formatted_document(self.module, manifest), "format"),
            ):
                path = root / f"{name}.json"
                path.write_text(json.dumps(doc), encoding="utf-8")
                result = run_script(command, str(path), str(manifest_path), str(root / f"{command}-batch.json"))
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(result.stdout.startswith("PASS: generated"))
            final = root / "final.json"
            final.write_text(json.dumps(formatted_document(self.module, manifest)), encoding="utf-8")
            result = run_script("verify", str(final), str(manifest_path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.count("PASS:"), 6)

    def test_normalizer_binds_imported_overview_content_to_manifest(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        overview = self.module.doc_tables(tab_of(doc))[1]
        labels = [row["label"] for row in self.manifest["rows"]]
        background_row = overview["table"]["tableRows"][labels.index("Background") + 1]
        first = self.module.cell_paragraphs(background_row["tableCells"][1])[0]
        first["paragraph"]["elements"][0]["textRun"]["content"] = "Different content\n"
        with self.assertRaises(self.module.ContractError):
            self.module.build_normalize_requests(doc, self.manifest)

    def test_normalizer_binds_imported_timeline_grid_to_manifest(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        timeline = self.module.doc_tables(tab_of(doc))[0]
        cell = self.module.cell_paragraphs(timeline["table"]["tableRows"][2]["tableCells"][3])[0]
        cell["paragraph"]["elements"][0]["textRun"]["content"] = "[target] Other raters\n"
        with self.assertRaisesRegex(self.module.ContractError, "timeline grid text differs.*row 2, column 3"):
            self.module.build_normalize_requests(doc, self.manifest)

    def test_normalizer_blocks_a_doc_missing_a_rule(self) -> None:
        doc = synthetic_document(self.module, self.manifest, conversion_header=True)
        body = tab_of(doc)["body"]["content"]
        rule = next(element for element in body if "paragraph" in element and any("horizontalRule" in child for child in element["paragraph"]["elements"]))
        body.remove(rule)
        with self.assertRaisesRegex(self.module.ContractError, "hierarchy does not match.*expected '<rule>'"):
            self.module.build_normalize_requests(doc, self.manifest)

    # format -----------------------------------------------------------------------------------

    def test_formatter_emits_every_required_operation_family(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        payload = self.module.build_format_requests(doc, self.manifest)
        self.assertEqual(payload["writeControl"], {"requiredRevisionId": "fixture-revision"})
        types = request_types(payload)
        for operation in (
            "updateDocumentStyle", "pinTableHeaderRows", "updateTableColumnProperties", "updateTableCellStyle",
            "updateTableRowStyle", "createParagraphBullets", "updateParagraphStyle", "updateTextStyle",
        ):
            self.assertIn(operation, types)
        document_style = next(request["updateDocumentStyle"]["documentStyle"] for request in payload["requests"] if "updateDocumentStyle" in request)
        self.assertEqual(document_style["documentFormat"]["documentMode"], "PAGELESS")
        self.assertFalse(document_style["flipPageOrientation"])
        self.assertNotIn("useCustomHeaderFooterMargins", document_style)
        self.assertEqual((document_style["pageSize"]["width"]["magnitude"], document_style["pageSize"]["height"]["magnitude"]), (792, 612))
        self.assertTrue(all(request["pinTableHeaderRows"]["pinnedHeaderRowsCount"] == 0 for request in payload["requests"] if "pinTableHeaderRows" in request))
        widths = [request["updateTableColumnProperties"]["tableColumnProperties"]["width"]["magnitude"]
                  for request in payload["requests"] if "updateTableColumnProperties" in request]
        self.assertEqual(widths, [180, 72, 54, 54, 54, 54, 54, 144, 554.4])
        link_styles = [request["updateTextStyle"]["textStyle"] for request in payload["requests"]
                       if "updateTextStyle" in request and "link" in request["updateTextStyle"]["textStyle"]]
        self.assertTrue(link_styles)
        blue = self.module.hex_color("#1155CC")
        self.assertTrue(all(style["foregroundColor"] == blue and style["underline"] for style in link_styles))
        named = {request["updateParagraphStyle"]["paragraphStyle"].get("namedStyleType") for request in payload["requests"] if "updateParagraphStyle" in request}
        self.assertTrue({"SUBTITLE", "TITLE", "HEADING_1", "HEADING_4", "HEADING_5", "NORMAL_TEXT"} <= named)

    def test_formatter_fills_status_cells_and_styles_the_grid_header(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        timeline_table = self.module.doc_tables(tab_of(doc))[0]
        payload = self.module.build_format_requests(doc, self.manifest)
        cell_updates = [request["updateTableCellStyle"] for request in payload["requests"]
                        if "updateTableCellStyle" in request
                        and request["updateTableCellStyle"]["tableRange"]["tableCellLocation"]["tableStartLocation"]["index"] == timeline_table["startIndex"]]
        fills = {
            (update["tableRange"]["tableCellLocation"]["rowIndex"], update["tableRange"]["tableCellLocation"]["columnIndex"]):
            update["tableCellStyle"]["backgroundColor"]
            for update in cell_updates
            if update["tableRange"]["rowSpan"] == 1 and update["tableRange"]["columnSpan"] == 1
        }
        hexc = self.module.hex_color
        self.assertEqual(fills[(1, 2)], hexc("#D9EAD3"))
        self.assertEqual(fills[(2, 6)], hexc("#FFF2CC"))
        self.assertEqual({fills[(row, 5)]["color"]["rgbColor"]["red"] for row in range(1, 5)}, {hexc("#F4CCCC")["color"]["rgbColor"]["red"]})
        self.assertNotIn((1, 3), fills)  # blank weeks stay white from the whole-grid pass
        week_header = next(update for update in cell_updates if update["tableRange"]["tableCellLocation"] == {
            "tableStartLocation": {"index": timeline_table["startIndex"], "tabId": "t.0"}, "rowIndex": 0, "columnIndex": 2})
        self.assertEqual(week_header["tableCellStyle"]["contentAlignment"], "BOTTOM")
        self.assertEqual(week_header["tableCellStyle"]["paddingTop"], {"magnitude": 2, "unit": "PT"})
        self.assertEqual(week_header["tableRange"]["columnSpan"], 5)
        row_heights = [(request["updateTableRowStyle"]["rowIndices"], request["updateTableRowStyle"]["tableRowStyle"]["minRowHeight"]["magnitude"])
                       for request in payload["requests"] if "updateTableRowStyle" in request]
        self.assertEqual(row_heights[:2], [([0], 0), ([1, 2, 3, 4], 20)])
        self.assertEqual(row_heights[2], (list(range(22)), 25.75))
        week_paragraphs = [request["updateParagraphStyle"]["paragraphStyle"] for request in payload["requests"]
                           if "updateParagraphStyle" in request and request["updateParagraphStyle"]["paragraphStyle"].get("alignment") == "END"]
        self.assertEqual(len(week_paragraphs), 5)
        fonts = {request["updateTextStyle"]["textStyle"]["weightedFontFamily"]["fontFamily"] for request in payload["requests"]
                 if "updateTextStyle" in request and "weightedFontFamily" in request["updateTextStyle"]["textStyle"]}
        self.assertEqual(fonts, {"DM Sans", "DM Serif Display"})

    def test_formatter_draws_overview_borders_and_merged_bands(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        overview_table = self.module.doc_tables(tab_of(doc))[1]
        payload = self.module.build_format_requests(doc, self.manifest)
        whole = next(request["updateTableCellStyle"] for request in payload["requests"]
                     if "updateTableCellStyle" in request
                     and request["updateTableCellStyle"]["tableRange"]["tableCellLocation"]["tableStartLocation"]["index"] == overview_table["startIndex"]
                     and request["updateTableCellStyle"]["tableRange"]["rowSpan"] == 22)
        for side in ("borderTop", "borderBottom", "borderLeft", "borderRight"):
            self.assertEqual(whole["tableCellStyle"][side]["width"], {"magnitude": 0.75, "unit": "PT"})
            self.assertEqual(whole["tableCellStyle"][side]["dashStyle"], "SOLID")
            self.assertEqual(whole["tableCellStyle"][side]["color"], self.module.hex_color("#000000"))
        self.assertEqual(whole["tableCellStyle"]["contentAlignment"], "TOP")
        band_styles = [request["updateParagraphStyle"]["paragraphStyle"] for request in payload["requests"]
                       if "updateParagraphStyle" in request and request["updateParagraphStyle"]["paragraphStyle"].get("namedStyleType") == "HEADING_4"]
        self.assertEqual(len(band_styles), 4)
        self.assertTrue(all((style["spaceAbove"]["magnitude"], style["spaceBelow"]["magnitude"], style["lineSpacing"]) == (14, 4, 115) for style in band_styles))
        labels = [request["updateParagraphStyle"]["paragraphStyle"] for request in payload["requests"]
                  if "updateParagraphStyle" in request and request["updateParagraphStyle"]["paragraphStyle"].get("namedStyleType") == "HEADING_5"]
        self.assertEqual(len(labels), 22 - 4 - 2)

    def test_formatter_creates_nested_and_numbered_lists_after_styling(self) -> None:
        source = fixture().replace(
            "| **Objectives** | - **Establish a human-grounded evaluation standard.** This will define the evidence needed for the adoption decision.<br>- **Identify material disagreement patterns.** This will show where refinement is necessary. |",
            "| **Objectives** | 1. **Establish a human-grounded evaluation standard.**<br>  1. Define the evidence needed for the adoption decision.<br>2. **Identify material disagreement patterns.** |",
            1,
        )
        manifest = self.module.parse_markdown(source)
        normalized = formatted_document(self.module, manifest, pre_bullets=True)
        overview = self.module.doc_tables(tab_of(normalized))[1]
        labels = [row["label"] for row in manifest["rows"]]
        payload = self.module.build_format_requests(normalized, manifest)
        requests = payload["requests"]
        bullets = [(index, request["createParagraphBullets"]) for index, request in enumerate(requests) if "createParagraphBullets" in request]
        presets = [request["bulletPreset"] for _, request in bullets]
        self.assertEqual(presets.count("NUMBERED_DECIMAL_NESTED"), 1)
        self.assertEqual(presets.count("BULLET_DISC_CIRCLE_SQUARE"), sum(1 for row in manifest["rows"] if row["list"] == "BULLET") + 1)

        method = self.module.cell_paragraphs(overview["table"]["tableRows"][labels.index("Method & approach")]["tableCells"][1])
        self.assertTrue(self.module.paragraph_text(method[2]["paragraph"]).startswith("\tSend every split decision"))
        index, bullet = next((index, request) for index, request in bullets if request["range"]["startIndex"] == method[0]["startIndex"])
        self.assertEqual(bullet["range"]["endIndex"], method[-1]["endIndex"])
        follow = [requests[position]["updateParagraphStyle"] for position in range(index + 1, index + 5)]
        self.assertEqual([update["paragraphStyle"]["indentStart"]["magnitude"] for update in follow], [36, 36, 72, 36])
        self.assertEqual([update["paragraphStyle"]["indentFirstLine"]["magnitude"] for update in follow], [18, 18, 54, 18])
        # Bullet creation consumes the nested item's tab, so it and the paragraph after it move up one index.
        self.assertEqual(follow[2]["range"], {"startIndex": method[2]["startIndex"], "endIndex": method[2]["endIndex"] - 1, "tabId": "t.0"})
        self.assertEqual(follow[3]["range"]["startIndex"], method[3]["startIndex"] - 1)
        # Inline bold inside a tabbed item starts after its tab.
        objectives = self.module.cell_paragraphs(overview["table"]["tableRows"][labels.index("Objectives")]["tableCells"][1])
        bold = [request["updateTextStyle"]["range"] for request in requests
                if "updateTextStyle" in request and request["updateTextStyle"]["fields"] == "bold"
                and objectives[0]["startIndex"] <= request["updateTextStyle"]["range"]["startIndex"] < objectives[-1]["endIndex"]]
        self.assertEqual(bold[0]["startIndex"], objectives[0]["startIndex"])
        # Text-changing writes come after every style write, from the highest index to the lowest.
        starts = [request["range"]["startIndex"] for _, request in bullets[1:]]
        self.assertEqual(starts, sorted(starts, reverse=True))
        self.assertGreater(bullets[1][0], max(position for position, request in enumerate(requests) if "updateTableColumnProperties" in request))

    def test_formatter_applies_legend_swatch_backgrounds(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        legend = self.module.find_paragraph(tab_of(doc)["body"]["content"], self.manifest["timeline_note"]["text"])
        payload = self.module.build_format_requests(doc, self.manifest)
        swatches = [request["updateTextStyle"] for request in payload["requests"]
                    if "updateTextStyle" in request and request["updateTextStyle"]["fields"] == "backgroundColor"]
        text = self.manifest["timeline_note"]["text"]
        found = {text[update["range"]["startIndex"] - legend["startIndex"]:update["range"]["endIndex"] - legend["startIndex"]]:
                 update["textStyle"]["backgroundColor"] for update in swatches}
        hexc = self.module.hex_color
        self.assertEqual(found, {"Green": hexc("#D9EAD3"), "Yellow": hexc("#FFF2CC"), "Red": hexc("#F4CCCC")})

    def test_formatter_requires_a_normalized_doc(self) -> None:
        imported = synthetic_document(self.module, self.manifest, conversion_header=False)
        with self.assertRaisesRegex(self.module.ContractError, "run normalize first"):
            self.module.build_format_requests(imported, self.manifest)

    def test_formatter_deletes_empty_paragraphs_a_merge_leaves_behind(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        band_cell = overview["table"]["tableRows"][2]["tableCells"][0]
        label = self.module.cell_paragraphs(band_cell)[0]
        extra = DocBuilder(self.module).paragraph_at(label["endIndex"], plain(""))
        band_cell["content"].append(extra)
        payload = self.module.build_format_requests(doc, self.manifest)
        deletes = [request["deleteContentRange"]["range"] for request in payload["requests"] if "deleteContentRange" in request]
        self.assertIn({"startIndex": label["endIndex"] - 1, "endIndex": extra["endIndex"] - 1, "tabId": "t.0"}, deletes)

    # verify -----------------------------------------------------------------------------------

    def test_hard_verifier_accepts_complete_option4_doc_and_rejects_visual_drift(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        checks = self.module.verify_document(doc, self.manifest)
        self.assertEqual(len(checks), 6)

        drifted = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(drifted))[1]
        overview["table"]["tableRows"][0]["tableCells"][0]["tableCellStyle"]["backgroundColor"] = self.module.hex_color("#FF0000")
        self.assert_verify_fails(drifted, "background mismatch")

    def test_verifier_rejects_unmerged_bands_and_phases(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        overview["table"]["tableRows"][2]["tableCells"][0]["tableCellStyle"]["columnSpan"] = 1
        self.assert_verify_fails(doc, "Section band 'Key Information' must be one merged cell")

        doc = formatted_document(self.module, self.manifest)
        timeline = self.module.doc_tables(tab_of(doc))[0]
        timeline["table"]["tableRows"][1]["tableCells"][0]["tableCellStyle"]["rowSpan"] = 1
        self.assert_verify_fails(doc, "Phase cell in timeline row 1 spans 1 rows; expected 2")

    def test_verifier_checks_status_fills_and_legend_swatches(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        timeline = self.module.doc_tables(tab_of(doc))[0]
        timeline["table"]["tableRows"][1]["tableCells"][2]["tableCellStyle"]["backgroundColor"] = self.module.hex_color("#FFFFFF")
        self.assert_verify_fails(doc, "Timeline background mismatch at 1,2")

        doc = formatted_document(self.module, self.manifest)
        legend = self.module.find_paragraph(tab_of(doc)["body"]["content"], self.manifest["timeline_note"]["text"])
        swatch_run = next(child for child in legend["paragraph"]["elements"] if child["textRun"]["content"] == "Yellow")
        swatch_run["textRun"]["textStyle"].pop("backgroundColor")
        self.assert_verify_fails(doc, "only legend swatches carry a background")

    def test_verifier_requires_two_rules_and_their_spacers(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        body = tab_of(doc)["body"]["content"]
        rules = [element for element in body if "paragraph" in element and any("horizontalRule" in child for child in element["paragraph"]["elements"])]
        self.assertEqual(len(rules), 2)
        body.remove(rules[1])
        self.assert_verify_fails(doc, "hierarchy does not match")

        doc = formatted_document(self.module, self.manifest)
        body = tab_of(doc)["body"]["content"]
        heading = self.module.find_paragraph(body, "Project Plan Overview")
        body.remove(body[body.index(heading) + 1])
        self.assert_verify_fails(doc, r"Expected 1 empty spacer paragraph\(s\) before 'the overview table'; found 0")

        doc = formatted_document(self.module, self.manifest)
        body = tab_of(doc)["body"]["content"]
        heading = self.module.find_paragraph(body, "Research Timeline")
        body.insert(body.index(heading), json.loads(json.dumps(body[body.index(heading) + 1])))
        self.assert_verify_fails(doc, "Expected 0 empty spacer")

    def test_verifier_checks_overview_borders_labels_and_row_heights(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        overview["table"]["tableRows"][5]["tableCells"][1]["tableCellStyle"]["borderTop"]["width"]["magnitude"] = 1
        self.assert_verify_fails(doc, "0.75pt solid black borders")

        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        label = self.module.cell_paragraphs(overview["table"]["tableRows"][3]["tableCells"][0])[0]
        label["paragraph"]["paragraphStyle"]["namedStyleType"] = "NORMAL_TEXT"
        self.assert_verify_fails(doc, "'Background' uses NORMAL_TEXT; expected HEADING_5")

        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        overview["table"]["tableRows"][4]["tableRowStyle"]["minRowHeight"]["magnitude"] = 39.25
        self.assert_verify_fails(doc, "25.75pt minimum height")

        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        overview["table"]["tableRows"][0]["tableRowStyle"]["tableHeader"] = True
        self.assert_verify_fails(doc, "must not be pinned")

    def test_verifier_checks_list_glyphs_and_nesting(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        tab_of(doc)["lists"]["bullets"]["listProperties"]["nestingLevels"][1]["glyphSymbol"] = "-"
        self.assert_verify_fails(doc, "uses glyph '-'; expected '○'")

        doc = formatted_document(self.module, self.manifest)
        overview = self.module.doc_tables(tab_of(doc))[1]
        labels = [row["label"] for row in self.manifest["rows"]]
        nested = self.module.cell_paragraphs(overview["table"]["tableRows"][labels.index("Method & approach")]["tableCells"][1])[2]
        nested["paragraph"]["bullet"].pop("nestingLevel")
        self.assert_verify_fails(doc, "sits at list level 0; expected 1")

    def test_verifier_rejects_arial_week_labels_and_review_highlights(self) -> None:
        doc = formatted_document(self.module, self.manifest)
        timeline = self.module.doc_tables(tab_of(doc))[0]
        label = self.module.cell_paragraphs(timeline["table"]["tableRows"][0]["tableCells"][2])[0]
        label["paragraph"]["elements"][0]["textRun"]["textStyle"]["weightedFontFamily"]["fontFamily"] = "Arial"
        self.assert_verify_fails(doc, "Wrong font for 'Nov. 2'")

        doc = formatted_document(self.module, self.manifest)
        heading = self.module.find_paragraph(tab_of(doc)["body"]["content"], "Research Timeline")
        heading["paragraph"]["elements"][0]["textRun"]["textStyle"]["backgroundColor"] = self.module.hex_color("#FFFF00")
        self.assert_verify_fails(doc, "Text highlight mismatch")

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
            element["paragraph"]["elements"] = [first, second] + element["paragraph"]["elements"][1:]

        cell_doc = formatted_document(self.module, self.manifest)
        timeline = self.module.doc_tables(tab_of(cell_doc))[0]
        corrupt_second_run(self.module.cell_paragraphs(timeline["table"]["tableRows"][1]["tableCells"][1])[0])
        self.assert_verify_fails(cell_doc, "Wrong run font size")

        title_doc = formatted_document(self.module, self.manifest)
        corrupt_second_run(self.module.find_paragraph(tab_of(title_doc)["body"]["content"], self.manifest["top"]["title"]["text"]))
        self.assert_verify_fails(title_doc, "Wrong run font size")

    # tool surface -----------------------------------------------------------------------------

    def test_layout_tool_exposes_required_pipeline(self) -> None:
        for name in ("parse_markdown", "parse_timeline_table", "build_normalize_requests", "build_format_requests", "verify_document"):
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
            manifest = root / "manifest.json"
            output = root / "batch.json"
            manifest.write_text(json.dumps(self.manifest), encoding="utf-8")
            malformed = root / "malformed-doc.json"
            malformed.write_text("{not json", encoding="utf-8")
            wrong_shape = root / "wrong-shape-doc.json"
            wrong_shape.write_text("[]", encoding="utf-8")
            for document, extra, message in (
                (root / "missing-doc.json", [], "FAIL:"),
                (malformed, [], "FAIL:"),
                (wrong_shape, ["--required-revision-id", "revision-123"], "JSON root must be an object"),
            ):
                with self.subTest(document=document.name):
                    result = run_script("normalize", str(document), str(manifest), str(output), *extra)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn(message, result.stderr)
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
