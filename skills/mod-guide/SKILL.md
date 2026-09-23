---
name: mod-guide
description: Use when a UX researcher is about to conduct user interviews, usability tests, or diary study check-ins and needs a moderation guide with warm-up, discussion sections, probing techniques, and closing. Triggers on "write a moderation guide", "interview guide", "discussion guide", "facilitation script", "/mod-guide", or natural asks like "help me write interview questions for this study", "I need a script for my usability test", "prep questions for these sessions", or "build a discussion guide for [study]".
---

# Moderation Guide Builder

Generate a ready-to-facilitate moderation guide for an Instacart UX research session — in-depth interview (IDI), usability test with think-aloud, concept test, focus group, or diary study check-in. Grounded in Steve Portigal's *Interviewing Users* (2nd ed.), Indi Young's *Listening Deeply*, Nielsen Norman Group (Rosala, Pernice, Moran, Fessenden), Erika Hall's *Just Enough Research*, Nikki Anderson's *User Research Academy*, and Instacart's internal **AIxUXR Playbook** (Loosbrock & Venkatraman, 2025) — specifically the *Discussion Guide Drafter & Critic* spoke.

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

1. Study inputs have been read and the study parameters proposed from them.
2. The researcher has approved every applicable **Section 1** parameter (the upfront setup batch) **and** every **Section 2** guide-content block (Warm-Up → Core → optional Stimulus → Wrap-Up).
3. The self-critique pass and the multi-agent review have both run, with fixes folded in.
4. The Google Drive destination has been confirmed.
5. The guide has gone through the **create → style → verify** pipeline, native Google Docs first.
6. A working Google Doc link has been returned with a one-line pilot reminder and verification status.

Both quality checks run before the final Google Doc is drafted. Drive destination confirmation must happen before document creation.

Markdown is an intermediate representation, not the completed deliverable. A mock or demo stays out of Drive and the tracker unless the tester explicitly requests a test document.

## Flow overview

| Step | Work | Completion gate |
|---|---|---|
| **1** | Gather PRD, brief, kickoff notes, Slack thread, or free-form description → announce the 3-section structure to the researcher | Inputs received; researcher understands the full workflow |
| **2** | Analyze inputs; propose the study-parameters table (read-only context); run the Say-Do Gap risk check | Parameters and risk flag proposed |
| **3** | **Section 1 — Study Setup & Parameters:** the consolidated upfront batch of labeled pop-ups (study type, moderation, duration, participants, profile, topics/tasks [multi], Say-Do module, RACI [multi], stimuli) + Drive-destination & delivery-variant confirmation folded into this batch | All applicable parameters approved; destination confirmed; researcher says "Section 1 locked" |
| **4** | **Section 2 — Guide Content:** draft-first approval, one block at a time (Warm-Up → Core sub-steps, branched by study type → optional Stimulus/Concept → Wrap-Up), each locked before the next, transition announced after each lock | All content blocks approved |
| **4.5** | **Section 3 —** auto-run the 5-part self-critique (announced at end of Step 4) as the critique half | Gaps fixed or explicitly accepted |
| **5** | Auto-run the multi-agent review on the fixed content — before the Doc | Review complete; confirmed fixes folded in |
| **6** | Draft the Google Doc last: confirm destination, create native Google Doc, style (native default; optional Jedida variant), read back, verify, correct, return with pilot reminder | Content, structure, tables, links, and location pass |

## Portable Google Docs contract

The skill must work for any researcher with a write-capable Google Docs integration.

- **Native Google Docs is the default deliverable path.** Use the session's connected Google Docs / Drive tools and native Docs styling (standard font, native Title/Heading/body styles, native tables) unless the researcher explicitly asks for a personal variant.
- Do not depend on a personal template, custom font, custom palette, private reference document, hardcoded folder ID, local styling script, command-line utility (gws/gohan), or researcher-specific authentication setup for a real run to succeed.
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

> "To build your moderation guide, share whatever you have — PRD, project brief, kickoff Slack thread, meeting notes, or a plain-English description. I'll extract the study parameters and recommend a structure. If you have a Google Doc link, paste it."

**Accept any format:** PRD, brief, Slack thread, Gemini meeting notes, or verbal description. If a Google Doc URL is shared, read it via `google-docs:fetch-google-doc` or Glean (`mcp__glean_default__read_document`) — whichever is available in this environment. If neither tool is connected, ask the researcher to paste the doc's content directly rather than stalling on a missing tool.

### Orientation announcement

Once the inputs are in hand, before asking any parameter questions, say in chat:

