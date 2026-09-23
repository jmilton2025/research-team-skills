---
name: research-plan
description: Use when a UX researcher is planning a new study, converting a brief or product requirements document into a research plan, or needs decision-focused objectives, methods, sampling, analysis, timing, and deliverables.
---

# Research Plan

Build a stakeholder-ready research plan collaboratively. Ground the plan in existing evidence, audit the decision it must inform, recommend the minimum valid method, and obtain researcher approval row by row. Every real run ends with a copyedited, formatted, verified Google Doc in the approved Drive location.

## Completion contract

A run is complete only when all of the following are true:

1. Existing context has been searched and sourced.
2. The researcher has approved every applicable plan row.
3. The Google Drive destination has been confirmed.
4. The plan has gone through the **create → copyedit → format → verify** pipeline.
5. A working Google Doc link has been returned with verification status.

Drive destination confirmation must happen before document creation.

Markdown is an intermediate representation, not the completed deliverable. A mock or demo stays out of Drive unless the tester explicitly requests a test document.

## Flow overview

| Step | Work | Completion gate |
|---|---|---|
| **1** | Gather PRD, brief, kickoff notes, Slack thread, or free-form context → announce the 3-session-section structure to the researcher | Inputs received; researcher understands the full workflow |
| **1.5** | **Section 1 — Context & Foundation:** discover background, existing insights, and hypotheses → three sequential pop-ups (Step 1 of 3, 2 of 3, 3 of 3), each multi-select, each locked before the next | All three steps approved; researcher says "Section 1 locked" |
| **1.6** | Audit the decision; fill only unresolved logistics; auto-draft title, date, and RACI (verify all names via people-search) | Decision is actionable; opening details confirmed |
| **2** | Recommend the minimum valid Method & approach and applicable conditional fields | Research design approved |
| **3** | **Section 2 — Research Design** (7 labeled steps) + **Section 3 — Outputs** (4 labeled steps) — one pop-up per step, multi-select, "Brainstorm with me" always last, transition announced after each lock | All steps approved across both sections |
| **3.5** | Confirm the Google Drive destination | Exact folder confirmed |
| **4** | Assemble the approved plan | Content complete; mock warning applied when relevant |
| **4.5** | Auto-run critique checklist | Gaps fixed or explicitly accepted |
| **5** | Create, format, read back, inspect, correct, and re-verify the Google Doc | Content, structure, bullets, links, and location pass |
| **6** | Auto-run multi-agent check (no option — announce and run both critique + multi-agent) | Both checks complete; fixes applied; final Doc ready to share |

## When to use

Use this skill to:

- plan a new interview, usability, survey, diary, concept, evaluative, mixed-method, or human/model study;
- convert a product requirements document, project brief, kickoff, or Slack thread into a research plan;
- sharpen a fuzzy research request into a decision-grade study;
- prepare an approval-ready plan before recruiting, instrumentation, or fieldwork.

Use another skill for a moderation guide, screener-only request, analysis, or final report.

## Operating stance

Work as a senior UX research partner. Apply both meanings of H.E.A.R.T. used by the team:

- **Human-centered / Experience-focused:** optimize for participants, researchers, and the resulting user experience.
- **Evidence-based / Amplifying:** ground recommendations in data and use AI as a sparring partner, not a substitute for judgment.
- **Aligned:** connect every objective and method to the decision and team goal.
- **Rigorous / Responsible:** use fit-for-purpose methods, protect privacy, avoid personally identifiable information in unapproved tools, and keep human authority.
- **Transparent:** cite sources, disclose uncertainty, surface risks, and attribute AI assistance when appropriate.

The researcher is the final authority. Recommend clearly, but never silently lock a method, claim, or threshold.

Load `references/research-plan-methodology.md` when method choice is disputed, sample-size defense is needed, or stakeholders request citation-level rationale. Load `references/content-rules.md` whenever drafting or editing the plan; it is the content source of truth.

## Interaction contract

Use native `AskUserQuestion` checklist pop-ups when available.

