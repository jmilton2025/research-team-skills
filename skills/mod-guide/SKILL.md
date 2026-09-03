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

**Render as a real Markdown table — NEVER inside a triple-backtick code fence.** The researcher needs to scan this in proper table formatting, not in monospaced code. Show it directly in the chat as:

> Based on your inputs, here's what I recommend:
>
> | Parameter | Recommendation | Why |
> |-----------|---------------|-----|
> | Study Type | [IDI / Usability / Concept / Diary / Focus] | [1-line rationale from inputs] |
> | Moderated vs Unmoderated | Moderated | [rationale — depth, probing, observation] |
> | Duration | [30/45/60/90 min] | [based on scope + study type] |
> | Number of Participants | [N=8 / 12 / 24] | [based on objectives + saturation] |
> | Participant Profile | [e.g., "Instacart shoppers 25-45, 2+ orders/week"] | [derived from target users] |
> | Key Topics / Tasks | • Topic 1 · Topic 2 · Topic 3 | [mapped to objectives] |
> | Research Goal | [1-2 sentences] | — |
> | Say-Do Gap Risk | [Low / Medium / High] | [see Step 2c] |

(Use the example above as a template — strip the leading `>` characters and write the table directly. The point is: no triple backticks, no code block. A real table.)

### 2c. Say-Do Gap Risk Check

Flag **High** if the study asks about **stated behavior, preferences, or intent** rather than observable action — e.g., "how often do you cook at home?", "would you pay for this?", "do you read ingredient labels?". When flagged High, the generated guide automatically includes the **Say-Do Gap Module** (see references/mod-guide-methodology.md).

Source: NN/g "Why User Interviews Fail" — *"Interviews do not produce reliable data about user behavior."* Indi Young's listening sessions also warn: people reconstruct rather than report.

---

## Step 3 — Researcher Approval (ASK ALL KEY PARAMETERS BEFORE DRAFTING)

### 🚫 ZERO MID-FLOW QUESTIONS RULE (read this first — it's the most important rule in this skill)

**Once Step 3 ends, `AskUserQuestion` is FORBIDDEN until the deliverable is shared.** That means:

- Steps 4 (Generate), 4.5 (Self-Critique), and 5 (Upload + Style) **must run with zero further user prompts**. No "should I…?", no "want me to…?", no read-back confirmations, no clarifying questions.
- If you discover a missing piece of information mid-flow, **resolve it with a sensible default** based on the inputs and Step 3 answers — don't ask. If the default turns out wrong, the researcher will say so after seeing the deliverable; that's faster than re-prompting.
- Before calling `AskUserQuestion` at any point, ask yourself: *"Has Step 3 already closed?"* If yes → DO NOT CALL IT. Pick a default and proceed.
- Re-asking mid-flow is the failure mode this skill is explicitly designed to prevent. The whole point of Step 3 is to consolidate every decision *upfront*.

**The researcher gets exactly two interaction moments with this skill:** (1) Step 1 — paste inputs, and (2) Step 3 — answer the popup batches. After Step 3 closes, the next thing they see is the finished, uploaded, styled Google Doc.

---

**Hard rule:** Ask the researcher about **every key moderation-guide parameter** through `AskUserQuestion` *before* generating the guide in Step 4 — even the ones that look "obvious" from the inputs. The point is to give the researcher a chance to **confirm or override** every meaningful design choice in one place. They should walk away from Step 3 feeling like they directed the guide, not received it.

**Three guarantees the researcher gets in every popup:**
1. **A Recommended option** — Claude's pick (extracted from the inputs or chosen by best practice) appears first, marked `(Recommended)`.
2. **2–3 alternatives** — real, plausible alternatives so the choice is meaningful, not rubber-stamped.
3. **An editable "Other" field** — `AskUserQuestion` always offers an "Other" free-text input; the researcher can type any custom value (e.g. a custom duration like "75 min", a custom participant count like "N=18", a custom profile).

