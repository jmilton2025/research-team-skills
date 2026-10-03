# Content Rules — Research Plan

This file is the content source of truth for `/research-plan`. Every final Google Doc uses the exact **Option 4 — Leadership** hierarchy: concise opening, separate leadership timeline, and the two-column Project Plan Overview.

**Current contract: 2026-10-02.** It preserves the research rigor added in the June team workshops—decision audit before discovery, sourced existing insights, and minimum evidence to move the decision—while enforcing the verified Option 4 visual system for every researcher.

## Canonical order

1. Opening block: breadcrumb, title, last-updated date, RACI roles (Responsible, Accountable, Consulted, Informed), and mock warning when applicable.
2. **Research Timeline** heading, five-row leadership timeline, and one-sentence timing note.
3. **Project Plan Overview** heading.
4. Topic.
5. TL;DR summary of findings: *“To be filled out at the end of the study.”*
6. **Key Information**.
7. **Project Details**.
8. **Deliverables & Next Steps**.
9. **Appendix**.

The four named overview sections must stay in that order. The leadership timeline summarizes the approved detailed Timeline row; it never imports dates or week labels from an older study. The interactive approval walk in `SKILL.md` approves each row once, grouped by section (context first, then design, then outputs); assembly puts every row back in this canonical order.

## Source-use, disclosure, and provenance boundary

Audit the primary decision before discovery. If the answer is already chosen, the plan must reframe an open decision, measure implementation risk honestly, or stop and document the decision as closed; it must not disguise confirmatory work as open research.

**Connector access is not requester authorization.** Before discovery, confirm requester authority and **approved AI processing** for every non-public source or bounded source class. Record the **intended audience** and **source ACL**, plus **quote/link disclosure** permission; the finished plan must not expose a quote, link, or fact beyond the permission of its source.

Use only the **minimum necessary** source content. Redact or **de-identify** participant, customer, employee, and confidential business details before local storage or any authorized reviewer handoff. The reviewer receives only permitted, de-identified extracts—not complete source files by default. If processing or reviewer access is not authorized, use the critique-only path without handing off source content.

Keep a provenance record for every source used: canonical URL or file ID, owner/system, **source revision** or version, **retrieval timestamp**, and **content hash** when available. Mark unavailable values as unavailable. Claims, quotes, and links in the plan must trace back to that record.

## 1. Opening block

Auto-draft the title and current date. Ask for one simple confirmation rather than asking the researcher to compose each field.

Get RACI names from the researcher, not from a people or directory search. Pre-fill a role only with a name the researcher has supplied in this run (brief, PRD, kickoff notes, or their answers), ask in chat for any key role still missing, and then offer to add more people after the key four are confirmed.

Order:

1. Short title-case breadcrumb.
2. Wide, stakeholder-facing research-plan title.
3. `Last updated: [Month Year]`.
4. RACI as four true bullet paragraphs.
5. Mock warning, when applicable.

Always include all four roles. Unknown names use `[TBD — fill in]`.

- **Responsible:** the researcher running the study.
- **Accountable:** the owner of the decision.
- **Consulted:** partners whose expertise shapes the decision.
- **Informed:** people who need the outcome but do not make the decision.

If a person listed as Consulted is actually the decision owner, confirm the role and place that person in Accountable instead of leaving the ownership ambiguous. Never carry names over from an older plan or from memory; RACI names come from the researcher in this run.

A mock, demo, test, pressure scenario, regression, example, fixture, or otherwise simulated study includes this prominent line, even when its brief sounds realistic. Omit it only when the researcher confirms the study is real:

> ⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.

## 2. Topic and TL;DR

### Topic

Use one high-level sentence that states the user or evidence gap and the decision the study will support. Lead with why the study matters before naming its mechanics.

### TL;DR summary of findings

At planning time, insert exactly:

> *To be filled out at the end of the study.*

Do not ask the researcher to predict findings before the study.

