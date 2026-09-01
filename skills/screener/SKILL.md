---
name: screener
description: Use when a researcher, designer, or PM needs a standalone participant screener for a self-serve (DIY), unmoderated study — one that can be handed straight to a recruiting tool without a researcher walking through it. Triggers on "write a screener", "draft a screener", "build a recruiting screener", "screener for [study]", or "/screener".
---

# Screener

Generates a standalone, copy-paste-ready participant screener for a self-serve unmoderated study. Grounded in Erika Hall's *Just Enough Research* (right-size the recruit, don't over-scope the ask), Steve Portigal's *Interviewing Users* (the screener is where good and bad recruits get decided — and where "professional respondents" learn to guess the right answer if you let them), Tomer Sharon's *Validating Product Ideas* (screen for real behavior, not stated interest), Indi Young's mental-model segmentation (recruit by what people *do*, not just who they *are*), Nikki Anderson's *User Research Academy* screener-writing guidance, Nielsen Norman Group's participant-recruiting canon, dscout *People Nerds*, and the UserTesting Blog's self-serve screener best practices — the closest published analogue to this skill's exact use case. Also applies the Instacart-internal **AIxUXR Playbook**'s H.E.A.R.T. framework, with extra weight on **Responsible**: a DIY screener runs with no researcher in the room to catch a bad question live, so the draft has to be safe by default.

## Guiding philosophy: H.E.A.R.T., DIY edition

| Letter | Principle | What it means when there's no researcher moderating the screen |
|--------|-----------|------------------------------------------------------------------|
| **H** | **Human-centered** | Every gating question has a legitimate reason to exist. No question exists just because "it might be useful later." |
| **E** | **Experience-focused** | A screener is itself a UX. Long, repetitive, or confusing screeners lose good respondents before the study starts. |
| **A** | **Amplifying** | This skill drafts the logic; the requester still owns the final call on quotas and exclusions — especially anything that reads as sensitive. |
| **R** | **Responsible** | Collect only what's needed to qualify or quota. No unnecessary PII. Flag — don't silently draft — anything touching a vulnerable population, health, finances, or minors. |
| **T** | **Transparent** | Every disqualifying option is marked so it can't be missed by whoever sets up the recruiting tool. Every quota is stated as a number, not a vibe. |

## When to use this skill

Use this skill when the request is to produce a **standalone screener** — a document that fully specifies who qualifies, who doesn't, and how the sample should be split — with no researcher expected to interpret it afterward. That "no researcher in the loop" constraint is what separates this from a screener embedded inside a full research plan.

Trigger phrases:
- "/screener"
- "write a screener for [study]"
- "draft a recruiting screener"
- "build a screener I can hand to [recruiting tool / panel vendor]"
- "screen participants for [study]"

**Where this sits in the self-serve pipeline:** this skill is a downstream step for studies routed to the DIY track — a designer or PM running their own unmoderated study without a researcher driving it. It typically runs after a triage step decides the study is DIY-appropriate ([[diy-triage]]), and its output feeds directly into the unmoderated question script ([[unmod-script]]). If no triage has happened yet and it's unclear whether this study should be DIY at all, say so before drafting — see the escalation checklist in Step 5.

**Do NOT use this skill for:**
- The sampling section of a full research plan — that's owned by `research-plan`; this skill produces the standalone artifact, not a plan subsection.
- A moderated study's participant criteria, where a researcher will use judgment in real time — `mod-guide` assumes a live moderator and doesn't need every edge case pre-resolved in writing.

## Core principle: a screener has exactly two jobs — never blend them

1. **Qualify** — a hard yes/no on whether this person can give the study a valid signal at all. Qualifying logic must be unambiguous enough that a recruiting tool (or a human skimming applications) can apply it without judgment calls.
2. **Quota** — softer targets that shape sample *mix* (age spread, tenure, device split, attitude segment). Quota logic is a target to fill, not a pass/fail gate.

Collapsing the two is the most common screener failure: a "nice to have" demographic gets written as a hard screen-out, or a real disqualifier gets buried inside a multi-select where it's easy to miss. Every question in Step 3 below is tagged as one or the other — never both.

---

## Step 1 — Gather study basics

Because this skill is built for a requester working alone, keep intake to a **single short batch** — this is not the multi-round interrogation a full research plan deserves. Use `AskUserQuestion` once, up to 4–5 questions:

1. **What's being studied, in plain terms?** (e.g., "a checkout flow," "a new onboarding screen" — accept a one-line description, don't demand a brief)
2. **Who needs to qualify?** (the core behavior or role a valid respondent must have — e.g., "has bought X in the last 3 months," "manages the household's Y")
3. **Platform / device the study runs on** (mobile web, native app, desktop, specific OS — determines whether a device-check question is needed)
4. **Target sample size + any known quota splits** (e.g., "N=40, roughly half new-to-category / half experienced")
5. **Anything already known that should disqualify someone** (competitors, employees, existing beta testers, recent participants in a similar study — accept "not sure, use your default list")

