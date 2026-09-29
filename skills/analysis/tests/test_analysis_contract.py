#!/usr/bin/env python3
"""Offline regression tests for the analysis content and style helpers."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


TEST_DIR = Path(__file__).resolve().parent
SCRIPT_DIR = TEST_DIR.parent / "scripts"
FIXTURE = TEST_DIR / "fixtures" / "single_session_mock.json"
sys.path.insert(0, str(SCRIPT_DIR))

import analysis_contract  # noqa: E402
import style_instacart_green as style  # noqa: E402


class SingleSessionRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.packet = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_mock_fixture_has_one_context_item_and_one_finding(self) -> None:
        result = analysis_contract.validate_packet(self.packet)
        self.assertEqual([], result.errors)
        self.assertEqual(1, len(self.packet["context_items"]))
        self.assertEqual(1, len(self.packet["findings"]))

    def test_mock_fixture_avoids_cross_session_and_action_claims(self) -> None:
        analysis_body = {
            key: value
            for key, value in self.packet.items()
            if key != "excluded_annotations"
        }
        serialized = json.dumps(analysis_body, ensure_ascii=False)
        forbidden = (
            r"\bthemes?\b",
            r"\bclusters?\b",
            r"\bpatterns?\b",
            r"\b\d+(?:\.\d+)?\s*%",
            r"\b1\s*(?:of|/)\s*1\b",
            r"\bP[0-2]\b",
            r"\b(?:build|ship|launch|implement)\b",
            r"\brecommendations?\b",
        )
        for expression in forbidden:
            with self.subTest(expression=expression):
                self.assertIsNone(re.search(expression, serialized, re.IGNORECASE))

    def test_mock_finding_preserves_evidence_boundaries(self) -> None:
        finding = self.packet["findings"][0]
        self.assertTrue(finding["label"].startswith("Finding —"))
        self.assertTrue(
            any(
                item["task"] == "Task 4"
                and item["evidence_origin"] == "prompted"
                and item["evidence_kind"] == "self_report"
                for item in finding["evidence"]
            )
        )
        next_step = finding["next_research_step"]
        self.assertEqual("validation_hypothesis", next_step["kind"])
        self.assertEqual("High", next_step["validation_priority"]["level"])
        self.assertTrue(next_step["validation_priority"]["rationale"])
        self.assertEqual(
            {"analyst_generated"},
            {cue["label"] for cue in next_step["analyst_generated_cues"]},
        )

    def test_mock_context_uses_correct_task_provenance(self) -> None:
        evidence = self.packet["context_items"][0]["evidence"]
        self.assertEqual(
            ["Task 1", "Task 2", "Task 3", "Task 3", "Task 3"],
            [item["task"] for item in evidence],
        )
        self.assertIn("Walmart plus Instacart", evidence[0]["evidence_text"])
        self.assertIn("spouse and three children", evidence[1]["evidence_text"])
        self.assertIn("buy frozen pizza", evidence[2]["evidence_text"])
        self.assertIn("frozen foods", evidence[3]["evidence_text"])
        self.assertIn("don't buy meal kit", evidence[4]["evidence_text"])

    def test_mock_finding_cites_all_three_portion_cues(self) -> None:
        evidence_text = " ".join(
            item["evidence_text"] for item in self.packet["findings"][0]["evidence"]
        )
        self.assertIn("pounds", evidence_text)
        self.assertIn("whole sandwich or half a sandwich", evidence_text)
        self.assertIn("boughten in the past", evidence_text)
        self.assertNotIn("…", evidence_text)
        self.assertEqual(
            {"verbatim"},
            {
                item["text_representation"]
                for item in self.packet["findings"][0]["evidence"]
            },
        )

    def test_mock_has_no_fake_external_links(self) -> None:
        self.assertEqual([], self.packet["links"])
        self.assertIn("no external links or artifacts", self.packet["links_note"])

    def test_mock_excludes_platform_annotations_from_evidence(self) -> None:
        excluded = self.packet["excluded_annotations"]
        self.assertEqual(
            [
                {"value": "Dislike", "reason": "platform_annotation"},
                {"value": "Pain point", "reason": "platform_annotation"},
            ],
            excluded,
        )
        analysis_text = json.dumps(
            {
                "context_items": self.packet["context_items"],
                "findings": self.packet["findings"],
            },
            ensure_ascii=False,
        )
        self.assertNotIn("Dislike", analysis_text)
        self.assertNotIn("Pain point", analysis_text)

    def test_mock_discloses_source_limitations_and_confidence_dimensions(self) -> None:
        limitation_types = {item["type"] for item in self.packet["limitations"]}
        self.assertTrue({"consent_provenance", "speaker_separation"} <= limitation_types)
        expected_dimensions = {
            "source_integrity",
            "attribution_certainty",
            "evidence_directness",
            "within_case_coherence",
            "cross_case_support",
            "transferability",
        }
        for item in self.packet["context_items"] + self.packet["findings"]:
            with self.subTest(item=item["id"]):
                self.assertEqual(expected_dimensions, set(item["confidence"]))


class ContractValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.packet = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_single_session_rejects_product_action_and_priority_codes(self) -> None:
        self.packet["findings"][0]["next_research_step"] = {
            "label": "Recommendation",
            "kind": "product_action",
            "text": "Build the new view as P0.",
            "analyst_generated_cues": [],
        }
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "single_session findings must use a validation_hypothesis next_research_step, not a product action",
            result.errors,
        )
        self.assertTrue(any("priority code" in error for error in result.errors))
        self.assertTrue(any("build/ship recommendation" in error for error in result.errors))

    def test_test_artifact_requires_test_run_label_and_canonical_warning(self) -> None:
        self.packet["status_labels"] = []
        self.packet.pop("test_artifact_warning")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn("test artifacts must include the TEST RUN status label", result.errors)
        self.assertIn("test artifact warning is missing or non-canonical", result.errors)

    def test_test_artifact_requires_input_provenance(self) -> None:
        self.packet["method"].pop("input_provenance")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "test artifact method.input_provenance must identify real, simulated, or mixed input",
            result.errors,
        )

    def test_simulated_test_input_requires_simulated_data_label(self) -> None:
        self.packet["method"]["input_provenance"] = "simulated_data"
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "simulated or mixed test input must include the SIMULATED DATA status label",
            result.errors,
        )

    def test_real_test_input_rejects_simulated_data_label(self) -> None:
        self.packet["status_labels"].append("SIMULATED DATA")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "authorized real test input must not be labelled SIMULATED DATA",
            result.errors,
        )

    def test_test_run_rejects_draft_real_study_label(self) -> None:
        self.packet["status_labels"].append("DRAFT REAL STUDY")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "TEST RUN and DRAFT REAL STUDY must not be combined",
            result.errors,
        )

    def test_links_require_label_and_http_url(self) -> None:
        for malformed_url in ("https://@", "https://[bad"):
            with self.subTest(url=malformed_url):
                self.packet["links"] = [
                    {"label": "Transcript", "url": malformed_url}
                ]
                result = analysis_contract.validate_packet(self.packet)
                self.assertIn("links[0].url must be an http(s) URL", result.errors)

    def test_local_test_run_requires_a_note_when_links_are_empty(self) -> None:
        self.packet.pop("links_note")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "local test runs with no links require a non-empty links_note",
            result.errors,
        )

    def test_single_session_rejects_multiple_participants(self) -> None:
        self.packet["findings"][0]["evidence"][0]["participant_id"] = "P02"
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "single_session evidence must reference exactly one participant",
            result.errors,
        )

    def test_single_session_declared_participant_must_match_evidence(self) -> None:
        self.packet["method"]["participant_ids"] = ["P02"]
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "single_session method.participant_ids must exactly match the evidence participant",
            result.errors,
        )

    def test_declared_participants_and_status_labels_require_text_items(self) -> None:
        self.packet["method"]["participant_ids"] = [["P01"]]
        self.packet["status_labels"] = [{"label": "TEST RUN"}]
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn("method.participant_ids must contain only participant ID text", result.errors)
        self.assertIn(
            "status_labels may contain only TEST RUN, SIMULATED DATA, or DRAFT REAL STUDY",
            result.errors,
        )

    def test_single_session_rejects_spelled_percentage(self) -> None:
        self.packet["findings"][0]["analysis"] = "This occurred for 50 percent of people."
        result = analysis_contract.validate_packet(self.packet)
        self.assertTrue(any("percentage" in error for error in result.errors))

    def test_excluded_annotation_is_rejected_anywhere_in_analysis_content(self) -> None:
        self.packet["findings"][0]["analysis"] += " Pain point"
        result = analysis_contract.validate_packet(self.packet)
        self.assertTrue(any("appears in analysis content" in error for error in result.errors))

    def test_excluded_annotations_must_be_a_list(self) -> None:
        self.packet["excluded_annotations"] = {
            "value": "Pain point",
            "reason": "platform_annotation",
        }
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn("excluded_annotations must be a list", result.errors)

    def test_analyst_generated_cues_must_be_a_list(self) -> None:
        self.packet["findings"][0]["next_research_step"]["analyst_generated_cues"] = {
            "cue": "serving count",
            "label": "analyst_generated",
        }
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "findings[0].next_research_step.analyst_generated_cues must be a list",
            result.errors,
        )

    def test_evidence_requires_full_provenance(self) -> None:
        self.packet["findings"][0]["evidence"][0].pop("source_locator")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "findings[0].evidence[0].source_locator must be non-empty text",
            result.errors,
        )

    def test_evidence_requires_text_representation_and_normalization_note(self) -> None:
        evidence = self.packet["findings"][0]["evidence"][0]
        evidence.pop("text_representation")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "findings[0].evidence[0].text_representation must be non-empty text",
            result.errors,
        )
        evidence["text_representation"] = "normalized_verbatim"
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "findings[0].evidence[0].normalization_note must be non-empty text",
            result.errors,
        )

    def test_single_session_requires_validation_priority_with_rationale(self) -> None:
        self.packet["findings"][0]["next_research_step"].pop("validation_priority")
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "findings[0].next_research_step.validation_priority must be an object",
            result.errors,
        )

    def test_single_session_allows_research_implementation_language(self) -> None:
        self.packet["findings"][0]["next_research_step"]["text"] = (
            "Implement a follow-up interview probe about serving cues."
        )
        result = analysis_contract.validate_packet(self.packet)
        self.assertEqual([], result.errors)

    def test_single_session_allows_a_limitation_to_disclaim_recommendations(self) -> None:
        self.packet["limitations"].append(
            {
                "type": "claim_boundary",
                "text": "This n=1 memo is not a product recommendation.",
            }
        )
        result = analysis_contract.validate_packet(self.packet)
        self.assertEqual([], result.errors)

    def test_single_session_allows_limitations_to_name_forbidden_claim_types(self) -> None:
        self.packet["limitations"].append(
            {
                "type": "claim_boundary",
                "text": "This memo cannot establish themes or broader user patterns.",
            }
        )
        result = analysis_contract.validate_packet(self.packet)
        self.assertEqual([], result.errors)

    def test_single_session_allows_verbatim_evidence_to_use_pattern_language(self) -> None:
        self.packet["findings"][0]["evidence"][0]["evidence_text"] = (
            "I look for the pattern on the package."
        )
        result = analysis_contract.validate_packet(self.packet)
        self.assertEqual([], result.errors)

    def test_single_session_rejects_pattern_claim_language_in_analysis(self) -> None:
        self.packet["findings"][0]["analysis"] = "A pattern emerged across users."
        result = analysis_contract.validate_packet(self.packet)
        self.assertTrue(any("pattern language" in error for error in result.errors))

    def test_validation_priority_level_requires_text(self) -> None:
        priority = self.packet["findings"][0]["next_research_step"]["validation_priority"]
        priority["level"] = {"name": "High"}
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn(
            "findings[0].next_research_step.validation_priority.level must be High, Medium, or Low",
            result.errors,
        )

    def test_evidence_ids_must_be_unique(self) -> None:
        self.packet["findings"][0]["evidence"][0]["id"] = "E1"
        result = analysis_contract.validate_packet(self.packet)
        self.assertIn("evidence IDs must be unique", result.errors)

    def test_single_session_confidence_requires_n1_boundary_ratings(self) -> None:
        confidence = self.packet["findings"][0]["confidence"]
        confidence["cross_case_support"]["rating"] = "low"
        confidence["transferability"]["rating"] = "medium"
        result = analysis_contract.validate_packet(self.packet)
        self.assertTrue(any("cross_case_support rating must be N/A" in error for error in result.errors))
        self.assertTrue(
            any("transferability rating must be not_assessable" in error for error in result.errors)
        )

    def test_multi_session_shape_validates_without_single_session_context(self) -> None:
        packet = {
            "schema_version": 1,
            "mode": "multi_session",
            "title": "Cross-session synthesis",
            "test_artifact": False,
            "status_labels": [],
            "research_question": "How do shoppers assess portion fit?",
            "audience": ["Research"],
            "method": {"name": "General Affinity Synthesis", "scope": "Five sessions"},
            "links": [{"label": "Project", "url": "https://example.com/project"}],
            "findings": [
                {
                    "id": "F1",
                    "label": "Finding — corroborated across sessions",
                    "title": "Shoppers use category-specific cues.",
                    "analysis": "Two participants described different cues.",
                    "evidence": [
                        {
                            "id": "E1",
                            "task": "Task 4",
                            "participant_id": "P01",
                            "source": "transcript 1",
                            "source_locator": "Task 4",
                            "evidence_origin": "prompted",
                            "evidence_kind": "self_report",
                            "attribution_certainty": "certain",
                            "claim_status": "stated",
                            "scope_status": "included",
                            "text_representation": "verbatim",
                            "evidence_text": "I look at weight."
                        },
                        {
                            "id": "E2",
                            "task": "Task 4",
                            "participant_id": "P02",
                            "source": "transcript 2",
                            "source_locator": "Task 4",
                            "evidence_origin": "prompted",
                            "evidence_kind": "self_report",
                            "attribution_certainty": "certain",
                            "claim_status": "stated",
                            "scope_status": "included",
                            "text_representation": "verbatim",
                            "evidence_text": "I check the item count."
                        }
                    ],
                    "confidence": {
                        "source_integrity": {"rating": "high", "basis": "Clear transcripts."},
                        "attribution_certainty": {"rating": "high", "basis": "Speaker labels present."},
                        "evidence_directness": {"rating": "medium", "basis": "Self-report."},
                        "within_case_coherence": {"rating": "medium", "basis": "No contradictions found."},
                        "cross_case_support": {"rating": "medium", "basis": "Two participants."},
                        "transferability": {"rating": "low", "basis": "Small corpus."}
                    }
                }
            ],
            "priority_actions": [
                {"code": "P1", "action": "Test cue comprehension.", "confidence": "medium"}
            ],
            "limitations": [{"type": "scope", "text": "Small corpus."}]
        }
        result = analysis_contract.validate_packet(packet)
        self.assertEqual([], result.errors)


class ManifestAndStyleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.packet = json.loads(FIXTURE.read_text(encoding="utf-8"))
        style.OPS.clear()

    def tearDown(self) -> None:
        style.OPS.clear()

    def test_priority_colors_match_house_style(self) -> None:
        expected = {
            "P0": "#BA0239",
            "P1": "#FF7009",
            "P2": "#666666",
            "GUARDRAIL": "#003D29",
        }
        self.assertEqual(expected, {key: style.priority_color(key) for key in expected})

    def test_op_builders_accept_a_nondefault_tab_id(self) -> None:
        style.band(1, 4, tab_id="custom-tab")
        style.priority(5, 7, "P2", tab_id="custom-tab")
        self.assertTrue(style.OPS)
        self.assertEqual({"custom-tab"}, {operation["tab_id"] for operation in style.OPS})

    def test_manifest_uses_backend_specific_single_spacing(self) -> None:
        custom = analysis_contract.build_manifest(
            self.packet, backend="custom_mcp", tab_id="custom-tab"
        )
        raw = analysis_contract.build_manifest(
            self.packet, backend="docs_api", tab_id="raw-tab"
        )
        self.assertEqual(1, custom["style"]["normal_line_spacing"])
        self.assertEqual(100, raw["style"]["normal_line_spacing"])
        self.assertEqual("custom-tab", custom["style"]["tab_id"])
        self.assertEqual("raw-tab", raw["style"]["tab_id"])
        self.assertEqual(["context", "finding"], [b["type"] for b in custom["content_blocks"]])
        self.assertEqual(["TEST RUN"], custom["document"]["status_labels"])
        self.assertIn("analysis skill and workflow", custom["document"]["test_artifact_warning"])
        self.assertEqual(self.packet["links_note"], custom["document"]["links_note"])

    def test_single_session_manifest_does_not_emit_product_priority_colors(self) -> None:
        manifest = analysis_contract.build_manifest(self.packet)
        self.assertNotIn("priority_colors", manifest["style"])

    def test_multi_session_manifest_emits_product_priority_colors(self) -> None:
        self.packet["mode"] = "multi_session"
        self.packet["title"] = "Cross-session synthesis"
        self.packet["test_artifact"] = False
        self.packet["status_labels"] = []
        self.packet.pop("test_artifact_warning")
        self.packet["links"] = [
            {"label": "Project", "url": "https://example.com/project"}
        ]
        manifest = analysis_contract.build_manifest(self.packet)
        self.assertEqual(
            {"P0", "P1", "P2", "Guardrail"},
            set(manifest["style"]["priority_colors"]),
        )

    def test_cli_validates_and_emits_manifest_without_network(self) -> None:
        command = [
            sys.executable,
            str(SCRIPT_DIR / "analysis_contract.py"),
            "manifest",
            str(FIXTURE),
            "--backend",
            "docs_api",
            "--tab-id",
            "fixture-tab",
        ]
        completed = subprocess.run(command, check=False, capture_output=True, text=True)
        self.assertEqual(0, completed.returncode, completed.stderr)
        manifest = json.loads(completed.stdout)
        self.assertEqual("fixture-tab", manifest["style"]["tab_id"])
        self.assertEqual(100, manifest["style"]["normal_line_spacing"])

    def test_cli_returns_nonzero_and_json_errors_for_invalid_packet(self) -> None:
        self.packet["findings"] = []
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "invalid.json"
            path.write_text(json.dumps(self.packet), encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_DIR / "analysis_contract.py"),
                    "validate",
                    str(path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(1, completed.returncode)
        payload = json.loads(completed.stdout)
        self.assertFalse(payload["ok"])
        self.assertIn("findings must contain at least one item", payload["errors"])

    def test_cli_reports_nested_participant_id_as_json_without_traceback(self) -> None:
        self.packet["method"]["participant_ids"] = [["P01"]]
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "invalid-nested.json"
            path.write_text(json.dumps(self.packet), encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_DIR / "analysis_contract.py"),
                    "validate",
                    str(path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(1, completed.returncode)
        self.assertNotIn("Traceback", completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertIn(
            "method.participant_ids must contain only participant ID text",
            payload["errors"],
        )

    def test_cli_reports_structured_priority_level_without_traceback(self) -> None:
        priority = self.packet["findings"][0]["next_research_step"]["validation_priority"]
        priority["level"] = ["High"]
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "invalid-priority.json"
            path.write_text(json.dumps(self.packet), encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_DIR / "analysis_contract.py"),
                    "validate",
                    str(path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(1, completed.returncode)
        self.assertNotIn("Traceback", completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertIn(
            "findings[0].next_research_step.validation_priority.level must be High, Medium, or Low",
            payload["errors"],
        )


if __name__ == "__main__":
    unittest.main()
