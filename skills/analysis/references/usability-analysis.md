# Usability-Session Analysis Overlay

Load this reference when the data come from moderated or unmoderated usability, prototype, or task-based concept sessions. It adds task-level structure on top of the route chosen by sample size (SKILL.md §3); it never relaxes that route's claim limits.

## 1. Observation grid first (rainbow sheet)

Before clustering, build a **participant × task grid**, adapted from Tomer Sharon's rainbow spreadsheet and GOV.UK's usability analysis spreadsheet:

| Task | Observation (one behavior) | P01 | P02 | P03 | … |
|---|---|---|---|---|---|
| T1 Add substitute | Opened the item menu before finding "Replace" | ✓ | | ✓ | |
| T1 Add substitute | Completed without help | ✓ | ✓ | | |

Rules:

- **One behavior per row.** "Hesitated and then gave up" is two rows.
- **Observations only.** Conclusions, interpretations, and solutions don't belong in rows; they come later, on the ladder of inference.
- **Pre-seed rows from the plan and guide.** Turn each task's expected path and each hypothesis into observable yes/no rows before reviewing sessions, then add rows for what you didn't expect.
- **Keep do and say apart.** Log behavior in the grid and what the participant said in the evidence ledger, with its `observed` or `spontaneous` / `prompted` origin.
- **Discard biased moments.** If a moderator prompt led the participant at a step, mark that cell as moderator-influenced and keep it out of the counts.

## 2. Task outcomes

Report per task:

- **Unassisted success**, **assisted success**, and **not completed**, separately. Never fold assisted into success.
- **Counts, not rates, for small samples:** "3 of 6 completed unassisted". Below n=20, no percentages or averages.
- **Time on task** only when the plan measures it: report the median and the individual values for small n, and watch for bimodal results.
- **The most common first error.** It often points to the root cause.
- **A worst-case rollup for scanning:** a task is red if any participant failed it unassisted, amber if any needed help, and green otherwise. The rollup is a navigation aid, not a severity rating.
- **Post-task ratings** (SEQ, SUS) only when the guide collected them. Report the distribution, not just the mean.

## 3. Issue inventory, then root causes

1. **Inventory.** List every issue observed, with participant, task, grid row, and evidence IDs.
2. **Cluster by root cause.** Issues that are the same underlying problem merge; the inventory rows stay linked.
3. **Rate severity** per root-cause issue (below).
4. **Write the finding** on the ladder: observation → pattern → interpretation → implication.

Participant suggestions ("you should add a button here") are evidence of the problem the participant felt, not a requirement. Record them as such.

## 4. Severity rating

Use Nielsen's 0–4 scale, judged on **frequency** (how many hit it), **impact** (how hard it is to overcome), and **persistence** (whether people overcome it once or keep hitting it):

| Rating | Meaning |
|---|---|
| 0 | Not a usability problem |
| 1 | Cosmetic — fix if time allows |
| 2 | Minor — low priority |
| 3 | Major — important to fix, high priority |
| 4 | Catastrophe — fix before release |

- **Severity from one rater is unreliable.** Propose AI ratings as one independent rater; the researcher rates independently before seeing the AI's ratings, and disagreements are discussed, not averaged. Record both ratings and the resolution.
- **Severity is not prevalence.** A rating of 4 from one participant is still `1 of N`; the finding's claim language follows the route's limits, and its confidence dimensions still apply.
- **Severity is not priority.** Priority (P0/P1/P2), owners, and effort belong in `/report` and depend on business context the analysis doesn't hold.

## 5. QA additions for usability data

Add these to the Gate 1 and final checks in `quality-gates.md`:

- Every grid cell used in a count traces to a session locator.
- Assisted and unassisted outcomes are reported separately.
- No percentage or average appears below n=20.
- Each severity rating records both raters and the resolution.
- Moderator-influenced cells are excluded from counts.

## Sources

- Nielsen, J. *Severity Ratings for Usability Problems.* NN/g. https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
- NN/g. *Quantitative Metrics in Qualitative Studies.* https://www.nngroup.com/articles/metrics-qualitative/
- Sharon, T. *The Rainbow Spreadsheet.* https://smashing-patternlib.netlify.app/2013/04/rainbow-spreadsheet-collaborative-ux-research-tool
- GOV.UK User Research blog. *How a spreadsheet can make usability analysis faster and easier* (2019). https://userresearch.blog.gov.uk/2019/09/13/how-a-spreadsheet-can-make-usability-analysis-faster-and-easier/
- rampstackco `usability-testing` skill (issue inventory → root-cause clustering). https://github.com/rampstackco/claude-skills
- oakoss `usability-tester` skill (assisted/unassisted success, median time, first error). https://github.com/oakoss/agent-skills