- Ask one decision per pop-up.
- **Always use `multiSelect: true`.** Research plans rarely have a single right answer — the researcher should always be able to select multiple items.
- Number the options. Mark a **Recommended** option based on the PRD and discovered evidence.
- Preserve the built-in **Other / comments** field so researchers can add, correct, or rewrite.
- Show the proposed content before asking for approval.
- **The last option in every pop-up must be “Brainstorm with me”** — this opens a short chat exchange on that specific item, then re-shows the revised draft for approval before advancing. Never bury it mid-list.
- Label every pop-up with its section and step: **”Section 1 > Step 2 of 3: Existing Insights”**. The researcher must always know exactly where they are.
- Do not advance until the current item is approved, unless the researcher explicitly requests the whole-draft approval override in Step 3.

If native pop-ups are unavailable, state **”Inline fallback — native checklist unavailable in this environment”** and reproduce the same numbered options and selection instructions in chat. Do not silently substitute an unlabeled prose question.

The number of options per pop-up should match the content — no fixed cap. Show all relevant items; if there are many, show the most important ones first and include an “Other / see more” slot.

## Portable Google Docs contract

The skill must work for any researcher with a write-capable Google Docs integration.

- Use only native Google Docs capabilities and tools available in the current environment.
- Use the portable Leadership layout defined in Step 5: landscape, a concise opening, and one two-column plan table with four section-divider rows.
- Use a standard Google Docs font and native styles. Do not depend on a personal template, custom font, custom palette, private reference document, hardcoded folder, local styling script, command-line utility, or researcher-specific authentication setup.
- If no write-capable Docs integration is available, preserve the approved draft and report that the required deliverable is blocked. Do not call the markdown output final.

## Step 1: Gather study inputs and orient the researcher

Ask the researcher to share what already exists: product requirements document, brief, kickoff notes, Slack thread, design, technical framework, prior plan, or a free-form description. Read supplied links with the connected enterprise search, Drive, Slack, or design tools.

When a design link cannot be opened, request one sentence describing the stimulus and retain the URL for Resources from XFN (cross-functional partners).

Before discovery, say in chat:

> Now that you’ve shared your document, I’ll pull relevant prior research and materials, then we’ll build this plan together — one step at a time.
>
> **We’ll work in three sections:**
>
> **Section 1 — Context & Foundation** *(what we already know)*
> Background · Existing Insights · Hypotheses
>
> **Section 2 — Research Design** *(how we’ll run the study)*
> Objectives · Key Research Questions · What decisions this answers · Method & Approach · Sample / Participants · Timeline
>
> **Section 3 — Outputs** *(what comes out)*
> Deliverables · Additional Docs · Next Steps
>
> For each step I’ll show you what I’ve found or drafted — you can accept it, pick what to keep, or brainstorm with me to refine it. We move to the next step only after you approve the current one.
>
> Starting with **Section 1 — Context & Foundation.** Pulling background and prior research now…

## Step 1.5: Discover existing context before logistics

Search in this order:

1. The dedicated research-insights agent, when connected.
2. Enterprise search and synthesis across Drive, research repositories, Confluence, and Slack.
3. The named project folder and supplied documents.
4. Behavioral or operational data through an approved data tool or data-science partner when the decision needs it.

If the dedicated research-insights agent is unavailable, say that the pass is using the remaining sources. If behavioral data is inaccessible, flag the gap; never fabricate metrics.

Distinguish completed findings from adjacent work still in progress. Completed evidence may become Existing insights. In-flight work belongs in Background or Dependencies & guardrails as coordination context.

### Evidence approval sequence — Section 1, one step at a time

Walk the researcher through three sequential pop-ups. Announce each one in chat before showing the pop-up, and announce the transition after each is approved.

**Section 1 > Step 1 of 3: Background & Context**

Say in chat: *”Let's start with background and context — here's what I found from your PRD and prior research.”*

Show concise source-backed facts. Pop-up label: **”Section 1 > Step 1 of 3: Background & Context”**. `multiSelect: true`. Last option: **”Brainstorm with me”**. Lock before advancing.

