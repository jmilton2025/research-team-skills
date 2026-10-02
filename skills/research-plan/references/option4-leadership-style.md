# Option 4 — Leadership Visual Contract

This is the visual source of truth for every Google Doc produced by `/research-plan`. The machine-readable values live in [`option4-style-contract.json`](option4-style-contract.json); the formatter and verifier consume that contract.

The approved private Option 4 Google Doc was used once to audit these values. It is not a runtime dependency, and colleagues do not need access to it.

## Required hierarchy

Every finished plan has this order:

1. Breadcrumb.
2. Stakeholder-facing title.
3. Last-updated date.
4. Four RACI bullet paragraphs.
5. Full-width test warning for mock/demo runs only.
6. Optional short context note when the plan needs a historical or interpretation caveat.
7. **Research Timeline** heading.
8. Five-row leadership timeline table: one header plus four concise milestones.
9. One-sentence italic timing note.
10. Thin divider.
11. **Project Plan Overview** heading.
12. Two-column project-plan table, with Topic as the first visible row and no generic conversion header.

The detailed Timeline row remains in the project-plan table. The leadership timeline is a concise at-a-glance summary derived from it, not a replacement.

## Page and typography

- Pageless Google Docs editing mode with landscape-letter (792 × 612pt) export metadata.
- One-inch (72pt) print/export margins on every side for body paragraphs; 36pt header and footer margins.
- Google Docs derives `useCustomHeaderFooterMargins=true` when those margins are set. That response field is output-only and must not be sent in `updateDocumentStyle`.
- Breadcrumb: **DM Serif Display, 16pt, bold, gray `#666666`**.
- Title: **DM Serif Display, 26pt, bold, dark green `#003D29`**.
- H1 headings: **DM Serif Display, 20pt, bold, black**.
- Body, RACI, table labels, and table content: **DM Sans, 10pt**.
- Section bands: **DM Serif Display, 14pt, bold, white** on dark green.
- Context notes: **DM Sans, 9pt, italic, gray `#666666`**.

Apply named paragraph styles before direct text styles. Google Docs can clear direct font overrides when a named style is applied afterward.

## Warning treatment

For a mock/demo/test only:

- shade the entire warning paragraph pale yellow `#FFF2CC`;
- use DM Sans 10pt bold text in `#6F4A00`;
- retain the exact approved warning copy.

Inline highlighting is not equivalent to full-paragraph shading.

## Leadership timeline

- Exactly two columns and five rows: one header plus four milestones.
- Fixed widths: **144pt / 554.4pt**; 5pt cell padding on all sides.
- The widths intentionally total 698.4pt—50.4pt wider than the 648pt paragraph text area. Google Docs lets the approved tables extend into the print margins; do not shrink them to 648pt.
- Header row: dark green `#003D29`, white bold DM Sans 10pt, pinned as a repeating table header. The header text is exactly `Timing | Leadership milestone`.
- Left milestone column: gray `#D9D9D9`, bold DM Sans 10pt.
- Right column: white, DM Sans 10pt.
- Each left-hand label starts with its timing, then a short name, such as `Week 1: Setup & rubric` or `Weeks 2–3: Calibration`. Use `Day N:` or `Month N:` only for studies measured in days or months.
- Each left-hand label is no more than 24 characters, so it renders on one line in the 144pt column. In the 2026-10-02 mock, a 26-character label wrapped and split the timeline across pages. Each right-hand milestone is one concise sentence, no more than 160 characters. Put detailed dates, contingencies, and dependencies in the plan's Timeline row.
- The four milestones adapt to the study. Do not copy an old study's week labels or schedule.

If the leadership timeline spills onto another page, shorten any wrapped label or tighten only the timeline summary; preserve the approved detailed Timeline row.

## Project Plan Overview table

- Fixed widths: **144pt / 554.4pt**; 5pt cell padding on all sides. The intentional 698.4pt table width matches the approved reference; do not normalize it to the 648pt paragraph text area.
- Topic is the first visible row. Remove the `Section / element | Approved content` conversion header.
- Ordinary label and content cells are white.
- Label cells use bold black DM Sans 10pt.
- Multi-item content uses true Google Docs list paragraphs with 36pt start / 18pt first-line indentation.
- Preserve restrained bold lead-ins, italics, and active source links.
- The four section rows are `KEY INFORMATION`, `PROJECT DETAILS`, `DELIVERABLES & NEXT STEPS`, and `APPENDIX`.
- A section row remains two physical cells with `columnSpan=1` in both cells. Color both cells dark green so they read as one full-width band; do not merge them.
- Section text is white DM Serif Display 14pt bold.

## Required build pipeline

Use `scripts/option4_layout.py`:

1. `manifest` — parse the approved markdown into a style/content manifest.
2. Import the markdown into the confirmed Google Drive folder using a conversion path that turns the intermediate `---` into one native horizontal rule. The Docs batch API cannot create that rule after import.
3. `normalize` — rebuild cell text, remove the conversion header, and restore two-cell section rows.
4. Re-fetch the raw Google Docs JSON.
5. `format` — generate the exact Option 4 Google Docs batch operations.
6. Apply those operations and re-fetch the document.
7. `verify` — validate content and all machine-checkable visual invariants.
8. Export/render the Doc and visually inspect every page. The verifier cannot see page breaks, so a timeline split or an orphaned section band shows up only in the render.

The command accepts `--help` for exact arguments.

## Hard completion gate

A research plan is not complete when formatting is approximate. This gate is not researcher-, stakeholder-, or leadership-waivable: an instruction to accept a downgrade still blocks final delivery. Block completion instead of returning a downgraded layout when any of these are unavailable:

- a write-capable Google Docs integration;
- raw document structure or equivalent indices;
- native batch formatting needed to apply the contract;
- the bundled verifier;
- a PDF/thumbnail/render for visual inspection.

Do not substitute Arial, a one-table layout, merged section rows, generic colors, inline warning highlighting, or a structural-only check and still call the result final.
