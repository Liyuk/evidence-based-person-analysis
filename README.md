# 人际深度解析 · Person Deep Analysis

**不替你猜心，帮你把材料拆成证据、假设和未知。**

一个遵循 Agent Skills 格式的文本分析 skill：帮助你分析自述、个人介绍、选取的聊天片段、互动和虚构角色文本，区分材料事实、有限解释与未知。长聊天先限定议题或时间范围，只取必要片段；不要求导入完整档案。虚构角色分析只讨论作品如何呈现角色，不由角色推断作者心理。主要面向中文材料；不用于给现实人物下诊断、预测关系结局或替你做决定。

[English overview](README_EN.md) · [相似项目与差异研究](docs/research/github-comparable-projects.md) · [多视角心理学依据](docs/research/multilens-psychology-evidence.md) · [反诈/主体性支持依据](docs/research/fraud-and-coercive-control-guidance.md) · [多视角用途评审](docs/research/multilens-design-review.md) · [Blog 项目模块](docs/launch/blog-project-module.md) · [回归场景](evals/scenarios.json) · [贡献指南](CONTRIBUTING.md) · [MIT License](LICENSE)

## 60 秒上手

### 安装到 Codex 或其他支持的 Agent

本仓库已公开发布。用 Skills CLI 安装到目标宿主：

```sh
# Codex
npx skills add Liyuk/evidence-based-person-analysis --skill person-deep-analysis -g -a codex -y

# Claude Code
npx skills add Liyuk/evidence-based-person-analysis --skill person-deep-analysis -g -a claude-code -y
```

