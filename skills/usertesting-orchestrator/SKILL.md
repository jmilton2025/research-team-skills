---
name: usertesting-orchestrator
description: Coordinate the full UserTesting study build pipeline — plan → script → HTML — with 3-layer triangulation between them. Use this skill when asked to "build a UserTesting study end-to-end," "set up a new UT study," "audit all three artifacts," or when the request spans plan + script + HTML together. Sequences [[usertesting-plan]], [[usertesting-script]], and [[usertesting-html]] in the correct order, holds shared context (task count, button text, image labels), and runs the cross-artifact reconciliation pass. Universal — works for any topic.
metadata:
  type: skill
---

# UserTesting Orchestrator Skill

Coordinate the full UserTesting study pipeline. This skill owns the cross-artifact handoffs between plan, script, and HTML; the 3-layer triangulation audit; and the discipline of keeping all three artifacts in lockstep.

For the individual artifact skills, invoke directly:
- [[usertesting-plan]] — study-level structure
- [[usertesting-script]] — question-level document
- [[usertesting-html]] — visual stimuli

Use this orchestrator skill when the request spans **all three** or when artifacts have drifted out of sync.

## When to use this skill

Trigger phrases:
- "Build a UserTesting study end-to-end"
- "Set up a new UT study from scratch"
- "Audit / reconcile plan + script + HTML"
- "Run a 3-layer triangulation"
- "The script and HTML are out of sync — fix it"
- "Coordinate the full UT pipeline"

If the request is only about one artifact, invoke that artifact's skill directly without this orchestrator.

## Pipeline overview

The three artifacts are produced and maintained in a strict order:

1. **Plan** — defines task count, ordering, coverage levels, stimulus type per task, synthesis tail. Source of truth for study structure.
2. **Script** — flat Q1–QN questions with platform tags, action ladders, choice-order rules. Source of truth for question wording.
3. **HTML** — visual stimuli mockups. Source of truth for visual layout, button text, image labels, subtotals.

Each downstream artifact depends on shared context from the previous one. The orchestrator's job is to pass that context forward AND to detect drift afterward.

## Shared context — what flows between artifacts

| Context element | Set by | Used by |
|---|---|---|
| Task count, task order, fixed-vs-randomized slots | Plan | Script (numbering), HTML (section banners) |
| Stimulus type per task (dual-phone, two-cart, single-row, etc.) | Plan | HTML (layout) |
| Synthesis-tail format (drag-to-rank vs single-choice vs verbal ranking) | Plan | Script (Q-block) |
| Question wording, action-ladder text, choice options | Script | HTML (CTA button text MUST match prompt wording verbatim) |
| Button label per task (e.g., "Add all 6 ingredients to cart") | HTML | Script (prompt MUST quote button verbatim) |
| Image-number labels (Image 1 / Image 2) per phone | HTML | Script (side-by-side comparison wording references these labels) |
| Total question count + estimated minutes | Script | HTML (footer / end card text) |

## Workflow — building a new study end-to-end

### Step 1 — Plan
Invoke [[usertesting-plan]]. Confirm the 6 intake questions. Produce the plan deliverable (8 components: header, coverage matrix, task list, stimulus-type appendix, synthesis tail, discipline notes, add-on register, triangulation checklist).

### Step 2 — Script
Invoke [[usertesting-script]]. Pass forward from the plan:
- Task count and ordering
- Stimulus type per task (for stimulus-pinning notes)
- Synthesis-tail format
- Session-length budget

Produce the script (banner + Programming Instructions + intro card + Pre-task + Q1–QN + synthesis tail + demographics + closing).

### Step 3 — HTML
Invoke [[usertesting-html]]. Pass forward from plan + script:
- Task count and section-banner labels
- Stimulus type per task (layout pattern)
- Button text per task (so prompts and buttons stay in lockstep)
- Image-number labels needed (so side-by-side question wording maps correctly)

Produce the HTML (header overview table + design tokens + per-task layouts + image labels + verified subtotals + image-quality QA).

### Step 4 — 3-layer triangulation
Run the cross-artifact audit (see next section).

### Step 5 — Open and review
Auto-open all three artifacts in browser. Surface any open decisions or blockers to the user.

## 3-layer triangulation audit

Before fielding, audit three layers in parallel using sub-agents:

| Layer 1 (Master) | Layer 2 (Plan/Script) | Layer 3 (Stimuli HTML) |
|---|---|---|
| Master Research Plan — what's being measured | The script participants will experience | The visuals participants will see |