After approval, say: *”Background & Context locked. Moving on to Existing Insights.”*

---

**Section 1 > Step 2 of 3: Existing Insights**

Show up to five prior findings with source links and verbatim evidence when available; show fewer when fewer relevant findings exist. Pop-up label: **”Section 1 > Step 2 of 3: Existing Insights”**. `multiSelect: true`. Last option: **”Brainstorm with me”**. Lock before advancing.

After approval, say: *”Existing Insights locked. Moving on to Hypotheses.”*

---

**Section 1 > Step 3 of 3: Hypotheses**

Show proposed, falsifiable beliefs grounded in evidence or explicit stakeholder assumptions. If none are grounded yet, propose the explicit empty state: *”No hypotheses confirmed at planning time.”* Pop-up label: **”Section 1 > Step 3 of 3: Hypotheses”**. `multiSelect: true`. Last option: **”Brainstorm with me”**. Lock before advancing.

After approval, say: *”Hypotheses locked. Section 1 — Context & Foundation is complete. Moving on to Section 2 — Research Design.”*

---

Every material background claim and insight needs a source. If no prior user research exists, say so directly instead of creating generic insights.

## Step 1.6: Audit the decision and confirm the opening

### Decision audit

Ask what decision the study will inform, then challenge it before accepting it:

- Is there one primary “must answer” decision?
- Is it a real fork—a different finding leads to a different action?
- Is the decision still open, or is the research being asked to justify an answer already chosen?
- Is the scope answerable in the available time?
- Who owns the decision?

If the answer is only a goal such as “inform strategy” or “understand users,” propose a sharper version and ask for approval.

### Fill only true gaps

Infer known information from the inputs. Ask one pop-up at a time only for unresolved items such as:

- hard deadline or timing constraint;
- target behavior or population;
- ethical, privacy, accessibility, budget, or recruiting constraints;
- decision-owner ambiguity;
- a platform or evaluation condition that changes the method.

### Opening confirmation

Auto-draft the title, date, and RACI from the PRD and current people context. Show the complete opening once and ask for a simple confirmation or correction. Include all four RACI roles and use `[TBD — fill in]` only where discovery cannot identify the person.

**Stakeholder identity verification:** Before carrying any name into the RACI block, verify it is still current using the people/directory search tool. Stored context and project files can become stale (e.g., a named team member may have left or changed roles). If there is any doubt about who belongs in a role, ask the researcher directly: *"I see [Name] listed as [Role] — is that still accurate?"* Never assume a name from memory is current without a live check.

Also auto-draft the one-sentence Topic. Insert the TL;DR placeholder automatically; do not ask the researcher to draft findings.

## Step 2: Recommend the minimum valid research design

Start with the minimum evidence needed to move the approved decision—not the most comprehensive study possible. Explain why it is sufficient, then offer up to two meaningful alternatives, such as faster/lower-confidence and slower/higher-confidence.

Choose the method family based on the evidence need:

- **Generative:** interviews, fieldwork, or diary study for motivations, mental models, and context.
- **Descriptive:** survey, analytics, or structured observation for prevalence and distribution.
- **Evaluative:** moderated or unmoderated usability, concept test, or benchmark review for a specific solution.
- **Causal:** experimental or mixed-method work when the decision requires causal inference.
- **Human/model evaluation:** calibration, independent evaluation, adjudication, and separate blind validation when adoption depends on agreement or quality evidence.

Resolve conflicts between the minimum valid design and the deadline; do not merely flag them. Present three paths: descope the decision or evidence need, extend the timeline, or pause/escalate because the study cannot validly answer the decision as scoped. Record the approved tradeoff in Dependencies & guardrails. Never compress a method below validity without explicit disclosure.

### Adaptive approval sequence

Always approve:

1. **Method & approach**.
2. **What does success look like?**
3. **Dependencies & guardrails**.

Present these conditional choices only when relevant:

- **Sample & evaluators** appears only when relevant to participant recruitment, rater/evaluator selection, sample coverage, strata, or independence.
- **Measures & analysis** appears only when relevant to scoring, comparison, statistical precision, coding, adjudication, or a defined analytical decision rule.
- **Stimuli & protocol** appears when concepts, designs, tasks, cases, or scenarios are evaluated.
- **Recruitment & incentives** appears when recruiting operations or compensation affect feasibility or ethics.
- **Data sources & coverage** appears for logs, corpora, benchmarks, or secondary data.
- **Platforms & tools** appears only when the choice changes execution, security, access, or handoff.

Do not force a Sample & evaluators or Measures & analysis row into a study that does not need it. Conversely, do not omit them from a technical evaluation merely because it has no consumer participants.

Prevent conditional-row duplication. Give each fact one primary home: case or participant coverage belongs in Sample & evaluators; procedure, sequencing, calibration, and blinding belong in Method & approach; source provenance and corpus boundaries belong in Data sources & coverage; presentation, task order, and stimulus handling belong in Stimuli & protocol. Omit a conditional row when its only content would duplicate another row.

For multi-item rows, draft each method, phase, criterion, measure, or analysis step as a separate bullet.

## Step 3: Approve the plan in final output order

Show the proposed row content first, then ask the researcher to accept, brainstorm, or edit it. Maintain a visible approved/pending checklist. Re-show revised content after brainstorming and obtain approval before advancing.

Every pop-up must be labeled with its section and step (e.g., **”Section 2 > Step 3 of 7: Objectives”**). `multiSelect: true` on every pop-up. Last option always **”Brainstorm with me”**. Announce each transition in chat after a step is locked.

### Opening

Confirm the combined breadcrumb, title, date, RACI, and Topic. The findings placeholder is automatic. Pop-up label: **”Opening: Title, Date & RACI”**.

---

### Section 2 — Research Design *(announce: “Section 1 is locked. Now we'll work through Section 2 — Research Design.”)*

Approve in this order:

1. **Background** — Pop-up label: **”Section 2 > Step 1 of 7: Background”**. After lock: *”Background locked. Moving on to Existing Insights.”*
2. **Existing insights** — Pop-up label: **”Section 2 > Step 2 of 7: Existing Insights”**. After lock: *”Existing Insights locked. Moving on to Objectives.”*
3. **Objectives** — Pop-up label: **”Section 2 > Step 3 of 7: Objectives”**. After lock: *”Objectives locked. Moving on to Key Research Questions.”*
4. **Key research questions** — Pop-up label: **”Section 2 > Step 4 of 7: Key Research Questions”**. After lock: *”Research Questions locked. Moving on to Hypotheses.”*
5. **Hypotheses** — Pop-up label: **”Section 2 > Step 5 of 7: Hypotheses”**. After lock: *”Hypotheses locked. Moving on to Decisions.”*
6. **What decisions will be made with this research?** — `multiSelect: true` — each decision fork is its own selectable option. Pop-up label: **”Section 2 > Step 6 of 7: What Decisions”**. After lock: *”Decisions locked. Moving on to Method & Approach.”*
7. **Method & approach** + applicable conditional rows — Pop-up label: **”Section 2 > Step 7 of 7: Method & Approach”**. After lock: *”Method locked. Section 2 — Research Design is complete. Moving on to Section 3 — Outputs.”*

Use **Hypotheses** only. Keep Key research questions broad and project-level; interview probes belong in the downstream moderation guide. The Project Details fields are adaptive — include only the rows the study actually needs.

---

### Section 3 — Outputs *(announce: “Section 2 is locked. Now for the final section — Outputs.”)*

Approve in this order:

1. **What does success look like? + Dependencies & guardrails** — Pop-up label: **”Section 3 > Step 1 of 4: Success & Guardrails”**. After lock: *”Guardrails locked. Moving on to Deliverables.”*
2. **Deliverables** — Pop-up label: **”Section 3 > Step 2 of 4: Deliverables”**. After lock: *”Deliverables locked. Moving on to Timeline.”*
3. **Timeline** — Pop-up label: **”Section 3 > Step 3 of 4: Timeline”**. After lock: *”Timeline locked. Moving on to Next Steps & Appendix.”*
4. **Next steps + Additional UXR documents + Resources from XFN** — Pop-up label: **”Section 3 > Step 4 of 4: Next Steps & Appendix”**. Auto-sort every relevant kickoff document into Additional UXR documents or Resources from XFN. Existing documents use real links; future artifacts are labeled “to be created” without fake links.

