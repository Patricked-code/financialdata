# P1 SOURCE — Coris Bank International / CBIBF

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_COMPLETE_FOR_ISSUER`

- Ticker : `CBIBF`
- Dossier Drive : `1ASGO_gpl4szCOXSLJawprG078nYrjUV8`
- Dossiers directs : **4** (`2022`, `2023`, `2024`, `2025`)
- Premier inventaire de session : **8 PDF**
- État live revérifié : **15 PDF**
- Delta live : **+7 PDF**
- SHA-256 calculés : **15 / 15**
- registre hash : `inventory/hashes/CBIBF.csv`

## État live revérifié

- 2022 : **3 PDF** — annuel, états financiers, CAC annuel ;
- 2023 : **4 PDF** — T1, S1, T3, annuel ;
- 2024 : **5 PDF** — T1, S1, S1 `_2`, T3, annuel ;
- 2025 : **3 PDF** — T1, S1, T3.

Les 7 ajouts ont des `created_time` Drive autour de `2026-08-09T06:36–06:37Z`, alors que le premier inventaire avait été réalisé auparavant.

## Résultat SHA-256

Les **15 fichiers** ont été matérialisés depuis Drive puis hashés : **14 contenus binaires uniques** et un second fichier physique partageant les mêmes octets qu'un autre.

### Doublon binaire exact

- `2024_Rapport_S1_CBIBF.pdf` — Drive `1vBV6P-Of3cz9ixJOLqnVUbTc0hzFpI4E` ;
- `2024_Rapport_S1_CBIBF_2.pdf` — Drive `1Lxz7zOe-02J79x3Z0UBe-e7Ed0udTOlB` ;
- taille de chacun : **1 549 372 octets** ;
- SHA-256 commun : `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05` ;
- verdict : `EXACT_DUPLICATE`.

Les deux sources sont conservées et partagent le groupe enregistré dans `inventory/p1_duplicate_groups.csv`. Aucun autre SHA CBIBF ne se répète parmi les 15 fichiers.

## Leçon opérationnelle

Le corpus SOURCE peut évoluer pendant P1. Les snapshots historiques ne sont jamais réécrits silencieusement ; l'état live courant est enregistré séparément et les champs `first_seen_at` / `last_seen_at` restent obligatoires dans le manifeste.

## Restant transversal CBIBF

`DOCUMENT_MANIFEST_FULL_CBIBF = IN_PROGRESS` ; `SHA256_CBIBF = COMPLETE` ; `VERSION_SEMANTIC_REVIEW = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
