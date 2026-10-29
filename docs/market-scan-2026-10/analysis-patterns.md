# Patterns: reusable ideas for an `analysis` skill

Each item gives the idea, a short verbatim excerpt (≤5 lines), and its source. Items marked **★** do not appear in the current `skills/analysis/SKILL.md`. I read only that SKILL.md, not its `references/`, so a ★ item may already be in `quality-gates.md` or `analysis-methodology.md`. Unmarked items overlap with what the skill already does and are listed for completeness or as alternative wording.

---

## 1. Data intake and cleaning

**1.1 ★ Exclude moderator speech before coding, and check for it afterward.** In a blinded study, the largest LLM error source was coding facilitator turns as participant evidence, even when speakers were clearly labelled. The strict hallucination rate was 1.2% but the comprehensive error rate was 12.4%. Add a QA check that no evidence ID points to a moderator turn, unless it is explicitly tagged as elicitation context.
> "performance declined in speaker delineation ... despite researcher speech segments being clearly labelled in the transcript ... the comprehensive error rate of 12.4% was considerably higher ... arose largely from the LLMs coding facilitator speech segments"
Source: https://www.medrxiv.org/content/10.64898/2025.12.25.25343031.full.pdf

**1.2 ★ Transcript cleaning must not over-edit.** Normalize speaker labels and fix obvious transcription errors. Keep emotional cues (laughter, sighs, pauses) and keep quotes verbatim.
> "Handles overlapping speech and preserves emotional cues (laughter, sighs, pauses) ... Without the skill, Claude 'tends to over-edit.'"
Source: https://www.greatquestion.com/blog/claude-skills-ux-research-assistant

**1.3 Orthographic verbatim is enough for thematic analysis. Spot-check transcripts you didn't make.**
> "a rigorous orthographic verbatim transcript is sufficient ... non-verbal utterances where they carry meaning ... If transcripts were prepared by someone else, the analyst should still spot-check against the audio."
Source: https://github.com/brycewang-stanford/auto-empirical-research-skills/blob/HEAD/skills/53-keemanxp-thematic-analysis-skill/thematic-analysis/references/quality-checklist.md

**1.4 ★ Record which transcript version and which prompt or settings produced the output (audit trail).**
> "Record which transcript version the AI used. Keep a QA log of changes, especially quote edits. Save the prompt and settings used to generate the output."
Source: https://gotranscript.com/en/blog/ai-qual-research-qa-checklist-prevent-hallucinations-misattribution

**1.5 ★ For multi-source feedback, normalize to one row per item: source, date, segment, verbatim, sentiment.**
> "Each piece of feedback becomes a row with source, date, customer segment, verbatim quote, and sentiment."
Source: https://github.com/shawnpang/startup-founder-skills/blob/HEAD/skills/feedback-synthesis/SKILL.md

---

## 2. Per-session notes (n=1 and the first pass of multi-session work)

**2.1 ★ Write a familiarization note per data item before any coding, and save it as an artifact.**
> "Output of this phase: a familiarisation note for the user — a paragraph per data item summarising what struck you, plus a running list of initial ideas across the data set. Save this to the workspace as `phase2_familiarisation.md`."
Source: https://github.com/brycewang-stanford/auto-empirical-research-skills/blob/HEAD/skills/53-keemanxp-thematic-analysis-skill/thematic-analysis/SKILL.md

**2.2 Read end-to-end first, then tag on a second pass. Never tag from memory.**
> "Read the artifact end-to-end before tagging. Tagging while reading on first pass produces fragmentary tags."
> "Tagging by memory, not by reading ... Loses specifics; produces general tags that cluster poorly."
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/discovery-research-synthesis/references/tagging-and-clustering-discipline.md

**2.3 ★ Per-session slots worth adding: current solutions and satisfaction, workarounds, delighters, surprises.** Current tools reveal the real competitive set. Praise protects strengths from being broken in a redesign.
> "Current solutions reveal competitors ... (including spreadsheets, manual processes, and workarounds)"
> "Separate satisfaction from problems ... Knowing strengths prevents accidentally breaking them."
Source: https://github.com/shawnpang/startup-founder-skills/blob/HEAD/skills/user-research-synthesis/SKILL.md

