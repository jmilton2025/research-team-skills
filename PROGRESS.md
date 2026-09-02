# P4 (sub-stream) Progress — Research Team Skills

**Parent project:** P4 — Research OKR / AI Enablement
**Last updated:** 2026-09-02 12:18 PDT
**Current state:** **4th test complete — persona/generalization testing, not bug re-hunting.** 3 full independent DIY chains run for 3 different requester types (Jordan/content designer/Figma link, Alex/junior PM/no-doc-low-context, Sam/product designer/sequential 4-screen flow). Zero regressions on ~10 previously-verified fixes. Found the highest-leverage gap yet: **Figma-link intake is broken for both available Figma MCP servers, no documented fallback** — hit 2 of 3 chains independently. Also found: the `PENDING` status (added round 3) has no downstream propagation rule; no tie-breaker when upstream artifacts disagree on a hard number (N=6 vs N=40 in Jordan's chain); no signal that a low-confidence requester's handoff needs more active researcher involvement; no stimulus category for a live product feature with no link at all (hit 4/5 skills in Alex's chain). Full report: `mock-runs/DIY-PIPELINE-TEST4-REPORT-2026-09-02.md`. Not yet fixed — awaiting Jedida's call. Note: 2 of 15 agent structured-summaries in this run were corrupted placeholder junk ("test"/"placeholder" stub data) — caught by the synthesis agent, which rebuilt from the real output files instead; final report unaffected, but worth flagging as a workflow-reliability observation. Prior state: **All remaining nits from the 3rd test batch-fixed.** Added a `PENDING` third state to the shared status doc (distinct from `BLOCKED`); cross-referenced the recurring "rule lives away from where it's needed" pattern in all 4 places it recurred (`diy-research-plan` Section 1 field, `screener` Rule 1 ↔ worked example bidirectionally, `unmod-script`'s task-count heuristic restated near the Task Summary Table, `diy-packet`'s Rule 3 ↔ Rule 1 exception); `diy-packet` also got a formal Timeline field (Section 5) and a named third Step-0 case for the skip-routed path + an escalation-trigger fallback for it. Pipeline is now in good shape after 3 full test cycles — 28/30 original findings + all 7 previously-unexercised fixes confirmed or resolved, 2 genuine bugs found and fixed (X1's arithmetic, the warm-up priming Major), and the recurring documentation-placement pattern closed everywhere it appeared. Prior state: **3rd test complete — 28/30 original findings + 5/7 previously-unexercised fixes now confirmed held.** X1 confirmed broken (fixed: batching text said "three batches" for 6 questions at "up to 4 per call," should be two — corrected). One new Major found and fixed: `unmod-script`'s warm-up question could prime the exact concept a later task measures, even though it came before the scenario transition (order ≠ content-safety) — added explicit guidance + a self-critique checklist item. Remaining: ~15 minor/nit documentation-placement gaps (mostly "a rule and its cross-referencing rule live in different files/sections" shaped issues) not yet fixed — synthesis verdict says the pipeline is solid for supervised/pilot rollout as-is, not yet fully-unsupervised-safe. Decision point flagged to Jedida: keep iterating on the remaining nits, or treat this as good enough for pilot. Prior state: **Retest findings fixed.** All findings from the retest report applied: the `unmod-script` near-miss (a "required step" warning to re-derive comparison shape from the actual research question rather than trusting a repeated upstream label — this is the one that mattered most), a new shared doc (`references/output-status-and-labeling-conventions.md`) centralizing the BLOCKED-status convention (4 DIY skills) and the test-artifact-labeling convention (3 researcher-led skills), plus the remaining nits across `screener`, `diy-packet`, `research-plan`, `mod-guide`. The `mod-guide` fixes are woven into its file but NOT committed — that file has carried unrelated uncommitted WIP since June and stays that way; the 3 new fixes ride along whenever that WIP is eventually committed. Two mock-run test artifacts also had their internal `M2`/`M3` label collision renamed. A third demo, designed to hit the 7 still-unexercised fixes, is next. Prior state: **DIY research pipeline (OKR #5) re-tested after fixes — all 8 stages now "pass."** A second mock-run (different demo, deliberately routed to BOTH tracks) confirmed the fixes hold: both rollout blockers (the `AskUserQuestion` fallback, the dead `/rpp`/`/synth` commands) held under harder conditions, and the researcher-led chain (`research-plan`→`mod-guide`→`report`) ran end-to-end for the first time ever with zero dead commands. 7 of the original 30 fixes weren't exercised by this scenario's shape (unconfirmed, not broken). New findings surfaced: a recurring undocumented "BLOCKED status" pattern (4 skills independently improvised the same thing) and a near-miss in `unmod-script` where a fix only held because of manual re-derivation against a mislabeled upstream shape. Full report: `mock-runs/DIY-PIPELINE-RETEST-REPORT-2026-09-02.md`. Prior state: **DIY research pipeline (OKR #5) mock-tested + fixed** — a 5-agent test pass (one demo request run through all 5 skills sequentially) found ~30 real gaps, headlined by one platform-wide blocker (`AskUserQuestion` unavailable, no fallback in any skill) and 10 majors including two dead commands (`/rpp`, `/synth`). All ~30 fixes applied across all 5 skill files + 2 references files + one new shared conventions doc (`references/interactive-input-conventions.md`). `diy-triage` → `diy-research-plan` → `screener` → `unmod-script` → `diy-packet`, `/rpp`/`/synth` replaced with the real `/research-plan`/`/report` command names throughout. Repo now has 13 skills total. Core skills shipped — /mod-guide (7-phase pipeline + H.E.A.R.T.), jedi-doc-styling-1 (Research Plan template, 226/226 verifier pass), jedi-doc-styling-2 (GlossGenius). **research-plan skill now restructured to the canonical ResOps RPP template** (Option B: ResOps order + names, richer Jun-2 content folded in) with a section-by-section interactive pop-up walk (first pop-up = Existing Insights). Infrastructure: GitHub repo (public) + Drive folder + local skill chain validated end-to-end.

> Daily entries for this sub-stream may also appear in `~/Documents/Claude/Project-4-Research-OKR-AI-Enablement/PROGRESS.md` under a "Research Team Skills" sub-heading. This file is the dedicated log.

---

<!-- New daily entries are prepended ABOVE this line. Do not delete this marker. -->

## 📅 2026-09-02 (Wed, even later) — Re-test: do the fixes actually hold?

### What changed
Ran a second mock-run — deliberately a different, harder demo (a PM's cart-abandonment ask, framed to route to BOTH tracks at once) — specifically to check whether the fixes from the earlier test pass hold up outside the exact scenario they were written against. 9 agents: triage, then the DIY chain and researcher-led chain in parallel, each agent verifying its assigned fix(es) against the real output file rather than trusting its own claim, then one synthesis agent cross-checking everything.

**Result: all 8 stages passed** (vs. all "partial" the first time). Both rollout blockers held under harder conditions — the `AskUserQuestion` fallback, and `/rpp`/`/synth` finally resolving to the real `/research-plan`/`/report` on the very first researcher-led call the pipeline has ever gotten. `research-plan` → `mod-guide` → `report` ran fully end-to-end for the first time, with the `/report` step validated using clearly-labeled simulated findings (no real fieldwork exists in a mock test).

**Caveats, not failures:** 7 of the original 30 fixes (M3, M4, N6, N10, N15, X1, X2) weren't exercised by this scenario's shape — unconfirmed, not broken. Two new patterns surfaced: (1) 4 of the DIY skills each independently improvised the same undocumented "BLOCKED status" line when a hard gate fired — worth centralizing like the shared `AskUserQuestion` fix; (2) a real near-miss in `unmod-script` — its M7 fix (picking the right comparison shape) only held because the agent manually re-derived the shape from the actual research question rather than trusting the upstream plan/screener, which had both mislabeled it identically. Full report: `mock-runs/DIY-PIPELINE-RETEST-REPORT-2026-09-02.md`.

### Open / next
- Not yet decided whether to fix these new findings — asked Jedida.
- The 7 unexercised fixes still need a scenario that actually hits them.

---

## 📅 2026-09-02 (Wed, later) — Full mock-run test + fix pass on the DIY pipeline

### What changed
Jedida asked for a real end-to-end test: 5 agents each ran one DIY-pipeline skill, in order, against the same fictional demo request (a content designer, Priya, wants a fast unmoderated read comparing 3 copy variants on a substitution-notification card). Each agent actually followed its skill's real instructions — simulating the interactive Q&A, producing the real deliverable, writing it to `Project-4-Research-OKR-AI-Enablement/mock-runs/<skill>/demo-content-designer-2026-09-02.md` — while also acting as a critical QA reviewer of the skill's own text. A 6th agent verified every finding against the actual output files and wrote a consolidated report.

**Result:** the pipeline worked end-to-end (all 5 stages ran, each consumed its upstream artifact, `/diy-packet` genuinely assembled rather than re-derived), but every stage self-rated "partial." ~30 real, verified gaps were found — see `mock-runs/DIY-PIPELINE-TEST-REPORT-2026-09-02.md` for the full ranked list. Headline finding: **`AskUserQuestion` is unavailable in this runtime and every one of the 5 skills assumes it exists with no documented fallback** — a platform-wide issue, not a per-skill one.

Jedida asked to fix everything in the report. Ran 5 parallel agents (one per skill file) applying all ~30 fixes:
- Created `references/interactive-input-conventions.md` (repo-root, shared) — the `AskUserQuestion` fallback, written once and referenced by all 5 skills instead of duplicated.
- `diy-triage`: replaced dead `/rpp`/`/synth` references with the real `/research-plan`/`/report` command names throughout `SKILL.md` + `routing-rubric.md`; added a 6th triage question (prior research on this surface) to match the rubric's own 6-factor table; added a format→tool table for non-Google-Doc inputs.
- `diy-research-plan`: added a hard stimulus-link gate at intake (so a missing link surfaces early, not at final packaging); added a carve-out for multi-part questions triage already validated; added the missing research-partner gather question; added relative-timing guidance.
- `screener`: added the exact scope-note sentence (coordinated with `unmod-script`) resolving the recruiting-pool vs. variant-assignment boundary; added a bias-risk exclusion question; added a worked double-barreled-question example; fixed the unresolvable bracket-vs-no-brackets conflict; stated a default 6-month recency window.
- `unmod-script`: added the matching scope-note sentence; split the single 2-item comparison template into two named sub-shapes (relative preference vs. N-way independent comprehension); added a required Randomization/order field; fixed the multi-stimulus First Impression gap.
- `diy-packet`: resolved the internal "assemble, don't re-derive" vs. "add a comprehension check" self-contradiction; added a "why it matters" field, a merge rule for escalation triggers, and a Step 0 trust-vs-reopen clarification.
- Caught one bug from the fix pass itself: `diy-triage`'s new pointer to the shared conventions doc used the wrong relative path (missing `../../`) — fixed by hand after review.

### Open / next
- Committing + pushing to GitHub next.
- Not re-tested against a second demo after the fixes — the original test was against a single fictional scenario; a second mock-run (ideally a different request shape, e.g. one that actually needs the researcher-led track) would validate the fixes rather than just trust them.

---

## 📅 2026-09-02 (Wed) — 5th DIY skill added: `diy-research-plan`, `diy-packet` re-grounded

### What changed
Jedida flagged that yesterday's `diy-packet` build only used Kinnera's real example (a packet, no separate plan doc) — not Ndidi's (a standalone "Unmoderated Research Plan" doc). She also named the DIY track explicitly as 5 steps: triage, **a research plan**, screener, unmoderated script, and a DIY packet — one more step than what shipped yesterday. Ran 3 parallel agents:

- **`diy-research-plan`** (new) — the missing 5th step, sitting between `/diy-triage` and `/screener`. A ~half-page, six-section planning doc grounded structurally in Ndidi's real Unmoderated Research Plan (objective, who's tested, method-fit confirm, task shape, timeline, escalation triggers). Also cross-referenced Kinnera's packet example to write a "when you might skip this and go straight to `/diy-packet`" section for small/low-stakes asks — the two real examples actually used different structures (Ndidi wrote a separate plan; Kinnera skipped straight to a packet), and the new skill documents both patterns rather than picking one. `references/plan-vs-rpp-comparison.md` maps every RPP section to what it collapses into or gets cut, with a rationale per cut.
- **`diy-packet`** (re-grounded + repositioned) — pulled in Ndidi's example as a second structural source (added a comparison/reaction-format branch and a stimuli/materials table with counterbalancing, neither present before). Repositioned as the pipeline's final assembly/handoff step — it now bundles `/diy-research-plan` + `/screener` + `/unmod-script` outputs rather than re-deriving the plan itself, with a new "Assemble, don't re-derive" content rule and a differentiation table vs. `/diy-research-plan` (in addition to the existing one vs. `/research-plan`).
- **`diy-triage`** (routing updated only) — chain references updated from `/screener → /unmod-script → /diy-packet` to `/diy-research-plan → /screener → /unmod-script → /diy-packet` in both `SKILL.md` and `references/routing-rubric.md`. Triage decision logic itself untouched.

**Confidentiality check:** grep across all 5 DIY-track skill folders for real project/requester names — clean.

README updated: new `diy-research-plan` row, `diy-packet`'s description updated to "final assembly step", DIY track chain corrected to 5 steps, and a new paragraph noting both real case studies (packet-only vs. plan-then-packet) are reflected across the pipeline rather than just one.

### Open / next
- ✅ Committed (`48f5de8`) and pushed to GitHub — blocked briefly on a locked macOS Keychain hanging `git push`/`gh auth`; resolved once the keychain was unlocked, no code changes needed. See `ERRORS.md`.
- Still not mock-run against the real case studies before shipping (carried from yesterday).
- Still open: whether `/diy-triage`'s "both tracks" output needs a harder state machine; whether the "Progress deck" artifact from Ndidi's example warrants its own skill; the standing Jun-12 confidentiality re-verification on this now-larger public repo.
- `screener` is still grounded only in a researcher-led example (Home Feed Redesign's Screener tab) — neither Kinnera's nor Ndidi's DIY-track docs had an explicit standalone screener to pull from. Flagged, not fixed — no DIY-side screener example exists to re-ground it with.

---

## 📅 2026-09-01 (Tue) — DIY research pipeline (OKR #5): 4 new skills built + shipped to GitHub

### What changed
Built out the self-serve "DIY research" pipeline scoped with Kinnera, Megan, and Ndidi (OKR #5), grounded in 4 real case studies gathered from the team (3 consumer-side from Kinnera, 1 fulfillment-side from Ndidi). Ran 4 parallel build agents, each grounded in the real doc most relevant to its skill:

- **`diy-triage`** (new) — entry gate. Routes a raw ask (PRD/brief/loose question) to the DIY track, the researcher-led track, or both in parallel; explicitly covers the escalation case (start DIY, promote to researcher-led once scope grows) and the parallel-round case. `references/routing-rubric.md` holds the decision table.
- **`screener`** (new) — standalone participant screener for the DIY track, structurally grounded in a real Screener tab (structure only — no real questions/business content carried over, verified by grep). `references/screener-question-bank.md` has 13 generic reusable question-pattern categories.
- **`unmod-script`** (new) — plain-language unmoderated task list, grounded in a real unmod test script + an unmod guide (structure only). `references/unmod-writing-rules.md` contrasts moderated instinct vs. unmoderated requirement.
- **`diy-packet`** (new) — the condensed, self-serve counterpart to `/research-plan`, grounded in a real DIY Resource Packet (structure only). Explicit "How this differs from `/research-plan`" section makes the depth split concrete. `references/packet-checklist.md` covers self-serve-readiness.
- **`/rpp` and `/synth`** — no new skills built; these are the pipeline's names for the existing `/research-plan` and `/report` skills (already the right depth for the researcher-led track). `/mod-guide` is shared unchanged across both tracks.

**Confidentiality check:** repo confirmed PUBLIC on GitHub (open re-verification item from Jun 12 still unresolved — separate from this work). All 4 new skills were built to extract only structural/methodological patterns from the real source docs — grep across all new files for the real project names and requester names came back clean.

README updated: 4 new rows in the skills table + a new "DIY Research Pipeline (OKR #5)" section documenting the two-track architecture and the `/rpp`↔`research-plan` / `/synth`↔`report` aliasing.

### Open / next
- Committing + pushing to GitHub next.
- Not yet mock-run against the 4 real case studies (per the established `mock-runs/` pattern) — built directly to `skills/` given the timeline; worth a validation pass before wider rollout.
- Two items intentionally deferred, not blocking: whether `/diy-triage` should have a formal "both tracks" structured output (currently a described option, not a hard state machine), and whether the "Progress deck" artifact from Ndidi's example warrants its own skill.
- Standing Jun-12 confidentiality re-verification action on this repo is still open — unrelated to today's build but worth closing given more content just shipped to it.

---

## 📅 2026-06-08 (Mon) — research-plan skill restructured to canonical ResOps RPP ("Option B")

### What changed
Jedida supplied the official ResOps **Research Project Plan (RPP)** template (Doc `1s6Lg4ZsiIypqANdpg4hrCwxkgwP0qOwJvGNekzgj9k0`) as *the* format ("This is the format" ×3) and chose **"Option B"**: adopt the ResOps section names + order, but keep the richer Jun-2 content folded in. The team also wants the interactive pop-up to walk sections **in the same order as the plan**, one at a time, so researchers can approve + brainstorm each section in sequence.

**OUTPUT TEMPLATE (SKILL.md) — re-ordered to ResOps:**
- Header (Key Contacts → Key Stakeholders/RACI → Research Timeline phase grid with PL/KO/IP/RO codes) → **Topic → TL;DR Summary of Findings → Background → Existing Insights → Objectives → Key Research Questions → Hypotheses / Questions of Interest from XFN leads → What decisions will be made with such research? → What Research Priorities is this relevant to (Themes) → Proposed Research Timeline → Project Details → Additional / Documents.**
- Old → ResOps remap: Goal-led **Parameters table** split into Topic + What-decisions + Project Details + Proposed Research Timeline; **Methodology** → Project Details; **Deliverables** → Deliverable Format cell + Documents; **Risks** → Project Details → Dependencies (ResOps has no Risks section); **Appendix → Additional Documents** → Additional/Documents; **Appendix → Previous Research** → Existing Insights.
- Two new ResOps sections added: TL;DR Summary of Findings, What Research Priorities (Themes). Hypotheses renamed to the ResOps row name and de-flagged from "provisional" (now canonical).

**Step 3 rewritten — section-by-section pop-up walk:**
- Replaced the old 2-batch method-questions flow with a **guided walk: one pop-up per section, in the exact OUTPUT TEMPLATE order.** First pop-up = **Existing Insights** ("here's what we already know"), then Topic → Background → Objectives → Key Research Questions → Hypotheses → What decisions → Themes → Method → Sampling → (Stimuli/Deps/Comp/Platform/Format batched) → Proposed Research Timeline → Documents.
- Each section: show the draft first → AskUserQuestion (Accept / Brainstorm with me / Edit / section-specific alternatives) → "Brainstorm" drops into a short per-section back-and-forth ("think through with Claude") → advance only after approval, with a running ✓/◻ progress list. Override: "just generate the whole thing" skips the walk.

**Rules + companions reconciled:**
- CONTENT GENERATION RULES 1, 7, 10–16, 20, 24, 26 rewritten to ResOps (Topic leads, Project Details absorbs Method+Participants, Risks→Dependencies, Deliverables→Deliverable Format/Documents, plan ends at Additional/Documents, Hypotheses canonical).
- `references/content-rules.md` fully rewritten to the ResOps structure (§1 Key Research Questions, §4 Objectives, §5 Topic/What-decisions/Themes, §6 Background+Existing Insights, §7 Project Details, §8 Proposed Research Timeline, §9 Hypotheses, §10 Additional/Documents, §11 RACI).
- Step 1.6 "Goal" question → "Topic"; cross-reference table + content-rules.md description updated.

### Supporting artifact
- `SAMPLE-COMPARISON-resops-vs-richer.md` — two full sample plans (Option A exact ResOps vs Option B richer) on the Recipe→Cart Mapping demo study, used to make the Option B decision; includes the pop-up walk order.

### Open / next
- Not committed/pushed to GitHub yet — awaiting Jedida's go-ahead.

---

## 📅 2026-06-05 (Fri) — research-plan skill updated from 2026-06-02 team workshop feedback

### What changed
Reworked the **research-plan** skill (`skills/research-plan/SKILL.md` + `references/content-rules.md`) to absorb feedback from the 2026-06-02 workshop where Jedida demoed the research skills to the UX research team.

**Flow changes (SKILL.md):**
- **New Step 1.5 — Discover Existing Context FIRST.** Before any logistics, query the research-insights agent (`mcp__research-insights__research_insights__updated`) + Glean for prior research, read the project folder, then show the researcher a verbatim background summary + top-5 existing insights + proposed hypotheses to *confirm or correct*. Fixes the demo failure of leading with "what's the study name?".
- **New Step 1.6 — Logistics + active decision-quality audit.** Logistics (decision/name/goal/timeline) move after discovery; added an active challenge of whether the decision is real, singular, and answerable this quarter.
- **Step 2 — minimum-evidence methodology framing.** Lead with the leanest valid path to a "good enough" answer + 1-2 alternatives; flag timeline conflicts.
- **New Step 6 — `/multi-agent-check` handoff.** The generated plan is a DRAFT (step 1); always route to multi-agent-check (step 2) before sharing.

**Structure changes (output template + content-rules.md):**
- **Hypotheses moved OUT of Background to a standalone H2 after Research Questions** (reverses the 2026-05-12 v2 placement; per Prakriti: "comes after objectives and research questions… then decides your methodology").
- **New Existing Insights H2 after Background** — top 3-5 prior findings, each with a **verbatim** quote + clickable source (Amalia's no-source-no-insight rule; Prakriti + Amalia).
- Rewrote content-rules §6 (Background = Problem Statement + Product Context + new Existing Insights), added §12 (standalone Hypotheses), revised SKILL Rules 7 + 22, added Rules 27-31.

**Connections verified (Jedida asked):**
- ✅ Research-insights Glean agent is wired and callable.
- ❌ Snowflake is NOT wired as an MCP in this environment — skill now flags this and routes to a DS partner instead of fabricating data.

### Open / provisional
- Several ordering decisions (hypotheses placement; whether "Decisions this informs" becomes its own section) are flagged **PROVISIONAL** pending the team's canonical format doc (Bihan's template) + Prakriti's offline notes. A ⚠️ reconciliation note sits atop the OUTPUT TEMPLATE.
- Amalia preferred hypotheses grouped near Background (background → objective → hypothesis → research questions); Prakriti's after-questions placement is the current default — needs final confirmation.
- Not committed/pushed to GitHub yet (awaiting Jedida's go-ahead + the format doc).

---

## 📅 2026-05-11 (Mon) — seeded

### Notes
- PROGRESS.md initialized as part of new daily auto-save system. Auto-run fires at 4 PM PT weekdays via `com.jedida.daily-progress-save.plist`. Manual trigger: "save progress now".
- Re-labeled from "P5" to "P4 sub-stream" on 2026-05-11 after project renumbering — Project 5 is now `Project-5-End-to-End-Meals-Research/`.

---
