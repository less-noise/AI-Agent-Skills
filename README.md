# AI Skills 技能包

四个为 AI 助手设计的 Skill，覆盖简历求职、任务交接、学习导航和进度定位四种高频协作场景。每个 Skill 都包含完整的指令、参考示例和输出模板，直接放入 Cowork 的 skills 目录即可使用。

## 技能概览

| Skill            | 中文名   | 一句话描述                                     |
| ---------------- | -------- | ---------------------------------------------- |
| resume-assistant | 简历助手 | 把零散经历转化为可投递的专业简历               |
| task-handover    | 任务交接 | 生成标准化交接文档，让新会话无缝接手           |
| wayfinder        | 指路人   | 在学习和探索中建立方向感，先指路再赶路         |
| progress-locator | 定位仪   | 把模糊的"我在哪、还差多少"变成可量化的现状判断 |

---

## 1. 简历助手（resume-assistant）

把用户的零散经历——实习、项目、社团活动、工作履历——通过 STAR 追问、量化改写和身份策略，转化为可以直接投递的专业简历。支持应届生、有经验者和转行者三种身份策略，最终输出 PDF 或可打印 HTML。

**核心流程：** 判断任务类型 → 收集基础信息 → 方向定位（如需）→ STAR 追问 → 经历改写 → 排版输出

**包含资源：**

- `references/resume-examples.md` — STAR 追问和改写示例
- `assets/resume-template.html` — 单文件 A4 简历模板
- `scripts/generate_resume.py` — JSON 转 HTML 渲染脚本

**适用场景：** 写简历、改简历、方向不清晰、需要 STAR 挖掘、生成 ATS 兼容的 PDF/HTML

---

## 2. 任务交接（task-handover）

当上下文过长、额度将尽、需要切换会话，或者需要把工作交给人或另一个 AI 时，生成包含任务快照、目标、已完成内容、待办、关键约束和接班指令的标准化文档。目标是让接手方不看历史对话也能准确继续任务。

**八节结构：** 任务快照 → 最终目标 → 已完成内容 → 待完成内容 → 关键约束 → 已确认决策 → 上下文摘要 → 接班指令

**包含资源：**

- `references/examples.md` — 代码、写作、研究、规划四类任务的完整交接示例

**适用场景：** 长任务续接、上下文压缩、跨会话协作、任务转交他人

---

## 3. 指路人（wayfinder）

当用户缺乏全局视野时，不急着回答表面问题，而是先判断用户处于"道、法、器"三层中的哪一层。通过展开地图、锚定位置、解释意义、规划路径和预见场景五个工具，帮用户建立方向感后再深入执行。

**三层判断：** 道（方向与意义）→ 法（路径与方法）→ 器（工具与细节）

**包含资源：**

- `references/domain-maps.md` — 技术、人文社科、商业、创意、历史、技能六大领域的结构地图

**适用场景：** 进入陌生学习领域、方向迷茫、碎片化认知、不知道学什么、在细节里迷失

---

## 4. 定位仪（progress-locator）

把"我现在到哪了、还差多少、接下来做什么"这类模糊问题转化为清晰、量化、可行动的回答。从时间轴、深度和风险三个维度扫描当前状态，用阶段标记器、进度仪表盘、状态诊断仪、位置锚定器和下一步导航五个工具输出结构化判断。

**四问扫描：** 位置 → 进度 → 状态 → 下一步

**包含资源：**

- `references/output-templates.md` — 五种工具和完整输出骨架的格式化模板

**适用场景：** 项目中途卡壳、不确定进度、需要汇报状态、风险诊断、下一步行动不明

---

## 目录结构

```
skills/
├── resume-assistant/
│   ├── SKILL.md
│   ├── scripts/
│   │   └── generate_resume.py
│   ├── references/
│   │   └── resume-examples.md
│   └── assets/
│       └── resume-template.html
├── task-handover/
│   ├── SKILL.md
│   ├── references/
│   │   └── examples.md
│   ├── scripts/       (占位)
│   └── assets/        (占位)
├── wayfinder/
│   ├── SKILL.md
│   ├── references/
│   │   └── domain-maps.md
│   ├── scripts/       (占位)
│   └── assets/        (占位)
├── progress-locator/
│   ├── SKILL.md
│   ├── references/
│   │   └── output-templates.md
│   ├── scripts/       (占位)
│   └── assets/        (占位)
├── LICENSE.txt
└── README.md
```

## 安装方式

1. 将整个仓库克隆或下载到本地
2. 把四个 Skill 文件夹（`resume-assistant`、`task-handover`、`wayfinder`、`progress-locator`）放入 Cowork 的 skills 目录
3. 重启或刷新 Cowork 后即可在对话中触发

技能触发方式：在对话中描述你的需求，AI 会根据场景自动匹配对应的 Skill。例如说"帮我改一下简历"，AI 会加载简历助手；说"我现在卡住了不知道进度到哪了"，AI 会加载定位仪。

## 设计理念

四个 Skill 共同遵循的原则：

- **先诊断，后操作** — 不在信息不足时直接给出成品，先充分了解上下文
- **量化优先** — 进度、成果、风险尽量用数字表示，避免模糊描述
- **可接班** — 所有输出都设计为可以被其他人或新会话继续使用
- **结构化输出** — 每个 Skill 都有固定的输出框架，确保质量稳定

## 许可

MIT License
