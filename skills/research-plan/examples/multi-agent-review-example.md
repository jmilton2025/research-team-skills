# Example: Step 5 multi-agent review of a mock research plan

A saved result from one real run of `/multi-agent-check`, the two-reviewer check that Step 5 calls. Use it to see what a review returns, or in demos when you'd rather not run the check live. The plan is a **mock** (the “Your usuals” Buy It Again redesign, marked TEST ARTIFACT); the people and the product requirements document (PRD) are made up.

## Run at a glance

| | |
|---|---|
| **Date** | Sep 29, 2026 |
| **Input** | The plan after the Step 4.5 critique (about 2,300 words), plus 4 source files: the mock PRD and 3 prior internal studies (not included) |
| **Audience** | Jordan Park, the product manager who signs off, and leadership using the plan for the Oct 30 roadmap lock |
| **Reviewers** | 2: Evidence checker and Stakeholder reader |
| **Runtime** | Evidence checker 3 min 15 s · Stakeholder reader 3 min 12 s. Run side by side as the skill intends, the check takes about as long as the slower reviewer, plus the merge. (In this run the two were started about 5 minutes apart because the first launch hit a tool error.) |
| **Verdict** | FIX FIRST — 4 must-fixes |
| **Findings** | 25 fixes: 4 must-fix, 21 should-fix. The reviewers raised 27 between them; 2 were the same issue and were merged. |
| **Must-fix check** | The Evidence checker's one must-fix was confirmed against the sources by hand before it was listed (Step 4 of the skill) |
| **Applied?** | Not in this run. It was done to show the new check on the same draft as an earlier five-reviewer run (see the end). |

## What this run shows

- **Two views catch different things.** The two reviewers overlapped on only 2 of 27 findings. The Evidence checker found where the plan overstates or leaves out evidence; the Stakeholder reader found where Jordan couldn't act on it. All 3 of the Stakeholder reader's must-fixes are things an evidence check doesn't look for.
- **Facts can be right while the framing is wrong.** The Evidence checker confirmed every participant quote, count, name, and date, yet still found a must-fix: a heading that says more than its sources do.
- **Must-fixes get checked before they're listed.** The Evidence checker's must-fix was checked against the source lines it cited. It held up, so it stayed on the list.

## All 25 fixes

🔴 must-fix · 🟡 should-fix

| # | | Where | Problem | Flagged by |
|---|---|---|---|---|
| 1 | 🔴 | Existing insights (“Add all” bullet), Objective 2 | Heading overstates “control worries”; counter-evidence left out; implies “Add all” was tested some other way when it was never tested | Evidence checker |
| 2 | 🔴 | Next steps, first screen | Jordan is never asked to approve, and no date is given, though recruiting starts the next day | Stakeholder reader |
| 3 | 🔴 | Decisions | Some results fit no path (a split between the two groups, a change to the slot count), and “trust” has no bar | Stakeholder reader |
| 4 | 🔴 | RACI, Readout | “Informed: [TBD]” placeholder; leadership isn't named, and there's no route from the readout to the Oct 30 lock | Stakeholder reader |
| 5 | 🟡 | Existing insights (8 slots), H4 | Cites only the shoppers who wanted more items, not those who expected fewer | Evidence checker |
| 6 | 🟡 | Objective 3, H3 | “No prior evidence on store grouping” ignores related findings | Evidence checker |
| 7 | 🟡 | Existing insights, Method (H1) | Leaves out that shoppers expected frequency and recency orders to look alike, which weakens the comparison | Evidence checker |
| 8 | 🟡 | Existing insights, Topic | Leaves out that shoppers already remember their core staples | Evidence checker |
| 9 | 🟡 | Background, Topic, Appendix | Omits the two 2026 studies listed in the PRD | Evidence checker |
| 10 | 🟡 | Topic, Background | Two claims stronger than their sources | Evidence checker |
| 11 | 🟡 | Existing insights (rotating staples) | The researcher's interpretation reads as fact | Evidence checker |
| 12 | 🟡 | Existing insights (P2 quote) | Cited as a live test; that participant reacted to screenshots | Evidence checker |
| 13 | 🟡 | Stimuli, Recruitment vs. H4 | Screener asks for about 8 items, so H4 (are 8 slots too few?) can't pass or fail | Evidence checker |
| 14 | 🟡 | Timeline, Dependencies, Recruitment | Recruit count is 12 in one place, 14 with backups in another | Both |
| 15 | 🟡 | Sample | Uncited “5–8 per group” norm | Evidence checker |
| 16 | 🟡 | Deliverables | The Nov 16 build is treated as fixed and never explained; the fix list and clips have no dates | Both |
| 17 | 🟡 | First screen | No bottom line above the timeline; mislabeled column; vague “last updated” date | Stakeholder reader |
| 18 | 🟡 | Topic vs. Hypotheses | “H1” means both the first half of 2027 and Hypothesis 1 | Stakeholder reader |
| 19 | 🟡 | Throughout | Unexplained terms: ResOps, AnswerLab, XFN, BIA | Stakeholder reader |
| 20 | 🟡 | Dependencies | The two biggest schedule risks are left to an undated kickoff; no date to decide 12 vs. 10 sessions | Stakeholder reader |
| 21 | 🟡 | Decisions (Modified v3) | No rule for which sub-option applies | Stakeholder reader |
| 22 | 🟡 | Dependencies (Interpretation limit) | The key caveat for a roadmap decision is buried | Stakeholder reader |
| 23 | 🟡 | Background, bullet 1 | Bold lead (“Most carts are restocks”) isn't supported by the text under it | Stakeholder reader |
| 24 | 🟡 | Background, Resources | Leftover mock and process notes where links should be | Stakeholder reader |
| 25 | 🟡 | Background, Existing insights | Too dense for leadership; the same study is linked five times | Stakeholder reader |

