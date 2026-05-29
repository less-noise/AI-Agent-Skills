---
name: task-handover
description: Use this skill when the user needs a structured AI task handover, continuation brief, context summary, progress transfer, or new-session prompt, especially when context is too long, quota is running out, a conversation will switch, work must continue later, or another AI/person needs to resume without losing decisions, files, constraints, failures, and next steps.
---

# Task Handover

任务交接用于生成可接班的上下文文档。目标是让新 AI 或新会话不依赖历史对话，也能准确继续任务。

## Handover Structure

按以下 8 节生成，缺失信息写“无”或“待确认”，不要省略：

1. 任务快照：标题、类型、当前状态、中断原因、优先级、截止时间。
2. 最终目标：逐字引用原始需求，并写清验收标准。
3. 已完成内容：已执行步骤、已生成文件、失败或放弃的尝试。
4. 待完成内容：按高、中、低优先级列待办，并写验收标准。
5. 关键约束：格式、风格、范围、技术、路径、其他限制。
6. 已确认决策与用户偏好：记录已拍板事项、用户强调点、明确拒绝项。
7. 当前上下文摘要：200 字以内说明任务背景、关键变化和当前阶段。
8. 接班指令：可直接复制到新会话的第一条消息。

## Writing Rules

- 原始需求要逐字引用，不要改写成自己的总结。
- 进度要量化，例如“5 个接口完成 3 个”，不要写“大部分完成”。
- 文件路径优先写绝对路径。
- 错误信息、失败尝试、放弃原因必须保留。
- 不确定内容写“待确认”，不要用“可能”“应该”糊弄。
- 只有真实产出才能进入“已完成内容”。

## Attachments

按任务类型追加附件：

- 代码任务：语言、框架、依赖版本、关键文件、测试状态、最后运行命令、完整报错。
- 写作任务：目标读者、语气风格、结构大纲、字数要求、参考资料、需保留段落。
- 研究任务：研究问题、来源、分析框架、已得结论、待验证假设、数据路径。

## Resources

- Read `references/examples.md` when a complete handover example is needed for code, writing, research, or planning tasks.
- `scripts/` and `assets/` are placeholders because this skill is prompt-only.

## Quality Checklist

- 接手方不看历史对话也能继续。
- 下一步是单条、具体、可执行的动作。
- 失败尝试和拒绝项没有遗漏。
- 关键约束、路径、版本、命令没有模糊化。
- 接班指令可直接复制到新会话使用。
