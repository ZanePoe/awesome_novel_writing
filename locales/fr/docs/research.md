# Journal de recherche et critères d'inclusion

Première version achevée le 2026-11-05 : 41 projets, 6 catégories, les 13 projets de référence dédupliqués tous couverts. Le 2026-11-06, Reveric a été ajouté sur complément de l'utilisateur, portant le catalogue à 42 projets et 14 références. Cette passe s'est concentrée sur les projets et leurs implémentations ; les articles connexes n'ont pas été étendus en une liste de publications indépendante.

## Axes de recherche induits des projets de référence

| Direction | Mots-clés anglais | Mots-clés chinois |
| --- | --- | --- |
| Outils de création complets | AI novel writer, writing workspace, fiction IDE, local-first | AI 小说写作、小说工作台、桌面码字软件 |
| Automatisation long format | long-form fiction, writing agent, novel generator, harness | 长篇生成、分章写作、写作 Agent |
| État et cohérence | story bible, character state, foreshadowing, continuity, RAG | 世界观、人物状态、伏笔、连贯性、长期记忆 |
| Ressources pour agents | novel writing skill, workflow, prompt framework | 小说 Skill、网文技能、方法框架 |
| Révision | narrative revision, humanizer, style lint, editing | 叙事修复、去模板化、文风、审稿 |
| Adaptation | screenplay, short drama, story adaptation, narration | 剧本、短剧、小说改编、影视解说 |

## Trois passes de recherche

| Passe | Lots | Résultats | Nouvelles sources | Taux de nouvelles sources |
| --- | --- | --- | --- | --- |
| 1 | 15 | 331 | 300 | 90.6% |
| 2 | 4 | 127 | 90 | 70.9% |
| 3 | 3 | 17 | 15 | 88.2% |

22 lots de recherche ou de vérification au total, couvrant la recherche web, la recherche native GitHub, la collecte des liens des index externes et la vérification en lot des dépôts et des métriques. Le nombre de sources compte les URL du journal de recherche, pas les projets retenus ; tous les candidats ne sont pas pertinents.

La première passe est partie de l'ensemble des projets de référence et a couvert huit directions : définition, sources primaires, index externes, dépôts, comparatifs, évaluations, frontières et évolutions récentes. La recherche GitHub de `小说` mélange lecteurs, téléchargeurs, CMS et listes de livres, éliminés selon l'objectif d'écriture ; `easy-writing` mélange aussi des frameworks de développement homonymes, et le classement de recherche seul ne justifie aucune inclusion.

La deuxième passe a complété les directions Oh Story, webnovel-writer, NovelClaw, OpenFic, etc., en lisant les README officiels pour distinguer applications, skills et méthodologies. Les index externes servent à découvrir des pistes, sans recopier leurs étoiles, leurs informations de conférence ni leurs conclusions d'efficacité.

La troisième passe a vérifié les renommages, les exceptions de licence et le README en chinois de Sepia fourni par l'utilisateur, puis ajouté Long-Novel-GPT. Les métriques des projets finaux ont été collectées uniformément via l'API GraphQL GitHub, avec les commits sources des fonctionnalités figés.

La raison d'arrêt est la limite de trois passes fixée à l'avance, pas « tout a été exploré ». La troisième passe a encore produit des découvertes. Les genres verticaux, la fiction interactive, la traduction, les modèles d'écriture locaux et l'ensemble des outils de mini-drames industriels restent non couverts de façon exhaustive. Les outils purs de lecture, de collecte ou de publication de romans n'ont pas été forcés dans la liste comme outils d'écriture.

## Projets de référence, noms et déduplication

