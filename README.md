# 人际深度解析 · Person Deep Analysis

**不替你猜心，帮你把材料拆成证据、假设和未知。**

一个遵循 Agent Skills 格式的文本分析 skill：帮助你看清自述、个人介绍或少量互动材料明确表达了什么、有哪些有限的解释、还缺什么信息。它适合梳理材料，不用于给人定型、预测关系结局或替你做决定。主要面向中文材料；不做诊断。

[English overview](README_EN.md) · [相似项目与差异研究](docs/research/github-comparable-projects.md) · [多视角心理学依据](docs/research/multilens-psychology-evidence.md) · [多视角用途评审](docs/research/multilens-design-review.md) · [Blog 项目模块](docs/launch/blog-project-module.md) · [回归场景](evals/scenarios.json) · [贡献指南](CONTRIBUTING.md) · [MIT License](LICENSE)

## 60 秒上手

### 安装到 Codex 或其他支持的 Agent

发布到 GitHub 后，用 Skills CLI 选择目标宿主安装（把占位符换成真实仓库）：

```sh
# Codex
npx skills add <OWNER>/<REPO> --skill person-deep-analysis -g -a codex -y

# Claude Code
npx skills add <OWNER>/<REPO> --skill person-deep-analysis -g -a claude-code -y
```

Skills CLI 支持从仓库选择 skill 和指定宿主；具体选项可见 [CLI 文档](https://github.com/vercel-labs/skills)。上面的远端示例选择 Codex；若要安装到 Claude Code，将 `codex` 替换为 `claude-code`。CI 已从本仓库根目录在临时目录验证两种目标的安装路径、运行时文件完整性和仓库文档隔离；没有验证这两个宿主中的实际自动加载或模型行为。仓库尚未发布时，可先在本地检查发现结果：

```sh
npx --yes skills add . --list
```

然后从仓库根目录手动安装到 Codex：

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

要比较解释而非只做简析，可再说：

```text
请进入多视角 Steelman 模式。只使用材料支持的心理学视角，分别列出依据、额外假设、最强合理替代解释和未知；不适用的流派说明原因，保留冲突，不要强行合成结论。
```

仓库维护者可运行 `python3 scripts/validate_skill.py` 检查文件结构、YAML frontmatter 和本地 Markdown 链接，并运行 `python3 scripts/validate_evals.py` 检查可复用行为场景。安装前也可浏览 `skills/person-deep-analysis/SKILL.md`。

## 它和相似项目有什么不同？

| 项目取向 | 常见交付 | 本项目的边界 |
|---|---|---|
| [goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi) | 关系困境支持、权衡和行动建议 | 先做单人材料分析，不替用户决定关系方案 |
| 本次比较的聊天档案/关系分析工具 | 从聊天和多轮互动归纳双方模式 | 以用户当前提供的材料为入口，不要求导入或长期保存档案 |
| 本次比较的伴侣咨询/冲突处理框架 | 双方沟通、修复和干预建议 | 关系互动只是可选扩展，主线是理解用户提供的单人材料 |
| 本项目 | 观察 → 候选解释 → 依据 → 替代解释 → 未知 | 信息量自适应；不把框架标签当成事实 |

在本次比较的项目中，这套工作流的定位差异是：8 条启发式用于组织核实问题，M1–M5 按需分析需求、自我呈现、本人报告的经验、优势成本与互动；用户明确要求时，可用心理动力学、人本/需求、发展、CBT 等有限镜头并列解释与未知。法证/犯罪心理只提供证据纪律，不做犯罪或危险性预测。启发式未经本仓库验证为因果规律，多流派输出也不代表心理效度。更多来源见[比较研究](docs/research/github-comparable-projects.md)和[心理学依据](docs/research/multilens-psychology-evidence.md)。

## 合成示例

> 输入（合成）： “我喜欢独处，但希望伴侣每天联系；忙的时候我会晚些回复。”
>
> **观察：** 同时表达独处偏好、日常联系期待和延迟回复情境。  
> **候选解释：** 个人空间与稳定联系可能对她同样重要。  
> **替代解释：** “每天联系”可能只指简短问候，具体期待尚不清楚。  
> **未知：** 需要了解双方对频率、忙碌时告知方式的定义；不能据此判断依恋类型。

此示例为虚构文本，不代表真实用户或实证结论。

## 适合与不适合的用途

- **适合**：梳理一段自我介绍表达的偏好；区分一次互动中的原话、行为和解释；找出还需要核实的问题。
- **不适合**：诊断心理障碍、推断创伤或隐私属性、证明某人“是什么样的人”、判断关系必然走向，或处理即时危险。

## 边界与隐私

不诊断、不编造创伤经历、不从孤立信号推断稳定人格或隐私属性。单段互动只描述该次往返；单方叙述不能确认缺席者的人格。分析第三方材料前，尽量移除姓名、账号和位置等识别信息；不要把私密材料提交为公开案例。Skill 本身不能控制宿主如何保存或处理输入，使用者应遵循所用平台的数据设置。遇到自伤、暴力、胁迫或跟踪线索，优先处理现实安全需求。

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
