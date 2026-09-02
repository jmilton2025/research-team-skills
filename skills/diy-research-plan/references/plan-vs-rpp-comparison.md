# DIY Research Plan vs. Full RPP — Section-by-Section

A side-by-side of this skill's condensed output template against `/research-plan`'s full ResOps Research Project Plan (RPP) template, so the size and depth difference is concrete rather than a vibe. Load this when someone asks "why doesn't the DIY plan have a [X] section" or wants to see exactly what got cut and why.

## At a glance

| | `/research-plan` (RPP) | `/diy-research-plan` |
|---|---|---|
| **Audience** | A trained UX researcher | A designer, PM, or content lead with no research training |
| **Length** | ~8+ pages | ~half a page |
| **Section count** | 13 major sections + header block | 6 sections + a 3-line header |
| **Method justification** | Minimum-evidence framing, 1-2 alternatives, defended with citations when questioned | A 3-item checklist confirming the `/diy-triage` fit call still holds |
| **Sample-size defense** | Cites Nielsen (2000) / Guest et al. (2006) when pushed back on | States a rough N and moves on — the method is already pre-decided as DIY-appropriate |
| **Existing insights** | Standalone section, top 3-5 findings, each verbatim-sourced with a link | One yes/no line: did we check first |
| **Safety net** | Researcher's own judgment, live, plus the RPP Critique framework (`multi-agent-check`) | A hardcoded "when to loop a researcher back in" section, built into the doc itself |
| **What's downstream** | `/mod-guide` (a moderator reads and adapts it live) | `/screener` and `/unmod-script` (this doc only points to them) |

## Section-by-section mapping

| RPP section (`/research-plan`) | DIY plan equivalent (`/diy-research-plan`) | Why |
|---|---|---|
| Header — Key Contacts, Key Stakeholders/RACI, Research Timeline phase grid | Header — Owner + Research partner, two names, no RACI | A DIY study has one owner and one point of escalation, not a four-role RACI matrix |
| **Topic** | Folded into §1 "What We're Trying to Learn" | One sentence does the job both sections were doing at this scale |
| **TL;DR Summary of Findings** *(filled at study end)* | Cut entirely | No leadership-facing TL;DR slot needed — the owner reads their own results directly |
| **Background** (Problem Statement + Product Context) | A single "why it matters" line inside §1 | The requester already knows the context; a background section would just restate what prompted the ask |
| **Existing Insights** *(top 3-5, verbatim-sourced)* | One line in §1: "did we check first?" (yes/no + what was found) | Still mandatory to check — just not written up as its own sourced section |
| **Objectives** *(3, numbered, bold-lead statements)* | §1 "The one thing we need to know" — a single goal | DIY scope is deliberately one question; three objectives is a signal to trim, not a target to hit |
| **Key Research Questions** *(3, broad project-level)* | Same single question as above — no separate research-questions layer | At this scope, the objective and the research question are the same sentence |
| **Hypotheses / Questions of Interest from XFN leads** | Cut entirely | A DIY study is a single-round check, not a hypothesis-testing program with beliefs to pressure-test |
| **What decisions will be made with such research?** | Folded into §1's "why it matters" line | One line does the job a standalone section does at RPP scale |
| **Research Priorities (Themes)** | Cut entirely | Org-priority mapping is a researcher/leadership concern, not something a self-serve requester needs to state |
| **Method + Approach** *(Project Details — minimum-evidence framing, 1-2 alternatives)* | §3 "Why Unmoderated Is the Right Call Here" — a 3-item checklist | The method was already chosen by `/diy-triage`; this section re-confirms fit, it doesn't re-derive it |
| **Sampling Plan / Participants** *(Project Details — cohorts, completes, recruit source)* | §2 "Who's Being Tested" — one-line audience + rough N, pointer to `/screener` | Full sampling detail lives in the screener; this plan only needs enough to know what to ask `/screener` for |
| **Stimuli / Dependencies / Compensation / Research Platform / Deliverable Format** *(Project Details)* | Not present — pointer to `/screener`, `/unmod-script`, and `/diy-packet` | These are build-time details that belong to the downstream artifacts, not the alignment doc that precedes them |
| **Proposed Research Timeline** *(dated milestone table, ResOps SLA-aware)* | §5 "Rough Timeline" — 3 rough dates, no SLA citation | A DIY study doesn't run through ResOps recruiting SLAs; the dates are the requester's own build/launch/results targets |
| **Additional → Documents** *(clickable links, auto-linked from kickoff inputs)* | Cut entirely | No formal document ledger — any links the requester needs live in their own thread or the `/diy-triage` output |
| *(no RPP equivalent)* | §6 "When to Loop a Researcher Back In" | The RPP assumes a researcher is driving throughout, so it has no escalation section. A DIY plan has no one driving by default, so this is the one section it has that the RPP doesn't. |

## The one-line version

The RPP defends a study; the DIY plan just aligns two people on what's about to be built. Everything cut above was cut because a full RPP is proving something to a research audience that already expects that proof — a DIY plan is talking to someone who doesn't need it proven, only pointed in the right direction.
