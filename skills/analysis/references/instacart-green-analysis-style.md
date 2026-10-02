# Instacart Green — Analysis Deliverable Style

Use this reference whenever [`delivery-routing.md`](delivery-routing.md) selects
Instacart Green, including the Markdown fallback. Create a Google Doc only after
the analysis is approved, final QA has passed, and the destination is known.

## When this style applies

- **All researchers using the analysis skill:** Instacart Green is the analysis-specific default style. Apply it automatically and use the matching skeleton variant; do not ask the researcher to choose a style.
- **Explicit style override:** if the researcher asks for another supported style, use it instead. A format-only override retains Instacart Green structure and semantics.
- **Any environment without Google Docs tooling:** preserve this structure in Markdown or another supported format. Do not install or mandate a particular connector merely to reproduce the styling.

The bundled style specification and skeleton are the portable reference; no access to a private study document is required.

Colors come from the Instacart brand palette. Use DM Sans throughout when the target format supports it.

## Select exactly one structural variant

The variants share the visual system but not the decision language. Do not mix them.

### Variant A — single-session or n=1 evidence memo

Use for one participant/session. This is a directional evidence read, not a cross-participant synthesis.

1. **Applicable status label** — use the label rules in `delivery-routing.md`.
2. **Masthead** — breadcrumb → title → question/subtitle → author and date. No RACI.
3. **`## Executive Summary`** — a two-line brief, a clearly labelled participant-context block that is not a finding, then `Validation at a glance` and this table:

   | Validation priority | Research question / next step | Rationale | Evidence status |
   | --- | --- | --- | --- |
   | High / Medium / Low | [what to learn or test next] | [decision consequence, uncertainty, and feasibility] | [Participant-reported / Observed / Ambiguous / Not tested] |

4. **`## Findings`** — use the smallest defensible finding set; one narrow question normally produces one integrated finding rather than separate findings for each cue or quote. Each finding is a participant-bounded claim followed by four lines:
   - **`Analysis` —** what the evidence supports and what remains interpretive;
   - **`Confidence` —** the reasoned source-integrity, attribution, directness, within-case, cross-case, and transferability ratings;
   - **`Next research step` —** the question or activity that would validate or challenge it;
   - **`Quote` —** an exact quote attributed as `Participant P01`.
5. **`## Appendix`** — Method · Links · Limitations.
6. **Footer** — one italic provenance/status line.

Do **not** use P0/P1/P2, `Priority`, or `Recommendation` in this variant. Do not imply prevalence, saturation, or product prioritization from one session.

### Variant B — multi-session synthesis

Use only when evidence supports cross-participant synthesis and action prioritization.

1. **Applicable status label** — use the label rules in `delivery-routing.md`.
2. **Masthead** — breadcrumb → title → question/subtitle → author and date. No RACI.
3. **`## Executive Summary`** — a two-line brief, then `Priority at a glance` and this table:

   | Priority | Action | Confidence basis |
   | --- | --- | --- |
   | P0 | [highest-priority action] | [material confidence dimensions and limiting rationale] |
   | P1 | [next action] | [dimensions and rationale] |
   | P2 | [later action] | [dimensions and rationale] |
   | Guardrail | [optional hard do-not action] | — |

4. **`## Findings`** — each finding is a plain claim followed by four lines:
   - **`Analysis` —** why it was inferred;
   - **`Confidence` —** the reasoned confidence dimensions and the material constraint on the claim;
   - **`Recommendation` —** what to do;
   - **`Quote` —** an exact quote attributed as `Participant P##`.
5. **`## Appendix`** — Method · Links · Limitations.
6. **Footer** — one italic provenance/status line.

P0/P1/P2 appear only in the priority table. Do not scatter priority codes through findings.

### Participant identifiers are not priority codes

- Participant IDs are zero-padded and always written with a noun in prose or quote attribution: `Participant P01`, `Participant P02`.
- Priority codes are not zero-padded: `P0`, `P1`, `P2`. They appear only in the multi-session Priority column.
- `P01` means a participant; it never means priority one. `P1` means priority one; it never identifies a participant.

## Visual system

### Palette

| Token | Hex | Role |
| --- | --- | --- |
| **Kale** | `#003D29` | Title, section bands, table-header text, breadcrumb, subtitle, finding headings, appendix labels, footer |
| **Lime** | `#0AAD0A` | Author/date and positive status |
| **Ochre** | `#B45F06` | Finding run-in labels: `Analysis`, `Confidence`, `Next research step` or `Recommendation`, and `Quote` |
| **Carrot** | `#FF7009` | P1 flag and caution status in multi-session documents only |
| **Cashew** | `#FAF1E5` | Table-header fill |
| **Pomegranate** | `#BA0239` | P0 flag and negative status in multi-session documents only |
| **White** | `#FFFFFF` | Text on Kale bands and table body cells |
| **Body** | `#000000` | Default body text; quote text is italic `#333333` |

