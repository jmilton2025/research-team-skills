# Interview / IDI Guide — Template Reference

Load this when the researcher picks **Interview (IDI-style)** as the guide format (Step 2a / Section 1 > Step 1). It holds the type-specific pieces: the Section 1 parameters, the Section 2 block sequence, the full OUTPUT TEMPLATE, and interview-specific content rules. The **truly-shared spine** — parameter table, Pre-Session Checklist, Consent + Recording script, Post-Session Debrief — is assembled from SKILL.md's shared-scaffolding section, identical for both guide types, so it is not repeated here. Two things are **format-styled, not shared**: (1) the **document header** — the interview format uses its own two-tier title (all-caps study kicker + doc-type title + italic period, per the OUTPUT TEMPLATE below) and a RACI block, rather than the prototype's `UX Research | … | Round N` breadcrumb + Study-Title H1; and (2) the **Participants Log**, which is interview-specific.

Derived from the finished *AI Expert Interviews — Discussion Guide (Q1 May 2024)* (blinded external-expert IDIs via GLG) plus the skill's existing IDI conventions. This type also covers **diary check-ins** and **focus groups** (conversation-driven, no artifact-under-test); see `mod-guide-methodology.md` §3 for those sub-shapes.

---

## When this type applies

An interview guide is the right shape when there is **no artifact to test** — just topics or themes to discuss. Signals in the inputs:

- No prototype / mockup / screens of any kind.
- Goals phrased as "understand why / how they feel / their experience / their mental model / their vision" rather than task completion.
- Participants recruited to *talk about a domain* — often external experts (e.g. via GLG or an expert network), sometimes in blinded sessions.
- Future-looking, landscape/opinion-oriented studies (1/3/5-year outlook, "most promising applications").
- Coverage should **adapt to each participant's background** — run different themes for different people — with no success criteria.

Tie-breaker: if there is a testable artifact AND a "can they do X" question → build the prototype guide instead.

---

## Section 1 — Interview-specific parameters

Ask these **in addition to** the shared Section 1 rows (study title, moderation style, duration, participants, profile, **Row 7 topics/themes**, **Row 8 Say-Do**, stakeholders/RACI, Drive destination & delivery). Standard row conventions apply (Recommended first, real alternatives, editable Other, "Brainstorm with me" last, `Section 1 > Step N of M` labels). A row tagged **(= Row N)** is the shared row realized for this format — asked **once** in the main Section 1 batch, not a second time here.