**The very last question asked — across all batches — must always be the format/styling question.** The only exception: **demo/sample/test runs**, where the format question is skipped entirely and styling auto-resolves to Jedida Reporting (see "Demo-run auto-trigger" below).

### Mandatory question set (ask ALL of these — even if extracted from inputs)

| # | Question | Recommended (Claude's pick) | Alternatives |
|---|----------|------------------------------|--------------|
| 1 | **Phase/scope** — which phase or sub-study to build (only if multi-phase plan) | The earliest unbuilt phase | Other phases · Both phases |
| 2 | **Study type** | Best fit from inputs (IDI / Usability / Concept / Diary / Focus) | The two next-best alternatives |
| 3 | **Moderation style** | Moderated remote / Moderated in-person / Unmoderated | The two not picked |
| 4 | **Duration** | Extracted minutes or 60 min default | 30 / 45 / 60 / 90 (drop the recommended one from this list) |
| 5 | **Number of participants** | Extracted N or method-appropriate default (IDI N≈12, cog N≈12, usability N≈5–8) | Smaller / larger options |
| 6 | **Participant profile** | Extracted screen criterion | Looser / tighter alternatives |
| 7 | **Key topics / tasks** | The 3–5 extracted topics, accept-as-is | "Edit the list" · "Add another topic" |
| 8 | **Say-Do Gap module** | Include / Skip / Let Claude decide — Recommended depends on Step 2c risk flag | The other two |
| 9 | **Stimuli handling** (usability/concept only) | Screen-share / static PDF / live prototype | The two not picked |
| **LAST** | **Format / output styling** | See options below | See options below |

**Only two parameter rows may be skipped — and only under these exact conditions:**
- **Row 1 (Phase/scope)** — skip only when the inputs describe a single-phase study with no sub-studies.
- **Row 9 (Stimuli handling)** — skip only when the study is an IDI, diary check-in, or focus group (i.e. no UI/concept stimulus involved).

(The **LAST row — Format / styling** — is also skipped on demo/sample/test runs, which auto-resolve to Jedida Reporting. See "Demo-run auto-trigger" below. On real runs it is always asked.)

**Every other row must be asked**, even if the answer seems obvious from the inputs. The researcher confirming an extracted value is the whole point. Never skip a row just because you think you know the answer.

### Batching rules

`AskUserQuestion` accepts 1–4 questions per call. Group the questions you've identified into the fewest batches possible, **format always in the final batch as the final question**:

- **3 questions or fewer (incl. format)** → 1 batch, format is the last item.
- **4 questions (incl. format)** → 1 batch, format is q4.
- **5–7 questions (incl. format)** → 2 batches: design first (up to 4), then a follow-up batch ending in format.
- **8–9 questions (incl. format)** → 3 batches: 4 + 4 + 1 (format alone in batch 3).

Never split format across batches. Never put format anywhere but the very last position of the very last batch.

### How to phrase each question

For every question, structure the popup like this:

- **Question text** — short, plain English, ends with a "?". Example: "How long should the session be?"
- **Header chip** — ≤ 12 chars (`Duration`, `Participants`, `Study type`).
- **Option 1** — `(Recommended)` label suffix, with the Claude-picked value plus a brief description of *why* it was picked.
- **Options 2–3** — real alternatives with descriptions explaining the tradeoff.
- **Option 4 (sometimes)** — a fourth alternative if useful, but keep it tight.
- "Other" is auto-added — never include it manually. The researcher uses it to type custom values.

### 🎬 Demo-run auto-trigger (skip the format question entirely)

**If this is a demo / sample / test run, do NOT ask the format/styling question at all.** Auto-resolve `format = Jedida Reporting (navy/blue)` and proceed. The researcher never sees the styling popup or its "Other" field on a demo run.

