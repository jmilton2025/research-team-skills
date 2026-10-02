#!/usr/bin/env python3
"""Validate the content and exact Option 4 — Leadership research-plan contract.

Run from any directory:
    python3 skills/research-plan/tests/validate_contract.py
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

TEST_DIR = Path(__file__).resolve().parent
SKILL_DIR = TEST_DIR.parent
REPO_ROOT = SKILL_DIR.parents[1]

FILES = {
    "skill": SKILL_DIR / "SKILL.md",
    "rules": SKILL_DIR / "references" / "content-rules.md",
    "methodology": SKILL_DIR / "references" / "research-plan-methodology.md",
    "safety": SKILL_DIR / "references" / "source-and-delivery-safety.md",
    "style": SKILL_DIR / "references" / "option4-leadership-style.md",
    "style_json": SKILL_DIR / "references" / "option4-style-contract.json",
    "script": SKILL_DIR / "scripts" / "option4_layout.py",
    "readme": REPO_ROOT / "README.md",
    "test_readme": TEST_DIR / "README.md",
    "behavior_gate": TEST_DIR / "behavioral-release-gate.md",
    "example": SKILL_DIR / "examples" / "multi-agent-review-example.md",
    "fixture": TEST_DIR / "fixtures" / "leadership-plan.md",
}

texts = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}
failures: list[str] = []


def require(name: str, needle: str) -> None:
    if needle not in texts[name]:
        failures.append(f"{name}: missing required text: {needle!r}")


def forbid(name: str, needle: str) -> None:
    if needle in texts[name]:
        failures.append(f"{name}: contains retired contract text: {needle!r}")


def require_regex(name: str, pattern: str, label: str) -> None:
    if not re.search(pattern, texts[name], flags=re.IGNORECASE | re.DOTALL):
        failures.append(f"{name}: missing {label}")


def require_order(name: str, needles: tuple[str, ...], label: str) -> None:
    positions = [texts[name].find(needle) for needle in needles]
    if any(position < 0 for position in positions):
        failures.append(f"{name}: cannot check {label}; one or more items are missing")
    elif positions != sorted(positions):
        failures.append(f"{name}: {label} is out of order")


# Maintained contract files name the same structure and visual target.
required_sections = (
    "Key Information",
    "Project Details",
    "Deliverables & Next Steps",
    "Appendix",
)
for name in ("skill", "rules", "readme"):
    for heading in required_sections:
        require_regex(name, re.escape(heading), f"{heading} section")
    if name != "skill":
        require_order(name, required_sections, "four-part overview structure")
    require(name, "Option 4 — Leadership")

for name in ("skill", "rules"):
    for label in (
        "Method & approach",
        "What does success look like?",
        "Dependencies & guardrails",
        "Deliverables",
        "Next steps",
        "Additional UXR documents",
        "Resources from XFN",
    ):
        require(name, label)
    require_regex(
        name,
        r"Sample & evaluators.{0,500}(only|when|if).{0,500}(relevant|needed|appl)",
        "conditional Sample & evaluators guidance",
    )
    require_regex(
        name,
        r"Measures & analysis.{0,500}(only|when|if).{0,500}(relevant|needed|appl)",
        "conditional Measures & analysis guidance",
    )
    require_regex(name, r"(true|actual|native) Google Docs bullet", "native bullet requirement")
    require_regex(
        name,
        r"Topic.{0,160}first visible.{0,160}(no generic|remove.*generic)",
        "headerless final overview requirement",
    )
    require_regex(
        name,
        r"((duplicate|duplication).{0,300}conditional[- ]row|conditional[- ]row.{0,300}(duplicate|duplication))",
        "conditional-row de-duplication rule",
    )
    require_regex(
        name,
        r"(test|pressure scenario).{0,250}(simulated|mock warning|TEST ARTIFACT)",
        "test-scenario warning rule",
    )
    require(name, "No hypotheses confirmed at planning time.")
    require_regex(name, r"(fewer|up to five).{0,180}(fewer|relevant findings)", "thin-evidence rule")
    for term in ("descope", "extend the timeline", "pause/escalate"):
        require(name, term)
require("skill", "authorization basis")

# Exact Option 4 visual contract and no downgrade path.
for name in ("skill", "rules", "style"):
    for term in (
        "DM Serif Display",
        "DM Sans",
        "Research Timeline",
        "Project Plan Overview",
        "block completion",
    ):
        require_regex(name, re.escape(term), term)
for term in (
    "#003D29",
    "#FFF2CC",
    "144pt / 554.4pt",
    "two physical cells",
    "full-paragraph",
):
    require("style", term)
require_regex("skill", r"five-row leadership timeline", "five-row leadership timeline")
require_regex("skill", r"raw.{0,120}verif.{0,120}render|verif.{0,120}render", "machine plus visual verification gate")
require_regex("skill", r"not researcher-.{0,80}leadership-waivable", "non-waivable visual gate")
for name in ("skill", "rules"):
    forbid(name, "portable Leadership layout")
    forbid(name, "portable leadership layout")

# Workflow must confirm destination before creating and run the exact pipeline.
for term in (
    "Confirm the Google Drive Destination",
    "Read the document back as text",
    "structure-inspection tool",
    "Open the verified Google Doc in the browser",
    "scripts/option4_layout.py",
):
    require("skill", term)
# Read-back and inspection stay tool-agnostic so any connected Docs integration works.
for retired in ("get_doc_as_markdown", "inspect_doc_structure"):
    forbid("skill", retired)
require_regex("skill", r"private, non-repository working directory.{0,120}not `/tmp`", "private persistent working folder rule")
require_regex("skill", r"### Connection check.{0,900}multi-agent-check", "connection check before discovery")
require_regex("skill", r"multi-agent review has run when it is installed.{0,120}critique-only", "critique-only fallback")
require_regex("skill", r"Check each fix's wording against the sources", "fix-wording check before applying review fixes")
require("skill", "examples/multi-agent-review-example.md")
require("example", "fully synthetic demonstration")
require("example", "not a recorded study")
forbid("example", "one real run")
forbid("example", "prior internal studies")
require_regex("skill", r"auto-draft.{0,300}title.{0,300}date.{0,300}RACI", "auto-drafted opening")
require_order(
    "skill",
    (
        "## Step 3.5: Confirm the Google Drive Destination",
        "### 6.1 Final copyedit and manifest",
        "### 6.2 Create in the confirmed folder",
        "### 6.3 Normalize and apply the exact Option 4 layout",
        "### 6.4 Verify and visually inspect",
        "### 6.5 Return the verified document",
    ),
    "destination plus Option 4 delivery pipeline",
)

# Decision and safety contracts: audit the decision before reading authorized sources.
for term in (
    "Connector access is not requester authorization.",
    "approved AI processing",
    "intended audience",
    "source ACL",
    "quote/link disclosure",
    "minimum necessary",
):
    require("skill", term)
for name in ("rules", "safety"):
    for term in (
        "Connector access is not requester authorization.",
        "approved AI processing",
        "intended audience",
        "source ACL",
        "quote/link disclosure",
        "minimum necessary",
        "de-identify",
        "source revision",
        "retrieval timestamp",
        "content hash",
    ):
        require(name, term)
require_order(
    "skill",
    (
        "### Decision audit — before discovery",
        "### Source-use authorization gate",
        "### Connection check",
        "## Step 1.5: Discover existing context before logistics",
    ),
    "decision and source-use authorization before connector checks and discovery",
)
require_order(
    "skill",
    (
        "### Source-use authorization gate",
        "## Step 1.5: Discover existing context before logistics",
        "authorized design link",
    ),
    "design-content fallback after source authorization",
)
for term in ("Reopen or reframe", "Measure implementation risk", "Document the decision as closed", "refuse that framing"):
    require("skill", term)
for term in ("metadata and links only", "not to paste, upload, or expose non-public content"):
    require("skill", term)
require_regex(
    "skill",
    r"connection check.{0,240}(must not|does not).{0,120}(open|read|retrieve).{0,120}source content",
    "non-content-bearing connection check",
)
require_regex(
    "safety",
    r"processing.{0,120}reviewer access.{0,300}minimum necessary de-identified extracts",
    "authorized minimum reviewer handoff",
)
require_regex(
    "skill",
    r"self-critique.{0,200}critique agent.{0,300}(processing|reviewer access)",
    "authorized critique-agent handoff with self-critique fallback",
)
require_regex(
    "skill",
    r"otherwise.{0,120}critique-only.{0,120}without source (files|content)",
    "source-free critique fallback",
)

# Safety reference: validate destination, local handling, runtime capability, and write idempotency.
require("skill", "references/source-and-delivery-safety.md")
for term in (
    "destination ACL",
    "fresh permissions read",
    "effective Drive permissions",
    "inherited access",
    "link-sharing scope",
    "private, non-repository working directory",
    "owner-only permissions",
    "retention and cleanup plan",
    "sensitive content in command-line arguments",
    "Never blindly retry a create or update.",
    "exact folder, title, and attempt-time window",
    "required revision ID",
    "partial document",
    "quarantine",
):
    require("safety", term)
for term in ("Full capability preflight", "Never blindly retry a create or update.", "required revision ID", "partial document"):
    require("skill", term)
require_regex(
    "safety",
    r"destination ACL.{0,200}intended audience.{0,200}before (any )?(write|creation)",
    "destination audience and ACL gate before write",
)
require_regex(
    "safety",
    r"(broader|overbroad).{0,160}(stop|block).{0,240}(compliant|approved) (folder|destination)",
    "overbroad destination fails closed",
)
require_regex(
    "safety",
    r"Preflight.{0,1200}create.{0,1200}raw.{0,1200}revision.{0,1200}(export|render).{0,1200}(cleanup|quarantine)",
    "complete pre-creation capability preflight",
)
require_regex(
    "safety",
    r"ambiguous.{0,600}(known document ID|known Doc ID).{0,600}exact folder, title, and attempt-time window.{0,600}Never blindly retry",
    "ambiguous-result reconciliation before retry",
)
require_regex(
    "safety",
    r"horizontal rule.{0,500}(cleanup|quarantine).{0,300}(before|prior to).{0,200}(new|another) (import|attempt)",
    "structural-import cleanup before retry",
)
require_regex(
    "safety",
    r"required revision ID.{0,500}(re-fetch|refetch).{0,500}(regenerate|rebuild)",
    "revision-bound batch update recovery",
)
require(
    "safety",
    "If the expected post-state is verified, record success and do not resend.",
)
require_regex(
    "safety",
    r"material content change.{0,240}reapproval.{0,240}formatting-only",
    "concurrent-edit reapproval boundary",
)

# The behavioral-test guide must exercise every new safety decision under pressure.
for term in (
    "Closed decision",
    "Unauthorized source reuse",
    "Reviewer handoff",
    "Reviewer service failure",
    "Destination ACL mismatch",
    "Sensitive local workspace",
    "Missing write capability",
    "Ambiguous create/update result",
    "Revision conflict",
    "Malformed import",
    "Partial document",
):
    require("test_readme", term)

require("behavior_gate", "**Contract version:** 2026-10-02")
for term in (
    "Closed decision",
    "Unauthorized source reuse",
    "Reviewer handoff",
    "Reviewer service failure",
    "Destination ACL mismatch",
    "Sensitive local workspace",
    "Missing write capability",
    "Ambiguous create result",
    "Revision conflict",
    "Malformed import",
    "Partial document",
):
    require_regex("behavior_gate", rf"{re.escape(term)}.*?\*\*PASS\*\*", f"captured PASS for {term}")
require("behavior_gate", "PASS — 11 of 11 scenarios")

# Cross-file guidance must agree with the active contract.
require("readme", "three interactive sections")
require_order("readme", ("Context & Foundation", "Research Design", "Outputs"), "three interactive approval sections")
require("methodology", "broad, project-level question")
require("methodology", "do not belong in the research plan")
require("methodology", "researcher running the study as Responsible")
require("methodology", "decision owner as Accountable")
require("methodology", "Log analysis is usually **descriptive**")
require("methodology", "randomized A/B experiment")
require("methodology", "canonical **Dependencies & guardrails** row")
for retired in (
    "research question** is the interview-ready prompt",
    "Name the decision-maker (Responsible)",
    "Methods: usability test, concept test, A/B",
    "Methods: log analysis, mixed-method studies",
    "why a dedicated section",
):
    forbid("methodology", retired)
require("skill", "randomized experiments or defensible quasi-experiments")
require("skill", "Mixed methods may explain mechanisms but are not inherently causal")
forbid("skill", "experimental or mixed-method work when the decision requires causal inference")

obsolete_sample = SKILL_DIR / "SAMPLE-COMPARISON-resops-vs-richer.md"
if obsolete_sample.exists():
    failures.append("obsolete internal sample comparison must not ship in the public skill")

for term in (
    "AskUserQuestion",
    "multiSelect: true",
    "Other / comments",
    "Inline fallback — native checklist unavailable in this environment",
    "Accept",
    "Brainstorm with me",
):
    require("skill", term)
# Pop-up rules match AskUserQuestion: at most 4 options, multi-select only for combinable choices,
# and each row approved once (Section 2 no longer re-approves Section 1 rows or the opening).
require_regex("skill", r"At most 4 options per pop-up", "four-option pop-up cap")
require_regex("skill", r"multiSelect: true` only when the options can be combined", "conditional multi-select rule")
forbid("skill", "Always use `multiSelect: true`")
forbid("skill", "no fixed cap")
forbid("skill", "of 7:")
forbid("skill", "### Opening\n")

# Retired fixed-template concepts must not return.
for name in ("skill", "rules"):
    for retired in (
        "What Research Priorities is this relevant to (Themes)",
        "Hypotheses / Questions of Interest",
        "Sampling Plan / Participants",
        "Deliverable Format",
        "Additional → Documents",
        "Additional / Documents",
        "Proposed Research Timeline",
        "CANONICAL STRUCTURE: the ResOps Research Project Plan",
    ):
        forbid(name, retired)

# Machine-readable visual values are exact.
try:
    visual = json.loads(texts["style_json"])
    expected = {
        ("page", "document_mode"): "PAGELESS",
        ("page", "orientation"): "LANDSCAPE",
        ("colors", "dark_green"): "#003D29",
        ("colors", "warning_background"): "#FFF2CC",
    }
    for path, value in expected.items():
        actual = visual
        for key in path:
            actual = actual[key]
        if actual != value:
            failures.append(f"style_json: {'.'.join(path)} is {actual!r}, expected {value!r}")
    if visual["page"]["margins_pt"] != {"top": 72, "bottom": 72, "left": 72, "right": 72}:
        failures.append("style_json: margins must be 72pt on all sides")
    if visual["page"]["use_custom_header_footer_margins"] is not True:
        failures.append("style_json: custom header/footer margins must be enabled")
    if visual["structure"] != {"native_horizontal_rules": 1, "top_level_tables": 2}:
        failures.append("style_json: structure must require one native rule and two top-level tables")
    if visual["tables"]["column_widths_pt"] != [144, 554.4]:
        failures.append("style_json: table widths must be 144pt / 554.4pt")
    if visual["tables"]["total_width_pt"] != 698.4:
        failures.append("style_json: table total must remain 698.4pt")
    if visual["tables"]["intentional_text_area_overflow_pt"] != 50.4:
        failures.append("style_json: intentional table overflow must remain 50.4pt")
    if visual["tables"]["cell_padding_pt"] != 5:
        failures.append("style_json: table cell padding must be 5pt")
    if visual["tables"]["timeline_rows"] != 5:
        failures.append("style_json: timeline must have five rows")
    if visual["tables"]["timeline_left_cell_max_characters"] != 32:
        failures.append("style_json: leadership timeline labels must be capped at 32 characters")
    if visual["tables"]["timeline_right_cell_max_characters"] != 160:
        failures.append("style_json: leadership timeline summaries must be capped at 160 characters")
except (json.JSONDecodeError, KeyError, TypeError) as error:
    failures.append(f"style_json: invalid contract: {error}")

for function_name in (
    "def parse_markdown(",
    "def build_normalize_requests(",
    "def build_format_requests(",
    "def verify_document(",
):
    require("script", function_name)
for command in ("manifest", "normalize", "format", "verify"):
    require("script", f'"{command}"')

# Durable fixture carries the exact two-table hierarchy and canonical overview.
require_order(
    "fixture",
    (
        "TEST ARTIFACT",
        "# Research Timeline",
        "| Milestone | Leadership milestone |",
        "# Project Plan Overview",
        "| Section / element | Approved content |",
        "| **KEY INFORMATION** |",
        "| **PROJECT DETAILS** |",
        "| **DELIVERABLES & NEXT STEPS** |",
        "| **APPENDIX** |",
    ),
    "fixture hierarchy",
)

timeline_match = re.search(
    r"# Research Timeline\s+\| Milestone \| Leadership milestone \|\s+\|---\|---\|\s+(.*?)\n\s*\*",
    texts["fixture"],
    flags=re.DOTALL,
)
if not timeline_match:
    failures.append("fixture: cannot parse leadership timeline")
else:
    rows = [line for line in timeline_match.group(1).splitlines() if line.strip().startswith("|")]
    if len(rows) != 4:
        failures.append(f"fixture: leadership timeline has {len(rows)} body rows; expected four")

for label in (
    "Topic",
    "TL;DR summary of findings",
    "Background",
    "Existing insights",
    "Objectives",
    "Key research questions",
    "Hypotheses",
    "What decisions will be made with this research?",
    "Method & approach",
    "Sample & evaluators",
    "Measures & analysis",
    "What does success look like?",
    "Dependencies & guardrails",
    "Deliverables",
    "Timeline",
    "Next steps",
    "Additional UXR documents",
    "Resources from XFN",
):
    require("fixture", f"| **{label}** |")

require("fixture", "\n---\n")
require("fixture", "To be filled out at the end of the study.")
require("fixture", "The finished Google Doc uses native bullet paragraphs")
for retired in ("→", "Deliverable Format", "Research Priorities", "Additional → Documents"):
    forbid("fixture", retired)

appendix_position = texts["fixture"].find("| **APPENDIX** |")
appendix_text = texts["fixture"][appendix_position:] if appendix_position >= 0 else ""
appendix_labels = re.findall(r"^\| \*\*(.+?)\*\* \|", appendix_text, flags=re.MULTILINE)
if appendix_labels != ["APPENDIX", "Additional UXR documents", "Resources from XFN"]:
    failures.append("fixture: Appendix must contain exactly the two approved document rows")

for label in ("Method & approach", "Measures & analysis", "Deliverables", "Timeline", "Next steps"):
    require_regex(
        "fixture",
        rf"\| \*\*{re.escape(label)}\*\* \| .*?<br>- ",
        f"multiple fixture bullets for {label!r}",
    )

if failures:
    print(f"FAIL: {len(failures)} research-plan contract check(s) failed")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS: Option 4 — Leadership research-plan content and visual contracts are internally consistent")
