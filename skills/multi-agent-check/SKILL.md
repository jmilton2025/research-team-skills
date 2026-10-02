---
name: multi-agent-check
description: Use before a research deliverable is shared or published (research plan, moderation guide, analysis, report, UserTesting script) to have two independent researcher reviewers check it in parallel — one against the evidence, one as the stakeholder who will read it — and return one merged fix list with a Ready or Fix-first verdict.
---

# Multi-Agent Check

> Invoke with `/multi-agent-check`

Two other researchers read the draft before anyone else does. Each has one job and one point of view. They review independently and at the same time, then their notes are merged into one short fix list.

This is a final check, not a rewrite. The researcher owns the deliverable and decides which fixes to take.

## The two reviewers

| Reviewer | Their question | What they check |
|---|---|---|
| **Researcher 1 — Evidence checker** | *Is every claim true to the data?* | Quotes are word-for-word in the source · numbers, counts (N of M), names, and dates match the source · each finding has enough evidence behind it · nothing is claimed more strongly than the sample supports · inference isn't presented as something participants said · contradicting evidence isn't left out |
| **Researcher 2 — Stakeholder reader** | *Can the person this is for understand it and act on it?* | Reads as the named audience (PM, leadership, ML partner, design) · bottom line is up front · each recommendation is specific and traces to a finding · no unexplained jargon or acronyms · no internal notes, to-dos, or placeholders left in · tone fits the audience · easy to scan |

## Steps

### 1. Gather what the reviewers need

- **The draft** — the final version, after any self-critique. Accept a local file, pasted text, or a Google Doc link (read it with the connected Google Docs tool). Save it as a local file so both reviewers read the same text.
- **The sources** — transcripts, data, the brief or PRD, prior research: whatever the draft's claims rest on. For `/analysis`, also pass the approved scope and evidence ledger. For research instruments (moderation guides, discussion guides, surveys, or screeners), pass the approved study plan and applicable consent/privacy protocol. If no sources are available, the Evidence checker checks internal consistency and rigor and discloses that source-dependent claims could not be verified.
- **The audience** — who will read it.

When another skill calls this one at its quality step (`/research-plan`, `/mod-guide`, `/analysis`, `/report`), take these from that skill's context. Don't re-ask.

**Connections:** if reading the draft or a source needs a connector that isn't connected (Google Docs/Drive, Glean), stop at that step. Tell the researcher which connection, what it's for, and how to connect it (`/mcp` in Claude Code, or the connector's settings on claude.ai). Wait. Skip a source only if the researcher chooses to, and list it under **Couldn't check**.

**Data boundary:** the reviewers run inside this session. Never send the draft or sources to an outside tool or service to run the check.

### 2. Confirm (only when run on its own)

When the researcher runs `/multi-agent-check` directly, confirm in one line before starting:

> Two researchers will review **[draft]** for **[audience]**: an Evidence checker against [sources], and a Stakeholder reader reading as [audience]. Takes a few minutes. Start?

When another skill calls it as an automatic quality step, skip this — the researcher was already told the review is coming.

### 3. Run both reviewers at the same time

Send two Agent tool calls in one message so they run in parallel and neither sees the other's notes. Give each its brief below, with the draft path, source paths, and audience filled in.

**Evidence checker brief:**

```
You are a senior UX researcher doing a final evidence check on a draft before it is shared. Your only question: is every claim true to the data?

Read the draft at [DRAFT] and the sources at [SOURCES]. Check:
- Classify quotation purpose before checking it. Participant quotations and wording attributed to a source must appear word-for-word in that source; search for them. A paraphrase presented as an evidence quotation is a must-fix.
- Research instruments contain newly drafted moderator scripts, questions, probes, hypothetical scenarios, and response options. These are authored content, not evidence quotations; do not flag their absence from a source as invented participant evidence. Quoted feature names and terms are not participant quotations either. An attributed participant quotation inside a script still requires verbatim checking.
- This is not a factual-check exemption: verify numbers, counts (N of M), names, dates, and factual claims embedded in scripts, including recording, privacy, access, retention/deletion, and incentive promises, against the supplied plan or approved protocol.
- Each finding has enough evidence behind it, and nothing is claimed more strongly than the sample supports (e.g., "users" from 3 sessions).
- Inferences are not presented as something participants said.
- Evidence that contradicts a finding is not left out.
If there are no sources, check internal consistency instead: numbers agree across sections, sample sizes match, the method fits the research question, and questions aren't leading.

Report only real problems. For each: severity (must-fix = wrong, invented, or would mislead the reader; should-fix = weak or would draw a question), where it is, the problem, a concrete fix, and the evidence (the source line, or "not found in any source"). Your fix must not add details the sources don't support. If you couldn't open a source, list it under "Couldn't check" — never guess. End with a one-line overall read.
```

**Stakeholder reader brief:**

```
You are a senior UX researcher reading a draft the way [AUDIENCE] will read it, right before it is shared. Your only question: can they understand it and act on it?

Read the draft at [DRAFT]. Check:
- The bottom line is clear on the first screen.
- Each recommendation is specific, doable, and traces to a finding.
- No unexplained jargon or acronyms for this audience.
- No internal notes, to-dos, placeholders, or planning details left in.
- The tone fits this audience, and the draft is easy to scan.

Report only real problems. For each: severity (must-fix = the reader would misunderstand it or couldn't act on it; should-fix = harder to use than it needs to be), where it is, the problem, and a concrete fix. Don't change what the findings say — that's the Evidence checker's job. End with a one-line overall read.
```

If the Agent tool isn't available, say so and run the two briefs yourself, one after the other. Label the result **"Self-review — independent reviewers unavailable here."** Never call it an independent review.

### 4. Merge into one list

- Combine duplicates: when both reviewers flag the same thing, keep one item and name both.
- Before listing an Evidence checker must-fix, confirm it against the source yourself. Refute quote-mismatch findings about newly authored instrument scripts, questions, probes, scenarios, response options, or feature-name labels; still verify their factual claims and any attributed participant quotations. Drop findings you can't confirm and say why; source-dependent claims that remain unverifiable belong under **Couldn't check**, not a claim of readiness.
- Order: must-fix first, then should-fix.
- Verdict: **READY ✅** when there are no must-fixes; **FIX FIRST — N must-fixes** otherwise.

### 5. Show the result

```
MULTI-AGENT CHECK — [draft name]
Verdict: FIX FIRST — 2 must-fixes

Must fix
1. [Where] — [problem]. Fix: [concrete edit]. (Evidence checker)
2. [Where] — [problem]. Fix: [concrete edit]. (Both reviewers)

Should fix
- [Where] — [problem]. Fix: [concrete edit]. (Stakeholder reader)

Couldn't check
- [source] — [why]

Reviewer reads
- Evidence checker: [one line]
- Stakeholder reader: [one line]
```

Leave out any empty section.

### 6. Apply fixes

- **Run on its own:** show the list and let the researcher choose. Apply only the fixes they pick.
- **Called from another skill:** return the merged list to that skill, which folds in confirmed fixes at its own step.
- Re-run the check only if a must-fix changed a claim, or the researcher asks. One re-run is usually enough.

## Rules

- Two reviewers, two different views. Don't add reviewers, scores, or extra rounds.
- Every finding is concrete: where it is, what's wrong, and the exact fix.
- Not applying a fix is a normal outcome. The researcher decides.
- Never report the check as run if it didn't run. If it couldn't, say so; the calling skill then discloses a critique-only run.
