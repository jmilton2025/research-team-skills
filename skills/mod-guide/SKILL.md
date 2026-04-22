---
name: mod-guide
description: Use when a UX researcher is about to conduct user interviews, usability tests, or diary study check-ins and needs a moderation guide with warm-up, discussion sections, probing techniques, and closing. Triggers on "write a moderation guide", "interview guide", "discussion guide", "facilitation script", or "/mod-guide".
---

# Moderation Guide Builder

Generate a ready-to-facilitate moderation guide for an Instacart UX research session — in-depth interview (IDI), usability test with think-aloud, concept test, focus group, or diary study check-in. Grounded in Steve Portigal's *Interviewing Users* (2nd ed.), Indi Young's *Listening Deeply*, Nielsen Norman Group (Rosala, Pernice, Moran, Fessenden), Erika Hall's *Just Enough Research*, Nikki Anderson's *User Research Academy*, and Instacart's internal **AIxUXR Playbook** (Loosbrock & Venkatraman, 2025) — specifically the *Discussion Guide Drafter & Critic* spoke.

### Guiding Philosophy — H.E.A.R.T. (from Instacart's AIxUXR Playbook)

Every guide this skill produces — and every session it supports — must uphold the **H.E.A.R.T.** framework. The moderator is the final authority; this skill is a co-pilot, not the driver.

| Principle | What It Means for a Moderation Guide |
|-----------|--------------------------------------|
| **H — Human-centered** | Prioritize the participant's context, comfort, and dignity. Questions serve their lived experience, not our curiosity. |
| **E — Experience-focused** | Every interaction in the session (consent, warm-up, probes, close) must feel intuitive, respectful, and positive. A clunky moderator moment is bad research. |
| **A — Amplifying** | AI drafts the protocol; the human researcher drives strategy, synthesis, and empathy. The guide is a starting point, not a script cage. |
| **R — Responsible** | Proactive about ethics, PII, consent, and bias mitigation — not a box-check. Scrub PRDs/RPPs of PII before pasting. |
| **T — Transparent** | Disclose AI-assisted drafting to stakeholders. Disclose recording and purpose to participants. Trust is the currency. |

**Source:** AIxUXR Playbook §1.2 "The H.E.A.R.T. of AI in Research" (Instacart internal, Pilot, Sep 30, 2025).

---

## Step 1 — Gather Study Inputs

Ask the researcher to paste or share the study inputs. Say:

> "To build your moderation guide, share whatever you have — PRD, project brief, kickoff Slack thread, meeting notes, or a plain-English description. I'll extract the study parameters and recommend a structure. If you have a Google Doc link, paste it."

**Accept any format:** PRD, brief, Slack thread, Gemini meeting notes, or verbal description. If a Google Doc URL is shared, read it via `google-docs:fetch-google-doc` or Glean (`mcp__glean_default__read_document`).

---

## Step 2 — Analyze and Propose Structure

Analyze the inputs, then present recommended study parameters as a table. Extract directly from the source material — do not invent details.

### 2a. Interview Type Selector (determines template branch)

Choose the guide template based on study type. Each branches the output:

| Study Type | When to Use | Core Section Style | Time Split (warm-up / body / close) |
|-----------|-------------|--------------------|--------------------------------------|
| **In-Depth Interview (IDI)** | Understanding motivations, mental models, lived experience | Open-ended discussion, narrative probes, journey mapping | 10% / 80% / 10% |
| **Usability Test (think-aloud)** | Evaluating a design, prototype, or live product | Task-based with success criteria, think-aloud protocol | 10% / 75% / 15% |
| **Concept Test** | Reacting to stimuli (ads, features, flows) | Stimulus presentation, first impressions, comparison | 15% / 70% / 15% |
| **Diary Study Check-in** | Mid/end-of-study longitudinal sync | Entry review + follow-up probes on specific diary entries | 15% / 70% / 15% |
| **Focus Group** | Reactions to concepts in a social context | Turn-taking facilitation, divergent + convergent discussion | 15% / 70% / 15% |