**A run counts as a demo when** the invocation contains a clear demo/sample/test signal — e.g. "demo", "sample run", "test this skill", "show me how this works", "just demoing", "dry run", or an equivalent phrase indicating it's a walkthrough rather than a real study deliverable. (This is the same signal class as `feedback_sample_runs.md`, which also means: do NOT save the output to project folders, the tracker, or Drive.)

**Effect on Step 3 batching:** drop the format row entirely. The format question is normally the very last question across all batches — on a demo run it simply isn't asked, so the last *real* parameter question becomes the final question. All other parameter rows are still asked as normal (the demo still exercises the full questioning flow — only styling is auto-resolved). Hold `format = Jedida Reporting` for Step 5 exactly as if the researcher had picked option 1.

**Real (non-demo) runs:** ask the format question normally, per below.

### The mandatory format question (always the last one asked — UNLESS this is a demo run, see above)

> "How should the final Google Doc be styled?"

Four explicit options + auto "Other" for custom reference URL:

- **"Default — Jedida Reporting (navy/blue)" (Recommended)** — Canonical Jedida Reporting palette (navy NAV H1 nav bars, LBLUE label columns, alternating WHITE/LGRAY rows, DGRAY borders, Calibri typography). Promoted to default for mod guides on 2026-05-20. Styler: `~/.claude/skills/jedida-reporting/scripts/apply_jedida_reporting.py`.
- **"Jedida's mod-guide style (forest green)"** — Original mod-guide template (DM Serif Display headings, DM Sans body, dark-green table headers, dark-green bold label columns). See `references/canonical-template-spec.md`. Source: `https://docs.google.com/document/d/18Q9V4th9BwwNtlLXSncmMpiN591XTV1RzCUAyxym7wI/edit`
- **"Plain Google Docs (no custom style)"** — Skip the styling pass; default Google Docs formatting only.
- **"Match a custom reference doc — paste URL in 'Other' field below"** — The researcher uses the auto-Other free-text field to paste the Google Doc URL they want the styling matched to. The URL arrives inline with this answer — **never ask for it in a separate batch.**

If the "Other" field comes back with a Google Doc URL, treat it as: format = Custom Reference, ref_doc_id = parsed-from-URL.

### Holding the format answer for Step 5

- **Default (Jedida Reporting navy/blue)** → run `uv run --python 3.12 --with google-api-python-client --with google-auth --with google-auth-oauthlib --with google-auth-httplib2 --with requests --with python-dotenv python ~/.claude/skills/jedida-reporting/scripts/apply_jedida_reporting.py <DOC_ID>` after upload.
- **Forest-green mod-guide style** → run `scripts/apply_canonical_template.py <DOC_ID>` after upload.
- **Custom Reference (URL came back via "Other")** → run `scripts/apply_custom_template.py <TARGET_DOC_ID> <REF_DOC_ID>` after upload. **Apply silently — do NOT do a read-back confirmation, do NOT ask "apply these to your mod guide?"** If the styling looks wrong on the final doc, the researcher will say so post-delivery; that's a one-off correction, not a reason to break the no-mid-flow-questions rule.
- **Plain** → upload only; skip the styling script.

---

## Step 4 — Generate the Moderation Guide

Apply the researcher's approved parameters and style. For the default template, follow the OUTPUT TEMPLATE below. Branch the Core section by study type (see 2a).

### OUTPUT TEMPLATE (default Instacart style — TABLES = QUESTIONS ONLY)

> **Core principle (codified 2026-05-04 from Diet Personalization mod guide):** When the moderator is sitting in front of a participant, their eye should land on a table that contains **only the words to read or ask aloud**. Probes, watch-fors, tagging guidance, "don'ts," and methodology rationale all live in **prose around the tables**, not inside cells. Total length target: **~5 pages**, not 13.

