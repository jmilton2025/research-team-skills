# Cross-artifact diff template

Use one block per finding when surfacing drift between plan, script, and HTML (either during the standard build's triangulation or a drifted-study repair pass). Keep findings atomic — one block per mismatch, not a paragraph covering several.

```
### [Blocker | Mismatch | Polish] — <short title>

**Where:** <Plan | Script | HTML> — <task/question/section reference>

**Plan says:**   <quote or paraphrase, or "n/a">
**Script says:**  <quote or paraphrase, or "n/a">
**HTML shows:**   <quote or paraphrase, or "n/a">

**Why it's a problem:** <one sentence — what breaks or gets confusing if this ships as-is>

**Suggested fix:** <the specific edit, and which artifact it lands in>

**Decision needed:** <yes/no — if yes, what's being asked of the requester>
```

## Worked examples

```
### Blocker — Task count mismatch

**Where:** Plan (6 tasks) vs. Script (5 task blocks)

**Plan says:**   Coverage matrix lists 6 conditions including a "confirm-required vs. auto-applied" A/B task
**Script says:**  Only 5 task blocks — the A/B task was never drafted
**HTML shows:**   n/a (not yet built)

**Why it's a problem:** The core research question (confirm vs. auto-apply preference) has no instrument. Fielding as-is answers everything except the question Eng actually needs.

**Suggested fix:** Add the missing task block to the script before proceeding to HTML.

**Decision needed:** No — this is a build-completeness gap, not a judgment call.
```

```
### Mismatch — CTA text doesn't match between script and HTML

**Where:** Script Q3, HTML Task 1

**Plan says:**   n/a
**Script says:**  "Imagine you tapped 'Add all 7 ingredients to cart.'"
**HTML shows:**   Cart phone CTA button reads "Add all 8 ingredients to cart"

**Why it's a problem:** Participants cross-check the prompt against the button; a count mismatch causes them to pause and disambiguate instead of reacting to the actual test content.

**Suggested fix:** Correct the script prompt to "8" to match the HTML (or vice versa — confirm which count is actually correct against the recipe's real ingredient list first).

**Decision needed:** No — recount and fix.
```

```
### Polish — Cart A/Cart B chip present without an Image 1/Image 2 label

**Where:** HTML Task 4 (two-cart A/B)

**Plan says:**   n/a
**Script says:**  Q11 references "Cart A or Cart B"
**HTML shows:**   "Cart A" / "Cart B" chips under each phone, no "Image 1" / "Image 2" label

**Why it's a problem:** Every multi-phone stimulus should carry the image-number label as the stable reference point (position can randomize; the label doesn't). Cart A/B chips are a supplementary caption, not a substitute.

**Suggested fix:** Add "Image 1" / "Image 2" labels alongside the existing Cart A/B chips in the HTML.

**Decision needed:** No.
```
