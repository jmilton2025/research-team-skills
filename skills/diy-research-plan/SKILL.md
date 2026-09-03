---
name: diy-research-plan
description: Use when a request has already been triaged into the DIY track and a designer, PM, or content lead needs a short planning doc — objective, who's being tested, the key question, why unmoderated is the right method, rough timeline — before building the screener and script. Triggers on "write a DIY research plan", "quick plan for this self-serve study", "plan this out before I build the test", "what's the plan for this DIY study", or "/diy-research-plan".
---

# DIY Research Plan

Generates the short, plain-language planning doc that sits between DIY triage and the screener/script build — the fifth step in Instacart Research's self-serve pipeline: `/diy-triage` → **`/diy-research-plan`** → `/screener` → `/unmod-script` → `/diy-packet`. Grounded in Erika Hall's *Just Enough Research* (right-size the plan to the size of the decision — the planning document itself should stay proportional, not just the study), Indi Young's *Listening Deeply* (frame who's being tested by what they do, not just who they are), Steve Portigal's and Tomer Sharon's bias-elimination and non-leading question-design principles, Nikki Anderson's plain-language single-sentence framing of a research goal, Virginia Braun and Victoria Clarke's thematic-analysis logic (referenced here only as a forward pointer to where it's actually applied — the findings section of `/diy-packet` — since this doc doesn't do analysis itself), Nielsen Norman Group's guidance on when unmoderated testing is the right call, and dscout / the UserTesting Blog's self-serve-testing conventions. Also applies the Instacart-internal **AIxUXR Playbook**'s H.E.A.R.T. framework, leaning hardest on the same two principles `/screener` and `/unmod-script` lean on: **Amplifying** and **Responsible**.

## Guiding philosophy: H.E.A.R.T., planning-doc edition

| Letter | Principle | What this means for a DIY plan |
|--------|-----------|----------------------------------|
| **H** | **Human-centered** | The point of writing anything down before building the test is to protect the participants who'll take it — a rushed script is where leading questions and confusing tasks sneak in. |
| **E** | **Experience-focused** | This doc is the requester's first checkpoint. If it's confusing or feels like homework, they'll skip it next time and go straight to building — and skip the safety net with it. |
| **A** | **Amplifying** | This skill does the part a researcher would normally do in a five-minute kickoff chat — naming the one question, sanity-checking the method, sizing the ask — so the requester doesn't need training to do it themselves. |
| **R** | **Responsible** | A one-page plan is still a real plan. It gets a method check and an explicit escalation path, same as its heavier `/research-plan` counterpart — just condensed. |
| **T** | **Transparent** | The doc says plainly what it is *not* — not a screener, not a script, not a defense of methodology — so nobody mistakes a five-minute plan for five minutes of due diligence on something bigger. |

## When to use this skill

Use this skill when:
- `/diy-triage` has already routed a request to the DIY track, and the next thing needed is a short doc aligning the requester and their research partner on what's about to be built
- A designer, PM, or content lead has a self-serve study in mind and wants to think it through in writing before jumping to the screener or script
- A research partner wants a fast, consistent way to sanity-check a DIY request before it's built, without asking for a full RPP
- Someone asks for "just enough of a plan" for a study that clearly doesn't need `/research-plan`'s depth

Trigger phrases:
- "/diy-research-plan"
- "write a DIY research plan"
- "quick plan for this self-serve study"
- "plan this out before I build the test"
- "what's the plan for this DIY study"
- "I need something short before I build the screener"

**Do NOT use this skill when:**
- DIY-vs-researcher-led hasn't been decided yet — run `/diy-triage` first; this skill assumes that call is already made
- The ask is small and unambiguous enough that a separate plan doc adds nothing — see "When you might skip this" below and go straight to `/diy-packet`
- The requester has research training and wants the full researcher-led depth — use `/research-plan`
- What's actually needed is the screener or the script itself, not the plan that precedes them — use `/screener` or `/unmod-script`

## How this differs from `/research-plan`

Both skills answer "what should this study look like," for two different audiences and two very different levels of depth — deliberately, not by omission:

| | `/research-plan` (researcher-led) | `/diy-research-plan` (DIY / self-serve) |
|---|---|---|
| **Audience** | A trained UX researcher | A designer, PM, or content lead with no research training |
| **Length** | Full ResOps Research Project Plan, 13 sections, ~8+ pages | About half a page — six short sections, shorter even than `/diy-packet` |
| **Method justification** | Minimum-evidence framing with 1-2 alternatives, defended against sample-size canon when questioned | A three-item checklist confirming the `/diy-triage` fit call still holds — no alternatives compared, no citations |
| **Existing insights** | A standalone section, top 3-5 findings, each verbatim-sourced | One line: did you check first, yes or no |
| **Hypotheses, Themes, RACI** | All present, each its own section or header block | All cut — a DIY study is a single-round check, not a hypothesis-testing program with a Research Priorities mapping |
| **What's downstream** | `/mod-guide` (a moderator reads and adapts it live) | `/screener` and `/unmod-script` (this doc only points to them — it doesn't draft their content) |

Full section-by-section mapping lives in `references/plan-vs-rpp-comparison.md` — read it when someone asks "why doesn't this have a [Themes / Hypotheses / Existing Insights] section" or wants to see exactly what got cut and why.

## When you might skip this and go straight to `/diy-packet`

Not every DIY-track ask needs a standalone plan step. In practice, some self-serve requesters fold the handful of planning fields — what's being tested, the one learning goal, the audience, the prototype link — directly into the top of their script-build document, skipping a separate plan doc entirely and going straight from intake to a bundled packet. For a small, single-task, low-stakes ask, that's the right call: a separate plan doc would just restate the same five fields a second time.

**Skip straight to `/diy-packet` when:**
- There's exactly one task and one question — nothing to weigh against an alternative approach
- The requester already knows who they're testing and it's an easy, obvious screen
- Nobody downstream — a stakeholder, a research partner — needs to see and sign off on the approach before it gets built

**Run this `/diy-research-plan` step instead when:**
- There's more than one plausible method, task order, or audience and someone needs to choose between them
- There's real ambiguity about who to test, what the single most important question is, or whether unmoderated is even the right call
- A research partner or stakeholder will want to see the plan before the screener and script get built
- `/diy-triage`'s escalation watch flagged something worth a second look before time gets spent on a full build

The few extra minutes this step costs are cheap insurance against building the wrong script.

---

## Core workflow

### Step 0 — Confirm this step is worth running

Before drafting, apply the "when to skip" test above. If the ask is genuinely a one-task, one-question, easy-screen study, confirm before routing away rather than deciding unilaterally:

> "This looks like a one-task, easy-screen ask — I'd skip the standalone plan and go straight to `/diy-packet`. Sound right, or is there something here worth a quick plan first?"

Once confirmed, route to `/diy-packet` instead of drafting a plan nobody needed. Otherwise, continue.

### Step 1 — Gather Inputs

Ask for whatever the requester already has — the `/diy-triage` output, a PRD, a Slack thread, or a rough idea. Accept any format.

> "To sketch the plan, share what you've got: what you're testing, the one thing you most need to know, who should test it, and roughly when you need results. If `/diy-triage` already ran, its output covers most of this."

