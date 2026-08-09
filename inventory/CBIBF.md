# P1 SOURCE — Coris Bank International / CBIBF

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

- Ticker : `CBIBF`
- Dossier Drive : `1ASGO_gpl4szCOXSLJawprG078nYrjUV8`
- Dossiers directs : **4** (`2022`, `2023`, `2024`, `2025`)
- Premier inventaire de session : **8 PDF**
- État Drive revérifié plus tard dans la même session : **15 PDF**
- Delta live : **+7 PDF**

## État live revérifié

- 2022 : **3 PDF** — annuel, états financiers, CAC annuel ;
- 2023 : **4 PDF** — T1, S1, T3, annuel ;
- 2024 : **5 PDF** — T1, S1, S1 `_2`, T3, annuel ;
- 2025 : **3 PDF** — T1, S1, T3.

Les 7 ajouts ont des `created_time` Drive autour de `2026-08-09T06:36–06:37Z`, alors que le premier inventaire avait été réalisé auparavant.

## Doublon binaire vérifié

Les deux fichiers :

- `2024_Rapport_S1_CBIBF.pdf` — Drive `1vBV6P-Of3cz9ixJOLqnVUbTc0hzFpI4E` ;
- `2024_Rapport_S1_CBIBF_2.pdf` — Drive `1Lxz7zOe-02J79x3Z0UBe-e7Ed0udTOlB` ;

ont :

- même taille : **1 549 372 octets** ;
- même SHA-256 : `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.

Verdict : **EXACT_DUPLICATE**. Les deux sources restent conservées ; elles devront partager un `binary_duplicate_group_id` dans le manifeste.

## Leçon opérationnelle

Le corpus SOURCE peut évoluer pendant une passe P1. Les snapshots historiques ne doivent pas être réécrits silencieusement : le premier état 8 PDF est conservé dans l'historique Git, et l'état live 15 PDF devient le nouvel état courant.

## Restant transversal

`DOCUMENT_MANIFEST_CBIBF = IN_PROGRESS` ; `SHA256_CBIBF = 2/15` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
