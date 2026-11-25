# Ranking method and validation scope

The recomputable metric definitions follow [awesome_bot](https://github.com/ZanePoe/awesome_bot), and the main catalogue is ranked separately per category. Software, Skills and evaluation tools are different kinds of products; the maintenance score is not a leaderboard of writing quality.

## Raw data

`stargazerCount`, the default-branch SHA and commit dates, 30/90-day commit counts, archive state and license identification are read through the GitHub GraphQL API. The full collected data is stored in `data/metrics.json`, and the first snapshot is kept separately for traceability.

`commits_30d` and `commits_90d` use `history.totalCount` over default-branch history, with window start and end fixed at the same UTC collection moment. First-page commit counts are never written up as total commit counts.

The last-update field uses the default branch HEAD's `committedDate`. `pushed_at` and `updated_at` are stored separately, but repository metadata changes or pushes to other branches are never passed off as default-branch updates. The default branch is not necessarily called main, and experimental branches are counted as they are and labeled.

`latest_release` records the most recently created release node and whether it is a prerelease. A Skill without any release is not judged abandoned because of that.

## Maintenance tiers and formula

Projects are first sorted into four tiers: commits on the default branch within the last 90 days; no commits for 91–365 days; no commits for over 365 days; and archived, disabled or explicitly historical projects.

Within a tier, the combined score is:

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
maintenance_score = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Stars carry 40%, 90-day commit activity 35% and freshness 25%. Logarithms and caps reduce the advantage of very large projects; fixed anchors keep existing entries' scores unchanged when new entries are added. Ties compare stars, then sort stably by repository name.

The [ranking views](rankings.md) provide the balanced score, stars, 90-day activity and latest-commit views, all grouped by maintenance tier first. To sort purely by raw values, use the [CSV](../data/rankings.csv).

## Limitations

Commit counts include merges, bots and documentation updates, and a monorepo's total activity is not the same as activity in its novel-related modules. Once a Skill's rules are stable it may rarely commit, so a low activity score does not mean it is ineffective. A new project can have many commits and few users; an old project can have many stars and little current maintenance.

This round validated repository documentation, version boundaries, licenses and GitHub metadata. Not all software was installed, and no uniform writing exam was run. Nothing here supports claiming a project writes the best novels, sustains million-word quality reliably, or improves signing revenue.

A capability evaluation would need fixed models, budgets, story prompts, target lengths and versions, comparing setting consistency, character behavior, foreshadow payoff, repetition, amount of manual revision and generation cost. Authors' self-reported "millions of words" or "multi-agent improvements" are not mixed into cross-project numeric comparisons.

## Updates and failure handling

Metric refreshes require `gh` login or `GH_TOKEN`. The snapshot is replaced atomically only after all batches succeed; on partial API failure, an inaccessible repository or a missing default branch, the old file is kept and the job fails, so unknown values are never written as zeros.

Feature and license data are manually reviewed and carry their own review date and pinned-commit source. The daily refresh only updates metrics; it does not auto-confirm new features or reinterpret licenses. Renames, removals and license changes require a maintainer's recheck.
