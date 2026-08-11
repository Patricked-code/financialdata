# P1 INVENTORY — Bank of Africa Sénégal / BOAS

Date de vérification : 2026-08-11

Drive folder : `1Yc_zVZwKHCKhmYZaUd1GsMZAX-mMz84-`

Statut : `FILE_INVENTORIED / LIVE_FRESHNESS_RECHECKED / SHA256_COMPLETE / REMOTE_DELTA_IDENTIFIED`

## Sous-dossiers directs

17 dossiers : années `2010` à `2025` incluses + `divers`.

Aucun dossier 1998–2009 n'est présent dans l'arborescence directe actuelle.

## Nombre de fichiers par dossier de classement

Revérification live 2026-08-11, strictement par dossiers parents + MIME PDF :

| Dossier | Fichiers |
|---|---:|
| 2010 | 1 |
| 2011 | 2 |
| 2012 | 1 |
| 2013 | 0 |
| 2014 | 1 |
| 2015 | 2 |
| 2016 | 2 |
| 2017 | 3 |
| 2018 | 2 |
| 2019 | 4 |
| 2020 | 4 |
| 2021 | 3 |
| 2022 | 4 |
| 2023 | 4 |
| 2024 | 3 |
| 2025 | 5 |
| divers | 2 |
| **TOTAL** | **43** |

Le total live reste **43 PDF** : aucun delta par rapport au snapshot précédent.

## Familles documentaires observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1/T3/T4 ;
- rapports S1/S2 ;
- attestations CAC ;
- fiche boursière ;
- fichiers avec noms BRVM source non standardisés.

## Dossier vide observé

`2013` est présent mais aucun PDF direct n'a été retrouvé dans ce dossier lors de la revérification live.

Règle : ne pas assimiler ce vide de classement à une absence de données économiques avant revue documentaire et catalogue distant.

## `divers`

Deux fichiers :

- `fiche_sn.pdf` ;
- `divers_Rapport_S1_BOAS.pdf`.

La période du second a été résolue depuis son contenu visuel, et non depuis le dossier de classement :

- titre visible : **« RAPPORT D’ACTIVITE DU PREMIER SEMESTRE 2019 »** ;
- colonnes : premier semestre 2019, premier semestre 2018, exercice 2018 ;
- date visible : **« Fait à Dakar, le 09/09/2019 »** ;
- période économique/documentaire résolue : `S1_2019`.

Cette observation confirme la règle SOURCE : un dossier `divers` ne doit jamais déterminer la période d'un document.

## SHA-256

- **43 / 43 PDF matérialisés et hashés** ;
- **43 / 43 tailles Drive ↔ fichiers hashés validées** ;
- **43 SHA uniques** ;
- **zéro doublon binaire exact** ;
- registre : `inventory/hashes/BOAS.csv`.

Les variantes historiques `_2` / `_3` ne sont donc pas des doublons binaires exacts. En particulier :

- 2011 rapports annuels `_2` / `_3` : hashes distincts ;
- 2015 rapports annuels `_2` / `_3` : hashes distincts ;
- 2017 états financiers plain / `_2` : hashes distincts.

Aucune relation de supersession n'est inférée uniquement à partir du suffixe ; une revue de contenu serait nécessaire pour qualifier la relation sémantique précise.

## Delta BRVM courant observé

La page officielle BRVM de BOA Sénégal publiait déjà lors de la passe initiale des nouveautés 2026, notamment :

- `Etats Financiers - 1er trimestre 2026` ;
- `Rapport d'activités - 1er trimestre 2026` ;
- `Etats financiers - Exercice 2025` ;
- rapports T1/S1/T3/T4 2025.

Le Drive conserve actuellement les publications 2025 mais aucun dossier 2026 direct n'est présent.

Statut : `REMOTE_DELTA_IDENTIFIED`. Les publications 2026 restent à récupérer lors de la phase incrémentale du collecteur V2 ; elles ne sont pas inventées ni ajoutées artificiellement au corpus Drive actuel.

## Points P1 restant à faire pour BOAS

- consolider le manifeste document-level dans le maître ;
- compléter les métadonnées temporelles fines et les relations de versions historiques si nécessaire ;
- rapprocher les nouveautés 2026 via le collecteur V2.
