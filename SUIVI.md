# SUIVI — financialdata

Dernière mise à jour : 2026-08-10

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
- V9 après STAC : **3 028 PDF** ;
- état live courant V10 après NSBC : **3 031 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v10_20260810.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Deltas live observés

- CBIBF : **8 → 15 PDF** (`+7`) ;
- ORAC : **14 → 21 PDF** (`+7`) ;
- SICC : **19 → 36 PDF** (`+17`) ;
- MVSC : **20 → 35 PDF** (`+15`) ;
- UNLC : **20 → 23 PDF** (`+3`) ;
- ORGT : **23 → 35 PDF** (`+12`) ;
- SHEC : **37 → 39 PDF** (`+2`) ;
- STAC : **38 → 53 PDF** (`+15`) ;
- NSBC : **38 → 41 PDF** (`+3`).

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
Stratégie incrémentale : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 3 031** ;
- shards compatibles complets existants : CBIBF 15/15, ORAC 21/21 ;
- SICC 36/36, MVSC 35/35, UNLC 23/23, ORGT 35/35, SHEC 39/39 et STAC 53/53 sont indexés par Drive ID + taille + SHA mais nécessitent encore le backfill complet des métadonnées de shard avant consolidation canonique ;
- NSBC : **41 / 41 sources live identifiées et matérialisées**, Drive IDs/parents/tailles connus ; SHA encore non calculés à cause d'un blocage technique du runtime local.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **265 / 3 031** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **15 / 15** ;
- ORAC : **21 / 21** ;
- SICC : **36 / 36** ;
- MVSC : **35 / 35** ;
- UNLC : **23 / 23** ;
- ORGT : **35 / 35** ;
- SHEC : **39 / 39** ;
- STAC : **53 / 53** ;
- NSBC : **0 / 41 SHA calculés dans la passe actuelle** ; 41/41 fichiers matérialisés mais le runtime local a échoué avant exécution du calcul. Aucun hash n'est inventé.

### Doublons exacts

Groupes exacts actuellement prouvés : **3**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 états financiers `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 états financiers plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.

Tous les objets physiques restent conservés dans SOURCE. Les groupes sont enregistrés dans `inventory/p1_duplicate_groups.csv`.

### Résultats récents

- STAC : **53 fichiers / 53 contenus uniques**, aucune duplication binaire ;
- NSBC : live **41 fichiers**, tous matérialisés ;
- NSBC T1 2019 `_rev` : **correction/supersession sémantique validée** par mention « Version corrigée » et correction explicite des comparatifs 2018 ;
- NSBC EF 2021 `_rev` : **supersession sémantique validée** par mention « annule et remplace la parution du 04 avril 2022 » ; résultat net 2021 20 998 → 23 713 M FCFA ;
- NSBC EF 2019 plain / `_2` : tailles distinctes (1 325 452 vs 8 069 372 octets), donc pas un doublon binaire exact ; relation sémantique à contrôler visuellement car aucun texte natif n'est exposé ;
- ces deux cas de version NSBC ont été ajoutés au document canonique Drive de gouvernance le 2026-08-10.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. retenter le SHA-256 NSBC 41/41 dès qu'un runtime binaire exécutable est disponible ;
2. pendant ce blocage local, poursuivre sans arrêt les contrôles SOURCE réalisables via Drive : revérification live des prochains corpus courts non hashés, relations de version explicites et métadonnées documentaires ;
3. prochain corpus prioritaire : `ECOC` (ancien snapshot 32 PDF), à recompter strictement par dossiers parents + MIME avant toute conclusion ;
4. backfiller progressivement les shards SICC/MVSC/UNLC/ORGT/SHEC/STAC/NSBC ;
5. ne pas lancer P2 tant que la couverture P1/P1-R n'est pas jugée suffisante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3031 | MASTER_CONSOLIDATED=14/3031 | SHA256_VERIFIED=265/3031 | EXACT_DUPLICATE_GROUPS=3 | NSBC_LIVE=41/41_MATERIALIZED | NSBC_SHA=BLOCKED_RUNTIME_NOT_COMPUTED | NSBC_VERSION_LINKS=2_VALIDATED | NEXT=ECOC_LIVE_RECHECK`
