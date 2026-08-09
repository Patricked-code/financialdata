# DECISIONS — financialdata

Registre canonique des décisions validées. Une décision ne doit pas être réécrite silencieusement : si elle change, ajouter une nouvelle entrée qui explique la modification.

## D001 — 2026-08-09 — Dépôt canonique

**Décision** : `Patricked-code/financialdata` devient le dépôt canonique de mémoire persistante et de construction du projet de données financières.

**Conséquence** : les décisions, règles, suivis et modèles doivent être documentés ici.

## D002 — 2026-08-09 — Politique Git main-only

**Décision** : tout travail se fait directement sur `main`.

**Règles** :

- aucune branche nouvelle ;
- aucune PR nécessaire ;
- ne pas appliquer automatiquement les conventions Git d'autres projets ;
- ne pas contourner la règle avec une branche temporaire.

**Motif** : règle explicite du propriétaire du projet.

## D003 — 2026-08-09 — Mémoire persistante Markdown

**Décision** : les fichiers `.md` du dépôt constituent la mémoire persistante opérationnelle.

**Ordre de lecture** : `GOVERNANCE.md` → `CLAUDE.md` → `SUIVI.md` → `DECISIONS.md` → `TODO.md` → documents techniques et `docs/`.

## D004 — 2026-08-09 — Source avant analytics

**Décision** : le projet doit d'abord extraire et structurer les données sources avant normalisation, calculs et analytics.

Pipeline :

`SOURCE → INVENTAIRE → EXTRACTION EXHAUSTIVE → RAW → CONTRÔLE → MAPPED → CANONICAL → DERIVED → ANALYTICS`

## D005 — 2026-08-09 — Granularité RAW

**Décision** : une observation réellement publiée devient une observation RAW distincte.

Le RAW conserve la représentation publiée et la représentation machine, sans écrasement.

## D006 — 2026-08-09 — PUBLISHED vs DERIVED

**Décision** : une valeur explicitement publiée reste `PUBLISHED`, même s'il s'agit d'un ratio. Toute reconstruction/calcul interne est `DERIVED`.

## D007 — 2026-08-09 — Périodes

**Décision** : le nom d'un fichier/dossier ne suffit jamais pour déterminer la période économique. La période est résolue depuis le contenu du document et conservée séparément du libellé source.

## D008 — 2026-08-09 — Versions et doublons

**Décision** : les doublons, versions, fichiers révisés et restatements sont conservés et reliés ; ils ne sont pas supprimés de la couche source/RAW.

## D009 — 2026-08-09 — Modèle sectoriellement neutre

**Décision** : le cœur RAW ne doit pas être spécifique à la banque, à l'industrie ou à un autre secteur.

Les différences sectorielles sont portées par les types de faits et dimensions, pas par une rupture de traçabilité.

## D010 — 2026-08-09 — Étendre le schéma uniquement sur preuve

**Décision** : aucune nouvelle table/colonne ne doit être ajoutée uniquement par anticipation. Toute extension doit être reliée à une particularité documentée dans une source.

## D011 — 2026-08-09 — Passe conceptuelle 48 sociétés

**Décision** : la passe de découverte des 48 dossiers sociétés BRVM est considérée terminée pour la conception initiale.

**Important** : cela ne signifie pas que tous les PDF ont été extraits.

Statuts :

- `DISCOVERY_PASS_48_ISSUERS_COMPLETE`
- `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE`

## D012 — 2026-08-09 — Sources externes et GitHub

**Décision** : GitHub conserve la gouvernance et la mémoire opérationnelle ; les fichiers originaux externes restent les preuves primaires.

Les références Drive/PDF/sites officiels doivent être conservées dans la provenance et `SOURCES.md`.

## D013 — 2026-08-09 — PDF scanné

**Décision** : absence de texte natif ≠ document vide.

Ordre : texte natif → inspection/rendu PDF → OCR en dernier recours.

## D014 — 2026-08-09 — Données contextuelles externes dans un rapport

**Décision** : une donnée publiée dans le rapport d'un émetteur peut concerner le marché, un produit, une marque ou une autre entité.

Prévoir des dimensions comme `subject_scope_raw`, `reference_entity_raw`, `reference_product_raw` afin de ne pas attribuer automatiquement le fait à l'émetteur.

## D015 — 2026-08-09 — Réalisé vs prévision

**Décision** : les prévisions, guidances et targets publiées sont des faits source, mais doivent être distinguées du réalisé via `fact_nature_raw` ou équivalent.

Valeurs envisagées : `ACTUAL`, `FORECAST`, `GUIDANCE`, `TARGET`.

## D016 — 2026-08-09 — Audit et assurance

**Décision** : distinguer audit, attestation, examen limité et autres formes d'assurance. Le statut des comptes et celui du rapport d'audit doivent être stockés séparément lorsque publiés.

## D017 — 2026-08-09 — Événements

**Décision** : les événements chiffrés ou datés expliquant les comptes (cession, augmentation de capital, changement de contrôle, corporate action, événement post-clôture, etc.) doivent être conservés avec leur statut et leur source.

`event_facts_raw` est une table candidate à confirmer lors de l'implémentation du schéma.

## D018 — 2026-08-09 — Réglementaire

**Décision** : les ratios prudentiels et normes réglementaires publiés doivent être conservés comme faits `PUBLISHED`.

`regulatory_facts_raw` est une table candidate à confirmer selon le volume observé.
