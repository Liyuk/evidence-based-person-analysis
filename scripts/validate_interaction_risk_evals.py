#!/usr/bin/env python3
"""Validate interaction-risk cases and their acceptance anchors."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CASES_FILE = ROOT / "evals" / "interaction-risk-cases.json"
ACCEPTANCE_FILE = ROOT / "evals" / "interaction-risk-acceptance.md"
CURRENT_HOST_REPORT = ROOT / "evals" / "results" / "interaction-risk-analysis-host-acceptance.md"
REQUIRED_CASES = 20
REQUIRED_CATEGORIES = {
    "multi_event_decomposition",
    "single_event_boundary",
    "financial_scam",
    "credential_scam",
    "recovery_scam",
    "claim_action_decomposition",
    "counterevidence_update",
    "false_positive_control",
    "repeated_interaction_pattern",
    "workplace_bullying",
    "user_agency_and_reasoning",
    "compassion_and_recovery",
    "urgent_safety",
    "diagnosis_boundary",
    "multi_lens_steelman",
    "dual_use_refusal",
    "privacy_minimization",
    "causal_and_purpose_inference",
}


def fail(message: str) -> int:
    print(f"Interaction-risk evaluation validation failed: {message}", file=sys.stderr)
    return 1


def main() -> int:
    try:
        data = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(f"cannot read case JSON: {exc}")
    if not isinstance(data, dict) or data.get("version") != 1:
        return fail("case document must be an object with version 1")
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < REQUIRED_CASES:
        return fail(f"expected at least {REQUIRED_CASES} cases")

    ids: list[str] = []
    categories: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            return fail(f"case {index} must be an object")
        for field in ("id", "category", "input"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                return fail(f"case {index} needs a non-empty string {field!r}")
        for field in ("expected", "forbidden"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.strip() for value in values
            ):
                return fail(f"case {case['id']!r} needs a non-empty string list {field!r}")
        ids.append(case["id"])
        categories.add(case["category"])
    if len(ids) != len(set(ids)):
        return fail("case IDs must be unique")
    missing_categories = REQUIRED_CATEGORIES - categories
    if missing_categories:
        return fail(f"missing categories: {', '.join(sorted(missing_categories))}")

    try:
        acceptance = ACCEPTANCE_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        return fail(f"cannot read acceptance document: {exc}")
    missing_anchors = [
        case_id
        for case_id in ids
        if f"### [{case_id}]" not in acceptance
    ]
    if missing_anchors:
        return fail(f"missing acceptance anchors: {', '.join(missing_anchors)}")

    index_match = re.search(
        r"^## 场景索引\s*$([\s\S]*?)(?=^## |\Z)", acceptance, flags=re.MULTILINE
    )
    if not index_match:
        return fail("acceptance document is missing the scenario index")
    index_rows = re.findall(
        r"^\| \[([^]]+)\] \| ([^|]+) \|\s*$", index_match.group(1), flags=re.MULTILINE
    )
    indexed_ids = [case_id for case_id, _ in index_rows]
    if len(indexed_ids) != len(set(indexed_ids)):
        return fail("acceptance scenario index contains duplicate case IDs")
    if indexed_ids != ids:
        missing = sorted(set(ids) - set(indexed_ids))
        extra = sorted(set(indexed_ids) - set(ids))
        details = []
        if missing:
            details.append(f"missing from index: {', '.join(missing)}")
        if extra:
            details.append(f"unknown in index: {', '.join(extra)}")
        return fail("acceptance scenario index does not match case JSON (" + "; ".join(details) + ")")
    non_pending = [
        case_id for case_id, status in index_rows if status.strip() != "新 ID 未运行"
    ]
    if non_pending:
        try:
            host_report = CURRENT_HOST_REPORT.read_text(encoding="utf-8")
        except OSError:
            return fail(
                "acceptance statuses claim current-ID runs, but the current host report is missing"
            )
        if "$interaction-risk-analysis" not in host_report:
            return fail("current host report must identify an explicit $interaction-risk-analysis run")
        unreported = [case_id for case_id in non_pending if case_id not in host_report]
        if unreported:
            return fail("current host report does not mention indexed cases: " + ", ".join(unreported))

    print(
        f"Interaction-risk cases passed ({len(ids)} unique cases; "
        f"{len(REQUIRED_CATEGORIES)} required categories; acceptance index matches case JSON)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