Rationale: time splits follow NN/g's qualitative usability testing study guide and Rosala's interview-guide conventions.

### 2b. Present recommendations

```
Based on your inputs, here's what I recommend:

| Parameter | Recommendation | Why |
|-----------|---------------|-----|
| Study Type | [IDI / Usability / Concept / Diary / Focus] | [1-line rationale from inputs] |
| Moderated vs Unmoderated | Moderated | [rationale — depth, probing, observation] |
| Duration | [30/45/60/90 min] | [based on scope + study type] |
| Participant Profile | [e.g., "Instacart shoppers 25-45, 2+ orders/week"] | [derived from target users] |
| Key Topics / Tasks | • Topic 1  • Topic 2  • Topic 3 | [mapped to objectives] |
| Research Goal | [1-2 sentences] | — |
| Say-Do Gap Risk | [Low / Medium / High] | [see Step 2c] |
```

### 2c. Say-Do Gap Risk Check

Flag **High** if the study asks about **stated behavior, preferences, or intent** rather than observable action — e.g., "how often do you cook at home?", "would you pay for this?", "do you read ingredient labels?". When flagged High, the generated guide automatically includes the **Say-Do Gap Module** (see references/mod-guide-methodology.md).

Source: NN/g "Why User Interviews Fail" — *"Interviews do not produce reliable data about user behavior."* Indi Young's listening sessions also warn: people reconstruct rather than report.

---

## Step 3 — Researcher Reviews

Use **AskUserQuestion** to let the researcher confirm or adjust. Ask in batches of up to 4 questions. Mark Claude's recommendation "(Recommended)".

**Batch 1:**
1. **Study Type** — Claude's pick first, plus 2-3 alternatives.
2. **Moderation Style** — Moderated / Unmoderated.
3. **Duration** — 30 / 45 / 60 / 90 min.
4. **Participant Profile** — Claude's profile first, plus alternatives and Other.

**Batch 2 (if needed):**
5. **Topics / Tasks** — Accept extracted list, or edit.
6. **Say-Do Gap Module** — Include / Skip / Let Claude decide.
7. **Anything else?** — "Looks good, let's pick a style" / "Add more context" / "Change something".

---

## Step 3.5 — Style Reference (REQUIRED before generating)

After parameters are approved, ask for a style reference. Use **AskUserQuestion**:

**Question — Output Style**

> "One last thing before I generate your guide — I want to make sure the output matches your preferred style and format."

Options:
- **"I'll share a reference doc"** — "I have a previous moderation guide or template I'd like you to match."
- **"Use the default Instacart template" (Recommended)** — "Standard 2-column layout with section bars, RACI header, structured tables."
- **"Just give me a clean outline"** — "Simple headers and bullets, no tables or heavy formatting."

**If the researcher shares a reference doc:**

1. **Accept any format:** Google Doc URL, pasted text, uploaded file, or screenshot.
2. **If Google Doc URL:** Read via `google-docs:fetch-google-doc`, Glean, or `read-gdoc.py`.
3. **Analyze style patterns:**
   - Document structure (headers, tables, bullets, numbered lists, blockquotes)
   - Header hierarchy (H1/H2/H3 — section bars? numbered?)
   - Content layout (2-column tables, multi-column, bullets, prose)
   - Question format (numbered list, table rows, bold Q + indented probes)
   - Moderator notes (inline italics, callouts, blockquotes, labeled rows)
   - Level of detail (full verbatim scripts vs. concise bullets)
   - Tone (formal/academic, conversational, mixed)
4. **Confirm read-back:**

   > "Here's what I picked up from your reference doc:
   > - **Structure:** [e.g., Numbered sections with bullet sub-points]
   > - **Questions:** [e.g., Bold numbered questions with indented probe bullets]
   > - **Notes:** [e.g., Italic callout paragraphs between sections]
   > - **Tone:** [e.g., Conversational, direct]
   > - **Detail level:** [e.g., Full verbatim scripts for intro/close, concise bullets for probes]
   >
   > Does that capture your style? Anything you'd like me to adjust?"
