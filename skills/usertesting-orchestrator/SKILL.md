---
name: usertesting-orchestrator
description: Coordinate the full UserTesting study build pipeline — plan → script → HTML — with 3-layer triangulation between them. Use this skill when asked to "build a UserTesting study end-to-end," "set up a new UT study," "audit all three artifacts," or — just as often — whenever a plain-English ask (e.g. "can you put together the whole study, plan/script/mockups, so I can review one packet?") spans plan + script + HTML together, jargon or not. Sequences [[usertesting-plan]], [[usertesting-script]], and [[usertesting-html]] in the correct order, holds shared context (task count, button text, image labels), and runs the cross-artifact reconciliation pass. Universal — works for any topic.
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

These are examples, not the only phrasing that qualifies — the real trigger is **scope, not vocabulary**. A PM or designer who says "can you build the whole study — plan, script, and mockups — so I can review one packet?" or a hedged, self-initiated "I think we might want to test whether X still holds up" both call for this skill just as much as the jargon phrasing above. Don't wait for someone to say "triangulation" or "reconcile."

If the request is only about one artifact, invoke that artifact's skill directly without this orchestrator.

**If `[[usertesting-plan]]`, `[[usertesting-script]]`, or `[[usertesting-html]]` come back as an unknown skill:** this pipeline ships via this repo's `install.sh`, which symlinks all four skills into `~/.claude/skills/` — it may not have been run in the current environment. Don't stop and don't silently drop the discipline. Read that skill's `SKILL.md` straight from this repo (`skills/usertesting-plan/SKILL.md`, `skills/usertesting-script/SKILL.md`, `skills/usertesting-html/SKILL.md`) and apply its rules by hand. Note in the Step 5 open-blockers summary that the pipeline isn't registered as invokable skills yet, so the user can run `install.sh` before the next study.

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
| Question wording, action-ladder text, choice options | Script | HTML (layouts and captions must not contradict the prompt) |
| Button/CTA copy per task (e.g., "Add all 6 ingredients to cart") | **Script** — authors the exact copy as part of the prompt, since Script is produced before HTML in the pipeline order above | HTML (renders the button with this exact text; HTML does not invent its own wording — see Step 3) |
| Image-number labels (Image 1 / Image 2) per phone | HTML | Script (side-by-side comparison wording references these labels). Applies to every multi-phone stimulus, including two-cart A/B tasks — a "Cart A / Cart B" chip is an optional supplementary caption on top of the image number, never a substitute for it. Asked-vs-delivered dual-phone tasks reference a single object ("the cart you received"), not a two-way choice, so they don't need "image 1 or image 2" preference wording at all. |
| Total question count + estimated minutes | Script | **Not built into HTML by default** — usertesting-html has no standard footer/end-card rule for this. Only pass it forward if the study explicitly asks for an on-screen "Question Q of N" footer; otherwise this context has no downstream consumer. |

## Workflow — building a new study end-to-end

