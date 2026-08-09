# P1 INVENTORY — Bank of Africa Niger / BOAN

Date de vérification : 2026-08-09

Drive folder : `1qtb3jsPG28k_C3JNuEU35oKWhK5y41Xa`

Statut : `FILE_INVENTORIED / HASH_PENDING / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

28 dossiers : années `1999` à `2025` incluses + `divers`.

Aucun dossier `1998` n'a été observé dans l'arborescence directe actuelle.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 1999 | 1 |
| 2000 | 1 |
| 2001 | 1 |
| 2002 | 1 |
| 2003 | 2 |
| 2004 | 1 |
| 2005 | 2 |
| 2006 | 2 |
| 2007 | 2 |
| 2008 | 1 |
| 2009 | 0 |
| 2010 | 2 |
| 2011 | 3 |
| 2012 | 4 |
| 2013 | 2 |
| 2014 | 4 |
| 2015 | 0 |
| 2016 | 0 |
| 2017 | 0 |
| 2018 | 4 |
| 2019 | 3 |
| 2020 | 4 |
| 2021 | 5 |
| 2022 | 3 |
| 2023 | 3 |
| 2024 | 4 |
| 2025 | 4 |
| divers | 1 |
| **TOTAL** | **60** |

## Familles documentaires observées

- rapports annuels historiques ;
- rapports T1/T3 ;
- rapports S1/S2 ;
- états financiers ;
- attestations CAC ;
- rapports CAC annuels ;
- fiche boursière dans `divers` ;
- noms source non standardisés sur certaines périodes.

## Dossiers vides observés

`2009, 2015, 2016, 2017`.

Règle : ne pas interpréter ces dossiers vides comme absence de données économiques sans revue du contenu des autres documents et du catalogue BRVM.

## Candidats versions / collisions de nom

Nombreux rapports annuels historiques portent des suffixes `_2`, `_3`, `_4`, `_5`.

Ils restent `DUPLICATE_REVIEW_PENDING` tant que les hash et le contenu n'ont pas été comparés.

Exemples :

- 2003 : rapport annuel + `_2` ;
- 2005 : rapport annuel + `_2` ;
- 2006 : rapport annuel + `_2` ;
- 2007 : rapport annuel + `_3` ;
- 2010 : rapport annuel + `_4` ;
- 2011 : `_2`, `_3`, `_4` ;
- 2012 : `_2`, `_3`, `_4`, `_5` ;
- 2014 : `_2`, `_3`, `_4`, `_5`.

## Delta BRVM courant observé le 2026-08-09

La page officielle BRVM de BOA Niger publie actuellement, entre autres :

- rapport d'activités T1 2026 ;
- rapport d'activités S2 2025 ;
- rapport CAC sur les états financiers annuels 2025 ;
- rapport CAC sur conventions réglementées / crédits dirigeants 2025 ;
- rapport du Conseil d'administration à l'AGO 2025 ;
- rapport T3 2025 ;
- attestation CAC S1 2025 ;
- rapport S1 2025 ;
- rapport T1 2025.

Le dossier Drive 2025 inventorié contient T1, S1, attestation CAC S1 et T3, mais pas les équivalents évidents des publications S2/annuelles/Conseil 2025, et il n'existe pas encore de dossier 2026.

Statut : `REMOTE_DELTA_IDENTIFIED`.

Ces publications ne sont pas téléchargées pendant P1. Elles servent à valider le futur collecteur incrémental V2.

## Points P1 restant à faire pour BOAN

- calculer/collecter les hash de tous les fichiers ;
- confirmer doublons et versions historiques ;
- résoudre les périodes économiques depuis le contenu ;
- expliquer les trous 2009 et 2015–2017 ;
- produire l'inventaire machine-lisible consolidé ;
- plus tard, rapprocher le corpus Drive du catalogue BRVM courant via le collecteur V2.