5. **Generate matching their style** — content quality (questions, probes, notes) stays the same; only format adapts.

**If default template:** Use the OUTPUT TEMPLATE below.
**If clean outline:** Simple markdown — H2 headers, bullet lists, numbered questions, blockquote moderator notes. No tables.

---

## Step 4 — Generate the Moderation Guide

Apply the researcher's approved parameters and style. For the default template, follow the OUTPUT TEMPLATE below. Branch the Core section by study type (see 2a).

### OUTPUT TEMPLATE (default Instacart style)

```
*UX Research | Moderation Guide | [Quarter Year]*

# [Study Title — derived from research goal]

Last updated: [Month Year]

- **Responsible:** [Researcher name] (UX Researcher)
- **Consulted:** [Names with roles]
- **Informed:** [Names with roles]

| Parameter | Detail |
|-----------|--------|
| **Study Type** | [final] |
| **Moderation** | [Moderated / Unmoderated] |
| **Duration** | [final] |
| **Participants** | [final] |
| **Research Goal** | [final] |

---

## Study Overview

| Label | Detail |
|-------|--------|
| **Objective** | [1-2 sentence research objective] |
| **Key Questions** | 1. [Q1]<br><br>2. [Q2]<br><br>3. [Q3] |
| **Success Metrics** | [What "good data" looks like] |
| **Sessions** | [5-8 usability / 8-12 IDI / 4-6 focus groups] |

## Session Logistics

| Label | Detail |
|-------|--------|
| **Duration** | [final] |
| **Format** | [Moderated Remote / In-Person / Unmoderated] |
| **Tools** | [UserZoom / Dovetail / Zoom / Figma prototype] |
| **Recording** | Audio + video + screen share (with consent) |
| **Observers** | Max 2-3 silent observers; structured note template |

## Consent + Recording Script (~60 seconds — READ VERBATIM)

| Label | Detail |
|-------|--------|
| **Script** | "Hi [participant], thanks so much for joining me today. I'm [moderator], a researcher at Instacart.<br><br>Before we dive in, a few quick things:<br><br>• **Purpose.** We're here to learn from your experience — there are no right or wrong answers. I didn't design what we're looking at, so you won't hurt my feelings. I'm learning about the [product/concept], not evaluating you.<br><br>• **Recording.** With your permission, I'd like to record audio, video, and screen. The recording stays internal at Instacart and is used only for research. Is that okay?<br><br>• **Confidentiality.** Your name won't appear in any report. Anything you share is confidential.<br><br>• **Breaks.** This will take about [duration]. You can skip any question or end the session anytime.<br><br>• **Questions before we start?"** |
| **Moderator Note** | Wait for a verbal "yes" on recording before starting the recorder. If they say no, offer notes-only and continue. Pause 30-60 seconds of small talk after consent to settle rapport (NN/g: insufficient rapport-building is the #1 facilitation mistake). |

## Warm-Up (~[X] minutes)

| Label | Detail |
|-------|--------|
| **Question 1** | "[Warm-up — easy, open, non-leading — e.g., 'Tell me a little about yourself and what a typical week looks like.']"<br><br>**Purpose:** Build rapport, calibrate vocabulary |
| **Question 2** | "[Context — baseline behavior in domain]"<br><br>**Purpose:** Understand starting context without priming |
| **Question 3** | "[Bridge — pivots toward core topic]"<br><br>**Purpose:** Transition to main discussion |
| **Moderator Note** | Warm-up is rapport, not data. Aim for 80% participant talk time (NN/g). Listen actively, nod, follow naturally. Avoid the word "interview" — call it a "chat." |

## Core [Discussion / Tasks] (~[X] minutes)

[For each topic/task, generate a subsection with a 2-column table.]

### [N.1] [Topic / Task Name]

| Label | Detail |
|-------|--------|
| **Setup** | [Scenario or stimulus to read — describe the goal, not the UI. Say "find a way to…" not "click the button to…"] |
| **Questions** | **Q1:** "[Broad open-ended question — funnel top]"<br><br>• Probe (Echo): "[Participant's last phrase]?"<br><br>• Probe (Tell-me-more): "Tell me more about that."<br><br>**Q2:** "[Specific-example / critical incident — 'Tell me about the last time you…']"<br><br>• Probe (Silence): Count to 5-10 before filling the gap<br><br>• Probe (Laddering): "Why was that important to you?"<br><br>**Q3:** "[Contrast / comparison]"<br><br>• Probe (Hypothetical — use sparingly): "If [prior experience] had gone differently, what would you have done?" |
| **Watch For** | • [Behavior or reaction to note]<br><br>• [Confusion, hesitation, workarounds]<br><br>• [Emotional signals — frustration, delight, surprise] |
| **Moderator Note** | Funnel: broad → specific (NN/g Rosala). Avoid leading clarifiers like "Was it because X?" — use neutral "Tell me why you chose that" (NN/g 6 Mistakes). If participant says "typically" or "usually," redirect: "Can you tell me about a specific recent time?" (Critical Incident Technique). |

[REPEAT subsection for each topic/task]

### [IF Usability Test] Think-Aloud Protocol — Insert After Consent

| Label | Detail |
|-------|--------|
| **Intro Script** | "As you use [the product], please think out loud — say whatever comes to mind. What you're looking for, what you expect, what surprises or confuses you. There's no right way to do this; just narrate your thinking. If you go quiet for a bit, I may gently remind you to keep talking — that's normal."<br><br>**Demo tip:** "Here's an example: if you're shopping for pasta and see the product grid, you might say 'I'm looking for shapes, I'd expect filters on the left…'" |
| **Prompts when silent** | After 10 seconds of silence: "What are you thinking right now?" or "What are you looking for?" Never "Do you see X?" (leading). |
| **Boomerang** | If participant asks "Should I click this?" — return: "What would you normally do?" (NN/g *Talking to Users*). |
| **Moderator Note** | Silence is a tool. Count to 10 before interrupting (NN/g Fessenden). If they stop talking mid-task, prompt; do not explain the UI. |

### [IF Say-Do Gap risk is Medium/High] Say-Do Gap Module — Insert into relevant Core topics

| Label | Detail |
|-------|--------|
| **Replace typical-behavior questions with specific-incident prompts** | Instead of "How often do you cook at home?" ask "Tell me about the last time you cooked dinner at home." (NN/g Critical Incident Technique) |
| **Ground stated preferences in artifacts** | "Can you walk me through your last grocery order on your phone right now?" or "Show me the last time you [behavior]." |
| **Diary / photo prompts (if feasible)** | "Can you send me a photo of your fridge / pantry / cart before our next session?" |
| **Probe the gap directly** | When stated vs. shown diverges: "Earlier you mentioned X — I'm curious how that connected to [what I just saw]?" (Portigal — neutral framing, no accusation) |
| **Moderator Note** | Attitudinal interviews measure *stated* beliefs, not behavior. Combine with observation where possible (NN/g). Never ask participants to predict future behavior — "people are bad at predicting their future behavior" (NN/g 6 Mistakes). |

## Wrap-Up and Debrief (~[X] minutes)

| Label | Detail |
|-------|--------|
| **Script** | **[READ LOOSELY]**<br><br>"We're coming to the end of our session. A few closing questions:<br><br>1. Overall, how would you describe your experience with [what we discussed/tested] today?<br><br>2. Was there anything that surprised you, or that you expected to be different?<br><br>3. If you could change one thing, what would it be?<br><br>4. Is there anything else you'd like to share that I didn't ask about?<br><br>Thank you so much — your feedback will directly shape how we improve [product/experience]. [Incentive + next steps.]" |
| **Moderator Note** | Write your top 3 impressions IMMEDIATELY after the session (<5 min) — memory decays fast:<br><br>1. [Impression tied to study goal]<br><br>2. [Impression tied to study goal]<br><br>3. [Impression tied to study goal] |
```

