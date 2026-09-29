# Prototype / Usability Guide — Template Reference

Load this when the researcher picks **Prototype / Usability** as the guide format (Step 2a / Section 1 > Step 1). It holds the type-specific pieces the skill needs: the extra Section 1 parameters, the Section 2 block sequence, the full OUTPUT TEMPLATE, and prototype-specific content rules. The **shared scaffolding** (Moderation Guide header, ownership block/RACI, parameter table, Pre-Session Checklist, Post-Session Debrief) is assembled from SKILL.md's shared-scaffolding section. Consent/think-aloud is handled as a short **read-aloud Introduction list** (see Section 2), not a standalone Consent table.

> **Format rule (Jedida, 2026-09-24):** in a prototype/usability guide the read-aloud Introduction and every phase/task, comparison, and recap block render as **bold-label lists** (`- **Label:** "line"`), never Cue tables. The **only** two tables the guide keeps are the top **Parameter dashboard** and the **Session Flow** agenda.

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

Walk these blocks in order, each shown as a draft → approved → locked before the next, labeled `Section 2 > Step N of M`. M = the number of blocks this study actually has.

**Pop-up rule:** Pop-ups only for the Phases (core blocks). Background & Warm-Up and Wrap-Up are auto-generated — no pop-up, no approval gate.

1. **Objectives & Research Questions** — study-background paragraph, one bold sub-header per Topic/feature, each with a hypothesis, P0/P1-labeled objectives, and "Key Questions." **Auto-generated — no pop-up.**
2. **Session Flow** — simple phase list (Introduction → Background & Warm-Up → Phase 1 → Phase 2 → Phase 3 → Wrap-Up). No minute-by-minute breakdown. **Auto-generated — no pop-up.** *(Rendered as a table — one of the two tables a prototype guide keeps.)*
3. **Introduction & Think-Aloud Setup (read aloud)** *(no pop-up)* — a short **bold-label list** (`- **Cue:** "read-aloud line"`), NOT a table: welcome, what-we'll-do, think-aloud ("brain on speakerphone"), prototype/stimulus caveat, control, and — for sensitive / health-adjacent studies — a recording-(and observation-)consent line. Auto-generated from template.
4. **Background & Warm-Up** *(no pop-up)* — simple numbered questions (Q1, Q2, Q3), no table format, no "Probes to use" header. Observation cues in prose at end. Auto-generated from template.
5. **Phases (the core)** — **one block per phase / stimulus** from the approved P5 list. Named Phase 1, Phase 2, Phase 3 — simple, consistent. Each: stimulus link, question prompts as a **bold-label list** (`- **Cue:** "ask/do line"`) — **not a table** — with observation cues in prose below. **Pop-up for each phase.**
6. **Wrap-Up** *(no pop-up)* — standard 3-question numbered close. Auto-generated.
7. **Communication & Deliverables (+ Timeline)** *(vendor-run only)* — Slack channel, EOD update spec, deliverables with dates.

The shared scaffolding (Moderation Guide header, RACI block, parameter table, Pre-Session Checklist, Post-Session Debrief) is assembled around these per SKILL.md.

---

## OUTPUT TEMPLATE — Prototype / Usability

> **Core principle:** the moderator's eye should land on a **bold-label list holding only what to say or do** — scenario setup, tap directives, first-impression prompts. Objectives, hypotheses, experimental-design rationale, observation cues, and methodology all live in **prose or front-matter, never inside the list.** Only the Parameter dashboard and the Session Flow agenda are tables. Target length **~6–8 pages.**

