---
name: diy-packet
description: Use when the DIY-track pieces for a self-serve study — a research plan, screener, and/or unmoderated script — already exist and need to be bundled into one condensed, shareable kit a designer or PM can actually run the study from. This is the final assembly/handoff step in the DIY pipeline, not where the plan gets drafted. Triggers on "DIY research packet", "self-serve test packet", "build me a DIY packet", "designer-led unmoderated study", or "/diy-packet".
---

# DIY Research Packet Builder

Assembles a condensed, self-serve research packet for the **DIY track** — a single short document a designer or PM can pick up and run an unmoderated study from without a researcher moderating. This is the **last stop** in the DIY pipeline (`/diy-triage` → `/diy-research-plan` → `/screener` → `/unmod-script` → `/diy-packet`): by the time this skill runs, the study has already been scoped, screened, and scripted upstream. This skill's job is to bundle those existing outputs — plus stimuli and launch instructions — into one shareable kit, not to re-decide the learning goal, audience, or questions from scratch.

Grounded in Erika Hall's *Just Enough Research* (right-sizing scope to the decision at hand), Nielsen Norman Group's guidance on when unmoderated testing is (and isn't) the right method, Steve Portigal and Tomer Sharon's bias-free question-design principles — translated here into scaffolding a non-researcher can follow without training — Nikki Anderson's plain-language framing of a research goal, Virginia Braun and Victoria Clarke's thematic-analysis logic (scaled down to a one-pass read), dscout and the UserTesting Blog's self-serve/DIY-testing best practices, and Instacart's internal **AIxUXR Playbook** H.E.A.R.T. framework — particularly **Amplifying** (the AI does the bias-scrubbing and structuring work a researcher would normally do live) and **Responsible** (guardrails don't disappear just because a researcher isn't moderating).

## Guiding philosophy: H.E.A.R.T. (AIxUXR Playbook)

| Letter | Principle | What this means for a DIY packet |
|--------|-----------|-----------------------------------|
| **H** | **Human-centered** | Participants still deserve non-leading questions and clear consent, even with no moderator live to build rapport or repair a confusing task on the fly. |
| **E** | **Experience-focused** | The packet itself is the requester's whole experience of "doing research." If it's confusing, they'll write a biased script and never know it. |
| **A** | **Amplifying** | This skill does the part a researcher would normally do live — catching leading language, structuring tasks, sizing the sample — so the requester doesn't have to be trained to do it. |
| **R** | **Responsible** | A DIY study still needs a fit check, a bias pass, and an escalation path. "Self-serve" is not "unsupervised forever" — the packet says exactly when to loop a researcher back in. |
| **T** | **Transparent** | The packet is explicit about what it is *not* covering (no follow-up probing, no moderator judgment calls) so the requester doesn't over-trust the data it produces. |

## When to use this skill

Use this skill when:
- The DIY-track pieces already exist — a `/diy-research-plan` output, a `/screener`, and/or an `/unmod-script` — and now need to be bundled into one document a designer or PM can actually pick up and run
- A researcher is closing out a DIY intake and needs to hand the requester everything in one shot (plan summary, screening criteria, test questions, stimuli/launch steps, and a findings template) instead of several separate docs
- Someone asks for "the lightweight version" of a research plan, or says the full plan is overkill — and the underlying DIY plan, screener, and script are already drafted or being drafted alongside this
- The deliverable needs to be handed to someone who has never run a study before and won't have a researcher walking them through it live

Trigger phrases:
- "/diy-packet"
- "build me a DIY packet"
- "give me a self-serve test packet"
- "I need something a PM can run without me"
- "make this DIY-friendly"
- "bundle this into a packet"
- "condense this into something [name] can run themselves"

Do NOT use this skill when:
- No `/diy-research-plan` exists yet for this study — run that first (or `/diy-triage` if it's not even clear this belongs in the DIY track at all). This skill assembles a plan's output; it doesn't decide the learning goal or method from scratch.
- The study needs a moderator present (motivations, mental models, multi-path journeys, anything needing follow-up probing) — that's a researcher-led study; use `/research-plan` and `/mod-guide` instead
- The requester already has research training and just wants the full plan — use `/research-plan`
- The ask is to write the test questions or the participant screen themselves, outside a packet — those are `/unmod-script`'s and `/screener`'s jobs; this skill bundles their *output*, not replacements for running them

## How this differs from `/research-plan`

`/research-plan` and `/diy-packet` cover the same underlying decision — "what should this study look like" — but for two different audiences, and the difference is deliberate, not accidental:

| | `/research-plan` (researcher-led) | `/diy-packet` (DIY / self-serve) |
|---|---|---|
| **Audience** | A trained UX researcher, who understands methodology tradeoffs and bias risk | A designer or PM with no research training, running the study alone |
| **Length** | Full ResOps-format Research Project Plan — many sections, ~8+ pages | One short document, roughly **a quarter the length** of a full plan |
| **Sections** | Background, Existing Insights, Objectives, Key Research Questions, Hypotheses, Method, full RACI, Timeline, Appendix | What you're testing, who to test with, what to ask, how to run it, how to read results — five sections, no more |
| **Language** | Research vocabulary is expected and used (objectives vs. research questions, saturation, TEDW stems) | Plain language only. No unexplained research jargon — every term is either dropped or explained inline |
| **Depth of methodology defense** | Cites saturation literature, defends sample size, documents alternatives considered | States the number and moves on — the method is already pre-decided as DIY-appropriate by the fit gate carried over from `/diy-research-plan` |
| **What's missing on purpose** | Nothing — it's the deep version | Existing-insights review, hypothesis section, full RACI, methodology alternatives, timeline milestones — all cut. A DIY packet assumes someone already decided this doesn't need that depth |
| **Safety net** | Researcher's own judgment, live in the room | Built into the document: a fit-gate checklist, hardcoded bias-resistant wrap-up questions, and an explicit "stop and call a researcher" list |

If a request turns out to need the researcher-led depth mid-build — the topic touches motivations, requires follow-up probing, or the requester keeps asking "but what if they say X" — stop and say so; route to `/research-plan` instead of stretching this skill to cover it.

## How this differs from `/diy-research-plan`

Both sit in the DIY track, but at opposite ends of it — one decides the study, the other packages it to run:

| | `/diy-research-plan` (upfront) | `/diy-packet` (final handoff) |
|---|---|---|
| **When it runs** | Right after `/diy-triage` routes a request to DIY | Last — after `/screener` and `/unmod-script` have already produced their output |
| **Job** | Decide and scope the study: what's being tested, the single learning goal, rough audience, rough method | Package everything needed to actually run it: one document bundling the plan, the screening criteria, the test questions, and the stimuli/launch steps |
| **Where content comes from** | Derived fresh from the requester's input | Assembled from upstream outputs — this skill summarizes, it doesn't re-decide |
| **Output** | A short planning doc | A shareable, fill-in-ready kit |

If `/diy-research-plan`'s output doesn't exist yet for a study, that's the signal to run it first — not to draft plan-level content (learning goal, audience, method) inside this skill.

---

## Core workflow

### Step 0 — Confirm the Upstream Pieces Exist

This skill assembles; it doesn't re-decide. Before drafting, check what's already been produced upstream for this study:

| Piece | Produced by | If missing |
|---|---|---|
| The plan (what's being tested, the learning goal, rough audience/method) | `/diy-research-plan` | Run that first — don't improvise a learning goal or scope inside the packet |
| Screening criteria | `/screener` | Run that first, or hand-author from the plan's audience description if no dedicated screener exists yet |
| Test questions | `/unmod-script` | Run that first, or hand-author from the plan's learning goal if no dedicated script exists yet |
| Fit for DIY at all | `/diy-triage` | If nobody's confirmed this belongs in DIY (vs. researcher-led), stop and route there — this skill assumes that call was already made |

If the plan genuinely doesn't exist and there's no time to run `/diy-research-plan` separately, it's fine to gather the same minimum inputs inline (what's being tested, the single learning goal, the design link, who to test with, timeline) — but say plainly that this packet is doing double duty as plan-and-packet, so the requester knows the plan wasn't reviewed on its own.

### Step 1 — Gather the Pieces to Bundle

Ask for whatever already exists, and accept any format — a `/diy-research-plan` doc, a screener, a script, a Slack thread, or just links.

> "To build your DIY packet, share what's already been put together: the research plan (or the rough idea if there isn't one yet), the screener or audience description, the test questions or script if drafted, and the stimulus/design link. I'll bundle it into one runnable kit."

What the packet needs, and where it should come from:
1. **What's being tested** — from the plan's scope
2. **The single learning goal** — from the plan (if there isn't a plan yet and the requester hands you five goals directly, that's a signal to route to `/diy-research-plan` first rather than trimming scope inside the packet)
3. **The prototype, design link, or stimuli** — from the plan or the requester directly; if the study compares multiple items or versions, collect each one (see Section 4a in the OUTPUT TEMPLATE)
4. **Who should test it** — from `/screener`'s output, or the plan's rough audience description if no dedicated screener exists yet
5. **The test questions** — from `/unmod-script`'s output, or hand-authored from the plan's learning goal if no dedicated script exists yet
6. **Timeline** — from the plan

### Step 2 — Propose the Packet Structure

Show the sections this packet will contain (see OUTPUT TEMPLATE below) and confirm before generating — same courtesy as any other plan in this repo, just against a much shorter structure:

> "Here's what I'll build — a one-page packet, not a full plan:
> 1. Is this right for DIY? (quick fit check, carried over from the plan)
> 2. What you're testing
> 3. Who to test with
> 4. What to ask + test materials
> 5. How to run it + how to read results
>
> Sound right, or is there something specific you need added?"

### Step 3 — Assemble the Packet

Apply the content rules below and produce the OUTPUT TEMPLATE by pulling from the upstream outputs gathered in Step 1 — summarize and format, don't re-derive. Keep the whole document to roughly **a quarter the length of a full Research Project Plan** — if it's running long, that's a sign content belongs in `/diy-research-plan` or `/research-plan` instead, not that this document needs another section.

---

## OUTPUT TEMPLATE

```
# DIY Test Packet: [Study name — plain-language, e.g. "New checkout button — is it noticeable?"]

**Owner (running this):** [Requester name]
**Research partner (loop in if stuck):** [Researcher name]
**Date:** [Month Year]

---

## 1. Is This Right for DIY?

*(Carried over from `/diy-research-plan`'s fit check — this isn't re-run from scratch here, just restated so the requester sees it before they start building.)*

Quick check before you build anything — self-serve unmoderated testing works well for this kind of study when:

- ☐ You're testing a specific task or reaction, not "why do people do this"
- ☐ There's a design or prototype link ready to show people
- ☐ One round of feedback is enough — you don't need to follow up based on what someone says
- ☐ You checked existing research first and this genuinely hasn't been answered

If you checked all four — you're good to go. If not, stop here and talk to [Research partner] before building the test.

## 2. What You're Testing

*(Pulled from `/diy-research-plan`'s output — this section summarizes the plan, it doesn't re-decide it.)*

| Field | What to fill in | Your input |
|---|---|---|
| **Feature / area** | The specific part of the product this is about | [ ] |
| **Learning goal** | The ONE most important question — if you can't say it in one sentence, it's too many questions for one DIY test | [ ] |
| **Starting scenario** | The one-line story that puts someone in the right frame of mind before they start (e.g., "Imagine you're shopping for a weeknight dinner") | [ ] |
| **Design / prototype link** | The single link people will test — or "see Section 4a" if there's more than one | [ ] |

## 3. Who to Test With

*(Full detail lives in the screener — see `/screener`. This is the short version so you know what you're asking for.)*

- **Who:** [one-line audience description, behavior first — not just demographics]
- **How many:** [N — DIY studies are typically small; a handful of sessions is enough for a qualitative read, not a statistically sized sample]
- **Screening criteria:** [bullet list — the 2-4 things that make someone the right fit]

## 4. What to Ask

*(Full script lives in `/unmod-script`. This is the shape it follows — every question here has already been checked for leading language, so keep this phrasing if you can.)*

**Before they see anything:**
1. [Context question — broad, doesn't hint at what you're about to show them]
2. [Context question, if needed]

**Task [1]: [Plain name for this step]**

| Field | What to fill in | Your input |
|---|---|---|
| **Where they start** | The screen or state the participant begins on | [ ] |
| **What to ask them to do** | Describe the goal, not the UI — "find a way to…" not "tap the button" | [ ] |
| **What you want to learn here** | The one question this task is actually answering | [ ] |

*(Repeat the Task block for each screen or step — most DIY packets need 2-4, rarely more.)*

**If this is a comparison test (two versions, or several items reacted to the same way) instead of a step-by-step flow:** replace the Task block above with one repeated question set applied to each item — same questions, once per item, e.g. "Which version gives you a clearer sense of what would happen? / What would you do here? / Why?" List each item once, reusing the identical question wording for all of them, and add a comprehension-check question (a multiple-choice "which of these best matches what you think this means" with an "I'm not sure" option) wherever the test is checking whether specific wording is understood, not just which version people prefer.

**Wrap-up (always include these — they catch anything the task-specific questions miss):**
1. [Optional: 1-3 questions comparing or summarizing the whole experience]
2. "What was the most confusing or unexpected part of this experience?" — *(fixed — always ask this one)*
3. "If you could change one thing about what you just saw, what would it be?" — *(fixed — always ask this one)*

## 4a. Test Materials (only if there's more than one item or version)

*(Skip this section entirely for a single-link, single-flow test — it's only needed when the study reacts to multiple stimuli, e.g. several items or an A/B comparison.)*

| Item / version | Link or asset | Notes (e.g. which label or variant this one shows) |
|---|---|---|
| [ ] | [ ] | [ ] |

**If this is a two-version comparison:** note which version each participant sees first, and alternate it across participants (e.g. half see version A first, half see version B first) so no single version has an unfair "seen first" advantage.

## 5. How to Run It

1. Build your audience using the criteria from Section 3.
2. Load the test questions from Section 4 into your unmoderated testing tool, in order — and if Section 4a lists multiple items or versions, load all of them and set up the alternating order noted there.
3. Preview the test yourself end-to-end before sending it out.
4. Launch, and check back once responses start coming in.

## 6. How to Read the Results

*(This is a findings summary, not a full report — see `/report` if this needs to go to leadership.)*

| Field | Your input |
|---|---|
| **Background** | [1-2 sentences — what this was and why] |
| **Link to the study / recordings** | [ ] |
| **Key insights** | [1-3 patterns you noticed across sessions — not one quote from one person] |
| **Recommendation(s)** | [What you'd do based on what you saw] |
| **How you'll use this** | [The decision this unblocks] |
| **Related docs** | [Links] |

**If you have more than ~5-8 responses:** watch/skim all of them before writing anything down — patterns across sessions matter more than the most memorable single moment (Braun & Clarke's thematic-analysis logic, scaled down to a single pass).

## 7. When to Stop and Loop In a Researcher

Stop and message [Research partner] if:
- People are answering in ways that make you want to ask a follow-up you can't ask
- Multiple participants are confused by the *test itself*, not the thing you're testing
- The findings would change a decision bigger than the one this test was scoped for
- You're not sure whether what you saw is a real pattern or 2 people being unlucky
```

---

## CONTENT GENERATION RULES

1. **Assemble, don't re-derive.** Sections 1-4 summarize content that should already exist in the `/diy-research-plan`, `/screener`, and `/unmod-script` outputs — pull from them rather than re-deciding the fit, learning goal, audience, or questions from scratch. If one of those upstream outputs genuinely doesn't exist yet, that's a signal to run that skill first; only hand-author its content inline as a last resort, and say plainly when you've done so.
2. **Guidance lives next to every input field.** Every fill-in-the-blank row gets a plain-language sentence explaining what's wanted — never assume the requester knows research vocabulary. This is the single biggest difference from `/research-plan`'s content rules: there, the researcher is expected to know what "sample size" means. Here, they aren't, so the packet teaches it inline or avoids the term entirely.
3. **One learning goal, not several.** If the requester lists more than one core question, that's the signal to trim to DIY scope (Hall) — push back before drafting rather than building a bloated packet.
4. **Tasks describe goals, not UI.** "Find a way to add this to your list" — not "tap the plus icon." Same rule `/mod-guide` uses for moderated studies; it matters even more here because there's no moderator to notice a participant got stuck on wording rather than the design.
5. **No leading or hypothetical questions.** Apply Portigal's and Sharon's bias-elimination rules to every question in the packet — the requester can't be expected to catch this themselves, so this skill catches it for them before it ships.
6. **The wrap-up safety-net questions are non-negotiable.** Always include a "what was confusing/unexpected" and a "what would you change" question, even if the requester didn't ask for them. They catch problems the task-specific questions miss, and cost nothing to include.
7. **Escalation triggers are explicit, not implied.** Section 7 must name concrete signals ("people are confused by the test itself"), not a vague "reach out if needed." A non-researcher won't know what "needed" means without examples.
8. **Findings section stays a findings summary, not a report.** Resist the pull to expand Section 6 into the full Finding → Insight → Recommendation ladder from `/report`. If the study's results need that level of rigor, that's a sign it should route to a researcher-authored `/report` instead.
9. **Length discipline.** Target roughly a quarter of a full Research Project Plan. If a section is growing past a few lines per field, cut it back or flag that this request has outgrown DIY scope.
10. **Plain language throughout.** No unexplained acronyms, no research jargon left standing without a plain-English gloss. If a term must appear (e.g., "screener"), define it in the same sentence the first time it's used.
11. **One document.** The whole point of a packet is that it's one thing to hand off — don't split it into a suite of linked docs. Where it needs the script or screener in full detail, point to `/unmod-script` and `/screener` rather than pasting their full output inline.
12. **Comparison-format tests get a materials table, not a bigger Task block.** When the study reacts to several items or two versions rather than walking through a linear flow, don't force it into the "Task 1 / Task 2" shape — use the repeated-question-set pattern plus Section 4a's materials table, and call out the alternating order if there are two versions being compared. This is the shape a side-by-side concept or preference test needs; a step-by-step flow test doesn't need it at all.

Before calling the packet done, run it against `references/packet-checklist.md` — a short checklist of what makes a packet genuinely self-serve rather than a researcher-shaped document with the jargon lightly sanded off.

---

## Tool usage

- **AskUserQuestion** — confirm which upstream pieces already exist and the proposed packet structure (Steps 0 and 2)
- **Read** — read pasted content, PRDs, or local files the requester shares
- **Glean** (`mcp__glean_default__search` / `read_document`) — check whether this question is already answered before building anything new, if that check wasn't already done upstream in `/diy-research-plan`
- **`/diy-research-plan`** — produces the plan this packet's Sections 1-2 summarize; if it doesn't exist yet, that's the signal to run it first rather than drafting plan-level content (learning goal, audience, method) directly inside the packet
- **`/unmod-script`** (this repo's `usertesting-script` skill covers the same ground) — generates the full question-level script Section 4 points to
- **`/screener`** — generates the full participant-screening detail Section 3 points to; where no dedicated screener skill is available, hand-author the criteria directly from Section 3's bullets
- **`/research-plan`** — the escalation target whenever the fit check or Step 3's escalation triggers fire
- **`/report`** — the escalation target if the findings in Section 6 need full stakeholder-report rigor

---

## Sources & methodology

| Source | Contribution to this skill |
|--------|----------------------------|
| **Erika Hall**, *Just Enough Research* | Right-sizing scope to the decision — the core justification for a DIY packet existing at all, and for the fit-gate checklist (Section 1) that keeps it from being used where it doesn't belong |
| **Nielsen Norman Group** | Guidance on when unmoderated testing is (and isn't) appropriate — the basis for the fit-gate criteria carried into Section 1 |
| **Steve Portigal**, *Interviewing Users* / *Doorbells, Danger, and Dead Batteries* | Bias-elimination discipline, applied here to script the requester can't be expected to self-audit |
| **Tomer Sharon**, *Validating Product Ideas* | Non-leading question construction; matching method rigor to the size of the decision |
| **Nikki Anderson** | Plain-language framing of a research goal as a single sentence, adapted into the packet's "learning goal" field |
| **Virginia Braun & Victoria Clarke** | Thematic-analysis logic — scaled down to the single-pass "watch everything before writing anything down" guidance in Section 6 |
| **dscout** / **UserTesting Blog** | Self-serve and DIY unmoderated-testing best practices — informed the overall packet shape (fit check → build → run → read → escalate) |
| **AIxUXR Playbook** (Instacart-internal) | H.E.A.R.T. framework, adapted for a non-researcher audience — particularly Amplifying (AI does the bias/structuring work) and Responsible (guardrails and an explicit escalation path stay mandatory even without a researcher moderating) |
