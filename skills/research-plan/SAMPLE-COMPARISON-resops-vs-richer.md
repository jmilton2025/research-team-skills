# Sample comparison — ResOps RPP exact vs. order-matched-richer

Same study in both structures so you can pick which one the `research-plan` skill should output.
Study used: **Recipe-to-Cart Mapping — "good enough" acceptability thresholds** (the Jun 2 demo study).

Both follow the ResOps section ORDER. The only difference is how much of your richer content (Existing Insights w/ verbatim sources, Goal-led framing, bold-lead styling) stays in.

---
---

# OPTION A — Match ResOps exactly

> Output = the official RPP template, verbatim structure. Safest for ResOps approval. Drops the Goal-led Parameters table and the standalone Existing Insights section.

# Research Project Plan: Recipe-to-Cart Mapping Acceptability

**Key Contacts:** Jedida Milton (UX Researcher)

**Key Stakeholders:**
**Responsible:** Jedida Milton (UXR)
**Accountable:** Trace Levinson (PM, Meals)
**Consulted:** Callum Wood (DS, AIQA — *decision-maker*), Eric Hermann (Meals Lead)
**Informed:** Prakriti Parijat (UXR skip-level), Heather Matley (Content)

### Research Timeline
*(phase × date grid — Phase 1 Plan, Phase 2 Recruit, Phase 3 Fieldwork, Phase 4 Synthesis, Phase 5 Readout, with PL/KO/IP/RO status codes)*

### Project Plan Overview

