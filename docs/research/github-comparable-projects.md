# GitHub 相似项目对照：人物与关系分析 Skill

调研日期：2026-09-24（本轮复核）
范围：查看八个 GitHub 仓库的公开 README、Skill 文件和可见项目结构；这里只据仓库公开材料描述其设计，不把项目自述等同于心理学有效性或实际效果证明。新增项目以 README 与运行时 Skill 为一手来源；对无法独立核实的性能或效果不作判断。

本文件记录有限样本的仓库公开材料对照；结论只适用于本次选定的八个项目，不推断整个生态的分布。仓库内容会变化，结论应视为本次查阅时的快照。

## 摘要

本项目 `person-deep-analysis` 的核心是帮助用户理解**所提供材料明确表达了什么、哪些有限解释可能成立、还缺什么信息**。8 条启发式用于组织核实问题，M1–M5 按需分析；DLC 扩展到关系互动和叙事呈现。在本次八个样本中，最清楚的定位差异是：本项目把单人简介、自述和有限互动材料的证据边界作为默认入口，而若干相近项目进一步面向伴侣关系判断、长期聊天档案、行动建议或行为推演。各项目仍在证据区分、替代解释和安全边界等方面存在明显重叠；这只是样本内的用途侧重比较，不代表全生态唯一或总体分布。

调研当时，项目已有清楚的模块划分、证据引用要求和两个案例，但推断边界及仓库入口仍需加强。下文保留当时的对照观察；文末另记后来落地的调整，避免把历史建议误读为当前缺项。

## 可比项目

### 1. goutoujunshi：关系决策顾问型 Skill

[项目英文 README](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/README_EN.md) 描述了一个围绕用户当前关系困境提供支持和决策建议的 Skill。其流程包括情绪承接、建立多方画像、区分事实/推断/未知、按需检索知识、衡量互惠和机会成本，最终给出建议、话术、观察期和停止条件。它允许用户用自然叙述输入，并只追问可能改变建议的关键信息。

结构上，仓库把入口 `SKILL.md`、Codex 元数据 `agents/openai.yaml`、知识与实践参考文档、架构/安全文档、校验脚本和记忆脚本分开。README 还明确：记忆须先获同意、可撤回/删除；导入计划先预览并限制查询范围；拒绝、暴力、胁迫、跟踪、自伤等情况有独立边界。

本轮复核其当前 README 与主 Skill：项目仍将自身描述为覆盖关系全周期的情绪支持与策略顾问，包含聊天分析、可执行建议、可选长期记忆和 ChatLab；其流程明确区分事实/推断/未知，并设有同意、撤回和安全边界。README 还声明支持把分析转为可发送话术、邀约、练习和观察/停止条件。[README](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/README_EN.md) · [SKILL.md](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/SKILL.md)

**重叠与差异：** 两者都可能处理聊天/自述，区分事实与推断，说明未知并给替代解释。侧重点不同：goutoujunshi 明确以关系目标、情绪支持和下一步策略为中心；本项目默认以有限材料能支持的个人层面观察与解释边界为中心，不默认给关系推进/退出方案，也不要求建立多方关系档案。

**对本项目的借鉴：** 可借鉴其按需求调用知识和明确安全/记忆边界；保持本项目对人物画像交付的专注，不复制其关系策略顾问范围。

### 2. Analyze Romantic Relationships：关系证据判断型