> Now that you've shared your inputs, I'll pull out the study parameters, then we'll build this moderation guide together — one step at a time.
>
> **We'll work in three sections:**
>
> **Section 1 — Study Setup & Parameters** *(the decisions that shape the guide)*
> Study type · Moderation style · Duration · Participants · Profile · Key topics/tasks · Say-Do Gap module · Stakeholders (RACI) · Stimuli · Drive destination & delivery style
>
> **Section 2 — Guide Content** *(the questions the moderator will actually read)*
> Warm-Up → Core (one block per topic area/task) → optional Stimulus/Concept → Wrap-Up
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

### 2a. Interview Type Selector (determines template branch)

Choose the guide template based on study type. Each branches the output:

| Study Type | When to Use | Core Section Style | Time Split (warm-up / body / close) |
|-----------|-------------|--------------------|--------------------------------------|
| **In-Depth Interview (IDI)** | Understanding motivations, mental models, lived experience | Open-ended discussion, narrative probes, journey mapping | 10% / 80% / 10% |
| **Usability Test (think-aloud)** | Evaluating a design, prototype, or live product | Task-based with success criteria, think-aloud protocol | 10% / 75% / 15% |
| **Concept Test** | Reacting to stimuli (ads, features, flows) | Stimulus presentation, first impressions, comparison | 15% / 70% / 15% |
| **Diary Study Check-in** | Mid/end-of-study longitudinal sync | Entry review + follow-up probes on specific diary entries | 15% / 70% / 15% |
| **Focus Group** | Reactions to concepts in a social context | Turn-taking facilitation, divergent + convergent discussion | 15% / 70% / 15% |

Rationale: time splits follow NN/g's qualitative usability testing study guide and Rosala's interview-guide conventions.

### 2b. Present recommendations

**Render as a real Markdown table — NEVER inside a triple-backtick code fence.** The researcher needs to scan this in proper table formatting, not in monospaced code. Show it directly in the chat as:

> Based on your inputs, here's what I recommend:
>
> | Parameter | Recommendation | Why |
> |-----------|---------------|-----|
> | Study Type | [IDI / Usability / Concept / Diary / Focus] | [1-line rationale from inputs] |
> | Moderated vs Unmoderated | Moderated | [rationale — depth, probing, observation] |
> | Duration | [30/45/60/90 min] | [based on scope + study type] |
> | Number of Participants | [N=8 / 12 / 24] | [based on objectives + saturation] |
> | Participant Profile | [e.g., "Instacart shoppers 25-45, 2+ orders/week"] | [derived from target users] |
> | Key Topics / Tasks | • Topic 1 · Topic 2 · Topic 3 | [mapped to objectives] |
> | Research Goal | [1-2 sentences] | — |
> | Say-Do Gap Risk | [Low / Medium / High] | [see Step 2c] |

(Use the example above as a template — strip the leading `>` characters and write the table directly. The point is: no triple backticks, no code block. A real table.)

