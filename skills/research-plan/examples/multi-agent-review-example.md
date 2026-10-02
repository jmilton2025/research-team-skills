# Example: Synthetic Step 5 multi-agent review

This is a fully synthetic demonstration of the two-reviewer check that Step 5 calls. It is not a recorded study or a source of customer evidence. The product, people, dates, source notes, findings, counts, and quotes below are invented so this example can be shared safely.

## Run at a glance

| | |
|---|---|
| **Input** | A fictional research plan for a “Pantry Pilot” saved-list concept, plus three fabricated source notes |
| **Audience** | Casey Lee, the fictional product manager responsible for the decision |
| **Reviewers** | Evidence checker and Stakeholder reader |
| **Runtime** | Illustrative: both reviewers run in parallel; actual runtime varies with plan and source length |
| **Verdict** | FIX FIRST — 4 must-fixes |
| **Findings** | 12 fixes: 4 must-fix and 8 should-fix |

## What this example shows

- **The reviewers cover different risks.** The Evidence checker tests claims against the supplied material; the Stakeholder reader tests whether the intended audience can make the decision.
- **A fact can be cited yet still be overstated.** A heading may generalize beyond what a narrow fictional source note supports.
- **Must-fixes are checked before they are listed.** A proposed correction must be supported by the permitted source extract, not merely sound plausible.

## Merged fix list

🔴 must-fix · 🟡 should-fix

| # | | Where | Problem | Flagged by |
|---|---|---|---|---|
| 1 | 🔴 | Existing insights | The heading says shoppers “need” automatic grouping, but the fictional source records only one request for it | Evidence checker |
| 2 | 🔴 | Next steps | The decision owner is not asked to approve anything by a specific date | Stakeholder reader |
| 3 | 🔴 | Decisions | The action paths omit a mixed result in which clarity improves but completion does not | Stakeholder reader |
| 4 | 🔴 | RACI | The Accountable role is still `[TBD]`, so final authority is unclear | Stakeholder reader |
| 5 | 🟡 | Existing insights | One counterexample from the fictional source notes is omitted | Evidence checker |
| 6 | 🟡 | Sample | The participant count is listed without a decision-based rationale | Evidence checker |
| 7 | 🟡 | Recruitment and Timeline | The planned and backup participant totals disagree | Both |
| 8 | 🟡 | Method | The concept order is fixed, creating an avoidable order effect | Evidence checker |
| 9 | 🟡 | Dependencies | The prototype-readiness dependency has no owner or decision date | Stakeholder reader |
| 10 | 🟡 | Deliverables | The readout is named, but its approval purpose is not | Stakeholder reader |
| 11 | 🟡 | First page | Two abbreviations appear before they are defined | Stakeholder reader |
| 12 | 🟡 | Background | The section is too dense for the intended leadership audience | Stakeholder reader |

**Could not check:** two fictional source links were intentionally omitted from the example packet. A real run would label those claims unverified or remove them rather than imply that the links had been reviewed.

## Two worked examples

### #1 🔴 Claim stronger than its source

- **Problem:** The draft says shoppers need automatic grouping. The permitted fictional source extract says only that one participant asked whether groups could be created automatically.
- **Supported fix:** “One participant requested automatic grouping; broader demand is unverified.”
- **Check:** The corrected wording retains the narrow observation and removes the unsupported generalization.

### #2 🔴 No actionable approval request

- **Problem:** The plan says the researcher will circulate it, but never states what Casey must approve or when approval is needed.
- **Fix:** Add a one-line request near the top and an owned Next step: “Casey: approve the study direction by the agreed planning date before recruitment begins.”

## Example verdict

**FIX FIRST.** Resolve the four must-fixes, verify every revised evidence claim against the permitted source extracts, then run the normal copyedit and Google Docs delivery pipeline.
