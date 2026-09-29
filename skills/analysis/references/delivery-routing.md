# Analysis Delivery Routing

Use this decision contract before creating, uploading, or styling an analysis artifact. Delivery authorization, evidence status, and visual style are separate decisions.

## Decision matrix

| Scenario | Default working deliverable | When an external Google Doc may be created | Style rule | If Google Docs is unavailable |
| --- | --- | --- | --- | --- |
| **Jedida · real study** | Draft in chat/Markdown until the requested delivery is clear. | Create a Google Doc when Jedida explicitly requests it or the current project context explicitly requires a Google Doc. Use the confirmed project folder; if the destination is ambiguous, confirm it before creation. | Instacart Green is auto-locked; do not ask for a style choice. | Return a complete Markdown/local artifact and say that Docs placement and visual formatting remain unverified. |
| **Jedida · skill test or mock run** | A clearly labelled test artifact in chat/Markdown. Keep it out of shared Drive by default. | **Only after both** (1) Jedida explicitly requests a Google Doc for the test and (2) the destination folder is confirmed in the current task. | If a Doc is authorized, Instacart Green is auto-locked. | Keep the test local/in chat; do not treat missing Docs tooling as a test failure unless Docs delivery is what the test is evaluating. |
| **Other researcher · real study or test** | Use the requested format; otherwise provide a neutral accessible chat/Markdown draft and ask once only if output format materially affects the result. | Create a Google Doc only when the researcher requests one and its destination is confirmed. | Use the researcher's requested style. If none is stated and style matters, offer a concise choice; do not assume Instacart Green. | Return the complete content in a supported format and identify only the missing Docs-specific verification. |
| **Any user · Docs requested but unavailable** | Produce the complete, correctly labelled analysis in Markdown or another available format. | Do not claim a Doc was created. Do not install or mandate a connector without separate authorization. | Preserve the selected structure and style semantics as far as the available format allows. | Provide the artifact plus a short statement of what remains: Drive placement, native Docs formatting, and link verification. |

An explicit style preference does not authorize an external write. A known folder does not by itself authorize creating a test document. For a test run, both the request and folder confirmation are required.

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

After Google Doc creation is authorized, use the available supported adapter:

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