**2.4 ★ Treat workarounds as unmet needs.**
> "Flag workarounds — these are unmet needs in disguise"
Source: https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/product-management/skills/synthesize-research/SKILL.md

**2.5 ★ Code behavior and motivation separately. Tag emotion sparingly.**
> "'User clicked X' is behavior; 'User clicked X because they thought it would Y' is motivation."
> "Tag emotional valence sparingly ... tagging every artifact for emotional state produces noise."
Source: rampstack tagging-and-clustering-discipline.md (URL above)

---

## 3. Coding approach (inductive, deductive, hybrid)

**3.1 ★ Make the four analytic decisions explicit before coding:** rich description vs one aspect, inductive vs theoretical, semantic vs latent, and epistemology. Check that the write-up matches them (Braun & Clarke pitfall 5).
> "Walk the user through each decision. Do not assume realist + semantic + inductive by default just because the paper notes this is the common (often unspoken) default. Ask."
Source: keemanxp SKILL.md (URL in 2.1)

**3.2 ★ Codebook row: definition, inclusion, exclusion, and a cited example. Version it, and re-code earlier transcripts when a definition shifts.**
> "| Code | Definition | Inclusion criteria | Exclusion criteria | Example quote (with cite) |"
> "Iterate the codebook as you code. Note the version. When a code's definition shifts, re-code earlier transcripts to apply the new definition."
Source: https://github.com/Marazii/research-co-pilot/blob/HEAD/skills/qualitative-coding/SKILL.md

**3.3 ★ Let tags proliferate, then collapse them later.** Premature merging only supports confirmation.
> "Early tagging may produce 80-150 tags across a batch. That is correct. ... Granular tags can always be collapsed in the clustering stage; collapsed tags cannot be unmerged"
Source: rampstack tagging-and-clustering-discipline.md

**3.4 Let semantic tags emerge from the data. Fixed metadata (segment, channel, recency) can be applied consistently.**
> "The exception. Some categorical metadata is fine to apply consistently (user segment, source channel, recency). The semantic tagging that drives synthesis should still emerge from the data."
Source: rampstack tagging-and-clustering-discipline.md

