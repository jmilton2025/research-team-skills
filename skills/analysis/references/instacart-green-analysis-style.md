# Instacart Green — Analysis Deliverable Style (DEFAULT)

**This is the default visual style AND structure for every `/analysis` deliverable in Jedida's environment.** Confirmed by Jedida on 2026-09-28 (structure finalized in the same session). Apply it automatically — do not ask which style to use, and do not fall back to the Mode A/B/C 2-column templates or Option 4 Leadership for an analysis unless the researcher explicitly asks.

Reference doc (the approved v2 look + structure): `Frozen Foods — Single-Session Read (Restructured v2)` →
https://docs.google.com/document/d/1epz6xfDE7TTa-3o66KQcpx-4Mp03rAl_-k_ZuBlqw_4/edit

Colors come from the `anthropic-skills:instacart-brand` skill; typography is DM Sans throughout.

---

## Palette (roles)

| Token | Hex | Role in an analysis doc |
|---|---|---|
| **Kale** | `#003D29` | Title; **section bands** (fill, white text on it); table-header text; breadcrumb; subtitle; finding sub-headings; appendix labels; footer |
| **Lime** | `#0AAD0A` | Author/date line; **positive status** ("Reliable", "Strong") |
| **Ochre** | `#B45F06` | **finding run-in labels** — `Analysis` / `Recommendation` / `Quote` (bold) |
| **Carrot** | `#FF7009` | **P1** priority flag; caution status |
| **Cashew** | `#FAF1E5` | **Table header row** fill |
| **Pomegranate** | `#BA0239` | **P0** priority flag; **negative status** ("At risk") |
| **White** | `#FFFFFF` | Text on Kale bands; table body cells |
| Body text | `#000000` | Default body; quote text uses `#333333` italic |

Keep to Kale + Lime + White as the dominant trio; Ochre / Carrot / Cashew / Pomegranate are accents used only where noted. **Turmeric `#ECAA01` is no longer used** (the old "Bottom line" callout was retired 2026-09-28). Do not introduce blues, grays-as-a-palette, or off-brand colors.

## Typography — DM Sans everywhere

| Element | Font | Size | Weight | Color |
|---|---|---|---|---|
| Breadcrumb (line 1) | DM Sans | 8 | italic | Kale |
| Title | DM Sans | 18 | bold | Kale |
| Subtitle | DM Sans | 10 | regular | Kale |
| Author · date | DM Sans | 12 | bold | Lime |
| Section band (H2) | DM Sans | 12 | bold | White (on Kale) |
| Body | DM Sans | 10 | regular | Black |
| Table header | DM Sans | 10 | bold | Kale (on Cashew) |
| Footer | DM Sans | 9 | italic | Kale |

## Structure (top → bottom) — this order is fixed