**Hand-off to Section 1 (Step 3):** this table is read-only context, not a checkpoint — do not wait for the researcher to react to it. Post the table and immediately continue into Section 1's `AskUserQuestion` batches in the same turn. The table exists so the researcher can see Claude's reasoning at a glance *while* answering the popups (each popup's "Recommended" option is exactly what the table already proposed), not as a separate approve/reject step.

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
| 1 | **Phase/scope** — which phase or sub-study to build (only if multi-phase plan) | single | The earliest unbuilt phase | Other phases · Both phases |
| 2 | **Study type** | single | Best fit from inputs (IDI / Usability / Concept / Diary / Focus) | The two next-best alternatives |
| 3 | **Moderation style** | single | Moderated remote / Moderated in-person / Unmoderated | The two not picked |
| 4 | **Duration** (session length — exclusive) | single | Extracted minutes or 60 min default | 30 / 45 / 60 / 90 (drop the recommended one from this list) |
| 5 | **Number of participants** | single | Extracted N or method-appropriate default (IDI N≈12, usability N≈5–8, concept/focus N≈8–12) | Smaller / larger options |
| 6 | **Participant profile** | single | Extracted screen criterion | Looser / tighter alternatives |
| 7 | **Key topics / tasks** | **multi** | The 3–5 extracted topics, all pre-selected | "Add another topic" · individual topics selectable so the researcher can drop any |
| 8 | **Say-Do Gap module** | single | Include / Skip / Let Claude decide — Recommended depends on Step 2c risk flag | The other two |
| 9 | **Stakeholders (RACI)** | **multi** | Researcher = Responsible; decision-owner/PM = Accountable; PM, EM, design lead = Consulted; skip-level and partners = Informed — extracted names where known, `[TBD — fill in]` elsewhere | "Edit names" · "Use TBD placeholders for all" — each named stakeholder is an individually selectable line |
| 10 | **Stimuli handling** (usability/concept only) | single | Screen-share / static PDF / live prototype | The two not picked |
| **LAST** | **Drive destination & delivery style** (portable-first) | single | See "The mandatory delivery question" below | See below |

**Stakeholder identity verification (Row 9):** Before carrying any name into the RACI block, verify it is still current using the people/directory search tool (e.g. `mcp__glean_default__employee_search` or the connected directory search). Stored context and project files go stale — a named team member may have left or changed roles. If there is any doubt about who belongs in a role, ask the researcher directly *inside the RACI pop-up's "Other" field prompt or as part of this same Section 1 question* (e.g. "I see [Name] listed as [Role] — is that still accurate?"). Never carry a name forward from memory or a stale file without a live check. *(Current-session caveat: the people/Glean MCPs may require auth; if the directory search is unavailable, say so, keep the name only if the researcher confirms it live, and otherwise use `[TBD — fill in]`.)*

**Only two parameter rows may be skipped — and only under these exact conditions:**
- **Row 1 (Phase/scope)** — skip only when the inputs describe a single-phase study with no sub-studies.
- **Terminology note (Row 1):** "Phase" here means a study *sub-phase* — e.g. a diagnostic wave followed by a validation wave within this one study — not the RPP's "Phase 1–5" process-stage grid (Plan/Recruit/Fieldwork/Synthesis/Readout) in the Research Timeline header. Same word, different meaning — don't conflate the two.
- **Row 10 (Stimuli handling)** — skip only when the study is an IDI, diary check-in, or focus group with no UI/concept stimulus at all. A card-sort or stimulus-review IDI still involves a stimulus, so still ask this row even though the study is nominally an "IDI."

**Never fabricate a stakeholder name.** If a name isn't in the inputs, use `[TBD — fill in]` rather than guessing — this mirrors the `/research-plan` skill's RACI convention and Jedida's "grounded in data, never assumed" rule.

(The **LAST row — Drive destination & delivery style** — is also skipped on demo/sample/test runs, which create no Drive artifact and auto-resolve styling per the demo rule. See "Demo-run auto-trigger" below. On real runs it is always asked, so the destination is confirmed before any doc is created.)

**Every other row must be asked**, even if the answer seems obvious from the inputs. The researcher confirming an extracted value is the whole point. Never skip a row just because you think you know the answer.

### Multi-cohort studies (comparison-cohort branching)

When the research plan specifies more than one cohort (e.g. an "abandoner" cohort vs. a "non-abandoner" comparison cohort — the same contrastive-design pattern the upstream `/research-plan` skill supports), don't leave per-cohort wording to be improvised inline. Label any question-set row above, and any Ask-table row in Section 2 (Step 4), that needs divergent phrasing per cohort with an explicit `(Cohort A) / (Cohort B)` suffix (or however many cohorts exist) — e.g. "Q5 (Cohort A)" / "Q5 (Cohort B)".

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

**Delivery / styling variant** — single-select (this is the "report audience variant" style of exclusive choice). **Native Google Docs is the default and Recommended path** (portable-first); the personal pipeline is the optional, clearly-labeled Instacart / Jedida variant:

- **"Native Google Docs (portable default)" (Recommended)** — Standard Google Docs: native Title/Heading/body styles, a standard Docs font at readable size, native tables. Works for any researcher with a write-capable Docs integration; no personal scripts, no CLI, no custom fonts. This is the default whenever the researcher expresses no preference.
- **"Instacart / Jedida variant — Jedida Reporting (navy/blue)"** *(optional personal pipeline)* — Jedida Reporting palette (navy NAV H1 nav bars, LBLUE label columns, alternating WHITE/LGRAY rows, DGRAY borders, Calibri typography). Styler: `~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py`. Requires Jedida's local scripts/auth.
- **"Instacart / Jedida variant — forest-green mod-guide style"** *(optional personal pipeline)* — Original mod-guide template (DM Serif Display headings, DM Sans body, dark-green table headers, dark-green bold label columns). See `references/canonical-template-spec.md`. Source: `https://docs.google.com/document/d/18Q9V4th9BwwNtlLXSncmMpiN591XTV1RzCUAyxym7wI/edit`
- **"Brainstorm with me"** — last option, as on every pop-up.

**To match a custom reference doc instead** (also an optional Jedida-variant path), the researcher types the Google Doc URL directly into the auto-added "Other" field. Mention this in the question text so the researcher knows "Other" is live for this purpose.

If the "Other" field comes back with a parseable Google Doc URL, treat it as: delivery = Custom Reference variant, ref_doc_id = parsed-from-URL. If "Other" comes back with something that is NOT a parseable Google Doc URL (a typo, or unrelated free-text feedback), fall back to the Recommended native default rather than blocking — don't re-prompt to clarify; flag the ambiguity to the researcher after the doc is delivered instead.

> **Note on the 2026-09-08 global default:** Jedida's CLAUDE.md makes "Jedi's Template" the automatic default styling for *every* new Google Doc in her personal environment. This delivery question is a deliberate, mod-guide-specific, portable exception: for any researcher, native Google Docs is the default; Jedida's personal templates (Jedida Reporting / forest-green / custom-match / Jedi's Template) are opt-in variants. Don't silently apply a personal template to a shared run; that would break portability and remove the researcher's choice this step exists to preserve.

### Holding the delivery answer for Step 6

- **Native Google Docs (portable default)** → after creating the doc, apply native Google Docs styling only (native Title/heading/body styles, standard font, native tables). No personal script, no CLI. This is the path for every researcher who does not opt into a variant.
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

**The blocks, in order (M = the number of blocks this study actually has):**

1. **Warm-Up & Identity** phase — the broad, non-priming opener.
2. **Core** — **one block per topic area / task** from the approved Row-7 topics/tasks list, branched by study type (see 2a): IDI narrative probes, usability think-aloud task blocks, concept first-impressions/comparison, diary entry-review follow-ups, or focus-group turn-taking. Each Core topic/task is its own labeled step so the researcher approves the questions for that topic before the next. **When the Say-Do Gap module is Included (Section 1, Row 8), each affected Core block's draft must carry the visible `**Say-Do Gap Probe:**` prose line** (see the OUTPUT TEMPLATE note) — this is what the researcher approves and what makes Include vs. Skip visibly different in the delivered guide.
3. **Optional Stimulus / Concept phase** — include this block only when Row 10 (stimuli handling) applies.
4. **Wrap-Up** — surprise/reflection, one-thing-to-change, open floor, close.

The fixed scaffolding — breadcrumb, RACI header, parameter table, Pre-Session Checklist, Consent + Recording script, and Post-Session Debrief — is assembled automatically around the approved blocks (the Consent script is read verbatim, so it is shown for confirmation, not re-drafted). Show the scaffolding alongside the first content block so the researcher sees the whole shape.

**Whole-draft override:** if the researcher explicitly asks for the full guide at once instead of block-by-block, skip the per-block pop-ups but still show the complete assembled draft for a single approval, keep the confirmed destination, and perform every Section 3 and verification step. Default to block-by-block unless they ask.

### Quality-gate announcement (say this after the last content block is locked)

Once all content blocks are approved, tell the researcher exactly what happens next so they know what to expect:

> All blocks are approved — I now have everything I need. Here's what I'll do before I hand you the final guide:
>
> 1. **Run a critique pass** — the self-critique audit below pressure-tests the guide for methodology gaps, biased phrasing, and weak probes.
> 2. **Run the multi-agent review** — several independent reviewers check the guide for inconsistencies and problems in parallel.
> 3. **Then I'll produce your moderation guide** — the formatted, verified Google Doc in your confirmed Drive folder.
>
> Running the critique and multi-agent checks now — I'll fold in any fixes before the Doc is created.

The moderation guide (the final Google Doc) is drafted **last**, after both checks. The expected sequence is **approved blocks → self-critique → multi-agent → fixes → create the Google Doc → share.** Never describe the guide as final before both checks have run.

### Assembly

Apply the researcher's approved parameters and blocks. For the default layout, follow the OUTPUT TEMPLATE below. Branch the Core section by study type (see 2a). Assemble the approved blocks into the markdown intermediate; the final formatted deliverable is the Google Doc created in Step 6.

**Test/demo/mock-run output:** add the shared `⚠️ TEST ARTIFACT` header line — see `../../references/output-status-and-labeling-conventions.md`. Treat any invocation described as a test, sample, demo, mock, fixture, or pressure scenario as simulated even when the brief sounds realistic; omit the label only when the researcher confirms it is a real study. Keep it prominent, and do not save a demo/mock to Drive, the tracker, or project folders.

**Verbatim-sourcing discipline:** every question, name, and detail in the guide traces to the inputs or the researcher's Section 1/Section 2 answers. Quote source material verbatim where the guide reproduces it (e.g. the participant's own phrasing in a `[recall their phrasing]` placeholder, or a capture-verbatim flag). Do not invent stakeholder names, quotes, or details — mark unknowns `[TBD — fill in]`.

