# Prototype / Usability Guide — Template Reference

Load this when the researcher picks **Prototype / Usability** as the guide format (Step 2a / Section 1 > Step 1). It holds the type-specific pieces the skill needs: the extra Section 1 parameters, the Section 2 block sequence, the full OUTPUT TEMPLATE, and prototype-specific content rules. The **shared scaffolding** (breadcrumb, stakeholder/ownership block, parameter table, Pre-Session Checklist, Consent + Recording script, Post-Session Debrief) is assembled from SKILL.md's shared-scaffolding section — identical for both guide types — so it is not repeated here.

Derived from four finished Instacart discussion guides: *IC4B Concept Testing* (internal), *Caper RR Round 3*, *Round 7 Bad Addresses*, and *Caper Cart Round 4 – Checkout Sprint* (agency-run, AnswerLab).

---

## When this type applies

A prototype/usability guide is the right shape whenever the study puts an **artifact in front of the participant and asks them to do something with it**. Signals in the inputs:

- A prototype / Figma / Android-Studio link, mockups, screens, or an on-device/on-cart stimulus of any kind.
- Words like *usability, test, task, flow, walkthrough, click, can they complete X, where do they get stuck, find the friction*.
- A design under evaluation — especially **multiple variants** (Option A vs. B) or interventions to compare.
- A goal phrased as "can users complete / understand / navigate X."
- Counterbalancing or order-effects are a concern (implies multiple stimuli shown in sequence).

A short warm-up interview living *inside* a prototype session does **not** make it an interview guide — the presence of tasks + a stimulus makes the whole thing a prototype guide.

---

## Section 1 — Prototype-specific parameters

Ask these **in addition to** the shared Section 1 rows (study title, moderation style, duration, participants, profile, **Row 7 topics/tasks/flows**, stakeholders/RACI, Drive destination & delivery). Every row still gets a Recommended option, real alternatives, an editable Other field, and "Brainstorm with me" last; every pop-up is labeled `Section 1 > Step N of M`. A row tagged **(= Row N)** is the shared row realized for this format — asked **once** in the main Section 1 batch, not a second time here.

