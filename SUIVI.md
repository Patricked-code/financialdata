# SUIVI — financialdata

Dernière mise à jour : 2026-08-11

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
- V10 après NSBC : **3 031 PDF** ;
- état live courant V11 après ECOC : **3 041 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v11_20260810.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Deltas live observés

- CBIBF : **8 → 15 PDF** (`+7`) ; ORAC : **14 → 21** (`+7`) ; SICC : **19 → 36** (`+17`) ; MVSC : **20 → 35** (`+15`) ; UNLC : **20 → 23** (`+3`) ; ORGT : **23 → 35** (`+12`) ; SHEC : **37 → 39** (`+2`) ; STAC : **38 → 53** (`+15`) ; NSBC : **38 → 41** (`+3`) ; ECOC : **32 → 42** (`+10`).
- BIIC : snapshot **2 PDF**, revérification live 2026-08-11 **2 PDF**, donc aucun delta.

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`. Stratégie : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 3 041** ;
- CBIBF 15/15, ORAC 21/21, SICC 36/36, MVSC 35/35, UNLC 23/23, ORGT 35/35, SHEC 39/39, STAC 53/53, NSBC 41/41, ECOC 42/42 et BIIC 2/2 disposent désormais de Drive IDs + tailles + SHA ;
- backfill métadonnées temporelles encore requis avant consolidation canonique complète.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **350 / 3 041** ;
- TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC **2/2**.
- BIIC : T2 SHA `6dfb9d495eebaf39a2336aa6871498502c8d1a5f440b2a89d920f2dceeee6456`, T3 SHA `9f5e57270040e7fbcfa0a7d0b7367861e287b55d6b33b55a882cce78e176c10f` ; 2 contenus uniques ; registre `inventory/hashes/BIIC.csv`.

### Doublons exacts

Groupes exacts actuellement prouvés : **4**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 EF `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 EF plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.
4. ECOC 2021 EF plain / `_2` — SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.

Tous les objets physiques restent conservés dans SOURCE ; groupes dans `inventory/p1_duplicate_groups.csv`.

### Résultats récents

- ECOC : **42/42 SHA**, 41 contenus uniques, 1 groupe exact ; revue des variantes dans `inventory/reviews/ECOC_VERSION_REVIEW_20260811.md`.
- ECOC T1 2023 `_rev` : vraie correction/supersession ; commentaire PNB 16,9 → 25,8 Md FCFA et dépôts 26,5 % → 14,9 %.
- ECOC T3 2024 `_rev` : binaire distinct mais aucune supersession sémantique démontrée.
- ECOC annuel 2024 `_rev` : correction/supersession ; page 9 `(55 320) → (52 320)`.
- BIIC : live confirmé **2 PDF**, SHA **2/2**, aucun doublon exact ; le dossier 2024 ne contient toujours aucun PDF direct.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. passer au prochain corpus court non hashé : **BOAS** (snapshot historique 43 PDF) ;
2. revérifier d'abord le total live BOAS exclusivement par dossiers parents + MIME ;
3. versionner tout delta avant calcul SHA ;
4. matérialiser/hash 100 % du corpus avec validation taille Drive ↔ fichier ;
5. poursuivre ensuite les corpus non hashés par taille croissante ;
6. ne pas lancer P2 tant que la couverture P1/P1-R n'est pas jugée suffisante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3041 | MASTER_CONSOLIDATED=14/3041 | SHA256_VERIFIED=350/3041 | EXACT_DUPLICATE_GROUPS=4 | ECOC=42/42_SHA_COMPLETE | BIIC=2/2_SHA_COMPLETE | NEXT=BOAS_LIVE_RECHECK_AND_SHA`