## 3. Leadership timeline

Every plan includes a separate at-a-glance timeline above Project Plan Overview:

- exactly two columns and five rows: the header `Timing | Leadership milestone` plus four study-specific milestones;
- left labels that start with their timing, then a short name (`Week 1: Setup & rubric`, `Weeks 2–3: Calibration`, `Week 4: Decision readout`), each short enough to stay on one line: at most 134pt wide in bold DM Sans 10pt, which the parser measures (usually 24 to 27 characters, depending on the letters; shorten an over-width label and tell the researcher); use `Day N:` or `Month N:` only when the study runs in days or months;
- one-sentence leadership summaries no longer than 160 characters in the right column;
- milestones derived from the approved detailed Timeline row, never copied from a reference study; two milestones may share a week, and the week numbers must match the detailed row;
- an italic one-sentence timing note immediately below the table.

The four milestones should cover the study's meaningful leadership checkpoints, such as setup, fieldwork or evaluation, synthesis or validation, and decision/readout. Keep detailed dependencies, dates, and contingencies in the Timeline row. If the at-a-glance table spills awkwardly across pages, tighten the summary without changing the approved detailed timeline.

## 4. Key Information

Use these rows in this order:

1. Background.
2. Existing insights.
3. Objectives.
4. Key research questions.
5. Hypotheses.
6. What decisions will be made with this research?

### Background

Write 3–6 true bullet paragraphs. Each bullet uses a short bold lead-in plus one concise explanation. Cover the problem, current state, evidence gap, and relevant product context. Keep implementation detail only when it changes scope or interpretation.

Open with a **Why now** bullet: the sourced reason this study matters at this moment. End that bullet with `**Strategic fit:** [TBD — fill in] (the H2 / OKR priority this supports)` unless a source names the priority, in which case state it and cite it.

Every material claim must cite its source: a link, or the source name and date when no link exists (`Source: kickoff notes, 2026-10-02.`). If a background statement is an interpretation rather than a direct fact, label it as such.

### Existing insights

Include up to five findings that materially shape this study; include fewer when fewer relevant findings exist. Each item must contain:

- one plainly stated insight, with its scope and caveats in the bold heading itself (for example, “(preliminary, one week)” or “(denominator assumed to be all tagged orders)”);
- a clickable source link, or the source name and date when no link exists; and
- a verbatim supporting quote when the finding rests on a specific line.

A reader who sees only the bold headings should still know which figures are preliminary and what each figure is a share of.

Do not treat an in-flight adjacent project as a completed insight. Put it in Background or Dependencies & guardrails as coordination context. If no relevant prior research exists, state: *“No prior user research on [topic] — this is net-new territory.”*

### Objectives

Objectives are statements, not questions. Use a true bulleted list; each objective contains:

- a short bold statement of what the study must establish; and
- at most one sentence explaining what is missing and what decision the objective unlocks.

Do not force exactly three. Use the minimum complete set, usually 2–4. Every objective must pass Anderson’s test: “I need [information] to make [decision] that affects [goal].”

### Key research questions

These are broad project-level questions, not interview probes. Use a true bulleted list; each item contains one bold strategic question and, when needed, one sentence of framing.

Do not put TEDW prompts (“Tell me…”, “Explain…”, “Describe…”, “Walk me through…”) here. Those belong in a moderation or discussion guide. Use the minimum complete set and map each question to an objective.

### Hypotheses

Use the heading **Hypotheses** only. Include concise, falsifiable team beliefs that the study can pressure-test. Prefix them `H1`, `H2`, and so on, but do not force a fixed count. Each hypothesis should be grounded in an existing insight, stakeholder belief, or explicit assumption. Label its origin in italics after the statement:

- *(Researcher hypothesis, inferred from [source and the specific evidence].)* when the researcher derived it from a source;
- *(Stakeholder assumption, stated by [role] in [source].)* only when a stakeholder actually stated the belief. Never label a researcher inference as a stakeholder assumption.

