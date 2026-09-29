---
name: mod-guide
description: Use when a UX researcher is about to conduct user interviews, usability tests, or diary study check-ins and needs a moderation guide with warm-up, discussion sections, probing techniques, and closing. Triggers on "write a moderation guide", "interview guide", "discussion guide", "facilitation script", "/mod-guide", or natural asks like "help me write interview questions for this study", "I need a script for my usability test", "prep questions for these sessions", or "build a discussion guide for [study]".
---

# Moderation Guide Builder

Generate a ready-to-facilitate moderation guide for an Instacart UX research session. The skill builds **two structurally distinct guide formats** (chosen first, in Step 2a / Section 1):

- **Prototype / Usability** — task-and-scenario tables tied to prototype screens, think-aloud, observation cues, ease ratings, experimental design, optional vendor (agency) back-matter. Covers usability tests and concept tests. Template: `references/template-prototype-usability.md`.
- **Interview (IDI-style)** — open questions as nested prose probes in timed thematic blocks, no artifact. Covers in-depth interviews, diary check-ins, and focus groups. Template: `references/template-interview.md`.

Both share one spine (stakeholder header, parameter table, pre-session checklist, verbatim consent, post-session debrief) and one delivery pipeline. Grounded in Steve Portigal's *Interviewing Users* (2nd ed.), Indi Young's *Listening Deeply*, Nielsen Norman Group (Rosala, Pernice, Moran, Fessenden), Erika Hall's *Just Enough Research*, Nikki Anderson's *User Research Academy*, Instacart's internal **AIxUXR Playbook** (Loosbrock & Venkatraman, 2025) — the *Discussion Guide Drafter & Critic* spoke — and four finished Instacart discussion guides (IC4B, Caper RR3, Bad Addresses, Checkout Sprint) plus the AI Expert Interviews guide.

### Guiding Philosophy — H.E.A.R.T. (from Instacart's AIxUXR Playbook)

Every guide this skill produces — and every session it supports — must uphold the **H.E.A.R.T.** framework. The moderator is the final authority; this skill is a co-pilot, not the driver.

| Principle | What It Means for a Moderation Guide |
|-----------|--------------------------------------|
| **H — Human-centered** | Prioritize the participant's context, comfort, and dignity. Questions serve their lived experience, not our curiosity. |
| **E — Experience-focused** | Every interaction in the session (consent, warm-up, probes, close) must feel intuitive, respectful, and positive. A clunky moderator moment is bad research. |
| **A — Amplifying** | AI drafts the protocol; the human researcher drives strategy, synthesis, and empathy. The guide is a starting point, not a script cage. |
| **R — Responsible** | Proactive about ethics, PII, consent, and bias mitigation — not a box-check. Scrub PRDs/RPPs of PII before pasting. |
| **T — Transparent** | Disclose AI-assisted drafting to stakeholders. Disclose recording and purpose to participants. Trust is the currency. |

**Source:** AIxUXR Playbook §1.2 "The H.E.A.R.T. of AI in Research" (Instacart internal, Pilot, Sep 30, 2025).

The researcher is the final authority. Recommend clearly, but never silently lock a study parameter, question, probe, or delivery choice. Ground every parameter and question in the supplied inputs; if a fact is not in the inputs, mark it `[TBD — fill in]` rather than inventing it ("grounded in data, never assumed").

---

## Completion contract

A run is complete only when all of the following are true:

0. **The guide format has been chosen** — **Prototype / Usability** or **Interview (IDI-style)** — and the matching template reference has been loaded (`references/template-prototype-usability.md` or `references/template-interview.md`). This is the first Section 1 decision and it forks every downstream step (Section 1 parameters, Section 2 blocks, OUTPUT TEMPLATE). See Step 2a.
1. Study inputs have been read and the study parameters proposed from them.
2. The researcher has approved every applicable **Section 1** parameter (the upfront setup batch) **and** every **Section 2** guide-content block — the block sequence depends on the chosen format (interview: Objectives → Introduction & Rapport → Thematic deep-dive blocks → Wrap-Up → optional Parking Lot; prototype: Objectives → Intro → Background → Task Flows → optional Comparisons/Recap → Wrap-Up → optional vendor back-matter).
3. The self-critique pass and the multi-agent review have both run, with fixes folded in.
4. The Google Drive destination has been confirmed.
5. The guide has gone through the **create → format → verify** pipeline — the **Option 4 — Leadership** visual contract by default (native Google Docs; plain-native or a Jedida variant only when the researcher picks it or as a disclosed fallback).
6. A working Google Doc link has been returned with a one-line pilot reminder and verification status.

Both quality checks run before the final Google Doc is drafted. Drive destination confirmation must happen before document creation.

Markdown is an intermediate representation, not the completed deliverable. A mock or demo stays out of Drive and the tracker unless the tester explicitly requests a test document.

## Flow overview

| Step | Work | Completion gate |
|---|---|---|
| **1** | Gather PRD, brief, kickoff notes, Slack thread, or free-form description → announce the 3-section structure to the researcher | Inputs received; researcher understands the full workflow |
| **2** | Analyze inputs; propose the study-parameters table (read-only context); run the Say-Do Gap risk check | Parameters and risk flag proposed |
| **3** | **Section 1 — Study Setup & Parameters:** the consolidated upfront batch of labeled pop-ups. **First question = guide format (Prototype/Usability vs Interview)**, then the shared rows (moderation, duration, participants, profile, topics/tasks/flows, Say-Do, RACI [multi]) + the **truly format-specific rows from the matching template reference** (prototype: prototype links/backup, device, experimental design, rating style, delivery model; interview: recruit source, blinded?, conditional blocks, horizon framing) + Drive-destination & delivery-variant confirmation folded in last | Format chosen; all applicable parameters approved; destination confirmed; researcher says "Section 1 locked" |
| **4** | **Section 2 — Guide Content:** draft-first approval, one block at a time, using the **block sequence from the matching template reference** (interview: Objectives → Introduction & Rapport → Thematic deep-dive blocks → Wrap-Up → optional Parking Lot; prototype: Objectives → Intro → Background → Task Flows → optional Comparisons/Recap → Wrap-Up → optional vendor back-matter), each locked before the next, transition announced after each lock | All content blocks approved |
| **4.5** | **Section 3 —** auto-run the 5-part self-critique (announced at end of Step 4) as the critique half | Gaps fixed or explicitly accepted |
| **5** | Auto-run the multi-agent review on the fixed content — before the Doc | Review complete; confirmed fixes folded in |
| **6** | Draft the Google Doc last: confirm destination, create the doc, style (**Option 4 — Leadership default** via `option4_guide_layout.py`; plain-native fallback; optional Jedida variant), read back, verify the visual contract, correct, return with pilot reminder | Content, structure, tables, links, location, and Option 4 visual contract pass |

## Portable Google Docs contract

The skill must work for any researcher with a write-capable Google Docs integration.

- **Option 4 — Leadership is the default deliverable look**, applied by the bundled `scripts/option4_guide_layout.py` formatter against `references/option4-guide-style.json` using the session's connected Google Docs / Drive tools only — the same clean, edited leadership design `/research-plan` produces. Plain native Google Docs is a fallback (disclosed) or an explicit researcher pick; a personal Jedida variant applies only when the researcher opts in.
- Do not depend on a personal template, custom font beyond the bundled Option 4 contract, private reference document, hardcoded folder ID, personal styling script, command-line utility (gws/gohan), or researcher-specific authentication setup for a real run to succeed. The Option 4 formatter is bundled with the skill and portable; it is not a personal dependency.
- **Optional "Instacart / Jedida variant":** the personal pipeline (`md2doc`/`upload-gdoc.py`, `apply_jedida_reporting.py`, `apply_canonical_template.py`, `apply_custom_template.py`, CLAUDE.md folder-routing, hardcoded project-folder IDs) is preserved as an *optional* path the researcher can choose in Section 1. It is never the default and is never required.
- Confirm the exact Drive destination before creating any doc. Never write to a hardcoded personal folder without confirmation.
- If no write-capable Docs integration is available, preserve the approved markdown draft and report that the required deliverable is blocked. Do not call the markdown output final.

## Interaction contract

Use native `AskUserQuestion` checklist pop-ups when available.

