---
name: usertesting-html
description: Build or audit the visual stimuli HTML for a UserTesting study. Use this skill when asked to "build UT stimuli," "create the stimulus HTML," "design the test mockups," "mock up the test screens," "get the UI ready for testing," "get quick user feedback mockups," "review/audit stimuli HTML," "fix subtotals," "audit product images," or to apply visual patterns (dual-phone, two-cart side-by-side, single-row substitution cards, image labels, design tokens). Outputs HTML mockups with proper Instacart-style design tokens, image-number labels, subtotal arithmetic verified, no-leak captions, and image-quality QA. The layout patterns and QA rules generalize to any topic; the worked examples below use Instacart recipe-to-cart mechanics for concreteness.
metadata:
  type: skill
---

# UserTesting HTML Skill

Build the visual stimuli HTML that participants see during a UserTesting study. This skill owns layout patterns (dual-phone, two-cart, single-row card), design tokens, image labels, subtotal arithmetic, no-leak caption discipline, and image-quality QA.

[[usertesting-plan]], [[usertesting-script]], and [[usertesting-orchestrator]] are names of this skill's sibling skills in the same repo — invoke them with the Skill tool by that exact name (e.g. `Skill(skill: "usertesting-plan")`) if they're installed in this environment. If a lookup by that name fails (not installed here, or you're running standalone), don't treat it as a blocker: read this file's own rules and confirm the missing inputs directly with the requester in one message instead. For study-level structure, prefer [[usertesting-plan]]. For question wording and platform tagging, prefer [[usertesting-script]]. For end-to-end pipeline orchestration, use [[usertesting-orchestrator]].

## When to use this skill

Trigger phrases:
- "Build/create the UserTesting stimuli"
- "Make the test mockups"
- "Design the stimulus HTML"
- "Mock up the test screens" / "mock up what this would look like"
- "Get the UI ready for testing" / "get me test mockups"
- "I need quick user feedback mockups" (no plan or script yet)
- "Review/audit the stimuli HTML"
- "Fix the cart subtotals"
- "Audit the product images"
- "Add image labels to the phones"

This skill is commonly invoked standalone, before any plan or script document exists — a PM or designer asking for fast pixels to sanity-check with stakeholders is a normal, expected trigger, not an edge case. See Workflow step 1 for how to proceed without those artifacts.

## Core rules

### 1. Visual layout patterns — pick based on what the question asks

| Question goal | Layout pattern |
|---|---|
| Compare what was asked vs. what was delivered | Dual-phone side-by-side: asked on left, delivered on right |
| A/B preference between two strategies | Two-cart side-by-side, **randomize L/R** |
| React to a specific UI signal (label, badge, warning) | Single cart with the signal visible, no comparison |
| Isolated substitution decision (no full cart context) | Single-row stimulus card (asked → delivered) |
| Pre-action expectation-setting | Content-only screen with no action button |
| Measure whether an explicit trust/confidence signal (a badge, score, or disclosure label) changes stated confidence | Single cart with the signal visible for one reaction, OR two-cart A/B (signal vs. no signal) if the comparison itself is the measurement — pick per Rule 12's no-leak discipline either way |

### 2. Dual-phone pattern

- **LEFT phone** = source/recipe view (title, steps, ingredient list, primary CTA button)
- **RIGHT phone** = result view (cart, deliverable, output state)
- Both visible at once on one screen
- For asked-vs-delivered framing, the source phone is always LEFT (no L/R randomization)

### 3. Two-cart side-by-side pattern (A/B preference)

- Two cart phones side by side on one screen
- **Randomize which appears L vs R** — position bias is real
- Use neutral "Cart A / Cart B" position chips ONLY if the question references them; otherwise no caption

**Implementing the randomization in a static file:** a single HTML file can't randomize per participant on its own. Pick one and note the choice in the header overview table or build notes:
- Produce two mirrored files (e.g., `-la.html` / `-lb.html` with positions swapped) and tell the UserTesting programmer to alternate which one loads, or
- Ship one file and add an explicit note for the programmer to randomize L/R at the platform level.

Don't silently pick a fixed L/R order and call it done — that's the position bias the rule exists to prevent.

### 4. Single-row substitution card pattern (isolated decision)

Build with this CSS pattern so it reads as one decision, not a list. This is an isolated-decision card, not a full recipe/item screen — it does NOT get the Rule 8 hero block (no thumbnail/name/meta-line/star-rating header); the card IS the whole stimulus.

**Grid:** 3-column, `grid-template-columns: 1fr 44px 1fr` (asked-pane · arrow column · added-pane)

**Panes:**
- **Asked pane** — gray background (`var(--asked-bg)`, signals "this is what was wanted"), label above the row: `Recipe asked:`
- **Arrow column** — fixed 44px width, single arrow glyph (→), no background
- **Added pane** — green background (`var(--added-bg)`, signals "this is what was delivered"), label above the row: `We added:`

**Mismatch pill** — OPTIONAL ornamentation. Use only on context-only cards (no reaction asked) or in stakeholder walkthroughs / training materials. **Remove from any fielded card that asks for unprompted reaction** — the pill names the mismatch the question is meant to elicit, which makes the question leading. Default to no pill.

**Context-only screens** (when the card needs explanatory framing without a question): use `.ut-context-card` — dashed-border block, no green/gray panes, no pill.

**Multi-select choices** (when the card is paired with a recap question): use `.ut-choices.multi li::before` to render a square checkbox marker — distinguishes multi-select from single-choice visually.

### 5. Recipe / content name MUST match across both phones

If the source phone shows "Classic Buttermilk Pancakes," the deliverable phone heading must ALSO show "Classic Buttermilk Pancakes" — exact spelling, exact casing. No abbreviations, no paraphrases.

**Why:** name mismatches break perceived continuity ("did I land on the right page?") and confuse participants.

### 6. Image-number labels under EVERY phone in multi-image stimuli

When a stimulus shows 2+ phones, label each phone with both an image number AND a content descriptor on two stacked lines:

```html
<div class="phone-label">Image 1<br>Recipe</div>
<div class="phone-label">Image 2<br>Cart</div>
```

CSS:
```css
.phone-label {
  text-align: center;
  font-size: 11.5px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
```

**Why:** unlabeled or single-label phones force participants to mentally tag them ("the one on the left… the recipe one…") and slow down their answers. Numeric labels give moderators and participants a clean shared reference point that stays stable under randomization and orientation changes. The script side relies on these labels (see [[usertesting-script]] Rule 14).

**Numbering scope:** numbering resets per task — each task's phones are labeled Image 1, Image 2 (and Image 3+ only if that task genuinely shows more than 2 phones) independently of every other task. Don't run a single incrementing count across the whole file. This keeps the script's "image 1 / image 2" wording (usertesting-script Rule 14) correct for every task without renumbering per task.

### 7. Meta-line order standardized — never reorder

Standard format: `Serves [N] · [N] ingredients · [T] min`

NEVER reorder. Apply identically across every recipe/item in the study.

**Why:** visual scanning becomes faster when the order is invariant.

### 8. Hero block parity across all stimuli

Every recipe/content SOURCE screen (the thing being asked for — e.g., the left phone in dual-phone, or a single content-only screen) uses the same hero block: thumbnail image, name (same font/size), meta line, star rating. Even content-only screens (e.g., ingredient-list warm-up) get the full hero block — only the action section is hidden.

**Exception:** cart/delivered RESULT screens (the right phone in dual-phone, either phone in two-cart, single-cart-annotated screens) use the cart-row layout instead — item rows + subtotal, no hero block, no star rating. Real cart UIs don't carry the source recipe's star rating, and forcing one on breaks realism rather than protecting it. Single-row substitution cards (Rule 4) also skip the hero block entirely — see that rule.

**Why:** visual inconsistency reads as "broken" or "lower fidelity" and contaminates how participants judge the underlying UX.

### 9. Missing-item call-out convention

When an item is missing from a cart, label it consistently: **"Not available / Missing"**. Apply identical label across every missing-item stimulus.

### 10. Wrong-item stimulus isolation rule

Post-add wrong-item carts must NOT label the wrong item as "wrong," "swap," "substitute," or any other flag. Unprompted detection only works if the participant must notice the issue themselves.

**Why:** any label primes the participant and contaminates the detection rate.

**Exception:** if the task has been converted to dual-phone for visual consistency (and now tests prompted comparison instead of unprompted detection), the wrong-item flag is still off — but the question wording shifts from "did you notice anything?" to "compare image 1 and image 2." Document the methodological tradeoff (see [[usertesting-plan]] standing preferences on visual consistency).

**When the feature under test IS a disclosure/labeling mechanism** (e.g., testing whether a new "why this changed" card helps users catch a swap): this rule still governs the *unflagged baseline* task — that task exists specifically to measure the old, silent experience as a counterfactual, and must stay unflagged exactly as written above. It does NOT mean the product's own real disclosure UI has to be hidden on the task that's actually testing that UI — a card the live product would show is the stimulus being tested, not a researcher-added leak, and suppressing it tests the wrong thing entirely (the old experience, not the new one). Confirm with [[usertesting-plan]] which of the two the wrong-item/capstone task is meant to be — an unflagged baseline, or a flagged test of the real feature — and build accordingly; don't strip a real product surface because this rule reads as absolute. See the triangulation checklist's Sub-agent C row for the audit version of this same distinction.

### 11. Subtotal on every cart — and subtotal must equal line-item sum

Every cart screen shows a subtotal. After ANY edit that touches a price or line-item, recalculate every subtotal in the file. A simple `sum(line_item_prices) === subtotal` mental check per cart is the audit.

**Why:** participants notice. A subtotal that doesn't match line-items reads as "this prototype is broken" and triggers them to question every other detail (does the warning apply? is the count correct?). It also generates wasted "I think your math is wrong" verbal answers that aren't real signal.

### 12. Pre-reveal captions must NOT leak the failure mode

Any caption, sub-header, or context line that appears BEFORE the participant observes the stimulus must be neutral — never name the substitution, mismatch, or failure mode being tested.

❌ Leaky: "Option A · With substitute" / "Cart with quantity mismatch" / "This cart shows the wrong unit"
✅ Neutral: "Here are two carts for [recipe]." / "Here's your shopping cart." / no caption

**Why:** participants are supposed to *discover* the mismatch and react. A caption that pre-labels the variation tells them what to look for and contaminates the unprompted-noticing measurement.

Captions are allowed for purely descriptive labels (recipe name, "Cart A / Cart B" position chips) — never for the mechanic.

This rule governs everything the participant can see. It does NOT cover the internal researcher/programmer reference banner described in Rule 14 below, which names the failure mode on purpose — that banner is never participant-facing and must be removed or hidden before the file is fielded. See Rule 14 for exactly how the two rules coexist in the same file.

### 13. Question wording mirrors stimulus button text verbatim — HTML-side rule

If the recipe phone's button says "Add all 6 ingredients to cart," the question text must also say "you tapped 'Add all 6 ingredients to cart'" — not "Add all to cart" or "added everything." Whichever artifact is built FIRST sets the button text; the other one is drafted or revised to match it verbatim afterward. In practice that usually means HTML sets it (see the orchestrator's shared-context table) and the script side ([[usertesting-script]] Rule 15) keeps prompts in lockstep — but if a script already exists when this skill is invoked, its wording is authoritative and the HTML button text must match it instead. Never assume the other artifact exists; ask if it's unclear which was built first.

