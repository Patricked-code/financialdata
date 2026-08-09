# P1 SOURCE — Oragroup / ORGT

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA_COMPLETE`

- Ticker : `ORGT`
- Dossier Drive : `1QrW_-bDR6rzYT5cRljX8I9JhKztYWSkN`
- Dossiers directs : **8**, années `2018` à `2025`
- Premier inventaire de session : **23 PDF**
- État Drive live revérifié par parents + MIME : **35 PDF**
- Delta live : **+12 PDF**

## Particularités SOURCE

- corpus récent et continu au niveau dossiers ;
- familles T1/S1/T3, états financiers, CAC/attestations ;
- 2018 : états financiers + rapport annuel ;
- 2019 : S1, T3 et deux états financiers physiques ;
- 2020 : T1, S1, T3, deux états financiers et deux rapports CAC annuels ;
- 2021 : T1, S1, T3, états financiers et deux rapports CAC S1 ;
- 2022 : T1, S1, T3, états financiers, attestation CAC S1 ;
- 2023 : T1, T3, états financiers, attestation CAC S1 ;
- 2024 : S1, T3, états financiers ;
- 2025 : T1, S1, T3 et attestation CAC S1.

Plusieurs fichiers supplémentaires ont des `created_time` Drive observés vers 06:33–06:34Z, après le premier inventaire.

## SHA-256

Les **35 PDF** ont été matérialisés depuis Drive puis hashés avec contrôle des tailles.

- `SHA256_ORGT = COMPLETE_35_35` ;
- contenus binaires uniques : **35 / 35** ;
- doublons binaires exacts trouvés : **0** ;
- registre : `inventory/hashes/ORGT.csv`.

Les couples suivants ont tous des SHA distincts :

- états financiers ORGT 2019 plain / `_2` ;
- états financiers ORGT 2020 plain / `_2` ;
- rapports CAC annuels ORGT 2020 plain / `_2` ;
- rapports CAC S1 ORGT 2021 plain / `_2`.

Leur éventuelle relation de version ou complément reste sémantique et ne doit pas être déduite du nom.

## Règle

Le total live a été recompté sans filtre de nom, uniquement sur les huit dossiers parents et `mimeType = application/pdf`. Les 35 sources physiques restent distinctes dans SOURCE.

## Restant transversal

`DOCUMENT_MANIFEST_ORGT = ROW_COVERAGE_35_35 / SHARD_BACKFILL_PENDING` ; `SHA256_ORGT = COMPLETE_35_35` ; `BINARY_DUPLICATES = NONE_FOUND` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
