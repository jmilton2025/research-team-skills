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
for skill in research-plan mod-guide analysis report; do
  ln -sf "$(pwd)/skills/$skill" "$HOME/.claude/skills/$skill"
done
```

## Verify

Open Claude Code and type `/` — you should see `/research-plan`, `/mod-guide`, `/analysis`, and `/report` in the skill list.

## Uninstall

```bash
for skill in research-plan mod-guide analysis report; do
  rm "$HOME/.claude/skills/$skill"
done
```

## Update

```bash
cd ~/research-team-skills && git pull
```

Symlinks stay valid — the latest skill version is picked up automatically.
