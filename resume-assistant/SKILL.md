---
name: resume-assistant
description: Use this skill when the user wants to create, improve, review, polish, or export a resume/CV, including job hunting, career switching, internship applications, campus recruitment, resume diagnosis, target-role selection, STAR experience mining, and PDF/HTML resume generation.
---

# Resume Assistant

简历助手用于把用户的零散经历转化为可投递的专业简历。必须先挖掘经历和目标，再写内容和排版；不要在信息不足时直接生成成品。

## Core Workflow

1. 判断任务类型：新建简历、优化已有简历、方向定位、成品导出。
2. 收集基础信息：姓名、手机、邮箱、求职城市、目标岗位或行业。
3. 如果用户方向不清楚，先做方向定位：背景、经历、兴趣、擅长点、可选方向。
4. 判断用户类型：应届生、有经验者、转行者。
5. 用 STAR 追问每段关键经历：Situation、Task、Action、Result。
6. 将经历改写为“动作动词 + 行动范围 + 方法 + 量化结果”。
7. 选择简历结构并输出：优先 PDF；环境受限时输出可打印 HTML。
8. 交付后给出文件路径、核心亮点，并询问是否需要调整。

## Required Information

- 姓名、手机号、邮箱、求职城市。
- 目标岗位、目标行业、目标公司类型。
- 教育背景、工作/实习经历、项目经历、技能证书。
- 每段经历的真实贡献、使用方法、影响范围、量化结果。

## Identity Strategy

- 应届生：教育背景前置，突出实习、项目、竞赛、社团，控制 1 页。
- 有经验者：工作经历前置，按时间倒序排列，控制 2 页以内。
- 转行者：先写核心能力摘要，再写与新方向相关经历，旧经历只保留可迁移部分。

## Experience Writing Rules

- 用强动作动词开头：主导、推动、搭建、优化、整合、交付、提升、降低。
- 必须追问量化结果；用户记不清时引导估算数量级，不得编造。
- 避免最终稿出现“参与”“协助”“学习”“了解”等弱贡献词。
- 每条要点优先写成果，不写岗位职责清单。

## Output Rules

- PDF 为首选成品格式。
- HTML 作为稳定备选，必须单文件、内嵌 CSS、支持 `@media print`、A4 尺寸。
- 如需生成 HTML，准备结构化 JSON 后运行：

```powershell
python .\resume-assistant\scripts\generate_resume.py .\resume.json .\outputs\resume.html
```

## Resources

- Read `references/resume-examples.md` when examples of STAR probing, rewrite quality, or identity-specific resume sections are needed.
- Use `assets/resume-template.html` as the HTML rendering template.
- Use `scripts/generate_resume.py` only after resume content has been confirmed or drafted.

## Quality Checklist

- 基础信息完整。
- 身份类型和简历结构匹配。
- 每段经历有动作、范围、方法、结果。
- 没有编造数字。
- 没有弱贡献词残留。
- 页数、字号、留白、颜色和 ATS 兼容性符合要求。
