# SUIVI — financialdata

Dernière mise à jour : 2026-08-11

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- état live courant V11 : **3 041 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v11_20260810.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

Deltas live documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10. BIIC, BOAS, BOAM et SCRC ont été revérifiés sans nouveau delta.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 041** ;
- les corpus déjà hashés disposent de Drive IDs + tailles + SHA ; backfill des métadonnées temporelles/shards encore requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **482 / 3 041** ;
- TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC **45/45**.

### Doublons exacts

Groupes exacts prouvés : **6**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 EF `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 EF plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.
4. ECOC 2021 EF plain / `_2` — SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.
5. BOAM 2023 EF / rapport CAC annuel — SHA `77f20998d8b1def30299a400bbe4584093fb54a6e40d05f7ab5fa7721896e31e`.
6. BOAM 2024 rapports CAC annuels plain / `_2` — SHA `dc403fad3b516f6a94eecefafb56db518987c5fb3097edd0d68a7ffe8077f207`.

Tous les objets physiques restent conservés dans SOURCE ; registre `inventory/p1_duplicate_groups.csv`.

### Résultats récents SCRC

- live : **45 PDF**, aucun delta ;
- 45/45 tailles Drive ↔ fichiers validées ; **45 SHA uniques**, zéro doublon exact ; registre `inventory/hashes/SCRC.csv` ;
- variantes EF 2017 `plain/_2/_3`, 2018 `plain/_2`, 2020 `plain/_2`, 2021 `plain/_2`, 2022 `plain/_2/_3`, 2023 `plain/_2` : toutes binaires distinctes ;
- `divers_Attestation_CAC_Annuel_SCRC.pdf` : le nom est trompeur ; revue visuelle prouve une attestation CAC **semestrielle au 30 juin 2017**, couvrant le 1er janvier–30 juin 2017 et datée du 20 octobre 2017 ; période résolue `S1_2017` ;
- aucun nouveau champ conceptuel nécessaire : campagne/site/production agro sont déjà prévus.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **TTLS** (snapshot historique 45 PDF), prochain corpus non hashé de même taille ;
2. revérifier le live par dossiers parents + MIME avant hash ;
3. versionner tout delta avant calcul SHA ;
4. matérialiser/hash 100 % + validation taille Drive ↔ fichier + revue des collisions/versions ;
5. poursuivre ensuite les corpus non hashés par taille croissante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3041 | MASTER_CONSOLIDATED=14/3041 | SHA256_VERIFIED=482/3041 | EXACT_DUPLICATE_GROUPS=6 | SCRC=45/45_SHA_COMPLETE | NEXT=TTLS_LIVE_RECHECK_AND_SHA`
