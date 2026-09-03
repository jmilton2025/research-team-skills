# Output status & labeling conventions (shared across DIY-pipeline and researcher-led skills)

Two patterns kept getting reinvented independently, differently, by different skills. Fix each once, here, rather than per skill.

## 1. Blocked status (DIY-track skills: `diy-research-plan`, `screener`, `unmod-script`, `diy-packet`)

When a hard gate fires and the deliverable can't be marked launch-ready (e.g. a missing stimulus link), don't invent an ad hoc status line. Use this exact convention:

- Add a single line directly under the document's header: **`Status: BLOCKED — <one-sentence reason>`** (e.g. `Status: BLOCKED — waiting on stimulus link from requester`).
- Omit this line entirely when nothing is blocking — don't add `Status: READY` or similar; absence of the line means ready.
- If a downstream skill receives an upstream artifact with a `Status: BLOCKED` line, it should surface that blocker rather than working around it or ignoring it.
- **A third state, for the case that isn't fully blocked but isn't clean either:** when the document is otherwise complete and only one or two minor items are pending on something trivial (e.g. the requester already agreed to send an asset same-day), use **`Status: PENDING — <one-sentence reason>`** instead of BLOCKED. The distinction: BLOCKED means don't proceed to the next skill yet; PENDING means proceed, but the named item still needs to close out before this ships to real participants.
- **When a tool, not the requester, is the reason something can't be verified** (e.g. a Figma link exists and is real, but this session's tooling can't fetch it — see `interactive-input-conventions.md`'s intake-fallback section) — that is a `PENDING` case, not `BLOCKED`. `BLOCKED` is for "the requester hasn't produced the thing yet." A real, ready asset that this session's tools simply can't reach is unverified content, not a missing asset — mark it `PENDING — <what's unverified and why>` and proceed.
- **Propagation:** if a downstream skill receives an upstream artifact carrying `Status: PENDING`, carry that status forward into its own output (don't silently absorb it into a lower section, and don't treat it as fully resolved) until the named item actually clears. This mirrors the existing rule for `BLOCKED` — the two states differ in whether you proceed, not in whether you propagate.
- **Retirement:** once a `BLOCKED` or `PENDING` item's underlying condition actually resolves (the asset arrives, the copy gets confirmed), the skill producing the *next* artifact in the chain should state the resolution explicitly in its own output, and note that the status no longer applies. Don't assume the original document will be edited after the fact — in a cold pickup (a different researcher, or the same one after time has passed), nobody will know to go back and remove it otherwise.

## 2. Test-run / demo labeling (all skills in this repo)

None of these skills has a way to say "this output was generated as part of a mock-run / demo test, not a real deliverable." When generating output for anything you know is a test or simulation (invented findings, a fictional demo scenario, simulated stakeholder answers, etc.) rather than a real study:

- Add a single line directly under the document's header: **`⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.`**
- This applies most importantly to `/report`, where fabricated findings might otherwise read as real ones if the file were found later without context — but any skill's output can be mistaken for real work if separated from its mock-runs folder, so the convention applies repo-wide, not just to the three researcher-led skills.
- Omit this line for any real, non-test invocation.

## Referenced by

- `skills/diy-research-plan/SKILL.md`, `skills/screener/SKILL.md`, `skills/unmod-script/SKILL.md`, `skills/diy-packet/SKILL.md` (§1 and §2)
- `skills/diy-triage/SKILL.md`, `skills/research-plan/SKILL.md`, `skills/mod-guide/SKILL.md`, `skills/report/SKILL.md` (§2)
