# Coverage Matrix Template

The coverage matrix is Output-structure component 2 — the plan-level table that proves every research question (Intake Q1/Q3) maps to at least one task, and every task earns its slot. This is also what Layer-1↔Layer-2 triangulation checks against (see usertesting-orchestrator's `triangulation-checklist.md`), so keep row-per-task granularity even for a small study.

## Single-axis studies (one comparison dimension)

Use this when Intake Q3 names one axis (e.g., confidence-level wording: high vs. medium vs. low).

| Task # | Research question covered (Q1/Q3) | Axis value(s) tested | Stimulus type | Fixed or randomized slot | Notes |
|---|---|---|---|---|---|
| 1 | [e.g., "Do users notice the badge unprompted?"] | [n/a — detection task] | Wrong-item/unprompted-detection | Fixed (first) | Mandatory per Rule 3 |
| 2 | [e.g., "Does high-confidence wording read as trustworthy?"] | [High] | Single-row card | Randomized-middle | |
| 3 | [ ] | [Medium] | Single-row card | Randomized-middle | |
| 4 | [ ] | [Low] | Single-row card | Randomized-middle | |
| 5 | [e.g., "Overall reaction after seeing the range"] | [n/a — synthesis] | — | Fixed (last) | Feeds synthesis tail |

## Two-axis studies (grid — comparison × treatment)

Use this when the study crosses two dimensions (e.g., failure severity × two competing designs).

| Task # | Axis A value | Axis B value | Research question covered | Stimulus type | Fixed/randomized | Notes |
|---|---|---|---|---|---|---|
| 1 | [ ] | [ ] | [ ] | Dual-phone side-by-side | Randomized-middle | |
| 2 | [ ] | [ ] | [ ] | Dual-phone side-by-side | Randomized-middle | |

Leave a cell blank rather than guessing — an unfilled cell is a visible gap the requester can catch; a guessed value can pass review unnoticed.

## Filling it out

1. Start from Intake Q1 (the decision) and Q3 (the axis) — list every value the axis takes. Each value needs at least one task, unless the requester explicitly scopes one out (document why in Discipline notes if so).
2. Add the mandatory wrong-item/unprompted-detection task from Rule 3 (usually Task 1, since it needs to run before participants are primed).
3. Cross-check against Intake Q5 (failure modes) — every named failure mode should appear as either its own task or an explicit note on why it's covered elsewhere.
4. Total the tasks against the "Time budgeting" table in SKILL.md before finalizing — if the matrix doesn't fit the fielding window from Q8, cut using one of the three documented scope options rather than silently dropping a row.
5. Sanity-check ordering rules against Task-design Rules 4–6 (fixed bookends, randomize-the-middle, adjacent comparison pairs) and the "Precedence when rules 4–6 collide" note — a fully-fixed order is a valid outcome, not a failure to randomize.

## What NOT to put in this matrix

- Question wording (that's [[usertesting-script]]'s job — this matrix names *what* gets tested, not the exact prompt)
- Button/CTA copy or visual layout (that's [[usertesting-html]])
- Synthesis-tail question format choice (goes in the Synthesis tail component — see `synthesis-tail-templates.md` — though it's fine to reference which task numbers feed into it here)
