# P1 SOURCE — Total Sénégal / TTLS

Date : 2026-08-11
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_PENDING`

- Ticker : `TTLS`
- Dossier Drive : `1yX73IPdGDnVtDhfzTPCj3X8z7tK11WQ2`
- Dossiers directs : **11** = années `2016–2025` + `divers`
- Snapshot précédent : **45 PDF**
- Revérification live stricte par dossiers parents + MIME : **47 PDF**
- Delta live : **+2 PDF**
- Nouveau total projet V12 : **3 043 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v12_20260811.md`

## Particularités SOURCE

- `divers_Rapport_CAC_Annuel_TTLS.pdf` : période économique à résoudre depuis le contenu ;
- 2016 comporte trois états financiers (`plain`, `_2`, `_3`) + S1 ;
- 2017 comporte T1, bilan semestriel d'un contrat de liquidité, projet de publication des états financiers de synthèse 2017 et états financiers 2017 ;
- 2018 comporte S1, CAC annuel, états financiers et deux rapports annuels physiques ; les deux annuels font exactement **3 058 310 octets** et doivent être départagés par SHA ;
- 2021–2024 contiennent plusieurs familles et variantes financières ;
- 2024 compte **7 objets physiques** dans la revérification live ;
- 2025 contient T1/S1/T3.

## Règle

Les 47 objets restent des sources physiques distinctes jusqu'au verdict hash/contenu. Le delta V12 est persisté avant hash. `divers`, les noms et les suffixes ne déterminent jamais à eux seuls la période ou la relation de version.

## Restant transversal

`SHA256 = IN_PROGRESS_0_OF_47_AFTER_V12_RECHECK` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = RECHECKED_DELTA_PLUS_2`.
