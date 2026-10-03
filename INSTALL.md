# Install the Research Team Skills

These skills work inside Claude Code. Install them by symlinking into `~/.claude/skills/` so they're discovered automatically.

## Quick Install (recommended)

```bash
# 1. Clone this repo somewhere you'll keep it
git clone https://github.com/jmilton2025/research-team-skills.git ~/research-team-skills

# 2. Symlink each skill into ~/.claude/skills/
cd ~/research-team-skills
./install.sh
```

## Manual Install

```bash
# From the cloned repo directory:
for skill in research-plan mod-guide analysis report multi-agent-check usertesting-plan usertesting-script usertesting-html usertesting-orchestrator; do
  ln -sf "$(pwd)/skills/$skill" "$HOME/.claude/skills/$skill"
done
```

## Requirements

- Claude Code.
- Python 3.9 or later. On a Mac, `/usr/bin/python3` works once Apple's Command Line Tools are installed (`xcode-select --install`). The skills' scripts use only the standard library.
- For skills that deliver a Google Doc (such as `/research-plan` and `/mod-guide`): a Google Docs integration that can create, batch-update, and export a Doc. For `/research-plan`, the `gws` command-line tool also works.

## Verify

Open Claude Code and type `/` — you should see `/research-plan`, `/mod-guide`, `/analysis`, `/report`, `/multi-agent-check`, and the 4 `/usertesting-*` skills in the skill list.

## Uninstall

```bash
for skill in research-plan mod-guide analysis report multi-agent-check usertesting-plan usertesting-script usertesting-html usertesting-orchestrator; do
  rm "$HOME/.claude/skills/$skill"
done
```

## Update

```bash
cd ~/research-team-skills && git pull
```

Symlinks stay valid — the latest skill version is picked up automatically.

Update only between runs, never while a `/research-plan` run is in progress. The run's manifest records a fingerprint of the skill's layout files, and the later build steps stop with “Skill files changed since this manifest was generated” if they change mid-run. If that happens, rerun the manifest step, as the message says.

## Need the self-serve DIY skills instead?

If you're a designer, PM, or content lead who just needs a fast tactical read without a researcher — see the companion [diy-research-skills](https://github.com/jmilton2025/diy-research-skills) repo instead.
