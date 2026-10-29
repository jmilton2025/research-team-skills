# Catalog: UX research report / readout / findings sources

Scanned 2026-10-29. "Opened" = I read the content myself (file in a git clone, or page text via fetch). "partial" = page opened but the key text was gated or truncated. "blocked" = 403/404/paywall/auth; not cited in patterns.md.

## A. Claude skills / plugins (SKILL.md)

| # | Name | URL | Type | What it covers | Opened? | Quality 1-5 |
|---|------|-----|------|----------------|---------|-------------|
| 1 | discovery-research-synthesis (rampstackco) | https://github.com/rampstackco/claude-skills/tree/main/skills/discovery-research-synthesis | Claude skill + 9 reference files | Research-to-decision synthesis. Frames three outcomes: data-dump, insight-theater, actionable-synthesis. Six-stage sequence ending in a "so-what". "Writing for decisions, not decks". 14 failure modes. Reference-after-shipping test. | yes (cloned) | 5 |
| 2 | ux-research (rampstackco) | https://github.com/rampstackco/claude-skills/blob/main/skills/ux-research/SKILL.md | Claude skill | End-to-end UXR. Includes a findings doc template (question, method, top insights, themes, outliers, next steps) and an "if required data is unavailable" rule. | yes (cloned) | 4 |
| 3 | pyramid-principle plugin (tyroneross): long-form, short-form, presentation, source-integrity, audit | https://github.com/tyroneross/pyramid-principle | Claude plugin (6 skills) | Minto structure for reports and decks. Governing thought first, MECE peer sets, assertion headlines, confidence-to-drafting-action table, claim/source recheck, "no framework labels" rule. | yes (cloned) | 5 |
| 4 | Anthropic design:research-synthesis | anthropics/knowledge-work-plugins: design/skills/research-synthesis/SKILL.md; https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills/research-synthesis | Claude skill (official) | Synthesis output template: exec summary, themes with prevalence and quotes, Insight→Opportunity table (impact/effort), segments, recommendations, methodology notes. | yes (local + cloned) | 3 |
| 5 | Anthropic product-management:synthesize-research | .../product-management/skills/synthesize-research/SKILL.md | Claude skill (official) | 5-8 findings with frequency, impact and confidence (H/M/L). Frequency×impact matrix. Triangulation. Survey-reporting mistakes. Opportunity sizing with ranges. "Each finding should stand on its own." | yes (local + cloned) | 4 |
| 6 | Anthropic product-management:stakeholder-update | .../product-management/skills/stakeholder-update/SKILL.md | Claude skill (official) | Variants by audience (exec, eng, cross-functional, customer, board). Exec version under 200-300 words. G/Y/R honesty. Specific asks with dates. Risk communication in 5 steps. | yes (local + cloned) | 4 |
| 7 | Anthropic design:user-research | .../design/skills/user-research/SKILL.md | Claude skill (official) | Method table. Lists deliverables (synthesis report, highlight reel). Thin on reporting. | yes | 2 |
| 8 | Anthropic internal-comms (3P updates) | https://github.com/anthropics/skills/blob/main/skills/internal-comms/examples/3p-updates.md | Claude skill (official) | Strict 30-60-second exec format (Progress / Plans / Problems, 1-3 sentences each, data-driven). | yes (cloned) | 3 |
| 9 | Anthropic doc-coauthoring | https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md | Claude skill (official) | Three stages, ending in "Reader Testing": a fresh sub-agent with no context answers predicted reader questions to expose blind spots. | yes (cloned) | 4 |
| 10 | agent-studio user-research (oimiragieo) | https://github.com/oimiragieo/agent-studio/blob/main/.claude/skills/user-research/SKILL.md | Claude skill | NN/g-flavored. Finding block = Finding / Heuristic / Evidence / Severity P0-P2 / Confidence / Recommendation. "Based on N participants" framing. Single-source findings flagged as low confidence. | yes (cloned) | 3 |
| 11 | ux-researcher-designer (alirezarezvani) | https://github.com/alirezarezvani/claude-skills/blob/main/product-team/skills/ux-researcher-designer/SKILL.md | Claude skill | Personas and journeys. Priority Score = Frequency × Severity × Solvability. Findings checklist. | yes (grep only) | 2 |
| 12 | Great Question Claude skills (blog + skill pages: readout, theme-quality-auditor, evidence-integrity-auditor) | https://www.greatquestion.com/blog/claude-skills-ux-research-assistant ; https://www.greatquestion.com/resources/claude-skills-library/theme-quality-auditor ; https://www.greatquestion.com/resources/claude-skills-library/evidence-integrity-auditor | Vendor Claude skills | Readout by audience (PM / design / leadership). Theme auditor flags topic-label themes. Evidence auditor verifies quotes against transcripts, flags thin evidence, small-sample %, missing dissent. "Signals worth investigating" section. | partial (descriptions only; SKILL.md gated behind a download form) | 4 (ideas) |
| 13 | Tessl review of rampstackco ux-research | https://tessl.io/registry/skills/github/rampstackco/claude-skills/ux-research/review | Skill review | Meta-feedback: avoid restating warnings, move templates to references, watch for trigger overlap. | yes | 2 |
| 14 | teslasoft research skill (skills.sh) | https://skills.sh/teslasoft-de/claude-skills-marketplace/research | Claude skill listing | Generic UXR skill. Reporting rules were not visible. | partial | 1 |
| 15 | research-brief (Mikefluff, via claudskills) | https://claudskills.com/skills/research-brief/ | Claude skill listing | 200-1000 word brief: TL;DR, cited facts, quotes, angles, open questions. | partial | 2 |

