# Shared context handoff — plan → script → HTML

What to carry forward at each handoff point in the pipeline, and who owns each piece of information. This is the same table that lives in SKILL.md's "Shared context" section, expanded with a per-step checklist — use whichever is faster to reference.

## Ownership table

| Context element | Set by | Used by | Notes |
|---|---|---|---|
| Task count, task order, fixed-vs-randomized slots | Plan | Script (numbering), HTML (section banners) | |
| Stimulus type per task (dual-phone, two-cart, single-row, etc.) | Plan | HTML (layout) | |
| Synthesis-tail format (drag-to-rank vs single-choice vs verbal ranking) | Plan | Script (Q-block) | |
| Question wording, action-ladder text, choice options | Script | HTML (layouts and captions must not contradict the prompt) | |
| Button/CTA copy per task (e.g., "Add all 6 ingredients to cart") | **Script** | HTML | Script authors the exact copy as part of the prompt, since Script is produced before HTML in the pipeline order. HTML renders a button with this exact text — it does not invent its own wording. This is a one-way handoff; don't let HTML's rendered button become a second source of truth that Script has to "catch up" to. |
| Image-number labels (Image 1 / Image 2) per phone | HTML | Script | Applies to every multi-phone stimulus, including two-cart A/B tasks. A "Cart A / Cart B" chip is an optional supplementary caption on top of the image number, never a substitute. Asked-vs-delivered dual-phone tasks reference a single object ("the cart you received"), not a two-way choice — they don't need "image 1 or image 2" wording at all. |
| Total question count + estimated minutes | Script | Not built into HTML by default | usertesting-html has no standard footer/end-card rule. Only pass this forward if the study explicitly asked for an on-screen "Question Q of N" footer. |

## Step 1 → Step 2 handoff (Plan → Script)

Before invoking usertesting-script, confirm you can hand it:
- [ ] Final task count and order (which slots are fixed, which are randomized)
- [ ] Stimulus type per task (drives which platform-tagging + pinning notes the script needs)
- [ ] The synthesis-tail format chosen (drag-to-rank / single-choice+escape / verbal ranking) — this determines which question-type template to use
- [ ] Session-length budget (so the script author can sanity-check the running time estimate against it)
- [ ] Any add-on questions already classified Absorb/Hold/Reject

## Step 2 → Step 3 handoff (Script → Plan+Script → HTML)

Before invoking usertesting-html, confirm you can hand it:
- [ ] Task count and the exact section-banner label for each (recipe/subject name + task number + variation, matching Rule 14 in usertesting-html)
- [ ] Stimulus type per task (layout pattern to build)
- [ ] The exact button/CTA copy per task, as authored in the script (HTML must render this verbatim, not paraphrase it)
- [ ] Which tasks need image-number labels vs. which are single-object dual-phone tasks that don't need comparison wording
- [ ] Whether a "Question Q of N" footer was explicitly requested (default: no)

## After Step 3 (HTML → back to Script, verification only)

HTML doesn't get to change wording, but it can surface problems the earlier steps didn't anticipate — e.g. a recipe/content name that's too long for the phone frame, or a subtotal that doesn't reconcile. Flag these back rather than quietly adjusting the script or plan to fit:
- [ ] Any button copy that had to be shortened or reworded to fit — flag, don't silently diverge from the script prompt
- [ ] Any stimulus type substitution made for visual-consistency reasons (see the "visual consistency over methodological purity" standing preference) — document in all three artifacts, not just HTML
