# P1 INVENTORY — Bank of Africa Mali / BOAM

Date de vérification : 2026-08-09

Drive folder : `127BPCvkfMC25L3hXZ4dKo1NEW_eg0FRK`

Statut : `FILE_INVENTORIED / HASH_PENDING / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

16 dossiers : `2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, divers`.

Le dossier `2015` n'est pas présent.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 2010 | 1 |
| 2011 | 3 |
| 2012 | 2 |
| 2013 | 0 |
| 2014 | 0 |
| 2016 | 1 |
| 2017 | 3 |
| 2018 | 2 |
| 2019 | 4 |
| 2020 | 5 |
| 2021 | 4 |
| 2022 | 5 |
| 2023 | 7 |
| 2024 | 4 |
| 2025 | 2 |
| divers | 1 |
| **TOTAL** | **44** |

## Familles observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1/T3/T4 ;
- rapports S1 ;
- attestations CAC ;
- rapports CAC annuels ;
- rapport du conseil d'administration / assemblée générale ;
- fiche boursière dans `divers` ;
- documents avec noms source non standardisés.

## Dossiers vides / lacunes de classement

- dossiers 2013 et 2014 présents mais vides ;
- dossier 2015 absent.

Ne pas assimiler ces constats à l'absence de données économiques avant analyse des comparatifs, `divers` et sources distantes.

## Version explicitement signalée

`2021_Etats_Financiers_BOAM_rev.pdf`

Drive ID : `1EWdFXD8BAVYdiPDXGPmiTb6nKAhGRYFv`

Le suffixe `_rev` provient du mécanisme historique de détection de mots comme `annule`, `remplace`, `corrige`, `revision` dans le nom source.

Statut : `VERSION_REVIEW_REQUIRED` jusqu'à identification de la version antérieure et comparaison de contenu/hash.

## Documents de gouvernance/corporate

Le dossier 2022 contient :

`rapport_du_conseil_dadministration_-_assemblee_generale_ordinaire_-_boa_mali.pdf`

Il doit être conservé dans SOURCE et pourra alimenter plus tard `corporate_facts_raw` / `event_facts_raw` selon son contenu.

## Delta BRVM courant identifié le 2026-08-09

La page officielle BRVM BOA Mali publie actuellement au moins :

- `Rapport d'activités - 1er trimestre 2026` ;
- `Etats financiers - Exercice 2025` ;
- `Rapport d'activités - 3ème trimestre 2025` ;
- `Rapport d'activités - 1er semestre 2025` ;
- `Rapport d'activités au 1er trimestre 2025`.

Le corpus Drive BOAM contient pour 2025 seulement :

- `2025_Rapport_T1_BOAM.pdf` ;
- `2025_Rapport_S1_BOAM.pdf`.

Aucun dossier 2026 n'est présent.

Donc, au minimum, trois documents actuellement visibles sur la BRVM ne sont pas représentés par leur équivalent évident dans l'inventaire Drive :

- T3 2025 ;
- états financiers 2025 ;
- T1 2026.

Statut : `REMOTE_DELTA_IDENTIFIED`.

P1 documente le delta sans écraser ni modifier le corpus historique.

## Points P1 restant à faire pour BOAM

- hash des 44 fichiers ;
- rapprochement de `2021_Etats_Financiers_BOAM_rev.pdf` avec sa version antérieure ;
- résolution des périodes économiques ;
- validation des dossiers vides 2013/2014 et de l'absence 2015 ;
- rapprochement contrôlé du delta BRVM courant ;
- inventaire machine lisible complet avec tailles/dates/checksums.
