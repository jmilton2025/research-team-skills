# Patterns: reusable ideas for a UX research `report` skill

Each item gives the idea, a short excerpt (5 lines or fewer), and the source. Excerpts from cloned repos are exact. Excerpts from web pages are quotes as returned by the page fetch. Items marked ★ are the most specific or least obvious.

---

## 1. Purpose framing: write for decisions, not for the meeting

**1.1 ★ Name the three outcomes and test for the right one.** Data-dump means no synthesis. Insight-theater means a polished deck that drives no decision. Actionable synthesis is the goal. Give the skill this test to apply.
> "Three months after a synthesis ships, can team members name the decisions the synthesis informed? If yes, the synthesis was actionable. If team members remember the deck but cannot name the decisions, it was insight-theater."
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/discovery-research-synthesis/SKILL.md

**1.2 ★ Ask "what decision will this inform?" before writing.** Store the answer and make every section serve it.
> "What decisions will this research inform?"
Source: Anthropic PM synthesize-research (`anthropics/knowledge-work-plugins: product-management/skills/synthesize-research/SKILL.md`). Also PromptHub's `{{DECISION_CONTEXT}}` variable: https://prompthub-local-1.pages.dev/en/templates/research-findings-executive-briefing-crafter/

**1.3 Make the document the reference artifact and the deck a summary of it.**
> "A short executive summary deck (5-8 slides) can pair with a substantive document. The deck summarizes; the document carries the work."
> "Optimize for the reference use, not the presentation moment."
Source: rampstackco `references/writing-for-decisions-not-decks.md`

**1.4 Choose the format by how involved the audience was.** Boards suit highly involved stakeholders. Slides suit low-context readers or group presentations. A written document suits complex studies, future readers who won't have a presenter, and avoiding "insight distortion". Source: https://dscout.com/people-nerds/easy-user-research-report-template. GitLab offers a similar rule: slides when "there is a story to tell behind the insights", a repository entry for small-scope findings. Source: https://handbook.gitlab.com/handbook/product/ux/experience-research/research-insights/

---

## 2. Audience tailoring

**2.1 One core report plus derived audience cuts.** Executive (one page, top 3 findings and recommendations), product team (full findings and evidence), design team (detailed findings, UI annotations, specific design recommendations). Source: https://www.koji.so/docs/ux-research-report-template

**2.2 Give each audience a different emphasis.** PMs get actionable recommendations, designers get behavior and journey moments, and leadership gets business impact, risk and opportunity. Source: https://www.greatquestion.com/blog/claude-skills-ux-research-assistant

**2.3 ★ Exec cut rules taken from stakeholder updates.** Cap at about 200-300 words. Lead with the outcome. Make asks specific and dated. Lead with bad news.
> "Asks must be specific: "Decision on X by Friday" not "support needed.""
> "If there is bad news, lead with it. Do not hide it after good news."
Source: Anthropic PM stakeholder-update SKILL.md

**2.4 Very short broadcast cut (30-60 seconds to read).** Fixed lines of 1-3 sentences each, matter-of-fact, with metrics where possible. A useful pattern for a Slack teaser that links to the report.
> "Each section should be no more than 1-3 sentences: clear, to the point. It should be data-driven, and generally include metrics where possible."
Source: https://github.com/anthropics/skills/blob/main/skills/internal-comms/examples/3p-updates.md

**2.5 Plain language and accessibility for mixed audiences.** Keep outputs screen-reader friendly. "Use participant language to keep findings authentic." Source: https://newjersey.github.io/innovation-ux/how-we-work/research/share-findings/

---

## 3. Executive summary / BLUF / answer-first

**3.1 ★ Use the under-one-minute headline test.**
> "Put the headline finding in the first three sentences—don't make readers excavate it."
> A stakeholder should "grasp the headline finding in under a minute."
Source: https://dovetail.com/research-report-template/

**3.2 ★ The exec summary must stand alone.** Use 3-5 bullets, each pairing a finding with its recommendation.
> "three to five bullets, each one a finding plus its recommendation."
> "A reader who only has ninety seconds should be able to get the whole point from that block alone."
Source: https://getversive.com/help/build-a-research-report

**3.3 Write the summary last and put it first.** A finding that isn't in the exec summary probably won't get acted on. Template opener: "We conducted [X interviews / survey with X participants] to understand [research question]." Source: https://www.koji.so/docs/ux-research-report-template

