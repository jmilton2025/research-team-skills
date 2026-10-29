# Option 4 — Leadership Visual Contract

This is the visual source of truth for every Google Doc produced by `/research-plan`. The machine-readable values live in [`option4-style-contract.json`](option4-style-contract.json) (contract version 2026-10-29); the formatter and verifier consume that contract.

The layout matches the visual design of the approved International retailer research plan (Q3 2025): its page, typography, timeline grid, rules, and table treatment. It does not copy that plan's content; the rows stay as `content-rules.md` defines them. The reference was used once to audit these values. It is not a runtime dependency, and colleagues do not need access to it.

## Required hierarchy

Every finished plan has this order:

1. Breadcrumb.
2. Stakeholder-facing title.
3. Last-updated date.
4. Four RACI bullet paragraphs.
5. Full-width warning banner for test runs only.
6. Optional short context note when the plan needs a historical or interpretation caveat.
7. An empty paragraph, then a native horizontal rule.
8. **Research Timeline** heading, then an empty paragraph.
9. The Gantt timeline grid.
10. The italic legend note, then an empty paragraph.
11. A second native horizontal rule.
12. **Project Plan Overview** heading, then an empty paragraph.
13. Two-column project-plan table, with Topic as the first visible row and no generic conversion header.

Each rule's own paragraph sits directly above its heading, as in the reference; the heading's 20pt space above separates them. The empty spacer paragraphs are plain NORMAL_TEXT at 10pt. The detailed Timeline row remains in the project-plan table; the grid charts it week by week.

## Page and typography

- Pageless Google Docs editing mode with landscape-letter (792 × 612pt) export metadata.
- One-inch (72pt) print/export margins on every side for body paragraphs; 36pt header and footer margins.
- Google Docs derives `useCustomHeaderFooterMargins=true` when those margins are set. That response field is output-only and must not be sent in `updateDocumentStyle`.

Each role uses the reference's named-style type and values:

