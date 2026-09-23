# Option 4 — Leadership Visual Contract (Moderation Guide)

This is the visual source of truth for the **optional "leadership design" path** of `/mod-guide`. The machine-readable values live in [`option4-guide-style.json`](option4-guide-style.json); the formatter and verifier ([`../scripts/option4_guide_layout.py`](../scripts/option4_guide_layout.py)) consume that contract.

**This is not the default.** Per the mod-guide "Portable Google Docs contract," native Google Docs styling is the default deliverable, and this Option 4 leadership look is an opt-in variant a researcher chooses in Section 1. When chosen, it makes a finished moderation guide open in the same clean, edited leadership style that `/research-plan`'s Option 4 pipeline produces — so any researcher who opens the document sees one consistent visual system, not a raw import.

The visual language is shared with `/research-plan` Option 4. The `page`, `colors`, `typography`, `warning`, and `spacing` tokens are copied verbatim from that skill's contract; only the document `structure` and table geometry are moderation-guide-specific. `derived_from` in the JSON points at the canonical origin. No private reference document is a runtime dependency.

## Required hierarchy

A finished guide has this order (it MUST end at Post-Session Debrief):

1. Breadcrumb — `UX Research | Moderation Guide | [Quarter Year]`.
2. Study title.
3. Optional bold phase subtitle.
4. `Last updated: [Month Year]` metadata line.
5. Four RACI bullet paragraphs.
6. Full-width `⚠️ TEST ARTIFACT` warning — mock/demo runs only.
7. Parameters table (Study Type / Duration / Format / Participants / Goal).
8. **Pre-Session Checklist** section band → ☐ bullet list (not a table).
9. **Consent + Recording Script — Read Verbatim** section band → Cue / Read-aloud table.
10. One **Phase** section band per phase (Warm-Up → Core → optional Stimulus → Wrap-Up). Core carries silent-tagging ☐ bullets and `### 2.x` sub-phases, each with prose above a question table.
11. **Post-Session Debrief** section band → numbered list (not a table). Terminal element.

Probes, watch-fors, "don'ts," tagging guidance, and methodology rationale live in **prose around the tables** — never inside table cells. Tables contain only the short label and the exact words to read or ask aloud.

## Page and typography

- Pageless Google Docs editing mode with landscape-letter (792 × 612pt) export metadata. Landscape is mandatory: the 698.4pt tables do not fit portrait letter's 468pt text area.
- One-inch (72pt) margins on every side; 36pt header/footer margins.
- Google Docs derives `useCustomHeaderFooterMargins=true` from those margins. That field is output-only and must not be sent in `updateDocumentStyle`.
- Breadcrumb: **DM Serif Display, 16pt, bold, gray `#666666`**.
- Title: **DM Serif Display, 26pt, bold, dark green `#003D29`**.
- Phase subtitle *(new)*: **DM Serif Display, 14pt, bold, dark green `#003D29`** — dark-green-on-white, distinct from the white-on-green band.
- `Last updated` line: **DM Sans, 9pt, italic, gray `#666666`** (the `context_note` token — this is metadata).
- Section bands: **DM Serif Display, 14pt, bold, white** on dark green `#003D29`.
- Sub-phase headings (`2.1`/`2.2`/`2.5`) *(new)*: **DM Serif Display, 12pt, bold, dark green `#003D29`** — green-on-white so it never reads as a band. Alt: DM Sans 11pt bold `#003D29`.
- Body, RACI, list items, and all table text: **DM Sans, 10pt, black**.
- The research-plan 20pt-black `heading` token is intentionally **unused**; the 14pt bands take its structural role.

Apply named paragraph styles before direct text styles — Google Docs clears direct font overrides when a named style lands afterward.

## Warning treatment (mock/demo only)

- Shade the entire warning paragraph pale yellow `#FFF2CC` (full-paragraph shading, not inline highlight).
- DM Sans 10pt bold text in `#6F4A00`.
- Use the exact copy from [`../../references/output-status-and-labeling-conventions.md`](../../references/output-status-and-labeling-conventions.md): `⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.`

## Section bands — the key difference from research-plan

Research-plan puts its section bands as rows *inside* one big overview table. A moderation guide has no single spine table — it has several small tables interleaved with phase headings — so the band treatment moves onto the **`##` phase-heading paragraphs themselves.**

