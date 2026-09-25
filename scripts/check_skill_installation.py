#!/usr/bin/env python3
"""Install from this repository into temporary Codex and Claude Code projects."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_SOURCE = REPO_ROOT
SKILL_NAME = "interaction-risk-analysis"
SKILLS_CLI_VERSION = "1.7.0"
TIMEOUT_SECONDS = 120
REQUIRED_RUNTIME_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "modules/m5-interaction-patterns.md",
    "references/interaction-decomposition.md",
    "references/methodology-and-limitations.md",
    "references/axioms.md",
    "references/signal-mapping.md",
    "references/reasoning-with-the-user.md",
    "references/scams-and-social-engineering.md",
    "references/relationship-coercion.md",
    "references/workplace-and-social-bullying.md",
    "references/safety-and-agency.md",
)


def main() -> int:
    with TemporaryDirectory(prefix="interaction-risk-install-") as temp_dir:
        try:
            result = subprocess.run(
                [
                    "npx",
                    "--yes",
                    f"skills@{SKILLS_CLI_VERSION}",
                    "add",
                    str(SKILL_SOURCE),
                    "--skill",
                    SKILL_NAME,
                    "--agent",
                    "codex",
                    "claude-code",
                    "--yes",
                    "--copy",
                ],
                cwd=temp_dir,
                check=False,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            print(f"Skills CLI installation timed out after {TIMEOUT_SECONDS}s", file=sys.stderr)
            return 1
        output = result.stdout + result.stderr
        print(output, end="" if output.endswith("\n") else "\n")
        if result.returncode:
            print(f"Skills CLI exited with status {result.returncode}", file=sys.stderr)
            return result.returncode
        installed_entries = {
            "Codex": Path(temp_dir) / ".agents" / "skills" / SKILL_NAME,
            "Claude Code": Path(temp_dir) / ".claude" / "skills" / SKILL_NAME,
        }
        for agent, installed_entry in installed_entries.items():
            missing = [name for name in REQUIRED_RUNTIME_FILES if not (installed_entry / name).is_file()]
            if missing:
                print(
                    f"{agent}-target install is missing runtime files: {', '.join(missing)}",
                    file=sys.stderr,
                )
                return 1
            leaked = [name for name in ("evals", "docs", "scripts") if (installed_entry / name).exists()]
            if leaked:
                print(f"Repository-only content leaked into {agent} skill install: {', '.join(leaked)}", file=sys.stderr)
                return 1
        print("Sandboxed repository installs passed for Codex and Claude Code; skill files are complete and repo-only content is excluded.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