**Why:** if the question paraphrases the button, participants get distracted disambiguating which action is being referenced.

### 14. Section banners — internal reference chrome, matches the script's task numbering, NEVER shown to participants

Each section banner in the HTML matches the script's task number — e.g., `Task 4 · Tomato Basil Soup · 80% (Basil garnish missing)`. This is deliberately the same kind of information Rule 12 bans from participant-facing captions — that's intentional, because **the section banner is internal chrome for the researcher and programmer, not part of the stimulus.** It exists so the two of you can say "Task 4" and mean the same screen; a participant must never see it.

**Build it as internal-only, not as an assumption to remember:**
- Give it a distinct class, e.g. `.internal-ref-banner`, styled visibly different from any participant-facing text (a bold, obviously-a-label treatment) so it can't be mistaken for stimulus copy.
- Whoever screenshots or exports the file for UserTesting must crop it out / it must be hidden before a participant sees the screen. Don't rely on someone remembering this by convention alone — say so explicitly in the file's build notes, and treat "internal banners still visible" as a leak on the same footing as a leaky caption under Rule 12.
- If the file will be screenshotted as-is (not manually cropped), consider a print/export CSS rule that hides `.internal-ref-banner` and toggle it back on for internal review — whichever mechanism you use, note it in the header overview table so the next person doesn't re-discover the gap.

