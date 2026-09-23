# Mod-guide Option 4 (leadership design) tests

These tests protect the **optional "leadership design" path** for `/mod-guide` — the
STRUCTURE-AGNOSTIC formatter + verifier in
[`../scripts/option4_guide_layout.py`](../scripts/option4_guide_layout.py) that
reproduces `/research-plan`'s clean, edited Option 4 look for a moderation guide.
They are fully offline: no Google Docs API call is made. Every test builds a
synthetic raw-Docs JSON tree in Python and runs the same
parse / normalize / format / verify code paths the live pipeline uses.

## Run them

From the repository root, either:

```bash
python3 skills/mod-guide/tests/test_option4_guide_layout.py
```

or with pytest (optional — the file is runnable directly with `unittest`, so pytest
may be absent):

```bash
python3 -m pytest skills/mod-guide/tests/test_option4_guide_layout.py
```

Both run with only the Python standard library (Python 3). No network, no
credentials, no `gws`/gohan.

## Two fixtures — two guide shapes

mod-guide produces two structurally different documents, and the formatter must
handle both, so there are two fixtures. Each is an intentional **TEST ARTIFACT**,
never a real study, and every paragraph text is unique so the offline harness can
bind styling by exact text.

- [`fixtures/mock-interview-guide.md`](fixtures/mock-interview-guide.md) — an
  Interview / IDI guide. Exercises the **two-tier header** (all-caps kicker + `#`
  title + italic period line), the **extended RACI** block (Responsible /
  Accountable / Consulted / Contributor / External / Informed / Session
  Summaries), the `⚠️ TEST ARTIFACT` warning, a gray Parameter|Detail dashboard
  table, prose-bullet themes with **indented probe sub-bullets** (a nested list), a
  numbered Post-Session Debrief, and a **3-col Participants Log table AFTER the
  debrief** plus a Parking Lot.
- [`fixtures/mock-prototype-guide.md`](fixtures/mock-prototype-guide.md) — a
  vendor-run Prototype / Usability guide. Exercises a single breadcrumb, a bold
  phase subtitle, a `Last updated` line, a `Links:` run-in body line, **no**
  warning (the no-warning path), a Session Flow Overview `Time|Phase` table,
  `#|Ask / Do` task tables under `### Flow` **sub-phase** headings, and a **3-col
  `Description | Owner | Date` Timeline table in the vendor back-matter AFTER the
  debrief**.

## What the suite covers

- **Contract exactness** — `option4-guide-style.json` name, `structure_agnostic`
  flag, page geometry, colors, and the generic table tokens (total width,
  narrow-vs-label first-column widths, the `#` trigger, gray-vs-white label
  backgrounds). Confirms the old per-kind `tables.kinds` block is gone.
- **Generic column-width inference** — `table_column_widths()` returns
  `[90, 608.4]` for a `#` table, `[144, 554.4]` for a 2-col label table, and
  `[144, 277.2, 277.2]` for a 3-col table, each summing to 698.4.
- **Parsing both shapes** — the interview manifest (10 sections, 3 tables, two-tier
  header, seven RACI labels, nested probe list, study type) and the prototype
  manifest (8 sections, 7 tables, phase subtitle + context note + `Links:` body
  line, two `### Flow` sub-phases, a 3-col timeline).
- **No terminal / forbidden-section gate** — the parser now accepts a guide that
  does NOT end at Post-Session Debrief and one that carries a `Master Probe Bank`
  trailing section (those content rules moved to SKILL.md / the templates).
- **Manifest integrity** — a stale contract version or tampered content is rejected
  before normalize/format run, for both fixtures.
- **Inline parsing** — HTML-entity decoding, balanced link-URL parentheses, and
  UTF-16 offset math (needed for ☐ and en-dashes).
- **Normalize** — uppercases the band headings, deletes each table's conversion
  header row (one `deleteTableRow` per table, for a variable table count), drops
  native horizontal rules, and binds imported N-col cell content to the manifest (a
  tampered 3-col timeline cell is rejected).
- **Format request shape** — the batch includes every required operation family,
  uses PAGELESS 792×612, never sends `useCustomHeaderFooterMargins`, shades **every**
  H2 band dark green, and uses both the bullet and numbered list presets.
- **Verifier (visual only)** — accepts both fully styled docs (5 checks each) and
  the whole point of the rework: **it accepts a table AFTER the Post-Session
  Debrief** in both fixtures. It still rejects visual drift — a band that lost its
  shading, a label cell turned red, wrong table column widths, a debrief rendered
  as a non-list, and a surviving horizontal rule.
- **Pipeline surface** — `parse_markdown`, `build_normalize_requests`,
  `build_format_requests`, and `verify_document` are all callable.

## Known limitation

These tests validate the batch operations and the verifier against synthetic and
hand-styled Docs JSON. A real end-to-end run — importing a fixture to a live Google
Doc, applying the normalize and format batches through a write-capable Docs
integration, re-fetching, and running `verify` on the returned JSON, plus a PDF
render inspection — is still required before releasing changes to the live visual
pipeline, exactly as the research-plan suite's "Live Google Docs integration gate"
describes. The one value to confirm against the research-plan builder on that live
run is the table border color/weight (the base Option 4 contract does not define
it; mirror `../../research-plan/scripts/option4_layout.py`).
