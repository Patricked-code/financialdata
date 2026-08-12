# P1 SOURCE — Société Ivoirienne de Banque / SIBC

Date : 2026-08-12
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_COMPLETE`

- Ticker : `SIBC`
- Dossier Drive : `1CRsJHHElXoRpB1VsdrQX5QrZW_iWDDbl`
- Dossiers directs : **10**, années `2016–2025`
- Snapshot précédent : **46 PDF**
- Revérification live stricte par dossiers parents + MIME : **49 PDF**
- Delta live : **+3 PDF**
- Nouveau total projet V13 : **3 046 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v13_20260811.md`

## Particularités SOURCE

- 2016 : deux états financiers ;
- 2017 : trois rapports T1 (`plain`, `_2`, `_3`) de même taille **60 027 octets**, plus CAC S1, T3 et états financiers ;
- 2018 : T1, deux rapports CAC annuels, S1, T3, deux états financiers nommés `_rev` / `_rev_2`, rapport annuel ;
- 2019 : T1/S1/T3/états financiers ;
- 2020 : T1, deux rapports S1, T3, deux états financiers ;
- 2021 : T1, rapport CAC annuel, S1, T3 et états financiers ;
- 2022 : T1, deux S1, T3 et un rapport d'activité supplémentaire ;
- 2023 : T1/S1/CAC S1/T3/annuel ;
- 2024 : T1/S1/CAC S1/T3/annuel ;
- 2025 : T1/S1/T3.

## SHA-256

- **49 / 49 PDF matérialisés et hashés** ;
- **49 / 49 tailles Drive ↔ fichiers hashés validées** ;
- **46 SHA uniques** ;
- **2 groupes de doublons binaires exacts** dans SIBC ;
- registre : `inventory/hashes/SIBC.csv`.

### Groupe exact SIBC — T1 2017

- `2017_Rapport_T1_SIBC.pdf` ;
- `2017_Rapport_T1_SIBC_2.pdf` ;
- `2017_Rapport_T1_SIBC_3.pdf` ;
- **60 027 octets** chacun ;
- SHA commun `3446b816e1a15b4a8d2df8bfeff775dbaa7166b52823c0d8d2bf8f1b06fc6b23` ;
- groupe `SHA256:3446b816e1a15b4a8d2df8bfeff775dbaa7166b52823c0d8d2bf8f1b06fc6b23`.

### Groupe exact SIBC — S1 2022

- `2022_Rapport_S1_SIBC.pdf` ;
- `2022_Rapport_S1_SIBC_2.pdf` ;
- **6 481 666 octets** chacun ;
- SHA commun `b96ab01184f501d6f726250132108e742d8b5ede7ca862ce088b5aa29d7c88ec` ;
- groupe `SHA256:b96ab01184f501d6f726250132108e742d8b5ede7ca862ce088b5aa29d7c88ec`.

Tous les objets Drive restent conservés en SOURCE. Aucune suppression silencieuse.

### Variantes binaires distinctes

- les deux états financiers 2016 ont des tailles et SHA distincts ;
- les deux rapports CAC annuels 2018 ont des tailles et SHA distincts ;
- `2018_Etats_Financiers_SIBC_rev.pdf` et `_rev_2.pdf` sont binaires distincts ; le suffixe `_rev` ne prouve pas encore une relation de supersession ;
- les deux rapports S1 2020 sont binaires distincts ;
- les deux états financiers 2020 sont binaires distincts ;
- aucun autre groupe exact n'a été trouvé parmi les 49 sources.

## Règle

Les noms, dossiers et suffixes ne déterminent jamais seuls la période, le doublon ou la relation de version. Les objets physiques restent séparés jusqu'au verdict SHA/contenu.

## Restant transversal

`SHA256 = COMPLETE_49_OF_49` ; `VERSION_LINKS = CONTENT_REVIEW_REMAINING_FOR_BINARY_DISTINCT_VARIANTS` ; `ECONOMIC_PERIODS = PARTIAL` ; `REMOTE_FRESHNESS = RECHECKED_DELTA_PLUS_3`.
