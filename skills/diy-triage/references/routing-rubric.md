# DIY Triage — Routing Rubric

The full decision rubric behind `/diy-triage`. Consult this whenever the five triage questions in `SKILL.md` Step 2 don't cleanly resolve to one track — the table below shows how each factor pulls, and the sections after it cover the escalation and parallel-track cases in more depth.

## Core decision factors

| Factor | Pulls toward DIY | Pulls toward researcher-led | Pulls toward both |
|---|---|---|---|
| **Who's asking** | A designer, PM, or content lead working solo, comfortable reading their own data | A researcher is already looped in, or the requester explicitly wants a researcher's read | A solo requester needs a fast answer now *and* knows a bigger call is coming that will need a researcher |
| **Reversibility / stakes** | Low-stakes, easy to undo — a copy variant, a layout tweak, a small flow adjustment | Structural or hard to unwind — a new flow, a policy shift, something that reshapes a core journey | The immediate change is low-stakes but sits inside a larger, harder-to-reverse initiative |
| **Timeline pressure** | Answer needed this week or next; no runway to recruit and moderate | Weeks of runway; the decision isn't time-boxed | A tactical answer is needed now, with a deeper study following on a longer clock |
| **Type of question** | "Can they find it / complete it / understand it / prefer A over B" — a can-they-do-it question, answerable by watching completion and choice | "Why do they struggle / what are they actually trying to do / how does this change trust or behavior over time" — a why question, answerable only by a live, adaptive conversation | Both a can-they-do-it check and a why question live in the same brief |
| **Who needs to be satisfied** | The requester can read the unmoderated data themselves and act on it | Leadership, a cross-functional partner, or the requester wants a researcher's synthesis and sign-off before acting | A fast tactical read satisfies immediate needs; a researcher's deeper read is still expected for the larger decision |
| **Prior research on this surface** | Well-trodden ground — a pattern the team has tested before, low ambiguity in what "success" looks like | Net-new territory, or prior unmoderated reads have come back ambiguous | Some prior grounding exists for the tactical piece, but the strategic piece is genuinely new |

**How to weigh a mixed set:** no single factor is a veto. If four of six factors point DIY and one points researcher-led, that one factor is worth naming explicitly in the escalation watch rather than overriding the DIY call — see below.

## The escalation case — start DIY, revisit if X

A DIY routing call is a starting bet, not a permanent one. Every DIY (and "both") recommendation carries a named escalation watch. Below are the conditions that most commonly justify moving a study from DIY to researcher-led mid-stream, drawn from the pattern of studies that started self-serve and were later promoted:

| Trigger | What it looks like | Why it justifies escalation |
|---|---|---|
| **Ambiguous or contradictory read** | Completion rates look fine, but comments or drop-off patterns don't add up to a coherent story | An unmoderated read can surface *that* something's off but can't ask *why* — that gap is exactly what a researcher closes |
| **Scope grows mid-study** | What started as a single flow tweak turns out to touch a bigger, harder-to-reverse decision once the team is in it | The reversibility factor changed after the original triage call was made — re-run the rubric against the new scope |
| **A new stakeholder wants the "why"** | Someone who wasn't in the loop at kickoff — often more senior, or from an adjacent team — asks for the reasoning behind the numbers, not just the numbers | This is a "who needs to be satisfied" shift; the original DIY output was scoped for a different audience |
| **Timeline loosens** | The decision that felt urgent at triage time turns out to have more runway than expected | Removes the single biggest constraint that pushed the original call toward DIY |
| **Pattern repeats across rounds** | The same DIY study design keeps producing the same "can't tell why" result across iterations | A recurring can't-tell-why result is itself evidence the underlying question is a why-question, not a can-they-do-it question |

When any of these show up, don't silently keep going on the DIY track and don't silently swap to researcher-led either — re-run Step 2's questions against the new information and state the updated call the same way as a first-time triage. The requester should see the same one-line recommendation + reason + next-step format both times.

## The parallel case — both tracks on one brief

Route both, in parallel, only when the brief contains two genuinely different questions that need two different instruments — not as a hedge against an unclear rubric result. The tell: Q4 (type of question) or Q5 (who needs to be satisfied) comes back split rather than landing on one side.

When routing both:

- **Treat them as two separate rounds**, each with its own timeline and its own deliverable — a combined study plan that tries to answer a can-they-do-it question and a why-question with one instrument usually answers neither well.
- **Sequence them independently.** The DIY read often turns around first (unmoderated moves faster); the researcher-led study may still be recruiting. Don't hold the DIY deliverable hostage to the moderated study's timeline, or vice versa.
- **Cross-reference in both deliverables.** Each round's output should note that a parallel read exists on the other track, so a reader of just one document doesn't mistake it for the whole picture.
- **Watch for the DIY round changing the researcher-led round's design.** If the tactical read surfaces something unexpected, it's fair (and often valuable) to fold that into the moderated study's discussion guide before fielding — that's collaboration between the two rounds, not scope creep.

## Quick-reference: track → downstream skills

| Track | Chain |
|---|---|
| DIY | `/screener` → `/unmod-script` → `/diy-packet` |
| Researcher-led | `/rpp` (research-plan) → `/mod-guide` → `/synth` (report) |
| Both | Both chains above, run concurrently as separate rounds |