### OUTPUT TEMPLATE (default layout — TABLES = QUESTIONS ONLY)

> **Core principle (codified 2026-05-04 from Diet Personalization mod guide):** When the moderator is sitting in front of a participant, their eye should land on a table that contains **only the words to read or ask aloud**. Probes, watch-fors, tagging guidance, "don'ts," and methodology rationale all live in **prose around the tables**, not inside cells. Total length target: **~5 pages**, not 13.

```
*UX Research | Moderation Guide | [Quarter Year]*

# [Study Title — derived from research goal]

**[Phase or sub-title if applicable, e.g. "Phase 1: Diagnostic Deep Dive (Contextual Inquiry IDIs)"]**

Last updated: [Month Year]

- **Responsible:** [Name] (Role) — use `[TBD — fill in]` if not confirmed in Section 1
- **Accountable:** [Name] (Role) — use `[TBD — fill in]` if not confirmed in Section 1
- **Consulted:** [Names with roles] — use `[TBD — fill in]` if not confirmed in Section 1
- **Informed:** [Names with roles] — use `[TBD — fill in]` if not confirmed in Section 1

| Parameter | Detail |
|-----------|--------|
| **Study Type** | [final] |
| **Duration** | [X] minutes — [warm-up/core/close split in minutes, derived from the % split in Step 2a applied to the final duration, e.g. a 60-min IDI at 10%/80%/10% → "6 / 48 / 6"; add a 4th "probe" bucket carved out of the core-time minutes, not on top of them, only when the Say-Do Gap Module is included] |
| **Format** | [Moderated remote / In-person / Unmoderated], [tools] |
| **Participants** | [profile + screening criterion] |
| **Goal** | [1-sentence research goal — what we're learning, separated by · for multiple objectives] |

---

## Pre-Session Checklist

[Bullet list with ☐ checkboxes — NOT a table. Each item: "category — what to verify"]

- ☐ Participant validated — [screening criterion confirmed]
- ☐ Device — [participant on their own device, app loaded, etc.]
- ☐ [Stimuli / artifacts loaded]
- ☐ Recording armed · consent script ready · observers cameras-off

---

## Consent + Recording Script — READ VERBATIM (~60 sec)

[2-col table. Col 1 = short cue label. Col 2 = exact words to read aloud — no annotations, no moderator notes inside the table.]

| Cue | Read aloud |
|-----|------------|
| **Open** | "Hi [name], thanks for joining. I'm [moderator], a researcher at Instacart." |
| **Purpose** | "I'm here to learn from your experience — no right or wrong answers, nothing being judged. I didn't design any of this, so you can't hurt my feelings." |
| **What we'll do** | "[Concrete description of what's about to happen.]" |
| **Recording** | "With your permission, I'd like to record audio, video, and screen. It stays internal at Instacart. **Is that okay?**" |
| **Confidentiality** | "Your name and any identifying details will be removed before anything is shared internally." |
| **Control** | "About [X] minutes. You can skip any question or end at any time — and you'll still get the incentive." |
| **Open floor** | "Any questions before we start?" |

> Wait for explicit verbal **"yes"** before pressing record. Take 30–60 seconds of small talk after consent before Q1.

---

## Phase 1 — Warm-Up & [Domain] Identity (~[X] min)

[PROSE OUTSIDE TABLE — 1-sentence goal, then probe list, then "Don't" warnings.]

**Goal:** [1-sentence statement of what this phase is for.]

**Probes to use:** Echo · Tell-me-more · Silence (count to 7) · Laddering ("Why is that important to you?") · Critical Incident ("Tell me about the last time…") · Specificity ("What does '[word]' mean for *you*?")

**Don't:** [Things the moderator should avoid — e.g. priming the studied label, mentioning the product by name first, leading framings.]

| # | Ask |
|---|-----|
| **Q1** | "[Open warm-up question — broad, easy, non-priming.]" |
| **Q2** | "[Identity / vocabulary question.]" |
| **Q3** | "[Rules vs. goals question.]" |
| **Q4** | "[Context / surrounding-people question.]" |

---

## Phase 2 — [Core Method, e.g. Contextual Inquiry / Tasks / Concept Test] (~[X] min) — CORE

[PROSE OUTSIDE TABLE — explain what this phase IS, list the categories the moderator silently tags, give the framing rule.]

This is the spine of the study. [1-2 sentences explaining the method and what to silently capture.]

**If the Say-Do Gap Module is Included (Step 3, Row 8):** add a `**Say-Do Gap Probe:**` prose line directly under this phase's goal sentence, naming which of methodology.md §2b's techniques apply to *this* phase's questions beyond the baseline CONTENT GENERATION RULES (rules 4 and 5 — critical-incident phrasing and no-hypotheticals — already apply to every guide regardless of risk flag, so they alone don't count as "the module"). The module's actual incremental content is: grounding questions in an artifact (§2b.2), diary/photo pre-work (§2b.3), directly probing a stated/observed gap non-accusatorially (§2b.4), and the social-desirability counter-moves in §2c (normalize, decouple from identity, third-person framing). This line is what makes Include vs. Skip visibly different in the delivered guide — without it, both settings produce an identical document.

[If applicable, list the silent-tagging categories as ☐ bullets with one-line descriptions.]
- ☐ **CATEGORY 1** — [definition]
- ☐ **CATEGORY 2** — [definition]
- ☐ **CATEGORY 3** — [definition]

### 2.1 [Sub-phase name] (~[X] min)

[Optional 1-line "don't" or "watch for" prose.]

| # | Ask |
|---|-----|
| **Setup** | "[The setup line you say aloud — describe the goal, not the UI.]" |
| **If hesitant** | "[Reassurance line if they push back.]" |

### 2.2 [Sub-phase name] (~[X] min)

[Prose: which probes apply, what the sub-question structure tests.]

| # | Ask |
|---|-----|
| **Q5** | "[Open question for this sub-phase.]" |
| **Q6a** | "[Probe sub-question.]" |
| **Q6b** | "[Probe sub-question.]" |
| **Q6c** | "[Probe sub-question.]" |

[Repeat 2.X subsections as needed. Each one: 1-2 lines of prose ABOVE the table, table BELOW with question rows only.]

### 2.5 [Final sub-phase, often a Say-Do or reconciliation step]

[Prose: framing rule — "never accuse, never imply contradiction is wrong" / "watch for whether they reframe identity vs. behavior" — these stay OUT of the table.]

| # | Ask |
|---|-----|
| **Q12** | "[The reconciliation question, including any [recall their phrasing] placeholders.]" |
| **Q12 follow-up** | "[Optional follow-up question.]" |

---

## Phase 3 — [Optional stimulus / language test phase] (~[X] min)

[Prose: setup, time-management call ("if Phase 2 ran long, cut from 5 to 3"), what to capture verbatim.]

| # | Ask |
|---|-----|
| **Setup** | "[Stimulus introduction.]" |
| **Q13** | "[First-impression question.]" |
| **Q14** | "[Trust / friction question.]" |
| **Q15** | "[Reframe / rewrite question.]" |

---

## Phase 4 — Wrap-Up (~5 min)

| # | Ask |
|---|-----|
| **Q16** | "[Surprise / reflection question.]" |
| **Q17** | "[One-thing-to-change question.]" |
| **Q18** | "[Open floor.]" |
| **Close** | "Thank you so much — [study-specific gratitude]. [Confirm incentive + next steps.]" |

---

## Post-Session Debrief

[Numbered list, NOT a table. Within 5 min of session end, capture three things while memory is fresh.]

1. **[Primary classification field]:** ☐ [Option A] · ☐ [Option B] · ☐ [Option C] · ☐ Mixed
2. **[Secondary judgment field]:** ☐ [Option A] · ☐ [Option B] · ☐ Ambiguous — plus one-line rationale
3. **Most diagnostic verbatim quote:** one sentence, exact words from the participant
```