- Every `##` heading becomes a dark-green full-width band: DM Serif Display 14pt bold, white text, paragraph background `#003D29`, 20pt above / 6pt below, UPPERCASE label.
- **Primary render (this contract): a shaded native Heading 2 paragraph.** This preserves the document outline so a moderator can jump between phases mid-session. Same shading mechanism as the warning paragraph, green instead of yellow. The band spans the 648pt paragraph text area — ~50pt narrower than the tables beneath it, because paragraph shading cannot overflow into the print margins the way the tables do. This is expected and acceptable; do not force a paragraph to 698.4pt.
- **Documented alternative (`band_render_alt`): a single-row two-cell 698.4pt table** (144 + 554.4, both cells dark green). This reproduces research-plan's exact band width and margin overflow, but the phase heading is no longer a native heading, so the document loses its outline. Recommended against for a facilitation guide.
- Dividers: the markdown `---` separators are dropped during normalize (target `native_horizontal_rules: 0`). The bands do the sectioning; a rule plus a band would double-separate.

## Tables — three kinds, one aligned outer edge

All three kinds share: 2 columns, 5pt cell padding, white body cells, DM Sans 10pt cell text, 100% table line spacing, **total width 698.4pt** (every table's outer edge aligns down the page), and the intentional 50.4pt overflow into the print margins — do not normalize to 648pt. Header rows are removed on import; the first content row is the first visible row.

| Kind | Where | Column widths (pt) | Label column background |
|---|---|---|---|
| **Parameters** | top of guide (Study Type … Goal) | 144 / 554.4 | gray `#D9D9D9` — reads as an at-a-glance dashboard |
| **Consent** | Consent + Recording Script (Cue / Read-aloud) | 144 / 554.4 | white `#FFFFFF` — reads as clean content |
| **Question** | every phase & sub-phase (`#` / Ask) | 90 / 608.4 | white `#FFFFFF` — narrow `#` column, wide Ask column |

Both label-column looks (gray dashboard, white content) are native Option 4 treatments assigned by function, not a divergence. The narrow 90pt `#` column fits the longest question labels (`Q12 follow-up`, `If hesitant`); use the 96pt fallback if any label wraps.

**Borders** are the one value the base Option 4 contract does not define. Do not invent one — mirror whatever `../../research-plan/scripts/option4_layout.py` applies, using a single consistent thin neutral border across all three kinds. This is the sole value to confirm against the research-plan builder.

## Required build pipeline

Use `scripts/option4_guide_layout.py` (same four stages as research-plan):

1. `manifest` — parse the approved markdown into a style/content manifest (with a self-digest and contract binding).
2. Import the markdown into the confirmed Google Drive folder with the connected Docs importer.
3. `normalize` — bind imported content to the manifest, uppercase the band headings, delete each table's conversion header row, and drop every horizontal rule.
4. Re-fetch the raw Google Docs JSON.
5. `format` — generate the exact Option 4 Google Docs batch operations.
6. Apply those operations and re-fetch the document.
7. `verify` — validate content and every machine-checkable visual invariant (raises and exits 1 on any drift).
8. Export/render the Doc and visually inspect the opening page, the Core page, and the last page.

The command accepts `--help` for exact arguments. The batch files use the native Google Docs API request schema, so they apply through the session's connected Docs integration (the MCP `batch_update_doc` tool, `gws`, etc.) — no personal template, `gws`/gohan, or custom auth is required, which is exactly what makes the clean edited look reproducible for any researcher who opens the finished document.

## Hard completion gate

When the researcher has opted into this leadership variant, the guide is not complete when the formatting is approximate. Block completion instead of returning a downgraded layout when any of these are unavailable:

- a write-capable Google Docs integration;
- raw document structure or equivalent indices;
- native batch formatting needed to apply the contract;
- the bundled verifier;
- a PDF/thumbnail/render for visual inspection.

Do not substitute a non-DM font, drop the section bands, leak probes/watch-fors into table cells, add a table after Post-Session Debrief, or return after a structural-only check and still call the result final. (This gate applies only to the opt-in leadership path; the portable native-Google-Docs default remains the mod-guide default and is unaffected.)