```
*UX Research | Moderation Guide | [Quarter Year]*

# [Study Title — derived from research goal]

**[Phase or sub-title if applicable, e.g. "Phase 1: Diagnostic Deep Dive (Contextual Inquiry IDIs)"]**

Last updated: [Month Year]

- **Responsible:** [Name] (Role)
- **Accountable:** [Name] (Role)
- **Consulted:** [Names with roles]
- **Informed:** [Names with roles]

| Parameter | Detail |
|-----------|--------|
| **Study Type** | [final] |
| **Duration** | [X] minutes — [warm/core/probe/close split, e.g. "10 / 35 / 10 / 5"] |
| **Format** | [Moderated remote / In-person / Unmoderated], [tools] |
| **Participants** | [profile + screening criterion] |
| **Goal** | [1-sentence research goal — what we're learning, separated by · for multiple objectives] |

---

## Pre-Session Checklist

[Bullet list with ☐ checkboxes — NOT a table. Each item: "category — what to verify"]

- ☐ Participant validated — [screening criterion confirmed]
- ☐ Device — [participant on their own device, app loaded, etc.]
- ☐ [Stimuli / artifacts loaded]
- ☐ Recording armed · consent script ready · observers cameras-off

---

## Consent + Recording Script — READ VERBATIM (~60 sec)

[2-col table. Col 1 = short cue label. Col 2 = exact words to read aloud — no annotations, no moderator notes inside the table.]

| Cue | Read aloud |
|-----|------------|
| **Open** | "Hi [name], thanks for joining. I'm [moderator], a researcher at Instacart." |
| **Purpose** | "I'm here to learn from your experience — no right or wrong answers, nothing being judged. I didn't design any of this, so you can't hurt my feelings." |
| **What we'll do** | "[Concrete description of what's about to happen.]" |
| **Recording** | "With your permission, I'd like to record audio, video, and screen. It stays internal at Instacart. **Is that okay?**" |
| **Confidentiality** | "Your name and any identifying details will be removed before anything is shared internally." |
| **Control** | "About [X] minutes. You can skip any question or end at any time — and you'll still get the incentive." |
| **Open floor** | "Any questions before we start?" |

> Wait for explicit verbal **"yes"** before pressing record. Take 30–60 seconds of small talk after consent before Q1.

---

## Phase 1 — Warm-Up & [Domain] Identity (~[X] min)

[PROSE OUTSIDE TABLE — 1-sentence goal, then probe list, then "Don't" warnings.]

**Goal:** [1-sentence statement of what this phase is for.]

**Probes to use:** Echo · Tell-me-more · Silence (count to 7) · Laddering ("Why is that important to you?") · Critical Incident ("Tell me about the last time…") · Specificity ("What does '[word]' mean for *you*?")

**Don't:** [Things the moderator should avoid — e.g. priming the studied label, mentioning the product by name first, leading framings.]

| # | Ask |
|---|-----|
| **Q1** | "[Open warm-up question — broad, easy, non-priming.]" |
| **Q2** | "[Identity / vocabulary question.]" |
| **Q3** | "[Rules vs. goals question.]" |
| **Q4** | "[Context / surrounding-people question.]" |

---

## Phase 2 — [Core Method, e.g. Contextual Inquiry / Tasks / Concept Test] (~[X] min) — CORE

[PROSE OUTSIDE TABLE — explain what this phase IS, list the categories the moderator silently tags, give the framing rule.]

This is the spine of the study. [1-2 sentences explaining the method and what to silently capture.]

[If applicable, list the silent-tagging categories as ☐ bullets with one-line descriptions.]
- ☐ **CATEGORY 1** — [definition]
- ☐ **CATEGORY 2** — [definition]
- ☐ **CATEGORY 3** — [definition]

### 2.1 [Sub-phase name] (~[X] min)

[Optional 1-line "don't" or "watch for" prose.]

| # | Ask |
|---|-----|
| **Setup** | "[The setup line you say aloud — describe the goal, not the UI.]" |
| **If hesitant** | "[Reassurance line if they push back.]" |

### 2.2 [Sub-phase name] (~[X] min)

[Prose: which probes apply, what the sub-question structure tests.]

| # | Ask |
|---|-----|
| **Q5** | "[Open question for this sub-phase.]" |
| **Q6a** | "[Probe sub-question.]" |
| **Q6b** | "[Probe sub-question.]" |
| **Q6c** | "[Probe sub-question.]" |

[Repeat 2.X subsections as needed. Each one: 1-2 lines of prose ABOVE the table, table BELOW with question rows only.]

### 2.5 [Final sub-phase, often a Say-Do or reconciliation step]

[Prose: framing rule — "never accuse, never imply contradiction is wrong" / "watch for whether they reframe identity vs. behavior" — these stay OUT of the table.]

| # | Ask |
|---|-----|
| **Q12** | "[The reconciliation question, including any [recall their phrasing] placeholders.]" |
| **Q12 follow-up** | "[Optional follow-up question.]" |

---

## Phase 3 — [Optional stimulus / language test phase] (~[X] min)

[Prose: setup, time-management call ("if Phase 2 ran long, cut from 5 to 3"), what to capture verbatim.]

| # | Ask |
|---|-----|
| **Setup** | "[Stimulus introduction.]" |
| **Q13** | "[First-impression question.]" |
| **Q14** | "[Trust / friction question.]" |
| **Q15** | "[Reframe / rewrite question.]" |

---

## Phase 4 — Wrap-Up (~5 min)

| # | Ask |
|---|-----|
| **Q16** | "[Surprise / reflection question.]" |
| **Q17** | "[One-thing-to-change question.]" |
| **Q18** | "[Open floor.]" |
| **Close** | "Thank you so much — [study-specific gratitude]. [Confirm incentive + next steps.]" |

---

## Post-Session Debrief

[Numbered list, NOT a table. Within 5 min of session end, capture three things while memory is fresh.]

1. **[Primary classification field]:** ☐ [Option A] · ☐ [Option B] · ☐ [Option C] · ☐ Mixed
2. **[Secondary judgment field]:** ☐ [Option A] · ☐ [Option B] · ☐ Ambiguous — plus one-line rationale
3. **Most diagnostic verbatim quote:** one sentence, exact words from the participant
```

