# 案例复核

`cases/` 中的案例用于人工检查分析过程是否可追溯、是否区分观察与假设，以及在信息不足时是否收敛。可复用输入和通过/禁止行为标准保存在 `scenarios.json`；逐场景说明和已执行的检查记录见 `behavior-regression.md`。运行 `python3 scripts/validate_evals.py` 检查场景 JSON、覆盖类别和报告锚点是否保持同步。

要比较 skill 是否带来实际帮助，按 [小规模用户验证方案](user-validation-protocol.md) 对照普通提示与 skill 输出。该方案是待执行的评估设计，不是已完成的用户研究或有效性证据。

26 个场景覆盖证据边界、多视角适用性、聊天/虚构角色分析，以及诈骗和胁迫情境中的主体性支持与双重用途边界。反诈与支持原则的公开来源见[研究记录](../docs/research/fraud-and-coercive-control-guidance.md)；聊天/虚构角色及反诈专项 Codex CLI 试跑分别见[范围扩展记录](results/2026-09-25-scope-expansion-smoke.md)和[反诈/主体性报告](results/2026-09-24-fraud-agency-forward-test.md)。

复核每个案例时，确认：

- 结论能否回指输入中的具体材料与来源；
- 观察、假设和未知是否清楚分开；
- 是否考虑可解释同一观察的替代原因；
- 是否避免从单条信号推断创伤、诊断、依恋类型或稳定人格；
- 单方叙述多人互动时，是否保留另一方视角缺失的限制；
- 是否对可能的风险线索优先回应现实安全需求。

Codex CLI 显式调用烟雾测试见 [结果记录](results/2026-09-24-codex-cli-runtime-smoke.md)。网络合成案例的 Skill/普通提示对照和模型盲评分数见 [A/B 试跑记录](results/2026-09-24-network-example-ab-pilot.md)；聊天记录和虚构角色扩展的两条宿主试跑见[范围扩展记录](results/2026-09-25-scope-expansion-smoke.md)。这些小样本试跑用于找规则缺口；单次生成和单一模型评分不足以估计稳定效果。

这些案例是工作流程示例，不是心理学理论的验证数据，也不证明实际效果或对所有文化情境都适用。已完成有限的 Codex CLI 显式调用及三例 A/B 试跑；评分由一个模型完成，且两轮对普通组安全门槛判断不一致。没有人类双人盲评、用户研究或跨模型/重复生成一致性结论。结构校验及 Skills CLI 发现测试只证明包结构与发现结果；测试也不代表桌面宿主自动触发或稳定优于普通提示。完整范围见[测试记录](behavior-regression.md)、[烟雾测试结果](results/2026-09-24-codex-cli-runtime-smoke.md)和[A/B 试跑记录](results/2026-09-24-network-example-ab-pilot.md)。
