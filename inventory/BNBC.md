# P1 INVENTORY — Bernabé Côte d'Ivoire / BNBC

Date : 2026-08-18
Statut : `FILE_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING / VERSION_REVIEW`

- Ticker : `BNBC`
- Dossier Drive canonique : `10u65PBoBi1nWppgn1Ttm-r96iCwdzsKs`
- Sous-dossiers directs live : **28**, années `1998–2025`
- Dossier `divers` : non observé
- Snapshot manifeste avant recheck : **78 PDF**
- Recheck live strict par les **28 parent IDs réels** + `mimeType='application/pdf'` : **92 PDF**
- Delta live : **+14**
- SOURCE global : **V20 = 3 114 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v20_20260818.md`

## Cardinal annuel live vérifié

`1998–2002: 1/an` ; `2003–2008: 2/an` ; `2009–2011: 4/an` ; `2012: 5` ; `2013: 4` ; `2014: 3` ; `2015: 2` ; `2016: 3` ; `2017: 4` ; `2018: 5` ; `2019: 9` ; `2020: 6` ; `2021: 5` ; `2022: 5` ; `2023: 3` ; `2024: 6` ; `2025: 3`.

## Particularités SOURCE à revoir après SHA

- nombreuses variantes historiques `_2/_3/_4/_5` ;
- 2019 contient **5 variantes physiques** d'états financiers (`plain`, `_2`, `_3`, `_4`, `_5`) en plus des rapports T1/S1/T3 et de l'attestation CAC S1 ;
- 2020 contient deux rapports S1 et deux états financiers ;
- 2022 et 2024 contiennent chacun deux états financiers ;
- aucun suffixe ne constitue une preuve de doublon ou de version ;
- tous les objets physiques SOURCE sont conservés.

## Passe suivante exacte

1. matérialiser les **92/92 PDF** de la liste live parent-scoped ;
2. valider tailles et signatures `%PDF-` ;
3. calculer SHA-256 sur 100 % ;
4. identifier les groupes exacts sans supprimer aucun objet ;
5. revoir les variantes 2019/2020/2022/2024 par contenu lorsque les SHA diffèrent ;
6. créer `inventory/hashes/BNBC.csv` et valider son blob GitHub post-commit ;
7. finaliser BNBC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Restant transversal

`SHA256 = IN_PROGRESS` ; `VERSION_LINKS = IN_PROGRESS` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