| # | Question | Select | Recommended | Alternatives |
|---|----------|--------|-------------|--------------|
| P1 | **Delivery model** — who runs the sessions | single | Internal (Instacart-moderated) → "Research Plan" label | Vendor-run (agency, e.g. AnswerLab) → "Discussion Guide" label + Communication/Deliverables/Timeline back-matter |
| P2 | **Prototype / stimulus** — the artifact(s) under test | single | The extracted prototype link(s) | "Add a backup prototype" · "Multiple variants to compare" · `[TBD — paste link]` |
| P3 | **Backup stimulus** — fallback if the main prototype fails | single | A backup link, "use only if the main fails" | "No backup" |
| P4 | **Device / platform** | single | Extracted device (desktop w/ remote control, Fire tablet, iPad, physical Caper cart, participant's own phone) | The other plausible devices |
| P5 **(= Row 7)** | **Task flows** — the ordered list of flows/tasks to walk (this IS the shared Row 7, realized as task flows — don't ask twice) | **multi** | The 3–6 extracted flows, all pre-selected, each individually droppable | "Add a flow" |
| P6 | **Experimental design** — how stimuli are ordered across participants | single | None (single prototype, fixed order) | "Between-subjects" · "Within-subjects, counterbalanced" · "Full counterbalance grid" |
| P7 | **Post-task rating style** | single | Single 1–5 ease scale (1 = difficult, 5 = easy), reused verbatim per flow | "Named bipolar scale (e.g. intrusive↔helpful)" · "Qualitative ease/clarity questions only, no number" · "No rating" |
| P8 | **Feedback-then-Task pattern** — unaided reaction before the directed task | single | Include on first-impression screens | "Task-only (skip unaided reaction)" |

*(Truly prototype-specific asks = P1, P2, P3, P4, P6, P7, P8. P5 is the shared Row 7.)* **Row 8 (Say-Do Gap module)** is also a shared row — normally **Skip** for a prototype test (the session observes behavior directly), asked in the main batch only when the study also collects meaningful stated-preference data (mirrors how the interview reference tags its I5).

**Never use SUS/SEQ batteries** unless the researcher explicitly asks — these guides use one lightweight, bespoke, reused rating. Mark any unknown stimulus/device/link `[TBD — fill in]` rather than inventing it.

---

## Section 2 — Prototype content blocks (draft-first, one at a time)

Walk these blocks in order, each shown as a draft → approved → locked before the next, labeled `Section 2 > Step N of M`. M = the number of blocks this study actually has (skip Comparisons/Recap when not multi-variant; skip vendor back-matter when internal).

1. **Objectives & Research Questions** — kept *separate* from the moderator script: study-background paragraph, then one bold sub-header per Topic/feature, each with a hypothesis, P0/P1-labeled objectives, and a "Key Questions:" sub-block.
2. **Test Stimuli & Setup** — primary + backup prototype links, device, the experimental-design / counterbalance note, and the **Session Flow Overview** agenda table (one cell, timed phases summing to the session length).
3. **Introduction** *(verbatim read-aloud — confirm, don't re-draft)* — independent-researcher framing, no-right-answers ("we're testing the designs, not your abilities"), think-aloud request, consent/recording, observers, and the prototype-limitations caveat.
4. **Background / Warm-Up** — profiling before any stimulus (who shops, in-store vs. online, list use, prior product familiarity, relevant past issues) + a tech-setup/remote-control handoff.
5. **Task Flows (the core)** — **one block per flow** from the approved P5 list. Each: scenario setup, think-aloud directive, guided-tap steps, behavior forks, moderator/WoZ cues, observation cues, and the reused post-task rating + reflection.
6. **Comparisons** *(only for multi-variant studies)* — forced-choice preference across variants.
7. **Cross-flow Recap** *(optional)* — "when would you do X vs. Y" + remaining confusion across the whole experience.
8. **Wrap-Up** — most-important / most-confusing, moderator checks stakeholders for follow-ups, participant questions, incentive/thank-you.
9. **Communication & Deliverables (+ Timeline)** *(vendor-run only)* — Slack channel for stakeholder questions, EOD update spec, deliverables with dated milestones, optional project timeline.

The shared scaffolding (breadcrumb, RACI/POC block, parameter table, Pre-Session Checklist, Consent script, Post-Session Debrief) is assembled around these per SKILL.md.

---

## OUTPUT TEMPLATE — Prototype / Usability

> **Core principle:** the moderator's eye should land on a **table whose cells hold only what to say or do** — scenario setup, tap directives, and observation cues. Objectives, hypotheses, experimental-design rationale, and methodology all live in **prose or front-matter, never in the task cells.** Target length **~6–8 pages.**

```
*UX Research | [Research Plan | Discussion Guide] | [Round N · Quarter Year]*

# [Study Title — e.g. "Caper Cart Round 4: Checkout Sprint"]

**[Feature / prototype under test — one line]**

Last updated: [Month Year]

- **Responsible:** [Name] (Role) — `[TBD — fill in]` if unconfirmed
- **Accountable:** [Name] (Role)
- **Consulted:** [Designer, UXR, PM, EM]
- **Informed:** [partners, stakeholders]

**Links:** [Google Folder] · [Figma / Prototype] · [Participant Grid] · [Screener]

| Parameter | Detail |
|-----------|--------|
| **Study Type** | Moderated usability test (think-aloud) — [internal / vendor-run by AGENCY] |
| **Duration** | [X] minutes — [intro / background / tasks / wrap split in minutes] |
| **Format** | [Moderated remote via Zoom / in-person on-device], [device] |
| **Participants** | N=[main] + [alternates] — [screening criterion] |
| **Stimulus** | [Prototype platform]; primary [link], backup [link] (use only if main fails) |
| **Goal** | [1–2 sentence research goal] |

---

## Session Flow Overview

[One-cell at-a-glance agenda table listing every timed phase, summing to the session length — attested in IC4B and Bad Addresses. Build it whenever the researcher wants an agenda up top.]

| Time | Phase |
|------|-------|
| [3 min] | Introduction |
| [5 min] | Background |
| [X min] | Prototype Tasks — Flow 1 … Flow N |
| [X min] | Comparisons / Recap (if applicable) |
| [2 min] | Wrap-Up |

---

## Objectives & Research Questions

[Study-background / problem paragraph — what prompted this round.]

**Topic 1 — [feature/flow]**
- *Hypothesis:* [what we expect]
- **[P0]** [prioritized objective]
- **[P1]** [secondary objective]
- *Key Questions:* [the questions this topic answers — NOT read aloud]

**Topic 2 — [feature/flow]**
- *Hypothesis:* …
- **[P0]** …

---

## Pre-Session Checklist

[Shared scaffolding — bullets with ☐. Include prototype-specific items:]
- ☐ Participant validated — [screening criterion]
- ☐ Prototype loaded & tested — primary link opens; backup ready
- ☐ Device — [participant on their own device / remote-control handoff confirmed]
- ☐ Recording armed · consent script ready · observers cameras-off · Slack channel open (vendor)

---

## Consent + Recording + Think-Aloud Script — READ VERBATIM (~90 sec)

[2-col table, Cue | Read aloud. Shared consent lines PLUS the two prototype-mandatory additions:]

| Cue | Read aloud |
|-----|------------|
| **Open** | "Hi [name], thanks for joining. I'm [moderator] — [independent-researcher framing: "I don't work for Instacart and didn't design what you'll see, so please be totally candid."]" |
| **No right answers** | "There are no right or wrong answers — we're testing the designs, not your abilities. If something's confusing, that's the design's fault, not yours." |
| **Think-aloud** | "As you go, please think out loud — put your brain on speakerphone. Tell me what you're looking at, what you expect, what surprises or confuses you." |
| **Prototype caveat** | "These are early prototypes, so some things may not be clickable and some text is placeholder. If something doesn't work, just tell me what you'd expect to happen." |
| **Recording** | "With your permission I'd like to record audio, video, and screen — it stays internal. **Is that okay?**" |
| **Observers** | "A couple of colleagues may be observing silently to take notes." |
| **Open floor** | "Any questions before we start?" |

> Wait for an explicit verbal **"yes"** before recording. Demo the think-aloud with a quick everyday example before Task 1.

---

## Background / Warm-Up (~[X] min)

**Goal:** Profile shopping habits and prior familiarity to contextualize the tasks — before any stimulus.

**Probes to use:** Echo · Tell-Me-More · Critical Incident ("the last time…") · Specificity

| # | Ask |
|---|-----|
| **Q1** | "Who usually does the grocery shopping in your home, and how?" |
| **Q2** | "How often do you shop in-store versus online?" |
| **Q3** | "Have you used [product/feature under test] before? Tell me about that." |
| **Setup** | "[Tech handoff — I'm going to give you remote control / hand you the device now.]" |

---

## Prototype Tasks (~[X] min) — CORE

[PROSE: name the experimental design here if any — between/within-subjects, counterbalance grid in arrow notation. Then the flows.]

### Flow 1 — [name] (~[X] min)

**Stimulus:** [PROTOTYPE link] · [Screen range]
[Optional 1-line watch-for in prose.]

| # | Ask / Do |
|---|-----|
| **Scenario** | "Imagine you wanted to [goal, not UI]. Show me how you'd do that." |
| **[Feedback]** | "Before you do anything — what's going on on this screen? What would you do here?" |
| **Task** | "Now go ahead and [directed task]." |
| **[Mod / WoZ]** | *[Stage direction — not read aloud: e.g. "Mod: tap lower-left to trigger the prompt", or a behavior fork "[If they remove the item] → note whether they search or re-watch instructions".]* |
| **[If they get stuck]** | "What would you expect to happen? What would you try next?" |

> **Observation cues (moderator, not read aloud):** Do they [target action]? (yes/no) · If not, what do they do instead? · Any hesitation or concern?

**Post-task (reuse verbatim after every flow):**
| # | Ask |
|---|-----|
| **R1** | "In your own words, what did you just do?" |
| **R2** | "What felt easy or hard about that, and why?" |
| **R3** | "On a scale of 1–5, 1 = difficult and 5 = easy, how would you rate that? Why?" |

### Flow 2 — [name] (~[X] min)

[Repeat the pattern.]

---

## Comparisons (~[X] min) — *multi-variant studies only*

| # | Ask |
|---|-----|
| **C1** | "Thinking about [Option A] and [Option B] — which felt easier, and why?" |
| **C2** | "Which would you rather use for [goal]?" |

---

## Cross-Flow Recap (~[X] min) — *optional*

| # | Ask |
|---|-----|
| **Recap1** | "When would you use [X] versus [Y]?" |
| **Recap2** | "Anything still confusing after going through all of that?" |

---

## Wrap-Up (~[X] min)

| # | Ask |
|---|-----|
| **W1** | "Thinking back over everything, what mattered most to you?" |
| **W2** | "What was the most confusing part?" |
| **W3** | "Anything I didn't ask about that I should have?" |
| **Close** | "[Moderator: check Slack for stakeholder follow-ups.] Thank you so much — [confirm incentive + next steps]." |

---

## Post-Session Debrief

[Shared scaffolding — numbered list, within 5 min of end:]
1. **Task outcomes:** per flow — ☐ completed unaided · ☐ completed with help · ☐ failed — one-line why
2. **Top friction point:** the single most diagnostic breakdown + which screen
3. **Most diagnostic verbatim quote:** one sentence, exact words

---

## Communication & Deliverables — *vendor-run only*

**Communication.** Day-of questions run through a shared **Slack channel**; moderator checks it before each wrap-up. **EOD update:** participant composition + 3–5 top takeaways (framed as "a creative exercise, not conclusions") + 1–2 paraphrased quotes.

**Deliverables.** [Express Research Summary — 3–5pp doc or 10–20-slide deck on the Instacart template, draft [date] / final [date].] · [Session recordings — shared drive, 1–5 business days, PII removed.] · [Report readout — remote presentation, [date].]

**Timeline** *(optional 3-col table: Description | Owner | Date).*
```

**IMPORTANT:** the guide ends at the Post-Session Debrief for internal studies, or at Communication & Deliverables (+ Timeline) for vendor-run studies. No Master Probe Bank, Bias Checklist, or Self-Critique inside the doc.

---

## Prototype-specific content-generation rules

1. **Tasks describe goals, not UI.** "Find a way to add these items" — never "click the green Add button." (NN/g)
2. **Every task row carries an observation cue in prose below the table**, in the form: `Do they [action]? (yes/no) · If not, what do they do instead? · Any concerns?` Never put cues inside the task cell.
3. **Scenario framing is a first-person "Imagine you…"** setup that gives context without leading to the answer.
4. **Feedback-then-Task pattern** on first-impression screens: unaided reaction row ("what's going on here?") *before* the directed task row.
5. **Think-aloud is scripted with the house metaphor** ("put your brain on speakerphone") and always paired with the **prototype-limitations caveat**.
6. **Experimental design is stated in prose in the task-section header**, not in cells: between-/within-subjects, counterbalanced order, or a numbered counterbalance grid in arrow notation when order matters.
7. **Behavior forks and moderator/WoZ triggers** are bracketed stage directions in prose or a labeled row: `[If they remove the item]`, `[Fork 1 / Fork 2]`, `[Mod: tap lower-left to trigger the prompt]`.
8. **Ratings are lightweight, bespoke, and reused verbatim** across flows for comparability — a single 1–5 ease scale or a named bipolar scale. No SUS/SEQ.
9. **Prototype references are inline links labeled `[PROTOTYPE]`**, with a top **Links row** (Google Folder · Figma · Participant Grid · Screener). Reference screens by `[Screen N]` tags in screen order.
10. **Timing is annotated in every section heading** and a one-cell **Session Flow Overview** agenda table up top is encouraged, summing to the session length.
11. **Objectives carry P0/P1 labels and hypotheses**; they live in the Objectives section, never in the task tables.

---

## House-style notes (prototype guides)

- Doc-type label: **"Research Plan"** when Instacart-authored/internal; **"Discussion Guide"** when agency-authored/vendor-run.
- A **Table of Contents** (bolded prose list + one-line description per section) is used in agency guides; optional for internal.
- Vendor back-matter (Communication, Deliverables, Timeline) is set off by horizontal rules as bold run-in headers, with dated milestones and the "takeaways are a creative exercise, not conclusions" guardrail on EOD updates.
- Screenshots may be embedded in the stimulus context in screen order; when building natively, reference screens by name/number and link the prototype rather than embedding images unless the researcher supplies them.
