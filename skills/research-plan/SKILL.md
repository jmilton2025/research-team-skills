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

Load `~/.claude/skills/jedidas-design-template/references/visual-spec.md` when:
- Generating the markdown structure for "Jedida's design template" (Step 4)
- Building or applying the styling pipeline (Step 5) — it is the source of truth for fonts, colors, RACI block, table layout, and sticky-header behavior

Load `~/.claude/skills/jedidas-design-template/references/api-gotchas.md` when:
- Writing any custom Google Docs `batchUpdate` request — 13 landmines documented
- Diagnosing a styling regression (blacked-out cells, broken hanging indents, SUBSCRIPT artifacts)

Both reference files now live in the **`jedidas-design-template`** skill — the single source of truth for Jedida's canonical document design. This skill (`research-plan`) delegates all styling work there.

### Cross-references — single source of truth pattern

This skill (`research-plan`) owns **content rules** (what goes where, how questions are scoped). The styling skill `jedi-doc-styling-1` owns **typography + bolding rules** (what the doc looks like, what to bold). Each links to the other rather than duplicating.

Always load the relevant cross-references when the question is mixed (content + styling):

| Concern | Source file | Path |
|---|---|---|
| Research Questions = broad project-level (NOT TEDW probes); 3-question 1:1 default; Questions/Objectives as numbered lists with bold leads; ResOps RPP section order (Topic → TL;DR → Background → Existing Insights → Objectives → Key Research Questions → Hypotheses → What decisions → Themes → Proposed Research Timeline → Project Details → Additional/Documents); Background = Problem + Product Context; Existing Insights with verbatim sources; Project Details absorbs Method + Participants; Additional/Documents as clickable markdown links; RACI in header | `research-plan/references/content-rules.md` | `~/.claude/skills/research-plan/references/content-rules.md` |
| What to bold (anchor-not-substance, ≤10% density, complete-sentence bodies, one north-star phrase per question) | `jedi-doc-styling-1/references/bolding-philosophy.md` | `~/.claude/skills/jedi-doc-styling-1/references/bolding-philosophy.md` |
| Bullet anchor + body type spec (§9d); Bulleted Lead-in pattern (§9e); H2 banners; H3 left-borders | `jedi-doc-styling-1/references/design-spec.md` | `~/.claude/skills/jedi-doc-styling-1/references/design-spec.md` |
| When researcher wants the Research Plan reference template (Arial 11pt body, DM Serif 26pt green title, dark forest-green dual-table) instead of the default Mod Guide template | `jedi-doc-styling-1` skill | Run `python3 ~/.claude/skills/jedi-doc-styling-1/scripts/apply_jedi_style_1.py <DOC_ID>` |

### Step 1: Gather Study Inputs

To begin, ask the researcher to share what they already have. Accept any input format — a PM PRD, a Slack thread, a kickoff-meeting transcript, a Google Doc, or a free-form description. Say:

> "To draft a tailored research plan, share what you have — a PRD, brief, Slack thread, kickoff notes, or just a paragraph describing the study. Point me at the project folder too, and I'll pull existing context before I ask you anything."

If a Google Doc URL is provided, use Glean (`mcp__glean__read_document`) or the `google-docs:fetch-google-doc` skill to read it. If a Slack thread URL is provided, use the Slack MCP to pull the thread.

### Step 1.5: Discover Existing Context & Insights FIRST (before any logistics questions)

**This step runs BEFORE asking the researcher for goal / decision / timeline / stakeholders.** Team feedback (Prakriti + Amalia, 2026-06-02 research workshop): the plan must open with *what we already know*, not logistics. Jumping to "who are the beta users / what's the timeline / who are the stakeholders" before establishing context is the #1 thing to fix.

Proactively search for prior context and insights — do NOT wait to be asked, and do NOT assume the researcher's project folder holds everything (Prakriti: "all the context will always not live in your folder"):

1. **Dedicated research-insights agent (PRIMARY).** Call `mcp__research-insights__research_insights__updated` with the study topic. This is the team's User & Market Research agent and is the right first stop for "does this answer already exist?" Prakriti called this out specifically — connect to the *research agent*, not just general Glean: *"we should connect it to glean research agent not just glean overall."*
2. **Glean.** `mcp__glean__search` (keyword) for relevant docs and `mcp__glean__chat` (synthesis) for "what prior research exists on [topic]." Filter to `gdrive` / `confluence` / `slack` as useful. This catches prior research from *other researchers and other teams*, not just the current project.
3. **Project folder.** Read the researcher's named project / Drive folder for first-party context.
4. **Snowflake / behavioral data.** ⚠️ No Snowflake MCP is wired in this environment (verified 2026-06-05). If the study needs behavioral sizing, hand off to the `data:write-query` or `snowflake-development` skill, or flag that the researcher must pull it. NEVER fabricate numbers — see CLAUDE.md "Permanent Facts."

Then **show, don't interrogate.** Present back as a confirm-or-correct, NOT a 15-question quiz (Prakriti: *"It can say, here's the context. Does this look right? Yes. So move to right."*):

> "Here's what I found before drafting — does this look right?
>
> **Background & context** *(verbatim from sources, with links)*
> - "[verbatim sentence pulled from PRD / doc]" — [Source name](URL)
> - "[verbatim sentence]" — [Source name](URL)
>
> **Existing insights — what we already know** *(top 5, each with a source)*
> 1. [Insight stated plainly] — [Source](URL)
> 2. …
>
> **Proposed hypotheses** *(derived from the above, to pressure-test)*
> - H1 — [belief]
> - H2 — [belief]
>
> Correct anything that's off, or tell me what I'm missing."

**Verbatim rule (Amalia):** background and prior-research items are quoted **verbatim with a source link**, not silently synthesized into Claude's own words. Synthesis is fine *in addition*, but the researcher must be able to see the source text without leaving the plan — otherwise she has to go re-verify it and it saves no time. See content rule #27.

Only after context + existing insights are confirmed do you move to logistics.

### Step 1.6: Logistics + Decision Audit

Now use AskUserQuestion to fill the operational gaps the inputs didn't cover. Ask only for what's missing. Batch (max 4 per batch):

**Batch 1 — Decision & scope:**

