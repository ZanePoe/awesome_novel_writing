# Méthode de classement et périmètre de vérification

On reprend la définition d'indicateurs reproducible de [awesome_bot](https://github.com/ZanePoe/awesome_bot) ; le catalogue principal trie séparément par catégorie. Logiciels, Skills et outils d'évaluation ne sont pas la même famille de produits : le score de maintenance ne vaut pas classement général de qualité d'écriture.

## Données brutes

Lecture via l'API GraphQL GitHub de `stargazerCount`, du SHA et des dates de commit de la branche par défaut, des compteurs de commits à 30/90 jours, de l'état d'archivage et de l'identification de licence. Les données complètes collectées sont stockées dans `data/metrics.json` ; le premier instantané est conservé à part pour la traçabilité.

`commits_30d` et `commits_90d` utilisent `history.totalCount` sur l'historique de la branche par défaut, les fenêtres de début et de fin étant figées au même instant UTC de collecte. Le nombre de commits de la première page n'est jamais écrit comme le nombre total de commits.

La dernière mise à jour reprend la `committedDate` du HEAD de la branche par défaut. `pushed_at` et `updated_at` sont conservés à part, mais les changements de métadonnées du dépôt ou les pushes d'autres branches ne sont pas faits passer pour des mises à jour de la branche par défaut. La branche par défaut ne s'appelle pas nécessairement main ; les commits des branches expérimentales sont comptés tels quels et signalés.

`latest_release` enregistre le nœud de release le plus récemment créé et son statut de pré-sortie. Un Skill sans release n'est pas pour autant déclaré abandonné.

## Paliers de maintenance et formule

Triage d'abord en quatre paliers : commit sur la branche par défaut dans les 90 derniers jours ; aucun commit depuis 91–365 jours ; aucun commit depuis plus de 365 jours ; archivé, désactivé ou explicitement historique.

Score composite dans le palier :

```text
P = min(1, ln(1 + stars) / ln(1 + 100000))
A = min(1, ln(1 + commits_90d) / ln(1 + 500))
R = exp(-max(0, days_since_default_branch_HEAD) / 90)
score_de_maintenance = 100 × (0.40 × P + 0.35 × A + 0.25 × R)
```

Les étoiles pèsent 40 %, l'activité à 90 jours 35 % et la fraîcheur 25 %. Les logarithmes et les plafonds réduisent l'avantage des très gros projets ; des ancres fixes évitent qu'une nouvelle entrée modifie le score des entrées existantes. À égalité, on compare les étoiles, puis un tri stable par nom de dépôt.

[Les vues de classement](rankings.md) offrent quatre vues — score composite, étoiles, activité à 90 jours et dernier commit — toutes stratifiées d'abord par palier de maintenance. Pour trier uniquement sur les valeurs brutes, utiliser [le CSV](../../../data/rankings.csv).

## Limites

Les volumes de commits incluent fusions, robots et mises à jour de documentation ; pour les monorepos, l'activité totale ne vaut pas activité du module romanesque. Un Skill dont les règles sont stables peut publier rarement, donc un faible score d'activité ne signifie pas invalidité. Un projet récent peut accumuler beaucoup de commits avec peu d'utilisateurs ; un projet ancien peut avoir beaucoup d'étoiles avec peu de maintenance actuelle.

Cette passe a vérifié la documentation des dépôts, les frontières de versions, les licences et les métadonnées GitHub ; aucun logiciel n'a été installé et aucune épreuve d'écriture uniforme n'a été exécutée. On ne peut donc pas en conclure qu'un projet écrit mieux des romans que les autres, qu'il maintient stablement une qualité sur un million de mots ou qu'il améliore les revenus de publication.

Une évaluation de capacités devrait figer modèle, budget, sujet de récit, longueur visée et version, puis comparer la cohérence des bibles, les comportements des personnages, la récupération des fils rouges, les répétitions, le volume de retouches humaines et le coût de génération. Les chiffres auto-déclarés par les auteurs — « plusieurs millions de mots », « gain multi-agents » — ne se mélangent pas aux données des autres projets.

## Mises à jour et gestion des pannes

Le rafraîchissement des métriques dépend de l'authentification `gh` ou de `GH_TOKEN`. L'instantané n'est remplacé de façon atomique qu'après réussite de tous les lots ; en cas d'échec partiel de l'API, de dépôt inaccessible ou de branche par défaut manquante, l'ancien fichier est conservé et la tâche échoue, afin de ne pas écrire un inconnu comme zéro.

Les fonctionnalités et les licences sont des données revues par un humain, avec leur propre date de vérification et des sources figées sur des commits. Le rafraîchissement quotidien ne met à jour que les métriques ; il ne confirme aucune nouvelle fonctionnalité ni ne réinterprète une licence. Les renommages, suppressions et changements de licence demandent une revue du mainteneur.