Minimum inputs before drafting:
1. **What's being tested** — feature, screen, or flow
2. **The one learning goal** — if the requester gives you several, that's a signal to trim before drafting (Hall's right-sizing principle), same as `/diy-packet`'s rule
3. **Who should test it** — rough, behavior-first audience description
4. **Whether this has been checked already** — search existing research (Glean / the team's research-insights channel) before treating this as net-new
5. **Rough timeline** — when results are needed
6. **The actual stimulus link/asset** — not just confirmation that a stimulus exists. This is a hard gate, and which status it gets depends on *why* it's unconfirmed: if the requester hasn't produced a working link or file at all, that's on them — use the blocked-status convention in `../../references/output-status-and-labeling-conventions.md` (§1): add **`Status: BLOCKED — waiting on stimulus link from requester`** directly under the doc header, and hold off treating the plan as ready to hand to `/screener` and `/unmod-script` until it's in hand. If the stimulus is real and ready but this session's tooling simply can't fetch or verify it (e.g. a Figma link that exists but can't be pulled) — that's a tool limitation, not the requester's fault — use **`Status: PENDING — <what's unverified and why>`** instead (same reference, §1) and proceed rather than holding the plan back
7. **Who the research partner is** — the person to loop in if this needs a second look (goes in the doc header and Section 6). If the requester says no researcher is involved at all, don't leave this blank or invent a name — default to naming the research team generally (or whoever owns this pipeline) and say so explicitly in the doc

### Step 2 — Propose the Plan Structure

Show the six sections this plan will contain and confirm before generating:

> "Here's what I'll sketch out — about half a page, not a full plan:
> 1. What we're trying to learn
> 2. Who's being tested
> 3. Why unmoderated is the right call here
> 4. What we'll ask (rough shape only)
> 5. Rough timeline
> 6. When to loop a researcher back in
>
> Sound right?"

**Reading "sound right?" answers.** Not every confirmation here is genuine sign-off — a requester who's new to this, or just wants it off their plate, may answer with pure deferral ("whatever you think is right," "you're the expert," a fast "yeah, sure") rather than actually weighing the proposal. When that's what's happening, say so explicitly in the doc (see `/diy-triage`'s "Requester confidence note" field, if the upstream input carries one) and default to the more conservative, more thorough option at that checkpoint rather than the leanest one — a requester who's deferring needs more active guidance from here, not a formality-only checkpoint. This applies to Step 0's skip-or-continue confirm above as much as it does here.

### Step 3 — Generate the Plan

Apply the content rules below and produce the OUTPUT TEMPLATE. If it's running past roughly half a page, that's a sign either the study has outgrown DIY scope (loop back to `/diy-triage`) or that content belonging in `/screener` / `/unmod-script` has crept in here — trim it back rather than let the doc grow.

---

## OUTPUT TEMPLATE

```
# DIY Research Plan: [Study name — plain language, e.g. "New sort option — does it make sense at a glance?"]

**Owner (running this):** [Requester name]
**Research partner (loop in if stuck):** [Researcher name — if the requester says no one specific is assigned, name the research team generally instead of leaving this blank]
**Date:** [Month Year]

---

## 1. What We're Trying to Learn

| Field | What to fill in | Your input |
|---|---|---|
| **The one thing we need to know** | If you can't say it in one sentence, it's too many questions for one DIY study — pick the most important one and park the rest (unless `/diy-triage` already validated multiple sub-questions as in-scope for this one DIY study — see Rule 1's carve-out below — in which case unify them into one sentence instead of picking just one) | [ ] |
| **Why it matters** | What decision this unblocks, or what happens if we don't answer it | [ ] |
| **Did we check first?** | Search existing research (Glean / research-insights) before treating this as unanswered — note what you found, even if it's "nothing" | [ ] |

## 2. Who's Being Tested

*(Full detail lives in the screener — see `/screener`. This is just enough to know what to ask for.)*

- **Who:** [one-line audience description — what they DO, not just who they are]
- **How many:** [N — a handful of sessions is normal for a DIY read; this isn't a statistically sized sample]

## 3. Why Unmoderated Is the Right Call Here

*("Unmoderated" just means the participant does the test on their own, with no researcher watching live to guide them or answer questions — as opposed to a moderated session, where someone is. This is a fast confirm, not a defense — the fit call itself was already made in `/diy-triage`. If any box stops being true once you dig in, stop and say so rather than writing the plan anyway.)*

- ☐ This is a single-round, task-based question — not a "why do they do this" question
- ☐ There's a prototype or live surface ready to show people
- ☐ One round of feedback is enough; no follow-up probing needed

## 4. What We'll Ask (rough shape — not the full script)

*(Full script lives in `/unmod-script`. List the tasks in one line each so a reviewer can sanity-check the shape before it's written out in full.)*

1. [Task 1 — one line, the goal not the UI, e.g. "find a way to reorder the list"]
2. [Task 2]
3. [Task 3, if needed — most DIY studies need 2-4, rarely more]

- If the task count was already deliberately scoped upstream (by the requester or by `/diy-triage`), don't second-guess it against the "2-4" guideline above — carry it forward as-is
- If more than one variant/stimulus exists, note how it should be distributed across sessions and flag it for `/unmod-script` to resolve — deciding which participant sees which variant, in what order, and how to keep that balanced across the group (sometimes called assignment, order, and counterbalancing) is `/unmod-script`'s territory, not this skill's

## 5. Rough Timeline

*(If the requester only gave relative timing — "this week," "next sprint" — keep it relative in the table below; don't invent a calendar date.)*

| Milestone | Target date |
|---|---|
| Screener + script ready | [ ] |
| Test launched | [ ] |
| Results needed by | [ ] |

## 6. When to Loop a Researcher Back In

Stop and message [Research partner] if:
- The "one thing we need to know" turns out to need a follow-up question you can't ask in an unmoderated format
- Two or more of the Section 3 boxes stop being true once you actually look closely
- The answer would change a decision bigger than the one this study was scoped for
```

---

## CONTENT GENERATION RULES

1. **One learning goal, stated once.** If the input carries more than one core question, trim to DIY scope before drafting (Hall) rather than letting the plan quietly carry all of them. **Carve-out:** if `/diy-triage`'s output already explicitly validated multiple sub-questions as in-scope for this one DIY study, don't drop any of them to get to "one" — unify them into a single umbrella learning-goal sentence instead.
2. **Guidance sits next to every fill-in field**, in plain language — never assume the requester knows research vocabulary. Same rule `/diy-packet` uses, applied one step earlier.
3. **Section 3 is a fast confirm, not a defense.** No alternatives compared, no citations, no sample-size rationale — that rigor belongs to `/research-plan`. This plan only re-checks that the `/diy-triage` fit call still holds now that more detail exists.
4. **Tasks in Section 4 describe goals, not UI**, even in one-line shorthand — "find a way to reorder the list," not "tap the sort icon." Bias-elimination (Portigal, Sharon) applies from the first rough draft, not just the final script.
5. **This is not the screener or the script.** Point to `/screener` and `/unmod-script` for their full detail rather than drafting it here — duplicating their content is the single fastest way this doc stops being "half a page."
6. **Never skip the existing-research check.** Section 1's "did we check first?" row is mandatory, not optional — matches the same principle `/diy-packet` and `/diy-triage` enforce.
7. **Escalation triggers are concrete, not a vague "reach out if needed."** Section 6 must name actual signals, same discipline `/diy-packet`'s escalation section uses.
8. **Length discipline: roughly half a page.** This plan is shorter than `/diy-packet` itself — it only has to align two people on what's about to be built, not carry the study. If it's growing, something belongs in `/screener`, `/unmod-script`, or a full `/research-plan` instead.
9. **Plain language throughout.** No unexplained acronyms or research jargon left standing without a plain-English gloss.
10. **One document, six sections, no more.** Don't add a Themes, Hypotheses, RACI, or Existing-Insights-with-verbatim-sources section just because `/research-plan` has one — see `references/plan-vs-rpp-comparison.md` for why each of those was cut on purpose, not by oversight.

---

## Tool usage

- **AskUserQuestion** — confirm the "worth running" check (Step 0) and the proposed structure (Step 2). See `../../references/interactive-input-conventions.md` for the fallback if `AskUserQuestion` is unavailable.
- **Read** — read pasted content, `/diy-triage` output, or local files the requester shares
- **Glean** (`mcp__glean_default__search` / `read_document`) — check whether this question is already answered before drafting Section 1's "did we check first?" row
- **`/diy-triage`** — the upstream input; if it hasn't run yet, route there first
- **`/screener`** — downstream; Section 2 hands off to it
- **`/unmod-script`** — downstream; Section 4 hands off to it
- **`/diy-packet`** — the alternative when Step 0 says this step isn't worth running, and the eventual bundler once the screener and script exist
- **`/research-plan`** — the escalation target whenever Step 0, Section 3, or Section 6's triggers fire
- **`references/plan-vs-rpp-comparison.md`** — the full section-by-section diff against `/research-plan`'s output template

---

## Sources & methodology

| Source | Contribution to this skill |
|--------|----------------------------|
| **Erika Hall**, *Just Enough Research* | Right-sizing the plan to the decision — the reason this doc is a half-page and not a scaled-down RPP |
| **Indi Young**, *Listening Deeply* | Framing "who's being tested" (Section 2) by what people do, not just who they are |
| **Steve Portigal**, *Interviewing Users* / *Doorbells, Danger, and Dead Batteries* | Bias-elimination discipline, applied to the rough task list in Section 4 before it's ever written out in full |
| **Tomer Sharon**, *Validating Product Ideas* | Non-leading question construction; validating that something works vs. understanding why |
| **Nikki Anderson** | Plain-language, single-sentence framing of a research goal — the basis for Section 1's "one thing we need to know" |
| **Virginia Braun & Victoria Clarke** | Thematic-analysis logic — not used here directly; cited as the forward pointer to where it's actually applied, in `/diy-packet`'s findings section |
| **Nielsen Norman Group** | Guidance on when unmoderated testing is the right method — the basis for Section 3's fast confirm |
| **dscout** / **UserTesting Blog** | Self-serve and DIY-testing conventions — informed the overall shape (learn → who → why this method → rough ask → timeline → escalate) |
| **AIxUXR Playbook** (Instacart-internal) | H.E.A.R.T. framework, adapted for the planning-doc stage — particularly Amplifying (this skill does the five-minute-kickoff-chat work a researcher would normally do live) and Responsible (a one-page plan still gets a method check and an escalation path) |
