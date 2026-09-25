#!/usr/bin/env python3
"""Check repository packaging, skill frontmatter, and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = REPO_ROOT / "skills" / "interaction-risk-analysis"
REQUIRED_FILES = (
    "skills/interaction-risk-analysis/SKILL.md",
    "skills/interaction-risk-analysis/agents/openai.yaml",
    "skills/interaction-risk-analysis/references/methodology-and-limitations.md",
    "skills/interaction-risk-analysis/references/interaction-decomposition.md",
    "skills/interaction-risk-analysis/references/axioms.md",
    "skills/interaction-risk-analysis/references/signal-mapping.md",
    "skills/interaction-risk-analysis/references/reasoning-with-the-user.md",
    "skills/interaction-risk-analysis/references/scams-and-social-engineering.md",
    "skills/interaction-risk-analysis/references/relationship-coercion.md",
    "skills/interaction-risk-analysis/references/workplace-and-social-bullying.md",
    "skills/interaction-risk-analysis/references/safety-and-agency.md",
    "archive/person-deep-analysis/SKILL.md",
    "docs/research/multilens-psychology-evidence.md",
    "docs/research/multilens-design-review.md",
    "docs/research/network-evaluation-sources.md",
    "docs/research/fraud-and-coercive-control-guidance.md",
    "docs/launch/blog-project-module.md",
    "docs/demos/README.md",
    "docs/demos/01-romance-investment.md",
    "docs/demos/02-task-deposit.md",
    "docs/demos/03-emotional-blackmail.md",
    "docs/demos/04-emotional-abuse-and-control.md",
    "docs/demos/05-peer-bullying.md",
    "docs/demos/06-workplace-bullying.md",
    "docs/demos/07-single-memory-conflict.md",
    "docs/demos/08-counterevidence-update.md",
    "README.md",
    "README_EN.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "docs/launch/README.md",
    "docs/launch/content-kit.md",
    "docs/research/github-comparable-projects.md",
    "docs/research/interaction-risk-skills-landscape.md",
    "docs/research/demo-scenario-sources.md",
    "evals/README.md",
    "evals/behavior-regression.md",
    "evals/safety-scenarios.json",
    "evals/safety-regression.md",
    "evals/interaction-risk-cases.json",
    "evals/interaction-risk-acceptance.md",
    "evals/results/2026-09-25-person-analysis-anti-fraud-acceptance.md",
    "evals/results/2026-09-25-decomposition-method-evaluation.md",
    "evals/results/2026-09-25-public-safety-skill-forward-test.md",
    "evals/results/2026-09-24-network-example-ab-pilot.md",
    "evals/results/2026-09-25-scope-expansion-smoke.md",
    "evals/results/2026-09-24-fraud-agency-forward-test.md",
    "evals/results/2026-09-25-scope-expansion-smoke.md",
    "evals/scenarios.json",
    "evals/cases/case-single-dating.md",
    "evals/cases/case-couple-conflict.md",
    ".github/workflows/validate.yml",
    "scripts/check_skill_discovery.py",
    "scripts/check_skill_installation.py",
    "scripts/validate_skill.py",
    "scripts/validate_safety_evals.py",
    "scripts/validate_interaction_risk_evals.py",
    "scripts/validate_evals.py",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


def check_frontmatter(errors: list[str]) -> None:
    skill_file = SKILL_ROOT / "SKILL.md"
    if not skill_file.is_file():
        return
    content = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        errors.append("skills/interaction-risk-analysis/SKILL.md: missing YAML frontmatter")
        return
    fields = match.group(1)
    name_match = re.search(r"^name:\s*([^\s#]+)\s*$", fields, flags=re.MULTILINE)
    for field in ("name", "description"):
        if not re.search(rf"^{field}:\s*\S", fields, flags=re.MULTILINE):
            errors.append(f"SKILL.md: frontmatter is missing a non-empty {field!r} field")
    if name_match and name_match.group(1) != SKILL_ROOT.name:
        errors.append(
            f"SKILL.md name {name_match.group(1)!r} does not match directory {SKILL_ROOT.name!r}"
        )
    description_match = re.search(
        r"^description:\s*>-?\s*\n((?:[ \t].*\n?)+)", fields, flags=re.MULTILINE
    )
    if description_match and len(description_match.group(1).strip()) > 1024:
        errors.append("SKILL.md: frontmatter description exceeds 1024 characters")
    if description_match and not description_match.group(1).lstrip().startswith("Use when"):
        errors.append("SKILL.md: description should begin with a clear usage trigger ('Use when')")


def check_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (REPO_ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_no_root_skill(errors: list[str]) -> None:
    if (REPO_ROOT / "SKILL.md").exists():
        errors.append("repository root must not contain SKILL.md; installable skill belongs under skills/")


def check_single_installable_skill(errors: list[str]) -> None:
    skill_files = sorted((REPO_ROOT / "skills").glob("*/SKILL.md"))
    expected = REPO_ROOT / "skills" / "interaction-risk-analysis" / "SKILL.md"
    if skill_files != [expected]:
        names = [str(path.relative_to(REPO_ROOT)) for path in skill_files]
        errors.append(f"expected exactly one installable skill {expected.relative_to(REPO_ROOT)}, found {names}")


def check_markdown_links(errors: list[str]) -> None:
    for source in REPO_ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in source.relative_to(REPO_ROOT).parts):
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
                parsed = urlparse(target)
                if parsed.scheme or target.startswith("//") or target.startswith("#"):
                    continue
                path = unquote(parsed.path)
                if not path:
                    continue
                resolved = (source.parent / path).resolve()
                if not resolved.exists():
                    relative = source.relative_to(REPO_ROOT)
                    errors.append(f"{relative}:{line_number}: local link target not found: {path}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_frontmatter(errors)
    check_no_root_skill(errors)
    check_single_installable_skill(errors)
    check_markdown_links(errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed (package files, frontmatter, root boundary, local Markdown links).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
