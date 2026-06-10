# Content Rules — Research Plan Skill

These are the **content** rules for a research plan — what goes where, how questions are scoped, how objectives are compressed. They govern the *substance* of the doc, not its typography. The typography spec lives in the [`jedi-doc-styling-1`](../../jedi-doc-styling-1/) skill.

**Companion files (cross-referenced):**
- [`jedi-doc-styling-1/references/bolding-philosophy.md`](../../jedi-doc-styling-1/references/bolding-philosophy.md) — what to bold, ≤10% density, complete-sentence bodies.
- [`jedi-doc-styling-1/references/design-spec.md`](../../jedi-doc-styling-1/references/design-spec.md) — anchor + body type spec (§9d), Bulleted Lead-in pattern (§9e).

Single source of truth: **content rules live here in `research-plan`; styling rules live in `jedi-doc-styling-1`.** Each skill links to the other rather than duplicating.

**Locked in: 2026-05-12. Updated: 2026-06-02 (team workshop). Restructured to canonical ResOps RPP: 2026-06-08.**

On **2026-06-08** Jedida supplied the official ResOps **Research Project Plan (RPP)** template (Doc `1s6Lg4ZsiIypqANdpg4hrCwxkgwP0qOwJvGNekzgj9k0`) as *the* format, and chose **"Option B"**: adopt the ResOps section names + order, but **keep the richer Jun-2 content folded in** (Existing Insights with verbatim sources, bold-lead scannable styling, "minimum evidence to move the decision" framing). This file now reflects that structure. The canonical section order is:

> Header (Key Contacts → Key Stakeholders/RACI → Research Timeline phase grid) → **Topic → TL;DR Summary of Findings → Background → Existing Insights → Objectives → Key Research Questions → Hypotheses / Questions of Interest from XFN leads → What decisions will be made with such research? → What Research Priorities is this relevant to (Themes) → Proposed Research Timeline → Project Details → Additional / Documents.**

The interactive pop-up (SKILL.md Step 3) walks these sections in this SAME order, one at a time — first pop-up is Existing Insights — so researchers approve and brainstorm each section in sequence.

---

## 1. Key Research Questions = broad project-level, NOT interview probes

This is the **most-confused rule**, so it leads. *(ResOps row name: "Key Research Questions.")*

| Type | Belongs in | Format | Example |
|---|---|---|---|
| **Broad research question** | The research plan's *Key Research Questions* section | Bold broad question + 1 sentence of follow-on framing | "**What does 'good' recipe-to-cart mapping mean to users?** What signals make a cart feel acceptable vs. broken, and how does that judgment shift when the recipe is for tonight's dinner vs. weekend prep?" |
| **Probing interview question** | The downstream **moderation / discussion guide** (separate artifact) | TEDW stem (Tell me / Explain / Describe / Walk me through) | "Walk me through the last time you cooked from a recipe you found in the app." |

Do NOT put TEDW probes in the research plan. The plan answers *what the study will resolve at a project level*. The moderation guide answers *what we'll literally ask participants in a session*. Different doc, different scope, different generation skill (`/moderation-guide`).

### Why it matters

Leadership reads the research plan to decide whether to fund / scope / time-box the study. Probing questions look like fieldwork minutiae and bury the strategic bet. Broad questions surface the bet immediately:

> *"What does 'good' recipe-to-cart mapping mean to users?"* — leadership instantly knows what's on the line.

If a researcher pushes back, the answer is: probes belong in the moderation guide because that's where they're actually moderated. The plan is for the *decision* the study informs.

---

## 2. Default = 3 broad questions, mapped 1:1 to 3 objectives

The template specifies **3 key research questions** by default, mapped 1:1 with the 3 objectives. This is a substance rule, not a formatting one — most studies have one strategic uncertainty per objective.

