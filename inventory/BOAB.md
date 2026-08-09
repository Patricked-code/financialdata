# P1 INVENTORY — Bank of Africa Bénin / BOAB

Date de vérification : 2026-08-09

Drive folder : `1F_xz9lxMql3HH2OY9IQtLyo7vkxsO6YM`

Statut : `FILE_INVENTORIED / HASH_PENDING / OUT_OF_SCOPE_REVIEW`

## Sous-dossiers directs

29 dossiers : années `1998` à `2025` incluses + `divers`.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 1998 | 1 |
| 1999 | 0 |
| 2000 | 0 |
| 2001 | 0 |
| 2002 | 0 |
| 2003 | 1 |
| 2004 | 1 |
| 2005 | 0 |
| 2006 | 1 |
| 2007 | 1 |
| 2008 | 1 |
| 2009 | 2 |
| 2010 | 2 |
| 2011 | 4 |
| 2012 | 3 |
| 2013 | 3 |
| 2014 | 3 |
| 2015 | 0 |
| 2016 | 0 |
| 2017 | 2 |
| 2018 | 5 |
| 2019 | 4 |
| 2020 | 4 |
| 2021 | 5 |
| 2022 | 4 |
| 2023 | 4 |
| 2024 | 4 |
| 2025 | 3 |
| divers | 1 |
| **TOTAL** | **59** |

## Familles observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1/T3 ;
- rapports S1 ;
- rapports/attestations CAC ;
- fichiers avec noms source non standardisés ;
- fiche boursière dans `divers`.

## Dossiers vides observés

`1999, 2000, 2001, 2002, 2005, 2015, 2016`.

Règle : ne pas conclure à l'absence de période économique avant vérification de `divers`, des comparatifs contenus dans d'autres documents et des sources futures.

## Anomalie de périmètre détectée

Dans le dossier `2021`, l'inventaire contient :

`avis_ndeg232_brvmdg_-_premiere_cotation_-_tpci_590_2021-2031_1.pdf`

Drive ID : `1Kwjh33LePuBodRHQvErNqfReIIu8a6g-`

Le titre concerne une première cotation `TPCI 5,90% 2021-2031` et ne permet pas de l'attribuer à BOA Bénin.

Statut : `OUT_OF_SCOPE_REVIEW`.

Règle :

- conserver le fichier et sa provenance actuelle ;
- ne pas le supprimer pendant P1 ;
- ne pas l'associer comme document BOAB validé tant que son contenu/contexte n'a pas confirmé le lien ;
- prévoir `scope_validation_status` / `issuer_assignment_status` dans le registre documentaire ;
- si le classement est erroné, documenter la correction et préserver l'ancien chemin comme provenance historique.

## Candidats versions / collisions de noms

Nombreux suffixes `_2`, `_3`, `_4`, `_6` dans les rapports annuels 2008–2014.

Ils restent `DUPLICATE_REVIEW_PENDING` jusqu'à comparaison par hash/contenu.

## Points P1 restant à faire pour BOAB

- hash de tous les fichiers ;
- revue des candidats versions/doublons ;
- validation du fichier TPCI hors périmètre probable ;
- résolution des périodes économiques ;
- vérification du rôle de `fiche_bj_0.pdf` ;
- inventaire machine lisible avec tailles/dates/checksums.