If the requester pastes a brief, kickoff note, or Slack thread instead of answering live, extract these five answers from it and read them back for confirmation rather than re-asking from scratch.

---

## Step 2 — Propose the screening logic, then confirm

Before drafting the full screener, present a short recommendation table and get a one-question approval (`AskUserQuestion`, single question, "looks right" vs. "adjust"):

| Parameter | Recommendation |
|---|---|
| **Core qualifying gate** | [The one behavior/role every respondent must have — stated as a pass/fail test] |
| **Quota dimensions** | [The 1–3 splits that matter for this study — e.g., tenure, device, attitude segment] |
| **Standard exclusions** | Company/competitor employees · market-research professionals · immediate family of either · recent participant in a similar study (default list — see Step 3) |
| **Device/platform check** | [Included / not needed] — based on Step 1 answer 3 |
| **Estimated length** | [N questions, ~X min] |

Do not skip this confirmation just because the answers seem obvious — a wrong quota assumption is expensive to fix after the screener is already live in a recruiting tool.

---

## Step 3 — Draft the screener

### 3a. Screening Logic Legend (put this at the top of every screener, don't make the reader infer conventions)

| Tag | Meaning |
|---|---|
| **SCREEN OUT** | Selecting this option ends the screener immediately — respondent does not qualify. |
| **EXCLUSIVE** | This option cannot be combined with any other choice in a multi-select (e.g., "None of these"). |
| **RANDOMIZE** | Answer options should be shown in random order per respondent, to avoid position bias. |
| **DO NOT RANDOMIZE** | Options must stay in the fixed order shown (e.g., a scale, a chronological list, a recognizable brand list where order aids recall). |
| **MUST SELECT [bolded option] — OTHERWISE SCREEN OUT** | Used when only specific answers among several plausible-sounding ones actually qualify; bolding in the source document is the qualifying flag. |

### 3b. Recommended question order

Published guidance (UserTesting Blog, NN/g) and Portigal's screener-gaming warnings point the same direction: **put hard disqualifiers first.** Every question before a screen-out wastes respondent time and, on paid panels, wastes recruiting spend. Soft, quota-only, or segmentation questions can come later since nobody is disqualified by them.

1. **Hard eligibility gates** — minimum age, and the standard exclusion list (Step 3d). Screen out immediately.
2. **Role / core-behavior gate** — the one qualifying test from Step 2. Often phrased as "which of these best describes you," with only specific bolded options qualifying and everything else screening out.
3. **Recency / frequency-of-use qualifier** — ties directly to whether the person can speak to the study topic at all; may double as a quota dimension.
4. **Device / platform check** — only if the study is device- or OS-specific.
5. **Standard demographic quotas** — age bracket, household composition, region, etc. Quota-only; the hard age *minimum* is already handled in step 1.
6. **Behavioral / context quotas** — adjacent-product usage, subscriptions held, who they're using the product for. Multi-select; mark each RANDOMIZE or DO NOT RANDOMIZE explicitly.
7. **Occasion / use-case check** — what they've used the product *for* recently. Often carries its own soft disqualifier ("none of these" → screen out) if the study needs a specific occasion to have occurred.
8. **Motivation / decision-factor questions** — non-disqualifying; informs later segmentation, not eligibility.
9. **Attribute / preference segmentation** — non-disqualifying traits relevant to the study (e.g., accessibility needs, lifestyle attributes, category preferences) — used to assign stimuli or personalize the study experience, not to gate.
10. **Attitude / importance rating** — a single Likert-style item, non-disqualifying.
11. **Psychographic segment** — one single-select attitudinal question, framed so every option sounds acceptable to select ("may select" tone — nobody should feel judged into picking the "good" answer). Non-disqualifying; used for quota only.

If panel/recruiting cost isn't a concern for this study, the requester may prefer a warm-up-first order (broad demographics before the eligibility gate) for respondent experience. Note the trade-off, default to disqualifiers-first, and let them override in Step 2's confirmation.

### 3c. Output template

