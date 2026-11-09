# awesome_novel_writing

**AI 小说写作、长篇创作 Agent、写作技能、文风修订与剧本改编项目合集。**

Curated AI novel-writing apps, long-form fiction agents, writing skills, revision tools, and screenplay workflows — with evidence-linked descriptions and reproducible GitHub maintenance rankings.

从灵感、设定与大纲，到章节、连续性检查、修订和改编，按实际创作环节寻找工具。收录重心是 GitHub 上可查看实现的项目，同时明确标注许可待核验与附加许可条件。

[分类目录](#分类目录) · [项目详表](docs/projects.md) · [排序视图](docs/rankings.md) · [方法](docs/methodology.md) · [检索记录](docs/research.md) · [贡献](CONTRIBUTING.md)

```mermaid
flowchart LR
    A[灵感 / 世界观 / 人物] --> B[大纲 / 章节计划]
    B --> C[章节写作]
    C --> D[事实 / 伏笔 / 连续性检查]
    D --> E[文风修订 / 人工审稿]
    E --> C
    E --> F[剧本改编 / 影视解说]
```

图示是选型路径，各项目的覆盖范围不同。首版为精选起点，不声称穷尽全部项目；star 和开发活动不等于作品质量。

## 当前收录

**42 个项目，覆盖全部 14 个去重后的参考项目。** 功能核验：2026-11-06；指标快照：`2026-11-09T08:35:46+00:00`（UTC）。

每类先按维护状态分层，再综合 star（40%）、90 天提交活动（35%）和最近默认分支提交（25%）排序。归档项目后置。**维护分不代表小说质量、文学水平或一键成书成功率。**

## 分类目录

`★` 表示用户提供的参考项目。每项只有一个主分类；软件、Skill、方法框架与评测工具分开比较。功能介绍来自公开文档，未安装执行第三方项目。

| 分类 | 数量 | 排序靠前的项目 |
| --- | --- | --- |
| 小说创作软件与工作台 | 17 | Biz Novel Studio、书童 Pagekin、StoryForge 故事熔炉 |
| 自动写作 Agent 与创作引擎 | 6 | InkOS、Openwrite、novel-harness / Storyteller |
| 长篇创作技能与方法框架 | 7 | Oh Story、webnovel-writer、chinese-novelist |
| 文风修订、去模板化与质量检查 | 6 | avoid-ai-writing、Sepia、Humanizer |
| 剧本、短剧改编与影视解说 | 5 | drama-skills、shuohao-skills、juben / ai-juben |
| 创意写作评测工具 | 1 | Longform Writing Bench |

### 小说创作软件与工作台

| 项目 | 用途 | 形态 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Biz Novel Studio](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant) ★ · 许可注意 | 围绕世界、角色、逐章写作与检查组织整本小说生产。 | 桌面 / 自托管工作台 | 3,404 | 608 | 2026-11-09 | 88.2 | AGPL-3.0 + 商用附加说明 |
| [书童 Pagekin](https://github.com/EthanYoQ/Pagekin) ★ | 从设定、章节蓝图到正文、审稿与修订的长篇写作工作台。 | 桌面应用 | 2,479 | 3,386 | 2026-11-09 | 87.1 | GPL-3.0 |
| [StoryForge 故事熔炉](https://github.com/yuanbw2025/storyforge) | 覆盖小说创作、故事改编与互动体验的本地优先叙事工具。 | 创作工作台 | 1,004 | 2,247 | 2026-11-08 | 83.8 | MIT |
| [Denova](https://github.com/alfredxw/denova) ★ | 把小说、互动故事、资料库和 Agent 工具放进同一工作区。 | 创作平台 | 994 | 454 | 2026-11-09 | 83.4 | Apache-2.0 |
| [NeuroBook](https://github.com/notnotype/neuro-book) | 用编辑器、项目文件与可扩展工具组织长篇写作。 | 创作 IDE / 预览版 | 777 | 5,103 | 2026-11-07 | 82.7 | AGPL-3.0 |
| [Goink](https://github.com/sigpanic/goink) | 结合 Agent 写作决策、结构化记忆和写后状态检查的写作系统。 | 桌面应用 | 512 | 543 | 2026-11-08 | 81.5 | AGPL-3.0 |
| [Reveric 幻界](https://github.com/looplj/reveric) ★ · 许可注意 | 以智能体连接长篇小说、剧本改编、分镜、3D 导演台和剪辑流程的桌面创作工作台。 | 本地优先桌面创作工作台 | 735 | 124 | 2026-11-09 | 75.1 | AGPL-3.0 + Section 7 署名要求 |
| [OpenFic](https://github.com/syrizelink/OpenFic) | 用设定、角色和可定制 Prompt / Agent 工作流支持长篇共创。 | 跨平台应用 | 1,292 | 145 | 2026-10-28 | 74.9 | Apache-2.0 |
| [易创 easy-writing](https://github.com/yilujian/easy-writing) ★ | 本地章节编辑、码字统计、AI 辅助创作与作品管理。 | 桌面应用 | 855 | 33 | 2026-11-03 | 66.8 | AGPL-3.0 |
| [AI Novel Generator](https://github.com/YILING0013/AI_NovelGenerator) | 把人物、关系、故事计划和正文放在项目里，生成候选后由人审阅保存。 | 本地工作台 | 6,428 | 5 | 2026-11-05 | 64.5 | AGPL-3.0 |
| [Vela](https://github.com/heider-x/vela) | 把大纲、起草、重写和审阅与本地 RAG 资料库结合。 | 桌面 IDE | 589 | 24 | 2026-10-19 | 60.1 | GPL-3.0 |
| [Novel Studio](https://github.com/bbaz123/novel-studio) | 编辑器结合故事设定、角色状态、伏笔管理与连续性检查。 | 本地 Web 工作台 | 7 | 189 | 2026-10-25 | 58.0 | MIT |
| [51mazi 我要码字](https://github.com/xiaoshengxianjun/51mazi) | 小说编辑与创作辅助工具，包含 AI 写作及创作素材能力。 | 桌面应用 | 495 | 13 | 2026-08-31 | 47.9 | MIT |
| [NovelClaw](https://github.com/iLearn-Lab/NovelClaw) | 以章节草稿、可检查运行、审稿和可编辑记忆组织长期创作。 | 自托管工作台 | 373 | 3 | 2026-10-12 | 46.7 | MIT |
| [青烛 ai-novelist](https://github.com/FlickeringLamp/ai-novelist) | 探索工具调用与人在回路的 AI 文本共创。 | 桌面创作工具 | 226 | 0 | 2026-07-25 | 26.5 | MIT |
| [xnovelist](https://github.com/giapnguyen74/xnovelist) | 在浏览器本地组织文稿，自选模型提供 AI 写作辅助。 | 浏览器本地应用 | 12 | 0 | 2026-06-08 | 13.4 | MIT |
| [Agnes Creative OS](https://github.com/MXD706/agnes) · 许可注意 | 覆盖世界观、角色、剧情、章节、审查与长期记忆的小说工作台。 | 本地工作台 | 3 | 0 | 2026-05-27 | 8.8 | 待核验 |

### 自动写作 Agent 与创作引擎

| 项目 | 用途 | 形态 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [InkOS](https://github.com/Narcooo/inkos) ★ | 支持故事规划、写作、审稿和修订的创作 Agent 系统。 | 创作 Agent / 工作台 | 11,074 | 131 | 2026-10-24 | 80.7 | AGPL-3.0 |
| [Openwrite](https://github.com/LiPu-jpg/Openwrite) | 以 AI 工作流组织小说创作、文风处理和内容审核。 | 创作引擎 | 935 | 253 | 2026-11-08 | 79.7 | Apache-2.0 |
| [novel-harness / Storyteller](https://github.com/Dankular/Storyteller) · 许可注意 | 用故事设定、情节点、伏笔账本与连续性记录支持长篇分章写作。 | 写作 Harness | 0 | 7 | 2026-09-12 | 24.9 | 待核验 |
| [Novelist Agent](https://github.com/AxolDad/novelist) · 许可注意 | 用数据库记忆与多路审稿机制维护长篇中的人物、情节和语调。 | Agent 系统 / Alpha | 2 | 0 | 2026-01-06 | 4.7 | 待核验 |
| [Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT) · 许可注意 | 以大纲、章节与正文的分层扩写组织长篇小说生成。 | 长篇生成器 / Agent | 1,253 | 0 | 2025-11-05 | 25.2 | 待核验 |
| [Kimi Writing Agent](https://github.com/Doriandarko/kimi-writer) · 许可注意 | 使用模型规划、写作、管理文件并从上下文摘要恢复长篇创作。 | CLI / Agent | 597 | 0 | 2025-11-08 | 22.6 | MIT + 商用署名条款 |

### 长篇创作技能与方法框架

| 项目 | 用途 | 形态 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Oh Story](https://github.com/zenstory-ai/oh-story-claudecode) | 覆盖网文研究、拆文、长短篇写作与修订的技能工作流。 | Agent 技能包 | 8,444 | 152 | 2026-11-09 | 84.7 | MIT |
| [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | 用分层规划、故事状态与检索支持长篇网文连载。 | Agent 插件 / 技能 | 7,911 | 18 | 2026-11-07 | 72.2 | GPL-3.0 |
| [chinese-novelist](https://github.com/PenglongHuang/chinese-novelist-skill) ★ | 通过问答、创作记忆和章节约束辅助中文小说创作。 | Agent Skill | 4,695 | 30 | 2026-11-01 | 71.6 | MIT |
| [webnovel-writer-opencode](https://github.com/lujih/webnovel-writer-opencode) | 将长篇网文工作流适配到 OpenCode，并增加写作管理能力。 | OpenCode 移植 / 扩展 | 226 | 190 | 2026-11-01 | 71.4 | GPL-3.0 |
| [FuFu 小说创作助手](https://github.com/usagifufu/FuFu-Novel-Writing) · 许可注意 | 组织研究、世界观、大纲、伏笔、章节和审校的长篇写作流程。 | WorkBuddy 技能包 | 4 | 12 | 2026-10-19 | 39.8 | 待核验 |
| [novel-writing-framework](https://github.com/LAY-lgtm/novel-writing-framework) ★ | 把大纲、逐章写作、自检和平台适配整理成工程化写作方法。 | 方法论 / Agent 技能 | 268 | 0 | 2026-05-31 | 23.6 | MIT |
| [long-novel-writer](https://github.com/jiaw-Zh/long-novel-writer) · 许可注意 | 围绕分层摘要和故事事实管理组织长期连载。 | 长篇写作 Skill | 94 | 0 | 2026-05-15 | 19.3 | 待核验 |

### 文风修订、去模板化与质量检查

| 项目 | 用途 | 形态 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) ★ | 诊断并改写模板化 AI 文风，提供仅检测和原地编辑等模式。 | Agent Skill / 检查工具 | 5,502 | 499 | 2026-11-05 | 88.8 | MIT |
| [Sepia](https://github.com/Nanako0129/sepia) ★ | 先修复小说叙事结构，再处理词句；其他文体按场合采用规则。 | Agent Skill | 3,694 | 389 | 2026-11-03 | 85.5 | MIT |
| [Humanizer](https://github.com/blader/humanizer) | 根据常见 AI 写作特征检查并改写文本。 | 英文润色 Skill | 66,773 | 60 | 2026-10-28 | 83.6 | MIT |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 以中文化规则识别和修订机械、空泛的 AI 表达模式。 | 中文润色 Skill | 22,335 | 1 | 2026-09-23 | 53.5 | MIT |
| [qifeng-writing](https://github.com/Yuriloll/qifeng-writing) ★ | 诊断中文推文和文章的事实、结构、叙事与语言问题。 | 中文写作 Skill | 40 | 2 | 2026-08-31 | 30.6 | MIT |
| [llmlint](https://github.com/notnotype/llmlint) | 用规则扫描写作痕迹，为修订提供可定位的问题。 | 文本规则检查器 | 13 | 3 | 2026-08-15 | 26.6 | AGPL-3.0 |

### 剧本、短剧改编与影视解说

| 项目 | 用途 | 形态 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [drama-skills](https://github.com/zenstory-ai/drama-skills) | 围绕短剧故事开发、剧本、资产与分镜组织创作流程。 | 短剧技能包 | 3,977 | 346 | 2026-11-08 | 86.4 | MIT |
| [shuohao-skills](https://github.com/eternityspring/shuohao-skills) ★ | 从小说改编大纲、人物和剧本延伸到场面调度与分镜交付。 | 短剧制作技能包 | 6,311 | 104 | 2026-10-26 | 78.0 | Apache-2.0 |
| [juben / ai-juben](https://github.com/VanGong1999/juben) ★ | 以专业 Agent 工作流辅助影视策划、剧本创作与评估。 | 剧本 Agent 平台 | 182 | 5 | 2026-10-19 | 48.0 | MIT |
| [ai-short-drama](https://github.com/Hao0321/ai-short-drama) | 面向 AI 短剧的剧情设计与剧本创作技能。 | 编剧 Skill | 81 | 1 | 2026-08-13 | 28.6 | MIT |
| [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) ★ | 指导 Agent 调用 CLI 完成影视解说制作。 | CLI 配套 Skill | 3,187 | 0 | 2026-07-05 | 34.1 | MIT |

### 创意写作评测工具

| 项目 | 用途 | 形态 | Stars | 90天提交 | 最近提交 UTC | 维护分 | 许可 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Longform Writing Bench](https://github.com/EQ-bench/longform-writing-bench) · 许可注意 | 评测模型的创意规划、修改与短中篇故事生成。 | 研究 / 评测工具 | 47 | 0 | 2025-10-26 | 13.8 | 待核验 |

## 如何选择

- 想先打开软件写作：看小说工作台，比较编辑与审稿体验、模型配置和备份方式。
- 想把分章写作做成可重复流程：看创作 Agent 与长篇技能，优先检查状态、伏笔和修订机制。
- 已经有正文，需要改稿：看 Sepia、avoid-ai-writing 等修订工具；一般文章规则不一定适合小说。
- 想把小说改成短剧：看剧本与改编分类；影视解说不等于原创剧本。

更具体的边界与来源见 [项目详表](docs/projects.md)，创作环节与分类见 [分类标准](docs/taxonomy.md)。

## 排序、数据与维护

- [综合 / Star / 活跃度 / 最近提交排序](docs/rankings.md)
- [排序公式与局限](docs/methodology.md)
- [检索过程、项目更名和种子映射](docs/research.md)
- [数据 JSON](data/projects.json) · [指标 JSON](data/metrics.json) · [排序 CSV](data/rankings.csv)
- [贡献指南](CONTRIBUTING.md)

```sh
python scripts/refresh_metrics.py   # 需要 gh 登录或 GH_TOKEN
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

GitHub Actions 每日刷新已收录仓库的指标与排序。新增项目、分类、功能及许可判断经过人工核验后更新。API 查询不完整时保留上一份完整快照。

## 许可与致谢

本目录原创整理与脚本采用 [MIT](LICENSE)，链接到的项目依各自许可。公开源码、README 的开源宣称和 GitHub 识别出的许可证需要结合项目附加说明阅读。未核验的许可不会默认写成 MIT。

排序与更新实现沿用 [awesome_bot](https://github.com/ZanePoe/awesome_bot)。发现线索参考 [Awesome Novel Tools](https://github.com/yutingzhao1991/awesome-novel-tools) 和 [Awesome Novel Skills](https://github.com/UnderleveledBuilder/awesome-novel-skills)，最终介绍回到原始仓库核验。
