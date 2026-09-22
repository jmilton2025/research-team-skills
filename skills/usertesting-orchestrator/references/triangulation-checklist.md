# 3-layer triangulation — printable audit form

Copy this per study run. Fill in every row before treating a build as fielding-ready.

## Layer definitions

| Layer | What it is | Source |
|---|---|---|
| 1 — Master Research Plan | What's being measured, and why | An existing PRD / stakeholder brief / `research-plan` doc, **or** — when none exists (the common case, not the exception) — the Plan produced in Step 1, explicitly documented as standing in for Layer 1 |
| 2 — Plan + Script | The study's task/coverage structure AND the question-level experience | usertesting-plan + usertesting-script outputs |
| 3 — Stimuli HTML | What participants actually see | usertesting-html output |

State which case applies before starting: `[ ] Independent Master exists` / `[ ] Plan is standing in for Master (documented substitution)`.

## Sub-agent A — Master ↔ Plan (+ Plan ↔ Script)

- [ ] Every research question in the Master has a corresponding task in the Plan's coverage matrix
- [ ] Every failure mode in scope (per intake) is isolated in exactly one task — no task conflates two
- [ ] Plan ↔ Script checks (run every time, not just on repair):
  - [ ] Task count in plan = number of task blocks in script
  - [ ] Task ordering rules (fixed bookends, randomized middle, fixed slots) match
  - [ ] Synthesis-tail format chosen in plan = format used in script
  - [ ] Script's flat Q1–QN count is consistent with the plan's task list + synthesis tail + demographics (manual sanity check — the plan has no single aggregate-count field)
  - [ ] Add-on questions classified in plan (Absorb/Hold/Reject) match what's present or absent in script

## Sub-agent B — Plan/Script ↔ HTML

- [ ] Every task in script has a matching section banner in HTML
- [ ] Every CTA button label in HTML appears verbatim in the matching script prompt
- [ ] Every side-by-side question in script uses "image 1 / image 2" wording → the labels actually exist under the phones in HTML
- [ ] Every recipe/content name matches across both phones in HTML AND across script references
- [ ] If (and only if) a "Question Q of N" footer or minutes estimate was explicitly requested, it's present in HTML and matches the script's total
- [ ] No leaked pre-reveal captions in HTML
- [ ] No pre-revealing mismatch pills on fielded stimuli
- [ ] All subtotals = sum of line items per cart
- [ ] Image labels present under every phone in multi-image stimuli (no gaps)

## Sub-agent C — Master ↔ HTML

- [ ] The visuals actually support the measurement claimed in the Master — e.g. if the Master's question is a preference between two UI treatments, the HTML shows two genuinely different treatments, not a cosmetic variant of the same one
- [ ] Any stimulus simplification (fewer items, fewer screens) doesn't remove the signal the Master needs
- [ ] Any wrong-item / unprompted-detection task is unflagged, per usertesting-html's isolation rule, *unless* the feature under test is itself the disclosure mechanism — in that case, confirm the Plan places an unflagged version as an explicit baseline/counterfactual task, separate from a flagged task that tests the actual feature

## Severity tagging

Tag every finding from all three sub-agents with one of:
- **Blocker** — would invalidate data (subtotal arithmetic broken, leaked caption, missing question, wrong question-type tag)
- **Mismatch** — would confuse the participant (button text vs. prompt mismatch, missing image label)
- **Polish** — cosmetic, low-impact

Use the same three tags whether this is a fresh build's triangulation or a repair pass on a drifted study (see "Workflow — fixing a drifted study" in SKILL.md) — one vocabulary, so reports are comparable across both entry points.

## Sign-off

- [ ] Every Blocker resolved or explicitly accepted with a documented reason
- [ ] Every divergence from the Master documented in the script header (not silently reconciled)
- [ ] Open-blockers summary written (sample size, session length, self-assumed intake answers, pipeline-invocation status)
