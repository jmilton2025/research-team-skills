---
name: usertesting-plan
description: Design a UserTesting research plan (study-level structure) for any unmoderated test. Use this skill when asked to "write a UserTesting plan," "design a research plan," "set up a study structure," "scope a UserTesting study," "can you scope this out for UserTesting," "put together a research plan before we field this," or to decide task count, ordering, coverage levels, stimulus type, or end-of-session synthesis questions. Outputs a research plan with task breakdown, ordering rules, stimulus type per task, synthesis tail, and a 3-layer triangulation checklist. Universal — works for any topic, not just recipes.
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
- "Can you scope this out?" / "Can you set this up?" (when the surrounding context is an unmoderated UserTesting ask — a PRD, mocks, and a "need signal before X" framing are the usual tells)
- "How many tasks should this study have?"
- "What's the ordering for these tasks?"
- "Help me set up coverage levels"
- "Draft the end-of-session synthesis questions"
- "Audit this study plan"

## Intake — ask these BEFORE writing

Never start drafting without resolving all eight intake questions below. Questions 1–6 shape the study design; 7–8 exist only because the Header block (Output structure, component 1) needs them and nothing else in this workflow collects them — don't skip them just because they feel like logistics rather than research design.

Ask in batches of at most 4. If more than 4 remain unresolved after the requester's opening message, send a second batch of the rest — never cram everything into one message, and never silently drop a question to stay under 4.

