#!/usr/bin/env python3
"""Validate the repeatable manual behavior-evaluation scenario set."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCENARIOS_FILE = ROOT / "evals" / "scenarios.json"
REPORT_FILE = ROOT / "evals" / "behavior-regression.md"
REQUIRED_CATEGORIES = {
    "low_information",
    "apparently_conflicting_signals",
    "single_excerpt",
    "absent_person_and_hearsay",
    "diagnosis_boundary",
    "immediate_safety",
    "language_and_sparse_evidence",
    "privacy_minimization",
    "multilens_applicability",
    "steelman_no_false_balance",
    "psychodynamic_overreach",
    "developmental_causality",
    "humanistic_subjectivity",
    "needs_model_nonhierarchical",
    "cbt_self_report_boundary",
    "forensic_crime_prediction",
    "cross_lens_disagreement",
    "counterevidence_update",
    "explicit_steelman_components",
    "ambiguous_nonviolent_residence_visit",
    "fraud_pattern_support",
    "coercive_control_and_agency",
    "dual_use_manipulation",
    "diagnosis_vs_behavior",
    "chat_record_scoped_analysis",
    "fictional_character_textual_analysis",
}


def main() -> int:
    try:
        data = json.loads(SCENARIOS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read evaluation scenarios: {exc}", file=sys.stderr)
        return 1
    if not isinstance(data, dict):
        print("Evaluation scenario document must be a JSON object", file=sys.stderr)
        return 1
    if data.get("schema_version") != 1:
        print("Unsupported or missing scenario schema_version", file=sys.stderr)
        return 1
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or len(scenarios) < len(REQUIRED_CATEGORIES):
        print("Expected at least one scenario for each required behavior category", file=sys.stderr)
        return 1
    ids: list[str] = []
    categories: set[str] = set()
    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            print(f"Scenario {index} must be an object", file=sys.stderr)
            return 1
        for field in ("id", "category", "input", "expected", "forbidden"):
            if field not in scenario:
                print(f"Scenario {index} is missing {field!r}", file=sys.stderr)
                return 1
        string_fields = ("id", "category", "input")
        if not all(
            isinstance(scenario[field], str) and scenario[field].strip()
            for field in string_fields
        ):
            print(f"Scenario {index} has an invalid id, category, or input", file=sys.stderr)
            return 1
        if not all(
            isinstance(scenario[field], list)
            and scenario[field]
            and all(isinstance(item, str) and item.strip() for item in scenario[field])
            for field in ("expected", "forbidden")
        ):
            print(f"Scenario {scenario['id']!r} needs non-empty string lists for expected and forbidden", file=sys.stderr)
            return 1
        ids.append(scenario["id"])
        categories.add(scenario["category"])
    if len(set(ids)) != len(ids):
        print("Scenario ids must be unique", file=sys.stderr)
        return 1
    missing_categories = REQUIRED_CATEGORIES - categories
    if missing_categories:
        print(f"Missing behavior categories: {', '.join(sorted(missing_categories))}", file=sys.stderr)
        return 1
    report = REPORT_FILE.read_text(encoding="utf-8")
    missing_ids = [
        scenario_id
        for scenario_id in ids
        if not any(
            line.lstrip().startswith("#") and f"[{scenario_id}]" in line
            for line in report.splitlines()
        )
    ]
    if missing_ids:
        print(f"Behavior report is missing scenario headings: {', '.join(missing_ids)}", file=sys.stderr)
        return 1
    print(f"Evaluation scenarios passed ({len(ids)} unique cases; {len(REQUIRED_CATEGORIES)} required behavior categories).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
