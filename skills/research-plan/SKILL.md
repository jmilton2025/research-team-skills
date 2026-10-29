---
name: research-plan
description: Use when a UX researcher is planning a new study, converting a brief or product requirements document into a research plan, or needs decision-focused objectives, methods, sampling, analysis, timing, and deliverables.
---

# Research Plan

Build a stakeholder-ready research plan collaboratively. Ground the plan in existing evidence, audit the decision it must inform, recommend the minimum valid method, and obtain researcher approval row by row. Every real run that passes the decision audit ends with a copyedited, formatted, verified Google Doc in the approved Drive location; a run stopped at the decision audit ends with a closed-decision note instead.

## Completion contract

A run is complete only when all of the following are true:

1. Existing context has been searched and sourced.
2. The researcher has approved every applicable plan row.
3. The critique pass has run, and the multi-agent review has run when it is installed and authorized and the researcher didn't skip it (otherwise the run is disclosed as critique-only, using the exact wording in Step 5), with fixes folded in.
4. The Google Drive destination has been confirmed.
5. The plan has gone through the **copyedit → create → normalize → Option 4 format → verify → render** pipeline.
6. The exact **Option 4 — Leadership** visual contract has passed, and a working Google Doc link has been returned with verification status.

The quality checks run before the Google Doc is drafted. Drive destination confirmation must happen before document creation.

Markdown is an intermediate representation, not the completed deliverable. A test run stays out of Drive unless the tester explicitly asks for a test document; without one, it ends with the approved Markdown and says no Doc was created.

## Flow overview

| Step | Work | Completion gate |
|---|---|---|
| **1** | Check connections and flag any sign-in (e.g., Glean) in the first message → gather the request without opening sources → audit the decision → authorize source use → set the run type from what the researcher said → announce the 3-section structure | Decision is genuinely open and actionable; sources and connections are authorized or skipped; researcher understands the workflow |
| **1.5** | **Section 1 — Context & Foundation:** discover background, existing insights, and hypotheses → three sequential pop-ups (Step 1 of 3, 2 of 3, 3 of 3), each checked against the content rules before it's shown and locked before the next | Background, Existing insights, and Hypotheses approved, and rule-compliant or recorded as an accepted exception |
| **1.6** | Fill only unresolved logistics; auto-draft title, date, and Topic; ask the researcher to confirm the key RACI people, then offer to add more | Opening approved |
| **2** | Recommend the minimum valid method direction and the conditional rows the study needs | Method direction picked (the rows are approved in Step 3) |
| **3** | **Section 2 — Research Design** (4 labeled steps: Objectives, Key research questions, Decisions, Method & approach) + **Section 3 — Outputs** (4 labeled steps) — one pop-up per step, "Brainstorm with me" always offered, transition announced after each lock; the Timeline step runs the `timeline` check before its pop-up | All remaining rows approved; no row approved twice; the timeline grid passes the `timeline` check |
| **3.5** | Confirm the Google Drive destination | Exact folder confirmed |
| **4** | Assemble the approved plan (markdown intermediate, saved in a persistent working folder) and run the `lint` check | Content complete; layout checks pass; the warning banner matches the run type |
| **4.5** | Auto-run critique checklist, starting from the `lint` results (announced at end of Step 3) | Gaps fixed or explicitly accepted |
| **5** | Show the review plan and ask once: run the multi-agent review or skip it — before the Doc. If it isn't installed or reviewer processing is not authorized, don't ask; disclose a critique-only run | Review complete (or critique-only disclosed with its reason); confirmed fixes folded in |
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

### Review surface — HTML review page first

When the Artifact tool is available, show drafts on the **editable HTML review page** in [`../../references/review-page/README.md`](../../references/review-page/README.md) instead of pop-ups. Build it with that folder's `review_page.py`, publish it with `capabilities: {"artifact": {}, "sample": {}}`, and republish the same file for each section (Section 1 — Context & Foundation, Section 2 — Research Design, Section 3 — Outputs), plus the gates between them (decision audit, method direction, Drive destination, review permission), so the researcher keeps one link. Each step or gate becomes one page item, with its step label unchanged. List-shaped rows (Background, Existing insights, Hypotheses, objectives, questions, guide blocks, findings, recommendations) are **bullet checklists**: present every proposed bullet first, with its source, then let the researcher keep, edit, remove, or add bullets (Select all / Clear all) and click **Accept selected**, or **Brainstorm with me** to work the card with a senior researcher on the page. Then they click **Send to Claude** and say **done** in chat. Read the page back and apply every decision under the same approval rules this skill sets for pop-ups: an edit is still checked against the content rules, and a missing decision is never approval. Quick yes/no confirmations may stay as pop-ups. When the Artifact tool isn't available, use the pop-ups below. Say which surface the run is using right after intake.

Use native `AskUserQuestion` checklist pop-ups when available, within the tool's limits:

- Ask one decision per pop-up.
- **At most 4 options per pop-up.** “Brainstorm with me” takes one slot, so show up to 3 content options. When a row has more items than fit (e.g., six background facts), list them all, numbered, in chat first; then offer grouped options (e.g., “Keep all 6 (Recommended)”, “Keep 1–4, drop 5–6”) and let the researcher name specific items in the comments field.
- **Use `multiSelect: true` only when the options can be combined** (e.g., which insights to keep, which fixes to apply). Use single-select for either/or choices (e.g., which method direction, which Drive folder).
- Put the **Recommended** option first, with “(Recommended)” in its label. Base it on the PRD and discovered evidence.
- Keep the built-in **Other / comments** field so researchers can add, correct, or rewrite. The tool adds it automatically; don't add your own “Other” option.
- Show the proposed content in chat before the pop-up. Options are short labels, not the content itself.
- **Offer “Brainstorm with me” as the last option in every approval pop-up.** It opens a short chat exchange on that specific item, then re-shows the revised draft for approval before advancing. In that exchange, talk like a **senior UX researcher brainstorming with a colleague**: lead with a point of view, offer 2–4 concrete ideas with their tradeoffs, ask 1–2 sharp questions, and name one risk to watch, grounded only in the run's sources ([`../../references/review-page/README.md`](../../references/review-page/README.md) § Brainstorm with me).
- Label every pop-up with its section and step in the question text: **“Section 1 > Step 2 of 3: Existing Insights”**. The researcher must always know exactly where they are. Pop-ups outside the three sections use their own short name instead, such as **“Opening: Title, Date & RACI”**, **“Method direction”**, or **“Drive destination”**. (The short header chip holds at most 12 characters, so the full label goes in the question.)
- Do not advance until the current item is approved, unless the researcher explicitly requests the whole-draft approval override in Step 3.

