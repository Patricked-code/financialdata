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
- V2 après CBIBF : **2 957 PDF** ;
- V3 après ORAC : **2 964 PDF** ;
- V4 après SICC : **2 981 PDF** ;
- V5 après MVSC : **2 996 PDF** ;
- V6 après UNLC : **2 999 PDF** ;
- état live courant V7 après ORGT : **3 011 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v7_20260809.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Deltas live observés

- CBIBF : **8 → 15 PDF** (`+7`) ;
- ORAC : **14 → 21 PDF** (`+7`) ;
- SICC : **19 → 36 PDF** (`+17`) ;
- MVSC : **20 → 35 PDF** (`+15`) ;
- UNLC : **20 → 23 PDF** (`+3`) ;
- ORGT : **23 → 35 PDF** (`+12`).

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
Stratégie incrémentale : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 3 011** ;
- shards compatibles complets existants : CBIBF 15/15, ORAC 21/21 ;
- SICC 36/36, MVSC 35/35, UNLC 23/23 et ORGT 35/35 sont indexés par Drive ID + taille + SHA mais nécessitent encore le backfill complet des métadonnées de shard avant consolidation canonique.

### Couvertures document-level déjà prouvées

- TRITRAF : **8 / 8** dans le maître ;
- BIIC : **2 / 2** dans le maître ;
- CBIBF : **15 / 15** dans `inventory/manifests/CBIBF.csv` ;
- ORAC : **21 / 21** dans `inventory/manifests/ORAC.csv` ;
- SICC : **36 / 36** IDs + parents + tailles + SHA ;
- MVSC : **35 / 35** IDs + parents + tailles + SHA ;
- UNLC : **23 / 23** IDs + parents + tailles + SHA ;
- ORGT : **35 / 35** IDs + parents + tailles + SHA ;
- SNTS/ONATEL : 1 anomalie seed ;
- BICC 2022 : 1 seed.

La consolidation finale refusera tout `source_drive_file_id` dupliqué entre maître et shards.

## P1_TRANSVERSE — SHA256

- SHA calculés : **173 / 3 011** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **15 / 15** ;
- ORAC : **21 / 21** ;
- SICC : **36 / 36** ;
- MVSC : **35 / 35** ;
- UNLC : **23 / 23** ;
- ORGT : **35 / 35**.

### Doublons exacts

Un seul groupe exact actuellement trouvé :

`2024_Rapport_S1_CBIBF.pdf` / `2024_Rapport_S1_CBIBF_2.pdf`

SHA commun :
`8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.

Groupe enregistré dans `inventory/p1_duplicate_groups.csv`.

### Résultats récents

- ORAC : 21 contenus uniques ; tailles du registre revalidées contre Drive ;
- SICC : 36 contenus uniques ; aucune variante `_2/_3` n'est un doublon binaire ;
- MVSC : 35 contenus uniques ; variantes historiques et deux états financiers 2019 distincts ;
- UNLC : 23 contenus uniques ; les deux rapports annuels 2020 sont distincts ;
- ORGT : 35 contenus uniques ; toutes les paires d'états financiers/CAC proches sont binaires distinctes.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. poursuivre sur le prochain corpus court avec **revérification live préalable** : SHEC ;
2. calculer son SHA complet et rechercher les doublons exacts ;
3. poursuivre ensuite les corpus courts non hashés ;
4. backfiller progressivement les shards SICC/MVSC/UNLC/ORGT ;
5. ne pas lancer P2 tant que la couverture P1/P1-R n'est pas jugée suffisante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3011 | MASTER_CONSOLIDATED=14/3011 | SHA256=173/3011 | EXACT_DUPLICATE_GROUPS=1 | SICC=36/36 | MVSC=35/35 | UNLC=23/23 | ORGT=35/35 | NEXT=SHEC_LIVE_RECHECK`