**Why:** prevents off-by-one errors when researcher and programmer cross-reference, without leaking the failure mode to participants — which is why it must stay separated from anything Rule 12 governs.

### 15. Header overview table at top of file

The HTML stimuli file includes a top-of-file overview table summarizing every task and what variation it tests. Gives the researcher a quick visual map; speeds debugging.

### 16. Default phone mockup specs

- iPhone-style frame (393 × 852 viewport approximation)
- Top bar with back chevron + title + heart icon
- 14px horizontal padding inside the phone body
- Apply identically to every phone in the HTML

### 17. Side-by-side phones share scaled width

When two phones appear side by side, scale each proportionally so both fit on a standard desktop screen without horizontal scroll.

### 18. `.phone--compact` variant for dense content

When a screen has more rows than the default phone frame can show, scope a `.phone--compact` modifier class applied ONLY to the affected task:

- Hero padding: 10×14 (smaller than default)
- Thumbnail: 52×52
- Banner padding: 7×16
- Row thumbnails: 44×44
- Row padding: 6px

Other tasks keep default sizing. Scope the compact variant — don't shrink the whole study.

### 19. Recipe/content simplification to isolate the test signal

When the task is "would the user actually [take action] on X?" (where X is a specific item or behavior), strip the source content down to the smallest set that forces a clean signal on X. Don't test 12 items when you're only measuring intent for 3 of them — noise overwhelms signal. The simplified set must still be believable.