| Pattern | When to apply |
|---|---|
| **3 questions, 1:1 with objectives** *(default)* | Most studies. Each objective has exactly one broad uncertainty driving it. |
| **Fewer than 3** | Rare — only when one objective has no question of its own (i.e., it's pure synthesis, not investigation). Document why. |
| **More than 3** | Rare — only when one objective genuinely has two distinct broad sub-uncertainties (e.g., "what counts as a substitute?" AND "in what order are substitutes chosen?"). Otherwise it's probe-leakage. |

If a researcher's first draft has 5+ questions, that's a smell that probes leaked in. Audit each — if a question reads like "Tell me about…" or "Walk me through…", move it to the moderation guide.

---

## 3. Key Research Questions = numbered list, NOT a table

The Key Research Questions section is a **numbered list**, not a table. Each item is one bold broad question + one sentence of follow-on framing.

```
## Key Research Questions

1. **[Bold broad project-level question?]** [One sentence of follow-on framing — what sub-uncertainty or angle this opens.]
2. **[Bold broad project-level question?]** [One sentence of follow-on framing.]
3. **[Bold broad project-level question?]** [One sentence of follow-on framing.]
```

Rules:

| Rule | Reasoning |
|---|---|
| **Numbered list, not a table.** Each list item is a paragraph: bold question + plain prose framing. | The v1 2-column table format (Topic \| Question) implied separate "topic anchors" for each question. The v2 lock-in dropped that — questions stand on their own; the bold question IS the anchor. |
| **One bold north-star phrase per question.** Bold the entire broad question; leave the framing sentence plain. | Per [`bolding-philosophy.md`](../../jedi-doc-styling-1/references/bolding-philosophy.md) — multi-bold dilutes the signal. |
| **End the bold with the question mark.** The question mark is part of the bold span, not appended after. | Visual closure — the eye recognizes a bold question as a unit. |
| **Framing sentence = ONE sentence, not two.** If you need two sentences, the question is too big — split into two questions. | Forcing one-sentence framing keeps the section scannable. |

The same numbered-list shape applies to **Objectives** — see §4.

---

## 4. Objectives compression pattern (numbered list, bold + 1-2 sentence context)

Each objective compresses to a **bold statement + 1-2 sentences of context**, as a numbered list item — NOT an H3 + 2 sub-bullets, NOT a 2-column table row. *(ResOps row name: "Objectives.")*

```
## Objectives

1. **[Bold statement of objective.]** [1-2 sentences of context — why this matters, what's missing today, what decision it unlocks.]
2. **[Bold statement of objective.]** [1-2 sentences of context.]
3. **[Bold statement of objective.]** [1-2 sentences of context.]
```

Rules:

| Rule | Reasoning |
|---|---|
| **Bold = the *what*; plain prose = the *why*.** | Leadership scans the bold statements first to grasp the study's three pillars; only reads the prose if a pillar grabs them. |
| **Statements, not questions.** End in a period, never a question mark. | Per Anderson (2022) — objectives are statements; questions live in the Key Research Questions section. |
| **1-2 sentences of context, never more.** | If you need a paragraph, the objective is too big — split it. |
| **Context names the *decision* the objective unlocks.** | Per Anderson's Mad-Lib test ("I need [info] to make [decision]"). The "what's missing today" framing makes the decision visible. |

**Out of Scope as a separate subsection was REMOVED.** If scope-creep is a real concern, surface it in **Project Details → Dependencies** as a scope/dependency risk (one line with a date or owner). Do not add a standalone "Out of Scope" subsection back — it bloated the Objectives section without adding decision value.

---

## 5. Topic, What-decisions, and Themes — the framing sections (replaces the old Parameters table)

The pre-2026-06-08 template opened with a Goal-led **Parameters table**. The ResOps RPP has no such table; its contents are re-mapped to three dedicated sections plus Project Details:

| Old Parameters row | → ResOps home |
|---|---|
| **Goal** (row 1) | **Topic** — the one-sentence leadership framing at the very top. Lead with the *why* before the *how*. |
| **Primary Decision** | **What decisions will be made with such research?** — its own section after Hypotheses. |
| **Study Type / Method / Sample** | **Project Details** (Method + Approach, Sampling Plan / Participants). |
| **Timeline** | **Proposed Research Timeline** (dated milestones) + the **Research Timeline** phase grid in the header. |
| *(new in ResOps)* | **What Research Priorities is this relevant to (Themes)** — which org/research themes this maps to. |

### Topic

One high-level sentence. Leadership reads this first to decide whether to read further. Replaces the old "Goal" row. Bold the decision-driving phrase inside it.

> **Topic:** Define the **user-grounded threshold for "good enough" recipe-to-cart mapping** — the line between an acceptable cart and a broken one.

### TL;DR Summary of Findings

A placeholder at plan-time: *"To be filled out at the end of the study."* It sits right after Topic in the ResOps template (findings get pasted here at readout).

### What decisions will be made with such research?

Bullet form. Each must be a **real fork** — a different finding leads to a different action. If a "decision" doesn't change anyone's behavior, it isn't one; cut it or sharpen it. This is where the audited Step-1.6 primary decision lands.

- **Calibrate the AIQA framework's severity thresholds** to the user-grounded line.
- **Select among the improved-mapping A/B variants** for rollout.

### What Research Priorities is this relevant to (Themes)

Short bullets naming the themes/priorities this study maps to.

- Good Ingredient Impressions (Meals northstar).
- AI quality evaluation.

**Bolding:** bold the answer-word, never the row/section label. Density ≤ 10% (the old ≤15% Parameters-table allowance is retired — there is no Parameters table).

---

## 6. Background = Problem Statement + Product Context, followed by an Existing Insights H2

The Background section is **two sub-blocks**, each a tight bullet list — never a paragraph. Immediately after it comes a separate `## Existing Insights` H2 surfacing what's already known. *(ResOps places Existing Insights between Background and Objectives — Option B keeps it.)*

```
## Background

### Problem Statement
- **[Lead-word]** — [One-sentence explanation of the gap.]   (3 bullets max)
- **[Lead-word]** — [One-sentence explanation of the gap.]
- **[Lead-word]** — [One-sentence explanation of the gap.]

### Product Context
- [Concise 1-2 sentence bullet]   (3-4 bullets max)
- [Concise 1-2 sentence bullet]
- [Concise 1-2 sentence bullet]

## Existing Insights
*(what we already know — top 3-5, each with a verbatim source link)*

1. **[Insight stated plainly.]** "[Verbatim supporting line from the source.]" — [Source name](URL)
2. **[Insight stated plainly.]** — [Source name](URL)
3. **[Insight stated plainly.]** — [Source name](URL)
```

Rules:

| Block | Format | Anti-pattern |
|---|---|---|
| **Problem Statement** | 3 bullets max. Each = 1-3 word bold lead-word + one-sentence explanation. Render the two sub-labels as `###` H3, not bold paragraphs. | A paragraph. A 5-item list. Generic lead-words like "Issue 1." |
| **Product Context** | 3-4 bullets, 1-2 sentences each. | A wall of context. Backstory unrelated to *this study's* decisions. |
| **Existing Insights** | 3-5 numbered items, each = one plainly-stated insight + clickable source; quote the supporting line **verbatim** where the insight rests on a specific prior finding. | Stating an insight without a source. Padding with generic/assumed "insights." Burying it below the fold. |

**Why Existing Insights sits near the top (after Background, before Objectives):** the team must see *what's already known* before scoping the study, so they don't reinvent the wheel (Prakriti + Amalia, 2026-06-02). It's sourced via the research-insights agent + Glean during Step 1.5. **Prior Research lives here** (the old Appendix → Previous Research subsection folded in). If there's genuinely no prior research: *"No prior user research on [topic] — this is net-new territory."* — never fabricate.

---

## 7. Project Details absorbs Method, Participants, Stimuli, Dependencies, Compensation, Platform, Deliverable Format

There is **no standalone Methodology, Participants, Deliverables, or Risks H2 section.** All of it lives in the single ResOps **Project Details** table. *(ResOps block name: "Project Details.")*

```
## Project Details

| Element | Detail |
|---|---|
| **Method + Approach** | *Minimum evidence to move the decision:* 8 moderated interviews (45 min) + survey N=75–100, 5-pt acceptability scale. Lean alt: survey-only if timeline tightens. |
| **Sampling Plan / Participants** | <ul><li>Ordered from a recipe ≥2× in past 60 days</li><li>Quad-cell by cooking context</li><li>iOS + Android + web; US-based</li><li>[recruit query link]</li></ul> |
| **Stimuli** | 5–6 mocked recipe→cart scenarios at varying mapping quality (Figma). |
| **Dependencies** | Blazer recruit query [link]; stimulus mocks finalized by May 18. *(Surface schedule/recruit RISKS here with a date or owner — ResOps has no separate Risks section.)* |
| **Compensation** | $75 (qual) / $5 (quant). |
| **Research Platform** | Zoom (sessions), Qualtrics (survey), Dovetail (synthesis). |
| **Deliverable Format** | Readout deck (Google Slides) + severity matrix (Sheet). |
```

Rules:

- **Method + Approach leads with "minimum evidence to move the decision."** The leanest valid path first, then a lean alternative if the timeline tightens. Not the most comprehensive study possible (Prakriti, 2026-06-02).
- **No prose rationale paragraphs.** If the method needs defending in detail, save it for the readout. The plan is decision-ready, not academic.
- **Sampling Plan carries behavioral criteria, not demographics.** "Ordered from a recipe ≥2× in past 60 days" — not "Ages 25–55, suburban."
- **Multi-criteria cells use `<ul><li>` bullets** (Sampling, Stimuli, Dependencies) so they read as scannable checklists. Single-criterion cells (Compensation, Platform, Deliverable Format) stay one line.
- **Risks fold into Dependencies.** "Schedule risk" is not a risk; "Prototype not finalized until April 30; fieldwork cannot begin before then" is. Each risk gets a date or owner. An un-owned mitigation is a wish.
- **Deliverables fold into Deliverable Format (the format) + Additional → Documents (the artifact links).** No standalone numbered Deliverables list.

---

## 8. Proposed Research Timeline = dated milestone table (separate from the header phase grid)

Two timeline artifacts, do not conflate them:

| Artifact | Where | What |
|---|---|---|
| **Research Timeline** (phase grid) | Document header | Phase × stage grid with status codes — **PL** Planning, **KO** Kick off, **IP** In progress, **RO** Read Out. |
| **Proposed Research Timeline** (milestones) | Its own H2, late in the plan | Dated milestone list following ResOps. |

```
## Proposed Research Timeline

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
```

Rules:

- **Keep the ResOps milestone names** — they map to the ResOps recruiting/SLA workflow. Don't rename "Submit Participant Recruiting Request" to a generic "Recruit."
- **Honor the 10-business-day recruiting SLA** in the Recruit dates row — flag if the requested timeline violates it.
- 2-column (Milestone | Date). Add an Owner column ONLY if multiple owners are realistic.

---

## 9. Hypotheses / Questions of Interest from XFN leads = standalone H2, AFTER Key Research Questions

Hypotheses are their own H2 section named exactly **"Hypotheses / Questions of Interest from XFN leads"** (the ResOps row name), positioned **after Key Research Questions and before What-decisions**. This matches BOTH the 2026-06-02 workshop (Prakriti: hypotheses "comes after objectives and research questions… then it decides your methodology") AND the ResOps template — **canonical as of 2026-06-08, no longer provisional.**

```
## Key Research Questions
1. ...

## Hypotheses / Questions of Interest from XFN leads
*(expected outcomes / team beliefs to pressure-test per Portigal 2023 — each traces to an Existing Insight)*

- **H1** — [Team belief / expected outcome, one sentence.]
- **H2** — [Team belief / expected outcome, one sentence.]
- **H3** — [Team belief / expected outcome, one sentence.]

## What decisions will be made with such research?
...
```

Rules:

| Rule | Reasoning |
|---|---|
| **Standalone H2, not a Background sub-block.** | Prakriti, 2026-06-02; matches the ResOps row. |
| **Placed between Key Research Questions and What-decisions.** | They are what the methodology is designed to test — the method (Project Details) follows from the beliefs being pressure-tested. |
| **3 bullets, one sentence each, prefixed `**H1**`/`**H2**`/`**H3**`.** | Tight, scannable. |
| **Each hypothesis traces back to an item in Existing Insights.** | Hypotheses are derived from what's already known — not invented. Keeps the Portigal (2023) confirmation-bias guardrail intact. |

---

## 10. Additional → Documents = clickable markdown links, the final section

The plan ends at **Additional → Documents** — no FAQ, no Open Questions, no separate Resources & Links, no Risks section follows it. *(ResOps block name: "Additional," with a "Documents" list.)*

```
## Additional

**Documents**

- **[Discussion Guide](#)** — to be generated via `/moderation-guide` skill
- **[Questionnaire / Survey (Qualtrics)](#)** — to be drafted by May 13–14
- **[Screener](#)** — to be drafted by May 14
- **[Datasheet / recruit query](#)** — pending DS pull
- **[PRD / Brief](#)** — pending Trace
- **[Stimulus mocks (Figma)](#)** — pending stimulus owner decision
- **[Final Report](#)** — created at readout
```

Rules:

| Rule | Reasoning |
|---|---|
| **EVERY item is a clickable markdown link.** Format: `[Document Name](URL)`. | When the doc is uploaded to Google Docs and styled, the items render as blue underlined links — readers click directly to the source. |
| **Use `(#)` as placeholder URL for docs that don't exist yet.** | The link styling shows up immediately; the researcher fills in real URLs as the docs land. Without a URL, markdown renders as plain bold text and loses the visual cue. |
| **Single Documents list — no Previous Research subsection here.** | Prior research moved to **Existing Insights** (§6). Don't sprout new subsections like "Tools" or "Templates" — tools belong in Project Details → Research Platform. |
| **Auto-link every doc surfaced in the kickoff inputs.** | Capture every doc the researcher cited (PRD, Slack thread, Glean doc, Screener, Mod Guide, Dovetail project, PII consent script) and emit each as a link. The researcher shouldn't re-type doc names she already mentioned. |

---

## 11. RACI block — keep all four roles in the document HEADER

RACI lives in the document header — the four disc-bullet lines under **Key Stakeholders**, above the **Topic** section — NOT as a standalone H2 section.

Always include all four RACI roles (Responsible / Accountable / Consulted / Informed), even if some names aren't known yet. Use `[TBD — fill in]` placeholders.

```
**Key Contacts:** Jedida Milton (UX Researcher)

**Key Stakeholders:**
- **Responsible:** Jedida Milton (UX Researcher)
- **Accountable:** Trace Levinson (PM, Meals)
- **Consulted:** Callum Wood (DS, AIQA — *decision-maker*), Eric Hermann (Meals Lead), [TBD — fill in]
- **Informed:** Prakriti Parijat (UXR Skip-level), Heather Matley (Content)
```

Why: forces stakeholder alignment early. An empty `Accountable:` slot is a flag that the decision-owner hasn't been named, which is itself information.

When the *decision-maker* is a Consulted party (not the Accountable), call it out inline with `*decision-maker*` in italics. Example: `Callum Wood (DS, AIQA — *decision-maker*)`.

See also: `~/.claude/projects/.../memory/feedback_raci_placeholder_format.md`.

---

## Source

Locked in during the v2 Recipe→Cart Mapping research plan iteration on **2026-05-12**. Prior version crystallized during the v3 iteration (Doc `1kp8qSIM8sMys2ytwHuBcwQKOhnAJVcENlq8ucik5hxM`).

**Updated 2026-06-02** from the team workshop where Jedida demoed the research skills. Team feedback drove: a new Existing Insights H2 surfacing what's already known (Prakriti + Amalia), a verbatim-source requirement on every insight (Amalia), existing-context discovery running first via the research-insights agent + Glean (Step 1.5), an active decision-quality audit (Step 1.6), minimum-evidence methodology framing (Step 2), and a `/multi-agent-check` draft→critique handoff (Step 6).

**Restructured 2026-06-08** to the canonical ResOps **Research Project Plan (RPP)** template (Doc `1s6Lg4ZsiIypqANdpg4hrCwxkgwP0qOwJvGNekzgj9k0`) under Jedida's **"Option B"** (match ResOps order + names, keep the richer Jun-2 content). Section re-mapping from the old template:
- Goal-led **Parameters table** → split into **Topic** + **What decisions will be made** + **Project Details** + **Proposed Research Timeline** (§5).
- **Methodology** (absorbed Participants) → **Project Details** (§7).
- **Deliverables** → **Project Details → Deliverable Format** + **Additional → Documents** (§7, §10).
- **Risks** → **Project Details → Dependencies** (ResOps has no Risks section) (§7).
- **Appendix → Additional Documents** → **Additional → Documents** (§10); **Appendix → Previous Research** → **Existing Insights** (§6).
- **Research Questions** → **Key Research Questions**; **Research Objectives** → **Objectives**; **Hypotheses** → **Hypotheses / Questions of Interest from XFN leads** (no longer provisional) (§1, §4, §9).
- New ResOps sections added: **TL;DR Summary of Findings**, **What Research Priorities is this relevant to (Themes)** (§5).
- The interactive pop-up (SKILL.md Step 3) now walks these sections in the same order, one at a time, first pop-up = Existing Insights.
