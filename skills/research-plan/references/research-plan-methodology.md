# Research Plan Methodology Reference

Loaded on demand when methodology depth is needed. Cite these sources in the prose output of the plan when researchers push back, when stakeholders question sample size, or when method selection is non-obvious.

---

## 1. Canonical Section Comparison

Three top references converge on a similar set of sections. The Instacart template merges them.

| Section | NNG (Gibbons, 2022) | Erika Hall (2019, 2nd ed) | Nikki Anderson / dscout (2022) |
|---------|---------------------|---------------------------|--------------------------------|
| Background / Problem | Yes | "Define the problem" (Step 1) | Yes — includes stakeholder list |
| Objectives / Goals | Yes | Implicit in problem framing | Yes — 3–5 research questions per objective |
| Research Questions | Yes — distinct from objectives | Implicit | Yes — mapped 1:1 to objectives |
| Hypotheses / Assumptions | Optional | Encouraged (surface assumptions early) | Yes — separate section |
| Methodology & Rationale | Yes | "Select the approach" (Step 2) | Yes — brief justification |
| Participants & Recruitment | Yes | Yes | Yes — includes screener criteria |
| Timeline / Milestones | Yes | Yes | Yes — marked as estimates |
| Deliverables | Yes | "Report the results" (Step 6) | Yes |
| Resources / Links | Implicit | Implicit | Yes — prototypes, tickets, recordings |
| Stakeholders / RACI | Implied | Implied | Yes — named in Background |
| Risks / Open Questions | Sometimes | Yes — surface assumptions | Sometimes |

## 2. Objectives vs. Research Questions — Nikki Anderson framework

Anderson (dscout, 2022) draws a sharp line that matters for plan quality:

- A **research goal / objective** is a statement of what the team wants to learn. It is not phrased as a question.
  - Example: "Discover how Merchant Portal users currently search for content."
  - Example: "Uncover the pain points users encounter when finding content."
- A **research question** is the interview-ready prompt that operationalizes the goal, usually 3–5 per objective.
  - Use the TEDW approach: "**T**ell me, **E**xplain, **D**escribe, **W**alk me through."
  - Example (from the goal above): "Walk me through the last time you searched for a recipe in the Merchant Portal."

Anderson's Mad-Lib for pressure-testing a goal:

> "I need [information] to understand [proposed research goal] to make [decision] that will impact [team/organizational goal]."

If the Mad-Lib reads awkwardly, the goal is not tied to a decision and should be reworked or cut.

## 3. SMART Objectives — applying the classic framework to UX research

SMART = Specific, Measurable, Achievable, Relevant, Time-bound.

Applied to UX research:

| SMART Criterion | Translation for UX Research |
|-----------------|-----------------------------|
| **Specific** | Names one behavior, artifact, or decision — no "improve the experience" wording |
| **Measurable** | The team can tell when the objective is answered (e.g., "identify at least 3 friction points", "learn whether N of 8 participants complete the task without help") |
| **Achievable** | Scoped to the study type, timeline, and budget. Do not promise generalizable N=6 findings. |
| **Relevant** | Tied to a pending product decision. If no decision hinges on the answer, cut the objective. |
| **Time-bound** | Delivered by a named milestone (readout date, launch decision date) |

A useful test: every objective should be answerable by a specific deliverable slide or table in the readout.

## 4. Methodology Selection Logic

Combining NNG (Farrell, 2017 — "UX Research Cheat Sheet"), Erika Hall's four research types, and big-tech practice:

**By research type (Erika Hall):**

- **Generative** — explore unknown territory, define problems. Methods: IDI, field study, diary study.
- **Descriptive** — characterize known behavior/context. Methods: survey, analytics review, diary study.
- **Evaluative** — test a specific solution or concept. Methods: usability test, concept test, A/B.
- **Causal** — explain why something happens. Methods: log analysis, mixed-method studies.

**By project phase (NNG — Farrell, 2017):**

| Phase | Methods |
|-------|---------|
| Discover | Field studies, interviews, diary studies |
| Explore | Competitive analysis, prototyping, card sorting, persona building |
| Test | Usability testing, accessibility eval, benchmark testing |
| Listen | Surveys, analytics, search-log analysis, FAQ review |

**When in doubt:** "If you can do only one activity and aim to improve an existing system, do qualitative (think-aloud) usability testing." (Farrell, NNG, 2017)

**Method quick-pick table:**

| If the team needs to… | Use | Typical N |
|-----------------------|-----|-----------|
| Understand motivations, mental models, context | In-Depth Interview (IDI) | 6–12 |
| Observe behavior in natural setting | Field study / contextual inquiry | 4–8 |
| Evaluate a flow or prototype for friction | Moderated usability test | 5–8 per persona |
| Measure a behavior or attitude at scale | Survey | N≥100 for descriptive; N≥385 for ±5% CI |
| Track behavior over time in context | Diary study | 8–15 over 1–2 weeks |
| Compare two or more concepts | Concept test or unmoderated preference test | 30–50 unmoderated, or 8–12 moderated |
| Validate terminology or IA | Card sort / tree test | 15–30 (tree test) |

## 5. Sample Size Rationales — defending N to skeptics

