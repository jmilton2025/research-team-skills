---
name: diy-packet
description: Use when a designer or PM needs to run their own lightweight unmoderated study without a researcher moderating it, and wants a condensed self-serve kit instead of a full research plan. Triggers on "DIY research packet", "self-serve test packet", "build me a DIY packet", "designer-led unmoderated study", or "/diy-packet".
---

# DIY Research Packet Builder

Generates a condensed, self-serve research packet for the **DIY track** — a single short document a designer or PM can pick up and run an unmoderated study from without a researcher moderating. Grounded in Erika Hall's *Just Enough Research* (right-sizing scope to the decision at hand), Nielsen Norman Group's guidance on when unmoderated testing is (and isn't) the right method, Steve Portigal and Tomer Sharon's bias-free question-design principles — translated here into scaffolding a non-researcher can follow without training — Nikki Anderson's plain-language framing of a research goal, Virginia Braun and Victoria Clarke's thematic-analysis logic (scaled down to a one-pass read), dscout and the UserTesting Blog's self-serve/DIY-testing best practices, and Instacart's internal **AIxUXR Playbook** H.E.A.R.T. framework — particularly **Amplifying** (the AI does the bias-scrubbing and structuring work a researcher would normally do live) and **Responsible** (guardrails don't disappear just because a researcher isn't moderating).

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
- A designer or PM wants to run their **own** unmoderated study (task-based usability check, first-impression test, A/B comparison of two static designs, simple concept reaction) without a researcher sitting in on sessions
- A researcher is prepping a **DIY intake** — someone submitted a lightweight request and it's been triaged as self-serve rather than researcher-led
- Someone asks for "the lightweight version" of a research plan, or says the full plan is overkill for what they need
- The deliverable needs to be handed to someone who has never run a study before and won't have a researcher walking them through it live

Trigger phrases:
- "/diy-packet"
- "build me a DIY packet"
- "give me a self-serve test packet"
- "I need something a PM can run without me"
- "make this DIY-friendly"
- "condense this into something [name] can run themselves"

Do NOT use this skill when:
- The study needs a moderator present (motivations, mental models, multi-path journeys, anything needing follow-up probing) — that's a researcher-led study; use `/research-plan` and `/mod-guide` instead
- The requester already has research training and just wants the full plan — use `/research-plan`
- The ask is to write the test questions or the participant screen on their own, outside a packet — those are the `/unmod-script`- and `/screener`-shaped outputs this skill bundles *pointers to*, not replacements for

## How this differs from `/research-plan`

`/research-plan` and `/diy-packet` cover the same underlying decision — "what should this study look like" — but for two different audiences, and the difference is deliberate, not accidental:

| | `/research-plan` (researcher-led) | `/diy-packet` (DIY / self-serve) |
|---|---|---|
| **Audience** | A trained UX researcher, who understands methodology tradeoffs and bias risk | A designer or PM with no research training, running the study alone |
| **Length** | Full ResOps-format Research Project Plan — many sections, ~8+ pages | One short document, roughly **a quarter the length** of a full plan |
| **Sections** | Background, Existing Insights, Objectives, Key Research Questions, Hypotheses, Method, full RACI, Timeline, Appendix | What you're testing, who to test with, what to ask, how to run it, how to read results — five sections, no more |
| **Language** | Research vocabulary is expected and used (objectives vs. research questions, saturation, TEDW stems) | Plain language only. No unexplained research jargon — every term is either dropped or explained inline |
| **Depth of methodology defense** | Cites saturation literature, defends sample size, documents alternatives considered | States the number and moves on — the method is already pre-decided as DIY-appropriate by the fit gate below |
| **What's missing on purpose** | Nothing — it's the deep version | Existing-insights review, hypothesis section, full RACI, methodology alternatives, timeline milestones — all cut. A DIY packet assumes someone already decided this doesn't need that depth |
| **Safety net** | Researcher's own judgment, live in the room | Built into the document: a fit-gate checklist, hardcoded bias-resistant wrap-up questions, and an explicit "stop and call a researcher" list |

If a request turns out to need the researcher-led depth mid-build — the topic touches motivations, requires follow-up probing, or the requester keeps asking "but what if they say X" — stop and say so; route to `/research-plan` instead of stretching this skill to cover it.

---

## Core workflow

### Step 0 — DIY-Fit Gate (run this first, always)

Before drafting anything, check whether the study actually belongs in the DIY track. Unmoderated, self-serve testing is a good fit for narrow, task-based, single-round questions — and a bad fit for anything needing a human to adapt in the moment (NN/g's moderated-vs-unmoderated guidance; Hall's "just enough" scoping principle: the method should match the size of the decision, not the enthusiasm of the requester).

Ask (or infer from the request, then confirm):

| Check | DIY is a good fit when… | Route to `/research-plan` + `/mod-guide` instead when… |
|---|---|---|
| **Task type** | A specific goal on a live product or static design — can they complete it, do they notice it, which of two versions is clearer | Understanding *why* someone behaves a certain way, or their mental model |
| **Path** | A single, mostly-linear flow | Multiple valid paths where the participant may need guidance to explore alternatives |
| **Follow-up** | The question can be fully answered in one round, no adaptive probing needed | You'd want to ask "tell me more" based on what they just said |
| **Stimulus** | A prototype, static design, or live surface participants can react to on their own | Nothing to show yet — this is pre-concept, exploratory work |
| **Scale question** | Qualitative signal from a handful of sessions is enough | You need statistically representative, quantitative sizing |
| **Existing answer** | Nobody's checked whether this is already answered | — always check first, regardless of method (search existing research, e.g. via Glean or the team's research-insights channel, before building anything new) |