If native pop-ups are unavailable, state **“Inline fallback — native checklist unavailable in this environment”** and reproduce the same numbered options and selection instructions in chat. Do not silently substitute an unlabeled prose question.

## Option 4 — Leadership Google Docs contract

The skill must produce the same leadership-ready visual system for every researcher. It matches the visual design of the approved International retailer research plan (Q3 2025); runtime access to that private Doc is neither assumed nor required.

- **This layout is the default, not a choice.** Every real run's final Doc uses this layout automatically. Don't ask the researcher which style or template to use, and don't apply any other template on top, even one the researcher's own settings name as their default for new Google Docs; that default covers their other Docs, not research plans.
- Use the bundled machine-readable contract in `references/option4-style-contract.json` and the executable pipeline in `scripts/option4_layout.py`.
- Build the exact hierarchy: concise opening → native rule → **Research Timeline** Gantt grid (`Phase | Activity | one column per week`) with its color legend → native rule → **Project Plan Overview** table.
- Apply DM Serif Display and DM Sans, the exact colors, pageless editing mode with landscape-letter export geometry, one-inch print margins, fixed table widths, the green / yellow / red week fills, pale-yellow warning treatment, white body cells with 0.75pt black borders, and merged dark-green Title Case section bands.
- Keep adaptive study content, phases, and week labels; never copy wording, dates, week labels, people, or findings from the reference plan.
- Run the bundled verifier and inspect rendered pages. Structural similarity or a successful API response is not enough.
- If the connected environment cannot apply or verify the exact contract, preserve the approved draft and **block completion**. Do not return a standard-font, one-table, generic-color, list-style timeline, unmerged-band, or structural-only fallback as final.
- This visual gate is not researcher-, stakeholder-, or leadership-waivable. An instruction to accept a downgrade still blocks final delivery; return the approved draft as blocked, not an approximate Google Doc as final.

## Step 1: Gather study inputs and orient the researcher

### Connection check — first, before any questions

Start the run here. Check each connection the run depends on, with a quick authentication or metadata call rather than trusting the tool list (a listed tool can still ask for sign-in; Claude Code also reports servers that need authentication when the session starts). This connection check must not open or retrieve source content; content access starts only under the source-use authorization gate below. If a connector's only tools return content (search or chat, as with most Glean servers), don't run a test query: use the session's sign-in report or its `/mcp` status, and treat the first authorized query in Step 1.5 as the live check.

| Connection | Needed for |
|---|---|
| Enterprise search (e.g., Glean) | Prior research, supplied internal docs (Steps 1–1.5) |
| Research-insights agent | Prior findings (Step 1.5) |
| Google Drive / Docs (connector or `gws`) | Reading supplied docs; creating and verifying the final Doc (Step 6) |
| Slack | Supplied kickoff threads; check only when a Slack link comes up |
| `multi-agent-check` skill | The multi-agent review (Step 5); check the live skill list |

**Flag every missing or signed-out connection in your first message**, so the researcher can sign in while you gather inputs instead of finding out halfway through discovery. That covers every row above except Slack. Name the connection, say what it's for, and give the sign-in steps. Glean is the one most often signed out; for any other connection, use the same steps with its name swapped in:

> **Glean isn't signed in.** I use it to find prior research and the internal docs you share. To sign in, type this in Claude Code (the chat box you're using now):
>
> ```
> /mcp
> ```
>
> Pick **glean** (if the list shows more than one Glean entry, such as `glean` and `glean_default`, do this for each one marked as needing sign-in), choose **Authenticate**, finish signing in on the browser tab that opens, then come back and say **done**. On claude.ai, connect it from your connector settings instead. Or say **skip Glean** to continue without it.

Continue with the inputs, decision audit, and source-use gate while the researcher signs in; none of them needs a connection. When a new source type comes up later (a Slack thread, say), check that connection the moment it's mentioned and flag it the same way. Re-check right before discovery: if a connection is still missing, wait for sign-in or an explicit skip, then report connected and skipped sources. A skipped connection's sources stay unverified and cannot support a claim. Missing Docs write access means the run will end with a blocked draft, and missing `multi-agent-check` means a critique-only review, disclosed as `critique-only review — multi-agent-check not installed`.

### Request inputs — metadata and links only

Ask first for metadata and links only: what artifacts exist (product requirements document, brief, kickoff notes, Slack thread, design, technical framework, or prior plan) plus a non-sensitive description of the request. Tell the researcher not to paste, upload, or expose non-public content until the source-use authorization gate passes. Collect links without opening or searching them.

### Decision audit — before discovery

Ask what decision the study will inform, then challenge it before reading prior evidence:

- Is there one primary “must answer” decision?
- Is it a real fork—a different finding leads to a different action?
- Is the decision still open, answerable in the available time, and owned by a named person?
- **Is it researchable?** Split the ask into three parts before planning: what a study can answer, what needs instrumentation, analytics, or a data partner instead, and what is a product decision that no study will change. Plan only the first part; name the other two in Dependencies & guardrails so the requester can route them. If nothing researchable remains, say so with reasoning the researcher can forward, and use the closed-decision branch below.

If the request is only a goal such as “inform strategy” or “understand users,” propose a sharper decision and ask for approval. If the answer has already been chosen, do not run discovery under confirmatory framing. Offer three explicit branches in one single-select pop-up labeled **“Decision audit”**, with **“Brainstorm with me”** last. Recommend **Reopen or reframe** when the requester is open to changing the direction; otherwise recommend **Measure implementation risk**:

1. **Reopen or reframe** a genuine decision fork that evidence could change.
2. **Measure implementation risk** without pretending the research selects the already-chosen direction.
3. **Document the decision as closed and stop** the research-plan workflow. Write a short closed-decision note in chat: the decision, its owner, the date, and why research won't change it. No Google Doc is created.

If the requester still insists, after that choice, that research justify a closed answer, refuse that framing and stop. Continue only after an open, actionable decision is approved.

### Source-use authorization gate

