# Contributing

New projects, category corrections and extra version or license evidence are welcome. A low star count is never a reason for rejection.

1. Edit `data/projects.json`; do not hand-edit the generated README tables.
2. Provide the canonical GitHub URL, the purpose, the project form, the applicability boundary and evidence links pinned to commits.
3. Choose one primary category. Adjacent general-purpose writing tools must state their relation to fiction; do not mix software, Skills and research benchmarks into one class.
4. Distinguish implemented features, development previews and roadmap items. Model quality, target word counts and author-reported benchmarks must not be written as independently validated conclusions.
5. Verify the license; additional commercial terms and license gaps must be preserved. Public visibility does not automatically mean MIT.
6. Forks or ports are listed separately only when the host, functionality or maintenance path differs in an explainable way, and the source relationship must be stated.
7. After adding a project, refresh the full metric snapshot and regenerate the documents:

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

`data/seed-references.json` records the initial reference projects and normally does not change with ordinary contributions. Every manual feature review must update the date and the evidence commit; automatic star refreshes do not touch these fields.

Do not commit model keys, private search addresses, unpublished manuscripts or internal article bodies. Research summaries are saved under `record/` as `YYYY-MM-DD-<title in Chinese>.md`.

## Multilingual files

- `data/projects.json` is the canonical Chinese review data: facts change once, here.
- Wording in other languages comes from `locales/<lang>/entries.json` (`description`, `form`, `boundary`, `license_label`, `license_note`, plus a `name` override when the canonical name contains Chinese) and `locales/<lang>/ui.json`; `zh` falls back directly to `data/projects.json`, so there is no `locales/zh/entries.json`.
- When adding a project or rewriting a positioning, boundary or license conclusion, the en/es/hi/fr locales must be updated in the same PR, or `python scripts/build.py --check` and `python -m unittest discover -s tests -v` will fail.
- Static documents: English lives in the root `docs/` and `CONTRIBUTING.md`; other languages use the same relative paths under `locales/<lang>/`. Relative links inside a mirror resolve from that file's own directory, so from `locales/<lang>/docs/` a link to the repository root's `data/`, `scripts/`, `research/`, `LICENSE` or `record/` is written as `../../../`, while from `locales/<lang>/CONTRIBUTING.md` it is `../../`; `docs/readme-intro.md` is the exception — it is inlined into the README and resolves from the locale root.
- `record/` and `research/` keep the original language they were written in as an audit trail; they are not machine-translated.
- Generated files (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv`, and the same-named files in each language mirror) are never hand-edited; produce them with `python scripts/build.py`.
