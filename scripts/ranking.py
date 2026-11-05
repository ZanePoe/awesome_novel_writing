"""Maintenance ranking reused from ZanePoe/awesome_bot (MIT)."""
from datetime import datetime, timezone
import math

def dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)

def age_days(metric, as_of):
    return max(0.0, (dt(as_of)-dt(metric['last_commit_at'])).total_seconds()/86400)

def score(metric, as_of):
    popularity = min(1, math.log1p(metric['stars']) / math.log1p(100000))
    activity = min(1, math.log1p(metric['commits_90d']) / math.log1p(500))
    freshness = math.exp(-age_days(metric, as_of)/90)
    return round(100 * (0.40*popularity + 0.35*activity + 0.25*freshness), 2)

def tier(project, metric, as_of):
    if metric['archived'] or metric['disabled'] or project['scope']=='historical': return 3
    age=age_days(metric, as_of)
    return 0 if age<=90 else 1 if age<=365 else 2

def status(project, metric, as_of):
    return ['近90天有提交','91–365天未提交','超过365天未提交','归档 / 历史'][tier(project,metric,as_of)]

def rank(projects, metrics, as_of, mode='balanced'):
    def key(p):
        m=metrics[p['repo']]
        primary={'balanced':-score(m,as_of),'stars':-m['stars'],'activity':-m['commits_90d'],'recent':-dt(m['last_commit_at']).timestamp()}[mode]
        return (tier(p,m,as_of),primary,-m['stars'],p['repo'].lower())
    return sorted(projects,key=key)

def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])

