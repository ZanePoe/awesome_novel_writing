# 贡献指南

欢迎新增项目、修正分类或补充版本与许可证据。低 star 不是拒绝理由。

1. 修改 `data/projects.json`，不要手工修改生成的 README 表格。
2. 提供 canonical GitHub 地址、用途、项目形态、适用边界及固定提交的证据链接。
3. 选择一个主分类。相邻的通用写作工具需说明与小说的关系，不把软件、Skill 与研究基准混为一谈。
4. 区分已实现、开发预览和 roadmap。模型效果、目标字数与作者自报基准不得写成独立验证结论。
5. 核验许可证，附加商用说明与许可缺口必须保留。公开可见不自动等于 MIT。
6. fork 或移植版只有在宿主、功能或维护路线存在可解释差异时单独收录，并写明来源关系。
7. 新增项目后重新获取完整指标快照并生成文档：

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

`data/seed-references.json` 记录初始参考项目，通常不随普通贡献更改。每次人工功能核验需更新日期和 evidence commit；自动 star 刷新不更新这些字段。

不要提交模型密钥、私有搜索地址、未公开稿件或内部文章正文。调研总结保存在 `record/YYYY-MM-DD-中文标题.md`。
