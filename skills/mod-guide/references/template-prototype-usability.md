# Prototype / Usability Guide — Template Reference

Load this when the researcher picks **Prototype / Usability** as the guide format (Step 2a / Section 1 > Step 1). It holds the type-specific pieces the skill needs: the extra Section 1 parameters, the Section 2 block sequence, the full OUTPUT TEMPLATE, and prototype-specific content rules. The **shared scaffolding** (Moderation Guide header, ownership block/RACI, parameter table, Pre-Session Checklist, Post-Session Debrief) is assembled from SKILL.md's shared-scaffolding section. Consent/think-aloud is handled once, as a short **read-aloud Introduction list** (see Section 2), not as a second standalone Consent table.

> **Format rule:** in a prototype/usability guide the read-aloud Introduction and every reaction/task phase, comparison, and recap block render as **bold-label lists** (`- **Label:** "line"`), never Cue tables. The **only** two tables the guide keeps are the top **Parameter dashboard** and the **Session Flow** agenda.

The template is informed by completed internal prototype and usability studies; source-study identifiers are intentionally omitted from this public package.

---

## When this type applies

A prototype/usability guide is the right shape whenever the study puts an **artifact in front of the participant and asks them to react to, interpret, compare, or use it**. Signals in the inputs:

- A prototype / Figma / Android-Studio link, mockups, screens, or an on-device/on-cart stimulus of any kind.
- Words like *usability, concept test, first impression, reaction, comprehension, desirability, task, flow, walkthrough, click, can they complete X, where do they get stuck, find the friction*.
- A design under evaluation — especially **multiple variants** (Option A vs. B) or interventions to compare.
- A goal phrased as "can users complete / understand / navigate X."
- Counterbalancing or order-effects are a concern (implies multiple stimuli shown in sequence).

A short warm-up interview living *inside* an artifact-based session does **not** make it an interview guide. The approved construct determines whether each core phase is reaction-led, task-led, or explicitly mixed.

---

## Section 1 — Prototype-specific parameters

Ask these **in addition to** the shared Section 1 rows (study title, moderation style, duration, participants, profile, **Row 7 topics/tasks/flows**, stakeholders/RACI, Drive destination & delivery). Every row still gets a Recommended option, real alternatives, an editable Other field, and "Brainstorm with me" last; every pop-up is labeled `Section 1 > Step N of M`. A row tagged **(= Row N)** is the shared row realized for this format — asked **once** in the main Section 1 batch, not a second time here.

