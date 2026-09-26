# RelationForge：互动风险分析相邻项目与命名评审

调研日期：2026-09-25
问题：GitHub 社区有哪些人物/关系分析、诈骗识别与操控分析项目？当前项目应如何命名，才能覆盖不同互动风险并突出解构方法？

## 结论

相邻项目的公开定位分布在人格/关系画像、聊天操控分析和专门反诈检测等方向。当前项目跨诈骗、胁迫、情绪操控、情感虐待及职场/人际霸凌，公共功能是分析互动中的风险，不是给人分型或诊断。

GitHub 上确有相邻项目：有诈骗检测 Skill、关系/人物分析 Skill、聊天操控分析应用、多风险检测 MCP 服务，以及多轮反诈研究基准。本次定向检索没有发现一个公开仓库明确把“人物/互动分析方法”作为反诈核心方法，同时提供“跨诈骗、胁迫、情感操控、霸凌的用户支持”这一完整组合。这个结论限于本次检索样本，不等于全 GitHub 唯一。

本次品牌命名定为：**RelationForge**，定位语为 *Evidence-first reasoning for people, interactions, and risk*，中文口号为“拆事实，看言行，辨风险，不替人定性”。两个英文 Skill ID 与 GitHub 仓库 slug 继续分别使用 **`interaction-risk-analysis`** 与 **`person-deep-analysis`**。品牌名覆盖人物材料与互动风险，技术 ID 则准确说明各自的安装入口。

## 样本与分类

