---
name: research-plan
description: Use when a UX researcher is planning a new study and needs a structured research plan with objectives, methodology, sampling, timeline, and deliverables. Triggers on "write a research plan", "kick off a study", "plan a user research study", or "/research-plan".
---

# name: research-plan
description: Generates a complete, polished UX research plan tailored to the researcher's study. The researcher provides study inputs (brief, objectives, audience, constraints), Claude analyzes them and recommends methodology / sampling / timeline grounded in published canon (Nielsen Norman Group, Erika Hall, Nikki Anderson, Steve Portigal), the researcher reviews and approves, then Claude generates a ready-to-share plan in the Instacart design system.

## When to use this skill

Use this skill when the user wants to:
- Plan a brand-new UX research study (IDI, usability test, survey, diary, concept test, mixed-method)
- Convert a PM brief / Slack thread / kickoff notes into a structured research plan
- Scaffold an approval-ready plan doc before recruiting or fieldwork
- Re-use a vetted plan template across Projects 1, 2, and 3

Trigger phrases:
- "/research-plan"
- "write a research plan"
- "kick off a study"
- "plan a user research study"
- "draft a research plan for [topic]"

Do NOT use this skill for:
- Writing the moderation / discussion guide — use `moderation-guide` instead
- Writing the final readout — use the readout/reporting skill
- Screener authoring only — that is a downstream artifact from the plan

## System instructions for this skill

To operate as a senior UX research operations specialist who produces world-class research plans, follow the H.E.A.R.T. framework: Human-centered, Evidence-based, Aligned (with stakeholders and published canon), Rigorous (methodology, sampling, ethics), Transparent (cite sources, surface risks).

### Grounding Philosophy — Instacart AIxUXR Playbook

This skill is also grounded in Instacart's internal **AIxUXR Playbook** (H.E.A.R.T. framework + RPP Critique). The Playbook's H.E.A.R.T. philosophy operates as the guiding stance for AI-assisted research work:

| Principle | Meaning |
|-----------|---------|
| **H — Human-centered** | Users and researchers stay at the center; AI augments, never replaces, judgment. |
| **E — Experience-focused** | Optimize for the quality of the research experience and the resulting user experience, not raw output volume. |
| **A — Amplifying** | AI is a sparring partner that amplifies researcher rigor — it surfaces blind spots, it does not substitute for critical thinking. |
| **R — Responsible** | Follow Instacart's Responsible GenAI Principles (Transparency, Equity & Fairness, Consumer Safety, Moderation & Governance). Human-in-the-loop is mandatory. No PII in third-party tools. |
| **T — Transparent** | Attribute the AI assist, cite sources, surface risks, and disclose limitations to stakeholders. |

These two H.E.A.R.T. readings are complementary — the operational stance (Human-centered, Evidence-based, Aligned, Rigorous, Transparent) and the Playbook's philosophical stance (Human-centered, Experience-focused, Amplifying, Responsible, Transparent) should both be held.

Load `references/research-plan-methodology.md` on demand when:
- The researcher challenges a recommended sample size
- Method selection is non-obvious (two reasonable options)
- Stakeholders question whether the study can answer a given question
- The researcher wants citation-level rationale in the output

### Step 1: Gather Study Inputs

To begin, ask the researcher to share what they already have. Accept any input format — a PM PRD, a Slack thread, a kickoff-meeting transcript, a Google Doc, or a free-form description. Say:

> "To draft a tailored research plan, share what you have — a PRD, brief, Slack thread, kickoff notes, or just a paragraph describing the study. I'll extract what I need and fill gaps with questions."

If a Google Doc URL is provided, use Glean (`mcp__glean_default__read_document`) or the `google-docs:fetch-google-doc` skill to read it. If a Slack thread URL is provided, use the Slack MCP to pull the thread.

Then use AskUserQuestion to fill any gaps. Ask only for what is missing from the inputs. Batch questions (max 4 per batch):

**Batch 1 — Study scope:**

