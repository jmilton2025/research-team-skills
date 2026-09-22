# Output status & labeling conventions (this repo's researcher-led skills)

> The DIY-track skills this doc's §1 (BLOCKED/PENDING) originally covered moved to the companion [diy-research-skills](https://github.com/jmilton2025/diy-research-skills) repo on 2026-09-03, and took their own copy of this doc (with §1) with them. This copy keeps only what `research-plan`, `mod-guide`, and `report` still reference — test-artifact labeling. The two copies are independent going forward, not synced.

## Test-run / demo labeling (`research-plan`, `mod-guide`, `report`, `usertesting-orchestrator`)

None of these skills has a built-in way to say "this output was generated as part of a mock-run / demo test, not a real deliverable." When generating output for anything you know is a test or simulation (invented findings, a fictional demo scenario, a stress-test of the skill itself, etc.) rather than a real study:

- Add a single line directly under the document's header: **`⚠️ TEST ARTIFACT — generated for a mock-run / demo, not a real deliverable. Do not file or share as real research.`**
- This applies most importantly to `/report`, where fabricated findings might otherwise read as real ones if the file were found later without context — and to `usertesting-orchestrator`, which can produce a full plan+script+HTML bundle (three fabricated-looking deliverables) in one pass.
- Omit this line for any real, non-test invocation.

## Referenced by

- `skills/research-plan/SKILL.md`, `skills/mod-guide/SKILL.md`, `skills/report/SKILL.md`, `skills/usertesting-orchestrator/SKILL.md`
