# 公益识骗与反操控 Skill 重构 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 将唯一主 Skill 收敛为帮助普通人识别诈骗、心理操控和霸凌并保留自主判断的公众安全工具，同时把旧人物分析 Skill 归档。

**Architecture:** 新建一个精简安装包 `skills/scam-and-manipulation-support/`，共享证据推理流程，按风险场景路由到专门参考。将旧 Skill 移出可安装目录保存，不继承与公益安全主线无关的人物画像功能。用独立的合成场景清单、行为报告、仓库校验与 Codex CLI 前向试跑验证。

**Tech Stack:** Agent Skills Markdown/YAML、Python 3 标准库校验脚本、Skills CLI 1.7.0、Codex CLI 合成场景运行。

**Spec:** `docs/superpowers/specs/2026-09-24-public-safety-skill-refactor.md`

## Global Constraints

- 唯一可安装包为 `skills/scam-and-manipulation-support/`。
- 风险结论必须从具体行为、时间/场景和影响推出，不从单一词语或人格标签推出。
- 保留支持与同理，但让用户可质疑假设、选择是否回答和决定下一步。
- 已有未提交改动必须保留；GitHub 远端 slug 和发布版本保持不变。
- 行为实测只用合成案例，至少 8 个代表场景，不声称实证准确率。

## Review Focus

- 只有一次伤人感受或正常工作反馈时，Skill 是否避免把冲突误报成霸凌/操控。
- 用户要求 AI 帮自己推断时，Skill 是否邀请其核对证据但不引导预设答案。
- 高风险转账/凭证索取时，Skill 是否先给直接止损选项，而不过度延长问答。
- 用户已受骗并自责时，Skill 是否能避免羞辱、避免虚假追回承诺。
- 面对监控/报复风险时，建议记录或举报是否会根据安全性与用户选择调整。

---

### Task 1: 建立新的安全场景回归集

**Files:**
- Create: `evals/safety-scenarios.json`
- Create: `evals/safety-regression.md`
- Create: `scripts/validate_safety_evals.py`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Produces: JSON `scenarios` entries with `id`, `category`, `input`, non-empty `expected`, and non-empty `forbidden` arrays.
- Produces: validator requiring 20 named behavioral categories and one Markdown report anchor per case.

- [x] **Step 1: Write the failing scenario set and validator contract first.** Add 20+ concrete synthetic inputs, categories, outcomes, and report anchors. Categories: investment/romance fraud; task/job scam; impersonation/credential theft; recovery scam; false-positive invoice verification; emotional blackmail; gaslighting uncertainty; coercive isolation; boundary testing; workplace harassment; legitimate critical feedback; bystander support; online pile-on; immediate threat; self-blame after loss; uncertain motive/behavioral choice; user-led inference; counterevidence update; privacy minimization; manipulation dual-use refusal.
- [x] **Step 2: Run the safety validator and record the expected failure** because `validate_safety_evals.py` does not yet exist.
- [x] **Step 3: Implement a standard-library validator** that checks schema, uniqueness, required categories, non-empty criteria, and report headings without checking model-generated wording.
- [x] **Step 4: Run the validator** and confirm it reports at least 20 unique cases with all categories present.
- [x] **Step 5: Add the validator to CI** and run it again.

### Task 2: Repackage the runtime around the new mission

**Files:**
- Move: `skills/person-deep-analysis/` → `archive/person-deep-analysis/`
- Create: `skills/scam-and-manipulation-support/SKILL.md`
- Create: `skills/scam-and-manipulation-support/agents/openai.yaml`
- Create: `skills/scam-and-manipulation-support/references/reasoning-with-the-user.md`
- Create: `skills/scam-and-manipulation-support/references/scams-and-social-engineering.md`
- Create: `skills/scam-and-manipulation-support/references/relationship-coercion.md`
- Create: `skills/scam-and-manipulation-support/references/workplace-and-social-bullying.md`
- Create: `skills/scam-and-manipulation-support/references/safety-and-agency.md`
- Modify: `scripts/validate_skill.py`
- Modify: `scripts/check_skill_discovery.py`
- Modify: `scripts/check_skill_installation.py`