| | |
|---|---|
| **Topic** | Define the user-grounded threshold for what counts as a "good enough" recipe-to-cart mapping. |
| **TL;DR Summary of Findings** | *To be filled out at the end of the study.* |
| **Key Information** | |
| **Background** | The Meals workstream is shipping AI-mapped recipe→cart, but we have no user-grounded definition of an acceptable mapping. The improved-mapping A/B starts late May; without a threshold we can't interpret whether a mapping "win" is meaningful to users. This study runs in parallel to inform A/B interpretation; it does not gate the launch. |
| **Objectives** | • Establish what users consider an acceptable vs. broken recipe→cart mapping.<br>• Identify which failure modes most damage trust.<br>• Calibrate the AIQA severity rubric against real user reactions. |
| **Key Research Questions** | • What does "good" recipe-to-cart mapping mean to users?<br>• Which mismatch types are tolerable vs. dealbreakers?<br>• How does acceptability shift by cooking context (tonight's dinner vs. weekend prep)? |
| **Hypotheses / Questions of Interest from XFN leads** | • Users tolerate quantity mismatches more than wrong-item swaps.<br>• Trust drops sharply once 2+ items in a cart are visibly wrong.<br>• Acceptability is stricter for time-pressured "tonight" cooking. |
| **What decisions will be made with such research?** | • Calibrate the AIQA framework's severity thresholds.<br>• Select among the improved-mapping A/B variants for rollout. |
| **What Research Priorities is this relevant to (Themes)** | • Good Ingredient Impressions (Meals northstar).<br>• AI quality evaluation. |
| **Proposed Research Timeline** | |
| RPP share at Crit / Solicit feedback | May 12 |
| Submit Participant Recruiting Request | May 13 |
| Recruit Dates (ResOps SLA: 10 business days) | May 14–23 |
| Study Launch Date | May 19 |
| Study End Date | May 23 |
| Insights Synthesis | May 24–26 |
| Final Deliverables | May 27 |
| Upload Findings Deck to Sharpr | May 28 |
| **Project Details** | |
| **Method + Approach** | Mixed-method: 8 moderated remote interviews (45 min, stimulus walkthrough) + survey (N=75–100, same scenarios + 5-pt acceptability scale). |
| **Sampling Plan / Participants** | Adult Instacart users who ordered from a recipe ≥2× in past 60 days; quad-cell across cooking contexts; iOS+Android+web; US-based. Sample query: [link]. |
| **Stimuli** | 5–6 mocked recipe→cart scenarios at varying mapping quality. [Figma link] |
| **Dependencies** | Recruit list pull (Blazer query) [link]; stimulus mocks finalized by May 18. |
| **Compensation** | $75 per qual session / $5 per survey complete. |
| **Research Platform** | Zoom (qual), Qualtrics (survey), Dovetail (synthesis). |
| **Deliverable Format** | Readout deck (Google Slides) + severity matrix (Sheet). |
| **Additional** | |
| **Documents** | • Discussion Guide [link]<br>• Survey instrument (Qualtrics) [link]<br>• Screener [link]<br>• Datasheet [link]<br>• Final Report [link] |

---
---

# OPTION B — Match ResOps order, keep richer content

> Same section names + order as ResOps, but the Jun 2 team asks stay folded in: **Existing Insights with verbatim sources** sits right after Background, bold-lead styling stays, and the "good enough / minimum evidence" framing is preserved. Not the bare template — a richer version of it.

# Research Project Plan: Recipe-to-Cart Mapping Acceptability

**Key Contacts:** Jedida Milton (UX Researcher)

**Key Stakeholders:**
- **Responsible:** Jedida Milton (UXR)
- **Accountable:** Trace Levinson (PM, Meals)
- **Consulted:** Callum Wood (DS, AIQA — *decision-maker*), Eric Hermann (Meals Lead)
- **Informed:** Prakriti Parijat (UXR skip-level), Heather Matley (Content)

### Research Timeline
*(phase × date grid, PL/KO/IP/RO status codes)*

## Topic
Define the **user-grounded threshold for "good enough" recipe-to-cart mapping** — the line between an acceptable cart and a broken one.

## TL;DR Summary of Findings
*To be filled out at the end of the study.*

## Background

**Problem Statement**
- **Threshold gap** — We ship AI-mapped recipe→cart with no user-grounded definition of "acceptable."
- **A/B interpretation risk** — The improved-mapping A/B starts late May; a "win" is uninterpretable without a user threshold.
- **Severity blindspot** — The AIQA rubric rates mapping errors but isn't calibrated to how users actually react.

**Product Context**
- Recipes are strategic for the Meals workstream.
- This study runs in parallel and informs A/B *interpretation* — it does not gate the launch.

## Existing Insights
*(what we already know — sourced via the research-insights agent + Glean in discovery)*

1. **Wrong-item swaps erode trust faster than quantity errors.** "Participants forgave a doubled quantity but abandoned the cart after a single wrong protein." — [P2 AIQA readout](#)
2. **Cart trust is fragile past the second visible error.** — [P1 Parser Eval Phase 2](#)
3. *No prior research directly on cooking-context sensitivity — net-new for this study.*

## Objectives
1. **Establish the acceptable-vs-broken mapping line.** What signals make a cart feel usable vs. abandoned.
2. **Rank failure modes by trust damage.** Which mismatch types are dealbreakers.
3. **Calibrate the AIQA severity rubric** against observed user reactions.

## Key Research Questions
1. **What does "good" recipe-to-cart mapping mean to users?** What signals an acceptable vs. broken cart.
2. **Which mismatch types are tolerable vs. dealbreakers?**
3. **How does acceptability shift by cooking context** (tonight's dinner vs. weekend prep)?

## Hypotheses / Questions of Interest from XFN leads
*(team beliefs to pressure-test — each traces to an Existing Insight)*
- **H1** — Users tolerate quantity mismatches more than wrong-item swaps.
- **H2** — Trust drops sharply once 2+ items in a cart are visibly wrong.
- **H3** — Acceptability is stricter for time-pressured "tonight" cooking.

## What decisions will be made with such research?
- **Calibrate AIQA severity thresholds** to the user-grounded line.
- **Select among the improved-mapping A/B variants** for rollout.

## What Research Priorities is this relevant to (Themes)
- Good Ingredient Impressions (Meals northstar).
- AI quality evaluation.

## Proposed Research Timeline
| Phase | Date |
|---|---|
| RPP share at Crit | May 12 |
| Recruiting request | May 13 |
| Recruit (ResOps SLA 10 biz days) | May 14–23 |
| Launch | May 19 |
| End | May 23 |
| Synthesis | May 24–26 |
| Final deliverables | May 27 |
| Sharpr upload | May 28 |

## Project Details
| Element | Detail |
|---|---|
| **Method + Approach** | *Minimum evidence to move the decision:* mixed-method — 8 moderated interviews (45 min) + survey (N=75–100). Lean alt: survey-only if timeline tightens. |
| **Sampling Plan / Participants** | Ordered from a recipe ≥2× in past 60 days; quad-cell by cooking context; iOS+Android+web; US. [query link] |
| **Stimuli** | 5–6 mocked recipe→cart scenarios at varying quality. [Figma] |
| **Dependencies** | Blazer recruit query [link]; stimulus mocks by May 18. |
| **Compensation** | $75/session, $5/survey. |
| **Research Platform** | Zoom, Qualtrics, Dovetail. |
| **Deliverable Format** | Readout deck (Slides) + severity matrix (Sheet). |

## Additional
**Documents**
- **[Discussion Guide](#)** — via `/moderation-guide`
- **[Survey instrument](#)**
- **[Screener](#)**
- **[Final Report](#)**

---
---

## Pop-up walk order (both options use this)

The interactive flow runs in RPP order so researchers approve/brainstorm one section at a time:

1. **Existing Insights** *(first pop-up — "here's what we already know", confirm/correct)*
2. Topic
3. Background
4. Objectives
5. Key Research Questions
6. Hypotheses / Questions of Interest
7. What decisions will be made
8. Research Priorities (Themes)
9. Method + Approach
10. Sampling / Participants
11. Stimuli → Dependencies → Compensation → Platform → Deliverable Format
12. Timeline
13. Documents

Discovery (research-insights agent + Glean) runs up front to pre-fill every step, but is surfaced to the researcher as step 1 (the insights pop-up) before the section walk begins.
