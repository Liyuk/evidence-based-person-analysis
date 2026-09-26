# 双 Skill 保留与项目文案清理设计

## 目标

将仓库整理为两个可独立安装的 Agent Skill，同时让公开入口只介绍当前可用能力，不再把改名过程、旧仓库迁移、历史运行状态或 GitHub 项目背景写给普通使用者。

## Skill 结构

```text
skills/
├── interaction-risk-analysis/   互动风险识别与解构
└── person-deep-analysis/         人际深度解析
```

- `interaction-risk-analysis` 保持当前内容和定位，处理诈骗、操控、胁迫、虐待与霸凌等互动风险。
- `person-deep-analysis` 从现有原始人物分析包恢复为正式安装入口，保留人物自述、聊天片段、关系互动和虚构角色分析能力。
- 两个 Skill 共享仓库级评估与校验，但运行时目录相互独立，安装任一 Skill 时不带入另一个 Skill。
- `person-deep-analysis` 的 frontmatter、元数据和默认调用示例统一使用 `person-deep-analysis`。

## 文案清理范围

- 根目录 README、中英文发布说明、贡献指南和 `docs/launch/`：删除旧名称、改名过程、历史运行状态、旧仓库跳转和面向 GitHub 浏览者的解释；保留安装命令、当前能力、边界、示例入口和校验方式。
- `evals/`、`docs/research/`、`docs/superpowers/`、`archive/`：保留作为内部评估、研究和追溯资料，但将仍指向已不存在目录的链接改为现行路径。
- 不删除合成案例、评估结果或研究依据；历史事实只在确实需要解释测试条件时保留，不出现在普通用户入口。

## 校验与 CI

- 结构校验要求恰好发现 `interaction-risk-analysis` 和 `person-deep-analysis` 两个 Skill。
- 发现校验确认 Skills CLI 列出且仅列出这两个名称。
- 安装校验分别把两个 Skill 安装到 Codex 和 Claude Code 临时目录，检查各自运行时文件完整，并确认仓库级 `docs/`、`evals/`、`scripts/` 未泄漏。
- 运行现有全部 Python 校验和双 Skill 的发现/安装检查。

## 不在本次范围

- 不更改 Skill 的分析方法、安全边界或评估标准。
- 不删除研究、评估和归档文件。
- 不创建、修改或发布 GitHub 远端仓库。
