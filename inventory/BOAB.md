# P1 INVENTORY — Bank of Africa Bénin / BOAB

Date de vérification initiale : 2026-08-09  
Dernière revérification live + SHA-256 : 2026-08-17

Drive folder : `1F_xz9lxMql3HH2OY9IQtLyo7vkxsO6YM`

Statut : `FILE_INVENTORIED / LIVE_RECHECK_COMPLETE / SHA256_COMPLETE / OUT_OF_SCOPE_CONFIRMED`

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

## Revérification live du 2026-08-17

- contrôle strict des 29 dossiers parents ;
- filtre MIME `application/pdf` ;
- **59 PDF live**, identiques en nombre au snapshot V13 ;
- **delta live : 0** ;
- aucun fichier SOURCE supprimé ou déplacé.

## SHA-256

- 59 / 59 fichiers matérialisés depuis Google Drive ;
- 59 / 59 signatures PDF valides (`%PDF`) ;
- tailles des octets matérialisés enregistrées ;
- 59 / 59 SHA-256 calculés ;
- **59 SHA-256 uniques** ;
- **0 groupe de doublon exact** ;
- registre : `inventory/hashes/BOAB.csv` ;
- statut registre : `COMPUTED_SIZE_VALIDATED`.

Les variantes historiques suffixées `_2`, `_3`, `_4`, `_6` ne sont donc **pas des doublons binaires exacts** entre elles dans le corpus BOAB courant. Elles restent des sources distinctes jusqu'à une éventuelle revue sémantique/versioning.

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

## Anomalie de périmètre confirmée

Dans le dossier `2021`, l'inventaire contient :

`avis_ndeg232_brvmdg_-_premiere_cotation_-_tpci_590_2021-2031_1.pdf`

Drive ID : `1Kwjh33LePuBodRHQvErNqfReIIu8a6g-`

La lecture du contenu source confirme qu'il s'agit de l'**Avis N°232–2021 / BRVM / DG**, relatif au **Trésor Public de Côte d'Ivoire** et à la première cotation de l'emprunt obligataire **TPCI 5,90 % 2021-2031**, symbole `TPCI.O66`. Le contenu ne concerne pas Bank of Africa Bénin.

Statut : `OUT_OF_SCOPE_CONFIRMED / ISSUER_ASSIGNMENT_REVIEW_REQUIRED`.

Règle :

- conserver le fichier et sa provenance actuelle ;
- ne pas le supprimer pendant P1 ;
- ne pas l'associer comme document BOAB validé ;
- prévoir `scope_validation_status` / `issuer_assignment_status` dans le registre documentaire ;
- lors de la réconciliation du manifeste, documenter son attribution correcte sans effacer l'ancien chemin comme provenance historique.

## Candidats versions / collisions de noms

Les suffixes `_2`, `_3`, `_4`, `_6` des rapports annuels 2008–2014 ont été comparés au niveau binaire lors de la passe SHA du 2026-08-17 : aucune collision SHA-256 n'a été trouvée parmi les 59 sources BOAB.

Verdict binaire : **0 `EXACT_DUPLICATE`** pour BOAB.

Les relations sémantiques éventuelles (`VERSION_OF`, `SUPERSEDES`, etc.) restent à traiter séparément et ne sont pas déduites du nom de fichier.

## Points P1 restant à faire pour BOAB

- résolution des périodes économiques fines pour l'ensemble des sources ;
- vérification/documentation du rôle exact de `fiche_bj_0.pdf` ;
- backfill du manifeste documentaire maître et des métadonnées temporelles/shards ;
- revue sémantique des versions lorsque nécessaire ;
- réconciliation de l'anomalie TPCI dans le manifeste sans perte de provenance.

## Résultat de la passe

`BOAB=59/59_SHA_COMPLETE | LIVE=59 | DELTA=0 | UNIQUE_SHA=59 | EXACT_DUPLICATE_GROUPS_ADDED=0 | OUT_OF_SCOPE_TPCI=CONFIRMED`
