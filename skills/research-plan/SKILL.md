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
3. The critique pass has run, and the multi-agent review has run when it is installed and authorized (otherwise the run is disclosed as critique-only), with fixes folded in.
4. The Google Drive destination has been confirmed.
5. The plan has gone through the **copyedit → create → normalize → Option 4 format → verify → render** pipeline.
6. The exact **Option 4 — Leadership** visual contract has passed, and a working Google Doc link has been returned with verification status.

The quality checks run before the Google Doc is drafted. Drive destination confirmation must happen before document creation.

Markdown is an intermediate representation, not the completed deliverable. A mock or demo stays out of Drive unless the tester explicitly requests a test document.

## Flow overview

| Step | Work | Completion gate |
|---|---|---|
| **1** | Gather the request without opening sources → audit the decision → authorize source use → check connections → announce the 3-section structure | Decision is genuinely open and actionable; sources and connections are authorized or skipped; researcher understands the workflow |
| **1.5** | **Section 1 — Context & Foundation:** discover background, existing insights, and hypotheses → three sequential pop-ups (Step 1 of 3, 2 of 3, 3 of 3), each locked before the next | Background, Existing insights, and Hypotheses approved |
| **1.6** | Fill only unresolved logistics; auto-draft title, date, RACI, and Topic (verify all names via people search) | Opening approved |
| **2** | Recommend the minimum valid method direction and the conditional rows the study needs | Method direction picked (the rows are approved in Step 3) |
| **3** | **Section 2 — Research Design** (4 labeled steps: Objectives, Key research questions, Decisions, Method & approach) + **Section 3 — Outputs** (4 labeled steps) — one pop-up per step, "Brainstorm with me" always offered, transition announced after each lock | All remaining rows approved; no row approved twice |
| **3.5** | Confirm the Google Drive destination | Exact folder confirmed |
| **4** | Assemble the approved plan (markdown intermediate, saved in a persistent working folder) | Content complete; mock warning applied when relevant |
| **4.5** | Auto-run critique checklist (announced at end of Step 3) | Gaps fixed or explicitly accepted |
| **5** | Auto-run multi-agent review on the fixed content — before the Doc; if it isn't installed or reviewer processing is not authorized, disclose a critique-only run | Review complete (or critique-only disclosed); confirmed fixes folded in |
| **6** | Copyedit, create, normalize, apply the exact Option 4 — Leadership layout, verify, render, correct, and return | Content, links, location, exact visual contract, and rendered pages pass |

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

Load `references/research-plan-methodology.md` when method choice is disputed, sample-size defense is needed, or stakeholders request citation-level rationale. Load `references/content-rules.md` whenever drafting or editing the plan; it is the content source of truth. Load `references/source-and-delivery-safety.md` before using non-public sources or creating a Google Doc. Load `references/option4-leadership-style.md` before assembling or formatting the final Google Doc.

## Interaction contract

Use native `AskUserQuestion` checklist pop-ups when available, within the tool's limits:

- Ask one decision per pop-up.
- **At most 4 options per pop-up.** “Brainstorm with me” takes one slot, so show up to 3 content options. When a row has more items than fit (e.g., six background facts), list them all, numbered, in chat first; then offer grouped options (e.g., “Keep all 6 (Recommended)”, “Keep 1–4, drop 5–6”) and let the researcher name specific items in the comments field.
- **Use `multiSelect: true` only when the options can be combined** (e.g., which insights to keep, which fixes to apply). Use single-select for either/or choices (e.g., which method direction, which Drive folder).
- Put the **Recommended** option first, with “(Recommended)” in its label. Base it on the PRD and discovered evidence.
- Keep the built-in **Other / comments** field so researchers can add, correct, or rewrite. The tool adds it automatically; don't add your own “Other” option.
- Show the proposed content in chat before the pop-up. Options are short labels, not the content itself.
- **Offer “Brainstorm with me” as the last option in every approval pop-up.** It opens a short chat exchange on that specific item, then re-shows the revised draft for approval before advancing.
- Label every pop-up with its section and step in the question text: **“Section 1 > Step 2 of 3: Existing Insights”**. The researcher must always know exactly where they are. (The short header chip holds at most 12 characters, so the full label goes in the question.)
- Do not advance until the current item is approved, unless the researcher explicitly requests the whole-draft approval override in Step 3.

