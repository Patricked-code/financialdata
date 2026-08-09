# P1 INVENTORY — Air Liquide Côte d'Ivoire / SIVC

Date de vérification : 2026-08-09

Drive folder : `1TkwLDXla5LKvdpQ_KSEFrl_yNz-X1AB2`

Statut : `FILE_INVENTORIED / HASH_PENDING`

## Sous-dossiers directs

22 dossiers annuels :

`2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025`

Constats :

- aucun dossier `2015` observé ;
- aucun dossier `divers` observé ;
- dossier `2024` présent mais aucun fichier trouvé lors de l'inventaire direct ;
- présence de noms standardisés et de noms source non standardisés.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 2003 | 1 |
| 2004 | 1 |
| 2005 | 1 |
| 2006 | 2 |
| 2007 | 2 |
| 2008 | 2 |
| 2009 | 2 |
| 2010 | 3 |
| 2011 | 3 |
| 2012 | 4 |
| 2013 | 4 |
| 2014 | 2 |
| 2016 | 2 |
| 2017 | 4 |
| 2018 | 2 |
| 2019 | 2 |
| 2020 | 4 |
| 2021 | 3 |
| 2022 | 2 |
| 2023 | 2 |
| 2024 | 0 |
| 2025 | 5 |
| **TOTAL** | **53** |

## Familles de documents observées

- rapports annuels ;
- états financiers ;
- T1 ;
- T3 ;
- S1 ;
- S2 ;
- attestations CAC ;
- rapports CAC ;
- publications avec nom source non standardisé.

## Candidats versions / doublons

Les suffixes `_2`, `_3`, `_4`, `_5` sont nombreux dans les rapports historiques. Ils ne doivent **pas** être interprétés comme doublons binaires sans hash.

Exemples :

- `2010_Rapport_Annuel_SIVC.pdf`, `_3`, `_4` ;
- `2011_Rapport_Annuel_SIVC_2.pdf`, `_3`, `_4` ;
- `2012_Rapport_Annuel_SIVC_2.pdf` à `_5` ;
- `2013_Rapport_Annuel_SIVC_2.pdf` à `_5`.

Statut : `DUPLICATE_REVIEW_PENDING`.

## Version explicitement signalée par la source

Dans le dossier 2025 :

`erium_ci_resultat_3t2025_annule_et_remplace_le_precedent_publie.pdf`

Drive ID : `1443Ihn5G-NgeGJ-CYFXY-DtLbwICtfwN`

Le nom indique explicitement « annule et remplace le précédent publié ».

Règle : créer une relation de version/supersession après identification du document précédent ; ne supprimer aucun fichier.

## Points P1 restant à faire pour SIVC

- collecter/calculer les hash de contenu ;
- confirmer les doublons exacts ;
- identifier les versions remplacées ;
- compléter les tailles/dates dans un futur inventaire machine lisible ;
- résoudre les périodes économiques depuis le contenu des documents ;
- vérifier si l'absence de dossier 2015 correspond à une lacune réelle ou à un classement ailleurs.
