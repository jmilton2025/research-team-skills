# Interview / IDI Guide — Template Reference

Load this when the researcher picks **Interview (IDI-style)** as the guide format (Step 2a / Section 1 > Step 1). It holds the type-specific pieces: the Section 1 parameters, the Section 2 block sequence, the full OUTPUT TEMPLATE, and interview-specific content rules. The shared spine — `# Moderation Guide`, `## [Study Title]`, ownership/RACI, parameter table, Pre-Session Checklist, and Post-Session Debrief — comes from SKILL.md. Interview consent is rendered once, as the table in this template.

The template is informed by completed internal IDI studies; source-study identifiers are intentionally omitted from this public package. It also covers **diary check-ins** and **focus groups** (conversation-driven, no artifact under test); load `mod-guide-methodology.md` §3 automatically for those subtypes.

---

## When this type applies

An interview guide is the right shape when there is **no artifact to test** — just topics or themes to discuss. Signals in the inputs:

- No prototype / mockup / screens of any kind.
- Goals phrased as "understand why / how they feel / their experience / their mental model / their vision" rather than task completion.
- Participants recruited to *talk about a domain* — often external experts (e.g. via GLG or an expert network), sometimes in blinded sessions.
- Future-looking, landscape/opinion-oriented studies (1/3/5-year outlook, "most promising applications").
- Coverage should **adapt to each participant's background** — run different themes for different people — with no success criteria.

Tie-breaker: if there is a testable artifact AND a "can they do X" question → build the prototype guide instead.

