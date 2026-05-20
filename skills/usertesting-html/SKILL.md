---
name: usertesting-html
description: Build or audit the visual stimuli HTML for a UserTesting study. Use this skill when asked to "build UT stimuli," "create the stimulus HTML," "design the test mockups," "review/audit stimuli HTML," "fix subtotals," "audit product images," or to apply visual patterns (dual-phone, two-cart side-by-side, single-row substitution cards, image labels, design tokens). Outputs HTML mockups with proper Instacart-style design tokens, image-number labels, subtotal arithmetic verified, no-leak captions, and image-quality QA. Universal — patterns generalize to any topic.
metadata:
  type: skill
---

# UserTesting HTML Skill

Build the visual stimuli HTML that participants see during a UserTesting study. This skill owns layout patterns (dual-phone, two-cart, single-row card), design tokens, image labels, subtotal arithmetic, no-leak caption discipline, and image-quality QA.

For study-level structure, hand off to [[usertesting-plan]]. For question wording and platform tagging, hand off to [[usertesting-script]]. For end-to-end pipeline orchestration, use [[usertesting-orchestrator]].

## When to use this skill

Trigger phrases:
- "Build/create the UserTesting stimuli"
- "Make the test mockups"
- "Design the stimulus HTML"
- "Review/audit the stimuli HTML"
- "Fix the cart subtotals"
- "Audit the product images"
- "Add image labels to the phones"

## Core rules

### 1. Visual layout patterns — pick based on what the question asks

| Question goal | Layout pattern |
|---|---|
| Compare what was asked vs. what was delivered | Dual-phone side-by-side: asked on left, delivered on right |
| A/B preference between two strategies | Two-cart side-by-side, **randomize L/R** |
| React to a specific UI signal (label, badge, warning) | Single cart with the signal visible, no comparison |
| Isolated substitution decision (no full cart context) | Single-row stimulus card (asked → delivered) |
| Pre-action expectation-setting | Content-only screen with no action button |

### 2. Dual-phone pattern

- **LEFT phone** = source/recipe view (title, steps, ingredient list, primary CTA button)
- **RIGHT phone** = result view (cart, deliverable, output state)
- Both visible at once on one screen
- For asked-vs-delivered framing, the source phone is always LEFT (no L/R randomization)

### 3. Two-cart side-by-side pattern (A/B preference)

- Two cart phones side by side on one screen
- **Randomize which appears L vs R** — position bias is real
- Use neutral "Cart A / Cart B" position chips ONLY if the question references them; otherwise no caption

### 4. Single-row substitution card pattern (isolated decision)

Build with this CSS pattern so it reads as one decision, not a list.

**Grid:** 3-column, `grid-template-columns: 1fr 44px 1fr` (asked-pane · arrow column · added-pane)

**Panes:**
- **Asked pane** — gray background (signals "this is what was wanted"), label above the row: `Recipe asked:`
- **Arrow column** — fixed 44px width, single arrow glyph (→), no background
- **Added pane** — green background (signals "this is what was delivered"), label above the row: `We added:`

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

### 7. Meta-line order standardized — never reorder

Standard format: `Serves [N] · [N] ingredients · [T] min`

NEVER reorder. Apply identically across every recipe/item in the study.

**Why:** visual scanning becomes faster when the order is invariant.

### 8. Hero block parity across all stimuli

Every recipe/item screen uses the same hero block: thumbnail image, name (same font/size), meta line, star rating. Even content-only screens (e.g., ingredient-list warm-up) get the full hero block — only the action section is hidden.

**Why:** visual inconsistency reads as "broken" or "lower fidelity" and contaminates how participants judge the underlying UX.

### 9. Missing-item call-out convention

When an item is missing from a cart, label it consistently: **"Not available / Missing"**. Apply identical label across every missing-item stimulus.

### 10. Wrong-item stimulus isolation rule

Post-add wrong-item carts must NOT label the wrong item as "wrong," "swap," "substitute," or any other flag. Unprompted detection only works if the participant must notice the issue themselves.

**Why:** any label primes the participant and contaminates the detection rate.