**IMPORTANT:** The guide MUST end at Wrap-Up. Do NOT add Probing Techniques Bank, Observer Notes Template, or Do's/Don'ts inside the guide. Those live in `references/mod-guide-methodology.md` for the moderator to consult separately.

---

### FORMATTING RULES

- H2 and H3 headings get 36pt space above — clear visual breaks between sections after tables.
- Use `<br><br>` (double line break) between items in table cells — between Q1/Q2/Q3, between probes, between bullets — so each paragraph gets 6pt spaceBelow + 120% lineSpacing via the styling script.
- ALL content sections use 2-column tables (narrow Label ~20% | wide Detail ~80%).

---

### CONTENT GENERATION RULES

1. **No leading questions.** Every question open-ended, non-directional. Never assume the participant's opinion. (NN/g Rosala — 6 Mistakes)
2. **No interface terminology in tasks.** Describe goals, not UI ("find a way to…" not "click the button to…").
3. **Funnel technique.** Within each topic: broad → specific → closed. Broad first avoids priming (NN/g).
4. **Specific incidents over typical behavior.** "Tell me about the last time you…" beats "How often do you…" — closes the say-do gap (NN/g Critical Incident Technique).
5. **No hypotheticals except as projective tools.** "If this could change anything…" is fine at the end; "Would you use this?" is not (NN/g).
6. **No compound questions.** One question at a time (NN/g).
7. **[Moderator Note] callouts.** Embed practical facilitation tips — these are the human-skill reminders that make the guide useful in-session.
8. **Time-aware.** Allocate per study type (2a). Core gets 70-80% of total.
9. **Participant-appropriate language.** Match vocabulary to the participant profile.
10. **Name the probe type in-line** (Echo, Silence, Laddering, etc.) so the moderator builds muscle memory. See `references/mod-guide-methodology.md` for the full taxonomy.

