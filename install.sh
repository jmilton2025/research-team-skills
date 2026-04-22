#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"

mkdir -p "$SKILLS_DIR"

for skill in research-plan mod-guide analysis report; do
  src="$REPO_DIR/skills/$skill"
  dst="$SKILLS_DIR/$skill"

  if [ ! -d "$src" ]; then
    echo "Skipping $skill — source directory not found at $src"
    continue
  fi

  if [ -e "$dst" ] && [ ! -L "$dst" ]; then
    echo "Warning: $dst exists and is not a symlink. Backing up to $dst.bak"
    mv "$dst" "$dst.bak"
  fi

  ln -sfn "$src" "$dst"
  echo "Linked /$skill → $src"
done

echo ""
echo "Done. Open Claude Code and type / to see the new skills."