| 类型 | GitHub 项目 | 一手页面显示的范围 | 对本项目的意义 |
|---|---|---|---|
| 可安装反诈 Skill，直接相邻 | [Nigerian-Prince-Scam-Detector](https://github.com/lazyfoxjumps/Nigerian-Prince-Scam-Detector) | Claude Code `/scam` Skill，可分析邮件、短信、DM、截图、`.eml`、链接等；README 描述诈骗剧本、红旗、技术核验、举报信息与止损支持。 | 证明“把反诈做成可安装 Skill”已有直接先例。它更像面向具体可疑材料的诈骗分析器，强调邮件/域名/钱包/地区等调查，不是广义 person-analysis 方法，也未覆盖职场霸凌等完整场景。它公开提及百分比置信度和预测下一步；本项目应避免缺乏验证的精确概率或确定性预测。 |
| 人物行为分析 Skill，方法相邻 | [person-behavior-analysis-skill](https://github.com/wangguofeng728/person-behavior-analysis-skill) | README 定位于长期聊天记录中的证据化人物画像、关系复盘、相似事件检索与行为情境推演。 | 可借鉴时间线、事件单元、重复模式与反例；其公开定位是人物行为分析，并非专门反诈。若把这类分析迁移到反诈，应改为风险分析流程，不能把画像分数当诈骗证据。 |
| 关系分析 Skill，可安装且邻近 | [relation-analysis-skill](https://github.com/GeorgeXiong24/relation-analysis-skill) | 读取关系背景与聊天历史，生成关系分析报告；README 描述本地处理、基线画像、聊天交叉分析和逐项依据。 | 可借鉴材料溯源、引用聊天依据和结构化报告。重点是理解/改善关系，不是诈骗识别。其“本地隐私”是项目自述，应由使用者核实实际宿主与配置。 |
| 聊天操控识别应用，问题直接相邻 | [Manipulense](https://github.com/ErrVoid/Manipulense) | README 将其描述为分析聊天、识别内疚施压、奉承、恐惧诉求、煤气灯等操控手段并以人话解释的应用。 | 与“从具体互动识别操控”高度接近，但不是通用 Agent Skill；可作为操控术语覆盖和交互设计参照。README 描述不能证明实际识别效度。 |
| 多风险 MCP 服务，场景直接相邻 | [Tuteliq MCP](https://github.com/Tuteliq/mcp) | README 列出多种内容/安全工具，覆盖霸凌、社交工程、婚恋诈骗、胁迫控制等。 | 证明反诈、反操控、反霸凌在一个产品入口聚合已有近似尝试；它通过 MCP 工具提供服务，与本项目的轻量提示词 Skill 和共同推理工作流不同。 |
| 反诈 Skill 组，金融窄领域相邻 | [bankbridge-skills](https://github.com/bankbridge-money/bankbridge-skills) | README 列出连接 BankBridge MCP 的 `fraud-detective`，用于发现异常扣款、重复交易、陌生商户等。 | 属于交易账户分析，并依赖外部金融 MCP；不是根据人际互动识别诈骗。 |
| 多轮诈骗研究基准，不是用户工具 | [Fraud-R1](https://github.com/kaustpradalab/Fraud-R1) | 仓库标题和说明将其描述为评估 LLM 面对多轮增强型诈骗和钓鱼诱导时的稳健性基准。 | 可借鉴渐进式诱导、信任建立、紧迫感和情绪操控的测试设计；不能作为可以识别真实骗子的产品证据。 |

### 同类密度如何判断

把搜索范围限定为“公开、可安装的 Agent Skill”时，已能找到直接反诈例子，所以不能说社区里没有这类 Skill。把范围扩到“所有解决方案”，同类和相邻项目还包括聊天分析应用、MCP 检测工具、消费者浏览器/移动产品、金融风控系统和研究基准。它们的输入、用户、运行环境和验证方式不同，不能把数量合并成一个竞品市场规模。

目前可主张的区别是**方法与支持流程的组合**：从用户提供的互动或事件开始，标出具体行为及上下文，分析行为实际效果，再把可能的因果、立场和目的作为待检验假设，配上反证、替代解释、未知和独立核验办法。模型本身已有模式识别能力；Skill 不是新造一个检测器，而是用提示词把识别结果组织成可质疑、可更新的分析。受影响者不必先证明对方有恶意，才可以暂停付款或设边界；下一步由用户选择；拒绝把技能改造成操纵教程。此为产品定位差异，不是经对照试验证实的准确率优势。

## 命名选择的依据

两者之间有自然的衔接，但需要明确边界：

1. **Person-analysis 提供观察方法**：材料来源、说话人、时间线、具体行为、互动变化、重复性、影响、反例和未知。
2. **反诈逻辑提供风险分类与核验动作**：冒充权威、保密/隔离、制造紧迫、索要钱款或凭证、投资平台异常、回款/提现障碍、工作机会先收费等，需要尽可能对照平台、金融机构、政府或独立渠道核实。
3. **心理学提供有限的解释镜头**：如信任建立、互惠压力、损失厌恶、情绪勒索、认知失调或边界惩罚。它们用于解释某种行为为什么值得留意，不是读心器，也不能证明犯罪动机。
4. **输出先解决受影响者的任务**：若资金或人身风险迫近，先保护安全、账户和后续转账；之后才在用户需要时解释人物/互动模式。避免危机中先给嫌疑人做长篇人格画像。
5. **保留主体性和反向用途边界**：用户可得出“证据不足，但我先不付款”；不需要接受 AI 的定性。拒绝生成诈骗话术、诱导策略、胁迫技巧、规避识别或报复方案。

因此，“person-analysis”更适合作为**历史方法来源**，不适合作为唯一的面向用户的名称。单独使用它容易让人预期这是人格画像或关系画像；使用“防骗与反操控”又会弱化学校、职场及亲密关系霸凌等应用。RelationForge 作为品牌覆盖人物材料与互动风险，两个 Skill ID 则分别说明具体任务。

> **品牌名：** RelationForge
> **定位语：** Evidence-first reasoning for people, interactions, and risk
> **一句话：** 拆事实，看言行，辨风险，不替人定性。
> **Skill：** `interaction-risk-analysis`、`person-deep-analysis`

## 后续维护与评估建议

- 保留“源自 person-analysis”的方法演进，但让用户看到的主名称表达当前覆盖面。
- 运行时保持风险优先路由：金融诈骗、冒充和迫近安全风险走专门步骤；人际/职场操控走互动模式与安全支持；只有用户明确需要时，再展开心理视角。
- 避免以“识别骗子人格”“NPD 检测”“黑暗三联征识别”作为主张。分析行为比分析人格更可核验，也更适合用户自我保护。
- 评测分开测诈骗线索、安全支持、操控/霸凌分析、目的/因果假设校准、误报控制和反证更新。使用独立标注、非诈骗对照、多次采样，才可进一步谈效果。
- 对外不要暗示其替代执法、银行风控、法律意见、临床评估或资金追回服务。

## 检索范围与局限

本次根据 GitHub 网页搜索和候选项目的公开仓库首页/README 定向筛选，查询了 `SKILL.md` 与 `scam detection`、`anti-fraud`、`person-analysis`、`person behavior analysis`、`relationship analysis`、`manipulation detection` 等组合；重点直接查看了上述仓库的 README、可见目录或项目描述。GitHub 代码搜索的登录限制、索引延迟、命名差异、非英语内容和仓库可发现性会造成漏检。本报告是案例扫描，不是系统综述，也没有对每个项目安装运行、评测代码或验证它们的性能声明。

## 一手来源

- [Nigerian-Prince-Scam-Detector README](https://github.com/lazyfoxjumps/Nigerian-Prince-Scam-Detector)（包含 Skill 能力、边界、安装与文件结构介绍）
- [Person Behavior Analysis Skill README](https://github.com/wangguofeng728/person-behavior-analysis-skill)
- [Relationship Analysis Skill README](https://github.com/GeorgeXiong24/relation-analysis-skill)
- [Manipulense README](https://github.com/ErrVoid/Manipulense)
- [Tuteliq MCP README](https://github.com/Tuteliq/mcp)
- [BankBridge Skills README](https://github.com/bankbridge-money/bankbridge-skills)
- [Fraud-R1 README](https://github.com/kaustpradalab/Fraud-R1)