Do not combine hypotheses with a second category of stakeholder questions. If no hypothesis is grounded in evidence or an explicit stakeholder assumption, keep the row and state: *“No hypotheses confirmed at planning time.”* Do not invent one to fill the space.

### What decisions will be made with this research?

Use true bullet paragraphs. Each item must be a real fork: a different finding produces a different action. Name the owner or affected decision when useful. If the answer cannot change behavior, sharpen or remove the item.

Define each decision outcome once, in this row, as a bold-led bullet: `**Proposed definitions, to confirm with the decision owner in Week 1:** go = …; narrow = …; no-go = …`. Use the study's own outcome names when they differ. Reuse those exact terms, unchanged, in Topic, Key research questions, What does success look like?, Deliverables, the Timeline, and Next steps; do not introduce synonyms such as “fund” or “drop” elsewhere.

Do not add a research-priorities or themes row.

## 5. Project Details

`Method & approach` is the core row. Add other rows only when the PRD, approved research questions, or study type makes them useful. Do not emit empty or irrelevant methodology fields merely because they exist in another plan.

### Core rows

| Row | Rule |
|---|---|
| **Method & approach** | Always include. Lead with the minimum valid evidence needed to move the decision. Put each method, phase, or procedure in its own true Google Docs bullet paragraph. Offer a faster/lower-confidence or slower/higher-confidence alternative during approval, but include only the chosen approach in the plan. |
| **What does success look like?** | Always include. Define success in the context of the product requirements document (PRD), research question, and decision. A numeric threshold is appropriate only when the evidence supports one; otherwise define the credible evidence or decision-readiness outcome. |
| **Dependencies & guardrails** | Always include. Use true bullet paragraphs for dependencies, sequencing constraints, ethics, privacy, accessibility, decision boundaries, and known interpretation risks. Attach an owner or date when one exists. Add a guardrail that names every preliminary figure the plan cites and states that each is a starting point, not a result. |

### Conditional rows

| Row | Include when |
|---|---|
| **Sample & evaluators** | Include only when relevant: the study recruits participants, uses human evaluators, requires sampling strata, or needs defensible coverage. State behavioral criteria before demographics, sample rationale, exclusions, and evaluator independence where applicable. State precision for the allocation actually planned (proportional, or equal strata re-weighted, which is wider), and say that per-stratum estimates are wider. Mark strata provisional when the source does not define them all, and report very small strata descriptively rather than as rates. |
| **Measures & analysis** | Include only when relevant: the decision depends on metrics, scoring, comparison, statistical precision, coding, adjudication, or a defined analysis approach. Put every measure and analysis step in its own true Google Docs bullet paragraph. When the decision is an investment call, include an absolute-impact measure (the rate gap × volume, in affected units per week or month), not rates alone. |
| **Stimuli & protocol** | The study evaluates concepts, designs, tasks, scenarios, content, or benchmark cases. Name counterbalancing or blinding when needed. |
| **Recruitment & incentives** | Operational recruiting details materially affect feasibility or ethics. |
| **Data sources & coverage** | Behavioral, log, corpus, benchmark, or secondary-data work requires explicit source and coverage definitions. |
| **Platforms & tools** | Tool choice changes study execution, access, security, or handoff. |

Use the study’s language for any additional conditional row. Do not create generic rows that add no decision value.

Prevent conditional-row duplication by keeping each fact in one primary row. Coverage and evaluator criteria belong in Sample & evaluators; procedure, calibration, sequencing, and blinding belong in Method & approach; source provenance and corpus boundaries belong in Data sources & coverage; presentation and task-order rules belong in Stimuli & protocol. If a conditional row would only repeat another row, omit it.

### Adaptive examples