1. **Primary decision** — what product/design decision will this research inform? (Anderson's Mad-Lib: "I need [info] to make [decision] that impacts [team goal].")
2. **Study name** — a one-line title (e.g., "LLM Parser V5 ingredient accuracy — HITL Phase 2").
3. **Topic** — one-sentence statement of what this study is about and the user-grounded thing it will define (becomes the **Topic** section — the leadership one-liner at the top of the RPP).
4. **Timeline** — weeks from plan-approval to readout (1 / 2 / 3 / 4+ / hard deadline date).

**Decision audit (Prakriti):** when the researcher states the primary decision, *audit it for crispness before accepting it*. The point of a research plan is to name the **minimum evidence needed to move a specific decision** — so the decision has to be decision-grade. If it's vague — "help with strategy", "understand users better", "inform the roadmap" — push back instead of silently accepting it:

> "That reads more like a goal than a decision. A plan earns its keep by naming the *minimum evidence needed to move a specific decision* — who decides what, and what would change based on the finding? Want to sharpen it with the PM, or should I propose a crisper version?"

Prakriti's example of the behavior wanted: *"cloud should say that's not a great decision. And so then you talk to PMs or get that decision to be very crisp."* A sharp decision is what makes the methodology (Step 2) answerable.

**Batch 2 — Sample & stakeholders:**

5. **Target audience** — participants by behavior, not just demographics.
6. **Stakeholders** — who is Responsible / Accountable / Consulted / Informed? (Default: researcher is Responsible; decision-owner is Accountable; PM, EM, design lead are Consulted; skip-level and partners are Informed.)
7. **Constraints** — budget, recruitment panel, incentive caps, legal/PII limits.

*(Hypotheses are no longer asked as a logistics question — they're proposed from existing insights in Step 1.5 and confirmed there, then land in the standalone Hypotheses section. See content rule #7.)*

### Pacing (Prakriti): the plan is the foundation — don't rush the front half

Do NOT auto-bypass the context, existing-insights, hypotheses, or decision steps to "save time." Prakriti was explicit: *"I don't think we should spend only five minutes on a research plan… research plan is the foundation."* These steps are where the plan earns its value; a 5-minute plan that skips them isn't a plan. Spend the depth up front — context, existing insights, sharp research questions, hypotheses, and an audited decision. Timeline and methodology *mechanics* can move fast; the strategic front half cannot. The only exception is an explicitly scoped quick study (*"I'm taking this to 5 users, quick turn"*) — then a lighter pass is fine.

### Step 2: Analyze & Propose Methodology

**Frame methodology as "the minimum evidence needed to move the decision" — not "the most thorough study possible."** Prakriti (2026-06-02): *"it knows all the different methodology and what's the minimum evidence I need to get this through, and then it suggests a few."* Open the methodology recommendation by restating the audited decision from Step 1.6, then propose the **leanest valid path** to evidence that would actually move it, plus 1–2 alternatives (e.g., "moderated-first", "unmoderated + card sort", "two-phase hybrid"). Recommend one, flag any timeline conflict ("you have one week — a two-phase study won't fit; here's the single-phase version"), and let the researcher override.

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

### Step 3: Researcher Reviews & Approves — SECTION-BY-SECTION, in RPP order

**This is the core of how the team wants to use the skill** (2026-06-08, Jedida relaying the team): *"the researchers wanna go through it one by one so that they can approve it… the pop-up should be in the same order that the research plan is, so they can brainstorm and think through with Claude."*

So Step 3 is NOT a few batched method questions. It is a **guided walk through the plan's sections, one pop-up per section, in the exact same order as the OUTPUT TEMPLATE.** For each section: show Claude's proposed draft of that section, then a pop-up to approve / brainstorm / edit it, then move to the next. The researcher is co-authoring section by section, not approving a finished artifact at the end.

**Walk order (identical to the OUTPUT TEMPLATE order — DO NOT reorder):**

1. **Existing Insights** *(FIRST pop-up)* — "Here's what we already know" (from Step 1.5 discovery). Confirm / correct / add. This comes first because it grounds everything that follows (Prakriti + Amalia: lead with what's known). *(Topic + TL;DR are auto-drafted and shown alongside, but the discovery review is the first interactive gate.)*
2. **Topic** — the one-line leadership framing.
3. **Background** — Problem Statement (3 bold-lead bullets) + Product Context.
4. **Objectives** — Claude's 3 proposed objectives; approve / edit / rewrite.
5. **Key Research Questions** — 3 broad project-level questions; approve / edit / rewrite.
6. **Hypotheses / Questions of Interest from XFN leads** — beliefs to pressure-test; approve / edit.
7. **What decisions will be made with such research?** — confirm the decision fork(s).
8. **What Research Priorities is this relevant to (Themes)** — confirm theme mapping.
9. **Method + Approach** *(Project Details)* — the minimum-evidence recommendation + 1–2 alternatives; pick the tradeoff.
10. **Sampling Plan / Participants** *(Project Details)* — cohorts, completes, recruit source.
11. **Stimuli → Dependencies → Compensation → Research Platform → Deliverable Format** *(rest of Project Details)* — can batch these last logistics cells into one pop-up.
12. **Proposed Research Timeline** — dated milestones; confirm / shift.
13. **Additional → Documents** — confirm the auto-linked doc list; add any missing.

**How each section pop-up works (the pattern, repeated per section):**

- **Show the draft first.** Render Claude's proposed content for that one section (drafted from Step 1.5/1.6 discovery + Step 2 analysis), so the researcher is reacting to something concrete, not a blank prompt.
- **Then AskUserQuestion** with options shaped like: **"Accept this [section]" (Recommended)** / **"Brainstorm it with me"** / **"I'll edit / rewrite it"** / (section-specific alternatives where they exist — e.g. for Method: the lean vs. higher-confidence variants; for Sample Size: N ± 2).
- **"Brainstorm it with me"** → drop into a short back-and-forth on just that section (this is the "think through with Claude" the team asked for), then re-show the revised draft and re-confirm before advancing.
- **Advance in order.** Only move to the next section after the current one is approved. Keep a running "✓ approved / ◻ pending" list of the 13 sections so the researcher always knows where they are in the walk.

**Pacing & batching:** sections 1–9 are the strategic front half — give each its own pop-up, don't rush them (see the Pacing note above; Prakriti: *"the research plan is the foundation"*). Sections 11 and 13 are logistics and can each be a single batched pop-up. Never collapse the whole walk back into 2 generic batches — that defeats the section-by-section approval the team explicitly asked for.

**Override:** if the researcher says *"just generate the whole thing, I'll review at the end"*, skip the walk and go straight to Step 4 (single full draft), then still route through Step 6 multi-agent-check. The section-by-section walk is the default, not a hard gate.

To convert approved inputs into objectives + research questions, apply Nikki Anderson's framework:

- **Research goal / objective** is a statement, not a question. Format: "Discover how [users] currently [behavior]" or "Uncover [pain points / mental models] around [topic]".
- **Research question** operationalizes the goal for fieldwork. Use the TEDW stem: "**T**ell me", "**E**xplain", "**D**escribe", "**W**alk me through". Aim for 3–5 questions per objective. *(Note: these TEDW probes are for the downstream moderation guide — the plan's Key Research Questions stay broad and project-level. See content rule #5.)*
- Pressure-test each objective with Anderson's Mad-Lib: "I need [info] to understand [goal] to make [decision] that impacts [team goal]."

### Step 3.5: Style Reference (REQUIRED before generating)

After parameters are approved, ask for a style reference using AskUserQuestion. This step is mandatory — copy the pattern from `moderation-guide/SKILL.md`.

**Question — Output Style**

> "One last thing before I generate your plan — I want to make sure the output matches your preferred style and format."

Options:

- **"Apply Jedi's Doc Styling 1" (Recommended)** — "Jedida's locked-in default for research plans. Deep forest green `#2D4A3E` title in DM Serif Display 26pt, italic green breadcrumb in DM Sans, Arial 11pt body, dark forest-green dual-table layout. Calls into the `jedi-doc-styling-1` skill."
- **"Apply Jedi's Doc Styling 2"** — "GlossGenius look — alternate styling option. Same content; different visual feel. Calls into the `jedi-doc-styling-2` skill."
- **"Apply Jedida's Design Template"** — "Original canonical look — DM Serif title, RACI chip highlights, design table with section bars, sticky header. Calls into the `jedidas-design-template` skill."
- **"I'll share a reference doc"** — "I have a previous research plan, template, or document I'd like you to match."
- **"Just give me a clean outline"** — "Simple headers and bullets, no tables or heavy formatting."

**Default is Jedi's Doc Styling 1** — Jedida locked it in on 2026-05-12 as the canonical look for all research plans. Only deviate when the researcher explicitly picks another option.

**If the researcher picks Jedi's Doc Styling 1 (default):** generate the plan in markdown using the OUTPUT TEMPLATE below, then run the upload + styling pipeline in Step 5 (which calls `apply_jedi_style_1.py`).

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

**If the researcher picks Jedi's Doc Styling 2 OR Jedida's Design Template:** use the same OUTPUT TEMPLATE below — only the Step 5 styling pipeline changes.

**If the researcher picks "clean outline":** simple markdown — H2 headers, bullet lists, no tables.

### Step 4: Generate the Research Plan

Generate the complete plan based on approved parameters and chosen style. For the default template, follow the OUTPUT TEMPLATE below exactly. Adapt section depth and content to the study type (IDI vs. survey vs. diary).

**Test/demo labeling:** If this invocation is a mock-run, demo, or otherwise built on invented/simulated study inputs rather than a real study, label it per `../../references/output-status-and-labeling-conventions.md` (§2) before presenting the draft — a research plan found without context could otherwise be mistaken for a real deliverable.

---

#### OUTPUT TEMPLATE

> ✅ **CANONICAL STRUCTURE: the ResOps Research Project Plan (RPP) template** — Doc `1s6Lg4ZsiIypqANdpg4hrCwxkgwP0qOwJvGNekzgj9k0` ("[TEMPLATE - MAKE A COPY] Research Project Plan"). Locked **2026-06-08**. Section names + order match the official ResOps template exactly. Per Jedida's **"Option B"** choice (2026-06-08), the Jun-2 team enhancements are FOLDED IN rather than dropped: **Existing Insights** (verbatim sources) sits right after Background, bold-lead scannable styling stays, and Method + Approach uses the "minimum evidence to move the decision" framing.
> **The interactive pop-up walks these sections in THIS SAME ORDER** (Step 3) so researchers approve/brainstorm one section at a time. First pop-up = Existing Insights. **Do NOT reorder.**
> Canonical order: Header (Key Contacts → Key Stakeholders/RACI → Research Timeline grid) → **Topic → TL;DR → Background → Existing Insights → Objectives → Key Research Questions → Hypotheses / Questions of Interest → What decisions will be made → Research Priorities (Themes) → Proposed Research Timeline → Project Details → Additional/Documents.**

```
# Research Project Plan: [Project Name]

Last updated: [Month Year]

**Key Contacts:** [Researcher name] (UX Researcher)

**Key Stakeholders:**
- **Responsible:** [Researcher name] (UX Researcher) — or `[TBD — fill in]`
- **Accountable:** [Decision-owner name] (Role) — or `[TBD — fill in]`
- **Consulted:** [Name] (Role) — mark the *decision-maker* inline if Consulted, e.g. "(DS, AIQA — *decision-maker*)" — or `[TBD — fill in]`
- **Informed:** [Name] (Role) — or `[TBD — fill in]`

### Research Timeline

Phase × stage grid. Status codes: **PL** = Planning, **KO** = Kick off, **IP** = In progress, **RO** = Read Out.

| Phase | Stage | Status |
|---|---|---|
| Phase 1 | [Plan / RPP approval] | PL |
| Phase 2 | [Recruit] | |
| Phase 3 | [Fieldwork] | |
| Phase 4 | [Synthesis] | |
| Phase 5 | [Readout] | |

## Topic

[One high-level sentence — what this study is about and the user-grounded thing it will define. Leadership reads this first; it replaces the old Goal row. Lead with the *why* before the *how*.]

## TL;DR Summary of Findings

*To be filled out at the end of the study.*

## Background

Detailed context, all relevant background. Two scannable sub-blocks — never a wall of prose.

### Problem Statement

3 bullets max, each with **bold lead-word + 1-sentence explanation**. Leadership scans the 3 bold keywords, then reads the explanations only if a keyword catches their eye.

- **[Lead-word, e.g., "Threshold gap"]** — [One-sentence explanation of the gap.]
- **[Lead-word, e.g., "Failure-mode blindspot"]** — [One-sentence explanation of the gap.]
- **[Lead-word, e.g., "A/B interpretation risk"]** — [One-sentence explanation of the gap.]

### Product Context

3-4 bullets max, 1-2 sentences each (NOT a paragraph).

- [Concise bullet — e.g., "Recipes feature is strategic for the Meals workstream."]
- [Concise bullet — e.g., "Improved-mapping A/B test starts end of May (Aasish prepping pipeline, Dimitri running, Aasish analyzing)."]
- [Concise bullet — e.g., "This research runs in parallel and informs A/B *interpretation* — does not gate the launch."]

> **Why H3?** The two subheadings (Problem Statement / Product Context) are sub-headings *within* Background & Context. Rendering as `###` H3 (bold NAV 11pt in the Jedida Reporting styler) gives them visual hierarchy distinct from the body text. Do NOT use `**Problem Statement**` bold paragraphs — that flattens the hierarchy. See `feedback_canonical_research_plan_styler.md`.

## Existing Insights
*(what we already know — top 3-5, each with a verbatim source link)*

Added per the 2026-06-02 team workshop (Prakriti + Amalia): the plan must surface *what's already known* near the top, BEFORE objectives — so the team doesn't reinvent the wheel and so leadership sees the existing evidence base first. Sourced from the research-insights agent + Glean + prior studies in Step 1.5.

Each item is **one plainly-stated insight + a clickable source link**. Where the insight rests on a specific prior finding, quote it **verbatim** (Amalia's rule) so the reader can trust it without re-checking. NEVER state an insight without a source; if no prior research exists, say so explicitly.

1. **[Insight stated plainly.]** "[Verbatim supporting line from the source, if applicable.]" — [Source name](URL)
2. **[Insight stated plainly.]** — [Source name](URL)
3. **[Insight stated plainly.]** — [Source name](URL)

> If there is genuinely no prior research on the topic: *"No prior user research on [topic] — this is net-new territory."* Do not pad with generic or assumed insights.

## Objectives

The business objective(s) this research will inform, in bullet form (ResOps row name: "Objectives"). Numbered list, 3 objectives. **Keep each short and scannable** — one tight sentence with the *what* bolded, followed by ≤1 sentence of decision-context. Bold the keywords *inside* the objective (the decision-driving phrase), not just the lead.

Objectives are statements per Anderson (2022) — if it ends in a question mark, rewrite.

1. **[One-line objective statement with the decision-driving phrase bolded.]** [Optional ≤1 sentence: what's missing today / what decision it unlocks.]
2. **[One-line objective statement.]** [Optional ≤1 sentence of context.]
3. **[One-line objective statement.]** [Optional ≤1 sentence of context.]

## Key Research Questions

The key questions stakeholders hope to answer through research, comprehensive, bullet format (ResOps row name: "Key Research Questions"). Numbered list. **Keep each short** — one broad project-level question with the strategic uncertainty bolded, followed by ≤1 sentence of follow-on framing.

These are NOT TEDW interview probes ("Walk me through the last time…") — those belong in the moderation/discussion guide, a downstream artifact generated by `/moderation-guide`. See `references/content-rules.md` §1.

1. **[Short, broad project-level question with the key uncertainty bolded?]** [Optional ≤1 sentence of follow-on framing.]
2. **[Short, broad project-level question?]** [Optional ≤1 sentence of follow-on framing.]
3. **[Short, broad project-level question?]** [Optional ≤1 sentence of follow-on framing.]

## Hypotheses / Questions of Interest from XFN leads
*(expected outcomes / team beliefs to pressure-test per Portigal 2023 — each traces to an item in Existing Insights)*

3 bullets, each one sentence. The team's current beliefs / expected outcomes the study will validate or invalidate (ResOps row name: "Hypotheses / Questions of Interest from XFN leads" — "identify the expected outcome"). They sit **after Key Research Questions and before What-decisions** because they are what the methodology is designed to test.

- **H1** — [Team belief / expected outcome, one sentence.]
- **H2** — [Team belief / expected outcome, one sentence.]
- **H3** — [Team belief / expected outcome, one sentence.]

## What decisions will be made with such research?

The concrete decision(s) the audited Step-1.6 primary decision feeds. Bullet form. Each must be a **real fork** — a different finding leads to a different action. If a "decision" doesn't change anyone's behavior, it isn't one; cut it or sharpen it.

- **[Decision 1 — bold the decision, then who owns it / what would change.]**
- **[Decision 2.]**

## What Research Priorities is this relevant to (Themes)

Which research themes / org priorities this study maps to (ResOps row name). Short bullets.

- [Theme / priority 1 — e.g., "Good Ingredient Impressions (Meals northstar)."]
- [Theme / priority 2 — e.g., "AI quality evaluation."]

## Proposed Research Timeline

The ResOps operational milestone list (NOT the phase grid up top — this is the dated schedule). 2-column table (Milestone | Date).

| Milestone | Date |
|---|---|
| RPP share at Crit / solicit feedback | [date] |
| Submit Participant Recruiting Request | [date] |
| Recruit dates *(ResOps SLA: minimum 10 business days notice)* | [range] |
| Study Launch Date | [date] |
| Study End Date | [date] |
| Insights Synthesis | [range] |
| Final Deliverables | [date] |
| Upload Findings Deck to Sharpr | [date] |

## Project Details

Single crisp table — the ResOps "Project Details" block. Absorbs method, sampling, stimuli, dependencies, compensation, platform, and deliverable format. No prose rationale paragraphs — just the facts. **Multi-criteria cells use `<ul><li>` bullets**, not run-on sentences (e.g., Sampling cohorts, multiple stimuli).

| Element | Detail |
|---|---|
| **Method + Approach** | *Minimum evidence to move the decision:* [how research is conducted + tools + number of completes — be specific, e.g., "8 moderated interviews (45 min) + survey N=75–100, 5-pt acceptability scale"]. [Lean alternative if timeline tightens.] |
| **Sampling Plan / Participants** | <ul><li>[Participant base + behavioral cohorts, e.g., "Ordered from a recipe ≥2× in past 60 days"]</li><li>[Comparative cohorts spelled out]</li><li>[# completes per cohort + total sample needed]</li><li>[Link to query / contact list]</li></ul> |
| **Stimuli** | [Relevant links — e.g., "5–6 mocked recipe→cart scenarios at varying mapping quality (Figma)"] |
| **Dependencies** | [Blazer query / CSV link for the recruit; any blocking dependency + its date. Surface schedule/recruitment RISKS here with a date or owner — ResOps has no separate Risks section.] |
| **Compensation** | [$X per X] |
| **Research Platform** | [e.g., Zoom (sessions), Qualtrics (survey), Dovetail (synthesis)] |
| **Deliverable Format** | [e.g., "Readout deck (Google Slides) + severity matrix (Sheet)"] |

## Additional

**Documents** — links to all relevant documents. ALL items are clickable markdown links — `[Document Name](URL)`. For docs that don't exist yet, use `(#)` as a placeholder URL so the link styling shows up; the researcher fills in real URLs as the docs are created.

**Auto-linking rule (Rule #26):** Any document the researcher mentions in the kickoff inputs (PRD, Slack thread, Glean doc, brief) MUST appear here as a clickable link — use the real URL when present in the source, else `(#)`.

- **[Discussion Guide](#)** — to be generated via `/moderation-guide` skill
- **[Questionnaire / Survey (Qualtrics)](#)** — [drafted by date]
- **[Screener](#)** — [drafted by date]
- **[Datasheet / recruit query](#)** — [context]
- **[PRD / Brief](#)** — [auto-pulled from researcher's input; context, e.g., "pending Trace"]
- **[Stimulus mocks (Figma)](#)** — [context]
- **[Final Report](#)** — [created at readout]
- **[Other relevant doc surfaced in kickoff](#)** — [context]
```

**IMPORTANT:** The plan MUST end at **Additional → Documents**. Do NOT append extra sections (no "FAQ", no "Open Questions", no "Risks", no "Resources & Links"). Additional/Documents is the final element — it matches the ResOps RPP template's last block.

**Mapping from the old (pre-2026-06-08) template → ResOps RPP structure:**

The skill previously used a Goal-led Parameters table + standalone Methodology / Timeline / Deliverables / Risks / Appendix sections. Those were re-mapped onto the official ResOps RPP (Doc `1s6Lg4ZsiIypqANdpg4hrCwxkgwP0qOwJvGNekzgj9k0`) on 2026-06-08 per Jedida's **"Option B"** (match ResOps order, keep the richer Jun-2 content):

| Old section | → ResOps RPP home |
|---|---|
| Parameters table → **Goal** row | **Topic** (the leadership one-liner) |
| Parameters table → **Primary Decision** row | **What decisions will be made with such research?** (its own section) |
| Parameters table → Study Type / Method / Sample / Tools | **Project Details** (Method + Approach, Sampling Plan / Participants, Research Platform) |
| Parameters table → Timeline row | **Proposed Research Timeline** (dated milestones) + the **Research Timeline** phase grid in the header |
| **Methodology** (absorbed Participants) | **Project Details** (Method + Approach, Sampling Plan / Participants, Stimuli) |
| **Deliverables** | **Project Details → Deliverable Format** + **Additional → Documents** |
| **Risks** *(no Risks section in ResOps)* | **Project Details → Dependencies** (surface schedule/recruit risks here with a date or owner) |
| **Appendix → Additional Documents** | **Additional → Documents** |
| **Appendix → Previous Research** | **Existing Insights** (verbatim sources, after Background) |

**Sections KEPT from the Jun-2 workshop enhancements (Option B — folded into ResOps order, not dropped):**
- **Existing Insights (H2, after Background).** Surfaces what's already known — top 3-5 prior findings, each with a verbatim quote + clickable source — so the team doesn't reinvent the wheel (Prakriti + Amalia). Sourced via the research-insights agent + Glean in Step 1.5. ResOps has no native row for this; it lives between Background and Objectives.
- **Hypotheses now matches the ResOps row name** ("Hypotheses / Questions of Interest from XFN leads") and sits after Key Research Questions — consistent with both the team workshop and the ResOps template.
- **Bold-lead scannable styling** (Problem Statement bullets, bold keywords inside Objectives/Questions) is preserved on top of the ResOps skeleton.
- **"Minimum evidence to move the decision"** framing is carried into Project Details → Method + Approach.

---

### CONTENT GENERATION RULES

1. **Topic leads the plan.** The ResOps RPP opens with **Topic** (the leadership one-liner) → TL;DR → Background. There is NO Goal-led Parameters table anymore (re-mapped to ResOps on 2026-06-08 — see the old→ResOps mapping under the OUTPUT TEMPLATE). The old "Goal" is now Topic; the old "Primary Decision" is now its own *"What decisions will be made"* section; Study Type / Method / Sample / Timeline live in Project Details + Proposed Research Timeline. Never reorder the canonical section order.
2. **Objectives are statements, not questions.** If an objective ends in a question mark, rewrite it. Cite Anderson (2022) when pushed back on.
3. **Every objective ties to a decision.** Apply Anderson's Mad-Lib test ("I need [info] to make [decision] that impacts [team goal]"). If it fails, cut or rework.
4. **Objectives compress to bold statement + 1-2 sentence context.** NOT H3 + sub-bullets, NOT a 2-column table. A numbered list of 3 objectives, each with the *what* in bold and the *why* as plain prose. See OUTPUT TEMPLATE.
5. **Research questions in the plan are BROAD project-level questions.** They capture the strategic uncertainty the study resolves — NOT TEDW-format interview probes ("Walk me through…", "Tell me about…"). TEDW probes belong in the moderation/discussion guide, generated by `/moderation-guide`. Single source of truth: `references/content-rules.md` §1.
6. **Research questions = bold question + 1 sentence framing.** A numbered list of 3 questions, each one bold broad question followed by one sentence of follow-on framing (sub-uncertainty or angle). NOT a table.
7. **Hypotheses are a STANDALONE H2 section named "Hypotheses / Questions of Interest from XFN leads," placed AFTER Key Research Questions.** This matches BOTH the 2026-06-02 workshop (Prakriti: hypotheses "comes after objectives and research questions… then it decides your methodology") AND the ResOps RPP row name — confirmed canonical 2026-06-08, no longer provisional. 3 one-sentence bullets stating the team's beliefs / expected outcomes the study will validate or invalidate (Portigal 2023 confirmation-bias guardrail). Each hypothesis should trace back to an item in the Existing Insights section.
8. **Problem Statement = 3 bold-lead bullets, not paragraphs.** Each bullet has a 1-3 word bold lead-word + one-sentence explanation. Leadership scans the 3 bold keywords before reading any explanation.
9. **Product Context = 3-4 bullets, not paragraphs.** 1-2 sentences each. If you find yourself writing a paragraph, break it into bullets.
10. **Project Details absorbs Method, Participants & Recruitment.** No standalone Methodology or Participants section — Method + Approach, Sampling Plan / Participants, Stimuli, Dependencies, Compensation, Research Platform, and Deliverable Format are all rows in the single ResOps **Project Details** table.
11. **Proposed Research Timeline is the dated milestone table** (Milestone | Date), separate from the **Research Timeline** phase grid in the header. Milestones follow ResOps: RPP share at Crit → Recruiting request → Recruit dates (SLA: min 10 business days) → Launch → End → Synthesis → Final Deliverables → Sharpr upload.
12. **Deliverables fold into Project Details → Deliverable Format + Additional → Documents.** No standalone Deliverables section. Name the format in the Deliverable Format cell; list the actual artifact links under Additional → Documents.
13. **Risks fold into Project Details → Dependencies — ResOps has no Risks section.** Surface schedule/recruit risks inside the Dependencies cell, each with a date or owner. "Schedule risk" is not a risk; "Prototype not finalized until April 30; fieldwork cannot begin before then" is.
14. **Additional → Documents items are clickable markdown links.** Format: `[Document Name](URL)`. For docs that don't exist yet, use `(#)` as a placeholder URL so the link styling shows up; researcher fills in real URLs as the docs land. This is the single document list (no separate Previous Research subsection — prior research lives in Existing Insights).
15. **Plan ends at Additional → Documents.** No FAQ, no separate Resources & Links, no Risks, no Open Questions section — Additional → Documents IS the final element and the resources list.
16. **RACI lives in the document header.** Above Topic, under Key Stakeholders, as 4 disc bullets (R/A/C/I), each with `[TBD — fill in]` placeholders for unknown names. NO standalone Stakeholders & RACI H2 section.
17. **Sample size defended by decision, not dogma.** Open with the decision the study informs; cite canon (Nielsen 2000 for usability N=5; Guest et al. 2006 for IDI saturation) only when questioned.
18. **No interface terminology in research questions.** Describe user goals, not UI. "Find a recipe" not "click the search icon."
19. **Time-aware protocol shape.** If the Methodology row includes a session-protocol breakdown, the time slots must sum to session duration.
20. **Anchor-not-substance bolding.** Bold the *answer-word*, never the row label. Tables aim for ≤10% bold density. See `jedi-doc-styling-1/references/bolding-philosophy.md`.
21. **Bullet bodies are complete sentences, not fragments.** A reader landing on a single bullet without surrounding context must still understand it. See `jedi-doc-styling-1/references/bolding-philosophy.md`.
22. **Background subheadings render as H3, not bold paragraphs.** Problem Statement / Product Context are sub-sections *within* the H1 "Background & Context" — they MUST be `###` H3 (rendered as bold NAV 11pt by the Jedida Reporting styler) so they have visual hierarchy above the bullet body text. *(Hypotheses is NO LONGER a Background sub-section as of 2026-06-02 — it's now a standalone H2 after Research Questions; see Rule 7.)* Do NOT use `**Problem Statement**` bold paragraphs — that flattens the hierarchy. Same rule applies to any sub-section break within an H1 (e.g., a future "Constraints" or "Open Questions" inside Background). The hierarchy is: **H1 section (Background & Context, 18pt NAV) → H3 sub-section (Problem Statement, 11pt NAV bold) → 10pt body bullets with inline `**bold lead-word**`**.
23. **Objectives + Research Questions stay tight and scannable.** Each item = one short bold statement + optional ≤1 sentence of context. Bold the decision-driving keywords *inside* the statement (not just the lead word). If an objective/question needs more than 2 lines of total prose, it's doing too much — split or cut. Bold density across the 3 items stays ≤15%.
24. **Project Details multi-criteria cells use `<ul><li>` bullets.** When a single cell (Sampling Plan / Participants, Stimuli, Dependencies) carries more than one distinct criterion, render each criterion as a bullet inside the cell via inline HTML (`<ul><li>...</li><li>...</li></ul>`) so the cell reads as a scannable checklist. Single-criterion cells (Compensation, Research Platform, Deliverable Format) stay as one line. Reason: Jedida confirmed 2026-05-20 that "each criterion for a participant should be in a different row" — bullets inside the cell are the Markdown-compatible equivalent that survives both the upload and the Jedida Reporting styler.
25. **Risks stay short and high-level — one line each, bold risk-name as lead.** Pattern: `**[Risk name]** — [one-line specific description]. *Mitigation:* [one-line mitigation].` Never let a risk sprawl into a paragraph; if it needs more depth, that depth belongs in the Risk Register, not the plan.
26. **Additional → Documents auto-links every doc surfaced in the kickoff inputs.** When parsing the kickoff brief / PRD / Slack thread / Glean docs in Step 1, capture every document name the researcher cites (e.g., "OGLT Operating Sync notes", "CSS Survey instrument", "Screener", "Moderation Guide", "Dovetail project", "PII consent script") and emit each as a clickable markdown link `[Document Name](URL)` under Additional → Documents — use the real URL if found in the kickoff source, else `(#)` placeholder. Never leave a referenced upstream doc out. The researcher should not have to re-type doc names she already mentioned. If this study arrived via `/diy-triage` — especially a "both tracks" routing call — also link back to the `/diy-triage` output itself, and, if one exists, sideways to the sibling DIY-track deliverable (e.g. a `/diy-research-plan`, `/screener`, or `/unmod-script` output already in flight for the same ask), in addition to whatever else this rule already requires.
27. **Discover existing context BEFORE asking logistics** *(added 2026-06-02 workshop)*. Step 1.5 runs first: query the research-insights agent (`mcp__research-insights__research_insights__updated`) + Glean for prior research, then read the project folder. Surface what you found — verbatim background summary + top-5 existing insights + proposed hypotheses — and ask the researcher to *confirm or correct*, not to supply from scratch. Only after that does Step 1.6 collect logistics (decision, name, goal, timeline). The demo failure mode was asking "what's the study name?" before establishing what's already known — never lead with logistics.
28. **Every insight and background claim carries a verbatim source** *(Amalia's rule, 2026-06-02)*. In Existing Insights, each item is one plainly-stated insight + a clickable source link; where it rests on a specific prior finding, quote that line **verbatim** so the reader trusts it without re-checking. NEVER state an insight without a source. If no prior research exists, say so explicitly — *"No prior user research on [topic] — this is net-new territory."* — never pad with generic or assumed insights.
29. **Run an active decision-quality audit in Step 1.6** *(added 2026-06-02)*. Don't passively accept the stated decision. Challenge it: Is there exactly one "Must Answer" decision? Is it a real fork (a different finding → a different action), or is the decision already made and the research is theater? Is the scope tight enough to answer this quarter? If the decision is fuzzy or pre-baked, flag it before building the plan — a plan anchored to a non-decision wastes the study.
30. **Methodology = the minimum evidence to move the decision** *(added 2026-06-02)*. Frame the method as the leanest valid path to a "good enough" answer for the core decision — not the most comprehensive study possible. Lead with that minimal recommendation, then offer 1-2 alternatives (faster/cheaper vs. higher-confidence) so the researcher chooses the tradeoff. Flag any conflict between the chosen method and the stated timeline.
31. **Hand off to `/multi-agent-check` after the draft** *(added 2026-06-02, per Prakriti + Jedida)*. The generated plan is a DRAFT (step 1). Step 6 routes it to the `multi-agent-check` skill (step 2) for the parallel-lens critique before it's shared. Never present the draft as final — always surface the draft → multi-agent-check → share sequence.

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
| **Clarity of Objectives** | Are objectives written as statements (not questions), bold lead + 1-2 sentence context (per v2 lock-in)? Does the context name *what's missing today* and *what decision the objective unlocks*? Does each objective pass Anderson's Mad-Lib test ("I need [info] to make [decision] that impacts [team goal]")? Flag any objective that ends in a question mark, exceeds 2 sentences of context, or lacks a decision link. |
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

## Step 5: Offer Google Docs Upload + Apply Canonical Styling

After generating the plan, ask:

> "Your research plan is ready! Would you like me to upload it to Google Docs?"

If yes, run the **3-step pipeline** below. **Default path is Jedi's Doc Styling 1** — Jedida locked it in on 2026-05-12 as the canonical look for all research plans. Only run the alternative pipelines if the researcher explicitly picked a different option in Step 3.5.

### 5.1 — Upload markdown to Google Docs

```bash
# Preferred: gws CLI (auth-bridge fallback per memory/reference_gws_auth_bridge.md)
cd <directory containing plan.md>
gws drive files create \
  --upload <plan.md> \
  --upload-content-type 'text/markdown' \
  --json '{"name":"<Plan Title>","parents":["<P5 or matching project folder ID>"],"mimeType":"application/vnd.google-apps.document"}'

# Alternative: md2doc upload <plan.md>     (requires Python 3.10+; use `uv run` if local Python is older)
```

This creates the Google Doc with content but **no styling**. Capture the resulting `DOCUMENT_ID` from the JSON response.

**Path note:** the `gws drive files create --upload` command resolves paths relative to the current working directory and rejects `..`-traversal. Always `cd` into the directory containing the markdown file first, then pass just the filename.

### 5.2 — Apply Jedi's Doc Styling 1 (DEFAULT)

```bash
python3 ~/.claude/skills/jedi-doc-styling-1/scripts/apply_jedi_style_1.py <DOCUMENT_ID>
```

This runs 5 passes (idempotent; safe to re-run):

| Pass | What it does |
|---|---|
| 0 — Cleanup | Scans for `baselineOffset: SUBSCRIPT` artifacts (md2doc's `<br>` is a known offender — gotcha #13) and clears them |
| 1 — Document | Default text style: Arial 11pt black; sets margins and page setup |
| 2 — Named styles | TITLE → DM Serif Display 26pt bold `PRIMARY_GREEN` (`#2D4A3E`); SUBTITLE → DM Sans italic green breadcrumb; HEADING_1/2/3 → green hierarchy |
| 3 — Patterns | RACI block (disc bullets, hanging indent, bold labels, chip backgrounds), parameters table heading row, etc. |
| 4 — Tables | Dark forest-green header rows for design tables; cell padding; border colors |
| 5 — Lists | Bullet preset cleanup, numbered-list anchor styling |

All canonical specs live in `~/.claude/skills/jedi-doc-styling-1/references/design-spec.md` (palette, typography, RACI recipe, table layout). All API landmines live in `~/.claude/skills/jedi-doc-styling-1/references/api-gotchas.md`.

### 5.3 — (Alternative styles, only if researcher explicitly picked one in Step 3.5)

```bash
# Jedi Style 2 — GlossGenius look
python3 ~/.claude/skills/jedi-doc-styling-2/scripts/apply_jedi_style_2.py <DOCUMENT_ID>

# Jedida's Design Template — original DM Serif + RACI chips + design table
python3 ~/.claude/skills/jedidas-design-template/scripts/apply_template_styling.py <DOCUMENT_ID>
```

Surgical passes from `jedi-doc-styling-1` (only if v1.2.0 content patterns landed):

```bash
python3 ~/.claude/skills/jedi-doc-styling-1/scripts/restyle_section_headers.py <DOCUMENT_ID>
python3 ~/.claude/skills/jedi-doc-styling-1/scripts/apply_bullet_anchor_spec.py <DOCUMENT_ID>
python3 ~/.claude/skills/jedi-doc-styling-1/scripts/apply_bulleted_leadins.py <DOCUMENT_ID>
```

### 5.4 — Verify the styling landed

```bash
# DEFAULT — verify Style 1
python3 ~/.claude/skills/jedi-doc-styling-1/scripts/verify_jedi_style_1.py <DOCUMENT_ID>

# Alternatives
python3 ~/.claude/skills/jedi-doc-styling-2/scripts/verify_jedi_style_2.py <DOCUMENT_ID>
python3 ~/.claude/skills/jedidas-design-template/scripts/verify_styling.py <DOCUMENT_ID>
```

Each verifier exits non-zero if any check fails — re-run the corresponding apply script if so. Aim for 100% pass; <100% means a styling regression to investigate.

### 5.5 — File it

Place in the correct Google Drive project folder per `~/CLAUDE.md` (route by **subject matter, not recency** — see CLAUDE.md routing cheat sheet):

| Project | Subject matter | Drive folder ID |
|---|---|---|
| **P1** — Parser Evaluation (HITL) | Parser V2/V5, HITL annotation, Guidelines v2.0, parser eval (any phase) | `1mQufRUr8GZf5ruZKIrVpSJSt9LhhKJuU` |
| **P2** — Golden Dataset & E2E AIQA | Golden Dataset, AIQA framework, 3-pronged eval, "Good Ingredient Impressions," Bucket sampling | `19rmLOpVoVgtZkjfTJHx1UkHBI-H5HZJV` |
| **P3** — AI Recipe Corpus | AI Recipe Corpus, AI-generated recipe quality, 5 Tier 1 dimensions | `1W52c36zeY0r1EYtVFctcFMsrWY6c-BMK` |
| **P4** — Research OKR / AI Enablement | Research OKR, AIxUXR Playbook, research-team-skills, All Hands deck, skills/automations | `1zw--MN_umb_VczMmVhOss6PTn-BCJleg` |
| **P5** — End-to-End Meals Research | End-to-end meals umbrella spanning ingredient↔parsed↔product, substitution & quantity logic, post-2026-05-11 pipeline | `1XZ9iwyg2U47_nNkpuI-U1DxN1-DpZ519` |
| **P6** — Search Personalization | MAVEN, LLM Relevance Oracle, brand similarity, lost-intent resurfacing, Suggest, QU, non-English search | `1HSCcGXr06nqY7wBXbQD9icwew284RCrW` |
| **Research/** — general | Studies not tied to any project bucket | (no Drive folder; local only) |

Share the Google Doc link back to the researcher and offer next-step skills: `/moderation-guide` to generate the discussion guide from the approved plan.

### Auth note

The styling scripts use the `gws` CLI (`/Users/jedidamilton/.config/gohan/bin/gws`), not the slides-generator OAuth token (which lacks Docs scope — gotcha #9). If `gws` isn't available, see `memory/reference_gws_auth_bridge.md` for the auth-bridge fallback.

## Step 6: Hand off to Multi-Agent Check (draft → critique → share)

*(Added per the 2026-06-02 team workshop — Prakriti + Jedida agreed the generated plan is a DRAFT, not a finished artifact.)*

The plan this skill produces is **step 1 of two**: a strong first draft. Before it's shared with stakeholders, it goes through `multi-agent-check` (**step 2**) — the parallel-lens critique gate Jedida already owns. Always make this sequence explicit; never present the draft as final.

After upload + styling, tell the researcher:

> "This is a solid draft. The next step is to pressure-test it through the multi-agent check before sharing — want me to run `/multi-agent-check` on it now?"

If yes, invoke the **`multi-agent-check`** skill on the generated plan (the Google Doc or the local markdown). Per its hardcoded pre-flight protocol, it will ask 1-2 clarifying questions and show its plan before dispatching the 6 review lenses (Factual Verifier, Quantitative Rigor, Overreach Detector, Prakriti's strategic lens, ML/DS Partner accuracy, Voice & Clarity). Let it run its own flow — do not pre-empt its questions.

The full pipeline the team agreed on: **draft (this skill) → `/multi-agent-check` → apply fixes → share.** For analysis-stage work the chain is longer (5-pass analysis → dashboard → multi-agent-check) but for a research *plan*, draft → multi-agent-check → share is the gate.

## Tool usage

- **AskUserQuestion** — Gather inputs, present recommendations, get approvals, ask for style reference.
- **`mcp__research-insights__research_insights__updated`** *(the "User & Market Research" agent — PRIMARY discovery tool, Step 1.5)* — This is the dedicated Glean research agent Prakriti asked the skill to lead with. Query it FIRST to surface what's already known about the topic before asking the researcher anything. Returns synthesized prior-research insights with sources. Verified wired in this environment (2026-06-05).
- **Glean keyword + chat** (`mcp__glean__search`, `mcp__glean__chat`) — Secondary discovery in Step 1.5: `search` for keyword hits across indexed Drive/docs, `chat` for synthesis across multiple sources. Use after the research-insights agent to widen the net.
- **Snowflake** — *NOT wired as an MCP in this environment (verified 2026-06-05).* Only the `snowflake-development` and `data:write-query` skills exist. When a plan needs behavioral/usage data, FLAG that Snowflake isn't connected and route the researcher to those skills or to a DS partner — never fabricate query results.
- **Glean** (`mcp__glean_default__read_document`) — Read Google Doc PRDs or style references when URL is provided.
- **google-docs:fetch-google-doc** — Alternative fetcher for Google Docs.
- **Slack MCP** — Pull kickoff threads when a Slack URL is provided.
- **gws-docs** (or md2doc `upload-gdoc.py`) — Upload markdown to Google Docs.
- **`jedidas-design-template` skill** — The single source of truth for Jedida's canonical document design. All styling work delegates here. Triggered explicitly (e.g. "apply Jedida's design template") or implicitly via Step 5 of this skill.
- **`~/.claude/skills/jedidas-design-template/scripts/apply_template_styling.py`** — 6-pass styling pipeline (header → subscript cleanup → body H1s → section bars → sub-labels → sticky header).
- **`~/.claude/skills/jedidas-design-template/scripts/verify_styling.py`** — Regression checker. Run after every styling pass.
- **`~/.claude/skills/jedidas-design-template/scripts/_helpers.py`** — Shared `gws` CLI wrappers, color/font constants, paragraph/table finders, request builders. Import from custom passes.
- **`~/.claude/skills/jedi-doc-styling-1/scripts/restyle_section_headers.py`** *(v1.2.0)* — Surgical pass: H2 banners (0pt indent), H3 left-border, lead-in labels, empty-paragraph cleanup. Run after upload when content uses v1.2.0 patterns.
- **`~/.claude/skills/jedi-doc-styling-1/scripts/apply_bullet_anchor_spec.py`** *(v1.2.0)* — Surgical pass: regex-detects `Anchor:` prefixes on bullets, applies DM Sans 12pt bold ACCENT_GREEN to the anchor + DM Sans Medium 11pt black to the body.
- **`~/.claude/skills/jedi-doc-styling-1/scripts/apply_bulleted_leadins.py`** *(v1.2.0)* — Surgical pass: detects short bold non-list labels immediately followed by bullets; styles label deep-forest 11pt and overrides sub-bullet indent (18pt/0pt — gotcha #16).
- **references/content-rules.md** — Single source of truth for research-plan content rules, restructured to the canonical ResOps RPP on 2026-06-08 ("Option B"): broad vs. probing Q's (§1), 3-question default mapped 1:1 to objectives (§2), Key Research Questions as numbered list not table (§3), Objectives as bold + 1-2 sentence context (§4), Topic / What-decisions / Themes replace the old Parameters table (§5), Background = Problem Statement + Product Context followed by Existing Insights with verbatim sources (§6), Project Details absorbs Method + Participants + Stimuli + Dependencies + Compensation + Platform + Deliverable Format — Risks fold into Dependencies, Deliverables fold into Deliverable Format/Documents (§7), Proposed Research Timeline as dated milestones distinct from the header phase grid (§8), Hypotheses / Questions of Interest standalone after Key Research Questions (§9), Additional → Documents as clickable markdown links + the final section (§10), RACI in header (§11). Load when generating or editing the plan.
- **references/research-plan-methodology.md** — Load on demand for sample-size defense, methodology depth, canonical citations, pitfall catalog.
- **`~/.claude/skills/jedidas-design-template/references/visual-spec.md`** — Canonical palette, typography, RACI recipe, design-table layout, sticky-header constraint. Source of truth for Jedida's design template.
- **`~/.claude/skills/jedidas-design-template/references/api-gotchas.md`** — 13 documented Google Docs `batchUpdate` landmines (with wrong vs right examples) — read before writing any custom styling pass.

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
| Jedida's design template — palette, typography, RACI block, design-table layout, sticky-header constraint | Diet Personalization Mod Guide reference doc (`1ErEB2IZuvS3EYyLt8OWdwZbGy4tTQtIRMBGoD4WaYIQ`) + International Expansion: Retailer e-commerce header (`1K7IgFKKxiinsDY4lrhG5lAI3argJMELjqT2QHuBJP-4`). Measured directly via Google Docs API on 2026-05-04. Encoded in `~/.claude/skills/jedidas-design-template/` (single source of truth). |

**Methodology note:** This skill is grounded in Instacart's AIxUXR Playbook (H.E.A.R.T. framework + RPP Critique) in addition to the external UX research canon above. Internal Playbook sources provide the Responsible AI guardrails, the critique persona patterns (Generalist / Staff / PM / Sr. Leader / DEI), and the human-in-the-loop accountability model; external canon provides the methodological foundation.

The plan is the primary output — it should be polished enough to share with stakeholders as-is in markdown, and to upload as a Google Doc without post-edit.
