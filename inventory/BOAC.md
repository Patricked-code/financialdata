# P1 INVENTORY — Bank of Africa Côte d'Ivoire / BOAC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Drive folder : `1GNIORLdGneVshpR3oOBmq2_xDxKAu86g`

Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

19 dossiers : années `2008` à `2025` incluses + `divers`.

## Nombre de fichiers par dossier — live V14

| Dossier | V13 | Live V14 | Delta |
|---|---:|---:|---:|
| 2008 | 0 | 1 | +1 |
| 2009 | 0 | 2 | +2 |
| 2010 | 2 | 4 | +2 |
| 2011 | 3 | 4 | +1 |
| 2012 | 4 | 5 | +1 |
| 2013 | 3 | 4 | +1 |
| 2014 | 2 | 4 | +2 |
| 2015 | 3 | 3 | 0 |
| 2016 | 2 | 2 | 0 |
| 2017 | 4 | 4 | 0 |
| 2018 | 5 | 6 | +1 |
| 2019 | 7 | 7 | 0 |
| 2020 | 5 | 5 | 0 |
| 2021 | 3 | 5 | +2 |
| 2022 | 4 | 5 | +1 |
| 2023 | 4 | 4 | 0 |
| 2024 | 4 | 4 | 0 |
| 2025 | 3 | 3 | 0 |
| divers | 2 | 2 | 0 |
| **TOTAL** | **60** | **74** | **+14** |

Checkpoint du delta : `inventory/P1_48_ISSUERS_CHECKPOINT_v14_20260817.md`.

Le delta a été persisté avant tout calcul SHA BOAC. Aucun objet n'a été supprimé, déplacé, fusionné ou dédupliqué.

## Familles observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1/T3 ;
- rapports S1 ;
- attestations CAC ;
- rapports CAC annuels ;
- publications avec noms source non standardisés ;
- fiche boursière dans `divers`.

## Dossiers anciennement vides

L'inventaire du 2026-08-09 indiquait `2008` et `2009` comme vides. La revérification du 2026-08-17 constate désormais :

- `2008` : 1 PDF ;
- `2009` : 2 PDF.

Plusieurs objets nouvellement visibles dans les dossiers historiques ont un `createdTime` Drive du 2026-08-09 vers 06:36–06:37, postérieur à l'inventaire initial effectué plus tôt ce jour-là.

Règle : dossier vide ≠ absence de période économique ; l'état live doit être revérifié avant chaque passe transverse.

## `divers`

Deux fichiers observés :

- `fiche_ci_0.pdf` ;
- `divers_Rapport_S1_BOAC.pdf`.

Le second nécessite résolution de période depuis le contenu.

## Candidats versions / collisions de noms

Nombreux suffixes `_2`, `_3`, `_4`, `_5` sur les rapports annuels et certains états financiers historiques.

Deux paires nécessitent une attention particulière au SHA car leurs tailles Drive sont identiques :

- `2019_Etats_Financiers_BOAC.pdf` / `_2` : **314 350 octets** chacun ;
- `2021_Rapport_S1_BOAC.pdf` / `_2` : **1 559 400 octets** chacun.

Statut : `DUPLICATE_REVIEW_PENDING` jusqu'à preuve SHA-256. La taille ou le nom seuls ne constituent pas une preuve de doublon.

## Delta BRVM courant identifié le 2026-08-09

La page officielle courante BOA Côte d'Ivoire publie notamment :

- `Rapport des Commissaires Aux Comptes et Etats Financiers annuels - Exercice 2025` ;
- `Rapport d'activités - 1er trimestre 2026`.

URLs PDF observées :

- `https://www.brvm.org/sites/default/files/20260612_-_rapport_des_commissaires_aux_comptes_et_etats_financiers_annuels_-_exercice_2025_-_boa_ci.pdf`
- `https://www.brvm.org/sites/default/files/20260601_-_rapport_dactivites_-_1er_trimestre_2026_-_boa_ci.pdf`

Dans le corpus Drive live V14 :

- le dossier 2025 contient T1, S1 et T3 ;
- aucun dossier 2026 n'est présent ;
- l'état financier 2025 courant et le T1 2026 ne sont donc toujours pas représentés dans le Drive inventorié.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Important : ce delta BRVM externe est distinct du delta Drive interne +14 constaté en V14. P1 documente le delta distant ; il ne télécharge pas automatiquement ces documents tant que le collecteur V2 et le manifeste incrémental ne sont pas validés.

## Conséquence pour le collecteur

BOAC confirme le besoin de :

- `first_seen_at` / `last_seen_at` ;
- comparaison du catalogue courant au manifeste local ;
- téléchargement incrémental ;
- détection de nouvelle version ;
- suivi des documents distants absents localement.

Voir `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## Points P1 restant à faire pour BOAC

- hash des **74 fichiers live V14** ;
- revue des collisions `_2/_3/...` ;
- résolution de la période de `divers_Rapport_S1_BOAC.pdf` ;
- validation détaillée des types documentaires ;
- rapprochement contrôlé avec le delta BRVM courant ;
- backfill du manifeste documentaire avec tailles/dates/checksums et métadonnées temporelles.

## Point de reprise BOAC

`BOAC_LIVE=74 | V13=60 | DELTA=+14 | CHECKPOINT=V14 | HASH=PENDING`
