# SUIVI — financialdata

Dernière mise à jour : 2026-08-12

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- état live courant V13 : **3 046 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v13_20260811.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

Deltas live documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2, SIBC +3. BIIC, BOAS, BOAM, SCRC, SIVC, SEMC et BOABF ont été revérifiés sans nouveau delta à leur passe courante.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 046** ;
- les corpus déjà hashés disposent de Drive IDs + tailles + SHA dans leurs registres `inventory/hashes/*.csv` ; backfill des métadonnées temporelles/shards encore requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **742 / 3 046** (**24,36 %**) ;
- restant non hashé sur l'état V13 : **2 304 PDF** ;
- TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF **57/57**.

### Doublons exacts

Groupes exacts prouvés : **10**.

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

SIVC ajoute 0 groupe exact (53/53 SHA uniques), SEMC ajoute 0 groupe exact (54/54 SHA uniques). BOABF contient **56 SHA uniques sur 57 sources** et un seul groupe exact.

Tous les objets physiques restent conservés dans SOURCE ; registre global `inventory/p1_duplicate_groups.csv`.

### Résultats récents BOABF

- live strict : **57 PDF**, identique au snapshot précédent ; delta **0** ; total V13 reste **3 046 PDF** ;
- 18 dossiers directs contrôlés individuellement ; **2015, 2017 et 2018 restent vides** ;
- 57/57 tailles Drive ↔ fichiers validées ; **56 SHA uniques**, un groupe exact ; registre `inventory/hashes/BOABF.csv` ;
- la paire `divers_Etats_Financiers_BOABF.pdf` / `_2` est exactement identique : 814 269 octets et SHA `cda4d28d932b4b1c715a83170279d312000cfce9e4f1b487597d3db1b3821979` ;
- rendu visuel de la première page : `Exercice clos le 31 décembre 2017` et `Etats financiers au 31 décembre 2017` ; période résolue **FY 2017** ;
- aucun autre doublon exact parmi les 57 sources ; les variantes historiques restent distinctes jusqu'à revue sémantique.

### Contrôle de qualité du registre BOABF

Lors de la première persistance du CSV BOABF, une discordance de transcription entre les SHA calculés localement et le contenu transmis à GitHub a été détectée avant propagation en aval. Le registre a été immédiatement corrigé depuis les hashes locaux vérifiés, puis contrôlé sur ses premières et dernières lignes. Le manifeste et les totaux n'ont été mis à jour qu'après correction.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **BOAB** (59 PDF dans le manifeste V13), plus petit corpus non hashé suivant ;
2. revérifier le live par dossiers parents + MIME avant hash ;
3. versionner tout delta avant calcul SHA ;
4. matérialiser/hash 100 % + validation taille Drive ↔ fichier + revue des collisions/versions ;
5. poursuivre ensuite les corpus non hashés par taille croissante ;
6. poursuivre en parallèle le backfill du manifeste documentaire et P1-R sans démarrer P3 exhaustif prématurément.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3046 | MASTER_CONSOLIDATED=14/3046 | SHA256_VERIFIED=742/3046 | SHA_COVERAGE=24.36% | EXACT_DUPLICATE_GROUPS=10 | BOABF=57/57_SHA_COMPLETE | NEXT=BOAB_LIVE_RECHECK_AND_SHA`
