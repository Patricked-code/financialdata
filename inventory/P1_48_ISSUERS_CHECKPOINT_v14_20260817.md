# P1 SOURCE — checkpoint inventaire live V14

Date : 2026-08-17
Dépôt canonique : `Patricked-code/financialdata`
Branche autorisée : `main` uniquement.

## État

- sociétés : **48 / 48** ;
- total live précédent V13 : **3 046 PDF** ;
- BOAC précédent : **60 PDF** ;
- revérification BOAC strictement par ses 19 dossiers parents (`2008` à `2025` + `divers`) avec `mimeType = application/pdf` : **74 PDF** ;
- delta BOAC : **+14 PDF** ;
- nouveau total live V14 : **3 060 PDF**.

## Détail du delta BOAC

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

## Règle de preuve

Le delta est persisté **avant tout calcul SHA BOAC**. Aucun fichier n'est fusionné, supprimé ou considéré comme doublon sur la base du nom, du suffixe ou de la taille seule.

Plusieurs objets nouvellement visibles dans les dossiers historiques ont un `createdTime` Drive du 2026-08-09 vers 06:36–06:37, postérieur à l'inventaire initial BOAC effectué plus tôt le 2026-08-09. Le checkpoint enregistre uniquement l'état live constaté ; la qualification des versions/doublons est reportée à la passe SHA/contenu.

## Particularités à contrôler au hash

- nombreux suffixes `_2`, `_3`, `_4`, `_5` sur 2009–2015 ;
- `2021_Rapport_S1_BOAC.pdf` et `_2` ont tous deux une taille Drive de **1 559 400 octets** : candidat doublon exact à prouver exclusivement par SHA-256 ;
- `2019_Etats_Financiers_BOAC.pdf` et `_2` ont tous deux une taille Drive de **314 350 octets** : candidat doublon exact à prouver exclusivement par SHA-256 ;
- `divers_Rapport_S1_BOAC.pdf` nécessite toujours une résolution de période depuis le contenu ;
- le delta BRVM externe déjà documenté (EF 2025 et T1 2026 absents du corpus Drive inventorié) reste distinct de ce delta Drive interne.

Statut : `INVENTORY_COMPLETE_48_OF_48_LIVE_REFRESH_V14 / BOAC_HASH_PENDING`.
