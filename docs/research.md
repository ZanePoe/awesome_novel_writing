# 检索记录与收录判断

2026-11-05 完成首版：41 个项目、6 个分类，13 个去重参考项目全部覆盖。本轮关注项目与实现，没有把相关论文扩展为独立论文清单。

## 从参考项目归纳的检索轴

| 方向 | 英文关键词 | 中文关键词 |
| --- | --- | --- |
| 完整创作工具 | AI novel writer, writing workspace, fiction IDE, local-first | AI 小说写作、小说工作台、桌面码字软件 |
| 长篇自动化 | long-form fiction, writing agent, novel generator, harness | 长篇生成、分章写作、写作 Agent |
| 状态与连续性 | story bible, character state, foreshadowing, continuity, RAG | 世界观、人物状态、伏笔、连贯性、长期记忆 |
| Agent 资源 | novel writing skill, workflow, prompt framework | 小说 Skill、网文技能、方法框架 |
| 修订 | narrative revision, humanizer, style lint, editing | 叙事修复、去模板化、文风、审稿 |
| 改编 | screenplay, short drama, story adaptation, narration | 剧本、短剧、小说改编、影视解说 |

## 三轮检索

| 轮次 | 批次 | 结果条数 | 新增来源 | 新增来源率 |
| --- | --- | --- | --- | --- |
| 1 | 15 | 331 | 300 | 90.6% |
| 2 | 4 | 127 | 90 | 70.9% |
| 3 | 3 | 17 | 15 | 88.2% |

共 22 个检索或核验批次，包含网页检索、GitHub 原生搜索、精选目录链接采集，以及仓库与指标批量核验。来源数是检索台账的 URL 数量，不是已收录项目数，也不是每个候选都相关。

第一轮从全部参考项目出发，覆盖定义、原始来源、精选目录、仓库、对比、评测、边界与近期变化八个方向。GitHub 搜索 `小说` 会混入阅读器、下载器、CMS 和书单，按创作目标剔除；`easy-writing` 也会混入同名开发框架，不能仅按搜索排名收录。

第二轮补入 Oh Story、webnovel-writer、NovelClaw、OpenFic 等方向，读取官方 README，识别应用、技能和方法论的差异。精选目录用于发现线索，不直接照抄其 star、会议信息或效果结论。

第三轮核验更名、许可证例外、用户提供的 Sepia 中文 README，并补入 Long-Novel-GPT。通过 GitHub GraphQL 统一采集最终项目的指标，固定功能来源提交。

停止原因是预设三轮检索上限，不是“已经穷尽”。第三轮仍有新发现。垂直题材、交互式小说、翻译、本地写作模型及全部行业短剧工具尚未全面展开。纯小说阅读、采集或发布工具未作为写作工具强行填充清单。

## 参考项目、名称与去重

| 用户名称 / 旧称 | 当前收录 |
| --- | --- |
| Denova | [alfredxw/denova](https://github.com/alfredxw/denova) |
| 易创 easy-writing | [yilujian/easy-writing](https://github.com/yilujian/easy-writing) |
| ai-juben | [VanGong1999/juben](https://github.com/VanGong1999/juben)，经用户确认 |
| AI Novel Writer | [书童 Pagekin](https://github.com/EthanYoQ/AI-Novel-Writer)，同一仓库 |
| AI Novel Writing Assistant | [Biz Novel Studio](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant)，同一仓库 |
| Storyteller | [Dankular/Storyteller](https://github.com/Dankular/Storyteller)，README 当前名 novel-harness |
| 重复的 Sepia 与 `-g` | 同一仓库只计一项，未安装技能 |

所有种子映射保存在 [seed-references.json](../data/seed-references.json)。canonical repo 是项目去重键，仓库重命名不新增项目。OpenCode 移植版因宿主与功能不同单列，并说明与上游关系；未收录无明确差异的同内容 fork。

## 原始文档纠错

- [qifeng-writing](https://github.com/Yuriloll/qifeng-writing) 明确以中文文章和推文为中心，纯小说仍需专门方法，因此归入相邻修订工具。
- [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) 指导调用影视解说 CLI，不写成原创长篇生成器。
- [NeuroBook](https://github.com/notnotype/neuro-book) 当前 v2 正在重建，部分 AI 工作室能力列于路线图；目录保留预览版边界。
- [Novel Studio](https://github.com/bbaz123/novel-studio) 的默认分支为实验线，指标确实取该分支，未强行使用旧 main。
- [Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT) 的部分一键成书能力仍列在计划，不能把首页口号当成已完成验收。

## 许可证核验

GitHub SPDX 识别与人工例外检查分开保存。Biz Novel Studio 的 LICENSE 同时包含 AGPL 和服务型商业授权说明；Kimi Writer 的 LICENSE 是带额外商业署名条件的文本。两者保留原文链接，不简化成普通 AGPL/MIT。

Agnes 明确表示未声明许可；部分小型写作 Harness、Skill 和评测仓库未定位到完整许可证。README 徽章或一句 MIT 声明不足以把它们自动标成许可已核验。具体状态见 [项目详表](projects.md)。本目录记录作者条款，不作跨项目可商用保证。

## 内容工厂

沿用 `content-factory-search-api`，通过 curl 调用结构化检索；日期范围 **2026-08-05 至 2026-11-05**，查询 `小说` 与 `inkos OR sepia OR 小说写作`。两组返回成功 JSON，但结果数组为空。未执行全历史检索，也未把空结果解释为这些项目不存在。

没有返回内容时未进行向量计算。最终收录依据 GitHub 原始仓库；私有搜索地址、密钥和内部正文不进入公开仓库。

## 验证与局限

功能介绍依据官方文档，未安装运行全部软件，未用统一模型、预算和故事题做盲评。各作者关于章节数量、百万字、AI 去味与多 Agent 的宣传不用于能力排名。此轮没有组件消融实验，不能判断“移除记忆后质量下降多少”。

完成项目/种子完整性校验、排序边界测试、API 失败保留旧快照测试和生成文件一致性检查。详细指标口径见 [methodology.md](methodology.md)。

公开审计材料：

- [检索日志](../research/search-log.json)：查询、轮次和结果统计。
- [收录决策](../research/decisions.json)：用途、边界、固定提交和许可核验。
- [基线覆盖](../research/coverage.json)：13 个参考链接全部覆盖。
- [首版指标](../research/initial-metrics.json) 与 [当前指标](../data/metrics.json)：初始与持续更新分开。
- [状态](../research/status.json) 与 [完整性结果](../research/verification.json)：停止原因和已知空结果。

完整来源文本和工具日志留在本地。公开研究统计包含 84 条判断和 123 条指标，内容可通过上述决策和快照回查。
