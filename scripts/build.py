"""Generate the novel-writing catalogue and rankings from reviewed JSON data."""
from __future__ import annotations
import argparse
import csv
from datetime import datetime
import io
import json
from pathlib import Path
import re
from ranking import dt, age_days, score, tier, status, rank, table

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={
    'workspace':'小说创作软件与工作台',
    'automation':'自动写作 Agent 与创作引擎',
    'skills':'长篇创作技能与方法框架',
    'revision':'文风修订、去模板化与质量检查',
    'screenplay':'剧本、短剧改编与影视解说',
    'evaluation':'创意写作评测工具',
}
REVIEW_LABELS={'verified':'开放许可证已核验','unverified':'许可待核验','custom':'存在附加许可说明','source_available':'受限源码许可'}

def validate(projects,seed_references,snapshot):
    assert snapshot['schema_version']==1
    dt(snapshot['as_of'])
    repos=[p['repo'] for p in projects]
    assert len(repos)==len(set(x.lower() for x in repos)), 'Duplicate canonical repo'
    assert set(repos)==set(snapshot['repositories']), 'Snapshot/catalogue mismatch'
    for p in projects:
        assert re.fullmatch(r'[\w.-]+/[\w.-]+',p['repo'])
        assert p['category'] in CATEGORIES and p['scope'] in {'core','adjacent','historical'}
        assert p['description'] and p['boundary'] and p['form'] and p['evidence']
        datetime.strptime(p['reviewed_at'],'%Y-%m-%d')
        for e in p['evidence']:
            assert e['url'].startswith('https://') and e['path'] and e['line']>0
        assert re.fullmatch(r'[a-f0-9]{40}',p['evidence_commit'])
        assert p['license_review']['status'] in REVIEW_LABELS
        m=snapshot['repositories'][p['repo']]
        assert m['canonical_repo'].lower()==p['repo'].lower(), 'Resolve redirects before publishing'
        assert all(type(m[k]) is int and m[k]>=0 for k in ['stars','forks','commits_30d','commits_90d'])
        assert m['commits_30d']<=m['commits_90d']
        dt(m['last_commit_at'])
        assert re.fullmatch(r'[a-f0-9]{40}',m['head_sha'])
    seeds=[s['canonical_repo'] for s in seed_references]
    assert len(seeds)==len(set(seeds)), 'Duplicate seed reference'
    assert set(seeds)=={p['repo'] for p in projects if p['seed']}, 'A user reference is missing'
    assert all(s['status']=='resolved' for s in seed_references)

