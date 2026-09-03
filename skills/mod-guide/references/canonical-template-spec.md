# Forest-Green Mod-Guide Template Spec (Fallback)

> **Status:** This is the **fallback** mod-guide styler, applied only when a researcher explicitly picks "Jedida's mod-guide style (forest green)" in Step 3. The **default** mod-guide styler is **Jedida Reporting (navy/blue)** — promoted to default on 2026-05-20 — at `~/.claude/skills/jedida-reporting/scripts/apply_jedida_reporting.py`. The forest-green values below remain locked and valid; they just no longer represent the default style. (Filename kept as `canonical-template-spec.md` because `SKILL.md`, `apply_canonical_template.py`, and `apply_custom_template.py` reference this path.)

**Source-of-truth reference doc:** `18Q9V4th9BwwNtlLXSncmMpiN591XTV1RzCUAyxym7wI`
([open in Google Docs](https://docs.google.com/document/d/18Q9V4th9BwwNtlLXSncmMpiN591XTV1RzCUAyxym7wI/edit))

This is the locked visual spec that `scripts/apply_canonical_template.py` applies for the forest-green fallback. It was extracted from the reference doc above and locked in on 2026-05-05 after a successful visual match against the mock mod guide at `1QbhwoDgbOf4ixPy9_rkH-OF4snLp0d5kJ5NleGMuS58`.

This doc is **documentation only** — not executable. The values below are mirrored in `scripts/apply_canonical_template.py`.

---

## Page setup

| Property | Value |
|---|---|
| Page size | 612 pt × 792 pt (US Letter, portrait) |
| Margins | 72 pt all sides (top, bottom, left, right) |

---

## Body text — `NORMAL_TEXT`

| Property | Value |
|---|---|
| Font | DM Sans |
| Size | 10 pt |
| Color | `#161416` |
| Line spacing | 115 |
| Space below | 4 pt |

---

## Headings — DM Serif Display, color `#2D4A3E`

| Style | Size | Bold | Notes |
|---|---|---|---|
| `TITLE` / `HEADING_1` | 26 pt | bold | Main doc title |
| `HEADING_2` | 16 pt | **non-bold** | `lineSpacing=110`, `spaceAbove=36pt`, `spaceBelow=12pt` |
| `HEADING_3` | 14 pt | bold | |
| `HEADING_4` | 12 pt | bold | |

---

## Special first-line paragraphs

| Element | Font | Size | Style | Color |
|---|---|---|---|---|
| Breadcrumb (first `NORMAL_TEXT` paragraph with pipes, e.g. `*UX Research \| Mod Guide \| Q2 2026*`) | DM Sans | 10 pt | italic | `#2D4A3E` |
| "Last updated: …" line | DM Sans | 10 pt | regular | `#666666` |

---

## Tables (2-column label/content)

| Property | Value |
|---|---|
| Col 0 width | 96 pt (FIXED_WIDTH) |
| Col 1 width | 715.5 pt (FIXED_WIDTH) |
| Borders (all 4 sides) | 0.5 pt SOLID `#C7C7C7` |
| Padding (all 4 sides) | 8 pt |
| `contentAlignment` | TOP (note: API default; setting it doesn't always persist on read-back, but renders TOP visually — set anyway) |

### Header row (row 0)

| Property | Value |
|---|---|
| Background | `#2D4A3E` |
| Text | DM Sans 10 pt **bold** `#FFFFFF` |

### Body rows — col 0 (label)

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | DM Sans 10 pt **bold** `#2D4A3E` |

### Body rows — col 1 (content)

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | DM Sans 10 pt regular `#161416` |

---

## Bullets

Preset: `BULLET_DISC_CIRCLE_SQUARE` (●  →  ○  →  ■)

---

## Run cleanup (the smoking gun)

When md2doc imports markdown with `<br>`, some runs end up with `baselineOffset = SUBSCRIPT`. This is the #1 cause of "looks visually different from the reference even though everything else matches."

**Fix:** explicitly set `baselineOffset = NONE` on every run. The styler script does this in its first phase.

---

## Color palette

| Token | Hex |
|---|---|
| Brand green | `#2D4A3E` |
| Body black | `#161416` |
| Muted gray (secondary text, "Last updated") | `#666666` |
| Table border | `#C7C7C7` |
| Name chip background | `#EEF1EE` |
| Hyperlink blue | `#1155CC` |
| White (header text, body cell bg) | `#FFFFFF` |
