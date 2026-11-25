# Research log and inclusion decisions

The first release was completed on 2026-11-05: 41 projects across 6 categories, covering all 13 deduplicated reference projects. On 2026-11-06, Reveric was added from a user supplement, bringing the totals to 42 projects and 14 reference projects. This round focused on projects and implementations; related papers were not expanded into a separate paper list.

## Search axes derived from the reference projects

| Direction | English keywords | Chinese keywords |
| --- | --- | --- |
| Complete creation tools | AI novel writer, writing workspace, fiction IDE, local-first | AI 小说写作、小说工作台、桌面码字软件 |
| Long-form automation | long-form fiction, writing agent, novel generator, harness | 长篇生成、分章写作、写作 Agent |
| State and continuity | story bible, character state, foreshadowing, continuity, RAG | 世界观、人物状态、伏笔、连贯性、长期记忆 |
| Agent resources | novel writing skill, workflow, prompt framework | 小说 Skill、网文技能、方法框架 |
| Revision | narrative revision, humanizer, style lint, editing | 叙事修复、去模板化、文风、审稿 |
| Adaptation | screenplay, short drama, story adaptation, narration | 剧本、短剧、小说改编、影视解说 |

## Three search rounds

| Round | Batches | Results | New sources | New-source rate |
| --- | --- | --- | --- | --- |
| 1 | 15 | 331 | 300 | 90.6% |
| 2 | 4 | 127 | 90 | 70.9% |
| 3 | 3 | 17 | 15 | 88.2% |

There were 22 search or verification batches in total, including web search, GitHub native search, curated-directory link harvesting, and bulk verification of repositories and metrics. The source count is the number of URLs in the search ledger — not the number of included projects, and not every candidate was relevant.

Round 1 started from all reference projects and covered eight directions: definitions, original sources, curated directories, repositories, comparisons, evaluations, boundaries and recent changes. A GitHub search for `小说` mixes in readers, downloaders, CMSes and book lists, which were filtered out against the creation-focused goal; `easy-writing` also collides with a same-named development framework, so search rank alone cannot justify inclusion.

Round 2 added directions such as Oh Story, webnovel-writer, NovelClaw and OpenFic, reading official READMEs and telling apart applications, skills and methodologies. Curated directories served as leads; their stars, conference information or effectiveness claims were not copied over.

Round 3 verified renames and license exceptions, reviewed the user-provided Chinese README of Sepia, and added Long-Novel-GPT. Final-project metrics were collected uniformly via the GitHub GraphQL API, with feature sources pinned to commits.

The stopping reason was the preset three-round limit, not "everything has been found" — round 3 still produced new discoveries. Vertical genres, interactive fiction, translation, local writing models and the industry's short-drama tooling were not exhaustively explored. Pure novel-reading, scraping or publishing tools were not force-fitted into the list as writing tools.

## Reference projects, names and deduplication

| User-provided name / former name | Currently listed as |
| --- | --- |
| Denova | [alfredxw/denova](https://github.com/alfredxw/denova) |
| 易创 easy-writing | [yilujian/easy-writing](https://github.com/yilujian/easy-writing) |
| ai-juben | [VanGong1999/juben](https://github.com/VanGong1999/juben), confirmed by the user |
| AI Novel Writer | [Pagekin](https://github.com/EthanYoQ/Pagekin); the repository was renamed and the old address redirects automatically |
| AI Novel Writing Assistant | [Biz Novel Studio](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant), same repository |
| Storyteller | [Dankular/Storyteller](https://github.com/Dankular/Storyteller); the README's current name is novel-harness |
| Duplicate Sepia entries with `-g` | Counted once per repository; the skill was not installed |

All seed mappings are stored in [seed-references.json](../data/seed-references.json). The canonical repository is the deduplication key, and a rename does not add a project. OpenCode ports are listed separately because their host and features differ, with the upstream relationship stated; same-content forks without an explainable difference were not included.

## Corrections to the original documents

- [qifeng-writing](https://github.com/Yuriloll/qifeng-writing) is explicitly centered on Chinese articles and posts, and pure fiction still needs dedicated methods, so it sits in the adjacent revision tools group.
- [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) instructs calling a film-narration CLI; it is not described as an original long-form generator.
- [NeuroBook](https://github.com/notnotype/neuro-book) is rebuilding on v2, and some AI-studio capabilities are listed on the roadmap; the catalogue keeps the preview-version boundary.
- [Novel Studio](https://github.com/bbaz123/novel-studio) has an experimental default branch; the metrics do come from that branch instead of forcing an older main.
- Some of [Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT)'s one-click book capabilities remain in the plan; landing-page slogans are not treated as completed acceptance.
- [Reveric](https://github.com/looplj/reveric) currently uses the `unstable` default branch, and the catalogue reviews that branch. Its `NOTICES` file, under AGPLv3 Section 7, requires modified versions to keep the project attribution and the original-project link, and a commercial-licensing path is offered.

## License verification

GitHub SPDX identification and manual exception checks are stored separately. The LICENSE of Biz Novel Studio contains AGPL plus service-style commercial-authorization notes; the Kimi Writer LICENSE is a text with an extra commercial attribution condition. Both keep their original license links and are not simplified into plain AGPL/MIT.

Agnes explicitly states that no license is declared; for some small writing harnesses, Skills and evaluation repositories no complete license text was located. A README badge or a one-line MIT claim is not enough to mark such entries as license-verified. Current status appears in the [project details](projects.md). This catalogue records the authors' terms and makes no cross-project commercial-use guarantee.

## Content-factory search

The `content-factory-search-api` was reused, calling structured search via curl; the date range was **2026-08-05 to 2026-11-05** with the queries `小说` and `inkos OR sepia OR 小说写作`. Both calls returned valid JSON, but the result arrays were empty. A full-history search was not run, and the empty results were not interpreted as these projects not existing.

When nothing was returned, no vector computation was performed. Final inclusion relies on the original GitHub repositories; private search addresses, keys and internal article bodies never enter the public repository.

## Validation and limits

Feature descriptions are based on official documentation; not all software was installed or run, and no blind evaluation used a fixed model, budget and story prompt. Authors' claims about chapter counts, million-word output, AI-flavor removal or multi-agent gains are not used for capability ranking. This round ran no ablation experiments, so it cannot judge "how much quality drops after removing memory".

Completed: project/seed completeness checks, ranking boundary tests, the stale-snapshot-on-API-failure test, and generated-file consistency checks. Full metric definitions are in [methodology.md](methodology.md).

Public audit material:

- [Search log](../research/search-log.json): queries, rounds and result counts.
- [Inclusion decisions](../research/decisions.json): purpose, boundary, pinned commits and license verification.
- [Baseline coverage](../research/coverage.json): all 14 reference links covered.
- [Initial metrics](../research/initial-metrics.json) and [current metrics](../data/metrics.json): the baseline and the ongoing refresh are kept apart.
- [Status](../research/status.json) and [verification results](../research/verification.json): stopping reasons and known empty results.

Full source texts and tool logs stay local. The public research statistics contain 84 judgments and 123 metric records, traceable through the decision and snapshot files above.
