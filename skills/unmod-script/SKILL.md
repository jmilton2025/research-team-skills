---
name: unmod-script
description: Use when a UX researcher needs to draft the task list and instructions for an unmoderated usability test that participants complete on their own, with no moderator present (UserTesting, Maze, or a similar self-serve tool). Triggers on "write an unmoderated script", "draft an unmod test", "self-serve task list", "unmoderated instructions", or "/unmod-script".
---

# Unmoderated Test Script Builder

Drafts the plain-language task list and instructions a participant works through alone, with no researcher present to clarify, redirect, or rescue confusion. Grounded in Steve Portigal's *Interviewing Users* (rapport and question-design principles adapted to a self-guided format), Erika Hall's *Just Enough Research* (right-sizing scope, answer-led framing), Tomer Sharon's *Validating Product Ideas* (concept-comparison design), Nikki Anderson's *User Research Academy* (plain-language question construction), Nielsen Norman Group's remote and unmoderated-testing guidance, the UserTesting Blog's task-writing conventions, and dscout People Nerds. Also applies the Instacart-internal **AIxUXR Playbook**'s H.E.A.R.T. framework where relevant.

### Guiding philosophy — H.E.A.R.T. (AIxUXR Playbook)

| Letter | Principle | What it means when there's no moderator in the room |
|--------|-----------|-------------------------------------------------------|
| **H** | **Human-centered** | The participant is alone with the screen. Every instruction has to carry the warmth and reassurance a moderator would normally provide in the moment. |
| **E** | **Experience-focused** | A confusing instruction doesn't get caught and corrected live — it just produces bad data or a dropped session. The script *is* the moderator. |
| **A** | **Amplifying** | AI drafts the task flow; the researcher validates it against the actual research questions and pilots it before fielding. |
| **R** | **Responsible** | No PII in stimuli or scenarios. Flag anywhere a task could produce a distressing or unsafe outcome for a participant working alone. |
| **T** | **Transparent** | The researcher stays the accountable author. Disclose AI-assisted drafting to stakeholders per team norms. |

## When to use this skill

Use this skill when a researcher needs a self-serve, no-moderator-present task list — the document a participant reads and follows entirely on their own. It sits in the **DIY research pipeline**: it runs after `/screener` (which defines and recruits the right participants) and its output feeds into `/diy-packet` (which bundles the screener, this script, stimuli, and launch instructions into one shareable package for a self-serve requester).

Trigger phrases:
- "/unmod-script"
- "write an unmoderated test script"
- "draft the task list for a self-serve study"
- "write instructions for a UserTesting study" (plain-language task list, not the platform-tagged question doc — see Differentiation below)
- "help with an unmoderated usability test"
- "turn this PRD into a DIY test"

### Differentiation from related skills

- **`usertesting-plan` / `usertesting-script` / `usertesting-html` / `usertesting-orchestrator`** own the *platform-mechanics* layer of a UserTesting build — 4-way question-type tagging to dodge the platform's Written-Response bug, action-ladder ordering, stimulus HTML, cross-artifact triangulation. This skill owns the *participant-facing narrative* layer — the plain-language words a person reads with nobody there to explain them. A study can use both: draft the task list here first, then hand the approved task list to `usertesting-script` if it needs full platform-tagging rigor for a heavily-instrumented build.
- **`mod-guide`** is this skill's moderated counterpart — same underlying research questions, but written for a moderator to read aloud and adapt live. Where `mod-guide` can leave room for improvisation ("probe if it feels relevant"), this skill cannot: every branch, fallback, and clarification has to be written out in advance, because nobody is there to improvise one.
- **`research-plan`** owns the study-level why (objectives, hypotheses, methodology, timeline). This skill assumes that's already settled — either from a research plan doc or from `/screener` — and turns it into the moment-by-moment participant experience.

## Step 1 — Gather Study Inputs

Ask the researcher to share whatever they have. Accept any format:

> "To draft your unmoderated script, share what you've got — a PRD, a research plan, the output from `/screener`, a Slack thread, or just a plain description of what you're testing. If you have a Google Doc link, paste it and I'll pull the structure."