1. **Subject matter** — what is being tested? (e.g., recipe-to-cart mapping, checkout flow, onboarding)
2. **Failure modes** — what specific UX problems are in scope? (missing items, substitutions, quantity mismatch, etc.)
3. **Coverage / variation set** — how many distinct conditions, and along which axis or axes? (e.g., 3 failure-mode variants of one treatment; or a 2×3 grid of [treatment] × [failure mode]. Get the axes named explicitly — a bare number like "5 conditions" can't be turned into a coverage matrix.)
4. **Stimulus type** — what visual will participants see? (dual-phone, two-cart comparison, single-row card, ingredient-list-only, single-cart-annotated)
5. **Session length budget** — how many minutes? (default: ~15 min for unmoderated). Flag immediately — before drafting the task list — if the coverage from Q3 looks unlikely to fit; see "Time budgeting" below.
6. **Group split** — is this one study or split into A/B groups testing different failure-mode families?
7. **Sample size** — how many completes? If the requester doesn't have a number, say so explicitly in the header rather than inventing a plausible-looking n (a directional pilot commonly runs n=5–15; a higher-confidence read runs n=30+ — offer both rather than picking silently).
8. **Fielding window** — target field dates, and when results are needed. If this is tight against still having to build the script ([[usertesting-script]]) and HTML ([[usertesting-html]]) after this plan, flag that risk now rather than letting an aggressive date pass through unflagged.

Further disambiguation guidance for vague or jargon-free answers to each question lives in `references/intake-checklist.md`.

## Core rules

### Task design

1. **Test ONE failure mode per task.** Mixing failure modes in one task makes results uninterpretable. If two modes are entangled, split into two tasks.
2. **Baseline first.** The 100%-success / control task always runs FIRST so participants form a "this is what success looks like" mental model.
3. **Wrong-item / unprompted-detection task runs LAST.** Participants must not be primed to look for errors — which assumes every task before it was a success/baseline case. If the study design requires several tasks that each carry a deliberate error (common for failure-mode or trust-erosion studies), true "unprompted" detection is only possible for the first error a participant meets. For every error-task after that, reframe the goal as *does this specific error also get caught / rated as damaging*, not *unprompted detection* — say so explicitly in Discipline notes rather than claiming priming-free detection you didn't actually get.
4. **Randomize the middle, fix the bookends.** First task fixed (baseline); last task fixed (wrong-item or capstone); middle tasks randomized to control fatigue/order effects.
5. **Fixed slots for novel-signal tasks.** Tasks that test a specific platform signal (e.g., a new label or warning) run in fixed slots so every participant sees them in the same context.
6. **Sequence cross-task comparison pairs back-to-back.** When two tasks test variations of the same concept (e.g., quantity-too-low and quantity-too-high), place them adjacent in fixed order so participants naturally compare. State which member of the pair goes first and why (e.g., subtle-then-obvious to avoid anchoring the later judgment, or obvious-then-subtle to calibrate the scale first) — "fixed order" means deliberately chosen and documented, not defaulted.
7. **Warm-up before cart tasks.** If the study tests action-on-content (e.g., recipe-to-cart), run a content-only warm-up (no action) before any action task. Surfaces baseline expectations.

**Precedence when rules 4–6 collide.** Rules 5 (fixed novel-signal slots) and 6 (adjacent comparison pairs) apply first; rule 4 then randomizes whatever middle tasks are left unclaimed. It is a valid, expected outcome for that remaining pool to be empty or down to a single task — most studies with a comparison pair plus a novel-signal task will land there. When it happens, the study is fully fixed-order end to end; say that plainly in Discipline notes rather than describing a fixed-order study as "randomized."

### Stimulus type selection

| Goal | Stimulus type |
|---|---|
| Compare what was requested/expected vs. what was actually delivered/shown | Dual-phone (or dual-screen) side-by-side — expected left, result right. (Grocery example: item asked for vs. substituted item.) |
| Compare two alternative treatments head-to-head (e.g., old design vs. new design, A vs. B) | Two-screen side-by-side, randomize L/R to control position bias |
| Test a single UI signal in context (label, warning, badge, attribute tag) | Single screen with the signal visible, no comparison |
| Isolated decision on one item, decoupled from the full interface | Single-row/single-card view (request → result, no full screen) |
| Pre-action expectation-setting (warm-up) | Content-only screen, no action available |
| Wrong-item / unprompted-detection (the mandatory final task, rule 3) | The same screen type used elsewhere in the study, shown WITHOUT comparison framing and without the error called out — it must be discoverable on its own, not flagged by the stimulus design |

The grocery/cart language above is illustrative, not literal — "screen" can equally mean a cart, a recipe card, an onboarding step, a search results page, or any other interface being tested.

### Time budgeting

Rough per-slot costs for an unmoderated session, used to reconcile requested coverage (intake Q3) against the session length budget (intake Q5) before drafting the task list — do this check as soon as both are known, not after the task list is fully drafted:

| Slot | Typical time |
|---|---|
| Intro / consent | ~30–45 sec |
| Content-only warm-up (no action) | ~45 sec–1 min |
| Single-screen task, no comparison | ~90–120 sec |
| Dual-screen / two-cart comparison task | ~100–130 sec |
| Capstone / unprompted-detection task | ~110–140 sec |
| Synthesis tail (3–5 questions) | ~3–4 min |
| Demographics | ~30–45 sec |

If summing the requested coverage against these ranges pushes the session past the Q5 budget — a near-certain outcome once coverage exceeds ~5–6 conditions in a 15-min session — do not silently cut a condition and do not silently let the session run long. Flag the specific overage (e.g., "this runs ~15.7 min against a 12–15 min target"), then propose a scope option and let the requester choose:

- **Deep-cover fewer conditions this round.** Pick the highest-risk condition(s); hold the rest for a follow-up round via the Add-on register ("Hold").
- **Split into a second study / A-B group.** Only if intake Q6 allows it.
- **Trim the synthesis tail or drop a lower-priority task.** Smallest structural change, but weakens coverage — say so.

### Synthesis tail (end-of-session block)

Include 3–5 synthesis questions AFTER per-task questions, BEFORE demographics:

1. **Recap MULTI-SELECT** — "Which would you no longer use / shop / continue?" (swap the verb for the subject — "trust," "cook from," "shop from," etc. — this is a template, not fixed wording) + include "None — I would still use all of them" as an option.
2. **Verbal "why?"** — immediately after the multi-select. Forces commitment before rationalization.
3. **Pain-point question** — choose ONE format based on the measurement goal:
   - **DRAG-TO-RANK forced ordering** if the goal is to detect hierarchy
   - **SINGLE CHOICE with escape option pinned last** if the goal is to detect a single biggest pain point AND measure indifference
   - **VERBAL ranking with options on-screen** if the list is ≤6 items and reasoning is part of the signal (collapses single-choice + verbal-why into one slot)
4. **Detection timing question** — "When would you notice this?"
5. **Directive closing prompt** — never generic. Ask 2–3 specific things (e.g., "What would you improve? What would make this easier? What features did you wish worked differently?"). ~60 sec.

### Discipline rules

- **No conditional logic — this is the default, not a suggestion.** Every participant sees every question in the same form. No branching, no skip logic. **Rare, explicitly-approved exception:** if a study genuinely can't work without a follow-up that only fires for a subset of participants (e.g., a probe that only makes sense after a specific verbal answer), treat it as a deviation from this default that needs a decision, not a default tool to reach for — surface it as one of the 2–3 approaches under "Show 2–3 approaches before significant edits" so the requester picks it deliberately, document the specific trigger condition in Discipline notes, and confirm the platform build actually supports it before scripting around it. Only once approved does [[usertesting-html]]'s Rule 20 conditional banner apply — it exists to make an approved exception visible to the programmer, not to normalize branching as routine.
- **Personal-preference caveat in intro.** Required wording (adapt to subject): *"These [items] are just examples for the study. Please answer based on what's in the [interface] and how it's working — not on whether you personally like or have a preference for the content."* Add a proxy-framing sentence — *"Imagine you're [using this on behalf of] someone who [is engaged with all of these]"* — ONLY when the study is a caregiver/proxy scenario (shopping or deciding on someone else's behalf) where personal taste could otherwise contaminate answers. For a solo-user or perception-only study (e.g., "does this label look accurate to you"), drop the proxy sentence entirely — a caveat that doesn't parse for the subject matter is worse than no caveat.
- **Demographics at the END, never the start.** Form-filling mindset at the start contaminates UX responses.
- **Warm-up framing is intentional.** Decide per study whether the warm-up sits as (a) a Pre-task block (clearer for analysis) or (b) Task 1 (clearer for programmer handoff). Pick one per study and document the choice in this plan's Discipline notes (Output structure, component 6) — carry the same decision into the script header when [[usertesting-script]] runs, so the two documents don't disagree.

### Add-on absorption discipline

When the team adds questions mid-study, classify each before fielding:

- **(a) Absorb** into existing study — fits the instrument and timing
- **(b) Hold** for a future round — requires a different instrument, recipe, or sample
- **(c) Reject** — duplicates existing question or doesn't serve the research question

Document the rationale per question — not just the decision. Cuts get a future home so they're not lost. If no add-ons have surfaced yet, the register still appears in the output (component 7) — write "None this round" rather than omitting the section. Template: `references/decision-log-template.md`.

### 3-layer coverage-audit triangulation

Before fielding, audit three layers in parallel:

- Layer 1: **Master Research Plan** — source of truth for what's being measured
- Layer 2: **Group Test Plan / Script** — what participants will experience
- Layer 3: **Stimuli HTML** — what participants will see

Use parallel sub-agents (one per layer comparison) for independent verification. Document accepted divergences in the script header — do NOT auto-reconcile the master unless explicitly told. Some divergences are intentional (e.g., recipe swap, simplified screen count).

**No pre-existing Master Research Plan (e.g., self-initiated research with no PRD)?** This plan document IS Layer 1 until/unless the work is promoted into a larger program with its own master plan — say that explicitly rather than leaving Layer 1 blank.

**Running usertesting-plan on its own, before [[usertesting-script]] or [[usertesting-html]] exist yet?** The triangulation can't be a real audit — Layers 2 and 3 don't exist. Output component 8 becomes a set of pending hand-off assignments instead of a completed checklist (see Output structure below). Tell the requester plainly that the plan alone is not fieldable yet — the script and HTML still need to be built — especially when they've given a fielding date, so "can you scope this out?" doesn't get silently understood as "field-ready by Friday."

## Standing preferences

- **Show 2–3 approaches before significant edits.** Don't pick one and run with it by default.
- **Label pending vs. live edits clearly.** Use `v2-queued (not pushed)` vs. `v1-live (in Google Doc)` markers. Don't cite pending changes as canonical.
- **Frame ambiguous structural decisions BEFORE pushing.** Surface 2–3 options and wait for confirmation, even if the "right" answer seems obvious. Structural ambiguity compounds quietly (wrong task count → wrong randomization → wrong session length).
- **Visual consistency over methodological purity — document the tradeoff.** When a design choice that improves visual consistency competes with a methodology constraint, favor consistency BUT document the methodology that was traded away AND flag the affected metric for special handling at analysis. Participants notice visual inconsistency before they engage with content; an odd-one-out task contaminates more data than the methodology compromise does.
- **Flag every mismatch explicitly, never silently skip.** When something can't be added or doesn't match the spec, flag it with reason + suggested action + decision request.
- **Auto-open created deliverables in browser.** After generating any plan doc, open it. If the output stayed inline (chat text, no doc was created — e.g. a scoping conversation that hasn't been asked to produce a doc yet), there's nothing to open; don't treat that as a missed step.

## Output structure

The plan deliverable contains these eight components, in order:

1. **Header block** — Subject, length budget, group split, sample size, fielding window (sourced from intake Q1–Q8 — see Intake above)
2. **Coverage matrix** — table of variation × task showing which failure mode each task isolates
3. **Task list** — numbered Q1–QN tasks (each number = one platform task/question slot) with stimulus type, what's being measured, fixed-vs-randomized slot, time budget
4. **Stimulus-type appendix** — for each unique stimulus type, what it shows and why
5. **Synthesis tail** — the 3–5 end-of-session questions with format + escape options
6. **Discipline notes** — randomization rules, intro caveat, demographics placement, warm-up framing decision
7. **Add-on register** — any add-on questions classified as Absorb / Hold / Reject, with rationale. If nothing has surfaced yet, include the section anyway and write "None this round" — the 8-component structure stays constant whether or not it was triggered.
8. **Triangulation checklist** — 3-layer audit assignments (Master ↔ Plan ↔ HTML). On a plan-only run (script/HTML not built yet), list Layers 2–3 as "not yet drafted" with the hand-off skill named, rather than presenting an unfinished audit as complete.

## Workflow

1. Run the 8-question intake (batched, max 4 per message — via AskUserQuestion where available; see Intake above). Wait for answers.
2. Reconcile requested coverage against the session length budget (see "Time budgeting"). Flag and resolve any overage before proceeding.
3. Show 2–3 task-ordering approaches (e.g., baseline-fixed + 4-randomized + capstone-fixed vs. 2 fixed bookends + 3 randomized middle). Wait for selection.
4. Draft the coverage matrix.
5. Draft the task list with per-task stimulus type.
6. Draft the synthesis tail using the format that matches the measurement goal.
7. Run the add-on absorption pass — write "None this round" in the register if nothing has surfaced yet.
8. Output the plan in the 8-component structure above. Auto-open if it was written to a doc; if the output is inline chat text, skip the auto-open step rather than treating it as an error.

## Bundled resources

Load whichever of these matches the step you're on — they're worked reference material, not a replacement for the inline rules above.

- `references/coverage-matrix-template.md` — blank coverage matrix to fill in
- `references/intake-checklist.md` — the 8 intake questions and how to disambiguate vague or jargon-free answers
- `references/synthesis-tail-templates.md` — pre-written templates for each pain-point format
- `references/decision-log-template.md` — Absorb/Hold/Reject log format

## Hand-offs

- For question wording and platform tagging → invoke [[usertesting-script]]
- For visual stimuli HTML → invoke [[usertesting-html]]
- To run the full pipeline plan→script→HTML in order → invoke [[usertesting-orchestrator]]