**3.4 ★ BLUF mechanics the skill can run as an edit pass.** Find the single most important sentence, move it to the top, delete setup, and reorder the rest by "what you would miss most if it were cut". If no single most important sentence exists, the thinking is unclear, so fix that first. Source: https://library-d7m.pages.dev/communication-framework/writing-and-structure/bluf-and-inverted-pyramid

**3.5 Governing thought plus minimal SCQA.** Add Situation or Complication only when the reader can't understand the answer without it.
> "Include the minimum Situation or Complication the reader needs, then state the governing thought before the document body. When the context is shared, begin with the governing thought."
Source: https://github.com/tyroneross/pyramid-principle/blob/main/skills/pyramid-long-form/SKILL.md

**3.6 Lead with one insight even when the study found several, and pick its supporting reasons.**
> "Pick the reasons that support your main insight instead of listing every finding from your study"
> "Learn how to lead with one clear insight when your study uncovered several"
Source: https://maven.com/user-research-strategist/pyramid-principle-reporting-for-user-research

**3.7 When BLUF is the wrong tool.** It suits persuasive pieces poorly (the reader needs the setup), as well as sensitive topics and teaching contexts. Use SCQA or story structure there. Source: library-d7m BLUF page (above).

---

## 4. Structure and ordering

**4.1 ★ Order the body by decision impact, not by the order the work happened.** Methodology goes to an appendix.
> "A report that opens with sample size, screener criteria, and demographics delays the information a stakeholder needs."
> Order findings "by how much they should change the reader's next action."
Source: https://getversive.com/help/build-a-research-report

**4.2 Organize findings by study type.** Evaluative studies go by research goal, generative studies by theme, large datasets by affinity category. Source: https://www.koji.so/docs/ux-research-report-template. dscout adds that structuring by goals is what "stakeholders find it the easiest to digest": https://dscout.com/people-nerds/easy-user-research-report-template

**4.3 Synthesize across sources. Never structure by interview or sub-folder.**
> "Don't structure the report by sub-folder or project—synthesize everything into unified themes"
Source: https://docs.dovetail.com/help/docs/report-prompt-guide

**4.4 ★ Use parallel per-finding sections.** Same fields in every finding, so readers learn the shape once and editors can check completeness.
> "Length variation is fine; structural variation is not."
Source: rampstackco `writing-for-decisions-not-decks.md`

**4.5 Make every finding readable on its own.**
> "Each finding should stand on its own — a reader should be able to read any single finding and understand it without reading the rest."
Source: Anthropic PM synthesize-research SKILL.md

**4.6 Put evidence under the claim it supports.** Avoid a separate "Background" or "Data" section.
> "Place evidence under the claim it supports. Do not create a separate background or data section when the material belongs under a specific claim."
Source: pyramid-long-form SKILL.md

**4.7 Add sections that are cheap but valuable:**
- "Outliers worth investigating: single-participant observations that may be signal in disguise." Source: https://github.com/rampstackco/claude-skills/blob/main/skills/ux-research/SKILL.md
- "Signals worth investigating" (raised by only 1-2 people) plus a contradictions section. Source: Great Question blog.
- "Questions for Further Research" and "Methodology Notes". Source: Anthropic design research-synthesis SKILL.md.
- "Kudos to the team". Source: dscout template.

---

## 5. Writing findings and insights

**5.1 ★ Pick a level on the data → finding → insight → recommendation ladder, and label it.**
> Finding: "60% of users struggled to find the "Money transfer" feature on a dashboard."
> Insight: "Navigation doesn't match users' mental models for money transfer, causing confusion and delays."
> Recommendation: "We recommend to rename sections or reorganize the dashboard to prioritize "Transfer Money"."
Source: https://smart-interface-design-patterns.com/articles/data-findings-insights/

**5.2 ★ Evaluative studies can stop at findings. Don't fake insights.**
> "evaluative research questions are normally addressable with findings, whereas generative ones often require insights."
> Insights "should be communicable in 1-2 sentences rather than entire paragraphs" — the evidence "can - and should - be much more in-depth."
Source: https://answerlab.com/insights/what-are-research-insights-what-makes-them-different-from-findings

**5.3 ★ Insight formulas.** Have the skill choose a formula per study type:
> Tension: "[User type] is trying to [goal] but [barrier], because [root cause], which means [implication]."
> Behavioral: "When [trigger or context], [users] tend to [behavior], which suggests [underlying belief or need]."
> JTBD: "[User] is trying to [make progress], but currently relies on [workaround] because [the core need] is not being met."
Also: end with a "This means..." sentence and require at least 3 supporting participants. Source: https://www.koji.so/docs/writing-insight-statements

