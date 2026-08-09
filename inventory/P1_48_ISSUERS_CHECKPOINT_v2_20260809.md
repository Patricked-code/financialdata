# P1 — CHECKPOINT 48 ÉMETTEURS — V2 LIVE REFRESH

Date : 2026-08-09
Statut : `INVENTORY_COMPLETE_48_OF_48 / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE`

## Pourquoi une V2

Le checkpoint initial a compté **2 950 PDF**. Pendant la même session, une nouvelle lecture directe du dossier CBIBF a montré que le corpus Drive avait évolué.

CBIBF est passé de **8 à 15 PDF**, soit **+7 fichiers** réellement présents avec des `created_time` Drive vers 06:36–06:37Z.

L'ancien checkpoint n'est pas supprimé ni réécrit silencieusement : il reste un snapshot historique. Cette V2 devient l'état live courant.

## État live courant

- sociétés : **48 / 48** ;
- PDF SOURCE : **2 957** ;
- delta depuis snapshot initial : **+7** ;
- cause observée : nouveaux fichiers CBIBF apparus dans Drive pendant la session.

## CBIBF live

- 2022 : 3 PDF ;
- 2023 : 4 PDF ;
- 2024 : 5 PDF ;
- 2025 : 3 PDF ;
- total : **15**.

## Doublon exact déjà prouvé dans le delta

`2024_Rapport_S1_CBIBF.pdf`
Drive : `1vBV6P-Of3cz9ixJOLqnVUbTc0hzFpI4E`

`2024_Rapport_S1_CBIBF_2.pdf`
Drive : `1Lxz7zOe-02J79x3Z0UBe-e7Ed0udTOlB`

- taille des deux : **1 549 372 octets** ;
- SHA-256 des deux : `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05` ;
- verdict : `EXACT_DUPLICATE`.

Les deux fichiers restent conservés comme sources distinctes avec un même `binary_duplicate_group_id`.

## Conséquence opérationnelle

Le manifeste SOURCE doit être un registre vivant et historisé :

- `first_seen_at` / `last_seen_at` sont indispensables ;
- un total global doit toujours être rattaché à un snapshot ;
- P1-FRESH doit comparer l'état distant à l'état enregistré, même pendant une longue passe d'inventaire ;
- aucune mutation du corpus ne doit réécrire silencieusement l'histoire.

## Prochain état

`LIVE_TOTAL = 2957 → DOCUMENT_MANIFEST_EXPANSION → SHA256 → DUPLICATE_GROUPS → VERSION_RELATIONS → PERIODS → ASSIGNMENT → FRESHNESS`
