# Image-Quality QA Checklist

Full reference for Rule 22. Run this pass after every HTML revision that
touches a product row, and as a final sweep before sending to stakeholders
or fielding.

## The 5-point audit

Run all 5 checks against every product image AND every emoji in the file.

| # | Check | Ask yourself |
|---|---|---|
| 1 | **Cuisine / content accuracy** | Does the image depict the correct subject? (e.g., a tomato-basil soup hero shot, not a generic red-bowl stock photo) |
| 2 | **Preparation state** | Is the culinary/physical form correct? (e.g., culinary shallots not flowering shallots; flat-leaf parsley not curly; a cheese-and-ham omelet shown as cheese-and-ham, not a plain egg omelet) |
| 3 | **Brand pattern** | If a brand badge or label references a brand, does the product photo actually match that brand's real packaging/product? |
| 4 | **Resolution** | No obvious upscaling artifacts, no compression banding around edges? |
| 5 | **Emoji match** | Does the emoji accurately represent the content? (e.g., 🍳 for an omelet should read as egg + cheese, not a generic food emoji standing in) |

## No real product photography available (the common default for an early draft)

None of the plan/script/HTML skills in this repo define an image-sourcing
pipeline — don't wait on one before building.

- Build with clearly-representative emoji or generic stand-in art.
- Run **ONLY check 5** (emoji match). Checks 1–4 are un-runnable without real
  photos — skipping them at this stage is expected, not a gap to paper over.
- Mark the file **"DRAFT — placeholder imagery, not fielding-ready"** in both
  the header overview table and the build notes.
- Never field a study on placeholder imagery. The full 5-point pass only
  counts as complete once real photography replaces every placeholder and
  checks 1–4 are actually run against it.

## Why this matters

Image accuracy is a trust signal. Even one wrong product photo triggers
participants to question every other detail in the stimulus — counts,
subtotals, warnings — and once trust is broken in one image, downstream
verbal feedback gets distorted. Running this checklist is the cheapest way
to protect the most expensive part of the study: participant time and
recruit cost.

## Quick pass log (copy into build notes)

```
Image QA pass — [date]
File: [filename]
Real photography available: [yes / no — placeholder]

Task 1 — [item name]
  1. Cuisine/content accuracy: [pass / fail / N/A — placeholder]
  2. Preparation state:        [pass / fail / N/A — placeholder]
  3. Brand pattern:             [pass / fail / N/A — placeholder]
  4. Resolution:                [pass / fail / N/A — placeholder]
  5. Emoji match:                [pass / fail]

[repeat per task/product row]

Overall: [DRAFT — placeholder imagery, not fielding-ready / fielding-ready]
```