### 20. Conditional follow-up banner — yellow "Shown only if…" callout

**This rule only applies to the rare, explicitly-approved exception to [[usertesting-plan]]'s default "no conditional logic" rule** (no branching, no skip logic, every participant sees every question). Most studies never trigger this rule at all — if the plan hasn't documented and approved a specific conditional follow-up in its Discipline notes, don't add branching to the HTML on your own judgment; build flat, per the default. When a study genuinely has an approved conditional question, mark it so the deviation is visible everywhere it matters, not just in the HTML.

Conditional questions (those that only fire for a subset of participants) get a yellow callout banner directly above the question card.

CSS:
```css
.conditional-banner {
  background: var(--conditional-bg);
  border-left: 4px solid var(--conditional-border);
  padding: 8px 12px;
}
```

Copy starts with **"Shown only if…"** stating the trigger condition in plain English. Lives above the question, never inside it — moderators and programmers spot the branching at a glance.

**Why:** UserTesting programmers wire branching by reading the HTML; an inline gray note gets missed.

### 21. Design tokens — use the established set, do NOT invent new colors

Every HTML stimulus uses the established design-token set so visuals stay consistent across tasks. Default Instacart-style token set (adapt for other brands):

| Token | Hex | Where it's used |
|---|---|---|
| `--ic-green` | `#0AAD0A` | Primary CTA, brand accent, success states |
| `--label-ink` | `#2D4A3E` | Section banners, headers, primary text |
| `--ic-bg` | `#FFFFFF` | Phone body background |
| `--row-divider` | `#E8E8E8` | Cart row dividers |
| `--meta-muted` | `#6B7280` | Meta labels, secondary text |
| `--asked-bg` | `#F3F4F6` | Single-row card asked-pane background (Rule 4) |
| `--added-bg` | `#E6F4EA` | Single-row card added-pane background (Rule 4) |
| `--star-color` | `#F5A623` | Hero-block star rating (Rule 8) |
| `--conditional-bg` | `#FEF3C7` | Conditional-question callout background (Rule 20) |
| `--conditional-border` | `#F59E0B` | Conditional-question callout left border (Rule 20) |

These 10 cover every pattern named elsewhere in this file — add the token block at the top of the HTML in `<style>` in full, even for a build that only needs a subset. **Never** introduce ad-hoc hex values inline — if a color beyond this set is genuinely required, add it to the token block AND document why.

**Why:** consistent visual language keeps the stimulus realistic and prevents accidental hierarchy signals (a "different green" reads as "different state").

### 22. Image-quality QA pass — before any stakeholder review or fielding

Run a dedicated image-accuracy pass before sharing or fielding. Audit every product image AND every emoji for:

1. **Cuisine / content accuracy** — image depicts the correct subject (e.g., tomato-basil soup hero, not generic red-bowl image)
2. **Preparation state** — culinary form is correct (e.g., culinary shallots, not flowering shallots; flat-leaf parsley not curly; cheese-and-ham omelet not plain egg omelet)
3. **Brand pattern** — if a brand badge references a brand, the product photo must match the brand
4. **Resolution** — no obvious upscaling artifacts, no compression banding around edges
5. **Emoji match** — recipe emoji accurately represents the content (e.g., 🍳 omelet should show egg + cheese, not generic food emoji)

**When:** after every HTML revision that touches a product row, AND as a final sweep before sending to stakeholders or fielding.

**Why:** image accuracy is a trust signal. Even one wrong product photo triggers participants to question every other detail (counts, subtotals, warnings) — and once trust is broken in one image, downstream verbal feedback gets distorted. Image-audit is the cheapest way to protect the most-expensive part of the study (participant time + recruit cost).

