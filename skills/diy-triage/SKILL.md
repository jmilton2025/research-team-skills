---
name: diy-triage
description: Use when a designer, PM, content lead, or fulfillment partner shows up with a research need (a PRD, a product brief, or a loose ask) and the question is whether it can be self-serve or needs a UX researcher. Triggers on "should this be DIY", "do I need a researcher for this", "triage this research ask", "can I self-serve this", or "/diy-triage".
---

# DIY Research Triage

This is the entry gate for Instacart Research's self-serve research pipeline. It takes a raw research ask — a PRD, a product brief, a Slack paste, or just a loose question someone is turning over — and routes it to the right path *before* anyone spends time building a study. Grounded in Erika Hall's *Just Enough Research* (right-size the method to the decision, don't default to the heaviest tool available), Tomer Sharon's *Validating Product Ideas* (the distinction between validating that something works and understanding why), Indi Young's *Listening Deeply* (behavioral "why" questions need a human listening, not a form), Steve Portigal (what only a moderated conversation can surface), Nikki Anderson's research-operations triage practice, Nielsen Norman Group's moderated-vs-unmoderated selection guidance, and dscout / UserTesting Blog's DIY-vs-moderated decision frameworks. It also carries the Instacart-internal **AIxUXR Playbook**'s H.E.A.R.T. philosophy — specifically **Amplifying**: self-serve tools amplify a non-researcher's ability to get a fast, reliable read; they don't replace a researcher when the question needs interpretation a form can't provide.

## Guiding principle

Every triage call comes down to one question underneath all the others: **does answering this need someone to *watch and interpret*, or just to *count and confirm*?**

- **Count-and-confirm** questions — can people find it, complete it, understand it, prefer A over B — are answerable by a well-built unmoderated read. This is the DIY track.
- **Watch-and-interpret** questions — why they struggle, what they're actually trying to do, how a change reshapes behavior or trust over time — need a researcher watching and probing live. This is the researcher-led track.
- Most asks are a mix. The job of this skill is to name which parts are which, not to force a single answer onto a mixed ask.

## When to use this skill

Use this skill when:
- A designer, PM, content lead, or fulfillment-side partner has a research need and doesn't know (or hasn't decided) whether it needs a researcher
- A PRD or product brief just landed and someone needs a fast read on scope before committing time
- A researcher is triaging their own intake queue and wants a consistent, defensible routing call
- A DIY study is already underway and something has changed — new data, new stakeholder, wider scope — and it's worth asking whether it should escalate

Trigger phrases:
- "/diy-triage"
- "should this be DIY or do I need a researcher"
- "do I need a researcher for this"
- "triage this research ask"
- "can I self-serve this"
- "here's a PRD, what kind of research does this need"

## The two tracks (and the third option)

| Track | What it produces | Downstream skills |
|---|---|---|
| **DIY** — self-serve, no researcher required | An unmoderated read the requester runs and interprets themselves | `/diy-research-plan` → `/screener` → `/unmod-script` → `/diy-packet` |
| **Researcher-led** — needs a UX researcher | A moderated study with a researcher driving design, fieldwork, and synthesis | `/rpp` (the team's research-plan skill) → `/mod-guide` → `/synth` (the team's report skill) |
| **Both, in parallel** — one brief, two reads | A fast tactical DIY read *and* a deeper moderated study, run side by side, each documented as its own round | Both chains above, run concurrently, cross-referenced in the final deliverable |

"Both" is not a hedge — it's the right call whenever a single brief contains a count-and-confirm question *and* a watch-and-interpret question that neither track alone can answer. See Step 3.

## Step 1 — Take in the ask

Ask the requester to paste whatever they have:

> "Paste what you've got — a PRD, a product brief, a Slack thread, kickoff notes, or just describe the ask in your own words. I'll pull out what matters for routing and ask a few quick questions."

Accept any format. If it's a Google Doc link, read it via Glean (`mcp__735858e3-df5d-4167-8a6d-f4047ed77a06__read_document`) or `google-docs:fetch-google-doc`.

From the material, extract (don't invent — if something isn't in the source, ask rather than guess):
- **The decision this research is meant to inform** (what happens differently depending on the answer)
- **Who's asking** (their role, and whether a researcher is already looped in)
- **Timeline** (when the decision needs to be made)
- **What's already known** (has this shipped before, is this net-new, is there prior research to build on)

## Step 2 — Ask the triage questions

Run these through `AskUserQuestion`, batched (up to 4 per call, so this fits in one or two batches). Each question exists because it's a documented decision factor — see `references/routing-rubric.md` for the full rubric these map to.

**Q1 — Who owns this decision?**
- A designer, PM, or content lead working solo (**leans DIY**)
- A designer/PM partnering with a researcher already (**leans researcher-led or both**)
- Not sure yet / whoever's asking hasn't decided

**Q2 — How reversible is the decision this research feeds?**
- Low-stakes, easy to undo — a copy tweak, a layout variant, a small flow change (**leans DIY**)
- Structural or hard to unwind once shipped — a new flow, a policy change, something that reshapes a core journey (**leans researcher-led**)
- Somewhere in between / depends what we find

**Q3 — What's the timeline pressure?**
- Need a read this week or next (**leans DIY** — unmoderated turns around faster)
- Weeks of runway, decision isn't urgent (**leans researcher-led**, room to recruit and moderate)

**Q4 — What kind of question is this, underneath?**
- "Can people find it / complete it / understand it / pick A over B" — a **can-they-do-it** question (**leans DIY**)
- "Why do they struggle / what are they actually trying to do / how do they feel about it" — a **why** question (**leans researcher-led**)
- Honestly, both — there's a surface-level check *and* a deeper "why" buried in the same ask (**leans both**)

