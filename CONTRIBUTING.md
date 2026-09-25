# 贡献指南

欢迎补充边界修正、识别流程改进、宿主兼容反馈、翻译和评估案例。贡献应服务于项目承诺：**根据具体行为帮助普通人核对诈骗、操控或霸凌风险，说明判断依据和未知，并把决定权留给当事人。**

## 提交前

- 先搜索已有 issue/文档，说明具体场景、预期行为和当前问题。
- 改动 `skills/interaction-risk-analysis/` 时，保持运行时包自包含，文件引用使用 Skill 目录内的相对路径。
- 修改解构、反诈或安全行为时，更新相应的 `evals/interaction-risk-cases.json` / `evals/interaction-risk-acceptance.md`，并在适用时更新 `safety-scenarios.json` 与 `safety-regression.md`。
- 诈骗和心理学术语的事实主张应有可靠来源；区分研究证据、观察线索和项目假设。不要以仓库自述或单个例子宣称有效。
- `archive/person-deep-analysis/` 保留旧版原始内容供追溯。活跃 Skill 位于 `skills/interaction-risk-analysis/`；修改时同步验收场景，避免复制未经审查的旧版规则。

## 案例隐私

只提交合成案例，或已取得明确授权且无法识别当事人的材料。默认按合成案例处理。不要提交真实私密聊天、照片、社交账号、姓名、联系方式、位置、病史或可拼接识别身份的细节。删除信息不等于匿名；若不确定，请用虚构文本重写场景。

## 验证

```sh
python3 scripts/validate_skill.py
python3 scripts/validate_evals.py
python3 scripts/validate_safety_evals.py
python3 scripts/validate_interaction_risk_evals.py
```

评估文档用于行为复核，不是自动心理评分或效果证明。如果校验器或宿主运行与预期不符，请记录准确环境、合成输入、差异和复现步骤，不提交真实私人材料。

## Pull request 内容

请说明改了什么、为什么、影响哪些使用场景、运行了哪些检查，以及仍有哪些限制。行为规则改动应至少覆盖一个正常场景和一个容易越界的反例。
