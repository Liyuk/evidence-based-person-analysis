# 人际深度解析 Skill 仓库整理实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (recommended) or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将现有 skill 整理为仓库根目录可安装、可理解、可维护的单一 skill 仓库。

**Architecture:** 将 `person-deep-analysis/` 内的规范内容提升到仓库根目录，保留 `SKILL.md` 作为唯一主入口；将案例、研究和设计资料按职责放入 `evals/cases/` 与 `docs/`。补充对外 README、宿主元数据、证据与安全边界，并以无依赖 Python 校验器检查静态仓库完整性。

**Tech Stack:** Markdown、YAML frontmatter、Python 3 标准库。

**Spec:** `docs/superpowers/specs/2026-09-24-skill-repository.md`

## Global Constraints

- 不增加运行时依赖或第三方 Python 依赖。
- 不添加许可证或替用户决定授权条款。
- 八条公理只能作为生成假设的启发式，不能写成普遍因果事实。
- 不扩展为临床诊断、记忆、自动社交媒体抓取、CLI 或在线服务。
- 工作区没有 Git 元数据；不提交、不推送、不发布。
- 原始示例中缺乏依据的创伤/依恋断言要校准为假设并加入替代解释。

## Review Focus

- 根目录提升后 `SKILL.md` 中的相对路径是否全部仍有效。
- 案例示例是否仍把单一行为直接等同创伤、依恋类型或稳定人格。
- YAML frontmatter 与 `agents/openai.yaml` 字段是否满足宿主/Agent Skills 的预期结构。
- 静态校验器是否处理空文件、缺失引用及目录路径中的空格等常见情况。
- 用户输入涉及自伤、胁迫等安全问题时是否明确退出普通画像流程。

---

### Task 1: 将 skill 内容提升为仓库根目录

**Files:**
- Move: `person-deep-analysis/SKILL.md` → `SKILL.md`
- Move: `person-deep-analysis/modules/` → `modules/`
- Move: `person-deep-analysis/dlc/` → `dlc/`
- Move: `person-deep-analysis/references/` → `references/`
- Move: `person-deep-analysis/evals/` → `evals/cases/`
- Move: `person-deep-analysis/docs/research/` → `docs/research/`
- Move: `docs/superpowers/specs/2026-09-24-skill-repository.md` remains in place

- [x] 检查并列出将迁移的文件，保留原始内容，不迁移 `.DS_Store`。
- [x] 迁移主文件和模块/参考/DLC 目录；案例移到 `evals/cases/`，研究报告移到根目录 `docs/research/`。
- [x] 检查主入口和目录树，修正指向旧前缀的路径；未运行链接校验器。
- [x] 删除空的旧目录。

### Task 2: 编写仓库 README 与宿主元数据

**Files:**
- Create: `README.md`
- Create: `agents/openai.yaml`
- Modify: `SKILL.md`

- [x] 写 README，说明用途、适用/不适用范围、安装/调用方式、输入输出示例、分析局限和目录索引。
- [x] 添加 `agents/openai.yaml`，名称与 `SKILL.md` frontmatter 保持一致，描述触发场景并给出简洁中文展示信息。
- [x] 在 `SKILL.md` 增加主分析流程、模块按需读取、DLC 触发方式及低信息量时的收敛策略。
- [x] 保留现有五模块和 DLC 的核心定位，避免 README 和入口定义冲突。

### Task 3: 统一证据、不确定性和安全规范

**Files:**
- Modify: `SKILL.md`
- Modify: `references/axioms.md`
- Create: `references/methodology-and-limitations.md`
- Create: `references/safety-boundaries.md`
- Modify: `modules/m1-deficiency.md`
- Modify: `modules/m2-self-cognition.md`
- Modify: `modules/m3-trauma-tracing.md`
- Modify: `modules/m4-shadow-risk.md`
- Modify: `modules/m5-relationship-prediction.md`
- Modify: `dlc/relationship-dynamics.md`
- Modify: `dlc/narrative-identity.md`

- [x] 将八条公理及主入口中的等号式因果表述改为“候选信号/启发式”，注明不能据此确认动机、创伤或人格。
- [x] 定义统一推理记录格式：观察/来源、假设、支持证据、替代解释、不确定性和待核实信息。
- [x] 加入来源上下文要求：区分本人原话、用户转述、剪辑片段和观察；证据不足时降低结论力度。
- [x] 加入单方材料限制、文化/场景解释、用户纠正机制以及必要时先提澄清问题的规则。
- [x] 单独写明不诊断、不编造经历、不推断隐私属性；涉及自伤、暴力、胁迫、跟踪时优先安全支持。
- [x] 更新模块和 DLC 的关键推断约束。

### Task 4: 校准案例并形成可复核评估要求

**Files:**
- Modify: `evals/cases/case-single-dating.md`
- Modify: `evals/cases/case-couple-conflict.md`
- Create: `evals/README.md`

- [x] 将案例中对创伤、依恋、动机的确定断言改写为有证据支持的假设，加入替代解释。
- [x] 修订检查清单，加入材料溯源、事实/推断区分、替代解释、信息不足时克制和单方叙述限制。
- [x] 在 `evals/README.md` 说明人工复核方式及评估局限。
- [x] 保持示例可读，不为了机器评分强行加入复杂格式。

### Task 5: 增加轻量结构校验器并检查交付

**Files:**
- Create: `scripts/validate_skill.py`
- Modify: `README.md`
- Modify: `evals/README.md`

- [x] 使用 Python 标准库实现 frontmatter 基本字段、必需文件、相对 Markdown 链接目标的静态检查。
- [x] 校验器报告文件路径与问题行，不声称评估分析结论的真实性。
- [x] 在 README 说明命令和检查范围。
- [x] 运行仓库结构校验器（通过），并用 Ruby 标准库解析 `SKILL.md` 与 `agents/openai.yaml`（通过）。
- [x] 尝试 skill-creator 自带检查器；当前环境缺少 PyYAML，无法启动。独立前测和复测结果记录于 `evals/behavior-regression.md`。
- [x] 完成只读静态复核，并按反馈修订术语与案例评估项。
