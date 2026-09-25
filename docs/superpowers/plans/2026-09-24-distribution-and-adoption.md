# Skill 分发与采用 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (recommended) or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把人际深度解析做成可发现、易试用、可安装、易分享且边界清楚的跨宿主 Skill 仓库。

**Architecture:** 唯一运行时 Skill 移到 `skills/person-deep-analysis/`；仓库根 README、贡献指南、评估、CI、校验器与传播素材独立于安装单元。用 Skills CLI 做发现 smoke test，用结构校验和人工前测分别覆盖包结构与行为边界。

**Tech Stack:** Agent Skills Markdown/YAML、Skills CLI、Python 3.9 标准库、GitHub Actions YAML。

**Spec:** `docs/superpowers/specs/2026-09-24-distribution-and-adoption.md`

## Global Constraints

- 用户已授权直接执行计划与自验，不在任务间暂停询问。
- 首要用户为中文 Agent Skills 使用者，同时提供英文发现入口。
- 不声称临床、实证或预测效度；不使用真实个人私密材料作宣传。
- 不新建 GitHub 远端、不发帖、不联系他人。用户已选择 MIT；使用本机配置的 Git 作者名 `Liyuk` 作为许可证版权署名。
- 工作目录没有 Git 元数据；在当前工作区修改，不提交、不推送。
- 跨宿主命令依官方 Skills CLI 当前文档编写，保留用户可本地执行的方式。

## Review Focus

- `skills/person-deep-analysis` 目录与 frontmatter 的 `name` 是否一致，依赖引用是否仍然相对 skill 根目录。
- Skills CLI 本地发现是否只枚举单个 skill，仓库外层的 `SKILL.md` 或文档是否造成误发现。
- README 的安装命令是否把仓库发现与实际 skill 名称对应起来，且不出现虚构 GitHub 地址。
- 单段冲突、单方材料、诊断诉求和即时危险的预期行为是否一致。
- CI/校验器是否检查真正的 skill 子目录，而不是错误读取仓库根目录。
- 宣传文案是否夸大“读心/预测/诊断”能力或暴露私密素材。

---

### Task 1: 分离可安装 Skill 与仓库级内容

**Files:**
- Move: `SKILL.md` → `skills/person-deep-analysis/SKILL.md`
- Move: `agents/openai.yaml` → `skills/person-deep-analysis/agents/openai.yaml`
- Move: `modules/` → `skills/person-deep-analysis/modules/`
- Move: `dlc/` → `skills/person-deep-analysis/dlc/`
- Move: `references/` → `skills/person-deep-analysis/references/`
- Modify: `scripts/validate_skill.py`
- Modify: `README.md`

- [x] 创建 `skills/person-deep-analysis/` 并迁移运行时目录，不迁移仓库级 `evals/`、`docs/`、`scripts/`。
- [x] 检查 skill 内所有引用仍以 skill 根目录为基准；从 skill 入口移除仓库级 `evals/` 与 `docs/` 路径介绍。
- [x] 修改校验器，使其明确校验 `skills/person-deep-analysis/`，检查目录名与 frontmatter `name` 一致。
- [x] 更新根 README 的目录索引与手工安装路径。

### Task 2: 重写定位与首次使用入口

**Files:**
- Modify: `README.md`
- Create: `README_EN.md`
- Create: `CONTRIBUTING.md`
- Create: `LICENSE` (MIT; copyright line uses configured Git author name)
- Modify: `skills/person-deep-analysis/SKILL.md`
- Modify: `skills/person-deep-analysis/agents/openai.yaml`

- [x] 中文 README 首屏加入差异化一句话、适用/不适用场景、快速上手、CLI 安装与本地发现命令。
- [x] 加入与 `goutoujunshi`、聊天档案分析和多框架伴侣咨询的定位对照，强调本项目的证据结构与信息量自适应。
- [x] 加入不超过 15 行的合成输入/输出演示，示范“观察—假设—替代解释—未知”。
- [x] 新增英文入口 README，准确标示主要分析内容为中文，保留英文检索关键词和安装说明。
- [x] 优化 SKILL description 与 OpenAI metadata 的中英文关键词，让触发场景清楚但不宣称诊断/预测。
- [x] 写 CONTRIBUTING 指南：贡献模块、案例、翻译的流程；案例必须合成/匿名且满足评估边界。
- [x] 按用户指定 MIT 授权加入 LICENSE；版权声明使用本机已配置 Git 作者名 `Liyuk`。

### Task 3: 构建回归评估与仓库 CI

**Files:**
- Modify: `scripts/validate_skill.py`
- Modify: `evals/README.md`
- Modify: `evals/behavior-regression.md`
- Create: `evals/scenarios.json`
- Create: `scripts/validate_evals.py`
- Create: `.github/workflows/validate.yml`

- [x] 校验器检查 skill 主文件、必需模块/reference、frontmatter 名称和仓库相对 Markdown 链接。
- [x] 把七条关键行为场景整理成机器可读的输入与预期/禁止行为，并链接到人工复核报告：低信息、矛盾线索、单段互动、单方叙述、诊断请求、即时安全风险、英文语言保持。
- [x] 添加场景数据校验器，并纳入 CI。
- [x] 添加 GitHub Actions workflow，在 pull request 和主分支 push 时运行结构校验和单 skill 发现断言。
- [x] 在评估文档说明结构检查、手工行为前测和宿主真实运行测试的区别，不把静态检查称为模型表现证明。

### Task 4: 编写安全、可复用的传播套件

**Files:**
- Create: `docs/launch/README.md`
- Create: `docs/launch/content-kit.md`
- Modify: `README.md`
- Modify: `docs/research/github-comparable-projects.md`

- [x] 写 30 天轻量分发顺序：仓库可安装性 → skills.sh/Skills CLI → 中文 AI 社区演示 → 收集反馈 → 复盘。
- [x] 给出衡量指标：发现/安装转化、完成一次分析的比例、用户认为有用的部分、越界或误导反馈。
- [x] 提供至少三条可复制的演示内容方向/分享文案，所有人物与文本均标为合成示例。
- [x] 加入禁止公开真实聊天、照片、账号或可识别信息的传播边界。
- [x] 把生态文档对 root-level SKILL 与 `skills/<name>/SKILL.md` 的发现/安装经验记入 research，给出本仓库选此布局的理由。

### Task 5: 端到端自验并修复

**Files:**
- Modify: `evals/behavior-regression.md`
- Modify: `docs/superpowers/plans/2026-09-24-distribution-and-adoption.md`

- [x] 用 Python 结构校验器检查最终仓库。
- [x] 用回归场景校验器检查七类、唯一 ID、输入及报告锚点。
- [x] 用 Ruby YAML parser 解析 SKILL frontmatter 与 `agents/openai.yaml`。
- [x] 用固定版本 Skills CLI 本地发现 smoke test 确认只发现 `person-deep-analysis`，并在临时目录验证 Codex 与 Claude Code 目标安装和文件完整性。
- [x] 按回归场景人工复核规则并记录既有前测结果及本轮限制。
- [x] 静态复核中英文入口、路径、命令、定位差异与安全声明；修复无效许可证链接。
- [x] 更新本计划实际执行状态；GitHub 远端仍待项目所有者创建；当前目录没有 Git 元数据。