Extract, or ask directly if missing:
1. **What's being tested** — a live product, a prototype/mockup, or a side-by-side concept comparison
2. **Research questions** — what the study needs to learn (pull from a linked research plan if one exists)
3. **Participant profile** — who's taking this (often already defined by `/screener`)
4. **Session length budget** — total minutes available
5. **Stimuli** — what the participant will actually see (link, prototype, static images) and how many distinct scenarios/items
6. **Platform** — which self-serve tool will this run on (UserTesting, Maze, other)?

Do not invent study details. If something's missing and can't be inferred, ask — don't guess at a research question or a participant profile.

If a hard gate blocks the script from being launch-ready (e.g., no stimulus link yet), don't invent an ad hoc status line — use the shared `Status: BLOCKED — <reason>` convention in `../../references/output-status-and-labeling-conventions.md` (§1).

Scope note: variant assignment, order, and counterbalancing across items a participant sees are this skill's territory -- not /screener's. /screener only defines who qualifies and the recruiting-pool quotas; it does not assign which variant(s) a given participant sees or in what order.

## Step 2 — Propose the Task Structure

Before drafting full instructions, propose a compact reference table so the researcher can sanity-check scope in one glance — this is also the artifact a designer or PM stakeholder skims first.

| Task | Participant Goal | Key Research Question |
|------|------------------|------------------------|
| Task 1 — [name] | [what the participant is trying to do] | [what this task tells us] |
| Task 2 — [name] | [...] | [...] |

Two study shapes call for slightly different table content:

- **Sequential task flow** (participant moves through a product end to end) — one row per task, ordered as the participant will experience them.
- **Concept / side-by-side comparison** (participant reacts to paired stimuli, item by item) — one row per item or item category, not per interaction step; note which comparison each row is testing.

**Typical task count:** 5–8 sequential tasks, or 4–6 item/category blocks for a comparison test. Fewer than 4 tasks/items, when more could reasonably be tested, rarely justifies a full build; more than 8-10 tasks risks fatigue with nobody there to notice a participant disengaging partway through.

**Randomization / order:** For any study where a participant sees 2 or more items/tasks in sequence, specify how order will be randomized or counterbalanced across participants — or that order is intentionally fixed, and why — before drafting the full script. Order effects (fatigue, memory bleed from one item coloring the next) are a real risk in a within-subject design, with nobody there to notice a participant tiring or drifting partway through. This extends the same neutrality principle used in the comparison template below: however positions are labeled (e.g. "Version A" / "Version B"), the label must track ORDER (first-shown / second-shown), never fixed item IDENTITY (e.g. never permanently "Version A = current version") — otherwise the counterbalancing this field exists to enable gets silently undone by identity-based labels.

Present the table and ask:

> "Does this scope look right? Anything to add, cut, or reorder before I write the full script?"

## Step 3 — Researcher Approves Structure

Confirm before drafting the full instructions. If the researcher wants to adjust task count, order, or scenario framing, revise the table and re-confirm rather than drafting ahead of approval.

## Step 4 — Draft the Full Script

Generate the participant-facing document using the OUTPUT TEMPLATE below. Apply every rule in `references/unmod-writing-rules.md` — this is the file that captures what changes when nobody is present to clarify a confusing moment.

### The shape every unmoderated script follows

