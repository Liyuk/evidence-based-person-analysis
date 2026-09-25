# Interaction Risk Analysis

**Deconstruct interactions involving scams, manipulation, abuse, or bullying. Keep the decision with the user.**

An Agent Skill for ordinary people dealing with suspicious interactions, romance scams, coercion, emotional manipulation or abuse, and interpersonal bullying. It separates what was said, what happened, how events unfolded, the effects of behavior, possible purposes, counterevidence, and unknowns. Models already recognize many patterns; the Skill supplies a repeatable prompt method for making those judgments inspectable and revisable, rather than treating a familiar label as the answer. It does not diagnose people or decide who is a criminal.

[Eight paired scenario demos](docs/demos/README.md) preserve historical outputs from ordinary Codex and explicit `$person-analysis` runs before the rename, using synthetic prompts grounded in official public guidance.

## Install

This repository provides one installable Skill: `interaction-risk-analysis`.

For Codex:

```sh
npx skills add Liyuk/interaction-risk-analysis --skill interaction-risk-analysis -g -a codex -y
```

For Claude Code:

```sh
npx skills add Liyuk/interaction-risk-analysis --skill interaction-risk-analysis -g -a claude-code -y
```

## How it works

For a multi-event romance-investment scenario, the Skill can lay out the timeline, distinguish an identity claim from verified facts, and explain why a move off-platform, blocked verification, secrecy, and urgent payment together deserve caution. It can then separate a behavior's practical effect from possible intent, identify what evidence could distinguish competing explanations, and offer next steps. A single suspicious phrase is not enough to infer a stable personality or repeated pattern.

```text
$interaction-risk-analysis
Use this method to deconstruct the interaction: build an event timeline; separate quotes, claims, observed behavior, and inference; explain the behavior's practical effects and possible purposes with evidence, counterevidence, alternatives, and unknowns. Distinguish sequence from causation and effect from intent. Say what evidence would change the assessment, then offer optional responses. Do not jump to a familiar label or decide the case for me.
```

The project grew from earlier person-analysis work, but the current Skill is named for its public task: analyzing interaction risks. It asks the model to make evidence and competing explanations inspectable; it does not claim a unique detection ability.

## Scope and limits

Use it for romance/investment and job scams, impersonation, credential requests, recovery scams, emotional blackmail, coercion, isolation, monitoring, workplace bullying, and bounded profile or relationship-material analysis. It also tests false positives such as a single memory disagreement or ordinary constructive feedback.

This is not an automatic detector, clinical diagnosis, legal finding, investigation, bank fraud system, or fund-recovery service. It cannot establish identity, criminal liability, or hidden motives from chat alone. Psychology is an optional explanatory lens, not proof. In urgent situations, address immediate financial or personal safety first. Avoid sharing unnecessary names, account details, or full private chats.

## Evaluation

The repository contains 20 synthetic acceptance cases with expected and forbidden behaviors, including causal and purpose inference. These cases have not yet been run individually with the renamed `interaction-risk-analysis` ID. Eight scenario demos preserve ordinary Codex and explicit Skill outputs from before the rename, when the Skill ID was `person-analysis`; they are historical results, not reruns of the current ID. The [historical acceptance report](evals/results/2026-09-25-person-analysis-anti-fraud-acceptance.md) records those runs and their limits.

```sh
python3 scripts/validate_skill.py
python3 scripts/validate_evals.py
python3 scripts/validate_safety_evals.py
python3 scripts/validate_interaction_risk_evals.py
python3 scripts/check_skill_discovery.py
python3 scripts/check_skill_installation.py
```

The GitHub repository slug and installable Skill ID are `interaction-risk-analysis`. License: MIT.
