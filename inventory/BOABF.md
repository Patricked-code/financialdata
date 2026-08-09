# P1 INVENTORY — Bank of Africa Burkina Faso / BOABF

Date de vérification : 2026-08-09

Drive folder : `1hQwExoX3z7LZKg89inSre8bKGjFoZ-lP`

Statut : `FILE_INVENTORIED / HASH_PARTIAL`

## Sous-dossiers directs

18 dossiers :

`2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, divers`

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

## Familles de documents observées

- rapports annuels ;
- états financiers ;
- rapports T1 ;
- rapports T3 ;
- rapports S1 ;
- rapports S2 ;
- attestation CAC ;
- fiche boursière ;
- documents historiques rangés dans `divers`.

## Anomalies / règles confirmées

### Dossiers annuels vides

Les dossiers 2015, 2017 et 2018 ne contiennent pas de fichier direct lors de l'inventaire actuel.

Cela ne signifie pas absence de données économiques pour ces années.

### `divers` peut combler une période

`divers_Etats_Financiers_BOABF.pdf` contient des états portant sur l'exercice clos au 31 décembre 2017 avec comparatifs 2016/2017.

Règle : mesurer la couverture par périodes contenues dans les documents, pas uniquement par dossiers.

### Doublon binaire déjà vérifié

Les deux fichiers :

- `divers_Etats_Financiers_BOABF.pdf`
- `divers_Etats_Financiers_BOABF_2.pdf`

ont déjà été vérifiés comme doublons binaires exacts dans le pilote antérieur.

SHA-256 connu :

`cda4d28d932b4b1c715a83170279d312000cfce9e4f1b487597d3db1b3821979`

Règle : conserver les deux `document_id` / Drive IDs et la relation `DUPLICATE`, mais ne pas double-compter un futur fait canonique.

## État des hash

- hash vérifié pour la paire de doublons `divers` ci-dessus ;
- hash de l'ensemble des 57 fichiers : `NOT_COMPLETE`.

## Points P1 restant à faire pour BOABF

- collecter/calculer les hash des 55 autres fichiers ;
- construire le registre machine lisible complet avec tailles/dates ;
- classer versions/collisions de noms historiques ;
- résoudre les périodes économiques de tous les documents ;
- vérifier les dossiers vides contre `divers` et contre le contenu des publications comparatives.
