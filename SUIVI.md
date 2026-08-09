# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- snapshot initial : **2 950 PDF** — `inventory/P1_48_ISSUERS_CHECKPOINT.md` ;
- V2 après delta CBIBF : **2 957 PDF** ;
- V3 après delta ORAC : **2 964 PDF** ;
- état live courant V4 : **2 981 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v4_20260809.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Deltas live observés

- CBIBF : **8 → 15 PDF** (`+7`) ;
- ORAC : **14 → 21 PDF** (`+7`) ;
- SICC : **19 → 36 PDF** (`+17`).

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
Stratégie incrémentale : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 2 981** ;
- sources distinctes actuellement capturées dans le maître + shards compatibles : **48 / 2 981** ;
- sources supplémentaires déjà identifiées et hashées SICC mais dont le backfill complet du shard reste à terminer : **36**.

### Couvertures document-level

- TRITRAF : **8 / 8** dans le maître ;
- BIIC : **2 / 2** dans le maître ;
- CBIBF : **15 / 15** dans `inventory/manifests/CBIBF.csv` ;
- ORAC : **21 / 21** dans `inventory/manifests/ORAC.csv` ;
- SICC : **36 / 36 IDs + parents + tailles + SHA identifiés**, métadonnées temporelles du shard encore à backfiller ;
- SNTS/ONATEL : 1 anomalie seed ;
- BICC 2022 : 1 seed.

La consolidation finale refusera tout `source_drive_file_id` dupliqué entre maître et shards.

## P1_TRANSVERSE — SHA256

- SHA calculés : **80 / 2 981** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **15 / 15** ;
- ORAC : **21 / 21** ;
- SICC : **36 / 36**.

### Doublons exacts

Un seul groupe exact actuellement trouvé :

`2024_Rapport_S1_CBIBF.pdf` / `2024_Rapport_S1_CBIBF_2.pdf`

SHA commun :
`8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.

Groupe enregistré dans `inventory/p1_duplicate_groups.csv`.

### SICC

Les **36 SHA sont tous distincts**. Les variantes `_2` / `_3` de 2007–2016 ne sont donc pas des doublons binaires. Leur relation sémantique/version reste non revue.

### ORAC — contrôle qualité corrigé

Les 21 SHA ont été revalidés sur les fichiers Drive matérialisés. Les valeurs de hash correspondaient, mais plusieurs `file_size_bytes` du registre initial étaient erronées. `inventory/hashes/ORAC.csv` a été corrigé avec les tailles revalidées et le statut `COMPUTED_SIZE_REVALIDATED`.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. backfill des métadonnées temporelles du shard SICC ;
2. continuer sur le prochain corpus court en **revérifiant d'abord son état live** : `MVSC` ;
3. puis `UNLC` ;
4. poursuivre SHA / manifeste / périodes / versions sans lancer P2 prématurément.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=2981 | MASTER_CONSOLIDATED=14/2981 | MANIFEST_COMPATIBLE_CAPTURED=48/2981 | SICC_INDEXED_PENDING_SHARD_BACKFILL=36 | SHA256=80/2981 | EXACT_DUPLICATE_GROUPS=1 | NEXT=MVSC_LIVE_RECHECK`
