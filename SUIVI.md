# SUIVI — financialdata

Dernière mise à jour : 2026-08-11

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- état live courant V12 : **3 043 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v12_20260811.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

Deltas live documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2. BIIC, BOAS, BOAM et SCRC ont été revérifiés sans nouveau delta.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 043** ;
- les corpus déjà hashés disposent de Drive IDs + tailles + SHA ; backfill des métadonnées temporelles/shards encore requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **529 / 3 043** ;
- TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS **47/47**.

### Doublons exacts

Groupes exacts prouvés : **7**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 EF `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 EF plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.
4. ECOC 2021 EF plain / `_2` — SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.
5. BOAM 2023 EF / rapport CAC annuel — SHA `77f20998d8b1def30299a400bbe4584093fb54a6e40d05f7ab5fa7721896e31e`.
6. BOAM 2024 rapports CAC annuels plain / `_2` — SHA `dc403fad3b516f6a94eecefafb56db518987c5fb3097edd0d68a7ffe8077f207`.
7. TTLS 2018 rapports annuels plain / `_2` — SHA `46b4ee85f5ad173c2de754c1054b0118b18e3a9758acec3db59cc56358275237`.

Tous les objets physiques restent conservés dans SOURCE ; registre `inventory/p1_duplicate_groups.csv`.

### Résultats récents TTLS

- live : **47 PDF** contre 45 auparavant, delta **+2**, d'où V12 = **3 043 PDF** ;
- 47/47 tailles Drive ↔ fichiers validées ; **46 SHA uniques**, 1 groupe exact ; registre `inventory/hashes/TTLS.csv` ;
- deux rapports annuels 2018 strictement identiques : 3 058 310 octets, SHA `46b4ee85f5ad173c2de754c1054b0118b18e3a9758acec3db59cc56358275237` ;
- aucun autre doublon exact parmi les 47 sources ;
- `divers_Rapport_CAC_Annuel_TTLS.pdf` : 68 pages, couche texte native ; titre « Rapport général et rapports spéciaux des commissaires aux comptes » ; période publiée **exercice clos le 31 décembre 2020** ; période résolue `FY_2020` ;
- la règle contenu > nom/dossier est confirmée une nouvelle fois.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **SIBC** (snapshot précédent 46 PDF), plus petit corpus non hashé suivant ;
2. revérifier le live par dossiers parents + MIME avant hash ;
3. versionner tout delta avant calcul SHA ;
4. matérialiser/hash 100 % + validation taille Drive ↔ fichier + revue des collisions/versions ;
5. poursuivre ensuite les corpus non hashés par taille croissante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3043 | MASTER_CONSOLIDATED=14/3043 | SHA256_VERIFIED=529/3043 | EXACT_DUPLICATE_GROUPS=7 | TTLS=47/47_SHA_COMPLETE | NEXT=SIBC_LIVE_RECHECK_AND_SHA`