If native pop-ups are unavailable, state **“Inline fallback — native checklist unavailable in this environment”** and reproduce the same numbered options and selection instructions in chat. Do not silently substitute an unlabeled prose question.

## Option 4 — Leadership Google Docs contract

The skill must produce the same leadership-ready visual system for every researcher. Runtime access to Jedida's private reference Doc is neither assumed nor required.

- Use the bundled machine-readable contract in `references/option4-style-contract.json` and the executable pipeline in `scripts/option4_layout.py`.
- Build the exact hierarchy: concise opening → separate five-row leadership timeline under **Research Timeline** → **Project Plan Overview** table.
- Apply DM Serif Display and DM Sans, the exact colors, pageless editing mode with landscape-letter export geometry, one-inch print margins, fixed table widths, pale-yellow warning treatment, white body cells, and dark-green two-cell section bands.
- Keep adaptive study content and milestones; never copy wording, dates, week labels, people, or findings from the historical reference plan.
- Run the bundled verifier and inspect rendered pages. Structural similarity or a successful API response is not enough.
- If the connected environment cannot apply or verify the exact contract, preserve the approved draft and **block completion**. Do not return a standard-font, one-table, generic-color, merged-band, or structural-only fallback as final.
- This visual gate is not researcher-, stakeholder-, or leadership-waivable. An instruction to accept a downgrade still blocks final delivery; return the approved draft as blocked, not an approximate Google Doc as final.

## Step 1: Gather study inputs and orient the researcher

Ask first for metadata and links only: what artifacts exist (product requirements document, brief, kickoff notes, Slack thread, design, technical framework, or prior plan) plus a non-sensitive description of the request. Tell the researcher not to paste, upload, or expose non-public content until the source-use authorization gate passes. Collect links without opening or searching them.

### Decision audit — before discovery

Ask what decision the study will inform, then challenge it before reading prior evidence:

- Is there one primary “must answer” decision?
- Is it a real fork—a different finding leads to a different action?
- Is the decision still open, answerable in the available time, and owned by a named person?

If the request is only a goal such as “inform strategy” or “understand users,” propose a sharper decision and ask for approval. If the answer has already been chosen, do not run discovery under confirmatory framing. Offer three explicit branches:

1. **Reopen or reframe** a genuine decision fork that evidence could change.
2. **Measure implementation risk** without pretending the research selects the already-chosen direction.
3. **Document the decision as closed and stop** the research-plan workflow.

If the requester insists that research justify a closed answer, refuse that framing and stop. Continue only after an open, actionable decision is approved.

### Source-use authorization gate

Read `references/source-and-delivery-safety.md` and complete its authorization gate before accessing any non-public source. **Connector access is not requester authorization.** Record the authorization basis, approved AI processing, intended audience and source ACL, quote/link disclosure, minimum necessary de-identification, and provenance. If any required authorization is unknown, stop before reading that source; ask the researcher to confirm it or skip it. A skipped source remains unverified and cannot support a claim.

### Connection check

After the source-use gate, check each connection the run depends on, with a quick authentication or metadata call rather than trusting the tool list (a listed tool can still ask for sign-in). This connection check must not open or retrieve source content; content access starts only under the approved gate above.

| Connection | Needed for |
|---|---|
| Research-insights agent | Prior findings (Step 1.5) |
| Enterprise search (e.g., Glean) | Prior research, supplied internal docs (Steps 1–1.5) |
| Google Drive / Docs (connector or `gws`) | Reading supplied docs; creating and verifying the final Doc (Step 6) |
| Slack | Supplied kickoff threads |
| People / directory search | Verifying RACI names (Step 1.6) |
| `multi-agent-check` skill | The multi-agent review (Step 5); check the live skill list |

For each missing connection, explain its purpose and how to connect it, then wait for connection or an explicit skip. Report connected/skipped sources before discovery; dependent claims remain unverified. Missing Docs write access means the run will end with a blocked draft, and missing `multi-agent-check` means critique-only review.

Before discovery, say in chat:

