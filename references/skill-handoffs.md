# Skill Handoffs — research-plan → mod-guide → analysis → report

The four core skills form one chain. Each skill's approved output is the next skill's input, so a study keeps the same questions, hypotheses, decision terms, and people from kickoff to readout.

```
/research-plan ──► /mod-guide ──► (fieldwork) ──► /analysis ──► /report
      ▲                                                            │
      └──────────── TL;DR row, decision readout, open questions ◄──┘
```

## What each handoff carries

| From → To | Carry forward | How the receiving skill uses it |
|---|---|---|
| **`/research-plan` → `/mod-guide`** | The approved plan: objectives, key research questions, hypotheses (H1…), decision-outcome terms, method & approach, sample and cohorts, stimuli, timeline, recording/consent protocol, RACI with the DRI | Pre-fills Section 1 parameters and the RACI; builds the Step 2d crosswalk so every objective, question, and hypothesis maps to a guide block; flags any deviation as a plan amendment |
| **`/mod-guide` → `/analysis`** | The approved guide: must-have vs. nice-to-have items, tasks with their expected path and success criteria, the question-to-objective crosswalk, cohort labels, any mid-study change log | Seeds the usability observation grid from the expected paths; checks coverage of must-haves; flags guide changes that limit comparison across sessions. Themes still cut across the guide's questions instead of mirroring them. |
| **`/research-plan` → `/analysis`** | Key research questions, hypotheses, and decision terms, word for word | Fills the §5a crosswalk: each research question answered, partially answered, or not answered; each hypothesis supported, challenged, mixed, or not testable; the decision outcome in the plan's own terms |
| **`/analysis` → `/report`** | The approved evidence ledger, verified quotes, confidence ratings, severity ratings, the plan crosswalk, limitations, and final QA status | Uses only verified quotes; builds *What We Set Out to Answer* from the crosswalk; sets wording from confidence; shows severity next to priority; carries limitations once, in Methodology |
| **`/report` → `/research-plan`** | The BLUF, the decision readout, and open questions | Fills the plan's *TL;DR summary of findings* row; open questions seed the next `/research-plan` |

## Rules for every handoff

1. **Ask for the upstream artifact; don't rebuild it.** When the previous skill's output exists, ask for its link or file first. If it doesn't exist, say so and work from what the researcher supplies. Don't silently reconstruct a plan, guide, or analysis.
2. **Keep approved content as approved.** A receiving skill never re-words or reinterprets upstream decisions. A needed change is shown as a proposed amendment and approved by the researcher.
3. **Same IDs end to end.** Keep the plan's hypothesis IDs (H1, H2…), number research questions in the plan's order (RQ1, RQ2…), and keep participant IDs (P01…) and evidence IDs (E-…) unchanged from analysis to report.
4. **Same decision terms.** Use the plan's outcome words (for example go / narrow / no-go) unchanged in the guide, analysis, and report. No synonyms.
5. **Same people.** Carry the plan's approved RACI, with the DRI marked, into each later skill as the pre-fill. The researcher confirms, adds, or edits it at each step.
6. **Same number format.** Count first, then percentage: "8 of 14 (57%)". For n≤4, counts only.
7. **Test labels carry forward.** An upstream `TEST ARTIFACT` or `TEST RUN` label stays on every downstream artifact built from it (see `output-status-and-labeling-conventions.md`).
8. **Authorization doesn't carry automatically.** Each skill re-runs its own source-authorization gate for any non-public source it opens, even when the upstream skill already used it.
9. **Reviews ask first.** Each skill asks the researcher once before running the multi-agent review; a "yes" in one skill isn't permission in the next.
10. **Offer the next step; don't run it.** When a skill finishes, it names the next skill in one line and what to bring to it. It runs that skill only if the researcher asks.