## B. Prompts (GPT / generic)

| # | Name | URL | Type | What it covers | Opened? | Quality |
|---|------|-----|------|----------------|---------|---------|
| 16 | AI Design Patterns: user-research-synthesis prompt | https://ai-design-patterns.pages.dev/prompts/user-research-synthesis | Prompt | 5-section report. Pain points ranked by severity. Recommendations with success metrics. Usage rule: only for already-coded mixed sources. | yes | 2 |
| 17 | PromptHub: Research Findings Executive Briefing Crafter | https://prompthub-local-1.pages.dev/en/templates/research-findings-executive-briefing-crafter/ | Prompt | Variables: SOURCE_MATERIAL, AUDIENCE, DECISION_CONTEXT, TONE, LENGTH. Prompt body gated. | partial | 2 |
| 18 | dev.to "35 ChatGPT prompts for UX researchers" | https://dev.to/clawgear/35-chatgpt-prompts-for-ux-researchers-user-interviews-synthesis-and-stakeholder-reports-that-2kp1 | Prompt list | Prompts behind a paid toolkit. | partial (paywalled) | 1 |

## C. Practitioner guidance / frameworks

| # | Name | URL | Type | What it covers | Opened? | Quality |
|---|------|-----|------|----------------|---------|---------|
| 19 | GitLab Handbook: Research insights | https://handbook.gitlab.com/handbook/product/ux/experience-research/research-insights/ | Handbook | Actionable vs. informative insights. Three parts: insight / why / action. Banned hedge verbs. "ACTIONABLE:" prefix. Issue + scoped label tracking. Document why an insight was closed. | yes | 5 |
| 20 | Dovetail: research report template | https://dovetail.com/research-report-template/ | Vendor guide | Six sections. 3-5 findings (claim + evidence + why it matters). "Opinion with formatting". End each finding with what to do and who decides. Under-one-minute headline test. | yes | 5 |
| 21 | Dovetail: report prompt guide | https://docs.dovetail.com/help/docs/report-prompt-guide | Vendor AI prompt guide | Organize by theme, not by interview. 2-3 quotes per theme from different participants. Source tags [Interview]/[Support]/[Review]. Don't request info that isn't in the data. | yes | 4 |
| 22 | AnswerLab: insights vs findings | https://answerlab.com/insights/what-are-research-insights-what-makes-them-different-from-findings | Practitioner article | Findings = what / shallow why. Insights = deep why. Recommendations = solution-centric. Evaluative studies usually need only findings. Insight in 1-2 sentences, evidence separate. | yes | 5 |
| 23 | NN/g: Data vs findings vs insights | https://www.nngroup.com/articles/data-findings-insights-differences/ | NN/g article | Definitions. Insights connect to recommendations. Triangulation. "Insights are not meant to be prescriptive." | yes | 4 |
| 24 | NN/g: Metrics in qualitative studies | https://www.nngroup.com/articles/metrics-qualitative/ | NN/g article | Report small-n numbers anecdotally ("1 out of 6"), not as averages or %, with a population caveat. | yes | 5 |
| 25 | NN/g: Severity ratings | https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ | NN/g article | Frequency × impact × persistence (+ market impact). 0-4 scale. | yes | 4 |
| 26 | NN/g: Present research results responsibly (video page) | https://www.nngroup.com/videos/present-research-responsively/ | NN/g video summary | State who the data represents and the limitations. | partial (summary only, no transcript) | 3 |
| 27 | Koji: writing insight statements | https://www.koji.so/docs/writing-insight-statements | Vendor guide | Four insight formulas (tension, behavioral, JTBD, emotional arc). Data→finding→insight ladder. Supported by 3 or more participants. End with "This means...". | yes | 4 |
| 28 | Koji: UX research report template | https://www.koji.so/docs/ux-research-report-template | Vendor guide | Sections. Findings organized by goal (evaluative) or theme (generative). Severity Critical/Major/Minor. Recommendation = action + rationale + P0-P2 + owner. Exec / product / design variants. | yes | 4 |
| 29 | Versive: build a research report stakeholders will read | https://getversive.com/help/build-a-research-report | Vendor guide | Finding / evidence / action block. Exec summary = 3-5 bullets of finding + recommendation that stand alone in 90 seconds. Charts next to their finding. Order by decision impact. | yes | 5 |
| 30 | NJ Office of Innovation: share findings | https://newjersey.github.io/innovation-ux/how-we-work/research/share-findings/ | Gov playbook | Required elements, including limitations. Anonymized quotes. Format by audience. Screen-reader-friendly outputs. | yes | 3 |
| 31 | Smart Interface Design Patterns (Vitaly Friedman): data, findings, insights | https://smart-interface-design-patterns.com/articles/data-findings-insights/ | Article | What happened + Why + So what. Hindsights vs foresights. Worked example ladder. | yes | 4 |
| 32 | Fountain Institute: writing user insights | https://thefountaininstitute.com/blog/writing-user-insights | Article | "I saw + I know" formula. 5-step insight card. "Not an insight" list. An insight with only one possible solution is a solution idea. | yes | 4 |
| 33 | dscout People Nerds report template (Nikki Anderson) | https://dscout.com/people-nerds/easy-user-research-report-template | Practitioner template | Recommendation = insight + evidence link + consequence of inaction + priority by users affected + HMW. Activation workshop. Format by stakeholder involvement. "Insight distortion". | yes | 5 |
| 34 | Maven: Pyramid Principle reporting for UR (Nikki Anderson) | https://maven.com/user-research-strategist/pyramid-principle-reporting-for-user-research | Course page | Answer-first instead of background→methods→findings. Pick supporting reasons, don't list every finding. Exec summary readable in 2 minutes. | yes (course outline only) | 3 |
| 35 | Looppanel: UX research reports | https://www.looppanel.com/blog/ux-research-reports | Vendor guide | Structure. "A few standout numbers". Avoid data dump / chart collection. | yes | 2 |
| 36 | Library-d7m: BLUF & inverted pyramid | https://library-d7m.pages.dev/communication-framework/writing-and-structure/bluf-and-inverted-pyramid | Writing guide | BLUF mechanics (find the one sentence, move it up, delete setup). When not to use BLUF. | yes | 4 |
| 37 | Maze: UX research impact framework | https://maze.co/blog/ux-research-impact/ | Vendor guide | Impact tracker fields (outcome, impact size, source files, approach, lead, product area). Outcome categories with metrics. Expect lag of months to years. | yes | 4 |
| 38 | Sprig: framework for demonstrating research impact (Sosik / Smith) | https://sprig.com/blog/framework-for-demonstrating-research-impact | Vendor guide | Six tracking fields. Impact types. Scale ladder. "Praise alone is not counted." Ranked impact ladder. | yes | 4 |
| 39 | Molich, Jeffries & Dumas, "Making usability recommendations useful and usable" (JUS 2007), via blog summary | https://usability-ed.blogspot.com/2010/10/making-recommendations-usable.html | Research summary | Only 14/84 (17%) of professional recommendations were both useful and usable. Failure modes: vague, not actionable, wouldn't improve usability. | yes (summary only) | 3 |