**3.5 ★ Use in-vivo codes first (participants' words), abstract later. Use gerund-style codes for process.**
> "Stay close to the data. Use participants' language in early codes (in vivo) before abstracting."
> "Open coding — line-by-line, often gerund-style ('avoiding disclosure', 'rationalizing risk')."
Source: Marazii qualitative-coding SKILL.md

**3.6 ★ Code inclusively. Keep surrounding context. One extract can take several codes or none.**
> "Code extracts inclusively — keep a little surrounding context so meaning is not lost. A single extract can be coded under multiple codes, or none. Retain accounts that depart from the dominant story"
Source: keemanxp SKILL.md

**3.7 ★ Route LLM effort by coding type.** LLMs were non-inferior to humans at applying a predefined codebook, and variable at open theme generation and latent meaning. So let the LLM apply the codebook, and keep a human checkpoint on inductive theme construction and on any latent claim.
> "LLMs performed similarly to humans when applying pre-defined codes (deductive analysis) ... in open-ended theme generation (inductive analysis) their performance was more variable, particularly in areas requiring interpretation of tone, nuance, or conversational context."
Source: Hill et al. medRxiv (URL in 1.1)

**3.8 ★ Two-stage LLM pipeline: themes per interview first, then a separate cross-interview merge pass.** Reject runs that drop an interview.
> "Phase 3 generated themes per interview, and Phases 4–5 merged them across all 15 interviews in a separate pass." / "Pipelines were excluded if they omitted interviews"
Source: https://arxiv.org/html/2510.18456 (summary of the paper's method)

**3.9 ★ The prompt asks for a quote, why it is relevant to the RQ, a sensitivity flag, and the interview and line for each code.**
> "Prompt 1 asked for the verbatim quote, a short explanation of relevance, a sensitivity note, and the interview number and line."
Source: https://arxiv.org/html/2510.18456

**3.10 ★ Usability observation sheet (rainbow spreadsheet): observation rows x participant columns, written in advance as single behaviors.** Predetermined observations let you deduce against expectations. Conclusions and solutions do not belong in observation rows.
> "Write each observation as a single behavior ... warns against 'double-barreled' observations"
> "remove duplicates and anything that isn't an observation, such as conclusions, inferences, solutions, or action items."
Source: https://smashing-patternlib.netlify.app/2013/04/rainbow-spreadsheet-collaborative-ux-research-tool

**3.11 ★ GOV.UK variant: each task has falsifiable assumptions, marked yes/no per participant.** The "do" and "say" notes are kept separate.
> "assumptions should be 'observable actions that can be classed as "yes" or "no"' ... One records what participants *do* ... The other records what participants *say*, capturing exact words."
Source: https://userresearch.blog.gov.uk/2019/09/13/how-a-spreadsheet-can-make-usability-analysis-faster-and-easier/

---

## 4. Evidence tracing and quote verification

**4.1 ★ Check claim-to-quote semantics, not just that the string matches.** Known verifier blind spots: the claim says "found a change" while the quote says "found no change" (polarity reversal); numbers are swapped between categories; an uncited qualitative sentence slips in. Add explicit checks for negation and direction, and for each number counting the same thing in the claim and the quote.
> "`polarity-reversal` | claim and sentence say 'found a change'; the quote says 'found no change'"
> "`number-swap` | source, quote and claim say 40 adults and 60 children; the sentence says 60 adults and 40 children"
> "a number must count the same word it counts in the claim or quote"
Source: https://github.com/poemswe/co-researcher/blob/HEAD/evals/published/paper/README.md

**4.2 ★ Mechanical existence check with fuzzy matching (Levenshtein) for every quote.** Your `scripts/analysis_contract.py` could run this.
> "used Levenshtein distance 'to check that provided quotes exist in the transcript'"
Source: https://authorconnect.aisnet.org/conferences/AMCIS2025/papers/2130

**4.3 ★ Use a `[QUOTE NEEDED]` placeholder instead of generating or paraphrasing a quote.**
> "Quotes must come directly from the input. If none is available, insert a clearly marked placeholder, `[QUOTE NEEDED]`, instead of generating one."
Source: https://www.enterpret.com/blog/how-to-build-a-user-research-claude-skill-for-pms

**4.4 ★ Quote audit checks beyond existence:** the speaker matches at that timestamp, the quote is about the same product, workflow, or period, and joined lines are marked with an ellipsis.
> "verify that each quote's speaker label matches the transcript at that timestamp"
> "Confirm the quote concerns the same product, workflow, or period the report describes."
> "If two separate lines were combined, mark the join with an ellipsis and keep the meaning intact."
Source: https://gotranscript.com/en/blog/ai-qual-research-qa-checklist-prevent-hallucinations-misattribution

**4.5 ★ Collate every relevant extract at coding time. Choose the quotable ones only at write-up.** This stops quote-first theme building.
> "Every extract that fits a theme should be filed under it. Do not pick only the most quotable ones at the coding stage — that decision belongs in Phase 6"
Source: keemanxp quality-checklist.md

**4.6 ★ Excerpt JSON with a per-excerpt memo, including contrasts with other participants.**
> `{"lines": "142-148", "text": "...", "codes": [...], "memo": "Participant frames non-disclosure as a choice, not constraint — contrast with P01."}`
Source: Marazii qualitative-coding SKILL.md

---

## 5. Hallucination guards for LLM synthesis

**5.1 ★ Even-sampling guard: tag every observation with a participant ID, and after clustering check that every participant appears.** This targets the LLM habit of building themes from the first one or two transcripts.
> "After clustering, check that each participant appears at least once in the output — if any are absent, go back ... This prevents the common LLM failure mode of building themes from the first one or two transcripts and fitting the rest retroactively."
Source: https://github.com/owl-listener/designer-skills/blob/HEAD/design-research/skills/affinity-diagram/SKILL.md

**5.2 ★ Batch large corpora (15+ transcripts) into groups of 10-12, then synthesize the batch outputs.**
> "Works best with 5 to 15 transcripts. For 15+, run batches of 10 to 12, then synthesize the batch outputs."
Source: https://www.greatquestion.com/blog/claude-skills-ux-research-assistant

**5.3 ★ Red-flag scan for fabricated synthesis.**
> "Quotes that read as written rather than spoken. Uniformly positive or negative sentiment. Counts the team never requested. People, tools, or features that do not appear in the data. No mention of outliers or 'it depends.' Admin pain points attributed to end users, or the reverse."
Source: GoTranscript checklist (URL in 4.4)

**5.4 ★ Pass only verified output forward.** In multi-pass pipelines, unverified codes from transcript k must not seed coding of transcript k+1.
> "Unreliable content is removed, and only verified results are passed on to the next transcript."
Source: https://arxiv.org/abs/2605.20193

**5.5 ★ Watch for overgeneralization at higher abstraction levels.** Second-order themes drift into non-informative statements once first-order meaning is lost. Re-ground each theme in its exact codes.
> "The system extracted 1st-order concepts, but it lost the meanings attached to them ... 2nd-order themes and aggregate dimensions were inaccurate and often bordering on non-informative."
Source: https://authorconnect.aisnet.org/conferences/AMCIS2025/papers/2130

**5.6 ★ Self-check against the top rubric column inside the prompt.**
> "an internal self-check based on the 'Excellent' rubric column"
Source: https://arxiv.org/html/2510.18456

**5.7 ★ The no-fabrication clause covers numbers, not only quotes.** A stated gap counts as a complete answer.
> "Fabricating, estimating, or interpolating a required number to complete the deliverable is never sanctioned. A stated gap is a complete answer."
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/usability-testing/SKILL.md

---

## 6. Counting and frequency language

**6.1 ★ Pick one unit of prevalence (data item, participant, or occurrence) and keep it throughout. Map vague quantifiers to it.**
> "If you describe prevalence, be consistent ('most participants', 'a number of participants', 'in over half the data set') and pick a unit of analysis (data item, participant, occurrence) and stick to it."
Source: keemanxp SKILL.md
> "Map words like 'most,' 'many,' and 'a few' to your counting method. Avoid percentages when the sample is small"
Source: GoTranscript checklist

**6.2 Recount every "X of Y" from the evidence and list the participant IDs next to it.**
> "Recount any 'X of Y' statements and list the supporting participant IDs."
Source: GoTranscript checklist

**6.3 ★ Prevalence is not decisive.** A theme can be brief in many items or extended in a few. Its importance is judged against the RQ.
> "Prevalence matters but is not decisive. A theme can appear in many items briefly, or in a few items at length."
Source: keemanxp SKILL.md

**6.4 ★ Frequency is not importance. Allow an explicit ICP or "whale" exception.**
> "A pain point mentioned by 2 of 10 users may be more critical than one mentioned by 8 if those 2 users represent your ideal customer profile."
Source: shawnpang user-research-synthesis
> "Require 3+ independent mentions ... Exception: if the one customer is a whale account citing it as a churn risk."
Source: shawnpang feedback-synthesis

**6.5 ★ Recency check: compare against the prior period before calling something rising.**
> "A flood of recent feedback about one issue can overshadow a persistent problem. Always compare against the prior period."
Source: shawnpang feedback-synthesis

**6.6 ★ For surveys, report the distribution and not just the mean. Code open-ends for themes the closed items never asked about.**
> "Reporting averages without distributions. A 3.5 average could mean everyone is lukewarm or half love it and half hate it."
> "Look for themes that appear in open-ended responses but not in structured questions — these are things you did not think to ask about"
Source: Anthropic synthesize-research SKILL.md

---

## 7. Severity and priority scoring

**7.1 ★ Nielsen 0-4 severity with four factors, rated independently by several evaluators.** The LLM rating should count as one rater, and the researcher rates independently.
> "0: I don't agree that this is a usability problem at all ... 4: Usability catastrophe: imperative to fix this before product can be released"
> Factors: frequency, impact, persistence, market impact. "severity ratings from a single evaluator are too unreliable to be trusted."
Source: https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/

**7.2 ★ Simple severity formula: Impact (1-3) x Frequency (1-3).**
> "Severity = Impact x Frequency" / "3 - High Impact: Blocks task completion for some or all users"
Source: https://github.com/oakoss/agent-skills/blob/HEAD/skills/usability-tester/references/metrics-severity.md

**7.3 ★ Issue inventory first (issue, participant, task, severity), then cluster by root cause.**
> "1. Issue inventory. Every issue observed, with which participant, which task, severity. 2. Cluster. Issues that are the same root problem."
Source: rampstack usability-testing SKILL.md

**7.4 ★ Usability metrics hygiene:** report assisted and unassisted success separately, use the median for time on task, watch for bimodal distributions, and look at the most common first error.
> "Report both unassisted and assisted success rates separately" / "Calculate median time (more robust than mean for small samples)" / "Identify the most common first error (often reveals the root cause)"
Source: oakoss metrics-severity.md

**7.5 ★ Worst-case rollup per task (traffic light): one red participant makes the task red.**
> "each task takes the worst colour observed across participants. One red makes the task red overall."
Source: commenter on the GOV.UK post (https://userresearch.blog.gov.uk/2019/09/13/how-a-spreadsheet-can-make-usability-analysis-faster-and-easier/)

**7.6 ★ Opportunity Score for feedback and JTBD outcomes: Importance x (1 - Satisfaction).**
> "Opportunity Score = Importance x (1 - Satisfaction), normalized to 0-1. This surfaces problems that are both important and underserved."
Source: shawnpang feedback-synthesis

**7.7 ★ Include a "Not prioritized (and why)" section, and allow "not-act" implications.**
> "Some patterns imply not-acting ... it affects too few users, it represents segment misfit, addressing it would compromise other priorities. Naming the not-act implication is honest synthesis."
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/discovery-research-synthesis/SKILL.md

---

## 8. Contradiction and outlier handling

**8.1 ★ Every pattern gets a mandatory "But consider" block** covering contradictions, segment differences, and edge cases.
> "Each major pattern in synthesis has a 'but consider' section: contradictions in the data, segment differences, edge cases. ... A pattern with no countervailing evidence is suspicious"
Source: rampstack tagging-and-clustering-discipline.md

**8.2 ★ Leftovers are signal. Flag single-source patterns instead of dropping them.**
> "Surface the leftovers. Tags that do not fit any cluster are signal."
Source: rampstack tagging-and-clustering-discipline.md
> "Patterns that appear in only one interview should be flagged as single-source, not discarded"
Source: owl-listener affinity-diagram
> "Single observations are labeled 'interesting but not validated' rather than promoted to themes."
Source: Enterpret

**8.3 ★ Qual-vs-quant disagreement lookup table: the shape of the disagreement tells you where to look.**
> "Data shows abandonment; users report no difficulty | They abandoned for a reason they do not attribute to the interface"
> "Data improved; users report it feels worse | You optimised a proxy."
> "Users are enthusiastic; retention is flat | Stated preference, not revealed."
Source: https://github.com/owl-listener/designer-skills/blob/HEAD/design-research/skills/qual-quant-triangulation/SKILL.md

**8.4 ★ Category-error check: a why-question asked of a dashboard, or a how-many question asked of six interviews, is not a real contradiction. Never average two accounts.**
> "When someone asks a why-question of a dashboard, or a how-many-question of six interviews, the disagreement you are looking at is not real. It is a category error."
> "Do not average the two accounts into a compromise finding"
Source: owl-listener qual-quant-triangulation

**8.5 ★ Before calling it a contradiction, check that both sources describe the same population.**
> "Check that both sources describe the same population before calling it a contradiction — different segments are not a disagreement"
Source: owl-listener qual-quant-triangulation

**8.6 ★ When a note fits two clusters, duplicate it. Don't discount small clusters.**
> "When a note fits two clusters, duplicate it and place it in both." / "Don't discount a small cluster; it may reflect a distinct perspective."
Source: https://www.nngroup.com/articles/affinity-diagram/

---

## 9. Mapping back to research questions

**9.1 ★ Record the RQ verbatim as an artifact and re-read it at the start of every phase.** A theme that is coherent but off-RQ goes to the discard pile.
> "Record the agreed research question(s) verbatim ... Refer back to this file at the start of each subsequent phase."
> "A theme that is internally coherent but unrelated to the question is a candidate for the discard pile."
Source: keemanxp SKILL.md

**9.2 ★ Anti-pattern: themes that mirror the interview guide questions one to one.**
> "The themes in the write-up correspond one-to-one with the questions in the interview schedule ... Themes should cut across questions and find patterns that the interview schedule did not anticipate."
Source: https://github.com/brycewang-stanford/auto-empirical-research-skills/blob/HEAD/skills/53-keemanxp-thematic-analysis-skill/thematic-analysis/references/pitfalls.md

**9.3 ★ Theme definitions must state central concept, boundaries, uniqueness, and contribution to the RQ.**
> "required definitions covering the central concept, boundaries, uniqueness, and contribution to the RQ."
Source: https://arxiv.org/html/2510.18456

**9.4 ★ Put the answers to each RQ first (rainbow summary sheet).**
> "Summary (placed first): research questions, answers to those questions, action items, and primary findings."
Source: Sharon rainbow spreadsheet

**9.5 ★ Each implication names the specific decision it informs (the "so-what").**
> "For each implication, the specific decision it informs. 'Should we prioritize the onboarding redesign in Q2?' The so-what is what makes the synthesis decision-grade."
Source: rampstack discovery-research-synthesis SKILL.md

---

## 10. Confidence levels

**10.1 Name the evidence status of each insight as explicitly stated or inferred.** Your skill already does this.
> "Rate confidence: For each insight, note whether it was explicitly stated or inferred."
Source: https://github.com/owl-listener/designer-skills/blob/HEAD/design-research/skills/summarize-interview/SKILL.md

**10.2 ★ Calibrated vocabulary for synthesis claims: "High confidence / Emerging evidence / Contested".** "Contested" is a useful label for disputed themes.
> "Use calibrated language for confidence levels (e.g., 'High Confidence', 'Emerging Evidence', 'Contested')."
Source: https://github.com/poemswe/co-researcher/blob/HEAD/skills/research-synthesis/SKILL.md

**10.3 ★ Thin patterns get three honest options: tentative, pause and gather more, or drop.** Never present them as if fully supported.
> "Name the pattern as tentative pending more data ... Pause synthesis to gather more research ... Drop the pattern ... Inflating thin patterns to fill space is a synthesis failure."
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/discovery-research-synthesis/references/when-to-gather-more-data.md

**10.4 ★ Warn about weak data early instead of over-claiming at write-up.**
> "If the data are weak (thin, surface-level, common-sense), a good analysis is much harder. Flag this to the user early rather than over-claiming at the write-up stage."
Source: keemanxp SKILL.md

---

## 11. Segmenting by participant attributes

**11.1 ★ Use a participant profile table (ID, role or segment, tenure, date, key characteristic)** so readers can judge representativeness.
> "| ID | Role/Segment | Tenure | Interview Date | Notes |"
Source: https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/discover-interview-synthesis/references/TEMPLATE.md

**11.2 ★ Framework-analysis matrix: rows are participants, columns are themes.** It makes segment differences visible, and it is the analytic twin of the rainbow sheet.
> "Chart data into a matrix (rows = participants, columns = themes). Map and interpret across cases."
Source: Marazii qualitative-coding SKILL.md

**11.3 ★ Name the segments the sample covers and scope the recommendation to them.**
> "Name patterns for the 50-500 segment with confidence. Acknowledge that enterprise and small business patterns are not represented. Recommend either separate research for the missing segments or scoping the decision to the segment the data covered."
Source: rampstack when-to-gather-more-data.md

**11.4 ★ Use contradictions as a segment detector.** Most such contradictions turn out to be sub-segment or context differences.
> "'Most users find configuration confusing; experienced users find it efficient' might mean the pattern is segment-specific, not universal."
Source: rampstack tagging-and-clustering-discipline.md

**11.5 ★ Bias notes: who was NOT interviewed, leading questions, survivorship (current vs churned users).**
> "Note recruitment bias (who was NOT interviewed), leading question bias (review the interview script), and survivorship bias (current users vs. churned users)."
Source: shawnpang user-research-synthesis

---

## 12. Quality gates

**12.1 ★ Patton's dual criterion for every theme: internal homogeneity and external heterogeneity.** Run both review levels: extracts against the theme, then the theme map against the whole dataset.
> "Internal homogeneity — data within a theme cohere meaningfully. External heterogeneity — themes are clearly distinct from each other."
Source: keemanxp SKILL.md

**12.2 ★ "Cover the extracts" test for analysis vs paraphrase.**
> "cover the extracts and read only the analytic commentary. Does it stand alone as an argument about the topic? If yes, the analysis is doing real work."
Source: keemanxp pitfalls.md

**12.3 ★ Cluster-boundary test and minimum two clustering passes.**
> "Test cluster boundaries. Take a tag from one cluster and ask: could this fit in another cluster instead? If yes, the cluster boundaries are unclear; refine." / "Iterate clustering at least twice."
Source: rampstack tagging-and-clustering-discipline.md

**12.4 ★ Mechanical cluster-size rules.**
> "If a cluster has more than 15 items, split it. If a cluster has fewer than 3 items, consider merging or flagging as an outlier. Relabel clusters after regrouping"
Source: https://github.com/sarveshsea/design-skills/blob/HEAD/skills/data-synthesis/SKILL.md

**12.5 ★ IRR metric choice for sparse codes: report Gwet's AC1 alongside κ.** Low code prevalence crushes κ even at high raw agreement. This applies to coding-reliability and tagging modes only, not reflexive thematic analysis.
> "LLMs yielded a mean agreement of 93.5% ... with κ = 0.34 ... Mean Gwet's AC1 was ... 0.93 ... reflecting high agreement despite the low overall code prevalence (7.8%"
Source: Hill et al. medRxiv

**12.6 ★ Skill evals written as "Must contain / Must not" cases built to fail shallow answers.**
> "Each case is designed so a plausible-sounding but shallow answer fails at least one check. ... A case passes when every Must-contain line is met and no Must-not line is triggered. ... Record the failing check, not just the score"
Source: https://github.com/owl-listener/designer-skills/blob/HEAD/design-research/skills/qual-quant-triangulation/EVALS.md

**12.7 ★ Back-test the skill on a past study with a known conclusion.**
> "Run the Skill on a past study with a known conclusion and compare its output to the shipped synthesis ... found the same top themes, surfaced at least one surprising quote, and respected the three-session threshold."
Source: Enterpret

**12.8 ★ Output-quality eval input: raw notes from 5 participants that contain conflicting signals,** judged against a no-skill control arm.
> "The skill arm and the control arm each receive everything below ... and produce an interview-synthesis artifact for it. Judges never see this header. The input is RAW interview notes"
Source: https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/discover-interview-synthesis/evals/output-scenarios/onboarding-interviews.md

**12.9 ★ Participant recognition (member checking) and adjacent-team challenge sessions as optional validation steps.**
> "Misrecognition signals fabrication: the synthesis projected interpretations the data did not support"
> "Synthesis owner takes notes; does not defend; the session is for surfacing concerns"
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/discovery-research-synthesis/references/synthesis-review-and-validation.md

**12.10 ★ Minimum QA routine (15-30 min) with an evidence gate of at least 2 anchored excerpts per theme.**
> "Evidence gate: require at least two anchored excerpts per theme, and flag unanchored themes as unverified. Quote audit ... Number check ... Context pass ... Final read: remove any statement that implies more certainty than the evidence supports."
Source: GoTranscript checklist

---

## 13. Naming and writing findings

**13.1 ★ A theme is a claim, not a bucket.**
> "Themes that are categories (e.g., 'pricing') rather than claims, such as 'users read our pricing as enterprise and self-disqualify'"
Source: https://claudskills.com/skills/atomic-synthesis/SKILL.md

**13.2 ★ Pattern-name tests: implication legibility and no truisms.**
> "A reader who sees only the pattern name should be able to guess the product implication."
> "'Users want fast performance' is not a pattern; it is a truism. ... If the pattern name reads as something everyone could have said before the research, the pattern is not a pattern."
Source: rampstack discovery-research-synthesis SKILL.md

**13.3 ★ Ban "themes emerged". The analyst constructs themes and should say so in active voice.**
> "Themes do not 'emerge'. The analyst identifies them. Do not use 'themes emerged' in the write-up — it is a passive construction that hides the analyst's active role"
Source: keemanxp SKILL.md

**13.4 ★ Insight sentence template.**
> "We learned that [finding] which means [implication] so we should [recommendation]."
Source: shawnpang user-research-synthesis

**13.5 ★ Specific, falsifiable implications that acknowledge cost.**
> "A vague implication ('we should improve onboarding') is not actionable. A specific implication ('staged onboarding that defers the third configuration step until after the user reaches the first success state') is."
Source: rampstack discovery-research-synthesis SKILL.md

**13.6 ★ Aim for 4-8 themes. More than 12 is category bloat. Three solid themes beat six weak ones.**
> "4 named patterns is often the right number; 6-8 is common; more than 12 is usually category bloat."
Source: rampstack discovery-research-synthesis SKILL.md
> "It is much better to report three solid themes than six weak ones."
Source: keemanxp pitfalls.md

**13.7 ★ Atomic reuse: link to existing team vocabulary and prior findings before coining new labels.**
> "Connect: link nuggets and themes to existing knowledge ('reuse-before-coin') rather than coining new terms."
Source: claudskills atomic-synthesis

---

## 14. Anti-patterns (consolidated)

- **Anecdotalism.** Reifying one or two vivid extracts into a theme. (keemanxp quality-checklist item 3)
- **Interview questions used as themes.** (keemanxp pitfalls #2)
- **Paraphrase instead of analysis.** (keemanxp pitfalls #1; NN/g thematic analysis: "Descriptions that repeat what participants said without analytical thinking")
- **Mismatch between theory and claims.** For example, claiming a semantic, realist approach in the method and then making latent or constructionist claims in the findings. (keemanxp pitfalls #5)
- **Pre-designed taxonomy and named-before-clustered themes.** These produce confirmation, not discovery. (rampstack)
- **Cluster collapsing to fit a target count.** (rampstack)
- **Treating participant suggestions as features.** "Users solve their problem; product team designs the solution." (rampstack usability-testing)
- **Insight theater and quote walls.** Evidence should go in an appendix, with patterns and implications leading. (rampstack)
- **Hedge stacking.** "Hedged pattern names ... signal a researcher who did not commit." (rampstack) There is tension with the hedged register Braun & Clarke recommend, so pick one stance per audience.
- **Moderator speech coded as participant evidence.** (Hill et al.)
- **Front-loaded themes built from the first transcripts.** (owl-listener)
- **Resolving a conflict by re-running the study that gave the preferred answer.** (owl-listener)
- **Fatigue in tagging sessions.** "Tag quality decaying as fatigue sets in." This is the LLM analogue of long-context drift, and a reason to batch. (rampstack)