**Interfaces:**
- Consumes: Task 1 `safety-scenarios.json` categories as behavioral requirements.
- Produces: one skill named `scam-and-manipulation-support`; all runtime references are relative under that folder.

- [x] **Step 1: Before moving the package, run baseline Codex CLI simulations** on at least two representative existing fraud/control cases and one ambiguous non-harm case; save outputs under a temporary directory outside the repository.
- [x] **Step 2: Update validators first** to require the new single skill and its exact required runtime files; change discovery/install expected name and runtime manifest. Run the current package checks and observe expected failure.
- [x] **Step 3: Move the old Skill to archive** and write new skill files from the approved spec, with an always-used observe→hypothesis→evidence/counterevidence→independent-check→user-choice loop and immediate-safety/financial-stop exceptions.
- [x] **Step 4: Run structural validator, discovery check and isolated install check**; fix any missing references or accidental archive discovery.

### Task 3: Align user-facing project information

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `CONTRIBUTING.md`
- Modify: `evals/README.md`
- Modify: local Markdown references to moved Skill files
- Create: `docs/launch/public-safety-project-module.md`

**Interfaces:**
- Consumes: new skill ID and runtime workflow from Task 2.
- Produces: consistent Chinese/English mission, installation commands, sample usage and explicitly bounded claims.

- [x] **Step 1: Update README title, short promise, install command, example and capability boundaries** to center public safety and shared inference; describe legacy analysis as archived, not a second product.
- [x] **Step 2: Update contributor and eval docs** to distinguish static case standards from model-run results and protect synthetic/privacy boundaries.
- [x] **Step 3: Search for stale install IDs and moved local links**; fix documentation links while keeping historical descriptions historically accurate.
- [x] **Step 4: Run repository link/package validation** and confirm no stale runtime reference is presented as installable.

### Task 4: Run and assess behavior simulations

**Files:**
- Modify: `evals/safety-regression.md`
- Create: `evals/results/2026-09-25-public-safety-skill-forward-test.md`
- Modify: runtime references only for failures demonstrated by scenarios

**Interfaces:**
- Consumes: scenario input/criteria from Task 1 and installed package from Task 2.
- Produces: per-case baseline/final qualitative result, observed evidence, known limits, and retest record.

- [x] **Step 1: Run 8 or more synthetic prompts through Codex CLI with explicit Skill invocation** using `--ephemeral --sandbox read-only` and an isolated temporary project.
- [x] **Step 2: Score each output against every relevant expected/forbidden criterion**; label pass/partial/fail and quote only short synthetic snippets as evidence.
- [x] **Step 3: Fix demonstrated Important/Critical failures** with a scenario that reproduces the defect; re-run affected case before editing and after editing.
- [x] **Step 4: Run all structural, eval, CLI discovery, and installation checks** and record exact commands/results and remaining limitations.

### Task 5: Final review and handoff

**Files:**
- Modify: this plan's completion checkboxes and final test record.

**Interfaces:**
- Consumes: complete Tasks 1–4 outputs.
- Produces: final reviewed branch with migration and validation evidence.

- [x] **Step 1: Inspect full diff** for deleted user work, stale names, diagnosis/false-positive hazards, privacy leaks, and overclaiming.
- [x] **Step 2: Run `git diff --check`, `python3 scripts/validate_skill.py`, `python3 scripts/validate_evals.py`, `python3 scripts/validate_safety_evals.py`, `python3 scripts/check_skill_discovery.py`, and `python3 scripts/check_skill_installation.py`.**
- [x] **Step 3: Report changed architecture, real scenario results, failures fixed, remaining limitations, current branch and uncommitted status.**