### Step 1 — Plan
Invoke [[usertesting-plan]]. **Confirm the 8 intake questions** (see usertesting-plan's Intake section) — if the requester already answered them (even informally, folded into a request message rather than listed), restate them back in the plan's structure rather than re-asking; only ask, in the batches usertesting-plan's own intake instructs (max 4 per batch), for whatever they actually left out. If this is self-initiated research with no separate stakeholder to ask, answer all eight yourself from context and flag every self-assumed answer for sign-off in the Step 5 open-blockers summary — don't let invented parameters read as stakeholder-confirmed. Produce the plan deliverable (8 components: header, coverage matrix, task list, stimulus-type appendix, synthesis tail, discipline notes, add-on register, triangulation checklist).

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
Open all three artifacts: Plan and Script open as their Google Doc if one was uploaded; HTML opens as the local file in a browser — these are two different mechanisms, not one "auto-open" action. If Doc upload isn't available in this environment, say so and hand back the local file/markdown path instead of failing silently — don't skip opening the artifacts that did work because one didn't. Surface any open decisions or blockers to the user (Output structure item 6 below).

## 3-layer triangulation audit

Before fielding, audit three layers in parallel using sub-agents:

| Layer 1 (Master Research Plan) | Layer 2 (Plan + Script) | Layer 3 (Stimuli HTML) |
|---|---|---|
| What's being measured, and why | The plan's task/coverage structure AND the script participants will experience | The visuals participants will see |

**What counts as the Master Research Plan:** an existing document that states the research questions independently of this build — a PRD, a stakeholder brief, or a separate plan doc from the `research-plan` skill. **When none exists** — a fast turnaround from a verbal or Slack ask, or self-initiated research with no PRD; both are the common case, not the exception — the Plan produced in Step 1 stands in for Layer 1. Say so explicitly wherever Layer 1 is referenced (script header, triangulation report): it's a documented substitution, not a skipped step, and it means Sub-agents A and C below are checking the Plan's internal consistency rather than against independent ground truth.

**Dispatch sub-agents in parallel** — one per layer comparison:
- Sub-agent A: Master ↔ Plan (does the plan's coverage matrix hit every research question?). Run the Plan ↔ Script checks from the reconciliation checklist below as part of this pass, every time — not only when repairing a drifted study. A first build can drift internally too, and the standard build path shouldn't skip the one check (Plan against Script) that catches it.
- Sub-agent B: Plan/Script ↔ HTML (does every stimulus exist, and does button text match prompts?)
- Sub-agent C: Master ↔ HTML (do visuals support the measurements claimed in the master?)

Document accepted divergences in the script header. Do NOT auto-reconcile the master unless explicitly told. Some divergences are intentional (e.g., recipe swap, simplified screen count, doc-debt accepted).

## Cross-artifact reconciliation pass

When artifacts have drifted (often after multiple revisions), run this checklist:

### Plan ↔ Script
- [ ] Task count in plan = number of task blocks in script
- [ ] Task ordering rules (fixed bookends, randomized middle, fixed slots) match
- [ ] Synthesis-tail format chosen in plan = format used in script (drag-to-rank vs single-choice + escape vs verbal ranking)
- [ ] Script's flat Q1–QN count is consistent with the plan's task list (per-task question load) plus its synthesis tail and demographics — the plan's output structure has no single aggregate-count field, so treat this as a manual sanity check, not a lookup
- [ ] Add-on questions classified in plan are present (Absorb) or absent (Hold / Reject) from script

### Script ↔ HTML
- [ ] Every task in script has a matching section banner in HTML
- [ ] Every CTA button label in HTML appears verbatim in the matching script prompt (Rule 15 / Rule 13 cross-ref)
- [ ] Every side-by-side question in script uses "image 1 / image 2" wording → labels actually exist in HTML
- [ ] Every recipe / content name matches across both phones in HTML AND across script references
- [ ] If a "Question Q of N" footer or minutes estimate was explicitly requested, it's present and matches the script's total — usertesting-html doesn't build this by default, so don't fail the check for its absence unless it was actually asked for
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
- **Open every artifact that was created, by its own mechanism.** Plan doc + script doc open as Google Docs (if uploaded); HTML opens as a local file. Don't treat this as one uniform "auto-open" action — see Step 5.
- **Flag every mismatch explicitly.** During reconciliation, surface each drift with reason + suggested action + decision request.
- **Visual consistency over methodological purity — document the tradeoff.** When a layout change in HTML affects what the script can measure, document the change in BOTH artifacts (the methodology compromise in plan, the prompt rewrite in script, the visual choice in HTML) and flag the affected metric for analysis.
- **Label test/demo runs.** When any part of this pipeline is generated for a mock-run, stress test, or demo rather than a real fielding, follow the same convention as `research-plan` / `mod-guide` / `report`: add `⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.` directly under the header of the plan, script, and HTML (see `../../references/output-status-and-labeling-conventions.md`). This skill can produce a full plan+script+HTML bundle in one pass — the highest fabrication risk in the repo — so don't skip the label because the content looks obviously fake to you; it may not to someone who finds the file later without this context.
- **One severity vocabulary, not two.** The 3-layer triangulation's per-sub-agent findings (Sub-agent A/B/C) and the drifted-study workflow's Blocker/Mismatch/Polish triage are the same kind of finding from two different entry points (new build vs. repair). Tag every sub-agent finding with Blocker/Mismatch/Polish too, so a triangulation report from a fresh build and a repair pass on a drifted one are directly comparable.

## Output structure

When orchestrating end-to-end, deliver:

1. **Plan doc** (via [[usertesting-plan]])
2. **Script doc** (via [[usertesting-script]])
3. **HTML stimuli file** (via [[usertesting-html]])
4. **3-layer triangulation report** — Master ↔ Plan/Script ↔ HTML diff with accepted divergences flagged
5. **Plain-English summary** — 3–5 sentences, no researcher jargon ("VERBAL RESPONSE," "4-way tagging," "triangulation" don't belong here): what's being tested, what's in the packet, and the one open question the study is built to answer. Include this whenever the requester's own message didn't use this skill's internal vocabulary — a PM or designer bringing a PRD, not a fellow researcher, which per the trigger-phrase note above is the common case, not the exception.
6. **Open-blockers summary** — sign-offs pending, content confirms outstanding, decisions waiting. Always explicitly call out: any sample size or session-length figure that was invented rather than sourced (no skill in this pipeline gives sizing guidance — flag it as a placeholder needing sign-off before fielding); any intake answer that was self-assumed rather than stakeholder-confirmed; and whether the pipeline skills were actually invokable or applied by hand from this repo's files (see the fallback note under "When to use this skill").

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
