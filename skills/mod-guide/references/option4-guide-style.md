# Option 4 — Leadership Visual Contract (Moderation Guide)

This is the visual source of truth for the default **Option 4 — Leadership** path of `/mod-guide`. The machine-readable values live in [`option4-guide-style.json`](option4-guide-style.json); the formatter and verifier ([`../scripts/option4_guide_layout.py`](../scripts/option4_guide_layout.py)) consume that contract.

**This is the default deliverable look.** It is applied by the bundled `option4_guide_layout.py` with no personal environment or private reference Doc. Plain-native Google Docs is an explicit choice or a pre-approved, disclosed fallback. The finished moderation guide uses the same clean leadership visual system as `/research-plan`, not a raw import.

The visual language is shared with `/research-plan` Option 4: page geometry, colors, DM Serif Display / DM Sans, section bands, and tables. `derived_from` in the JSON points at that origin. The top matter, vertical rhythm, list geometry, inline label styles, and Session Flow table match **the approved Meals MVP moderation guide (October 2026)**, the researcher's reference for this look. That guide's design is reproduced here, not its content, and no reference document is a runtime dependency.

## Structure-agnostic

The critical property of this contract: it is **structure-agnostic.** mod-guide produces two structurally different documents, and the formatter styles by **element role inferred generically**, not by a fixed sequence of named semantic sections. It never assumes a particular section order, a fixed section list, a terminal section, or a fixed table shape.

The two guide shapes it supports today:

- **Interview / IDI** — the canonical top matter; Parameter and Consent tables; Research Objectives; and thematic **prose bullets with indented probes**. It ends at Post-Session Debrief or an optional Parking Lot.
- **Prototype / Usability** — the same canonical top matter; Parameter and `Phase | Description` Session Flow tables; Introduction, task phases, comparisons, and recap as **bold-label read/do lists**; and optional vendor **Communication & Deliverables** back-matter.

Both shapes share a Parameter | Detail table, a Pre-Session Checklist, and a Post-Session Debrief. Consent appears once per format: an interview Cue | Read aloud table or the prototype Introduction list. The formatter recognizes element roles, not study-specific section names.

## Top matter, in order

| # | Line | Markdown | Rendered as |
|---|---|---|---|
| 1 | Document title | `# Moderation Guide` | **TITLE** named style; DM Serif Display 26pt bold `#003D29`; 0 / 3pt; keep with next |
| 2 | Study title | `## [Study Title]` (required, immediately after the title) | a **NORMAL_TEXT paragraph, not a heading**; DM Serif Display 14pt bold `#003D29`; 0 / 3pt; keep with next |
| 3 | Study period | `Study period: [dates or TBD — fill in]` | DM Serif Display **16pt bold italic** gray `#666666`; 0 / 16pt; keep with next |
| 4 | RACI | `- **Responsible:** …` bullets (any label set) | ● bullets, DM Sans 10pt, bold label and regular value; 12 / 12pt (Docs collapses the space between items); indent 36 / 18pt |
| 5 | Links (optional) | `**Links:** [Label](url) · [Label](url)` | DM Sans 10pt; bold `Links:`; links **black and underlined, never blue**, separated by ` · ` |
| 6 | Parameter table | a `Parameter \| Detail` table | gray `#D9D9D9` bold label column, white value column |

Lines 1–3 stack with no spacer between them. The study title is written as `##` so the parser can find it, but it never becomes a band or an outline heading.

## How roles are inferred