If two or more checks land in the right-hand column, say so plainly and recommend the researcher-led path instead of building the packet. Don't build a DIY packet for a study that needs a moderator — that's the single most common way self-serve research produces misleading results.

### Step 1 — Gather Inputs

Ask for whatever the requester already has — a PRD, a Slack thread, a rough idea, or a link to what they want feedback on. Accept any format.

> "To build your DIY packet, share what you've got: a link to the design/prototype, what you're trying to learn, and who should test it. A rough paragraph is fine — I'll structure it."

Minimum inputs needed before drafting:
1. **What's being tested** — feature, screen, or flow
2. **The single learning goal** — the one thing this study needs to answer (if the requester gives you five goals, that's a signal the study is too big for DIY — push back per Hall's right-sizing principle before drafting)
3. **The prototype or design link**
4. **Who should test it** — rough audience description (used to point to `/screener`, not to build a full sampling plan here)
5. **Timeline** — when they need results

### Step 2 — Propose the Packet Structure

Show the five sections this packet will contain (see OUTPUT TEMPLATE below) and confirm before generating — same courtesy as any other plan in this repo, just against a much shorter structure:

> "Here's what I'll build — a one-page packet, not a full plan:
> 1. Is this right for DIY? (quick fit check)
> 2. What you're testing
> 3. Who to test with
> 4. What to ask
> 5. How to run it + how to read results
>
> Sound right, or is there something specific you need added?"

### Step 3 — Generate the Packet

Apply the content rules below and produce the OUTPUT TEMPLATE. Keep the whole document to roughly **a quarter the length of a full Research Project Plan** — if it's running long, that's a sign content belongs in `/research-plan` instead, not that this document needs another section.

---

## OUTPUT TEMPLATE

