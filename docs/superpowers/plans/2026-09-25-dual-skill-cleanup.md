# 双 Skill 恢复与文案清理实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 将仓库整理为可独立安装的 `interaction-risk-analysis` 与 `person-deep-analysis` 两个 Skill，并清理公开文案中的过时历史叙述。

**Architecture:** 将现有 `archive/person-deep-analysis/` 恢复为 `skills/person-deep-analysis/`，两个 Skill 保持独立运行时目录。仓库级评估、研究和归档资料继续保留，但公开入口只呈现当前能力、安装方法和边界；发现与安装检查改为验证两个 Skill。

**Tech Stack:** Markdown、YAML、Python 校验脚本、Skills CLI 1.7.0、GitHub Actions。

**Spec:** `docs/superpowers/specs/2026-09-25-dual-skill-cleanup-design.md`

## Global Constraints

- 两个正式 Skill ID 固定为 `interaction-risk-analysis` 和 `person-deep-analysis`。
- 不删除评估、研究和归档资料。
- 任一 Skill 的安装不得混入另一个 Skill 或仓库级 `docs/`、`evals/`、`scripts/`。
- 不改变两个 Skill 的分析方法和安全边界。

## Review Focus

- Skills CLI 是否只发现两个正式 Skill，而不是把 `archive/` 当作入口。
- 两个 Skill 是否都能分别安装到 Codex 与 Claude Code，且引用文件完整。
- 公开 README 是否还残留旧名称、改名过程或过时的单 Skill 描述。
- 历史评估材料中的链接是否仍能指向当前存在的路径。
- 运行时 Skill 是否意外包含仓库级研究或评估文件。

### Task 1: 恢复原始 Skill 安装入口

**Files:**
- Move: `archive/person-deep-analysis/` → `skills/person-deep-analysis/`
- Modify: `skills/person-deep-analysis/SKILL.md` only if its internal links require the new runtime location

- [ ] 移动原始 Skill 目录，保持其模块、DLC、references 与 `agents/openai.yaml` 完整。
- [ ] 修正运行时内部链接或入口名称，使所有引用都在 `skills/person-deep-analysis/` 内可解析。
- [ ] 检查 `skills/*/SKILL.md` 恰好包含两个正式入口。

### Task 2: 更新结构、发现与安装校验

**Files:**
- Modify: `scripts/validate_skill.py`
- Modify: `scripts/check_skill_discovery.py`
- Modify: `scripts/check_skill_installation.py`

- [ ] 将结构校验从单 Skill 改为校验两个 Skill 的 frontmatter、必要文件和本地链接。
- [ ] 让发现校验要求 Skills CLI 报告且仅报告两个 ID。
- [ ] 让安装校验分别安装两个 Skill 到 Codex 与 Claude Code 临时目录，检查各自关键运行时文件和无仓库级内容泄漏。
- [ ] 为每个校验脚本运行一次失败前/通过后的针对性检查。

### Task 3: 清理公开项目文案

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `CONTRIBUTING.md`
- Modify: `docs/launch/README.md`
- Modify: `docs/launch/content-kit.md`
- Modify: `docs/launch/blog-project-module.md`
- Modify: `docs/demos/README.md` as needed for current entry wording

- [ ] README 明确列出两个 Skill 及其适用场景、独立安装命令和共同边界。
- [ ] 删除改名过程、旧 Skill ID、旧仓库跳转、历史运行状态和面向 GitHub 浏览者的额外说明。
- [ ] 保留实际安装所需的仓库地址，不将 GitHub 迁移背景写进用户文案。
- [ ] 将英文入口与中文入口的 Skill 名称、范围和限制对齐。

### Task 4: 修复内部链接与当前状态描述

**Files:**
- Modify: `evals/README.md`
- Modify: `docs/research/` 中仍指向已移动目录的文件
- Modify: `docs/superpowers/specs/` 与 `docs/superpowers/plans/` 中需要保持当前结构准确的链接

- [ ] 只修复会失效的路径和当前结构说明，不删除历史评估结果。
- [ ] 将当前运行时路径统一为 `skills/interaction-risk-analysis/` 或 `skills/person-deep-analysis/`。
- [ ] 重新运行本地 Markdown 链接检查。

### Task 5: 全量验证

**Files:**
- Test: all repository validation scripts and `.github/workflows/validate.yml` command set

- [ ] 运行 `python3 scripts/validate_skill.py`。
- [ ] 运行 `python3 scripts/validate_evals.py`。
- [ ] 运行 `python3 scripts/validate_safety_evals.py`。
- [ ] 运行 `python3 scripts/validate_interaction_risk_evals.py`。
- [ ] 运行 `python3 scripts/check_skill_discovery.py`。
- [ ] 运行 `python3 scripts/check_skill_installation.py`。
- [ ] 对失败项修复后完整重跑，并记录最终结果。