| Element role | How it is recognized | Styled as |
|---|---|---|
| **Document title** | the required first heading `# Moderation Guide` | top-matter row 1 |
| **Study title** | the immediately following `## [Study Title]` | top-matter row 2 |
| **Study period** | a top-matter line whose text begins `Study period:` | top-matter row 3 |
| **RACI / ownership** | consecutive top-matter bullets `- **Label:** …` | top-matter row 4 |
| **Links line** | a top-matter line whose text begins `Links:` | top-matter row 5 |
| **TEST ARTIFACT warning** | a paragraph whose text is the exact warning copy | full-paragraph pale-yellow `#FFF2CC` shading, DM Sans 10pt bold `#6F4A00` |
| **Section band** | every `## ` after the study title | HEADING_2, dark-green `#003D29` full-width band, white DM Serif Display 14pt bold, UPPERCASE, 20 / 6pt |
| **Sub-phase heading** | EVERY `### ` | HEADING_3, DM Serif Display 12pt bold `#003D29`, 12 / 4pt |
| **Table** | EVERY Markdown table, any column count, any position | Option 4 table styling (see below) |
| **List** | EVERY bulleted / numbered block, including indented probe sub-bullets | DM Sans 10pt native list, nesting preserved (see Lists) |
| **Body** | any other paragraph | DM Sans 10pt black, 0 / 0pt |

Legacy lines still parse for backward compatibility but are not part of the canonical schema: a fully italic top-matter line or a line above the title (`breadcrumb`, DM Serif 16pt bold gray) and a `Last updated:` line (`context_note`, DM Sans 9pt italic gray).

### Inline label styles inside body text and lists

- **Topic lines** — `**Topic N — Name**` is a bold DM Sans 10pt **body line, not a heading**.
- **Objective / Key Questions** — `- *Objective:* …` and `- *Key Questions:* …`: the label is **italic, not bold**; the value is regular. These are the only italic labels in a guide.
- **Read / do lines** — `- **Label:** "quoted script"`: bold label, regular quoted script.
- **Checklist items** — ordinary ● bullets whose text starts with `☐ ` (not native checkboxes); the debrief may use inline `☐ a · ☐ b` options.
- **Moderator notes** — plain body text in `[brackets]`; no italic, gray, or callout treatment.

## Vertical rhythm

The reference look depends on its spacing. The pipeline reproduces it with **explicit empty spacer paragraphs**, as the reference does, not with paragraph spacing.

- **One spacer** sits between every pair of adjacent block groups: body → list, list → body, body → body, either side of a table, and before the next band.
- **No spacer:**
  - before the title;
  - between the title, the study title, and the study period;
  - after a section band, including between the Session Flow band and its table;
  - after an H3, and before an H3;
  - between items of the same list or RACI block.
- A spacer is a plain NORMAL_TEXT empty paragraph: 115% line spacing, 0 / 0pt, no indent, no bullet, no shading, keep-with-next off, widow/orphan control off. It has **no direct text style**, so it inherits the named style's font the way the reference spacers do.
- `normalize` reconciles the spacers. It inserts missing ones and removes extras, and it removes every imported `---` rule. When a surplus empty paragraph sits directly before a table, it is merged into the preceding paragraph, because Google Docs refuses to delete the newline that precedes a table. `format` styles every spacer, and `verify` rejects a missing, extra, or styled spacer.

## Lists

- Bullets use `BULLET_DISC_CIRCLE_SQUARE` (● ○ ■). Numbered lists use `NUMBERED_DECIMAL_ALPHA_ROMAN` (`1.` / `a.` / `i.`), and each numbered block restarts at 1.
- Indents step **36pt per level**, with an 18pt hanging indent: 36 / 18, 72 / 54, and 108 / 90pt.
- List items use 115% line spacing and 0 / 0pt paragraph spacing. RACI is the exception at 12 / 12pt.

## Page and typography

- Pageless Google Docs editing mode with landscape-letter (792 × 612pt) export metadata. Landscape is mandatory: the 698.4pt tables do not fit portrait letter's 468pt text area.
- One-inch (72pt) margins on every side; 36pt header/footer margins.
- Google Docs derives `useCustomHeaderFooterMargins=true` from those margins. That field is output-only and must not be sent in `updateDocumentStyle`.
- Named styles stay at their Google Docs defaults; every DM font is a direct text style. The research-plan 20pt-black `heading` token is intentionally **unused**; the 14pt bands take its structural role.
- DM Serif Display has no bold weight; `bold: true` renders as Google's synthesized bold, exactly as in the reference.