```
# Moderation Guide

## [Study Title — e.g. "Caper Cart Round 4: Checkout Sprint"]

*[Month Year]*

- **Responsible:** [Name] (Role) — `[TBD — fill in]` if unconfirmed
- **Accountable:** [Name] (Role)
- **Consulted:** [Designer, UXR, PM, EM]
- **Informed:** [partners, stakeholders]

**Links:** [Google Folder] · [Figma / Prototype] · [Participant Grid] · [Screener]

| Parameter | Detail |
|-----------|--------|
| **Study Type & Format** | Moderated [usability test / concept test / cognitive interview] — [in-person / remote via Zoom / on-device] |
| **Duration** | [X] minutes |
| **Participants** | N=[N] — [screening criterion] |
| **Stimulus** | [Link to stimulus — Phase A: [link] · Phase B: [link]] |
| **Goal** | [1–2 sentence research goal] |

---

## Session Flow

| Phase | |
|-------|--|
| Introduction & Think-Aloud Setup | |
| Background & Warm-Up | |
| Phase 1 — [Stimulus A name / description] | |
| Phase 2 — [Stimulus B name / description] | |
| [Phase 3 — if applicable] | |
| Wrap-Up | |

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

## Introduction & Think-Aloud Setup (~[X] min) — read aloud

*(Bold-label list — NOT a table.)*

- **Welcome:** "Hi [name], thanks for joining. I'm [moderator], a researcher at Instacart. [1-line purpose — no right/wrong answers.]"
- **What we'll do:** "[Concrete description — e.g. I'll show you some screens / questions and ask you to think out loud.]"
- **[Observers — read only if present]:** "A couple of colleagues may be watching quietly to take notes — cameras off, no interruptions."
- **Think-aloud:** "The most helpful thing is hearing your thoughts as they happen — like putting your brain on speakerphone."
- **Prototype/stimulus caveat:** "This is a draft we're testing — if something doesn't make sense, that's the design's fault, not yours."
- **[Recording (+ observation) consent — required for sensitive / health-adjacent studies]:** "With your permission I'd like to record audio and screen; it stays internal and identifying details are removed. Is it okay to record?"
- **Control:** "About [X] minutes. You can skip anything or stop anytime and still get the incentive. Any questions before we start?"

> Wait for an explicit verbal "yes" to recording before you begin. **Use silence:** after a prompt, give a ~5-second beat before re-asking — don't rescue or lead.

---

## Background & Warm-Up (~[X] min)

1. [Icebreaker / topic-adjacent question — e.g. "Who usually does the grocery shopping in your home?"]
2. [Frequency / behavior question — e.g. "How often do you shop in-store versus online?"]
3. [Familiarity / prior experience question — e.g. "Have you used [product/feature] before? Tell me about that."]
4. [Any session-specific logistics — e.g. "I'm going to give you remote control / hand you the device now."]

**Observation cues:** [What to watch for during warm-up — e.g. does the participant seem comfortable with the device? Any relevant context they surface unprompted?]

---

## Phase 1 — [Stimulus A name / description]

**Stimulus:** [LINK TO STIMULUS A]

*[Experimental-design note in prose here if any — between-/within-subjects, counterbalance order.]*

- **Scenario:** "I'm going to show you [what this is]. As you read / look at it, think out loud — tell me what you notice, what you think, what feels clear or confusing."
- **First impression (unaided):** "Before you do anything — what's your first impression?"
- **[Question prompts]:** [Questions specific to this phase — CP1, CP2, etc.]
- **[If stuck]:** "What would you expect to happen? What would you try next?"

**Observation cues:** [Prose line below the list — e.g. does the participant hesitate? Do they reread? Do they express confusion or confidence?]

---

## Phase 2 — [Stimulus B name / description]

**Stimulus:** [LINK TO STIMULUS B]

- **First impression (unaided):** "Take a look at this version. What do you notice first?"
- **[Question prompts]:** [Questions specific to this phase.]
- **[Comparison]:** "Compared to what you saw before — which feels more accurate / clearer to you? What's different?"

**Observation cues:** [Prose line below the list.]

---

## Phase 3 — [If applicable: e.g. Open-Ended / Comparisons]

**Stimulus:** [Link if applicable, or "No new stimulus — open questions"]

- **[Q1]:** "[Open-ended or comparison question]"
- **[Q2]:** "[Follow-up]"
- **[Q3]:** "[Anything else?]"

[Add or remove phases as needed. Each phase = one stimulus or one set of related questions. Simple naming: Phase 1, Phase 2, Phase 3.]

---

## Comparisons (~[X] min) — *multi-variant studies only*

- **C1:** "Thinking about [Option A] and [Option B] — which felt easier, and why?"
- **C2:** "Which would you rather use for [goal]?"

---

## Cross-Flow Recap (~[X] min) — *optional*

- **Recap1:** "When would you use [X] versus [Y]?"
- **Recap2:** "Anything still confusing after going through all of that?"

---

## Wrap-Up (~[X] min)

1. Thinking back to everything we've discussed, is there anything you didn't get a chance to share that you'd like to?
2. Do you have any questions for me?
3. Thank you again for your time today! [Confirm incentive + next steps.]

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
2. **Every phase carries an observation cue in prose below the list**, in the form: `Do they [action]? (yes/no) · If not, what do they do instead? · Any concerns?` Never put cues inside a list item.
3. **Scenario framing is a first-person "Imagine you…"** setup that gives context without leading to the answer.
4. **Feedback-then-Task pattern** on first-impression screens: unaided reaction row ("what's going on here?") *before* the directed task row.
5. **Think-aloud is scripted with the house metaphor** ("put your brain on speakerphone") and always paired with the **prototype-limitations caveat**.
6. **Experimental design is stated in prose in the task-section header**, not in list items: between-/within-subjects, counterbalanced order, or a numbered counterbalance grid in arrow notation when order matters.
7. **Behavior forks and moderator/WoZ triggers** are bracketed stage directions in prose or a labeled list item: `[If they remove the item]`, `[Fork 1 / Fork 2]`, `[Mod: tap lower-left to trigger the prompt]`.
8. **Ratings are lightweight, bespoke, and reused verbatim** across flows for comparability — a single 1–5 ease scale or a named bipolar scale. No SUS/SEQ.
9. **Prototype references are inline links labeled `[PROTOTYPE]`**, with a top **Links row** (Google Folder · Figma · Participant Grid · Screener). Reference screens by `[Screen N]` tags in screen order.
10. **Timing is annotated in every section heading** and a one-cell **Session Flow Overview** agenda table up top is encouraged, summing to the session length.
11. **Objectives carry P0/P1 labels and hypotheses**; they live in the Objectives section, never in the task lists.

---

## House-style notes (prototype guides)

- Doc-type label: **"Research Plan"** when Instacart-authored/internal; **"Discussion Guide"** when agency-authored/vendor-run.
- A **Table of Contents** (bolded prose list + one-line description per section) is used in agency guides; optional for internal.
- Vendor back-matter (Communication, Deliverables, Timeline) is set off by horizontal rules as bold run-in headers, with dated milestones and the "takeaways are a creative exercise, not conclusions" guardrail on EOD updates.
- Screenshots may be embedded in the stimulus context in screen order; when building natively, reference screens by name/number and link the prototype rather than embedding images unless the researcher supplies them.
