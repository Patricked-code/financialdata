# SUIVI — financialdata

Dernière mise à jour : 2026-08-17

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- état live courant V14 : **3 060 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v14_20260817.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

Le passage V13 → V14 provient de BOAC : snapshot précédent **60**, live revérifié **74**, delta **+14** persisté avant calcul SHA.

Deltas live déjà documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2, SIBC +3, BOAC +14. BIIC, BOAS, BOAM, SCRC, SIVC, SEMC, BOABF, BOAB, BOAN et AGLC ont été revérifiés sans nouveau delta lors de leur passe courante.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 060** ;
- les corpus déjà hashés disposent de Drive IDs + tailles + SHA dans leurs registres `inventory/hashes/*.csv` ;
- backfill des métadonnées temporelles/shards encore requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **995 / 3 060** (**32,52 %**) ;
- restant non hashé sur l'état V14 : **2 065 PDF** ;
- TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB **59/59** ; BOAC **74/74** ; BOAN **60/60** ; AGLC **60/60**.

### Doublons exacts

Groupes exacts prouvés : **11**.

1. CBIBF 2024 S1 plain / `_2` — SHA `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.
2. SHEC 2022 EF `_2` / `_3` — SHA `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.
3. SHEC 2025 EF plain / `_2` — SHA `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.
4. ECOC 2021 EF plain / `_2` — SHA `ca091608d953102461797fb13924c9bfb14357505a149bc20f924e41cde2ce7a`.
5. BOAM 2023 EF / rapport CAC annuel — SHA `77f20998d8b1def30299a400bbe4584093fb54a6e40d05f7ab5fa7721896e31e`.
6. BOAM 2024 rapports CAC annuels plain / `_2` — SHA `dc403fad3b516f6a94eecefafb56db518987c5fb3097edd0d68a7ffe8077f207`.
7. TTLS 2018 rapports annuels plain / `_2` — SHA `46b4ee85f5ad173c2de754c1054b0118b18e3a9758acec3db59cc56358275237`.
8. SIBC 2017 T1 plain / `_2` / `_3` — SHA `3446b816e1a15b4a8d2df8bfeff775dbaa7166b52823c0d8d2bf8f1b06fc6b23`.
9. SIBC 2022 S1 plain / `_2` — SHA `b96ab01184f501d6f726250132108e742d8b5ede7ca862ce088b5aa29d7c88ec`.
10. BOABF `divers` états financiers FY2017 plain / `_2` — SHA `cda4d28d932b4b1c715a83170279d312000cfce9e4f1b487597d3db1b3821979`.
11. BOAC 2021 S1 plain / `_2` — SHA `7e69b8618e901a4bb72442989a23913f47f268b9093c0a380461d5626ede0c97`.

Tous les objets physiques restent conservés dans SOURCE ; registre global `inventory/p1_duplicate_groups.csv`.

### Résultats BOAB — 2026-08-17

- live strict : **59 PDF**, delta **0** ;
- 59/59 fichiers matérialisés et signature PDF validée ;
- **59 SHA uniques**, **0 groupe exact** ;
- registre `inventory/hashes/BOAB.csv` ;
- anomalie d'attribution confirmée : `avis_ndeg232...tpci_590_2021-2031...pdf` concerne le Trésor Public de Côte d'Ivoire / TPCI 5,90 % 2021-2031, pas BOAB ; la source physique reste conservée avec attribution à revoir.

### Résultats BOAC — live V14 / 2026-08-17

- snapshot V13 : **60 PDF** ; live Drive revérifié : **74 PDF** ; delta **+14** ;
- 74/74 fichiers matérialisés ; 74/74 PDF valides ; **73 SHA uniques** ;
- registre `inventory/hashes/BOAC.csv` ;
- un groupe exact : `2021_Rapport_S1_BOAC.pdf` / `_2` ;
- `2019_Etats_Financiers_BOAC.pdf` / `_2` : même taille mais SHA distincts ;
- `divers_Rapport_S1_BOAC.pdf` : contenu confirmé S1 2022 ;
- `fiche_ci_0.pdf` : information boursière S1 2017.

### Résultats BOAN — 2026-08-17

- live strict : **60 PDF**, snapshot **60**, delta **0** ;
- 28 dossiers parents `1999–2025 + divers` contrôlés ;
- 60/60 tailles Drive ↔ local conformes ; 60/60 signatures PDF valides ;
- **60 SHA uniques**, **0 groupe exact** ;
- registre canonique : `inventory/hashes/BOAN.csv` ;
- une erreur de transcription du premier registre a été détectée par revalidation post-écriture puis corrigée avant clôture ;
- `fiche_ne_0.pdf` : contenu confirmé information boursière **S1 2017**.

### Résultats AGLC — 2026-08-17

- live strict : **60 PDF**, snapshot **60**, delta **0** ;
- 28 dossiers annuels `1998–2025` contrôlés ;
- 60/60 matérialisés ; 60/60 tailles conformes ; 60/60 signatures PDF valides ;
- **60 SHA uniques**, **0 groupe exact** ;
- registre : `inventory/hashes/AGLC.csv` ;
- validation post-commit bit-for-bit : Git blob local = GitHub `4c25045ffeb194aad7929b3b106a6fe6b7c7241c` ;
- 2020 : comptes IFRS individuels et consolidés conservés comme scopes distincts ;
- T1 2025 plain / `_rev` : binaires distincts et versions de la même publication ; `_rev` corrige notamment la valeur comparative annuelle du résultat net 2024 de **17 138 527** à **21 068 974 KFCFA** ;
- aucune formule explicite `annule et remplace` observée : ne pas renseigner automatiquement `supersedes_source_file_id`.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **BICC** — snapshot actuel **61 PDF** ;
2. revérifier strictement ses dossiers parents et compter les PDF live ;
3. si delta : versionner le nouveau dénominateur avant tout SHA et mettre à jour le total global ;
4. matérialiser/hash 100 % + validation taille Drive ↔ fichier + revue collisions/versions ;
5. mettre à jour `inventory/BICC.md`, `inventory/hashes/BICC.csv`, `p1_issuer_manifest.csv`, `p1_duplicate_groups.csv`, `SUIVI.md`, `TODO.md` et checkpoint si nécessaire ;
6. poursuivre ensuite **CIEC (61)** puis les autres corpus non hashés par taille croissante ;
7. poursuivre en parallèle le backfill du manifeste documentaire et P1-R sans démarrer P3 exhaustif prématurément.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3060 | MASTER_CONSOLIDATED=14/3060 | SHA256_VERIFIED=995/3060 | SHA_COVERAGE=32.52% | EXACT_DUPLICATE_GROUPS=11 | BOAN=60/60_SHA_COMPLETE | AGLC=60/60_SHA_COMPLETE | NEXT=BICC_LIVE_RECHECK_AND_SHA`