**No real product photography available (the common default for an early draft):** none of the plan/script/HTML skills define an image-sourcing pipeline, so don't wait on one. Build with clearly-representative emoji or generic stand-in art, run ONLY check 5 (emoji match) — checks 1–4 are un-runnable without real photos and skipping them is expected, not a gap to paper over — and mark the file **"DRAFT — placeholder imagery, not fielding-ready"** in the header overview table and build notes. Never field a study on placeholder imagery; the full 5-point pass only counts as complete once real photography replaces the placeholders and checks 1–4 are actually run against it.

## Standing preferences

- **Show 2–3 layout approaches before significant rebuilds.** Don't pick one and run — see Workflow step 1a for where this happens.
- **Pending vs. live HTML labeled clearly.** Mark `v2-queued (not pushed)` vs. `v1-live`. A brand-new file with no fielded version yet is `v1-draft (not yet fielded)` — don't reach for `v1-live` until it's actually live. Don't cite pending changes as canonical.
- **Flag every mismatch explicitly.** If a product image doesn't exist or a price would need to be invented, surface the conflict — don't paper over it.
- **Auto-open created HTML in browser.** After saving any HTML file, open it. If `open` (or the equivalent) fails — e.g. a headless, sandboxed, or remote session with no browser to open — don't treat that as a dead end: report the saved file's full path clearly instead, and note that the open step didn't run.
- **Name and place the file predictably.** Default filename pattern: `{study-name}-ut-stimuli-{v1-draft|v1-live|v2-queued|...}.html`. Save it alongside the study's plan/script docs if those already have an established location; otherwise ask where the deliverable should live rather than guessing a scratch path.
- **Visual consistency over methodological purity — document the tradeoff.** When a layout change improves visual consistency at the cost of a methodology constraint (e.g., converting a single-phone unprompted-detection task to dual-phone prompted-comparison), favor consistency BUT document the methodology that was traded away AND flag the affected metric for special handling.

## Workflow

1. Confirm the task list (task count, stimulus type per task) and the per-task inputs this skill needs (button text, image labels). Get these from an existing plan/script if one exists — invoking [[usertesting-plan]] and [[usertesting-script]] (via the Skill tool, if installed) is the fastest way to produce those artifacts properly. But when the ask is for fast pixels with no plan or script yet (a normal, common trigger for this skill — see "When to use this skill"), don't block on producing those first: confirm the handful of missing inputs directly with the requester in one message (task count, what each task is testing, and — per usertesting-plan's baseline-first rule — whether a 100%-success baseline task and a wrong-item/unprompted-detection capstone are both in scope), then proceed. HTML built this way is the authoritative source for button text and image labels until a script exists to reconcile against (Rule 13, Rule 6).
   - **1a. Show 2–3 layout approaches before building the full file**, per Standing preferences — even a quick verbal description of each option is enough for a fast-turnaround ask. Wait for a pick before building every task. Skip only if the requester has already specified the exact layout or explicitly asks to skip this step.
2. Set up the design-token block at the top of the HTML `<style>` — use the full Rule 21 set, not just the tokens the first task needs.
3. Build the header overview table.
4. For each task, build the section banner + stimulus layout (dual-phone / two-cart / single-row / single-cart-annotated).
5. Apply image-number labels under every phone in multi-image stimuli.
6. Verify recipe name continuity across phones.
7. Verify all CTA button text matches the corresponding script prompts verbatim (or vice versa — whichever artifact came first, per Rule 13).
8. Strip any leaky pre-reveal captions and any pre-revealing mismatch pills. Confirm every internal reference banner (Rule 14) is marked `.internal-ref-banner` and will be cropped/hidden before fielding — this is a leak check, not a nice-to-have.
9. Recalculate every subtotal: `sum(line_item_prices) === subtotal` per cart.
10. Run the image-quality QA pass on every product image and emoji (Rule 22) — including the placeholder-imagery flag if no real photography exists yet.
11. Auto-open the HTML in browser (see Standing preferences for the no-browser fallback).

## Bundled resources

- `assets/dual-phone-template.html` — copy-paste starter HTML with design tokens, hero block, dual-phone layout
- `assets/two-cart-template.html` — A/B side-by-side cart starter
- `assets/single-row-card-template.html` — single-row substitution card starter with `.single-row-card` CSS
- `references/design-tokens.md` — full token set + when to extend
- `references/image-qa-checklist.md` — the 5-point image audit
- `references/subtotal-audit-script.md` — quick script for sum-verification per cart

## Hand-offs

- For study-level structure → invoke [[usertesting-plan]]
- For question wording and platform tagging → invoke [[usertesting-script]]
- For full pipeline → invoke [[usertesting-orchestrator]]
