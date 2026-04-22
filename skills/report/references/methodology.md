# Report Methodology Reference

Deep reference for `/report`. Load when the researcher wants methodology rationale, when writing tricky sections (insights, recommendations), or when tailoring to a specific stakeholder audience.

Sources: Nielsen Norman Group (Sarah Gibbons, Kate Moran, Caleb Sponheim, Raluca Budiu), Tomer Sharon (*Validating Product Ideas*), Erika Hall (*Just Enough Research*), Steve Portigal (*Doorbells, Danger, and Dead Batteries*), Nikki Anderson (User Research Strategist), dscout People Nerds, Indi Young (*Listening Deeply*), U.S. military BLUF standard.

---

## 1. The Finding → Insight → Recommendation Ladder

The single most important discipline in research reporting. NNG ("Data vs. Findings vs. Insights"), Sharon, Anderson, and Levitt all draw sharp lines. Collapse the ladder and stakeholders get confused about what is being asked of them.

| Rung | NNG definition | Voice | Example |
|------|---------------|-------|---------|
| **Data** | Unanalyzed observations — transcripts, notes, metrics, survey output | Raw | "P4: 'I had no idea which brand I was buying.'" |
| **Finding** | Patterns in collected data or summaries across it. *Observed.* Lacks context of prior research, business goals, history | Past tense, descriptive | "7 of 10 shoppers could not identify the brand on the PDP within 30 seconds." |
| **Insight** | *Interpreted.* Focused explanation of an opportunity, based on other user research and business context. Answers "so what?" and "why does this matter?" | Present tense, explanatory | "Shoppers default to the product image as the brand signal; brand text below the fold is invisible during the scan phase." |
| **Recommendation** | *Actionable.* Solution-centric. Who does what, by when, at what priority | Imperative | "🔴 P0 — Move brand badge above the product title on the PDP. Owner: PDP squad. Ship: next sprint." |

**Rules:**
- Never label a finding as an insight. Sharon: "if information will solve something today but won't have significant impact in the future, it's most likely a finding."
- Every recommendation must trace back to at least one insight (which traces to findings, which trace to data). If the chain can't be drawn, cut the recommendation.
- NNG: "Insights are what researchers should strive to create. Findings alone do not justify shipping a change."

**Insight template (Nikki Anderson):**
> "I am *(persona/role)* trying to *(do X)* but *(barrier/problem)* because *(root cause)*, which makes me feel *(emotion)*."

---

## 2. BLUF — Bottom Line Up Front

From U.S. military communication standard. Adopted by NNG, dscout, and Animalz for executive writing.

**Rule:** The top of every report answers three questions in under 3 sentences:
1. **What did we learn?** (the dominant finding or insight)
2. **What does it mean?** (business consequence)
3. **What should we do?** (the single most important ask)

Execs who read only the first paragraph must walk away able to make a decision. If they can't, the BLUF failed.

**Bad BLUF** (process-led):
> "This study was conducted over 4 weeks with 12 participants using an unmoderated remote method. We explored how shoppers discover new brands during grocery browsing."

**Good BLUF** (answer-led):
> "Shoppers cannot identify brands on our PDP — 7 of 10 failed the brand-recall task. This is suppressing repeat purchase for private label (est. $X impact). Recommend moving brand badge above product title this sprint."

---

## 3. Report Anatomy (NNG + dscout composite)

Default section order for a standard stakeholder readout:

| # | Section | Length | Purpose |
|---|---------|--------|---------|
| 1 | **Header / RACI** | compact | Breadcrumb, title, responsible/consulted/informed, last-updated |
| 2 | **Executive Summary (BLUF)** | ≤1 page | 3-sentence BLUF + 3-5 key findings with priority emojis |
| 3 | **Methodology** | compact | Who, what, when, how, sample size, limitations |
| 4 | **Findings** | largest | Observed patterns, ordered by priority or narrative arc |
| 5 | **Insights** | medium | Interpretation — the "so what" |
| 6 | **Recommendations** | medium | Prioritized, owned, actionable in a table |
| 7 | **Next Steps / Open Questions** | compact | Follow-on research, decisions needed |
| 8 | **Appendix** | flexible | Demographics, discussion guide, coded data, additional quotes |

