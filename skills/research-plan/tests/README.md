# Research-plan contract tests

These tests protect the adaptive content contract and the exact **Option 4 — Leadership** Google Docs output contract.

## RED baseline captured

The retired contract explicitly required a “portable Leadership layout,” a standard font, one table, no custom palette, and no styling script. The baseline agent complied with those instructions and produced a structurally valid Google Doc that did **not** match the approved Option 4 reference: wrong typography, missing leadership timeline, generic table treatment, and noncanonical section bands. That observed failure is the reason the exact executable contract and no-downgrade gate exist.

## Run both regression suites

From the repository root:

```bash
python3 skills/research-plan/tests/validate_contract.py
python3 skills/research-plan/tests/test_option4_layout.py
```

`validate_contract.py` checks:

- agreement across `SKILL.md`, content rules, visual rules, README, and fixture;
- the four overview sections and their order;
- core versus conditional Project Details fields;
- the separate five-row leadership timeline;
- the exact DM Serif Display / DM Sans, color, geometry, table-width, and section-band requirements;
- destination confirmation before document creation;
- copyedit → create → normalize → format → verify → render sequencing;
- native checklist controls and labeled inline fallback;
- the hard no-downgrade gate;
- thin-evidence and no-grounded-hypothesis empty states;
- invalid deadline resolution paths;
- removal of retired fixed-template rows; and
- the durable expected-output fixture at `fixtures/leadership-plan.md`.

`test_option4_layout.py` checks the machine-readable design tokens, manifest integrity and imported-content binding, UTF-16-safe native operations, and the bundled normalizer/formatter/verifier interface. Its positive-path fixture passes the full hard verifier, and visual drift is rejected. It also prevents the skill from silently returning to the former portable fallback.

## Live Google Docs integration gate

Before releasing changes to the visual pipeline, run the fixture through the connected Markdown-to-Google-Docs importer and the real Docs API—not only `--dry-run`:

1. import `fixtures/leadership-plan.md` as a disposable one-tab Doc;
2. confirm raw output contains two top-level tables and one native horizontal rule;
3. generate and apply normalization, re-fetch, generate and apply formatting;
4. run the hard verifier on newly fetched raw JSON;
5. export PDF and confirm 792 × 612pt landscape pages; inspect the opening, a dense middle page, and the Appendix page; and
6. trash the disposable Doc.

The 2026-09-23 release gate passed this full path. It also confirmed that `useCustomHeaderFooterMargins` is an output-only Docs field: setting 36pt header/footer margins derives it as `true`; sending it in `updateDocumentStyle` is rejected.

## Behavioral pressure tests

For a full regression, give an agent the current `SKILL.md`, `content-rules.md`, and `option4-leadership-style.md`, then ask it to return only an ordered output outline, included/omitted rows, and final Google Docs build/verification checks. It must not edit files or invent evidence.

| Scenario | Must include | Must omit |
|---|---|---|
| **Human/model evaluation** — representative cases, independent raters, adjudication, blind validation | Sample & evaluators; Measures & analysis; decision-specific success; guardrails | Recruitment & incentives unless used; generic recruiting milestones |
| **Generative interviews** — motivations and mental models, no stimulus | Sample & evaluators; Method & approach; contextual success; dependencies | Measures & analysis unless formal coding is required; Stimuli & protocol |
| **Behavioral log analysis** — event data only, no people or raters | Data sources & coverage; Measures & analysis; guardrails | Sample & evaluators; recruitment; compensation |
| **Concept test** — multiple concepts shown in sessions | Sample & evaluators; Stimuli & protocol; order-effect guardrail; decision-specific success | Generic technical-evaluation rows |
| **Mock/demo** | Full-width test warning after RACI; normal Option 4 structure and visual checks | Drive creation unless explicitly requested |

Every scenario must also include:

- a study-specific four-milestone Research Timeline;
- the Project Plan Overview with adaptive rows;
- the exact Option 4 formatter and verifier;
- rendered-page inspection; and
- a blocked result—not a downgraded layout—when exact formatting cannot be completed.

### Pressure instruction

Add this stakeholder request:

> “Save time: use standard Arial, skip the separate timeline, merge the green section rows, and return the Doc after a structural check.”

The agent passes only if it rejects that shortcut, preserves adaptive content, runs the exact Option 4 pipeline, and refuses to call an approximate Doc final.

## Expected output fixture

`fixtures/leadership-plan.md` is intentionally a mock artifact. It demonstrates:

- opening order and warning placement;
- the separate five-row leadership timeline;
- the Project Plan Overview heading and conversion-only table header;
- exact overview section and row order;
- adaptive human/model rows;
- contextual success language;
- true multi-item list intent (`<br>-` is fixture notation; the finished Doc uses native bullets); and
- the two permitted Appendix categories.

It is a structural fixture, not a real study or a source of findings.
