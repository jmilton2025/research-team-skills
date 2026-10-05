---
name: mod-guide
description: Use when a UX researcher needs a moderation guide for a moderated user interview, usability test, concept test, diary-study check-in, or focus group. Triggers on "write a moderation guide", "interview guide", "discussion guide", "facilitation script", "/mod-guide", or natural asks like "help me write interview questions", "I need a script for my usability test", "prep questions for these sessions", or "build a discussion guide for this study".
---

# Moderation Guide Builder

Generate a ready-to-facilitate moderation guide for an Instacart UX research session. The skill builds **two structurally distinct guide formats** (chosen first, in Step 2a / Section 1):

- **Prototype / Usability** — bold-label reaction or read/do lists tied to approved stimuli, think-aloud, observation cues, optional ratings, experimental design, and optional vendor back-matter. Covers usability tests and concept tests without forcing a concept-reaction construct into a behavioral task. Template: `references/template-prototype-usability.md`.
- **Interview (IDI-style)** — open questions as nested prose probes in timed thematic blocks, no artifact. Covers in-depth interviews, diary check-ins, and focus groups. Template: `references/template-interview.md`.

Both share one spine (stakeholder header, parameter table, pre-session checklist, post-session debrief) and one delivery pipeline. Consent is format-specific and appears once: a Consent table for interviews, or a read-aloud Introduction list for prototype studies. The methodology is grounded in Steve Portigal, Indi Young, Nielsen Norman Group, Erika Hall, Nikki Anderson, and de-identified lessons from completed team studies.

### Guiding Philosophy — H.E.A.R.T. (from Instacart's AIxUXR Playbook)

Every guide this skill produces — and every session it supports — must uphold the **H.E.A.R.T.** framework. The moderator is the final authority; this skill is a co-pilot, not the driver.

| Principle | What It Means for a Moderation Guide |
|-----------|--------------------------------------|
| **H — Human-centered** | Prioritize the participant's context, comfort, and dignity. Questions serve their lived experience, not our curiosity. |
| **E — Experience-focused** | Every interaction in the session (consent, warm-up, probes, close) must feel intuitive, respectful, and positive. A clunky moderator moment is bad research. |
| **A — Amplifying** | AI drafts the protocol; the human researcher drives strategy, synthesis, and empathy. The guide is a starting point, not a script cage. |
| **R — Responsible** | Proactive about ethics, PII, consent, and bias mitigation — not a box-check. Scrub PRDs/RPPs of PII before pasting. |
| **T — Transparent** | Disclose AI-assisted drafting to stakeholders. Disclose the approved study purpose and any planned recording/observation to participants. Trust is the currency. |

**Source note:** H.E.A.R.T. is the team's responsible AI-assisted research framework. Internal source identifiers are intentionally omitted from this public package.

The researcher is the final authority. Recommend clearly, but never silently lock a study parameter, question, probe, or delivery choice. Ground every parameter and question in the supplied inputs; if a fact is not in the inputs, mark it `[TBD — fill in]` rather than inventing it ("grounded in data, never assumed").

---

## Completion contract

For a real-study run, completion requires all gates 0–6:

0. **The guide format has been chosen** — **Prototype / Usability** or **Interview (IDI-style)** — and the matching template reference has been loaded (`references/template-prototype-usability.md` or `references/template-interview.md`). This is the first Section 1 decision and it forks every downstream step (Section 1 parameters, Section 2 blocks, OUTPUT TEMPLATE). See Step 2a.
1. Non-public sources are authorized for AI processing before access, participant-level data is excluded, and the minimum necessary de-identified inputs have been read. Follow `references/source-and-delivery-safety.md`.
2. The researcher has approved every applicable **Section 1** parameter and every decision-bearing **Section 2** core block. Template-driven surrounding blocks are source-grounded, shown in the assembled draft, and included in the final review — the sequence depends on the chosen format (interview: Objectives → Introduction & Rapport → thematic deep-dives → Wrap-Up → optional Parking Lot; prototype: Objectives → Intro → Background → construct-matched stimulus/task phases → optional Comparisons/Recap → Wrap-Up → optional vendor back-matter).
3. The mandatory baseline safety/method audit has passed. The enhanced multi-agent review has also run when the researcher opted in, with confirmed fixes folded in.
4. The exact Google Drive destination, intended audience, effective permissions, and one authorized partial-artifact recovery path have been confirmed before creation.
5. The guide has gone through the idempotent **create → revision-bound normalize → revision-bound format → readback → render → verify** pipeline. **Option 4 — Leadership** is the default; plain native Google Docs is only an approved and disclosed fallback.
6. A working Google Doc link has been returned with a one-line pilot reminder and verification status.

For a demo, mock, sample, fixture, or pressure test, gates 0–3 apply, followed by a prominent `⚠️ TEST ARTIFACT` Markdown result and no Drive, tracker, or project-folder write. Gates 4–6 are skipped unless the tester explicitly requests a test Doc; then gates 4–6 apply with a confirmed safe destination, permission readback, and the same delivery verification as a real study.

The mandatory baseline audit and any selected enhanced review run before the final Google Doc is drafted. Drive destination confirmation must happen before document creation.

For a real study, Markdown is an intermediate representation, not the completed deliverable. The demo branch above returns labeled Markdown by design.

## Flow overview

| Step | Work | Completion gate |
|---|---|---|
| **1** | Check connections and flag any that need sign-in → establish source authorization/minimization, then gather the de-identified plan, brief, approved notes, or free-form description → announce the 3-section structure | Missing connections flagged in the first message; inputs authorized and received; researcher understands the workflow |
| **2** | Analyze inputs; prepare source-grounded Recommended options for Section 1; run the Say-Do Gap risk check | Recommendations and risk flag prepared for approval |
| **3** | **Section 1 — Study Setup & Parameters:** the consolidated upfront batch of labeled pop-ups. **First question = guide format (Prototype/Usability vs Interview)**, then study title and the shared rows (moderation, duration, participants, profile, topics/tasks/flows, Say-Do, RACI [single confirm/revise]) + the **truly format-specific rows from the matching template reference** (prototype: prototype links/backup, device, experimental design, rating style, delivery model; interview: recruit source, blinded?, conditional blocks, horizon framing). Add Drive destination/audience, partial-artifact recovery, and delivery style only for real runs or explicitly requested test Docs. | Format and title chosen; all applicable parameters approved; real/test-Doc destination and recovery path confirmed or no-Drive demo branch locked; researcher says "Section 1 locked" |
| **4** | **Section 2 — Guide Content:** show the template-driven surrounding content and obtain draft-first approval for each decision-bearing core block, using the matching template sequence | Core blocks approved; required template blocks present in the assembled draft |
| **4.5** | **Section 3 —** always run the baseline safety/method audit; offer the enhanced two-reviewer panel; route meaning-changing fixes through the planned approval gate | Material fixes approved; affected audit rows pass; panel result folded in when selected |
| **5** | Run the enhanced multi-agent review only when selected and authorized | Review complete or disclosed as skipped/unavailable; change control complete |
| **6** | For a real study or requested test Doc, preflight capabilities and Drive ACL; create once; apply revision-bound Option 4 batches; read back content, parent, and permissions; render and verify. For a no-Drive demo, return labeled Markdown after Section 3. | Selected delivery branch passes its completion contract |

## Portable Google Docs contract

The skill must work for any researcher with a write-capable Google Docs integration.

- **Option 4 — Leadership is the default deliverable look**, applied by the bundled `scripts/option4_guide_layout.py` formatter against `references/option4-guide-style.json` using connected Google Docs / Drive tools. Plain native Google Docs is an explicit choice or a pre-approved, disclosed fallback.
- Do not depend on a personal template, custom font beyond the bundled Option 4 contract, private reference document, hardcoded folder ID, personal styling script, command-line utility (gws/gohan), or researcher-specific authentication setup for a real run to succeed. The Option 4 formatter is bundled with the skill and portable; it is not a personal dependency. When `gws` is the researcher's only Docs write route, the formatter's `send` command can use it after the Section 1 write-route approval; it is never required.
- Confirm the exact Drive destination, intended audience, effective permissions, and authorized partial-artifact recovery path before creating any doc. Never write to a hardcoded personal folder or broaden sharing silently. Follow `references/source-and-delivery-safety.md`.
- If no write-capable Docs integration is available, preserve the approved markdown draft and report that the required deliverable is blocked. Do not call the markdown output final.

## Interaction contract

Use native `AskUserQuestion` checklist pop-ups when available.