**Q5 — Will a self-serve read satisfy whoever's waiting on this, or does someone expect a researcher's synthesis?**
- The requester can read the data themselves and make the call (**leans DIY**)
- Leadership, a cross-functional partner, or the requester themselves wants a researcher's interpretation and sign-off (**leans researcher-led**)
- Both — a fast tactical answer now, and a researcher's deeper read for the bigger call (**leans both**)

## Step 3 — Make the call

Weigh the five answers against `references/routing-rubric.md`. In general:

- **All or most answers lean DIY** → route DIY.
- **All or most answers lean researcher-led** → route researcher-led.
- **Q4 or Q5 comes back "both," or the answers split roughly down the middle** → route both, in parallel.
- **Answers conflict in a way the rubric doesn't resolve cleanly** → say so, name the tension, and ask the requester to break the tie rather than guessing.

State the call in one line, then the reason, then the next command:

> **Recommendation: [DIY / Researcher-led / Both]**
> **Why:** [one sentence tying back to the 1-2 answers that decided it]
> **Next:** [the specific next skill/command to run]

Do not pad this with a restatement of everything already discussed. The requester just answered five questions — they know the inputs.

### When "both" is the right call

Route both, in parallel, when the brief genuinely contains two different questions that need two different instruments — not when someone just wants extra reassurance. The tell is Q4 or Q5 coming back split: a fast completion/preference check *and* a "why do people behave this way" question living in the same ask. When this happens:

1. Route the count-and-confirm half through DIY (`/diy-research-plan` → `/screener` → `/unmod-script` → `/diy-packet`).
2. Route the why half through the researcher-led chain (`/rpp` → `/mod-guide` → `/synth`).
3. Document each as its own round (own timeline, own deliverable) rather than trying to force one combined study plan — they answer different questions and usually run on different clocks.
4. Note in both deliverables that a parallel read exists on the other track, so neither one is read as the whole picture.

## Step 4 — Name the escalation watch, every time

Even on a clean DIY call, name what would change the answer. This is not optional — a DIY study that quietly needed a researcher three weeks in is the single most expensive routing failure this skill exists to prevent.

Always close with an **escalation watch**: one to three concrete conditions that, if they show up mid-study, mean it's worth revisiting the call. Common triggers (full list in the rubric reference):

- The DIY read comes back ambiguous, contradictory, or "clean but hollow" — people complete the task but something about *why* doesn't add up
- The scope grows from a single, contained decision into a structural or strategic one
- A stakeholder who wasn't in the loop at triage time shows up wanting the "why," not just the "did it work"
- The timeline loosens enough that a moderated study becomes feasible where it wasn't before

Phrase it plainly:

> **Escalation watch:** if [specific trigger], come back and re-triage — this might need to move to the researcher-led track.

This is the explicit support for starting DIY and promoting mid-stream. It is not a failure state; a study that starts DIY and escalates once real signal justifies it is triage working correctly, not triage working incorrectly the first time.

## Output template

Keep the full triage output to what's below — this is a routing call, not a report. Match length to the decision, per usual.

```
## Triage: [one-line description of the ask, in plain language]

**Recommendation:** [DIY / Researcher-led / Both]
**Why:** [1 sentence]

**Next step(s):**
- [Specific next command — e.g. "/diy-research-plan" or "/rpp"]
- [If "both": both chains, named separately]

**Escalation watch:** [1-3 concrete triggers that would change this call]
```

## Content rules

1. **Extract, don't invent.** Every fact used in triage (timeline, requester role, reversibility) comes from what was pasted or answered — never assumed from the brief's tone or the researcher's guess.
2. **One-line reason, every time.** The recommendation is only as useful as the reason attached to it. "DIY" with no reason is not a triage call — it's a coin flip.
3. **Name the next command, not just the track.** "Researcher-led" isn't actionable on its own; "researcher-led — start with `/rpp`" is.
4. **"Both" is a real answer, not a fallback for indecision.** Only route both when Q4 or Q5 genuinely split — not as a way to avoid picking.
5. **Escalation watch is mandatory, not just for edge cases.** Every DIY and every "both" call gets one. Researcher-led calls can skip it only when there's no plausible scope-down (rare).
6. **Never fabricate a decision-owner or a deadline.** If Q1 or Q3 wasn't answered clearly, ask again rather than defaulting.
7. **Stay a router.** This skill hands off to `/diy-research-plan`, `/screener`, `/unmod-script`, `/diy-packet`, `/rpp`, `/mod-guide`, and `/synth` — it does not draft any of their content itself.

## Tool usage

- **AskUserQuestion** — Step 2's triage questions
- **Glean `read_document`** or **`google-docs:fetch-google-doc`** — read a linked PRD or brief
- **Read** — pasted content or local files
- **references/routing-rubric.md** — the full decision rubric behind Step 2 and Step 3; consult it whenever an answer set doesn't cleanly resolve

## Sources

- Hall, E. *Just Enough Research* — right-sizing method to the decision; the case against defaulting to the heaviest available tool
- Sharon, T. *Validating Product Ideas* — validating that something works vs. understanding why
- Young, I. *Listening Deeply* — why behavioral "why" questions require a human listening live, not a form
- Portigal, S. *Interviewing Users* / *Doorbells, Danger, and Dead Batteries* — what only a moderated conversation surfaces
- Anderson, N. — research-operations triage practice, User Research Academy
- Nielsen Norman Group — moderated vs. unmoderated method selection guidance
- dscout *People Nerds* and UserTesting Blog — DIY-vs-moderated decision frameworks
- **Instacart AIxUXR Playbook** (internal) — H.E.A.R.T. philosophy, specifically "Amplifying": self-serve tools extend a non-researcher's reach without replacing a researcher's judgment call
