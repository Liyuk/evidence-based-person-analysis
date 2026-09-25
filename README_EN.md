# Person Deep Analysis

**Don't guess what's in someone's mind. Separate the evidence, hypotheses, and unknowns.**

An Agent Skill for understanding what user-provided self-descriptions, personal profiles, or short interaction excerpts actually say, what limited interpretations they may support, and what context is missing. It helps organize material; it is not for labeling people, predicting relationship outcomes, or making decisions for the user. The workflow and examples are primarily in Chinese; English inputs can be analyzed, and you can request an English response.

## Install

After this repository is published, install the skill with [Skills CLI](https://github.com/vercel-labs/skills):

```sh
# Codex
npx skills add <OWNER>/<REPO> --skill person-deep-analysis -g --agent codex -y

# Claude Code
npx skills add <OWNER>/<REPO> --skill person-deep-analysis -g --agent claude-code -y
```

Replace `<OWNER>/<REPO>` with the actual GitHub source. For local discovery before publication:

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

## Good fit

- Clarify preferences stated in a short personal profile.
- Separate words, observable behavior, and interpretation in one interaction excerpt.
- Identify what additional context would change an interpretation.

Not for diagnosing, inferring trauma or sensitive traits, proving what someone is “really like,” predicting relationship outcomes, or responding to immediate danger.

## What makes it different

Among the projects in our comparison, several focus on relationship advice, couple-conflict interventions, chat-archive analysis, or relationship simulation. This skill focuses on a structured analysis of one person's supplied material, with optional relationship and narrative modules. It does not decide whether a user should stay in a relationship, infer trauma from a profile, or claim to reveal someone's true inner life.

Its heuristics are prompts for questions, not validated causal laws or clinical measures. It is not a diagnostic or crisis-response tool. If the material indicates imminent danger, prioritize real-world safety support over profile analysis.

Remove names, handles, locations, and other identifying details from third-party material when possible. This skill cannot control how the host platform stores or processes input; follow that platform's data settings.

An explicitly requested multi-perspective report can compare psychodynamic, humanistic/needs, developmental, and descriptive CBT lenses. Each is treated as a limited hypothesis generator, not an independent test of a person's inner life. Forensic psychology contributes evidence discipline only; the skill does not profile or predict crime.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Evaluation cases must be synthetic or carefully de-identified with permission; never submit private messages, photos, account details, or identifying information. See the [comparison research](docs/research/github-comparable-projects.md) and [evaluation limits](evals/README.md).

Licensed under the [MIT License](LICENSE).
