# P4 (sub-stream) Progress — Research Team Skills

**Parent project:** P4 — Research OKR / AI Enablement
**Last updated:** 2026-06-08
**Current state:** Core skills shipped — /mod-guide (7-phase pipeline + H.E.A.R.T.), jedi-doc-styling-1 (Research Plan template, 226/226 verifier pass), jedi-doc-styling-2 (GlossGenius). **research-plan skill now restructured to the canonical ResOps RPP template** (Option B: ResOps order + names, richer Jun-2 content folded in) with a section-by-section interactive pop-up walk (first pop-up = Existing Insights). Not yet committed to GitHub. Infrastructure: GitHub repo + Drive folder + local skill chain validated end-to-end.

> Daily entries for this sub-stream may also appear in `~/Documents/Claude/Project-4-Research-OKR-AI-Enablement/PROGRESS.md` under a "Research Team Skills" sub-heading. This file is the dedicated log.

---

<!-- New daily entries are prepended ABOVE this line. Do not delete this marker. -->

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