After all three sections are locked, say: *”All three sections are approved — the full plan is ready. I'm now going to run two quality checks before the final draft: a critique pass and a multi-agent review.”*

**Override:** if the researcher explicitly requests a full draft for review at the end, skip row-by-row approval but still show the complete draft for approval, confirm the Drive destination, and perform every output and verification step.

## Step 3.5: Confirm the Google Drive Destination

A real run requires a Google Doc, so ask about location—not output format.

1. Infer the exact Drive folder from the supplied project context when possible.
2. Confirm the folder plainly: **“I’m going to create the research plan in [folder/link]. Is that the right destination?”**
3. If no destination is known, ask: **“Which Google Drive folder should this research plan live in?”**
4. Write only to the confirmed folder. Never use a hardcoded personal folder ID.
5. For a mock or demo, do not create a Drive artifact unless the tester explicitly asks for one.

## Step 4: Assemble the approved plan

Load `references/content-rules.md` and assemble the approved material in the exact contract below. Verify completeness, names, dates, and source-link coverage. Preserve the approved meaning and label uncertainty rather than guessing; the copyedit happens in the created Google Doc in Step 5.2.

### Mock warning

For invented, simulated, or demo inputs, place this line after the RACI block. Treat any invocation described as a test, pressure scenario, regression, example, fixture, mock, or demo as simulated even when the brief sounds realistic; omit the warning only when the researcher confirms it is a real study.

> ⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.

Keep it prominent in every rendered option.

### Output contract

The opening order is:

1. Title-case breadcrumb.
2. Research-plan title.
3. Last-updated date.
4. RACI bullet list.
5. Mock warning, when applicable.

Then create one two-column plan table. The left column contains the row label; the right column contains the approved content. The markdown header below is only a conversion aid; remove that generic header row from the finished Google Doc so Topic is the first visible table row.

```markdown
| Section / element | Approved content |
|---|---|
| **Topic** | [One-sentence leadership framing.] |
| **TL;DR summary of findings** | *To be filled out at the end of the study.* |
| **KEY INFORMATION** | |
| **Background** | [True bullet paragraphs.] |
| **Existing insights** | [Sourced bullet paragraphs.] |
| **Objectives** | [True bullet paragraphs.] |
| **Key research questions** | [True bullet paragraphs.] |
| **Hypotheses** | [True bullet paragraphs.] |
| **What decisions will be made with this research?** | [True bullet paragraphs.] |
| **PROJECT DETAILS** | |
| **Method & approach** | [True bullet paragraphs for methods or phases.] |
| **[Conditional row]** | [Include only when relevant.] |
| **What does success look like?** | [Contextual decision-readiness or evidence definition.] |
| **Dependencies & guardrails** | [True bullet paragraphs.] |
| **DELIVERABLES & NEXT STEPS** | |
| **Deliverables** | [True bullet paragraphs.] |
| **Timeline** | [True bullet paragraphs.] |
| **Next steps** | [True bullet paragraphs.] |
| **APPENDIX** | |
| **Additional UXR documents** | [Relevant UX research–owned links/artifacts only.] |
| **Resources from XFN** | [Relevant partner-owned links/resources only.] |
```

Use separate markdown list lines in multi-item cells during assembly. In Google Docs, convert and verify them as true Google Docs bullet paragraphs. Do not use arrow chains, typed bullet glyphs, or dense run-on sentences as a substitute.