**IMPORTANT:**
- The guide MUST end at Post-Session Debrief. Do NOT add Master Probe Bank, Bias Mitigation Checklist, Self-Critique Audit, or a pilot reminder inside the guide document itself. Those live in `references/mod-guide-methodology.md` for the moderator to consult separately, or — for the pilot reminder specifically — get delivered as one line in the Step 6 chat summary alongside the doc link (see Step 4.5 Part 4 "Pilot reminder" and Step 6.3 item 1). Never inside the guide's own pages.
- **Tables contain ONLY questions / read-aloud lines.** Probes, watch-fors, tagging guidance, "don'ts," and methodology rationale ALWAYS live in prose above or below the table — never inside cells.

---

### FORMATTING RULES (visual + structural)

#### Structural
- **Tables = questions only.** Col 1 = short label (`Q1`, `Q2`, `Setup`, `Open`, `Cue`). Col 2 = the exact words the moderator reads or asks aloud.
- **Probes, watch-fors, "don'ts," tagging guidance, methodology rationale → prose ABOVE the table.** One sentence per concept where possible.
- **Use `>` blockquotes** for one-line moderator reminders that follow a table (e.g. "Wait for explicit verbal 'yes' before pressing record.").
- **No `<br><br>` line breaks inside table cells.** Each cell holds one short scannable line. If a question has multiple parts, split into separate rows (`Q12`, `Q12 follow-up`) or sub-questions (`Q6a`, `Q6b`, …).
- **Pre-Session Checklist and Post-Session Debrief are bullets/numbered lists, NOT tables** (they aren't questions).
- **Total target length: ~5 pages.** If the guide exceeds 7 pages, cut moderator-note paragraphs and redundant explanation.
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

### Part 1 — Methodological Audit (Structure & Flow)

| Dimension | What "Good" Looks Like |
|-----------|------------------------|
| **Opening rapport & consent** | Warm, non-clinical opening. Explicit recording consent before recorder starts. Participant knows purpose, duration, confidentiality, right to skip/stop. (AIxUXR §Prompt A "Introduction & Consent"; NN/g Fessenden) |
| **Four-phase structure** | Intro (5-10%) → Warm-up (10-15%) → Core (60-70%) → Wrap-up (5-10%). Times displayed per section. (AIxUXR §Prompt A "Calculate and Allocate Time") |
| **Funnel technique within Core** | Broad "Grand Tour" question first, then specific-incident probes, then closed clarifiers. No priming by leading with the narrow question. (AIxUXR §Prompt A.3; NN/g Rosala "Funnel Technique") |
| **Time budgeting** | Per-topic minutes allocated; Core gets 60-80% of total. Warm-up not eating Core. Wrap-up protected. (AIxUXR §Prompt A.1) |
| **Question sequencing / logical flow** | Each question builds on the last. No abrupt topic jumps without a bridge sentence. Transitions are signposted ("Now I'd like to shift to…"). (AIxUXR §V2 Prompt B Part 2) |
| **Wrap-up dual function** | (a) Verification — "Let me play back the themes I heard…" (b) "Anything else?" open catch-all. (AIxUXR §Prompt B SRQ1.2 "Dual Function of the Wrap-Up") |

### Part 2 — Question Quality Audit (Phrasing & Bias)

| Check | Fail Pattern → Fix |
|-------|--------------------|
| **Leading questions** | ❌ "Don't you find the new checkout faster?" → ✅ "Describe your experience using the new checkout." (AIxUXR §Prompt B example row; NN/g 6 Mistakes) |
| **Hypothetical / speculative** | ❌ "Would you use this?" / "What would you do if…?" → ✅ "Tell me about the last time you…" Reserve hypotheticals for the end as projective tools only. (AIxUXR §Prompt A.4 "No speculative questions"; Portigal) |
| **Closed yes/no framing** | ❌ "Did you like it?" → ✅ "How would you describe that experience?" (AIxUXR §V2 Prompt B; Hall) |
| **Compound / double-barrelled** | ❌ "How easy and enjoyable was it?" → ✅ Split into two questions. (NN/g) |
| **Jargon / insider terminology** | ❌ UI labels, internal product names, acronyms the participant hasn't used → ✅ Plain language matched to participant vocabulary. (AIxUXR §Responsible AI — "Inclusivity of language") |
| **Past behavior anchoring** | Every Core question tied to a concrete, recent incident — not "typically" or "in general." (AIxUXR §Prompt A.4 "Focus on past, concrete behavior"; NN/g CIT) |
| **Inclusivity & cultural assumptions** | Questions don't assume a household structure, income level, cooking frequency, dietary pattern, or tech proficiency. (AIxUXR §RAI "Equity and Fairness") |

### Part 3 — Probing & Moderator Guidance Audit

| Check | What to Verify |
|-------|----------------|
| **Probe quality per question** | Each Core question has 1-2 named probes attached (Echo, Tell-Me-More, Laddering, Silence, Critical Incident). No "naked" questions. (See Probing Taxonomy section.) |
| **Moderator Notes embedded** | `[Moderator Note: ...]` callouts appear at every transition and in at least every Core topic — covering probe strategy, silence, boomerang technique, what to watch for. (AIxUXR §Prompt A.5 "Embed Moderator Notes") |
| **Silence as a tool** | Note reminds moderator to count 5-10 seconds before filling gaps. (NN/g Fessenden; Portigal) |
| **Usability-specific: task framing** | Tasks describe the goal, not the UI ("find a way to…" not "click the red button"). (AIxUXR §Use Case 2 Critical Rule) |
| **Usability-specific: Priming → Expectation → Action → Alignment** | Each task includes the four-part sequence. (AIxUXR §Use Case 4; NN/g) |
| **Concept test: Problem validation before reveal** | Blind-need questions precede the concept reveal to avoid biasing desirability. (AIxUXR §Use Case 3 "The Reveal technique") |

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
2. **Default (portable) path — native Google Docs:** create the doc in the confirmed folder with the session's connected Google Docs tools, then apply native Title/Heading/body styles and native tables directly. No `md2doc`, no CLI, no personal script.
3. **Optional Jedida-variant path (only when the researcher opted in and Jedida's local environment is available):** upload via `md2doc`'s `upload-gdoc.py` to the confirmed folder, then apply the chosen variant styler:
   - **Jedida Reporting (navy/blue):** `~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py [doc-id]` — navy NAV H1 nav bars, LBLUE label columns, alternating WHITE/LGRAY rows, DGRAY borders, Calibri throughout, via 4 passes (sanitize → margins → named-style typography → H1 nav bars → tables with snug label column).
   - **Forest-green mod-guide style:** `scripts/apply_canonical_template.py [doc-id]` — clears SUBSCRIPT runs, sets page size + margins, applies run-level typography, styles all 2-col tables (col widths 96/715.5pt, dark-green header with white bold, dark-green bold label col, #161416 content col, 0.5pt #C7C7C7 borders, 8pt padding), sets H2 non-bold with 36pt above / 12pt below, NORMAL_TEXT 4pt spaceBelow + 115% lineSpacing, BULLET_DISC_CIRCLE_SQUARE.
   - **Custom — user-supplied reference doc:** `scripts/apply_custom_template.py [target-doc-id] [ref-doc-id]`. Apply silently — no read-back, no confirmation prompt.
   - **If a variant script crashes or errors at runtime** (missing dependency, auth failure, bad doc ID): do not retry in a loop and do not ask the researcher what to do. Fall back to the native Google Docs default styling, and say so plainly in the chat summary (e.g. "Jedida-variant styling failed [reason] — sharing the doc with native Google Docs styling; let me know if you want me to retry"). The doc and its content matter more than the variant; never block delivery on a styling failure.
4. **Demo/mock runs:** do not create a Drive artifact at all (see Demo-run auto-trigger). Return the markdown draft in chat with the `⚠️ TEST ARTIFACT` label; do not save to Drive, the tracker, or project folders.

### 6.2 Verify and correct

1. Read the created document back (e.g. `get_doc_as_markdown` or the connected Docs read tool).
2. Compare it against every approved block and the parameter header — RACI completeness (`[TBD — fill in]` where unconfirmed), the parameter table, Pre-Session Checklist and Post-Session Debrief as lists (not tables), the Consent script verbatim, and **tables containing only read-aloud lines** (probes/watch-fors/don'ts/rationale in prose, per the domain rule).
3. Confirm the guide **ends at Post-Session Debrief** — no Master Probe Bank, Bias Mitigation Checklist, Self-Critique Audit, or pilot reminder inside the doc.
4. Confirm length is ~5 pages (max 7); if over 7, cut moderator-note paragraphs and redundant explanation.
5. Correct every issue, then read back again. If rendering (PDF/thumbnail) is unavailable, disclose that verification was structural rather than visual.

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
- **Connected Google Docs / Drive tools** — **default (portable) path:** create the guide in the confirmed folder, apply native Title/heading/body styles and native tables, read it back to verify, and return the link. No personal script required.
- **md2doc** (`upload-gdoc.py`) — *optional Jedida-variant* uploader (personal pipeline only).
- **`~/.claude/skills/mod-guide/scripts/apply_jedida_reporting.py`** — *optional Jedida-variant* styler (navy/blue). Requires Jedida's local environment.
- **scripts/apply_canonical_template.py** — *optional Jedida-variant* forest-green mod-guide template (only when the researcher explicitly picks it).
- **scripts/apply_custom_template.py** — *optional Jedida-variant* — extract styling from a user-supplied reference doc and apply it to the target.
- **references/canonical-template-spec.md** — human-readable spec for the forest-green variant (mirrors the values in `apply_canonical_template.py`).
- **references/mod-guide-methodology.md** — load on demand when the researcher asks about a specific probe, bias, or study-type nuance.

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
