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

V18 provient de PRSC : snapshot 68 → live strict parent-scoped 70 (+2). SAFC a ensuite été rechecké **73 → 73, delta 0** : aucun V19 artificiel n'a été créé.

Deltas live déjà documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2, SIBC +3, BOAC +14, BICC +9, CIEC +1, SLBC +5, PRSC +2.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 077** ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 340 / 3 077 = 43,55 %** ;
- restant non hashé : **1 737 PDF** ;
- groupes exacts prouvés : **14**.

Corpus terminés notamment : TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB 59/59 ; BOAC 74/74 ; BOAN 60/60 ; AGLC 60/60 ; BICC 70/70 ; CIEC 62/62 ; SLBC 70/70 ; PRSC 70/70 ; **SAFC 73/73**.

### Résultats SAFC — V18 / 2026-08-17

- dossier Drive canonique : `1UhiUIVuMBHzRSt6jikV22wJoytCZk2j_` ;
- **27 dossiers directs**, couverture `1998–2014`, puis `2016–2025`; 2015 absent ;
- snapshot **73** → live strict parent-scoped **73**, delta **0** ;
- **73/73** matérialisés et signatures `%PDF-` valides ;
- **72 SHA uniques** ;
- **1 groupe exact** : `2007_Rapport_Annuel_SAFC.pdf` / `2007_Rapport_Annuel_SAFC_3.pdf`, 1 475 293 octets, SHA `85f0a68ee4e126d93fcb09dafbf644e24b61454d428974787391c6f5cde8884c` ;
- les deux objets physiques sont conservés ;
- registre `inventory/hashes/SAFC.csv` ;
- blob GitHub final **`4d68e2f99a3d8a90fe70ecf858c7064924f27dd3`**, identique au blob calculé localement ;
- les noms génériques T4 2022 et T4 2024 ont été récupérés grâce au parent-scoped et restent dans SOURCE ;
- aucune relation `SUPERSEDES` n'est déduite des suffixes seuls.

### Doublons exacts

Les **14 groupes exacts** restent tous conservés dans `inventory/p1_duplicate_groups.csv`. Le groupe n°14 est le groupe SAFC 2007 ci-dessus.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **PALC** — snapshot manifeste **75 PDF** ;
2. recheck strict du Drive canonique par parents réels + MIME ;
3. si delta : créer la prochaine version SOURCE avant tout SHA ;
4. matérialiser/hash 100 %, revue collisions et versions ;
5. mettre à jour inventaire, registre SHA, manifeste, doublons, SUIVI/TODO ;
6. poursuivre ensuite **BNBC (78)** puis les autres corpus réellement non hashés par taille croissante ;
7. continuer le backfill du manifeste documentaire, P1-R et P1-FRESH avant extraction RAW exhaustive.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3077 | MASTER_CONSOLIDATED=14/3077 | SHA256_VERIFIED=1340/3077 | SHA_COVERAGE=43.55% | UNHASHED=1737 | EXACT_DUPLICATE_GROUPS=14 | PRSC=70/70_SHA_COMPLETE | SAFC=73/73_SHA_COMPLETE | NEXT=PALC_LIVE_RECHECK_AND_SHA`