**Dispatch sub-agents in parallel** — one per layer comparison:
- Sub-agent A: Master ↔ Script (does the script cover every research question?)
- Sub-agent B: Script ↔ HTML (does every stimulus exist, and does button text match prompts?)
- Sub-agent C: Master ↔ HTML (do visuals support the measurements claimed in the master?)

Document accepted divergences in the script header. Do NOT auto-reconcile the master unless explicitly told. Some divergences are intentional (e.g., recipe swap, simplified screen count, doc-debt accepted).

## Cross-artifact reconciliation pass

When artifacts have drifted (often after multiple revisions), run this checklist:

### Plan ↔ Script
- [ ] Task count in plan = number of task blocks in script
- [ ] Task ordering rules (fixed bookends, randomized middle, fixed slots) match
- [ ] Synthesis-tail format chosen in plan = format used in script (drag-to-rank vs single-choice + escape vs verbal ranking)
- [ ] Total question count in plan ≈ Q1–QN in script
- [ ] Add-on questions classified in plan are present (Absorb) or absent (Hold / Reject) from script

### Script ↔ HTML
- [ ] Every task in script has a matching section banner in HTML
- [ ] Every CTA button label in HTML appears verbatim in the matching script prompt (Rule 15 / Rule 13 cross-ref)
- [ ] Every side-by-side question in script uses "image 1 / image 2" wording → labels actually exist in HTML
- [ ] Every recipe / content name matches across both phones in HTML AND across script references
- [ ] Question-count footers in HTML ("Question Q? of N") match the script's total
- [ ] No leaked pre-reveal captions in HTML
- [ ] No pre-revealing mismatch pills on fielded stimuli
- [ ] All subtotals = sum of line items per cart
- [ ] Image labels present under every phone in multi-image stimuli (no gaps)

### Master ↔ everything
- [ ] Every research question in the master has a corresponding task and question in script + stimulus in HTML
- [ ] Any divergence is intentional and documented in the script header

## Standing preferences

- **Show 2–3 approaches before significant structural decisions.** Especially when artifacts conflict — surface the options.
- **Pending vs. live state labeled clearly.** Track `v2-queued (not pushed)` vs. `v1-live` per artifact. Don't cite pending edits as canonical.
- **Frame ambiguous decisions BEFORE pushing.** Structural ambiguity (e.g., 6 vs. 7 tasks, recipe-context block vs. Task 1) compounds quietly — surface and confirm before propagating downstream.
- **Auto-open all created artifacts.** Plan doc + script doc + HTML — open all three when complete.
- **Flag every mismatch explicitly.** During reconciliation, surface each drift with reason + suggested action + decision request.
- **Visual consistency over methodological purity — document the tradeoff.** When a layout change in HTML affects what the script can measure, document the change in BOTH artifacts (the methodology compromise in plan, the prompt rewrite in script, the visual choice in HTML) and flag the affected metric for analysis.

## Output structure

When orchestrating end-to-end, deliver:

1. **Plan doc** (via [[usertesting-plan]])
2. **Script doc** (via [[usertesting-script]])
3. **HTML stimuli file** (via [[usertesting-html]])
4. **3-layer triangulation report** — Master ↔ Plan/Script ↔ HTML diff with accepted divergences flagged
5. **Open-blockers summary** — sign-offs pending, content confirms outstanding, decisions waiting

## Workflow — fixing a drifted study

If the user reports that "the script and HTML are out of sync" (or similar):

1. Read all three artifacts.
2. Run the cross-artifact reconciliation checklist (above).
3. Group findings by severity:
   - **Blocker** — would invalidate data (e.g., subtotal arithmetic broken, leaked caption pre-reveals failure mode, missing question, wrong question type tag)
   - **Mismatch** — would confuse the participant (e.g., button text doesn't match prompt, image label missing under a phone)
   - **Polish** — cosmetic, low-impact
4. Show the list to the user. Ask which to fix in this pass.
5. Route fixes to the relevant artifact skill ([[usertesting-script]] for prompt edits, [[usertesting-html]] for visual edits, [[usertesting-plan]] for structural changes).
6. Re-run triangulation after the fixes.

## Bundled resources

- `references/triangulation-checklist.md` — printable 3-layer audit form
- `references/cross-artifact-diff-template.md` — diff format for surfacing drift
- `references/shared-context-handoff.md` — what to pass between skills in step 1 → 2 → 3

## Cross-skill references

- [[usertesting-plan]] — study-level structure
- [[usertesting-script]] — question-level document
- [[usertesting-html]] — visual stimuli