**Couldn't check:** the links to the three prior studies (the local exports don't include them), the older research plan listed in the Appendix, the 2026 diary study beyond the PRD's one-line summary, and the dashboard and Figma file (the draft already marks both as unverified).

**Reviewer reads:**

- **Evidence checker:** the plan cites its sources accurately, but overstates the “Add all” evidence and leaves out findings that complicate its hypotheses.
- **Stakeholder reader:** well-sourced and clear enough for Jordan to approve, once it has an explicit sign-off ask, decision rules that cover every result, and named leadership in place of the placeholder.

## Two worked examples

### #1 🔴 A heading that says more than its sources (Evidence checker)

- **Problem:** the insight's heading says auto-adding “raises control worries.” In the sources, the “few” participants cited were confused by the section's name, not worried about control. The one control comment came from 1 of 6 unmoderated sessions, in a study where most found the interaction straightforward. A third study had a participant who would welcome items being pre-selected. Objective 2 also says past studies “never tested it with shoppers' own items,” implying it was tested some other way; it was never tested.
- **Fix:** retitle to “One participant asked for ‘Add all’; evidence on control is thin and mixed,” add the sample size and the counterpoint, and change Objective 2 to “never tested it.”
- **Checked by hand:** each source line the reviewer cited was opened and matched before this was listed as a must-fix.

### #2 🔴 No clear ask for the person signing off (Stakeholder reader)

- **Problem:** the only sign-off item is written as the researcher's own task (“share the plan for sign-off by Sep 30”). Jordan is never asked to approve anything, and the recruiting request also goes out Sep 30, so it's unclear whether approval has to come first.
- **Fix:** a one-line ask near the top (“Needed from Jordan: approve by Sep 30 so the recruiting request can go to ResOps that day”) and a Next step that Jordan owns.

## Compared with the earlier five-reviewer run

The same draft and sources went through the earlier five-reviewer panel on Sep 28, 2026. That run took about 56 minutes and 7 agents, and returned 28 fixes (4 must-fix, 19 should-fix, 5 polish).

- **Raised by both runs:**
  - the “Add all” evidence (a must-fix both times)
  - the omitted 2026 PRD studies
  - store grouping's “no prior evidence”
  - the unlabeled interpretation
  - the uncited 5–8 norm
  - the recruit count
  - the fixed Nov 16 date
  - the RACI placeholder
  - the decision paths
  - the screener that can't test H4
- **Rated higher this time:** the RACI placeholder, the missing sign-off ask, and the gaps in the decision paths. The earlier panel called these should-fixes; the Stakeholder reader made them must-fixes.
- **Rated lower this time:**
  - The screener that can't test H4 was an earlier must-fix and is a should-fix here (#13).
  - The unsourced opening claim in the Topic was an earlier must-fix and is part of should-fix #10 here.
- **Not raised this time:**
  - the earlier must-fix that Objective 1 claims to test item selection it can't test
  - the example ranking-cue copy in the method: the Evidence checker judged its “e.g.” label enough
