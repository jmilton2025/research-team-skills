#!/usr/bin/env python3
"""Deterministic cross-file release checks for the /mod-guide skill.

This gate complements the formatter unit tests. It verifies that the public skill,
templates, safety contract, and machine-readable visual contract describe the same
portable default and the same canonical output schema. It makes no network calls.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import unittest


TEST_DIR = Path(__file__).resolve().parent
SKILL_DIR = TEST_DIR.parent
SKILL_PATH = SKILL_DIR / "SKILL.md"
SCRIPT_PATH = SKILL_DIR / "scripts" / "option4_guide_layout.py"
STYLE_JSON = SKILL_DIR / "references" / "option4-guide-style.json"
STYLE_MD = SKILL_DIR / "references" / "option4-guide-style.md"
SAFETY_PATH = SKILL_DIR / "references" / "source-and-delivery-safety.md"
INTERVIEW_TEMPLATE = SKILL_DIR / "references" / "template-interview.md"
PROTOTYPE_TEMPLATE = SKILL_DIR / "references" / "template-prototype-usability.md"
METHODOLOGY_PATH = SKILL_DIR / "references" / "mod-guide-methodology.md"
TEST_README = SKILL_DIR / "tests" / "README.md"
REMOVED_PERSONAL_ASSETS = (
    SKILL_DIR / "references" / "canonical-template-spec.md",
    SKILL_DIR / "scripts" / "apply_canonical_template.py",
    SKILL_DIR / "scripts" / "apply_custom_template.py",
    SKILL_DIR / "scripts" / "apply_jedida_reporting.py",
    SKILL_DIR / "scripts" / "font_and_widths.py",
    SKILL_DIR / "scripts" / "rebold_col1.py",
)


def load_layout_module():
    spec = importlib.util.spec_from_file_location("option4_guide_layout_contract", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_output_template(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    marker = "## OUTPUT TEMPLATE"
    if marker not in source:
        raise AssertionError(f"Missing OUTPUT TEMPLATE heading: {path}")
    parts = source.split(marker, 1)[1].split("```", 2)
    if len(parts) != 3:
        raise AssertionError(f"OUTPUT TEMPLATE must contain a fenced document: {path}")
    return parts[1].strip() + "\n"


class ModGuideCrossFileContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.layout = load_layout_module()
        cls.skill = SKILL_PATH.read_text(encoding="utf-8")
        cls.style_md = STYLE_MD.read_text(encoding="utf-8")
        cls.safety = SAFETY_PATH.read_text(encoding="utf-8")
        cls.interview = INTERVIEW_TEMPLATE.read_text(encoding="utf-8")
        cls.prototype = PROTOTYPE_TEMPLATE.read_text(encoding="utf-8")
        cls.methodology = METHODOLOGY_PATH.read_text(encoding="utf-8")
        cls.test_readme = TEST_README.read_text(encoding="utf-8")
        cls.contract = json.loads(STYLE_JSON.read_text(encoding="utf-8"))
        cls.interview_output = extract_output_template(INTERVIEW_TEMPLATE)
        cls.prototype_output = extract_output_template(PROTOTYPE_TEMPLATE)

    def test_skill_metadata_and_release_assets_are_complete(self) -> None:
        frontmatter = self.skill.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s*mod-guide\s*$")
        description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
        self.assertIsNotNone(description)
        self.assertTrue(description.group(1).startswith("Use when"))
        self.assertIn("concept test", description.group(1).casefold())
        self.assertIn("focus group", description.group(1).casefold())
        for path in (
            SCRIPT_PATH,
            STYLE_JSON,
            STYLE_MD,
            SAFETY_PATH,
            INTERVIEW_TEMPLATE,
            PROTOTYPE_TEMPLATE,
        ):
            self.assertTrue(path.is_file(), path)

    def test_shared_review_distinguishes_instruments_from_evidence_quotations(self) -> None:
        shared_review = (
            SKILL_DIR.parent / "multi-agent-check" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Two other researchers", shared_review)
        self.assertIn("Classify quotation purpose", shared_review)
        self.assertIn("authored content, not evidence quotations", shared_review)
        self.assertIn("not a factual-check exemption", shared_review)
        self.assertIn("approved study plan and applicable consent/privacy protocol", shared_review)
        self.assertIn("Refute quote-mismatch findings", shared_review)
        self.assertNotIn("Every string in quotation marks appears word-for-word", shared_review)

    def test_option4_is_the_only_documented_default(self) -> None:
        self.assertIn("Option 4 — Leadership is the default deliverable look", self.skill)
        self.assertIn("This is the default deliverable look", self.style_md)
        self.assertNotRegex(
            self.style_md,
            r"optional\s+[\"\u201c]leadership design[\"\u201d]\s+path",
        )

    def test_formatter_is_package_relative_and_portable(self) -> None:
        script = SCRIPT_PATH.read_text(encoding="utf-8")
        self.assertEqual(self.layout.SKILL_DIR, SKILL_DIR)
        self.assertNotIn("/Users/", script)
        self.assertNotIn("~/.claude", script)
        for path in REMOVED_PERSONAL_ASSETS:
            self.assertFalse(path.exists(), path)

    def test_safety_reference_is_wired_and_has_every_delivery_gate(self) -> None:
        self.assertIn("references/source-and-delivery-safety.md", self.skill)
        headings = [
            "## 1. Authorize sources before access",
            "## 2. Minimize working and reviewer data",
            "## 3. Bound consent and privacy language",
            "## 4. Confirm destination and permissions before creation",
            "## 5. Preflight the delivery capabilities",
            "## 6. Create idempotently",
            "## 7. Bind and reconcile writes",
            "## 8. Handle partial documents",
        ]
        offsets = [self.safety.index(heading) for heading in headings]
        self.assertEqual(offsets, sorted(offsets))

    def test_safety_contract_keeps_authorization_acl_and_retry_invariants(self) -> None:
        for invariant in (
            "Connector access is not requester authorization",
            "Never silently change sharing",
            "Never blindly retry a create",
            "writeControl.requiredRevisionId",
            "never resend the stale batch",
            "A failed or incomplete Doc is not a deliverable",
        ):
            with self.subTest(invariant=invariant):
                self.assertIn(invariant, self.safety)

    def test_gws_write_route_is_protected_approved_in_section1_and_optional(self) -> None:
        for phrase in (
            "Apply each Google Docs request body through the first of these that the integration offers",
            "a connector tool's request-body parameter",
            "the CLI's own file or standard-input option",
            "the bundled `send` helper",
            "starts `gws` directly, without a shell",
            "other programs on the same computer may be able to read",
            "approved it in Section 1",
            "If none of these is available or approved, block the write.",
            "`gws drive files create --upload FILE`",
            "For capability 3, name the request-body route from §2",
            "using the first available route in §2's order",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.safety)

        section1 = self.skill.split("## Step 3", 1)[1].split("## Step 4", 1)[0]
        step6 = self.skill.split("## Step 6", 1)[1].split("## Tool Usage", 1)[0]
        lines = section1.splitlines()
        last_row = next(i for i, line in enumerate(lines) if line.startswith("| **LAST** |"))
        route_row = next(i for i, line in enumerate(lines) if line.startswith("| **ROUTE** |"))
        self.assertEqual(route_row, last_row + 1)
        self.assertIn("only when `gws` is the only way to write", lines[route_row])
        for phrase in (
            '"Section 1 > Step N of M: Google Docs write route"',
            'with no "Brainstorm with me" option',
            '"Use the helper (Recommended)"',
            "\"Don't create the Doc\"",
            "reads no content",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, section1)
        self.assertIn("The one exception is the yes/no **Google Docs write route** approval", self.skill)
        self.assertIn("route chosen in Section 1", step6)
        self.assertIn("`drive files create --upload`", step6)
        self.assertNotIn("Use the helper", step6)
        self.assertIn("it is never required", self.skill)

        self.assertIn("drive files create --upload guide.md", self.style_md)
        self.assertIn("with `gws`, use `send`", self.style_md)
        script = SCRIPT_PATH.read_text(encoding="utf-8")
        self.assertNotIn("shell=True", script)
        self.assertTrue(callable(getattr(self.layout, "send_batch", None)))

    def test_pasted_non_public_content_does_not_bypass_authorization(self) -> None:
        required = (
            "Pasting or attaching content does not establish the requester's authority "
            "or approved AI-processing status"
        )
        for source_name, source in (("skill", self.skill), ("safety", self.safety)):
            with self.subTest(source=source_name):
                self.assertIn(required, source)
        self.assertNotIn("deliberately pastes is authorized", self.skill.casefold())
        self.assertNotIn("as authorization to use that content", self.safety.casefold())

    def test_participant_artifact_collection_requires_an_approved_protocol(self) -> None:
        required = (
            "Diary/photo pre-work and participant artifact collection are off unless "
            "the approved plan and protocol explicitly define"
        )
        for source_name, source in (
            ("skill", self.skill),
            ("interview", self.interview),
            ("methodology", self.methodology),
        ):
            with self.subTest(source=source_name):
                self.assertIn(required, source)
                self.assertIn("retention/deletion", source)

    def test_partial_artifact_recovery_is_preauthorized_before_creation(self) -> None:
        for source_name, source in (("skill", self.skill), ("safety", self.safety)):
            lowered = source.casefold()
            with self.subTest(source=source_name):
                self.assertIn("preauthorize exactly one partial-artifact recovery path", lowered)
                self.assertIn("block before creation", lowered)
        self.assertIn("session-only", self.safety)

    def test_supported_moderated_subtypes_have_explicit_output_contracts(self) -> None:
        moderation_row = next(
            line for line in self.skill.splitlines() if "**Moderation style**" in line
        )
        self.assertNotIn("Unmoderated", moderation_row)
        self.assertIn("Moderated remote", moderation_row)
        self.assertIn("Moderated in-person", moderation_row)
        self.assertIn(
            "[Moderated 1:1 IDI / moderated diary-study check-in / moderated focus group]",
            self.interview_output,
        )
        self.assertIn("Diary check-in behavioral scenario", self.test_readme)
        self.assertIn("Focus group behavioral scenario", self.test_readme)

    def test_section1_choices_fit_ui_limits_and_are_source_grounded(self) -> None:
        lines = self.skill.splitlines()
        title_index = next(i for i, line in enumerate(lines) if "**Study title**" in line)
        phase_index = next(i for i, line in enumerate(lines) if "**Phase/scope**" in line)
        self.assertLess(title_index, phase_index)

        duration = next(line for line in lines if "**Duration**" in line and line.startswith("|"))
        self.assertIn("two method-appropriate alternatives", duration)
        self.assertNotIn("30 / 45 / 60 / 90", duration)

        for source_name, source, labels in (
            ("interview", self.interview, ("| I2 |",)),
            ("prototype", self.prototype, ("| P1 |", "| P3 |", "| P6 |", "| P7 |")),
        ):
            for label in labels:
                row = next(line for line in source.splitlines() if line.startswith(label))
                with self.subTest(source=source_name, row=label):
                    self.assertRegex(row.casefold(), r"source|extracted|approved|\[tbd")

    def test_raci_comes_from_the_researcher_not_a_directory_search(self) -> None:
        self.assertIn("Ask the researcher for the RACI instead of looking people up", self.skill)
        self.assertIn("Key people first", self.skill)
        self.assertIn('"Confirm as shown (Recommended)"', self.skill)
        self.assertRegex(self.skill, r"Add more people.{0,400}finishes the same Row 9 approval")
        self.assertIn("don't carry names over from memory or older project files", self.skill)
        for source in (self.skill, self.interview, self.prototype):
            self.assertNotIn("employee_search", source)
            self.assertNotIn("people/directory search", source)
            self.assertNotIn("Directory / people search", source)
            self.assertNotIn("without a live check", source)

    def test_connection_check_runs_first_and_flags_sign_in(self) -> None:
        connection = self.skill.index("### Connection check — first, before any questions")
        step1 = self.skill.index("## Step 1 — Gather Study Inputs & Orient the Researcher")
        inputs_request = self.skill.index("To build your moderation guide, share the de-identified")
        self.assertLess(step1, connection)
        self.assertLess(connection, inputs_request)
        self.assertIn("Flag every missing or signed-out connection in your first message", self.skill)
        self.assertRegex(self.skill, r"/mcp\n>\s*```\n>\s*\n> Pick \*\*glean\*\*")
        self.assertRegex(self.skill, r"`glean` and `glean_default`")
        self.assertIn("choose **Authenticate**", self.skill)
        self.assertIn("say **skip Glean**", self.skill)
        self.assertRegex(self.skill, r"only tools return content.{0,200}don't run a test query")
        self.assertIn("Connection checks run at the start of Step 1, before this gate", self.safety)
        section = self.skill[connection:self.skill.index("### Source authorization and inputs")]
        self.assertNotIn("gws", section)

    def test_tool_contract_names_only_connected_or_packaged_readers(self) -> None:
        self.assertNotIn("download-gdoc.py", self.skill)
        self.assertNotIn("read-gdoc.py", self.skill)
        self.assertIn("Connected Google Docs / Drive read tools", self.skill)

    def test_dates_and_normalization_language_remain_evidence_grounded(self) -> None:
        for source_name, source in (
            ("skill", self.skill),
            ("interview", self.interview),
            ("prototype", self.prototype),
        ):
            with self.subTest(source=source_name):
                self.assertIn(
                    "Never substitute the current date or month for an unknown study period",
                    source,
                )
        self.assertIn(
            "[Source-approved study period or TBD — fill in]",
            self.interview_output,
        )
        self.assertIn(
            "[Source-approved study period or TBD — fill in]",
            self.prototype_output,
        )
        self.assertNotIn(
            "Lots of people I talk to skip this step — does that happen for you?",
            self.methodology,
        )
        self.assertIn("Do not normalize with invented prevalence claims", self.methodology)
        self.assertIn("What is the most recent time, if any", self.methodology)

    def test_templates_share_the_canonical_header_and_safe_top_level_schema(self) -> None:
        expected_headers = {
            "interview": [["Parameter", "Detail"], ["Cue", "Read aloud"]],
            "prototype": [["Parameter", "Detail"], ["Phase", "Time"]],
        }
        required_objectives = {
            "interview": "Research Objectives",
            "prototype": "Objectives & Research Questions",
        }
        for name, source in (
            ("interview", self.interview_output),
            ("prototype", self.prototype_output),
        ):
            with self.subTest(template=name):
                manifest = self.layout.parse_markdown(source)
                self.assertEqual(manifest["top"]["title"]["text"], "Moderation Guide")
                self.assertEqual(manifest["top"]["pre_title"], [])
                self.assertEqual(manifest["top"]["items"][0]["role"], "phase_subtitle")
                self.assertEqual(
                    [table["header"] for table in self.layout.manifest_tables(manifest)],
                    expected_headers[name],
                )
                self.assertIn(
                    required_objectives[name],
                    [section["source_label"] for section in manifest["sections"]],
                )
                self.assertIn("[TBD — confirm ResOps standard language]", source)

        self.assertNotIn("## Participants Log", self.interview_output)
        self.assertNotIn("Participant Grid", self.prototype_output)

    def test_output_templates_reject_unsafe_default_phrases(self) -> None:
        forbidden = (
            "internal research only",
            "recording armed",
            "participant grid",
        )
        for name, source in (
            ("interview", self.interview_output),
            ("prototype", self.prototype_output),
        ):
            lowered = source.casefold()
            for phrase in forbidden:
                with self.subTest(template=name, phrase=phrase):
                    self.assertNotIn(phrase, lowered)

    def test_both_templates_gate_specific_incident_followups_neutrally(self) -> None:
        interview = self.interview_output.casefold()
        prototype = self.prototype_output.casefold()
        for name, source in (("interview", interview), ("prototype", prototype)):
            with self.subTest(template=name):
                self.assertIn("what is the most recent time, if any", source)

        self.assertIn("if they name an incident", interview)
        self.assertIn("if none", interview)
        self.assertIn("if they name one", prototype)
        self.assertIn("after an incident is confirmed", prototype)

    def test_interview_timing_contract_counts_consent(self) -> None:
        self.assertIn("excluding Consent", self.interview_output)
        self.assertIn("every timed heading, including consent", self.interview.casefold())
        self.assertIn("every timed heading, including consent", self.skill.casefold())
        for source in (self.interview, self.skill):
            with self.subTest(source="template" if source == self.interview else "skill"):
                self.assertIn("Consent 1 + Introduction 2", source)
                self.assertRegex(
                    source,
                    r"never\s+`?Consent 1 \+ Introduction 3`?",
                )

    def test_raci_unknowns_are_rendered_per_field(self) -> None:
        for source_name, source in (
            ("interview", self.interview_output),
            ("prototype", self.prototype_output),
            ("shared", self.skill),
        ):
            for role in ("Responsible", "Accountable"):
                with self.subTest(source=source_name, role=role):
                    line = next(
                        line
                        for line in source.splitlines()
                        if line.startswith(f"- **{role}:**")
                    )
                    self.assertEqual(line.count("[TBD — fill in]"), 2)
            for role in ("Consulted", "Informed"):
                with self.subTest(source=source_name, role=role):
                    line = next(
                        line
                        for line in source.splitlines()
                        if line.startswith(f"- **{role}:**")
                    )
                    self.assertIn("[TBD — fill in]", line)

    def test_closed_question_audit_requires_complete_inventory(self) -> None:
        for source_name, source in (
            ("interview", self.interview),
            ("skill", self.skill),
        ):
            with self.subTest(source=source_name):
                self.assertIn("audit-only inventory", source)
                self.assertRegex(source, r"closed yes/no.{0,40}compound")

    def test_closed_question_guidance_limits_allowed_clarifiers(self) -> None:
        self.assertNotIn("Every question open-ended", self.skill)
        self.assertNotIn("broad → specific → closed", self.skill)
        self.assertNotIn(
            "No leading, hypothetical-about-future-behavior, closed yes/no, or compound questions",
            self.interview,
        )
        self.assertIn("factual clarifier", self.skill)
        self.assertIn("factual clarifier", self.interview)

    def test_methodology_timing_ranges_match_advertised_bounds(self) -> None:
        def totals_for(
            source: str, section_heading: str, next_heading: str
        ) -> tuple[int, int]:
            section = source.split(section_heading, 1)[1].split(next_heading, 1)[0]
            ranges = re.findall(r"\|\s*(\d+)(?:-(\d+))? min\s*\|", section)
            minimum = sum(int(low) for low, _ in ranges)
            maximum = sum(int(high or low) for low, high in ranges)
            return minimum, maximum

        methodology = (SKILL_DIR / "references" / "mod-guide-methodology.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(
            totals_for(
                methodology, "### 3d. Diary Study Check-in", "### 3e. Focus Group"
            ),
            (30, 45),
        )
        self.assertEqual(
            totals_for(
                methodology,
                "### 3e. Focus Group",
                "## 4. Full Bias-Mitigation Checklist",
            ),
            (60, 90),
        )

    def test_completion_contract_branches_real_and_demo_runs(self) -> None:
        self.assertIn("For a real-study run", self.skill)
        self.assertIn("For a demo, mock, sample, fixture, or pressure test", self.skill)
        self.assertIn("gates 0–3", self.skill)
        self.assertIn("gates 4–6", self.skill)

    def test_vendor_back_matter_is_source_grounded_and_style_compatible(self) -> None:
        lowered = self.prototype.casefold()
        for forbidden in (
            "slack channel",
            "eod update",
            "table of contents",
            "horizontal rules",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, lowered)
        self.assertIn("approved communication", lowered)
        self.assertIn("[tbd — fill in]", lowered)

    def test_rating_policy_allows_sus_or_seq_only_when_explicitly_selected(self) -> None:
        self.assertNotIn("No SUS/SEQ", self.prototype)
        self.assertGreaterEqual(
            self.prototype.count("SUS/SEQ only when the researcher explicitly selected"),
            2,
        )

    def test_prototype_first_impression_follows_the_approved_p8_choice(self) -> None:
        p8 = next(line for line in self.prototype.splitlines() if "| P8 |" in line)
        self.assertIn("include on", p8.casefold())
        self.assertIn("task-only (skip unaided reaction)", p8.casefold())
        for source in (self.prototype, self.skill):
            self.assertIn("P8 = Task-only", source)
            self.assertRegex(source, r"P8 = Task-only.{0,80}omit")
        self.assertNotIn("Scenario → unaided first impression", self.skill)
        self.assertNotIn(
            "Each phase has the complete Scenario → First impression", self.prototype
        )
        self.assertNotIn(
            "every phase a bold-label list with Scenario → First impression", self.skill
        )
        self.assertLess(
            self.prototype_output.index("[P8 gate:"),
            self.prototype_output.index("## Phase 1"),
        )

    def test_concept_test_contract_preserves_reaction_constructs(self) -> None:
        p8 = next(line for line in self.prototype.splitlines() if "| P8 |" in line)
        self.assertIn("Concept —", p8)
        self.assertIn("Usability —", p8)
        predicate = "initial recall, comprehension, reaction, or desirability"
        self.assertIn(predicate, p8)
        self.assertIn(predicate, self.methodology)
        for source_name, source in (
            ("skill", self.skill),
            ("prototype", self.prototype),
        ):
            with self.subTest(source=source_name):
                self.assertIn("construct-matched evidence-collection element", source)
                self.assertIn(
                    "Never convert a reaction, recall, comprehension, or desirability "
                    "hypothesis into an invented behavioral task",
                    source,
                )
                self.assertIn(
                    "Concept P8 = Task-only is invalid when an approved objective or "
                    f"hypothesis measures {predicate}",
                    source,
                )
                self.assertIn(
                    "Usability P8 = Task-only is invalid only when an approved objective "
                    "or hypothesis measures unaided initial comprehension or reaction",
                    source,
                )
        self.assertIn("reaction-led concept phase", self.prototype)
        self.assertIn("Use the 5-second rule only when", self.methodology)
        self.assertIn("selected in P8", self.methodology)
        self.assertIn("omit the exercise and leave no placeholder", self.methodology)
        self.assertNotIn(
            "Every supplied hypothesis must map to an executable task",
            self.skill,
        )
        self.assertNotIn(
            "Every hypothesis in the source plan must have an executable task",
            self.prototype,
        )
        self.assertIn("Concept reaction behavioral scenario", self.test_readme)
        self.assertIn("Usability Task-only behavioral scenario", self.test_readme)
        self.assertIn(
            "reveal → [P8-approved first impression, when included] → required "
            "construct-matched neutral prompts",
            self.skill,
        )

    def test_methodology_uses_a_neutral_incident_gate_before_last_time(self) -> None:
        methodology = (SKILL_DIR / "references" / "mod-guide-methodology.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn(
            '"Tell me about the last time you cooked dinner. What about the time before that?"',
            methodology,
        )
        self.assertIn("What is the most recent time, if any", methodology)
        self.assertIn("If they confirm one", methodology)
        for source in (self.skill, methodology):
            for line in source.splitlines():
                if "Tell me about the last time" in line:
                    self.assertRegex(line.casefold(), r"after|confirm|only")

    def test_warning_copy_references_resolve_from_their_files(self) -> None:
        json_source = self.contract["warning"]["copy_source"]
        self.assertTrue((STYLE_JSON.parent / json_source).resolve().is_file())

        match = re.search(
            r"\[[^\]]*output-status-and-labeling-conventions\.md[^\]]*\]"
            r"\(([^)]*output-status-and-labeling-conventions\.md)\)",
            self.style_md,
        )
        self.assertIsNotNone(match)
        self.assertTrue((STYLE_MD.parent / match.group(1)).resolve().is_file())

    def test_shipped_examples_avoid_closed_compound_and_predicted_use_prompts(self) -> None:
        methodology = (SKILL_DIR / "references" / "mod-guide-methodology.md").read_text(
            encoding="utf-8"
        )
        combined = f"{self.prototype}\n{methodology}".casefold()
        forbidden = (
            "which feels more accurate / clearer",
            "which felt easier, and why",
            "which would you rather use",
            "when would you use",
            "anything still confusing",
            "what do you remember, what did it make you feel",
            "is there anyone it's clearly *not* for",
            "anything else you want to flag",
            "tell me what you notice, what you think",
            "how [construct] was that? what made",
            "what would you expect to happen? what would you try next?",
        )
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, combined)
        for required in (
            "approved construct",
            "what kinds of situations, if any",
            'ask one at a time: "what do you remember?"',
            "who, if anyone, does it seem less suited to?",
        ):
            with self.subTest(required=required):
                self.assertIn(required, combined)

    def test_demo_branch_skips_destination_consistently(self) -> None:
        section1 = self.skill.split("## Step 3", 1)[1].split("## Step 4", 1)[0]
        section2 = self.skill.split("## Step 4", 1)[1].split("## Step 4.5", 1)[0]
        self.assertIn(
            "For a real study, or a demo/test run whose tester explicitly requested a test Doc",
            section1,
        )
        self.assertIn("For a demo/test run on the default no-Drive path", section1)
        self.assertIn("No destination, recovery, or style approval is required", section1)
        self.assertIn("**Real study or explicitly requested test Doc:**", section2)
        self.assertIn("**No-Drive demo/test:**", section2)
        self.assertNotRegex(section1, r"(?m)^The final batch ends with")
        self.assertNotIn("all parameters set and the destination confirmed", section2)

    def test_option4_modes_distinguish_strict_and_fallback_enabled(self) -> None:
        gate = self.style_md.split("## Hard completion gate", 1)[1]
        self.assertIn("An approximate Option 4 is never a completed deliverable", gate)
        self.assertIn("**Strict Option 4 — Leadership:**", gate)
        self.assertIn("with pre-approved plain-native fallback (default)", gate)
        self.assertIn("Required on every delivery path", gate)
        self.assertIn("block delivery on every path", gate)
        self.assertIn("If render is unavailable, delivery blocks on every path", self.skill)
        self.assertNotIn("When Option 4 is selected (the default)", gate)

    def test_material_post_audit_changes_require_reapproval(self) -> None:
        audit = self.skill.split("## Step 4.5", 1)[1].split("## Step 5", 1)[0]
        step5 = self.skill.split("## Step 5", 1)[1].split("## Step 6", 1)[0]
        step6 = self.skill.split("## Step 6", 1)[1]
        for phrase in (
            "Post-audit change control",
            "**Non-material:**",
            "**Material:**",
            "concise before/after diff",
            "explicit researcher approval",
            "re-run every affected audit row",
        ):
            self.assertIn(phrase, audit)
        self.assertIn("never silently fold meaning-changing fixes", step5)
        self.assertIn(
            "must already have completed the planned Section 3 approval", step6
        )
        self.assertIn("Reapprove material content changes", self.safety)

    def test_public_skill_has_no_person_specific_exceptions(self) -> None:
        person_specific_token = "sa" + "sha"
        for path in SKILL_DIR.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".py", ".json"}:
                self.assertNotIn(
                    person_specific_token,
                    path.read_text(encoding="utf-8").casefold(),
                )

    def test_prototype_wrapup_covers_reflection_catchall_questions_and_thanks(self) -> None:
        wrap_up = self.prototype_output.split("## Wrap-Up", 1)[1].split("---", 1)[0]
        self.assertIn("most important or confusing", wrap_up.casefold())
        self.assertIn("didn't get a chance to share", wrap_up.casefold())
        self.assertIn("questions do you have for me", wrap_up.casefold())
        self.assertIn("thank you again", wrap_up.casefold())
        self.assertIn("standard three-question close plus a thank-you", self.skill)

    def test_interview_wrapup_plays_back_themes_before_the_catchall(self) -> None:
        wrap_up = self.interview_output.split("## Wrap-Up", 1)[1].split("---", 1)[0]
        self.assertIn("play back the themes", wrap_up.casefold())
        self.assertIn("didn't get a chance to share", wrap_up.casefold())
        self.assertIn("questions do you have for me", wrap_up.casefold())
        self.assertIn("thank you again", wrap_up.casefold())

    def test_machine_contract_describes_the_current_templates(self) -> None:
        self.assertEqual(self.contract["name"], "Option 4 — Leadership (Moderation Guide)")
        self.assertTrue(self.contract["structure_agnostic"])
        shapes = " ".join(self.contract["supported_guide_shapes"]).casefold()
        self.assertNotIn("two-tier header", shapes)
        self.assertNotIn("single breadcrumb", shapes)
        self.assertNotIn("#|ask", shapes)
        width_rule = self.contract["tables"]["column_width_rule"]
        self.assertRegex(width_rule, r"Phase\s*\|\s*Time")
        self.assertIn("wide", width_rule.casefold())
        self.assertIn("144", width_rule)


if __name__ == "__main__":
    unittest.main()