Skills CLI 支持从仓库选择 skill 和指定宿主；具体选项可见 [CLI 文档](https://github.com/vercel-labs/skills)。CI 从本仓库根目录在临时目录验证了两种目标的安装路径、运行时文件完整性和仓库文档隔离。Codex CLI 显式调用与一次项目级隐式触发见[行为验证报告](evals/results/2026-09-24-codex-cli-runtime-smoke.md)；聊天/虚构角色分析见[范围扩展试跑](evals/results/2026-09-25-scope-expansion-smoke.md)；三例 Skill/普通提示对照和单模型盲化评分见[A/B 试跑](evals/results/2026-09-24-network-example-ab-pilot.md)；反诈/主体性专项复测见[专项结果](evals/results/2026-09-24-fraud-agency-forward-test.md)。这些小样本试跑用于发现规则缺口，不证明稳定效果或心理学效度；尚未验证桌面版自动加载、跨模型一致性或真实用户收益。若想在本地检查发现结果，可从克隆后的仓库根目录运行：

`npx skills` 是安装器 CLI，skill 本身直接从 GitHub 仓库安装，不需要单独发布 npm 包。只有未来提供可复用的 JavaScript 库或命令行工具时，才考虑 npm 发布。

```sh
npx --yes skills add . --list
```

手动安装到 Codex：

```sh
mkdir -p ~/.codex/skills
cp -R ./skills/person-deep-analysis ~/.codex/skills/
```

Claude Code 手动安装时，使用其个人技能目录：

```sh
mkdir -p ~/.claude/skills
cp -R ./skills/person-deep-analysis ~/.claude/skills/
```

### 使用

```text
用 $person-deep-analysis 看这段自我介绍。请区分原话、观察和解释，给主要判断列出依据、替代解释与未知；不要诊断，材料不够就收敛。
```

也可以分析聊天摘录或虚构角色：

```text
按时间顺序分析下面三段工作聊天。区分原话、行为和解释；判断这些消息属于几次独立事件，不要把一次交接概括成稳定人格。指出还缺什么，并提醒我哪些隐私应先删掉。
```

```text
分析小说中角色在三个关键场景里的选择和变化。请引用情节，区分文本事实、角色解释和叙事功能；不要诊断角色或推断作者经历。
```

要比较解释而非只做简析，可再说：

```text
请进入多视角 Steelman 模式。只使用材料支持的心理学视角，分别列出依据、额外假设、最强合理替代解释和未知；不适用的流派说明原因，保留冲突，不要强行合成结论。
```

仓库维护者可运行 `python3 scripts/validate_skill.py` 检查文件结构、YAML frontmatter 和本地 Markdown 链接，并运行 `python3 scripts/validate_evals.py` 检查可复用行为场景。安装前也可浏览 `skills/person-deep-analysis/SKILL.md`。

## 它和相似项目有什么不同？

| 项目取向 | 常见交付 | 本项目的边界 |
|---|---|---|
| [goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi) | 关系困境支持、权衡和行动建议 | 不默认给关系推进或退出方案 |
| [Analyze Romantic Relationships](https://github.com/jeejohn/analyze-romantic-relationships) | 关系叙述、聊天和时间线的证据判断与决策支持 | 不以双方关系裁决为默认交付 |
| [Person Behavior Analysis](https://github.com/wangguofeng728/person-behavior-analysis-skill) | 长期聊天档案、跨时段模式、相似事件检索与情境推演 | 不要求导入长期档案；聚焦当前有限材料 |
| 本项目 | 当前提供的自述、短聊天、互动或虚构角色文本 | 可选反诈/胁迫支持；以行为证据和当事人选择为中心，不诊断或画像犯罪风险 |

“证据优先”“保留未知”和“提供替代解释”并非本项目独有。本项目默认分析用户当前选取的现实人物材料（自述、聊天摘录、互动片段），也支持基于作品文本分析虚构角色；不要求长期聊天档案，也不默认给关系决策建议。它回答材料支持什么、还缺什么，虚构角色解释则限定在文本如何塑造角色。这个定位来自对八个公开仓库的有限样本比较，不代表全生态唯一。用户明确要求时，才用心理动力学、人本/需求、发展和描述性 CBT 等镜头组织问题；法证/犯罪心理只提供证据边界，不作犯罪或危险性预测。更多来源见[比较研究](docs/research/github-comparable-projects.md)和[心理学依据](docs/research/multilens-psychology-evidence.md)。

## 合成示例

> 输入（合成）： “我喜欢独处，但希望伴侣每天联系；忙的时候我会晚些回复。”
>
> **观察：** 同时表达独处偏好、日常联系期待和延迟回复情境。  
> **候选解释：** 个人空间与稳定联系可能对她同样重要。  
> **替代解释：** “每天联系”可能只指简短问候，具体期待尚不清楚。  
> **未知：** 需要了解双方对频率、忙碌时告知方式的定义；不能据此判断依恋类型。

此示例为虚构文本，不代表真实用户或实证结论。

## 适合与不适合的用途

- **适合**：梳理自我介绍和选取的聊天片段；比较多个独立互动场景；分析小说、影视、游戏等作品如何呈现角色及其变化。
- **适合**：整理疑似网恋/投资诈骗或关系控制中的可观察信号，了解可选择的安全与求助步骤；支持当事人恢复自己的判断和选择空间。
- **不适合**：诊断心理障碍、推断创伤或隐私属性、证明某人“是什么样的人”、判断关系必然走向，或处理即时危险。

## 边界与隐私

不诊断、不编造创伤经历、不从孤立信号推断稳定人格或隐私属性。NPD、PUA、杀猪盘等词不能替代对具体行为的核对；遇到疑似诈骗/操控时，Skill 帮助识别行为风险并提供选择式支持，不保证识别身份或追回资金，也不代替专业反诈/危机服务。它拒绝生成操控、欺诈或规避反诈识别的策略。单段互动只描述该次往返；单方叙述不能确认缺席者的人格。分析第三方材料前，尽量移除识别信息；不要提交私密材料作公开案例。Skill 不能控制宿主如何保存或处理输入。遇到迫近的人身危险，优先处理现实安全需求。

## 项目结构

```text
skills/person-deep-analysis/   可安装 skill 本体（入口、模块、参考和宿主元数据）
evals/                         行为回归场景、人工复核和待执行的对照验证方案
scripts/                       结构校验器
.github/workflows/             持续集成
CONTRIBUTING.md                贡献和案例隐私规则
docs/research/                 生态对照与心理学适用边界研究
docs/launch/                   面向发布的介绍与分享素材
docs/superpowers/              规格与执行计划
```

## 参与与授权

欢迎提交问题、改进建议、合成评估案例和翻译。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。项目采用 MIT License，版权声明见 [LICENSE](LICENSE)。
