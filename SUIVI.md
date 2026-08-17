# SUIVI — financialdata

Dernière mise à jour : 2026-08-17

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V16 = 3 070 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v16_20260817.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V16 provient de CIEC : snapshot **61**, live strict **62**, delta **+1**, persisté avant SHA. V15 provenait de BICC : 61 → 70 (+9). V14 provenait de BOAC : 60 → 74 (+14).

Deltas live déjà documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2, SIBC +3, BOAC +14, BICC +9, **CIEC +1**.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 070** ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 127 / 3 070 = 36,71 %** ;
- restant non hashé : **1 943 PDF** ;
- groupes exacts prouvés : **13**.

Corpus terminés notamment : TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB 59/59 ; BOAC 74/74 ; BOAN 60/60 ; AGLC 60/60 ; BICC 70/70 ; **CIEC 62/62**.

### Doublons exacts

Les 12 groupes précédents restent conservés et CIEC ajoute le groupe n°13 :

13. CIEC états financiers 2016 plain / `_2` — taille **36 570 octets**, SHA `87c568d69a67b3fe08befd474a348ab1e15d5c1ccadc035d2f751eda6cd4d0b8`.

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
- EF 2017 plain : 205 461 octets, SHA `e4b995b117d56a7d92af90fdfe118b5c5a599b9e288783fb4223d4aa43a3532a` ;
- EF 2017 `_rev` : 603 584 octets, SHA `71c4b64cd909364599b59f875ad28713d445d155548a1757c46e3627c7c7e3d1` ;
- les deux 2017 sont une même publication économique sous représentation physique différente : `VERSION_OF`, pas doublon exact ;
- aucune formule explicite `annule et remplace` observée : pas de `supersedes_source_file_id` automatique ;
- le deep pilot CIEC existant est conservé et enrichi par cette preuve binaire, pas refait de zéro.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **SLBC** — snapshot manifeste **65 PDF** ;
2. recheck strict de son Drive canonique par parents réels + MIME ;
3. si delta : créer V17 et mettre à jour le dénominateur avant tout SHA ;
4. matérialiser/hash 100 %, revue collisions et versions ;
5. mettre à jour inventaire, registre SHA, manifeste, doublons, SUIVI/TODO et checkpoint si nécessaire ;
6. poursuivre ensuite **PRSC (68 snapshot)**, **SAFC (73)**, **PALC (75)**, puis les autres corpus réellement non hashés par taille croissante ;
7. continuer en parallèle le backfill du manifeste documentaire et P1-R, sans démarrer P3 exhaustif prématurément.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3070 | MASTER_CONSOLIDATED=14/3070 | SHA256_VERIFIED=1127/3070 | SHA_COVERAGE=36.71% | EXACT_DUPLICATE_GROUPS=13 | BICC=70/70_SHA_COMPLETE | CIEC=62/62_SHA_COMPLETE | NEXT=SLBC_LIVE_RECHECK_AND_SHA`
