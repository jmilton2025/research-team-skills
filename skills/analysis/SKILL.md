---
name: analysis
description: Use when a UX researcher has interview transcripts, session recordings, or open-ended survey responses and needs to synthesize findings via thematic analysis, tagging, or general affinity-based synthesis. Triggers on "analyze interviews", "thematic analysis", "tag transcripts", "synthesize research", or "/analysis".
---

# UX Research Analysis

> Invoke with `/analysis`

Synthesize qualitative research data (interview transcripts, session recordings, open-ended survey responses, diary entries) into rigorous, defensible findings using one of three methodologies: General Affinity Synthesis, Thematic Analysis (Braun & Clarke), or Tagging.

## Guiding Philosophy — H.E.A.R.T. (AIxUXR Playbook)

Per Instacart's AIxUXR Playbook, all AI-assisted analysis must be governed by H.E.A.R.T.:

| Letter | Principle | What this skill enforces |
|--------|-----------|--------------------------|
| **H** | **Human-centered** — prioritize the needs, context, and well-being of customers, shoppers, retailers, and colleagues | Every theme/cluster/tag is grounded in participant quotes; observations are separated from interpretation |
| **E** | **Experience-focused** — every interaction (researcher or participant) must be intuitive, respectful, positive | Structured outputs with clear visual hierarchy (2-column tables, RACI headers); no clunky AI-ese |
| **A** | **Amplifying** — AI augments researcher skill, it does not automate the job away | "Lead the dance" — the researcher remains the final authority on themes, insights, recommendations. AI handles repetitive extraction, clustering, formatting |
| **R** | **Responsible** — proactive ethics, privacy, bias mitigation | Zero PII policy; verify quotes against source; flag primacy bias and nuance deafness; surface contradictions |
| **T** | **Transparent** — attribute the assist; maintain participant/stakeholder trust | "Method notes" appendix documents AI's role; all outputs are drafts requiring rigorous human validation |

**The dance metaphor:** AI is a powerful but clumsy dance partner. It has no strategy, intuition, or soul. The researcher leads — setting the rhythm, guiding the steps, owning the final performance. If the AI leads, you get generic outputs and stepped-on toes.

**The golden rule (AIxUXR System Prompt):** If the output could end up in a research deliverable, treat AI as a specialized research engine — data-centric, objective, grounded. The researcher is always the final authority.

## When to use this skill

Use this skill when the researcher needs to:
- Move from raw qualitative data (5-30 transcripts, 50-500 survey opens) to structured findings
- Run a Braun & Clarke-style thematic analysis with defensible themes
- Apply a tagging schema across a transcript corpus (deductive, inductive, or hybrid)
- Produce a synthesis doc, theme report, or codebook for stakeholders

### When NOT to use this skill

- Large structured datasets with 50+ rows → use `/batch-analysis` (that skill is for scorecards, HITL reviews, pipeline audits — not qual synthesis)
- Moderating a session → use `/moderation-guide`
- Writing up findings as a stakeholder deliverable → use `/report`

## Three Modes

| Mode | Use When | Output |
|------|----------|--------|
| **General Affinity Synthesis** | Fast turnaround, smaller corpus (5-10 sessions), need to brief stakeholders on what was heard | Synthesis doc: clusters → observations → insights → recommendations |
| **Thematic Analysis** | Rigorous analysis, publishable quality, 10-30 interviews, theme development required | Theme report: themes, definitions, illustrative quotes, theoretical memos, prevalence |
| **Tagging** | Large corpus (30+ transcripts, or 200+ survey opens), need to count/filter, multi-coder team | Tagged transcript + codebook + tag frequency table |

---

## Step 1: Gather Inputs & Select Mode

Ask the researcher for inputs, then use **AskUserQuestion** to pick a mode.

### 1.1 Gather data

Ask what data is being analyzed:

> "Before we pick a methodology, tell me what you have:
> 1. **Data type** — interview transcripts, session notes, open-ended survey responses, diary entries, or a mix?
> 2. **Volume** — how many sessions/responses?
> 3. **Source** — local files, Google Drive, Dovetail/Dscout export, pasted text?
> 4. **Research question** — what were you trying to learn? (1-2 sentences)
> 5. **Stakeholder audience** — who is the output for? (engineer, PM, VP)"

Accept any format: pasted text, Google Doc URLs, local file paths, Dovetail/Dscout exports.

If Google Doc URLs are provided, read them via `google-docs:fetch-google-doc` or Glean (`mcp__glean_default__read_document`).

### 1.2 Select mode

Use **AskUserQuestion** with one question:

**Question — Which analysis mode?**

Options:
- **General Affinity Synthesis (Recommended for fast turnaround)** — "Cluster observations into patterns, extract insights, write recommendations. Best for 5-10 sessions, <1 week timeline."
- **Thematic Analysis (Braun & Clarke)** — "Rigorous 6-phase process producing defensible themes with illustrative quotes and theoretical memos. Best for 10-30 interviews, academic or high-stakes findings."
- **Tagging** — "Apply a tag schema (deductive, inductive, or hybrid) across a large corpus. Produces a codebook and frequency table. Best for 30+ transcripts or 200+ survey opens."

If the researcher is unsure, recommend based on volume: ≤10 sessions → General; 10-30 interviews → Thematic; 30+ or survey opens at scale → Tagging.

---

## Step 2: Propose Methodology

Branch based on the mode selected. Each branch proposes a concrete methodology tailored to the data, then presents it in a structured summary.

### Mode A: General Affinity Synthesis

**Methodology foundations:** NN/G affinity diagramming (Moran), synthesis ladder (Sharon), 1/3 prevalence rule (Anderson), AND the AIxUXR Playbook's **Transcript Summarizer** workflow (Loosbrock, Rothschild-Keita, Franicevic, Oct 2025) for session-level summarization patterns.

Propose:

| Parameter | Proposal | Why |
|-----------|----------|-----|
| **Unit of analysis** | [Quotes, observations, or behavioral moments from transcripts] | Per NN/G (Rosala), smallest meaningful unit is a single observation or verbatim quote |
| **Clustering approach** | [Bottom-up from observations → clusters → insights] | Affinity diagramming: Kate Moran at NN/G describes this as "collaboratively sort findings into themed groups" |
| **Insight ladder** | Notes → Observations → Insights → Recommendations | Sharon's synthesis ladder — each step increases abstraction; insights are interpretive claims, recommendations are actionable |
| **Prevalence rule** | [1/3 threshold: if ~33% of participants mention similar, it's a pattern] | Per Nikki Anderson (User Research Academy) |
| **Output format** | 2-column synthesis doc (Label \| Content) with cluster tables + insight/rec table | Matches Jedida's design system |

#### Session summarization patterns (AIxUXR Playbook — Transcript Summarizer)

When the General mode includes producing a **per-session summary** (not just cross-session synthesis), apply the Playbook's structured Session Summary template in addition to the cross-session affinity clusters:

| Section | What it contains | Why it matters |
|---------|------------------|----------------|
| **High-Level Summary** | 2-3 sentence overview: participant context, primary behavior/channel, single most significant challenge or unmet need | Defeats "blank page syndrome"; gives stakeholders the gist in one glance |
| **Key Quotes (2-3)** | Verbatim quotes with participant attribution + timestamp, e.g., `— Alex (00:08)`. Italicize quotes | Grounds summary in primary evidence; timestamps enable auditability |
| **Participant Context** | Relevant background (role, segment, constraints), assistive tech if applicable, domain familiarity | Readers without session access need this to calibrate the findings |
| **Key Insights & Highlights** | Bucket into 3 categories: (1) **Barriers** — things that prevent task completion, (2) **Usability Issues** — things that cause friction, (3) **Unmet Needs/Goals** — what users wish they could do | Per Playbook, this triage drives actionability — not all friction is equal |
| **Implications for Key Decisions** | Per-summary section: "Based on this participant's feedback, what is the single most important implication for [project X]?" Frame as direct input to a decision | Every summary must connect to a business/product decision, not just describe |
| **Executive Summary** | Copy High-Level Summary + Key Quotes + 3-4 Actionable Takeaways (decision-framed bullets) | Slack/email-ready; socializes findings to XFN partners |

#### Pre-summarization: Transcript Quality Audit (AIxUXR Playbook, Step 0)

Before running Mode A on a transcript corpus, verify transcript hygiene. Garbage in, garbage out.

| Issue | Action | Example |
|-------|--------|---------|
| **PII present** | Anonymize before processing. Replace names with pseudonyms like `[Participant Name]`; remove emails entirely | "John Smith at `00:02:15`" → "[Participant Name]" |
| **Inconsistent speaker labels** | Standardize to `Interviewer` / `Participant` or single consistent pseudonym | "Speaker 2" and "John" used interchangeably → normalize to "Participant" |
| **Unintelligible sections** | Listen to source audio to correct; if unfixable, leave explicit note `[Audio unclear at HH:MM]` | |
| **Noisy timestamps** | Optional — remove line-by-line timestamps if they confuse structure, but preserve quote-level timestamps for attribution | |

#### Bias flags to embed in every session summary

Per the AIxUXR Playbook, flag these explicitly in your Method Notes appendix:

| Bias | What to do |
|------|-----------|
| **Primacy bias** | Scan the full transcript — the AI over-emphasizes information from the beginning. Verify that themes from later sections aren't missed |
| **Nuance deafness** | AI cannot reliably detect sarcasm, humor, emotional undertones. If the session had notable affect (long pauses, sighs, laughter), the human researcher must add this context via `[Note: ...]` inline |
| **Hallucination risk** | Every quote must be verifiable in the source transcript. If paraphrasing, mark `[paraphrased]`. If you cannot find a quote, remove it |
| **Confidence labeling** | Per AIxUXR System Prompt, label confidence as **High / Medium / Low**. Low = data insufficient/contradictory/ambiguous — signal for more research or cautious treatment |

### Mode B: Thematic Analysis (Braun & Clarke 2022)

**Methodology foundations:** Braun & Clarke's reflexive TA (2022) — the gold-standard academic framework — supplemented by the AIxUXR Playbook's **AI-Assisted Thematic Analysis** workflow (Silverman, Venkatraman, Loosbrock, Oct 2025) for AI-specific execution patterns, codebook development, and insight-crafting. The Playbook complements Braun & Clarke; it does not replace the 6-phase rigor.

Propose:

| Parameter | Proposal | Why |
|-----------|----------|-----|
| **TA variant** | **Reflexive TA** (default) | Per Braun & Clarke 2022, reflexive TA treats themes as *constructed through researcher engagement*, not discovered. The alternatives (coding reliability TA, codebook TA) assume themes "exist" in data and are better for multi-coder teams requiring IRR. Use those only if requested. |
| **Orientation** | Inductive vs deductive (ask) | Inductive = codes emerge from data (grounded-theory style). Deductive = start with framework (e.g., JTBD, usability heuristics). Hybrid is common — start inductive, refine with framework |
| **Theme level** | Semantic vs latent (ask) | Semantic = surface-level, what participants explicitly say. Latent = interpretive, underlying assumptions/ideologies. Choose based on research question |
| **Theme type** | Fully-realized themes (patterns of shared meaning), NOT topic summaries | Per Braun & Clarke 2022: the #1 pitfall in reflexive TA is reporting topic summaries ("Participants talked about X") instead of patterns of shared meaning with a central organizing concept. Themes must tell an interpretive story |
| **Phases** | All 6: Familiarization → Coding → Generating initial themes → Reviewing themes → Defining & naming themes → Writing up | Per Braun & Clarke. Each phase has concrete deliverables — see `references/analysis-methodology.md` |
| **Output format** | Theme report: H2 per theme, 2-col table (Definition \| Illustrative quotes \| Memo \| Prevalence) | Matches Jedida's design system |

#### AI-Assisted Thematic Analysis workflow (AIxUXR Playbook)

The Playbook reimagines thematic analysis as a convergent, 5-step AI-assisted pipeline. Use this sequence INSIDE Braun & Clarke's 6 phases — it accelerates Phases 2-4 (coding, initial theme generation, theme review) while the researcher remains accountable for Phases 1, 5, and 6.

| Playbook Step | What it does | Maps to B&C Phase | Recommended model |
|---------------|--------------|-------------------|-------------------|
| **1. Generate Codebook** | Produce a deductive codebook from the RPP + discussion guide + pre-defined codes. Output: Category \| Code \| Definition \| Example | Informs Phase 2 (Coding) | Gemini 2.5 Pro (advanced reasoning) |
| **2. Process Structured Data** | Apply codebook to each anonymized transcript one-by-one, extract verbatim quotes into pipe-separated structured data: `Participant \| Segment \| Theme \| Quote`. Use a **"gold standard"** manually-coded transcript as a style anchor | Phase 2 (Coding) | Gemini 2.5 Pro |
| **3. (Optional) EOD Slack Summary** | Draft stakeholder-ready XFN update from top-of-mind takeaways | Informs Phase 6 (Writing) | Claude Opus 4.1 (writing) |
| **4a. Deductive Synthesis** | For each code in the codebook, analyze ALL tagged quotes together to extract granular sub-themes + segment patterns + recommendations | Phase 3 (Generating initial themes) | Gemini 2.5 Pro |
| **4b. Inductive Synthesis** | Cluster all quotes (including `Other`-tagged ones) into emergent cross-code themes. Finds patterns AMONG and BETWEEN the granular codes | Phase 3 + 4 (Generating & Reviewing themes) | Gemini 2.5 Pro |
| **5a. Craft Insight** | Transform each theme into an insight statement. Insight = **Truth + (Unmet) Need + Opportunity**. Single-sentence bold statement + 2-4 supporting points + 1-2 opportunity statements | Phase 5 (Defining & naming themes) | Claude Opus 4.1 |
| **5b. Craft Tagline** | Distill insight into 3+ headline options, 3-10 words, 80-100 chars, informative + intriguing | Phase 6 (Writing up) | GPT 4.1 (taglines) |
| **6. Devil's Advocate** | Systematic peer review against 7 quality criteria (see Self-Critique below) | Phase 4 (Reviewing themes) | Gemini 2.5 Pro |

#### Playbook coding heuristics

Per the AIxUXR Playbook's Prompt 2 (Individual Transcript Structured Data), the AI's extraction must follow these rules:

| Rule | Plain English |
|------|---------------|
| **Exhaustive extraction, not curation** | If a participant repeats the same idea three times, create three separate rows. Redundancy > missing evidence |
| **Capture the complete thought** | A multi-sentence explanation of one idea = one row. Don't fragment coherent thoughts |
| **Include moderator question for context** | If the participant's response is meaningless without the prompt, include the moderator's verbatim question in the row |
| **Handle uncoded themes** | If a meaningful quote doesn't fit the codebook, still capture it and tag as `Other`. These seed inductive (4b) synthesis |
| **Emulate the gold standard** | A manually-coded "golden" transcript from the same project guides style, granularity, and volume |
| **Structured data > raw transcripts at scale** | Playbook learning: synthesizing from pipe-separated quotes is "far more reliable, token-efficient, and powerful" than re-feeding raw transcripts each pass |

#### Theme-granularity heuristic (Playbook Prompt 4a)

The Playbook warns against over-aggregation. Prefer SPECIFIC themes over few BROAD ones:

- ❌ Broad (avoid): one theme called "Navigation Issues"
- ✅ Specific (prefer): three themes — "Unreadable Aisle Signage" / "Unpredictable Store Layouts" / "Physical Obstructions in Aisles"

This aligns with Braun & Clarke's "central organizing concept" test — each theme must express a distinct pattern of shared meaning.

#### Theme-validation checks (Playbook Prompt 6 "Devil's Advocate" — 7 criteria)

Before finalizing themes/insights, run the Playbook's structured critique. Grade each (A / A- / B+ etc.) with justification:

| # | Criterion | Check |
|---|-----------|-------|
| 1 | **Novelty** | Is the insight net-new, non-obvious, surprising? Compare against past research |
| 2 | **Actionability** | Clear XFN-friendly implication? |
| 3 | **Memorability** | Punchy, memorable headline/tagline? |
| 4 | **Rationale** | Clear "back-pocket" reason why this matters to the business? |
| 5 | **Simplicity** | Communicated in the simplest way without losing nuance? |
| 6 | **Language safety** | XFN-friendly, research-lead-friendly, avoids alarmist/dissonant terms and sensitive terminology? |
| 7 | **Methodological soundness** | Framed as a true insight, not just a finding? Passes the **Truth + (Unmet) Need + Opportunity** test? |

**Critical caveat (Playbook):** The AI is "nuance-deaf" and subject to **primacy bias** (over-weighting early transcript content). After AI-assisted theme generation, the researcher must manually scan for outlier themes and use the Devil's Advocate prompt to challenge findings.

Critical caveat to state explicitly:

> "Per Braun & Clarke 2022, reflexive TA rejects the language of themes 'emerging' from data — themes are **constructed** through your engagement. I will use language like 'I developed the theme...' or 'The theme was generated from...' rather than 'The theme emerged.' This is methodological, not stylistic."

### Mode C: Tagging

**Methodology foundations:** Dscout/NN/G tagging practice (Anderson, Eisenhauer), Cohen's κ for IRR, AND the AIxUXR Playbook's **AI-Assisted Open-Ends Analyzer** workflow (Mamyan, Zheng) for survey open-end coding at scale — especially codebook construction, disambiguation rules, and human-in-the-loop validation.

Propose:

| Parameter | Proposal | Why |
|-----------|----------|-----|
| **Tag approach** | Deductive, Inductive, or Hybrid (ask) | Deductive: schema designed up front (faster, needs domain framework). Inductive: tags grow from data (slower, more exploratory). Hybrid: start with seed tags, let new ones emerge. Per Dscout/Nikki Anderson, hybrid is most common in practice |
| **Tag hierarchy** | Parent → child (e.g., `friction > pricing > sticker-shock`) | Recommended when corpus is 200+ items. Flat tag lists become unwieldy at scale |
| **Tag types** | Descriptive (what was said) + Analytical (what it means) | Per Dscout: start with descriptive to stay close to participant language, then layer analytical codes once patterns are visible |
| **Codebook** | Tag name, definition, inclusion criteria, exclusion criteria, example quote | This is the single most important artifact for multi-coder consistency |
| **IRR (inter-rater reliability)** | Ask: single coder or multi-coder? If multi, compute Cohen's κ on 10-20% double-coded sample, target κ ≥ 0.70 | Only matters for multi-coder projects. See `references/analysis-methodology.md` |
| **Output format** | Tagged corpus + codebook (2-col table) + frequency table | Frequency table surfaces prevalence for stakeholder briefings |

#### Open-Ends Analyzer workflow (AIxUXR Playbook, 4 steps)

For survey open-ends specifically, follow the Playbook's Open-Ends Analyzer pipeline. Each step has a clear human-vs-AI role:

| Step | Human Role ("Driver") | AI Role ("Co-Pilot") | Output |
|------|----------------------|----------------------|--------|
| **1. Prepare & Anonymize** | Strip PII (names, emails, identifying details), consolidate into a single clean document | N/A | Clean, anonymized dataset |
| **2. Generate Initial Thematic Clusters** | Craft precise prompt from approved blueprint; feed prepared data | Analyze text, identify 5-7 thematic clusters with supporting quotes | Structured tag list + associated quotes |
| **3. Validate, Refine & Synthesize** *(critical HITL)* | Apply expert judgment to merge/split/rename/discard tags; verify all quotes against source; look for what AI missed; counter confirmation bias by asking "what's missing?" before "is this right?" | N/A — AI's job is done for this step | Final human-validated codebook + tagged excerpts |
| **4. Create Summary for Reporting** *(optional)* | Prompt AI to summarize the human-validated themes into a reporting format | Reformat and summarize refined themes | Draft summary paragraph or bulleted list |

**Playbook guardrail:** Only use themes you have personally validated in Step 3. Never ship AI output directly to stakeholders without human-in-the-loop review.

#### Codebook construction rules (AIxUXR Open-Ends Playbook)

When the AI generates tags, enforce these three rules on the codebook:

| Rule | Definition | Example |
|------|------------|---------|
| **Granularity** | Specific enough to be actionable, broad enough to capture multiple related comments. Avoid tags that are too similar or overlap significantly | ❌ `Bad experience` (too broad) → ✅ `Shopper refunding instead of substituting` (specific, actionable) |
| **Mutual exclusivity** | Strive to make tags as MECE as possible. If a response could fit two tags, choose the **primary** (most prominent) one | A response about "wrong item + late delivery" should be coded for the PRIMARY frustration, not both |
| **Actionability** | Prioritize tags that represent distinct customer pain points (not catch-alls) | `Vague` is a legitimate tag for low-confidence responses — use it honestly rather than force-fitting |

#### Disambiguation rules (Playbook Prompts 1 & 2)

Use a **seed set of hand-coded examples** to anchor the AI's tagging logic. The Playbook provides this pattern:

```
Response → Code
"none" → None
"The zip code changes before I place the order" → Zip code changing inconsistently
"Driver don't match profile picture" → Driver identity
"It takes time to add a new address" → Address management usability
```

Feeding the AI 10-20 correctly-coded examples first dramatically improves consistency. This is a **one-shot / few-shot** prompting pattern.

#### Edge-case handling

| Edge case | How to handle |
|-----------|---------------|
| **Null/dismissive responses** (`None`, `N/A`, `nothing much`) | Tag with a dedicated `None` code. Do NOT treat as "no data" — the prevalence of null responses is itself informative |
| **Multi-code responses** | Each user can have multiple codes if multiple challenges are described, but each distinct challenge corresponds to one code. Use binary (1/blank) marker columns for spreadsheet-friendly output |
| **Low-confidence responses** | Tag as `Vague` rather than force-fitting. Report the `Vague` frequency as a data-quality signal |
| **Uncoded themes** (don't fit existing codebook) | Tag as `Other` and flag for human review. These feed the inductive pass |
| **Consistent sentiment** (per Playbook scope) | Open-Ends Analyzer works best on questions expected to have consistent sentiment (e.g., a "challenges" question expected to be negative). Mixed-sentiment opens may need sentiment tagging as a separate axis |

#### Reliability checks

For tagging at scale, layer these on top of standard IRR (Cohen's κ):

| Check | How |
|-------|-----|
| **Golden set validation** | Hand-code 10-20% of the corpus first; compare AI output against the gold set. Target ≥ 80% agreement |
| **Disagreement reconciliation** | Where coder disagreements arise, document WHY (ambiguity, tag overlap, participant phrasing) and refine inclusion/exclusion criteria in the codebook |
| **Tag-evolution log** | For inductive/hybrid runs, log every tag added, merged, dropped during analysis. This is an auditable artifact |
| **Primacy-bias scan** | Per AIxUXR guidance: AI over-weights early responses. Sample from the middle and end of the corpus to verify coverage |
| **Hallucination spot-check** | Verify 10% of tagged quotes against source — did the AI misattribute or invent any? |

---

## Step 3: Researcher Reviews & Approves

Present the proposed methodology as a structured summary. Then use **AskUserQuestion** to confirm in batches of up to 4 questions.

### Batch 1 — Methodology approval

**Question 1 — Methodology**
- Options: "Approve as proposed" (Recommended), "Adjust one parameter", "Start over with a different mode"

**Question 2 — Orientation** (if Thematic or Tagging)
- Options: Inductive, Deductive, Hybrid (with Claude's recommendation marked)

**Question 3 — Theme level** (if Thematic only)
- Options: Semantic (surface-level), Latent (interpretive), Both

**Question 4 — IRR** (if Tagging + multi-coder)
- Options: Single coder (no IRR), Multi-coder with Cohen's κ, Multi-coder with % agreement only

### Batch 2 — Scope and format (if needed)

**Question 5 — Scope**
- Options: "Analyze all data" (Recommended), "Sample N transcripts first", "Pilot with 2-3 then review"

**Question 6 — Final check**
- Options: "Looks good, let's pick a style!" (Recommended), "I want to adjust the output format", "I want to add more context"

---

## Step 3.5: Style Reference (REQUIRED before generating)

After methodology is approved, ask for an output style reference. Use **AskUserQuestion**:

**Question — Output Style**

> "One last thing before I generate your analysis — I want to make sure the output matches your preferred style and format."

Options:
- **"I'll share a reference doc"** — "I have a previous synthesis doc, theme report, or codebook I'd like you to match."
- **"Use the default Instacart template" (Recommended)** — "Use the standard 2-column layout with section bars, RACI header, and structured tables."
- **"Just give me a clean outline"** — "Simple headers and bullets, no tables or heavy formatting."

**If the researcher shares a reference doc:**

1. Accept any format: Google Doc URL, pasted text, uploaded file, or screenshot
2. If Google Doc URL: read via `google-docs:fetch-google-doc` or Glean
3. Analyze the reference doc's style patterns. Extract:
   - **Document structure:** section ordering, header hierarchy, table usage
   - **Theme/cluster/tag presentation:** how are themes/tags introduced? (H2 per theme, table row per theme, numbered list)
   - **Quote formatting:** block quotes, italicized inline, labeled with participant ID
   - **Prevalence reporting:** percentages, N of N, "most participants", qualitative language
   - **Memo/rationale style:** inline, separate section, moderator-note-style callouts
4. Confirm the style read-back with the researcher:

   > "Here's what I picked up from your reference doc:
   > - **Structure:** [e.g., One H2 per theme with 2-col table inside]
   > - **Quotes:** [e.g., Italicized block quotes with `— P07` attribution]
   > - **Prevalence:** [e.g., 'X of Y participants' + qualitative band]
   > - **Memos:** [e.g., Inline under 'Interpretation' label]
   >
   > Does that capture your style? Anything to adjust?"

5. Generate the output matching their style.

**If the researcher picks the default template:**
- Use the appropriate OUTPUT TEMPLATE below (one per mode)

**If the researcher picks "clean outline":**
- Use simple markdown: H2 per theme/cluster/tag, bullet lists, blockquote quotes. No tables.

---

## Step 4: Execute Analysis

Generate the analysis based on mode + approved methodology + chosen style.

**Methodology reference:** For detailed execution of each mode, load `references/analysis-methodology.md`:
- Braun & Clarke's 6-phase walkthrough with worked example
- Tag schema patterns and hierarchy design
- Inter-rater reliability (Cohen's κ) formula and interpretation
- Theme vs topic summary pitfall with corrected examples
- Ladder of inference for General Synthesis

### Execution principles (all modes)

1. **Ground every claim in data.** Every theme, cluster, or tag gets at least 2-3 illustrative quotes with participant attribution (e.g., `— P07`).
2. **Report prevalence honestly.** Use "X of Y participants" format. Avoid "most" or "many" without a number. Per Anderson, use ~1/3 as the pattern threshold.
3. **Separate observation from interpretation.** A quote is an observation; the theme definition is interpretation. Never conflate.
4. **Use reflexive language** (Thematic mode): "I developed..." not "The theme emerged...". Per Braun & Clarke 2022.
5. **Avoid topic summaries** (Thematic mode): "Participants talked about pricing" is a topic, not a theme. A theme has a central organizing concept: "Pricing transparency builds trust — hidden fees feel like betrayal."
6. **Do not fabricate quotes.** If a quote is paraphrased, mark it clearly: `[paraphrased]`.

---

#### OUTPUT TEMPLATE — Mode A: General Affinity Synthesis

```
*UX Research | Synthesis | [Quarter Year]*

# [Study Title] — Synthesis

Last updated: [Month Year]

- **Responsible:** [Researcher name] (UX Researcher)
- **Consulted:** [Names with roles]
- **Informed:** [Names with roles]

| Parameter | Detail |
|-----------|--------|
| **Data** | [N sessions / N transcripts / N survey responses] |
| **Method** | General Affinity Synthesis |
| **Research question** | [1-2 sentence RQ] |
| **Analysis window** | [Dates] |

## Executive Summary

| Label | Detail |
|-------|--------|
| **Top insight** | [1 sentence — the single most important finding] |
| **Top recommendation** | [1 sentence — the single most actionable ask] |
| **Confidence** | [High / Medium / Low + rationale based on sample + pattern strength] |

## Clusters

### Cluster 1: [Cluster name]

| Label | Detail |
|-------|--------|
| **Description** | [2-3 sentence description of what this cluster captures] |
| **Prevalence** | [X of Y participants — ~Z%] |
| **Illustrative quotes** | *"[Quote 1]"*<br><br>— P04<br><br>*"[Quote 2]"*<br><br>— P11<br><br>*"[Quote 3]"*<br><br>— P17 |
| **Observation** | [Factual summary of what was heard — close to participant language] |
| **Insight** | [Interpretive claim — what this MEANS, not just what was said] |
| **Recommendation** | [Actionable ask — who does what, by when, measured how] |

[Repeat per cluster — typically 4-7 clusters]

## Insight → Recommendation Map

| Insight | Recommendation | Owner | Effort | Priority |
|---------|----------------|-------|--------|----------|
| [Insight 1] | [Rec 1] | [Name/team] | S/M/L | P0/P1/P2 |
| [Insight 2] | [Rec 2] | [Name/team] | S/M/L | P0/P1/P2 |

## Appendix

| Label | Detail |
|-------|--------|
| **Participants** | [P01-P08 profile table] |
| **Method notes** | [Coding approach, prevalence rule, analyst(s), analysis dates] |
| **Limitations** | [Sample size, selection bias, temporal scope] |
```

---

#### OUTPUT TEMPLATE — Mode B: Thematic Analysis (Braun & Clarke)

```
*UX Research | Thematic Analysis | [Quarter Year]*

# [Study Title] — Theme Report

Last updated: [Month Year]

- **Responsible:** [Researcher name] (UX Researcher)
- **Consulted:** [Names with roles]
- **Informed:** [Names with roles]

| Parameter | Detail |
|-----------|--------|
| **Data** | [N interviews / N hours of transcript] |
| **Method** | Reflexive Thematic Analysis (Braun & Clarke, 2022) |
| **Orientation** | [Inductive / Deductive / Hybrid] |
| **Theme level** | [Semantic / Latent / Both] |
| **Research question** | [1-2 sentence RQ] |

## Researcher Reflexivity Statement

| Label | Detail |
|-------|--------|
| **Analyst** | [Name, role, relevant context] |
| **Positionality** | [2-3 sentences: what perspectives, assumptions, or domain familiarity you bring to the data. Per Braun & Clarke, subjectivity is a resource, not a bias to eliminate] |
| **Theoretical framework** | [If deductive: what framework guided coding. If inductive: state "none a priori"] |

## Theme Overview

| Theme | Central Concept | Prevalence |
|-------|-----------------|------------|
| 1. [Theme name] | [1-sentence central organizing concept] | [N of N] |
| 2. [Theme name] | [1-sentence central organizing concept] | [N of N] |
| 3. [Theme name] | [1-sentence central organizing concept] | [N of N] |

## Theme 1: [Theme Name]

| Label | Detail |
|-------|--------|
| **Definition** | [Central organizing concept — NOT a topic summary. Must express a pattern of shared meaning. Example: "Trust is built through pricing transparency — hidden fees feel like betrayal, not inconvenience"] |
| **Prevalence** | [X of Y participants — Z%] |
| **Illustrative quotes** | *"[Quote 1 — best single expression of the theme]"*<br><br>— P04<br><br>*"[Quote 2 — shows a different facet]"*<br><br>— P11<br><br>*"[Quote 3 — shows boundary or contrast]"*<br><br>— P17 |
| **Sub-themes** | - **[Sub-theme 1]:** [1-sentence description]<br><br>- **[Sub-theme 2]:** [1-sentence description] |
| **Theoretical memo** | [2-4 sentences: how I constructed this theme, what codes fed into it, what was considered and rejected. Use reflexive language: "I developed this theme from codes X, Y, Z..." NOT "This theme emerged..."] |
| **Contradictions / boundary cases** | [Any participants or quotes that complicate or contradict the theme. Name them explicitly — per Braun & Clarke, honoring complexity is a rigor criterion] |

[Repeat per theme — typically 3-6 themes. More than 6 often signals topic summaries.]

## Theme Relationships

| Label | Detail |
|-------|--------|
| **Narrative** | [2-3 paragraphs: how do the themes relate? Do they form a story? Are they parallel or hierarchical?] |
| **Thematic map** | [Optional: a text-based diagram or description of theme relationships] |

## Recommendations

| Recommendation | Grounding Theme | Owner | Priority |
|----------------|-----------------|-------|----------|
| [Rec 1] | Theme X | [Name/team] | P0/P1/P2 |

## Appendix

| Label | Detail |
|-------|--------|
| **Codebook** | [Link or inline: code name, definition, example quote per code] |
| **Coding process** | [Tool used, analyst(s), coding passes, timeline] |
| **Trustworthiness** | [Per Lincoln & Guba: credibility, transferability, dependability, confirmability — how addressed] |
| **Limitations** | [Sample scope, analyst positionality limits, what this analysis cannot tell us] |
```

---

#### OUTPUT TEMPLATE — Mode C: Tagging

```
*UX Research | Tagged Corpus | [Quarter Year]*

# [Study Title] — Codebook & Tag Report

Last updated: [Month Year]

- **Responsible:** [Researcher name] (UX Researcher)
- **Consulted:** [Names with roles]
- **Informed:** [Names with roles]

| Parameter | Detail |
|-----------|--------|
| **Data** | [N transcripts / N survey responses — total excerpts tagged: N] |
| **Method** | Tagging ([Deductive / Inductive / Hybrid]) |
| **Coders** | [N analysts — names] |
| **IRR (if multi-coder)** | Cohen's κ = [X] on [N]% double-coded sample (target ≥ 0.70) |

## Codebook

| Tag | Parent | Definition | Inclusion criteria | Exclusion criteria | Example quote |
|-----|--------|------------|-------------------|-------------------|---------------|
| `pricing.sticker-shock` | `friction` | Strong negative reaction to displayed price before considering value | Reaction expressed at moment of seeing price; strong affect | Complaints about billing errors; post-purchase regret | *"I saw the total and just closed the tab."* — P07 |
| `trust.transparency` | `trust` | Positive response to clear disclosure of fees/process | Explicit appreciation of clear pricing/disclosure | General satisfaction with product | *"They showed me every fee up front — I actually trusted them."* — P12 |

[Repeat per tag — organize by parent tag. Typical corpus has 15-40 tags.]

## Tag Frequency

| Tag | Count | % of excerpts | % of participants | Priority |
|-----|-------|--------------|-------------------|----------|
| `friction.pricing.sticker-shock` | 23 | 18% | 71% (10/14) | P0 |
| `trust.transparency` | 17 | 13% | 64% (9/14) | P1 |

## Tag Co-Occurrence (Optional)

| Tag A | Tag B | Co-occurrence count | Interpretation |
|-------|-------|---------------------|----------------|
| `friction.pricing.sticker-shock` | `trust.transparency` | 11 | Strong: transparency consistently named as antidote to sticker shock |

## Key Patterns

| Label | Detail |
|-------|--------|
| **Top friction tags** | [Top 3 friction tags by participant prevalence] |
| **Top positive tags** | [Top 3 positive tags by participant prevalence] |
| **Surprising tags** | [Tags that appeared unexpectedly or broke the schema] |
| **Cold tags** | [Tags in original schema with 0-2 hits — candidates to drop or merge] |

## Appendix

| Label | Detail |
|-------|--------|
| **Tag evolution** | [If inductive/hybrid: tags added, merged, dropped during analysis] |
| **IRR details** | [Kappa formula, double-coded sample size, disagreements reconciliation] |
| **Tool** | [Dovetail / Dscout / Airtable / Google Sheet — link] |
| **Limitations** | [What the tag frequencies do and do not tell us] |
```

---

### CONTENT GENERATION RULES (all modes)

1. **Quote authenticity** — Use verbatim quotes when possible. Mark paraphrases as `[paraphrased]`. Never invent a quote.
2. **Participant attribution** — Every quote gets a participant ID (`— P07`). If anonymization requires, use role-based IDs (`— Shopper-A`).
3. **Prevalence precision** — Report "X of Y participants" or exact percentages. Avoid "most" or "some" alone.
4. **Insight vs observation** — Observations describe what was heard. Insights interpret what it means. Recommendations propose what to do. Never skip the ladder.
5. **Reflexive language (Thematic mode)** — Use "I developed...", "I constructed...", "I generated..." — never "The theme emerged..." Per Braun & Clarke 2022.
6. **Theme tests (Thematic mode)** — Each proposed theme must pass 3 tests: (1) central organizing concept expressible in 1 sentence, (2) supported by quotes from 2+ participants, (3) coherent across its supporting codes. If any fails, it's likely a topic summary — demote to sub-theme or drop.
7. **Tag discipline (Tagging mode)** — Every tag has a definition, inclusion criteria, exclusion criteria, and example. If you can't write inclusion/exclusion, the tag is too vague.
8. **Contradictions** — Actively seek and report quotes that complicate your synthesis. Per NN/G, credibility requires acknowledging disconfirming evidence.

---

## Step 4.5: Playbook-Specific Self-Critique (MANDATORY before delivery)

Before presenting the analysis to the researcher, run the AIxUXR Playbook's Devil's Advocate critique on your own output. This is the internal QA gate — a systematic pass against methodological, evidentiary, and communicative criteria. It is not optional. Per the AIxUXR System Prompt, the AI must label confidence (High / Medium / Low) and flag any findings it cannot support.

### Analysis-output self-critique checklist

Run through every item. For each, grade (A / A- / B+ / B / below-B) and justify briefly. If any item grades below A, revise before delivering.

| # | Check | Question | Fail signal |
|---|-------|----------|-------------|
| 1 | **Theme/cluster/tag exhaustiveness** | Have I captured every distinct idea in the data, or am I summarizing to the top N most obvious ones? | Participant quotes in the raw data don't map to any theme/cluster/tag. Primacy bias (early-transcript over-weighting). Cold tags in original schema with 0-2 hits haven't been flagged |
| 2 | **Quote representativeness** | Do the illustrative quotes span the range of the theme, including boundary cases? Are they drawn from multiple participants (not all from P04)? | All 3 quotes for a theme are from one participant. All quotes express the strongest version — no softer or ambivalent voices |
| 3 | **Bias flagged** | Have I explicitly surfaced primacy bias, nuance deafness, hallucination risk, and sample/selection bias in Method Notes? | Limitations section missing. No mention that AI was used. No confidence label on key findings |
| 4 | **Participant attribution correct** | Does every quote trace back to the correct participant in the source? Are pseudonyms consistent? Are timestamps accurate where cited? | Attribution mismatches source. "Participant 7" and "P07" used inconsistently. Timestamps not verified |
| 5 | **Hallucination scan** | Are all quotes verifiable in the source transcripts? No invented quotes, plausible-sounding but fabricated details, or hallucinated codes? | Any quote that cannot be found by text-search in the source. Any factual claim about participants not in the data |
| 6 | **Observation vs. interpretation separated** | Are observations (what was heard) visually/structurally distinct from insights (what it means) and recommendations (what to do)? | "Participants struggled with checkout" appears in the Insight column (that's an observation). Recommendations buried inside quote interpretation |
| 7 | **Thematic-mode only — Topic-summary pitfall** | Does each theme express a central organizing concept (a pattern of shared meaning), NOT just a topic label? | Theme titled "Pricing" (topic). Rename to "Hidden fees feel like betrayal, not inconvenience" (pattern of shared meaning) |
| 8 | **Tagging-mode only — Codebook rigor** | Does every tag have definition + inclusion + exclusion + example? Are tags MECE as much as possible? | Tag exists without inclusion/exclusion criteria. Two tags overlap semantically |
| 9 | **Confidence labeled** | Is each major finding labeled High / Medium / Low confidence with rationale? | Unlabeled claims. Over-confident language ("clearly", "obviously") without data to back it |
| 10 | **H.E.A.R.T. honored** | Human-centered (grounded in participant voice)? Experience-focused (scannable, clear)? Amplifying (researcher remains the final authority)? Responsible (PII scrubbed, bias flagged)? Transparent (AI role attributed)? | Any H.E.A.R.T. dimension missing — block delivery until addressed |

### If any critique item grades below A

1. Revise the specific section before delivering.
2. If revision isn't possible (e.g., evidence genuinely thin), explicitly state the limitation in Method Notes and lower the confidence label.
3. If the researcher asks for delivery anyway, honor the request but include a **Critique Summary** section at the top of the output flagging unresolved issues.

### Surface the critique in the output

Per H.E.A.R.T. Transparency, include a brief **Self-Critique Summary** section in the Appendix of every analysis output (a 2-col table: Check | Grade + Note). This gives the researcher a running QA signal and models responsible AI practice for stakeholders.

---

## Step 5: Offer Google Docs Upload

After generating the analysis, ask:

> "Your analysis is ready! Would you like me to upload it to Google Docs?"

If yes:
1. Upload via `gws-docs` or `md2doc` (upload-gdoc.py)
2. **Fix subscript formatting (MANDATORY)** — md2doc's `<br>` handling creates SUBSCRIPT formatting that makes text tiny. After upload, scan the doc via Google Docs API for all `baselineOffset == 'SUBSCRIPT'` ranges and reset them to `'NONE'`. Do this BEFORE styling.
3. If using the default Instacart template: apply styling via `style-gdoc-full.py`
4. Place in the correct Google Drive project folder per Jedida's CLAUDE.md auto-categorization rule (Project 1, 2, 3, or Research/)
5. Share the Google Doc link

---

## Tool usage

- **AskUserQuestion** — mode selection, methodology approvals, style reference, final checks
- **google-docs:fetch-google-doc** or **mcp__glean_default__read_document** — reading Google Doc inputs (transcripts, reference docs)
- **Read tool** — reading local transcript files
- **gws-docs / md2doc** — uploading final analysis to Google Docs
- **style-gdoc-full.py** — applying Instacart design system to uploaded doc
- **references/analysis-methodology.md** — load on demand for Braun & Clarke 6-phase walkthrough, tag schema patterns, IRR calculation

## Complementary skills

| Skill | Relationship |
|-------|--------------|
| `/batch-analysis` | **Complementary, not overlapping.** Use `/batch-analysis` for 50+ row structured datasets (scorecards, HITL reviews). Use `/analysis` for qualitative synthesis from transcripts/opens. If a study has both, run `/batch-analysis` on the structured data and `/analysis` on the qual portion |
| `/moderation-guide` | Upstream — generates the session guide whose transcripts feed `/analysis` |
| `/report` | Downstream — takes `/analysis` output and packages as stakeholder deliverable |
| `/research-plan` | Upstream — defines the research question that `/analysis` answers |

## Sources cited in this skill

### Academic & industry foundations

- **Braun, V., & Clarke, V. (2022).** *Thematic Analysis: A Practical Guide.* Sage. [thematicanalysis.net](https://www.thematicanalysis.net/)
- **Braun & Clarke (2022)** "Toward good practice in thematic analysis" — the topic-summary pitfall
- **Rosala, M. (NN/G)** "How to Analyze Qualitative Data from UX Research: Thematic Analysis" [nngroup.com/articles/thematic-analysis](https://www.nngroup.com/articles/thematic-analysis/)
- **Moran, K. (NN/G)** "Affinity Diagramming" [nngroup.com/articles/affinity-diagram](https://www.nngroup.com/articles/affinity-diagram/)
- **Budiu, R. (NN/G)** "Data Is More than Numbers: Why Qualitative Data Isn't Just Opinions" — rigor criteria
- **Anderson, N. (User Research Academy / Dscout)** — coding/tagging workflow, global tags framework, 1/3 prevalence rule
- **Eisenhauer, K. (Dscout)** — three tagging approaches (organizational, descriptive, thematic)
- **Young, I.** "Listening Deeply" — emergent affinity technique via mental attention focus
- **Sharon, T.** *Validating Product Ideas* — synthesis ladder (notes → observations → insights → recommendations)

### Instacart AIxUXR Playbook (internal)

- **Loosbrock, K.** "Playbook: The AI Research Engine System Prompt" (Sep 30, 2025) — core persona, H.E.A.R.T. philosophy, operating principles (objectivity, data-centric grounding, substance, efficiency), default 5-part report structure, analytical toolbox (thematic, sentiment, JTBD, quantitative summary, lit review)
- **Loosbrock, K., Venkatraman, S.** "AIxUXR Playbook" (Sep 30, 2025) — H.E.A.R.T. framework (Human-centered, Experience-focused, Amplifying, Responsible, Transparent); the dance metaphor for human–AI collaboration; Hub & Spoke model
- **Silverman, M., Venkatraman, S., Loosbrock, K.** "AI-Assisted Thematic Analysis of Interview Transcripts & Insights Framing" (Oct 31, 2025) — 5-step workflow (Codebook → Structured Data → Synthesis → Insights → QA), granularity heuristic, Devil's Advocate 7-point critique, Truth + Unmet Need + Opportunity insight framework
- **Loosbrock, K., Rothschild-Keita, A., Franicevic, L.** "AI-Assisted Transcript Summaries" (Oct 9, 2025) — Transcript Quality Audit (Step 0), Session Summary / Executive Summary templates, Barriers / Usability Issues / Unmet Needs triage, Implications-for-Decisions section, Responsible AI principles mapping
- **Mamyan, M., Zheng, X.** "AI-Assisted Open-Ends Analyzer" — 4-step Open-Ends workflow (Prepare → Cluster → Validate → Summarize), codebook construction rules (granularity, mutual exclusivity, actionability), seed-set / few-shot coding pattern, edge-case handling for null and vague responses