- Ask one decision per pop-up. (Section 1's upfront setup may still batch up to 4 of these decisions per `AskUserQuestion` call — each decision is still labeled and answered individually within the batch.)
- **Use `multiSelect: true` selectively — on decisions where more than one item legitimately applies:** key topics/tasks, stakeholders/RACI, and any multi-item quote/finding/recommendation/tag/theme decision. **Keep single-select for genuinely exclusive choices:** session duration, study type, moderation style, Say-Do module, stimuli handling, phase/scope, and the delivery/styling variant.
- Number the options. Mark a **Recommended** option based on the inputs and discovered evidence — it is exactly what the Step 2 parameters table already proposed.
- Preserve the built-in **Other / comments** field so researchers can add, correct, or rewrite (including custom durations, participant counts, or a reference-doc URL).
- Show the proposed content before asking for approval.
- **The last option in every pop-up must be "Brainstorm with me"** — this opens a short chat exchange on that specific item, then re-shows the revised draft for approval before advancing. Never bury it mid-list.
- Label every pop-up with its section and step: **"Section 1 > Step 3 of 10: Duration"** / **"Section 2 > Step 2 of 5: Core — Task Flow"**. The researcher must always know exactly where they are.
- No fixed option cap: show all relevant items; if there are many, show the most important first and include an "Other / see more" slot.
- Do not advance until the current item is approved, unless the researcher explicitly requests the whole-draft approval override in Step 4.

If native pop-ups are unavailable, state **"Inline fallback — native checklist unavailable in this environment"** and reproduce the same numbered options, labels, and selection instructions in chat. Do not silently substitute an unlabeled prose question.

---

## Step 1 — Gather Study Inputs & Orient the Researcher

Ask the researcher to paste or share the study inputs. Say:

> "To build your moderation guide, share whatever you have — PRD, project brief, kickoff Slack thread, meeting notes, or a plain-English description. **If it's a usability/prototype test, include the prototype or Figma link.** I'll extract the study parameters, recommend whether this is a prototype/usability guide or an interview guide, and build from there. If you have a Google Doc link, paste it."

**Accept any format:** PRD, brief, Slack thread, Gemini meeting notes, or verbal description. If a Google Doc URL is shared, read it via `google-docs:fetch-google-doc` or Glean (`mcp__glean_default__read_document`) — whichever is available in this environment. If neither tool is connected, ask the researcher to paste the doc's content directly rather than stalling on a missing tool.

### Orientation announcement

Once the inputs are in hand, before asking any parameter questions, say in chat:

> Now that you've shared your inputs, I'll pull out the study parameters, then we'll build this moderation guide together — one step at a time.
>
> **We'll work in three sections:**
>
> **Section 1 — Study Setup & Parameters** *(the decisions that shape the guide)*
> **Guide format (Prototype/Usability or Interview) — first** · Moderation style · Duration · Participants · Profile · Stakeholders (RACI) · then the parameters specific to your chosen format · Drive destination & delivery style
>
> **Section 2 — Guide Content** *(what the moderator will actually read)*
> Built from your format's template — an **interview** guide runs Objectives → Intro & Rapport → Themes → Wrap-Up; a **prototype/usability** guide runs Objectives → Intro → Background → Task Flows → Wrap-Up
>
> **Section 3 — Quality Gate & Delivery** *(check, then produce)*
> Self-critique → multi-agent review → the formatted, verified Google Doc in your confirmed Drive folder
>
> For each step I'll show you what I've drafted — you can accept it, pick what to keep, or brainstorm with me to refine it. We move to the next step only after you approve the current one.
>
> Starting with **Section 1 — Study Setup & Parameters.** Analyzing your inputs now…

This is the one planned questioning phase. There are no *unplanned* pop-ups: every pop-up the researcher sees belongs to one of these three announced sections. (This replaces the old "generate the whole guide silently" stance — see the reframed rule in Step 3.)

---

## Step 2 — Analyze and Propose Structure

Analyze the inputs, then present recommended study parameters as a table. Extract directly from the source material — do not invent details.

### 2a. Guide Format Selector (THE top-level fork — determines the whole template)

**The skill produces two kinds of moderation guide, and they are structurally different documents.** Every downstream step (Section 1 parameters, Section 2 blocks, OUTPUT TEMPLATE, verification) branches on this choice. Pick the format **first**, load its template reference, and build from it:

| Format | Load this reference | Body shape | Anchored to | Use when |
|--------|--------------------|-----------|-------------|----------|
| **Prototype / Usability** | `references/template-prototype-usability.md` | Task **tables** (`Task \| Scenario \| Directives/Probes \| Observation Cues`) tied to prototype screens | An artifact — Figma/live product/screens | The participant **does a task** with a design under test |
| **Interview (IDI-style)** | `references/template-interview.md` | Open questions as **nested prose bullets** in timed thematic blocks — no body tables | Nothing — the conversation *is* the session | The participant **talks** — recounts experience, opinion, mental model |

**How the choice is made:** always **ask the researcher explicitly** (this is the first Section 1 question — see Step 3). Do *not* silently auto-select. You may still *recommend* a format from the input signals below, but the researcher confirms it.

**Decision signals (to set the Recommended option):**
- → **Prototype/Usability** when inputs include a prototype/Figma link, mockups, screens, or an on-device/on-cart stimulus; or words like *usability, task, flow, walkthrough, click, can they complete X, where do they get stuck*; or a design under evaluation (especially multiple variants); or counterbalancing is a concern.
- → **Interview** when there is **no artifact** — just topics/themes to discuss; or goals phrased as *understand why / how they feel / their experience / their mental model / their vision*; or participants recruited to talk about a domain (e.g. external experts via GLG); or future/landscape/opinion studies.
- **Tie-breaker:** a testable artifact **AND** a "can they do X" question → Prototype. Purely "learn what they think and why," no artifact → Interview. A short warm-up interview *inside* a prototype session does **not** make it an interview guide — tasks + a stimulus make the whole thing a prototype guide.

**Where the old 5 study types land:** *Usability Test* and *Concept Test* (stimulus/task-driven) → **Prototype/Usability**. *In-Depth Interview (IDI)*, *Diary Study Check-in*, and *Focus Group* (conversation-driven) → **Interview**. Sub-shape nuances (diary entry-review, focus-group turn-taking, concept-test 5-second rule) live in `references/mod-guide-methodology.md` §3.

**Time split (applied to the confirmed duration):**

| Format / study type | Time Split |
|---------------------|-----------|
| Prototype — Usability Test | 5% intro / 5% background / 75% tasks / 15% wrap (four buckets — the prototype parameter table wants intro/background/tasks/wrap separately) |
| Prototype — Concept Test | 5% intro / 10% background / 70% tasks / 15% wrap |
| Interview — IDI | 10% intro+warm-up / 80% core (themes) / 10% wrap |
| Interview — Diary check-in | 15% / 70% / 15% |
| Interview — Focus Group | 15% / 70% / 15% |

Rationale: time splits follow NN/g's qualitative usability testing study guide and Rosala's interview-guide conventions.

### 2b. Skip the recommendation table — go straight to Section 1 pop-ups

**Do NOT show a "Based on your inputs, here's what I recommend" summary table.** After analyzing the inputs internally, go straight into the Section 1 `AskUserQuestion` pop-ups (Step 3). The extracted parameters inform the Recommended options in each pop-up — they do not need to be shown as a standalone table first.

**Hand-off to Section 1 (Step 3):** immediately after Step 2a/2c analysis, launch the first Section 1 `AskUserQuestion` batch in the same turn. No intermediate table, no interim summary in chat.

### 2c. Say-Do Gap Risk Check

Flag **High** if the study asks *only or mostly* about stated behavior, preferences, or intent rather than observable action — e.g., "how often do you cook at home?", "would you pay for this?", "do you read ingredient labels?" (see references/mod-guide-methodology.md §2a for the full signal list). Flag **Low** if the study is a usability test or otherwise observes actual behavior with a planned follow-up (§2a). Flag **Medium** for everything in between — e.g. a study that's mostly observational (usability, contextual inquiry) but includes a handful of stated-preference or frequency questions alongside the core task-based content.

**Effect on the generated guide:** both **Medium and High** automatically include the **Say-Do Gap Module** (the §2b probes and §2c social-desirability counter-moves) — Medium studies just need it applied more selectively, to the specific stated-preference questions rather than throughout. Only **Low** skips the module entirely. This also sets the Recommended default for Row 8 (Say-Do Gap module) in Step 3: Medium/High → Recommended = Include; Low → Recommended = Skip.

Source: NN/g "Why User Interviews Fail" — *"Interviews do not produce reliable data about user behavior."* Indi Young's listening sessions also warn: people reconstruct rather than report.

---

## Step 3 — Section 1: Study Setup & Parameters (CONSOLIDATE ALL PARAMETERS UPFRONT)

Section 1 is the consolidated upfront batch: every study parameter is decided here, in one place, before any guide content is drafted. Keep this consolidate-decisions-upfront design — it is what makes the rest of the flow predictable.

### 🚫 ZERO *UNPLANNED* QUESTIONS RULE (read this first)

The old version of this skill forbade **all** questions after the parameter batch and generated the whole guide silently. That is no longer the design. The design now is **step-by-step everywhere**: Section 2 walks the guide content in draft → approve → lock pop-ups, and Section 3 announces the quality gate. Those pop-ups are **planned, pre-announced phases** the researcher was told about in the Step 1 orientation — they are not mid-flow surprises.

So the rule is: **zero *unplanned* questions.** That means:

- Every pop-up must belong to one of the three announced sections (Section 1 parameters, Section 2 content approval, or the Section 3 gate). Do not invent an unannounced clarifying question.
- If you discover a missing piece of information that is *not* one of the planned decisions, **resolve it with a sensible default** based on the inputs and the approved parameters — don't spawn a surprise pop-up. If the default turns out wrong, the researcher will correct it when they see that block's draft.
- Section 3 (self-critique, multi-agent review, upload + style) still runs with **no** further researcher pop-ups — it is deterministic. Status updates are welcome; questions are not.
- Re-asking the *same* decision, or asking something the researcher already answered, is the failure mode this skill prevents. Consolidate parameters here; walk content in Section 2; then execute Section 3 silently.

**The researcher's interaction moments are:** (1) Step 1 — paste inputs, (2) Section 1 — answer the parameter batch, and (3) Section 2 — approve each content block. After Section 2 closes, the next thing they see is the finished, verified Google Doc.

---

**Hard rule:** Ask the researcher about **every key moderation-guide parameter** through `AskUserQuestion` *before* drafting guide content in Section 2 — even the ones that look "obvious" from the inputs. The point is to give the researcher a chance to **confirm or override** every meaningful design choice in one place. They should walk away from Section 1 feeling like they directed the guide, not received it.

**Guarantees the researcher gets in every popup:**
1. **A Recommended option** — Claude's pick (extracted from the inputs or chosen by best practice) appears first, marked `(Recommended)`. It matches exactly what the Step 2 parameters table proposed.
2. **2–3 alternatives** — real, plausible alternatives so the choice is meaningful, not rubber-stamped.
3. **An editable "Other" field** — `AskUserQuestion` always offers an "Other" free-text input; the researcher can type any custom value (e.g. a custom duration like "75 min", a custom participant count like "N=18", a custom profile, or a reference-doc URL).
4. **"Brainstorm with me" as the last option** — every pop-up ends with this; it opens a short chat exchange on that specific parameter, then re-shows the revised choice for approval before advancing.
5. **A section/step label** — every pop-up is labeled **"Section 1 > Step N of M: <name>"**, where M is the number of applicable parameter questions actually being asked (conditional rows that are skipped don't count).

**The very last item in Section 1 — across all batches — must always be the Drive-destination & delivery-variant confirmation** (see "The mandatory delivery question" below), so the destination is confirmed before any doc is created. The only exception: **demo/sample/test runs**, where the delivery question is skipped entirely, no Drive artifact is created, and styling auto-resolves per the demo rule (see "Demo-run auto-trigger" below).

### Mandatory question set (ask ALL of these — even if extracted from inputs)

The **Select** column says whether the pop-up is `multiSelect: true` (more than one item legitimately applies) or single-select (a genuinely exclusive choice). Every pop-up's last option is **"Brainstorm with me"** and every pop-up is labeled **"Section 1 > Step N of M: <name>"**.

| # | Question | Select | Recommended (Claude's pick) | Alternatives |
|---|----------|--------|------------------------------|--------------|
| **0** | **Guide format** — Prototype/Usability vs Interview (**ALWAYS FIRST, always asked**) | single | The format the Step 2a signals point to (prototype if there's an artifact/task; interview if it's talk-only) | The other format · "Brainstorm with me" — on picking, **load the matching template reference** and pull its format-specific rows into Row 10 below |
| 1 | **Phase/scope** — which phase or sub-study to build (only if multi-phase plan) | single | The earliest unbuilt phase | Other phases · Both phases |
| 2 | **Study sub-type** (within the chosen format) | single | Interview → IDI / Diary / Focus; Prototype → Usability / Concept — best fit from inputs | The next-best sub-types (skip when only one plausibly fits) |
| 3 | **Moderation style** | single | Moderated remote / Moderated in-person / Unmoderated | The two not picked |
| 4 | **Duration** (session length — exclusive) | single | Extracted minutes or 60 min default | 30 / 45 / 60 / 90 (drop the recommended one from this list) |
| 5 | **Number of participants** | single | Extracted N or method-appropriate default (IDI N≈12, usability N≈5–8, concept/focus N≈8–12) | Smaller / larger options |
| 6 | **Participant profile** | single | Extracted screen criterion | Looser / tighter alternatives |
| 7 | **Key topics / tasks / flows** | **multi** | The 3–6 extracted topics (interview) or task flows (prototype), all pre-selected | "Add another" · individual items selectable so the researcher can drop any |
| 8 | **Say-Do Gap module** | single | Include / Skip / Let Claude decide — Recommended depends on Step 2c risk flag (usually **Include** for interviews on stated behavior; usually **Skip** for prototype tests, which observe behavior) | The other two |
| 9 | **Stakeholders (RACI)** | **multi** | Researcher = Responsible; decision-owner/PM = Accountable; PM, EM, design lead = Consulted; skip-level and partners = Informed — extracted names where known, `[TBD — fill in]` elsewhere | "Edit names" · "Use TBD placeholders for all" — each named stakeholder is an individually selectable line |
| 10 | **Format-specific rows** — pull from the loaded template reference (Row 7 above already captured the topics/tasks/flows; Row 8 the Say-Do module — don't re-ask them here) | varies | **Prototype** (`template-prototype-usability.md`, the truly-specific rows P1–P4, P6–P8): delivery model (internal/vendor) · prototype link(s) · backup · device · experimental design · rating style · feedback-then-task. **Interview** (`template-interview.md`, the truly-specific rows I1, I2, I4, I6): recruit source · blinded? · conditional blocks · horizon framing | Each row's own alternatives, per the reference |
| **LAST** | **Drive destination & delivery style** (portable-first) | single | See "The mandatory delivery question" below | See below |

**Stakeholder identity verification (Row 9):** Before carrying any name into the RACI block, verify it is still current using the people/directory search tool (e.g. `mcp__glean_default__employee_search` or the connected directory search). Stored context and project files go stale — a named team member may have left or changed roles. If there is any doubt about who belongs in a role, ask the researcher directly *inside the RACI pop-up's "Other" field prompt or as part of this same Section 1 question* (e.g. "I see [Name] listed as [Role] — is that still accurate?"). Never carry a name forward from memory or a stale file without a live check. *(Current-session caveat: the people/Glean MCPs may require auth; if the directory search is unavailable, say so, keep the name only if the researcher confirms it live, and otherwise use `[TBD — fill in]`.)*

**Row 0 (Guide format) is NEVER skipped — it is always the first question.** Rows that may be skipped, and only under these exact conditions:
- **Row 1 (Phase/scope)** — skip only when the inputs describe a single-phase study with no sub-studies.
- **Terminology note (Row 1):** "Phase" here means a study *sub-phase* — e.g. a diagnostic wave followed by a validation wave within this one study — not the RPP's "Phase 1–5" process-stage grid (Plan/Recruit/Fieldwork/Synthesis/Readout) in the Research Timeline header. Same word, different meaning — don't conflate the two.
- **Row 2 (Study sub-type)** — skip only when exactly one sub-type plausibly fits the chosen format (e.g. inputs unambiguously describe a standard IDI).
- **Row 8 (Say-Do module)** — for a prototype/usability guide this is usually Skip (the session observes behavior); ask it only when the prototype study also collects meaningful stated-preference data.
- **Row 10 (Format-specific rows)** — governed by the loaded template reference; ask every applicable row it defines, and skip only the ones the reference itself marks optional (e.g. prototype "backup stimulus" when there is no backup; interview "horizon framing" for non-future studies).

**Never fabricate a stakeholder name.** If a name isn't in the inputs, use `[TBD — fill in]` rather than guessing — this mirrors the `/research-plan` skill's RACI convention and Jedida's "grounded in data, never assumed" rule.

(The **LAST row — Drive destination & delivery style** — is also skipped on demo/sample/test runs, which create no Drive artifact and auto-resolve styling per the demo rule. See "Demo-run auto-trigger" below. On real runs it is always asked, so the destination is confirmed before any doc is created.)

**Every other row must be asked**, even if the answer seems obvious from the inputs. The researcher confirming an extracted value is the whole point. Never skip a row just because you think you know the answer.

### Multi-cohort studies (comparison-cohort branching)

When the research plan specifies more than one cohort (e.g. an "abandoner" cohort vs. a "non-abandoner" comparison cohort — the same contrastive-design pattern the upstream `/research-plan` skill supports), don't leave per-cohort differences to be improvised inline. Label any question-set row above, and any Ask-table row in Section 2 (Step 4), that diverges per cohort with an explicit `(Cohort A) / (Cohort B)` suffix (or however many cohorts exist) — e.g. "Q5 (Cohort A)" / "Q5 (Cohort B)".

**For a prototype/usability guide the cohorts often see *different stimuli or task flows*, not just differently-worded questions** — a between-subjects design (Section 1 Row P6). In that case the `(Cohort A)/(Cohort B)` label goes on the **flow/stimulus assignment** itself (which prototype variant or flow each cohort runs), and the cohort labels must be the same structure as the P6 experimental design and its counterbalance grid — one coherent scheme, not two unrelated mechanisms. State the per-cohort stimulus/flow assignment once, up top, alongside the experimental-design note.

### Batching rules

`AskUserQuestion` accepts up to 4 questions per call. Count the total number of rows you're actually asking (skipped rows don't count) — this is M, the denominator in every "Section 1 > Step N of M" label. Group them into the fewest batches of ≤4 each — that's `⌈N / 4⌉` batches for N questions. Fill every batch before the last to exactly 4; the final batch holds whatever remains (1–4 questions) with **the Drive destination & delivery question as its last item**. For example: 6 questions → batches of 4 + 2 (delivery is the 2nd item of batch 2); 9 questions → batches of 4 + 4 + 1 (delivery alone in batch 3).

Never split the delivery question across batches. Never put it anywhere but the very last position of the very last batch — the destination must be confirmed before Section 2 drafting begins.

### How to phrase each question

For every question, structure the popup like this:

- **Question text** — short, plain English, ends with a "?". Example: "How long should the session be?"
- **Header chip** — ≤ 12 chars (`Duration`, `Participants`, `Study type`).
- **Option 1** — `(Recommended)` label suffix, with the Claude-picked value plus a brief description of *why* it was picked.
- **Options 2–3** — real alternatives with descriptions explaining the tradeoff.
- **Option 4 (sometimes)** — a fourth alternative if useful, but keep it tight.
- "Other" is auto-added — never include it manually. The researcher uses it to type custom values.

### 🎬 Demo-run auto-trigger (skip the delivery question entirely)

**If this is a demo / sample / test run, do NOT ask the Drive-destination & delivery question at all.** Auto-resolve to the native Google Docs default, create **no** Drive artifact, and proceed. The researcher never sees the delivery popup or its "Other" field on a demo run.

**A run counts as a demo when** the invocation contains a clear demo/sample/test signal — e.g. "demo", "sample run", "test this skill", "show me how this works", "just demoing", "dry run", or an equivalent phrase indicating it's a walkthrough rather than a real study deliverable. (This is the same signal class as `feedback_sample_runs.md`, which also means: do NOT save the output to project folders, the tracker, or Drive.)

**Effect on Section 1 batching:** drop the delivery row entirely. The delivery question is normally the very last question across all batches — on a demo run it simply isn't asked, so the last *real* parameter question becomes the final question, and M shrinks by one. All other parameter rows are still asked as normal (the demo still exercises the full questioning flow — only delivery is auto-resolved). Hold delivery = native Google Docs default (no Drive write) for Step 6.

**Real (non-demo) runs:** ask the delivery question normally, per below.

### The mandatory delivery question (always the last one asked — UNLESS this is a demo run, see above)

This single Section 1 pop-up confirms **both** the Drive destination and the styling variant, so the destination is locked before any doc is created (portable Google Docs contract). Phrase it, e.g.:

> "Where should the final guide live, and how should it be styled? (Confirm the Drive folder, or paste a reference-doc URL below to match its style.)"

**Destination:** infer the exact Drive folder from the supplied project context when possible and state it plainly in the question (e.g. "I'll create it in [folder/link] — right destination?"). If no destination is known, the researcher supplies it here. Write only to the confirmed folder; never write to a hardcoded personal folder ID.

**Delivery / styling variant** — single-select (this is the "report audience variant" style of exclusive choice). **Option 4 — Leadership is the default and Recommended path** (portable-first): the same clean, edited leadership look `/research-plan` produces, applied by the bundled formatter with no personal scripts or auth. The personal pipelines are optional, clearly-labeled Instacart / Jedida variants:

- **"Option 4 — Leadership (portable default)" (Recommended)** — The clean leadership design: DM Serif Display / DM Sans typography, dark-green section bands on the phase/theme headings, pale-yellow mock-warning treatment, landscape letter, fixed table styling. Applied by the bundled `scripts/option4_guide_layout.py` against `references/option4-guide-style.json` — native Google Docs only, portable for any researcher with a write-capable Docs integration. This is the default whenever the researcher expresses no preference.
- **"Plain native Google Docs"** — Standard Google Docs native Title/Heading/body styles and native tables, no Option 4 styling. The minimal fallback if the researcher wants an unstyled doc; not the default.
- **"Instacart / Jedida variant — Jedida Reporting (navy/blue)"** *(optional personal pipeline)* — Jedida Reporting palette (navy NAV H1 nav bars, LBLUE label columns, alternating WHITE/LGRAY rows, DGRAY borders, Calibri typography). Styler: `~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py`. Requires Jedida's local scripts/auth.
- **"Instacart / Jedida variant — forest-green mod-guide style"** *(optional personal pipeline)* — Original mod-guide template (DM Serif Display headings, DM Sans body, dark-green table headers, dark-green bold label columns). See `references/canonical-template-spec.md`. Source: `https://docs.google.com/document/d/18Q9V4th9BwwNtlLXSncmMpiN591XTV1RzCUAyxym7wI/edit`
- **"Brainstorm with me"** — last option, as on every pop-up.

**To match a custom reference doc instead** (also an optional Jedida-variant path), the researcher types the Google Doc URL directly into the auto-added "Other" field. Mention this in the question text so the researcher knows "Other" is live for this purpose.

If the "Other" field comes back with a parseable Google Doc URL, treat it as: delivery = Custom Reference variant, ref_doc_id = parsed-from-URL. If "Other" comes back with something that is NOT a parseable Google Doc URL (a typo, or unrelated free-text feedback), fall back to the Recommended native default rather than blocking — don't re-prompt to clarify; flag the ambiguity to the researcher after the doc is delivered instead.

> **Note on the 2026-09-08 global default:** Jedida's CLAUDE.md makes "Jedi's Template" the automatic default styling for *every* new Google Doc in her personal environment. This delivery question is a deliberate, mod-guide-specific, portable exception: for any researcher, the portable **Option 4 — Leadership** look is the default (applied by the bundled formatter, no personal environment needed); Jedida's personal templates (Jedida Reporting / forest-green / custom-match / Jedi's Template) are opt-in variants. Don't silently apply a personal template to a shared run; that would break portability and remove the researcher's choice this step exists to preserve.

### Holding the delivery answer for Step 6

- **Option 4 — Leadership (portable default)** → after creating the doc, run the bundled `scripts/option4_guide_layout.py` pipeline (see Step 6). This is the path for every researcher who does not opt into a personal variant — it produces the clean, edited leadership look with native Google Docs only.
- **Plain native Google Docs (fallback)** → apply native Title/heading/body styles and native tables only, no Option 4 styling. Use only if the researcher explicitly picks it, or as the disclosed fallback when the Option 4 formatter/verifier cannot run in the environment (see Step 6's completion gate).
- **Optional — Jedida Reporting (navy/blue)** → after upload, run `uv run --python 3.12 --with google-api-python-client --with google-auth --with google-auth-oauthlib --with google-auth-httplib2 --with requests --with python-dotenv python ~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py <DOC_ID>`. Requires Jedida's local environment.
- **Optional — forest-green mod-guide style** → after upload, run `scripts/apply_canonical_template.py <DOC_ID>`. Requires Jedida's local environment.
- **Optional — Custom Reference (URL came back via "Other")** → after upload, run `scripts/apply_custom_template.py <TARGET_DOC_ID> <REF_DOC_ID>`. **Apply silently — no read-back confirmation, no "apply these to your mod guide?" prompt.** If the styling looks wrong on the final doc, the researcher will say so post-delivery; that's a one-off correction, not a reason to spawn an unplanned question.

---

## Step 4 — Section 2: Guide Content (DRAFT-FIRST, ONE BLOCK AT A TIME)

With Section 1 locked, build the guide **content** collaboratively, one block at a time. Announce the section transition: *"Section 1 is locked — all parameters set and the destination confirmed. Now we'll build the guide content together, one block at a time. I'll show you each block's draft; you accept it, pick what to keep, or brainstorm with me, and we lock it before moving on."*

### Draft-first block-by-block approval

Show the proposed block content first, then ask the researcher to accept, brainstorm, or edit it. Maintain a visible approved/pending checklist of the content blocks. Re-show revised content after brainstorming and obtain approval before advancing.

Every content pop-up must be labeled with its section and step (e.g. **"Section 2 > Step 3 of 6: Core — Task Flow"**). Announce each transition in chat after a block is locked (e.g. *"Warm-Up locked. Moving on to Core — Motivations."*).

**Select behavior in Section 2:** the questions/quotes/probes *within* a block are a multi-item set — when a pop-up asks the researcher which drafted questions to keep for a block, use `multiSelect: true` (each question is individually selectable). Use single-select only for a genuinely exclusive choice within a block (e.g. "accept this whole block as drafted / revise it / brainstorm"). "Brainstorm with me" is always the last option.

**The blocks, in order — use the sequence from the loaded template reference (M = the number of blocks this study actually has):**

**If the format is Interview** (`references/template-interview.md`):
1. **Objectives** — plain goal bullets (no hypotheses / P0 labels). **No pop-up — auto-generated from inputs, shown for confirmation only.**
2. **Introduction & Rapport** — verbatim 3-bullet welcome (recording/privacy · session overview · logistics). Auto-generated from template. **No pop-up, no approval gate.**
3. **Background Questions** — topic-adjacent icebreaker questions. Auto-generated from template (use grocery/in-store standard block for store-based studies). **No pop-up, no approval gate.**
4. **Thematic deep-dive blocks** — **one block per theme** from the approved Row-7 list; open questions as nested prose probes; conditional themes flagged "if applicable." **Pop-up for each block.** **When the Say-Do Gap module is Included (Row 8), each affected block's draft carries the visible `**Say-Do Gap Probe:**` prose line** — this is what makes Include vs. Skip visibly different.
5. **Wrap-Up** + optional **Parking Lot** — standard close. **No pop-up, no approval gate.**

**If the format is Prototype/Usability** (`references/template-prototype-usability.md`):
1. **Objectives & Research Questions** — hypotheses + P0/P1 labels, kept separate from the script. **No pop-up — auto-generated.**
2. **Session Flow** — simple phase list (Background & Warm-Up → Phase 1 → Phase 2 → Phase 3 → Wrap-Up). No minute-by-minute breakdown, no counterbalance grid here. **Auto-generated.**
3. **Background & Warm-Up** *(no pop-up, no approval gate)* — simple numbered questions (Q1, Q2, Q3), no table format, no "Probes to use:" header. Observation cues at the end. Auto-generated from template.
4. **Phases (the core)** — **one block per phase / stimulus** from the approved Row-7 list. Named Phase 1, Phase 2, Phase 3 — simple, consistent naming. Each: stimulus link, question prompts as a table (Cue | Ask/Do), observation cues in prose below. **Pop-up for each phase.**
5. **Wrap-Up** *(no pop-up, no approval gate)* — standard 3-question numbered close. Auto-generated.
6. **Communication & Deliverables (+ Timeline)** — vendor-run only.

The **shared scaffolding** — header (Moderation Guide title + study title), ownership block (RACI), parameter table, Pre-Session Checklist, and Post-Session Debrief — is standardized on **both** formats and assembled automatically around the approved blocks. The Consent + Recording script is **not included** in the guide — sessions start directly with Background & Warm-Up. Show the scaffolding alongside the first content block so the researcher sees the whole shape.

**Whole-draft override:** if the researcher explicitly asks for the full guide at once instead of block-by-block, skip the per-block pop-ups but still show the complete assembled draft for a single approval, keep the confirmed destination, and perform every Section 3 and verification step. Default to block-by-block unless they ask.

### Quality-gate announcement (say this after the last content block is locked)

Once all content blocks are approved, **ask the researcher** whether they want to run the two quality checks before the final doc. Use `AskUserQuestion`:

> "All blocks are approved! Before I create the Google Doc, I can run two optional quality checks:
> 1. **Critique pass** — I self-audit for methodology gaps, biased phrasing, and weak probes.
> 2. **Multi-agent review** — independent reviewers check in parallel.
> 
> Would you like to run these before the final guide?"

Options: "Yes — run both checks first" (Recommended) · "Skip — go straight to the Google Doc" · "Brainstorm with me"

**Only run the checks if the researcher says yes.** If they say skip, proceed directly to Step 6 (create the Google Doc). Never auto-run the checks without asking.

The moderation guide (the final Google Doc) is drafted **last**. Expected sequence when checks are included: **approved blocks → self-critique → multi-agent → fixes → create Google Doc → share.** When checks are skipped: **approved blocks → create Google Doc → share.**

### Assembly

Apply the researcher's approved parameters and blocks. **Both OUTPUT TEMPLATES live in their references** (interview → `references/template-interview.md`, prototype/usability → `references/template-prototype-usability.md`); only the **shared scaffolding** is rendered inline below. Load the matching reference and follow its skeleton, table shapes, and generation rules; wrap it in the shared scaffolding. Both share the "tables hold only read-aloud/do lines" principle and the same delivery pipeline. Assemble the approved blocks into the markdown intermediate; the final formatted deliverable is the Google Doc created in Step 6.

**Test/demo/mock-run output:** add the shared `⚠️ TEST ARTIFACT` header line — see `../../references/output-status-and-labeling-conventions.md`. Treat any invocation described as a test, sample, demo, mock, fixture, or pressure scenario as simulated even when the brief sounds realistic; omit the label only when the researcher confirms it is a real study. Keep it prominent, and do not save a demo/mock to Drive, the tracker, or project folders.

**Verbatim-sourcing discipline:** every question, name, and detail in the guide traces to the inputs or the researcher's Section 1/Section 2 answers. Quote source material verbatim where the guide reproduces it (e.g. the participant's own phrasing in a `[recall their phrasing]` placeholder, or a capture-verbatim flag). Do not invent stakeholder names, quotes, or details — mark unknowns `[TBD — fill in]`.

### Shared scaffolding (both formats)

Both guide types wrap the **same spine** — parameter table, Pre-Session Checklist, Consent script, Post-Session Debrief. Assemble it around the format-specific body (interview blocks or prototype task flows). The Consent script is read verbatim (confirm, don't re-draft); a **prototype** guide inserts three extra cues into it — "no right answers," think-aloud ("put your brain on speakerphone"), and the prototype-limitations caveat — per `references/template-prototype-usability.md`.

**The document header is always "Moderation Guide."** Both formats use `# Moderation Guide` as the document title, followed by `## [Study Title]` and `*[Month Year]*`. Do not use "UX Research | Research Plan | Q3/Q4 2026" or any breadcrumb format — the doc type is always "Moderation Guide." The ownership block is standardized as full RACI on both.

> **Core principle (codified 2026-05-04 from Diet Personalization mod guide):** the moderator's eye should land on **only the words to read, ask, or do aloud**. Probes, watch-fors, observation cues, "don'ts," and methodology rationale all live in **prose around** those lines, never mixed in. Interview length target **~4–5 pages**; prototype guides run **~6–8 pages** (task lists + screens).
>
> **Prototype format update (Jedida, 2026-09-24):** in a **prototype/usability** guide the read-aloud Introduction and every phase/task, comparison, and recap block are **bold-label lists** (`- **Label:** "line"`), NOT Cue tables. The **only** two tables a prototype guide keeps are the top **Parameter dashboard** and the **Session Flow** agenda. (Interview guides are unchanged — they already use prose bullets, with a Cue table only for consent.) See `references/template-prototype-usability.md`.

```
# Moderation Guide

## [Study Title — derived from research goal]

*[Month Year]*

- **Responsible:** [Name] (Role) — `[TBD — fill in]` if not confirmed in Section 1
- **Accountable:** [Name] (Role) — `[TBD — fill in]`
- **Consulted:** [Names with roles] — `[TBD — fill in]`
- **Informed:** [Names with roles] — `[TBD — fill in]`

[Prototype only — a Links row: **Links:** [Google Folder] · [Figma/Prototype] · [Participant Grid] · [Screener]]

| Parameter | Detail |
|-----------|--------|
| **Study Type & Format** | [Combined — e.g. "Moderated usability test — in-person" or "Moderated cognitive interview — remote via Zoom"] |
| **Duration** | [X] minutes |
| **Participants** | N=[N] — [screening criterion] |
| [Prototype only] **Stimulus** | [Link to stimulus — Phase A: [link] · Phase B: [link]] |
| **Goal** | [1-sentence research goal] |

---

## Pre-Session Checklist

[Bullet list with ☐ checkboxes — NOT a table:]
- ☐ Participant validated — [screening criterion confirmed]
- ☐ [Prototype loaded & tested; backup ready — prototype only]
- ☐ Device — [participant on their own device / remote-control handoff]
- ☐ Recording armed · consent script ready · observers cameras-off [· Slack channel open — vendor prototype]

---

## Consent + Recording Script — READ VERBATIM (~60 sec interview / ~90 sec prototype)

[2-col table. Col 1 = short cue label. Col 2 = exact words to read aloud — no annotations inside the table. A PROTOTYPE guide inserts "No right answers", "Think-aloud", and "Prototype caveat" cues here per its reference.]

| Cue | Read aloud |
|-----|------------|
| **Open** | "Hi [name], thanks for joining. I'm [moderator], a researcher [at Instacart — or, for a vendor-run study, the independent-researcher framing: "I don't work for Instacart and didn't design what you'll see"]." |
| **Purpose** | "I'm here to learn from your experience — no right or wrong answers, nothing being judged." |
| **What we'll do** | "[Concrete description of what's about to happen.]" |
| **Recording** | "With your permission, I'd like to record audio, video, and screen. It stays internal at Instacart. **Is that okay?**" |
| **Confidentiality** | "Your name and any identifying details will be removed before anything is shared internally." |
| **Control** | "About [X] minutes. You can skip any question or end at any time — and you'll still get the incentive." |
| **Open floor** | "Any questions before we start?" |

> Wait for explicit verbal **"yes"** before pressing record.

---

## [FORMAT-SPECIFIC BODY — build from the matching reference; see below]

---

## Post-Session Debrief

[Numbered list, NOT a table. Within 5 min of session end:]
1. **[Primary field — interview: top themes / prototype: per-flow task outcomes]:** ☐ [A] · ☐ [B] · ☐ [C] · ☐ Mixed
2. **[Secondary field — interview: most surprising / prototype: top friction point]:** ☐ … — plus a one-line rationale
3. **Most diagnostic verbatim quote:** one sentence, exact words from the participant
```

### OUTPUT TEMPLATE — the format-specific body

The body that sits **between the Consent script and the Post-Session Debrief** is format-specific — build it from the matching reference, following its skeleton, table shapes, and generation rules exactly:

- **Interview** → `references/template-interview.md`: **Objectives** (plain goals — no hypotheses/P0) → **Introduction & Rapport** (+ screen-out script) → **Thematic deep-dive blocks** (open questions as nested prose probes; conditional "if applicable" blocks) → **Wrap-Up** → **Participants Log** → optional **Parking Lot**. When the Say-Do Gap module is Included, each affected theme block's draft carries a visible `**Say-Do Gap Probe:**` prose line (see that reference's Say-Do rule).
- **Prototype/Usability** → `references/template-prototype-usability.md`: **Objectives** (hypotheses + P0) → **Test Stimuli & Session Flow Overview** → **Introduction** (read-aloud **bold-label list** — think-aloud + prototype caveat + consent) → **Background/Warm-Up** → **Task Flows** (each phase a **bold-label list**, not a table — with an observation-cue prose line below + reused ease rating) → optional **Comparisons/Recap** (lists) → **Wrap-Up** → **Communication & Deliverables (+ Timeline)** for vendor-run. Only the Parameter dashboard and Session Flow agenda are tables.

The shared scaffolding above wraps this body identically for both formats.

**IMPORTANT:**
- The guide MUST end at its last content section, which depends on format: the **(optional) Parking Lot, else the Participants Log**, for an **INTERVIEW** guide; the **Post-Session Debrief** for an **INTERNAL prototype** guide; or **Communication & Deliverables (+ Timeline)** for a **VENDOR-RUN prototype** guide. (The Post-Session Debrief is a shared element that sits near the end but is *not* the last section for interviews or vendor prototypes.) Do NOT add Master Probe Bank, Bias Mitigation Checklist, Self-Critique Audit, or a pilot reminder inside the guide document itself. Those live in `references/mod-guide-methodology.md` for the moderator to consult separately, or — for the pilot reminder specifically — get delivered as one line in the Step 6 chat summary alongside the doc link (see Step 4.5 Part 4 "Pilot reminder" and Step 6.3 item 1). Never inside the guide's own pages.
- **Tables contain ONLY questions / read-aloud / do lines.** Probes, watch-fors, observation cues, tagging guidance, "don'ts," and methodology rationale ALWAYS live in prose above or below the table — never inside cells. (Prototype guides: phase/task content is a bold-label list — observation cues go in a prose line *below* the list.)

---

### FORMATTING RULES (visual + structural)

#### Structural
- **Tables = questions only.** Col 1 = short label (`Q1`, `Q2`, `Setup`, `Open`, `Cue`). Col 2 = the exact words the moderator reads or asks aloud.
- **Probes, watch-fors, "don'ts," tagging guidance, methodology rationale → prose ABOVE the table.** One sentence per concept where possible.
- **Use `>` blockquotes** for one-line moderator reminders that follow a table (e.g. "Wait for explicit verbal 'yes' before pressing record.").
- **No `<br><br>` line breaks inside table cells.** Each cell holds one short scannable line. If a question has multiple parts, split into separate rows (`Q12`, `Q12 follow-up`) or sub-questions (`Q6a`, `Q6b`, …).
- **Pre-Session Checklist and Post-Session Debrief are bullets/numbered lists, NOT tables** (they aren't questions).
- **Total target length is format-dependent: interview ~4–5 pages (max 7); prototype/usability ~6–8 pages** (task lists + screens push it longer). If a guide exceeds its ceiling, cut moderator-note paragraphs and redundant explanation — never the task/observation content.
- **Comparison-cohort studies:** label any Ask-table row needing per-cohort variants with the `(Cohort A) / (Cohort B)` convention (see "Multi-cohort studies" in Step 3) rather than improvising inline labels.

#### Visual (portable-first — default vs. optional variants)

**Default — Native Google Docs (portable):** apply only native Google Docs styling with the session's connected Docs tools — the native Title style for the title, native Heading styles (H1/H2/H3) for phase headings, native body style for prose, and native tables for the question tables. Use a standard Docs font at a readable size. Keep the breadcrumb visually secondary and the title dominant. Keep RACI as real bullet paragraphs. Keep tables to two columns (short label / read-aloud line) with readable padding. No custom fonts, no custom palette, no local script, no CLI. This is what every researcher gets unless they opt into a variant in Section 1.

**Optional — Instacart / Jedida variant (Jedida Reporting navy/blue):** only when the researcher explicitly picks it in Section 1.
- **Body / table cells:** Calibri 10pt (`#000000`)
- **Headings (H1/H2/H3):** Calibri bold, navy `#1F4E79`; H1 paragraphs get a full-width NAV background (navy fill + WHITE bold text) as a nav bar
- **Title:** navy `#1F4E79`, bold, large
- **Table header row:** WHITE text on navy `#1F4E79` background, bold
- **Label column (col 1, 2-col tables):** LBLUE `#D6E4F0` fill, bold navy text, snug width (~130pt fixed per `feedback_two_col_table_label_snug.md`)
- **Alternating body rows:** WHITE / LGRAY `#F5F5F5`
- **Borders:** DGRAY `#D0D0D0`
- **Page margins:** 45pt (~0.625")

**Optional — Instacart / Jedida variant (forest-green mod-guide style):** only when the researcher explicitly picks it in Section 1.
- DM Sans 10pt body · DM Serif Display 20/16/16pt headings in dark green `#2D4A3E` · dark-green table headers · dark-green bold label columns · col widths 115/350pt · light gray `#F6F7FA` alternating rows.

#### Styling pipeline

**Default path (native Google Docs — no personal scripts):** create the doc in the confirmed Drive folder with the session's connected Google Docs tools, then apply native Title/Heading/body styles and native tables directly. This path has no dependency on `md2doc`, `gws`/`gohan`, or any local styling script, so it works for any researcher.

**Optional Jedida-variant path (personal pipeline — only when the researcher opts in and Jedida's local environment is available):** run in order after upload:

1. `md2doc upload-gdoc.py [file] --folder-id [confirmed folder]` → creates the doc and applies the HTML import (style-gdoc-full pass for base structure)
2. **Jedida Reporting (navy/blue):** `~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py [doc-id]` → runs 4 passes (sanitize → document margins → named styles → H1 nav bars → tables with snug label column).
3. **Forest-green mod-guide style:** `~/.claude/skills/mod-guide/scripts/apply_canonical_template.py [doc-id]` → applies the locked canonical spec (page setup, DM Sans body / DM Serif Display headings, dark-green table headers, dark-green bold label cols, 0.5pt #C7C7C7 borders, 8pt cell padding, BULLET_DISC_CIRCLE_SQUARE, clears SUBSCRIPT runs, H2 non-bold + 36pt above / 12pt below). See `references/canonical-template-spec.md`.
4. **Custom — user-supplied reference doc:** `~/.claude/skills/mod-guide/scripts/apply_custom_template.py [target-doc-id] [ref-doc-id]` → extracts the ref doc's spec at runtime and applies the same phases.

> The legacy 3-pass pipeline (`style-gdoc-full` → `font_and_widths.py` → `rebold_col1.py`) is **superseded** by the consolidated single-script approach above. The old scripts are still present in `scripts/` for backward compatibility but should not be used by new flows.
>
> All Jedida-variant scripts use `uv run --python 3.12 --with google-api-python-client --with google-auth --with google-auth-oauthlib --with google-auth-httplib2 --with requests --with python-dotenv --with markdown --with pillow python [script]`, and require Jedida's local auth/environment. If any of these are unavailable, fall back to the native Google Docs default rather than blocking delivery.

---

### CONTENT GENERATION RULES

1. **No leading questions.** Every question open-ended, non-directional. Never assume the participant's opinion. (NN/g Rosala — 6 Mistakes)
2. **No interface terminology in tasks.** Describe goals, not UI ("find a way to…" not "click the button to…").
3. **Funnel technique.** Within each topic: broad → specific → closed. Broad first avoids priming (NN/g).
4. **Specific incidents over typical behavior.** "Tell me about the last time you…" beats "How often do you…" — closes the say-do gap (NN/g Critical Incident Technique).
5. **No hypotheticals except as projective tools.** "If this could change anything…" is fine at the end; "Would you use this?" is not (NN/g).
6. **No compound questions inside a single Ask cell.** If a question has 2-3 follow-ups that always go together (e.g. "What is it asking? What does '[word]' mean? How would you say this in your own words?"), they may share a cell. Otherwise split into Q + Q-follow-up rows.
7. **Probes named in PROSE above the table, not in-line in cells.** Use a single `Probes to use:` line per phase.
8. **Time-aware.** Allocate per study type (Step 2a). Core gets 70-80% of total.
9. **Participant-appropriate language.** Match vocabulary to the participant profile.
10. **Watch-fors and "don'ts" go in prose**, not in [Watch For] or [Moderator Note] table rows. Keep them above the question table they apply to.
11. **Capture-verbatim flags** (e.g. "Capture Q11 verbatim — feeds the survey wording") go in prose above the relevant table, not as a separate row.

---

### PROBING TAXONOMY — QUICK REFERENCE

Reference `references/mod-guide-methodology.md` for the full taxonomy (definitions, examples, sources). In-line names to use in the guide:

| Probe | One-line rule |
|-------|---------------|
| **Echo** (NN/g Fessenden) | Repeat their last phrase with slight interrogatory tone. |
| **Silence** (Portigal, Hall) | Count 5-10. Let them fill the gap — don't rescue. |
| **Tell-Me-More** (Anderson, NN/g) | "Tell me more about that." Evergreen. |
| **Laddering / Why** (Portigal) | "Why was that important to you?" Climb from behavior to value. |
| **Critical Incident** (Flanagan via NN/g) | "Tell me about the last time you…" Replaces typical-behavior questions. |
| **Contrast** (Portigal) | "How did that compare to [prior experience]?" |
| **Hypothetical / Projective** (Portigal — late only) | "If we came back in 5 years, what would be different?" |
| **Boomerang** (NN/g Fessenden) | Return their question: "What would you normally do?" |
| **Columbo** (NN/g Fessenden) | Trail off mid-sentence; let them complete. |
| **Specificity** (NN/g) | When vague words appear (frustrated, confusing): "What do you mean by [word]?" |

---

### BIAS MITIGATION CHECKLIST

Embed these reminders in `[Moderator Note]` callouts through the guide. Full discussion in references/.

- [ ] **Leading questions** — No "Do you like…?", "Was it because…?", or "Would you prefer…?" (NN/g, Hall)
- [ ] **Social desirability** — Participants lean helpful/positive. Normalize negative answers explicitly: "I didn't design this." (Portigal, Indi Young)
- [ ] **Acquiescence bias** — Avoid yes/no framing. Use open questions. (Hall — *Just Enough Research*)
- [ ] **Confirmation bias (moderator)** — Brain-dump hypotheses before the session so you aren't hunting for them. (Portigal)
- [ ] **Recall bias** — Pin to recent, specific incidents ("last time") not general patterns. (NN/g CIT)
- [ ] **Stated-vs-actual (say-do gap)** — Don't trust self-reported frequency or intent. Combine with observation. (NN/g, Indi Young)
- [ ] **Observer effect** — Max 2-3 silent observers; no one else in frame. (NN/g Rosala)
- [ ] **Moderator talk-ratio** — Aim for 80% participant talk time. (NN/g)

---

## Step 4.5 — Section 3: Self-Critique Checklist (the critique half of the quality gate)

This is the **critique half** of the Section 3 quality gate announced at the end of Step 4. It runs automatically — no researcher pop-ups — before the multi-agent review (Step 5) and before the Google Doc is created (Step 6). Say in chat: *"Running the critique pass now — pressure-testing the guide for methodology gaps, biased phrasing, and weak probes."*

Run the assembled guide through this self-audit (do not rebuild it — this is the skill's existing audit). Adapted from the AIxUXR Playbook's **Discussion Guide Critic** prompt (Loosbrock, Oct 2025), which positions the reviewer as a *methodological auditor + strategic sparring partner* grounded in the Systematic Literature Review of Best Practices for Qualitative Interview Guides.

**How to use:** Walk each dimension yourself, self-contained — the Parts below already internalize the AIxUXR Critic Prompt's checks, so there's no separate external prompt/doc to run. If any row fails, revise the guide and re-walk the checklist, up to 2 revision passes; on the 3rd pass, carry any still-unresolved rows forward flagged inline as `[Auditor Note: ...]` rather than looping indefinitely, so the researcher sees the caveat. Fold clear fixes into the assembled guide, then proceed to the multi-agent review (Step 5) before creating the Doc.

**🔀 FORMAT-AWARE — apply only the rows that fit the chosen format.** Each row is tagged **[Interview]**, **[Prototype]**, or **[Both]**. Skip a row tagged for the other format — do NOT flag a correctly-built prototype guide for "missing warm-up questions" or a correctly-built interview guide for "missing task success criteria." Read the **expected phase names and time split from the chosen format's Step 2a row**, not from a hardcoded interview shape: interview-IDI Core ≈ 80%, usability Core (tasks) ≈ 75%, concept ≈ 70%. A prototype guide's "Core" is the Task Flows block; its warm-up is the Background block.

### Part 1 — Methodological Audit (Structure & Flow)

| Dimension | Tag | What "Good" Looks Like |
|-----------|-----|------------------------|
| **Opening rapport & consent** | [Both] | Warm, non-clinical opening. Explicit recording consent before recorder starts. Participant knows purpose, duration, confidentiality, right to skip/stop. Prototype adds the think-aloud intro + prototype-limitations caveat. (AIxUXR §Prompt A "Introduction & Consent"; NN/g Fessenden) |
| **Phase structure** | [Both] | Phases and times match the **chosen format's Step 2a row**, displayed per section. Interview: Intro → Warm-up → Core (themes) → Wrap-up. Prototype: Intro → Background → Task Flows → Wrap-up (+ vendor back-matter). Don't force interview phase names onto a prototype guide. (AIxUXR §Prompt A "Calculate and Allocate Time") |
| **Funnel within Core** | [Interview] | Broad "Grand Tour" question first, then specific-incident probes, then closed clarifiers. (Prototype analog: tasks ordered simple → complex; unaided Feedback row before the directed Task row.) (AIxUXR §Prompt A.3; NN/g Rosala) |
| **Time budgeting** | [Both] | Per-phase minutes allocated and summing to the session length; Core/Task-Flows gets the format's share (IDI ≈ 80%, usability ≈ 75%, concept ≈ 70%). Warm-up/Background not eating Core. Wrap-up protected. (AIxUXR §Prompt A.1) |
| **Question / task sequencing** | [Both] | Each question or task builds on the last; no abrupt jumps without a bridge; transitions signposted. (AIxUXR §V2 Prompt B Part 2) |
| **Wrap-up dual function** | [Both] | (a) Reflection — interview: "play back the themes"; prototype: most-important / most-confusing. (b) "Anything else?" open catch-all. (AIxUXR §Prompt B SRQ1.2) |

### Part 2 — Question Quality Audit (Phrasing & Bias)

| Check | Tag | Fail Pattern → Fix |
|-------|-----|--------------------|
| **Leading questions** | [Both] | ❌ "Don't you find the new checkout faster?" → ✅ "Describe your experience using the new checkout." (AIxUXR §Prompt B example row; NN/g 6 Mistakes) |
| **Hypothetical / speculative** | [Both] | ❌ "Would you use this?" / "What would you do if…?" → ✅ "Tell me about the last time you…" Reserve hypotheticals for the end as projective tools only. (AIxUXR §Prompt A.4; Portigal) |
| **Closed yes/no framing** | [Both] | ❌ "Did you like it?" → ✅ "How would you describe that experience?" — *except* the deliberate post-task 1–5 ease rating in a prototype guide, which is meant to be scaled. (AIxUXR §V2 Prompt B; Hall) |
| **Compound / double-barrelled** | [Both] | ❌ "How easy and enjoyable was it?" → ✅ Split into two questions. (NN/g) |
| **Jargon / insider terminology** | [Both] | ❌ UI labels, internal product names, acronyms the participant hasn't used → ✅ Plain language matched to participant vocabulary. (AIxUXR §Responsible AI — "Inclusivity of language") |
| **Past-behavior anchoring** | [Interview] | Interview Core questions tied to a concrete, recent incident — not "typically"/"in general." *Do NOT apply to prototype task rows* (they are present-tense observed actions by design — check instead that the task's **scenario** grounds a realistic situation). (AIxUXR §Prompt A.4; NN/g CIT) |
| **Goals-not-UI task framing** | [Prototype] | Tasks describe the goal, not the interface ("find a way to add these items", never "click the green Add button"). Every task has a scenario; first-impression screens use the Feedback-then-Task pattern. (AIxUXR §Use Case 2) |
| **Inclusivity & cultural assumptions** | [Both] | Questions don't assume a household structure, income level, cooking frequency, dietary pattern, or tech proficiency. (AIxUXR §RAI "Equity and Fairness") |

### Part 3 — Probing & Moderator Guidance Audit

| Check | Tag | What to Verify |
|-------|-----|----------------|
| **Probe quality per question** | [Interview] | Each interview Core question has 1-2 named probes attached (Echo, Tell-Me-More, Laddering, Silence, Critical Incident). No "naked" questions. (Prototype: think-aloud + observation cues play this role.) (See Probing Taxonomy.) |
| **Moderator Notes / cues embedded** | [Both] | Interview: `[Moderator Note: ...]` at every transition + Core topic. Prototype: per-phase **observation cues** (yes/no + "if not, what instead?") in a prose line below each phase list, plus behavior forks / WoZ triggers. (AIxUXR §Prompt A.5) |
| **Silence as a tool** | [Both] | Reminds moderator to count 5-10 seconds before filling gaps. (NN/g Fessenden; Portigal) |
| **Observation cues present** | [Prototype] | Every task flow carries a success/observation cue (yes/no + "if not, what do they do instead?") and a reused post-task ease rating. No task flow without a cue. |
| **Task framing: goal not UI** | [Prototype] | Tasks describe the goal, not the UI ("find a way to…" not "click the red button"). (AIxUXR §Use Case 2 Critical Rule) |
| **Priming → Expectation → Action → Alignment** | [Prototype] | Each task includes the four-part sequence (set context → what do you expect → do it → did it match?). (AIxUXR §Use Case 4; NN/g) |
| **Problem validation before reveal** | [Prototype — concept only] | Blind-need questions precede the concept reveal to avoid biasing desirability. (AIxUXR §Use Case 3 "The Reveal technique") |

### Part 4 — Strategic & Efficiency Audit

| Check | What to Verify |
|-------|----------------|
| **Coverage of research objectives** | Every objective in the RPP maps to at least one Core question. No orphan objectives; no orphan questions without an objective. (AIxUXR §V2 Prompt B Part 1) |
| **Redundancy check** | Scan for questions that probe the same underlying construct twice. Consolidate to save session time. (AIxUXR §V2 Prompt B Part 4 "Redundancy & Efficiency Report") |
| **Gaps / additional questions** | Are there adjacent insights the guide misses? Suggest 1-3 generative additions tied to objectives. (AIxUXR §V2 Prompt B Part 3) |
| **Scope discipline** | Critique stays methodological/strategic. Do NOT suggest UI copy changes, design decisions, or product strategy. (AIxUXR §V2 Prompt B role: "NOT a UI/UX copywriter") |
| **Pilot reminder** | The Step 6 chat summary (not the guide document itself) includes a one-line reminder to pilot the guide with a teammate or friendly participant before formal data collection. (AIxUXR §6 "Always, pilot your guide") |

### Part 5 — Responsible-AI & Construct-Validity Checks (from Questionnaire Critique)

Applies especially when the guide includes structured rating questions or quant-style intercepts within a qual session.

| Check | What to Verify |
|-------|----------------|
| **Construct validity** | For any rating/scale question, ensure the revised wording still measures the intended construct — not just a clearer-sounding variant. (AIxUXR §Questionnaire Critique "VALIDATE THE CONSTRUCT") |
| **Automation-bias guardrail** | Researcher must sanity-check every AI-suggested revision against the original research intent, not blindly accept. (AIxUXR §Questionnaire Critique "Primary Risk: Automation Bias") |
| **PII scrub** | Confirm the RPP/PRD pasted into any AI prompt has been stripped of real participant names, emails, phone numbers, addresses. (AIxUXR §Critical Guardrails "NO PII, EVER") |
| **Attribution & disclosure** | When sharing the final guide with stakeholders, note that AI was used for the first-pass draft/critique. Transparency builds trust. (AIxUXR §6 "Attribute the Assist"; H.E.A.R.T. "Transparent") |
| **Guide is a protocol, not a cage** | Remind researcher: in live session, deviate from the script when valuable emergent narratives appear. (AIxUXR §6 "The Guide is a Protocol, Not a Cage") |

---

## Step 5 — Section 3: Multi-Agent Review (automatic, before the Doc)

Run the multi-agent review on the fixed guide content — before the Google Doc is created. This is the second half of the quality gate. It is automatic; do not ask permission. The researcher was already told this is coming (the end-of-Step-4 announcement).

- Say in chat: *"Running the multi-agent review now — several independent reviewers check the guide for inconsistencies and problems in parallel."*
- Check the live skill list, then invoke `/multi-agent-check` when it is installed. Let that skill run its own questions and approval gate.
- If `multi-agent-check` is not installed in this environment, disclose that the parallel review cannot run and proceed on the critique-only pass (Step 4.5).
- Fold any confirmed fixes into the assembled guide before creating the Doc.

The expected sequence is **approved blocks → self-critique → multi-agent → fixes → create the Google Doc → share.** Never describe the guide as final before both checks have run.

---

## Step 6 — Upload, Style, Verify + Share (NO researcher QUESTIONS — execute the delivery silently)

🚫 **Step 6 runs with zero `AskUserQuestion` calls to the researcher.** The upload-yes/no question is gone; the styling-choice and destination were already decided in Section 1; the read-back confirmation is gone. (Note: `/multi-agent-check` in Step 5 may run its own gate — that is that skill's, not this delivery step's.) If a fact is missing, pick a sensible default and proceed.

Status updates are welcome (a one-line "Creating the doc… Applying [style]…" message). What's not fine: any question, any "want me to…?" Treat Step 6 like a deterministic script.

### 6.1 Confirm destination and create the doc

1. Use the Drive destination confirmed in Section 1. (Re-state it in the status line; do not re-ask.) If, for a real run, no destination was ever confirmed, that is a Section 1 gap — confirm it before writing, then proceed.
2. **Default (portable) path — Option 4 — Leadership:** produce the clean, edited leadership look with the bundled formatter — native Google Docs only, no personal scripts or auth. Run the `scripts/option4_guide_layout.py` pipeline against `references/option4-guide-style.json` (load `references/option4-guide-style.md` first for the visual contract):
   - `manifest` — parse the approved guide markdown into a build manifest;
   - import the markdown into the confirmed Drive folder;
   - `normalize` — clean up conversion artifacts and rebuild cells;
   - `format` — generate and apply the exact Option 4 Google Docs batch operations (DM Serif Display / DM Sans typography, dark-green section bands on the phase/theme headings, pale-yellow mock-warning shading, fixed table styling);
   - `verify` — validate the visual invariants (page geometry, fonts, colors, band styling, table widths/padding), then export/render and eyeball the opening page and a dense page.
   - **Completion gate:** if the environment cannot apply or verify the contract (no write-capable Docs integration, no render), do NOT silently ship a half-styled doc — fall back to the plain-native path below and say so plainly in the chat summary (consistent with "never block delivery on a styling failure"). Note: the one contract value not yet defined is table border color/weight; mirror it from `research-plan/scripts/option4_layout.py` on a live run for a consistent thin neutral border.
3. **Plain native Google Docs (fallback / explicit pick):** create the doc in the confirmed folder with the session's connected Google Docs tools, then apply native Title/Heading/body styles and native tables directly. No Option 4 styling, no CLI, no personal script. Use only when the researcher picks it or the Option 4 gate above falls back.
4. **Optional Jedida-variant path (only when the researcher opted in and Jedida's local environment is available):** upload via `md2doc`'s `upload-gdoc.py` to the confirmed folder, then apply the chosen variant styler:
   - **Jedida Reporting (navy/blue):** `~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py [doc-id]` — navy NAV H1 nav bars, LBLUE label columns, alternating WHITE/LGRAY rows, DGRAY borders, Calibri throughout, via 4 passes (sanitize → margins → named-style typography → H1 nav bars → tables with snug label column).
   - **Forest-green mod-guide style:** `scripts/apply_canonical_template.py [doc-id]` — clears SUBSCRIPT runs, sets page size + margins, applies run-level typography, styles all 2-col tables (col widths 96/715.5pt, dark-green header with white bold, dark-green bold label col, #161416 content col, 0.5pt #C7C7C7 borders, 8pt padding), sets H2 non-bold with 36pt above / 12pt below, NORMAL_TEXT 4pt spaceBelow + 115% lineSpacing, BULLET_DISC_CIRCLE_SQUARE.
   - **Custom — user-supplied reference doc:** `scripts/apply_custom_template.py [target-doc-id] [ref-doc-id]`. Apply silently — no read-back, no confirmation prompt.
   - **If a variant script crashes or errors at runtime** (missing dependency, auth failure, bad doc ID): do not retry in a loop and do not ask the researcher what to do. Fall back to the Option 4 default styling (or plain native if Option 4 also can't run), and say so plainly in the chat summary (e.g. "Jedida-variant styling failed [reason] — sharing the doc with the Option 4 leadership styling instead; let me know if you want me to retry"). The doc and its content matter more than the variant; never block delivery on a styling failure.
5. **Demo/mock runs:** do not create a Drive artifact at all (see Demo-run auto-trigger). Return the markdown draft in chat with the `⚠️ TEST ARTIFACT` label; do not save to Drive, the tracker, or project folders.

### 6.2 Verify and correct

1. Read the created document back (e.g. `get_doc_as_markdown` or the connected Docs read tool).
2. Compare it against every approved block and the parameter header — ownership block completeness (`[TBD — fill in]` where unconfirmed), the parameter table, Pre-Session Checklist and Post-Session Debrief as lists (not tables), the Consent script verbatim, and **tables containing only read-aloud/do lines** (probes/watch-fors/observation-cues/don'ts/rationale in prose, per the domain rule).
3. **Confirm the guide ends at the format-correct last section** (per the "guide MUST end at…" rule): interview → optional Parking Lot, else Participants Log; internal prototype → Post-Session Debrief; vendor prototype → Communication & Deliverables (+ Timeline). No Master Probe Bank, Bias Mitigation Checklist, Self-Critique Audit, or pilot reminder inside the doc.
4. **Confirm length against the format ceiling:** interview ~4–5 pages (max 7); prototype ~6–8 pages. If over ceiling, cut moderator-note paragraphs and redundant explanation — never task/observation content.
5. **When the format is Prototype/Usability, additionally confirm the prototype must-haves:** primary + backup prototype links; the read-aloud Introduction and every phase/task, comparison, and recap block rendered as **bold-label lists, not Cue tables** (only the Parameter dashboard and Session Flow agenda are tables); a per-phase **observation-cue prose line below each phase list** (not inside list items); the reused post-task ease rating after every flow; the experimental-design/counterbalance prose note (if any); P0/P1 objectives kept out of the task lists; the top Links row; and (vendor-run) the Communication & Deliverables back-matter.
6. Correct every issue, then read back again. If rendering (PDF/thumbnail) is unavailable, disclose that verification was structural rather than visual.

### 6.3 Return the verified guide

1. Share the final Google Doc link in chat with a short summary of what's in the guide, plus a one-line **pilot reminder** (per Step 4.5 Part 4) to test the guide with a teammate or friendly participant before formal data collection.
2. State verification status: "content complete, structure checked, links checked" plus any explicit limitation.
3. **Only after the link is shared** is the skill allowed to respond to follow-up questions or correction requests from the researcher.
4. Do not update project trackers or progress files unless the researcher separately asks (and never for a demo/mock, or Sasha/personal content).

---

## Tool Usage

- **AskUserQuestion** — present recommendations and gather approvals: the Section 1 parameter batch, the Section 2 block-by-block content approvals, and the Section 1 delivery/destination question.
- **Directory / people search** (`mcp__glean_default__employee_search` or the connected directory search) — verify current stakeholder identities before carrying RACI names forward (Section 1, Row 9). *(May require auth in this session; if unavailable, keep a name only on the researcher's live confirmation, else `[TBD — fill in]`.)*
- **`/multi-agent-check`** — the parallel review in Step 5; check the live skill list and invoke when installed, else disclose and proceed critique-only.
- **google-docs:fetch-google-doc** / **Glean** (`mcp__glean_default__read_document`) — read PRDs, briefs, or reference docs from Google Drive (whichever is connected).
- **Read** tool or **download-gdoc.py** / **read-gdoc.py** — fallback readers for Google Docs.
- **Connected Google Docs / Drive tools** — create the guide in the confirmed folder, apply the batch operations from the Option 4 formatter (or native styles on the plain-native fallback), read it back to verify, and return the link. No personal script required.
- **`scripts/option4_guide_layout.py`** — **default (portable) styler:** the bundled Option 4 — Leadership formatter+verifier (`manifest`/`normalize`/`format`/`verify`). Produces the clean, edited leadership look with native Google Docs only. Drives from `references/option4-guide-style.json`.
- **`references/option4-guide-style.json`** + **`references/option4-guide-style.md`** — the Option 4 visual contract (machine-readable + human-readable); load the `.md` before formatting. Visual tokens are shared verbatim with `/research-plan`'s Option 4.
- **md2doc** (`upload-gdoc.py`) — *optional Jedida-variant* uploader (personal pipeline only).
- **`~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py`** — *optional Jedida-variant* styler (navy/blue). Requires Jedida's local environment.
- **scripts/apply_canonical_template.py** — *optional Jedida-variant* forest-green mod-guide template (only when the researcher explicitly picks it).
- **scripts/apply_custom_template.py** — *optional Jedida-variant* — extract styling from a user-supplied reference doc and apply it to the target.
- **references/template-prototype-usability.md** — **load in Section 1 when the format is Prototype/Usability.** Holds the prototype Section 1 params, Section 2 blocks, OUTPUT TEMPLATE, and generation rules.
- **references/template-interview.md** — **load in Section 1 when the format is Interview.** Holds the interview Section 1 params, Section 2 blocks, OUTPUT TEMPLATE, and generation rules. (Only the format-neutral shared scaffolding is inline in Step 4; the interview body template lives here.)
- **references/canonical-template-spec.md** — human-readable spec for the forest-green variant (mirrors the values in `apply_canonical_template.py`).
- **references/mod-guide-methodology.md** — load on demand when the researcher asks about a specific probe, bias, or study-type nuance (incl. §3 sub-shapes: usability think-aloud, concept 5-second rule, diary entry-review, focus-group turn-taking).

---

## Sources

- Portigal, S. (2023). *Interviewing Users: How to Uncover Compelling Insights* (2nd ed.). Rosenfeld Media. [portigal.com](https://portigal.com/books/interviewing-users-2/)
- Young, I. *Listening Deeply* and mental model method. [indiyoung.com](https://indiyoung.com/method/)
- Hall, E. (2019). *Just Enough Research* (revised ed.). A Book Apart.
- Sharon, T. (2016). *Validating Product Ideas: Through Lean User Research*. Rosenfeld Media.
- Nielsen Norman Group: Rosala, M. — [User Interviews 101](https://www.nngroup.com/articles/user-interviews/), [6 Mistakes When Crafting Interview Questions](https://www.nngroup.com/articles/interview-questions-mistakes/), [Writing an Effective Guide for a UX Interview](https://www.nngroup.com/articles/interview-guide/), [The Funnel Technique](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/), [5 Facilitation Mistakes](https://www.nngroup.com/articles/interview-facilitation-mistakes/), [Why User Interviews Fail](https://www.nngroup.com/articles/why-user-interviews-fail/), [The Critical Incident Technique in UX](https://www.nngroup.com/articles/critical-incident-technique/); Pernice, K. & Moran, K. — [Thinking Aloud: The #1 Usability Tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/); Fessenden, T. — [Talking with Users in a Usability Test](https://www.nngroup.com/articles/talking-to-users/), [Checklist for Moderating a Usability Test](https://www.nngroup.com/articles/usability-checklist/).
- Anderson, N. — [User Research Academy](https://www.userresearchacademy.com/) and dscout *People Nerds*.
- dscout — [17 Pro Tips to Perfect One-on-One Interviews](https://dscout.com/people-nerds/tips-master-researcher-participant-interviews), [Dig Deeper with Follow-Up Questions](https://dscout.com/people-nerds/generative-research-questions).
- **Instacart AIxUXR Playbook** (internal) — Loosbrock, K., Venkatraman, S., & Milton, J. (2025). *Playbook for integrating AI within UXR workflows* (Pilot, Sep 30 / Oct 9 / Dec 1, 2025). Specifically: §1.2 "The H.E.A.R.T. of AI in Research"; *Discussion Guide Drafter & Critic* spoke (Prompt A generation, Prompt B critique — V1 and V2 revised with Bhargavi's feedback); *Questionnaire Critic* spoke (Responsible AI principles, construct validity, automation-bias guardrails). Knowledge base: *A Systematic Literature Review of Best Practices for Crafting and Evaluating Moderated Qualitative Interview Guides in UX Research*.