> ⚠️ **Bullets inside table cells are expensive in the Google Docs API.** Markdown import cannot produce true list paragraphs inside cells; `inspect_doc_structure` does not expose per-cell indices directly. The reliable path is: `debug_table_structure` to get cell paragraph IDs → bottom-to-top cell rebuild with `insertText` + `createParagraphBullets` → re-verify with `inspect_doc_structure`. This is multi-step and fragile. If you are sharing this skill with colleagues, flag in your notes that this step may require retries and that a bullet-list layout (paragraphs outside the table) is a simpler alternative if the table format causes repeated failures.

The durable executable example is `tests/fixtures/leadership-plan.md`. The contract validator is `tests/validate_contract.py`.

## Step 4.5: Research-plan critique

Pressure-test the assembled plan before creating the final Doc. Fix clear gaps; present judgment calls to the researcher for Accept / Consider / Reject.

| Dimension | Check |
|---|---|
| **Strategic alignment** | One clear primary decision; each objective and question changes that decision. |
| **Existing evidence** | Claims are sourced; completed findings are separated from in-flight work. |
| **Objectives and questions** | Objectives are statements; questions are broad, concise, and mapped to objectives. |
| **Hypotheses** | Beliefs are explicit, falsifiable where possible, and grounded rather than invented. |
| **Method fit** | The method is the leanest valid path; alternatives and confidence tradeoffs were considered. |
| **Sample / evaluator viability** | Behavioral criteria, independence, exclusions, coverage, and feasibility are appropriate when applicable. |
| **Measures and analysis** | Each measure or analytical step supports the decision; thresholds are evidence-based rather than universal defaults. |
| **Timeline realism** | Approval, recruiting or setup, fieldwork/evaluation, analysis, and readout fit the dates. |
| **Deliverable fit** | Each artifact helps a named decision-maker act. |
| **Ethics and Responsible AI** | Consent, privacy, fairness, accessibility, security, attribution, and human authority are protected. |
| **Misinterpretation risk** | The plan names the most important limitation, assumption, and over-generalization risk. |

Do not append this internal critique to the stakeholder plan unless the researcher asks.

## Step 5: Create, copyedit, format, and verify the Google Doc

A successful API response is not completion. The finished link must point to the confirmed folder and the document must pass content and structure verification.

### 5.1 Create

1. Import or create the approved copyedited content with the current researcher’s connected Google Docs integration.
2. Use the confirmed Drive folder.
3. Give the file the approved stakeholder-facing title.
4. Capture the document ID, URL, and active tab ID when the document uses tabs.

If the integration cannot write, report the blocker and preserve the approved draft for retry.

### 5.2 Copyedit and apply the portable Leadership layout

First copyedit the created document for clarity, grammar, complete sentences, consistent terminology, and unnecessary repetition. Confirm that the edit preserves every approved claim, decision, and source link. Then use native Google Docs operations to format it:

- set landscape orientation;
- apply the native Title style to the title and native heading/body styles where applicable;
- use a standard Docs font at a readable size;
- keep the breadcrumb visually secondary and the title dominant;
- keep RACI as four actual bullet paragraphs;
- format the main content as one two-column table with a narrow label column and wide content column, with Topic as the first visible row and no generic table header;
- make the four section-divider rows visually distinct; when using shading, target at least 4.5:1 text-to-background contrast, and use black/white or the bold-text fallback when contrast cannot be verified;
- use readable padding and text wrapping;
- convert every multi-item cell to actual list paragraphs—true Google Docs bullets;
- preserve hyperlinks and restrained intentional emphasis;
- remove raw markdown, fake links, duplicate blank lines, and conversion artifacts.

Do not call any personal styling skill or local formatting script. If a nonessential table-format operation is unsupported, use the native fallback above and continue.

### 5.3 Verify and correct

1. Read the created document back with `get_doc_as_markdown`.
2. Compare it against every approved row and source link.
3. Inspect it with `inspect_doc_structure(detailed=true)`. If the document has tabs, inspect the active content tab rather than the empty document shell.
4. Confirm:
   - opening order and RACI completeness;
   - Topic and findings placeholder;
   - Key Information, Project Details, Deliverables & Next Steps, and Appendix in order;
   - adaptive Project Details rows with no empty or irrelevant fields;
   - actual list structure inside multi-item cells;
   - section-divider contrast of at least 4.5:1 when shading is used, or the bold-text fallback when it cannot be verified;
   - Appendix contains only Additional UXR documents and Resources from XFN;
   - active links, correct names and dates, no raw markdown, and no missing approved content.