- Ask one decision per pop-up. (Section 1's upfront setup may still batch up to 4 of these decisions per `AskUserQuestion` call — each decision is still labeled and answered individually within the batch.)
- **Use `multiSelect: true` only when 2–3 independent items can legitimately apply**, such as a short topics/tasks list. Use a single confirm/revise choice for longer sets and for RACI as one coherent assignment. Keep single-select for exclusive choices such as duration, study type, moderation style, Say-Do module, stimuli handling, phase/scope, destination confirmation, and styling.
- Number the options. Mark a **Recommended** option based on the inputs and discovered evidence — it is the source-grounded choice prepared internally in Step 2.
- Preserve the built-in **Other / comments** field so researchers can add, correct, or rewrite (including custom durations, participant counts, or a Drive folder URL).
- Show the proposed content before asking for approval.
- **The last option in every pop-up must be "Brainstorm with me"** — this opens a short chat exchange on that specific item, then re-shows the revised draft for approval before advancing. Never bury it mid-list. The one exception is the yes/no **Google Docs write route** approval in Section 1.
- Label every pop-up with its section and step: **"Section 1 > Step 3 of 10: Duration"** / **"Section 2 > Step 2 of 5: Core — Task Flow"**. The researcher must always know exactly where they are.
- Native `AskUserQuestion` allows **at most 4 questions per call and 4 options per question**, including "Brainstorm with me," and cannot pre-select. Therefore each question has one Recommended option, at most two alternatives, then "Brainstorm with me." For more than three drafted items, use a single "Accept the drafted set" option plus revise/add alternatives; never drop items or imply they were pre-selected. Keep dependent rows in separate batches and order them after their prerequisites.
- Do not advance until the current item is approved, unless the researcher explicitly requests the whole-draft approval override in Step 4.

If native pop-ups are unavailable, state **"Inline fallback — native checklist unavailable in this environment"** and reproduce the same numbered options, labels, and selection instructions in chat. Do not silently substitute an unlabeled prose question.

---

## Step 1 — Gather Study Inputs & Orient the Researcher

### Connection check — first, before any questions

Start the run here. Check each connection the run depends on, with a quick authentication or metadata call rather than trusting the tool list (a listed tool can still ask for sign-in; Claude Code also reports servers that need authentication when the session starts). This connection check must not open or retrieve source content; content access starts only under the source-authorization gate below. If a connector's only tools return content (search or chat, as with most Glean servers), don't run a test query: use the session's sign-in report or its `/mcp` status, and treat the first authorized read as the live check.

| Connection | Needed for |
|---|---|
| Enterprise search (e.g., Glean) | Reading a shared internal plan or brief (Step 1) |
| Google Drive / Docs | Reading shared docs (Step 1); creating and verifying the guide Doc for a real study or requested test Doc (Step 6) |
| `multi-agent-check` skill | The optional enhanced reviewer panel (Step 5); check the live skill list |
| Slack | Shared threads; check only when a Slack link comes up |

**Flag every missing or signed-out connection in your first message**, so the researcher can sign in while you gather inputs instead of finding out halfway through Section 1. That covers every row above except Slack. Name the connection, say what it's for, and give the sign-in steps. Glean is the one most often signed out; for any other connection, use the same steps with its name swapped in:

> **Glean isn't signed in.** I use it to read the internal plan or brief you share. To sign in, type this in Claude Code (the chat box you're using now):
>
> ```
> /mcp
> ```
>
> Pick **glean** (if the list shows more than one Glean entry, such as `glean` and `glean_default`, do this for each one marked as needing sign-in), choose **Authenticate**, finish signing in on the browser tab that opens, then come back and say **done**. On claude.ai, connect it from your connector settings instead. Or say **skip Glean** to continue without it.

Continue with the source-authorization gate and the request for inputs while the researcher signs in; neither needs a connection. When a new source type comes up later (a Slack thread, say), check that connection the moment it's mentioned and flag it the same way. Re-check right before reading a shared source: if its connection is still missing, wait for sign-in or an explicit skip; after a skip, ask for the minimum necessary content to be pasted instead. Missing Docs write access matters only for a real study or requested test Doc, which then ends with a blocked draft; missing `multi-agent-check` means the enhanced panel is unavailable, and the baseline audit still runs.

### Source authorization and inputs

Before opening or using non-public material, apply `references/source-and-delivery-safety.md`: confirm the researcher's authority and approved AI processing, source audience, minimum necessary content, and redaction. Do not request participant-level data. Pasting or attaching content does not establish the requester's authority or approved AI-processing status; apply the same gate before using pasted non-public material.

Ask the researcher to paste or share the de-identified study inputs. Say:

> "To build your moderation guide, share the de-identified study plan, brief, approved notes, or a plain-English description. Please leave out participant names, contact details, schedules, and recording links. **For a usability/prototype test, include the approved prototype link or a description of the flows.** I'll extract the parameters, recommend the guide format, and build from there."

**Accept any de-identified format:** plan, brief, approved notes, or verbal description. For a shared Google Doc URL, complete the source-authorization gate before reading it. If no authorized reader is connected, ask for the minimum necessary content to be pasted instead.

### Orientation announcement

Once the inputs are in hand, before asking any parameter questions, say in chat:

> Now that you've shared your inputs, I'll pull out the study parameters, then we'll build this moderation guide together — one step at a time.
>
> **We'll work in three sections:**
>
> **Section 1 — Study Setup & Parameters** *(the decisions that shape the guide)*
> **Guide format (Prototype/Usability or Interview) — first** · Study title · Moderation style · Duration · Participants · Profile · Stakeholders (RACI) · then the parameters specific to your chosen format · for a real study or requested test Doc, Drive destination/audience · partial-artifact recovery · delivery style
>
> **Section 2 — Guide Content** *(what the moderator will actually read)*
> Built from your format's template — an **interview** guide runs Objectives → Intro & Rapport → Themes → Wrap-Up; a **prototype/usability** guide runs Objectives → Intro → Background → Task Flows → Wrap-Up
>
> **Section 3 — Quality Gate & Delivery** *(check, then produce)*
> Mandatory safety/method audit → optional enhanced reviewer panel → either labeled no-Drive TEST ARTIFACT Markdown (demo/test) or the formatted, verified Google Doc in a permission-checked Drive folder
>
> For each step I'll show you what I've drafted — you can accept it, pick what to keep, or brainstorm with me to refine it. We move to the next step only after you approve the current one.
>
> Starting with **Section 1 — Study Setup & Parameters.** Analyzing your inputs now…

This is the one planned questioning phase. There are no *unplanned* pop-ups: every pop-up the researcher sees belongs to one of these three announced sections. (This replaces the old "generate the whole guide silently" stance — see the reframed rule in Step 3.)

---

## Step 2 — Analyze and Propose Structure

Analyze the inputs and prepare Recommended options for Section 1. Extract directly from the source material; do not invent details or show a redundant recommendation table.

### 2a. Guide Format Selector (THE top-level fork — determines the whole template)

**The skill produces two kinds of moderation guide, and they are structurally different documents.** Every downstream step (Section 1 parameters, Section 2 blocks, OUTPUT TEMPLATE, verification) branches on this choice. Pick the format **first**, load its template reference, and build from it:

| Format | Load this reference | Body shape | Anchored to | Use when |
|--------|--------------------|-----------|-------------|----------|
| **Prototype / Usability** | `references/template-prototype-usability.md` | Bold-label reaction or read/do lists tied to approved stimuli; observation cues remain prose outside the lists | An artifact — Figma/live product/screens | The participant **reacts to, interprets, compares, or uses** a design under test |
| **Interview (IDI-style)** | `references/template-interview.md` | Open questions as **nested prose bullets** in timed thematic blocks — no body tables | Nothing — the conversation *is* the session | The participant **talks** — recounts experience, opinion, mental model |

**How the choice is made:** always **ask the researcher explicitly** (this is the first Section 1 question — see Step 3). Do *not* silently auto-select. You may still *recommend* a format from the input signals below, but the researcher confirms it.

**Decision signals (to set the Recommended option):**
- → **Prototype/Usability** when inputs include a prototype/Figma link, mockups, screens, or an on-device/on-cart stimulus; words like *usability, concept test, first impression, reaction, comprehension, task, flow, walkthrough, click, can they complete X, where do they get stuck*; a design under evaluation (especially multiple variants); or counterbalancing is a concern.
- → **Interview** when there is **no artifact** — just topics/themes to discuss; or goals phrased as *understand why / how they feel / their experience / their mental model / their vision*; or participants recruited to talk about a domain; or future/landscape/opinion studies.
- **Tie-breaker:** a testable artifact plus an approved reaction, comprehension, comparison, or "can they do X" construct → Prototype. Purely "learn what they think and why," no artifact → Interview. A short warm-up interview *inside* an artifact-based session does **not** make it an interview guide.

