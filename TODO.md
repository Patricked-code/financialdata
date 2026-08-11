# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live V11 **3 041 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v11_20260810.md` ; index `inventory/p1_issuer_manifest.csv`.
- [ ] continuer la revérification live société par société.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 041**.
- [x] BIIC 2/2, BOAS 43/43, BOAM 44/44, ECOC 42/42, SCRC 45/45 : Drive IDs, tailles et SHA disponibles.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45.
- [x] total SHA calculés : **482 / 3 041**.
- [x] groupes exacts : **6**.
- [ ] prochain : TTLS 45 PDF après revérification live.

### Doublons / versions

- [x] six groupes exacts actuellement documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] BOAM EF 2023 / rapport CAC annuel 2023 et CAC annuels 2024 : doublons exacts.
- [x] BOAM T3/T4 2019 : même taille, SHA différents.
- [x] BOAM `_rev` 2021 : prédécesseur non retrouvé, aucune supersession prouvée.
- [x] SCRC : **45 SHA uniques** ; toutes les variantes EF `plain/_2/_3` observées sont binaires distinctes.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Périodes / qualité

- [x] BOAS `divers_Rapport_S1_BOAS.pdf` = S1 2019, preuve visuelle.
- [x] SCRC `divers_Attestation_CAC_Annuel_SCRC.pdf` = **attestation CAC S1 2017**, période 01/01–30/06/2017, datée 20/10/2017 ; le libellé `Annuel` du nom est contredit par le contenu.
- [x] règle renforcée : noms/dossiers ne dictent jamais la période ; le contenu source prévaut.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`TTLS_LIVE_RECHECK_AND_SHA` puis poursuite par taille croissante.