---

### PROBING TAXONOMY — QUICK REFERENCE

Reference `references/mod-guide-methodology.md` for the full taxonomy (definitions, examples, sources). In-line names to use in the guide:

| Probe | One-line rule |
|-------|---------------|
| **Echo** (NN/g Fessenden) | Repeat their last phrase with slight interrogatory tone. |
| **Silence** (Portigal, Hall) | Count 5-10. Let them fill the gap — don't rescue. |
| **Tell-Me-More** (Anderson, NN/g) | "Tell me more about that." Evergreen. |
| **Laddering / Why** (Portigal) | "Why was that important to you?" Climb from behavior to value. |
| **Critical Incident** (Flanagan via NN/g) | "Tell me about the last time you…" Replaces typical-behavior questions. |
| **Contrast** (Portigal) | "How did that compare to [prior experience]?" |
| **Hypothetical / Projective** (Portigal — late only) | "If we came back in 5 years, what would be different?" |
| **Boomerang** (NN/g Fessenden) | Return their question: "What would you normally do?" |
| **Columbo** (NN/g Fessenden) | Trail off mid-sentence; let them complete. |
| **Specificity** (NN/g) | When vague words appear (frustrated, confusing): "What do you mean by [word]?" |

---

### BIAS MITIGATION CHECKLIST

Embed these reminders in `[Moderator Note]` callouts through the guide. Full discussion in references/.

- [ ] **Leading questions** — No "Do you like…?", "Was it because…?", or "Would you prefer…?" (NN/g, Hall)
- [ ] **Social desirability** — Participants lean helpful/positive. Normalize negative answers explicitly: "I didn't design this." (Portigal, Indi Young)
- [ ] **Acquiescence bias** — Avoid yes/no framing. Use open questions. (Hall — *Just Enough Research*)
- [ ] **Confirmation bias (moderator)** — Brain-dump hypotheses before the session so you aren't hunting for them. (Portigal)
- [ ] **Recall bias** — Pin to recent, specific incidents ("last time") not general patterns. (NN/g CIT)
- [ ] **Stated-vs-actual (say-do gap)** — Don't trust self-reported frequency or intent. Combine with observation. (NN/g, Indi Young)
- [ ] **Observer effect** — Max 2-3 silent observers; no one else in frame. (NN/g Rosala)
- [ ] **Moderator talk-ratio** — Aim for 80% participant talk time. (NN/g)

