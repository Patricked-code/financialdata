# P1 SOURCE — Société Ivoirienne de Banque / SIBC

Date : 2026-08-11
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_PENDING`

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

## Règle

Les 49 objets restent des sources physiques distinctes jusqu'au verdict SHA/contenu. Les trois T1 2017 de même taille sont des candidats de duplication exacte, jamais une duplication supposée. Les suffixes `_rev`, `_2`, `_3` ne prouvent pas une relation de version.

## Restant transversal

`SHA256 = IN_PROGRESS_0_OF_49_AFTER_V13_RECHECK` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = RECHECKED_DELTA_PLUS_3`.
