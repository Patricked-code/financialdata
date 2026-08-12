# P1 SOURCE — Bank of Africa Burkina Faso / BOABF

Date de vérification : 2026-08-12

Drive folder : `1hQwExoX3z7LZKg89inSre8bKGjFoZ-lP`

Statut : `P1_INVENTORIED / LIVE_SOURCE_RECHECKED_NO_DELTA / SHA256_COMPLETE`

## Sous-dossiers directs

18 dossiers :

`2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, divers`

## Revérification live 2026-08-12

Les 18 dossiers directs ont été relus individuellement.

- snapshot précédent : **57 PDF** ;
- live strict : **57 PDF** ;
- delta : **0** ;
- total projet V13 inchangé : **3 046 PDF**.

Les dossiers **2015, 2017 et 2018 sont toujours réellement vides** lors de la revérification live. Cela ne signifie pas absence de données économiques pour ces périodes : le contenu de `divers` couvre notamment FY 2017.

## Nombre de fichiers par dossier de classement

| Dossier | Fichiers |
|---|---:|
| 2009 | 1 |
| 2010 | 3 |
| 2011 | 3 |
| 2012 | 4 |
| 2013 | 3 |
| 2014 | 4 |
| 2015 | 0 |
| 2016 | 1 |
| 2017 | 0 |
| 2018 | 0 |
| 2019 | 6 |
| 2020 | 1 |
| 2021 | 7 |
| 2022 | 5 |
| 2023 | 6 |
| 2024 | 6 |
| 2025 | 4 |
| divers | 3 |
| **TOTAL** | **57** |

## SHA-256

- **57 / 57 PDF matérialisés et hashés** ;
- **57 / 57 tailles Drive ↔ fichiers locaux validées** ;
- **56 SHA uniques** ;
- **1 groupe de doublons binaires exacts** ;
- aucun autre doublon exact parmi les 57 sources ;
- registre : `inventory/hashes/BOABF.csv`.

### Groupe exact BOABF — états financiers FY 2017

Les deux objets physiques :

- `divers_Etats_Financiers_BOABF.pdf` — Drive `1mLDRIfTmxeeWNAE8xKfJGQVDvYVN8Ya5` ;
- `divers_Etats_Financiers_BOABF_2.pdf` — Drive `1LWk4x6_lpIG8zq6piF-dxCYDC69ND98Y` ;

ont exactement :

- taille : **814 269 octets** chacun ;
- SHA-256 : `cda4d28d932b4b1c715a83170279d312000cfce9e4f1b487597d3db1b3821979` ;
- statut : `EXACT_DUPLICATE`.

Les deux Drive IDs restent conservés comme sources physiques distinctes. Aucune suppression ni fusion SOURCE.

## Période économique de la paire `divers`

Le PDF a été rendu visuellement le 2026-08-12. La première page affiche explicitement :

- `BOA-BF` ;
- `Rapports des Commissaires aux comptes à l’Assemblée générale ordinaire des actionnaires` ;
- **`Exercice clos le 31 décembre 2017`** ;
- **`ANNEXES : Etats financiers au 31 décembre 2017`** ;
- `Bilan et Hors bilan / Compte de résultat`.

Verdict :

`ECONOMIC_PERIOD = FY_2017 / CONTENT_VISUALLY_RESOLVED`

La présence de ces états dans `divers` démontre une nouvelle fois que la couverture économique ne peut pas être inférée uniquement depuis l’existence ou l’absence d’un dossier annuel.

## Familles de documents observées

- rapports annuels historiques ;
- états financiers ;
- rapports T1 ;
- rapports T3 ;
- rapports S1 ;
- rapports S2 ;
- rapports CAC ;
- fiche boursière ;
- documents historiques rangés dans `divers`.

## Règles confirmées

- suffixe `_2`, `_3`, `_4`, `_5` ≠ preuve de doublon/version ;
- dossier vide ≠ absence de période économique ;
- doublon binaire exact = preuve SHA, tout en conservant chaque objet physique SOURCE ;
- contenu PDF > nom et dossier pour période/type.

## Restant transversal

`SHA256 = COMPLETE_57_OF_57` ; `EXACT_DUPLICATES = ONE_GROUP_TWO_OBJECTS` ; `VERSION_LINKS = CONTENT_REVIEW_REMAINING_FOR_BINARY_DISTINCT_VARIANTS` ; `ECONOMIC_PERIODS = PARTIAL_WITH_DIVERS_FY2017_RESOLVED` ; `REMOTE_FRESHNESS = RECHECKED_NO_DELTA`.