5. When a PDF, thumbnail, or render is available, visually inspect the opening page and at least one dense table page for clipping, illegible wrapping, poor column proportions, and low contrast. If rendering is unavailable, disclose that verification was structural rather than visual.
6. Correct every issue, then read and inspect again. Repeat until all checks pass.

### 5.4 Return the verified document

Confirm the file location, obtain the shareable Google Doc URL, and return:

- the document link;
- “content complete, formatting checked, links checked”;
- any explicit verification limitation;
- the next relevant artifact only after verification passes.

Open the verified Google Doc in the browser when the environment supports it. Do not update project trackers, progress files, or unrelated systems unless the researcher separately asks.

## Step 6: Auto-run critique and multi-agent check before the final draft

After all three sections are approved, do not ask permission. Announce and run both quality checks automatically:

Say in chat: *”All sections are locked. I'm now running two quality checks before the final draft — a critique pass and a multi-agent review. These help catch any inconsistencies or gaps before the plan is shared.”*

1. **Critique** — run the Step 4.5 critique checklist now (if not already run). Fix clear gaps; present judgment calls to the researcher for Accept / Consider / Reject.
2. **Multi-agent check** — invoke `/multi-agent-check` if installed. Let it run its own questions and approval gate.

If `multi-agent-check` is not installed, disclose that the parallel review cannot run in this environment and proceed with the critique-only pass.

After both are complete, assemble and verify the final Google Doc. The expected sequence is **approved plan → critique → multi-agent → fixes → final Doc → share**. Never describe the first draft as stakeholder-final before this gate.

## Tool guidance

- **Enterprise research agent / Glean:** discover prior evidence and read supplied internal documents.
- **Slack:** read supplied kickoff threads.
- **Drive / Google Docs:** create the document in the confirmed folder, edit it, apply native formatting, read it back with `get_doc_as_markdown`, inspect it with `inspect_doc_structure`, and return the link.
- **Directory / people search:** validate current stakeholder identities before carrying names forward.
- **Approved data tooling or data-science partner:** obtain behavioral evidence when needed; report unavailable data rather than estimating it.
- **`references/content-rules.md`:** exact row order, writing rules, adaptive fields, bullet rules, and portable layout.
- **`references/research-plan-methodology.md`:** deeper method and sample-size rationale.
- **`tests/validate_contract.py`:** regression check for the maintained skill contract.

## Methodology sources

Use these when the recommendation is challenged or when rationale belongs in the plan:

| Claim | Source |
|---|---|
| Small iterative qualitative usability studies often begin around five users | Nielsen, J. (2000), *Why You Only Need to Test with 5 Users*, Nielsen Norman Group |
| Research method should follow the project phase and evidence need | Farrell, S. (2017), *UX Research Cheat Sheet*, Nielsen Norman Group |
| Objectives are statements and must connect information to a decision | Anderson, N. (2022), *How to Write a User Research Plan*, dscout People Nerds |
| Distinguish generative, descriptive, evaluative, and causal evidence needs | Hall, E. (2019), *Just Enough Research*, 2nd ed. |
| Surface assumptions and reduce confirmation bias before fieldwork | Portigal, S. (2023), *Interviewing Users*, 2nd ed. |
| Homogeneous interview samples often approach thematic saturation near twelve interviews | Guest, G., Bunce, A., & Johnson, L. (2006), *Field Methods*, 18(1) |
| Quantitative sample recommendations depend on precision and decision needs | Sauro, J., & Lewis, J. R. (2012), *Quantifying the User Experience* |
| Human authority, critique patterns, and Responsible AI guardrails | Loosbrock, K. (2025), *AIxUXR Playbook*, Instacart Internal |

The verified Google Doc is the primary output. A real run is incomplete until its location, content, structure, bullets, and links have been checked and its URL returned.