1. **Welcome & context-setting** — states plainly that the participant isn't being tested, that there are no right or wrong answers, that they should think out loud / narrate as they go, that confusion is useful signal worth saying out loud, and how long the session will take.
2. **Warm-up / behavioral baseline** — a small number of general questions about the participant's existing habits in the relevant domain, asked *before* any scenario framing so answers aren't primed by what they're about to see. Coming before the scenario isn't enough on its own: a warm-up question's own *content* can still prime the exact concept a later task is trying to measure unprompted (e.g., asking about "running low / out of stock" experiences right before a first-glance task that measures whether a screen communicates that same concept). Check every warm-up question against the study's actual comprehension/first-impression target, not just against the scenario transition — if a warm-up question names the concept the task is trying to measure cold, rewrite it to a more general framing or move it to after that specific task.
3. **Scenario transition** — a short, realistic narrative that sets up why the participant is about to do what they're about to do, without revealing what the study is trying to find out.
4. **Launch instruction** — an explicit, unambiguous instruction to open the stimulus (link, prototype, image set), with nothing assumed about how they'll find it.
5. **First-impression capture** — before any interaction, ask what they notice, what stands out, what surprises them. This is the one moment that disappears the instant a participant starts clicking, so it has to be captured deliberately.
6. **Task blocks** (sequential studies) — each task opens with an **anchor**: a plain statement of where the participant should now be ("You should now be viewing…"). This is the single most important unmoderated-specific device — it re-orients anyone who got lost, with no moderator around to notice or fix it. Each block then moves observation → interpretation → intended action → reflection, using questions that describe goals, not interface elements. Add a one-line fallback for any step where the participant might get stuck or a UI element might not behave as expected.
   
   **Comparison blocks** (concept/side-by-side studies) — each block opens with a short scenario-setting statement per item, then pairs a comprehension/clarity check (fixed choices, e.g. "left is clearer / right is clearer / about the same / not sure") with an open-ended "why did you choose that" follow-up, then a behavioral-intent question (fixed choices reflecting the real decision the concept is meant to support) with its own "why" follow-up. Add a confidence rating scale (5-point, "not at all confident" → "extremely confident") only where the research question is specifically about trust or reassurance.
7. **Synthesis & wrap-up** — reflective questions across the whole session: how the experience compares to expectations, whether anything felt confusing at any point, what they'd tell a friend, the single biggest thing they'd change.
8. **Warm closing** — a genuine, specific thank-you. Not a form-letter close.

### What "success" means per task

Unmoderated scripts rarely define hard pass/fail criteria the way a usability test with an observer might. Instead, each task or block carries a **key research question** (from the Step 2 table) that the questions are built to answer — comprehension, confidence, preferred framing, intended action. Write task questions so the researcher can read the raw responses afterward and answer that question directly, without having to infer it. Completion of the task (the participant reaching the end of the flow) is a separate, secondary signal from whether they understood or felt confident along the way — don't conflate the two in the questions themselves.

---

## OUTPUT TEMPLATE

```
# [Study Title — plain description of what's being tested]

**Study:** [one line — what this covers]
**Platform:** [UserTesting / Maze / other self-serve tool]
**Estimated length:** [X] minutes
**Randomization / order:** [how task/item order is randomized or counterbalanced across participants, or "Fixed order — no randomization" if intentionally fixed]

---

## Task Summary (Reference Table)

| Task | Participant Goal | Key Research Question |
|------|------------------|------------------------|
| Task 1 — [name] | [goal] | [question] |
| Task 2 — [name] | [goal] | [question] |
[...]

*[Count check: 5–8 rows (sequential) / 4–6 (comparison) is typical — see Step 2's heuristic. Fewer is fine if genuinely warranted; don't pad just to hit a number.]*

---

## Full Script

### Welcome

Hi there — thank you so much for joining us today!

A few quick things before we start:
- **You're not being tested.** We're testing a product experience — there are no right or wrong answers.
- **Please think out loud** as you go. Tell us what you're noticing, wondering about, or feeling.
- **If something feels confusing or unclear, say so.** That's useful, not a problem.
- This should take about **[X] minutes**. Go at your own pace.

### Warm-Up Questions

1. [General habit question — domain-relevant, non-priming]
2. [General habit question]
3. [Familiarity/frequency question relevant to the study]

### Scenario Transition

[Short, realistic "Imagine this…" framing that sets up the task without revealing what's being measured.]

### Launch

Please click the following link to begin: **[LINK]**

Take a moment to look around before doing anything. We'll guide you from there.

### First Impression

Before clicking on anything, just look at what's in front of you.
- What's your first impression?
- What do you notice right away?
- Is there anything that surprises you?

*[For multi-stimulus studies, repeat this First Impression prompt inside each item block below, not just once here.]*

---

### Task 1 — [Name]

**Anchor:** You should now be viewing [the specific screen/state].

[1-2 sentences framing the goal in plain, non-jargon language.]

1. [Observation question]
2. [Interpretation question]
3. [Action instruction, if any]
4. [Reflection question]

*[If a fallback is needed: "If you don't see X, do Y instead."]*

[Repeat per task, each opening with its own Anchor line.]

---

### Final Synthesis & Wrap-Up

1. Looking back at the full experience, how would you describe it in your own words?
2. Were there any moments you weren't sure what was happening or what to expect next?
3. How did this compare to what you expected going in?
4. If a friend were about to try this, what would you want them to know?
5. If you could change just one thing, what would it be?

### Closing

Thank you so much for your time and honest perspective today. Your feedback directly shapes what real customers experience — we're genuinely grateful you took part.
```

