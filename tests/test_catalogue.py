import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import build
import refresh_metrics

class RankingTests(unittest.TestCase):
    def metric(self, **kw):
        result=dict(stars=100,commits_90d=10,last_commit_at='2026-11-01T00:00:00Z',archived=False,disabled=False)
        result.update(kw); return result
    def test_monotonic_and_bounded(self):
        now='2026-11-05T00:00:00Z';m=self.metric()
        base=build.score(m,now)
        for update in [dict(stars=1000),dict(commits_90d=100),dict(last_commit_at=now)]:
            self.assertGreater(build.score(self.metric(**update),now),base)
        self.assertEqual(build.score(self.metric(stars=10**9,commits_90d=10**9,last_commit_at=now),now),100)
        self.assertGreaterEqual(build.score(self.metric(stars=0,commits_90d=0),now),0)
    def test_archive_cannot_win_with_stars(self):
        ps=[dict(repo='x/big',scope='core'),dict(repo='x/small',scope='core')]
        ms={'x/big':self.metric(stars=999999,archived=True),'x/small':self.metric(stars=1)}
        for mode in ['balanced','stars','activity','recent']:
            self.assertEqual(build.rank(ps,ms,'2026-11-05T00:00:00Z',mode)[0]['repo'],'x/small')
    def test_default_branch_date_controls_tier(self):
        p=dict(scope='core');m=self.metric(last_commit_at='2025-01-01T00:00:00Z',updated_at='2026-11-05T00:00:00Z',pushed_at='2026-11-05T00:00:00Z')
        self.assertEqual(build.tier(p,m,'2026-11-05T00:00:00Z'),2)
    def test_timezone_and_future_clamp(self):
        self.assertEqual(build.age_days(self.metric(last_commit_at='2026-11-05T08:00:00+08:00'),'2026-11-05T00:00:00Z'),0)
        self.assertEqual(build.age_days(self.metric(last_commit_at='2026-11-06T00:00:00Z'),'2026-11-05T00:00:00Z'),0)
    def test_deterministic_tie(self):
        ps=[dict(repo='z/b',scope='core'),dict(repo='a/b',scope='core')]
        self.assertEqual(build.rank(ps,{p['repo']:self.metric() for p in ps},'2026-11-05T00:00:00Z')[0]['repo'],'a/b')

class IntegrityTests(unittest.TestCase):
    def test_catalogue_and_snapshot(self):
        read=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'))
        build.validate(read('data/projects.json'),read('data/seed-references.json'),read('data/metrics.json'))
    def test_partial_refresh_preserves_old_snapshot(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir()
            (root/'data/projects.json').write_text(json.dumps([{'repo':f'x/r{i}'} for i in range(9)]),encoding='utf-8')
            out=root/'data/metrics.json';out.write_text('old-good-snapshot',encoding='utf-8')
            with patch.object(refresh_metrics,'ROOT',root), patch.object(sys,'argv',['refresh','--output',str(out)]), patch.object(refresh_metrics,'fetch_batch',side_effect=[{'x/r0':{}},RuntimeError('partial failure')]):
                with self.assertRaises(RuntimeError):refresh_metrics.main()
            self.assertEqual(out.read_text(encoding='utf-8'),'old-good-snapshot')
    def test_graphql_errors_not_accepted_as_success(self):
        from datetime import datetime,timezone
        from types import SimpleNamespace
        response=SimpleNamespace(returncode=0,stdout=json.dumps({'data':{'r0':None},'errors':[{'message':'rate limited'}]}),stderr='')
        with patch.object(refresh_metrics.subprocess,'run',return_value=response):
            with self.assertRaises(RuntimeError):refresh_metrics.fetch_batch(['x/repo'],datetime.now(timezone.utc))

    def test_vanished_repository_is_carried_forward(self):
        from datetime import datetime,timezone
        from types import SimpleNamespace
        now=datetime.now(timezone.utc).replace(microsecond=0)
        previous={'x/gone':{'canonical_repo':'x/gone','url':'https://github.com/x/gone','stars':10,'forks':1,'archived':False,'disabled':False,'license_spdx':'MIT','license_name':'MIT License','default_branch':'main','head_sha':'a'*40,'last_commit_at':'2026-11-01T00:00:00Z','commits_30d':1,'commits_90d':2,'pushed_at':'2026-11-01T00:00:00Z','updated_at':'2026-11-01T00:00:00Z','latest_release':None,'collected_at':'2026-11-20T00:00:00+00:00','source':'https://api.github.com/graphql'}}
        failed=SimpleNamespace(returncode=1,stdout='',stderr="gh: Could not resolve to a Repository with the name 'x/gone'.")
        live={'nameWithOwner':'x/live','url':'https://github.com/x/live','stargazerCount':3,'forkCount':1,'isArchived':False,'isDisabled':False,'licenseInfo':None,'pushedAt':'2026-11-24T00:00:00Z','updatedAt':'2026-11-24T00:00:00Z','defaultBranchRef':{'name':'main','target':{'oid':'b'*40,'committedDate':'2026-11-24T00:00:00Z','c30':{'totalCount':1},'c90':{'totalCount':2}}},'releases':{'nodes':[]}}
        ok=SimpleNamespace(returncode=0,stdout=json.dumps({'data':{'r0':live}}),stderr='')
        with patch.object(refresh_metrics.subprocess,'run',side_effect=[failed,ok]) as run:
            out=refresh_metrics.fetch_batch(['x/gone','x/live'],now,previous)
        self.assertEqual(sorted(out),['x/gone','x/live'])
        self.assertTrue(out['x/gone']['missing_upstream'])
        self.assertEqual(out['x/gone']['collected_at'],'2026-11-20T00:00:00+00:00','carried record keeps its own collection time')
        self.assertEqual(out['x/gone']['head_sha'],'a'*40,'carried record keeps its numbers untouched')
        self.assertEqual(out['x/gone']['missing_since'],now.isoformat())
        self.assertNotIn('missing_upstream',out['x/live'])
        self.assertEqual(run.call_count,2)

    def test_vanished_repository_without_history_still_fails(self):
        from datetime import datetime,timezone
        from types import SimpleNamespace
        failed=SimpleNamespace(returncode=1,stdout='',stderr="gh: Could not resolve to a Repository with the name 'x/gone'.")
        with patch.object(refresh_metrics.subprocess,'run',return_value=failed):
            with self.assertRaises(RuntimeError):
                refresh_metrics.fetch_batch(['x/gone'],datetime.now(timezone.utc),{'x/other':{'head_sha':'c'*40}})

if __name__=='__main__':unittest.main()
