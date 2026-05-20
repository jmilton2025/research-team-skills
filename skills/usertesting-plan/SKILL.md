---
name: usertesting-plan
description: Design a UserTesting research plan (study-level structure) for any unmoderated test. Use this skill when asked to "write a UserTesting plan," "design a research plan," "set up a study structure," "scope a UserTesting study," or to decide task count, ordering, coverage levels, stimulus type, or end-of-session synthesis questions. Outputs a research plan with task breakdown, ordering rules, stimulus type per task, synthesis tail, and a 3-layer triangulation checklist. Universal — works for any topic, not just recipes.
metadata:
  type: skill
---

# UserTesting Plan Skill

Design the study-level structure of a UserTesting research plan. This skill owns task count, task order, coverage levels, stimulus type per task, synthesis questions, and the discipline rules that keep a plan defensible.

For question-level wording, the script document, and platform-tagging discipline, hand off to [[usertesting-script]]. For the visual stimuli HTML, hand off to [[usertesting-html]]. For the full plan→script→HTML pipeline, use [[usertesting-orchestrator]].

## When to use this skill

Invoke whenever the request is about **study design** rather than question wording or visuals. Trigger phrases:
- "Write/design a UserTesting plan"
- "Scope a research plan"
- "How many tasks should this study have?"
- "What's the ordering for these tasks?"
- "Help me set up coverage levels"
- "Draft the end-of-session synthesis questions"
- "Audit this study plan"

## Intake — ask these BEFORE writing

Never start drafting without resolving the six intake questions. If the user did not provide them, ask in a single message, no more than 4 at a time:

1. **Subject matter** — what is being tested? (e.g., recipe-to-cart mapping, checkout flow, onboarding)
2. **Failure modes** — what specific UX problems are in scope? (missing items, substitutions, quantity mismatch, etc.)
3. **Coverage / variation set** — how many distinct conditions? (e.g., 100/80/40 baseline-to-failure variants)
4. **Stimulus type** — what visual will participants see? (dual-phone, two-cart comparison, single-row card, ingredient-list-only, single-cart-annotated)
5. **Session length budget** — how many minutes? (default: ~15 min for unmoderated)
6. **Group split** — is this one study or split into A/B groups testing different failure-mode families?

## Core rules

### Task design

1. **Test ONE failure mode per task.** Mixing failure modes in one task makes results uninterpretable. If two modes are entangled, split into two tasks.
2. **Baseline first.** The 100%-success / control task always runs FIRST so participants form a "this is what success looks like" mental model.
3. **Wrong-item / unprompted-detection task runs LAST.** Participants must not be primed to look for errors.
4. **Randomize the middle, fix the bookends.** First task fixed (baseline); last task fixed (wrong-item or capstone); middle tasks randomized to control fatigue/order effects.
5. **Fixed slots for novel-signal tasks.** Tasks that test a specific platform signal (e.g., a new label or warning) run in fixed slots so every participant sees them in the same context.
6. **Sequence cross-task comparison pairs back-to-back.** When two tasks test variations of the same concept (e.g., quantity-too-low and quantity-too-high), place them adjacent in fixed order so participants naturally compare.
7. **Warm-up before cart tasks.** If the study tests action-on-content (e.g., recipe-to-cart), run a content-only warm-up (no action) before any action task. Surfaces baseline expectations.

### Stimulus type selection

| Goal | Stimulus type |
|---|---|
| Compare what was asked vs. what was delivered | Dual-phone side-by-side (asked left, result right) |
| A/B substitution-strategy preference | Two-cart side-by-side, randomize L/R |
| Test a single UI signal (label, warning, badge) | Single cart with the signal visible, no comparison |
| Isolated substitution decision | Single-row card (asked → delivered, no full cart) |
| Pre-action expectation-setting | Content-only screen (no action available) |

### Synthesis tail (end-of-session block)

Include 3–5 synthesis questions AFTER per-task questions, BEFORE demographics:

1. **Recap MULTI-SELECT** — "Which would you no longer use / shop / continue?" + include "None — I would still use all of them" as an option.
2. **Verbal "why?"** — immediately after the multi-select. Forces commitment before rationalization.
3. **Pain-point question** — choose ONE format based on the measurement goal:
   - **DRAG-TO-RANK forced ordering** if the goal is to detect hierarchy
   - **SINGLE CHOICE with escape option pinned last** if the goal is to detect a single biggest pain point AND measure indifference
   - **VERBAL ranking with options on-screen** if the list is ≤6 items and reasoning is part of the signal (collapses single-choice + verbal-why into one slot)
