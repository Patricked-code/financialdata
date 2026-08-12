# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live V13 **3 046 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v13_20260811.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] SIBC revérifié : **49 PDF** au lieu de 46, delta `+3` persisté avant hash.
- [ ] continuer la revérification live société par société, prochain corpus : **SIVC**.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 046**.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, y compris SIBC 49/49.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49.
- [x] total SHA calculés : **578 / 3 046** (**18,98 %**).
- [x] groupes exacts : **9**.
- [ ] prochain : **SIVC** après revérification live stricte.

### Doublons / versions

- [x] neuf groupes exacts actuellement documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] SIBC T1 2017 plain / `_2` / `_3` : `EXACT_DUPLICATE`, SHA `3446b816e1a15b4a8d2df8bfeff775dbaa7166b52823c0d8d2bf8f1b06fc6b23`.
- [x] SIBC S1 2022 plain / `_2` : `EXACT_DUPLICATE`, SHA `b96ab01184f501d6f726250132108e742d8b5ede7ca862ce088b5aa29d7c88ec`.
- [x] SIBC : aucun autre doublon exact parmi 49 sources ; variantes 2018 `_rev` / `_rev_2`, CAC 2018, S1 2020 et EF 2020 restent binaires distinctes.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Périodes / qualité

- [x] BOAS `divers_Rapport_S1_BOAS.pdf` = S1 2019, preuve visuelle.
- [x] SCRC `divers_Attestation_CAC_Annuel_SCRC.pdf` = attestation CAC S1 2017, preuve visuelle.
- [x] TTLS `divers_Rapport_CAC_Annuel_TTLS.pdf` = rapport général et rapports spéciaux CAC **FY 2020**, exercice clos le 31/12/2020, preuve texte native.
- [x] règle renforcée : noms/dossiers ne dictent jamais la période ; le contenu source prévaut.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`SIVC_LIVE_RECHECK_AND_SHA` puis poursuite par taille croissante.
