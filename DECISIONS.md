# DECISIONS — financialdata

Registre canonique des décisions validées. Une décision ne doit pas être réécrite silencieusement : si elle change, ajouter une nouvelle entrée qui explique la modification.

## D001 — 2026-08-09 — Dépôt canonique

`Patricked-code/financialdata` est le dépôt canonique de mémoire persistante et de construction du projet.

## D002 — 2026-08-09 — Politique Git main-only

Tout travail se fait directement sur `main`; aucune branche nouvelle, aucune PR normale.

## D003 — 2026-08-09 — Mémoire persistante Markdown

Les fichiers `.md` du dépôt constituent la mémoire persistante opérationnelle.

## D004 — 2026-08-09 — Source avant analytics

`SOURCE → INVENTAIRE → EXTRACTION EXHAUSTIVE → RAW → CONTRÔLE → MAPPED → CANONICAL → DERIVED → ANALYTICS`.

## D005 — 2026-08-09 — Granularité RAW

Une observation réellement publiée devient une observation RAW distincte.

## D006 — 2026-08-09 — PUBLISHED vs DERIVED

Une valeur explicitement publiée reste `PUBLISHED`; toute reconstruction/calcul interne est `DERIVED`.

## D007 — 2026-08-09 — Périodes

Le nom d'un fichier/dossier ne suffit jamais pour déterminer la période économique.

## D008 — 2026-08-09 — Versions et doublons

Les doublons, versions, fichiers révisés et restatements sont conservés et reliés.

## D009 — 2026-08-09 — Modèle sectoriellement neutre

Le cœur RAW ne doit pas être spécifique à un secteur.

## D010 — 2026-08-09 — Étendre le schéma uniquement sur preuve

Aucune nouvelle table/colonne ne doit être ajoutée uniquement par anticipation.

## D011 — 2026-08-09 — Passe conceptuelle 48 sociétés

`DISCOVERY_PASS_48_ISSUERS_COMPLETE`; `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE`.

## D012 — 2026-08-09 — Sources externes et GitHub

GitHub conserve la gouvernance et la mémoire opérationnelle ; les fichiers originaux externes restent les preuves primaires.

## D013 — 2026-08-09 — PDF scanné

Absence de texte natif ≠ document vide. Ordre : texte natif → rendu visuel → OCR en dernier recours.

## D014 — 2026-08-09 — Données contextuelles externes dans un rapport

Prévoir `subject_scope_raw`, `reference_entity_raw`, `reference_product_raw` lorsque nécessaire.

## D015 — 2026-08-09 — Réalisé vs prévision

Prévisions/guidances/targets publiées distinctes du réalisé.

## D016 — 2026-08-09 — Audit et assurance

Distinguer audit, attestation, examen limité et autres formes d'assurance.

## D017 — 2026-08-09 — Événements

Les événements chiffrés ou datés expliquant les comptes doivent être conservés avec statut/source. `event_facts_raw` reste une table candidate.

## D018 — 2026-08-09 — Réglementaire

Les ratios prudentiels/normes publiés restent `PUBLISHED`. `regulatory_facts_raw` reste une table candidate.

## D019 — 2026-08-09 — Sources révisables mais historisées

Le registre des sources est vivant ; une révision ne réécrit jamais silencieusement l'historique.

## D020 — 2026-08-09 — Continuité obligatoire pour tous les agents

Tout agent reprend au point officiel de `SUIVI.md` sans régression.

## D021 — 2026-08-09 — Vérification initiale du script Python Drive

Ancien constat issu d'une recherche textuelle : aucun `.py` trouvé.

Statut : `SUPERSEDED_BY_D022`.

## D022 — 2026-08-09 — Correction : script Python confirmé à la racine

La liste directe confirme `telecharger_rapports_brvm.py` (Drive ID `1F1WRVMG4C27EOTMq5Gt9FT9Mosv-Rryz`, 14546 octets, mapping 48 sociétés).

Pour la présence directe d'un objet Drive, privilégier l'inventaire du dossier à une recherche textuelle potentiellement incomplète.

## D023 — 2026-08-09 — Méthode P1 d'inventaire

`RACINE → DOSSIER SOCIÉTÉ → SOUS-DOSSIERS DIRECTS → FICHIERS → MÉTADONNÉES/HASH → VERSIONS/DOUBLONS → PÉRIODES RÉELLES`.

Un suffixe `_2`, `_3`, etc. n'est pas une preuve de doublon binaire.

## D024 — 2026-08-09 — Validation de l'attribution émetteur

La présence physique d'un fichier sous un dossier société ne suffit pas à valider son attribution à cet émetteur.

Prévoir `issuer_assignment_status = VALIDATED | REVIEW_REQUIRED | OUT_OF_SCOPE_CONFIRMED` ou équivalent.

## D025 — 2026-08-09 — Statut du collecteur historique V1

`telecharger_rapports_brvm.py` est reconnu comme **collecteur historique ayant servi à constituer le corpus Drive**.

Décision : conserver la V1 comme référence ; ne pas la modifier silencieusement ; ne pas utiliser une évolution future pour écraser l'historique ; documenter toute V2 séparément et vérifier la non-régression avant usage.

## D026 — 2026-08-09 — Collecteur V2 incrémental et versionné

Le futur collecteur doit comparer la source BRVM courante à un manifeste persistant.

