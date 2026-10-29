# Analysis Delivery Routing

These are the default delivery rules for the `analysis` skill only. They do not set delivery defaults for `research-plan`, `mod-guide`, `report`, or any other skill; each skill owns its own delivery default. Requesting analysis with this skill selects the analysis delivery default below. Deck creation still waits for analytic approval, final QA, and a confirmed destination.

## Decision matrix

The finished analysis is a **Google Slides deck built from Instacart's official brand template**, following [`../../../references/brand-deck/README.md`](../../../references/brand-deck/README.md). The Instacart Green Google Doc described in `instacart-green-analysis-style.md` remains available only when the researcher asks for a Doc.

| Scenario | Default completed deliverable | Creation rule | Style rule | If Slides is unavailable |
| --- | --- | --- | --- | --- |
| **Any researcher · real study** | One brand-template analysis deck. | After analysis approval and final QA, copy the template into the confirmed project folder, build the deck from approved content only, and verify every slide. If the destination is unknown or ambiguous, ask once and wait. Don't ask about format or style. | The brand template's own styles, kept by filling its text boxes in place. | Return the complete analysis in Markdown and state that the deck, Drive placement, and slide verification remain incomplete, naming the missing tool or access. |
| **Any researcher · skill test or mock run** | Labelled Markdown. A test deck only when the tester asks for one. | A requested test deck goes only to a confirmed test folder, with the test label on the title and closing slides. | Brand template, plus the required test/provenance label. | Return the complete, correctly labelled Markdown. Missing Slides tooling is a delivery limitation, not an analysis failure. |
| **Explicit researcher override** | Exactly what was asked for: an Instacart Green Google Doc, or Markdown only. | Follow the requested format. For any external write, ask once for an unknown or ambiguous destination, then wait. | Instacart Green for a Doc; the brand template for a deck. | Return the complete content in an available format and name the format-specific step that couldn't run. |

The default route authorizes one completed deck after the analysis and final-QA gates pass. It doesn't authorize early drafts, extra copies, or writing to an inferred destination. Before retrying after an ambiguous copy or creation result, check the confirmed folder for the deck, to avoid duplicates.

### What goes on the analysis deck

- **n=1 memo or n=2–4 pilot signals:** Title → Method & sample → Research questions answered (when a question or plan exists) → one Finding slide per evidence-backed observation or signal, in participant-specific or signal language → Next research steps on the next-steps slide (validation priorities, never product work) → Closing. No BLUF recommendations slide, no P0/P1/P2, and no recommendations table.
- **n≥5:** Title → Bottom line → Method & sample → Research questions answered → Findings (claim headline; evidence with count and percentage; "But consider" in the evidence box) → Task success & severity (usability overlay only) → Insights → recommendations (only when the multi-session evidence supports prioritization) → Next steps → Appendix (codebook or crosswalk) → Closing.
- Every quote on a slide is verbatim from the evidence ledger, and every number uses the count-plus-percentage format.

## Status labels are distinct

Place applicable labels above the masthead and repeat their meaning in the footer or Method note. Do not use one as a synonym for another.

| Label | Use when | Do not imply |
| --- | --- | --- |
| **TEST RUN** | The artifact's primary purpose is to evaluate the skill, workflow, prompts, or renderer. | It does not mean the input is synthetic. If authorized real input was used, say so in Method without presenting the test as a completed real-study deliverable. |
| **SIMULATED DATA** | Participant data, quotes, sessions, or results were generated or fictional. | It is not real participant evidence and must not support product or organizational decisions. |
| **DRAFT REAL STUDY** | The artifact analyzes authorized real-study data but is still under researcher review and has not been approved as final. | It is not a skill test and it is not simulated. Remove or replace the label only when the study's approval process supports doing so. |

Labels may be combined only when both facts are independently true. The clearest valid combination is `TEST RUN` + `SIMULATED DATA`. Avoid combining `TEST RUN` with `DRAFT REAL STUDY`; choose the artifact's primary purpose and state input provenance explicitly in Method.

## Output structure routing

- **One participant/session:** use the single-session/n=1 variant in `instacart-green-analysis-skeleton.md`. It keeps participant context separate from findings and uses `Validation priority · Research question / next step · Rationale · Evidence status` plus `Analysis · Confidence · Next research step · Quote`. Validation priority ranks the need for more evidence, never product work. It never uses P0/P1/P2 or Recommendation language.
- **Multiple sessions with adequate cross-participant evidence:** use the multi-session variant. It uses `Priority · Action · Confidence basis` and `Analysis · Confidence · Recommendation · Quote`.
- **Multiple sessions without adequate evidence for prioritization:** use the n=1 evidence language or a descriptive cross-session memo, and explain the limitation. Do not manufacture priority codes to fill a template.

Participant IDs such as `Participant P01` are evidence-source identifiers. Priority codes `P0`, `P1`, and `P2` are action-ranking labels used only in a supported multi-session priority table.

## Adapter routing

After the route's approval, QA, and destination requirements are met:

- **Deck (default):** use the connected Google Slides / Google Workspace tools and the build and verify steps in `../../../references/brand-deck/README.md`.
- **Instacart Green Doc (on request):** use the native Google Docs MCP or `gws`/raw Google Docs API, following `instacart-green-analysis-style.md` for formatting operations, adapter-specific line-spacing units, and verification.

If no adapter is available, use the fallback in the matrix and report the exact limitation.

## Offline content and render contract

For a structured render or a skill regression test, serialize the approved content into a JSON packet using `../tests/fixtures/single_session_mock.json` as the n=1 example. That public fixture is fully simulated and carries both `TEST RUN` and `SIMULATED DATA`; it contains no actual participant evidence. Run the stdlib-only regression suite and validator before any external creation:

```bash
python3 skills/analysis/tests/test_analysis_contract.py
python3 skills/analysis/scripts/analysis_contract.py validate PACKET.json
python3 skills/analysis/scripts/analysis_contract.py manifest PACKET.json --backend custom_mcp --tab-id t.0
```

Use `--backend docs_api` for `gws` or raw Google Docs API rendering. The manifest records the adapter-specific spacing and tab ID; it does not call a network service, authorize delivery, or replace evidence QA. A local `TEST RUN` may truthfully use an empty `links` list with a `links_note` instead of fabricated URLs.
