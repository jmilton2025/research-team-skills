# Reusable patterns for a research-plan skill

Every excerpt below is verbatim from a source I opened (see `catalog.md`) and runs 5 lines or fewer. The ideas are sorted by theme and, within each theme, roughly by how specific and non-obvious they are.

Some entries carry a "(gap?)" flag. It comes from a keyword check of the user's own `skills/research-plan/` (SKILL.md plus references) that found no or very weak matches. It is a hint to check, not a verdict.

---

## 1. Intake and triage: is this a research question at all?

**1.1 Triage the request before planning it. Some requests belong in analytics, and some are decisions already made.** (gap?)
Have the skill split a raw stakeholder ask, even a Slack thread, into three parts: what a study can answer, what needs instrumentation or data, and what is really a product decision. If nothing is left for research, it should say so with reasoning the user can forward.
> "When the question isn't researchable it says so early. Some questions belong in your analytics, and some are decisions the team already made and would like cover for."
> "it separates the parts a study can answer from the parts needing instrumentation or a product decision. When nothing is left for research it says so, with reasoning you can forward to the stakeholder."
Source: https://www.greatquestion.com/resources/claude-skills-library/research-brief-writer

**1.2 Score priority and support level at intake, one answer per question.**
GitLab's Research Issue scores every request on 6 dimensions, each with 5 levels: business impact if not done, users affected, whether it blocks a decision, timeline flexibility, whether alternatives exist, and strategic alignment. A second rubric decides how much researcher support the request gets: research type, whether a non-researcher could run it, multiple methods, and confidence in the solution.
> "3. Is this blocking any immediate decisions? … 1. Blocking critical launch … 5. No specific decision"
> "5. Are there alternative ways to get this information? … 1. No alternatives exist … 5. Many alternatives"
Source: https://gitlab.com/gitlab-org/ux-research/-/blob/master/.gitlab/issue_templates/Research%20Issue.md

**1.3 Researcher to-do: close the request with "will not do" when research isn't needed.**
The template makes "not needed" a first-class outcome rather than a failure.
> "If the research is not needed, apply the ~"closed::will not do" label, and close the issue."
Source: same GitLab template.

**1.4 Narrow evaluative intake: name the 1–3 things you're unsure about and why now.**
For fast evaluative studies, require the requester to list the specific aspects they're unsure about, and to say why validation is needed now.
> "Clear description of the design/concept, highlighting 1-3 specific aspects you're unsure about"
> "Context: Why does this need validation now? What's driving the urgency?"
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/rapid-validations/

**1.5 Goal-setting questions that force a definition of "done".**
> "How will I know when I've learned it? What must be true in order for this research to be considered "done"?"
> "What decision will this research enable? … know what you want people to be able to do with the answers to your research question."
Source: https://www.userinterviews.com/ux-research-field-guide-chapter/create-user-research-plan

**1.6 Ask for context in pieces, because the AI won't ask the right questions by itself.**
NN/g's main finding is that one-shot "generate a research plan" prompts produce generic output. The plan should be built piece by piece, in dependency order.
> "Don't expect the AI to ask you the right questions in order to get a comprehensive outcome."
> "deconstruct the plan into parts and have the AI chatbot tackle each part individually."
Source: https://www.nngroup.com/articles/plan-research-ai/
The order NN/g gives: context, then research questions, then methods mapped to each RQ, then inclusion criteria, then screener, tasks and guide. Inclusion criteria come only *after* methods, and the screener only *after* the inclusion criteria.

---

## 2. Decision framing

**2.1 Name the decision and its owner, with a bad example to calibrate against.**
> "Good example: Owner: Custom Models Team / Decision: Determine which specific external data sources to include in a curated MCP integration list for iteration 1"
> "Bad example: Owner: / Decision: Help us make decisions on designing the side bar."
Source: GitLab Research Issue template (URL above).

