# Mod-guide Option 4 (leadership design) tests

These tests protect the **optional "leadership design" path** for `/mod-guide` — the
formatter+verifier in [`../scripts/option4_guide_layout.py`](../scripts/option4_guide_layout.py)
that reproduces `/research-plan`'s clean, edited Option 4 look for a moderation
guide. They are fully offline: no Google Docs API call is made. Every test builds
a synthetic raw-Docs JSON tree in Python and runs the same
parse / normalize / format / verify code paths the live pipeline uses.

## Run them

From the repository root, either:

```bash
python3 skills/mod-guide/tests/test_option4_guide_layout.py
```

or with pytest:

```bash
python3 -m pytest skills/mod-guide/tests/test_option4_guide_layout.py
```

Both run with only the Python standard library (Python 3). No network, no
credentials, no `gws`/gohan.

## What the suite covers

- **Contract exactness** — `option4-guide-style.json` name, page geometry, colors,
  the three table kinds' widths, and the gray-vs-white label-column split.
- **Contract self-check** — `load_contract()` raises if any table kind's column
  widths, total width, or intentional-overflow token are internally inconsistent.
- **Manifest parsing** — the fixture parses into 7 sections and 8 tables, the
  `document_meta` flags (test artifact, phase subtitle, stimulus phase, study
  type), the verbatim `⚠️ TEST ARTIFACT` copy, and the Core phase's silent-tagging
  bullets + three `### 2.x` sub-phases.
- **Guide-specific structural rules** — the parser rejects a guide that does not
  end at Post-Session Debrief and rejects a forbidden trailing section (Master
  Probe Bank / Bias Mitigation Checklist / Self-Critique Audit) inside the doc.
- **Manifest integrity** — a stale contract version or tampered content is
  rejected by `validate_manifest` before normalize/format run.
- **Inline parsing** — HTML-entity decoding, balanced link-URL parentheses, and
  UTF-16 offset math (needed because the content has ☐ and en-dashes).
- **Normalize** — uppercases the band headings, deletes each table's conversion
  header row (one `deleteTableRow` per table), and drops native horizontal rules,
  and it binds imported cell content to the manifest (a tampered cell is rejected).
- **Format request shape** — the batch includes every required operation family
  (`updateDocumentStyle`, `updateTableColumnProperties`, `updateTableCellStyle`,
  `createParagraphBullets`, `updateParagraphStyle`, `updateTextStyle`), uses
  PAGELESS 792×612, never sends `useCustomHeaderFooterMargins`, shades a band
  dark green, and uses both the bullet and numbered list presets.
- **Hard verifier** — accepts a fully styled doc (5 checks) and rejects visual
  drift: a band that lost its shading, and a parameters label cell turned red.
- **The two guide-specific verifier rules the task calls out:**
  - *tables contain only questions* — probe/watch-for text leaked into a question
    cell is rejected (cell content is bound exactly to the manifest label +
    read-aloud/question text);
  - *ends at Post-Session Debrief* — the debrief must be a native numbered list
    (rejected if rendered as a plain paragraph or a table) and no horizontal rule
    may survive anywhere in the document.
- **Pipeline surface** — `parse_markdown`, `build_normalize_requests`,
  `build_format_requests`, and `verify_document` are all callable.

## The fixture

[`fixtures/mock-moderation-guide.md`](fixtures/mock-moderation-guide.md) is an
intentional **TEST ARTIFACT** — a mock IDI moderation guide, not a real study. It
exercises every element type: breadcrumb, title, phase subtitle, `Last updated`
line, RACI, the `⚠️ TEST ARTIFACT` warning, the Parameters / Consent / Question
tables, the Pre-Session Checklist and Post-Session Debrief lists, silent-tagging
bullets, and the Core phase's `### 2.1 / 2.2 / 2.5` sub-phases. Tables hold only
questions / read-aloud lines; probes and watch-fors live in prose, per the
mod-guide hard rule.

## Known limitation

These tests validate the batch operations and the verifier against synthetic and
hand-styled Docs JSON. A real end-to-end run — importing the fixture to a live
Google Doc, applying the normalize and format batches through a write-capable Docs
integration, re-fetching, and running `verify` on the returned JSON, plus a PDF
render inspection — is still required before releasing changes to the live visual
pipeline, exactly as the research-plan suite's "Live Google Docs integration gate"
describes. The one value to confirm against the research-plan builder on that live
run is the table border color/weight (the base Option 4 contract does not define
it; mirror `../../research-plan/scripts/option4_layout.py`).