Read `references/source-and-delivery-safety.md` and complete its authorization gate before accessing any non-public source. **Connector access is not requester authorization.** Record the authorization basis, approved AI processing, intended audience and source ACL, quote/link disclosure, minimum necessary de-identification, and provenance. If any required authorization is unknown, stop before reading that source; ask the researcher to confirm it or skip it. A skipped source remains unverified, cannot support a claim, and stays out of the plan, Appendix included. An authorization the researcher gives later in the run counts from then on; record it with the others.

### Run type — set by what the researcher says

Don't ask about the run type. A run is a test only when the person starting it says so (a mock test, test, demo, pressure scenario, or regression run); otherwise it's a real study. Set the warning banner (see Step 4) now, so it's right from the first draft:

- **Test on invented inputs** (a made-up brief, sample scenario, or fixture) → TEST ARTIFACT banner.
- **Any other test**, including one on real, authorized project inputs → TEST RUN banner.
- **Not called a test** → real study, no banner.

### Announce the three sections

Before discovery, say in chat:

> Now that you’ve shared your document, I’ll pull relevant prior research and materials, then we’ll build this plan together — one step at a time.
>
> **We’ll work in three sections:**
>
> **Section 1 — Context & Foundation** *(what we already know)*
> Background · Existing Insights · Hypotheses
>
> *The primary decision is set. After Section 1, I’ll draft the title, date, and Topic, and ask you to confirm the key people for the RACI.*
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

Before each pop-up, check the draft against that row's rules in `references/content-rules.md` and fix it first. A pop-up approves content; it doesn't waive the rules. Only the researcher's explicit choice to keep a version after you've named the rule does that, and Step 4.5 then records it as an accepted exception. Step 4's `lint` check catches anything that slips through, but by then the researcher has already approved it, so fixing it means asking again.

**Section 1 > Step 1 of 3: Background & Context**

Say in chat: *“Let's start with background and context — here's what I found from your PRD and prior research.”*

Show concise source-backed facts in chat, numbered. The row holds 3–6 bullets, and the first bullet's bold lead-in is **Why now**, ending with **Strategic fit:** and the priority a source names, or `[TBD — fill in]` when no source names it. Likewise, when no source says why now, the bullet reads `**Why now:** [TBD — fill in]`; never invent a reason. When you find more than 6 facts, merge related ones or move in-flight work to Dependencies & guardrails; the Recommended option must be a compliant set. Pop-up label: **“Section 1 > Step 1 of 3: Background & Context”**. The researcher picks which facts to keep, so use multi-select (grouped when there are more than 3 facts), with **“Brainstorm with me”** last. If the researcher's picks break the rule (more than 6 bullets, or no Why now first), name the rule, show a merged draft that keeps every fact they picked, and ask once more with the same label, offering **“Use the merged draft (Recommended)”**, **“Keep my picks as they are”**, and **“Brainstorm with me”**. If they keep their picks, lock them and say it's recorded as an accepted exception; don't ask a third time. Lock before advancing.

After approval, say: *“Background & Context locked. Moving on to Existing Insights.”*

---

**Section 1 > Step 2 of 3: Existing Insights**

Show up to five prior findings in chat with source links; show fewer when fewer relevant findings exist. Quote marks mean word for word from the cited source artifact (the report, transcript, product requirements document, or doc itself) opened in this run. Never quote internal notes, memory, summaries, trackers, or session notes, and never put quote marks around your own paraphrase. Paraphrase without quote marks and cite the artifact instead; if you can't check a line against the artifact, paraphrase it. Pop-up label: **“Section 1 > Step 2 of 3: Existing Insights”**. Multi-select for which findings to keep (grouped when there are more than 3), with **“Brainstorm with me”** last. Lock before advancing.

After approval, say: *“Existing Insights locked. Moving on to Hypotheses.”*

---

**Section 1 > Step 3 of 3: Hypotheses**

Show proposed, falsifiable beliefs grounded in evidence or explicit stakeholder assumptions. Label each one's origin: a researcher hypothesis inferred from a named source, or a stakeholder assumption only when a stakeholder actually stated it. Check that every hypothesis carries its italic origin label before the pop-up. If none are grounded yet, propose the explicit empty state: *“No hypotheses confirmed at planning time.”* Pop-up label: **“Section 1 > Step 3 of 3: Hypotheses”**. Multi-select for which hypotheses to keep (grouped when there are more than 3), with **“Brainstorm with me”** last. Lock before advancing.

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

Auto-draft the breadcrumb, title, date, and one-sentence Topic from the inputs. Insert the TL;DR placeholder automatically; do not ask the researcher to draft findings.

**Ask the researcher for the RACI instead of looking people up.** The researcher knows who is on the study today, so asking is faster and more accurate than a search. Pre-fill a role only with a name the researcher has given in this run: in the brief, product requirements document, or kickoff notes they shared, or in their answers so far (the decision audit names the decision owner). Don't run a people or directory search, and don't carry names over from memory or older project files.

0. **Pull every stakeholder from the supplied docs.** Before asking, extract every person the PRD, brief, kickoff notes, or shared thread names: owners, approvers, PM/EM/design/data leads, partners, and anyone tagged for review. Map each to the RACI role their source implies, and note where you found them (`from PRD`). Capture as many names as the sources give; don't drop someone because their role already has a name. Mark the main DRI — the person who drives the study day to day, usually the Responsible researcher unless a source names someone else — with `(DRI)` after their name. Show the pre-filled RACI in chat so the researcher can confirm, add, edit, or move anyone.
1. **Key people first.** If any of the four roles has no name yet, ask for it in chat, one name per role: Responsible (usually the researcher), Accountable (the decision owner), Consulted, and Informed.
2. **Confirm the opening once.** Show the complete opening (breadcrumb, title, date, RACI, and Topic). Topic appears in the Doc as the first overview row, but it's confirmed here with the opening. Pop-up label: **“Opening: Title, Date & RACI”**, with the options **“Confirm as shown (Recommended)”**, **“Add more people”**, and **“Brainstorm with me”**. Corrections go in the comments field.
3. **Then offer more people.** If the researcher picks “Add more people,” collect the extra names and roles in chat (a role can hold more than one name), then show the updated RACI in chat and ask them to reply **confirm** or correct it. This finishes the same opening approval; don't show the pop-up again.

This is the only time the opening is approved. Include all four RACI roles; a role the researcher leaves blank stays `[TBD — fill in]`.

## Step 2: Recommend the minimum valid research design