**5.4 What happened + why + so what.** A compact rubric for checking any insight. Source: Smart Interface Design Patterns (above).

**5.5 ★ Headings must be claims, not topic labels.** Test: could the reader agree or disagree with it?
> "Can the audience agree or disagree with it? If yes, it is an assertion. If the only possible response is "okay, I see what this section is about," it is a topic label."
> "Remove the slide body, chart, and bullets. Does the headline still communicate the point...?"
Source: https://github.com/tyroneross/pyramid-principle/blob/main/skills/pyramid-presentation/references/slide-headline-rules.md. Great Question's theme auditor flags topic labels like "Onboarding" against claims like "People give up on setup before they see any value": https://www.greatquestion.com/resources/claude-skills-library/theme-quality-auditor

**5.6 ★ Strong verbs, specific nouns.** Rewrite weak headline verbs (is/has/provides/shows/indicates) as dynamic ones (dropped, blocked, shifted, contradicted). Write "Three factors", not "several factors". Use parallel grammar across peer headings. Source: slide-headline-rules.md (above).

**5.7 ★ Pattern names should make the implication guessable, and should not be truisms.**
> "'Onboarding' is a category. 'Users abandon configuration before reaching the success state because the third configuration step requires data they do not have on hand' is a pattern."
> "If the pattern name reads as something everyone could have said before the research, the pattern is not a pattern."
Source: rampstackco discovery-research-synthesis SKILL.md

**5.8 Check for "mirrors the discussion guide".** Flag a theme that just restates a guide question. Also flag emergence language ("themes emerged") and suggest "developed" or "constructed". Source: Great Question theme-quality-auditor page.

**5.9 Things that are not insights:**
> "Insights aren't a single data point." / "Insights aren't customer wants and requests." / "Insights don't justify already-held beliefs." / "Insights aren't solutions."
> "If you've got an insight where only one solution is possible, then you don't have an insight. You have a solution idea."
Source: https://thefountaininstitute.com/blog/writing-user-insights

**5.10 Keep observation separate from interpretation, and behavior from stated preference.**
> "'5 of 8 users clicked the wrong button' is an observation. 'The button placement is confusing' is an interpretation."
Source: Anthropic design research-synthesis SKILL.md. The PM skill adds: "Behavioral observations are stronger evidence than stated preferences."

**5.11 Cap the count.** Use 3-5 findings (Dovetail), 5-8 (Anthropic PM), or 4-8 (rampstackco). More than about 12 is "category bloat", which calls for re-clustering, not shipping.

---

## 6. Evidence and quotes

**6.1 ★ A finding with no evidence is only an opinion.**
> "A finding without evidence is an opinion with formatting."
> "Every claim cites a quote, a clip, or a number a reader can check."
Source: https://dovetail.com/research-report-template/

**6.2 Quotes have rules.** Use 2-3 per finding. Choose quotes that state the finding. Attribute by participant number, consistently. More quotes "reads as padding". Drop vague quotes such as "It was fine, I guess." Source: https://getversive.com/help/build-a-research-report. Dovetail asks for quotes "from different participants": https://docs.dovetail.com/help/docs/report-prompt-guide

**6.3 Attribute by participant type, not name.**
> "Attribute to participant type, not name: "Enterprise admin, 200-person team" not "Sarah""
> "A quote is evidence, not a finding. The finding is your interpretation of what the quote means."
Source: Anthropic PM synthesize-research SKILL.md

**6.4 ★ Tag the source type on evidence in multi-source reports.** For example `[Interview]`, `[Support]`, `[Review]`, `[Community]`. Readers can then see triangulation at a glance. Source: Dovetail report prompt guide.

**6.5 ★ Verify quotes against transcripts before publishing.** Label each quote verified, lightly edited, altered, or not located, and give the closest match. Also flag over-quoted participants. Source: https://www.greatquestion.com/resources/claude-skills-library/evidence-integrity-auditor. Versive also lists "Sharing a theme or paraphrase without first checking it against the source quotes" as an anti-pattern.

**6.6 Keep the evidence summary short in the body and put full depth in an appendix.** Write 2-3 sentences of evidence summary per pattern with a link. Avoid leading with quote walls. Source: rampstackco writing-for-decisions-not-decks.md. Counterpoint: dscout warns that removing too much context causes "insight distortion". Link to it rather than cutting it.