4. **Detection timing question** — "When would you notice this?"
5. **Directive closing prompt** — never generic. Ask 2–3 specific things (e.g., "What would you improve? What would make this easier? What features did you wish worked differently?"). ~60 sec.

### Discipline rules

- **No conditional logic.** Every participant sees every question in the same form. No branching, no skip logic.
- **Personal-preference caveat in intro.** Required wording (adapt to subject): *"These [items] are just examples for the study. Please answer based on what's in the [interface] and how it's working — not on whether you personally like or have a preference for the content. Imagine you're [using this on behalf of] someone who [is engaged with all of these]."*
- **Demographics at the END, never the start.** Form-filling mindset at the start contaminates UX responses.
- **Warm-up framing is intentional.** Decide per study whether the warm-up sits as (a) a Pre-task block (clearer for analysis) or (b) Task 1 (clearer for programmer handoff). Pick one per study and document the choice in the script header.

### Add-on absorption discipline

When the team adds questions mid-study, classify each before fielding:

- **(a) Absorb** into existing study — fits the instrument and timing
- **(b) Hold** for a future round — requires a different instrument, recipe, or sample
- **(c) Reject** — duplicates existing question or doesn't serve the research question

Document the rationale per question — not just the decision. Cuts get a future home so they're not lost.

### 3-layer coverage-audit triangulation

Before fielding, audit three layers in parallel:

- Layer 1: **Master Research Plan** — source of truth for what's being measured
- Layer 2: **Group Test Plan / Script** — what participants will experience
- Layer 3: **Stimuli HTML** — what participants will see

Use parallel sub-agents (one per layer comparison) for independent verification. Document accepted divergences in the script header — do NOT auto-reconcile the master unless explicitly told. Some divergences are intentional (e.g., recipe swap, simplified screen count).

## Standing preferences

- **Show 2–3 approaches before significant edits.** Don't pick one and run with it by default.
- **Label pending vs. live edits clearly.** Use `v2-queued (not pushed)` vs. `v1-live (in Google Doc)` markers. Don't cite pending changes as canonical.
- **Frame ambiguous structural decisions BEFORE pushing.** Surface 2–3 options and wait for confirmation, even if the "right" answer seems obvious. Structural ambiguity compounds quietly (wrong task count → wrong randomization → wrong session length).
- **Visual consistency over methodological purity — document the tradeoff.** When a design choice that improves visual consistency competes with a methodology constraint, favor consistency BUT document the methodology that was traded away AND flag the affected metric for special handling at analysis. Participants notice visual inconsistency before they engage with content; an odd-one-out task contaminates more data than the methodology compromise does.
- **Flag every mismatch explicitly, never silently skip.** When something can't be added or doesn't match the spec, flag it with reason + suggested action + decision request.
- **Auto-open created deliverables in browser.** After generating any plan doc, open it.

## Output structure

The plan deliverable contains these eight components, in order:

1. **Header block** — Subject, length budget, group split, sample size, fielding window
2. **Coverage matrix** — table of variation × task showing which failure mode each task isolates
3. **Task list** — numbered Q1–QN tasks with stimulus type, what's being measured, fixed-vs-randomized slot, time budget
4. **Stimulus-type appendix** — for each unique stimulus type, what it shows and why
5. **Synthesis tail** — the 3–5 end-of-session questions with format + escape options
6. **Discipline notes** — randomization rules, intro caveat, demographics placement, warm-up framing decision
7. **Add-on register** — any add-on questions classified as Absorb / Hold / Reject, with rationale
8. **Triangulation checklist** — 3-layer audit assignments (Master ↔ Plan ↔ HTML)

## Workflow

1. Run the 6-question intake. Wait for answers.
2. Show 2–3 task-ordering approaches (e.g., baseline-fixed + 4-randomized + capstone-fixed vs. 2 fixed bookends + 3 randomized middle). Wait for selection.
3. Draft the coverage matrix.
4. Draft the task list with per-task stimulus type.
5. Draft the synthesis tail using the format that matches the measurement goal.
6. Run the add-on absorption pass if there are pending add-on questions.
7. Output the plan in the 8-component structure above. Auto-open if it was written to a doc.

## Bundled resources

- `references/coverage-matrix-template.md` — blank coverage matrix to fill in
- `references/intake-checklist.md` — the 6 intake questions and how to disambiguate answers
- `references/synthesis-tail-templates.md` — pre-written templates for each pain-point format
- `references/decision-log-template.md` — Absorb/Hold/Reject log format

## Hand-offs

- For question wording and platform tagging → invoke [[usertesting-script]]
- For visual stimuli HTML → invoke [[usertesting-html]]
- To run the full pipeline plan→script→HTML in order → invoke [[usertesting-orchestrator]]