Use this structure. Everything in `[brackets]` is a placeholder the requester (or Claude, from Step 1's answers) fills in — never leave a bracket in the delivered document.

```
# [Study Name] — Recruiting Screener

Owner: [Name/team] · Platform: [where this will be fielded] · Target N: [total] · Est. length: [X min]

## Screening Logic Legend
[Insert the legend table from 3a verbatim]

## Quotas
| Quota group | Target N | Definition |
|---|---|---|
| [Group A] | [n] | [what defines this bucket] |
| [Group B] | [n] | [what defines this bucket] |

---

1. What is your age? SCREEN OUT anyone under [minimum].
   a. Under [minimum] — **SCREEN OUT**
   b. [age band] · c. [age band] · d. [age band] · … (AIM FOR A MIX across remaining bands)

2. Do you currently work for [Company], a competitor, or a market research firm? Or is anyone in your household?
   a. Yes — **SCREEN OUT**
   b. No

3. Have you participated in a research study about [this topic/product area] in the last [X months]?
   a. Yes — **SCREEN OUT**
   b. No

4. Which of the following best describes you? **MUST SELECT ONE BOLDED OPTION BELOW; OTHERWISE SCREEN OUT.**
   a. **[The core qualifying behavior/role, stated plainly]**
   b. [A close-but-disqualifying variant] — **SCREEN OUT**
   c. [Another disqualifying variant] — **SCREEN OUT**

5. In the past [X months], how often have you [core behavior]?
   a. [frequency band] · b. [frequency band] · c. Never — **SCREEN OUT** (if recency is a hard requirement)

6. [Device/platform check — only if the study is device-specific]
   Which of the following do you use? Select all that apply. **[RANDOMIZE]**
   a. [Platform/device A] · b. [Platform/device B] · c. None of these **[EXCLUSIVE]**

7. Which of the following best describes your household? (quota only, not disqualifying)
   [Standard household/composition options] · Prefer not to answer

8. Which of the following [adjacent products/services], if any, have you used in the past [X months]? Select all that apply. **[DO NOT RANDOMIZE if list order aids brand recognition]**
   [Option list] · None of these **[EXCLUSIVE]**

9. In the past [X months], have you used [product] for any of the following? Select all that apply. **[RANDOMIZE]**
   [Occasion/use-case options] · None of these — **SCREEN OUT** (only if a specific occasion is required)

10. Which of the following played a role in your decision to [core behavior]? Select all that apply. (non-disqualifying)
    [Motivation/decision-factor options]

11. [Attribute/preference segmentation relevant to this study — e.g., accessibility needs, category preferences]. Select all that apply. (non-disqualifying, feeds personalization)
    [Option list] · None of the above

12. How important is [attribute from Q11] to your experience with [product]?
    Extremely important · Very important · Somewhat important · Not very important · Not at all important

13. Which of the following best describes you? Please select one. (non-disqualifying — phrase every option so none reads as the "wrong" answer)
    [Segment A] · [Segment B] · [Segment C]

---

## Termination message
"Thank you for your interest — based on your answers, you don't qualify for this particular study. We appreciate your time."

## Qualify message
"Thanks! Based on your answers, you qualify for this study. [Next steps — scheduling link, study access link, etc.]"
```

---

## CONTENT GENERATION RULES

1. **One disqualifying condition per question.** Never bury a screen-out inside a multi-part or double-barreled question — if it needs its own SCREEN OUT tag, it needs its own answer option.
2. **Every screen-out option is visually tagged**, every time, with no exceptions — the whole point is that a recruiting-tool setup or a fast skim can't miss it.
3. **Neutral wording on every option.** Never phrase an option so the "correct" (qualifying) answer is obvious — Portigal's core screener-gaming warning: professional respondents learn to spot and select the answer that gets them in.
4. **Disqualifiers first, segmentation last** (Step 3b) unless the requester explicitly prefers a warm-up-first order for respondent experience.
5. **Randomize opinion/behavior option lists** to avoid primacy bias; **keep brand lists, scales, and chronological lists in fixed order** where recognition or logical sequence matters. Tag every multi-select explicitly as one or the other — never leave it unmarked.
6. **"None of these" / "None of the above" is always EXCLUSIVE** in a multi-select — mark it so recruiting-tool logic can't let it combine with real answers.
7. **Include the standard exclusion list by default**: company/competitor employees, market-research professionals, immediate family of either, and recent participation in a similar study. Drop only if the requester explicitly says it doesn't apply.
8. **Keep it short.** Rule of thumb: under ~12–15 questions and under 5 minutes for a self-serve unmoderated screener. There's no researcher present to notice mid-flight that a screener is bleeding respondents — length has to be right the first time.
9. **Plain language, no internal jargon.** This document may be read or administered by someone outside the research team (a vendor, a panel, the requester's own recruiting tool) with no researcher to translate.
10. **Minimize PII.** Collect only what's needed to qualify or quota (H.E.A.R.T. "Responsible"). No unnecessary names, contact details, or sensitive attributes beyond what the study genuinely requires.
11. **Every quota bucket gets a target N.** "Aim for a mix" alone isn't a quota — pair qualitative guidance with an actual number wherever the requester gave one, or a sensible default with a flag to confirm.
12. **Device/platform checks only when relevant.** Don't ask about devices the study doesn't touch.

---

## Step 4 — Self-Critique Checklist (run silently before delivering)

| Check | What "pass" looks like |
|---|---|
| **Qualify/quota separation** | No question does both jobs. Every screen-out is a hard qualifier; every quota question is clearly soft. |
| **Every screen-out tagged** | No implicit disqualifiers — a skim of the document alone reveals every terminate condition. |
| **No leading options** | No option's wording telegraphs which answer qualifies. |
| **No double-barreled questions** | Each question tests exactly one thing. |
| **Quota math sums to target N** | Quota group targets add up to (or sensibly exceed, for over-recruit buffer) the total sample size from Step 1. |
| **Length check** | Under ~12–15 questions / ~5 minutes, or a flagged exception with a reason. |
| **Plain language** | No internal product jargon, acronyms, or feature code names — a vendor or panel respondent with zero context can answer every question. |
| **PII minimization** | Nothing collected beyond what's needed to qualify or quota. |
| **Standard exclusions present** | Employee/competitor/market-research/recent-participant exclusions included or explicitly waived by the requester. |
| **Escalation flag** | See below — if anything trips this, say so before delivering rather than silently drafting around it. |

**Escalation out of the DIY track:** if the study topic touches a vulnerable population, minors, health, finances, or anything else where a wrong qualifying call has real consequences, flag it plainly: *"This touches [X] — that's usually outside what a self-serve screener should carry alone. Want me to draft it anyway, or would you rather loop in a researcher first?"* Draft it only if the requester confirms.

---

## Step 5 — Deliver

Default output is **clean, plain markdown** — this is meant to be pasted directly into a recruiting tool, a panel vendor's portal, or a screener builder, not routed through a styling pass. Don't offer a Google Doc upload unless asked; if asked, upload plain (no custom template) since the destination is usually a system that ignores rich formatting anyway.

Close with a short status note: what qualifies, what disqualifies, the quota structure, and anything flagged for the requester's attention (an escalation flag from Step 4, a default exclusion that was assumed rather than confirmed, an estimated length that ran long). If this screener feeds a downstream script, mention that [[unmod-script]] is the natural next step once the screener is locked.

---

## Common Screener Failures

| Failure | Symptom | Fix |
|---|---|---|
| Hidden disqualifier | A screen-out option looks like a normal answer choice | Tag every screen-out explicitly, no exceptions |
| Gameable wording | One option is obviously "the answer that gets you in" | Rewrite neutrally so no option stands out |
| Quota-as-gate confusion | A nice-to-have demographic is written as a hard screen-out | Reclassify as quota; only true eligibility blockers screen out |
| Demographics-first bloat | Ten questions run before the one that actually disqualifies most people | Reorder — hard gates first |
| Missing device check | Study is platform-specific but the screener never asks | Add a device/platform question when Step 1 flags it |
| Forgotten standard exclusions | No employee/competitor/market-research exclusion at all | Include the default list unless explicitly waived |
| Quota math doesn't add up | Bucket targets don't sum to the stated sample size | Recompute before delivering |
| Screener too long | 20+ questions for an unmoderated self-serve study | Cut to the ~12–15 question / ~5 minute target |
| Sensitive topic, no flag | Health/financial/minor-related study drafted with no escalation note | Flag it per Step 4 before delivering |

---

## Tool Usage

- **AskUserQuestion** — Step 1 (single intake batch) and Step 2 (one approval question). Not used again after Step 2 — the deliverable should not require further back-and-forth to finish.
- **Read** — read pasted briefs, Slack threads, or kickoff notes to extract Step 1's answers instead of re-asking.
- **`google-docs:fetch-google-doc`** / **Glean `read_document`** — only if the requester points to an existing brief or prior screener as a starting reference.
- The generated markdown is the primary, final deliverable — a self-serve screener has no researcher downstream to polish it further.

---

## Sources

- Hall, E. *Just Enough Research*. A Book Apart. — right-sizing the recruit to the study.
- Portigal, S. *Interviewing Users: How to Uncover Compelling Insights* (2nd ed.). Rosenfeld Media. — screener-gaming and the "professional respondent" risk.
- Sharon, T. *Validating Product Ideas: Through Lean User Research*. Rosenfeld Media. — screening for real behavior over stated intent.
- Young, I. *Listening Deeply* / mental-model segmentation. [indiyoung.com](https://indiyoung.com/)
- Anderson, N. — [User Research Academy](https://userresearchacademy.com/), screener-writing guidance.
- Nielsen Norman Group — participant-recruiting and screener-design articles. [nngroup.com](https://www.nngroup.com/articles/)
- dscout — [People Nerds](https://dscout.com/people-nerds), participant-quality and recruiting guidance.
- UserTesting Blog — self-serve / unmoderated screener best practices. [usertesting.com/blog](https://www.usertesting.com/blog)
- **Instacart AIxUXR Playbook** (internal) — H.E.A.R.T. framework, applied here with emphasis on Responsible (PII minimization, escalation out of DIY when a study is sensitive).