- An interview study usually needs Sample & evaluators, Stimuli & protocol only if stimuli exist, and may not need Measures & analysis.
- A human/model calibration study usually needs Sample & evaluators plus Measures & analysis, but may not need participant recruitment or compensation.
- A log analysis may need Data sources & coverage and Measures & analysis, but no Sample & evaluators row if there are no human participants or raters.
- A quick concept review may need Stimuli & protocol and Sample & evaluators, with a qualitative success definition rather than a universal threshold.

## 6. Deliverables & Next Steps

Use these rows in this order:

1. Deliverables.
2. Timeline.
3. Next steps.

### Deliverables

Name what stakeholders will receive, not merely a file type. Put each artifact in its own true Google Docs bullet paragraph and connect it to the decision or objective it serves.

Use **Deliverables** as the label.

### Timeline

Use true bullet paragraphs for phases or dated milestones. Choose the level of detail the study needs:

- a short phase plan for exploratory or technical evaluation work;
- dated recruiting, fieldwork, synthesis, and readout milestones for participant studies;
- an explicit Research Operations (ResOps) recruiting lead-time note only when the standard recruiting workflow applies.

Do not force generic week labels or recruiting milestones into the detailed Timeline row. The separate leadership table always contains four concise study-specific milestones, while this row carries the dates and operational detail the study actually needs. If the minimum valid design cannot fit the requested deadline, require a choice: descope the decision or evidence need, extend the timeline, or pause/escalate the study. Record the accepted tradeoff in Dependencies & guardrails; do not silently compress the design below validity.

### Next steps

List immediate actions required to start the study, each as a true bullet paragraph. Include owners or dates when known. Do not repeat the full timeline.

## 7. Appendix

The Appendix contains exactly two rows:

1. **Additional UXR documents** (“UXR” means UX research).
2. **Resources from XFN** (“XFN” means cross-functional partners).

### Additional UXR documents

Include prior studies and research-owned artifacts such as the research brief, moderation guide, screener, survey instrument, analysis workspace, consent language, and final report. Prune the list to the approved method. Do not invent placeholder artifacts the study will never use.

### Resources from XFN

“XFN” means cross-functional partners. Include partner-owned inputs such as the product requirements document, design files, technical framework, scorecard, experiment plan, requirements, and kickoff notes.

Auto-carry every relevant document surfaced in the kickoff inputs into one of these two rows. Existing documents use real clickable links. A source with no link, such as a pasted draft, is listed once here with its date and “(pasted; no link exists)”. Future artifacts may be plain text marked “to be created”; do not create fake links.

Nothing follows these two Appendix rows.

## 8. Bullet and prose rules

- Use actual list paragraphs in the Google Doc—true Google Docs bullets—not typed bullet glyphs, arrow chains, or dense sentences separated by semicolons.
- In the intermediate markdown, use separate `- ` lines. After import, apply and verify list formatting inside table cells with Google Docs editing tools.
- Methods, phases, sample criteria, measures, analysis steps, dependencies, guardrails, deliverables, timeline phases, and next steps each receive separate bullets when there is more than one item.
- Every bullet must make sense on its own.
- Use bold lead-ins sparingly to support scanning. Bold the decision-driving words, not every label or full paragraph.
- Preserve clickable source links. Never invent one. When a source has no link, cite it by name and date on each bullet (`Source: kickoff notes, 2026-10-02.`) and note that no link exists only once, in Resources from XFN; don't repeat “link unavailable” tags through the plan.
- Write for the stakeholder, not the pipeline. Leave out internal workflow terms (for example, “source gate”). Define an internal tool or system name in plain English on first use; when you don't know what it does, write `[TBD — fill in] plain-English description` instead of guessing.
- State past decisions only when a source records them. Without a source, write “out of scope for this plan” rather than “was descoped” or “was decided.”

## 9. Study-type adaptation

