# Example: Step 5 multi-agent review of a mock research plan

A saved result from one real run of the Step 5 review panel. Use it in demos instead of running the panel live, and to see what a review returns. The plan is a **mock** (the “Your usuals” Buy It Again redesign, marked TEST ARTIFACT); the people and the product requirements document (PRD) are made up.

## Run at a glance

| | |
|---|---|
| **Date** | Sep 28, 2026 |
| **Input** | The plan after the Step 4.5 critique, plus 4 source files: the mock PRD and 3 prior internal studies (not included) |
| **Reviewers** | 5: fact-check (with quote audit), quant rigor, overreach, leadership readiness, ML/DS partner. Voice was off. |
| **Runtime** | About 56 min, 7 agents (5 reviewers, 1 verifier, 1 lead) |
| **Score** | 6.2 / 10 (fact-check 7 · quant rigor 6 · overreach 5 · leadership 6 · ML/DS 6.5) |
| **Verdict** | HOLD: 4 must-fixes before sign-off |
| **Quote audit** | 22 unique quotes checked against the sources; 1 not verbatim (example UI copy the plan wrote itself, #23) |
| **Findings** | 28 fixes: 4 must-fix, 19 should-fix, 5 polish; 0 disputed by the verifier |
| **Researcher applied** | 11 (1 must-fix, 10 should-fix). 3 needed their wording corrected against the source first (#5, #15, #19). |

## What this run shows

- **Reviewers converge on the real problems.** 5 of the 28 fixes were flagged by all 5 reviewers independently, including the top 2 must-fixes.
- **The researcher picks.** Not applying a fix is a normal outcome. #10 would have filled the RACI “Informed” row with a guessed group, which the skill forbids (it keeps `[TBD — fill in]` until a real name is confirmed).
- **Fix wording needs checking too.** Three should-fix replacements added details the sources don't support. They were caught by hand in this run; the verifier now checks should-fix wording against the sources automatically.

## All 28 fixes

🔴 must-fix · 🟡 should-fix · 🟢 polish

| # | | Where | Problem | Flagged by | Applied? |
|---|---|---|---|---|---|
| 1 | 🔴 | Topic (first overview row) | Unsourced opening claim and overstated decision | All 5 | No |
| 2 | 🔴 | Screener, sample, stimuli, method, H4 | Stimulus can't show H4 or a real H1 difference | All 5 | Yes |
| 3 | 🔴 | Objective 1 | Claims to test item selection it can't test | Overreach, Leadership, ML/DS | No |
| 4 | 🔴 | Existing insight 4, Objective 2, H2 source | Insight rests on too little evidence | Overreach, Fact-check, Quant, ML/DS | No |
| 5 | 🟡 | Evidence age, Background, Appendix, Next steps | Omits the PRD owner's 2026 evidence | All 5 | Yes, corrected |
| 6 | 🟡 | Decisions | Hold path unsupported; path 1 unreachable | Fact-check, Overreach, Leadership, ML/DS | No |
| 7 | 🟡 | Synthesis, Success | Undefined group-level calls; a split between groups has no path | Quant, Overreach, Leadership, ML/DS | No |
| 8 | 🟡 | Timeline, Next steps | Sign-off ask buried; recruit count wrong | Leadership, ML/DS, Quant, Fact-check | No |
| 9 | 🟡 | Background 1–3, Next steps, Resources | PRD claims read as verified findings | All 5 | Yes |
| 10 | 🟡 | RACI | Placeholder in the header block | Leadership, Fact-check, ML/DS | No |
| 11 | 🟡 | Dependencies, Next steps | Ranking owner has no role in the study | ML/DS, Leadership, Overreach | Yes, in part |
| 12 | 🟡 | Dependencies, Stimuli, Timeline | Recruit count and prototype build load understated | Quant, Fact-check, Leadership | No |
| 13 | 🟡 | Interpretation limit | Implies a planned A/B test; best-case bias unstated | Fact-check, ML/DS, Overreach, Quant | No |
| 14 | 🟡 | Existing insight 1 | Headline broader than its source supports | All 5 | Yes |
| 15 | 🟡 | Existing insight 3 | Unlabeled interpretation misstates the ranking | Fact-check, Overreach, Leadership, ML/DS | Yes, corrected |
| 16 | 🟡 | Background (new bullet) | Business stakes and team goal missing | Leadership | Yes |
| 17 | 🟡 | Existing insight 2, H1 source, Order comparison | General rule drawn from one narrow finding | Fact-check, Overreach, Quant | Yes |
| 18 | 🟡 | Existing insight 5, H4 source | Evidence measures something other than the claim | Fact-check, Quant, Overreach, ML/DS | Yes |
| 19 | 🟡 | Objective 3, H3 source | “No prior evidence” ignores related findings | Fact-check, ML/DS | Yes, corrected |
| 20 | 🟡 | Why 6 per group, Backups | Uncited norm; minimum stated two ways | Fact-check, Quant, Overreach | Yes |
| 21 | 🟡 | Sample definitions | Screener thresholds loose and undefined | Quant | No |
| 22 | 🟡 | Scenario order, Ranking-cue probe | Fixed order confounds cue and scenario effects | Overreach, Quant | No |
| 23 | 🟡 | Ranking-cue probe | Invented copy reads as the design's own | Fact-check | No |
| 24 | 🟢 | Deliverables | Implies a trust measure and a fixed build date | Overreach, Fact-check, Leadership, ML/DS | No |
| 25 | 🟢 | Timeline Synthesis row; first uses of PRD, ResOps, BIA | Terms used before they're defined | Leadership, ML/DS | Acronyms spelled out in the Step 6 copyedit |
| 26 | 🟢 | Throughout | Mixed words and numerals for counts | Quant | No |
| 27 | 🟢 | Title | Product name capitalized inconsistently | Fact-check | No |
| 28 | 🟢 | Appendix, 4th link | Unverified link | Fact-check | Resolved: link checked |

## Three worked examples

### #2 🔴 Stimulus can't show H4 or a real H1 difference (applied)

- **Problem:** the screener asked for “about 8 usual items,” so each prototype would roughly fill the 8 visible slots and nothing more. That can't test H4 (are 8 slots too few?), and some participants' predicted-need and recency orders would barely differ, so H1 had nothing to compare.
- **Fix, as applied:** the screener asks for every item bought regularly (up to 15) and records each person's count; a new sample rule requires at least 3 items bought on some trips but not every trip; the prototype shows the first 8 in each order with the rest behind “expand”; Design checks that the two orders really differ; synthesis reports H1 and H4 separately for people with more or fewer than 8 usuals.

### #15 🟡 Fix wording corrected against the source (applied, corrected)

- **Problem:** the insight ended with “That's the behavior v3's predicted-need ranking is betting on,” an interpretation presented as fact.
- **Reviewer's fix:** label it as interpretation and add a clause summarizing what most participants in the prior study described.
- **What was applied:** the interpretation label, *without* the added clause. The prior study doesn't support that clause, so applying the fix as written would have added a new unsupported claim.

### #23 🟡 Quote audit catch (not applied)

- **Problem:** the method's example ranking cue, “You buy this about every 2 weeks,” is in quotation marks but doesn't appear in the PRD or the designs. Readers could take it as the design's real copy.
- **Fix:** label it as draft copy written for this study: “(e.g., draft copy written for this study, not part of v3: …)”.
