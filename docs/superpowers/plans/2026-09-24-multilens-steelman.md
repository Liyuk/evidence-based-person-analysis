# 多视角 Steelman 报告实施计划

> 按任务顺序实施；每项完成后运行对应校验。仓库当前没有 Git 元数据，不创建提交或远端。

**目标：** 在 `person-deep-analysis` 加入用户显式触发的多心理学视角 Steelman 报告，扩展行为评估，提供可直接用于 blog 的项目模块，并如实验证边界。

**结构：** 证据记录为所有报告的共同底座；多视角深度报告在明确请求时触发；各理论和 Steelman 规则拆入 `references/perspectives/`，按需加载；行为用例保存在仓库级 evals，不进入安装包。

**规格：** `docs/superpowers/specs/2026-09-24-multilens-steelman-design.md`

## 文件职责

- 修改 `skills/person-deep-analysis/SKILL.md` 与 `agents/openai.yaml`：触发词、步骤、路由、输出原则。
- 新建 `skills/person-deep-analysis/references/perspectives/*.md`：五种理论镜头和报告规则，载明来源与局限。
- 移动 M1/M3/M5 文件并更新 `scripts/validate_skill.py`：对齐中性命名与路径。
- 修改 `evals/scenarios.json`、`evals/behavior-regression.md`、`scripts/validate_evals.py`、`evals/README.md`：增加机器可读边界用例并记录手工走查。
- 新建 `docs/launch/blog-project-module.md`，更新 README 与 `docs/launch/README.md`：让用户找到 blog 内容和验证状态。

## Task 1：调整运行时结构和入口路由

- [x] 将 M1、M3、M5 重命名为 `m1-needs-and-preferences.md`、`m3-experience-and-development.md`、`m5-interaction-patterns.md`，同步标题/正文/所有路径引用。
- [x] 新建 `references/perspectives/` 中五种镜头与 Steelman 报告说明；引用研究底稿中的原始/专业来源。
- [x] 更新 `SKILL.md`：普通分析保持简洁；用户明确要求多视角/Steelman 时才读取报告规则和适用镜头；并列候选解释，保留冲突，不强造解释、不打理论分。
- [x] 更新 OpenAI 默认提示及描述，使用户能显式请求“多视角 Steelman 报告”。
- [x] 在模块正文中清理“人格类型”或“预测”暗示，同时保留明确有效的材料边界。

**完成条件：** 所有引用可解析，旧文件路径不再出现；普通模式和多视角模式路由清楚，危险线索仍先进入安全流程。

## Task 2：扩充行为评估集

- [x] 增加至少 8 个专项场景：全流派硬套、心理动力/童年倒推、发展因果误判、Maslow 固定阶梯、自述 CBT 映射、犯罪预测请求、Steelman 虚假平衡、流派解释冲突、反例更新；合理合并时确保覆盖全项。
- [x] 每项定义正向行为和禁止行为；不能只以出现术语作为通过标准。
- [x] 更新 eval 校验器，要求新类别全部覆盖但允许将来继续增加场景。
- [x] 更新行为报告索引与限制说明，新增场景先记录静态走查结果，再标清未进行的宿主实测。

**完成条件：** JSON 解析，ID 唯一，所有必需类别与报告锚点同步；没有把文档走查标成宿主运行或理论效度证据。

## Task 3：写 blog 项目模块

- [x] 创建一份可独立复制使用的中文项目介绍，含一句话定位、用户痛点、工作流程、多视角差异、合成示例、边界、如何试用/贡献和当前验证状态。
- [x] 合成示例中所有视角围绕同一组事实，展示共识与冲突；只提供证据支持的解释，并说明视角不适用时可省略。
- [x] 更新中文 README、发布计划，将 blog 模块纳入导航。

**完成条件：** 文案可离开本次对话独立阅读，任何“证据”或“效果”说法都有可追溯来源或明确标为项目设计目标；案例明确为合成。

## Task 4：验收和修复

- [x] 运行 `python3 scripts/validate_skill.py`、`python3 scripts/validate_evals.py`；18 个用例/类别通过。另以删去场景标题的临时负例确认评测校验器会失败。
- [x] 运行 skill-creator `quick_validate.py` 与 Ruby YAML parser；创建临时依赖目录提供 PyYAML，检查后不向仓库或全局 Python 环境写依赖。
- [x] 运行 Skills CLI discovery 与隔离 Codex/Claude Code install checks，确认仅发现唯一 skill、perspective references 完整随包安装且仓库级 blog/eval 内容未混入安装包。
- [x] 按新增场景逐项做指令级静态走查，必要时生成代表性报告并评审其证据引用、Steelman、公平但不虚假平衡和安全边界。
- [x] 检查中英 README、模块标题、技能元数据、研究引用和 blog 项目模块的一致性；已修复前测发现的非必要留证建议。
- [x] 记录验收结果、未执行的目标宿主端行为验证和小规模用户对照研究限制。

**完成条件：** 所有自动检查通过；所有新增行为用例有可审计预期和复核记录；未验证内容明确保持“待验证”。