Apply named paragraph styles before direct text styles — Google Docs clears direct font overrides when a named style lands afterward.

## Warning treatment (test and demo runs only)

The reference guide has no warning block, so real-study guides carry none. Test, demo, and mock runs keep it:

- Shade the entire warning paragraph pale yellow `#FFF2CC` (full-paragraph shading, not inline highlight); DM Sans 10pt bold text in `#6F4A00`.
- Use the exact copy from [`../../../references/output-status-and-labeling-conventions.md`](../../../references/output-status-and-labeling-conventions.md): `⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.`

## Section bands — the key difference from research-plan

Research-plan puts its section bands as rows *inside* one big overview table. A moderation guide has no single spine table, so the band treatment moves onto each **section `##` heading after the study title**.

- Every section `##` after the study title becomes a dark-green full-width band: HEADING_2, DM Serif Display 14pt bold, white text, paragraph background `#003D29`, 20pt above / 6pt below, UPPERCASE label. The 20pt space above sits inside the shading, so the label sits low in a tall band.
- **Primary render (this contract): a shaded native Heading 2 paragraph.** This preserves the document outline so a moderator can jump between sections mid-session. The band spans the 648pt paragraph text area — ~50pt narrower than the tables beneath it, because paragraph shading cannot overflow into the print margins the way the tables do. This is expected and acceptable.
- **Documented alternative (`band_render_alt`): a single-row two-cell 698.4pt table** — matches research-plan's exact band width but loses the outline. Recommended against for a facilitation guide.
- Dividers: the markdown `---` separators are dropped during normalize (target `native_horizontal_rules: 0`). The bands and spacers do the sectioning.

## Tables — generic geometry, one aligned outer edge

