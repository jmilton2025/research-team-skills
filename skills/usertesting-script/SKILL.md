---
name: usertesting-script
description: Write or audit a UserTesting script (the question-level document handed to the UserTesting programmer). Use this skill when asked to "write a UserTesting script," "draft test questions," "review a UT script," "tag questions for the programmer," "fix question wording," or to apply platform-tagging discipline (avoiding the Written-Response auto-default bug). Outputs flat Q1–QN questions with proper VERBAL / SINGLE CHOICE / MULTI-SELECT / DRAG-TO-RANK tags, choice-order rules, action ladders, probing rules, and a warm closing card. Universal — works for any topic.
metadata:
  type: skill
---

# UserTesting Script Skill

Write the question-level script that the UserTesting platform programmer wires up. This skill owns question wording, question-type tagging (the 4-way anti-platform-bug discipline), action-ladder design, choice-order rules, probing rules, and the warm closing card.

For study-level structure (task count, ordering, coverage), hand off to [[usertesting-plan]]. For visual stimuli, hand off to [[usertesting-html]]. For end-to-end pipeline orchestration, use [[usertesting-orchestrator]].

## When to use this skill

Trigger phrases:
- "Write/draft a UserTesting script"
- "Review/audit this script"
- "Fix the question wording"
- "Tag questions for the UserTesting programmer"
- "How do I phrase this question?"
- "Help with the action ladder"
- "What's the closing question?"

## Core rules

### 1. Question types — only 4 allowed

Never use "Written response." Always pick from:

1. **VERBAL RESPONSE** — participant speaks answer aloud
2. **SINGLE CHOICE** — taps one option
3. **MULTI-SELECT** — taps one or more options
4. **DRAG-TO-RANK** — drags items into order (optional; many studies use single-choice + escape or verbal ranking instead)

**Why:** Written response on UserTesting produces shallow surface answers — verbal elicits richer reasoning.

### 2. 4-way platform tagging (anti-platform-bug)

UserTesting sometimes auto-defaults verbal questions to "Written response," which is silently destructive. Belt-and-braces: tag every question in **four** places.

Template for VERBAL:
```
### Question Q[N] — VERBAL RESPONSE

**Verbal response:**
[Prompt body]

Please give a verbal response.

> **USERTESTING QUESTION TYPE: VERBAL RESPONSE** (NOT Written response).
```

Apply the same 4-place pattern to SINGLE CHOICE and MULTI-SELECT (substitute the type name). When adding a new type mid-revision, also update the **top-of-doc banner** so all valid types are declared.

**Top-of-doc banner template:**
```
🚨 READ THIS FIRST — UserTesting Question Type Rules
This study uses ONLY: VERBAL RESPONSE · SINGLE CHOICE · MULTI-SELECT
DO NOT use "Written response" for any question.
```

### 3. Numbering — flat Q1–QN, never compound

Number questions Q1 → Q[final] in one flat sequence across the entire script. Section/task headers can still organize the markdown source, but the question numbers stay flat.

❌ Bad: "Task 1 Q1," "Task 2 Q1," nested "1.1 / 1.2 / T1 / G1 / D1"
✅ Good: Q1, Q2, Q3 … Q31

**Why:** UserTesting platform handles flat numbering cleanly; compound numbering creates programming overhead and confuses participants.

### 4. Question tags vs. display cards

- **Q# = Question** — tag on the platform
- **Intro cards, context cards, stimulus cards = display-only** — NOT tagged as a question

**Why:** UserTesting counts "Question" tags toward the task list; mistagging display content inflates the count.

### 5. Stimulus pinning — visible across all questions in a task

Once a stimulus screen is set (single cart, dual-phone, single-row card), pin it visible while ALL questions for that task cycle. Letting it disappear forces participants to recall details and degrades response quality.

### 6. Action ladders — mildest first, NEVER randomize

Action ladders are ordinal. Randomizing destroys the ordering.

**4-option cart-level ladder (default for cart-action questions):**
1. Add as-is
2. Edit the cart first (swap, remove, or add items)
3. Buy this cart now and get the missing item(s) elsewhere
4. Skip this and pick a different option

**3-option cart-edit ladder (when "buy elsewhere" is not a relevant option):**
1. Add the cart as-is
2. Edit the cart first
3. I would no longer [continue with this]

**3-option single-row substitution ladder (Accept / Modify / Skip):**
1. Accept — "That works for me"
2. Modify — "I'd swap it myself" / "I'd swap for a smaller size"
3. Skip — "I'd skip it"

Pick the shortest ladder that captures the decision space.

### 7. Soft abandonment wording

Use **"I would no longer [shop/use/continue]"** — NEVER "back out," "abandon," "give up," or other harsh phrasing.

**Why:** harsh wording triggers face-saving ("I'd never give up!"); soft wording gets honest answers.

### 8. Probing rule — "Anything else?" max once

For verbal responses, allow ONE probe with "Anything else?" if the answer is short. If the participant says "I don't know" or stops, move on.

