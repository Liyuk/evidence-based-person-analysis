#!/usr/bin/env python3
"""Assert Skills CLI discovers exactly this repository's installable skill."""

from __future__ import annotations

import re
import subprocess
import sys


EXPECTED = "person-deep-analysis"
SKILLS_CLI_VERSION = "1.7.0"
TIMEOUT_SECONDS = 120


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
    count_match = re.search(r"Found\s+(\d+)\s+skills?", output, flags=re.IGNORECASE)
    if not count_match or int(count_match.group(1)) != 1:
        print("Expected Skills CLI to discover exactly one skill", file=sys.stderr)
        return 1
    if EXPECTED not in output:
        print(f"Expected Skills CLI to list {EXPECTED!r}", file=sys.stderr)
        return 1
    print(f"Discovery check passed: exactly {EXPECTED} is available.")
    return 0


def run() -> int:
    try:
        return main()
    except subprocess.TimeoutExpired:
        print(f"Skills CLI discovery timed out after {TIMEOUT_SECONDS}s", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(run())
