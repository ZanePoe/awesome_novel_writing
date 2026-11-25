"""Generate the multilingual novel-writing catalogue and transparent GitHub rankings."""
from __future__ import annotations
import argparse,csv,io,json,re
from datetime import datetime
from pathlib import Path
from ranking import dt,age_days,score,tier,rank,table
ROOT=Path(__file__).resolve().parents[1]
DEFAULT='en'; MIRRORED=['zh','es','hi','fr']; LOCALES=[DEFAULT,*MIRRORED]
STATIC=['docs/readme-intro.md','docs/taxonomy.md','docs/methodology.md','docs/research.md','CONTRIBUTING.md']
KEYWORD_FILES=['docs/research.md']
CJK=re.compile(r'[\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]')
INLINE=['docs/readme-intro.md']
GENERATED={'README.md','docs/projects.md','docs/rankings.md'}
def ui(locale):
    return json.loads((ROOT/'locales'/locale/'ui.json').read_text(encoding='utf-8'))
def placeholders(template):
    return set(re.findall(r'(?<!\{)\{(\w+)\}(?!\})',template))
def entries(locale,projects):
    """Per-locale wording; Chinese falls back to the canonical reviewed data."""
    if locale=='zh':
        return {p['repo']:{'name':p['name'],'description':p['description'],'form':p['form'],'boundary':p['boundary'],'license_label':p['license_review']['label'],'license_note':p['license_review'].get('note','')} for p in projects}
    raw=json.loads((ROOT/'locales'/locale/'entries.json').read_text(encoding='utf-8'))
    out={}
    for p in projects:
        t=raw[p['repo']]
        out[p['repo']]={'name':t.get('name') or p['name'],'description':t['description'],'form':t['form'],'boundary':t['boundary'],'license_label':t['license_label'],'license_note':t['license_note']}
    return out
def path(locale,name):
    if locale==DEFAULT: return Path(name)
    if name=='README.md': return Path(f'locales/{locale}/README.md')
    return Path(f'locales/{locale}')/name
def prefix(locale,depth=0):
    """`../` count from a generated file to the repository root; depth 1 means the file sits in that locale's docs/. A mirror root is two levels down (locales/<lang>/), English sits at the root."""
    return ('../'*(2+depth)) if locale!=DEFAULT else ('../'*depth)
def anchor(title):
    """GitHub's github-slugger rule: lowercase, drop ASCII punctuation and U+2000-206F/U+2E00-2E7F, spaces to hyphens. Other scripts (CJK punctuation included, Devanagari marks included) survive."""
    drop=set('\\\'!"#$%&()*+,./:;<=>?@[]^`{|}~')
    out=[]
    for ch in title.strip().lower():
        if ch in drop or '\u2000'<=ch<='\u206f' or '\u2e00'<=ch<='\u2e7f':continue
        out.append('-' if ch==' ' else ch)
    return ''.join(out)
def switcher(langs,locale):
    items=[]
    for code,name in langs:
        if code==locale: items.append(f'**{name}**')
        elif code==DEFAULT: items.append(f'[{name}]({"README.md" if locale==DEFAULT else "../../README.md"})')
        elif locale==DEFAULT: items.append(f'[{name}](locales/{code}/README.md)')
        else: items.append(f'[{name}](../{code}/README.md)')
    return '🌐 '+' · '.join(items)