**Conditional probe wording** — when probing for a specific missed concept, use *"How would you handle…"* — NOT *"Why didn't you mention…"* "Why didn't you mention X?" implies the participant did something wrong and triggers defensiveness.

### 9. Choice-order rules per question type

| Question type | Randomize? | Why |
|---|---|---|
| Action ladder | Do NOT randomize | Order is ordinal |
| Side-by-side comparison ("image 1 or image 2?") | Randomize L/R of the **physical stimulus**, not the option labels | Position bias on stimulus; labels stay stable |
| Recap multi-select | Do NOT randomize | Preserve recipe/item order so participants match the recap |
| Pain-point single choice | Randomize first N, pin escape option ("all the same") LAST | Lets users opt out of forcing a preference |
| Stack-rank with no escape | Do NOT randomize | Goal is hierarchy detection |
| Temporal sequence | Do NOT randomize | Order is the variable being tested |
| Ordinal rating scale | Do NOT randomize | Order is the scale |
| Demographics (ordinal) | Do NOT randomize | Order is the scale |

### 10. Recap multi-select before the verbal "why?"

End-of-study recap pattern:
- **MULTI-SELECT first** — "Which of these would you no longer [use]?" + include "None — I would still [use] all of them"
- **VERBAL immediately after** — "Why those? What was the dealbreaker?"

Program on the same screen if the platform allows; otherwise back-to-back. Forces participants to commit before rationalizing.

### 11. Pain-point question format depends on measurement goal

| Goal | Format |
|---|---|
| Detect rank-ordering of pain points | DRAG-TO-RANK, forced (no escape option) |
| Detect single biggest pain point + measure indifference | SINGLE CHOICE, randomize first N, pin "all the same" last |
| Capture hierarchy + reasoning in one slot (≤6 options) | VERBAL ranking with all options displayed on screen, randomized display order |

### 12. Verbal ranking — when to prefer over single-choice + verbal-why

Collapse a single-choice + verbal "why?" pair into one VERBAL ranking when:
- The list is ≤6 options (working-memory limit)
- Reasoning is part of the signal
- You want hierarchy + indifference + reasoning in one slot

**Mechanic:**
- All options displayed on screen so the participant can see them while ranking
- Display order randomized (controls primacy/recency on the displayed list)
- One probe: "Anything else stand out about why that's the worst one for you?"
- ~60 sec time budget

Saves ~30–45 sec vs. the split-question pair and removes a platform dependency.

### 13. Standard verbal follow-up wording

For every verbal "why?" follow-up immediately after a single-choice or ranking question, use:

**"State your reason out loud. Why did you pick the previous option? Please give a verbal response."**

**Why:** "previous option" is platform-agnostic — works whether the prior question was tap, drag, or spoken. "That one" assumes a tap-choice; vague forms ("Why did you say that?") cause participants to forget what they just said.

### 14. Side-by-side comparison wording — "Image 1 / Image 2," never "left / right"

Whenever a question references one of two stimuli in a side-by-side comparison, name them by **image number**, not by screen position.

✅ "Look at image 1 and image 2 side by side. Which would you rather have, the image 1 [cart] or the image 2 [cart]?"
❌ "Look at the [cart] on the left and the [cart] on the right…"

**Why:** "left / right" is bound to screen geometry — breaks the moment a participant rotates a device, the platform mirrors, or randomization swaps positions. "Image 1 / Image 2" is stable because it's bound to the labels under each phone (see [[usertesting-html]] Rule on image labels).

The physical stimulus shown as Image 1 vs Image 2 is still randomized via within-task randomization — labels stay stable; position is what randomizes.

### 15. Instruction CTA must echo stimulus button text verbatim

Whenever a question references an action the participant "took," quote the button/CTA label exactly from the stimulus — including counts and qualifiers.

✅ "Imagine you tapped 'Add all 6 ingredients to cart.'" (button literally says `Add all 6 ingredients to cart`)
❌ "Imagine you added all the ingredients to your cart."
❌ "Imagine you tapped 'Add all to cart.'" (when button says "Add all 6")

**Why:** participants cross-check the prompt against the button. Any mismatch — even a paraphrase — causes them to pause and disambiguate, wasting the first ~5 seconds of every task.

### 16. Pre-reveal context cards must be neutral

Any context card, caption, or sub-header that appears BEFORE the participant observes the stimulus must be neutral — never name the substitution, mismatch, or failure mode being tested.

❌ Leaky: "Option A · With substitute" / "Cart with quantity mismatch" / "This cart shows the wrong unit"
✅ Neutral: "Here are two [carts] for [recipe]." / "Here's your [cart]." / no caption at all

**Why:** participants are supposed to *discover* the mismatch and react. A caption that pre-labels the variation tells them what to look for and contaminates the unprompted-noticing measurement.

### 17. Concrete-grounding question after abstract one

After an abstract question ("when you're [doing X] and [Y happens] — what do you usually do?"), follow with a concrete-grounding one ("tell me about the last time you [did X] on [platform]").

**Why:** the concrete question elicits richer detail than the abstract one alone.

