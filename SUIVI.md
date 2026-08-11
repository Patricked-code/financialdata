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
- V2 après CBIBF : **2 957 PDF** ; V3 ORAC : **2 964** ; V4 SICC : **2 981** ; V5 MVSC : **2 996** ; V6 UNLC : **2 999** ; V7 ORGT : **3 011** ; V8 SHEC : **3 013** ; V9 STAC : **3 028** ; V10 NSBC : **3 031** ; V11 ECOC : **3 041 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v11_20260810.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Deltas live observés

CBIBF `+7`, ORAC `+7`, SICC `+17`, MVSC `+15`, UNLC `+3`, ORGT `+12`, SHEC `+2`, STAC `+15`, NSBC `+3`, ECOC `+10`.

- BIIC : 2 → 2, aucun delta ;
- BOAS : 43 → 43, aucun delta.

Les snapshots antérieurs sont conservés dans Git. Aucun état SOURCE n'est réécrit silencieusement.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`. Stratégie : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées : **14 / 3 041** ;
- CBIBF 15/15, ORAC 21/21, SICC 36/36, MVSC 35/35, UNLC 23/23, ORGT 35/35, SHEC 39/39, STAC 53/53, NSBC 41/41, ECOC 42/42, BIIC 2/2 et BOAS 43/43 disposent de Drive IDs + tailles + SHA ;
- backfill métadonnées temporelles encore requis avant consolidation canonique complète.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **393 / 3 041** ;
- TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS **43/43**.
- BOAS : 43 tailles Drive ↔ fichiers validées, **43 SHA uniques, zéro doublon exact** ; registre `inventory/hashes/BOAS.csv`.

### Doublons exacts

Groupes exacts prouvés : **4**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 EF `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 EF plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.
4. ECOC 2021 EF plain / `_2` — SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.

Tous les objets physiques restent conservés dans SOURCE ; groupes dans `inventory/p1_duplicate_groups.csv`.

### Résultats récents

- ECOC : 42/42 SHA, 41 contenus uniques, 1 groupe exact ; revue `inventory/reviews/ECOC_VERSION_REVIEW_20260811.md`.
- BIIC : live 2 PDF, SHA 2/2, aucun doublon.
- BOAS : live **43 PDF**, SHA **43/43**, 43 contenus uniques, aucun doublon exact ; anciennes variantes `_2/_3` toutes binaires distinctes.
- BOAS `divers_Rapport_S1_BOAS.pdf` : période résolue visuellement comme **premier semestre 2019**, date visible **09/09/2019** ; preuve que le dossier `divers` ne dicte jamais la période.
- BOAS : dossier 2013 toujours sans PDF direct ; nouveautés BRVM 2026 restent `REMOTE_DELTA_IDENTIFIED` pour le collecteur V2.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. passer à **BOAM** (snapshot historique 44 PDF), plus petit corpus non hashé suivant ;
2. revérifier le total live exclusivement par dossiers parents + MIME ;
3. versionner tout delta avant hash ;
4. matérialiser et hasher 100 % du corpus avec validation taille Drive ↔ fichier ;
5. poursuivre ensuite les corpus non hashés par taille croissante ;
6. ne pas lancer P2 tant que la couverture P1/P1-R n'est pas jugée suffisante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3041 | MASTER_CONSOLIDATED=14/3041 | SHA256_VERIFIED=393/3041 | EXACT_DUPLICATE_GROUPS=4 | BOAS=43/43_SHA_COMPLETE | NEXT=BOAM_LIVE_RECHECK_AND_SHA`
