# Interactive input conventions (shared across all DIY-pipeline skills)

Every skill in the DIY research pipeline (`diy-triage`, `diy-research-plan`, `screener`, `unmod-script`, `diy-packet`) gathers or confirms input from the requester at one or more points. The preferred mechanism is the `AskUserQuestion` tool — structured, multiple-choice-friendly, easy for the requester to scan.

**`AskUserQuestion` is not guaranteed to be available in every runtime.** A 2026-09-02 test pass found it absent in 5/5 DIY-pipeline skill runs, with no documented fallback in any of them — the implementer was left to guess rather than ask, which directly contradicts this pipeline's own "never fabricate, ask rather than default" rule.

## The rule

Before any step that calls for `AskUserQuestion`:

1. Attempt it as normal.
2. If it isn't available (missing from the active tool list, or a `ToolSearch` for it returns no match), **fall back to asking conversationally in the same message** — write out the same questions, in the same batches, as plain numbered text — and wait for the requester's reply before proceeding.
3. Record the requester's answers inline in your working notes (or the output doc's draft) exactly as if they'd come through the structured tool. Don't skip a question because the structured tool isn't available, and don't answer it yourself.

This applies identically across all 5 skills — fix it once here rather than five separate times per SKILL.md.

## Referenced by

- `skills/diy-triage/SKILL.md`
- `skills/diy-research-plan/SKILL.md`
- `skills/screener/SKILL.md`
- `skills/unmod-script/SKILL.md`
- `skills/diy-packet/SKILL.md`
