# ROADMAP — financialdata

Dernière mise à jour : 2026-08-09

Ce document décrit le plan canonique du projet depuis son objectif initial jusqu'aux couches analytiques finales.

## 1. Objectif initial

Construire une base de données financière BRVM exhaustive, traçable, réutilisable et maintenable à partir des documents réellement publiés par les sociétés cotées.

Le projet doit être capable de :

- conserver tous les documents sources par société et période ;
- récupérer à terme automatiquement les nouvelles publications BRVM ;
- ne jamais perdre une version historique ;
- extraire exhaustivement les valeurs publiées, tableaux, textes, données opérationnelles, corporate, audit, réglementaire et autres faits documentaires ;
- conserver la valeur et le libellé tels que publiés ;
- préserver page, tableau, cellule, unité, devise, période, scope et provenance ;
- distinguer publication source et calcul interne ;
- permettre ensuite une normalisation multi-sociétés et multi-secteurs ;
- calculer plus tard des indicateurs et analytics uniquement à partir de données source traçables.

Règle maîtresse :

> Une ligne RAW correspond à une observation réellement publiée dans une source identifiable.

## 2. Architecture de données cible

Six couches persistantes :

`0 SOURCE → 1 RAW → 2 MAPPED → 3 CANONICAL → 4 DERIVED → 5 ANALYTICS`

Deux dimensions transversales :

- `LINEAGE / VERSIONING` ;
- `DATA QUALITY / CONTROL`.

Les couches 0 et 1 sont prioritaires. Les couches 2 à 5 ne doivent pas être utilisées pour masquer une insuffisance du corpus source ou RAW.

## 3. Pipeline de travail

`PDF / SOURCES`
→ `INVENTAIRE DOCUMENTAIRE`
→ `MISE À JOUR / RÉCONCILIATION DES SOURCES`
→ `EXTRACTION EXHAUSTIVE`
→ `RAW STRUCTURÉ`
→ `CONTRÔLE / TRAÇABILITÉ`
→ `MAPPING SÉMANTIQUE`
→ `CANONICALISATION`
→ `CALCULS DERIVED`
→ `ANALYTICS`

## P0 — Gouvernance et mémoire persistante

**Statut : COMPLETE**

Objectifs :

- dépôt canonique GitHub ;
- `main` uniquement ;
- aucune branche ;
- mémoire persistante Markdown ;
- reprise obligatoire par `SUIVI.md` ;
- décisions historisées ;
- travail sans régression.

Livrables principaux :

- `GOVERNANCE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `SUIVI.md`
- `DECISIONS.md`
- `TODO.md`
- `ARCHITECTURE.md`
- `DATA_MODEL.md`
- `SOURCES.md`
- `ROADMAP.md`

## P1 — Inventaire documentaire exhaustif du corpus existant

**Statut : IN_PROGRESS**

But : établir la couche SOURCE réelle avant extraction.

Pour chacune des 48 sociétés historiques :

1. identifier le dossier société ;
2. inventorier tous les sous-dossiers annuels et `divers` ;
3. inventorier chaque fichier ;
4. conserver Drive ID, chemin historique, nom, MIME, taille et dates ;
5. identifier dossiers vides ;
6. détecter anomalies d'attribution émetteur ;
7. repérer candidats doublons / collisions de noms / versions ;
8. calculer ensuite SHA-256 ;
9. résoudre les périodes économiques depuis le contenu ;
10. mesurer la couverture documentaire réelle.

P1 n'est pas l'extraction financière.

### P1-A — Inventaire arborescence/fichiers

Objectif : 48/48 sociétés documentées dans `inventory/`.

### P1-B — Manifeste machine-lisible

Produire un registre consolidé document par document avec identifiants et métadonnées SOURCE.

### P1-C — Hash / versions / doublons

Calculer SHA-256 et établir les relations :

- `DUPLICATE`
- `VERSION_OF`
- `SUPERSEDES`
- `REVISED_AT_SAME_URL`
- `REVIEW_REQUIRED`

### P1-D — Périodes et attribution

Valider :

- émetteur réel ;
- période(s) économique(s) ;
- type documentaire ;
- scope ;
- classement historique vs contenu réel.

## P1-FRESH — Maintien du corpus à jour / collecteur BRVM V2

Ne pas confondre avec l'inventaire du corpus historique.

Le script historique `telecharger_rapports_brvm.py` reste la référence de collecte V1.

Après établissement du manifeste P1 :

1. implémenter le collecteur V2 en `--dry-run` ;
2. découvrir le catalogue BRVM courant ;
3. comparer au manifeste SOURCE ;
4. produire les statuts `NEW`, `UNCHANGED`, `REVISED`, `DUPLICATE`, `NOT_SEEN_THIS_RUN` ;
5. valider les deltas ;
6. activer ensuite le téléchargement incrémental ;
7. conserver `first_seen_at`, `last_seen_at`, URL, titre BRVM, hash et version ;
8. détecter nouveaux émetteurs, nouveaux slugs et changements de dénomination ;
9. ne jamais écraser ni supprimer silencieusement l'historique.

Référence : `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## P2 — Schéma RAW v1