def render(projects,seeds,snapshot):
    metrics=snapshot['repositories'];as_of=snapshot['as_of'];ordered=rank(projects,metrics,as_of)
    reviewed=max(p['reviewed_at'] for p in projects)
    intro=(ROOT/'docs/readme-intro.md').read_text(encoding='utf-8').strip()
    readme=[intro,f'## 当前收录\n\n**{len(projects)} 个项目，覆盖全部 {len(seeds)} 个去重后的参考项目。** 功能核验：{reviewed}；指标快照：`{as_of}`（UTC）。\n\n每类先按维护状态分层，再综合 star（40%）、90 天提交活动（35%）和最近默认分支提交（25%）排序。归档项目后置。**维护分不代表小说质量、文学水平或一键成书成功率。**',
    '## 分类目录\n\n`★` 表示用户提供的参考项目。每项只有一个主分类；软件、Skill、方法框架与评测工具分开比较。功能介绍来自公开文档，未安装执行第三方项目。']
    overview=[]
    for key,label in CATEGORIES.items():
        group=[p for p in ordered if p['category']==key]
        overview.append([label,len(group),'、'.join(p['name'] for p in group[:3])])
    readme.append(table(['分类','数量','排序靠前的项目'],overview))
    detail=['# 项目说明与证据\n\n文档核验不等于实机测评。来源固定到核验时的 commit，自动刷新 star 不会把功能或许可重新标为已审查。\n']
    for key,label in CATEGORIES.items():
        group=[p for p in ordered if p['category']==key]
        readme.append('### '+label)
        rows=[]
        for p in group:
            m=metrics[p['repo']];review=p['license_review']
            tag=' ★' if p['seed'] else ''
            if tier(p,m,as_of)==3:tag+=' · 归档/历史'
            if review['status']!='verified':tag+=' · 许可注意'
            rows.append([f"[{p['name']}](https://github.com/{p['repo']}){tag}",p['description'],p['form'],f"{m['stars']:,}",f"{m['commits_90d']:,}",m['last_commit_at'][:10],f"{score(m,as_of):.1f}",review['label']])
            links=' · '.join(f"[来源 {i+1}]({e['url']})" for i,e in enumerate(p['evidence']))
            detail.extend([f"## [{p['name']}](https://github.com/{p['repo']})",p['description'],f"- 分类：{label}；形态：{p['form']}。\n- 适用边界：{p['boundary']}\n- 维护状态：{status(p,m,as_of)}；30 天提交 {m['commits_30d']} 次，90 天提交 {m['commits_90d']} 次。\n- 许可：[{review['label']}]({review['source']})；{REVIEW_LABELS[review['status']]}。{review['note']}\n- 功能核验：{p['reviewed_at']}；{links}。"])
        readme.append(table(['项目','用途','形态','Stars','90天提交','最近提交 UTC','维护分','许可'],rows))
    readme.extend(['## 如何选择\n\n- 想先打开软件写作：看小说工作台，比较编辑与审稿体验、模型配置和备份方式。\n- 想把分章写作做成可重复流程：看创作 Agent 与长篇技能，优先检查状态、伏笔和修订机制。\n- 已经有正文，需要改稿：看 Sepia、avoid-ai-writing 等修订工具；一般文章规则不一定适合小说。\n- 想把小说改成短剧：看剧本与改编分类；影视解说不等于原创剧本。\n\n更具体的边界与来源见 [项目详表](docs/projects.md)，创作环节与分类见 [分类标准](docs/taxonomy.md)。',
    '## 排序、数据与维护\n\n- [综合 / Star / 活跃度 / 最近提交排序](docs/rankings.md)\n- [排序公式与局限](docs/methodology.md)\n- [检索过程、项目更名和种子映射](docs/research.md)\n- [数据 JSON](data/projects.json) · [指标 JSON](data/metrics.json) · [排序 CSV](data/rankings.csv)\n- [贡献指南](CONTRIBUTING.md)\n\n```sh\npython scripts/refresh_metrics.py   # 需要 gh 登录或 GH_TOKEN\npython scripts/build.py\npython -m unittest discover -s tests -v\npython scripts/build.py --check\n```\n\nGitHub Actions 每日刷新已收录仓库的指标与排序。新增项目、分类、功能及许可判断经过人工核验后更新。API 查询不完整时保留上一份完整快照。',
    '## 许可与致谢\n\n本目录原创整理与脚本采用 [MIT](LICENSE)，链接到的项目依各自许可。公开源码、README 的开源宣称和 GitHub 识别出的许可证需要结合项目附加说明阅读。未核验的许可不会默认写成 MIT。\n\n排序与更新实现沿用 [awesome_bot](https://github.com/ZanePoe/awesome_bot)。发现线索参考 [Awesome Novel Tools](https://github.com/yutingzhao1991/awesome-novel-tools) 和 [Awesome Novel Skills](https://github.com/UnderleveledBuilder/awesome-novel-skills)，最终介绍回到原始仓库核验。'])
    rankings=[f'# 排序视图\n\n快照：`{as_of}`。这是维护元数据排序，不是写作能力比赛。所有视图先按活跃、较久未更新、长期未更新、归档/历史分层，再按该视图指标降序。同分比较 star 与仓库名。\n\n[公式和限制](methodology.md) · [CSV 原始排序数据](../data/rankings.csv)']
    for mode,label in [('balanced','综合维护分'),('stars','Star 优先'),('activity','90 天提交优先'),('recent','最近默认分支提交优先')]:
        rows=[]
        for p in rank(projects,metrics,as_of,mode):
            m=metrics[p['repo']]
            rows.append([f"[{p['name']}](https://github.com/{p['repo']})",CATEGORIES[p['category']],status(p,m,as_of),m['stars'],m['commits_90d'],m['last_commit_at'][:10],score(m,as_of)])
        rankings.extend(['## '+label,table(['项目','分类','维护层','Stars','90天提交','最近提交 UTC','维护分'],rows)])
    csvbuf=io.StringIO(newline='');writer=csv.writer(csvbuf,lineterminator='\n')
    writer.writerow(['repo','name','category','form','seed','license','license_status','stars','commits_30d','commits_90d','last_commit_at','maintenance_status','score','as_of'])
    for p in ordered:
        m=metrics[p['repo']]
        writer.writerow([p['repo'],p['name'],p['category'],p['form'],p['seed'],p['license_review']['label'],p['license_review']['status'],m['stars'],m['commits_30d'],m['commits_90d'],m['last_commit_at'],status(p,m,as_of),score(m,as_of),as_of])
    return {'README.md':'\n\n'.join(readme)+'\n','docs/projects.md':'\n\n'.join(detail)+'\n','docs/rankings.md':'\n\n'.join(rankings)+'\n','data/rankings.csv':csvbuf.getvalue()}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    read=lambda name:json.loads((ROOT/name).read_text(encoding='utf-8'))
    projects,seeds,snapshot=read('data/projects.json'),read('data/seed-references.json'),read('data/metrics.json')
    validate(projects,seeds,snapshot);outputs=render(projects,seeds,snapshot)
    for name,content in outputs.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=content:raise SystemExit(f'Stale generated file: {name}')
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    print(f'{"Checked" if args.check else "Generated"} {len(outputs)} files; {len(projects)} projects')

if __name__=='__main__':main()