---

## Step 4.5 — Self-Critique Checklist (AIxUXR Playbook "Methodological Auditor")

Before generating the final deliverable — or handing the guide to the researcher — run the guide through this self-audit. Adapted from the AIxUXR Playbook's **Discussion Guide Critic** prompt (Loosbrock, Oct 2025), which positions the reviewer as a *methodological auditor + strategic sparring partner* grounded in the Systematic Literature Review of Best Practices for Qualitative Interview Guides.

**How to use:** Walk each dimension. If any row fails, revise the guide before returning it. Flag unresolved issues inline as `[Auditor Note: ...]` so the researcher sees the caveat. For especially high-stakes studies, run the external AIxUXR Critic Prompt (Prompt B) as a second-pass peer review.

### Part 1 — Methodological Audit (Structure & Flow)

| Dimension | What "Good" Looks Like |
|-----------|------------------------|
| **Opening rapport & consent** | Warm, non-clinical opening. Explicit recording consent before recorder starts. Participant knows purpose, duration, confidentiality, right to skip/stop. (AIxUXR §Prompt A "Introduction & Consent"; NN/g Fessenden) |
| **Four-phase structure** | Intro (5-10%) → Warm-up (10-15%) → Core (60-70%) → Wrap-up (5-10%). Times displayed per section. (AIxUXR §Prompt A "Calculate and Allocate Time") |
| **Funnel technique within Core** | Broad "Grand Tour" question first, then specific-incident probes, then closed clarifiers. No priming by leading with the narrow question. (AIxUXR §Prompt A.3; NN/g Rosala "Funnel Technique") |
| **Time budgeting** | Per-topic minutes allocated; Core gets 60-80% of total. Warm-up not eating Core. Wrap-up protected. (AIxUXR §Prompt A.1) |
| **Question sequencing / logical flow** | Each question builds on the last. No abrupt topic jumps without a bridge sentence. Transitions are signposted ("Now I'd like to shift to…"). (AIxUXR §V2 Prompt B Part 2) |
| **Wrap-up dual function** | (a) Verification — "Let me play back the themes I heard…" (b) "Anything else?" open catch-all. (AIxUXR §Prompt B SRQ1.2 "Dual Function of the Wrap-Up") |

### Part 2 — Question Quality Audit (Phrasing & Bias)

| Check | Fail Pattern → Fix |
|-------|--------------------|
| **Leading questions** | ❌ "Don't you find the new checkout faster?" → ✅ "Describe your experience using the new checkout." (AIxUXR §Prompt B example row; NN/g 6 Mistakes) |
| **Hypothetical / speculative** | ❌ "Would you use this?" / "What would you do if…?" → ✅ "Tell me about the last time you…" Reserve hypotheticals for the end as projective tools only. (AIxUXR §Prompt A.4 "No speculative questions"; Portigal) |
| **Closed yes/no framing** | ❌ "Did you like it?" → ✅ "How would you describe that experience?" (AIxUXR §V2 Prompt B; Hall) |
| **Compound / double-barrelled** | ❌ "How easy and enjoyable was it?" → ✅ Split into two questions. (NN/g) |
| **Jargon / insider terminology** | ❌ UI labels, internal product names, acronyms the participant hasn't used → ✅ Plain language matched to participant vocabulary. (AIxUXR §Responsible AI — "Inclusivity of language") |
| **Past behavior anchoring** | Every Core question tied to a concrete, recent incident — not "typically" or "in general." (AIxUXR §Prompt A.4 "Focus on past, concrete behavior"; NN/g CIT) |
| **Inclusivity & cultural assumptions** | Questions don't assume a household structure, income level, cooking frequency, dietary pattern, or tech proficiency. (AIxUXR §RAI "Equity and Fairness") |