**2.2 Pick one main impact type.**
The options are decision impact (strategy or plan change, product or design change), knowledge impact (gap filled, perception captured, next opportunity) or UXR-maturity impact. Choosing one keeps "knowledge" studies honest about not being tied to a decision.
> "What is the type of **main** impact intended? Select the **ONE** option that best fits the outcomes."
Source: GitLab Research Issue template.

**2.3 Classify the decision level, which then drives how open the questions should be.**
User Interviews uses four levels. **Vision** is big-picture and open-ended. **Strategy** means the problem is known and you are deciding the approach. **Definition** asks how solutions behave in context, with more focused questions. **Evaluation** looks at use of the existing product.
> "Within any organization or product team, there are four levels of decision-making, which act a bit like a funnel."
Source: https://www.userinterviews.com/blog/a-framework-for-decision-driven-research

**2.4 Write each objective *as* the decision.**
> "Write each objective as the decision it informs—"decide whether to rebuild onboarding" beats "understand onboarding.""
Source: https://dovetail.com/ux-research-plan-template/
> "**Objective [N]:** Understand [specific thing] so we can [decision this informs]."
Source: https://github.com/mohitagw15856/pm-claude-skills/blob/HEAD/plugins/pm-design/skills/ux-research-plan/SKILL.md

**2.5 Anchor the timeline to the decision date, not to fieldwork.**
> "If your research is meant to inform a decision, note when the team anticipates that it will make that decision (for example, is your research due before the next quarterly planning meeting?)"
Source: https://guides.18f.org/ux-guide/research/plan/

**2.6 Tie the plan to the delivery roadmap, and don't out-research the team.**
> "Do not do lots of research that the team cannot respond to, or get left behind if they're making quick progress."
Source: https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service

---

## 3. Goals, research questions and hypotheses

**3.1 Verb rules for goals. Ban "understand" and "explore".** (gap?)
18F requires output verbs. GitLab allows "understand", so there is a real disagreement here; 18F's rule is the stricter, more testable one.
> "use verbs that specify the output like "describe," "evaluate," "quantify," or "identify." Avoid vague words like "understand" or "explore.""
Source: https://guides.18f.org/ux-guide/research/plan/

