# financialdata

Dépôt canonique de travail pour la constitution d'une base de données financières source, traçable et historisée à partir de documents publiés par les sociétés cotées et autres sources financières de référence.

## Objectif

Le projet commence par la collecte et l'extraction fidèle des sources, avant toute normalisation ou analyse :

`SOURCES → INVENTAIRE → EXTRACTION EXHAUSTIVE → RAW STRUCTURÉ → CONTRÔLE / TRAÇABILITÉ → MAPPED → CANONICAL → DERIVED → ANALYTICS`

Principe fondamental : **une observation réellement publiée = une observation RAW traçable à sa source**.

## Règle Git absolue

Ce dépôt fonctionne volontairement en **main-only** :

- branche de travail unique : `main` ;
- **aucune nouvelle branche ne doit être créée** ;
- **aucune Pull Request n'est requise pour le travail de ce projet** ;
- toute modification autorisée est appliquée directement sur `main` ;
- avant toute modification, l'agent doit lire les fichiers Markdown de mémoire persistante ;
- toute décision nouvelle doit être documentée dans les fichiers de gouvernance avant ou avec la modification qu'elle justifie ;
- aucune information source ne doit être inventée, corrigée silencieusement ou remplacée par une estimation.

Cette règle spécifique au dépôt `Patricked-code/financialdata` prévaut sur les habitudes Git utilisées dans d'autres projets.

## Mémoire persistante — ordre de lecture obligatoire

Avant tout travail, lire dans cet ordre :

1. [`GOVERNANCE.md`](GOVERNANCE.md) — règles non négociables du dépôt.
2. [`AGENTS.md`](AGENTS.md) — règles universelles de tous les agents automatisés.
3. [`CLAUDE.md`](CLAUDE.md) — instructions complémentaires destinées aux agents Claude/IA.
4. [`SUIVI.md`](SUIVI.md) — point de reprise opérationnel et état réel du chantier.
5. [`DECISIONS.md`](DECISIONS.md) — décisions validées et leur justification.
6. [`TODO.md`](TODO.md) — travaux restant à exécuter.
7. [`ARCHITECTURE.md`](ARCHITECTURE.md) — architecture des couches et flux de données.
8. [`DATA_MODEL.md`](DATA_MODEL.md) — principes de modélisation et tables cibles.
9. [`SOURCES.md`](SOURCES.md) — sources, corpus et règles de provenance.
10. [`docs/BRVM_RAW_DATABASE_GOVERNANCE.md`](docs/BRVM_RAW_DATABASE_GOVERNANCE.md) — observations conceptuelles détaillées issues du corpus BRVM.
11. [`docs/ISSUER_DISCOVERY_MATRIX.md`](docs/ISSUER_DISCOVERY_MATRIX.md) — couverture de la passe de découverte des sociétés.

## État initial

Au 9 août 2026 :

- dépôt GitHub initialisé ;
- `main` est la seule branche autorisée pour le travail ;
- corpus BRVM `RAPO / Rapport V2` relié au projet comme source documentaire ;
- passe de découverte conceptuelle des 48 dossiers société : **terminée** ;
- extraction RAW exhaustive de tous les documents : **non terminée** ;
- premier pilote approfondi BOABF réalisé partiellement ;
- aucune conclusion de complétude ne doit être déduite du seul nom d'un dossier, d'un fichier ou d'une année.

## Règles de vérité

- Le PDF/fichier source est la preuve primaire.
- Le RAW conserve le libellé, la valeur, l'unité, la période, le périmètre et la provenance tels que publiés.
- Une donnée publiée et une donnée recalculée sont deux objets distincts.
- Les comparatifs, doublons, versions, restatements et corrections restent historisés.
- Une cellule illisible reste `NULL`/`REVIEW_REQUIRED` plutôt que d'être inventée.
- Les ratios publiés restent des faits `PUBLISHED`; les ratios recalculés appartiennent à `DERIVED`.

## Source de vérité du projet

GitHub devient la mémoire persistante opérationnelle du projet. Les sources externes (Drive, PDF, sites officiels) restent les preuves documentaires et doivent être référencées dans `SOURCES.md` et dans la provenance des données.
