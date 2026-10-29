# Skill Handoffs — research-plan → mod-guide → analysis → report

**Every skill works on its own.** Many researchers use only one skill — just a research plan, or just a moderation guide, or just a report. A handoff is a bonus when an upstream artifact exists, never a requirement. A skill must never block, stall, or keep asking because there's no upstream artifact: it asks once whether one exists, and if the answer is no (or the researcher doesn't know), it continues standalone from whatever they supply — a PRD, a brief, notes, or a plain description.

When the researcher does use several skills on one study, they form a chain. Each skill's approved output becomes the next skill's input, so the study keeps the same questions, hypotheses, decision terms, and people from kickoff to readout.

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

1. **Ask once, then go standalone.** Fold one optional question into the normal intake: *"Do you have a research plan (or guide / analysis) for this study? If not, no problem — I'll work from what you share."* If there's none, continue with the skill's own full intake. Don't ask again, don't recommend running the upstream skill first unless the researcher's inputs are too thin for this skill to work, and don't silently reconstruct a plan, guide, or analysis — any upstream-shaped section (for example, the report's *What We Set Out to Answer*) is built from what the researcher supplies, or omitted.
2. **Keep approved content as approved.** A receiving skill never re-words or reinterprets upstream decisions. A needed change is shown as a proposed amendment and approved by the researcher.
3. **Same IDs end to end.** Keep the plan's hypothesis IDs (H1, H2…), number research questions in the plan's order (RQ1, RQ2…), and keep participant IDs (P01…) and evidence IDs (E-…) unchanged from analysis to report.
4. **Same decision terms.** Use the plan's outcome words (for example go / narrow / no-go) unchanged in the guide, analysis, and report. No synonyms.
5. **Same people.** Carry the plan's approved RACI, with the DRI marked, into each later skill as the pre-fill. The researcher confirms, adds, or edits it at each step.
6. **Same number format.** Count first, then percentage: "8 of 14 (57%)". For n≤4, counts only.
7. **Test labels carry forward.** An upstream `TEST ARTIFACT` or `TEST RUN` label stays on every downstream artifact built from it (see `output-status-and-labeling-conventions.md`).
8. **Authorization doesn't carry automatically.** Each skill re-runs its own source-authorization gate for any non-public source it opens, even when the upstream skill already used it.
9. **Reviews ask first.** Each skill asks the researcher once before running the multi-agent review; a "yes" in one skill isn't permission in the next.
10. **Offer the next step; don't run it.** When a skill finishes, it may name the next skill in one line and what to bring to it. It runs that skill only if the researcher asks; a researcher who only wanted this one deliverable is done.

## Standalone entry points

| Researcher starts at | What the skill uses instead of an upstream artifact |
|---|---|
| `/research-plan` only | The PRD, brief, kickoff notes, or a description; ends with the plan Doc |
| `/mod-guide` only | A brief, PRD, notes, or a description of the study; builds its own objectives and RACI from those; the crosswalk maps to the objectives approved in Section 1 |
| `/analysis` only | The de-identified data plus the researcher's research question; the §5a crosswalk records that question instead of a plan |
| `/report` only | The researcher's findings, notes, or analysis doc; *What We Set Out to Answer* appears only when the researcher supplies the questions the study set out to answer |
