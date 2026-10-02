# Option 4 — Leadership Visual Contract (Moderation Guide)

This is the visual source of truth for the default **Option 4 — Leadership** path of `/mod-guide`. The machine-readable values live in [`option4-guide-style.json`](option4-guide-style.json); the formatter and verifier ([`../scripts/option4_guide_layout.py`](../scripts/option4_guide_layout.py)) consume that contract.

**This is the default deliverable look.** It is applied by the bundled `option4_guide_layout.py` with no personal environment or private reference Doc. Plain-native Google Docs is an explicit choice or a pre-approved, disclosed fallback. The finished moderation guide uses the same clean leadership visual system as `/research-plan`, not a raw import.

The visual language is shared with `/research-plan` Option 4. The `page`, `colors`, `typography`, `warning`, and `spacing` tokens are copied verbatim from that skill's contract; `derived_from` in the JSON points at the canonical origin. No private reference document is a runtime dependency.

## Structure-agnostic

The critical property of this contract: it is **structure-agnostic.** mod-guide now produces two structurally different documents, and the formatter styles by **element role inferred generically**, not by a fixed sequence of named semantic sections. It never assumes a particular section order, a fixed section list, a terminal section, or a fixed table shape.

The two guide shapes it supports today:

- **Interview / IDI** — `# Moderation Guide`, then `## [Study Title]`; RACI/ownership; Parameter and Consent tables; Research Objectives; and thematic **prose bullets with indented probes**. It ends at Post-Session Debrief or an optional Parking Lot.
- **Prototype / Usability** — the same canonical title/top matter; Parameter and Session Flow tables; Introduction, task phases, comparisons, and recap as **bold-label read/do lists**; and optional vendor **Communication & Deliverables** back-matter.

Both shapes share a Parameter|Detail table, a Pre-Session Checklist, and a Post-Session Debrief. Consent appears once per format: an interview Cue|Read aloud table or the prototype Introduction list. The formatter recognizes element roles, not study-specific section names.

## How roles are inferred

| Element role | How it is recognized | Styled as |
|---|---|---|
| **Document title** | the required first heading `# Moderation Guide` | DM Serif Display 26pt bold, dark green `#003D29` |
| **Study title** | the immediately following `## [Study Title]`, treated as top matter rather than a section band | DM Serif Display 14pt bold, dark green `#003D29` |
| **`Last updated` line** | a top-matter line beginning `Last updated:` | DM Sans 9pt italic gray `#666666` (`context_note`) |
| **RACI / ownership** | consecutive top-matter bullets `- **Label:** …` (any label set) | DM Sans 10pt native bullets |
| **TEST ARTIFACT warning** | a paragraph whose text is the exact warning copy | full-paragraph pale-yellow `#FFF2CC` shading, DM Sans 10pt bold `#6F4A00` |
| **Section band** | every `## ` after the required Study Title top-matter line | dark-green `#003D29` full-width band, white DM Serif Display 14pt bold, UPPERCASE |
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
- Use the exact copy from [`../../../references/output-status-and-labeling-conventions.md`](../../../references/output-status-and-labeling-conventions.md): `⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.`

## Section bands — the key difference from research-plan

Research-plan puts its section bands as rows *inside* one big overview table. A moderation guide has no single spine table, so the band treatment moves onto each **section `##` heading after the required Study Title top-matter line**.

- Every section `##` after Study Title becomes a dark-green full-width band: DM Serif Display 14pt bold, white text, paragraph background `#003D29`, 20pt above / 6pt below, UPPERCASE label.
- **Primary render (this contract): a shaded native Heading 2 paragraph.** This preserves the document outline so a moderator can jump between sections mid-session. The band spans the 648pt paragraph text area — ~50pt narrower than the tables beneath it, because paragraph shading cannot overflow into the print margins the way the tables do. This is expected and acceptable.
- **Documented alternative (`band_render_alt`): a single-row two-cell 698.4pt table** — matches research-plan's exact band width but loses the outline. Recommended against for a facilitation guide.
- Dividers: the markdown `---` separators are dropped during normalize (target `native_horizontal_rules: 0`). The bands do the sectioning.

## Tables — generic geometry, one aligned outer edge

Every table — whatever its columns, wherever it sits — shares: 5pt cell padding, white body cells, DM Sans 10pt cell text, 100% table line spacing, and **total width 698.4pt** (every table's outer edge aligns down the page, with the intentional 50.4pt overflow into the print margins). The Markdown header row is a conversion header and is dropped on import (the first content row becomes the first visible row); header presence is detected per table by row count, so a table may or may not arrive with the header attached.

Geometry is inferred from each table's complete header:

- **Column widths** — `Phase|Time` → `[554.4, 144]`; `Parameter|Detail` and `Cue|Read aloud` → `[144, 554.4]`; a legacy first header cell of `#` → `[90, 608.4]`. For 3+ columns, the first label column is 144pt and the remainder is split evenly.
- **Label-column background** — the top-matter Parameter dashboard gets the gray `#D9D9D9` label column; in-section Consent and Session Flow tables use white body cells.
- **First-column bold** — the first column is bold only when every first-cell value is fully bold in the approved Markdown. Inline emphasis is otherwise preserved exactly.
- **N columns** — the formatter remains column-count agnostic even though the current templates use two-column tables.

**Borders** use the Google Docs default — the pipeline sends no border request at all (mirroring `/research-plan`'s Option 4 pipeline, which also sends none). Do not invent a border value. (Settled 2026-10-02 after two live builds: both verified clean with Docs-default borders.)

## What the verifier checks (VISUAL invariants only)

The verifier is a **visual gate**, not a semantic-structure gate. It checks: page geometry + margins; document title / study title / H2-band / H3 / body / context-note font+size+color; RACI and lists rendered as native bullets; warning shading when a warning is present; **every section** H2 shaded dark-green with white DM Serif 14pt; **every** table's cell padding, white body cells, DM Sans 10pt text, and header-appropriate widths; content fidelity against the manifest; and zero surviving horizontal rules.

It deliberately does **not** enforce guide semantics such as task/objective coverage, consent wording, or the correct terminal section. Those content rules live in SKILL.md, the template references, and the contract validator. The visual verifier keeps the structural sanity checks that the document has the canonical title/top matter, at least one section band, and styled tables.

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