### Part 3 — Probing & Moderator Guidance Audit

| Check | What to Verify |
|-------|----------------|
| **Probe quality per question** | Each Core question has 1-2 named probes attached (Echo, Tell-Me-More, Laddering, Silence, Critical Incident). No "naked" questions. (See Probing Taxonomy section.) |
| **Moderator Notes embedded** | `[Moderator Note: ...]` callouts appear at every transition and in at least every Core topic — covering probe strategy, silence, boomerang technique, what to watch for. (AIxUXR §Prompt A.5 "Embed Moderator Notes") |
| **Silence as a tool** | Note reminds moderator to count 5-10 seconds before filling gaps. (NN/g Fessenden; Portigal) |
| **Usability-specific: task framing** | Tasks describe the goal, not the UI ("find a way to…" not "click the red button"). (AIxUXR §Use Case 2 Critical Rule) |
| **Usability-specific: Priming → Expectation → Action → Alignment** | Each task includes the four-part sequence. (AIxUXR §Use Case 4; NN/g) |
| **Concept test: Problem validation before reveal** | Blind-need questions precede the concept reveal to avoid biasing desirability. (AIxUXR §Use Case 3 "The Reveal technique") |

### Part 4 — Strategic & Efficiency Audit

| Check | What to Verify |
|-------|----------------|
| **Coverage of research objectives** | Every objective in the RPP maps to at least one Core question. No orphan objectives; no orphan questions without an objective. (AIxUXR §V2 Prompt B Part 1) |
| **Redundancy check** | Scan for questions that probe the same underlying construct twice. Consolidate to save session time. (AIxUXR §V2 Prompt B Part 4 "Redundancy & Efficiency Report") |
| **Gaps / additional questions** | Are there adjacent insights the guide misses? Suggest 1-3 generative additions tied to objectives. (AIxUXR §V2 Prompt B Part 3) |
| **Scope discipline** | Critique stays methodological/strategic. Do NOT suggest UI copy changes, design decisions, or product strategy. (AIxUXR §V2 Prompt B role: "NOT a UI/UX copywriter") |
| **Pilot reminder** | Final output includes a reminder to pilot the guide with a teammate or friendly participant before formal data collection. (AIxUXR §6 "Always, pilot your guide") |

### Part 5 — Responsible-AI & Construct-Validity Checks (from Questionnaire Critique)

Applies especially when the guide includes structured rating questions or quant-style intercepts within a qual session.

| Check | What to Verify |
|-------|----------------|
| **Construct validity** | For any rating/scale question, ensure the revised wording still measures the intended construct — not just a clearer-sounding variant. (AIxUXR §Questionnaire Critique "VALIDATE THE CONSTRUCT") |
| **Automation-bias guardrail** | Researcher must sanity-check every AI-suggested revision against the original research intent, not blindly accept. (AIxUXR §Questionnaire Critique "Primary Risk: Automation Bias") |
| **PII scrub** | Confirm the RPP/PRD pasted into any AI prompt has been stripped of real participant names, emails, phone numbers, addresses. (AIxUXR §Critical Guardrails "NO PII, EVER") |
| **Attribution & disclosure** | When sharing the final guide with stakeholders, note that AI was used for the first-pass draft/critique. Transparency builds trust. (AIxUXR §6 "Attribute the Assist"; H.E.A.R.T. "Transparent") |
| **Guide is a protocol, not a cage** | Remind researcher: in live session, deviate from the script when valuable emergent narratives appear. (AIxUXR §6 "The Guide is a Protocol, Not a Cage") |

---

## Step 5 — Offer Google Docs Upload

After generating the guide, ask:

> "Your moderation guide is ready! Would you like me to upload it to Google Docs?"