```
# DIY Test Packet: [Study name — plain-language, e.g. "New checkout button — is it noticeable?"]

**Owner (running this):** [Requester name]
**Research partner (loop in if stuck):** [Researcher name]
**Date:** [Month Year]

---

## 1. Is This Right for DIY?

Quick check before you build anything — self-serve unmoderated testing works well for this kind of study when:

- ☐ You're testing a specific task or reaction, not "why do people do this"
- ☐ There's a design or prototype link ready to show people
- ☐ One round of feedback is enough — you don't need to follow up based on what someone says
- ☐ You checked existing research first and this genuinely hasn't been answered

If you checked all four — you're good to go. If not, stop here and talk to [Research partner] before building the test.

## 2. What You're Testing

| Field | What to fill in | Your input |
|---|---|---|
| **Feature / area** | The specific part of the product this is about | [ ] |
| **Learning goal** | The ONE most important question — if you can't say it in one sentence, it's too many questions for one DIY test | [ ] |
| **Starting scenario** | The one-line story that puts someone in the right frame of mind before they start (e.g., "Imagine you're shopping for a weeknight dinner") | [ ] |
| **Design / prototype link** | The single link people will test | [ ] |

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

**Wrap-up (always include these — they catch anything the task-specific questions miss):**
1. [Optional: 1-3 questions comparing or summarizing the whole experience]
2. "What was the most confusing or unexpected part of this experience?" — *(fixed — always ask this one)*
3. "If you could change one thing about what you just saw, what would it be?" — *(fixed — always ask this one)*

## 5. How to Run It

1. Build your audience using the criteria from Section 3.
2. Load the test questions from Section 4 into your unmoderated testing tool, in order.
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

1. **Guidance lives next to every input field.** Every fill-in-the-blank row gets a plain-language sentence explaining what's wanted — never assume the requester knows research vocabulary. This is the single biggest difference from `/research-plan`'s content rules: there, the researcher is expected to know what "sample size" means. Here, they aren't, so the packet teaches it inline or avoids the term entirely.
2. **One learning goal, not several.** If the requester lists more than one core question, that's the signal to trim to DIY scope (Hall) — push back before drafting rather than building a bloated packet.
3. **Tasks describe goals, not UI.** "Find a way to add this to your list" — not "tap the plus icon." Same rule `/mod-guide` uses for moderated studies; it matters even more here because there's no moderator to notice a participant got stuck on wording rather than the design.
4. **No leading or hypothetical questions.** Apply Portigal's and Sharon's bias-elimination rules to every question in the packet — the requester can't be expected to catch this themselves, so this skill catches it for them before it ships.
5. **The wrap-up safety-net questions are non-negotiable.** Always include a "what was confusing/unexpected" and a "what would you change" question, even if the requester didn't ask for them. They catch problems the task-specific questions miss, and cost nothing to include.
6. **Escalation triggers are explicit, not implied.** Section 7 must name concrete signals ("people are confused by the test itself"), not a vague "reach out if needed." A non-researcher won't know what "needed" means without examples.
7. **Findings section stays a findings summary, not a report.** Resist the pull to expand Section 6 into the full Finding → Insight → Recommendation ladder from `/report`. If the study's results need that level of rigor, that's a sign it should route to a researcher-authored `/report` instead.
8. **Length discipline.** Target roughly a quarter of a full Research Project Plan. If a section is growing past a few lines per field, cut it back or flag that this request has outgrown DIY scope.
9. **Plain language throughout.** No unexplained acronyms, no research jargon left standing without a plain-English gloss. If a term must appear (e.g., "screener"), define it in the same sentence the first time it's used.
10. **One document.** The whole point of a packet is that it's one thing to hand off — don't split it into a suite of linked docs. Where it needs the script or screener in full detail, point to `/unmod-script` and `/screener` rather than pasting their full output inline.

Before calling the packet done, run it against `references/packet-checklist.md` — a short checklist of what makes a packet genuinely self-serve rather than a researcher-shaped document with the jargon lightly sanded off.

---

## Tool usage

- **AskUserQuestion** — confirm the DIY-fit gate result and the proposed structure (Steps 0 and 2)
- **Read** — read pasted content, PRDs, or local files the requester shares
- **Glean** (`mcp__glean_default__search` / `read_document`) — check whether this question is already answered before building anything new (Step 0's "existing answer" check)
- **`/unmod-script`** (this repo's `usertesting-script` skill covers the same ground) — generates the full question-level script Section 4 points to
- **`/screener`** — generates the full participant-screening detail Section 3 points to; where no dedicated screener skill is available, hand-author the criteria directly from Section 3's bullets
- **`/research-plan`** — the escalation target whenever Step 0 or Step 3's escalation triggers fire
- **`/report`** — the escalation target if the findings in Section 6 need full stakeholder-report rigor

---

## Sources & methodology

| Source | Contribution to this skill |
|--------|----------------------------|
| **Erika Hall**, *Just Enough Research* | Right-sizing scope to the decision — the core justification for a DIY packet existing at all, and for the fit gate that keeps it from being used where it doesn't belong |
| **Nielsen Norman Group** | Guidance on when unmoderated testing is (and isn't) appropriate — the basis for the Step 0 fit-gate criteria |
| **Steve Portigal**, *Interviewing Users* / *Doorbells, Danger, and Dead Batteries* | Bias-elimination discipline, applied here to script the requester can't be expected to self-audit |
| **Tomer Sharon**, *Validating Product Ideas* | Non-leading question construction; matching method rigor to the size of the decision |
| **Nikki Anderson** | Plain-language framing of a research goal as a single sentence, adapted into the packet's "learning goal" field |
| **Virginia Braun & Victoria Clarke** | Thematic-analysis logic — scaled down to the single-pass "watch everything before writing anything down" guidance in Section 6 |
| **dscout** / **UserTesting Blog** | Self-serve and DIY unmoderated-testing best practices — informed the overall packet shape (fit check → build → run → read → escalate) |
| **AIxUXR Playbook** (Instacart-internal) | H.E.A.R.T. framework, adapted for a non-researcher audience — particularly Amplifying (AI does the bias/structuring work) and Responsible (guardrails and an explicit escalation path stay mandatory even without a researcher moderating) |
