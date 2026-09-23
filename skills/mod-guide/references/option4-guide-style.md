# Option 4 — Leadership Visual Contract (Moderation Guide)

This is the visual source of truth for the **optional "leadership design" path** of `/mod-guide`. The machine-readable values live in [`option4-guide-style.json`](option4-guide-style.json); the formatter and verifier ([`../scripts/option4_guide_layout.py`](../scripts/option4_guide_layout.py)) consume that contract.

**This is not the default.** Per the mod-guide "Portable Google Docs contract," native Google Docs styling is the default deliverable, and this Option 4 leadership look is an opt-in variant a researcher chooses in Section 1. When chosen, it makes a finished moderation guide open in the same clean, edited leadership style that `/research-plan`'s Option 4 pipeline produces — so any researcher who opens the document sees one consistent visual system, not a raw import.

The visual language is shared with `/research-plan` Option 4. The `page`, `colors`, `typography`, `warning`, and `spacing` tokens are copied verbatim from that skill's contract; `derived_from` in the JSON points at the canonical origin. No private reference document is a runtime dependency.

## Structure-agnostic

The critical property of this contract: it is **structure-agnostic.** mod-guide now produces two structurally different documents, and the formatter styles by **element role inferred generically**, not by a fixed sequence of named semantic sections. It never assumes a particular section order, a fixed section list, a terminal section, or a fixed table shape.

The two guide shapes it supports today:

- **Interview / IDI** — a **two-tier header** (an all-caps study kicker line above the title, then `# Discussion Guide`, then an italic period line `*[Q1 · Month Year]*` below it); an **extended RACI / ownership block** (any `**Label:** …` bullets — Responsible, Accountable, Consulted, Contributor, External, Informed, Session Summaries, POC, …); Research Objectives; a body of **prose bullets with indented probes** (no question tables); and a guide that ends at a **Participants Log** (a 3-col table) or a Parking Lot — i.e. **a table can appear after Post-Session Debrief.**
- **Prototype / Usability** — a single breadcrumb `*UX Research | [Research Plan | Discussion Guide] | [Round N · Quarter Year]*`; a `# Study Title`; an optional bold subtitle; Session Flow Overview; Objectives & Research Questions; a Consent + Recording + Think-Aloud script; `#|Ask` and `#|Ask / Do` task tables under `### Flow N` sub-headings; optional Comparisons / Cross-Flow Recap; and vendor back-matter **Communication & Deliverables (+ Timeline)** after Post-Session Debrief for vendor runs.

Both shapes share a Parameter|Detail table, a Pre-Session Checklist (bullets), a Consent (Cue|Read-aloud) table, and a Post-Session Debrief (numbered list) — but the formatter recognizes those by their generic element role (a top-matter 2-col table, a bulleted list, a table, a numbered list), not by name.

## How roles are inferred

| Element role | How it is recognized | Styled as |
|---|---|---|
| **Title** | the first `# ` (Heading-1) in the document | DM Serif Display 26pt bold, dark green `#003D29` |
| **Breadcrumb / kicker** | a short non-heading line ABOVE the title (single breadcrumb or all-caps kicker) AND an italic period line immediately after the title (interview two-tier) | DM Serif Display 16pt gray `#666666` |
| **Phase subtitle** | a top-matter line that is fully bold (`**…**`) | DM Serif Display 14pt bold, dark green `#003D29` |
| **`Last updated` line** | a top-matter line beginning `Last updated:` | DM Sans 9pt italic gray `#666666` (`context_note`) |
| **RACI / ownership** | consecutive top-matter bullets `- **Label:** …` (any label set) | DM Sans 10pt native bullets |
| **TEST ARTIFACT warning** | a paragraph whose text is the exact warning copy | full-paragraph pale-yellow `#FFF2CC` shading, DM Sans 10pt bold `#6F4A00` |
| **Section band** | EVERY `## ` (Heading-2) | dark-green `#003D29` full-width band, white DM Serif Display 14pt bold, UPPERCASE |
| **Sub-phase heading** | EVERY `### ` (Heading-3, e.g. "Flow 1", "2.1") | DM Serif Display 12pt bold, dark green `#003D29` |
| **Table** | EVERY Markdown table, any column count, any position | Option 4 table styling (see below) |
| **List** | EVERY bulleted / numbered block, including indented probe sub-bullets | DM Sans 10pt native list, nesting preserved |
| **Body** | any other paragraph (goals, probes-to-use, "Don't" lines, blockquote reminders) | DM Sans 10pt black |

## Page and typography

- Pageless Google Docs editing mode with landscape-letter (792 × 612pt) export metadata. Landscape is mandatory: the 698.4pt tables do not fit portrait letter's 468pt text area.
- One-inch (72pt) margins on every side; 36pt header/footer margins.
- Google Docs derives `useCustomHeaderFooterMargins=true` from those margins. That field is output-only and must not be sent in `updateDocumentStyle`.
- The research-plan 20pt-black `heading` token is intentionally **unused**; the 14pt bands take its structural role.

Apply named paragraph styles before direct text styles — Google Docs clears direct font overrides when a named style lands afterward.

## Warning treatment (mock/demo only)

- Shade the entire warning paragraph pale yellow `#FFF2CC` (full-paragraph shading, not inline highlight); DM Sans 10pt bold text in `#6F4A00`.
- Use the exact copy from [`../../references/output-status-and-labeling-conventions.md`](../../references/output-status-and-labeling-conventions.md): `⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.`