If yes:
1. Upload via `gws-docs` (or md2doc `upload-gdoc.py`).
2. **Fix subscript formatting (MANDATORY)** — md2doc's `<br>` handling can produce SUBSCRIPT-styled text. After upload, scan via Google Docs API for `baselineOffset == 'SUBSCRIPT'` ranges and reset to `'NONE'` BEFORE styling.
3. **Default template style:** Apply `style-gdoc-full.py` — handles table colors, cell padding, font sizes (11pt body, bold col 1), column widths (proportional, col 1 auto-fit), breadcrumb, RACI chips, dash-to-disc bullets, paragraph spacing (6pt spaceBelow + 120% lineSpacing), and 36pt section spacing above H2/H3.
4. **Custom reference style:** Upload as-is.
5. File into the appropriate Google Drive project folder (Project 1 / Project 2 / Project 3) if applicable. Share the link.

---

## Tool Usage

- **AskUserQuestion** — present recommendations, gather approvals, ask for style reference.
- **google-docs:fetch-google-doc** / **Glean** (`mcp__glean_default__read_document`) — read PRDs, briefs, or style reference docs from Google Drive.
- **Read** tool or **download-gdoc.py** / **read-gdoc.py** — fallback readers for Google Docs.
- **gws-docs** or **md2doc** (`upload-gdoc.py`) — upload the final guide to Google Docs.
- **style-gdoc-full.py** — apply Instacart design system (default template only).
- **references/mod-guide-methodology.md** — load on demand when the researcher asks about a specific probe, bias, or study-type nuance.

---

## Sources

- Portigal, S. (2023). *Interviewing Users: How to Uncover Compelling Insights* (2nd ed.). Rosenfeld Media. [portigal.com](https://portigal.com/books/interviewing-users-2/)
- Young, I. *Listening Deeply* and mental model method. [indiyoung.com](https://indiyoung.com/method/)
- Hall, E. (2019). *Just Enough Research* (revised ed.). A Book Apart.
- Sharon, T. (2016). *Validating Product Ideas: Through Lean User Research*. Rosenfeld Media.
- Nielsen Norman Group: Rosala, M. — [User Interviews 101](https://www.nngroup.com/articles/user-interviews/), [6 Mistakes When Crafting Interview Questions](https://www.nngroup.com/articles/interview-questions-mistakes/), [Writing an Effective Guide for a UX Interview](https://www.nngroup.com/articles/interview-guide/), [The Funnel Technique](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/), [5 Facilitation Mistakes](https://www.nngroup.com/articles/interview-facilitation-mistakes/), [Why User Interviews Fail](https://www.nngroup.com/articles/why-user-interviews-fail/), [The Critical Incident Technique in UX](https://www.nngroup.com/articles/critical-incident-technique/); Pernice, K. & Moran, K. — [Thinking Aloud: The #1 Usability Tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/); Fessenden, T. — [Talking with Users in a Usability Test](https://www.nngroup.com/articles/talking-to-users/), [Checklist for Moderating a Usability Test](https://www.nngroup.com/articles/usability-checklist/).
- Anderson, N. — [User Research Academy](https://www.userresearchacademy.com/) and dscout *People Nerds*.
- dscout — [17 Pro Tips to Perfect One-on-One Interviews](https://dscout.com/people-nerds/tips-master-researcher-participant-interviews), [Dig Deeper with Follow-Up Questions](https://dscout.com/people-nerds/generative-research-questions).
- **Instacart AIxUXR Playbook** (internal) — Loosbrock, K., Venkatraman, S., & Milton, J. (2025). *Playbook for integrating AI within UXR workflows* (Pilot, Sep 30 / Oct 9 / Dec 1, 2025). Specifically: §1.2 "The H.E.A.R.T. of AI in Research"; *Discussion Guide Drafter & Critic* spoke (Prompt A generation, Prompt B critique — V1 and V2 revised with Bhargavi's feedback); *Questionnaire Critic* spoke (Responsible AI principles, construct validity, automation-bias guardrails). Knowledge base: *A Systematic Literature Review of Best Practices for Crafting and Evaluating Moderated Qualitative Interview Guides in UX Research*.