> Now that you’ve shared your document, I’ll pull relevant prior research and materials, then we’ll build this plan together — one step at a time.
>
> **We’ll work in three sections:**
>
> **Section 1 — Context & Foundation** *(what we already know)*
> Background · Existing Insights · Hypotheses
>
> *The primary decision is set. After Section 1, I’ll draft the title, date, RACI, and Topic for one quick confirmation.*
>
> **Section 2 — Research Design** *(how we’ll run the study)*
> Objectives · Key Research Questions · Decisions · Method & Approach (plus sample, measures, or stimuli rows when the study needs them)
>
> **Section 3 — Outputs** *(what comes out)*
> Success & Guardrails · Deliverables · Timeline · Next Steps & Appendix
>
> For each step I’ll show you what I’ve found or drafted — you can accept it, pick what to keep, or brainstorm with me to refine it. Each part is approved once, and we move to the next step only after you approve the current one.
>
> Starting with **Section 1 — Context & Foundation.** Pulling background and prior research now…

## Step 1.5: Discover existing context before logistics

After the decision and source-use gates pass, if an authorized design link cannot be opened, request one non-sensitive sentence describing the stimulus and retain the URL for Resources from XFN (cross-functional partners).

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

Say in chat: *“Let's start with background and context — here's what I found from your PRD and prior research.”*

Show concise source-backed facts in chat, numbered. Pop-up label: **“Section 1 > Step 1 of 3: Background & Context”**. The researcher picks which facts to keep, so use multi-select (grouped when there are more than 3 facts), with **“Brainstorm with me”** last. Lock before advancing.

After approval, say: *“Background & Context locked. Moving on to Existing Insights.”*

---

**Section 1 > Step 2 of 3: Existing Insights**

Show up to five prior findings in chat with source links and verbatim evidence when available; show fewer when fewer relevant findings exist. Pop-up label: **“Section 1 > Step 2 of 3: Existing Insights”**. Multi-select for which findings to keep (grouped when there are more than 3), with **“Brainstorm with me”** last. Lock before advancing.

After approval, say: *“Existing Insights locked. Moving on to Hypotheses.”*

---

**Section 1 > Step 3 of 3: Hypotheses**

Show proposed, falsifiable beliefs grounded in evidence or explicit stakeholder assumptions. If none are grounded yet, propose the explicit empty state: *“No hypotheses confirmed at planning time.”* Pop-up label: **“Section 1 > Step 3 of 3: Hypotheses”**. Multi-select for which hypotheses to keep (grouped when there are more than 3), with **“Brainstorm with me”** last. Lock before advancing.

After approval, say: *“Hypotheses locked. Section 1 — Context & Foundation is complete. Next I’ll confirm the opening details, then we’ll move into Section 2 — Research Design.”*

These three rows are now approved. Don't ask for them again in Step 3; if later work changes one (e.g., a new hypothesis surfaces), show just the change and ask once.

---

Every material background claim and insight needs a source. If no prior user research exists, say so directly instead of creating generic insights.

## Step 1.6: Confirm logistics and the opening

### Fill only true gaps

Infer known information from the inputs. Ask one pop-up at a time only for unresolved items such as:

- hard deadline or timing constraint;
- target behavior or population;
- ethical, privacy, accessibility, budget, or recruiting constraints;
- decision-owner ambiguity;
- a platform or evaluation condition that changes the method.

### Opening confirmation

Auto-draft the title, date, and RACI from the PRD and current people context. Show the complete opening (breadcrumb, title, date, RACI, and Topic) once and ask for a simple confirmation or correction. Pop-up label: **“Opening: Title, Date & RACI”**. This is the only time the opening is approved. Include all four RACI roles and use `[TBD — fill in]` only where discovery cannot identify the person.

**Stakeholder identity verification:** Before carrying any name into the RACI block, verify it is still current using the people/directory search tool. Stored context and project files can become stale (e.g., a named team member may have left or changed roles). If there is any doubt about who belongs in a role, ask the researcher directly: *"I see [Name] listed as [Role] — is that still accurate?"* Never assume a name from memory is current without a live check.

Also auto-draft the one-sentence Topic. Insert the TL;DR placeholder automatically; do not ask the researcher to draft findings.

## Step 2: Recommend the minimum valid research design

Start with the minimum evidence needed to move the approved decision—not the most comprehensive study possible. Explain why it is sufficient, then offer up to two meaningful alternatives, such as faster/lower-confidence and slower/higher-confidence.

Choose the method family based on the evidence need:

- **Generative:** interviews, fieldwork, or diary study for motivations, mental models, and context.
- **Descriptive:** survey, analytics, or structured observation for prevalence and distribution.
- **Evaluative:** moderated or unmoderated usability, concept test, or benchmark review for a specific solution.
- **Causal:** randomized experiments or defensible quasi-experiments when the decision requires causal inference. Mixed methods may explain mechanisms but are not inherently causal.
- **Human/model evaluation:** calibration, independent evaluation, adjudication, and separate blind validation when adoption depends on agreement or quality evidence.

Resolve conflicts between the minimum valid design and the deadline; do not merely flag them. Present three paths: descope the decision or evidence need, extend the timeline, or pause/escalate because the study cannot validly answer the decision as scoped. Record the approved tradeoff in Dependencies & guardrails. Never compress a method below validity without explicit disclosure.

### Pick the direction, then draft the rows

Ask one single-select pop-up for the method direction: the recommended design first, up to two alternatives, and **“Brainstorm with me”** last. This picks the direction only; the rows themselves are approved once, in Step 3.

Every plan drafts **Method & approach** (approved in Section 2), plus **What does success look like?** and **Dependencies & guardrails** (approved together in Section 3).

Draft these conditional rows only when relevant; they are approved with Method & approach:

- **Sample & evaluators** appears only when relevant to participant recruitment, rater/evaluator selection, sample coverage, strata, or independence.
- **Measures & analysis** appears only when relevant to scoring, comparison, statistical precision, coding, adjudication, or a defined analytical decision rule.
- **Stimuli & protocol** appears when concepts, designs, tasks, cases, or scenarios are evaluated.
- **Recruitment & incentives** appears when recruiting operations or compensation affect feasibility or ethics.
- **Data sources & coverage** appears for logs, corpora, benchmarks, or secondary data.
- **Platforms & tools** appears only when the choice changes execution, security, access, or handoff.

Do not force a Sample & evaluators or Measures & analysis row into a study that does not need it. A technical evaluation with raters, sampling strata, or defensible coverage still needs Sample & evaluators even when it has no consumer participants; a pure log analysis with no participants or raters omits that row.

Prevent conditional-row duplication. Give each fact one primary home: case or participant coverage belongs in Sample & evaluators; procedure, sequencing, calibration, and blinding belong in Method & approach; source provenance and corpus boundaries belong in Data sources & coverage; presentation, task order, and stimulus handling belong in Stimuli & protocol. Omit a conditional row when its only content would duplicate another row.

For multi-item rows, draft each method, phase, criterion, measure, or analysis step as a separate bullet.

## Step 3: Approve the remaining rows in output order

Show the proposed row content first, then ask the researcher to accept, brainstorm, or edit it. Maintain a visible approved/pending checklist. Re-show revised content after brainstorming and obtain approval before advancing.

Every pop-up must be labeled with its section and step (e.g., **“Section 2 > Step 1 of 4: Objectives”**) and follow the pop-up rules in the Interaction contract. Announce each transition in chat after a step is locked.

Background, Existing insights, and Hypotheses were approved in Section 1, and the opening in Step 1.6. Don't re-ask for them here.

---

### Section 2 — Research Design *(announce: “The decision, opening, and method direction are set. Now we'll work through Section 2 — Research Design.”)*

Approve in this order:

1. **Objectives** — Pop-up label: **“Section 2 > Step 1 of 4: Objectives”**. After lock: *“Objectives locked. Moving on to Key Research Questions.”*
2. **Key research questions** — Pop-up label: **“Section 2 > Step 2 of 4: Key Research Questions”**. After lock: *“Research Questions locked. Moving on to Decisions.”*
3. **What decisions will be made with this research?** — multi-select; each decision fork is its own option (grouped when there are more than 3). Pop-up label: **“Section 2 > Step 3 of 4: What Decisions”**. After lock: *“Decisions locked. Moving on to Method & Approach.”*
4. **Method & approach** + applicable conditional rows — Pop-up label: **“Section 2 > Step 4 of 4: Method & Approach”**. After lock: *“Method locked. Section 2 — Research Design is complete. Moving on to Section 3 — Outputs.”*

Use **Hypotheses** only. Keep Key research questions broad and project-level; interview probes belong in the downstream moderation guide. The Project Details fields are adaptive — include only the rows the study actually needs.

---

### Section 3 — Outputs *(announce: “Section 2 is locked. Now for the final section — Outputs.”)*

Approve in this order:

1. **What does success look like? + Dependencies & guardrails** — Pop-up label: **“Section 3 > Step 1 of 4: Success & Guardrails”**. After lock: *“Success & Guardrails locked. Moving on to Deliverables.”*
2. **Deliverables** — Pop-up label: **“Section 3 > Step 2 of 4: Deliverables”**. After lock: *“Deliverables locked. Moving on to Timeline.”*
3. **Timeline** — Pop-up label: **“Section 3 > Step 3 of 4: Timeline”**. After lock: *“Timeline locked. Moving on to Next Steps & Appendix.”*
4. **Next steps + Additional UXR documents + Resources from XFN** — Pop-up label: **“Section 3 > Step 4 of 4: Next Steps & Appendix”**. Auto-sort every relevant kickoff document into Additional UXR documents or Resources from XFN. Existing documents use real links; future artifacts are labeled “to be created” without fake links.

After all three sections are locked, tell the researcher exactly what happens next so they know what to expect:

> All three sections are approved — I now have everything I need. Here's what I'll do before I hand you the final plan:
>
> 1. **Run a critique pass** — a pressure-test that checks the plan for gaps, weak logic, and unsupported claims. I will self-critique unless the authorized source-use boundary permits a separate critique reviewer.
> 2. **Run it through the multi-agent review when the authorized source-use boundary permits it** — two researchers review it in parallel: an Evidence checker (is every claim true to the permitted source extracts?) and a Stakeholder reader (can your audience understand it and act on it?). Runtime varies with source length, service availability, and rate limits.
> 3. **Then I'll draft your Google Doc** — the formatted, verified plan in your confirmed Drive folder.
>
> Running the critique and multi-agent checks now — I'll fold in any fixes before the Doc is created.

If the Step 1 connection check found `multi-agent-check` isn't installed, or the source-use gate does not authorize reviewer processing, drop item 2 and say the plan gets the self-critique pass only.

**Override:** if the researcher explicitly requests a full draft for review at the end, skip row-by-row approval but still show the complete draft for approval, confirm the Drive destination, and perform every output and verification step.

## Step 3.5: Confirm the Google Drive Destination

A real run requires a Google Doc, so ask about location—not output format.

1. Infer the exact Drive folder from the supplied project context when possible.
2. Confirm the folder plainly: **“I’m going to create the research plan in [folder/link]. Is that the right destination?”**
3. If no destination is known, ask: **“Which Google Drive folder should this research plan live in?”**
4. Apply the destination gate in `references/source-and-delivery-safety.md`: confirm the **destination ACL** and **intended audience before any write or creation**. If access is broader, stop before writing and ask for a compliant folder or separately authorized sharing change.
5. Write only to the confirmed folder. Never use a hardcoded personal folder ID.
6. For a mock or demo, do not create a Drive artifact unless the tester explicitly asks for one.

## Step 4: Assemble the approved plan

Load `references/content-rules.md` and assemble the approved material in the exact contract below. Verify completeness, names, dates, and source-link coverage. Preserve the approved meaning and label uncertainty rather than guessing; the copyedit happens in the created Google Doc in Step 6.2.

Follow the working-file rules in `references/source-and-delivery-safety.md`: use a persistent **private, non-repository working directory**, not `/tmp`; set owner-only permissions; keep minimum necessary content; define retention and cleanup; and keep sensitive content out of command-line arguments.

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

Then add the separate Option 4 leadership timeline and the Project Plan Overview. The leadership timeline has one header plus four study-specific milestones derived from the approved detailed Timeline row. Each left-hand label is no more than 32 characters; each right-hand summary is one sentence and no more than 160 characters. The old reference study's four-week schedule is never reused.

