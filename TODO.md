# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live V12 **3 043 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v12_20260811.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] TTLS revérifié : **47 PDF** au lieu de 45, delta `+2` persisté avant hash.
- [ ] continuer la revérification live société par société.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 043**.
- [x] BIIC 2/2, BOAS 43/43, BOAM 44/44, ECOC 42/42, SCRC 45/45, TTLS 47/47 : Drive IDs, tailles et SHA disponibles.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47.
- [x] total SHA calculés : **529 / 3 043**.
- [x] groupes exacts : **7**.
- [ ] prochain : SIBC après revérification live.

### Doublons / versions

- [x] sept groupes exacts actuellement documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] TTLS annuels 2018 plain / `_2` : `EXACT_DUPLICATE`, SHA `46b4ee85f5ad173c2de754c1054b0118b18e3a9758acec3db59cc56358275237`.
- [x] TTLS : aucun autre doublon exact parmi 47 sources ; variantes EF 2016/2021/2022/2023/2024 restent binaires distinctes.
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

`SIBC_LIVE_RECHECK_AND_SHA` puis poursuite par taille croissante.
