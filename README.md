# 互动风险识别与解构

**看清诈骗、操控、虐待与霸凌中的互动风险；依据行为解构，不替人定性。**

这是一个面向普通人的 Agent Skill。它帮助你分析可疑互动、网恋诈骗、情绪操控、胁迫、情感虐待和人际霸凌：分清原话、行为、事件顺序、重复模式、行为效果、可能目的、反证和未知，再给可独立核验的选择。不诊断人格，也不替你裁定谁是“坏人”。模型本身已有模式识别能力；Skill 提供一套提示方法，让判断更有结构、可检查和修正，不把熟悉的标签直接当答案。

[English](README_EN.md) · [八种场景的实际对照演示](docs/demos/README.md) · [相邻项目研究](docs/research/interaction-risk-skills-landscape.md) · [验收场景](evals/interaction-risk-cases.json) · [行为验收标准](evals/interaction-risk-acceptance.md) · [博客项目介绍](docs/launch/blog-project-module.md) · [MIT License](LICENSE)

## 安装

本仓库只有一个可安装 Skill：`interaction-risk-analysis`（互动风险识别与解构）。

安装到 Codex：

```sh
npx skills add Liyuk/interaction-risk-analysis --skill interaction-risk-analysis -g -a codex -y
```

安装到 Claude Code：

```sh
npx skills add Liyuk/interaction-risk-analysis --skill interaction-risk-analysis -g -a claude-code -y
```

## 它怎样拆解问题

例如，一位网恋对象先转到其他平台，之后提出投资；当你要求核实公司时，对方反问“你信不信我”，最后催你当晚转账并保密。Skill 会按时间还原事件，把身份主张和已核实事实分开，解释转移渠道、限制核验、保密和催款如何组成风险链；同时列出仍不知道什么、什么独立证据会改变判断，以及可以先采取的步骤。

使用时可以直接描述经历，也可以把这段分析方法带进提示词：

```text
$interaction-risk-analysis
请按这套方法解构这些互动：按时间拆事件，分清原话、事实主张、可观察行为和推断；分析行为产生的实际效果，以及可能的因果、立场或目的，并给出依据、反证、合理替代解释和未知。区分“之后发生”与“因此导致”、效果与意图；说明哪些新证据会改变判断，再给可选回应。不要先套熟悉标签，也不要替我下结论。
```

## 分析方法

复杂场景按以下顺序处理：

1. 标明材料来源、说话人、时间范围和上下文缺口。
2. 拆成“发生了什么 → 对方如何回应 → 后来发生什么 → 有何影响”的事件单元。
3. 区分单一线索、同一事件的连续升级和跨事件重复模式。
4. 检查行为实际改变了什么，再提出可能的立场或目的；把效果、动机和因果关系分开，列出依据、反证、合理替代解释与未知。
5. 指出什么信息能区分这些解释，并独立核验身份、平台、交易或承诺。
6. 先处理迫近的资金、账户和人身风险；应对方式由用户选择。

这不是让模型关闭已有判断能力，而是让它把识别到的线索摊开说明，避免直接跳到“这是某种套路”的结论。实际运行中，普通模型本身也可能答得很好；项目主张的是一套可复用的分析纪律，不是 Skill 独有的检测能力。

这套方法沿用项目早期 `person-analysis` 工作中的人物与互动解构经验，并纳入反诈、安全、霸凌和可选心理学视角。重点是让用户看见线索怎样通向假设，再自行核对和决定；Skill 不声称拥有普通模型没有的“识人”能力。

## 适用范围

- 网恋/投资诈骗、杀猪盘、刷单与兼职骗局、传销/资金盘、冒充权威、凭证索取和追回资金二次诈骗。
- 情绪勒索、胁迫、隔离控制、监控、反复否认现实及越界后的惩罚。
- 职场、学校、群聊和社交网络中的重复羞辱、排斥、造谣、报复和权力滥用。
- 有限的人物自述、关系互动、聊天片段或虚构角色分析；明确区分证据与理论解释。
- 误报对照：单次记忆分歧、正常反馈或一次疏忽不足以单独证明操控、诈骗或霸凌。

## 边界

这不是自动检测器、心理诊断、法律裁决、侦查、银行风控或资金追回服务。不保证发现所有风险。只凭聊天通常不能确认身份、犯罪事实或隐藏动机。心理学视角只能帮助提出有限解释，不能诊断或预测危险。遇到急迫危险，先处理现实安全；提供地区性热线或法律步骤前需要核对当地官方来源。不要提交不必要的姓名、账号、联系方式或完整私聊；Skill 不能控制宿主如何处理输入。

## 场景与验收

仓库维护 20 个合成验收场景，检查事件解构、因果/目的推断、误报控制、反证更新、安全步骤和用户主体性。另有八个按四类平衡的合成演示，保留更名前以 `$person-analysis` 运行的普通 Codex / Skill 对照输出；这些是旧 Skill ID 下的历史结果，不是新 ID 的重复试跑。[场景演示](docs/demos/README.md)、[历次宿主验收记录](evals/results/2026-09-25-person-analysis-anti-fraud-acceptance.md)和[解构方法试跑](evals/results/2026-09-25-decomposition-method-evaluation.md)都注明测试条件和结论边界。

可运行仓库检查：

```sh
python3 scripts/validate_skill.py
python3 scripts/validate_evals.py
python3 scripts/validate_safety_evals.py
python3 scripts/validate_interaction_risk_evals.py
python3 scripts/check_skill_discovery.py
python3 scripts/check_skill_installation.py
```

## 目录结构

```text
skills/interaction-risk-analysis/          唯一可安装 Skill
  modules/                                  旧版 M1–M5 人物分析模块
  dlc/                                      按需关系、叙事与虚构角色分析
  references/                               解构、反诈、反操控、安全和理论参考
evals/interaction-risk-cases.json          当前验收案例
evals/results/                              宿主运行与历史评估记录
archive/person-deep-analysis/                旧版原始包，保留追溯
docs/                                       竞品研究、方法依据和项目说明
scripts/                                    结构、场景、发现及安装检查
```

许可证：MIT。GitHub 仓库与 Skill ID 均为 `interaction-risk-analysis`；GitHub 对原仓库地址保留跳转。