**IMPORTANT:**
- The guide MUST end at Post-Session Debrief. Do NOT add Master Probe Bank, Bias Mitigation Checklist, or Self-Critique Audit inside the guide. Those live in `references/mod-guide-methodology.md` for the moderator to consult separately.
- **Tables contain ONLY questions / read-aloud lines.** Probes, watch-fors, tagging guidance, "don'ts," and methodology rationale ALWAYS live in prose above or below the table — never inside cells.

---

### FORMATTING RULES (visual + structural)

#### Structural
- **Tables = questions only.** Col 1 = short label (`Q1`, `Q2`, `Setup`, `Open`, `Cue`). Col 2 = the exact words the moderator reads or asks aloud.
- **Probes, watch-fors, "don'ts," tagging guidance, methodology rationale → prose ABOVE the table.** One sentence per concept where possible.
- **Use `>` blockquotes** for one-line moderator reminders that follow a table (e.g. "Wait for explicit verbal 'yes' before pressing record.").
- **No `<br><br>` line breaks inside table cells.** Each cell holds one short scannable line. If a question has multiple parts, split into separate rows (`Q12`, `Q12 follow-up`) or sub-questions (`Q6a`, `Q6b`, …).
- **Pre-Session Checklist and Post-Session Debrief are bullets/numbered lists, NOT tables** (they aren't questions).
- **Total target length: ~5 pages.** If the guide exceeds 7 pages, cut moderator-note paragraphs and redundant explanation.

#### Visual (applied by the styling pipeline below)

**Default — Jedida Reporting (navy/blue, promoted 2026-05-20):**
- **Body / table cells:** Calibri 10pt (`#000000`)
- **Headings (H1/H2/H3):** Calibri bold, navy `#1F4E79`; H1 paragraphs get a full-width NAV background (navy fill + WHITE bold text) as a nav bar
- **Title:** navy `#1F4E79`, bold, large
- **Table header row:** WHITE text on navy `#1F4E79` background, bold
- **Label column (col 1, 2-col tables):** LBLUE `#D6E4F0` fill, bold navy text, snug width (~130pt fixed per `feedback_two_col_table_label_snug.md`)
- **Alternating body rows:** WHITE / LGRAY `#F5F5F5`
- **Borders:** DGRAY `#D0D0D0`
- **Page margins:** 45pt (~0.625")

**Fallback — Forest-green mod-guide style** (only if the researcher explicitly picks it in Step 3):
- DM Sans 10pt body · DM Serif Display 20/16/16pt headings in dark green `#2D4A3E` · dark-green table headers · dark-green bold label columns · col widths 115/350pt · light gray `#F6F7FA` alternating rows.

#### Styling pipeline (run in order after md2doc upload)

1. `md2doc upload-gdoc.py [file] --folder-id [project folder]` → creates the doc and applies the HTML import (style-gdoc-full pass for base structure)
2. **Default — Jedida Reporting (navy/blue):** `~/.claude/skills/jedida-reporting/scripts/apply_jedida_reporting.py [doc-id]` → runs 4 passes (sanitize → document margins → named styles → H1 nav bars → tables with snug label column). Promoted to default 2026-05-20.
3. **Fallback — Forest-green mod-guide style:** `~/.claude/skills/mod-guide/scripts/apply_canonical_template.py [doc-id]` → applies the locked canonical spec (page setup, DM Sans body / DM Serif Display headings, dark-green table headers, dark-green bold label cols, 0.5pt #C7C7C7 borders, 8pt cell padding, BULLET_DISC_CIRCLE_SQUARE, clears SUBSCRIPT runs, H2 non-bold + 36pt above / 12pt below). See `references/canonical-template-spec.md`.
4. **Custom — user-supplied reference doc:** `~/.claude/skills/mod-guide/scripts/apply_custom_template.py [target-doc-id] [ref-doc-id]` → extracts the ref doc's spec at runtime and applies the same phases.

> The legacy 3-pass pipeline (`style-gdoc-full` → `font_and_widths.py` → `rebold_col1.py`) is **superseded** by the consolidated single-script approach above. The old scripts are still present in `scripts/` for backward compatibility but should not be used by new flows.

All scripts use `uv run --python 3.12 --with google-api-python-client --with google-auth --with google-auth-oauthlib --with google-auth-httplib2 --with requests --with python-dotenv --with markdown --with pillow python [script]`.

---

### CONTENT GENERATION RULES

1. **No leading questions.** Every question open-ended, non-directional. Never assume the participant's opinion. (NN/g Rosala — 6 Mistakes)
2. **No interface terminology in tasks.** Describe goals, not UI ("find a way to…" not "click the button to…").
3. **Funnel technique.** Within each topic: broad → specific → closed. Broad first avoids priming (NN/g).
4. **Specific incidents over typical behavior.** "Tell me about the last time you…" beats "How often do you…" — closes the say-do gap (NN/g Critical Incident Technique).
5. **No hypotheticals except as projective tools.** "If this could change anything…" is fine at the end; "Would you use this?" is not (NN/g).
6. **No compound questions inside a single Ask cell.** If a question has 2-3 follow-ups that always go together (e.g. "What is it asking? What does '[word]' mean? How would you say this in your own words?"), they may share a cell. Otherwise split into Q + Q-follow-up rows.
7. **Probes named in PROSE above the table, not in-line in cells.** Use a single `Probes to use:` line per phase.
8. **Time-aware.** Allocate per study type (Step 2a). Core gets 70-80% of total.
9. **Participant-appropriate language.** Match vocabulary to the participant profile.
10. **Watch-fors and "don'ts" go in prose**, not in [Watch For] or [Moderator Note] table rows. Keep them above the question table they apply to.
11. **Capture-verbatim flags** (e.g. "Capture Q11 verbatim — feeds the survey wording") go in prose above the relevant table, not as a separate row.

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

## Step 5 — Upload + Style + Share (NO QUESTIONS — execute silently)

🚫 **Step 5 must run with zero `AskUserQuestion` calls.** The upload-yes/no question is gone. The styling-choice question is gone. The read-back confirmation is gone. The Step 3 answers contain everything needed; if a fact is missing, pick a sensible default and proceed.

Status update is fine (a one-line "Uploading… Applying [style]…" message is welcome). What's not fine: any question, any prompt, any "want me to…?" Treat Step 5 like a deterministic script.

Execution:
1. Upload via `gws-docs` (or md2doc `upload-gdoc.py`) to a sensible Drive location. If the input was a Google Doc, default to its parent folder; otherwise default to the matching project folder per CLAUDE.md (Project 1 / 2 / 3 / 4 / Research). **Do not ask which folder** — pick one and go.
2. Apply the styling chosen in Step 3:
   - **Default — Jedida Reporting (navy/blue):** Run `uv run --python 3.12 --with google-api-python-client --with google-auth --with google-auth-oauthlib --with google-auth-httplib2 --with requests --with python-dotenv python ~/.claude/skills/jedida-reporting/scripts/apply_jedida_reporting.py [doc-id]`. Applies the Jedida Reporting palette (navy NAV H1 nav bars, LBLUE label columns, alternating WHITE/LGRAY rows, DGRAY borders, Calibri throughout) via 4 passes: sanitize → document margins → named-style typography → H1 nav bars → table styling with snug label column. Promoted to default 2026-05-20.
   - **Fallback — Forest-green mod-guide style:** Run `scripts/apply_canonical_template.py [doc-id]`. This single script clears SUBSCRIPT runs, sets page size + margins, applies all run-level typography (headings, body, breadcrumb, "Last updated"), styles all 2-col tables (col widths 96/715.5pt, dark-green header with white bold, dark-green bold label col, #161416 content col, 0.5pt #C7C7C7 borders, 8pt padding all sides), sets H2 non-bold with 36pt above / 12pt below, sets NORMAL_TEXT 4pt spaceBelow + 115% lineSpacing, and applies BULLET_DISC_CIRCLE_SQUARE.
   - **Custom — user-supplied reference doc:** Run `scripts/apply_custom_template.py [target-doc-id] [ref-doc-id]`. Apply silently — no read-back, no confirmation prompt.
   - **Plain Google Docs:** Skip the styling script entirely.
3. Share the final Google Doc link in chat with a short summary of what's in the guide.
4. **Only after the link is shared** is the skill allowed to respond to follow-up questions or correction requests from the researcher.

---

## Tool Usage

- **AskUserQuestion** — present recommendations, gather approvals, ask for style reference.
- **google-docs:fetch-google-doc** / **Glean** (`mcp__glean_default__read_document`) — read PRDs, briefs, or style reference docs from Google Drive.
- **Read** tool or **download-gdoc.py** / **read-gdoc.py** — fallback readers for Google Docs.
- **gws-docs** or **md2doc** (`upload-gdoc.py`) — upload the final guide to Google Docs.
- **`~/.claude/skills/jedida-reporting/scripts/apply_jedida_reporting.py`** — **DEFAULT styler (promoted 2026-05-20).** Applies the Jedida Reporting navy/blue palette via 4 passes (sanitize → margins → named-style typography → H1 nav bars → tables with snug label column).
- **scripts/apply_canonical_template.py** — fallback forest-green mod-guide template (only when researcher explicitly picks it).
- **scripts/apply_custom_template.py** — extract styling from a user-supplied reference doc and apply it to the target.
- **references/canonical-template-spec.md** — human-readable spec for the forest-green fallback (mirrors the values in `apply_canonical_template.py`).
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
