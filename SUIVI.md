# SUIVI — financialdata

Dernière mise à jour : 2026-08-17

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V15 = 3 069 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v15_20260817.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V15 provient de BICC : snapshot **61**, live strict **70**, delta **+9**, persisté avant SHA. V14 provenait de BOAC : 60 → 74, delta +14.

Deltas live déjà documentés : CBIBF +7, ORAC +7, SICC +17, MVSC +15, UNLC +3, ORGT +12, SHEC +2, STAC +15, NSBC +3, ECOC +10, TTLS +2, SIBC +3, BOAC +14, **BICC +9**.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 069** ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 065 / 3 069 = 34,70 %** ;
- restant non hashé : **2 004 PDF** ;
- groupes exacts prouvés : **12**.

Corpus terminés notamment : TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB 59/59 ; BOAC 74/74 ; BOAN 60/60 ; AGLC 60/60 ; **BICC 70/70**.

### Doublons exacts

Les 11 groupes précédents restent inchangés et BICC ajoute le groupe n°12 :

12. BICC T3 2022 plain / `_2` — taille **123 093 octets**, SHA `492df4551aa01c2e97415323331b50a3f4eed65e952d38e2e97b7a524b64fae0`.

Tous les objets physiques restent conservés. Registre global : `inventory/p1_duplicate_groups.csv`.

### Résultats AGLC — 2026-08-17

- live 60, delta 0 ; 60/60 hashés ; 60 SHA uniques ; 0 groupe exact ;
- registre `inventory/hashes/AGLC.csv`, blob post-commit validé `4c25045ffeb194aad7929b3b106a6fe6b7c7241c` ;
- IFRS 2020 individuel/consolidé conservés comme scopes distincts ;
- T1 2025 plain / `_rev` = versions distinctes ; pas de `SUPERSEDES` sans preuve explicite.

### Résultats BICC — V15 / 2026-08-17

- arborescence : 28 dossiers annuels `1998–2025` ;
- snapshot 61 → live strict **70**, delta **+9** ;
- checkpoint V15 créé avant hash ; SOURCE global **3 069** ;
- **70/70** matérialisés et signatures PDF valides ;
- **69 SHA uniques** ; **1 groupe exact** : T3 2022 plain / `_2` ;
- registre `inventory/hashes/BICC.csv` ;
- validation post-commit bit-for-bit : blob local = GitHub `25baddade1e9e0366f3bdabfa6cdb2f13a5993ae` ;
- EF 2019 plain / `_rev` : mêmes valeurs économiques principales, `_rev` enrichit/corrige la présentation et ajoute un commentaire sur provisions cacao/anacarde et dysfonctionnements SI ; relation `VERSION_OF`, pas `EXACT_DUPLICATE`, pas de `SUPERSEDES` explicite ;
- T2 2022 et S1 2022 restent des périodes distinctes ;
- `bilan_et_compte_de_resultat_bicici_31_12_2022_.pdf` reste un profil P1-R utile.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **CIEC** — snapshot actuel **61 PDF** ;
2. recheck strict par dossiers parents + MIME ;
3. versionner tout delta avant SHA ;
4. matérialiser/hash 100 %, collisions et versions ;
5. mettre à jour inventaire, registre SHA, manifeste, doublons, SUIVI/TODO et checkpoint si nécessaire ;
6. poursuivre ensuite les corpus non hashés par taille croissante ;
7. continuer en parallèle manifeste documentaire + P1-R, sans démarrer P3 exhaustif prématurément.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3069 | MASTER_CONSOLIDATED=14/3069 | SHA256_VERIFIED=1065/3069 | SHA_COVERAGE=34.70% | EXACT_DUPLICATE_GROUPS=12 | BICC=70/70_SHA_COMPLETE | NEXT=CIEC_LIVE_RECHECK_AND_SHA`