Principe :

`DISCOVER → COMPARE_MANIFEST → DOWNLOAD_DELTA → HASH → VALIDATE → VERSION_LINK → STORE → REPORT`.

Il doit détecter nouveaux documents, nouvelles années, même URL avec contenu révisé, documents `annule/remplace/corrige`, doublons par hash, changements de catalogue et nouveaux/slugs modifiés.

## D027 — 2026-08-09 — P1 avant activation du collecteur V2

Ordre : terminer P1 → créer le manifeste machine-lisible → développer V2 en dry-run → comparer/valider le delta → seulement ensuite autoriser le téléchargement incrémental.

Document : `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## D028 — 2026-08-09 — Réconciliation de fraîcheur avec la BRVM courante

P1 peut enregistrer `REMOTE_DELTA_IDENTIFIED` lorsqu'une comparaison directe avec la page BRVM officielle révèle des publications absentes du corpus Drive.

Ces documents ne sont pas automatiquement téléchargés pendant P1.

Premiers cas vérifiés : BOAC et BOAM.

## D029 — 2026-08-09 — Roadmap canonique du projet

Le plan complet est fixé dans `ROADMAP.md`.

Phases :

- `P0` gouvernance ;
- `P1` inventaire SOURCE historique ;
- `P1-FRESH` réconciliation et maintien à jour via collecteur V2 ;
- `P2` schéma RAW v1 ;
- `P3` extraction RAW exhaustive ;
- `P4` contrôle / qualité / lineage ;
- `P5` MAPPED ;
- `P6` CANONICAL ;
- `P7` DERIVED ;
- `P8` ANALYTICS.

Cette séparation ne change pas l'architecture de données à six couches ; elle explicite seulement les phases de réalisation.

## D030 — 2026-08-09 — Deltas de fraîcheur BOAN et BOAS

La comparaison P1 avec le catalogue BRVM courant confirme aussi `REMOTE_DELTA_IDENTIFIED` pour :

- BOAN : publications S2/annuelles 2025 et T1 2026 au minimum non représentées par leur équivalent évident dans le Drive ;
- BOAS : publications T1 2026 / états financiers T1 2026 au minimum, sans dossier Drive 2026.

Ces éléments restent des deltas documentés ; aucun téléchargement automatique n'est déclenché pendant P1.

## D031 — 2026-08-09 — Accélération P1 et reconnaissance PDF en parallèle

L'inventaire n'est pas la finalité du projet. Il sert à construire des bases de données à partir des données reconnues dans les PDF.

Décision : P1 passe en mode `BATCH_FAST` pour les tâches répétitives de métadonnées et ajoute une sous-phase parallèle `P1-R PDF_RECOGNITION_DISCOVERY`.

P1-R est autorisée avant P2/P3 uniquement pour apprendre/documenter les structures récurrentes et exceptions ; elle ne doit pas être présentée comme extraction RAW exhaustive.

Document de référence : `docs/PDF_RECOGNITION_STRATEGY.md`.

## D032 — 2026-08-09 — Règles de reconnaissance vérifiées sur BICC/BIIC et lot 8–12

Des PDF ont été rendus visuellement et leur texte natif vérifié dans P1-R.

Décisions :

1. **Métadonnées PDF non souveraines** : les métadonnées internes sont conservées mais ne peuvent pas déterminer seules l'émetteur, la période ou le type documentaire. BIIC T2 2025 contient une métadonnée `Title` incompatible avec le contenu visible. Contradiction → `DOCUMENT_METADATA_MISMATCH / REVIEW_REQUIRED`.
2. **T2 est supporté** : le document BIIC confirme explicitement `DEUXIEME TRIMESTRE 2025`. Le classifieur doit reconnaître T1/T2/T3/T4/S1/S2 et autres périodes publiées.
3. **Stock vs flow dépend du contexte de tableau** : le libellé de période `juin-25` est un stock pour les indicateurs de bilan et un cumul/flux pour les indicateurs de compte de résultat.
4. **Variations publiées = RAW** : colonnes `Variation Valeur` et `Variation %` sont conservées comme observations publiées, même recalculables.
5. **Tableau et narratif peuvent republier la même réalité sous unités/arrondis différents** : ne pas fusionner silencieusement en RAW.
6. **Géométrie nécessaire** : BICC 2022 montre ACTIF/PASSIF et engagements donné/reçu côte à côte ; la position des cellules fait partie de la sémantique.
7. **Filename ≠ identité** : collisions jusqu'à `_11` observées. `_2/_3/...` n'est pas un doublon ; `_rev` déclenche `VERSION_REVIEW_REQUIRED` mais ne suffit pas à établir la supersession.
8. **Framework et scope indépendants** : AGLC 2020 publie séparément des comptes individuels IFRS et consolidés IFRS ; `accounting_framework_raw` et `consolidation_scope_raw` sont deux dimensions distinctes.
9. **Corpus sparse autorisé** : BIIC possède un historique Drive très court ; aucune période/document ne doit être synthétisé pour combler une lacune SOURCE.

Profils de preuve :

- `docs/recognition_profiles/BANKING_FINANCIAL_STATEMENTS_BICC_2022.md`
- `docs/recognition_profiles/BANKING_ACTIVITY_BIIC_T2_2025.md`