**dscout variant** — three ways to structure findings; pick one per readout and commit:
- **By research goal** (Anderson's default — best for PM readers)
- **By theme** (emerged topics — best for exploratory studies)
- **By affinity category** (matches analysis artifact — best for research-team readers)

---

## 4. Audience Variants

Per dscout ("How to Present Research So Stakeholders Sit Up and Take Action") and NNG ("State of UX 2026"), tailor four dimensions: length, framing, evidence type, ask.

### Executive (C-suite, skip-levels, VP+)
- **Length:** 1-2 pages. Hard cap.
- **Framing:** Business impact — revenue, conversion, NPS, retention. Frame against OKRs.
- **Evidence:** One hero quote, one hero metric, one hero chart. No raw transcripts.
- **Ask:** Single clear decision needed. "Approve X" or "Fund Y" or "Accept Z risk."
- **Cut:** Methodology detail, caveats, participant demographics (move to appendix or omit).

### Product / PM
- **Length:** 8-15 pages. Full NNG structure.
- **Framing:** User goals mapped to PRD objectives. Roadmap implications.
- **Evidence:** Direct quotes, video clips, task-success metrics, journey fragments.
- **Ask:** Prioritized recommendation table (P0/P1/P2) with owner and effort estimate.
- **Keep:** Methodology, limitations, open questions. PMs will ask.

### Engineering
- **Length:** 6-10 pages. Behavior-first.
- **Framing:** Failure modes, edge cases, error states, latency observations.
- **Evidence:** Screen recordings at failure moments, specific error messages, device/OS breakdowns.
- **Ask:** Bug-like recommendations with repro steps and priority matrix (impact × effort).
- **Cut:** Emotional framing, aspirational quotes. Keep it diagnostic.

### Research Team / Mixed Internal
- **Length:** 15-25 pages. Methodology-heavy.
- **Framing:** Reproducibility. Study design choices. What worked, what didn't.
- **Evidence:** Full discussion guide, coded data, affinity diagrams, analyst notes.
- **Ask:** Methodological learnings for next study, not product decisions.
- **Keep:** Everything. Appendix gets long.

---

## 5. Evidence Rules (Portigal)

Steve Portigal (*Doorbells, Danger, and Dead Batteries*, Dollars to Donuts podcast) on presenting qualitative evidence:

- **Show, don't tell.** Every major finding needs at least one piece of primary evidence.
- **Video clips > quotes > photos > paraphrase.** In that order of stakeholder impact.
- **Quotes are verbatim.** Never clean up grammar. Preserve hedges ("um," "I guess"). They signal uncertainty that matters.
- **Attribute with care.** Use participant codes (P04) not names. Include relevant demographic tag: "P04, 34F, weekly Instacart shopper."
- **Context the quote.** Never drop a quote cold. Prefix with the task/question: "When asked to find private-label peanut butter, P04 said: '…'"
- **Three-quote rule for a pattern.** A pattern claimed with one quote is anecdote. Three independent participants = pattern.
- **War-story framing.** Portigal: stories with tension ("and then the device died…") outperform polished summaries because they create memory hooks.

---

## 6. Recommendation Format

Every recommendation is a row in a table with these columns:

| Priority | Recommendation | Owner | Insight Source | Effort | Impact |
|----------|---------------|-------|----------------|--------|--------|
| 🔴 P0 | Move brand badge above product title on PDP | PDP squad (Meith) | Insight #1: Brand invisible during scan | S | H |
| 🟡 P1 | Add "shop this brand" CTA on PDP | Merchandising (Trace) | Insight #2: Brand loyalty underused | M | M |
| 🟢 P2 | Explore brand-first sort on search | Search squad | Insight #3 | L | M |

**Rules:**
- **Priority emoji leads.** 🔴 P0 (ship this quarter) / 🟡 P1 (next quarter) / 🟢 P2 (backlog).
- **Owner is a named human**, not a team.
- **Every rec cites an insight number.** Traceable to evidence.
- **Effort and impact are T-shirt sizes** (S/M/L). Not hours.
- **Imperative voice.** "Move X," not "consider moving X."
- Recs that can't be owned are "Open Questions," not recommendations.

---

## 7. Common Report Failures

Pooled from Sharon, NNG (Gibbons on "research that sticks"), and the dscout post-mortems.

| Failure | Symptom | Fix |
|---------|---------|-----|
| Methodology-led intro | First page describes sample size, not findings | Lead with BLUF. Move methodology to §3. |
| Finding labeled as insight | "Users want X" with no interpretation | Interpret in context or demote to finding. |
| Unowned recommendations | "Someone should…" | Assign named owner or cut. |
| Evidence-less claims | Findings with no quote/clip | Add primary evidence or reduce confidence language. |
| Audience confusion | Exec rec buried in page 12 | Audience variant violated. Re-scope. |
| Over-hedging | Every finding caveated | Caveat once in Methodology. |
| Clip overload | Every quote included | Curate. Strongest 3 per finding. Rest in appendix. |
| No open questions | Report presented as final word | Every study has follow-ons. List them. |
| Rec-to-insight inflation | 12 recs from 6 insights | Ratio should be roughly 1:1 or fewer recs than insights. |
| Sanitized quotes | Every quote reads like a press release | Restore verbatim. Hedges and "um" matter. |

---

## 8. Qualitative Data Visualization (Indi Young + NNG)

Options for making qualitative findings scannable:

- **Journey fragment** — 3-5 step strip showing the moment of failure. Not a full journey map.
- **Mental model card** — Young's pattern. Two columns: what they are trying to accomplish vs. what the product does.
- **Affinity cluster summary** — Named themes with count of participants who mentioned each.
- **Quote wall** — 5-8 verbatim quotes on one page, grouped by insight. High density, fast scan.
- **Severity-tagged finding list** — Each finding prefixed with 🔴🟡🟢.
- **Stop-light usability matrix** (dscout) — Rows = tasks, cells = green/yellow/red by participant.
- **Rainbow chart** — Participant × finding matrix, colored cells show who said what. Best for appendix.

---

## 9. Tone & Style

- **Active voice.** "Shoppers could not find X" not "X was not findable by shoppers."
- **Past tense for findings.** "7 of 10 failed." Present tense slips into speculation.
- **Present tense for insights.** "Shoppers rely on the image as the brand signal."
- **Imperative for recommendations.** "Move the badge."
- **Never apologize for the method** in the findings section. Caveat once in methodology.
- **Numbers with denominator.** "7 of 10" not "70%" when n is small. NNG: never report percentages for n<20 qualitative samples.

---

## 10. Length Heuristics

| Readout type | Exec Summary | Full Body | Appendix |
|-------------|--------------|-----------|----------|
| Executive deck | 1 slide | 5-10 slides | link-only |
| Executive doc | 1 page | 1 extra page max | link-only |
| PM report | 1 page | 6-12 pages | 2-6 pages |
| Eng report | 1 page | 4-8 pages | 2-4 pages |
| Research-team report | 1 page | 10-20 pages | 5-15 pages |
| Readout deck (any audience) | 3 slides | 10-20 slides | back-up slides |

If the readout exceeds these, cut ruthlessly or split into two documents.

---

## 11. The "So What" Test (NNG)

Before shipping any finding, insight, or recommendation, apply the So-What Test:

- **Finding:** "7 of 10 failed the brand task." → *So what?* → Forces researcher to write the insight.
- **Insight:** "Brand text is invisible during scan." → *So what?* → Forces the recommendation.
- **Recommendation:** "Move the brand badge." → *So what happens if we don't?* → Forces the business-impact framing in the BLUF.

If any row fails the So-What Test, it is not ready to ship in the readout. It either gets sharper or gets cut.