**6.7 Embed mixed media where it supports a claim.**
> "Mixed media allows you to show people what happened rather than just telling them."
Source: https://dscout.com/people-nerds/easy-user-research-report-template

---

## 7. Recommendations: actionable, owned, prioritized

**7.1 ★ End every finding with an action and a decider.**
> "End each finding with what the team should do about it, and who decides."
Source: https://dovetail.com/research-report-template/

**7.2 ★ Ban hedge verbs in actions.**
> "Avoid using words like: consider, possibly, maybe, suggest, etc. People can interpret these actions as optional. Instead, use directive terminology, such as: conduct, explore, redesign, etc."
Source: https://handbook.gitlab.com/handbook/product/ux/experience-research/research-insights/

**7.3 ★ Label each insight actionable or informative.** Actionable insights need an action that is "clearly defined, achievable, and directly tied back to the insight". The action type can be "Product change" or "Exploration needed". Informative insights only build knowledge. Source: GitLab handbook (above).
> "Users weren't able to submit a merge request ... because they couldn't find the "Submit" button. They expected it to be located at the top of the page. Action: Iterate on the design to relocate the 'Submit' button to the top of the page and retest (link to Issue # XYZ)."

**7.4 ★ State the consequence of inaction and use HMW.** Each recommendation carries: the insight, an evidence link, the consequence if no action is taken, a priority based on how many users are affected, and a "How Might We" statement. Pair the report with an activation workshop. Source: https://dscout.com/people-nerds/easy-user-research-report-template

**7.5 Recommendation fields.** Action, rationale tied to the insight, P0/P1/P2, owner. Source: https://www.koji.so/docs/ux-research-report-template. agent-studio uses the block `Finding / Evidence / Severity: P0-P2 | Confidence: H/M/L / Recommendation` plus a "prioritized recommendations table": https://github.com/oimiragieo/agent-studio/blob/main/.claude/skills/user-research/SKILL.md

**7.6 ★ Make implications falsifiable, note their cost, and allow "don't act".**
> "Implications should be falsifiable."
> "Synthesis that implies 30 product changes without acknowledging that delivering them all is impossible is not synthesis; it is a wishlist."
> "Some patterns imply not-acting."
Source: rampstackco discovery-research-synthesis SKILL.md

**7.7 ★ Add a decision-input section that validates or challenges the roadmap.**
> "Which roadmap items does the synthesis validate? Which does it challenge?"
> "Which decisions can the team make now with this synthesis as input? Which decisions need more research before making?"
Source: rampstackco writing-for-decisions-not-decks.md

**7.8 Prioritization rubrics.** Frequency × impact matrix with four quadrants (Anthropic PM). Frequency × Severity × Solvability (alirezarezvani). NN/g severity is frequency, impact, persistence and market impact on a 0-4 scale ("4: Usability catastrophe: imperative to fix this before product can be released"): https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/. The Insight → Opportunity table with Impact and Effort columns comes from Anthropic design research-synthesis.

**7.9 Evidence that this needs enforcing.** Across 17 professional teams, only 14 of 84 recommendations (17%) were both useful and usable. The common failures were vagueness, lack of actionability, and fixes that wouldn't improve usability. Source: Molich, Jeffries & Dumas (JUS 2007), summary at https://usability-ed.blogspot.com/2010/10/making-recommendations-usable.html

**7.10 Specific beats generic.**
> "'Improve onboarding' is not actionable. 'Add a progress indicator to the setup flow' is."
Source: Anthropic PM synthesize-research SKILL.md

**7.11 Avoid impractical "whacky design recommendations".** Source: dscout template.

---

## 8. Confidence, numbers and limitations

**8.1 ★ Map confidence to drafting behavior, not just to a label.**
> | High | State directly without strengthening the source. |
> | Medium | Attribute the source or state the limitation. |
> | Low | Keep out of central support; use only as a limitation or verification lead. |
> | Unverified | Exclude as fact and name the missing evidence when the gap matters. |
Source: https://github.com/tyroneross/pyramid-principle/blob/main/skills/pyramid-source-integrity/SKILL.md

**8.2 ★ Treat evaluative words and causal links as claims.**
> "Treat words such as `significant`, `successful`, `only`, `high`, `low`, `improve`, `reduce`, `solve`, and `likely` as claims..."
> "Do not combine two concurrent facts into a causal sentence with `because`, `therefore`, `leading to`... unless the source establishes the relationship."
Source: pyramid-source-integrity SKILL.md

