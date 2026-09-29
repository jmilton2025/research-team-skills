#!/usr/bin/env python3
"""Validate analysis content and emit an offline rendering manifest.

This module performs no API calls. It gives the analysis skill a deterministic
gate between approved research content and either the custom Docs MCP adapter or
the raw Google Docs API adapter.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

import style_instacart_green as style


CANONICAL_TEST_WARNING = (
    "⚠️ TEST RUN — generated to test the analysis skill and workflow, not as an "
    "approved research deliverable. Input may be authorized real data or simulated "
    "data; see Method for provenance. Do not file or share as approved research."
)
MODES = {"single_session", "multi_session"}
BACKENDS = {"custom_mcp", "docs_api"}
STATUS_LABELS = {"TEST RUN", "SIMULATED DATA", "DRAFT REAL STUDY"}
INPUT_PROVENANCE = {"authorized_real_data", "simulated_data", "mixed"}
CONFIDENCE_DIMENSIONS = {
    "source_integrity",
    "attribution_certainty",
    "evidence_directness",
    "within_case_coherence",
    "cross_case_support",
    "transferability",
}
SINGLE_SESSION_FORBIDDEN = {
    "theme language": re.compile(r"\bthemes?\b", re.IGNORECASE),
    "cluster language": re.compile(r"\bclusters?\b", re.IGNORECASE),
    "pattern language": re.compile(r"\bpatterns?\b", re.IGNORECASE),
    "percentage": re.compile(r"\b\d+(?:\.\d+)?\s*(?:%|percent\b)", re.IGNORECASE),
    "1-of-1 framing": re.compile(r"\b1\s*(?:of|/)\s*1\b", re.IGNORECASE),
    "priority code": re.compile(r"\bP[0-2]\b", re.IGNORECASE),
    "build/ship recommendation": re.compile(
        r"\b(?:build|ship|launch|implement)\w*\b.{0,50}"
        r"\b(?:feature|view|screen|interface|ui|product|experience|roadmap)\b",
        re.IGNORECASE,
    ),
    "product/roadmap priority language": re.compile(
        r"\b(?:product|roadmap)\s+priorit(?:y|ies|ization|ise|ize|ized)\b",
        re.IGNORECASE,
    ),
}


@dataclass(frozen=True)
class ValidationResult:
    errors: list[str]
    mode: str | None
    context_count: int
    finding_count: int

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "mode": self.mode,
            "counts": {
                "context_items": self.context_count,
                "findings": self.finding_count,
            },
            "errors": self.errors,
        }


class ContractError(ValueError):
    """Raised when a render manifest is requested for invalid content."""


def _is_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _require_text(container: Mapping[str, Any], key: str, path: str, errors: list[str]) -> None:
    if not _is_nonempty_text(container.get(key)):
        errors.append(f"{path}.{key} must be non-empty text")


def _validate_confidence(
    value: Any, path: str, errors: list[str], *, mode: str | None
) -> None:
    if not isinstance(value, Mapping):
        errors.append(f"{path}.confidence must be an object")
        return
    if set(value) != CONFIDENCE_DIMENSIONS:
        expected = ", ".join(sorted(CONFIDENCE_DIMENSIONS))
        errors.append(f"{path}.confidence must contain exactly: {expected}")
        return
    for dimension in sorted(CONFIDENCE_DIMENSIONS):
        detail = value.get(dimension)
        if not isinstance(detail, Mapping):
            errors.append(f"{path}.confidence.{dimension} must be an object")
            continue
        _require_text(detail, "rating", f"{path}.confidence.{dimension}", errors)
        _require_text(detail, "basis", f"{path}.confidence.{dimension}", errors)
    if mode == "single_session":
        cross_case = value.get("cross_case_support", {})
        if isinstance(cross_case, Mapping) and cross_case.get("rating") != "N/A":
            errors.append(f"{path}.confidence.cross_case_support rating must be N/A")
        transferability = value.get("transferability", {})
        if (
            isinstance(transferability, Mapping)
            and transferability.get("rating") != "not_assessable"
        ):
            errors.append(
                f"{path}.confidence.transferability rating must be not_assessable"
            )


def _validate_evidence(value: Any, path: str, errors: list[str]) -> None:
    evidence = _list(value)
    if not evidence:
        errors.append(f"{path}.evidence must contain at least one item")
        return
    for index, item in enumerate(evidence):
        item_path = f"{path}.evidence[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{item_path} must be an object")
            continue
        for key in (
            "id",
            "task",
            "participant_id",
            "source",
            "source_locator",
            "evidence_origin",
            "evidence_kind",
            "attribution_certainty",
            "claim_status",
            "scope_status",
            "text_representation",
            "evidence_text",
        ):
            _require_text(item, key, item_path, errors)
        evidence_origin = item.get("evidence_origin")
        if not _is_nonempty_text(evidence_origin) or evidence_origin not in {
            "observed",
            "spontaneous",
            "prompted",
            "annotation",
        }:
            errors.append(
                f"{item_path}.evidence_origin must be observed, spontaneous, prompted, or annotation"
            )
        attribution = item.get("attribution_certainty")
        if not _is_nonempty_text(attribution) or attribution not in {
            "certain",
            "probable",
            "uncertain",
        }:
            errors.append(
                f"{item_path}.attribution_certainty must be certain, probable, or uncertain"
            )
        claim_status = item.get("claim_status")
        if not _is_nonempty_text(claim_status) or claim_status not in {"stated", "inferred"}:
            errors.append(f"{item_path}.claim_status must be stated or inferred")
        representation = item.get("text_representation")
        if not _is_nonempty_text(representation) or representation not in {
            "verbatim",
            "normalized_verbatim",
            "paraphrase",
            "observed_description",
        }:
            errors.append(
                f"{item_path}.text_representation must be verbatim, normalized_verbatim, paraphrase, or observed_description"
            )
        if representation == "normalized_verbatim":
            _require_text(item, "normalization_note", item_path, errors)


def _validate_links(
    value: Any,
    errors: list[str],
    *,
    allow_empty_local_test: bool,
    links_note: Any,
) -> None:
    if not isinstance(value, list):
        errors.append("links must be a list")
        return
    links = value
    if not links:
        if allow_empty_local_test:
            if not _is_nonempty_text(links_note):
                errors.append(
                    "local test runs with no links require a non-empty links_note"
                )
            return
        errors.append("links must contain at least one item")
        return
    for index, link in enumerate(links):
        path = f"links[{index}]"
        if not isinstance(link, Mapping):
            errors.append(f"{path} must be an object")
            continue
        _require_text(link, "label", path, errors)
        url = link.get("url")
        try:
            parsed = urlparse(url) if _is_nonempty_text(url) else None
            valid_url = bool(
                parsed
                and parsed.scheme in {"http", "https"}
                and parsed.hostname
            )
        except ValueError:
            valid_url = False
        if not valid_url:
            errors.append(f"{path}.url must be an http(s) URL")


def _validate_context_items(
    value: Any, errors: list[str], *, mode: str | None
) -> list[Any]:
    items = _list(value)
    if not items:
        errors.append("context_items must contain at least one item")
        return items
    for index, item in enumerate(items):
        path = f"context_items[{index}]"
        if not isinstance(item, Mapping):
            errors.append(f"{path} must be an object")
            continue
        for key in ("id", "label", "claim"):
            _require_text(item, key, path, errors)
        if _is_nonempty_text(item.get("label")) and not item["label"].startswith("Context —"):
            errors.append(f"{path}.label must start with 'Context —'")
        _validate_evidence(item.get("evidence"), path, errors)
        _validate_confidence(item.get("confidence"), path, errors, mode=mode)
    return items


def _validate_findings(value: Any, mode: str | None, errors: list[str]) -> list[Any]:
    findings = _list(value)
    if not findings:
        errors.append("findings must contain at least one item")
        return findings
    for index, finding in enumerate(findings):
        path = f"findings[{index}]"
        if not isinstance(finding, Mapping):
            errors.append(f"{path} must be an object")
            continue
        for key in ("id", "label", "title", "analysis"):
            _require_text(finding, key, path, errors)
        if _is_nonempty_text(finding.get("label")) and not finding["label"].startswith("Finding —"):
            errors.append(f"{path}.label must start with 'Finding —'")
        _validate_evidence(finding.get("evidence"), path, errors)
        _validate_confidence(finding.get("confidence"), path, errors, mode=mode)
        if mode == "single_session":
            if "recommendation" in finding:
                errors.append("single_session findings must not contain a recommendation field")
            next_step = finding.get("next_research_step")
            if not isinstance(next_step, Mapping) or next_step.get("kind") != "validation_hypothesis":
                errors.append(
                    "single_session findings must use a validation_hypothesis next_research_step, not a product action"
                )
                continue
            _require_text(next_step, "label", f"{path}.next_research_step", errors)
            _require_text(next_step, "text", f"{path}.next_research_step", errors)
            validation_priority = next_step.get("validation_priority")
            if not isinstance(validation_priority, Mapping):
                errors.append(
                    f"{path}.next_research_step.validation_priority must be an object"
                )
            else:
                priority_level = validation_priority.get("level")
                if (
                    not _is_nonempty_text(priority_level)
                    or priority_level not in {"High", "Medium", "Low"}
                ):
                    errors.append(
                        f"{path}.next_research_step.validation_priority.level must be High, Medium, or Low"
                    )
                _require_text(
                    validation_priority,
                    "rationale",
                    f"{path}.next_research_step.validation_priority",
                    errors,
                )
            raw_cues = next_step.get("analyst_generated_cues")
            if not isinstance(raw_cues, list):
                errors.append(
                    f"{path}.next_research_step.analyst_generated_cues must be a list"
                )
                cues = []
            else:
                cues = raw_cues
            for cue_index, cue in enumerate(cues):
                cue_path = f"{path}.next_research_step.analyst_generated_cues[{cue_index}]"
                if not isinstance(cue, Mapping):
                    errors.append(f"{cue_path} must be an object")
                    continue
                _require_text(cue, "cue", cue_path, errors)
                if cue.get("label") != "analyst_generated":
                    errors.append(f"{cue_path}.label must be 'analyst_generated'")
    return findings


def _validate_limitations(value: Any, mode: str | None, errors: list[str]) -> None:
    limitations = _list(value)
    if not limitations:
        errors.append("limitations must contain at least one item")
        return
    types: set[str] = set()
    for index, limitation in enumerate(limitations):
        path = f"limitations[{index}]"
        if not isinstance(limitation, Mapping):
            errors.append(f"{path} must be an object")
            continue
        _require_text(limitation, "type", path, errors)
        _require_text(limitation, "text", path, errors)
        if _is_nonempty_text(limitation.get("type")):
            types.add(limitation["type"])
    if mode == "single_session":
        for required in ("consent_provenance", "speaker_separation"):
            if required not in types:
                errors.append(f"single_session limitations must include {required}")


def _analysis_text(packet: Mapping[str, Any]) -> str:
    content = {
        "context_items": packet.get("context_items", []),
        "findings": packet.get("findings", []),
    }
    return json.dumps(content, ensure_ascii=False)


def _claim_text(packet: Mapping[str, Any]) -> str:
    """Return analyst-authored claim text, excluding evidence and limitations."""
    text: list[str] = []
    for item in _list(packet.get("context_items")):
        if isinstance(item, Mapping):
            text.extend(
                value
                for value in (item.get("label"), item.get("claim"))
                if _is_nonempty_text(value)
            )
    for finding in _list(packet.get("findings")):
        if not isinstance(finding, Mapping):
            continue
        text.extend(
            value
            for value in (
                finding.get("label"),
                finding.get("title"),
                finding.get("analysis"),
            )
            if _is_nonempty_text(value)
        )
        next_step = finding.get("next_research_step")
        if isinstance(next_step, Mapping):
            text.extend(
                value
                for value in (next_step.get("label"), next_step.get("text"))
                if _is_nonempty_text(value)
            )
            validation_priority = next_step.get("validation_priority")
            if isinstance(validation_priority, Mapping) and _is_nonempty_text(
                validation_priority.get("rationale")
            ):
                text.append(validation_priority["rationale"])
    return "\n".join(text)


def _all_evidence(packet: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return [
        evidence_item
        for item in _list(packet.get("context_items")) + _list(packet.get("findings"))
        if isinstance(item, Mapping)
        for evidence_item in _list(item.get("evidence"))
        if isinstance(evidence_item, Mapping)
    ]


def _validate_single_session_boundaries(packet: Mapping[str, Any], errors: list[str]) -> None:
    if "priority_actions" in packet:
        errors.append("single_session packets must not contain priority_actions")
    claim_text = _claim_text(packet)
    for label, expression in SINGLE_SESSION_FORBIDDEN.items():
        if expression.search(claim_text):
            errors.append(f"single_session content contains forbidden {label}")
    serialized = _analysis_text(packet)
    evidence = _all_evidence(packet)
    participant_ids = {
        item.get("participant_id")
        for item in evidence
        if _is_nonempty_text(item.get("participant_id"))
    }
    if len(participant_ids) != 1:
        errors.append("single_session evidence must reference exactly one participant")
    method = packet.get("method")
    declared = method.get("participant_ids") if isinstance(method, Mapping) else None
    declared_is_text = isinstance(declared, list) and all(
        _is_nonempty_text(item) for item in declared
    )
    if not declared_is_text:
        errors.append("method.participant_ids must contain only participant ID text")
    elif len(declared) != 1 or set(declared) != participant_ids:
        errors.append(
            "single_session method.participant_ids must exactly match the evidence participant"
        )
    raw_annotations = packet.get("excluded_annotations", [])
    if not isinstance(raw_annotations, list):
        errors.append("excluded_annotations must be a list")
        raw_annotations = []
    for index, annotation in enumerate(raw_annotations):
        path = f"excluded_annotations[{index}]"
        if not isinstance(annotation, Mapping):
            errors.append(f"{path} must be an object")
            continue
        _require_text(annotation, "value", path, errors)
        if annotation.get("reason") != "platform_annotation":
            errors.append(f"{path}.reason must be 'platform_annotation'")
        value = annotation.get("value")
        if _is_nonempty_text(value) and value.casefold() in serialized.casefold():
            errors.append(f"{path}.value appears in analysis content and was not excluded")


def _validate_priority_actions(value: Any, errors: list[str]) -> None:
    if value is None:
        return
    actions = _list(value)
    if value is not None and not isinstance(value, list):
        errors.append("priority_actions must be a list")
        return
    for index, action in enumerate(actions):
        path = f"priority_actions[{index}]"
        if not isinstance(action, Mapping):
            errors.append(f"{path} must be an object")
            continue
        try:
            style.priority_color(action.get("code"))
        except ValueError:
            errors.append(f"{path}.code must be P0, P1, P2, or Guardrail")
        _require_text(action, "action", path, errors)
        _require_text(action, "confidence", path, errors)


def validate_packet(packet: Any) -> ValidationResult:
    """Validate a single-session memo or multi-session synthesis packet."""
    errors: list[str] = []
    if not isinstance(packet, Mapping):
        return ValidationResult(["packet must be a JSON object"], None, 0, 0)

    mode = packet.get("mode")
    if not _is_nonempty_text(mode) or mode not in MODES:
        errors.append("mode must be 'single_session' or 'multi_session'")
        normalized_mode = None
    else:
        normalized_mode = mode
    if packet.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    for key in ("title", "research_question"):
        _require_text(packet, key, "packet", errors)
    audience = _list(packet.get("audience"))
    if not audience or not all(_is_nonempty_text(item) for item in audience):
        errors.append("audience must contain at least one non-empty label")
    method = packet.get("method")
    if not isinstance(method, Mapping):
        errors.append("method must be an object")
    else:
        _require_text(method, "name", "method", errors)
        _require_text(method, "scope", "method", errors)

    raw_status_labels = packet.get("status_labels", [])
    status_labels = raw_status_labels if isinstance(raw_status_labels, list) else []
    status_labels_valid = isinstance(raw_status_labels, list) and all(
        _is_nonempty_text(label) and label in STATUS_LABELS
        for label in raw_status_labels
    )
    if not status_labels_valid:
        errors.append(
            "status_labels may contain only TEST RUN, SIMULATED DATA, or DRAFT REAL STUDY"
        )

    is_test = packet.get("test_artifact")
    if not isinstance(is_test, bool):
        errors.append("test_artifact must be true or false")
    elif is_test:
        if not str(packet.get("title", "")).startswith("[TEST]"):
            errors.append("test artifact title must start with [TEST]")
        if "TEST RUN" not in status_labels:
            errors.append("test artifacts must include the TEST RUN status label")
        if packet.get("test_artifact_warning") != CANONICAL_TEST_WARNING:
            errors.append("test artifact warning is missing or non-canonical")
        input_provenance = (
            method.get("input_provenance") if isinstance(method, Mapping) else None
        )
        if (
            not _is_nonempty_text(input_provenance)
            or input_provenance not in INPUT_PROVENANCE
        ):
            errors.append(
                "test artifact method.input_provenance must identify real, simulated, or mixed input"
            )
        elif input_provenance in {"simulated_data", "mixed"} and "SIMULATED DATA" not in status_labels:
            errors.append(
                "simulated or mixed test input must include the SIMULATED DATA status label"
            )
        elif input_provenance == "authorized_real_data" and "SIMULATED DATA" in status_labels:
            errors.append(
                "authorized real test input must not be labelled SIMULATED DATA"
            )
        if "DRAFT REAL STUDY" in status_labels:
            errors.append("TEST RUN and DRAFT REAL STUDY must not be combined")
    _validate_links(
        packet.get("links"),
        errors,
        allow_empty_local_test=is_test is True and "TEST RUN" in status_labels,
        links_note=packet.get("links_note"),
    )
    context_items = _list(packet.get("context_items"))
    if normalized_mode == "single_session":
        context_items = _validate_context_items(
            packet.get("context_items"), errors, mode=normalized_mode
        )
    elif "context_items" in packet:
        context_items = _validate_context_items(
            packet.get("context_items"), errors, mode=normalized_mode
        )
    findings = _validate_findings(packet.get("findings"), normalized_mode, errors)
    evidence_ids = [
        item.get("id")
        for item in _all_evidence(packet)
        if _is_nonempty_text(item.get("id"))
    ]
    if len(evidence_ids) != len(set(evidence_ids)):
        errors.append("evidence IDs must be unique")
    _validate_limitations(packet.get("limitations"), normalized_mode, errors)
    if normalized_mode == "single_session":
        _validate_single_session_boundaries(packet, errors)
    elif normalized_mode == "multi_session":
        _validate_priority_actions(packet.get("priority_actions"), errors)

    return ValidationResult(errors, normalized_mode, len(context_items), len(findings))


def build_manifest(
    packet: Mapping[str, Any], *, backend: str = "custom_mcp", tab_id: str = style.DEFAULT_TAB_ID
) -> dict[str, Any]:
    """Return a deterministic, adapter-aware rendering manifest."""
    result = validate_packet(packet)
    if not result.ok:
        raise ContractError("; ".join(result.errors))
    if backend not in BACKENDS:
        raise ValueError("backend must be 'custom_mcp' or 'docs_api'")
    if not _is_nonempty_text(tab_id):
        raise ValueError("tab_id must be non-empty text")

    content_blocks = [
        {"type": "context", "id": item["id"], "label": item["label"]}
        for item in _list(packet.get("context_items"))
    ]
    content_blocks.extend(
        {"type": "finding", "id": item["id"], "label": item["label"]}
        for item in _list(packet.get("findings"))
    )
    style_manifest = {
        "backend": backend,
        "tab_id": tab_id,
        "normal_line_spacing": style.normal_line_spacing(backend),
    }
    if packet["mode"] == "multi_session":
        style_manifest["priority_colors"] = {
            code: style.priority_color(code)
            for code in ("P0", "P1", "P2", "Guardrail")
        }
    return {
        "schema_version": 1,
        "mode": packet["mode"],
        "document": {
            "title": packet["title"],
            "test_artifact": packet["test_artifact"],
            "status_labels": packet.get("status_labels", []),
            "test_artifact_warning": packet.get("test_artifact_warning"),
            "links": packet["links"],
            "links_note": packet.get("links_note"),
        },
        "style": style_manifest,
        "content_blocks": content_blocks,
        "validation": result.to_dict(),
    }


def _load_packet(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate an analysis JSON packet or emit an offline render manifest."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate", help="validate content only")
    validate.add_argument("packet", help="path to an analysis JSON packet")
    manifest = subparsers.add_parser("manifest", help="validate and emit a render manifest")
    manifest.add_argument("packet", help="path to an analysis JSON packet")
    manifest.add_argument(
        "--backend", choices=sorted(BACKENDS), default="custom_mcp"
    )
    manifest.add_argument("--tab-id", default=style.DEFAULT_TAB_ID)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        packet = _load_packet(args.packet)
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    result = validate_packet(packet)
    if args.command == "validate":
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        return 0 if result.ok else 1
    if not result.ok:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
        return 1
    manifest = build_manifest(packet, backend=args.backend, tab_id=args.tab_id)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
