# GitHub 相似项目对照：历史调研快照（截至 2026-09-25）

调研日期：2026-09-24（本轮复核）
范围：本文件有两个时间和产品方向不同的历史切片：前半部分比较旧版人物/关系分析工具的 8 个仓库；后半部分围绕当时的公益反诈/反操控方向比较 11 个仓库。这里只据仓库公开 README、Skill 文件和可见结构描述设计，不把项目自述等同于实际效果证明。

本文件记录定向选出的 19 个仓库样本，不推断 GitHub 全站规模或总体分布。两个切片对应不同产品定位，不应简单理解为 19 个直接竞品。仓库内容会变化，结论应视为 2026-09-24 附近的查阅快照。

> **历史资料提示：** 本文中的“当前”“本轮”均指各段落标注的 2026-09-24/25 研究时点，不代表现在的项目状态。旧名称、仓库 slug、测试数量和建议只作为决策记录保留。现在有两个独立运行时入口：[`interaction-risk-analysis`](../../skills/interaction-risk-analysis/SKILL.md) 与 [`person-deep-analysis`](../../skills/person-deep-analysis/SKILL.md)；请以仓库 README 为准。

## 摘要

在 2026-09-24/25 的项目阶段，主线已转为帮助普通人核对诈骗、心理操控、胁迫与霸凌风险，并让使用者看见判断依据、未知和可选核验步骤。11 个公益安全样本中，未发现一个同时与“消费者可安装 Skill + 跨诈骗/关系操控/霸凌 + 非责备且主体性优先”完整同型的仓库；但诈骗 Skill、操控识别原型、MCP 工具和评测已有相邻尝试。因此只能说当时样本中的定位组合有差异，不能称为唯一或准确率领先。

此前的人物/关系分析方向及其 8 个仓库对照作为历史研究保留，不能当作当前主产品介绍。

前半部分保留原项目方向的历史对照观察；后半部分记录产品转向后的定向样本、竞品边界与当时实现状态。本文不是当前项目说明。

## 旧版人物/关系分析方向：仓库观察（历史）

### 1. goutoujunshi：关系决策顾问型 Skill

[项目英文 README](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/README_EN.md) 描述了一个围绕用户当前关系困境提供支持和决策建议的 Skill。其流程包括情绪承接、建立多方画像、区分事实/推断/未知、按需检索知识、衡量互惠和机会成本，最终给出建议、话术、观察期和停止条件。它允许用户用自然叙述输入，并只追问可能改变建议的关键信息。

结构上，仓库把入口 `SKILL.md`、Codex 元数据 `agents/openai.yaml`、知识与实践参考文档、架构/安全文档、校验脚本和记忆脚本分开。README 还明确：记忆须先获同意、可撤回/删除；导入计划先预览并限制查询范围；拒绝、暴力、胁迫、跟踪、自伤等情况有独立边界。