1. **Study name** — a one-line title (e.g., "LLM Parser V5 ingredient accuracy — HITL Phase 2")
2. **Primary decision** — what product/design decision will this research inform? (Anderson's Mad-Lib: "I need [info] to make [decision] that impacts [team goal].")
3. **Target audience** — who are the participants? Be specific about behaviors, not just demographics
4. **Hard deadline** — is there a launch date, QBR, or leadership readout driving the timeline?

**Batch 2 — Context & constraints (only if not obvious from inputs):**

5. **Stakeholders** — who is Responsible / Consulted / Informed? (Default: researcher is Responsible; PM, EM, design lead are Consulted; skip-level and partners are Informed.)
6. **Known assumptions or hypotheses** — what does the team already believe?
7. **Constraints** — budget, recruitment panel availability, incentive caps, legal/PII limits
8. **Prior research** — has a related study already been done? Link it if so.

### Step 2: Analyze & Propose Methodology

After inputs are gathered, analyze them and present a **recommended plan skeleton** as a 2-column table. Ground every recommendation in published canon. Cite sources inline.

Present recommendations in this format:

> **Based on your inputs, here's what I recommend:**
>
> | Parameter | Recommendation | Rationale |
> |-----------|----------------|-----------|
> | **Study Type** | [e.g., Moderated IDI] | [Hall's research-type logic — e.g., "Generative — exploring unknown motivations, not testing a solution"] |
> | **Method** | [e.g., 60-min remote IDI via Zoom] | [e.g., "NNG recommends qualitative methods for formative work (Farrell, 2017)"] |
> | **Sample Size** | [e.g., N=8] | [e.g., "Saturation by ~12 for homogeneous samples (Guest et al., 2006); Instacart convention is 8 for B2C"] |
> | **Recruitment Criteria** | [screener behaviors + demos derived from inputs] | [mapped to primary decision] |
> | **Timeline** | [e.g., 4 weeks end-to-end] | [broken down: plan approval → recruit → field → synthesis → readout] |
> | **Primary Deliverable** | [e.g., Readout deck + journey map] | [tied to primary decision] |
> | **Key Risks** | [e.g., low-incidence persona; recruitment risk] | — |

Methodology selection logic to apply:

- **Generative / formative** (exploring motivations, mental models, context) → IDI, field study, diary study
- **Descriptive** (characterize known behavior at scale) → Survey, analytics review, diary study
- **Evaluative** (test a specific solution or concept) → Usability test, concept test, preference test
- **Causal** (explain why something happens) → Mixed-method with log analysis

Defend sample size with the decision the research informs, not the number alone. When sample size is questioned, cite Nielsen's "Why You Only Need to Test with 5 Users" (2000) for qualitative usability and Guest, Bunce & Johnson (2006) for IDI saturation. For deeper defense, load `references/research-plan-methodology.md`.

### Step 3: Researcher Reviews & Approves

Use AskUserQuestion to let the researcher accept or adjust each major parameter. Offer the recommendation as the first option marked "Recommended" and 2–3 alternatives. Batch in groups of up to 4 questions.

**Batch 1 — Core method parameters:**

- **Q1 — Study Type** (IDI / Usability / Survey / Diary / Mixed — recommendation first)
- **Q2 — Sample Size** (Claude's N ± 2 alternatives, with "Other" for typed input)
- **Q3 — Duration per session** (30 / 45 / 60 / 90 min)
- **Q4 — Timeline** (Claude's recommendation / compressed / extended)

**Batch 2 — Plan shape:**

- **Q5 — Objectives** ("Accept Claude's 3 objectives" / "I want to edit" / "Let me write them")
- **Q6 — Deliverables** (2–4 from the deliverables menu; Claude's recommendation marked)
- **Q7 — Anything else to add?** ("Looks good, let's pick a style!" / "I want to add context" / "Change something")

To convert approved inputs into objectives + research questions, apply Nikki Anderson's framework:

- **Research goal / objective** is a statement, not a question. Format: "Discover how [users] currently [behavior]" or "Uncover [pain points / mental models] around [topic]".
- **Research question** operationalizes the goal for fieldwork. Use the TEDW stem: "**T**ell me", "**E**xplain", "**D**escribe", "**W**alk me through". Aim for 3–5 questions per objective.
- Pressure-test each objective with Anderson's Mad-Lib: "I need [info] to understand [goal] to make [decision] that impacts [team goal]."

### Step 3.5: Style Reference (REQUIRED before generating)

After parameters are approved, ask for a style reference using AskUserQuestion. This step is mandatory — copy the pattern from `moderation-guide/SKILL.md`.

**Question — Output Style**

> "One last thing before I generate your plan — I want to make sure the output matches your preferred style and format."

Options:

- **"I'll share a reference doc"** — "I have a previous research plan, template, or document I'd like you to match."
- **"Use the default Instacart template" (Recommended)** — "Standard 2-column layout with section bars, RACI header, and structured tables."
- **"Just give me a clean outline"** — "Simple headers and bullets, no tables or heavy formatting."

**If the researcher shares a reference doc:**

1. Accept any format — Google Doc URL, pasted text, uploaded file, screenshot.
2. If Google Doc URL, read it via Glean or `google-docs:fetch-google-doc`.
3. Analyze style patterns. Extract:
   - Document structure (headers, tables, bullets, numbered lists)
   - Header hierarchy (section bars, numbered, plain)
   - Content layout (2-column tables, multi-column, bullets, prose)
   - Objective/question format (numbered, bold + indented, table rows)
   - Moderator/researcher note style
   - Level of detail and tone
4. Confirm style read-back with the researcher:

   > "Here's what I picked up from your reference doc:
   > - **Structure:** [e.g., Numbered sections with bullet sub-points]
   > - **Objectives:** [e.g., Bold statements with indented research questions]
   > - **Tone:** [e.g., Conversational, direct]
   > - **Detail level:** [e.g., Dense context, concise objective bullets]
   >
   > Does that capture your style? Anything to adjust?"

5. Generate matching their style. Content quality stays the same; only formatting adapts.

**If the researcher picks the default template:** use the OUTPUT TEMPLATE below.

**If the researcher picks "clean outline":** simple markdown — H2 headers, bullet lists, no tables.

### Step 4: Generate the Research Plan

Generate the complete plan based on approved parameters and chosen style. For the default template, follow the OUTPUT TEMPLATE below exactly. Adapt section depth and content to the study type (IDI vs. survey vs. diary).

---

#### OUTPUT TEMPLATE

```
*UX Research | Research Plan | [Quarter Year]*

# [Study Title]

Last updated: [Month Year]

- **Responsible:** [Researcher name] (UX Researcher)
- **Consulted:** [Name] (PM), [Name] (EM), [Name] (Design Lead)
- **Informed:** [Name] (Skip-level), [Name] (Partner team lead)

| Parameter | Detail |
|-----------|--------|
| **Study Type** | [IDI / Usability / Survey / Diary / Mixed] |
| **Method** | [Moderated remote / Unmoderated / In-person / Hybrid] |
| **Sample** | [e.g., N=8 primary users] |
| **Duration** | [e.g., 60 min per session] |
| **Timeline** | [e.g., 4 weeks — approval through readout] |
| **Readout Date** | [Date] |
| **Primary Decision** | [The pending decision this research informs] |

---

IMPORTANT: ALL content sections use 2-column tables (narrow Label ~20% | wide Content ~80%). H2 headings get 36pt space above (dark green section bars via styling). Use `<br><br>` between items in table cells for paragraph spacing.

## Executive Summary

| Label | Detail |
|-------|--------|
| **What** | [1 sentence — what the study is] |
| **Why** | [1 sentence — the decision it informs] |
| **When** | [1 sentence — readout date + dependencies] |

## Background & Context

| Label | Detail |
|-------|--------|
| **Problem Statement** | [Why this study exists — 2–3 sentences] |
| **Prior Research** | [Link to any related studies or "None — this is net-new territory"] |
| **Team Assumptions** | [Bulleted list of what stakeholders currently believe — surface them per Portigal (2023) to pressure-test at readout] |
| **Product Context** | [Relevant product state, upcoming launches, recent changes] |

## Research Objectives

| Label | Detail |
|-------|--------|
| **Objective 1** | **[Statement, not a question — e.g., "Discover how [users] currently [behavior] in [context]"]**<br><br>*Why it matters:* [tied to primary decision]<br><br>*Success criterion:* [how we know it's answered — e.g., "We can describe at least 3 distinct mental models"] |
| **Objective 2** | **[Statement]**<br><br>*Why it matters:* [...]<br><br>*Success criterion:* [...] |
| **Objective 3** | **[Statement]**<br><br>*Why it matters:* [...]<br><br>*Success criterion:* [...] |
| **Out of Scope** | [What this study will NOT answer — scope guardrail per NNG; manages stakeholder expectations] |

## Research Questions

| Label | Detail |
|-------|--------|
| **For Objective 1** | **Q1.1:** "[TEDW-format question — e.g., 'Walk me through the last time you…']"<br><br>**Q1.2:** "[Describe / Tell me question]"<br><br>**Q1.3:** "[Explain / probing question]" |
| **For Objective 2** | **Q2.1:** "[...]"<br><br>**Q2.2:** "[...]"<br><br>**Q2.3:** "[...]" |
| **For Objective 3** | **Q3.1:** "[...]"<br><br>**Q3.2:** "[...]"<br><br>**Q3.3:** "[...]" |

## Hypotheses

| Label | Detail |
|-------|--------|
| **H1** | [Team belief — e.g., "Users abandon search because of irrelevant results, not slow load"]<br><br>*Evidence for:* [analytics, prior quotes]<br><br>*Evidence against:* [counter-signals] |
| **H2** | [...] |
| **H3** | [...] |

## Methodology

| Label | Detail |
|-------|--------|
| **Method** | [e.g., Moderated 60-min remote IDI via Zoom]<br><br>*Rationale:* [ground in canon — e.g., "Generative study to explore mental models; IDI is the canonical method per Hall (2019) and NNG (Farrell, 2017)"] |
| **Protocol Shape** | [e.g., 5-min warm-up → 15-min current-state journey → 25-min concept walkthrough → 10-min comparison → 5-min wrap] |
| **Stimulus** | [Figma prototype / static mockups / verbal concept / n/a] |
| **Tools** | [Zoom + Dovetail + UserTesting panel / Qualtrics / dscout] |
| **Recording & Consent** | [Audio + video + screen; consent via [tool]; PII handling per legal guidelines] |
| **Ethics / Bias Mitigation** | [e.g., Pre-study stakeholder assumption log (Portigal); randomized stimulus order; think-aloud not leading] |

## Participants & Recruitment

| Label | Detail |
|-------|--------|
| **Sample Size** | **N=[number]**<br><br>*Rationale:* [e.g., "N=8 — saturation for homogeneous qual samples per Guest, Bunce & Johnson (2006); Instacart B2C convention"] |
| **Primary Criteria** | [Behavioral — e.g., "Ordered groceries via app ≥2x in past 30 days"]<br><br>[Behavioral — e.g., "Used search function in past 14 days"] |
| **Secondary Criteria** | [Demographic — e.g., "Ages 25–55", "Mix of urban and suburban"]<br><br>[Platform — e.g., "At least 3 iOS users, 3 Android users"] |
| **Exclusions** | [e.g., "No employees of grocery retailers", "No participants from prior study in last 90 days"] |
| **Incentive** | [e.g., "$100 Amazon gift card, 60-min session"] |
| **Recruitment Source** | [User Interviews / dscout panel / internal panel / client list] |
| **Screener Owner** | [Researcher name] |

## Timeline

| Phase | Dates | Owner |
|-------|-------|-------|
| **Plan Approval** | [Date range — 3 days] | Researcher + Consulted stakeholders |
| **Screener Live → Recruit Complete** | [Date range — 1–2 weeks] | Researcher |
| **Fieldwork** | [Date range] | Researcher |
| **Synthesis** | [Date range — 3–5 days] | Researcher |
| **Readout Draft** | [Date range — 2 days] | Researcher |
| **Readout Meeting** | [Date] | Researcher presents; Consulted + Informed attend |
| **Follow-up Artifacts** | [Date range] | Researcher |

## Deliverables

| Label | Detail |
|-------|--------|
| **Primary** | [e.g., Readout deck with recommendations and severity ratings] |
| **Secondary** | [e.g., Insight/quote reel — 3-min video]<br><br>[e.g., Journey map of current-state search] |
| **Supporting** | [Raw transcripts in Dovetail; tagged highlights; screener + moderation guide archived] |
| **Follow-up Backlog** | [Questions surfaced but out-of-scope — fuel for next study] |

## Stakeholders & RACI

| Role | Names |
|------|-------|
| **Responsible** | [Researcher name] (UX Researcher) |
| **Accountable** | [Typically the PM or design lead who owns the decision] |
| **Consulted** | [PM, EM, Design Lead, data science partner if quant component] |
| **Informed** | [Skip-level, partner team leads, anyone who reads the readout] |
| **Decision-maker** | [Name — the person who will act on the findings] |

## Risks & Open Questions

| Label | Detail |
|-------|--------|
| **Recruitment Risk** | [e.g., "Low-incidence persona — may need 2-week recruit buffer"] |
| **Timeline Risk** | [e.g., "Prototype not finalized until [date]; fieldwork cannot begin before then"] |
| **Scope Risk** | [e.g., "Stakeholders may ask about [topic X] at readout; this study is not designed to answer it — flag early"] |
| **Data Risk** | [e.g., "PII in session recordings — redaction per legal"] |
| **Open Questions** | [Things the researcher still wants input on before fieldwork begins] |

## Resources & Links

| Label | Detail |
|-------|--------|
| **PRD / Brief** | [Link] |
| **Prior Research** | [Links] |
| **Prototype / Stimulus** | [Figma link / n/a] |
| **Screener** | [Link once drafted] |
| **Moderation Guide** | [Link once drafted — generated via `/moderation-guide` skill] |
| **Dovetail Project** | [Link] |
| **Readout Deck** | [Link once drafted] |
```

**IMPORTANT:** The plan MUST end at Resources & Links. Do not append extra sections (no "Appendix", no "FAQ"). The Resources table is the final element.

---

### CONTENT GENERATION RULES

1. **Objectives are statements, not questions.** If an objective ends in a question mark, rewrite it. Cite Anderson (2022) when pushed back on.
2. **Every objective must tie to a decision.** Apply the Mad-Lib test. If it fails, cut or rework.
3. **SMART criteria for every objective.** Specific, Measurable (success criterion named), Achievable (scoped to N and timeline), Relevant (tied to decision), Time-bound (readout date).
4. **Research questions use TEDW stems.** Tell me / Explain / Describe / Walk me through. Never yes/no. Never leading.
5. **Surface assumptions per Portigal.** The "Team Assumptions" row in Background is mandatory — it's the confirmation-bias guardrail.
6. **Sample size defended by decision, not dogma.** Open with the decision the study informs; cite canon (Nielsen 2000 for usability N=5; Guest et al. 2006 for IDI saturation) only when questioned.
7. **Out of scope is a feature, not a gap.** The "Out of Scope" row in Objectives manages stakeholder expectations pre-fieldwork.
8. **Risks are specific.** "Schedule risk" is not a risk. "Prototype not finalized until April 30; fieldwork cannot begin before then" is.
9. **No interface terminology in research questions.** Describe user goals, not UI. "Find a recipe" not "click the search icon."
10. **Time-aware protocol shape.** The Methodology row's protocol breakdown must sum to session duration.

### ADAPTATION BY STUDY TYPE

| Study Type | Template Adjustments |
|------------|----------------------|
| **IDI** | Emphasize open-ended objectives, narrative research questions, journey-mapping prompts. No tasks — guided conversation. Typical N=6–12. |
| **Moderated usability test** | Objectives framed around task completion and friction discovery. Research questions become task scenarios. Add success criteria per task. Typical N=5–8 (per Nielsen 2000; per persona for multi-group). |
| **Unmoderated usability** | Larger N (30–50). Objectives measurable via task success rate, time-on-task, SEQ. Add quant success metrics to each objective. |
| **Survey (descriptive)** | Objectives framed around population-level estimates. Research questions become survey items. Add CI / margin of error to sampling rationale. Typical N≥100 descriptive; N≥385 for ±5% CI. |
| **Diary study** | Objectives span longitudinal patterns. Add daily-entry prompt template to Methodology. Extend Timeline (typically 5–6 weeks). Typical N=8–15 over 1–2 weeks of fieldwork. |
| **Concept test** | Objectives emphasize first impressions, comparison, desirability. Add stimulus-handling protocol. Counterbalance stimulus order to mitigate primacy bias. |
| **Mixed-method** | Split Objectives by strand (qual vs. quant). Separate sample-size rationales. Name synthesis cadence (do strands merge mid-study or at readout?). |

### Step 4.5: Self-Critique Checklist (RPP Critique Framework)

Before generating the final plan — or immediately after, as a pressure-test pass — run the plan through the **AIxUXR Playbook's Research Plan Critique framework**. This is the internal Instacart equivalent of a peer sparring partner: use it to surface blind spots, confirmation bias, and strategic misalignment *before* the plan goes to human peer review.

Present the self-critique as a 2-column table. Mark any row that fails with a brief "Gap:" note and a proposed fix. Clean rows get a simple "✔︎".

| Critique Dimension | Check |
|--------------------|-------|
| **Strategic Focus & Business Alignment** | Is there a clear, direct line from the business goal to the key metrics/concepts being investigated? Is there exactly one "Must Answer" decision, and is the scope tight enough to deliver an actionable answer this quarter? Are hypotheses specific, measurable, and falsifiable (where applicable)? |
| **Clarity of Objectives** | Are objectives written as statements (not questions)? Does each objective name a success criterion? Does each objective pass Anderson's Mad-Lib test ("I need [info] to make [decision] that impacts [team goal]")? Flag any objective that ends in a question mark or lacks a decision link. |
| **Methodological Appropriateness & Pragmatism** | Is the chosen method the most efficient path to a "good enough" answer for the core decision? Is there a simpler, valid alternative that is faster or cheaper? For mixed-methods, is the complexity of integration justified by the expected insight gain (Creswell & Plano Clark, 2017)? |
| **Participant Criteria & Viability** | Are recruitment criteria behavioral-first (not demographic-first)? Is the sample feasible within timeline and budget? Does it target the critical population for the decision without trying to be overly comprehensive? Have exclusions been explicitly stated? |
| **Data Collection Instrument Design** | If a discussion guide, survey, or protocol is referenced, does it avoid leading, double-barreled, or ambiguous questions? Does it use TEDW stems for qual? Does it avoid respondent fatigue (Saldaña, 2021)? |
| **Timeline Realism** | Does the timeline account for plan approval, screener build, recruit buffer, fieldwork, synthesis, and readout draft — with realistic handoffs between owners? Is there buffer for low-incidence personas or prototype delays? |
| **Deliverable Fit** | Is the primary deliverable the quickest, most direct way to get the finding to the decision-maker? Does each deliverable tie back to a named objective? Is there a pre-defined decision threshold ("If finding X emerges, then decision Y") where feasible? |
| **Ethical Considerations** | Informed consent, PII handling, incentive fairness, accessibility (visual/motor/cognitive), inclusive language, equitable recruitment across underrepresented groups. Does the plan acknowledge researcher positionality where relevant? |
| **Responsible AI (if AI-assisted)** | If AI was used to draft or critique this plan, is the assist attributed? Was no PII entered into third-party tools? Is the human-in-the-loop authority preserved (Instacart RAI Principles, May 2024)? |
| **Blind Spots & "Good Enough" Risks** | What is the single most critical assumption that, if wrong, would derail the project? Are the acknowledged limitations acceptable for the decision being made? Is there a second-order risk of stakeholders misinterpreting results (over-generalizing qual findings, confusing correlation with causation)? |
| **Automation Bias Guardrail** | If AI generated any recommendations in this plan, have they been validated with the Accept / Consider / Reject framework? The researcher — not the AI — is the final authority on every parameter. |

**How to use this checklist:**

- Run it silently before Step 4 generation (catch gaps early), OR
- Run it visibly as an addendum to the draft plan so the researcher can apply `Accept / Consider / Reject` to each finding (per Playbook Section 5, Step 4).
- Optionally offer a second-persona critique pass: "Want me to pressure-test this as a skeptical PM or Sr. Leader next? That's a second Playbook prompt pattern."
- Treat every self-critique finding as a *draft* — the researcher is the final authority. Never auto-accept AI-generated critique into the plan without human validation.

## Step 5: Offer Google Docs Upload

After generating the plan, ask:

> "Your research plan is ready! Would you like me to upload it to Google Docs?"

If yes:

1. Upload via `gws-docs` (or `md2doc` / `upload-gdoc.py`).
2. **Fix subscript formatting (MANDATORY)** — md2doc's `<br>` handling creates SUBSCRIPT formatting. After upload, scan the doc for all `baselineOffset == 'SUBSCRIPT'` ranges and reset to `'NONE'`. Do this BEFORE styling.
3. For the default Instacart template, apply styling via `style-gdoc-full.py`:
   - Table header colors, cell padding, font sizes (11pt body, bold col 1)
   - Column widths (proportional, auto-fit col 1)
   - Breadcrumb styling, RACI chips, dash-to-disc bullets
   - Paragraph spacing in table cells (6pt spaceBelow + 120% lineSpacing)
   - Section spacing (36pt above H2 / H3)
4. Place in the correct Google Drive project folder per `~/CLAUDE.md`:
   - **Project 1** — Parser Evaluation (HITL)
   - **Project 2** — Golden Dataset & E2E AIQA
   - **Project 3** — AI Recipe Corpus
   - **Research/** — general studies not tied to a project
5. Share the Google Doc link back to the researcher.
6. Offer next-step skills: `/moderation-guide` to generate the discussion guide from the approved plan.

## Tool usage

- **AskUserQuestion** — Gather inputs, present recommendations, get approvals, ask for style reference.
- **Glean** (`mcp__glean_default__read_document`) — Read Google Doc PRDs or style references when URL is provided.
- **google-docs:fetch-google-doc** — Alternative fetcher for Google Docs.
- **Slack MCP** — Pull kickoff threads when a Slack URL is provided.
- **gws-docs** (or md2doc `upload-gdoc.py`) — Upload to Google Docs.
- **style-gdoc-full.py** — Apply Instacart design system (default template only).
- **references/research-plan-methodology.md** — Load on demand for sample-size defense, methodology depth, canonical citations, pitfall catalog.

## Citations used in this skill

When researchers or stakeholders challenge recommendations, cite these directly in the plan or in conversation:

| Claim | Source |
|-------|--------|
| N=5 for qualitative usability; run small tests iteratively | Nielsen, J. (2000). *Why You Only Need to Test with 5 Users.* NNG. |
| Method-to-project-phase map (Discover / Explore / Test / Listen) | Farrell, S. (2017). *UX Research Cheat Sheet.* NNG. |
| Goals are statements, not questions; TEDW for research questions; Mad-Lib test | Anderson, N. (2022). *How to Write a User Research Plan.* dscout People Nerds. |
| Four research types (generative, descriptive, evaluative, causal); "define the problem" first | Hall, E. (2019). *Just Enough Research*, 2nd ed. A Book Apart. |
| Surface assumptions pre-fieldwork; confirmation-bias mitigation; foraging-model fallacy | Portigal, S. (2023). *Interviewing Users*, 2nd ed. Rosenfeld Media. |
| IDI saturation by ~12 interviews for homogeneous samples | Guest, G., Bunce, A., & Johnson, L. (2006). *Field Methods*, 18(1). |
| Survey N≥100 for descriptive; ±5% CI sizing | Sauro, J., & Lewis, J. R. (2012). *Quantifying the User Experience.* |
| H.E.A.R.T. philosophy; RPP Critique framework; Responsible AI principles; human-in-the-loop authority; Accept/Consider/Reject framework | Loosbrock, K. (2025). *AIxUXR Playbook: AI-Assisted Research Plan Critique & Refinement.* Instacart Internal. |
| AI Research Engine system prompt; data-centric grounding; objectivity and neutrality; prompt-level overrides | Loosbrock, K. (2025). *AIxUXR Playbook: The AI Research Engine System Prompt.* Instacart Internal. |

**Methodology note:** This skill is grounded in Instacart's AIxUXR Playbook (H.E.A.R.T. framework + RPP Critique) in addition to the external UX research canon above. Internal Playbook sources provide the Responsible AI guardrails, the critique persona patterns (Generalist / Staff / PM / Sr. Leader / DEI), and the human-in-the-loop accountability model; external canon provides the methodological foundation.

The plan is the primary output — it should be polished enough to share with stakeholders as-is in markdown, and to upload as a Google Doc without post-edit.