Définir puis implémenter le modèle universel à partir des particularités documentées sur les 48 sociétés.

Noyau prévu :

- documents / versions / pages / sections ;
- tables_raw / table_cells_raw ;
- financial_facts_raw ;
- operating_facts_raw ;
- segment_facts_raw ;
- contractual_facts_raw ;
- corporate_facts_raw ;
- audit_facts_raw ;
- text_disclosures_raw ;
- candidats `event_facts_raw` et `regulatory_facts_raw` selon validation finale.

Contraintes :

- `raw_value_text` toujours conservé ;
- unités et multiplicateurs source conservés ;
- périodes comparatives séparées ;
- scopes individuels/consolidés/concession/etc. distincts ;
- PUBLISHED distinct de DERIVED ;
- provenance jusqu'au document/page/table/cellule lorsque disponible.

## P3 — Extraction RAW exhaustive

Pour chaque document validé SOURCE :

- extraire tout tableau et toute observation utile ;
- conserver comparatifs et périodes multiples ;
- conserver textes significatifs ;
- conserver audit, corporate actions, événements, données opérationnelles et réglementaires ;
- rendre les scans visuellement ;
- OCR uniquement en dernier recours ;
- ne jamais inventer une valeur illisible ou absente.

Ordre conseillé : travailler société par société avec lots vérifiables, tout en réutilisant le même moteur/schema.

## P4 — Contrôle, qualité et lineage

Développer en parallèle de P3 :

- contrôles arithmétiques sans correction silencieuse ;
- détection des incohérences source ;
- validation de parsing ;
- statut de confiance ;
- provenance complète ;
- relations versions/doublons ;
- journal des erreurs d'extraction ;
- tests de non-régression.

Une incohérence publiée est conservée et signalée, pas corrigée dans RAW.

## P5 — MAPPED

Interprétation sémantique sans modifier RAW.

Exemple :

`"Créances sur la clientèle" → CUSTOMER_LOANS`

Conserver version de mapping, confiance et règle appliquée.

## P6 — CANONICAL

Harmoniser :

- concepts ;
- périodes ;
- unités ;
- devises ;
- scopes ;
- catégories ;
- secteurs ;
- émetteurs / alias ;
- comparabilité multi-sociétés.

La valeur canonique doit toujours remonter aux faits RAW sources.

## P7 — DERIVED

Uniquement les calculs internes :

- croissance ;
- reconstitution de périodes lorsque méthodologiquement autorisée ;
- TTM ;
- CAGR ;
- marges calculées ;
- transformations de devise ;
- agrégations et autres formules.

Chaque fait dérivé doit stocker : formule, version, IDs des faits d'entrée et date de calcul.

## P8 — ANALYTICS

Couche finale :

- ROE/ROA calculés ;
- P/E, P/B ;
- dividend yield ;
- valorisation ;
- ratios de risque ;
- benchmarks ;
- rankings ;
- peers ;
- screener ;
- alertes ;
- scoring ;
- IA/NLP ;
- interfaces et API analytiques.

Un ratio publié par une société reste aussi en RAW sous forme `PUBLISHED`; le ratio calculé par le projet est un fait distinct `DERIVED/ANALYTICS`.

## 4. Définition de la réussite finale

Le projet est réussi lorsque :

1. chaque document source possède une identité/provenance stable ;
2. le corpus historique est inventorié et peut être maintenu à jour ;
3. chaque valeur RAW est traçable à une source réelle ;
4. aucune donnée source n'est silencieusement écrasée ;
5. les 48 sociétés historiques et les futurs émetteurs peuvent utiliser la même architecture ;
6. les particularités sectorielles sont préservées ;
7. toute normalisation est explicite ;
8. tout calcul est reproductible depuis ses inputs ;
9. tout analytics peut être audité jusqu'au PDF original ;
10. tout agent peut reprendre le travail via les fichiers `.md` sans perdre ni réinventer l'historique.

## 5. Discipline permanente

- Git : `main` uniquement.
- Avant travail : lire la mémoire persistante.
- Après travail significatif : mettre à jour `SUIVI.md` et `TODO.md`.
- Toute nouvelle règle conceptuelle : documenter avant modification de schéma.
- Toute source nouvelle/révisée : historiser.
- Toute extraction : source d'abord, analytics plus tard.
- Toute modification : vérifier la non-régression.
