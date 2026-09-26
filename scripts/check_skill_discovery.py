#!/usr/bin/env python3
"""Assert Skills CLI discovers exactly this repository's two installable skills."""

from __future__ import annotations

import re
import subprocess
import sys


EXPECTED = {"interaction-risk-analysis", "person-deep-analysis"}
SKILLS_CLI_VERSION = "1.7.0"
TIMEOUT_SECONDS = 120
ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
SKILL_LINE_RE = re.compile(r"^\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$")


def parse_available_skills(output: str) -> set[str]:
    start = output.find("Available Skills")
    end = output.find("Use --skill", start)
    if start < 0 or end < 0:
        return set()
    names: set[str] = set()
    for line in output[start:end].splitlines()[1:]:
        clean = line.replace("│", " ").strip()
        match = SKILL_LINE_RE.fullmatch(clean)
        if match:
            names.add(match.group(1))
    return names


def main() -> int:
    result = subprocess.run(
        ["npx", "--yes", f"skills@{SKILLS_CLI_VERSION}", "add", ".", "--list"],
        check=False,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
    )
    output = result.stdout + result.stderr
    print(output, end="" if output.endswith("\n") else "\n")
    if result.returncode:
        print(f"Skills CLI exited with status {result.returncode}", file=sys.stderr)
        return result.returncode
    normalized_output = ANSI_ESCAPE_RE.sub("", output)
    count_match = re.search(r"Found\s+(\d+)\s+skills?", normalized_output, flags=re.IGNORECASE)
    if not count_match or int(count_match.group(1)) != len(EXPECTED):
        print(f"Expected Skills CLI to discover exactly {len(EXPECTED)} skills", file=sys.stderr)
        return 1
    available = parse_available_skills(normalized_output)
    if available != EXPECTED:
        print(
            f"Expected Skills CLI to list only {sorted(EXPECTED)}; found {sorted(available)}",
            file=sys.stderr,
        )
        return 1
    print(f"Discovery check passed: exactly {', '.join(sorted(EXPECTED))} are available.")
    return 0


def run() -> int:
    try:
        return main()
    except subprocess.TimeoutExpired:
        print(f"Skills CLI discovery timed out after {TIMEOUT_SECONDS}s", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(run())
