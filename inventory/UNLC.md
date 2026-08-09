# P1 SOURCE — Unilever Côte d'Ivoire / UNLC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA_COMPLETE`

- Ticker : `UNLC`
- Dossier Drive : `12cli_1dw7QDl99D8oe09Co4fj087EZh8`
- Dossiers directs : **9** = années `2016–2023` + `divers`
- Premier inventaire de session : **20 PDF**
- État Drive live revérifié par parents + MIME : **23 PDF**
- Delta live : **+3 PDF**

## Particularités SOURCE

- aucun dossier 2024/2025 observé ;
- 2016 : S1 + états financiers ;
- 2017 : T1, publication semestrielle, publication T3, attestation CAC annuelle ;
- 2018 : rapport annuel ;
- 2019 : T1, attestation CAC annuelle et publication annuelle non auditée rangée dans `divers` ;
- 2020 : T1, états financiers, CAC annuel et deux rapports annuels physiques ;
- 2021 : T1, états financiers, annuel ;
- 2022 : T1, états financiers, annuel ;
- 2023 : T1, états financiers.

## SHA-256

Les **23 PDF** ont été matérialisés depuis Drive puis hashés avec contrôle des tailles.

- `SHA256_UNLC = COMPLETE_23_23` ;
- contenus binaires uniques : **23 / 23** ;
- doublons binaires exacts trouvés : **0** ;
- registre : `inventory/hashes/UNLC.csv`.

Les deux rapports annuels 2020 sont distincts :

- `2020_Rapport_Annuel_UNLC.pdf` → `ce866361e7ddd33e9034eaae8bf9e0812489644fd0354b4a714c62608e7f4885` ;
- `2020_Rapport_Annuel_UNLC_2.pdf` → `e910a2164613392e337869f60361af5d646b030433b442f16a2e723b1734f56f`.

Le suffixe `_2` ne constitue donc pas une duplication binaire ; la relation sémantique éventuelle reste à déterminer depuis le contenu.

## Règle

Le total live est obtenu sans filtre de nom, uniquement par les 9 dossiers parents et `mimeType = application/pdf`. Les 23 sources physiques restent conservées.

## Restant transversal

`DOCUMENT_MANIFEST_UNLC = ROW_COVERAGE_23_23 / SHARD_BACKFILL_PENDING` ; `SHA256_UNLC = COMPLETE_23_23` ; `BINARY_DUPLICATES = NONE_FOUND` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
