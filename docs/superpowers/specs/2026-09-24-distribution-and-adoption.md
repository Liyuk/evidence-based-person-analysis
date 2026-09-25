# 人际深度解析：分发与采用规格

## 目标

让不熟悉作者和方法的用户能快速发现、理解、试用、安装和分享 `person-deep-analysis`，同时保留证据约束与非诊断边界。主要受众是中文 Agent Skills 用户；英语入口服务于跨宿主搜索与传播。

## 当前定位与差异

- 与 `goutoujunshi` 区分：后者偏关系困境支持与行动建议；本项目聚焦从用户提供的有限材料中整理个人呈现、明确偏好和可见互动，不替用户决策。
- 与聊天档案/情侣咨询工具区分：本项目不抓取、不保存、不建立人物档案，不把关系建议作为默认交付。
- 独特工作流：信息量自适应、观察与假设分开、替代解释、材料不足时收敛；M1–M5 单人主线，关系与叙事分析可选。
- 使用承诺：只承诺结构化、可追溯的材料分析，不承诺揭示真实内心或预测关系结果。

## 设计决定

### 分发结构

将可安装单元移至 `skills/person-deep-analysis/`，仓库根目录只放仓库入口、评估、校验、贡献指南、传播材料和文档。这样 Skills CLI 可按标准 `--skill person-deep-analysis` 发现并只分发 skill 本体，避免把研究文档、评估案例和仓库工具混进用户的运行时 skill。

### 新手入口

- 中文 README 首屏说明适用问题、差异点、边界、即刻试用和 CLI 安装。
- 增加简洁英文入口，说明 skill 主要以中文工作、支持的宿主及一条使用示例。
- 对尚无 GitHub owner/repo 的情况，将远端命令清晰标为发布后模板；提供可立即运行的本地目录发现命令。

### 评估与维护

- 仓库校验覆盖 skill 文件、frontmatter 名称与目录一致、相对 Markdown 链接、主入口和元数据存在。
- CI 运行仓库校验、Skills CLI 1.7.0 本地发现及隔离 Codex/Claude Code 目标安装；固定 CLI 版本并设置超时。不把格式/安装检查当作模型行为证明。
- 回归场景覆盖低信息、矛盾线索、单段剪辑、单方叙述、诊断请求、即时安全风险及英文输入的语言保持。

### 传播素材

- 写清一条记忆点：“不替你猜心，帮你把材料拆成证据、假设和未知”。
- 提供经过匿名/合成的短 demo 和可复制的分享文案；禁止把用户真实私密聊天包装成营销案例。
- 分发先后：Skills CLI 可安装仓库与 skills.sh 页面 → 中文 AI/效率社区演示 → 收集匿名反馈和评估样例 → 根据使用反馈迭代。
- 不承诺“出圈”或心理准确率；以可用性、安装转化、有效反馈和风险问题为衡量项。

## 目录目标

```text
.
├── README.md
├── README_EN.md
├── CONTRIBUTING.md
├── skills/
│   └── person-deep-analysis/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── modules/
│       ├── dlc/
│       └── references/
├── evals/                     # 仓库级样例，不随运行时 skill 安装
├── scripts/validate_skill.py  # 仓库结构检查
├── .github/workflows/         # CI 发现与结构校验
└── docs/
    ├── launch/                # 定位与传播资料
    ├── research/              # GitHub 与生态对照
    └── superpowers/           # 规格与执行计划
```

## 范围

包括目录重组、中英 README、定位对照、贡献方式、回归矩阵、CI、本地 Skills CLI smoke test 和传播素材。MIT 已由用户选定并写入许可证，采用本机 Git 作者名 `Liyuk` 作版权声明；不包括创建/发布 GitHub 远端、购买域名、发帖/联系社区或对外承诺心理学效度。

## 验收标准

1. Skills CLI 从仓库根目录枚举出且只枚举 `person-deep-analysis` 一个 skill。
2. 仓库安装指引分别覆盖本地试用与远端发布后的安装；命令准确且不伪造 owner/repo。
3. 根 README 和英文 README 可让第一次看到项目的人在一分钟内理解用途、差异、边界和使用方式。
4. 传播素材提供至少三种可直接采用的内容模板，并使用合成材料。
5. 自动校验及 CI 能检查仓库/skill 结构；CLI 只发现一个 skill，临时项目安装能复制到 Codex 与 Claude Code 目标目录；回归清单覆盖重点行为边界。
6. 结构、YAML 和 Skills CLI smoke tests 全部通过；发现问题后修复并重跑。
7. 按用户选择加入 MIT 许可证；使用本机 Git 作者名 `Liyuk` 作版权署名，并在发布清单中标明远端仓库仍待创建。

## 参考资料

- Skills CLI README: https://github.com/vercel-labs/skills/blob/main/README.md
- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- skills-ref: https://github.com/agentskills/agentskills/tree/main/skills-ref
- Existing comparison: `docs/research/github-comparable-projects.md`