| Study type | Likely adaptations |
|---|---|
| **In-depth interview (IDI) / generative** | Narrative objectives and questions; behavioral Sample & evaluators; no task metrics unless the decision requires them. Typical N=6–12 for a reasonably homogeneous sample. |
| **Moderated usability** | Task-oriented Stimuli & protocol; task-level evidence in Measures & analysis; typical N=5 for one group, 3–4 per group for two groups, 3 per group for three or more (Nielsen, 2000 — see `research-plan-methodology.md` §5). Going above that is a judgment call; state the reason in the plan (e.g., each finding must hold within every group, or a no-show buffer) rather than citing a range. |
| **Unmoderated usability** | Larger sample; task success, time, and post-task ease measures when relevant. |
| **Survey** | Measures & analysis includes population, precision, confidence interval, and weighting assumptions when used. |
| **Diary study** | Timeline reflects setup, longitudinal fieldwork, check-ins, and synthesis; protocol includes entry cadence. |
| **Concept test** | Stimulus handling, order effects, comparison logic, and a contextual success definition. |
| **Mixed method** | Separate sample and analysis logic by strand; state when and how the evidence is integrated. |
| **Human/model evaluation** | Evaluator independence, calibration versus blind validation, adjudication, coverage, and decision-specific success evidence. |

## 10. Option 4 — Leadership visual contract

Every final Google Doc must match [`option4-leadership-style.md`](option4-leadership-style.md) and pass the machine-readable contract in [`option4-style-contract.json`](option4-style-contract.json):

- pageless editing mode with landscape-letter export geometry and one-inch print margins;
- DM Serif Display breadcrumb, title, headings, and section bands;
- DM Sans body, RACI, labels, timeline, and table content;
- a separate five-row Research Timeline headed `Timing | Leadership milestone` and a Project Plan Overview table, both with fixed 144pt / 554.4pt columns;
- pale-yellow full-paragraph test warning when applicable;
- white ordinary cells and dark-green `#003D29` two-cell section bands;
- Topic as the first visible overview row, with no generic conversion header;
- true native bullet paragraphs, active links, and restrained emphasis.

Use `scripts/option4_layout.py` to parse, normalize, format, and verify the document. The historical private Option 4 reference is an audit source only; colleagues do not need access to it. If the connected Google Docs environment cannot apply or verify the exact contract, **block completion** and preserve the approved draft for retry. A standard-font, one-table, generic-color, merged-band, or structural-only fallback is not a finished research plan.

## Source history

- 2026-05-12: objectives, broad research-question distinction, and scannable content patterns established.
- 2026-06-02: discovery-first workflow, verbatim sourcing, decision audit, minimum-evidence methodology, and critique handoff added from the team workshop.
- 2026-09-23: approved Leadership structure adopted after an end-to-end mock test; fields made adaptive; Deliverables & Next Steps separated; Appendix restricted.
- 2026-09-23: the mock exposed visual drift in the portable fallback; the exact Option 4 — Leadership timeline, typography, colors, geometry, formatter, and hard verification gate became mandatory for every final Doc.
- 2026-09-29: source authorization, minimization, provenance, destination ACL, reviewer-handoff, idempotent-write, revision-binding, and partial-document safety gates added.
- 2026-10-02: an end-to-end mock produced the approved standard deliverable. Adopted from it: the `Timing | Leadership milestone` header with `Week N: Short name` labels (enforced by the parser); a Why now bullet and strategic-fit placeholder in Background; scoped and caveated insight headings; origin-labeled hypotheses; decision outcomes defined once and reused; name-and-date citations for unlinked sources; plain stakeholder language; design-specific sample precision; absolute impact for investment decisions; and inspection of every rendered page.
- 2026-10-02 (same-day revision, after review of the approved Doc): the 24-character label cap would have rejected the approved Doc's own 27-character first label, which fit on one line. The parser now measures printed width (134pt maximum) instead of counting characters. The researcher now confirms the key RACI people and can add more, replacing the directory search. The connection check moved to the start of the run so that a signed-out connection, such as Glean, is flagged immediately.