- **N=5 for qualitative usability**: Nielsen (2000), "Why You Only Need to Test with 5 Users." Each user surfaces ~31% of usability problems; ROI flattens after five. For two distinct user groups, run 3–4 per group. For three+ groups, 3 per group. Run more small tests, not one big one.
- **N=6–12 for IDIs**: Guest, Bunce, & Johnson (2006) — saturation reached by ~12 interviews for homogeneous samples; Instacart convention is 8 for B2C studies, 6 for expert/B2B studies.
- **N≥100 for descriptive surveys**: Sauro & Lewis (2012), *Quantifying the User Experience*.
- **N≥385 for ±5% CI on a general-population proportion**: standard sample-size calculation, 95% confidence.
- **Diary study N=8–15**: dscout convention — enough to see variance across contexts without overwhelming synthesis.

When sample size is challenged, lead with the decision the research informs, not the number. "We are running N=6 because this is a formative study meant to generate hypotheses for a larger quant follow-up" beats "Nielsen says 5 is fine."

## 6. Common Pitfalls — Portigal, Hall, NNG

- **Foraging model fallacy (Portigal, 2013/2023)** — Framing research as "find pain points to fix" leaves insights on the table. Better framing: understand the person, their goals, and their context.
- **Confirmation bias (Portigal)** — Hold a pre-research stakeholder session to surface assumptions in writing. Revisit the list at readout.
- **Solution-shaped questions (Anderson)** — "Would you use feature X?" predicts nothing. Replace with "Walk me through the last time you faced [problem X solves]."
- **Conflated goals and questions (Anderson)** — Goals that end in a question mark are usually interview questions in disguise. Separate them.
- **Unscoped objectives (Hall)** — "Understand the user" is not an objective. Tie every objective to a pending decision.
- **Sample-size theater (Nielsen)** — Adding participants to feel more "confident" in qualitative work yields diminishing returns and delays the study.
- **Missing stakeholder alignment (NNG)** — Without a documented RACI and readout date, findings evaporate. Name the decision-maker (Responsible) in the plan itself.

## 7. Stakeholder Alignment Tactics

- **Before the plan:** 30-min kickoff with PM, EM, design lead. Capture assumptions and open questions verbatim.
- **Plan draft:** Circulate async for comments. Ask three specific questions: (1) Are the objectives the right ones? (2) Is the timeline realistic? (3) Who else should see the readout?
- **Plan approval:** Record the "approved" version with date and approvers. Changes after approval = amendment note at the top of the plan.
- **Mid-study checkpoint (for studies >2 weeks):** 15-min Slack update with early signals and any scope risks.
- **Readout:** Stakeholders named in Informed see the readout deck before the meeting. No surprises.

## 8. Timeline Conventions (Instacart)

| Study Type | Typical End-to-End |
|------------|--------------------|
| IDI (N=6–8, remote) | 3–4 weeks |
| Moderated usability (N=5–8) | 2–3 weeks |
| Unmoderated usability (N=30–50) | 1–2 weeks |
| Diary study (2-week protocol) | 5–6 weeks |
| Survey (descriptive) | 3–4 weeks |
| Mixed-method (qual + quant) | 6–8 weeks |

Breakdown per study: Plan approval (3 days) → Recruit (1–2 weeks) → Fieldwork → Synthesis (3–5 days) → Readout draft (2 days) → Readout meeting.

## 9. Deliverables Menu

Pick 2–4 per study. Over-promising deliverables is a common plan failure mode.

- Readout deck (primary — always include)
- Executive summary (1 page)
- Insight/quote reel (3–5 min video)
- Journey map or mental model diagram
- Jobs-to-be-done or opportunity map
- Heuristic scorecard
- Raw transcripts + tagged Dovetail project
- Recommendations doc with severity ratings
- Follow-up research backlog

## 10. Risks & Open Questions — why a dedicated section

NNG, Portigal, and Hall all implicitly or explicitly call for surfacing risk. A "Risks / Open Questions" section in the plan:

- Documents what the study cannot answer (scope guardrail)
- Names recruitment risks (specialized panels, low-incidence personas)
- Flags timeline dependencies (content not yet built, prototype unstable)
- Lists questions the team may ask at readout that the study is not designed to answer (managing stakeholder expectations pre-fieldwork)

## Sources Cited in Plan Output

- Nielsen, J. (2000). *Why You Only Need to Test with 5 Users.* Nielsen Norman Group.
- Farrell, S. (2017). *UX Research Cheat Sheet.* Nielsen Norman Group.
- Gibbons, S. (2022). *UX Research Plans (Video).* Nielsen Norman Group.
- Hall, E. (2019). *Just Enough Research*, 2nd ed. A Book Apart.
- Anderson, N. (2022). *How to Write a User Research Plan That Sets Your Project Up for Success.* dscout People Nerds.
- Anderson, N. (2022). *Write Kick@ss User Research Goals.* User Research Strategist.
- Portigal, S. (2023). *Interviewing Users: How to Uncover Compelling Insights*, 2nd ed. Rosenfeld Media.
- Guest, G., Bunce, A., & Johnson, L. (2006). How many interviews are enough? *Field Methods*, 18(1).
- Sauro, J., & Lewis, J. R. (2012). *Quantifying the User Experience.*