Keep Kale, Lime, and White dominant. Use accent colors only for the stated roles. Do not use Turmeric `#ECAA01`, blue, or gray as a decorative palette.

### Typography

| Element | Font | Size | Weight | Color |
| --- | --- | --- | --- | --- |
| Status label | DM Sans | 9 pt | bold | Pomegranate for `TEST RUN`/`SIMULATED DATA`; Carrot for `DRAFT REAL STUDY` |
| Breadcrumb | DM Sans | 8 pt | italic | Kale |
| Title | DM Sans | 18 pt | bold | Kale |
| Subtitle | DM Sans | 10 pt | regular | Kale |
| Author · date | DM Sans | 12 pt | bold | Lime |
| Section band | DM Sans | 12 pt | bold | White on Kale |
| Finding heading | DM Sans | 13 pt | bold | Kale |
| Body | DM Sans | 10 pt | regular | Black |
| Table header | DM Sans | 10 pt | bold | Kale on Cashew |
| Footer | DM Sans | 9 pt | italic | Kale |

## Fixed layout rules

- Executive Summary comes before Findings.
- Only `##` section headings receive Kale shading. Finding `###` headings remain unshaded.
- Add one white blank paragraph after the summary table so it does not touch the Findings band.
- Inside a finding, stack the four run-in lines tightly with no blank paragraph between them. Leave one blank paragraph between findings.
- The Appendix uses plain bold-Kale run-ins for Method, Links, and Limitations. Links are real hyperlinks when available; otherwise use explicit bracketed placeholders.
- Do not add a Bottom line section, per-finding Guardrail lines, shaded finding boxes, or a RACI block.
- Add comparison tables only for genuinely quantified, scannable evidence.

### Table styling

Use Cashew `#FAF1E5` with bold Kale text in the header row and white body cells. Keep the first column snug (about 80 pt) and content columns wider; target about 468 pt total width on portrait US Letter with 1-inch margins.

For the multi-session Priority table only: color P0 Pomegranate, P1 Carrot, P2 `#666666`, and Guardrail Kale. Use Lime for positive status and Pomegranate for at-risk status. The n=1 validation table uses no priority colors or priority codes.

## Thin section bands and line-spacing adapters

A section band is a Heading 2 paragraph with Kale shading and white, 12 pt, bold DM Sans text. Set spacing above and below to zero; Google Docs includes paragraph spacing in the shaded area.

The two supported adapters use different units for the same single-spacing result:

- **Custom MCP `batch_update_doc` adapter:** pass `line_spacing: 1`. That wrapper multiplies the value by 100 before calling Google Docs.
- **Raw Google Docs API or `gws` batchUpdate:** set `paragraphStyle.lineSpacing: 100`. The raw API expects a percentage.

Never pass `100` to the custom MCP wrapper—it can become stored `lineSpacing: 10000`. Never pass `1` to the raw API—it represents 1%, not single spacing. In the stored Google Doc JSON, successful single spacing is approximately `lineSpacing: 100`.

## Production workflow and interchangeable adapters

1. Route the deliverable and obtain any required external-write authorization with `delivery-routing.md`.
2. Copy only the appropriate variant from `instacart-green-analysis-skeleton.md` and replace every placeholder.
3. Preserve separate paragraphs for the four finding lines. Some Markdown importers merge consecutive non-blank lines; use blank source lines when needed, then remove only the resulting in-finding blank paragraphs after import.
4. Use whichever supported Docs adapter is actually available:
   - **Native Google Docs MCP:** import or create the document, inspect paragraphs/tables, apply one formatting batch where practical, and re-read the result. Where the MCP exposes the custom `batch_update_doc` wrapper, use its wrapper units.
   - **`gws` or raw Google Docs API:** create/insert content, send equivalent `documents.batchUpdate` requests, then read the document back. Use raw API units, including `lineSpacing: 100`.
5. Confirm the document is in the routed folder, then verify content and formatting: status label, title, table variant, hyperlinks, thin Kale bands, no stray shading, no RACI, and stored line spacing near 100.
6. Return the Google Doc link. If no Docs adapter is available, return the routed Markdown/local artifact and state that Google Docs formatting and placement were not verified.

Neither adapter is mandatory. Do not install tools, claim verification, or block the analysis because the preferred adapter is unavailable.