def validate(projects,seed_references,snapshot):
    u=ui('zh');repos=[p['repo'] for p in projects]
    assert snapshot['schema_version']==1;dt(snapshot['as_of'])
    assert len(repos)==len(set(x.lower() for x in repos));assert set(repos)==set(snapshot['repositories'])
    for p in projects:
        assert re.fullmatch(r'[\w.-]+/[\w.-]+',p['repo']);assert p['category'] in u['categories'] and p['scope'] in u['scopes'];assert p['description'] and p['boundary'] and p['form'] and p['evidence']
        datetime.strptime(p['reviewed_at'],'%Y-%m-%d');assert re.fullmatch(r'[a-f0-9]{40}',p['evidence_commit']);assert p['license_review']['status'] in u['license_status']
        for e in p['evidence']:assert e['url'].startswith('https://') and e['path'] and e['line']>0
        m=snapshot['repositories'][p['repo']];assert m['canonical_repo'].lower()==p['repo'].lower(),'Resolve redirects before publishing';assert all(type(m[k]) is int and m[k]>=0 for k in ['stars','forks','commits_30d','commits_90d']);assert m['commits_30d']<=m['commits_90d'];dt(m['last_commit_at'])
        assert re.fullmatch(r'[a-f0-9]{40}',m['head_sha'])
    seeds=[s['canonical_repo'] for s in seed_references]
    assert len(seeds)==len(set(seeds)),'Duplicate seed reference';assert set(seeds)=={p['repo'] for p in projects if p['seed']},'A user reference is missing';assert all(s['status']=='resolved' for s in seed_references)
    for f in STATIC: assert (ROOT/f).exists(), 'missing English static document: '+f
    def keys(value,base=''):
        if isinstance(value,dict): return sorted(k for child in [keys(value[k],base+'/'+k) for k in value] for k in child)
        return [base or '.']
    canonical={p['repo']:p['name'] for p in projects}
    shape=keys(u['templates'])
    for locale in MIRRORED:
        if locale=='zh': continue
        other=ui(locale)
        assert set(other)==set(u),'ui.json top-level keys differ for '+locale
        assert other['language']==locale and other['list_separator'].strip()
        assert keys(other['templates'])==shape, 'template keys differ for '+locale
        assert set(other['categories'])==set(u['categories']) and set(other['scopes'])==set(u['scopes']) and set(other['license_status'])==set(u['license_status']) and set(other['modes'])==set(u['modes'])
        assert len(other['tiers'])==4 and set(other['headers'])==set(u['headers']) and set(other['sections'])==set(u['sections']) and set(other['tags'])==set(u['tags'])
        for name,tmpl in other['templates'].items():
            assert placeholders(tmpl)==placeholders(u['templates'][name]),'placeholders differ for %s/%s' % (locale,name)
        assert not CJK.search(json.dumps({k:v for k,v in other.items() if k in ('categories','scopes','license_status','modes','tiers','headers','sections','tags','templates')},ensure_ascii=False)),'untranslated Chinese remains in '+locale+' ui.json'
        raw=json.loads((ROOT/'locales'/locale/'entries.json').read_text(encoding='utf-8'))
        assert set(raw)==set(repos),'entry coverage differs for '+locale
        for repo,t in raw.items():
            assert set(t)>={'description','form','boundary','license_label','license_note'} and all(str(t[k]).strip() for k in ('description','form','boundary','license_label','license_note')),'incomplete entry: %s %s' % (locale,repo)
            assert not CJK.search(json.dumps(t,ensure_ascii=False)),'untranslated Chinese remains in %s %s' % (locale,repo)
            if CJK.search(canonical[repo]):
                assert t.get('name'),'missing localized display name for %s %s' % (locale,repo)
        for f in STATIC: assert (ROOT/'locales'/locale/f).exists(),'missing %s static document: %s' % (locale,f)
    check_links()
def check_links():
    """Prose links resolve from the file's own directory; the inlined readme intro resolves from the locale root."""
    bad=[]
    for locale in LOCALES:
        base=ROOT if locale==DEFAULT else ROOT/'locales'/locale
        pending={(base/name).resolve() for name in GENERATED}
        for rel in STATIC:
            origin=base if rel in INLINE else base/Path(rel).parent
            for href in re.findall(r'\]\((?!https?:|#)([^)#]+?)(?:#[^)]*)?\)',(base/rel).read_text(encoding='utf-8')):
                target=(origin/href).resolve()
                if target in pending or target.exists():continue
                bad.append('%s:%s -> %s' % (locale,rel,href))
    assert not bad,'broken relative links: '+', '.join(bad)