| # | Question | Select | Recommended | Alternatives |
|---|----------|--------|-------------|--------------|
| I1 | **Recruit source** | single | Extracted source (internal panel / expert network like GLG / customer list) | The plausible alternatives |
| I2 | **Blinded session?** — is Instacart's identity withheld | single | No (disclosed) | "Yes — blinded; add the blinded-session note + screen-out script" |
| I3 **(= Row 7)** | **Thematic blocks** — the deep-dive topics to cover (this IS the shared Row 7, realized as themes — don't ask twice) | **multi** | The 2–4 extracted themes, all pre-selected, each droppable | "Add a theme" |
| I4 | **Conditional blocks** — themes that run only for some participants | **multi** | Any theme flagged "if applicable based on background" | "All blocks run for everyone" |
| I5 **(= Row 8)** | **Say-Do Gap module** — the shared Row 8, don't ask twice | single | Include / Skip / Let Claude decide — per Step 2c risk flag | The other two |
| I6 | **Horizon framing** — for future/vision studies | single | 1 / 3 / 5-year outlook | "No horizon framing" |

*(Truly interview-specific asks = I1, I2, I4, I6. I3 is the shared Row 7; I5 is the shared Row 8.)* Mark unknown stakeholders/recruit sources `[TBD — fill in]` rather than inventing them.

---

## Section 2 — Interview content blocks (draft-first, one at a time)

Walk these blocks in order, draft → approved → locked, labeled `Section 2 > Step N of M`.

**Pop-up usage rule:** Pop-ups (`AskUserQuestion`) are used **only** for the guide-format question (prototype vs. interview — Section 1 Step 1). Do **not** use pop-ups for Introduction, Background Questions, or Wrap-Up — these sections have fixed, template-driven content and are drafted directly, not gate-kept with pop-ups.

1. **Objectives** — plain goal bullets (understand / envision / identify), horizon-framed where relevant. **No hypotheses, no P0 labels** (that's the prototype style).
2. **Introduction & Rapport** *(verbatim — confirm, don't re-draft)* — condensed 3-bullet welcome (recording/privacy · session overview · logistics/prototype caveat), screen-out script. No pop-up.
3. **Background Questions** *(verbatim — confirm, don't re-draft)* — 4–6 topic-adjacent icebreaker questions. Use the grocery/in-store standard block for store-based studies. No pop-up.
4. **Thematic deep-dive blocks** — **one block per theme** from the approved I3 list. Open how/why/what questions as nested prose bullets (main question → indented probes). Flag conditional blocks in the heading ("(15 min — if applicable based on background)").
5. **Wrap-Up** *(verbatim — confirm, don't re-draft)* — standard 3-line close (open catch-all · questions for me · thank-you + incentive). No pop-up.
6. **Parking Lot** *(optional)* — emergent topics for later rounds, grouped.

The truly-shared spine (parameter table, Pre-Session Checklist, Consent script, Post-Session Debrief) is assembled around these per SKILL.md; the two-tier interview header/RACI block and the interview-specific **Participants Log** are defined in this template.

---

## OUTPUT TEMPLATE — Interview / IDI

> **Core principle:** the body is **open questions as nested prose bullets** — main question, then indented probes — **not tables**. Tables appear only in the shared scaffolding (parameter table, consent script) and the participants log. Target length **~4–5 pages.**

```
[AI EXPERT INTERVIEWS]        ← small all-caps kicker (the study)

# Discussion Guide             ← large doc-type title

*[Q1 · Month Year]*            ← study period, italic

- **Responsible:** [Name] (Role)
- **Accountable:** [Name] (Role)
- **Consulted:** [internal team]
- **Contributor:** [named contributors — keep as its own line when the study has a distinct contributor role; otherwise fold into Consulted]
- **External:** [partner network — e.g. GLG]
- **Informed:** [stakeholders]
- **Session Summaries:** [master-doc link]

---

| Parameter | Detail |
|-----------|--------|
| **Study Type** | 1:1 in-depth interview (IDI)[, blinded] |
| **Duration** | [X] minutes — [rapport / deep-dive / wrap split in minutes] |
| **Format** | Moderated remote, [tool] |
| **Recruit** | [source — e.g. GLG expert network], N=[N] |
| **Goal** | [1–2 sentence research goal] |

---

## Research Objectives

- [Understand current + future applications across the journey]
- [Inspire a 5-year vision]
- [Spot untapped opportunities]
- [Identify players/disruptors to monitor]

*(Plain goal bullets — no hypotheses, no P0 labels, no priority tiers.)*

---

## Pre-Session Checklist

[Shared scaffolding — bullets with ☐:]
- ☐ Participant validated — [screening criterion; expertise verified]
- ☐ Recording armed · consent script ready · observers cameras-off
- ☐ [Blinded-session materials ready, if applicable]

---

## Consent + Recording Script — READ VERBATIM (~60 sec)

[Shared scaffolding 2-col table, Cue | Read aloud. Consent/recording is always spelled out even though the source example left it implicit.]

| Cue | Read aloud |
|-----|------------|
| **Open** | "Hi [name], thanks for making the time. I'm [moderator], a researcher [framing — incl. blinded note if applicable]." |
| **Purpose** | "I want to learn from your experience with [domain] — there are no right or wrong answers." |
| **Recording** | "With your permission I'd like to record for internal research only. **Is that okay?**" |
| **Confidentiality** | "Your name and identifying details are removed before anything is shared internally." |
| **Open floor** | "Any questions before we start?" |

> Wait for an explicit verbal **"yes"** before recording.

---

## Introduction & Rapport Building (~[X] min)

**Goal:** Build rapport, set expectations, and screen out gracefully if needed.

> "Hi [name]! I'm [moderator name], [role framing — e.g. an independent researcher partnering with Instacart]. There are no right or wrong answers — we just want your honest opinion."

- **Recording & privacy:** I'll be recording and taking notes throughout. Everything stays internal to this study — your feedback will be shared anonymously.
- **What we'll do:**
  - *Interview guide:* "We're going to spend about [X] minutes talking about your [domain — e.g. grocery shopping] experience. I just want to hear what it's really like for you."
  - *Prototype guide:* "We're going to spend about [X] minutes looking at some [concepts / ideas / screens] and hearing what you think about them. As you go through each one, think out loud — share what you notice, like, or don't like."
- **[Prototype only — logistics note]:** "Some of what you'll see are early prototypes, so not everything will be tappable the way it would be on the real [product/device]. [Any required items — e.g. 'Also confirming — did you bring [cash/EBT] for today?']"

> Any questions before we start?

> **Screen-out (if they don't fit the profile):** "Thank you — it sounds like your background is a bit different from what we're exploring today, so I don't want to take more of your time. We'll still process your incentive. [End session.]"

---

## Background Questions (~[X] min)

**Goal:** Warm up the participant and establish relevant context before the core tasks/themes.

*(Icebreaker questions — keep general but topic-adjacent. Adapt to the study domain.)*

- [Who is typically involved in [the relevant behavior — e.g. grocery shopping, decision-making] in your household?]
- [How often do you [relevant behavior]? Is it usually [mode A] or [mode B]? Why do you tend to choose one over the other?]
- [Tell me about the last time you [relevant behavior] — walk me through what that was like.]
- [Are you familiar with [the product/concept under study]? Have you used it before?]
  - *[If yes]* Where / when? How did it go?
- [Any contextual grounding question specific to the study location or setup.]

**Grocery/in-store shopping studies — standard background block:**
- Who takes care of the grocery shopping for your household?
- How often do you shop for groceries — and is it mostly in-store or online? Why do you tend to choose one over the other?
  - What type of cart do you typically use when shopping in-store? Why?
- Tell me about your last grocery trip — where did you go and how did it go?
- How often do you shop at this store?

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

- Thinking back to everything we've discussed, is there anything you didn't get a chance to share that you'd like to?
- Do you have any questions for me?
- Thank you again for your time today! [Incentive delivery note if applicable.]

---

## Post-Session Debrief

[Shared scaffolding — numbered list, within 5 min of end:]
1. **Top 3 themes heard**
2. **Most surprising / disconfirming point**
3. **Most diagnostic verbatim quote:** one sentence, exact words

---

## Participants Log

*(Research-ops artifact — one row per scheduled participant.)*

| Date & Time | Panelist Bio | Recording |
|-------------|--------------|-----------|
| [schedule] | [sourced bio] | [Dovetail "Listen here" · Doc "Read summary"] |

---

## Parking Lot — Future Questions *(optional)*

Emergent topics not yet covered, grouped for later rounds:
- **[Group A]:** …
- **[Group B]:** …
```

**IMPORTANT:** the guide ends at the Parking Lot (or Participants Log if no parking lot). No Master Probe Bank, Bias Checklist, or Self-Critique inside the doc.

---

## Interview-specific content-generation rules

1. **Body = open questions as nested prose bullets** (main → indented probes). No task tables in the body.
2. **No leading, hypothetical-about-future-behavior, closed yes/no, or compound questions** (see the shared CONTENT GENERATION RULES + methodology §2, §4).
3. **Funnel each theme:** broad grand-tour question → specific-incident probes → closed clarifiers.
4. **Objectives are plain goals** — no hypotheses, no P0 labels (unlike prototype guides).
5. **Conditional coverage:** flag themes that run only for some participants in the heading; the moderator runs the blocks that fit each person. Time budget can be non-additive.
6. **Screen-out script** is included whenever recruiting risk exists (expert networks especially).
7. **Say-Do Gap module** applies here when the study asks about stated behavior/preferences — ground in artifacts, use critical-incident phrasing, counter social desirability (methodology §2). **When the module is Included (Section 1, Row 8), each affected theme block's draft must carry a visible `**Say-Do Gap Probe:**` prose line** directly under the block's goal, naming which §2b techniques apply to that block's questions (grounding in an artifact §2b.2, diary/photo pre-work §2b.3, probing a stated/observed gap non-accusatorially §2b.4, and the §2c social-desirability counter-moves). This line is what makes Include vs. Skip visibly different in the delivered guide — without it, both settings produce an identical document.
8. **Horizon framing** (1/3/5-year) for future/vision studies, scoped consistently to the domain.

---

## House-style notes (interview guides)

- Two-tier title: small all-caps kicker (the study) above the large doc-type title ("Discussion Guide"), study period in italics.
- RACI stakeholder block with hyperlinked names at the top; a Participants log (Date/Bio/Recording, with Dovetail "Listen here" + "Read summary" links) at the bottom.
- Timing annotated in every section heading, summing to session length (budget may be non-additive when conditional blocks only fire for some participants).
- Verbatim read-aloud scripts are quoted/italic and visually distinct from un-quoted question prompts.
