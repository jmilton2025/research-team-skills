# Market Scan & Comparison — October 2026

We compared the four core skills (`/research-plan`, `/mod-guide`, `/analysis`, `/report`) against published Claude skills, agent plugins, and public research-team handbooks, then folded the strongest ideas back into this repo.

## What was scanned

| Skill | Sources opened | Blocked / not opened | Strongest sources |
|---|---|---|---|
| Research plan | 35 | 5 | GitLab Research Issue template + handbook, 18F UX Guide, GOV.UK Service Manual, NN/g *Planning research with AI*, Great Question brief writer |
| Moderation guide | 34 | 10 | rampstackco `usability-testing`, slgoodrich `interview-frameworks` / `usability-frameworks`, GitLab scripts, NN/g task & leading-question articles, Ronsen (Lyssna) template |
| Analysis | 31 | 5 | Hill et al. 2025 (LLM vs. human analysts), keemanxp Braun & Clarke skill, rampstackco `discovery-research-synthesis`, owl-listener `affinity-diagram`, GoTranscript AI-QA checklist |
| Report | 39 | 10 | rampstackco *writing for decisions, not decks*, tyroneross `pyramid-principle`, GitLab *Research insights*, Dovetail / Versive guides, NN/g small-n metrics |

Full catalogs (with every URL and an opened/blocked flag) and pattern files with verbatim excerpts are in this folder: `*-catalog.md`, `*-patterns.md`. No source was cited without being opened.

## Headline

- **Your skills are deeper than anything on the market.** Most community skills are a template plus a checklist, and Anthropic's own `user-research` skill is a timing outline. None has your authorization gates, evidence ledger, multidimensional confidence, construct crosswalk, or verified delivery.
- **The gaps were in research craft and in the hand-offs between skills, not in rigor.** The market — especially GitLab, 18F, GOV.UK, and NN/g — has sharper, more operational rules for objective caps, no-shows, analysis time, task wording, mid-session recovery, usability severity, claim-style headings, and closing the loop after a readout.
- **The four skills didn't reference each other's outputs.** The plan defines hypotheses and go / narrow / no-go terms; analysis and report now answer them explicitly.

## Changes by skill

### `/research-plan`

| Area | Market practice | Before | Now |
|---|---|---|---|
| Researchability | Split the ask into study / analytics / already-made decision (Great Question; GitLab "will not do") | Decision audit only | Researchability split in the decision audit; non-research parts routed by name |
| Objectives | ≤4 objectives (GitLab); output verbs, not "understand" (18F) | "Usually 2–4" | Hard cap of 4 with a split rule; output verbs; objective written as the decision |
| Research questions | Open words; don't assume the solution (GOV.UK, 18F) | Broad and not TEDW | Open-word rule plus a weak → stronger rewrite table |
| Hypotheses | Facts / opinions / guesses sort (User Interviews); "We believe… will achieve…" (GitLab) | Origin labels | Sort first; GitLab form when an outcome is predicted |
| Method | State what it won't tell you; name rejected alternatives; map methods to RQs; no reflexive triangulation (Great Question, NN/g) | Minimum valid design + alternatives | All four, plus a **Won't tell us** bullet in Method & approach |
| Sample | Per-segment sizing; recruit 7 to seat 5; screener distractors (GOV.UK, rampstackco, NN/g) | Nielsen / Guest sizing | Per-segment, counts not percentages, no-show buffer, screener hygiene |
| Timeline | Anchor to the decision date; pilot; analysis ≈ 2× sessions (18F) or 1:2 (GOV.UK) | Phase plan | All three; the plan states its analysis ratio |
| Risks | Risks to a conclusive answer, each with a mitigation | Dependencies & guardrails | Conclusiveness risks and a mixed-results plan in that row; 4 new critique rows |

### `/mod-guide`

| Area | Market practice | Before | Now |
|---|---|---|---|
| Time pressure | Must / nice-to-have tiers; cut probes first; must-haves early (Great Question, GitLab) | Time splits only | Rule 14 plus an audit row |
| Probes | Core lines word for word; conditional "if they haven't mentioned X" probes | Named probe taxonomy | Rule 15 |
| Recall & warm-up | ≤2-month recall window; warm-up isn't data collection in disguise (GitLab, Great Question) | Neutral incident gate | Rules 16–17 |
| Tasks | Moderator-only expected path / success line; NN/g's 10 task mistakes | Goal-not-UI, scenario → expectation → task → alignment | Rules 18–19 plus audit rows |
| Leading questions | Opposite-answer test; "how often" is closed too (Great Question, Torres) | Leading / closed / compound audit | Two new Part 2 audit rows |
| In-session recovery | Stuck ladder, "I give up", participant questions, off-track, emotional moments, leading-question recovery | Not covered | Methodology §7 *Session Recovery Playbook* |
| Observers | Observer brief, lenses, side-channel questions (Lyssna, Krug) | Max 2–3 observers | Methodology §8 |
| Running the study | Pilot with no internal access; remote task delivery; calibration; mid-study change rules; moderator self-check | Pilot reminder | Methodology §9 |

