# DECISIONS — financialdata

Registre canonique des décisions validées. Une décision ne doit pas être réécrite silencieusement : si elle change, ajouter une nouvelle entrée qui explique la modification.

## D001 — 2026-08-09 — Dépôt canonique

**Décision** : `Patricked-code/financialdata` devient le dépôt canonique de mémoire persistante et de construction du projet de données financières.

**Conséquence** : les décisions, règles, suivis et modèles doivent être documentés ici.

## D002 — 2026-08-09 — Politique Git main-only

**Décision** : tout travail se fait directement sur `main`.

**Règles** : aucune branche nouvelle ; aucune PR nécessaire ; ne pas appliquer automatiquement les conventions Git d'autres projets ; ne pas contourner la règle avec une branche temporaire.

## D003 — 2026-08-09 — Mémoire persistante Markdown

**Décision** : les fichiers `.md` du dépôt constituent la mémoire persistante opérationnelle.

Ordre : `GOVERNANCE.md` → `AGENTS.md` → `CLAUDE.md` → `SUIVI.md` → `DECISIONS.md` → `TODO.md` → documents techniques et `docs/`.

## D004 — 2026-08-09 — Source avant analytics

**Décision** : `SOURCE → INVENTAIRE → EXTRACTION EXHAUSTIVE → RAW → CONTRÔLE → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

## D005 — 2026-08-09 — Granularité RAW

Une observation réellement publiée devient une observation RAW distincte.

## D006 — 2026-08-09 — PUBLISHED vs DERIVED

Une valeur explicitement publiée reste `PUBLISHED`; toute reconstruction/calcul interne est `DERIVED`.

## D007 — 2026-08-09 — Périodes

Le nom d'un fichier/dossier ne suffit jamais pour déterminer la période économique.

## D008 — 2026-08-09 — Versions et doublons

Les doublons, versions, fichiers révisés et restatements sont conservés et reliés ; ils ne sont pas supprimés de SOURCE/RAW.

## D009 — 2026-08-09 — Modèle sectoriellement neutre

Le cœur RAW ne doit pas être spécifique à un secteur.

## D010 — 2026-08-09 — Étendre le schéma uniquement sur preuve

Aucune nouvelle table/colonne ne doit être ajoutée uniquement par anticipation.

## D011 — 2026-08-09 — Passe conceptuelle 48 sociétés

Statuts : `DISCOVERY_PASS_48_ISSUERS_COMPLETE` ; `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE`.

## D012 — 2026-08-09 — Sources externes et GitHub

GitHub conserve la gouvernance et la mémoire opérationnelle ; les fichiers originaux externes restent les preuves primaires.

## D013 — 2026-08-09 — PDF scanné

Absence de texte natif ≠ document vide. Ordre : texte natif → rendu visuel → OCR en dernier recours.

## D014 — 2026-08-09 — Données contextuelles externes dans un rapport

Prévoir `subject_scope_raw`, `reference_entity_raw`, `reference_product_raw` lorsque nécessaire.

## D015 — 2026-08-09 — Réalisé vs prévision

Les prévisions/guidances/targets publiées sont source mais distinctes du réalisé.

## D016 — 2026-08-09 — Audit et assurance

Distinguer audit, attestation, examen limité et autres formes d'assurance.

## D017 — 2026-08-09 — Événements

Les événements chiffrés ou datés expliquant les comptes doivent être conservés avec statut et source. `event_facts_raw` reste une table candidate.

## D018 — 2026-08-09 — Réglementaire

Les ratios prudentiels/normes publiés restent `PUBLISHED`. `regulatory_facts_raw` reste une table candidate.

## D019 — 2026-08-09 — Sources révisables mais historisées

Le registre des sources est vivant ; une révision ne réécrit jamais silencieusement l'historique.

## D020 — 2026-08-09 — Continuité obligatoire pour tous les agents

Tout agent reprend au point officiel de `SUIVI.md` sans régression.

Processus : `ÉTAT EXISTANT → PREUVE → IMPACT → DÉCISION → CHANGEMENT COMPATIBLE → TEST NON-RÉGRESSION → SUIVI`.

## D021 — 2026-08-09 — Vérification initiale du script Python Drive

**Ancien constat** : une recherche Drive textuelle n'avait retrouvé aucun fichier `.py` ni nom contenant `python` ou `script`.

**Statut** : `SUPERSEDED_BY_D022`.

Cette entrée est conservée pour documenter l'erreur de méthode ; elle ne doit plus être utilisée comme vérité actuelle.

## D022 — 2026-08-09 — Correction : script Python confirmé à la racine

**Preuve supérieure** : la liste directe du dossier `RAPO / Rapport V2` confirme `telecharger_rapports_brvm.py`.

- Drive ID : `1F1WRVMG4C27EOTMq5Gt9FT9Mosv-Rryz`
- taille : `14546` octets
- MIME : `text/x-python`
- mapping embarqué : 48 sociétés

**Décision** : pour établir la présence/contenu direct d'un dossier Drive, privilégier `list_folder`/inventaire direct plutôt qu'une recherche textuelle qui peut omettre un objet.

Le script est une provenance du processus de collecte, mais **pas** la source de vérité pour les périodes économiques.

## D023 — 2026-08-09 — Méthode P1 d'inventaire

P1 est construit à partir de l'arborescence réelle :

`RACINE → DOSSIER SOCIÉTÉ → SOUS-DOSSIERS DIRECTS → FICHIERS → MÉTADONNÉES/HASH → VERSIONS/DOUBLONS → PÉRIODES RÉELLES`.

Un suffixe de fichier `_2`, `_3`, etc. indique seulement une collision de nom historique jusqu'à preuve par hash ; il ne suffit pas à conclure à un doublon.