**3.2 Cap objectives, and explain the cap through guide length.** (gap?)
> "Create no more than 4 objectives per research effort. … each objective will represent up to a dozen questions/tasks in your discussion guide."
> "It's a good rule of thumb to not have the user session last longer than 1 hour. Our typical research sessions at GitLab last 30-45 minutes."
Source: https://handbook.gitlab.com/handbook/product/ux/ux-research/defining-goals-objectives-and-hypotheses/
Other caps: "Limit to three objectives. More than three objectives means the study is trying to do too much. Split it into two studies." (https://designops-tools.pages.dev/documents/ux-research-plan/). Dovetail allows 1–2 objectives and 3–5 RQs.

**3.3 Derive goals and objectives from a brain-dump, in a fixed order.**
GitLab's chain runs: problem, then "Questions we need answers to" (a brain-dump, *not* interview questions), then hypothesis, then a single goal, then up to 4 objectives clustered from the brain-dump themes.
> "This is meant to be a brain dump … These aren't the questions you'll directly ask users"
> "Review the list of the 'Questions we need answers to' and identify the themes you see there."
Source: GitLab goals/objectives handbook (URL above).

**3.4 A hypothesis formula with a built-in success measure, and a rule for when *not* to write one.**
> "We believe [doing this] for [these people] will achieve [this outcome]."
> "will achieve [this outcome] is where you should document your measure of success."
> "If you're struggling to articulate your assumptions about users, it's probably better to start with developing a better understanding of users first, rather than forming weak hypotheses"
Source: GitLab goals/objectives handbook.

**3.5 RQ vs interview question, with a worked example.** (gap?)
> ""Why do trial users abandon setup?" is a research question; "Walk me through your setup" is an interview question that helps answer it."
Source: https://dovetail.com/ux-research-plan-template/

**3.6 Weak-to-better RQ rewrite table, worth borrowing as few-shot examples.**
> "| "Do users like our onboarding?" | "Where in onboarding do new users feel uncertain about whether to continue?" |"
> "| "Why is conversion low?" | "What's the user mental model when they reach the pricing page, and where does it diverge from our intent?" |"
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/ux-research/SKILL.md

**3.7 An RQ must not assume the solution, and must be ethical.**
> "Bad question: How do we get unemployed adults interested in our website? (This question is bad because it isn't directly focused on users and their goals; it also assumes that a website is the right solution"
> "consider whether answering your research questions would put participants in a compromising position."
Source: https://guides.18f.org/ux-guide/research/plan/

**3.8 Lint RQ wording: open words beat closed words.**
> "broad, open questions (like 'who', 'what', 'when', 'where' or 'why') are more helpful than narrow or specific ones (like 'do', 'have', 'will' or 'can')"
Source: https://www.gov.uk/service-manual/user-research/capturing-research-questions

**3.9 Treat the study as investigation, not validation.**
> "starting with a question is the best way to ensure you're using your research to investigate rather than to validate. … doing user research to prove you're right is not a good use of anyone's time or energy."
Source: User Interviews plan chapter (URL above).

---

## 4. Existing evidence and assumptions (before choosing a method)

**4.1 Sort what the team believes into facts, opinions and guesses.** (gap?)
> "we typically hold a kickoff brainstorm session where we start to tease apart: facts, opinions & guesses."
Source: https://www.userinterviews.com/blog/a-framework-for-decision-driven-research

**4.2 Turn unfounded assumptions into research questions explicitly.**
> "In the workshop be careful to turn any unfounded assumptions and opinions into research questions."
Source: https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service

**4.3 Triage assumptions by impact × risk, where risk = (1 − confidence) × effort.**
The four quadrants: defer, proceed, reject, and test. Only the high-impact, high-risk quadrant gets a study. Assumptions are generated from PM, designer and engineer perspectives across Value, Usability, Viability and Feasibility.
> "**Risk**: Defined as (1 - Confidence) × Effort"
> "**High Impact, High Risk** → Design an experiment to test it"
Source: https://github.com/phuryn/pm-skills/blob/HEAD/pm-product-discovery/skills/prioritize-assumptions/SKILL.md

**4.4 Name internal evidence sources, including front-line teams.**
> "One of the richest mines of customer information (and one that I see frequently overlooked by researchers and designers) is your own team. Folks from customer success, operations and support"
Source: User Interviews Decision Driven Research (URL above).

---

## 5. Method selection logic

**5.1 Recommend a method *and* name the alternatives it rejected, so the choice can be argued.** (gap? The user's skill mentions "alternative" only 4 times.)
> "It proposes a method and explains why that method suits the question. The alternatives it passed over are named alongside it, so you can argue with the choice in review."
Source: Great Question research brief writer (URL above).

**5.2 State what each method will and won't tell you.** (gap? "limitation" appears only 2 times.)
> "**What this method will and won't tell us:** - **Will tell us:** [...] - **Won't tell us:** [What's out of scope — be honest about limits]"
Source: pm-claude-skills ux-research-plan (URL above).
rampstack gives a ready per-source list, for example interviews do not surface "What users actually do in practice … Pricing willingness to pay (interview answers about price are notoriously unreliable)." Support tickets do not surface "The experience of users who did not contact support (silent struggling)." (https://github.com/rampstackco/claude-skills/blob/HEAD/skills/discovery-research-synthesis/references/research-types-and-when-each-fits.md)

**5.3 Three selection axes beyond qual vs quant.**
GitLab uses (a) *detail vs frequency*: do you need to understand the problem, or measure how common it is? (b) *user characteristics and usage over time*: roles, and learning curves that call for multiple intervals. (c) *design fidelity*.
> "The fidelity of research insights follows the fidelity of design."
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/choosing-a-research-methodology/

**5.4 Map each method to the specific RQs it answers.**
> "cite which research questions would be answered by which research method if you suggest multiple methods."
> "AI may suggest interviews and focus groups even for research questions better suited to a behavioral research method."
Source: https://www.nngroup.com/articles/plan-research-ai/

**5.5 Don't triangulate by reflex.**
NN/g pushes back on AI's habit of always recommending multiple methods. OpenRoster sets "never draw conclusions from a single data source" as a rule. The plan should justify a multi-method design instead of defaulting to one.
> "Often, these tools will suggest various methods and suggest you triangulate data from multiple sources. This approach is not always needed."
Source: NN/g plan-research-ai.

**5.6 Question type to method, as a short heuristic.**
> "**Why/how questions** → qualitative … **How many/how often** → quantitative … **Does X work better than Y** → comparative usability test or A/B test … **Unknown problem space** → generative research"
Source: https://github.com/OpenRoster-ai/awesome-agents/blob/HEAD/design-ux-researcher/skills/SKILL.md

**5.7 Keep generative and evaluative work separate in one plan.**
> "Do not design a plan that mixes generative and evaluative research without clearly separating them"
Source: pm-claude-skills ux-research-plan.

**5.8 Recommend within stated constraints, or say you're unconstrained.**
> "Name your constraints in the request, say an unmoderated-only quarter or a panel with no enterprise admins in it, and the recommendation gets made inside those limits. Left unconstrained, it recommends what the question deserves"
Source: Great Question research brief writer.

---

## 6. Sample, recruiting and participant criteria

**6.1 Sample size with a named source and a paste-ready rationale, reported as counts.** (gap? Saturation and source names appear only 2 times.)
> "Every answer names its source, such as Hennink and Kaiser's review of interview sample sizes or Guest, Namey and Chen's saturation rule. For qualitative work it gives a starting range to reason from, not a requirement."
> "A paste-ready rationale paragraph for your research plan that says findings will be reported as counts."
> "It won't run significance tests on interview data. … purposive samples don't support inference to a population"
Sources: https://greatquestion.co/blog/claude-skills-ux-research-assistant ; https://www.greatquestion.com/resources/claude-skills-library/sample-size-planner

**6.2 Size the sample per segment, not in total.**
> "Qualitative: 5–8 per distinct user segment for theme saturation … Survey/quantitative: calculate via power analysis (state α, power, expected effect size)"
Source: OpenRoster ux-researcher (URL above).

**6.3 Run more small rounds rather than one big round.**
> "You'll usually need between 4 and 8 participants for each round … If you need more participants to get clear findings, do more rounds rather than one big round. That way you can adjust after each round."
Source: https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service

**6.4 Over-recruit for no-shows, with explicit math.** (gap? "no-show" and "over-recruit" appear only 2 times.)
> "**Recruit volume:** Plan for 20 to 30 percent no-show. Recruit 7 to schedule 5."
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/ux-research/SKILL.md

**6.5 Build a screener table with must-have, nice-to-have and disqualify-if columns, tagging each answer.**
> "| Criterion | Must Have / Nice to Have | Disqualify if |"
Source: pm-claude-skills ux-research-plan.
> "- Daily [QUALIFY] - Weekly [QUALIFY] - Monthly [CONSIDER] - Rarely/Never [DISQUALIFY]"
Source: https://github.com/prorise-cool/prorise-claude-skills/blob/HEAD/.claude/skills/design-specialist/references/domains/ux-research/user-research-planning/SKILL.md

**6.6 Screener hygiene: disguise the target, include distractors, ask behaviour before demographics, and check articulation.**
> "Include multiple-choice questions and answer options that might disguise what the study is about and who I am looking to recruit."
Source: NN/g plan-research-ai.
> "Filter by user behavior > demographics … Ask the big, disqualifying questions early … Include open-ended questions to screen for articulation"
Source: User Interviews plan chapter.

**6.7 Treat participant safety as a recruitment criterion.**
> "Mitigate the chances of triggering a trauma response by not recruiting people at their most vulnerable."
> "having them observe usability tests and interviews with colleagues might cause participants anxiety or diminished honesty"
Source: https://guides.18f.org/ux-guide/research/plan/

**6.8 Plan inclusion per round, or plan dedicated rounds when per-round inclusion isn't possible.**
> "If your service has a broad audience, you should include disabled users and people who may need support to use your service in every round of research."
Source: GOV.UK plan page.

**6.9 Gate recruitment on a reviewed screener.**
> "If internal or external recruitment is needed, create a recruiting request issue **ONLY AFTER** your screener has been reviewed by the UX Researcher."
Source: GitLab Research Issue template.

---

## 7. Timeline and logistics

**7.1 Analysis-time ratios.** (gap? No match found for analysis time.)
> "A safe estimate for research analysis is about twice as long as the research itself" (18F)
> "For every 2 hours of research, you should do 1 hour of analysis." (GOV.UK, plan-a-round)
The two sources differ: 2:1 analysis to fieldwork versus 1:2. A skill could cite both and default to 18F's more conservative figure.
Sources: https://guides.18f.org/ux-guide/research/plan/ ; https://www.gov.uk/service-manual/user-research/plan-round-of-user-research

**7.2 Session caps per day and buffers.**
> "plan for no more than 6 one-hour sessions a day / allow at least 15 minutes between sessions" (lab)
> "plan for no more than 4 one-hour sessions a day / allow at least 30 minutes between sessions, plus travelling time" (field)
Source: GOV.UK plan-a-round.

**7.3 Sample timeline with phase durations, to borrow as a default shape.**
> "Recruiting and scheduling 1 week · In-depth interviews (remote) 1 week · Initial analysis 4 days · Collaborative analysis 2 days · Communicating the results 2 days"
Source: 18F plan page.

**7.4 Mark the dependencies that usually slip, such as procurement and recruiting lead times.**
> "A timeline shape from kickoff to readout, marking the dependencies that usually slip." (Great Question brief writer)
> "Start booking facilities and sending briefs to suppliers as soon as you can. Do not wait until you've finalised your plans" (GOV.UK)

**7.5 Pilot sessions as an explicit step.** (gap? No match found for "pilot".)
> "**Pilot.** Run 1 to 2 sessions before the main batch. Refine the guide."
Source: rampstack ux-research. GOV.UK also says: "Run through the test tasks on the day before the research."

---

## 8. Stakeholder alignment and team participation

**8.1 Set observation quotas.**
> "everyone should observe at least 2 hours of research every 6 weeks"
Source: GOV.UK plan page.

**8.2 Assign roles per stage: plan, do, analyze, share.**
> "determine which members of your partner agency's team will help at each stage of the research process (that is, plan; do; analyze, synthesize, and share)."
> "People who help accomplish the research are more likely to agree with its outputs."
Source: 18F plan page.

**8.3 Run a team research-question workshop, then dot-vote.**
> "putting a dot on the 5 questions they think need answering first"
> "write a summary question for each group of similar questions"
Source: GOV.UK capturing-research-questions.

**8.4 Add an observer role and observer guidance.**
GOV.UK defines an "observation room manager" who keeps observers taking notes and coordinates same-day analysis. NN/g recommends adding observer guidance on how to take notes without interrupting.
Sources: GOV.UK plan-a-round; https://www.nngroup.com/articles/pm-research-plan/

**8.5 Split the brief and the plan by the agreement each one wins.**
> "the brief is the shorter document that wins agreement on why the study exists, and the plan carries the operational detail once that agreement is in hand."
Source: Great Question brief writer. Dovetail puts it differently: "A brief is the request … A plan is the response."

---

## 9. Risks, assumptions and limitations

**9.1 Risks to conclusiveness, each with a mitigation.** (gap? No match found for "inconclusive".)
> "Risks: what could leave the study inconclusive, and what to do about each one."
Source: Great Question brief writer.

**9.2 Pre-commit to how inconclusive results will be handled.**
> "When data is ambiguous or sample is insufficient, state limitations clearly and recommend follow-up study rather than overstating confidence"
Source: OpenRoster ux-researcher.

**9.3 Pre-plan segment coverage gaps.**
rampstack's synthesis reference describes "segment under-representation" as a common failure, where "the easiest-to-recruit users are usually a specific segment". A plan can prevent this by naming which segments the decision depends on and which ones it will *not* cover. It can also scope the decision to the segments the data will cover.
> "Recommend either separate research for the missing segments or scoping the decision to the segment the data covered."
Source: https://github.com/rampstackco/claude-skills/blob/HEAD/skills/discovery-research-synthesis/references/when-to-gather-more-data.md

**9.4 Fill gaps with marked assumptions instead of blocking.**
> "fill each gap with a reasonable assumption marked *(assumed, confirm)* and list those assumptions at the end. Ask a question first only when the core subject itself is missing"
Source: pm-claude-skills ux-research-plan.

**9.5 Never fabricate data; a stated gap is a complete answer.**
> "Fabricating, estimating, or interpolating a required number to complete the deliverable is never sanctioned. A stated gap is a complete answer."
Source: rampstack ux-research.

**9.6 Run a bias session at planning time.**
18F runs a "frames of reference bias identification workshop" so the team "can avoid influencing the evidence they gather based on the things they presume to be true". It also lists the trust and power dynamics that change how willing participants are to share.
Source: 18F plan page.

---

## 10. Success criteria and impact tracking

**10.1 Track decision impact after the readout; research that changes nothing has failed.**
> "**Track impact.** Did decisions change because of the research? If not, the research failed regardless of quality."
Source: rampstack ux-research.

**10.2 Put a "What did we learn?" box at the top of the plan, filled after the study.**
The plan document doubles as the outcome record. GitLab also attaches a `decision::pending` label to the request.
> "#### What did we learn? <!-- Add information for this section after the research is complete. -->"
Source: GitLab Research Issue template.

**10.3 Fixed evaluative metrics plus a go/no-go.**
For concepts: value-fit, workflow-fit and understandability. For designs: perceived efficiency, task success or first click, and overall satisfaction. The output is "Go/no-go guidance based on quantified metrics".
Source: GitLab Rapid Validations.

**10.4 Each recommendation carries evidence, a success metric and a retest plan.**
> "Evidence basis (e.g., "7/10 participants failed Task 2 …") - Success metric (e.g., "Task 2 completion rate from 30% → 75%") - Measurement plan (when and how to retest)"
Source: OpenRoster ux-researcher.

**10.5 Set expectations about what this study will *not* settle.**
> "if you're in the discovery phase … make it clear that the insights from this research will inform product vision—but that further research will be needed to validate design decisions"
Source: User Interviews plan chapter.

---

## 11. Output structure

**11.1 Keep the plan short and link out to the instruments.**
> "One to two pages. A plan is a working agreement, not a thesis—if stakeholders can't read it in five minutes, they won't. Link out to supporting material like discussion guides and screeners rather than embedding them."
Source: Dovetail template.

**11.2 A sections checklist that includes ethics and team participation.**
18F's 9 sections: Background, Goals, Research questions, Methods, Team participation, Timeline, Participants and recruiting, Ethics considerations, and Outputs and outcomes. Background explicitly includes "shared beliefs or forces motivating the research itself".
Source: 18F plan page.

**11.3 Record subgoals honestly, such as coaching or capability-building.**
> "Explicitly stating these kinds of subgoals helps provide an honest account of the coaching work that the team will undertake alongside the research itself."
Source: 18F plan page. GitLab's version is the "Impact on UXR maturity" option.

**11.4 Plan the share-out as part of the plan, in a ready format.**
GitLab ships a Slack report template inside the intake issue with these fields: Project Title, Key Insights, links to the report, issue and recording, and Next steps.
Source: GitLab Research Issue template.

---

## 12. Quality checks and lints (things a skill can check automatically)

**12.1 Link each artifact to a peer-review checkbox.**
> "- Recruitment screener: - [ ] Peer reviewed by UXR / - Research plan: - [ ] Peer reviewed by UXR … - Prototype: - [ ] Preflight checked"
Source: GitLab Research Issue template.

**12.2 Specific AI failure modes to lint for in tasks and screeners.**
> "Using words that appear in the interface in task instructions (priming)"
> "Creating task instructions that ask users to imagine they are someone that they are not"
> "Not including distractor options in screening questionnaires"
> "Using overenthusiastic marketing language in recruitment materials"
Source: NN/g plan-research-ai.

**12.3 Use checker skills separate from generator skills.**
Great Question's newer skills "don't produce new work; they check work you already have". One is a *task scenario linter* and another a *screener porter*, which checks a screener before launch "such as questions that are easy to guess or sensitive questions with no consent". Each "ships with a small script that does the checking the same way every time".
Source: https://greatquestion.co/blog/claude-skills-ux-research-assistant

**12.4 Plan quality checklist, as items an agent can verify.**
> "- [ ] Research objectives map to real decisions - [ ] Discussion guide opens broad before going specific - [ ] Screener criteria are specific enough … - [ ] Tasks (if usability) are written from the user's perspective"
Source: pm-claude-skills ux-research-plan.

**12.5 A skill-quality rubric to evaluate the skill itself.**
tessl scores skills on Conciseness, Actionability, Workflow Clarity and Progressive Disclosure. Anthropic's `user-research` scored 64% because "techniques and artifacts are named rather than operationalized". rampstack scored 88% on content because of "explicit validation checkpoints and feedback loops".
Source: https://tessl.io/registry/skills/github/anthropics/knowledge-work-plugins/user-research/review

---

## 13. Anti-patterns worth encoding as refusals or warnings

- **Research without a decision; findings have no home.** (rampstack ux-research)
- **Planning the plan as an afterthought:** "Log deviations. If reality diverges from the plan (participant no-shows, session changes), document it here." This is an anti-pattern because most plans are never updated after the study. (DesignOps Tools; NN/g says the same: update the plan after the study.) (gap? No match found for "deviation".)
- **Hypothetical questions:** "Would you use a feature that...?" is a poor predictor of behaviour. (rampstack)
- **"Interviewing your hypothesis":** only asking questions that confirm what you already think. (rampstack)
- **Recruiting "anyone willing" or professional participants.** (rampstack)
- **A one-shot generic plan from a bare prompt.** (NN/g)
- **Presenting a range as a requirement, or a percentage from 8 interviews.** (Great Question sample size planner)
- **Too many objectives,** meaning more than 3–4; split the study. (GitLab, DesignOps)
- **Methods chosen before the question:** "If you jump directly to methodology, you may end up stunting your study before it's even started." (User Interviews)

---

## Source disagreements to resolve in the skill

| Topic | Position A | Position B |
|---|---|---|
| Goal verbs | 18F: avoid "understand" and "explore" | GitLab: "Always start goals using a verb such as identify, understand, learn, gauge" |
| Objective cap | Dovetail: 1–2 | DesignOps: 3 primary + 3 secondary; GitLab: no more than 4 |
| Analysis time | 18F: about 2× fieldwork | GOV.UK: 1 hr per 2 hrs of research |
| Qual interview n | GOV.UK: 4–8 per round | rampstack: 8–15 per cycle; Great Question: sourced range per segment |
| Triangulation | OpenRoster: never rely on one source | NN/g: multiple methods are "not always needed" |