def render(locale,u,words,projects,seeds,snapshot):
    m=snapshot['repositories'];asof=snapshot['as_of'];reviewed=max(p['reviewed_at'] for p in projects);ordered=rank(projects,m,asof);R=prefix(locale)
    cat=u['categories'];lic_status=u['license_status'];tags=u['tags'];T=u['templates'];S=u['sections']
    intro=(ROOT/('docs/readme-intro.md' if locale==DEFAULT else f'locales/{locale}/docs/readme-intro.md')).read_text(encoding='utf-8').strip()
    nav='## '+S['tags']+'\n\n'+' · '.join(f'[{label}](#{anchor(label)})' for label in cat.values())
    readme=[intro,nav,f'## {S["current"]}\n\n'+T['current'].format(total=len(projects),seeds=len(seeds),reviewed=reviewed,as_of=asof),f'## {S["toc"]}\n\n'+T['toc_note']]
    readme.append(table(u['headers']['categories'],[[label,len([p for p in ordered if p['category']==k]),u['list_separator'].join(words[p['repo']]['name'] for p in [x for x in ordered if x['category']==k][:3])] for k,label in cat.items()]))
    detail=[f'# {S["detail_title"]}\n\n'+T['detail_intro']+'\n']
    for k,label in cat.items():
        group=[p for p in ordered if p['category']==k];readme.append('### '+label);rows=[]
        for p in group:
            x=m[p['repo']];lic=p['license_review'];w=words[p['repo']];tag=''
            if p['seed']:tag=' '+tags['baseline']
            if tier(p,x,asof)==3:tag+=' · '+tags['archived']
            if lic['status']!='verified':tag+=' · '+tags['license']
            rows.append([f"[{w['name']}](https://github.com/{p['repo']}){tag}",w['description'],w['form'],f"{x['stars']:,}",f"{x['commits_90d']:,}",x['last_commit_at'][:10],f"{score(x,asof):.1f}",w['license_label']])
            links=' · '.join(f"[{T['source_link'].format(index=i+1)}]({e['url']})" for i,e in enumerate(p['evidence']))
            body=T['entry'].format(category=label,form=w['form'],boundary=w['boundary'],maintenance=u['tiers'][tier(p,x,asof)],commits_30d=x['commits_30d'],commits_90d=x['commits_90d'],license=w['license_label'],license_source=lic['source'],license_status=lic_status[lic['status']],license_note=w['license_note'],reviewed_at=p['reviewed_at'],sources=links)
            detail.extend([f"## [{w['name']}](https://github.com/{p['repo']})",w['description'],body])
        readme.append(table(u['headers']['detail'],rows))
    readme.extend([f'## {S["choose"]}\n\n'+T['choose'],f'## {S["data"]}\n\n'+T['data'].format(R=R),f'## {S["thanks"]}\n\n'+T['thanks'].format(R=R),T['records_note'].format(R=R)])
    rankings=[f'# {S["rankings_title"]}\n\n'+T['rankings_intro'].format(as_of=asof,R=prefix(locale,1))]
    for mode in ['balanced','stars','activity','recent']:
        rows=[]
        for p in rank(projects,m,asof,mode):
            x=m[p['repo']];rows.append([f"[{words[p['repo']]['name']}](https://github.com/{p['repo']})",cat[p['category']],u['tiers'][tier(p,x,asof)],x['stars'],x['commits_90d'],x['last_commit_at'][:10],score(x,asof)])
        rankings.extend(['## '+u['modes'][mode],table(u['headers']['rankings'],rows)])
    return {'README.md':'\n\n'.join(readme)+'\n','docs/projects.md':'\n\n'.join(detail)+'\n','docs/rankings.md':'\n\n'.join(rankings)+'\n'}
def csv_snapshot(projects,snapshot):
    m=snapshot['repositories'];asof=snapshot['as_of']
    buf=io.StringIO(newline='');w=csv.writer(buf,lineterminator='\n')
    w.writerow(['repo','name','category','form','seed','license','license_status','stars','commits_30d','commits_90d','last_commit_at','maintenance_tier','score','as_of'])
    for p in rank(projects,m,asof):
        x=m[p['repo']];w.writerow([p['repo'],p['name'],p['category'],p['form'],p['seed'],p['license_review']['label'],p['license_review']['status'],x['stars'],x['commits_30d'],x['commits_90d'],x['last_commit_at'],tier(p,x,asof),score(x,asof),asof])
    return buf.getvalue()
def render_all(projects,seeds,snapshot):
    u={locale:ui(locale) for locale in LOCALES};langs=[(locale,u[locale]['language_name']) for locale in LOCALES];out={}
    for locale in LOCALES:
        files=render(locale,u[locale],entries(locale,projects),projects,seeds,snapshot)
        for name,content in files.items():
            out[path(locale,name).as_posix()]=content
        key=path(locale,'README.md').as_posix()
        out[key]=switcher(langs,locale)+'\n\n'+out[key]
    out['data/rankings.csv']=csv_snapshot(projects,snapshot)
    return out
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');a=ap.parse_args();read=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'));projects,seeds,snapshot=read('data/projects.json'),read('data/seed-references.json'),read('data/metrics.json');validate(projects,seeds,snapshot);out=render_all(projects,seeds,snapshot)
    for name,content in out.items():
        fp=ROOT/name
        if a.check:
            if not fp.exists() or fp.read_text(encoding='utf-8')!=content:raise SystemExit('Stale generated file: '+name)
        else:fp.parent.mkdir(parents=True,exist_ok=True);fp.write_text(content,encoding='utf-8')
    print(('Checked' if a.check else 'Generated'),len(out),'files;',len(projects),'projects;',len(LOCALES),'locales')
if __name__=='__main__':main()
