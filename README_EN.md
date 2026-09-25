# Person Deep Analysis

**Don't guess what's in someone's mind. Separate the evidence, hypotheses, and unknowns.**

An Agent Skill for analyzing self-descriptions, profiles, selected chat excerpts, interactions, and fictional characters while separating textual evidence, limited interpretations, and unknowns. Chat analysis uses relevant excerpts rather than requiring a complete archive. Fictional-character analysis stays within how the work portrays a character and does not infer an author's psychology. It is not for diagnosing real people, predicting relationship outcomes, or making decisions for the user. The workflow and examples are primarily in Chinese; English inputs can be analyzed, and you can request an English response.

## Install

Install the published skill with [Skills CLI](https://github.com/vercel-labs/skills):

```sh
# Codex
npx skills add Liyuk/evidence-based-person-analysis --skill person-deep-analysis -g --agent codex -y

# Claude Code
npx skills add Liyuk/evidence-based-person-analysis --skill person-deep-analysis -g --agent claude-code -y
```

The repository has passed CI checks for Skills CLI discovery and isolated Codex/Claude Code installation layouts. A Codex CLI smoke test with explicit invocation and one project-level implicit-trigger check is recorded in the [behavior report](evals/results/2026-09-24-codex-cli-runtime-smoke.md); chat/fiction analysis is covered in a [scope-expansion smoke test](evals/results/2026-09-25-scope-expansion-smoke.md); a three-case Skill/baseline pilot with single-model blind scoring is in the [A/B report](evals/results/2026-09-24-network-example-ab-pilot.md); fraud/agency forward tests are summarized in the [specialized report](evals/results/2026-09-24-fraud-agency-forward-test.md). These small pilots helped find and fix rule gaps but do not establish stable gains or psychological validity. Desktop auto-loading, cross-model consistency, and real-user outcomes remain unevaluated. To check discovery from a local clone:

`npx skills` is the installer CLI; the Skill itself is installed directly from GitHub, so a separate npm package is not needed. Consider npm only if the project later ships a reusable JavaScript library or command-line tool.

```sh
npx --yes skills add . --list
```

For a manual Codex install:

```sh
mkdir -p ~/.codex/skills
cp -R ./skills/person-deep-analysis ~/.codex/skills/
```

The repository has been checked for local Skills CLI discovery and sandboxed Codex and Claude Code installs from the repository root. These checks verify destination layout, runtime files, and exclusion of repository-only documents, not automatic loading or model behavior inside either host. To target Claude Code with Skills CLI, replace `codex` with `claude-code`.

For a manual Claude Code install:

```sh
mkdir -p ~/.claude/skills
cp -R ./skills/person-deep-analysis ~/.claude/skills/
```

## Try it

```text
Use $person-deep-analysis on this profile. Separate direct observations from interpretations, give evidence and a plausible alternative for each main hypothesis, and state what remains unknown. Do not diagnose; narrow the analysis if the evidence is sparse.
```

For a deeper comparison, explicitly ask for a multi-perspective steelman report. The skill should identify which lenses fit the evidence, present supported explanations and alternatives, and leave unresolved disagreements visible.

You can also ask it to analyze selected chat excerpts or fictional characters. For chats, preserve speaker labels and chronology, and distinguish multiple messages within one event from independent repeated events. For fiction, cite scenes and separate what the work states from interpretations of the character and the story's narrative function.

## Good fit

- Clarify preferences stated in a short personal profile or selected chat excerpt.
- Compare interactions across independent scenes without treating every message as a separate event.
- Analyze how a novel, film, show, or game portrays a character and their development.
- Identify what additional context would change an interpretation.

It can help organize observable warning signs in suspected romance/investment scams or coercive relationship behavior and present user-chosen support options. It does not verify identities, guarantee recovery, replace professional/crisis support, diagnose NPD, or generate manipulation or fraud tactics. Not for inferring trauma or sensitive traits, predicting relationship outcomes, or profiling criminal risk.

## What makes it different

In our limited sample of eight public repositories, evidence-first analysis, alternatives, and uncertainty also appear in adjacent projects. For example, [Analyze Romantic Relationships](https://github.com/jeejohn/analyze-romantic-relationships) focuses on relationship claims and decision support, while [Person Behavior Analysis](https://github.com/wangguofeng728/person-behavior-analysis-skill) focuses on long-term chat records and longitudinal behavior hypotheses. This skill works from the material selected for the current request—self-descriptions, chat excerpts, interactions, or fictional work—and states what it supports and what remains unknown. It does not require a persistent chat archive or default to relationship decisions; fictional-character conclusions stay within the text. This sample-based positioning does not claim ecosystem-wide uniqueness. See the [comparison research](docs/research/github-comparable-projects.md) for scope and sources.

Its heuristics are prompts for questions, not validated causal laws or clinical measures. It is not a diagnostic or crisis-response tool. If the material indicates imminent danger, prioritize real-world safety support over profile analysis.

Remove names, handles, locations, and other identifying details from third-party material when possible. The person seeking help retains authority over their boundaries and next steps; the skill should support choices without blaming or directing them. For local hotlines, legal deadlines, or platform-specific actions, verify current official sources for the user's location. This skill cannot control how the host platform stores or processes input; follow that platform's data settings.

An explicitly requested multi-perspective report can compare psychodynamic, humanistic/needs, developmental, and descriptive CBT lenses. Each is treated as a limited hypothesis generator, not an independent test of a person's inner life. Forensic psychology contributes evidence discipline only; the skill does not profile or predict crime.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Evaluation cases must be synthetic or carefully de-identified with permission; never submit private messages, photos, account details, or identifying information. See the [comparison research](docs/research/github-comparable-projects.md), [evaluation limits](evals/README.md), and [primary-source note on fraud/coercive-control support](docs/research/fraud-and-coercive-control-guidance.md).

Licensed under the [MIT License](LICENSE).
