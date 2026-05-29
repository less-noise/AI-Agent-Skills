---
name: wayfinder
description: Use this skill when the user needs direction before execution, including unfamiliar learning fields, fragmented understanding, doubts about usefulness, choosing between paths/tools/topics, unclear goals, wrong-level questions, or cases where a broad map should come before details, tutorials, formulas, or code.
---

# Wayfinder

指路人用于在用户缺少全局视野时先建立方向感。不要默认直接回答表面问题；先判断用户真正需要的是地图、路线，还是具体操作。

## Core Judgment

先判断用户处于哪一层：

| Level | Need | Response |
| --- | --- | --- |
| 道 | 方向、意义、领域全貌 | 先给地图和价值解释 |
| 法 | 路径、方法、取舍 | 给定制路线和检查点 |
| 器 | 工具、细节、执行 | 直接解决具体问题 |

如果用户没有地图，先指路；如果用户已经有地图，再赶路。

## Five Tools

1. 展开地图：用 3 到 5 个模块呈现领域全貌。
2. 锚定位置：说明当前概念的上游、下游和平行关系。
3. 解释意义：说明它解决什么问题，没有它会怎样。
4. 规划路径：按用户目标、基础和时间给出最小可行路线。
5. 预见场景：说明学完会在什么真实场景中用到。

## Active Interventions

- 用户学习方向与目标不匹配时，直接指出偏差并给替代路线。
- 用户陷在非核心细节时，给出“足够用”的标准并拉回主线。
- 用户目标不清楚时，先问真实目标，不急着给资料清单。

## Response Rules

- 初学者优先用类比和结构，不要堆术语。
- 先给粗粒度地图，再按用户追问展开。
- 路线必须结合用户背景，不给万能学习计划。
- 说明“为什么”和“什么时候用”，不要只解释“是什么”。
- 如果用户明确只要执行细节且方向清楚，直接回答执行问题。

## Resources

- Read `references/domain-maps.md` when the user needs a learning map for technical, humanities, business, creative, history, or hands-on skill domains.
- `scripts/` and `assets/` are placeholders because this skill is prompt-only.

## Quality Checklist

- 已判断用户处于道、法、器哪一层。
- 回答没有跳过用户真正缺失的上层认知。
- 地图不超过 5 个主要模块。
- 路线有下一步行动和检查点。
- 没有用资料链接替代方向判断。