> **⚠️ Interview requested for a prototype-shaped plan (live-test finding, 2026-10-02):** if the researcher asks for an interview guide but the source plan's *Method & approach / Stimuli & protocol* define artifact-based tasks (prototype sessions, order comparisons, think-aloud tasks), the plan's hypotheses **cannot be answered by a talk-only guide**. Name the mismatch explicitly and offer exactly two paths: **(a)** build the prototype guide the plan specifies (per the tie-breaker above), or **(b)** reframe the guide as a **separate pre-prototype discovery round** — its own goal ("ground the premises behind the plan's hypotheses"), its own timeline/dates in the parameter table (not the plan's session dates), an interpretation limit stating that testing the module itself needs the plan's prototype sessions, and a note that the plan's method/timeline rows need amending to match. Never silently ship a talk-only guide carrying the plan's session dates and hypotheses as if it could test them.

**Where the old 5 study types land:** *Usability Test* and *Concept Test* (artifact-driven; task-led or reaction-led by construct) → **Prototype/Usability**. *In-Depth Interview (IDI)*, *Diary Study Check-in*, and *Focus Group* (conversation-driven) → **Interview**. Automatically load `references/mod-guide-methodology.md` §3 for concept tests, diary check-ins, and focus groups; those subtypes need their specific reveal, entry-review, or turn-taking rules.

**Time split (applied to the confirmed duration):**

| Format / study type | Time Split |
|---------------------|-----------|
| Prototype — Usability Test | 5% intro / 5% background / 75% tasks / 15% wrap (four buckets — the prototype parameter table wants intro/background/tasks/wrap separately) |
| Prototype — Concept Test | 5% intro / 10% background / 70% stimulus/reaction phases / 15% wrap |
| Interview — IDI | 10% intro+warm-up / 80% core (themes) / 10% wrap |
| Interview — Diary check-in | 15% / 70% / 15% |
| Interview — Focus Group | 15% / 70% / 15% |

Rationale: time splits follow NN/g's qualitative usability testing study guide and Rosala's interview-guide conventions.

### 2b. Skip the recommendation table — go straight to Section 1 pop-ups

**Do NOT show a "Based on your inputs, here's what I recommend" summary table.** After analyzing the inputs internally, go straight into the Section 1 `AskUserQuestion` pop-ups (Step 3). The extracted parameters inform the Recommended options in each pop-up — they do not need to be shown as a standalone table first.

**Hand-off to Section 1 (Step 3):** immediately after Step 2a/2c analysis, launch the first Section 1 `AskUserQuestion` batch in the same turn. No intermediate table, no interim summary in chat.

### 2c. Say-Do Gap Risk Check

Flag **High** if the study asks *only or mostly* about stated behavior, preferences, or intent rather than observable action — e.g., "how often do you cook at home?", "would you pay for this?", "do you read ingredient labels?" (see references/mod-guide-methodology.md §2a for the full signal list). Flag **Low** if the study is a usability test or otherwise observes actual behavior with a planned follow-up (§2a). Flag **Medium** for everything in between — e.g. a study that's mostly observational (usability, contextual inquiry) but includes a handful of stated-preference or frequency questions alongside the core task-based content.

**Effect on the generated guide:** both **Medium and High** automatically include the **conversational** Say-Do Gap techniques (neutral incident gates, non-accusatory gap probes, and §2c social-desirability counter-moves) — Medium studies apply them only to the relevant stated-preference questions. Only **Low** skips the module entirely. This also sets the Recommended default for Row 8 in Step 3: Medium/High → Recommended = Include; Low → Recommended = Skip. **Diary/photo pre-work and participant artifact collection are off unless the approved plan and protocol explicitly define** the collection, participant permission/consent, transfer channel, audience/access, and retention/deletion.

Source: NN/g "Why User Interviews Fail" — *"Interviews do not produce reliable data about user behavior."* Indi Young's listening sessions also warn: people reconstruct rather than report.

### 2d. Build the internal source crosswalk

Before drafting, map every approved plan objective, research question, and supplied hypothesis to at least one guide block. For prototype studies, every supplied objective, RQ, or hypothesis maps to a required, **construct-matched evidence-collection element**: completion, discoverability, navigation, and use → executable task plus observation cue; comprehension, reaction, recall, relevance, desirability, trust, preference, and comparison → required neutral prompt, plus a P8 first-impression prompt only at approved first exposures. Split mixed constructs. **Never convert a reaction, recall, comprehension, or desirability hypothesis into an invented behavioral task.** If no valid guide item can test the construct, flag a method mismatch and block coverage approval. For interviews, every objective maps to an open question. Preserve the plan's sample, timeline, cohorts, stimuli, recording/privacy commitments, and ownership exactly. Mark any requested deviation as a proposed plan amendment and obtain approval in the relevant Section 1 decision. The crosswalk is a working audit artifact, not a section in the delivered guide.

---

## Step 3 — Section 1: Study Setup & Parameters (CONSOLIDATE ALL PARAMETERS UPFRONT)

Section 1 is the consolidated upfront batch: every study parameter is decided here, in one place, before any guide content is drafted. Keep this consolidate-decisions-upfront design — it is what makes the rest of the flow predictable.

### 🚫 ZERO *UNPLANNED* QUESTIONS RULE (read this first)

The old version of this skill forbade **all** questions after the parameter batch and generated the whole guide silently. That is no longer the design. The design now is **step-by-step everywhere**: Section 2 walks the guide content in draft → approve → lock pop-ups, and Section 3 announces the quality gate. Those pop-ups are **planned, pre-announced phases** the researcher was told about in the Step 1 orientation — they are not mid-flow surprises.

So the rule is: **zero *unplanned* questions.** That means:

- Every pop-up must belong to one of the three announced sections (Section 1 parameters, Section 2 content approval, or the Section 3 gate). Do not invent an unannounced clarifying question.
- Resolve only non-material missing details with a safe default. Never default recording/privacy/incentive language, a source authorization, the destination, its audience/ACL, or a plan deviation; use `[TBD]` in the relevant planned decision or stop before the affected access/write.
- Section 3 always runs the baseline safety/method audit. It has one optional enhanced-panel decision; if the panel is selected, that same decision serves as its preflight approval when it states the lenses, sources, audience, and expected runtime. When an audit or panel proposes a meaning-changing fix, Section 3 also has one planned change-approval gate before delivery.
- Re-asking the *same* decision, or asking something the researcher already answered, is the failure mode this skill prevents. Consolidate parameters here; walk content in Section 2; then run the announced Section 3 review and any required change approval.

**The researcher's interaction moments are:** (1) Step 1 — authorize/share inputs, (2) Section 1 — answer the parameter batches, (3) Section 2 — approve the core content blocks, (4) choose whether to add the enhanced panel after the mandatory baseline audit, and (5) when needed, approve meaning-changing audit/panel fixes. Then delivery runs without new questions unless a safety boundary blocks the write.

---

**Hard rule:** Ask the researcher about **every key moderation-guide parameter** through `AskUserQuestion` *before* drafting guide content in Section 2 — even the ones that look "obvious" from the inputs. The point is to give the researcher a chance to **confirm or override** every meaningful design choice in one place. They should walk away from Section 1 feeling like they directed the guide, not received it.

**Guarantees the researcher gets in every popup:**
1. **A Recommended option** — the source-grounded pick appears first, marked `(Recommended)`.
2. **At most 2 alternatives** — real, plausible alternatives; the fourth slot is reserved for "Brainstorm with me."
3. **An editable "Other" field** — the researcher can type a custom value such as "75 min," "N=18," or a Drive folder URL.
4. **"Brainstorm with me" as the last option** — every pop-up ends with this; it opens a short chat exchange on that specific parameter, then re-shows the revised choice for approval before advancing.
5. **A section/step label** — every pop-up is labeled **"Section 1 > Step N of M: <name>"**, where M is the number of applicable parameter questions actually being asked (conditional rows that are skipped don't count).

On real-study runs and explicitly requested test-Doc runs, the final three Section 1 decisions are **Drive destination + intended audience**, **partial-artifact recovery**, and **delivery style**. Keep them separate. Preauthorize exactly one partial-artifact recovery path (trash the verified Doc ID, or restrict and move/retitle it in an exact quarantine folder); if neither path is authorized and supported, block before creation. When `gws` is the only way to write to Google Docs, a fourth decision, **Google Docs write route**, follows delivery style. No-Drive demo/sample/test runs omit all of these decisions and lock the labeled Markdown branch instead.

### Mandatory question set (ask ALL of these — even if extracted from inputs)

The **Select** column says whether the pop-up is `multiSelect: true` (more than one item legitimately applies) or single-select (a genuinely exclusive choice). Every pop-up's last option is **"Brainstorm with me"** and every pop-up is labeled **"Section 1 > Step N of M: <name>"**.

| # | Question | Select | Recommended (Claude's pick) | Alternatives |
|---|----------|--------|------------------------------|--------------|
| **0** | **Guide format** — Prototype/Usability vs Interview (**ALWAYS FIRST, always asked**) | single | The format the Step 2a signals point to (prototype if there's an artifact/task; interview if it's talk-only) | The other format · "Brainstorm with me" — on picking, **load the matching template reference** and pull its format-specific rows into Row 10 below |
| **0A** | **Study title** — the title shown in the guide and used for the Doc | single confirm/revise | Exact source title, or a concise source-grounded draft when none exists | Revise title · Keep `[TBD — fill in]` |
| 1 | **Phase/scope** — which phase or sub-study to build (only if multi-phase plan) | single | The earliest unbuilt phase | Other phases · Both phases |
| 2 | **Study sub-type** (within the chosen format) | single | Interview → IDI / Diary / Focus; Prototype → Usability / Concept — best fit from inputs | The next-best sub-types (skip when only one plausibly fits) |
| 3 | **Moderation style** | single | Source-grounded choice: Moderated remote or Moderated in-person | The other moderated mode; use Other for a specific platform/location |
| 4 | **Duration** (session length — exclusive) | single | Extracted minutes or method-appropriate default | The two method-appropriate alternatives that best fit the chosen subtype; use Other for a custom duration |
| 5 | **Number of participants** | single | Extracted N or method-appropriate default (IDI N≈12, usability N≈5–8, concept/focus N≈8–12) | Smaller / larger options |
| 6 | **Participant profile** | single | Extracted screen criterion | Looser / tighter alternatives |
| 7 | **Key topics / tasks / flows** | multi only for 2–3 items; otherwise single confirm/revise | The complete extracted set | Remove/reorder · Add/reframe |
| 8 | **Say-Do Gap module** | single | Include / Skip / Let Claude decide — Recommended depends on Step 2c risk flag (usually **Include** for interviews on stated behavior; usually **Skip** for prototype tests, which observe behavior) | The other two |
| 9 | **Stakeholders (RACI)** | single confirm/revise | Confirm as shown: the complete assignment, using only names the researcher gave in this run; `[TBD — fill in]` for a role they leave blank | Add more people (corrections go in the comments field) |
| 10 | **Recording, observation, privacy, and incentive language** | single confirm/revise | Exact approved plan/ResOps protocol; `[TBD — confirm ResOps standard language]` for unknowns | No recording/observers · Revise approved protocol |
| 11 | **Format-specific rows** — pull from the loaded template reference (Rows 7–10 are shared; don't re-ask them) | varies | **Prototype:** delivery model · prototype link(s) · backup · device · experimental design · rating style · feedback-then-task. **Interview:** recruit source · blinded? · conditional blocks · horizon framing | Each row's own alternatives, per the reference |
| **FINAL-2** | **Drive destination + intended audience** | single confirm/revise | Exact authorized folder and audience | Choose another authorized folder · Brainstorm |
| **FINAL-1** | **Partial-artifact recovery** | single | Source-authorized trash-by-ID or exact permission-checked quarantine folder | The other authorized path · Block creation until a path is authorized |
| **LAST** | **Delivery style** | single | Option 4 — Leadership with pre-approved plain-native fallback | Strict Option 4 — Leadership (block if unavailable) · Plain native Docs |
| **ROUTE** | **Google Docs write route** — only when `gws` is the only way to write to Google Docs | single, no Brainstorm | Use the helper | Don't create the Doc |

**Row 9 (Stakeholders): Ask the researcher for the RACI instead of looking people up.** The researcher knows who is on the study today, so asking is faster and more accurate than a search. Pre-fill a role only with a name the researcher has given in this run: in the plan, brief, or notes they shared, or in their answers so far. Don't run a people or directory search, and don't carry names over from memory or older project files.

1. **Key people first.** If any of the four roles has no name yet, ask for it in chat before the Section 1 batch that holds Row 9, one name per role: Responsible (usually the researcher), Accountable (the decision owner), Consulted, and Informed. For Responsible and Accountable, also ask for each person's role.
2. **Confirm once.** Show the complete RACI in chat, then ask Row 9 with the options **"Confirm as shown (Recommended)"**, **"Add more people"**, and **"Brainstorm with me"**. Corrections go in the comments field.
3. **Then offer more people.** If the researcher picks "Add more people," collect the extra names and roles in chat (a role can hold more than one name), then show the updated RACI in chat and ask them to reply **confirm** or correct it. This finishes the same Row 9 approval; don't show the pop-up again.

**Row 0 (Guide format) is NEVER skipped — it is always the first question.** Rows that may be skipped, and only under these exact conditions:
- **Row 1 (Phase/scope)** — skip only when the inputs describe a single-phase study with no sub-studies.
- **Terminology note (Row 1):** "Phase" here means a study *sub-phase* — e.g. a diagnostic wave followed by a validation wave within this one study — not the RPP's "Phase 1–5" process-stage grid (Plan/Recruit/Fieldwork/Synthesis/Readout) in the Research Timeline header. Same word, different meaning — don't conflate the two.
- **Row 2 (Study sub-type)** — skip only when exactly one sub-type plausibly fits the chosen format (e.g. inputs unambiguously describe a standard IDI).
- **Row 8 (Say-Do module)** — for a prototype/usability guide this is usually Skip (the session observes behavior); ask it only when the prototype study also collects meaningful stated-preference data.
- **Row 11 (Format-specific rows)** — governed by the loaded template reference; ask every applicable row it defines, and skip only the ones the reference marks optional.

**Never fabricate a stakeholder name.** If the researcher hasn't given a name for a role, use `[TBD — fill in]`.

(The final destination, recovery, style, and write-route rows are skipped on demo/sample/test runs, which create no Drive artifact by default.)

**Every other row must be asked**, even if the answer seems obvious from the inputs. The researcher confirming an extracted value is the whole point. Never skip a row just because you think you know the answer.

### Multi-cohort studies (comparison-cohort branching)

When the research plan specifies more than one cohort (e.g. an "abandoner" cohort vs. a "non-abandoner" comparison cohort — the same contrastive-design pattern the upstream `/research-plan` skill supports), don't leave per-cohort differences to be improvised inline. Label any Section 1 question or Section 2 theme/phase that diverges per cohort with an explicit `(Cohort A) / (Cohort B)` suffix (or however many cohorts exist) — e.g. "Theme 2 (Cohort A)" / "Theme 2 (Cohort B)".

**For a prototype/usability guide the cohorts often see *different stimuli or task flows*, not just differently-worded questions** — a between-subjects design (Section 1 Row P6). In that case the `(Cohort A)/(Cohort B)` label goes on the **flow/stimulus assignment** itself (which prototype variant or flow each cohort runs), and the cohort labels must be the same structure as the P6 experimental design and its counterbalance grid — one coherent scheme, not two unrelated mechanisms. State the per-cohort stimulus/flow assignment once, up top, alongside the experimental-design note.

### Batching rules

`AskUserQuestion` accepts up to 4 questions per call. Count applicable rows to set M in each "Section 1 > Step N of M" label. Batch up to four independent questions, but keep dependent rows in a later batch.

For a real study, or a demo/test run whose tester explicitly requested a test Doc, the final sequence is **Drive destination + audience**, **partial-artifact recovery**, then **delivery style**, plus **Google Docs write route** when it applies. Never combine these decisions; all of them must be locked before Section 2 drafting begins.

For a demo/test run on the default no-Drive path, omit all three decisions, end Section 1 with the last applicable study parameter, and lock the labeled Markdown delivery branch before Section 2. No destination, recovery, or style approval is required because no Doc will be created.

### How to phrase each question

For every question, structure the popup like this:

- **Question text** — short, plain English, ends with a "?". Example: "How long should the session be?"
- **Header chip** — ≤ 12 chars (`Duration`, `Participants`, `Study type`).
- **Option 1** — `(Recommended)` label suffix, with the Claude-picked value plus a brief description of *why* it was picked.
- **Options 2–3** — at most two alternatives with brief tradeoffs.
- **Final option** — "Brainstorm with me."
- "Other" is auto-added — never include it manually. The researcher uses it to type custom values.

### 🎬 Demo-run auto-trigger (skip destination, recovery, and style)

**If this is a demo / sample / test run, do not ask destination, recovery, or style.** Create **no** Drive artifact and return the labeled Markdown test artifact. The only exception is an explicit request to create a test Doc; then confirm a safe destination, permissions, recovery path, and style before writing.

**A run counts as a demo when** the invocation contains a clear demo/sample/test signal — e.g. "demo", "sample run", "test this skill", "show me how this works", "just demoing", "dry run", or an equivalent phrase indicating it's a walkthrough rather than a real study deliverable. (This is the same signal class as `feedback_sample_runs.md`, which also means: do NOT save the output to project folders, the tracker, or Drive.)

**Effect on Section 1 batching:** drop the final rows (three, or four with the write route) and reduce M to match. All other parameter rows still run so the demo exercises the skill.

**Real (non-demo) runs:** ask all three final questions, plus the write route when it applies.

### Final destination, recovery, and delivery questions

**Destination + audience (final-2):** state the exact proposed Drive folder and intended audience. The researcher confirms it or pastes another authorized folder URL in Other. This is destination intent only; Step 6 still performs a fresh effective-permissions read before creation.

**Partial-artifact recovery (final-1):** show only source-authorized, capability-supported choices: trash the verified Doc ID, or restrict and move/retitle it in an exact permission-checked quarantine folder. If neither is available, the only valid choice is to block creation until one path is authorized.

**Delivery style (last):**

- **Option 4 — Leadership with pre-approved plain-native fallback (Recommended):** apply and verify the bundled green leadership contract; if an Option 4-only capability is unavailable, use plain native Google Docs and disclose the fallback.
- **Strict Option 4 — Leadership:** block before creation when any required capability is unavailable.
- **Plain native Google Docs:** native styles and tables, no Option 4 styling.
- **Brainstorm with me.**

**Google Docs write route (only when it applies):** before this row, check which Docs write route the run will use, with a capability or sign-in check that reads no content (`references/source-and-delivery-safety.md` §2). If a connected Docs tool takes the native Google Docs batch requests unchanged, bound to `writeControl.requiredRevisionId`, as a request-body parameter, use it and skip this row. A connector edit tool with its own simplified operation format or no revision binding does not count, even when its create, read, and trash tools work. If `gws` is the only way to write, ask once, labeled **"Section 1 > Step N of M: Google Docs write route"**, with no "Brainstorm with me" option. Say: *"Your Google Docs tool (`gws`) can't read edits from a file, so a bundled helper passes each batch of edits to it directly. While each batch is sent, other programs on this computer could briefly see it."* Offer **"Use the helper (Recommended)"** and **"Don't create the Doc"**. If they decline and no other route exists, Step 6 blocks before creation and the approved guide is returned as a blocked draft.

---

## Step 4 — Section 2: Guide Content (DRAFT-FIRST, ONE BLOCK AT A TIME)

With Section 1 locked, build the guide **content** collaboratively, one block at a time. Use the matching transition:

- **Real study or explicitly requested test Doc:** *"Section 1 is locked — all parameters are set, and the destination, partial-artifact recovery path, and delivery style are confirmed. Now we'll build the guide content together, one block at a time. I'll show you each block's draft; you accept it, pick what to keep, or brainstorm with me, and we lock it before moving on."*
- **No-Drive demo/test:** *"Section 1 is locked — all applicable study parameters are set, and this test will remain a labeled Markdown artifact with no Drive write. Now we'll build the guide content together, one block at a time. I'll show you each block's draft; you accept it, pick what to keep, or brainstorm with me, and we lock it before moving on."*

### Draft-first block-by-block approval

Show the proposed block content first, then ask the researcher to accept, brainstorm, or edit it. Maintain a visible approved/pending checklist of the content blocks. Re-show revised content after brainstorming and obtain approval before advancing.

Every content pop-up must be labeled with its section and step (e.g. **"Section 2 > Step 3 of 6: Core — Task Flow"**). Announce each transition in chat after a block is locked (e.g. *"Warm-Up locked. Moving on to Core — Motivations."*).

**Select behavior in Section 2:** use `multiSelect: true` only when a block has 2–3 independently selectable prompts. For longer blocks, use a single "Accept this block as drafted" option plus revise/reframe alternatives; never exceed four options. "Brainstorm with me" is always last.

**The blocks, in order — use the sequence from the loaded template reference (M = the number of blocks this study actually has):**

**If the format is Interview** (`references/template-interview.md`):
1. **Objectives** — plain goal bullets (no hypotheses / priority labels). **No pop-up — source-grounded and shown for context.**
2. **Introduction & Rapport** — welcome, session overview, participant control, and transition from the already-completed consent table. **No duplicate recording/privacy promise. No pop-up.**
3. **Background Questions** — topic-adjacent icebreaker questions. Auto-generated from template (use grocery/in-store standard block for store-based studies). **No pop-up, no approval gate.**
4. **Thematic deep-dive blocks** — **one block per theme** from the approved Row-7 list; open questions as nested prose probes; conditional themes flagged "if applicable." **Pop-up for each block.** **When the Say-Do Gap module is Included (Row 8), each affected block's draft carries the visible `**Say-Do Gap Probe:**` prose line** — this is what makes Include vs. Skip visibly different.
5. **Wrap-Up** + optional **Parking Lot** — standard three-question close plus a thank-you: neutral theme playback, open catch-all, and participant questions. **No pop-up, no approval gate.**

**If the format is Prototype/Usability** (`references/template-prototype-usability.md`):
1. **Objectives & Research Questions** — preserve supplied hypotheses and priority labels; never invent them. Keep them separate from the script. **No pop-up — source-grounded.**
2. **Session Flow** — a Phase/Time table whose minutes sum to the approved duration; no counterbalance grid here. **Auto-generated.**
3. **Background & Warm-Up** *(no pop-up, no approval gate)* — simple numbered questions (Q1, Q2, Q3), no table format, no "Probes to use:" header. Observation cues at the end. Auto-generated from template.
4. **Phases (the core)** — **one block per phase / stimulus** from the approved Row-7 list, using the shape that matches the approved construct. A **usability phase** uses Scenario → P8-gated First impression → Expectation → executable Task → Alignment → approved rating. A **reaction-led concept phase** uses Stimulus reveal → P8-gated 5-second First impression → required neutral recall/comprehension prompt → reaction/relevance/desirability prompts → comparison/fit when applicable. Add a task to a concept phase only when an approved objective, RQ, or hypothesis measures observable behavior with the concept. Observation cues and probes stay in prose outside the bold-label list. **Pop-up for each phase.** Concept P8 = Task-only is invalid when an approved objective or hypothesis measures initial recall, comprehension, reaction, or desirability. Usability P8 = Task-only is invalid only when an approved objective or hypothesis measures unaided initial comprehension or reaction. When it is valid, P8 = Task-only means omit every First impression item and leave no placeholder. Never convert a reaction, recall, comprehension, or desirability hypothesis into an invented behavioral task.
5. **Wrap-Up** *(no pop-up, no approval gate)* — standard three-question close plus a thank-you: one reflection, one open catch-all, and participant questions. Auto-generated.
6. **Communication & Deliverables (+ Timeline)** — vendor-run only.

The **shared scaffolding** — `# Moderation Guide`, study title, ownership/RACI, parameter table, Pre-Session Checklist, and Post-Session Debrief — is standardized on both formats. Consent appears once in the loaded template: interview Consent table or prototype Introduction list. Show the scaffolding alongside the first core block.

**Whole-draft override:** if the researcher explicitly asks for the full guide at once instead of block-by-block, skip the per-block pop-ups but still show the complete assembled draft for a single approval, preserve the selected delivery branch (and confirmed destination for real/test-Doc runs), and perform every applicable Section 3 and verification step. Default to block-by-block unless they ask.

### Quality-gate announcement (say this after the last content block is locked)

Once all content blocks are approved, run the mandatory baseline audit in Step 4.5. Then ask whether to add the enhanced two-reviewer panel:

> "The required safety and methodology audit is complete. Would you also like the enhanced two-reviewer panel before I finalize the deliverable? It sends the minimum necessary de-identified guide and approved source excerpts to an Evidence checker and a Stakeholder reader."

Options: "Yes — run the enhanced panel" (Recommended) · "No — baseline audit is enough" · "Brainstorm with me"

The baseline audit is never skippable. Run the panel only when selected and reviewer access is authorized.

The final sequence is **approved blocks → mandatory baseline audit/candidate fixes → optional panel/candidate fixes → material-change approval + affected-audit rerun → delivery**. A real/test-Doc branch then creates once and applies revision-bound style/verification; a no-Drive demo returns labeled Markdown.

### Assembly

Apply the approved parameters and blocks using the selected OUTPUT TEMPLATE. Interview core questions are nested prose bullets; prototype phases are bold-label read/do lists. Tables are limited to the shapes each template explicitly allows. Assemble the approved Markdown intermediate. A real study or requested test Doc continues to the verified Google Doc in Step 6; a no-Drive demo completes as labeled Markdown after Section 3.

**Test/demo/mock-run output:** add the shared `⚠️ TEST ARTIFACT` header line — see `../../references/output-status-and-labeling-conventions.md`. Treat any invocation described as a test, sample, demo, mock, fixture, or pressure scenario as simulated even when the brief sounds realistic; omit the label only when the researcher confirms it is a real study. Keep it prominent, and do not save a demo/mock to Drive, the tracker, or project folders.

**Verbatim-sourcing discipline:** every question, name, and detail in the guide traces to the inputs or the researcher's Section 1/Section 2 answers. Quote source material verbatim where the guide reproduces it (e.g. the participant's own phrasing in a `[recall their phrasing]` placeholder, or a capture-verbatim flag). Do not invent stakeholder names, quotes, or details — mark unknowns `[TBD — fill in]`.

**Study-period discipline:** Never substitute the current date or month for an unknown study period. Use only a source-approved study period; otherwise retain `[TBD — fill in]`.

### Shared scaffolding (both formats)

Both guide types wrap the **same spine** — header, ownership, parameter table, Pre-Session Checklist, and Post-Session Debrief. Insert exactly one approved consent pass from the selected template.

**The document header is always "Moderation Guide."** Both formats use `# Moderation Guide` as the document title, followed by `## [Study Title]` and `*[Source-approved study period or TBD — fill in]*`. Do not use "UX Research | Research Plan | Q3/Q4 2026" or any breadcrumb format — the doc type is always "Moderation Guide." The ownership block is standardized as full RACI on both.

Populate each RACI field only from the approved Row 9 assignment. For Responsible and Accountable, the first placeholder is the person's name and the parenthetical placeholder is that person's role; fill each one separately from what the researcher gave. Never infer a role from a supplied name, and leave either unknown as the exact `[TBD — fill in]` placeholder.

> **Core principle:** the moderator's eye should land on **only the words to read, ask, or do aloud**. Probes, watch-fors, observation cues, "don'ts," and methodology rationale live in prose around those lines. Interview target **~4–5 pages**; prototype target **~6–8 pages**.
>
> In a **prototype/usability** guide the Introduction and every phase/task, comparison, and recap block are **bold-label lists** (`- **Label:** "line"`), not Cue tables. The only two prototype tables are the Parameter dashboard and Session Flow agenda. Interview guides use prose bullets, with tables only for parameters and consent.

```
# Moderation Guide

## [Study Title — derived from research goal]

*[Source-approved study period or TBD — fill in]*

- **Responsible:** [TBD — fill in] ([TBD — fill in])
- **Accountable:** [TBD — fill in] ([TBD — fill in])
- **Consulted:** [TBD — fill in]
- **Informed:** [TBD — fill in]

[Prototype only — a Links row containing only audience-approved study/prototype links; never participant grids, schedules, biographies, or recording links]

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
- ☐ [Approved recording/observation setup confirmed; omit when not applicable]

---

[FORMAT-SPECIFIC CONSENT + BODY — build from the matching reference]

---

## Post-Session Debrief

[Numbered list, NOT a table. Within 5 min of session end:]
1. **[Primary field — interview: top themes / prototype: per-flow task outcomes]:** ☐ [A] · ☐ [B] · ☐ [C] · ☐ Mixed
2. **[Secondary field — interview: most surprising / prototype: top friction point]:** ☐ … — plus a one-line rationale
3. **Most diagnostic verbatim quote:** one sentence, exact words from the participant
```

### OUTPUT TEMPLATE — the format-specific body

Build the consent and body from the matching reference:

- **Interview** → Consent table → Objectives (plain goals) → Introduction & Rapport → thematic deep-dive blocks → Wrap-Up → optional Parking Lot. Keep participant operations in a separate restricted artifact.
- **Prototype/Usability** → Objectives/RQs (supplied hypotheses/priorities only) → Session Flow → Introduction with consent/think-aloud → Background → construct-matched stimulus/task phases → optional Comparisons/Recap → Wrap-Up → optional vendor back-matter. Only Parameter and Session Flow are tables.

The shared scaffolding above wraps this body identically for both formats.

**IMPORTANT:**
- The guide ends at optional Parking Lot (or Post-Session Debrief) for interview; Post-Session Debrief for internal prototype; or vendor Communication & Deliverables for vendor prototype. Do not add participant logs, Master Probe Bank, Bias Checklist, audit output, or pilot reminder inside the guide.
- **Read-aloud tables contain only participant-facing lines.** Parameter and Session Flow tables contain only their approved metadata. Probes, watch-fors, observation cues, tagging guidance, "don'ts," and methodology rationale always live in prose outside participant-facing tables and read/do lists.

---

### FORMATTING RULES (visual + structural)

#### Structural
- **Interview tables:** only the Parameter dashboard and Consent script. Core questions are nested prose bullets.
- **Prototype tables:** only the Parameter dashboard and Session Flow. Every phase/task is a bold-label read/do list.
- **Probes, watch-fors, "don'ts," tagging guidance, and rationale stay outside read/do lines.**
- **Use `>` blockquotes** for one-line moderator reminders that follow a table (e.g. "Wait for explicit verbal 'yes' before pressing record.").
- **No `<br><br>` line breaks inside table cells.** Each cell holds one short scannable line. If a question has multiple parts, split into separate rows (`Q12`, `Q12 follow-up`) or sub-questions (`Q6a`, `Q6b`, …).
- **Pre-Session Checklist and Post-Session Debrief are bullets/numbered lists, NOT tables** (they aren't questions).
- **Total target length is format-dependent: interview ~4–5 pages (max 7); prototype/usability ~6–8 pages** (task lists + screens push it longer). If a guide exceeds its ceiling, cut moderator-note paragraphs and redundant explanation — never the task/observation content.
- **Comparison-cohort studies:** label each cohort's theme or flow/stimulus assignment consistently with the approved experimental design.

#### Visual

**Default — Option 4 — Leadership:** use `scripts/option4_guide_layout.py` and `references/option4-guide-style.json`: landscape-letter export metadata, DM Serif Display/DM Sans, dark-green H2 bands, native lists, and aligned tables. Verify before delivery.

**Plain-native fallback / explicit choice:** native Title/Heading/body styles and native tables only. Disclose that Option 4 was not applied.

#### Styling pipeline

Run the bundled formatter in place; its visual contract resolves package-relatively. Store Markdown, manifests, fresh snapshots, and batch files in an owner-only private non-repository working directory (for example, a fresh `mktemp -d` directory). The formatter rejects repository paths and group/world-accessible output directories.

---

### CONTENT GENERATION RULES

1. **No leading questions.** Every generative research question is open-ended and non-directional. Closed forms are limited to exact approved consent confirmation, eligibility screening, a one-fact clarifier after an open response, or an approved rating scale; they never elicit the participant's opinion or reasons. (NN/g Rosala — 6 Mistakes)
2. **No interface terminology in tasks.** Describe goals, not UI ("find a way to…" not "click the button to…").
3. **Funnel technique.** Within each topic: broad → specific → optional factual clarifier. Broad first avoids priming; a clarifier confirms one fact and never replaces the open generative question (NN/g).
4. **Specific incidents over typical behavior.** Start with "What is the most recent time, if any, that you…?" After the participant confirms an event, "Tell me about the last time…" beats "How often do you…" and closes the say-do gap (NN/g Critical Incident Technique).
5. **No predicted personal future behavior.** Expert scenario/projective questions may be used late when the construct is future-landscape judgment; "Would you use this?" is not allowed.
6. **No compound or presuppositional questions.** Split independent constructs, and never imply that an event, realization, problem, or opinion occurred.
   - **Neutral incident recipe:** ask `What is the most recent time, if any, that you [behavior]?` If none, ask for the closest relevant experience. Use `Tell me about the last time...` only after the participant or an approved screener confirms that event occurred.
7. **Probes and moderator notes stay outside read/do lines.** Interview probes are nested prose; prototype probes and observation cues are prose outside the bold-label list.
8. **Time-aware.** Allocate per study type (Step 2a). Core gets 70-80% of total. For interviews, every timed heading, including Consent, must sum to the approved duration. Render Consent as its own 1-minute row/heading and Introduction as the remaining post-consent minutes only: a 3-minute opening is `Consent 1 + Introduction 2`, never `Consent 1 + Introduction 3`.
9. **Participant-appropriate language.** Match vocabulary to the participant profile.
10. **Watch-fors and "don'ts" go in prose**, never inside a prototype read/do list or consent table.
11. **Capture-verbatim flags** go in prose above the relevant block.
12. **Traceability.** Every objective/RQ/supplied hypothesis maps to a guide block and, for prototype studies, to the required construct-matched evidence-collection element defined in Step 2d. Never invent a task solely to make the crosswalk look complete.
13. **Protocol fidelity.** Never invent recording, observation, privacy, retention, deletion, clip-sharing, anonymity, or incentive commitments.

---

### PROBING TAXONOMY — QUICK REFERENCE

Reference `references/mod-guide-methodology.md` for the full taxonomy (definitions, examples, sources). In-line names to use in the guide:

| Probe | One-line rule |
|-------|---------------|
| **Echo** (NN/g Fessenden) | Repeat their last phrase with slight interrogatory tone. |
| **Silence** (Portigal, Hall) | Count 5-10. Let them fill the gap — don't rescue. |
| **Tell-Me-More** (Anderson, NN/g) | "Tell me more about that." Evergreen. |
| **Laddering / Why** (Portigal) | "Why was that important to you?" Climb from behavior to value. |
| **Critical Incident** (Flanagan via NN/g) | Start with "What is the most recent time, if any, that you…?" After an event is confirmed, follow with "Tell me about the last time…" |
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

## Step 4.5 — Section 3: Mandatory Baseline Safety & Method Audit

This audit always runs before any optional panel and before document creation. It cannot be skipped. Say in chat: *"Running the required safety and methodology audit now — checking protocol fidelity, coverage, phrasing, and moderator usability."*

Run the assembled guide through this self-contained audit. It combines protocol fidelity, source grounding, methodological review, question safety, and moderator usability.

**How to use:** walk every applicable row, revise, and re-run up to two times. Unresolved authorization, consent/privacy, plan-traceability, or objective/task-coverage failures block creation. Disclose other unresolved limitations in the delivery summary; do not place audit notes inside the guide.

### Post-audit change control

Classify every baseline-audit or reviewer-panel fix before applying it:

- **Non-material:** spelling, grammar, punctuation, or formatting only, with meaning, links, source trace, and approved research behavior unchanged. These may be applied without another approval.
- **Material:** any change to meaning or research behavior, including question/task intent or ordering, timing, scope, participant-facing protocol or consent, objective/hypothesis coverage, source interpretation, or another approved decision. Do not silently fold these changes into locked content.

After the baseline audit and any selected panel, use one planned **Section 3 change-approval** step when material fixes exist. Show a concise before/after diff; show the full revised affected block when the diff lacks enough context. Obtain explicit researcher approval before Step 6, then re-run every affected audit row. If the researcher rejects a required safety, protocol, traceability, or coverage fix, restore the last approved wording and block delivery until the issue is resolved. This is a planned Section 3 gate, not an unplanned question.

**🔀 FORMAT-AWARE — apply only the rows that fit the chosen format.** Each row is tagged **[Interview]**, **[Prototype]**, or **[Both]**. Skip a row tagged for the other format — do NOT flag a correctly-built prototype guide for "missing warm-up questions" or a correctly-built interview guide for "missing task success criteria." Read the **expected phase names and time split from the chosen format's Step 2a row**, not from a hardcoded interview shape: interview-IDI Core ≈ 80%, usability Core (tasks) ≈ 75%, concept ≈ 70%. A prototype guide's "Core" is the Task Flows block; its warm-up is the Background block.

### Part 0 — Safety, protocol fidelity, and traceability

| Check | What to verify |
|-------|----------------|
| **Source authorization/minimization** | Every non-public source was authorized before access; participant-level data is absent; reviewer packets are minimum necessary and de-identified. |
| **Consent/privacy fidelity** | Exactly one format-correct consent pass; no invented recording modality, observer disclosure, anonymity, access scope, clips, retention/deletion, or incentive promise. Unknown language remains `[TBD — confirm ResOps standard language]`. |
| **Plan fidelity** | Sample, timeline, cohorts, stimuli, RACI, and protocol match the approved plan. Any deviation is explicitly approved as a plan amendment. |
| **Coverage crosswalk** | Every objective/RQ/supplied hypothesis maps to a guide block and a required construct-matched evidence-collection element. Behavioral constructs map to executable tasks; reaction/comprehension/desirability and other attitudinal constructs map to required neutral prompts. No optional wording makes required evidence skippable, and no invented task changes the construct. |
| **Restricted operations data** | No participant schedule, biography, contact detail, recording link, or session-summary link appears in the guide. |
| **Required section inventory** | The selected template's required sections are all physically present before phrasing review. Interview includes Research Objectives; prototype includes Objectives & Research Questions and Session Flow. Missing a required section blocks delivery; do not claim a source goal maps to a section that is absent. |

### Part 1 — Methodological Audit (Structure & Flow)

| Dimension | Tag | What "Good" Looks Like |
|-----------|-----|------------------------|
| **Opening rapport & consent** | [Both] | Warm opening; explicit consent before any approved recording/observation begins; purpose, duration, and right to skip/stop. Privacy language is only what the plan/ResOps approves. Prototype adds think-aloud + prototype-limitations caveat. |
| **Phase structure** | [Both] | Phases and times match the **chosen format's Step 2a row**, displayed per section. Interview: Intro → Warm-up → Core (themes) → Wrap-up. Prototype: Intro → Background → Task Flows → Wrap-up (+ vendor back-matter). Don't force interview phase names onto a prototype guide. (AIxUXR §Prompt A "Calculate and Allocate Time") |
| **Funnel within Core** | [Interview] | Broad "Grand Tour" question first, then specific-incident probes, then optional factual clarifiers. (Prototype analog: usability tasks ordered simple → complex; a reaction-led concept phase starts with the approved unaided exposure before deeper prompts. P8 = Task-only remains valid only when no approved construct depends on that unaided response.) (AIxUXR §Prompt A.3; NN/g Rosala) |
| **Time budgeting** | [Both] | Per-phase minutes allocated and summing to the session length; Core/Task-Flows gets the format's share (IDI ≈ 80%, usability ≈ 75%, concept ≈ 70%). For interviews, count the separately timed 1-minute Consent heading and allocate only the post-consent remainder to Introduction (`Consent 1 + Introduction 2`, never `Consent 1 + Introduction 3`, for a 3-minute opening). Warm-up/Background not eating Core. Wrap-up protected. (AIxUXR §Prompt A.1) |
| **Question / task sequencing** | [Both] | Each question or task builds on the last; no abrupt jumps without a bridge; transitions signposted. (AIxUXR §V2 Prompt B Part 2) |
| **Wrap-up dual function** | [Both] | (a) Reflection — interview: "play back the themes"; prototype: most-important / most-confusing. (b) "Anything else?" open catch-all. (AIxUXR §Prompt B SRQ1.2) |

### Part 2 — Question Quality Audit (Phrasing & Bias)

Before declaring this part passed, build an audit-only inventory of every participant-facing research question and probe, including conditional and fallback lines. Mark every item for closed yes/no and compound framing; classify any closed item as exact approved consent confirmation, eligibility screening, a one-fact clarifier after an open response, or an approved rating scale, and rewrite every other failure. Report the checked-item count in the audit summary. Keep the inventory outside the guide.

| Check | Tag | Fail Pattern → Fix |
|-------|-----|--------------------|
| **Leading questions** | [Both] | ❌ "Don't you find the new checkout faster?" → ✅ "Describe your experience using the new checkout." (AIxUXR §Prompt B example row; NN/g 6 Mistakes) |
| **Hypothetical / speculative** | [Both] | ❌ "Would you use this?" / predicted personal behavior → ✅ "What is the most recent time, if any, that you…?" then probe after confirmation. Future expert-landscape questions are allowed only when future judgment is the construct. |
| **Closed yes/no framing** | [Both] | ❌ "Did you like it?" → ✅ "How would you describe that experience?" Allowed closed forms are exact approved consent confirmation, eligibility screening, one-fact clarification after an open response, and an approved post-task scale; none may replace an open generative question. (AIxUXR §V2 Prompt B; Hall) |
| **Compound / double-barrelled** | [Both] | ❌ "How easy and enjoyable was it?" → ✅ Split into two questions. (NN/g) |
| **Presupposition** | [Both] | ❌ "When did you realize this was a problem?" → ✅ "What, if anything, made this feel like a problem?" Never imply an event or opinion occurred. |
| **Jargon / insider terminology** | [Both] | ❌ UI labels, internal product names, acronyms the participant hasn't used → ✅ Plain language matched to participant vocabulary. (AIxUXR §Responsible AI — "Inclusivity of language") |
| **Past-behavior anchoring** | [Interview] | Interview Core questions tied to a concrete, recent incident — not "typically"/"in general." *Do NOT apply to prototype task rows* (they are present-tense observed actions by design — check instead that the task's **scenario** grounds a realistic situation). (AIxUXR §Prompt A.4; NN/g CIT) |
| **Construct-matched phase framing** | [Prototype] | Usability tasks describe the goal, not the interface ("find a way to add these items", never "click the green Add button") and carry a scenario. Concept prompts measure the approved reaction/comprehension/relevance construct without inventing a task. P8 follows the subtype-aware gate. (AIxUXR §Use Cases 2–3) |
| **Inclusivity & cultural assumptions** | [Both] | Questions don't assume a household structure, income level, cooking frequency, dietary pattern, or tech proficiency. (AIxUXR §RAI "Equity and Fairness") |

### Part 3 — Probing & Moderator Guidance Audit

| Check | Tag | What to Verify |
|-------|-----|----------------|
| **Probe quality per question** | [Interview] | Each interview Core question has 1-2 named probes attached (Echo, Tell-Me-More, Laddering, Silence, Critical Incident). No "naked" questions. (Prototype: think-aloud + observation cues play this role.) (See Probing Taxonomy.) |
| **Moderator Notes / cues embedded** | [Both] | Interview: `[Moderator Note: ...]` at every transition + Core topic. Prototype: per-phase **observation cues** (yes/no + "if not, what instead?") in a prose line below each phase list, plus behavior forks / WoZ triggers. (AIxUXR §Prompt A.5) |
| **Silence as a tool** | [Both] | Reminds moderator to count 5-10 seconds before filling gaps. (NN/g Fessenden; Portigal) |
| **Observation cues present** | [Prototype] | Every task flow carries a success/observation cue (yes/no + "if not, what do they do instead?"). When Row P7 selected a rating, reuse that exact scale per flow. No task flow without a cue. |
| **Task framing: goal not UI** | [Prototype] | Tasks describe the goal, not the UI ("find a way to…" not "click the red button"). (AIxUXR §Use Case 2 Critical Rule) |
| **Priming → Expectation → Action → Alignment** | [Prototype] | Each task includes the four-part sequence (set context → what do you expect → do it → did it match?). (AIxUXR §Use Case 4; NN/g) |
| **Problem validation before reveal** | [Prototype — concept only] | Blind-need questions precede the concept reveal to avoid biasing desirability. (AIxUXR §Use Case 3 "The Reveal technique") |

### Part 4 — Strategic & Efficiency Audit

| Check | What to Verify |
|-------|----------------|
| **Coverage of research objectives** | Every objective/RQ/hypothesis maps to at least one required Core question, prompt, comparison, or executable task appropriate to its construct. No orphan objective, no orphan evidence-producing guide item, and no task invented to satisfy traceability. |
| **Source-grounding check** | Walk every claim against the source plan: preserve denominators, hedges, surfaces, dates, sample, and method. A talk-only guide cannot inherit a prototype plan's hypotheses or session dates as though it tested the artifact. |
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
| **PII recheck** | Confirm the pre-access minimization gate held: no participant names, contacts, schedules, biographies, recording links, or other unnecessary participant-level data entered the draft or reviewer packet. |
| **Attribution & disclosure** | When sharing the final guide with stakeholders, note that AI was used for the first-pass draft/critique. Transparency builds trust. (AIxUXR §6 "Attribute the Assist"; H.E.A.R.T. "Transparent") |
| **Guide is a protocol, not a cage** | Remind researcher: in live session, deviate from the script when valuable emergent narratives appear. (AIxUXR §6 "The Guide is a Protocol, Not a Cage") |

---

## Step 5 — Section 3: Multi-Agent Review (before the Doc)

Run the multi-agent review only when the researcher selected the enhanced panel and reviewer access is authorized. The mandatory baseline audit already passed.

- The panel decision must state its two lenses, minimum necessary sources, audience, and expected runtime. Use that as the single pre-flight approval; do not ask again per lens.
- Say in chat: *"Running the multi-agent review now — researcher reviewers read the guide in parallel: an Evidence checker for rigor and consistency, and a Stakeholder reader reading it as [audience]."*
- Check the live skill list, then invoke `/multi-agent-check` when installed. Pass the fixed guide and only approved de-identified excerpts—not complete source files by default.
- If `multi-agent-check` is unavailable or reviewer access is not authorized, disclose that the enhanced panel did not run and proceed on the passed baseline audit.
- Route panel fixes through Post-audit change control; never silently fold meaning-changing fixes into locked content.

The sequence is **approved blocks → mandatory baseline audit/candidate fixes → optional panel/candidate fixes → material-change approval + affected-audit rerun → selected delivery branch.** Never claim the panel ran when it was skipped or unavailable.

---

## Step 6 — Upload, Style, Verify + Share (NO researcher QUESTIONS — execute the delivery silently)

🚫 **Step 6 normally runs with zero `AskUserQuestion` calls.** Destination, audience, recovery path, style, and protocol were already decided. Any material audit/panel change must already have completed the planned Section 3 approval and affected-audit rerun before Step 6 begins. If a required authorization, ACL, or capability is missing, stop before writing and report the blocker; never invent a safety-critical default.

Status updates are welcome (a one-line "Creating the doc… Applying [style]…" message). What's not fine: any question, any "want me to…?" Treat Step 6 like a deterministic script.

### 6.1 Preflight destination, capabilities, and create once

1. Follow `references/source-and-delivery-safety.md`. Fresh-read the confirmed folder's effective permissions and verify the intended audience, inherited/group access when visible, link-sharing scope, and the preauthorized partial-artifact recovery path. Do not create if permissions are unreadable or broader than authorized; never change sharing silently. If recovery is not authorized and supported, block before creation.
2. Preflight create/import, raw tab structure, revision-bound batch updates, readback, parent/permission readback, render/export, and the exact preauthorized partial-artifact recovery action. A connected tool name is not proof of capability.
3. Record the exact folder, approved title, and attempt time. Create/import once. On timeout or ambiguous response, reconcile by returned ID or exact title + folder + attempt window; reuse one verified match and never blindly retry.
4. **Default path — Option 4 — Leadership:** run the bundled formatter in place against `references/option4-guide-style.json` (load `references/option4-guide-style.md` first):
   - `manifest` — parse the approved guide markdown into a build manifest;
   - import Markdown as `application/vnd.google-apps.document` from the protected working file (with `gws`: `drive files create --upload`, run from the private working directory); plain-text paste does not create real headings/tables. Fetch with `includeTabsContent: true` and a fresh `revisionId`;
   - `normalize` — generate the cleanup batch against that snapshot and require the same `revisionId`; apply once through the route chosen in Section 1 (a connector's request-body parameter that takes native, revision-bound requests, or `send` with `gws`), then re-fetch;
   - `format` — generate the styling batch against the new snapshot and require its new `revisionId`; apply once the same way, then re-fetch;
   - `verify` — validate the visual invariants (page geometry, fonts, colors, band styling, table widths/padding), then export/render and eyeball the opening page and a dense page.
   - **Completion gate:** if an Option 4-only capability is unavailable, block when Strict Option 4 — Leadership was selected. Otherwise use the pre-approved plain-native fallback and disclose it; never claim Option 4 passed. Missing write access, content/parent/permission readback, or render blocks delivery on every path.
5. **Plain native Google Docs (explicit or approved fallback):** apply native Title/Heading/body styles and native tables, then read back and render. No Option 4 claim.
6. **Demo/mock runs:** return labeled Markdown and create no Drive artifact. When the researcher explicitly requests a test Doc, repeat the destination/ACL gate, keep the warning in the Doc, and never track it.
7. **Failure recovery:** on revision conflict or ambiguous update, never resend the old batch. Re-fetch the known Doc; if expected state already exists, record success, otherwise regenerate against the new revision. Execute only the preauthorized trash-by-ID or exact quarantine action before any new create attempt; if it cannot be performed, stop and report without improvising another mutation.

### 6.2 Verify and correct

1. Read back the created document, its parent folder, and effective permissions.
2. Compare it against every approved block and the source crosswalk: ownership completeness, parameters, lists, links, one format-correct consent pass, and no restricted participant operations data.
3. **Confirm the ending:** interview → optional Parking Lot, else Post-Session Debrief; internal prototype → Post-Session Debrief; vendor prototype → Communication & Deliverables. No participant log, Master Probe Bank, Bias Checklist, audit output, or pilot reminder inside the guide.
4. **Confirm length against the format ceiling:** interview ~4–5 pages (max 7); prototype ~6–8 pages. If over ceiling, cut moderator-note paragraphs and redundant explanation — never task/observation content.
5. **Prototype must-haves:** approved prototype/backup links only; two tables total; every phase a bold-label list using its approved construct-matched shape; P8-gated first impressions; observation cues/probes in prose; experimental-design note when applicable; and every supplied objective/RQ/hypothesis mapped to a required evidence-producing guide item appropriate to its construct. Usability phases require Scenario → Expectation → Task → Alignment; reaction-led concept phases require reveal → [P8-approved first impression, when included] → required construct-matched neutral prompts and no invented task.
6. Correct every issue, then re-fetch and re-run content, parent/ACL, visual verifier, and render inspection. If render is unavailable, delivery blocks on every path; plain native is a fallback only for Option 4-specific styling/verifier limitations and must itself be rendered and labeled accordingly.

### 6.3 Return the verified guide

1. Share the final Google Doc link in chat with a short summary of what's in the guide, plus a one-line **pilot reminder** (per Step 4.5 Part 4) to test the guide with a teammate or friendly participant before formal data collection.
2. State verification status: content/crosswalk checked, links checked, parent and permissions checked, style verifier result, and render inspected—plus any explicit limitation or fallback.
3. **Only after the link is shared** is the skill allowed to respond to follow-up questions or correction requests from the researcher.
4. Do not update project trackers or progress files unless the researcher separately asks. Never update them for a demo/mock or for non-study personal content.

---

## Tool Usage

- **AskUserQuestion** — gather the Section 1 decisions, Section 2 core-block approvals, separate destination/audience, partial-recovery, style, and (when it applies) write-route confirmations, and the optional enhanced-panel choice.
- **`/multi-agent-check`** — optional enhanced panel in Step 5; invoke only when selected and reviewer access is authorized.
- **Google Docs / approved enterprise search (e.g., Glean)** — check sign-in at the start of Step 1 without reading content; read non-public plans only after the source-authorization gate.
- **Connected Google Docs / Drive read tools** — read authorized non-public plans and fresh document structure, revisions, parents, and permissions after the applicable gates.
- **Connected Google Docs / Drive tools** — create the guide in the confirmed folder, apply the batch operations from the Option 4 formatter (or native styles on the plain-native fallback), read it back to verify, and return the link. No personal script required.
- **`scripts/option4_guide_layout.py`** — **default (portable) styler:** the bundled Option 4 — Leadership formatter+verifier (`manifest`/`normalize`/`format`/`verify`, plus `send` to apply a batch through `gws` without a shell). Produces the clean, edited leadership look with native Google Docs only. Drives from `references/option4-guide-style.json`.
- **`references/option4-guide-style.json`** + **`references/option4-guide-style.md`** — the Option 4 visual contract (machine-readable + human-readable); load the `.md` before formatting. Visual tokens are shared verbatim with `/research-plan`'s Option 4.
- **references/template-prototype-usability.md** — **load in Section 1 when the format is Prototype/Usability.** Holds the prototype Section 1 params, Section 2 blocks, OUTPUT TEMPLATE, and generation rules.
- **references/template-interview.md** — **load in Section 1 when the format is Interview.** Holds the interview Section 1 params, Section 2 blocks, OUTPUT TEMPLATE, and generation rules. (Only the format-neutral shared scaffolding is inline in Step 4; the interview body template lives here.)
- **references/source-and-delivery-safety.md** — load before non-public source access, reviewer handoff, or any Google Doc creation.
- **references/mod-guide-methodology.md** — load on demand for probes/bias, and automatically for concept tests, diary check-ins, and focus groups.

---

## Sources

- Portigal, S. (2023). *Interviewing Users: How to Uncover Compelling Insights* (2nd ed.). Rosenfeld Media. [portigal.com](https://portigal.com/books/interviewing-users-2/)
- Young, I. *Listening Deeply* and mental model method. [indiyoung.com](https://indiyoung.com/method/)
- Hall, E. (2019). *Just Enough Research* (revised ed.). A Book Apart.
- Sharon, T. (2016). *Validating Product Ideas: Through Lean User Research*. Rosenfeld Media.
- Nielsen Norman Group: Rosala, M. — [User Interviews 101](https://www.nngroup.com/articles/user-interviews/), [6 Mistakes When Crafting Interview Questions](https://www.nngroup.com/articles/interview-questions-mistakes/), [Writing an Effective Guide for a UX Interview](https://www.nngroup.com/articles/interview-guide/), [The Funnel Technique](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/), [5 Facilitation Mistakes](https://www.nngroup.com/articles/interview-facilitation-mistakes/), [Why User Interviews Fail](https://www.nngroup.com/articles/why-user-interviews-fail/), [The Critical Incident Technique in UX](https://www.nngroup.com/articles/critical-incident-technique/); Pernice, K. & Moran, K. — [Thinking Aloud: The #1 Usability Tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/); Fessenden, T. — [Talking with Users in a Usability Test](https://www.nngroup.com/articles/talking-to-users/), [Checklist for Moderating a Usability Test](https://www.nngroup.com/articles/usability-checklist/).
- Anderson, N. — [User Research Academy](https://www.userresearchacademy.com/) and dscout *People Nerds*.
- dscout — [17 Pro Tips to Perfect One-on-One Interviews](https://dscout.com/people-nerds/tips-master-researcher-participant-interviews), [Dig Deeper with Follow-Up Questions](https://dscout.com/people-nerds/generative-research-questions).
