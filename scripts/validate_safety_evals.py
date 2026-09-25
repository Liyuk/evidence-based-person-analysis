#!/usr/bin/env python3
"""Validate the public-safety scenario set and its manual review anchors."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCENARIOS_FILE = ROOT / "evals" / "safety-scenarios.json"
REPORT_FILE = ROOT / "evals" / "safety-regression.md"
REQUIRED_CATEGORIES = {
    "romance_investment_fraud",
    "task_job_scam",
    "impersonation_and_credential_theft",
    "recovery_scam",
    "false_positive_control",
    "emotional_blackmail",
    "gaslighting_and_uncertainty",
    "coercive_control",
    "boundary_and_repeat_pattern",
    "workplace_bullying",
    "workplace_false_positive_control",
    "bystander_support",
    "online_bullying",
    "immediate_safety",
    "victim_self_blame",
    "uncertain_motive_and_choice",
    "user_led_reasoning",
    "counterevidence_update",
    "privacy_minimization",
    "dual_use_refusal",
    "language_matching",
}


def fail(message: str) -> int:
    print(f"Safety evaluation validation failed: {message}", file=sys.stderr)
    return 1


def main() -> int:
    try:
        data = json.loads(SCENARIOS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(f"cannot read scenario JSON: {exc}")
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return fail("scenario document must be an object with schema_version 1")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or len(scenarios) < 20:
        return fail("expected at least 20 concrete scenarios")

    ids: list[str] = []
    categories: set[str] = set()
    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            return fail(f"scenario {index} must be an object")
        for field in ("id", "category", "input"):
            if not isinstance(scenario.get(field), str) or not scenario[field].strip():
                return fail(f"scenario {index} needs a non-empty string {field!r}")
        for field in ("expected", "forbidden"):
            values = scenario.get(field)
            if not isinstance(values, list) or not values or not all(
                isinstance(value, str) and value.strip() for value in values
            ):
                return fail(f"scenario {scenario['id']!r} needs non-empty string list {field!r}")
        ids.append(scenario["id"])
        categories.add(scenario["category"])
    if len(ids) != len(set(ids)):
        return fail("scenario IDs must be unique")
    missing = REQUIRED_CATEGORIES - categories
    if missing:
        return fail(f"missing required categories: {', '.join(sorted(missing))}")
    try:
        report = REPORT_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        return fail(f"cannot read regression report: {exc}")
    missing_anchors = [
        scenario_id
        for scenario_id in ids
        if not any(
            line.startswith("### ") and f"[{scenario_id}]" in line
            for line in report.splitlines()
        )
    ]
    if missing_anchors:
        return fail(f"missing report anchors: {', '.join(missing_anchors)}")
    print(
        f"Safety evaluation scenarios passed ({len(ids)} unique cases; "
        f"{len(REQUIRED_CATEGORIES)} required categories)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
