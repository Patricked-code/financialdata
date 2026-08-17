# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live V14 **3 060 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v14_20260817.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] SIBC revérifié : **49 PDF** au lieu de 46, delta `+3` persisté avant hash.
- [x] SIVC revérifié : **53 PDF**, aucun delta.
- [x] SEMC revérifié : **54 PDF**, aucun delta.
- [x] BOABF revérifié : **57 PDF**, aucun delta.
- [x] BOAB revérifié : **59 PDF**, aucun delta.
- [x] BOAC revérifié : **74 PDF** au lieu de 60, delta `+14` persisté avant SHA dans V14.
- [x] BOAN revérifié : **60 PDF**, aucun delta.
- [x] AGLC revérifié : **60 PDF**, aucun delta.
- [ ] continuer la revérification live société par société, prochain corpus : **BICC** (snapshot 61), puis **CIEC** (61).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 060**.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, y compris BOAB, BOAC, BOAN et AGLC.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB 59/59 ; BOAC 74/74 ; BOAN 60/60 ; AGLC 60/60.
- [x] total SHA calculés : **995 / 3 060** (**32,52 %**).
- [x] restant non hashé : **2 065 PDF**.
- [x] groupes exacts : **11**.
- [x] BOAN : **60 SHA uniques / 0 groupe exact**.
- [x] AGLC : **60 SHA uniques / 0 groupe exact**.
- [x] AGLC registre revalidé post-commit bit-for-bit via Git blob SHA `4c25045ffeb194aad7929b3b106a6fe6b7c7241c`.
- [ ] prochain : **BICC** après revérification live stricte.

### Doublons / versions

- [x] onze groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] BOAC S1 2021 plain / `_2` : `EXACT_DUPLICATE`.
- [x] BOAC EF 2019 plain / `_2` : même taille mais SHA différents.
- [x] BOABF paire `divers` : `EXACT_DUPLICATE` FY2017.
- [x] SIBC T1 2017 plain / `_2` / `_3` : `EXACT_DUPLICATE`.
- [x] SIBC S1 2022 plain / `_2` : `EXACT_DUPLICATE`.
- [x] SIVC, SEMC, BOAB, BOAN, AGLC : aucune duplication exacte dans leurs passes courantes.
- [x] AGLC T1 2025 plain / `_rev` : versions distinctes de la même publication ; `_rev` corrige notamment le résultat net annuel comparatif 2024 de **17 138 527** à **21 068 974 KFCFA**.
- [x] AGLC T1 2025 : ne pas renseigner automatiquement `supersedes_source_file_id` ; aucune formule explicite `annule et remplace` observée.
- [x] SIVC T3 2025 : source explicitement `annule et remplace` ; cible précédente absente du Drive courant.
- [ ] SIVC T3 2025 : retrouver la cible remplacée via P1-FRESH/BRVM puis renseigner `supersedes_source_file_id` sans supposition.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] BOAN `fiche_ne_0.pdf` = information boursière **S1 2017**.
- [x] BOAC `divers_Rapport_S1_BOAC.pdf` = **S1 2022**.
- [x] BOAC `fiche_ci_0.pdf` = information boursière **S1 2017**.
- [x] BOAB anomalie TPCI 5,90 % 2021-2031 identifiée et préservée.
- [x] AGLC 2020 : comptes IFRS **individuels** et **consolidés** à préserver comme scopes distincts.
- [x] règle renforcée : noms/dossiers ne dictent jamais seuls la période, le scope ou la version ; le contenu source prévaut.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`BICC_LIVE_RECHECK_AND_SHA` puis `CIEC_LIVE_RECHECK_AND_SHA`, ensuite poursuite par taille croissante.