**8.3 ★ Small-n numbers: report counts, not percentages or averages, and add a population caveat.**
> "you have to report individual values, not aggregated statistics such as time averages or success rates."
> "only 1 out of the 6 participants was able to complete this task successfully."
Source: https://www.nngroup.com/articles/metrics-qualitative/. Great Question's auditor cites "40% of users" from 8 people as the canonical misleading example.

**8.4 Per-finding confidence with criteria.** High means strong evidence, Medium means suggestive, Low means early signal. "A finding from 2 interviews is a hypothesis, not a conclusion." Source: Anthropic PM synthesize-research SKILL.md. agent-studio flags single-source findings as Low and uses "Based on N participants..." framing.

**8.5 ★ Name data gaps instead of fabricating.**
> "Fabricating, estimating, or interpolating a required number to complete the deliverable is never sanctioned. A stated gap is a complete answer."
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/ux-research/SKILL.md

**8.6 Conviction without hedge-stacking. Honest uncertainty is a specific claim.**
> "If the data does not support the position, name a smaller position the data does support; do not hedge an oversized claim."
Source: rampstackco common-discovery-synthesis-failures.md. Pyramid adds: "Three weeks of data are insufficient to determine whether the decline is structural or seasonal" is better than "results are mixed" (slide-headline-rules.md).

**8.7 Say who the data represents.** "Indicate who your data represents and communicate the limitations of your findings." Source: https://www.nngroup.com/videos/present-research-responsively/. NJ lists limitations ("sample size, scope, or constraints") as required: https://newjersey.github.io/innovation-ux/how-we-work/research/share-findings/

**8.8 Surface dissent for every finding.** Ask whether any participant contradicted it. Contradictions often reveal segments. Sources: Great Question evidence-integrity-auditor; rampstackco ("Tag dissent and contradictions explicitly").

**8.9 Survey-reporting traps.** Averages without distributions, non-response bias, over-reading small differences, treating Likert as interval data, and correlation versus causation. Use ranges rather than false precision ("1,500-2,500 users monthly"). Source: Anthropic PM synthesize-research SKILL.md

---

## 9. Visualizing findings

**9.1 Put a chart next to the finding it supports, not in a chart appendix.** Source: https://getversive.com/help/build-a-research-report

**9.2 ★ Use visuals that carry argument, not decoration.** Good: pattern → implication → decision diagram, frequency chart, segment comparison table, an evidence map showing source distribution per pattern. Bad: stock images, quote walls without context, word clouds, persona illustrations. About one visual every 2-3 pages. Source: rampstackco writing-for-decisions-not-decks.md

**9.3 "Choose a few standout numbers"** rather than many statistics. Source: https://www.looppanel.com/blog/ux-research-reports

**9.4 The chart headline states the claim the chart shows.** Avoid "shows/indicates" verbs. Source: pyramid slide-headline-rules.md

---

## 10. Linking back to research questions and decisions

**10.1 Open with the question we set out to answer.** Close with recommended next steps. Source: rampstackco ux-research findings template.

**10.2 ★ Add a "So-what" per pattern: the decision it informs.**
> "**6. Name the so-what.** For each implication, the specific decision it informs. 'Should we prioritize the onboarding redesign in Q2?'"
Source: rampstackco discovery-research-synthesis SKILL.md

**10.3 Record hypotheses and out-of-scope items in Background.** Readers can then see what was confirmed or disproved. Source: https://www.koji.so/docs/ux-research-report-template

**10.4 Link actionable insights back to the originating research issue,** and to related insight issues. Source: GitLab handbook.

---

## 11. Length control

**11.1 Length bands by scope.** Full discovery synthesis: 6-12 pages. Single-source: 3-6 pages. Quick-turn: 2-4 pages. Readers "will engage with a 6-page synthesis they can finish in 20 minutes". Source: rampstackco writing-for-decisions-not-decks.md

**11.2 ★ A word limit is a maximum, not a target.**
> "Treat a word limit as a maximum unless the user explicitly requires an exact length."
Don't pad to fill the budget, and don't add common sections that have no content ("Introduction / Next Steps / Conclusion" only when material supports them). Source: pyramid short-form and long-form SKILL.md

**11.3 Fixed micro-limits.** Exec summary is 2-3 paragraphs or 3-5 bullets. Methodology is at most one page. 2-3 quotes per finding. Exec version is one page. Exec update is under 300 words. Sources: Koji, Versive, Anthropic stakeholder-update.

---

## 12. Follow-up and impact tracking