```markdown
# Research Timeline

| Milestone | Leadership milestone |
|---|---|
| [Milestone 1] | [Concise study-specific summary.] |
| [Milestone 2] | [Concise study-specific summary.] |
| [Milestone 3] | [Concise study-specific summary.] |
| [Milestone 4] | [Concise study-specific summary.] |

*[One-sentence timing dependency or decision-point note.]*

---

# Project Plan Overview

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

The generic `Section / element | Approved content` row is a conversion aid only. Remove it from the Google Doc so Topic is the first visible overview row. Do not remove the visible leadership-timeline header.

The bundled normalizer rebuilds every multi-item table cell as clean paragraphs before native bullets and links are applied. Use it instead of accepting conversion artifacts or simplifying the layout. The durable executable example is `tests/fixtures/leadership-plan.md`; the contract validators are `tests/validate_contract.py` and `tests/test_option4_layout.py`.

## Step 4.5: Research-plan critique

Pressure-test the assembled plan before creating the final Doc. Run the checklist as a **self-critique** by default. Use a separate critique agent only when `references/source-and-delivery-safety.md` authorizes its processing and reviewer access, and provide only minimum necessary de-identified extracts. Fix clear gaps; present judgment calls to the researcher for Accept / Consider / Reject.

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

Do not append this internal critique to the stakeholder plan unless the researcher asks. Fold clear fixes into the assembled plan, then move to the multi-agent review before creating the Doc.

## Step 5: Multi-agent review

Run the multi-agent review on the fixed plan content before the Google Doc is created only when the Step 1 gate authorizes both AI processing and reviewer access. The review is automatic within that already confirmed boundary; do not ask twice.

- Say in chat: *"Running the multi-agent review now — two researchers read the plan in parallel: an Evidence checker against the sources, and a Stakeholder reader reading it as [audience]."*
- Check the live skill list, then invoke `/multi-agent-check` when it is installed. Follow the reviewer-packet rules in `references/source-and-delivery-safety.md`; never pass complete source files by default.
- Run `multi-agent-check` only when it is installed and that authorization is present; **otherwise, proceed critique-only without source files or content** handed to another reviewer. This is a complete run, not a blocked one; say “critique-only” when you return the Doc.
- If the installed review fails or rate-limits (including HTTP 429), preserve any complete reviewer result and retry only the missing transient call once when the tool reports that no duplicate work or external write can occur. Otherwise stop the review, fall back to the self-critique, and disclose `critique-only — multi-agent review failed`. Never loop, hide the failure, or call a partial review complete.
- **Runtime:** do not promise a duration. It varies with plan/source length, service availability, and rate limits.
- **Live demo:** either run the check without a time promise or walk through the fully synthetic `examples/multi-agent-review-example.md` and identify it as synthetic.
- Fold any confirmed fixes into the assembled plan before creating the Doc. **Check each fix's wording against the sources before applying it.** Apply only what the source supports: if a fix adds a fact, count, attribution, study detail, or quote the source doesn't support, apply the supported part and tell the researcher what you left out and why.

The expected sequence is **approved plan → critique → multi-agent (or disclosed critique-only) → fixes → copyedit → exact Option 4 Google Doc → verify/render → share**. Never describe the plan as stakeholder-final before the quality checks and the final visual gate have run.

## Step 6: Copyedit, create, normalize, format, verify, and render the Google Doc

A successful API response is not completion. The final link must point to the confirmed folder and pass the exact **Option 4 — Leadership** machine and visual checks.

### 6.1 Final copyedit and manifest

Copyedit the approved Markdown for clarity, grammar, complete sentences, consistent terminology, and unnecessary repetition. Preserve every approved claim, decision, row, and source link. Resolve `scripts/…` paths below from the directory containing this `SKILL.md`; every other file lives in the working folder from Step 4. Then generate the manifest:

```bash
python3 scripts/option4_layout.py manifest APPROVED.md manifest.json
```

The manifest command is a preflight gate. It fails when the required headings or sections are missing, the Appendix has extra rows, the timeline does not have four milestones, or a leadership-timeline summary is too long.

#### Full capability preflight — before creation

Run the preflight in `references/source-and-delivery-safety.md`. Before creation, prove that the authenticated integration can create/import, expose raw structure and revision, apply revision-bound updates, re-fetch/read back, render, and perform authorized cleanup or quarantine. A tool name or sign-in is not proof. If any capability is unverified, preserve the Markdown and block before creation.

### 6.2 Create in the confirmed folder

Record the confirmed folder, approved title, and attempt time. Import the Markdown as a dedicated one-tab Doc in that folder; capture the ID, URL, active tab, and raw JSON. Confirm two tables and one native horizontal rule. If import is malformed, apply the safety reference's partial-document policy before another attempt.

For an ambiguous create/import result, follow the idempotency procedure in `references/source-and-delivery-safety.md`: reconcile the known ID or the exact folder, title, and attempt-time window. **Never blindly retry a create or update.**

Fetch raw JSON into the protected working directory. If the integration cannot expose equivalent structure and indices, preserve the Markdown and **block completion**. Never return a partial document as final.

### 6.3 Normalize and apply the exact Option 4 layout

Generate and apply normalization operations:

```bash
python3 scripts/option4_layout.py normalize imported-doc.json manifest.json normalize-batch.json \
  --required-revision-id "$IMPORTED_REVISION_ID"
