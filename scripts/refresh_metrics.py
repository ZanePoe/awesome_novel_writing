"""Refresh public GitHub metadata atomically; requires authenticated gh (or GH_TOKEN)."""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def fetch_batch(repos: list[str], now: datetime) -> dict:
    since30 = (now - timedelta(days=30)).isoformat()
    since90 = (now - timedelta(days=90)).isoformat()
    fields = []
    for i, repo in enumerate(repos):
        owner, name = repo.split('/')
        fields.append(f'''r{i}: repository(owner:{json.dumps(owner)},name:{json.dumps(name)}) {{
          nameWithOwner url stargazerCount forkCount isArchived isDisabled pushedAt updatedAt
          licenseInfo {{ spdxId name }}
          defaultBranchRef {{ name target {{ ... on Commit {{ oid committedDate
            c30: history(since:{json.dumps(since30)},until:{json.dumps(now.isoformat())}) {{ totalCount }}
            c90: history(since:{json.dumps(since90)},until:{json.dumps(now.isoformat())}) {{ totalCount }}
          }} }} }}
          releases(first:1,orderBy:{{field:CREATED_AT,direction:DESC}}) {{ nodes {{ tagName publishedAt isPrerelease }} }}
        }}''')
    payload = json.dumps({'query': 'query { ' + '\n'.join(fields) + ' }'})
    p = subprocess.run(['gh', 'api', 'graphql', '--input', '-'], input=payload,
                       capture_output=True, text=True, encoding='utf-8', timeout=120)
    if p.returncode:
        raise RuntimeError('GitHub query failed: ' + p.stderr.strip())
    response = json.loads(p.stdout)
    if response.get('errors'):
        raise RuntimeError('GitHub returned partial data: ' + json.dumps(response['errors']))
    output = {}
    for i, repo in enumerate(repos):
        r = response['data'].get(f'r{i}')
        if not r or not r.get('defaultBranchRef'):
            raise RuntimeError(f'{repo}: missing repository or default branch; previous snapshot preserved')
        branch = r['defaultBranchRef']
        commit = branch['target']
        output[repo] = {
            'canonical_repo': r['nameWithOwner'], 'url': r['url'],
            'stars': r['stargazerCount'], 'forks': r['forkCount'],
            'archived': r['isArchived'], 'disabled': r['isDisabled'],
            'license_spdx': (r['licenseInfo'] or {}).get('spdxId'),
            'license_name': (r['licenseInfo'] or {}).get('name'),
            'default_branch': branch['name'], 'head_sha': commit['oid'],
            'last_commit_at': commit['committedDate'],
            'commits_30d': commit['c30']['totalCount'], 'commits_90d': commit['c90']['totalCount'],
            'pushed_at': r['pushedAt'], 'updated_at': r['updatedAt'],
            'latest_release': next(iter(r['releases']['nodes']), None),
            'collected_at': now.isoformat(),
            'source': 'https://api.github.com/graphql',
        }
    return output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'data/metrics.json')
    args = parser.parse_args()
    projects = json.loads((ROOT / 'data/projects.json').read_text(encoding='utf-8'))
    repos = [p['repo'] for p in projects]
    now = datetime.now(timezone.utc).replace(microsecond=0)
    result = {}
    for start in range(0, len(repos), 8):
        result.update(fetch_batch(repos[start:start+8], now))
        print(f'Fetched {len(result)}/{len(repos)} repositories', file=sys.stderr)
    snapshot = {'schema_version': 1, 'as_of': now.isoformat(), 'window_days': [30, 90], 'repositories': result}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temp = args.output.with_suffix('.tmp')
    temp.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(args.output)
    print(f'Saved {len(result)} repositories to {args.output.name}')

if __name__ == '__main__':
    main()