**12.1 ★ Track actionable insights as tickets, and record why each one closed.**
> "When closing an actionable insight issue, it's important to document why it was closed and whether the original action was acted upon."
Scoped labels (`Actionable Insight::Product change`, `::Exploration needed`) count as performance indicators. Source: GitLab handbook.

**12.2 ★ Impact log fields.** Impact note (dated), research activity, focus area, activity type (evaluative / generative / iterative), impact type, scale (individual, project, body of work, org, beyond company).
> "Praise alone is generally not counted. Look for the actions that follow it."
Source: https://sprig.com/blog/framework-for-demonstrating-research-impact

**12.3 Impact ladder to aim for.** Usability fix before launch, then PM cites research in strategy, then exec cites it at an all-hands, then roadmap change, then strategy change. Source: Sprig (above).

**12.4 Outcome metrics by category, and expect lag.** Voice of customer: NPS, CSAT. Product experience: SUS, time on task. Business: conversion, churn. Impact "can take months or even years to appear". Run a three-month pilot of the tracker. Source: https://maze.co/blog/ux-research-impact/

**12.5 Six-month reference test** as a follow-up prompt the skill can schedule.
> "Six months after a synthesis ships, can the team: Name the patterns...? Cite the synthesis in roadmap discussions?"
Source: rampstackco writing-for-decisions-not-decks.md

**12.6 Offer next artifacts after the report.** A follow-up research plan for open questions, a personas or opportunity map, product implications for the roadmap. Source: Anthropic PM synthesize-research ("Review and Extend").

---

## 13. Quality checks before publishing

**13.1 ★ Reader test with a fresh sub-agent.** Predict 5-10 questions readers would ask. Have a context-free sub-agent answer them from the doc alone and check it for ambiguity, false assumptions and contradictions. Fix the gaps it finds.
> "For each question, invoke a sub-agent with just the document content and the question."
Source: https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md

**13.2 ★ Run check, write, recheck as separate passes.** Clear claims before drafting. After drafting, compare "every factual or evaluative clause, headline, table entry, and number" with the cleared claims. "The skill cannot approve its own factual output", so use a separate post-check. Source: pyramid-source-integrity SKILL.md

**13.3 Twelve-point audit** (rampstackco): sequence not skipped, patterns are not truisms, each has a falsifiable implication and a so-what, output is a document, opinionated, review loop done, data gaps named.

**13.4 Review loop before publishing.** Ask participants whether they "recognize themselves". Review with adjacent teams (support, sales). Hold a "challenge the synthesis" session. The owner listens and doesn't defend. Source: rampstackco synthesis-review / failures refs.

**13.5 Pre-return structural checks.** The governing thought comes first. Every heading is a claim. Peers share one role and one order. Each sentence makes one claim. No framework labels ("Answer:", "SCQA:") or self-check notes appear in the output. Source: pyramid long-form and short-form SKILL.md

**13.6 Guardrail for synthetic data.** Never report AI-generated or synthetic-user output as a finding ("nothing it produces should be reported as a finding"). Source: Great Question blog.

---

## 14. Anti-patterns (collected)

| Anti-pattern | Source |
|---|---|
| Opening with methodology or ordering by work sequence | Versive; Koji; Maven/Anderson |
| Quote walls / 60-slide decks ("insight-theater") | rampstackco |
| Raw transcripts plus a tag sheet ("data-dump") | rampstackco; Looppanel |
| Topic-label themes ("Pricing", "Onboarding") | Great Question theme auditor; pyramid headline rules |
| Truism patterns ("users want fast performance") | rampstackco |
| Hedge-stacking ("may sometimes seem to") and optional-sounding actions ("consider") | rampstackco; GitLab |
| Percentages and averages from n<10 | NN/g metrics-qualitative; Great Question |
| Wishlist of 20+ recommendations with no cost or priority | rampstackco |
| Unverified paraphrased quotes; unattributed quotes | Versive; Great Question evidence auditor |
| Causal "because" linking co-occurring facts | pyramid source-integrity |
| Padding to a word count; boilerplate Intro/Conclusion sections | pyramid long-form |
| Standalone exec summary that implies "no further context needed" (dscout's view, which conflicts with Versive and Dovetail. Resolve it by making the summary stand alone and linking to the evidence) | dscout |
| Static document filed and forgotten; no activation step | Koji; dscout |
| Word clouds, stock images, decorative personas | rampstackco |
| Reports "structured for the researcher, not the reader" | Dovetail |
