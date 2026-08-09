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

Décision :

- conserver la V1 comme référence ;
- ne pas la modifier silencieusement ;
- ne pas utiliser une évolution future pour écraser l'historique ;
- documenter toute V2 séparément et vérifier la non-régression avant usage.

## D026 — 2026-08-09 — Collecteur V2 incrémental et versionné

Le futur collecteur doit comparer la source BRVM courante à un manifeste persistant.

Principe :

`DISCOVER → COMPARE_MANIFEST → DOWNLOAD_DELTA → HASH → VALIDATE → VERSION_LINK → STORE → REPORT`.

Il doit détecter : nouveaux documents, nouvelles années, même URL avec contenu révisé, documents `annule/remplace/corrige`, doublons par hash, changements de catalogue et nouveaux/slugs modifiés.

Il doit préserver `first_seen_at`, `last_seen_at`, URL source, titre BRVM, nom source, hash, taille, métadonnées HTTP, provenance et relations de version.

## D027 — 2026-08-09 — P1 avant activation du collecteur V2

Le plan V2 est documenté mais **pas implémenté** pendant le lot actuel.

Ordre :

1. terminer P1 ;
2. créer le manifeste machine-lisible de l'existant ;
3. développer V2 en `dry-run` ;
4. comparer le delta ;
5. valider ;
6. seulement ensuite autoriser le téléchargement incrémental.

Document : `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## D028 — 2026-08-09 — Réconciliation de fraîcheur avec la BRVM courante

P1 peut enregistrer un statut `REMOTE_DELTA_IDENTIFIED` lorsqu'une comparaison directe avec la page BRVM officielle révèle des publications absentes du corpus Drive.

Ces documents ne sont pas automatiquement téléchargés pendant P1 : le delta est documenté et sera traité par le mécanisme incrémental validé.

Premiers cas vérifiés : BOAC et BOAM.