Every table — whatever its columns, wherever it sits — shares: 5pt cell padding, white body cells, DM Sans 10pt cell text, 100% table line spacing with 0 / 0pt paragraph spacing, top-aligned cells, and **total width 698.4pt** (every table's outer edge aligns down the page, with the intentional 50.4pt overflow into the print margins). There is no visible header row: the Markdown header row is a conversion header and is dropped on import, so the first content row becomes the first visible row. Header presence is detected per table by row count, so a table may or may not arrive with the header attached.

Geometry is inferred from each table's complete header:

- **Column widths** — every two-column table, including `Parameter | Detail`, `Cue | Read aloud`, and the `Phase | Description` Session Flow, uses `[144, 554.4]`. A legacy first header cell of `#` uses `[90, 608.4]`. For 3+ columns, the first label column is 144pt and the remainder is split evenly.
- **Label-column background** — the top-matter Parameter dashboard gets the gray `#D9D9D9` label column; in-section Consent and Session Flow tables use white cells.
- **First-column bold** — the first column is bold only when every first-cell value is fully bold in the approved Markdown (Parameter, Consent). Session Flow phase labels stay regular weight. Inline emphasis is otherwise preserved exactly.
- **N columns** — the formatter remains column-count agnostic even though the current templates use two-column tables.

**Session Flow** is a `Phase | Description` table placed directly under its band: the phase label on the left and a one-line description on the right, all regular weight on white. Each phase label keeps the approved timing visible, e.g. `Introduction & Think-Aloud Setup (5 min)`, and the minutes sum to the session length.

**Borders** use the Google Docs default (1pt black), and the pipeline sends no border request at all (mirroring `/research-plan`'s Option 4 pipeline). Do not invent a border value. (Settled 2026-10-02 after two live builds: both verified clean with Docs-default borders.)

## What the verifier checks (VISUAL invariants only)

The verifier is a **visual gate**, not a semantic-structure gate. It checks:

- page geometry and margins;
- named style, font, size, weight, italic, color, and spacing for the title, study title, study period, RACI, Links line, bands, H3, body, and lists, including black underlined links on the Links line;
- RACI and lists rendered as native bullets at the 36pt step;
- the spacer rhythm and each spacer's plain style;
- warning shading when a warning is present;
- **every section** H2 shaded dark-green with white DM Serif 14pt;
- **every** table's cell padding, backgrounds, DM Sans 10pt text, and header-appropriate widths;
- content fidelity against the manifest; and
- zero surviving horizontal rules.

It deliberately does **not** enforce guide semantics such as task/objective coverage, consent wording, or the correct terminal section. Those content rules live in SKILL.md, the template references, and the contract validator. The visual verifier keeps the structural sanity checks that the document has the canonical title/top matter, at least one section band, and styled tables.

## Required build pipeline

Use `scripts/option4_guide_layout.py` (same four stages as research-plan):

1. `manifest` — parse the approved markdown into a style/content manifest (with a self-digest and contract binding).
2. Import the markdown into the confirmed Google Drive folder with the connected Docs importer. With `gws`, run `gws drive files create --upload guide.md --upload-content-type text/markdown` from the private working directory (gws only uploads files inside the current directory), with only the name, `application/vnd.google-apps.document`, and the folder ID in `--json`. Markdown import creates native headings, tables, and bullets.
3. `normalize` — bind imported content to the manifest, uppercase the band headings, delete each table's conversion header row, drop every horizontal rule, and reconcile the spacer paragraphs. Column-count agnostic; header presence is detected per table.
4. Re-fetch the raw Google Docs JSON.
5. `format` — generate the exact Option 4 Google Docs batch operations.
6. Apply those operations and re-fetch the document. Apply every batch (normalize and format) through a protected request body, in the route order of `source-and-delivery-safety.md` §2; with `gws`, use `send`, which applies a revision-bound batch file without a shell.
7. `verify` — validate content fidelity and every machine-checkable visual invariant (raises and exits 1 on any drift).
8. Export/render the Doc and visually inspect the opening page, an interior page, and the last page.

The batch files use the native Google Docs API request schema, bound to the snapshot's `revisionId`. They apply only through a route that sends them unchanged with `writeControl.requiredRevisionId`: a connector tool that takes native batch requests as a request-body parameter, or `gws` through `send`. A connector edit tool with its own simplified operation format or no revision binding cannot apply them. Checked on 2026-10-05, Runlayer's Google Workspace connector was the only connector available, and its `batch_update_doc` has both limits, so formatting currently runs on `gws` through `send`. Runlayer still works for creating (`import_to_google_doc`), reading (`readDocument`), and trashing (`update_drive_file`) the Doc, but `readDocument` omitted `revisionId`, so the snapshots for `normalize` and `format` come from `gws`. No personal template or private reference Doc is required, which is what makes the clean edited look reproducible for any researcher who opens the finished document.

## Hard completion gate

An approximate Option 4 is never a completed deliverable.

- **Strict Option 4 — Leadership:** block before creation when any required capability below is unavailable.
- **Option 4 — Leadership with pre-approved plain-native fallback (default):** when an Option 4-only capability is unavailable, switch before creation to plain native Google Docs, disclose the fallback, and never claim that Option 4 passed.

**Required on every delivery path:**

- a write-capable Google Docs integration;
- content, parent-folder, and effective-permission readback; and
- a PDF, thumbnail, or equivalent render for visual inspection.

If any shared capability is unavailable, block delivery on every path.

**Required only to claim Option 4:**

- raw document structure or equivalent indices;
- native batch formatting needed to apply the contract; and
- the bundled verifier.

Do not substitute a non-DM font, drop the section bands, or return after a structural-only check and call the result Option 4. A plain-native fallback is a distinct, labeled delivery path—not a downgraded Option 4 result.