Start with the minimum evidence needed to move the approved decision—not the most comprehensive study possible. Explain why it is sufficient, then offer up to two meaningful alternatives, such as faster/lower-confidence and slower/higher-confidence.

Choose the method family based on the evidence need:

- **Generative:** interviews, fieldwork, or diary study for motivations, mental models, and context.
- **Descriptive:** survey, analytics, or structured observation for prevalence and distribution.
- **Evaluative:** moderated or unmoderated usability, concept test, or benchmark review for a specific solution.
- **Causal:** randomized experiments or defensible quasi-experiments when the decision requires causal inference. Mixed methods may explain mechanisms but are not inherently causal.
- **Human/model evaluation:** calibration, independent evaluation, adjudication, and separate blind validation when adoption depends on agreement or quality evidence.

Make the recommendation arguable:

- **Name what each method will and won't tell the team.** Every method has a blind spot (interviews don't show actual behavior or reliable willingness to pay; analytics don't explain why). State it in the method-direction pop-up so the researcher can weigh it.
- **Name the alternatives you passed over and why**, so the choice can be challenged in review.
- **Map each method to the key research questions it answers.** A method that answers none is cut; a question no method answers is a gap to fix now.
- **Don't add methods by reflex.** Recommend a second method only when one method cannot answer an approved question. When a plan mixes generative and evaluative work, keep the two strands visibly separate.
- **Recommend inside the stated constraints** (budget, panel access, unmoderated-only), and say when a constraint is what forces a weaker design.

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
3. **What decisions will be made with this research?** — multi-select; each decision fork is its own option (grouped when there are more than 3). Define each outcome once (for example, go / narrow / no-go) as proposed definitions to confirm with the decision owner, then reuse those exact terms in every later row. Pop-up label: **“Section 2 > Step 3 of 4: What Decisions”**. After lock: *“Decisions locked. Moving on to Method & Approach.”*
4. **Method & approach** + applicable conditional rows — Pop-up label: **“Section 2 > Step 4 of 4: Method & Approach”**. After lock: *“Method locked. Section 2 — Research Design is complete. Moving on to Section 3 — Outputs.”*

Use **Hypotheses** only. Keep Key research questions broad and project-level; interview probes belong in the downstream moderation guide. The Project Details fields are adaptive — include only the rows the study actually needs.

---

### Section 3 — Outputs *(announce: “Section 2 is locked. Now for the final section — Outputs.”)*

Approve in this order:

1. **What does success look like? + Dependencies & guardrails** — Pop-up label: **“Section 3 > Step 1 of 4: Success & Guardrails”**. After lock: *“Success & Guardrails locked. Moving on to Deliverables.”*
2. **Deliverables** — Pop-up label: **“Section 3 > Step 2 of 4: Deliverables”**. After lock: *“Deliverables locked. Moving on to Timeline.”*
3. **Timeline** — Draft the detailed Timeline row and the Research Timeline grid together (format in Step 4's output contract). The grid has one row per activity, grouped into numbered phases, and one column per week of the study, labeled with the week's start date (`Nov. 3`), or `Week N` until dates are set. Mark each week cell `[target]`, `[spillover]`, or `[event]`, or leave it blank, and derive every mark from the detailed row. Save the draft grid in the private working folder (the working-file rules in Step 4 apply from here), then run:

   ```bash
   python3 scripts/option4_layout.py timeline TIMELINE.md
   ```

   Resolve `scripts/…` from the directory containing this `SKILL.md`; `TIMELINE.md` is the draft in the working folder. The file may hold just the grid table. The check prints one line per week label, phase, activity, and week note (`OK` or `WRAP`, with its measured fit) and a `FAIL:` line for each problem: a label too wide for its column, a Phase cell that isn't `Phase N: Name` in order, a week cell that isn't blank or a status token, or an `[event]` week that doesn't cover every row. Fix every reported line without changing its meaning, tell the researcher what you shortened, and rerun until it prints `PASS`. Then show both the detailed row and the grid in chat for one approval. Pop-up label: **“Section 3 > Step 3 of 4: Timeline”**. After lock: *“Timeline locked. Moving on to Next Steps & Appendix.”*
4. **Next steps + Additional UXR documents + Resources from XFN** — Pop-up label: **“Section 3 > Step 4 of 4: Next Steps & Appendix”**. Auto-sort every relevant kickoff document into Additional UXR documents or Resources from XFN. Existing documents use real links; future artifacts are labeled “to be created” without fake links.

After all three sections are locked, tell the researcher exactly what happens next so they know what to expect:

> All three sections are approved — I now have everything I need. Here's what I'll do before I hand you the final plan:
>
> 1. **Run a critique pass** — a pressure-test that checks the plan for gaps, weak logic, and unsupported claims. I will self-critique unless the authorized source-use boundary permits a separate critique reviewer.
> 2. **Offer the multi-agent review** — independent reviewers check the plan against the permitted source extracts and read it as your audience would. I'll show you who reviews it and what each reviewer sees, then ask once: run it, or skip it and go critique-only.
> 3. **Then I'll draft your Google Doc** — the formatted, verified plan in your confirmed Drive folder.
>
> Running the critique pass now — I'll fold in any fixes before the review question.

If the Step 1 connection check found `multi-agent-check` isn't installed, the source-use gate does not authorize reviewer processing, or the researcher already asked to skip the review, drop item 2 and say the plan gets the critique pass only, with the reason. End that message with “Running the critique pass now — I'll fold in any fixes before I draft your Google Doc.”

**Override:** if the researcher explicitly requests a full draft for review at the end, skip row-by-row approval but still show the complete draft for approval, confirm the Drive destination, and perform every output and verification step.

## Step 3.5: Confirm the Google Drive Destination

A real run requires a Google Doc, so ask about location—not output format.

1. Infer the exact Drive folder from the supplied project context when possible.
2. Confirm the folder plainly: **“I’m going to create the research plan in [folder/link]. Is that the right destination?”**
3. If no destination is known, ask: **“Which Google Drive folder should this research plan live in?”**
4. Apply the destination gate in `references/source-and-delivery-safety.md`: confirm the **destination ACL** and **intended audience before any write or creation**. If access is broader, stop before writing and ask the researcher to pick a compliant folder or have the folder's owner narrow its sharing; never change sharing yourself. Steps 4–5 don't need the folder, so continue them while this is resolved; only creation waits.
5. Write only to the confirmed folder. Never use a hardcoded personal folder ID.
6. For a mock or demo, do not create a Drive artifact unless the tester explicitly asks for one.

## Step 4: Assemble the approved plan

Load `references/content-rules.md` and assemble the approved material in the exact contract below. Verify completeness, names, dates, and source-link coverage. Preserve the approved meaning and label uncertainty rather than guessing; the copyedit happens in the created Google Doc in Step 6.2.

Follow the working-file rules in `references/source-and-delivery-safety.md`: use a persistent **private, non-repository working directory**, not `/tmp`; set owner-only permissions; keep minimum necessary content; define retention and cleanup; and keep sensitive content out of command-line arguments.

### Warning banner

Place the banner for the run type set in Step 1 after the RACI block, copied exactly:

| Run type | Banner |
|---|---|
| Test on invented inputs (made-up brief, sample scenario, or fixture) | `⚠️ TEST ARTIFACT — mock inputs, not a real study. Do not use as a deliverable.` |
| Any other test, including one on real, authorized inputs | `⚠️ TEST RUN — real, authorized inputs, created to test the workflow. Not a stakeholder deliverable.` |
| Not called a test (real study) | No banner |

The builder accepts only these two lines; any other line starting with ⚠️ fails the manifest. Keep the banner prominent in every rendered option.

### Output contract

The opening order is:

1. Title-case breadcrumb.
2. Research-plan title.
3. Last-updated date.
4. RACI bullet list.
5. Warning banner, when applicable.
6. Optional short context note, only when the plan needs a historical or interpretation caveat (styled as a small italic gray line).

Then a `---` rule, the **Research Timeline** grid with its legend note, a second `---` rule, and the Project Plan Overview. Each `---` needs a blank line above it; the import turns each into a native horizontal rule.

The Research Timeline is a Gantt grid derived from the approved detailed Timeline row, in this Markdown form:

- **Header:** `Phase | Activity`, then one column per week, labeled with the week's start date (`Nov. 3`) or `Week N`. The grid holds at most 12 week columns (54pt each, so 900pt at most). For a longer study, keep the weeks that matter and replace one run of middle weeks with a single `…` column, never the first or last.
- **Phase cell:** `**Phase 1:** Short name` on the first row of a phase. Leave the Phase cell blank on the phase's later rows; the Doc merges the Phase cell down across them. Number phases 1, 2, 3 in order.
- **Activity cell:** a short plain name (`Calibration`). It may wrap to two lines of the 72pt column, but no word may be wider than the column.
- **Week cell:** blank (white), or a status token, optionally followed by a short note of one or two words: `[target]` (green, a target week), `[spillover]` (yellow, possible spillover), `[event]` (red, a fixed event), or `[target] Human raters`. An `[event]` week marks every row of that week.
- **Legend note:** the italic line under the grid ends with `; Green = target dates; Yellow = possible spillover`, plus `; Red = <the fixed event>` when the grid has `[event]` weeks. The Doc shades the words Green, Yellow, and Red with their colors.

The builder measures every label in DM Sans 10pt against its column: week labels on one line of 50pt (bold), phase names on one line of 170pt (bold), activities in at most two lines of 62pt, and week notes in at most two lines of 44pt. When a label is too wide, shorten it yourself without changing its meaning (the activity `Recruit & screen participants` needs three lines and becomes `Recruit & screen`), then tell the researcher what changed; don't ask them to count characters. A shortening that keeps the meaning isn't a material change and needs no reapproval; if no short name keeps it, ask the researcher. The `timeline` check at Section 3 > Step 3 runs these checks, so the approved grid should already pass. Never reuse a reference study's phases, weeks, or schedule.

After assembling, run the layout check on the whole draft:

```bash
python3 scripts/option4_layout.py lint APPROVED.md
```

It prints `FAIL:` for layout problems the builder would reject (missing sections or rules, a timeline grid problem, a legend that doesn't match the grid, an unrecognized banner); fix those before moving on. `FIX OR ACCEPT:` lines are content-rule gaps (for example, Background without a Why now bullet, or a hypothesis without an origin label), and `CONFIRM QUOTE:` lines list every quoted phrase of four or more words. Both feed the Step 4.5 critique. It prints `PASS` when there is nothing to report.

```markdown
---

# Research Timeline

| Phase | Activity | [Mon. D] | [Mon. D] | [Mon. D] | [Mon. D] |
|---|---|---|---|---|---|
| **Phase 1:** [Short name] | [Activity] | [target] | [target] | [event] | |
| | [Activity] | | [target] [Note] | [event] | [spillover] |
| **Phase 2:** [Short name] | [Activity] | | | [event] | [target] |

*Note: [Timing dependency or caveat]; Green = target dates; Yellow = possible spillover; Red = [fixed event]*

---

# Project Plan Overview

| Section / element | Approved content |
|---|---|
| **Topic** | [One-sentence leadership framing.] |
| **TL;DR summary of findings** | *To be filled out at the end of the study.* |
| **Key Information** | |
| **Background** | [True bullet paragraphs.] |
| **Existing insights** | [Sourced bullet paragraphs.] |
| **Objectives** | [True bullet paragraphs.] |
| **Key research questions** | [True bullet paragraphs.] |
| **Hypotheses** | [True bullet paragraphs.] |
| **What decisions will be made with this research?** | [True bullet paragraphs.] |
| **Project Details** | |
| **Method & approach** | [True bullet paragraphs for methods or phases.] |
| **[Conditional row]** | [Include only when relevant.] |
| **What does success look like?** | [Contextual decision-readiness or evidence definition.] |
| **Dependencies & guardrails** | [True bullet paragraphs.] |
| **Deliverables & Next Steps** | |
| **Deliverables** | [True bullet paragraphs.] |
| **Timeline** | [True bullet paragraphs.] |
| **Next steps** | [True bullet paragraphs.] |
| **Appendix** | |
| **Additional UXR documents** | [Relevant UX research–owned links/artifacts only.] |
| **Resources from XFN** | [Relevant partner-owned links/resources only.] |
```

Use separate markdown list lines in multi-item cells during assembly: `- ` items separated by `<br>`, with two leading spaces after the `<br>` for each nesting level (`<br>  - Sub-point`), or `1. ` items for a numbered list where order matters. In Google Docs, convert and verify them as true Google Docs bullet paragraphs (`●` `○` `■`), or numbered list paragraphs (`1.` / `1.1.`), 36pt deeper per level. Do not use arrow chains, typed bullet glyphs, or dense run-on sentences as a substitute.

The generic `Section / element | Approved content` row is a conversion aid only. Remove it from the Google Doc so Topic is the first visible overview row. Do not remove the visible timeline header row.

The bundled normalizer rebuilds every multi-item table cell as clean paragraphs before native bullets and links are applied. Use it instead of accepting conversion artifacts or simplifying the layout. The durable executable example is `tests/fixtures/leadership-plan.md`; the contract validators are `tests/validate_contract.py` and `tests/test_option4_layout.py`.

## Step 4.5: Research-plan critique

Pressure-test the assembled plan before creating the final Doc. Run the checklist as a **self-critique** by default. Use a separate critique agent only when `references/source-and-delivery-safety.md` authorizes its processing and reviewer access, and provide only minimum necessary de-identified extracts. Fix clear gaps; present judgment calls to the researcher for Accept / Consider / Reject.

Start from the Step 4 `lint` output: every `FIX OR ACCEPT` line is either fixed or explicitly accepted by the researcher, and every `CONFIRM QUOTE` line is resolved under Quote provenance below.

| Dimension | Check |
|---|---|
| **Strategic alignment** | One clear primary decision; each objective and question changes that decision. |
| **Existing evidence** | Claims are sourced; completed findings are separated from in-flight work. |
| **Quote provenance** | Every quoted phrase is confirmed word for word against the cited source artifact opened in this run; otherwise it is paraphrased without quote marks. Never confirm a quote against internal notes, memory, summaries, or trackers. |
| **Content rules** | Background has 3–6 bullets and opens with Why now and Strategic fit; every hypothesis has its origin label; each row follows `references/content-rules.md`. |
| **Objectives and questions** | Objectives are statements; questions are broad, concise, and mapped to objectives. |
| **Hypotheses** | Beliefs are explicit, falsifiable where possible, and grounded rather than invented. |
| **Method fit** | The method is the leanest valid path; alternatives and confidence tradeoffs were considered. |
| **Sample / evaluator viability** | Behavioral criteria, independence, exclusions, coverage, and feasibility are appropriate when applicable. |
| **Measures and analysis** | Each measure or analytical step supports the decision; thresholds are evidence-based rather than universal defaults. |
| **Timeline realism** | Approval, recruiting or setup, fieldwork/evaluation, analysis, and readout fit the dates. |
| **Deliverable fit** | Each artifact helps a named decision-maker act. |
| **Ethics and Responsible AI** | Consent, privacy, fairness, accessibility, security, attribution, and human authority are protected. |
| **Misinterpretation risk** | The plan names the most important limitation, assumption, and over-generalization risk. |
| **Researchability** | Parts of the ask that need analytics or instrumentation, or that are already-made product decisions, are named and routed rather than planned as research. |
| **Method limits** | Method & approach says what the chosen method won't tell the team; every method maps to at least one key research question, and every question has a method. |
| **Conclusiveness risk** | Dependencies & guardrails names what could leave the study inconclusive (no-shows, a low-incidence segment, an unstable prototype, a segment the decision depends on but the sample won't cover), each with a mitigation, and says what happens if results are mixed. |
| **Field readiness** | Participant studies budget for no-shows, a pilot session, and analysis time that is not squeezed into the readout week. |

Do not append this internal critique to the stakeholder plan unless the researcher asks. Fold clear fixes into the assembled plan, then move to the multi-agent review before creating the Doc.

## Step 5: Multi-agent review

Offer the multi-agent review on the fixed plan content before the Google Doc is created, and ask about it exactly once.

1. **When not to ask.** If `multi-agent-check` isn't installed, or the Step 1 gate doesn't authorize both AI processing and reviewer access, don't ask: proceed critique-only and record the matching status below. If the researcher already said earlier in this run to skip the review, don't ask again; record the skip.
2. **Show the review plan in chat.** Check the live skill list and read the installed `multi-agent-check` SKILL.md, because installs differ: the team version runs two reviewers (an Evidence checker and a Stakeholder reader), while a personal install may run more lenses or add its own steps. Name the reviewers that install will run and the permitted extracts each one receives, following the reviewer-packet rules in `references/source-and-delivery-safety.md` (no complete source file unless the recorded authorization covers sending that whole file to reviewers). Don't promise a runtime.
3. **Ask one pop-up.** Label: **“Step 5: Multi-agent review”**. Options: **“Run the review (Recommended)”**, **“Skip review (critique-only)”**, and **“Brainstorm with me”** last. A focus area for the reviewers goes in the comments field.
4. **That answer is the review's only question.** If the installed check has its own pre-flight approval, the plan you showed is that plan and “Run the review” is its approval: don't show the plan or ask for approval again, and pass that answer on if the check asks for approval anyway. Answer its clarifying questions from the researcher's comments, or with “no special focus” when it asks for a focus and there is none. Never answer a factual question for the researcher (for example, whether a sample size is final). Ask the researcher again only for a decision the pop-up didn't cover, such as that kind of factual question or a source the reviewers can't reach. Put all of these in one pop-up labeled **“Step 5: Reviewer questions”**, one question each, offering the likely answers as options (the comments field takes anything else) and no “Brainstorm with me” option, since they're factual. These come after the “Running the multi-agent review now” message, while the check sets up. (The team version already skips its own confirmation when another skill calls it.)

Then:

- After the researcher picks **Run the review**, say in chat: *“Running the multi-agent review now — [the reviewers from the plan you showed].”* and invoke `/multi-agent-check` with the extracts from the plan.
- Run `multi-agent-check` only when it is installed, that authorization is present, and the researcher didn't skip it; **otherwise, proceed critique-only without source files or content** handed to another reviewer. This is a complete run, not a blocked one; disclose the status when you return the Doc.
- If the installed review fails or rate-limits (including HTTP 429), preserve any complete reviewer result and rerun only the failed reviewer, once (reviewers only read, so this can't duplicate a write). If that fails too, stop the review, fall back to the self-critique, and record `critique-only review — multi-agent review failed`; still fold in the completed reviewers' fixes as below, and name those reviewers when you return the Doc. Never loop, hide the failure, or call a partial review complete.
- **Runtime:** do not promise a duration. It varies with plan/source length, service availability, and rate limits.
- **Live demo:** either run the check without a time promise or walk through the fully synthetic `examples/multi-agent-review-example.md` and identify it as synthetic.
- Fold any confirmed fixes (the ones the review kept after its own checks) into the assembled plan before creating the Doc. Apply them without asking one by one and list what you changed; ask the researcher only about a fix that changes meaning, using Step 4.5's Accept / Consider / Reject. **Check each fix's wording against the sources before applying it.** Apply only what the source supports: if a fix adds a fact, count, attribution, study detail, or quote the source doesn't support, apply the supported part and tell the researcher what you left out and why.

Record exactly one review status and repeat it word for word when you return the Doc (Step 6.5):

| Review status | When |
|---|---|
| `multi-agent review complete` | The installed review ran with independent reviewers and finished. |
| `self-review only — independent reviewers unavailable here` | The installed check ran but reported that it couldn't use independent reviewers in this environment. |
| `critique-only review — multi-agent review skipped at researcher's request` | The researcher picked **Skip review (critique-only)** or asked to skip it earlier in the run. |
| `critique-only review — multi-agent-check not installed` | The skill isn't in the live skill list. |
| `critique-only review — reviewer processing not authorized` | The Step 1 gate didn't authorize AI processing or reviewer access. |
| `critique-only review — multi-agent review failed` | The review failed or rate-limited, and the one allowed retry didn't recover it. |

The expected sequence is **approved plan → critique → multi-agent (or disclosed critique-only) → fixes → copyedit → exact Option 4 Google Doc → verify/render → share**. Never describe the plan as stakeholder-final before the quality checks and the final visual gate have run.

## Step 6: Copyedit, create, normalize, format, verify, and render the Google Doc

A successful API response is not completion. The final link must point to the confirmed folder and pass the exact **Option 4 — Leadership** machine and visual checks.

### 6.1 Final copyedit and manifest

Copyedit the approved Markdown for clarity, grammar, complete sentences, consistent terminology, and unnecessary repetition. Preserve every approved claim, decision, row, and source link. Resolve `scripts/…` paths below from the directory containing this `SKILL.md`; every other file lives in the working folder from Step 4. Then generate the manifest:

```bash
python3 scripts/option4_layout.py manifest APPROVED.md manifest.json
```

The manifest command is a preflight gate. It fails when the required headings, rules, or sections are missing, a section band isn't Title Case, the Appendix has extra rows, the timeline header isn't `Phase | Activity` plus 1 to 12 week columns, a Phase cell isn't `Phase N: Name` in order, a week cell isn't blank or a status token, an `[event]` week doesn't cover every row, a grid label is too wide for its column, the legend note doesn't match the grid, or the warning banner isn't one of the two approved lines. A too-wide error lists every label that doesn't fit, with its measured width; shorten each one as described in Step 4, tell the researcher, and rerun the command.

The manifest also records a fingerprint of the layout script and style contract. The later `normalize`, `format`, and `verify` steps fail with “Skill files changed since this manifest was generated” if either file changed mid-run, because a different builder could produce a different Doc. Don't pull, update, or edit the skill during a run. If you see that error, tell the researcher the skill was updated mid-run and re-read the changed skill files, since the update may change later steps too. Then rerun the `lint` check and the manifest command (the update may have changed the rules either one applies), fix anything they now flag and tell the researcher what changed (re-confirm only a change that alters meaning, as in Step 4), and regenerate every batch from a fresh fetch. If those fixes change text the Doc already holds, the Doc no longer matches the plan: handle it under the partial-document policy in `references/source-and-delivery-safety.md` and create a new Doc from the updated plan. Rerun the critique pass on any row whose meaning changed; the review status stands unless a fix adds a claim the reviewers didn't see, in which case say so when you return the Doc.

#### Full capability preflight — before creation

Run the preflight in `references/source-and-delivery-safety.md`. Before creation, prove that the authenticated integration can create/import, expose raw structure and revision, apply revision-bound updates, re-fetch/read back, render, and perform authorized cleanup or quarantine. A tool name or sign-in is not proof. If any capability is unverified, preserve the Markdown, block before creation, and give the blocked result (Step 6.5).

### 6.2 Create in the confirmed folder

Record the confirmed folder, approved title, and attempt time. Import the Markdown as a dedicated one-tab Doc in that folder; capture the ID, URL, active tab, and raw JSON. Confirm two tables and two native horizontal rules. If import is malformed, apply the safety reference's partial-document policy, then make at most one more attempt (§5 of the safety reference).

For an ambiguous create/import result, follow the idempotency procedure in `references/source-and-delivery-safety.md`: reconcile the known ID or the exact folder, title, and attempt-time window. **Never blindly retry a create or update.**

Fetch raw JSON into the protected working directory. If the integration cannot expose equivalent structure and indices, preserve the Markdown and **block completion**. Never return a partial document as final.

### 6.3 Normalize and apply the exact Option 4 layout

Generate and apply normalization operations:

```bash
python3 scripts/option4_layout.py normalize imported-doc.json manifest.json normalize-batch.json \
  --required-revision-id "$IMPORTED_REVISION_ID"
```

The normalizer validates the manifest version and digest, confirms that the imported timeline grid plus every Project Plan Overview label and body still match the approved Markdown, rebuilds clean cell paragraphs (status tokens become cell fills, so only the short notes stay as text, and each Phase cell becomes `Phase N:` above its name), removes the generic conversion header, merges each section band into one cell and each Phase cell down across its rows, and adds or removes empty spacer paragraphs so there is exactly one before each rule and one between each H1 and its table. One native batch can only use the fetched snapshot's indices, so it writes from the end of the document toward the start: overview text and merges first, then the spacers after the timeline, then the timeline's text and merges, then the spacers before it.

Immediately before each normalization or formatting write, fetch fresh raw JSON and its revision, bind the batch to that **required revision ID**, apply it through a protected request body (in the order set in the safety reference's §2: a connector tool's request-body parameter that takes these native, revision-bound requests unchanged, then a CLI file or stdin option, then the bundled `send` helper), then re-fetch and verify. With `gws`, which has no file option, apply each batch with the helper rather than pasting JSON into a shell command:

```bash
python3 scripts/option4_layout.py send normalize-batch.json --document-id "$DOC_ID" --response normalize-response.json
```

It refuses a batch without a required revision ID, runs `gws` without a shell, saves the reply to the private response file, and prints `PASS` with the new revision. On any failure or timeout it tells you not to resend: re-fetch and reconcile first. Follow the safety reference for conflicts and ambiguous results: never resend a stale batch; if the expected post-state is present, record success without resending; otherwise regenerate against the new snapshot. Material content changes require researcher reapproval. Block when reconciliation fails.

Generate and apply exact formatting operations:

```bash
python3 scripts/option4_layout.py format normalized-doc.json manifest.json format-batch.json \
  --required-revision-id "$NORMALIZED_REVISION_ID"
```

Apply `format-batch.json` with the same revision-bound sequence, then re-fetch again. This step must produce DM Serif Display/DM Sans typography on the reference's named-style roles (SUBTITLE breadcrumb, TITLE, HEADING_1 headings, HEADING_4 bands, HEADING_5 labels), pageless editing mode with landscape-letter export geometry, one-inch print margins, and the exact Option 4 colors and spacing. The timeline grid gets fixed 180pt / 72pt / 54pt-per-week columns, an unpinned dark-green header row (week labels bottom-right with 2pt padding), gray Phase and Activity columns, 20pt minimum activity rows, and the status fills; the legend's swatch words get their colors. The overview table gets fixed 144pt / 554.4pt columns, 0.75pt black borders, 25.75pt minimum rows, white body cells at 115% line spacing, merged dark-green section bands, native `●` `○` `■` bullets and `1.` / `1.1.` numbers, and `#1155CC` underlined links. Both tables intentionally extend past the 648pt paragraph text area (the timeline by up to 252pt, the overview by 50.4pt); this matches the reference and must not be “corrected” by shrinking them. List creation consumes the leading tabs that set each item's level, so those writes come last in the batch, from the highest index to the lowest. Google Docs has no batch request that edits a named style's definition, so the formatter applies the reference's named-style values directly to each paragraph that uses the style.

The script emits native Google Docs API requests. An equivalent connected integration may apply the same operations directly. If the environment cannot apply an essential operation, **block completion**—do not simplify the design.

### 6.4 Verify and visually inspect

1. Read the document back as text with the connected Google Docs integration (for example, a Markdown or plain-text export) and compare it against every approved row and source link.
2. Inspect the active content tab's structure (tables, cell text, list paragraphs, and links) in freshly fetched raw document JSON, or with the integration's structure-inspection tool when it has one.
3. Run the hard verifier against newly fetched raw JSON:

```bash
python3 scripts/option4_layout.py verify final-doc.json manifest.json
```

4. Export or render the Google Doc and inspect **every page**, not a sample. The verifier cannot see page breaks: in the 2026-10-02 mock it passed while the render showed the timeline split onto a second page and a section band orphaned at the foot of a later page. A grid wider than the 648pt text area prints scaled down in a PDF export (the reference's 900pt grid prints at about 78%); that is expected.
5. Confirm no clipping, illegible wrapping, orphaned section band, awkward timeline split, low contrast, or excess blank page. Every week label and phase name must sit on one line, and no activity or week note may break inside a word; the `timeline` and `manifest` checks measure them, so a wrapped label means the text changed after the check. A taller row can push the grid across a page break, which shifts everything below it, including the section bands. Shorten any wrapped label without changing its meaning. If every label fits and the timeline still splits, tighten the opening and the legend note first, then shorten RACI lines; preserve the approved detailed Timeline row. Don't reach for the row setting `preventOverflow` instead: it only stops a single row from breaking across a page and can't keep the grid's rows together. Re-render to confirm the band rejoined its rows.
6. Correct every issue with the same fresh-fetch, revision-bound, regenerate-on-conflict sequence; then re-fetch, rerun the verifier, and re-render. Repeat until all checks pass, for at most three rounds (a round is one correction batch followed by re-fetch, verify, and render; the first format pass doesn't count); if checks still fail after the third, handle the Doc under the partial-document policy and give the blocked result (below). For a text correction after formatting (for example, shortening a timeline label):
   1. Edit `APPROVED.md` first and regenerate `manifest.json`, so the verifier checks the new text. A material content change needs researcher reapproval; shortening a timeline label without changing its meaning is not one.
   2. Fetch fresh raw JSON and its revision. For each change, build a `deleteContentRange` for the old text, then an `insertText` of the new text at the same start index; both carry the active `tabId`.
   3. Order the pairs from the highest index to the lowest so no edit shifts another's indices, bind the batch to the fresh revision ID, and apply it through a protected request body (the `send` helper with `gws`).
   4. Re-fetch, rerun the verifier (it confirms the inserted text kept the cell's typography), and re-render every page.

A structural-only pass is insufficient. If raw verification or rendering is unavailable, **block completion** rather than returning an approximate document.

### 6.5 Return the verified document

Confirm the file location and return:

- the working Google Doc link;
- `content complete, Option 4 formatting checked, links checked, rendered pages checked`, followed by the exact review status recorded in Step 5 (for example, `critique-only review — multi-agent review skipped at researcher's request`);
- no styling caveat—any unresolved styling limitation means the document is not final.

Open the verified Google Doc in the browser when the environment supports it. Do not update project trackers, progress files, or unrelated systems unless the researcher separately asks.

End with one line offering the next step from [`../../references/skill-handoffs.md`](../../references/skill-handoffs.md): *"Next: `/mod-guide` can build the moderation guide from this plan. Bring this Doc link."* Don't start it unless asked.

This is the final step. The plan has already passed the critique (Step 4.5) and the multi-agent review or its disclosed critique-only fallback (Step 5); only the exact verified Option 4 Google Doc is handed back.

### Blocked result

When any step blocks completion, return no Doc link as final. Say in chat, in this order: **“Blocked — the Google Doc isn't finished.”**; what failed, in one line; where the approved plan is saved (its working-folder path); the Doc's state (not created; trashed or quarantined, with its ID and location; or unknown after an unreconciled create, with what was searched); the Step 5 review status, or that the review hadn't run yet; and what would unblock it.

## Resource routing

Use authorized enterprise search, Slack, and approved data tools for evidence; RACI names come from the researcher, not a people search. Use Drive/Docs only for the confirmed final destination. `references/content-rules.md` owns plan content, `references/source-and-delivery-safety.md` owns sensitive-source and write recovery, `references/research-plan-methodology.md` owns citation-level method rationale, and the Option 4 reference, JSON contract, script, and tests own final formatting. `examples/multi-agent-review-example.md` is synthetic demo material only.

The verified Google Doc is the primary output. A real run is incomplete until its location, content, links, exact Option 4 styling, and rendered pages have passed and its URL is returned.