1. **Masthead** (four short paragraphs, no RACI): breadcrumb → title → subtitle (the question) → author·date. **No RACI block.**
2. **`## Executive Summary`** (thin Kale band) — comes FIRST. Inside it:
   - a **2-line brief** (what was done + the single headline read);
   - a `Priority at a glance` bold-Kale sub-label (give it `space_above ~12` so it's clearly separated from the brief);
   - the **Priority-at-a-Glance table** — `Priority · Action · Confidence`. This is the **only** place P0/P1/P2 appear.
3. **A white gap after the priority table** (insert a blank paragraph — the table butts against the next band otherwise).
4. **`## Findings`** (thin Kale band) — a section header exactly like Executive Summary, so it's obvious the findings have started.
5. **Each finding** = a `### ` sub-heading (Kale bold ~13pt, `space_above ~10`, NOT a shaded band) stating the finding as a plain claim, followed by **three tightly-stacked lines with NO blank line between them**:
   - **`Analysis` —** why we inferred it   (label Ochre `#B45F06` bold)
   - **`Recommendation` —** what to do   (label Ochre bold)
   - **`Quote` —** "verbatim" — P##   (label Ochre bold; quote text italic `#333333`)
   A blank line separates one finding from the next. **No P-codes in findings. No per-finding "Guardrail" line** (put a hard "do not" as a row in the priority table; fold genuine safety/severity caveats into Limitations, or a labelled Safety Flag if severity-relevant).
6. **`## Appendix`** (thin Kale band): `**Method**` (plain bold-Kale run-in, **no highlight box**) · `**Links**` (small DM Sans 9 italic Kale, "Links" bold — real hyperlinks where available, else `[bracketed]` placeholders) · `**Limitations**` (bold-Kale run-in).
7. **Footer** — one italic Kale line (provenance / status marker).

**No "Bottom line" section** — it was removed 2026-09-28.

## Tables

The **Priority-at-a-Glance table** is standard. Add another table only for a genuinely quantified, scannable comparison; otherwise findings are prose (Analysis/Recommendation/Quote), never tables.
- Table styling: header row fill **Cashew `#FAF1E5`** + **Kale bold** text; body cells white; label column snug (~80pt for a Priority column), content columns wider; total width ≈ 468pt (portrait letter, 1in margins).
- Priority column codes are colored: **P0 Pomegranate**, **P1 Carrot**, **P2 gray `#666666`**, **Guardrail Kale**. Any status cells: Lime (positive) / Pomegranate (at risk).

## CRITICAL — the section band (this is where it goes wrong)

A section band is an `## ` (HEADING_2) paragraph with **paragraph shading = Kale**, **white 12pt bold DM Sans** text. To keep it a **thin strip right behind the text** (not a tall block):

- `line_spacing: 1`  ← **NOT 100.** The connected `batch_update_doc` MCP tool multiplies this value by 100 to get the Google Docs API percentage. Passing `100` stores `10000` (100× line height) and inflates the band into a huge block. Pass **`1`** for normal single spacing.
- `space_above: 0`, `space_below: 0` — Google Docs paints paragraph shading **over the space above/below too**, so any spacing there becomes green padding. Zero it. (If you want a gap around the band, add `space_below` to the *preceding* non-shaded paragraph instead.)
- shading_color: `#003D29`; text: white `#FFFFFF`, DM Sans 12 bold.

**Finding-block spacing:** within a finding, the `Analysis` / `Recommendation` / `Quote` lines are consecutive paragraphs with **no blank line between them** (tight block); a blank line separates one finding from the next. Finding `### ` sub-headings are plain (not shaded), so give them `space_above ~10` for separation — that spacing is white, not green.

## How to produce it (native Google Docs MCP path — no gws, no CLI)

1. Generate the analysis markdown from the skeleton (`instacart-green-analysis-skeleton.md`).
2. `import_to_google_doc` (content lands in tab **`t.0`**).
3. `inspect_doc_structure(document_id, tab_id="t.0", detailed=true)` → paragraph indices + table positions.
4. `debug_table_structure(document_id, table_index=N)` for each table → per-cell ranges (cell text = `[cell_start+1, cell_end-1]`).
5. Build the batch with `scripts/style_instacart_green.py` (palette + op-builders, `line_spacing=1` baked in), or hand-build following the tables above.
6. `batch_update_doc` — one atomic batch. Styling only changes no text length, so all indices stay valid across the batch.
7. Verify: re-read a band paragraph's JSON (`readDocument format=json`) and confirm `lineSpacing` is ~100 (normal), not 10000; confirm shading + white text.

**Finding-block rule (critical — this broke once).** In Markdown, `Analysis` / `Recommendation` / `Quote` written on consecutive lines with no blank between them **merge into one paragraph** (they render as one run-on line with clipped bold). So write them with a blank line between each (the skeleton does), which imports them as separate paragraphs *plus* blank paragraphs. Then **delete the in-finding blank paragraphs** — the blank between the sub-heading and Analysis, between Analysis and Recommendation, and between Recommendation and Quote — so the three lines stack tightly. **Keep** the blank line between one finding and the next. Do the deletes highest-index-first (each delete shifts later indices down). Order that works cleanly: apply all styling first (with the blanks present), then delete the blanks in a second call — the styling follows the paragraphs.

**Only `## ` bands get green shading.** Finding `### ` sub-headings, Analysis/Recommendation/Quote lines, and everything else must have **no** `shading_color`. If a stray green highlight lands behind a finding, an op targeted the wrong index — re-check. The `## Findings` band is styled identically to `## Executive Summary` (thin: `line_spacing 1`, `space_above`/`space_below` 0). Never leave two blank paragraphs stacked before a band.

**Final deliverable is ALWAYS the Google Doc** in this style — even for a mock/test run (add the TEST ARTIFACT warning then), even when the self-critique/multi-agent checks are skipped. Never hand back Markdown as the final artifact; only the Drive destination is still confirmed.

**Environment gotchas:** `open`/`osascript` are blocked in the sandbox — give the researcher the doc link, don't auto-open. Confirm the Drive destination before creating the doc. For a mock/test run, still create it: prefix the title with `[TEST]`, keep the TEST ARTIFACT warning, and write to whichever folder the researcher confirms (the project folder is fine if they pick it).