### `/analysis`

| Area | Market practice | Before | Now |
|---|---|---|---|
| Speaker separation | Moderator speech coded as evidence was the #1 LLM error (Hill et al. 2025) | Speaker separation audited | Moderator turns tagged as context before coding; Gate 1 check |
| Coverage | Every participant appears in the output (owl-listener) | — | Gate 1 participant-coverage check |
| Quote fidelity | Polarity and number-swap checks beyond string match (co-researcher evals) | Mechanical string check | Claim-to-quote meaning check; ellipsis rule for joins |
| Fabrication | `[QUOTE NEEDED]`; never interpolate numbers; red-flag scan (Enterpret, rampstackco, GoTranscript) | Never invent quotes | Placeholder, number rule, and red-flag scan |
| Plan link | Record RQs verbatim and answer them; themes must not mirror the guide (keemanxp) | Research question in proposal | New §5a crosswalk: RQ status, hypothesis verdicts, decision outcome in the plan's terms |
| Counterevidence | "But consider" per pattern; leftovers are signal; not-act implications (rampstackco) | Seek contradictions | Mandatory "But consider"; single-source signals; not-act allowed |
| Usability data | Rainbow sheet; assisted vs. unassisted; Nielsen 0–4 severity with the LLM as one rater | No usability mode | New `references/usability-analysis.md` overlay |
| Scale | Batch more than 15 transcripts in groups of 10–12; pass only verified output forward | — | Large-corpus overlay |
| Consistency | — | Example used "8 of 14 (57%)" | Counts with participant IDs, matching `/report`'s n<20 rule |

### `/report`

| Area | Market practice | Before | Now |
|---|---|---|---|
| Plan link-back | Answer the questions you set out to answer | — | New *What We Set Out to Answer* section: RQ status, hypothesis verdicts, decision readout |
| Headings | Claims, not topic labels or truisms (pyramid-principle, Great Question) | Answer-led title | Rule 16 plus a critic row |
| Confidence | Confidence sets the wording; causal and evaluative words are claims (pyramid source-integrity) | Calibration row | Rules 18–19 |
| Ordering & dissent | Order by decision impact; surface dissent per finding (Versive, Great Question) | Priority or narrative | Rules 20–21 |
| Recommendations | "Don't act" is valid; severity ≠ priority; evaluative studies may stop at findings | Owned, imperative, ≤ insights | Rules 22–24 |
| After the readout | Track insights to closure (GitLab); impact log (Sprig); 3-month decision test (rampstackco) | Ends at delivery | New §8.5 *Close the loop*: fill the plan's TL;DR row, ticket-ready recommendations, decision check |

## Consistency fixes across the four skills

| Issue | Fix |
|---|---|
| `/report` verified names with a people search; `/research-plan` and `/mod-guide` forbid it | `/report` now asks the researcher, like the others |
| `/report` said pop-ups had "no fixed cap" on options; the tool allows 4 | 4-option rule with a grouped-options pattern, matching the other skills |
| `/report` had no source-authorization or privacy gate | Added (connector access ≠ authorization; de-identified inputs; prefer `/analysis` output) |
| `/report` ran the multi-agent review automatically with no skip | Offered once with skip, failure handling, and standard critique-only statuses, matching `/research-plan` |
| `/report` had no connection check | First-message sign-in flag added |
| Analysis example percentages vs. `/report`'s n<20 rule | Example rewritten to counts |

## Considered, not adopted

- **GitLab's 6-dimension priority score at intake.** It's useful for a ResOps queue but adds a questionnaire to every plan; the decision audit already covers blocking decisions.
- **18F's ban on "understand" vs. GitLab allowing it.** We took 18F's stricter rule.
- **Observation quotas** (GOV.UK's "2 hours every 6 weeks"). That's a team norm, not a per-study rule.
- **Synthetic users or AI participants.** Several marketplace skills offer them. Kept out: they aren't evidence, and Great Question's guidance agrees.
- **Duplicating the guide per segment** (Ronsen). The existing cohort-labeling rule already covers it.

## Verification

All existing contract suites pass after the changes: `research-plan` validate_contract + 40 layout tests, `mod-guide` 39 contract + 36 layout tests, and `analysis` 45 contract tests. Output templates and the Option 4 layout contracts were left unchanged, except for the new *What We Set Out to Answer* block in the `/report` Product/PM template.