> **⚠️ Source-plan mismatch guardrail (2026-10-02):** if the source plan's Method & approach / Stimuli & protocol define artifact-based tasks (prototype sessions, order comparisons, think-aloud tasks) but the researcher asks for an interview guide anyway, the plan's hypotheses cannot be answered by a talk-only guide. Flag it and pick one path with the researcher (per SKILL.md Step 2a): build the prototype guide the plan specifies, or reframe as a **separate pre-prototype discovery round** — its own goal and dates in the parameter table (never the plan's session dates), and an interpretation limit stating that testing the module itself needs the plan's prototype sessions.

---

## Section 1 — Interview-specific parameters

Ask these **in addition to** the shared Section 1 rows (study title, moderation style, duration, participants, profile, **Row 7 topics/themes**, **Row 8 Say-Do**, stakeholders/RACI, Drive destination & delivery). Standard row conventions apply (Recommended first, real alternatives, editable Other, "Brainstorm with me" last, `Section 1 > Step N of M` labels). A row tagged **(= Row N)** is the shared row realized for this format — asked **once** in the main Section 1 batch, not a second time here.

| # | Question | Select | Recommended | Alternatives |
|---|----------|--------|-------------|--------------|
| I1 | **Recruit source** | single | Extracted source (internal panel / expert network like GLG / customer list) | The plausible alternatives |
| I2 | **Blinded session?** — is Instacart's identity withheld | single | Exact source-approved blinded/disclosed status; `[TBD — fill in]` when absent | The other status, only as a proposed plan change |
| I3 **(= Row 7)** | **Thematic blocks** — the deep-dive topics to cover (this IS the shared Row 7, realized as themes — don't ask twice) | multi only for 2–3 independent themes; otherwise single confirm/revise | The complete extracted theme set | Remove/reorder · Add/reframe |
| I4 | **Conditional blocks** — themes that run only for some participants | multi for 2–3 independent blocks; otherwise single confirm/revise | The complete conditional-block set | Run all blocks · Revise conditions |
| I5 **(= Row 8)** | **Say-Do Gap module** — the shared Row 8, don't ask twice | single | Include / Skip / Let Claude decide — per Step 2c risk flag | The other two |
| I6 | **Horizon framing** — for future/vision studies | single | The one source-supported horizon | One alternate horizon · No horizon framing |

*(Truly interview-specific asks = I1, I2, I4, I6. I3 is the shared Row 7; I5 is the shared Row 8.)* Mark unknown stakeholders/recruit sources `[TBD — fill in]` rather than inventing them. For Responsible and Accountable, verify the person's name and role independently; never infer a role from a supplied name.

---

## Section 2 — Interview content blocks (draft-first, one at a time)

Walk these blocks in order, draft → approved → locked, labeled `Section 2 > Step N of M`.

**Pop-up usage rule:** Section 1 still uses the complete parameter flow in SKILL.md. In Section 2, use approval pop-ups only for the thematic deep-dive blocks. Objectives, Introduction, Background Questions, Wrap-Up, and the shared scaffolding are template-driven and shown as context, not separately gate-kept.

1. **Objectives** — a required delivered section of plain, source-grounded goal bullets (understand / envision / identify), horizon-framed where relevant. **No hypotheses, no priority labels** (that's the prototype style — and even it uses "Priority-1/-2", never "P0/P1"). It is not a pop-up, but it must not be omitted.
2. **Introduction & Rapport** *(verbatim — confirm, don't re-draft)* — condensed welcome, session overview, participant control, and transition from the already-completed consent table; no duplicate recording/privacy promise. No pop-up.
3. **Background Questions** *(verbatim — confirm, don't re-draft)* — 4–6 topic-adjacent icebreaker questions. Use the grocery/in-store standard block for store-based studies. No pop-up.
4. **Thematic deep-dive blocks** — **one block per theme** from the approved I3 list. Open how/why/what questions as nested prose bullets (main question → indented probes). Flag conditional blocks in the heading ("(15 min — if applicable based on background)").
5. **Wrap-Up** *(verbatim — confirm, don't re-draft)* — standard three-question close plus a thank-you (neutral theme playback · open catch-all · questions for me · thank-you; add incentive language only when approved). No pop-up.
6. **Parking Lot** *(optional)* — emergent topics for later rounds, grouped.

The shared spine is assembled around these per SKILL.md. Participant schedules, biographies, recording links, and session-summary links belong in a separately permissioned ResOps artifact; never place them in the broadly shared moderation guide.

**Subtype realization is required, not a label swap:**

- **Moderated 1:1 IDI:** use the standard Background → thematic deep-dives → Wrap-Up sequence.
- **Moderated diary-study check-in:** use an approved session consent/recording check, brief reconnect, review only the approved minimum-necessary diary entries, and source-approved next-phase prompts. Never request new diary/photo uploads unless the collection protocol below is approved.
- **Moderated focus group:** add approved group ground rules/privacy limits, introductions, divergent discussion with turn-taking, and a convergent activity only when the source objective requires it. Do not promise participant-to-participant confidentiality.

Diary/photo pre-work and participant artifact collection are off unless the approved plan and protocol explicitly define the collection, participant permission/consent, transfer channel, audience/access, and retention/deletion.

---

## OUTPUT TEMPLATE — Interview / IDI

> **Core principle:** the body is **open questions as nested prose bullets** — main question, then indented probes — **not tables**. Tables appear only in the shared scaffolding (parameter table and consent script). Target length **~4–5 pages.**

**Study-period rule:** Never substitute the current date or month for an unknown study period.

```
# Moderation Guide

## [Study Title]

*[Source-approved study period or TBD — fill in]*

- **Responsible:** [TBD — fill in] ([TBD — fill in])
- **Accountable:** [TBD — fill in] ([TBD — fill in])
- **Consulted:** [TBD — fill in]
- **Informed:** [TBD — fill in]

---

| Parameter | Detail |
|-----------|--------|
| **Study Type** | [Moderated 1:1 IDI / moderated diary-study check-in / moderated focus group][, blinded] |
| **Duration** | [X] minutes — [consent / post-consent introduction / background / deep-dive / wrap split in minutes] |
| **Format** | Moderated [remote / in-person], [approved tool or location] |
| **Recruit** | [approved source], N=[N] |
| **Goal** | [1–2 sentence research goal] |

---

## Research Objectives

- [Source objective 1, restated without changing scope]
- [Source objective 2, if supplied]
- [Source objective 3, if supplied]

*(Plain goal bullets — no hypotheses, no P0 labels, no priority tiers.)*

---

## Pre-Session Checklist

[Shared scaffolding — bullets with ☐:]
- ☐ Participant validated — [screening criterion; expertise verified]
- ☐ [Approved recording/observation setup confirmed; omit when neither is planned]
- ☐ [Blinded-session materials ready, if applicable]

---

## Consent Script — READ VERBATIM (~1 min; separate timed heading)

[Shared scaffolding 2-col table, Cue | Read aloud. Use only approved protocol language. Omit the Recording/observation row when neither is planned.]

| Cue | Read aloud |
|-----|------------|
| **Open** | "Hi [name], thanks for making the time. I'm [moderator], a researcher [framing — incl. blinded note if applicable]." |
| **Purpose** | "I want to learn from your experience with [domain] — there are no right or wrong answers." |
| **Recording / observation — include only when planned** | "With your permission, I'd like to [approved recording modalities], and [approved observer disclosure, if applicable]. **Is that okay?**" |
| **Privacy** | "[State only the approved access, use, clip-sharing, retention, and deletion language. If it is not confirmed, use `[TBD — confirm ResOps standard language]`; never promise anonymity or internal-only use by default.]" |
| **Open floor** | "Any questions before we start?" |

> When recording or observing, wait for the protocol's required explicit consent before beginning.

---

## Introduction & Rapport Building (~[X] min, excluding Consent)

**Goal:** Build rapport, set expectations, and screen out gracefully if needed.

> "Hi [name]! I'm [moderator name], [approved role framing]. There are no right or wrong answers — I want to understand your experience in your own words."

- **Consent transition:** "Thanks for confirming."
- **What we'll do:** "We're going to spend about [X] minutes talking about your [domain] experience. I want to hear what it was really like for you."
- **Control:** "You can skip any question or stop at any time. [Approved incentive language only if confirmed.]"

> Any questions before we start?

> **Screen-out (if they don't fit the profile):** "Thank you — it sounds like your background is a bit different from what we're exploring today, so I don't want to take more of your time. [Use only the approved screen-out and incentive language from the plan/ResOps. End session.]"

---

## Background Questions (~[X] min)

**Goal:** Warm up the participant and establish relevant context before the core tasks/themes.

*(Icebreaker questions — keep general but topic-adjacent. Adapt to the study domain.)*

- [What is the most recent time, if any, that you [relevant behavior]?]
  - *[If they name an incident]* Walk me through what happened.
  - *[If none]* What is the closest relevant experience you have had?
- *[After an incident is confirmed]* Who, if anyone, was involved that time?
- *[After an incident is confirmed]* What led you to handle it that way?
- [What experience, if any, have you had with [product/concept]?]
  - *[If they name an experience]* Where / when? How did it go?
- [Any contextual grounding question specific to the study location or setup.]

**Grocery/in-store shopping studies — standard background block:**
- What is the most recent time, if any, that you got groceries?
  - *If they name a trip:* Walk me through what happened.
  - *If none:* What is the closest relevant shopping experience you have had?
- *After a trip is confirmed:* Who, if anyone, was involved that time?
  - What role did you play?
- *After a trip is confirmed:* What led you to shop that way (for example, in-store or online) on that occasion?
- What, if anything, did you use to carry or organize items? How did that work for you?
- Tell me about your most recent experience with this store, if you have one.

---

## [Theme 1 — e.g. Current Landscape] (~[X] min)

**Probes to use:** Echo · Tell-Me-More · Laddering ("why was that important?") · Silence · Contrast

- "[Open how/why/what question scoped to the domain.]"
  - *Probe:* "[indented follow-up]"
  - *Probe:* "[indented follow-up]"
- "[Second open question.]"
  - *Probe:* "[follow-up]"

## [Theme 2 — …] (~[X] min — if applicable based on background)

- "[Open question.]"
  - *Probe:* "…"

[Repeat per theme. Conditional themes carry the "if applicable" flag in the heading.]

---

## Wrap-Up (~[X] min)

*(Standard close — no pop-up needed for this section.)*

- **Reflection — play back the themes:** "I heard [brief, neutral summary]. What, if anything, would you change or add?"
- Thinking back to everything we've discussed, is there anything you didn't get a chance to share that you'd like to?
- What questions do you have for me?
- Thank you again for your time today! [Incentive delivery note only if the plan/ResOps confirms it.]

---

## Post-Session Debrief

[Shared scaffolding — numbered list, within 5 min of end:]
1. **Top 3 themes heard**
2. **Most surprising / disconfirming point**
3. **Most diagnostic verbatim quote:** one sentence, exact words

---

## Parking Lot — Future Questions *(optional)*

Emergent topics not yet covered, grouped for later rounds:
- **[Group A]:** …
- **[Group B]:** …
```

**IMPORTANT:** the guide ends at the optional Parking Lot, or at Post-Session Debrief when no Parking Lot is needed. Keep participant schedules, biographies, recording links, and session-summary links in a separately permissioned ResOps artifact. No Master Probe Bank, Bias Checklist, or Self-Critique inside the guide.

---

## Interview-specific content-generation rules

1. **Body = open questions as nested prose bullets** (main → indented probes). No task tables in the body.
2. **No leading, hypothetical-about-future-behavior, or compound questions.** Generative research questions are open-ended. Closed forms are limited to exact approved consent confirmation, eligibility screening, one-fact clarifiers after an open response, and an approved rating scale; they never elicit the participant's opinion or reasons.
3. **Funnel each theme:** broad grand-tour question → specific-incident probes → optional factual clarifier.
4. **Objectives are plain goals** — no hypotheses, no P0 labels (unlike prototype guides).
5. **Conditional coverage:** flag themes that run only for some participants in the heading; the moderator runs the blocks that fit each person. Time budget can be non-additive.
6. **Screen-out script** is included whenever recruiting risk exists (expert networks especially).
7. **Say-Do Gap module** applies here when the study asks about stated behavior/preferences — ground in artifacts, use critical-incident phrasing, counter social desirability (methodology §2). **When the module is Included (Section 1, Row 8), each affected theme block's draft must carry a visible `**Say-Do Gap Probe:**` prose line** directly under the block's goal, naming which §2b techniques apply to that block's questions (grounding in an artifact §2b.2, diary/photo pre-work §2b.3, probing a stated/observed gap non-accusatorially §2b.4, and the §2c social-desirability counter-moves). This line is what makes Include vs. Skip visibly different in the delivered guide — without it, both settings produce an identical document.
8. **Horizon framing** (1/3/5-year) for future/vision studies, scoped consistently to the domain.
9. **Baseline safety scan always runs:** remove unsupported privacy/recording/incentive claims, future-behavior hypotheticals, presuppositions, and questions that imply the answer. Before claiming a phrasing pass, build an audit-only inventory of every participant-facing research question and probe, including conditional and fallback lines. Mark every item for closed yes/no and compound framing; classify any closed item as approved consent, eligibility screening, a one-fact clarifier after an open response, or an approved rating scale, and rewrite every other failure. Report the checked-item count in the audit summary and keep the inventory outside the guide. Reframe future-looking research as expert judgment about drivers, constraints, or plausible scenarios — not the participant's predicted personal behavior. Verify the required Research Objectives section is physically present before claiming objective coverage.
10. **Collection boundary:** Diary/photo pre-work and participant artifact collection are off unless the approved plan and protocol explicitly define the collection, participant permission/consent, transfer channel, audience/access, and retention/deletion. Describing an artifact is not permission to upload, display, copy, or retain it.

---

## House-style notes (interview guides)

- Title: `# Moderation Guide`, then `## [Study Title]`, then study period in italics.
- RACI stakeholder block at the top. Participant operations live in a separate restricted artifact.
- Every timed heading, including Consent, sums to the approved session length. Render Consent as its own 1-minute row/heading and render Introduction as the remaining post-consent minutes only. For a 3-minute opening allocation, write `Consent 1 + Introduction 2`, never `Consent 1 + Introduction 3`. The theme budget may be non-additive only when conditional blocks cannot all fire for one participant.
- Verbatim read-aloud scripts are quoted/italic and visually distinct from un-quoted question prompts.
