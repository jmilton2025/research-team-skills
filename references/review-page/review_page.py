#!/usr/bin/env python3
"""Build and read the shared HTML review page used by the research skills.

  build STATE.json OUT.html   Fill template.html with a review state and write the page to publish.
  read PAGE.html              Print the review state saved in a published page (after Artifact read).

Standard library only. The state schema is documented in README.md beside this script.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "template.html"
STATE_RE = re.compile(r'(<script type="application/json" id="review-state">)(.*?)(</script>)', re.S)
KINDS = {"content", "choice"}
TONES = ("context", "design", "outputs", "setup", "choice")
SECTION_TONES = {"1": "context", "2": "design", "3": "outputs", "4": "setup"}
BRAINSTORM = "__brainstorm__"


class StateError(ValueError):
    pass


def validate(state: dict) -> None:
    for key in ("skill", "study", "round", "items"):
        if not state.get(key):
            raise StateError(f"state.{key} is required")
    ids = set()
    for i, item in enumerate(state["items"]):
        where = f"items[{i}]"
        for key in ("id", "title", "kind"):
            if not item.get(key):
                raise StateError(f"{where}.{key} is required")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", item["id"]):
            raise StateError(f"{where}.id must use letters, digits, - or _")
        if item["id"] in ids:
            raise StateError(f"{where}.id duplicates {item['id']}")
        ids.add(item["id"])
        if item["kind"] not in KINDS:
            raise StateError(f"{where}.kind must be one of {sorted(KINDS)}")
        if item["kind"] == "content" and not (item.get("bullets") or item.get("draft")):
            raise StateError(f"{where} needs bullets (list rows) or draft (single text)")
        if item.get("tone") and item["tone"] not in TONES:
            raise StateError(f"{where}.tone must be one of {list(TONES)}")
        bullet_ids = set()
        for j, b in enumerate(item.get("bullets") or []):
            if not b.get("text"):
                raise StateError(f"{where}.bullets[{j}].text is required")
            if b["id"] in bullet_ids:
                raise StateError(f"{where}.bullets[{j}].id duplicates {b['id']}")
            bullet_ids.add(b["id"])
            for src in b.get("sources") or []:
                if src.get("url") and not src["url"].startswith("https://"):
                    raise StateError(f"{where}.bullets[{j}] source URLs must be https")
        if item["kind"] == "choice":
            options = item.get("options") or []
            if len(options) < 2:
                raise StateError(f"{where} needs at least two options")
            if sum(1 for o in options if o.get("recommended")) > 1:
                raise StateError(f"{where} may mark only one option Recommended")
            for o in options:
                if not o.get("id") or not o.get("label"):
                    raise StateError(f"{where} options need id and label")
        for s in item.get("sources") or []:
            url = s.get("url")
            if url and not url.startswith("https://"):
                raise StateError(f"{where} source URLs must be https")


def build(state_path: Path, out_path: Path) -> None:
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state.setdefault("intro", "Edit any draft directly. Mark each item Accept, Edit, or Brainstorm with me, then send it back to Claude.")
    state.setdefault("banner", "")
    state["status"] = "awaiting_review"
    state["submitted_at"] = None
    for item in state["items"]:
        item.setdefault("decision", None)
        item.setdefault("comment", "")
        item.setdefault("brainstorm", [])
        if not item.get("tone"):
            if item.get("kind") == "choice":
                item["tone"] = "choice"
            else:
                m = re.match(r"Section (\d)", item.get("step") or "")
                item["tone"] = SECTION_TONES.get(m.group(1), "setup") if m else "setup"
        bullets = []
        for j, b in enumerate(item.get("bullets") or []):
            b = {"text": b} if isinstance(b, str) else dict(b)
            b.setdefault("id", f"b{j + 1}")
            b.setdefault("keep", True)
            b.setdefault("edited", None)
            b.setdefault("added", False)
            b.setdefault("sources", [])
            bullets.append(b)
        if bullets:
            item["bullets"] = bullets
    validate(state)
    payload = json.dumps(state, ensure_ascii=False).replace("<", "\\u003c")
    html = TEMPLATE.read_text(encoding="utf-8")
    title = f"{state['study']} Review".replace("<", "").replace(">", "")[:80]
    html = html.replace("<title>Research Review</title>", f"<title>{title}</title>", 1)
    html, count = STATE_RE.subn(lambda m: m.group(1) + payload + m.group(3), html, count=1)
    if count != 1:
        raise StateError("template.html is missing the review-state block")
    out_path.write_text(html, encoding="utf-8")
    print(f"PASS: wrote {out_path} with {len(state['items'])} items")


def bullet_state(b: dict) -> str:
    if not b.get("keep"):
        return "removed"
    if b.get("added"):
        return "added"
    return "edited" if b.get("edited") is not None else "kept"


def read(page_path: Path) -> None:
    match = STATE_RE.search(page_path.read_text(encoding="utf-8"))
    if not match:
        raise StateError("no review-state block found in the page")
    state = json.loads(match.group(2))
    print(json.dumps(state, ensure_ascii=False, indent=2))
    lines = [f"STATUS: {state.get('status')} · submitted_at: {state.get('submitted_at')}"]
    pending = []
    for item in state["items"]:
        decision = item.get("decision")
        if not decision:
            pending.append(item["id"])
        label = "brainstorm in chat" if decision == BRAINSTORM else decision or "NOT REVIEWED"
        lines.append(f"\n{item.get('step', '')} {item['title']} -> {label}")
        for b in item.get("bullets") or []:
            text = b["edited"] if b.get("edited") is not None else b["text"]
            lines.append(f"  [{bullet_state(b)}] {text}")
        turns = [t for t in item.get("brainstorm") or [] if t.get("role") == "assistant"]
        if turns:
            lines.append(f"  brainstorm: {len(turns)} senior-researcher replies on the page")
        if item.get("comment"):
            lines.append(f"  note: {item['comment']}")
    if pending:
        lines.append(f"\nPENDING (not approval): {', '.join(pending)}")
    print("\n".join(lines), file=sys.stderr)


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 4 and argv[1] == "build":
            build(Path(argv[2]), Path(argv[3]))
        elif len(argv) == 3 and argv[1] == "read":
            read(Path(argv[2]))
        else:
            print(__doc__, file=sys.stderr)
            return 2
    except (StateError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
