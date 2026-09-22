# Intake Checklist — the 8 questions, with disambiguation guidance

Copy this per study run. Ask in the batches SKILL.md's intake section instructs (max 4 per AskUserQuestion batch — Q1–Q4 first, then Q5–Q8 once the first batch is answered, or fewer per batch if the requester has already answered some inline).

The examples below span multiple domains on purpose — a badge, an onboarding flow, a search result, a recipe card, a cart. None of them is the "real" template; swap in whatever surface this study is actually testing.

---

## Q1 — What decision does this study inform?

The one-sentence "why." Not the topic — the decision the topic is standing in for.

- Good answer: "Whether to ship the substitution confidence badge as-is, or redesign the wording before it goes to more users."
- Too vague to build from: "Feedback on the new feature." Push back once: "Feedback that would change what — ship/no-ship, which of two wordings, or something else?"

## Q2 — What's the stimulus/feature under test?

The actual screen, component, or flow. Get specific enough to build a mockup from — a name alone ("the badge") isn't enough if there are multiple states or placements.

- Ask for: where it lives (which screen/flow), what states it can be in (e.g., high/medium/low confidence, or first-time vs. repeat), and whether a PRD/design file already exists to pull exact copy and visuals from.

## Q3 — What's the primary comparison or axis being tested?

Name the axis explicitly — this is what Rule 6 (comparison pairs) and the coverage matrix both key off. An axis is a dimension with at least two named points on it, not a single condition.

- Generalized worked example: if the study is testing a trust-signal treatment across severity levels, the axis might be "signal wording × how wrong the underlying data is" — e.g., a treatment shown when the system is very confident vs. barely confident vs. wrong. Name your own axis the same way: [dimension] × [the specific values that dimension takes in this study].
- If the requester gives you a single condition ("test the badge"), ask what it's being compared against — a prior version, no badge at all, a competitor's pattern, or nothing (pure reaction, no comparison). "No comparison" is a valid answer; document it as such rather than inventing one.

## Q4 — Who's the target participant?

Screener-level detail: role/persona, platform (app vs. web), any must-have or must-exclude behavior (e.g., "has placed a grocery order in the last 30 days," "has never used the feature before"). If self-initiated with no separate screener doc, this answer becomes the screener draft.

## Q5 — What failure mode(s) matter most?

The thing that would be bad if it happened and this study didn't catch it — a user missing a wrong substitution, a user not noticing a badge at all, a user misreading a confidence label as a warning. This drives which tasks are mandatory (see Rule 3 — every study needs at least one wrong-item/unprompted-detection task unless the requester explicitly waives it).

- If the requester says "I don't know, just general feedback" — offer 2–3 candidate failure modes based on Q1–Q3 and ask them to pick or add their own, rather than defaulting to "no failure mode" (that silently drops Rule 3's mandatory task).

## Q6 — Any content/stimulus constraints?

Real product names vs. placeholders, specific recipes/items that must (or must not) appear, brand voice constraints on copy, accessibility requirements. Also surface here if the requester wants the stimulus HTML built by a downstream skill ([[usertesting-html]]) vs. static screenshots supplied separately.

## Q7 — Sample size

Number of participants (or a range). If the requester doesn't have a number, don't invent one — flag it as an open blocker in the plan's discipline notes and note that no skill in this pipeline supplies statistical sizing guidance; sourcing a number is on the requester or a DS partner.

## Q8 — Fielding window

When this needs to go live and when results are needed back. Drives whether the study can afford multiple task types/failure modes or needs to cut scope (see "Time budgeting" in SKILL.md).

---

## Cross-cutting disambiguation notes

- **Jargon-free rephrasing.** If a requester answers with UserTesting platform jargon they don't actually mean precisely (e.g., calling everything a "survey"), don't correct them mid-intake — capture their intent in your own words in the plan, and let [[usertesting-script]] handle the precise platform-tag translation later.
- **Partial answers folded into the original ask.** If the requester's kickoff message already answers 3 of the 8 (common when a PRD or Slack thread is attached), restate those back for confirmation rather than re-asking, and only actively ask for the remainder.
- **"Just use your judgment" requests.** Still surface the 2–3 candidate answers for any genuinely open question (this is a standing preference, not optional) — but keep the ask tight: one batch, clearly labeled as decisions the requester can rubber-stamp rather than open-ended questions.