| Role | Named style | Font | Size | Bold | Color | Space above / below | Line spacing |
|---|---|---|---|---|---|---|---|
| Breadcrumb | SUBTITLE | DM Serif Display | 16pt | yes | `#666666` | 0 / 16pt | 115% |
| Title | TITLE | DM Serif Display | 26pt | yes | `#003D29` | 0 / 3pt | 115% |
| H1 headings | HEADING_1 | DM Serif Display | 20pt | yes | `#000000` | 20 / 6pt | 115% |
| Section bands | HEADING_4 | DM Serif Display | 14pt | yes | `#FFFFFF` (the style's own color is `#003D29`) | 14 / 4pt | 115% |
| Overview labels | HEADING_5 | DM Sans | 10pt | yes | `#000000` | 0 / 0 | 115% |
| Body, RACI, table content | NORMAL_TEXT | DM Sans | 10pt | no | `#000000` | 0 / 0 | 115% |

- TITLE, SUBTITLE, and the headings keep their lines together and keep with the next paragraph.
- `Last updated` is NORMAL_TEXT with 12 / 12pt spacing; RACI bullets are 36pt start / 18pt first-line indent with 12 / 12pt spacing.
- `Topic` and `TL;DR summary of findings` labels are NORMAL_TEXT with direct bold, as in the reference.
- Links: `#1155CC`, underlined.
- Context notes: **DM Sans, 9pt, italic, gray `#666666`**.

The Docs batchUpdate API has no request that edits a named style's definition. The formatter therefore applies the values above as direct paragraph and text styles on every paragraph that uses the named style, and the verifier checks the effective values. Apply named paragraph styles before direct text styles: Google Docs can clear direct font overrides when a named style is applied afterward.

## Warning treatment

For a test only, use one of the two approved lines, word for word:

- simulated or mock inputs: `⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.`
- real, authorized inputs used to test the workflow: `⚠️ TEST RUN — real, authorized inputs, created to test the workflow. Not a stakeholder deliverable.`

A real study has no banner, and the reference has none. For either line:

- shade the entire warning paragraph pale yellow `#FFF2CC`;
- use DM Sans 10pt bold text in `#6F4A00`;
- retain the exact approved warning copy; the manifest rejects any other line that starts with ⚠️.

Inline highlighting is not equivalent to full-paragraph shading.

## Research Timeline grid

The timeline is a Gantt grid: `Phase | Activity | one column per week`.

- **Widths (fixed):** Phase **180pt**, Activity **72pt**, and **54pt** per week. The grid holds at most 12 week columns, so it is at most **900pt** wide, 252pt wider than the 648pt text area, as in the reference; do not shrink it. A study longer than 12 weeks keeps the weeks that matter and replaces one run of middle weeks with a single `…` filler column, never the first or last.
- **Header row:** every cell dark green `#003D29`, not pinned, no minimum height. `Phase` and `Activity`: DM Sans 10pt bold white, 5pt padding, top-aligned, start-aligned, 100% line spacing. Week labels (`Nov. 3`, or `Week N` until dates are set): DM Sans 10pt bold white, 2pt padding, bottom-aligned, right-aligned, 115% line spacing. The reference's Arial week dates are an inconsistency; use DM Sans.
- **Activity rows:** 20pt minimum height, 5pt padding, top-aligned, 100% line spacing, 0 / 0 spacing.
- **Phase column:** gray `#D9D9D9`, bold DM Sans: `Phase N:` on one line and the phase name on the next. The Phase cell is **merged down** across all of that phase's activity rows.
- **Activity column:** gray `#D9D9D9`, regular DM Sans.
- **Week cells:** white by default. Status fills: **`#D9EAD3`** green for a target week, **`#FFF2CC`** yellow for possible spillover, and **`#F4CCCC`** red for a fixed event, which fills that week for every row. A cell may carry a one- or two-word regular note.
- **Borders:** left unset, so Google Docs draws its default grid, as in the reference.
- **Label fit:** the parser measures every label with the stored DM Sans advance widths (a character outside the table counts as the widest glyph). Week labels fit one line of 50pt in bold; phase names fit one line of 170pt in bold; activities fit at most two lines of 62pt and notes at most two lines of 44pt, with no word wider than its column.

### Markdown form

The approval step and the parser use this Markdown:

```markdown
| Phase | Activity | Nov. 2 | Nov. 9 | Nov. 16 | Nov. 23 | Nov. 30 |
|---|---|---|---|---|---|---|
| **Phase 1:** Setup & calibration | Rubric & sample | [target] | | | [event] | |
| | Calibration | | [target] Human raters | [target] | [event] | [spillover] |
| **Phase 2:** Validation & decision | Blind validation | | | | [event] | [target] |
| | Readout | | | | [event] | [target] Decision |

*Note: Timing depends on finalized inputs and evaluator capacity; Green = target dates; Yellow = possible spillover; Red = US holiday week*
```

- A Phase cell reads `Phase N: Name` (bold markers optional), numbered from 1 in order. A blank Phase cell continues the phase above and becomes part of its merged cell.
- A week cell is blank, or one of `[target]`, `[spillover]`, or `[event]`, optionally followed by a short plain note. Any other text fails. An `[event]` week must be `[event]` in every row.
- Activities and notes are plain text.

### Legend note

The italic paragraph directly under the grid: DM Sans 10pt italic black, NORMAL_TEXT, 115% line spacing. It holds one timing caveat and ends with `; Green = target dates; Yellow = possible spillover`, plus `; Red = <the fixed event>` exactly when the grid has `[event]` weeks. The words `Green`, `Yellow`, and `Red` carry the matching run background (`#D9EAD3`, `#FFF2CC`, `#F4CCCC`) as inline swatches; no other text in the Doc has a background.

The `timeline` command checks the grid before the Timeline approval, so labels should never wrap in the Doc. If the grid still spills onto another page, shorten any wrapped label, then tighten the opening and the legend note, then the RACI lines; preserve the approved detailed Timeline row.

## Project Plan Overview table

- Fixed widths: **144pt / 554.4pt**; 5pt cell padding on all sides; every cell top-aligned. The intentional 698.4pt table width matches the reference; do not normalize it to the 648pt paragraph text area.
- Borders: black `#000000`, **0.75pt solid** on all four sides of every cell. The reference's 1pt Appendix edges are an inconsistency.
- Rows: **25.75pt** minimum height. The reference's taller rows (39.25pt and 52.75pt) were sized to its own content, so they aren't carried over.
- Topic is the first visible row, and the first row is not pinned. Remove the `Section / element | Approved content` conversion header.
- Ordinary label and content cells are white. Label cells use the HEADING_5 role (bold black DM Sans 10pt); `Topic` and `TL;DR summary of findings` use NORMAL_TEXT plus bold.
- Body cells use NORMAL_TEXT at 115% line spacing.
- Multi-item content uses true Google Docs list paragraphs: `●` `○` `■` bullets (repeating below the third level) or DECIMAL `1.` / `1.1.` numbers. Level *n* (from 0) indents to 36·(*n*+1)pt with an 18pt hanging first line: 36/18, 72/54, 108/90, and so on. In Markdown, two leading spaces after a `<br>` nest an item one level.
- Preserve restrained bold lead-ins, italics, and active `#1155CC` underlined source links. Names stay plain text: the Docs batch API can't reliably turn names into person chips or file chips, so neither is used.
- The four section bands are `Key Information`, `Project Details`, `Deliverables & Next Steps`, and `Appendix`, in Title Case.
- A section band is **one merged cell** (`columnSpan=2`), dark green `#003D29`, with its name in the HEADING_4 role recolored white `#FFFFFF`. The HEADING_4 spacing (14 / 4pt) makes the band taller than a label row, as in the reference. The reference's near-white `#F3F3F3` on its first band is an inconsistency; every band uses white.
- Do not add the reference's yellow `#FFFF00` review highlights.

## Required build pipeline

Use `scripts/option4_layout.py`. Two checks run before the build:

- `timeline` — at Section 3 > Timeline, check a draft grid and print `PASS`, or a `FAIL` line for each label that doesn't fit and each phase, token, or event problem.
- `lint` — at Step 4, check the assembled plan for layout failures, content-rule gaps (`FIX OR ACCEPT`), and quotes to confirm against their source (`CONFIRM QUOTE`).

The build:

1. `manifest` — parse the approved markdown into a style/content manifest. It also records a fingerprint of the layout script and this contract; `normalize`, `format`, and `verify` fail if either changed mid-run.
2. Import the markdown into the confirmed Google Drive folder using a conversion path that turns each intermediate `---` into a native horizontal rule; the plan has two. The Docs batch API cannot create a rule after import. With `gws`, run `gws drive files create --upload plan.md --upload-content-type text/markdown` from the private working directory (gws only uploads files inside the current directory), with only the name, `application/vnd.google-apps.document`, and the folder ID in `--json`. This route was checked on 2026-10-05: it turned `---` into a native rule and kept native headings, tables, and bullets.
3. `normalize` — rebuild cell text (status tokens become fills, Phase cells split into `Phase N:` and the name, list items get one leading tab per nesting level), remove the conversion header, merge the section bands and Phase cells, and add or remove empty spacer paragraphs around the rules and tables.
4. Re-fetch the raw Google Docs JSON.
5. `format` — generate the exact Option 4 Google Docs batch operations. List creation consumes the leading tabs, so those writes come last, from the highest index to the lowest.
6. Apply those operations and re-fetch the document. Apply every batch (normalize and format) through a protected request body; with `gws`, use `send`, which applies a revision-bound batch file without a shell.
7. `verify` — validate content and all machine-checkable visual invariants.
8. Export/render the Doc and visually inspect every page. The verifier cannot see page breaks, so a timeline split or an orphaned section band shows up only in the render. A grid wider than the text area prints scaled down in a PDF export; that is expected.

The command accepts `--help` for exact arguments.

## Hard completion gate

A research plan is not complete when formatting is approximate. This gate is not researcher-, stakeholder-, or leadership-waivable: an instruction to accept a downgrade still blocks final delivery. Block completion instead of returning a downgraded layout when any of these are unavailable:

- a write-capable Google Docs integration;
- raw document structure or equivalent indices;
- native batch formatting needed to apply the contract;
- the bundled verifier;
- a PDF/thumbnail/render for visual inspection.

Do not substitute Arial, a one-table layout, a list-style or milestone-table timeline, unmerged section bands, generic colors, inline warning highlighting, or a structural-only check and still call the result final.