| Nom fourni / ancien nom | Entrée actuelle |
| --- | --- |
| Denova | [alfredxw/denova](https://github.com/alfredxw/denova) |
| 易创 easy-writing | [yilujian/easy-writing](https://github.com/yilujian/easy-writing) |
| ai-juben | [VanGong1999/juben](https://github.com/VanGong1999/juben), confirmé par l'utilisateur |
| AI Novel Writer | [书童 Pagekin](https://github.com/EthanYoQ/Pagekin), dépôt renommé, l'ancienne adresse redirige automatiquement |
| AI Novel Writing Assistant | [Biz Novel Studio](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant), même dépôt |
| Storyteller | [Dankular/Storyteller](https://github.com/Dankular/Storyteller), nom actuel du README : novel-harness |
| Doublons de Sepia et `-g` | Un seul compte pour le même dépôt, aucune installation de skill déclenchée |

Toutes les correspondances de références sont conservées dans [seed-references.json](../../../data/seed-references.json). Le dépôt canonique est la clé de déduplication ; un renommage de dépôt n'ajoute pas de projet. Le portage OpenCode est listé séparément parce que l'hôte et les fonctions diffèrent, avec sa relation à l'amont explicite ; les forks au contenu identique sans différence claire n'ont pas été retenus.

## Corrections des documents d'origine

- [qifeng-writing](https://github.com/Yuriloll/qifeng-writing) se centre explicitement sur les articles et posts en chinois ; un roman pur demande encore des méthodes dédiées, d'où son rang d'outil de révision adjacent.
- [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) guide l'appel d'un CLI d'explication de films et ne doit pas être écrit comme un générateur de romans originaux.
- [NeuroBook](https://github.com/notnotype/neuro-book) est en pleine refonte v2 ; certaines capacités de studio IA figurent sur la roadmap ; la fiche conserve la frontière de la version d'aperçu.
- [Novel Studio](https://github.com/bbaz123/novel-studio) a une branche par défaut expérimentale ; les métriques reprennent bien cette branche, sans forcer l'ancienne main.
- [Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT) inscrit encore une partie de ses capacités de livre entier en un clic à ses plans ; le slogan de la page d'accueil ne vaut pas acceptation réalisée.
- [Reveric](https://github.com/looplj/reveric) a `unstable` comme branche par défaut actuelle ; la fiche est vérifiée sur cette branche. Son fichier `NOTICES`, fondé sur la section 7 de l'AGPLv3, impose aux versions modifiées de conserver la signature du projet et le lien vers l'original, et prévoit une voie de licence commerciale.

## Vérification des licences

L'identification SPDX de GitHub et la revue humaine des exceptions sont conservées séparément. La LICENSE de Biz Novel Studio contient à la fois l'AGPL et des mentions d'autorisation commerciale pour l'usage en service ; celle de Kimi Writer est un texte assorti d'une condition d'attribution commerciale supplémentaire. Les deux conservent le lien vers le texte original, sans simplification en un AGPL/MIT ordinaire.

Agnes déclare explicitement n'avoir aucune licence ; certains petits harness d'écriture, Skills et dépôts d'évaluation n'ont pas de licence complète localisable. Un badge de README ou une ligne « MIT » ne suffisent pas à les marquer automatiquement comme licences vérifiées. Statuts détaillés dans [le détail des projets](projects.md). Ce catalogue consigne les clauses des auteurs, sans garantie d'usage commercial transverse.

## Content factory

En réutilisant `content-factory-search-api`, la recherche structurée a été appelée par curl ; plage de dates **du 2026-08-05 au 2026-11-05**, requêtes `小说` et `inkos OR sepia OR 小说写作`. Les deux requêtes ont renvoyé un JSON de succès, mais avec des tableaux de résultats vides. Aucune recherche sur tout l'historique n'a été exécutée et le résultat vide n'a pas été interprété comme l'inexistence de ces projets.

En l'absence de résultats, aucun calcul vectoriel n'a été lancé. L'inclusion finale repose sur les dépôts GitHub d'origine ; les adresses de recherche privées, les clés et les textes internes ne vont pas dans le dépôt public.

## Vérification et limites

Les descriptions de fonctionnalités reposent sur la documentation officielle ; tous les logiciels n'ont pas été installés ni exécutés et aucune évaluation aveugle avec modèle, budget et sujets de récit uniformes n'a été menée. Les annonces des auteurs sur le nombre de chapitres, le million de mots, la « dé-IA » ou le multi-agent ne servent pas à un classement de capacités. Cette passe n'a fait aucune expérience d'ablation de composants et ne peut pas dire de combien la qualité baisse quand on retire la mémoire.

Ont été exécutés : contrôle de complétude projets/références, tests aux limites du tri, test de conservation de l'ancien instantané en cas d'échec API et contrôle de cohérence des fichiers générés. Le détail des indicateurs est dans [methodology.md](methodology.md).

Matériaux d'audit publics :

- [Journal de recherche](../../../research/search-log.json) : requêtes, passes et statistiques de résultats.
- [Décisions d'inclusion](../../../research/decisions.json) : usage, frontières, commits figés et vérification de licence.
- [Couverture des références](../../../research/coverage.json) : les 14 liens de référence sont tous couverts.
- [Métriques de la première version](../../../research/initial-metrics.json) et [métriques actuelles](../../../data/metrics.json) : l'initial et les mises à jour courantes séparément.
- [Statut](../../../research/status.json) et [résultat de complétude](../../../research/verification.json) : raison d'arrêt et résultats vides connus.

Les textes sources complets et les journaux d'outils restent en local. Les statistiques publiques de la recherche comptent 84 décisions et 123 enregistrements de métriques, revérifiables via les décisions et instantanés ci-dessus.
