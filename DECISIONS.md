# DECISIONS — financialdata

Registre canonique des décisions validées. Une décision ne doit pas être réécrite silencieusement : si elle change, ajouter une nouvelle entrée qui explique la modification.

## D001 — 2026-08-09 — Dépôt canonique

**Décision** : `Patricked-code/financialdata` devient le dépôt canonique de mémoire persistante et de construction du projet de données financières.

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

**Observation** : l'inventaire BOAB contient dans le dossier 2021 un fichier nommé `avis_ndeg232_brvmdg_-_premiere_cotation_-_tpci_590_2021-2031_1.pdf`, dont le titre ne démontre pas de lien avec BOA Bénin.

**Décision** : la présence physique d'un fichier dans le dossier d'un émetteur ne suffit pas à valider son attribution économique/documentaire à cet émetteur.

Prévoir dans le registre SOURCE des statuts de validation tels que :

- `issuer_assignment_status = VALIDATED | REVIEW_REQUIRED | OUT_OF_SCOPE_CONFIRMED` ;
- `scope_validation_status` si nécessaire.

Un fichier suspect reste conservé avec son chemin historique jusqu'à revue. Une correction de classement doit être historisée, jamais silencieuse.
