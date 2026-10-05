# Option 4 — Leadership Visual Contract

This is the visual source of truth for every Google Doc produced by `/research-plan`. The machine-readable values live in [`option4-style-contract.json`](option4-style-contract.json); the formatter and verifier consume that contract.

The approved private Option 4 Google Doc was used once to audit these values. It is not a runtime dependency, and colleagues do not need access to it.

## Required hierarchy

Every finished plan has this order:

1. Breadcrumb.
2. Stakeholder-facing title.
3. Last-updated date.
4. Four RACI bullet paragraphs.
5. Full-width warning banner for test runs only.
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

For a test only, use one of the two approved lines, word for word:

- simulated or mock inputs: `⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.`
- real, authorized inputs used to test the workflow: `⚠️ TEST RUN — real, authorized inputs, created to test the workflow. Not a stakeholder deliverable.`

A real study has no banner. For either line:

- shade the entire warning paragraph pale yellow `#FFF2CC`;
- use DM Sans 10pt bold text in `#6F4A00`;
- retain the exact approved warning copy; the manifest rejects any other line that starts with ⚠️.

Inline highlighting is not equivalent to full-paragraph shading.

## Leadership timeline

- Exactly two columns and five rows: one header plus four milestones.
- Fixed widths: **144pt / 554.4pt**; 5pt cell padding on all sides.
- The widths intentionally total 698.4pt—50.4pt wider than the 648pt paragraph text area. Google Docs lets the approved tables extend into the print margins; do not shrink them to 648pt.
- Header row: dark green `#003D29`, white bold DM Sans 10pt, pinned as a repeating table header. The header text is exactly `Timing | Leadership milestone`.
- Left milestone column: gray `#D9D9D9`, bold DM Sans 10pt.
- Right column: white, DM Sans 10pt.
- Each left-hand label starts with its timing, then a short name, such as `Week 1: Setup & rubric` or `Weeks 2–3: Calibration`. Use `Day N:` or `Month N:` only for studies measured in days or months.
- Each left-hand label renders on one line: its printed width in bold DM Sans 10pt is at most **134pt**, the 144pt column less 5pt padding on each side. The contract stores DM Sans Bold advance widths, and the parser adds them up for each label; a character outside the table counts as the widest glyph. Character counts don't work: in the 2026-10-02 mock, the 27-character `Week 1: Setup & definitions` (133.1pt) fit, while 26- and 27-character labels measuring 141.1pt and 143.0pt wrapped and split the timeline across pages. Each right-hand milestone is one concise sentence that also renders on one line: at most **544.4pt** wide (the 554.4pt column less padding) in regular DM Sans 10pt, with bold words measured at bold width. The contract stores DM Sans Regular advance widths for this. That is usually about 110–120 characters; 160 characters is a hard cap. Put detailed dates, contingencies, and dependencies in the plan's Timeline row.
- The four milestones adapt to the study. Do not copy an old study's week labels or schedule.

The `timeline` command measures every label and milestone before the Timeline approval, so rows should never wrap in the Doc. If the leadership timeline still spills onto another page, shorten any wrapped row, then tighten the opening and the timing note, then the RACI lines; preserve the approved detailed Timeline row.

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

Use `scripts/option4_layout.py`. Two checks run before the build:

- `timeline` — at Section 3 > Timeline, measure a draft timeline table and print `PASS` or a `FAIL` line for each row that would wrap.
- `lint` — at Step 4, check the assembled plan for layout failures, content-rule gaps (`FIX OR ACCEPT`), and quotes to confirm against their source (`CONFIRM QUOTE`).

The build:

1. `manifest` — parse the approved markdown into a style/content manifest. It also records a fingerprint of the layout script and this contract; `normalize`, `format`, and `verify` fail if either changed mid-run.
2. Import the markdown into the confirmed Google Drive folder using a conversion path that turns the intermediate `---` into one native horizontal rule. The Docs batch API cannot create that rule after import. With `gws`, run `gws drive files create --upload plan.md --upload-content-type text/markdown` from the private working directory (gws only uploads files inside the current directory), with only the name, `application/vnd.google-apps.document`, and the folder ID in `--json`. This route was checked on 2026-10-05: it turned `---` into one native rule and kept native headings, tables, and bullets.
3. `normalize` — rebuild cell text, remove the conversion header, and restore two-cell section rows.
4. Re-fetch the raw Google Docs JSON.
5. `format` — generate the exact Option 4 Google Docs batch operations.
6. Apply those operations and re-fetch the document. Apply every batch (normalize and format) through a protected request body; with `gws`, use `send`, which applies a revision-bound batch file without a shell.
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