本轮复核其当前 README 与主 Skill：项目仍将自身描述为覆盖关系全周期的情绪支持与策略顾问，包含聊天分析、可执行建议、可选长期记忆和 ChatLab；其流程明确区分事实/推断/未知，并设有同意、撤回和安全边界。README 还声明支持把分析转为可发送话术、邀约、练习和观察/停止条件。[README](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/README_EN.md) · [SKILL.md](https://github.com/shengjidaguai-china/goutoujunshi/blob/main/SKILL.md)

**历史观察：** 旧版也处理聊天/自述，区分事实与推断；goutoujunshi 则以关系目标、情绪支持和下一步策略为中心。在本次研究所处阶段，人物分析包曾归档，项目主线转为诈骗、操控、胁迫和霸凌风险支持；此后人物分析包已恢复为独立 Skill。公益安全方向对照见下文。

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

## 旧版横向比较（历史快照）

| 项目 | 主要对象与交付 | 结构/机制 | 可见评估或边界 |
|---|---|---|---|
| 本项目当时的 `person-deep-analysis`（研究时已归档，现已恢复） | 个人材料、聊天片段、虚构角色；曾含有限反诈支持 | 8 条启发式 → 核实问题 → M1–M5；按需读取相关参考 | 当时有 26 个行为场景及若干单模型小样本试跑；这些结果不是现行独立 Skill 的复测 |
| goutoujunshi | 情绪支持、关系评估与策略建议；含聊天分析、记忆/ChatLab 选项 | 多方画像、事实/推断/未知、按需知识、权衡与行动计划 | README/SKILL 描述同意式长期记忆、撤回/清除、安全边界及校验脚本 |
| Analyze Romantic Relationships | 情侣关系证据分析；互动循环、沟通准备、可选决策支持 | 证据/结论编号、命题门槛、支持与反证、替代解释、裁决状态 | README 描述合成案例、JSON、标准库校验器、回归测试和 CI |
| Person Behavior Analysis | 长期聊天档案；画像、关系复盘、相似事件和条件化行为推演 | 时间线/事件单元、竞争机制假设、跨事件检索、结果更新 | README 描述隐私安全说明和合成示例；不可据自述判断预测效度 |
| relation-analysis-skill | 关系上下文 + 聊天历史；结构化报告 | 本地文件解析 → 基线 → 对话分析 → 报告 | 交付前 checklist、逐项证据、不确定性标记 |
| LoveLab | 双人对话；冲突分析与纵向指标 | 总控 + 多个窄任务 Skill；样例和 JSON 格式 | 样例和纵向数据结构；多宿主安装说明 |
| love-skill | 伴侣冲突；双方洞察和干预建议 | 双视角 intake、系统分析、多框架协议 | 框架适用边界需审慎核验；公开内容提供流程结构 |
| Crush.skill | 关系互动模拟/练习；模拟回复、报告与复盘 | Skill、CLI、共享核心、记忆和状态机 | 文档、测试与能力成熟度披露；合成测试不等同真人盲测 |
| PsychAgent | 多轮心理咨询研究；生成与评估流程 | 记忆/规划、技能检索、奖励选择 | 研究代码评测；明确研究用途和部署治理缺口 |

## 旧版独特性观察（历史，不代表当前定位）

1. **默认任务范围较窄，不是没有同类方法。** 本项目聚焦用户当前提交的个人简介、自述或有限互动材料，回答材料可支持哪些个人层面观察、哪些解释仍待核实。Analyze Romantic Relationships 也强调证据优先，Person Behavior Analysis 也关注人物行为；所以“证据优先”或“多个解释”不是本项目独有。相对差异在默认对象和交付：前者重关系命题及双方互动判断，后者重长期档案和纵向推演，本项目重当前材料下的个人层面观察与克制。
2. **统一的证据底座、可选的理论镜头。** 8 条启发式与五个描述性模块帮助形成核实问题；多视角模式仅在用户明确要求时调用心理动力学、人本/需求、发展和 CBT 等镜头，并保留适用边界与解释分歧。竞品也会提出心理机制竞争解释，故多解释本身非独有；本项目差异在于把多个学派作为可选组织镜头，而不是把它们当作独立佐证或诊断工具。这是工作流设计，不是心理规律有效性的主张。
3. **从信号索引转向核实问题。** `references/signal-mapping.md` 现在帮助提出核实问题，而不把单个信号直接映射成心理解释；`evals/` 提供案例与行为回归场景。
4. **DLC 模块可组合。** 关系动力与叙事身份可在单人主流程基础上按情境调用，不必把所有输入都塞进同一份分析。
5. **Steelman 不制造虚假平衡。** 只给有材料支撑的解释最强版本，不将不同理论当成多次独立验证，不要求所有解释等概率；法证/犯罪心理只提供证据纪律，不用于个体犯罪预测。

这些差异只说明当前样本中的框架与默认工作流侧重，不能称为全生态唯一，也不代表八条启发式得到实证验证或构成临床评估工具。项目已把心理学理论改为探索视角，并禁止从单条信号反推创伤、依恋或隐藏动机。

## 旧版调研建议与实现记录（历史）

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
- **验证与行为回归：结构及场景覆盖已纳入。** `validate_skill.py` 检查文件、frontmatter 和本地 Markdown 链接；`evals/scenarios.json` 有 26 个类别场景，覆盖有限材料、多视角、聊天片段、虚构人物和反诈/操控双重用途边界。两条新增范围扩展场景已在 Codex CLI 单次试跑，诈骗/主体性场景仍需跨运行及目标宿主复测；所有小样本结果仅用于排查行为缺口。
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

本节记录的是 2026-09-24 时的分发设计。当时唯一运行时包已调整为 `skills/person-analysis/`，通过 `--skill person-analysis` 安装；它把旧人物分析方法与反诈、反操控和安全支持合并，其他研究、案例及校验脚本留在仓库级。该包和 ID 后来再次改名；当前两个 Skill 的发现与隔离安装方式请以仓库 README 为准。

## 公益型识骗与反操控项目：GitHub 定向检索（2026-09-24）

### 范围与方法

本次围绕拟议方向做定向检索：帮助普通人从消息、互动或经历中识别诈骗、社交工程、情绪操控、胁迫和霸凌，并选择核实或自我保护步骤；优先寻找可安装的 Agent Skill、MCP 工具、面向消费者的检测产品和教育项目。检索词组合包括 `scam detection Agent Skill`、`anti-scam chatbot`、`romance scam detector`、`gaslighting/emotional manipulation`、`bullying romance scam MCP`、`scam awareness`、`scam SKILL.md Claude Code/OpenClaw`，并纳入用户补充的 Manipulense、ASK benchmark 与 Fraud-R1。逐项查看 GitHub 仓库公开 README/项目页；以下是从检索结果中筛选出的 **11 个相关仓库样本**，不包括前文已比较的关系分析 Skills。

这个数字是“本轮选出的可核对样本数”，不是 GitHub 全站结果总量或生态规模。GitHub 搜索与 Topic 标签不穷尽、会随时间改变，关键词覆盖不完整，项目 README 的能力自述也不是独立效果验证。作为一个可复查但更窄的切片，GitHub `scam-awareness` Topic 页面在本轮显示 7 个公开仓库；Topic 标签由维护者添加，不能据此推断所有同类项目数量。[Topic 页面](https://github.com/topics/scam-awareness)

### 直接重叠与相邻项目

| 仓库 | 类别 | 与本项目的重叠及边界 |
|---|---|---|
| [Tuteliq/mcp](https://github.com/Tuteliq/mcp) | **最接近的相邻产品：MCP 检测工具** | README 列出霸凌、社交工程、婚恋诈骗、胁迫控制、弱势处境利用等文本检测端点，并提供情境参数与行动计划工具；覆盖面与本项目公益目标明显重叠。差异在交付形态：它是供 MCP 客户端调用的多工具服务，本项目是可直接安装的分析 Skill，强调证据分层、解释不确定性、非责备语气和由当事人选择下一步。仓库的功能描述不证明检测准确率。 |
| [ErrVoid/Manipulense](https://github.com/ErrVoid/Manipulense) | **直接重叠：聊天操控识别应用** | README 描述导入聊天记录，识别内疚施压、奉承、恐惧诉求、煤气灯等策略并可视化互动中的影响变化。它在“读聊天、解释操控线索”上与本项目高度接近，但属于 Flutter/FastAPI 消费者应用，不是可安装 Agent Skill，公开介绍也未展示独立准确性评估。 |
| [lazyfoxjumps/Nigerian-Prince-Scam-Detector](https://github.com/lazyfoxjumps/Nigerian-Prince-Scam-Detector) | **直接重叠：面向个人的 Claude Code 反诈 Skill** | README 描述 `/scam` Skill 可分析邮件、短信、私信、截图和 `.eml`，有诈骗剧本、语言红旗、链接/邮件头检查及安全回复参考。它是本轮发现的最直接“防骗 + 可安装 Skill”相邻项目；范围聚焦诈骗识别和材料取证，未见霸凌/胁迫/情感操控的完整支持流程。其“识破每一种新骗局”等表述属于项目宣传，不能作为性能结论。 |
| [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | **直接重叠：兼职/副业反诈 Skill** | README 描述一组可安装 Skills，用公开需求信号寻找兼职/副业机会，并通过时效核查和反诈 rubric 验证具体机会。它是中文 Skill 形态的重要相邻项目，但集中在就业/收入机会核验，不覆盖广义关系操控、霸凌或电诈受害后的支持。 |
| [cablate/Fraud-Prevention](https://github.com/cablate/Fraud-Prevention) | **直接问题重叠：诈骗文本分析原型** | README 将其描述为用 LLM 分析诈骗文本、提升防诈意识的系统；方向直接重叠在“读一段信息，帮助识别诈骗”。它已于 2026-07-04 归档，且 README 展示的是较早期 Web/爬取/知识库架构，不是跨场景的可安装 Skill。 |
| [LeverCRO/clawback](https://github.com/LeverCRO/clawback) | **窄领域相邻：加密资产反诈 Skills** | README 将其称为 OpenClaw 的加密诈骗检测 Skills，面向链上资产、代币与交易风险。它证明“防骗能力做成 Agent Skill”已有相邻实践，但范围偏技术/金融资产，不覆盖日常社交工程、情绪勒索、霸凌或受影响者支持。 |
| [airifqiry/TrustAble](https://github.com/airifqiry/TrustAble) | **相邻：消费者端诈骗检测产品** | README 描述 Chrome 扩展分析网页、消息和电话内容，覆盖钓鱼、冒充、虚假紧迫感、婚恋、工作等诈骗类型。它与本项目共享“把可疑内容交给工具分析”的入口，但属于浏览器产品和检测分数输出，不是通用 Agent Skill 或心理操控支持流程。 |
| [ashleytoh/phish-n-cheats](https://github.com/ashleytoh/phish-n-cheats) | **相邻：反诈教育模拟器** | README 描述在模拟交易场景中与 AI “卖家”互动，随后对玩家的识别与选择评分并讲解。它聚焦训练和预防教育，而非用户带入真实经历后获得个案支持；同时是面向平台/信任安全的产品原型。 |
| [srijon57/ScamSentinel](https://github.com/srijon57/ScamSentinel) | **相邻：社区举报与信息核验平台** | README 描述用户提交诈骗报告、证据和社区反馈，并计划提供防诈问答/教育。与本项目都服务于公众防骗，但它重社区案例库和举报，本项目重个人材料的即时梳理与安全选择。 |
| [kaustpradalab/Fraud-R1](https://github.com/kaustpradalab/Fraud-R1) | **研究/评测相邻** | README 将其描述为评估 LLM 在多轮欺诈诱导下抵抗能力的基准，覆盖可信度建立、制造紧迫感和情绪操控等阶段。它可为本项目设计“多轮、渐进式诱导”回归测试提供参考，但不是给普通用户直接使用的防护工具。 |
| [megansquire/ask-benchmark](https://github.com/megansquire/ask-benchmark) | **研究/评测相邻：AI Scam Knowledge (ASK)** | README 描述 35 个诈骗场景按四级红旗强度构造，并对 AI 助手的风险提醒作 0–4 分评定，且以重复运行揭示输出波动与误报。它不是终端用户防护产品，但其渐进红旗、非诈骗对照和重复采样设计适合借鉴到本项目评测。 |

### 对数量与竞争强度的判断

- 若按**整个任务空间**计，相关项目不少：前文已有关系分析 Skills；本轮还找到覆盖多类风险的 MCP、诈骗文本分析原型、加密资产专用 Skills、浏览器诈骗检测、反诈教育模拟器、社区举报平台与评测基准。因此不能说“GitHub 上没有竞品”。
- 若严格限定为**普通用户可直接安装、围绕真实对话/经历、同时处理诈骗与心理操控并提供非责备、主体性优先支持的 Agent Skill**，本次 11 个样本里没有看到一个与该完整定位完全一致的仓库。Nigerian-Prince-Scam-Detector 与 ClawBack 已有反诈 Skill 形态，Manipulense 已有聊天操控识别应用，Tuteliq 覆盖诈骗/霸凌/胁迫多个检测端点；因此差异不能说成“第一款反诈 Skill”或“唯一操控检测工具”。更窄的机会在于把多种伤害情境、行为证据纪律、关怀方式和自主选择路径组合成一个跨场景的对话支持 Skill。这个判断只适用于本次有限检索，不能声称全站唯一。
- 市场空位不宜表述为“独家识别所有坏人”。更可信的差异是：**把诈骗预警与心理操控/霸凌支持放在同一入口；把行为证据、未知和替代解释说清；避免羞辱受影响者；提供可自主选择的核实与保护步骤；并拒绝将方法反向用于操控他人。**这属于产品流程和价值立场差异，不是已证实的识别准确度优势。

### 当时仓库实现与实测范围（已被后续版本取代）

在该快照所处版本，项目名为 **防骗与反操控**，唯一安装 Skill 是 `person-analysis`。该版本恢复旧版人物分析中的事件拆解、互动模式、竞争解释、证据/反证和按需多视角，并将这套方法优先用于社交工程/电诈、亲密关系操控、职场及社交霸凌。它不诊断人格或疾病，不以“识别坏人”为目标，也不替用户决定是否离开关系或举报。

与样本中单点诈骗 Skill、检测应用或关系顾问的差异，是同一入口以人物/互动解构作为分析方法，同时整合风险核验、非责备支持和用户选择。新版定义了 19 个专属合成验收场景，并提供 7 种普通 Codex 与显式 Skill 的配对输出演示；宿主试跑结果以 `evals/results/2026-09-25-person-analysis-anti-fraud-acceptance.md` 和 `docs/demos/README.md` 为准。之前 21 个防骗版场景及其 11 次试跑属于前一个运行时版本。无论样本还是新评估都不能证明检测准确率或现实效果。

### 命名与仓库标识

仓库样本的名称大多直接标出问题或功能（Scam Sentinel、Fraud Prevention、TrustAble、clawback、phish-n-cheats），而前文关系类 Skill 名称偏分析/关系顾问。**当时的命名建议**是优先让普通用户看懂“防骗 + 识别操控”；这条建议已由后续命名评审重新取舍。

可继续讨论的中文候选：

1. **防骗与反操控**：短、直接，涵盖电诈与人际操控；“反操控”较概括，宜配副标题说明情绪勒索、霸凌等。
2. **诈骗与操控风险识别**：范围明确、准确克制，但像功能模块名，公益温度较弱。
3. **识骗防操控**：短而有行动感，读起来略像口号，品牌辨识度需再看。
4. **看清套路，守住选择**：最有人文感，适合作为标语；单独作为仓库名时用途不够直观。

**当时的命名决定（已过期）：** 采用“防骗与反操控”，Skill ID 为 `person-analysis`，仓库 slug 为 `evidence-based-person-analysis`。这些标识已被当前名称取代：**互动风险识别与解构 / `interaction-risk-analysis`**。

### 本轮查阅的一手仓库页面

- [Tuteliq/mcp README](https://github.com/Tuteliq/mcp)
- [ErrVoid/Manipulense README](https://github.com/ErrVoid/Manipulense)
- [Nigerian-Prince-Scam-Detector README](https://github.com/lazyfoxjumps/Nigerian-Prince-Scam-Detector)
- [XBuilderLAB/cheat-on-money README](https://github.com/XBuilderLAB/cheat-on-money)
- [cablate/Fraud-Prevention README](https://github.com/cablate/Fraud-Prevention)
- [LeverCRO/clawback README](https://github.com/LeverCRO/clawback)
- [airifqiry/TrustAble README](https://github.com/airifqiry/TrustAble)
- [ashleytoh/phish-n-cheats README](https://github.com/ashleytoh/phish-n-cheats)
- [srijon57/ScamSentinel README](https://github.com/srijon57/ScamSentinel)
- [kaustpradalab/Fraud-R1 README](https://github.com/kaustpradalab/Fraud-R1)
- [ASK benchmark README](https://github.com/megansquire/ask-benchmark)
