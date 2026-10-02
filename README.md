# Research Team — Claude Code Skills

Shared Claude Code skills for UX researchers at Instacart. Built for the Research AI Enablement OKR (H1 2026).

Each skill is grounded in methodology from the most trusted voices in UX research — leading UX researchers in the industry and research teams at major big tech companies.

## Skills

| Command | Skill | What it does |
|---------|-------|--------------|
| `/research-plan` | Research Plan | Generates a structured research plan and delivers it as an edited, verified Google Doc in the exact Option 4 — Leadership visual system |
| `/mod-guide` | Moderation Guide | Builds interview or prototype/usability guides, audits them for protocol and method safety, and delivers a verified Option 4 Google Doc |
| `/analysis` | Analysis | Thematic analysis, tagging, and pattern recognition for qualitative and quantitative data |
| `/report` | Research Report | Research reports with executive summaries, findings, recommendations, and next steps |
| `/multi-agent-check` | Multi-Agent Check | Before anything is shared, two researcher reviewers check the finished deliverable in parallel — an Evidence checker (quotes, numbers, claim strength) and a Stakeholder reader (clarity, actionability) — and return one fix list with a Ready / Fix-first verdict |
| `/usertesting-plan` | UserTesting Plan | Designs the study-level structure for an unmoderated UserTesting study — task count, ordering, coverage levels, stimulus type per task, synthesis tail |
| `/usertesting-script` | UserTesting Script | Writes the question-level script handed to the UserTesting programmer — 4-way platform tagging, action ladders, choice-order rules, warm closing card |
| `/usertesting-html` | UserTesting HTML | Builds the visual stimuli HTML — dual-phone / two-cart / single-row card patterns, design tokens, image labels, subtotal audit, image-quality QA |
| `/usertesting-orchestrator` | UserTesting Orchestrator | Coordinates the full plan → script → HTML pipeline end-to-end, owns shared-context handoffs, runs the 3-layer triangulation audit |

All skills use collaborative approval gates: Claude recommends starting content, the researcher can accept, edit, or brainstorm alternatives, and nothing advances until the current decision is approved.

**`/research-plan` contract:**

1. Audit the decision before reading prior evidence; stop or reframe when the answer is already closed.
2. Authorize and discover existing evidence, then recommend the minimum valid research design.
3. Approve the plan in three interactive sections: **Context & Foundation → Research Design → Outputs**. The final Google Doc assembles those approved rows into the four overview bands: **Key Information → Project Details → Deliverables & Next Steps → Appendix**.
4. Confirm the exact Google Drive destination.
5. Copyedit, create, normalize, apply the exact Option 4 layout, verify, render, and only then return the Google Doc link.

Every final plan uses **Option 4 — Leadership**: pageless editing with landscape-letter export geometry, DM Serif Display/DM Sans typography, a separate at-a-glance Research Timeline, pale-yellow mock warning when applicable, and the two-column Project Plan Overview with white body cells and dark-green two-cell section bands. The bundled formatter and verifier make this consistent for colleagues without requiring access to a private reference Doc. Final delivery requires a write-capable Google Docs integration that can apply native batch updates, return raw document structure, and export/render the result; `gws` is the documented command-line path. If the exact contract cannot be applied and rendered, the skill blocks completion instead of returning a downgraded document. Project Details remains adaptive: **Method & approach**, **What does success look like?**, and **Dependencies & guardrails** are core; fields such as **Sample & evaluators** and **Measures & analysis** appear only when the study needs them. The Appendix contains only **Additional UXR documents** and **Resources from XFN**.

Mock/test runs keep artifacts out of Drive by default and add a prominent test warning unless the tester explicitly requests a test document.

**`/mod-guide` contract:**

1. Authorize and minimize non-public source material before access; participant operations data stays outside the guide.
2. Choose Interview or Prototype/Usability first, then approve the source-grounded parameters and content blocks for that format.
3. Run the mandatory safety/method audit; the enhanced two-reviewer panel is optional and receives only approved, de-identified material.
4. Confirm the exact Drive folder, intended audience, effective permissions, and one authorized partial-document recovery path before creation.
5. Create once; fail closed on document/manifest drift; apply revision-bound normalization and formatting; then read back content/location/permissions, render, and verify before returning the link.

Every moderation guide uses `# Moderation Guide` plus the study title. Interview bodies use nested question/probe bullets and one Consent table; prototype bodies use bold-label read/do lists and keep only the Parameter and Session Flow tables. Recording, privacy, anonymity, retention, and incentive language comes only from an approved plan or ResOps protocol. **Option 4 — Leadership** is the default visual system, with plain native Google Docs available only as an explicit or pre-approved disclosed fallback.

## Need a self-serve, no-researcher-required read instead?

The lighter, self-serve pipeline (`/diy-triage`, `/diy-research-plan`, `/screener`, `/unmod-script`, `/diy-packet`) moved to its own repo on 2026-09-03: [diy-research-skills](https://github.com/jmilton2025/diy-research-skills). It's for designers, PMs, and content leads who need a fast tactical read without a researcher running it, and it hands off to the skills in *this* repo (`/research-plan`, `/mod-guide`, `/report`) whenever a question actually needs one.

## Install

See [INSTALL.md](./INSTALL.md).

## Contributing

Found a better methodology? Want to add a new skill? Open a PR. Each skill lives in `skills/{skill-name}/SKILL.md`. Heavy methodology references live in `skills/{skill-name}/references/`.

Before changing `/research-plan`, run its contract test:

```bash
python3 skills/research-plan/tests/validate_contract.py
python3 skills/research-plan/tests/test_option4_layout.py
```

Behavioral pressure scenarios, the Option 4 fixture, and the exact visual-contract test are documented in `skills/research-plan/tests/README.md`.

Before changing `/mod-guide`, run its cross-file and formatter tests:

```bash
python3 skills/mod-guide/tests/validate_contract.py
python3 skills/mod-guide/tests/test_option4_guide_layout.py
```

The current template fixtures, revision/idempotency regressions, and behavioral acceptance scenarios are documented in `skills/mod-guide/tests/README.md`.

## Credits

Built by **[Jedida Milton](https://github.com/jmilton2025)** for the Research team.

Methodology grounded in the published work of the following researchers and organizations. Click any name to go directly to their work:

### Individual researchers & authors

- [Erika Hall](https://mule.design/) — co-founder, Mule Design; author of *Just Enough Research*
- [Indi Young](https://indiyoung.com/) — author of *Listening Deeply* and *Mental Models*
- [Steve Portigal](https://www.portigal.com/) — author of *Interviewing Users* and *Doorbells, Danger, and Dead Batteries*
- [Tomer Sharon](https://www.tomersharon.com/) — author of *Validating Product Ideas*
- [Nikki Anderson](https://userresearchacademy.com/) — founder, User Research Academy
- [Virginia Braun & Victoria Clarke](https://www.thematicanalysis.net/) — authors of *Thematic Analysis: A Reflexive Approach*

### Research publications & blogs

- [Nielsen Norman Group (nngroup.com)](https://www.nngroup.com/articles/)
- [dscout People Nerds](https://dscout.com/people-nerds)
- [UserTesting Blog](https://www.usertesting.com/blog)
- [Maze Research Blog](https://maze.co/blog/)
- [User Research Academy (Nikki Anderson)](https://userresearchacademy.com/)

### Big tech research teams

- [Meta Research](https://research.facebook.com/)
- [Google Design](https://design.google/)
- [Microsoft Research](https://www.microsoft.com/en-us/research/)
- [Amazon Science](https://www.amazon.science/)
