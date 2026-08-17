# SUIVI — financialdata

Dernière mise à jour : 2026-08-17

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V18 = 3 077 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v18_20260817.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V18 provient de PRSC : snapshot **68**, live strict parent-scoped **70**, delta **+2**, persisté avant SHA. V17 provenait de SLBC : 65 → 70 (+5). V16 provenait de CIEC : 61 → 62 (+1). V15 provenait de BICC : 61 → 70 (+9). V14 provenait de BOAC : 60 → 74 (+14).

Deltas live déjà documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2, SIBC +3, BOAC +14, BICC +9, CIEC +1, SLBC +5, **PRSC +2**.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 077** ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 267 / 3 077 = 41,18 %** ;
- restant non hashé : **1 810 PDF** ;
- groupes exacts prouvés : **13**.

Corpus terminés notamment : TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB 59/59 ; BOAC 74/74 ; BOAN 60/60 ; AGLC 60/60 ; BICC 70/70 ; CIEC 62/62 ; SLBC 70/70 ; **PRSC 70/70**.

### Doublons exacts

Les **13 groupes exacts** restent conservés. PRSC n'ajoute aucun groupe exact : **70 SHA uniques sur 70 objets**.

Le groupe n°13 reste CIEC états financiers 2016 plain / `_2` — taille **36 570 octets**, SHA `87c568d69a67b3fe08befd474a348ab1e15d5c1ccadc035d2f751eda6cd4d0b8`.

Tous les objets physiques restent conservés. Registre global : `inventory/p1_duplicate_groups.csv`.

### Résultats BICC — V15 / 2026-08-17

- snapshot 61 → live strict **70**, delta **+9** ;
- **70/70** PDF valides ; **69 SHA uniques** ;
- 1 groupe exact : T3 2022 plain / `_2`, SHA `492df4551aa01c2e97415323331b50a3f4eed65e952d38e2e97b7a524b64fae0` ;
- registre `inventory/hashes/BICC.csv`, blob post-commit validé `25baddade1e9e0366f3bdabfa6cdb2f13a5993ae` ;
- EF 2019 plain / `_rev` : `VERSION_OF`, pas `EXACT_DUPLICATE`, pas de `SUPERSEDES` explicite.

### Résultats CIEC — V16 / 2026-08-17

- arborescence : **29 dossiers directs = 1998–2025 + divers** ;
- snapshot 61 → live strict **62**, delta **+1** ;
- checkpoint V16 créé avant hash ; SOURCE global **3 070** ;
- **62/62** matérialisés, **62/62** signatures `%PDF-` valides ;
- **61 SHA uniques** ; **1 groupe exact** : EF 2016 plain / `_2` ;
- registre `inventory/hashes/CIEC.csv` ;
- validation post-commit bit-for-bit : blob local = GitHub `be1e68b95394d3c921adf506af3f0736b8d0c753` ;
- EF 2017 plain / `_rev` : même publication économique sous représentation physique différente, `VERSION_OF`, pas doublon exact ni `SUPERSEDES` automatique.

### Résultats SLBC — V17 / 2026-08-17

- arborescence : **28 dossiers directs = 1998–2025** ;
- snapshot 65 → live strict **70**, delta **+5** ;
- checkpoint V17 créé avant hash ; SOURCE global **3 075** ;
- **70/70** matérialisés et validés ; **70 SHA uniques** ; **0 groupe exact** ;
- registre `inventory/hashes/SLBC.csv`, blob GitHub validé `6b54e3cfc5f6616e274846ec041b1b758b491251` ;
- S1 2020 : deux binaires distincts mais rendu identique, `VERSION_OF`, pas `EXACT_DUPLICATE` ni `SUPERSEDES` sans preuve ;
- erratum AGO 2025 conservé dans SOURCE.

### Résultats PRSC — V18 / 2026-08-17

- dossier Drive canonique : `1uA4PVTKVuFPpR8uaQ87ORw3mzAIZ3f_h` ;
- arborescence live : **25 dossiers directs**, `1998–2007` puis `2011–2025` ;
- les dossiers 2008–2010 décrits dans l'inventaire initial ne sont pas visibles dans l'arborescence live actuelle ; la trace historique est conservée ;
- snapshot 68 → live strict parent-scoped **70**, delta **+2** ;
- checkpoint V18 créé avant hash ; SOURCE global **3 077** ;
- **70/70** matérialisés, signatures `%PDF-` et tailles validées ;
- **70 SHA uniques** ; **0 groupe exact** ;
- registre `inventory/hashes/PRSC.csv` ;
- validation post-commit exacte : blob local attendu = GitHub `78c6332bf1849eae6dff57f37e910d5ce2863348` ;
- deux noms génériques sont inclus par parent-scoped : `rapport_d27activite_1er_sem_2017_tmci.pdf` et `tractafric_motors_ci_-_rapport_dactivites_t1_2023.pdf` ;
- EF 2023 plain / `_rev` : même exercice clos 31/12/2023 sous formes détaillée/synthèse, `VERSION_OF`, pas `EXACT_DUPLICATE` et pas `SUPERSEDES` sans preuve explicite ;
- S1 2023 : trois objets distincts en binaire et en première page rendue, aucune fusion automatique ;
- EF 2024 : `_3` est semestriel au 30/06/2024 alors que plain/`_2` sont annuels au 31/12/2024 ;
- EF 2025 plain/`_2` : deux scans distincts, aucune fusion automatique.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **SAFC** — snapshot manifeste **73 PDF** ;
2. recheck strict du Drive canonique par parents réels + MIME ;
3. si delta : créer V19 et mettre à jour le dénominateur avant tout SHA ;
4. matérialiser/hash 100 %, revue collisions et versions ;
5. mettre à jour inventaire, registre SHA, manifeste, doublons, SUIVI/TODO et checkpoint si nécessaire ;
6. poursuivre ensuite **PALC (75 snapshot)**, **BNBC (78)** puis les autres corpus réellement non hashés par taille croissante ;
7. continuer en parallèle le backfill du manifeste documentaire et P1-R, sans démarrer P3 exhaustif prématurément.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3077 | MASTER_CONSOLIDATED=14/3077 | SHA256_VERIFIED=1267/3077 | SHA_COVERAGE=41.18% | UNHASHED=1810 | EXACT_DUPLICATE_GROUPS=13 | SLBC=70/70_SHA_COMPLETE | PRSC=70/70_SHA_COMPLETE | NEXT=SAFC_LIVE_RECHECK_AND_SHA`
