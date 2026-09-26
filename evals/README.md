# 评估资料

## 当前两个 Skill

RelationForge 的运行时入口分别是 [`interaction-risk-analysis`](../skills/interaction-risk-analysis/SKILL.md) 和 [`person-deep-analysis`](../skills/person-deep-analysis/SKILL.md)。以下评估记录按各自运行时版本和 Skill ID 阅读。

`interaction-risk-cases.json` 定义 20 个拆解与安全场景；`interaction-risk-acceptance.md` 是逐例验收锚点。**这 20 例尚未使用当前 Skill ID `interaction-risk-analysis` 逐例运行。**旧 Skill ID `person-analysis` 下的宿主运行记录见[历史报告](results/2026-09-25-person-analysis-anti-fraud-acceptance.md)，关于模型本身已有识别能力及新版解构方法的试跑见[方法评估](results/2026-09-25-decomposition-method-evaluation.md)。八个合成案例另有旧 ID 下普通 Codex / 显式 Skill 的配对输出，见 [`docs/demos/`](../docs/demos/README.md)。运行 `python3 scripts/validate_interaction_risk_evals.py` 检查案例结构。

`safety-scenarios.json` 与 `safety-regression.md` 保留了先前防骗与反操控版的 21 个场景；其模型运行记录 `results/2026-09-25-public-safety-skill-forward-test.md` 是先前版本的历史数据，不代表当前 `interaction-risk-analysis` 全部复测通过。

`scenarios.json`、`cases/`、`behavior-regression.md` 及 `person-deep-analysis` 报告记录更早版本的人物分析测试。`skills/person-deep-analysis/` 已恢复为独立运行时目录；历史运行结果不是这次恢复后的实测。运行 `python3 scripts/validate_evals.py` 检查这组历史测试材料。

无论新旧，这些都是工作流程测试，不验证心理学理论，不提供临床有效性、现实诈骗识别率或普遍模型效果保证。结构校验只检查格式；合成模型试跑只说明该次运行的表现。当前尚无真人用户研究、双人独立盲评或跨模型稳定性证据。
