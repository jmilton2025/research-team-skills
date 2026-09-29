# Analysis Delivery Routing

Use this decision contract before creating, uploading, or styling an analysis artifact. Requesting analysis with this skill selects the team default below; Google Doc creation still waits for analytic approval, final QA, and a confirmed destination.

## Decision matrix

| Scenario | Default completed deliverable | Google Doc creation rule | Style rule | If Google Docs is unavailable |
| --- | --- | --- | --- | --- |
| **Any researcher · real study** | One Instacart Green Google Doc. | After analysis approval and final QA, create and verify one Doc in the confirmed project folder. If the destination is unknown or ambiguous, ask once for it and wait. Do not ask for output-format or style confirmation. | Apply Instacart Green automatically. | Return the complete analysis in Markdown, preserve the Instacart Green structure as far as Markdown allows, and state that Drive placement, native Docs formatting, and link verification remain incomplete. |
| **Any researcher · skill test or mock run** | One clearly labelled Instacart Green Google Doc. | After analysis approval and final QA, create and verify one test Doc only in a confirmed test/project folder. If the destination is unknown or ambiguous, ask once for it and wait; do not choose a Drive location. | Apply Instacart Green automatically and retain the required test/provenance label. | Return the complete, correctly labelled test artifact in Markdown and state the Docs-specific limitation. Missing Docs tooling is a delivery limitation, not an analysis failure. |
| **Explicit researcher override** | Change only the requested dimension: a format-only override keeps Instacart Green; a style-only override keeps one Google Doc. If both are specified, change both. | Follow the requested format. For any external write, ask once for a destination that is unknown or ambiguous, then wait. | Use an explicitly requested style; otherwise retain Instacart Green. | Return the complete content in an available format and identify only the unavailable format-specific verification. |
| **Google Docs or GWS unavailable** | A complete Markdown artifact, not a partial preview. | Do not claim a Doc was created. Do not install or mandate a connector without separate authorization. | Preserve the selected structure and style semantics as far as Markdown allows. | Provide the artifact plus a short statement of what remains: Drive placement, native Docs formatting, and link verification. |

The default route authorizes one completed Google Doc after the analysis and final-QA gates pass; it does not authorize early drafts, extra copies, or writing to an inferred destination. Before retrying after an ambiguous creation result, check the confirmed folder for the Doc to avoid duplicates. An explicit researcher request for a different format or style overrides the default.

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

After the route's approval, QA, and destination requirements are met, use the available supported adapter:

- native Google Docs MCP; or
- `gws`/raw Google Docs API.

Neither is universally required. Follow `instacart-green-analysis-style.md` for equivalent formatting operations, adapter-specific line-spacing units, and verification. If no adapter is available, use the fallback in the matrix and report the exact limitation.

## Offline content and render contract

For a structured render or a skill regression test, serialize the approved content into a JSON packet using `../tests/fixtures/single_session_mock.json` as the n=1 example, then run the stdlib-only validator before any external creation:

```bash
python3 skills/analysis/scripts/analysis_contract.py validate PACKET.json
python3 skills/analysis/scripts/analysis_contract.py manifest PACKET.json --backend custom_mcp --tab-id t.0
```

Use `--backend docs_api` for `gws` or raw Google Docs API rendering. The manifest records the adapter-specific spacing and tab ID; it does not call a network service, authorize delivery, or replace evidence QA. A local `TEST RUN` may truthfully use an empty `links` list with a `links_note` instead of fabricated URLs.
