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
- V7 après ORGT : **3 011 PDF** ;
- V8 après SHEC : **3 013 PDF** ;
- état live courant V9 après STAC : **3 028 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v9_20260809.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Deltas live observés

- CBIBF : **8 → 15 PDF** (`+7`) ;
- ORAC : **14 → 21 PDF** (`+7`) ;
- SICC : **19 → 36 PDF** (`+17`) ;
- MVSC : **20 → 35 PDF** (`+15`) ;
- UNLC : **20 → 23 PDF** (`+3`) ;
- ORGT : **23 → 35 PDF** (`+12`) ;
- SHEC : **37 → 39 PDF** (`+2`) ;
- STAC : **38 → 53 PDF** (`+15`).

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
Stratégie incrémentale : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 3 028** ;
- shards compatibles complets existants : CBIBF 15/15, ORAC 21/21 ;
- SICC 36/36, MVSC 35/35, UNLC 23/23, ORGT 35/35, SHEC 39/39 et STAC 53/53 sont indexés par Drive ID + taille + SHA mais nécessitent encore le backfill complet des métadonnées de shard avant consolidation canonique.

## P1_TRANSVERSE — SHA256

- SHA calculés : **265 / 3 028** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **15 / 15** ;
- ORAC : **21 / 21** ;
- SICC : **36 / 36** ;
- MVSC : **35 / 35** ;
- UNLC : **23 / 23** ;
- ORGT : **35 / 35** ;
- SHEC : **39 / 39** ;
- STAC : **53 / 53**.

### Doublons exacts

Groupes exacts actuellement trouvés : **3**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 états financiers `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 états financiers plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.

Tous les objets physiques restent conservés dans SOURCE. Les groupes sont enregistrés dans `inventory/p1_duplicate_groups.csv`.

### Résultats récents

- SHEC : 39 fichiers / 37 contenus uniques, deux groupes exacts ;
- STAC : **53 fichiers / 53 contenus uniques**, aucune duplication binaire ;
- STAC 2012 plain / `_2` / `_3` / `_4` : quatre SHA distincts ;
- STAC 2013 plain / `_2` / `_3` : trois SHA distincts ;
- STAC 2014 plain / `_2` / `_3` : trois SHA distincts ;
- STAC 2019 états financiers plain / `_rev` : deux SHA distincts.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. poursuivre sur `NSBC` avec revérification live préalable ;
2. calculer son SHA complet et rechercher les doublons exacts ;
3. poursuivre les autres corpus courts non hashés ;
4. backfiller progressivement les shards SICC/MVSC/UNLC/ORGT/SHEC/STAC ;
5. ne pas lancer P2 tant que la couverture P1/P1-R n'est pas jugée suffisante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3028 | MASTER_CONSOLIDATED=14/3028 | SHA256=265/3028 | EXACT_DUPLICATE_GROUPS=3 | STAC=53/53 | NEXT=NSBC_LIVE_RECHECK`