## D. Blocked / not opened (not cited in patterns.md)

| Name | URL | Reason |
|------|-----|--------|
| Molich et al. full PDF | https://uxpajournal.org/wp-content/uploads/sites/7/pdf/useful-usable.pdf | Served a 278-byte HTML stub, not the PDF |
| UXPA magazine "Recommendations on Recommendations" | https://oldmagazine.uxpa.org/?p=5987 | 403 |
| uxdesign.cc "Tracking the impact of UX Research: a framework" | https://uxdesign.cc/tracking-the-impact-of-ux-research-a-framework-9e8b8f51599b | 403 |
| uxdesign.cc "wrong wording when talking about user findings" | https://uxdesign.cc/you-might-be-using-the-wrong-wording-when-talking-about-user-findings-480b70d75bf3 | 403 |
| Daniel Pidcock, Atomic Research (Medium) | https://medium.com/@danielpidcock/the-difference-between-atomic-research-and-atomic-research-22d2cb0227a8 | 403 |
| Great Question skills library index | https://greatquestion.co/resources/claude-skills-library | 404 |
| Great Question stakeholder-readout-generator | https://greatquestion.co/resources/claude-skills-library/stakeholder-readout-generator | 404 |
| NN/g "no numbers in qualitative studies" (guessed URL) | https://www.nngroup.com/articles/no-numbers-qualitative-studies/ | 404 (covered instead by #24) |
| OpenRoster-ai/awesome-openroster ux-researcher | https://github.com/OpenRoster-ai/awesome-openroster | git clone asked for auth (private, renamed, or missing) |
| GitHub API for anthropics repos | api.github.com | Session-scoped 403; used anonymous git clone instead |