| # | Question | Select | Recommended | Alternatives |
|---|----------|--------|-------------|--------------|
| P1 | **Delivery model** — who runs the sessions | single | Exact source-approved internal or vendor-moderated model; `[TBD — fill in]` when absent | The other model only as a proposed plan change; vendor-run adds approved Communication/Deliverables back-matter |
| P2 | **Prototype / stimulus** — the artifact(s) under test | single confirm/revise | The complete extracted prototype/link set | Add or compare another variant · Replace/revise the set |
| P3 | **Backup stimulus** — fallback if the main prototype fails | single | Exact source-approved backup link or source-approved "No backup"; `[TBD — fill in]` when absent | Propose another approved fallback · No backup |
| P4 | **Device / platform** | single | Extracted device/platform | The two most plausible alternatives; use Other for a custom setup |
| P5 **(= Row 7)** | **Stimuli / phases / task flows** — the ordered core sequence (this IS the shared Row 7 — don't ask twice) | multi only for 2–3 independent items; otherwise single confirm/revise | The complete ordered stimulus/phase/flow set | Remove/reorder · Add/reframe |
| P6 | **Experimental design** — how stimuli are ordered across participants | single | Exact extracted source design; when absent, `[TBD — fill in]` rather than assuming fixed order | The two remaining valid designs after removing the Recommended one, each as a proposed plan change |
| P7 | **Post-phase rating style** | single | Exact approved source scale reused verbatim per applicable phase, or source-approved no-rating choice; when absent, `[TBD — fill in]` | Propose one construct-matched scale · No numeric rating |
| P8 | **Unaided first impression at first exposure** | single | **Concept —** Include on each named first exposure whose approved objective/RQ/hypothesis measures initial recall, comprehension, reaction, or desirability; otherwise Task-only. Use the methodology's 5-second hide-and-recall sequence when included. **Usability —** Include only on named screens when an approved objective/RQ/hypothesis measures unaided initial comprehension or reaction; otherwise Task-only. | **Concept —** Include on an approved subset of named stimuli · Task-only when no approved construct depends on the unaided exposure, or as an approved material method amendment. **Usability —** Include on [named screens] · Task-only (skip unaided reaction) |

*(Truly prototype-specific asks = P1, P2, P3, P4, P6, P7, P8. P5 is the shared Row 7.)* **Row 8 (Say-Do Gap module)** is also a shared row — normally **Skip** for a prototype test (the session observes behavior directly), asked in the main batch only when the study also collects meaningful stated-preference data (mirrors how the interview reference tags its I5).

Use SUS/SEQ only when the researcher explicitly selected it in Row P7. Otherwise use one lightweight, approved scale repeated verbatim across applicable phases, or omit rating prompts when Row P7 selected no numeric rating. Mark any unknown stimulus/device/link `[TBD — fill in]` rather than inventing it.

---

## Section 2 — Prototype content blocks (draft-first, one at a time)

Walk these blocks in order, each shown as a draft → approved → locked before the next, labeled `Section 2 > Step N of M`. M = the number of blocks this study actually has.

**Pop-up rule:** Pop-ups only for the Phases (core blocks). Background & Warm-Up and Wrap-Up are auto-generated — no pop-up, no approval gate.

1. **Objectives & Research Questions** — study-background paragraph, one bold sub-header per topic/feature, then the approved objective and key questions. Carry a hypothesis or Priority-1/Priority-2 label only when the source plan or researcher supplied it; never invent either. **Auto-generated — no pop-up.**
2. **Session Flow** — simple phase list (Introduction → Background & Warm-Up → Phase 1 → Phase 2 → Phase 3 → Wrap-Up). No minute-by-minute breakdown. **Auto-generated — no pop-up.** *(Rendered as a table — one of the two tables a prototype guide keeps.)*
3. **Introduction & Think-Aloud Setup (read aloud)** *(no pop-up)* — a short **bold-label list** (`- **Cue:** "read-aloud line"`), NOT a table: welcome, what-we'll-do, think-aloud ("brain on speakerphone"), prototype/stimulus caveat, control, and a recording/observation consent line whenever either is planned. Auto-generated only from approved protocol language.
4. **Background & Warm-Up** *(no pop-up)* — simple numbered questions (Q1, Q2, Q3), no table format, no "Probes to use" header. Observation cues in prose at end. Auto-generated from template.
5. **Phases (the core)** — **one block per phase / stimulus** from the approved P5 list. Named Phase 1, Phase 2, Phase 3 — simple, consistent. Each uses one construct-matched bold-label shape: **usability phase** = Scenario → P8-gated First impression → Expectation → executable Task → Alignment → approved rating; **reaction-led concept phase** = Stimulus reveal → P8-gated 5-second First impression → required neutral recall/comprehension prompt → reaction/relevance/desirability prompts → comparison/fit when applicable. Add a task to a concept phase only when an approved objective/RQ/hypothesis measures observable behavior with the concept. Observation cues stay in prose below. **Pop-up for each phase.**
6. **Wrap-Up** *(no pop-up)* — standard three-question close plus a thank-you. Auto-generated.
7. **Communication & Deliverables (+ Timeline)** *(vendor-run only, and only from the approved vendor plan)* — approved communication channel/cadence, deliverables, owners, and dates; leave every unknown `[TBD — fill in]`.

The shared scaffolding (Moderation Guide header, RACI block, parameter table, Pre-Session Checklist, Post-Session Debrief) is assembled around these per SKILL.md.

Every supplied objective, RQ, or hypothesis must map to a required **construct-matched evidence-collection element**. Concept P8 = Task-only is invalid when an approved objective or hypothesis measures initial recall, comprehension, reaction, or desirability. Usability P8 = Task-only is invalid only when an approved objective or hypothesis measures unaided initial comprehension or reaction. Never convert a reaction, recall, comprehension, or desirability hypothesis into an invented behavioral task.

---

## OUTPUT TEMPLATE — Prototype / Usability

> **Core principle:** the moderator's eye should land on a **bold-label list holding only what to show, say, ask, or ask the participant to do** — stimulus reveal, neutral reaction/comprehension prompts, or goal-based tasks according to the approved construct. Objectives, hypotheses, experimental-design rationale, observation cues, and methodology all live in **prose or front-matter, never inside the list.** Only the Parameter dashboard and the Session Flow agenda are tables. Target length **~6–8 pages.**

**Study-period rule:** Never substitute the current date or month for an unknown study period.

```
# Moderation Guide

## [Study Title — e.g. "Checkout Confirmation Usability Test"]

*[Source-approved study period or TBD — fill in]*

- **Responsible:** [TBD — fill in] ([TBD — fill in])
- **Accountable:** [TBD — fill in] ([TBD — fill in])
- **Consulted:** [TBD — fill in]
- **Informed:** [TBD — fill in]

**Links:** [Approved research plan/folder] · [Figma / Prototype] · [Approved screener, if accessible to this guide's audience]

| Parameter | Detail |
|-----------|--------|
| **Study Type & Format** | [Moderated usability test / moderated concept test] — [in-person / remote / on-device] |
| **Duration** | [X] minutes |
| **Participants** | N=[N] — [screening criterion] |
| **Stimulus** | [Link to stimulus — Phase A: [link] · Phase B: [link]] |
| **Goal** | [1–2 sentence research goal] |

---

## Session Flow

| Phase | Time |
|-------|------|
| Introduction & Think-Aloud Setup | [X] min |
| Background & Warm-Up | [X] min |
| Phase 1 — [Stimulus A name / description] | [X] min |
| Phase 2 — [Stimulus B name / description] | [X] min |
| [Phase 3 — if applicable] | [X] min |
| Wrap-Up | [X] min |

---

## Objectives & Research Questions

[Study-background / problem paragraph — what prompted this round.]

**Topic 1 — [feature/flow]**
- *Hypothesis (only when supplied/approved):* [what the plan states]
- **[Priority-1 — only when supplied/approved]** [prioritized objective]
- **[Priority-2 — only when supplied/approved]** [secondary objective]
- *Key Questions:* [the questions this topic answers — NOT read aloud]

**Topic 2 — [feature/flow]**
- *Hypothesis:* …
- **[Priority-1]** …

*(Omit hypotheses and priority tags when the plan does not contain them. When used, tags are "Priority-1/-2", never "P0/P1" — participant IDs can use P1–P12.)*

---

## Pre-Session Checklist

[Shared scaffolding — bullets with ☐. Include prototype-specific items:]
- ☐ Participant validated — [screening criterion]
- ☐ Prototype loaded & tested — primary link opens; [backup ready — include only when a backup was approved]
- ☐ Device — [participant on their own device / remote-control handoff confirmed]
- ☐ [Approved recording/observation setup confirmed; omit when neither is planned]
- ☐ [Vendor communication channel ready — vendor-run only]

---

## Introduction & Think-Aloud Setup (~[X] min) — read aloud

*(Bold-label list — NOT a table.)*

- **Welcome:** "Hi [name], thanks for joining. I'm [moderator], [approved company/role framing, or blinded framing]. [1-line purpose — no right/wrong answers.]"
- **What we'll do:** "[Concrete description — e.g. I'll show you some screens / questions and ask you to think out loud.]"
- **[Observers — include only when approved and present]:** "[Approved observer disclosure.]"
- **Think-aloud:** "The most helpful thing is hearing your thoughts as they happen — like putting your brain on speakerphone."
- **Prototype/stimulus caveat:** "This is a draft we're testing — if something doesn't make sense, that's the design's fault, not yours."
- **Recording / observation consent (include whenever recording or live observation is planned):** "With your permission, I'd like to [approved recording modalities], and [approved observer disclosure, if applicable]. [Approved access/use statement, or `[TBD — confirm ResOps standard language]`.] Is that okay?" *(Never invent modalities, access scope, anonymity, clip sharing, retention, or deletion.)*
- **Control:** "About [X] minutes. You can skip anything or stop anytime[ — and still get the incentive — ONLY if the plan/ResOps confirms early-exit incentive policy]. Any questions before we start?"

> When recording or observing, wait for the protocol's required explicit consent before beginning. **Use silence:** after a prompt, give a ~5-second beat before re-asking — don't rescue or lead.

---

## Background & Warm-Up (~[X] min)

1. [Neutral incident gate — e.g. "What is the most recent time, if any, that you got groceries?" If they name one: "Walk me through what happened."]
2. [Context question after an incident is confirmed — e.g. "What led you to shop that way on that occasion?"]
3. [Prior-experience question — e.g. "What experience, if any, have you had with [product/feature]?"]
4. [Any session-specific logistics — e.g. "I'm going to give you remote control / hand you the device now."]

**Observation cues:** [What to watch for during warm-up — e.g. does the participant seem comfortable with the device? Any relevant context they surface unprompted?]

---

[Phase-shape gate: choose the construct-matched shape for each phase. A usability phase uses Scenario → P8-gated First impression → Expectation → Task → Alignment → approved rating. A reaction-led concept phase uses Stimulus reveal → P8-gated 5-second First impression → neutral Recall/comprehension → Reaction/relevance/desirability → Comparison/fit when applicable. Add Task only for an approved behavioral construct.]

[P8 gate: for a concept test, Include only on named first exposures whose approved objective/RQ/hypothesis measures initial recall, comprehension, reaction, or desirability; otherwise Task-only. For usability, keep First impression only on approved screen(s) tied to an unaided initial-comprehension/reaction construct. Concept P8 = Task-only is invalid when an approved objective or hypothesis measures initial recall, comprehension, reaction, or desirability. Usability P8 = Task-only is invalid only when an approved objective or hypothesis measures unaided initial comprehension or reaction. When validly Task-only, omit every First impression row below and leave no placeholder.]

## Phase 1 — [Stimulus A name / description]

**Stimulus:** [LINK TO STIMULUS A]

*[Experimental-design note in prose here if any — between-/within-subjects, counterbalance order.]*

- **Scenario:** "I'm going to show you [what this is]. As you look at it, think out loud."
- **First impression (unaided):** "Before you do anything — what's your first impression?"
- **Expectation:** "Before you try it, what do you expect will happen?"
- **Task:** "Imagine you [realistic situation]. Show me how you would [goal, without naming UI controls]."
- **Alignment:** "How did that compare with what you expected?"
- **Post-task rating (only when approved):** "On the approved [scale], how [construct] was that?"

**Rating probe (ask after the response, only when a rating was asked):** "What made you choose that rating?"

**Observation cues:** [Prose line below the list — e.g. does the participant hesitate? Do they reread? Do they express confusion or confidence?]

**Moderator probes if stuck (ask one at a time):** "What would you expect to happen?" Then, if needed: "What would you try next?"

---

## Phase 2 — [Stimulus B name / description]

**Stimulus:** [LINK TO STIMULUS B]

- **Scenario:** "Imagine you [realistic situation for Stimulus B]."
- **First impression (unaided):** "Take a look at this version. What do you notice first?"
- **Expectation:** "Before you try it, what do you expect will happen?"
- **Task:** "Imagine you [realistic situation]. Show me how you would [goal]."
- **Alignment:** "How did that compare with what you expected?"
- **Post-task rating (only when approved):** "On the approved [scale], how [construct] was that?"

**Rating probe (ask after the response, only when a rating was asked):** "What made you choose that rating?"

**Observation cues:** [Prose line below the list.]

---

## Phase 3 — [Optional third task / stimulus]

**Stimulus:** [LINK TO STIMULUS C]

- **Scenario:** "Imagine you [realistic situation for Stimulus C]."
- **First impression (unaided):** "Before you do anything — what do you notice first?"
- **Expectation:** "Before you try it, what do you expect will happen?"
- **Task:** "Show me how you would [goal, without naming UI controls]."
- **Alignment:** "How did that compare with what you expected?"
- **Post-task rating (only when approved):** "On the approved [scale], how [construct] was that?"

**Rating probe (ask after the response, only when a rating was asked):** "What made you choose that rating?"

**Observation cues:** [Prose line below the list.]

[Add, remove, or repeat the appropriate phase shape as needed. A task-led usability phase keeps Scenario → Expectation → Task → Alignment, with First impression inserted only at P8-approved exposures. A reaction-led concept phase replaces Expectation/Task/Alignment with the required neutral recall/comprehension and reaction/relevance/desirability prompts; never add a behavioral task unless the approved construct calls for one. Put cross-stimulus comparisons in the separate Comparisons or Cross-Flow Recap section.]

---

## Comparisons (~[X] min) — *multi-variant studies only*

- **C1 — approved construct:** "How would you compare the [approved construct, e.g. effort or clarity] of [Option A] and [Option B]?"
- **C2 — fit:** "How would you compare each option's fit for [goal]?"

**Comparison probe (ask one at a time after a response):** "What makes you say that?"

---

## Cross-Flow Recap (~[X] min) — *optional*

- **Recap1:** "What kinds of situations, if any, does each option seem suited to?"
- **Recap2:** "What, if anything, remains confusing after going through all of that?"

---

## Wrap-Up (~[X] min)

1. **Reflection (choose one lens: most important or confusing):** Thinking back across everything you tried, what stands out most?
2. Thinking back to everything we've discussed, is there anything you didn't get a chance to share that you'd like to?
3. What questions do you have for me?
4. Thank you again for your time today! [Use only approved incentive/next-step language; otherwise end after the thank-you.]

---

## Post-Session Debrief

[Shared scaffolding — numbered list, within 5 min of end:]
1. **Task outcomes:** per flow — ☐ completed unaided · ☐ completed with help · ☐ failed — one-line why
2. **Top friction point:** the single most diagnostic breakdown + which screen
3. **Most diagnostic verbatim quote:** one sentence, exact words

---

## Communication & Deliverables — *vendor-run only*

**Communication.** [Approved communication channel, audience, owner, and cadence; otherwise `[TBD — fill in]`.]

**Interim updates.** [Approved timing, audience, content, and claim-strength guardrail; otherwise omit.]

**Deliverables.** [Approved deliverable, owner, format, draft date, and final date; otherwise `[TBD — fill in]`.] · [Session recordings only when the approved plan defines access, location, and retention.] · [Approved readout, if any.]

**Timeline** *(optional bold-label list; keep the prototype guide to two tables total):*
- **[Deliverable]:** [Owner] — [Date]
```

**IMPORTANT:** the guide ends at the Post-Session Debrief for internal studies, or at Communication & Deliverables (+ Timeline) for vendor-run studies. No Master Probe Bank, Bias Checklist, or Self-Critique inside the doc.

---

## Prototype-specific content-generation rules

1. **Usability tasks describe goals, not UI.** "Find a way to add these items" — never "click the green Add button." Concept phases use neutral prompts matched to the approved reaction/comprehension construct and do not acquire an invented task. (NN/g)
2. **Every phase carries a construct-matched observation cue in prose below the list.** Usability example: `Do they [action]? (yes/no) · If not, what do they do instead? · Any concerns?` Concept example: what the participant notices, recalls, interprets, or reacts to before deeper probing. Never put cues inside a list item.
3. **Scenario framing for a usability task is a first-person "Imagine you…"** setup that gives context without leading to the answer. Concept-reveal framing identifies only the approved stimulus and exposure instruction; it does not prime the desired reaction.
4. **First exposure is controlled by subtype-aware P8.** Concept tests include the approved 5-second first-impression sequence only on named first exposures tied to an approved initial recall, comprehension, reaction, or desirability construct; otherwise they are Task-only. Usability studies include it only on named screens tied to an approved initial-comprehension/reaction construct. Concept P8 = Task-only is invalid when an approved objective or hypothesis measures initial recall, comprehension, reaction, or desirability. Usability P8 = Task-only is invalid only when an approved objective or hypothesis measures unaided initial comprehension or reaction. After that validity gate passes, P8 = Task-only means omit every First impression row and leave no placeholder.
5. **Think-aloud is scripted with the house metaphor** ("put your brain on speakerphone") and always paired with the **prototype-limitations caveat**.
6. **Experimental design is stated in prose in the task-section header**, not in list items: between-/within-subjects, counterbalanced order, or a numbered counterbalance grid in arrow notation when order matters.
7. **Behavior forks and moderator/WoZ triggers** are bracketed stage directions in prose outside the bold-label participant read/do list: `[If they remove the item]`, `[Fork 1 / Fork 2]`, `[Mod: trigger the prompt]`.
8. **Ratings are reused verbatim across applicable phases for comparability.** Use SUS/SEQ only when the researcher explicitly selected it in Row P7; otherwise use one lightweight approved, construct-matched scale or no numeric rating.
9. **Prototype references are inline links labeled `[PROTOTYPE]`**, with a top **Links row** containing only approved study/prototype links accessible to the guide's audience. Never add participant grids, schedules, biographies, or recording links. Reference screens by `[Screen N]` tags in screen order.
10. **Timing is annotated in every section heading** and the two-column **Session Flow** agenda up top sums to the session length.
11. **Traceability is mandatory:** build an internal objective/RQ/hypothesis → phase/evidence-item crosswalk. Every supplied objective, RQ, or hypothesis maps to a required **construct-matched evidence-collection element**: completion, discoverability, navigation, and use → executable task plus observation cue; comprehension, reaction, recall, relevance, desirability, trust, preference, and comparison → required neutral prompt, plus a P8 first-impression prompt only at approved first exposures. Split mixed constructs. Never convert a reaction, recall, comprehension, or desirability hypothesis into an invented behavioral task. If no valid guide item can test the construct, flag a method mismatch and block coverage approval. Every guide item maps back to an approved objective, question, or hypothesis. Record any change to the plan as a proposed amendment. Include hypotheses and Priority-1/Priority-2 labels only when the source plan or researcher supplied them; never invent them. They live in Objectives, never in participant-facing lists.

---

## House-style notes (prototype guides)

- The document title is always **"Moderation Guide"**; vendor status appears in the parameter dashboard, not the title.
- Vendor back-matter uses the ordinary H2 section band and bold run-in labels. Include only the approved channel, cadence, deliverables, owners, dates, and claim-strength guardrails; leave unknowns `[TBD — fill in]`.
- Screenshots may be embedded in the stimulus context in screen order; when building natively, reference screens by name/number and link the prototype rather than embedding images unless the researcher supplies them.
