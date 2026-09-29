<!--
SKELETON for an /analysis deliverable in the Instacart Green style (v2 — confirmed by Jedida 2026-09-28).
Fill [BRACKETS] with real content. Keep this exact shape and order:
- masthead = 4 plain lines (breadcrumb, title, subtitle, author) — NO RACI
- ## Executive Summary FIRST: a 2-line brief, then the "Priority at a glance" table INSIDE it
- ## Findings band (a section header like Executive Summary), then each finding as a ### sub-heading
- each finding = sub-heading + THREE lines, each its OWN paragraph: Analysis / Recommendation / Quote.
  In THIS markdown they are written with a blank line between them (below) — Markdown MERGES consecutive
  non-blank lines into one paragraph, which is wrong. The produce step then DELETES the in-finding blank
  paragraphs so the three lines stack tightly (see the contract's "How to produce it"). Labels render
  ochre #B45F06 bold; a blank line stays only BETWEEN findings.
- P-codes (P0/P1/P2) live ONLY in the Priority-at-a-glance table — never scatter them through the findings.
- NO "Bottom line" section. NO per-finding "Guardrail" line (a hard "do not" can be one row in the
  priority table; genuine safety/severity caveats go in Limitations or a labelled Safety Flag).
- ## Appendix: Method (plain, no highlight box) · Links · Limitations · italic footer.
Then style via scripts/style_instacart_green.py (see instacart-green-analysis-style.md).
-->

Research  |  [Study name] · [Deliverable type]  |  [Quarter Year]

[Study Title] ([N / method])

[One-line subtitle — the question this synthesis answers]

[Researcher name]  ·  [Month Year]

## Executive Summary

[Two lines: what was done + the single headline read.]

Priority at a glance

| Priority | Action | Confidence |
| --- | --- | --- |
| P0 | [highest-priority action] | [High / Medium / Low] |
| P1 | [action] | [confidence] |
| P2 | [action] | [confidence] |
| Guardrail | [an optional hard "do NOT" row] | — |

## Findings

### 1 · [Finding stated as a plain claim]

**Analysis** — [why we inferred it — the evidence/logic]

**Recommendation** — [what to do about it]

**Quote** — "[verbatim]" — [P##]

### 2 · [Next finding as a plain claim]

**Analysis** — […]

**Recommendation** — […]

**Quote** — "[verbatim]" — [P##]

## Appendix

**Method** — [the methodology used for this analysis].

**Links** — [Project folder] · [Session / transcript] · [Screener]

**Limitations** — [N, scope, biases; fold any safety/severity scope caveat here].

[Provenance / status line — italic footer.]
