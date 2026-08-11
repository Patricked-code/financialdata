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

- CBIBF : **8 → 15 PDF** (`+7`) ;
- ORAC : **14 → 21 PDF** (`+7`) ;
- SICC : **19 → 36 PDF** (`+17`) ;
- MVSC : **20 → 35 PDF** (`+15`) ;
- UNLC : **20 → 23 PDF** (`+3`) ;
- ORGT : **23 → 35 PDF** (`+12`) ;
- SHEC : **37 → 39 PDF** (`+2`) ;
- STAC : **38 → 53 PDF** (`+15`) ;
- NSBC : **38 → 41 PDF** (`+3`) ;
- ECOC : **32 → 42 PDF** (`+10`).

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
Stratégie incrémentale : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 3 041** ;
- shards compatibles complets existants : CBIBF 15/15, ORAC 21/21 ;
- SICC 36/36, MVSC 35/35, UNLC 23/23, ORGT 35/35, SHEC 39/39, STAC 53/53, NSBC 41/41 et ECOC 42/42 disposent de Drive IDs + tailles + SHA ; backfill métadonnées temporelles encore requis avant consolidation canonique complète ;
- ECOC : **42 sources live**, SHA 42/42 et revue des variantes explicites terminés.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **348 / 3 041** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **15 / 15** ;
- ORAC : **21 / 21** ;
- SICC : **36 / 36** ;
- MVSC : **35 / 35** ;
- UNLC : **23 / 23** ;
- ORGT : **35 / 35** ;
- SHEC : **39 / 39** ;
- STAC : **53 / 53** ;
- NSBC : **41 / 41** — 41 tailles Drive ↔ locales validées, 41 SHA uniques, zéro doublon exact ; registre `inventory/hashes/NSBC.csv` ;
- ECOC : **42 / 42** — 42 tailles Drive ↔ locales validées, 41 SHA uniques, 1 groupe de doublon exact ; registre `inventory/hashes/ECOC.csv`.

### Doublons exacts

Groupes exacts actuellement prouvés : **4**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 états financiers `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 états financiers plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.
4. ECOC 2021 états financiers plain / `_2` — SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.

Tous les objets physiques restent conservés dans SOURCE. Les groupes sont enregistrés dans `inventory/p1_duplicate_groups.csv`.

### Résultats récents

- STAC : **53 fichiers / 53 contenus uniques**, aucune duplication binaire ;
- NSBC : **41 fichiers / 41 contenus uniques**, aucune duplication binaire ;
- NSBC T1 2019 `_rev` : correction/supersession validée par mention « Version corrigée » et correction explicite des comparatifs 2018 ;
- NSBC EF 2021 `_rev` : supersession validée par mention « annule et remplace la parution du 04 avril 2022 » ; résultat net 2021 20 998 → 23 713 M FCFA ;
- NSBC EF 2019 plain / `_2` : hashes différents ; relation sémantique encore `VISUAL_REVIEW_REQUIRED` ;
- ECOC : live **42 PDF**, contre 32 auparavant ; 2017 contient bien un PDF T3, invalidant l'ancien constat d'absence ;
- ECOC 2021 EF plain / `_2` : **doublon binaire exact**, SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a` ;
- ECOC T1 2023 plain → `_rev` : `CORRECTED_VERSION_OF / SUPERSEDES` validé visuellement ; commentaire PNB 16,9 → 25,8 Md FCFA et hausse des dépôts 26,5 % → 14,9 % ;
- ECOC T3 2024 plain / `_rev` : hashes distincts, texte matériellement identique, différences de composition seulement ; `NO_SEMANTIC_SUPERSESSION_PROVEN` ;
- ECOC annuel 2024 plain → `_rev` : `CORRECTED_VERSION_OF / SUPERSEDES` ; comparaison de rendu des 10 pages, seule la page 9 diffère avec correction **(55 320) → (52 320)** ;
- rapport de preuve : `inventory/reviews/ECOC_VERSION_REVIEW_20260811.md`.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. vérifier en live le plus petit corpus restant sans registre SHA complet, en commençant par BIIC dont le snapshot historique ne compte que 2 PDF ;
2. si le total BIIC live est confirmé ou corrigé, versionner immédiatement le nouveau snapshot avant hash ;
3. matérialiser et hasher 100 % du corpus BIIC avec contrôle taille Drive ↔ fichier ;
4. poursuivre ensuite les autres corpus non hashés par taille croissante, avec revérification live préalable ;
5. backfiller progressivement les shards document-level ;
6. ne pas lancer P2 tant que la couverture P1/P1-R n'est pas jugée suffisante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3041 | MASTER_CONSOLIDATED=14/3041 | SHA256_VERIFIED=348/3041 | EXACT_DUPLICATE_GROUPS=4 | ECOC=42/42_SHA_COMPLETE | ECOC_EXPLICIT_VERSION_REVIEW=COMPLETE | NEXT=BIIC_LIVE_RECHECK_AND_SHA`