### 18. Intro card — first screen of every study

First screen = warm intro that:
- Sets time expectation ("This will take about [N] minutes")
- States the format ("Speak your answers out loud — there's nothing to type")
- Establishes "no right or wrong answers"
- Includes the personal-preference caveat (see Rule 19)

### 19. Personal-preference caveat — required

Adapt the wording to the subject, but always include:

*"These [items] are just examples for the study. Please answer based on what's in the [interface] and how it's working — not on whether you personally like the content, have an allergy, or [have any personal restriction]. Imagine you're [acting on behalf of] someone who [engages with all of these]."*

**Why:** prevents refusals based on personal taste rather than UX evaluation. Without this, you lose data on every item a participant personally objects to.

### 20. Warm thank-you closing card

Always end with a warm, specific thank-you card (display-only, NOT a Question).

✅ "Thank you so much for taking the time to share your thoughts with us today. Your feedback is incredibly helpful and will directly shape how we improve this experience. We really appreciate you."
❌ "Thank you for completing this study."

**Why:** participants who feel valued give higher-quality data on future studies.

### 21. Directive closing prompt, never generic

The final feedback question must be directive — ask 2–3 specific things, not "any final thoughts?"

✅ "What could we improve about this experience? What would make this process easier for you? Was there anything you didn't like, or any features you wished worked differently?" (~60 sec)
❌ "Any final thoughts?"

**Why:** generic prompts get generic non-answers; specific prompts get specific answers.

### 22. "Add to cart" / mental-model questions belong in Pre-task, NEVER the end

Any "what do you THINK happens when you tap [X]?" question goes in **Pre-task**, before participants see any actual behavior. End-of-study placement turns it into a recall test, which isn't the goal.

### 23. DRAG-TO-RANK fallback to verbal — write inline

If the UserTesting platform doesn't support DRAG-TO-RANK on a specific question, write the verbal fallback INLINE in the script (`Spoken text becomes: …`). Tests can't break if a feature is unavailable; the fallback is pre-written, not improvised.

### 24. Stimulus terminology rules

- Prefer **"shopper"** over "picker" in general writing
- Use "picker" only when referencing an existing platform feature that uses that term

### 25. No redundant question types

If a stack-rank already captures pain-point hierarchy at the end, don't ALSO ask a drag-to-rank earlier in the study. Redundancy fatigues participants and lowers per-question quality.

## Standing preferences

- **Show 2–3 wording approaches before significant rewrites.** Don't pick one and run.
- **Flag every mismatch explicitly.** If a question references a stimulus element that doesn't exist or has different wording, surface the conflict — don't paper over it.
- **Pending vs. live edits labeled clearly.** Mark `v2-queued (not pushed)` vs. `v1-live (in Google Doc)`. Don't cite pending changes as canonical.
- **Auto-open created docs.** After uploading a script to Google Doc, open it in the browser.

## Output structure

The script deliverable contains:

1. **Banner** — 🚨 READ THIS FIRST — UserTesting Question Type Rules + all valid types declared
2. **Programming Instructions** — global rules for the platform programmer (no conditional logic, randomization rules, stimulus pinning)
3. **Intro card** — display-only, with time / format / no-right-answers / personal-preference caveat
4. **Pre-task questions** — mental-model + concrete-grounding questions
5. **Task questions** — Q1 → QN, flat numbering, each task block with stimulus + questions
6. **Synthesis tail** — recap multi-select, verbal why, pain-point question, detection timing, directive closing
7. **Demographics** — at the end, never the start
8. **Warm thank-you closing card** — display-only

## Workflow

1. Confirm the plan inputs (task count, stimulus types per task, synthesis-tail format chosen). If unknown, invoke [[usertesting-plan]] first.
2. Draft the banner + Programming Instructions block.
3. Draft the intro card + Pre-task questions.
4. For each task, draft the question block with proper 4-way tagging, action ladder, and probing rules.
5. Draft the synthesis tail using the matched format.
6. Draft demographics + warm closing card.
7. Run the 4-way tagging audit: every Q has header tag + block label + spoken trailer + programming opener. If MULTI-SELECT appears, banner declares it.
8. Run the wording audit: CTA quotes match stimulus button wording verbatim (Rule 15); side-by-side wording uses "image 1 / image 2" (Rule 14); verbal follow-ups use the standard "previous option" wording (Rule 13).
9. Output the script. Auto-open if uploaded to Google Doc.

## Bundled resources

- `references/question-type-templates.md` — copy-paste templates for each of the 4 question types with full 4-way tagging
- `references/action-ladder-library.md` — pre-written 3-option and 4-option ladders for common decisions
- `references/closing-card-templates.md` — warm thank-you cards and directive closing prompts
- `references/probing-rule-cheatsheet.md` — when to probe, how to probe, soft vs. accusatory wording

## Hand-offs

- For study-level structure → invoke [[usertesting-plan]]
- For visual stimuli HTML → invoke [[usertesting-html]]
- For full pipeline → invoke [[usertesting-orchestrator]]