## Section bands — the key difference from research-plan

Research-plan puts its section bands as rows *inside* one big overview table. A moderation guide has no single spine table — it has several small tables interleaved with headings — so the band treatment moves onto the **`##` heading paragraphs themselves**, for **every** `##` heading generically.

- Every `##` heading becomes a dark-green full-width band: DM Serif Display 14pt bold, white text, paragraph background `#003D29`, 20pt above / 6pt below, UPPERCASE label.
- **Primary render (this contract): a shaded native Heading 2 paragraph.** This preserves the document outline so a moderator can jump between sections mid-session. The band spans the 648pt paragraph text area — ~50pt narrower than the tables beneath it, because paragraph shading cannot overflow into the print margins the way the tables do. This is expected and acceptable.
- **Documented alternative (`band_render_alt`): a single-row two-cell 698.4pt table** — matches research-plan's exact band width but loses the outline. Recommended against for a facilitation guide.
- Dividers: the markdown `---` separators are dropped during normalize (target `native_horizontal_rules: 0`). The bands do the sectioning.

## Tables — generic geometry, one aligned outer edge

Every table — whatever its columns, wherever it sits — shares: 5pt cell padding, white body cells, DM Sans 10pt cell text, 100% table line spacing, and **total width 698.4pt** (every table's outer edge aligns down the page, with the intentional 50.4pt overflow into the print margins). The Markdown header row is a conversion header and is dropped on import (the first content row becomes the first visible row); header presence is detected per table by row count, so a table may or may not arrive with the header attached.

Geometry is inferred, not fixed per named kind:

- **Column widths** — the first column is narrow (90pt) when the first header cell is `#` (question / task tables), otherwise it uses the label width (144pt). The remaining width is split evenly across the other columns. Examples: `#|Ask` → `[90, 608.4]`; `Parameter|Detail` / `Cue|Read aloud` / `Time|Phase` → `[144, 554.4]`; a 3-col `Date & Time|Panelist Bio|Recording` → `[144, 277.2, 277.2]`.
- **Label-column background** — a 2-col table in the **top matter** (the Parameter|Detail dashboard) gets the gray `#D9D9D9` label column so it reads as an at-a-glance dashboard; **every in-section table** (consent, question/task, Session Flow Overview, Participants Log, Timeline, …) uses a white `#FFFFFF` label column.
- **First-column bold** — the first column renders bold when EVERY first cell in the source Markdown is fully bold (`**Study Type**`, `**Open**`, `**Q1**`); a table whose first column is not uniformly bold (e.g. a Participants Log's `Date & Time` values) renders it at normal weight. Inline emphasis from the source is honored either way.
- **N columns** — 2-col and 3-col+ tables are all supported (a 3-col Participants Log or a 3-col `Description | Owner | Date` Timeline).

**Borders** are the one value the base Option 4 contract does not define. Do not invent one — mirror whatever `../../research-plan/scripts/option4_layout.py` applies, using a single consistent thin neutral border across every table.

## What the verifier checks (VISUAL invariants only)

The verifier is a **visual gate**, not a semantic-structure gate. It checks: page geometry + margins; title / breadcrumb / phase-subtitle / H2-band / H3 / body / context-note font+size+color; RACI and lists rendered as native bullets; warning shading when a warning is present; **every** H2 shaded dark-green with white DM Serif 14pt; **every** table's cell padding, white body cells, DM Sans 10pt text, and column-count-appropriate widths; content fidelity against the manifest; and zero surviving horizontal rules.

It deliberately does **not**: require the guide to end at Post-Session Debrief, reject a table after the debrief, or enforce "tables contain only questions." Those content rules live in SKILL.md and the two template references, not in this visual pass. The verifier keeps only the general structural sanity checks that the document has a title, at least one H2 band, and styled tables.

## Required build pipeline

Use `scripts/option4_guide_layout.py` (same four stages as research-plan):

1. `manifest` — parse the approved markdown into a style/content manifest (with a self-digest and contract binding).
2. Import the markdown into the confirmed Google Drive folder with the connected Docs importer.
3. `normalize` — bind imported content to the manifest, uppercase the band headings, delete each table's conversion header row, and drop every horizontal rule. Column-count agnostic; header presence is detected per table.
4. Re-fetch the raw Google Docs JSON.
5. `format` — generate the exact Option 4 Google Docs batch operations.
6. Apply those operations and re-fetch the document.
7. `verify` — validate content fidelity and every machine-checkable visual invariant (raises and exits 1 on any drift).
8. Export/render the Doc and visually inspect the opening page, an interior page, and the last page.

The batch files use the native Google Docs API request schema, so they apply through the session's connected Docs integration (the MCP `batch_update_doc` tool, `gws`, etc.) — no personal template, `gws`/gohan, or custom auth is required, which is what makes the clean edited look reproducible for any researcher who opens the finished document.

## Hard completion gate

When the researcher has opted into this leadership variant, the guide is not complete when the formatting is approximate. Block completion instead of returning a downgraded layout when any of these are unavailable:

- a write-capable Google Docs integration;
- raw document structure or equivalent indices;
- native batch formatting needed to apply the contract;
- the bundled verifier;
- a PDF/thumbnail/render for visual inspection.

Do not substitute a non-DM font, drop the section bands, or return after a structural-only check and still call the result final. (This gate applies only to the opt-in leadership path; the portable native-Google-Docs default remains the mod-guide default and is unaffected.)