### Comparison / multi-variant blocks (swap in for Task blocks)

These two shapes answer genuinely different research questions — pick based on the Key Research Question in the Step 2 table, not just on how many items there are.

**Required step — do not skip:** Do not trust an upstream-asserted comparison shape at face value, even if multiple upstream documents (plan, screener) state it identically — always re-derive the shape yourself from the actual Key Research Question text before drafting. Two documents repeating the same label is not independent confirmation; they likely both inherited it from the same source.

#### (a) Relative preference (2-way pick-a-favorite)

Use when the research question is "which do you like better" and there are exactly 2 items being compared head-to-head.

```
### [Item / Category Name] — [archetype or grouping label, if used]

**Scenario:** [One line setting up what the participant is choosing/configuring for this item — no reference to which version is "new" or "better."]

Looking at [the two versions / the screen], which gives you a clearer sense of [the thing being evaluated]?
- The [first] version is clearer
- The [second] version is clearer
- They feel about the same
- I'm not sure

Why did you choose that answer? [open-ended]

Given what you saw, what would you actually do?
- [Option A — matches the real decision this concept supports]
- [Option B]
- [Option C]
- I'm not sure

Why did you choose that answer? [open-ended]

*[Only where trust/reassurance is the specific research question:]*
How confident are you that [specific outcome]?
- Not at all confident · Slightly confident · Moderately confident · Very confident · Extremely confident
```

#### (b) Independent per-item comprehension (N-way absolute check)

Use when the research question is "do you understand/react to each one on its own" — independent comprehension, not relative preference — for 3 or more items (or 2, if no direct comparison is wanted). Each item gets its own self-contained task: show that item alone, ask about it alone, then move to the next. Repeat the full block once per item — never show two items side by side, and never use comparison language ("clearer than," "the other version," "compared to") inside it.

```
### [Item Name] — [archetype or grouping label, if used]

**Anchor:** You should now be viewing [Item Name].

[One line orienting the participant to this item alone — no reference to any other item or version.]

What does this [item / message / screen] tell you, in your own words? [open-ended comprehension question]

How would you react if you saw this in real use?
- [Option A — reaction/behavioral-intent choice specific to this item, not relative to any other]
- [Option B]
- [Option C]
- I'm not sure

Why did you choose that answer? [open-ended]

*[Only where trust/reassurance is the specific research question:]*
How confident are you that [specific outcome]?
- Not at all confident · Slightly confident · Moderately confident · Very confident · Extremely confident
```

[Repeat once per item.]

---

## CONTENT GENERATION RULES