```

The normalizer validates the manifest version and digest, confirms that the imported leadership timeline plus every Project Plan Overview label and body still match the approved Markdown, rebuilds clean overview-cell paragraphs, removes the generic conversion header, and restores two physical cells for section bands. It blocks rather than rewriting pre-overview timeline text, because a length change there would invalidate later Google Docs table indices in the same native batch.

Immediately before each normalization or formatting write, fetch fresh raw JSON and its revision, bind the batch to that **required revision ID**, apply it through a protected request body, then re-fetch and verify. Follow the safety reference for conflicts and ambiguous results: never resend a stale batch; if the expected post-state is present, record success without resending; otherwise regenerate against the new snapshot. Material content changes require researcher reapproval. Block when reconciliation fails.

Generate and apply exact formatting operations:

```bash
python3 scripts/option4_layout.py format normalized-doc.json manifest.json format-batch.json \
  --required-revision-id "$NORMALIZED_REVISION_ID"
```

Apply `format-batch.json` with the same revision-bound sequence, then re-fetch again. This step must produce DM Serif Display/DM Sans typography, pageless editing mode with landscape-letter export geometry, one-inch print margins, the exact Option 4 colors and spacing, fixed 144pt / 554.4pt table columns, a repeating dark-green timeline header, a gray milestone column, white overview body cells, true bullets, active links, and dark-green two-cell section bands. The two columns intentionally total 698.4pt and extend 50.4pt beyond the 648pt paragraph text area; this matches the approved source and must not be “corrected” by shrinking the table.

The script emits native Google Docs API requests. An equivalent connected integration may apply the same operations directly. If the environment cannot apply an essential operation, **block completion**—do not simplify the design.

### 6.4 Verify and visually inspect

1. Read the document back as text with the connected Google Docs integration (for example, a Markdown or plain-text export) and compare it against every approved row and source link.
2. Inspect the active content tab's structure (tables, cell text, list paragraphs, and links) in freshly fetched raw document JSON, or with the integration's structure-inspection tool when it has one.
3. Run the hard verifier against newly fetched raw JSON:

```bash
python3 scripts/option4_layout.py verify final-doc.json manifest.json
```

4. Export or render the Google Doc and inspect all three:
   - the opening page;
   - at least one dense middle table page; and
   - the final Appendix page.
5. Confirm no clipping, illegible wrapping, orphaned section band, awkward timeline split, low contrast, or excess blank page. If the leadership timeline splits, tighten only its at-a-glance summaries; preserve the approved detailed Timeline row.
6. Correct every issue with the same fresh-fetch, revision-bound, regenerate-on-conflict sequence; then re-fetch, rerun the verifier, and re-render. Repeat until all checks pass.

A structural-only pass is insufficient. If raw verification or rendering is unavailable, **block completion** rather than returning an approximate document.

### 6.5 Return the verified document

Confirm the file location and return:

- the working Google Doc link;
- `content complete, Option 4 formatting checked, links checked, rendered pages checked` (add `critique-only review` when the multi-agent review couldn't run);
- no styling caveat—any unresolved styling limitation means the document is not final.

Open the verified Google Doc in the browser when the environment supports it. Do not update project trackers, progress files, or unrelated systems unless the researcher separately asks.

This is the final step. The plan has already passed the critique (Step 4.5) and the multi-agent review or its disclosed critique-only fallback (Step 5); only the exact verified Option 4 Google Doc is handed back.

## Resource routing

Use authorized enterprise search, Slack, people search, and approved data tools for evidence and stakeholder verification; use Drive/Docs only for the confirmed final destination. `references/content-rules.md` owns plan content, `references/source-and-delivery-safety.md` owns sensitive-source and write recovery, `references/research-plan-methodology.md` owns citation-level method rationale, and the Option 4 reference, JSON contract, script, and tests own final formatting. `examples/multi-agent-review-example.md` is synthetic demo material only.

The verified Google Doc is the primary output. A real run is incomplete until its location, content, links, exact Option 4 styling, and rendered pages have passed and its URL is returned.
