# Guide de contribution

Les ajouts de projets, les corrections de catégorie et les compléments de version ou de preuve de licence sont bienvenus. Un faible nombre d'étoiles n'est jamais un motif de refus.

1. Modifiez `data/projects.json`, n'éditez jamais à la main les tableaux générés du README.
2. Fournissez l'adresse GitHub canonique, l'usage, la forme du projet, ses frontières d'application et des liens de preuve figés sur des commits.
3. Choisissez une catégorie principale. Pour un outil généraliste adjacent, expliquez son rapport à l'écriture romanesque ; ne mélangez pas logiciels, Skills et benchmarks de recherche.
4. Distinguez ce qui est implémenté, ce qui est en version d'aperçu et ce qui est sur la roadmap. L'efficacité d'un modèle, le volume de mots visé et les benchmarks auto-déclarés par l'auteur ne s'écrivent jamais comme des conclusions vérifiées de façon indépendante.
5. Vérifiez la licence ; les clauses commerciales supplémentaires et les manques de vérification doivent être conservés. Un code publiquement visible n'équivaut pas automatiquement à MIT.
6. Un fork ou un portage n'est listé séparément que si une différence explicable existe sur l'hôte, les fonctions ou la trajectoire de maintenance, avec sa relation à l'amont clairement écrite.
7. Après un ajout de projet, régénérez un instantané complet des métriques et les documents :

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

`data/seed-references.json` enregistre les projets de référence initiaux et ne change pas au fil des contributions ordinaires. Chaque vérification fonctionnelle humaine met à jour la date et le commit de preuve ; le rafraîchissement automatique des étoiles ne touche pas ces champs.

Ne commitez aucune clé de modèle, aucune adresse de recherche privée, aucun manuscrit non publié ni aucun texte interne d'articles. Les bilans de recherche se rangent dans `record/YYYY-MM-DD-<titre-en-chinois>.md`.

## Fichiers multilingues

- `data/projects.json` porte les données d'audit canoniques en chinois : un fait ne se corrige qu'à cet endroit.
- Les textes des autres langues viennent de `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`, plus `name` lorsque le nom canonique contient des caractères chinois) et de `locales/<lang>/ui.json` ; `zh` retombe directement sur `data/projects.json`, il n'existe donc pas de `locales/zh/entries.json`.
- Lors d'un ajout de projet ou d'une reformulation d'un positionnement, d'une frontière ou d'une conclusion de licence, complétez les quatre locales en/es/hi/fr dans la même pull request, sinon `python scripts/build.py --check` et `python -m unittest discover -s tests -v` échouent.
- Prose statique : l'anglais vit à la racine, dans `docs/` et `CONTRIBUTING.md` ; les autres langues dans les mêmes chemins relatifs sous `locales/<lang>/`. Dans une copie, les liens se résolvent depuis le dossier du fichier lui-même : ceux qui pointent vers la racine du dépôt depuis `locales/<lang>/docs/` — `data/`, `scripts/`, `research/`, `LICENSE`, `record/` — s'écrivent `../../../` ; depuis `locales/<lang>/CONTRIBUTING.md`, `../../` ; `docs/readme-intro.md` fait exception, car il est inséré dans le README et se résout depuis la racine de la langue, en écrivant `docs/…` et `CONTRIBUTING.md`.
- `record/` et `research/` conservent le texte d'origine tel qu'écrit, comme trace d'audit ; pas de traduction automatique.
- Les fichiers générés (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` et leurs copies dans chaque locale) ne se modifient jamais à la main ; ils sortent de `python scripts/build.py`.