**Exception:** if the task has been converted to dual-phone for visual consistency (and now tests prompted comparison instead of unprompted detection), the wrong-item flag is still off — but the question wording shifts from "did you notice anything?" to "compare image 1 and image 2." Document the methodological tradeoff (see [[usertesting-plan]] standing preferences on visual consistency).

### 11. Subtotal on every cart — and subtotal must equal line-item sum

Every cart screen shows a subtotal. After ANY edit that touches a price or line-item, recalculate every subtotal in the file. A simple `sum(line_item_prices) === subtotal` mental check per cart is the audit.

**Why:** participants notice. A subtotal that doesn't match line-items reads as "this prototype is broken" and triggers them to question every other detail (does the warning apply? is the count correct?). It also generates wasted "I think your math is wrong" verbal answers that aren't real signal.

### 12. Pre-reveal captions must NOT leak the failure mode

Any caption, sub-header, or context line that appears BEFORE the participant observes the stimulus must be neutral — never name the substitution, mismatch, or failure mode being tested.

❌ Leaky: "Option A · With substitute" / "Cart with quantity mismatch" / "This cart shows the wrong unit"
✅ Neutral: "Here are two carts for [recipe]." / "Here's your shopping cart." / no caption

**Why:** participants are supposed to *discover* the mismatch and react. A caption that pre-labels the variation tells them what to look for and contaminates the unprompted-noticing measurement.

Captions are allowed for purely descriptive labels (recipe name, "Cart A / Cart B" position chips) — never for the mechanic.

### 13. Question wording mirrors stimulus button text verbatim — HTML-side rule

If the recipe phone's button says "Add all 6 ingredients to cart," the question text must also say "you tapped 'Add all 6 ingredients to cart'" — not "Add all to cart" or "added everything." The HTML side enforces this by keeping button text stable; the script side ([[usertesting-script]] Rule 15) keeps prompts in lockstep.

**Why:** if the question paraphrases the button, participants get distracted disambiguating which action is being referenced.

### 14. Section banners match the script's task numbering

Each section banner in the HTML matches the script's task number — e.g., `Task 4 · Tomato Basil Soup · 80% (Basil garnish missing)`.

**Why:** prevents off-by-one errors when researcher and programmer cross-reference.

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

Conditional questions (those that only fire for a subset of participants) get a yellow callout banner directly above the question card.

CSS:
```css
.conditional-banner {
  background: #FEF3C7;  /* amber-50 */
  border-left: 4px solid #F59E0B;  /* amber-500 */
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

Add the token block at the top of the HTML in `<style>`. **Never** introduce ad-hoc hex values inline — if a new color is genuinely required, add to the token block AND document why.

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

## Standing preferences

- **Show 2–3 layout approaches before significant rebuilds.** Don't pick one and run.
- **Pending vs. live HTML labeled clearly.** Mark `v2-queued (not pushed)` vs. `v1-live`. Don't cite pending changes as canonical.
- **Flag every mismatch explicitly.** If a product image doesn't exist or a price would need to be invented, surface the conflict — don't paper over it.
- **Auto-open created HTML in browser.** After saving any HTML file, open it.
- **Visual consistency over methodological purity — document the tradeoff.** When a layout change improves visual consistency at the cost of a methodology constraint (e.g., converting a single-phone unprompted-detection task to dual-phone prompted-comparison), favor consistency BUT document the methodology that was traded away AND flag the affected metric for special handling.

## Workflow

1. Confirm the plan inputs (task count, stimulus type per task) and script inputs (button text per task, image labels per task). If unknown, invoke [[usertesting-plan]] and [[usertesting-script]] first.
2. Set up the design-token block at the top of the HTML `<style>`.
3. Build the header overview table.
4. For each task, build the section banner + stimulus layout (dual-phone / two-cart / single-row / single-cart-annotated).
5. Apply image-number labels under every phone in multi-image stimuli.
6. Verify recipe name continuity across phones.
7. Verify all CTA button text matches the corresponding script prompts verbatim.
8. Strip any leaky pre-reveal captions and any pre-revealing mismatch pills.
9. Recalculate every subtotal: `sum(line_item_prices) === subtotal` per cart.
10. Run the image-quality QA pass on every product image and emoji.
11. Auto-open the HTML in browser.

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
