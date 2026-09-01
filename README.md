# Research Team — Claude Code Skills

Shared Claude Code skills for UX researchers at Instacart. Built for the Research AI Enablement OKR (H1 2026).

Each skill is grounded in methodology from the most trusted voices in UX research — leading UX researchers in the industry and research teams at major big tech companies.

## Skills

| Command | Skill | What it does |
|---------|-------|--------------|
| `/research-plan` | Research Plan | Generates a structured research plan (objectives, methodology, timeline, deliverables) tailored to your study |
| `/mod-guide` | Moderation Guide | Generates moderation guides for in-depth interviews, usability tests, and diary studies |
| `/analysis` | Analysis | Thematic analysis, tagging, and pattern recognition for qualitative and quantitative data |
| `/report` | Research Report | Research reports with executive summaries, findings, recommendations, and next steps |
| `/usertesting-plan` | UserTesting Plan | Designs the study-level structure for an unmoderated UserTesting study — task count, ordering, coverage levels, stimulus type per task, synthesis tail |
| `/usertesting-script` | UserTesting Script | Writes the question-level script handed to the UserTesting programmer — 4-way platform tagging, action ladders, choice-order rules, warm closing card |
| `/usertesting-html` | UserTesting HTML | Builds the visual stimuli HTML — dual-phone / two-cart / single-row card patterns, design tokens, image labels, subtotal audit, image-quality QA |
| `/usertesting-orchestrator` | UserTesting Orchestrator | Coordinates the full plan → script → HTML pipeline end-to-end, owns shared-context handoffs, runs the 3-layer triangulation audit |
| `/diy-triage` | DIY Triage | Entry gate for a raw research ask — routes it to the DIY track, the researcher-led track, or both in parallel, and flags when a DIY study should escalate mid-stream |
| `/screener` | Screener | Standalone participant screener for a self-serve unmoderated study — no researcher needed to interpret it afterward |
| `/unmod-script` | Unmoderated Test Script | Plain-language task list and instructions for an unmoderated usability test, written for a participant working alone |
| `/diy-packet` | DIY Research Packet | Condensed, self-serve research packet bundling screener + script + launch instructions — the lightweight counterpart to `/research-plan` |

All skills follow the same pattern:

1. Ask introductory questions about your study
2. Propose a methodology grounded in published research standards
3. Let you review and adjust
4. Ask about style (reference doc, Instacart default template, or clean outline)
5. Generate the deliverable
6. Offer to upload to Google Docs

## DIY Research Pipeline (OKR #5)

A self-serve pipeline for designers, PMs, content leads, and fulfillment partners who need a research read without necessarily needing a researcher to run it. `/diy-triage` is the entry point; it routes into one of two tracks, or both:

- **DIY track** (self-serve, no researcher needed): `/screener` → `/unmod-script` → `/diy-packet`
- **Researcher-led track** (deeper, needs a UX researcher): `/rpp` → `/mod-guide` → `/synth`

`/rpp` and `/synth` aren't new skills — they're this pipeline's names for the existing `/research-plan` and `/report` skills, which already produce the depth a researcher-led study needs. `/mod-guide` is the same skill either way. The only genuinely new skills are the four DIY-track-specific ones plus the triage gate, listed in the table above. The deliberate split: `/rpp` (`/research-plan`) stays deep and technical; `/diy-packet` is the intentionally smaller, plain-language equivalent for someone running their own study.

## Install

See [INSTALL.md](./INSTALL.md).

## Contributing

Found a better methodology? Want to add a new skill? Open a PR. Each skill lives in `skills/{skill-name}/SKILL.md`. Heavy methodology references live in `skills/{skill-name}/references/`.

## Credits

Built by **[Jedida Milton](https://instacart.enterprise.slack.com/messages/U099PKHAM9D)** for the Research team.

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