1. **Every task or block opens with an anchor or scenario-setting statement.** No moderator is present to notice a participant is lost — the script has to do that job. See `references/unmod-writing-rules.md`.
2. **No interface jargon.** Describe goals ("find a way to…"), not UI elements ("tap the blue button").
3. **One instruction per step.** No compound instructions — nobody is there to help a participant untangle a two-part ask.
4. **No leading or loaded questions.** Neutral framing throughout — the scenario transition never hints at what the "right" reaction is.
5. **Concrete over hypothetical.** Prefer questions grounded in what the participant just did or saw over "would you..." speculation. Reserve hypotheticals for the wrap-up only, as a reflection tool.
6. **First-impression capture is non-negotiable** for any study involving a new screen or concept — it's the one data point that can't be recovered once interaction starts.
7. **Write every fallback in advance.** If a step could plausibly break, stall, or behave unexpectedly, write the recovery instruction into the script — don't rely on the participant improvising or a moderator catching it live.
8. **Plain, warm, human language throughout** — the welcome and closing carry real warmth; a flat, procedural tone reads as cold when there's no live moderator's voice to soften it.
9. **Comprehension checks use plausible distractors, not obviously-wrong options** — a multiple-choice comprehension question is only useful if a participant who skimmed the copy could plausibly pick the wrong answer.
10. **Time-box realistically.** Total time in the welcome message should match the actual sum of task times — participants abandon self-serve studies that run long without warning.
11. **Never fabricate a research question or participant profile.** If the source material doesn't specify one, ask the researcher rather than inventing plausible-sounding detail.

---

## Step 4.5 — Self-Critique Checklist

Before returning the draft, check it against `references/unmod-writing-rules.md` in full. At minimum, confirm:

- [ ] Every task/block has an anchor or scenario-setting statement — no step assumes the participant knows where they are.
- [ ] No question requires a moderator's live clarification to be understood as written.
- [ ] First-impression capture exists if any new screen or concept is shown.
- [ ] Every fixed-choice comprehension question has genuinely plausible wrong answers, not throwaway ones.
- [ ] Warm-up questions come before scenario framing, not after.
- [ ] No warm-up question names the specific concept a later task is measuring unprompted (order alone doesn't prevent content-priming — check each warm-up question's wording against every task's comprehension target, not just against the scenario transition).
- [ ] No compound (multi-part) instructions in a single step.
- [ ] Welcome message's time estimate matches the sum of task times.
- [ ] Nothing in the scenario framing tips off the "expected" or "correct" reaction.

## Tool usage

- **AskUserQuestion** — for the approval checkpoints in Steps 1–3 (gathering missing inputs, confirming task structure). See `../../references/interactive-input-conventions.md` (the repo-root `references/` folder) for the fallback if AskUserQuestion is unavailable.
- **google-docs:fetch-google-doc** / Glean `read_document` — read a linked research plan, PRD, or `/screener` output
- **Read** — read pasted content or local files
- The generated markdown is the primary deliverable — polished enough to hand directly to a stakeholder or paste into the self-serve platform's builder
- On request, upload to Google Docs using default formatting and route to the matching project folder — no custom styling pipeline is required for this deliverable

## Hand-offs

- **Before this skill:** `/screener` — defines and recruits the right participants; its output is a primary input here.
- **After this skill:** `/diy-packet` — bundles this script with the screener, stimuli, and launch instructions into one self-serve package.
- **For heavier platform-tagging rigor** (UserTesting-specific question typing, action ladders, stimulus HTML): hand the approved task list to `usertesting-script` / `usertesting-plan` / `usertesting-html`.
- **For the moderated equivalent of this same study:** `mod-guide`.

---

## Sources

| Source | Contribution to this skill |
|--------|----------------------------|
| **Steve Portigal**, *Interviewing Users* | Rapport and question-design principles, adapted from live interviewing to a fully written, self-guided format |
| **Erika Hall**, *Just Enough Research* | Right-sizing scope; answer-led, plain-language framing |
| **Tomer Sharon**, *Validating Product Ideas* | Concept-comparison test design; behavioral-intent question structure |
| **Nikki Anderson**, User Research Academy | Plain-language question construction; avoiding jargon in participant-facing copy |
| **Nielsen Norman Group** | Remote and unmoderated usability testing guidance; task-writing clarity conventions |
| **UserTesting Blog** | Task-writing conventions for self-guided testers on unmoderated platforms |
| **dscout People Nerds** | Participant-experience and engagement conventions for self-serve research |
| **AIxUXR Playbook** (Instacart-internal) | H.E.A.R.T. philosophy applied to a no-moderator-present format |