[README](https://github.com/jeejohn/analyze-romantic-relationships/blob/main/README.md) 将项目定位为面向关系叙述、聊天节选、时间线和可观察行为的证据优先分析；[运行时 Skill](https://github.com/jeejohn/analyze-romantic-relationships/blob/main/.agents/skills/analyze-romantic-relationships/SKILL.md) 将任务分为证据判断、互动循环、沟通准备、决策支持、情绪承接和安全分流。Skill 要求对关键材料和结论编号、按命题设证明门槛、列支持/反证/替代解释，并明确裁决状态；对重复证据不重复计权，也不强求责任对半。

**重叠与差异：** 这是与本项目最直接重叠的样本之一：双方都以材料为基础、限制读心和诊断、保留竞争解释及证据不足结论。该项目更明确聚焦情侣/婚恋中的双方关系命题（如互惠、承诺、婚姻意愿、利益因素和冲突修复），并提供关系证据账本、裁决与可选沟通/决策支持。本项目范围更窄，重心是从个体简介、自述或有限互动中整理个人层面的行为/心理观察及待核实问题；不把关系裁决作为默认产物。其 README 声明有合成案例、标准 JSON、依赖无关校验器和回归测试；这是仓库公开的工程构成，不能据此推断模型分析更准确。

### 3. Person Behavior Analysis：长期聊天记录与行为推演型

[README](https://github.com/wangguofeng728/person-behavior-analysis-skill/blob/main/README.md) 将项目描述为基于长期聊天记录的人物行为分析，覆盖关系变化、相似事件检索、动态更新和条件化情境推演；[运行时 Skill](https://github.com/wangguofeng728/person-behavior-analysis-skill/blob/main/skill/person-behavior-analysis/SKILL.md) 具体要求组织时间线和事件单元、跨情境寻找重复模式和反例，并提出竞争心理机制假设、比较历史相似事件、根据后续结果更新判断。

**重叠与差异：** 与本项目一样，它反对读心、固定标签和伪精确概率，要求注明证据、未知和替代解释。主要差异在材料规模与任务：该项目围绕长期记录、历史模式检索、人物模型更新和下一步情境推演；本项目不要求纵向聊天档案，重点处理用户当前提交的有限材料，并对心理视角作可选、受限的解释。README 中的“动态更新”描述功能意图，不等同于已验证的预测性能。

### 4. relation-analysis-skill：本地聊天档案分析型

[项目 README](https://github.com/GeorgeXiong24/relation-analysis-skill) 要求本地关系背景文件和聊天记录作为输入，执行文件解析、基线画像、聊天交叉分析、Markdown 报告生成及交付前清单检查。其报告包含时间线、关键回复、沟通模式和行动建议；每项评估要回指基线或具体聊天例子，未知推断要标记，不得编造。README 声称处理全程本地，但这属于项目设计声明，部署环境仍需自行核验。

**对本项目的借鉴：** 把当前案例扩展成稳定的输入/输出契约，要求每个结论挂接具体信号；增加分析材料的时间、来源、说话人和上下文记录。若未来支持批量文件分析，再将解析器与分析提示分层。

### 5. LoveLab：拆分式关系对话分析 Skill 组

[项目 README](https://github.com/thc1006/lovelab-skills) 展示了一个由总控分析 Skill 和多个专门 Skill 构成的仓库：四骑士、依恋、NVC、认知模式、互动动力、报告分别处理。它提供样例、标准 JSON 纵向追踪格式，且 README 声明遵循 Agent Skills 开放标准并列出多个宿主的接入方式。

**对本项目的借鉴：** 现有模块可继续保持独立文件，但需要明确何时调用 DLC、各模块共享哪些输入、重复结论如何合并。可给画像建立稳定的结构化输出 schema，并用多轮案例验证“同一对象跨时间分析”的一致性。

### 6. love-skill：多框架关系咨询流程

[仓库主 Skill 文件](https://github.com/pajama-studio/love-skill/blob/master/SKILL.md) 给出结构化 intake、伴侣双方并行分析、系统互动分析和多种理论框架；主文件引用详细框架与干预协议。它的定位是双视角咨询和冲突处理，而非单个对象的人格画像。

**对本项目的借鉴：** 它把“个人信号”和“双方循环”区分处理，这与本项目把多人关系作为 DLC 的设计吻合。应继续防止仅凭某一方单侧叙述给另一方定性，优先描述互动证据和多个可能解释。

### 7. Crush.skill：关系模拟器和工程化产品

[Crush.skill README](https://github.com/T1anhu4/Crush-skill) 将自己定位为从聊天记录构建关系/人格模型的模拟与练习工具，仓库中可见 Agent Skill、CLI、共享核心、记忆、文档、脚本、测试和界面。README 对稳定版与开发中的 Living Mind 能力作区分，并披露合成测试的范围及其不代表长期真人盲测。

**对本项目的借鉴：** 如果本项目要从提示词仓库成长为可发布 Skill 仓库，可学习“入口 Skill + 可复用模块/核心 + 测试/样例 + 发布边界”的工程布局；公开说明能力成熟度与评测局限，避免将心理画像包装成真实人物内心的读取。

### 8. PsychAgent：纵向心理咨询研究代码

[PsychAgent GitHub README](https://github.com/ECNU-ICALK/PsychAgent) 介绍多轮心理咨询研究代码：跨会话记忆与规划、显式技能检索、奖励引导的多候选轨迹选择；仓库包含生成、评估、配置、提示词和最小示例数据。README 同时提醒它仅用于研究实验，并列出真实部署还需处理的安全、隐私、知情同意、监控、升级和临床治理。

**对本项目的借鉴：** 这是工程/评估方面的参照，不是同类 Skill。其多会话架构可能过重，但“将评估流程、数据、配置和提示词显式化”适合借鉴；安全告知也适合吸收。

## 横向比较

| 项目 | 主要对象与交付 | 结构/机制 | 可见评估或边界 |
|---|---|---|---|
| 本项目 `person-deep-analysis` | 用户当前提供的个人材料；五模块，DLC 扩展关系互动与叙事呈现 | 8 条启发式 → 核实问题 → M1–M5；显式请求时可选心理学解释镜头 | 20 个行为场景；结构校验、独立指令前测、Codex CLI 烟雾测试及三例 A/B 试跑；单模型评分且评审不一致，未做人工双人盲评或用户研究 |
| goutoujunshi | 情绪支持、关系评估与策略建议；含聊天分析、记忆/ChatLab 选项 | 多方画像、事实/推断/未知、按需知识、权衡与行动计划 | README/SKILL 描述同意式长期记忆、撤回/清除、安全边界及校验脚本 |
| Analyze Romantic Relationships | 情侣关系证据分析；互动循环、沟通准备、可选决策支持 | 证据/结论编号、命题门槛、支持与反证、替代解释、裁决状态 | README 描述合成案例、JSON、标准库校验器、回归测试和 CI |
| Person Behavior Analysis | 长期聊天档案；画像、关系复盘、相似事件和条件化行为推演 | 时间线/事件单元、竞争机制假设、跨事件检索、结果更新 | README 描述隐私安全说明和合成示例；不可据自述判断预测效度 |
| relation-analysis-skill | 关系上下文 + 聊天历史；结构化报告 | 本地文件解析 → 基线 → 对话分析 → 报告 | 交付前 checklist、逐项证据、不确定性标记 |
| LoveLab | 双人对话；冲突分析与纵向指标 | 总控 + 多个窄任务 Skill；样例和 JSON 格式 | 样例和纵向数据结构；多宿主安装说明 |
| love-skill | 伴侣冲突；双方洞察和干预建议 | 双视角 intake、系统分析、多框架协议 | 框架适用边界需审慎核验；公开内容提供流程结构 |
| Crush.skill | 关系互动模拟/练习；模拟回复、报告与复盘 | Skill、CLI、共享核心、记忆和状态机 | 文档、测试与能力成熟度披露；合成测试不等同真人盲测 |
| PsychAgent | 多轮心理咨询研究；生成与评估流程 | 记忆/规划、技能检索、奖励选择 | 研究代码评测；明确研究用途和部署治理缺口 |

## 本项目的独特性

1. **默认任务范围较窄，不是没有同类方法。** 本项目聚焦用户当前提交的个人简介、自述或有限互动材料，回答材料可支持哪些个人层面观察、哪些解释仍待核实。Analyze Romantic Relationships 也强调证据优先，Person Behavior Analysis 也关注人物行为；所以“证据优先”或“多个解释”不是本项目独有。相对差异在默认对象和交付：前者重关系命题及双方互动判断，后者重长期档案和纵向推演，本项目重当前材料下的个人层面观察与克制。
2. **统一的证据底座、可选的理论镜头。** 8 条启发式与五个描述性模块帮助形成核实问题；多视角模式仅在用户明确要求时调用心理动力学、人本/需求、发展和 CBT 等镜头，并保留适用边界与解释分歧。竞品也会提出心理机制竞争解释，故多解释本身非独有；本项目差异在于把多个学派作为可选组织镜头，而不是把它们当作独立佐证或诊断工具。这是工作流设计，不是心理规律有效性的主张。
3. **从信号索引转向核实问题。** `references/signal-mapping.md` 现在帮助提出核实问题，而不把单个信号直接映射成心理解释；`evals/` 提供案例与行为回归场景。
4. **DLC 模块可组合。** 关系动力与叙事身份可在单人主流程基础上按情境调用，不必把所有输入都塞进同一份分析。
5. **Steelman 不制造虚假平衡。** 只给有材料支撑的解释最强版本，不将不同理论当成多次独立验证，不要求所有解释等概率；法证/犯罪心理只提供证据纪律，不用于个体犯罪预测。

这些差异只说明当前样本中的框架与默认工作流侧重，不能称为全生态唯一，也不代表八条启发式得到实证验证或构成临床评估工具。项目已把心理学理论改为探索视角，并禁止从单条信号反推创伤、依恋或隐藏动机。

## 调研建议及当前状态

### 分析流程

- **观察、假设、替代解释与未知：已纳入。** 主入口要求依据原话提出假设、给出替代解释并说明缺失信息；信息不足时收敛。
- **来源与上下文：已纳入。** 区分本人原话、转述、观察和剪辑片段；单段互动不总结重复循环。
- **校准问题与用户纠正：已纳入。** 关键未知可能改变判断时先问；新信息可修正假设。
- **关系互动边界：已纳入。** 单方材料不确认缺席方的人格；重复模式需要多个可比较场景。

### 理论与观点

- **启发式、替代解释与文化情境：已纳入。** 不把八条启发式当因果定律；先考虑偏好、现实安排、文化、场景和文体。
- **多视角理论边界：已纳入运行时文档。** 不同传统按需加载；主流程区分直接材料与理论解释，明确心理动力、发展、人本/需求、CBT 的可用范围；犯罪/法证心理不用于犯罪者画像或个体风险预测。它们是否提升输出质量仍未评估。
- **类型标签与隐私：已收紧。** 依恋概念只在多个互动场景作描述性参考；不诊断、不编造经历、不推断材料不支持的隐私属性。
- **安全升级：已纳入。** 对自伤、暴力、胁迫和跟踪线索暂停普通画像，优先回应现实安全需求。

### 工程与维护

- **仓库入口与元数据：已纳入。** 根 README、`agents/openai.yaml`、结构校验脚本和评估说明已添加；仓库已公开发布并采用 MIT License。此处仅记录本项目状态，不作为竞品优势判断。
- **验证与行为回归：结构及场景覆盖已纳入。** `validate_skill.py` 检查文件、frontmatter 和本地 Markdown 链接；`evals/scenarios.json` 有 20 个类别场景；独立指令前测覆盖多视角场景，并在 Codex CLI 中对四个合成案例做显式调用烟雾测试。测试发现“简短 Steelman”省略额外假设与削弱条件，以及模糊安全场景未直接核对当前安全状态；规则已收紧并复测通过。
- **评估设计：仍可加强。** 已在 Codex CLI 对三条合成案例比较普通提示与 Skill，并用单个模型进行盲化评分；两轮对普通组安全门槛判断不一致，不能当成稳定评分。尚无人工双人盲评、用户反馈、桌面 Codex/Claude Code 自动加载或跨模型/重复生成一致性测试。详见 [A/B 试跑报告](../../evals/results/2026-09-24-network-example-ab-pilot.md)。
- **隐私约束：已声明默认范围。** 当前 skill 不建立或保存人物档案；如果未来加入记忆或文件导入，再设计预览、撤回、删除和保存期限。
- **分层维护：已整理。** 主 `SKILL.md` 负责流程与边界，模块和 DLC 负责具体步骤，references 写方法限制，evals 放案例与回归提示。

## 主要一手来源

- [goutoujunshi README](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/README_EN.md)
- [goutoujunshi SKILL.md](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/SKILL.md)
- [Analyze Romantic Relationships README](https://github.com/jeejohn/analyze-romantic-relationships/blob/main/README.md)
- [Analyze Romantic Relationships SKILL.md](https://github.com/jeejohn/analyze-romantic-relationships/blob/main/.agents/skills/analyze-romantic-relationships/SKILL.md)
- [Person Behavior Analysis README](https://github.com/wangguofeng728/person-behavior-analysis-skill/blob/main/README.md)
- [Person Behavior Analysis SKILL.md](https://github.com/wangguofeng728/person-behavior-analysis-skill/blob/main/skill/person-behavior-analysis/SKILL.md)
- [relation-analysis-skill README](https://github.com/GeorgeXiong24/relation-analysis-skill)
- [LoveLab README](https://github.com/thc1006/lovelab-skills)
- [love-skill 主 Skill 文件](https://github.com/pajama-studio/love-skill/blob/master/SKILL.md)
- [Crush.skill README](https://github.com/T1anhu4/Crush-skill)
- [PsychAgent README](https://github.com/ECNU-ICALK/PsychAgent)

## 分发发现机制补充（2026-09-24）

为本仓库选择目录时，另核对了 [Vercel Skills CLI 文档](https://github.com/vercel-labs/skills/blob/main/README.md) 与 [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)。CLI 文档提供从 GitHub/本地 source 发现和按 skill 名称选择安装的工作流；规范采用 `SKILL.md` 作为入口，并允许将详细指令拆分到相对引用的 supporting files。CLI 中关于 root-level skill 打包的实践问题也见 [issue #1469](https://github.com/vercel-labs/skills/issues/1469)。

因此本仓库把唯一运行时单元放在 `skills/person-deep-analysis/`，把 evals、研究、校验脚本和传播资料留在仓库级。目标是通过 `--skill person-deep-analysis` 选择安装包，而不是让消费者把仓库开发资料作为运行时上下文。实际是否只发现一个 skill，由当前仓库的 CLI smoke test 验证；这不等于所有宿主安装都已实测。
