# P1 INVENTORY — Bank of Africa Côte d'Ivoire / BOAC

Date de vérification : 2026-08-09

Drive folder : `1GNIORLdGneVshpR3oOBmq2_xDxKAu86g`

Statut : `FILE_INVENTORIED / HASH_PENDING / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

19 dossiers : années `2008` à `2025` incluses + `divers`.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 2008 | 0 |
| 2009 | 0 |
| 2010 | 2 |
| 2011 | 3 |
| 2012 | 4 |
| 2013 | 3 |
| 2014 | 2 |
| 2015 | 3 |
| 2016 | 2 |
| 2017 | 4 |
| 2018 | 5 |
| 2019 | 7 |
| 2020 | 5 |
| 2021 | 3 |
| 2022 | 4 |
| 2023 | 4 |
| 2024 | 4 |
| 2025 | 3 |
| divers | 2 |
| **TOTAL** | **60** |

## Familles observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1/T3 ;
- rapports S1 ;
- attestations CAC ;
- rapports CAC annuels ;
- publications avec noms source non standardisés ;
- fiche boursière dans `divers`.

## Dossiers vides

`2008` et `2009` sont présents mais vides dans l'inventaire Drive actuel.

Règle : dossier vide ≠ absence de période économique.

## `divers`

Deux fichiers observés :

- `fiche_ci_0.pdf` ;
- `divers_Rapport_S1_BOAC.pdf`.

Le second nécessite résolution de période depuis le contenu.

## Candidats versions / collisions de noms

Nombreux suffixes `_2`, `_3`, `_4`, `_5` sur les rapports annuels et certains états financiers historiques.

Statut : `DUPLICATE_REVIEW_PENDING` jusqu'au hash/contenu.

## Delta BRVM courant identifié le 2026-08-09

La page officielle courante BOA Côte d'Ivoire publie notamment :

- `Rapport des Commissaires Aux Comptes et Etats Financiers annuels - Exercice 2025` ;
- `Rapport d'activités - 1er trimestre 2026`.

URLs PDF observées :

- `https://www.brvm.org/sites/default/files/20260612_-_rapport_des_commissaires_aux_comptes_et_etats_financiers_annuels_-_exercice_2025_-_boa_ci.pdf`
- `https://www.brvm.org/sites/default/files/20260601_-_rapport_dactivites_-_1er_trimestre_2026_-_boa_ci.pdf`

Dans le corpus Drive inventorié :

- le dossier 2025 contient seulement T1, S1 et T3 ;
- aucun dossier 2026 n'est présent ;
- l'état financier 2025 courant et le T1 2026 ne sont donc pas encore représentés dans le Drive inventorié.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Important : P1 documente ce delta ; il ne télécharge pas encore automatiquement ces documents tant que le collecteur V2 et le manifeste incrémental ne sont pas validés.

## Conséquence pour le collecteur

BOAC est le premier cas P1 où l'on a vérifié directement un écart entre le corpus Drive et la page BRVM courante.

Cela valide le besoin de :

- `first_seen_at` / `last_seen_at` ;
- comparaison du catalogue courant au manifeste local ;
- téléchargement incrémental ;
- détection de nouvelle version ;
- suivi des documents distants absents localement.

Voir `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## Points P1 restant à faire pour BOAC

- hash des 60 fichiers ;
- revue des collisions `_2/_3/...` ;
- résolution de la période de `divers_Rapport_S1_BOAC.pdf` ;
- validation détaillée des types documentaires ;
- rapprochement contrôlé avec le delta BRVM courant ;
- inventaire machine lisible complet avec tailles/dates/checksums.
