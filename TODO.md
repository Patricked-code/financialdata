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
- [x] BIIC 2/2, BOAS 43/43, BOAM 44/44, ECOC 42/42 : Drive IDs, tailles et SHA disponibles.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44.
- [x] total SHA calculés : **437 / 3 041**.
- [x] groupes exacts : **6**.
- [ ] prochain : SCRC ou TTLS, 45 PDF chacun, après revérification live.

### Doublons / versions

- [x] quatre groupes exacts antérieurs CBIBF/SHEC/ECOC.
- [x] BOAM EF 2023 / rapport CAC annuel 2023 : `EXACT_DUPLICATE`, SHA `77f20998d8b1def30299a400bbe4584093fb54a6e40d05f7ab5fa7721896e31e`.
- [x] BOAM CAC annuels 2024 plain / `_2` : `EXACT_DUPLICATE`, SHA `dc403fad3b516f6a94eecefafb56db518987c5fb3097edd0d68a7ffe8077f207`.
- [x] BOAM T3/T4 2019 : même taille mais SHA différents.
- [x] BOAM `2021_Etats_Financiers_BOAM_rev.pdf` : prédécesseur non retrouvé, aucune supersession démontrée ; revue `inventory/reviews/BOAM_VERSION_REVIEW_20260811.md`.
- [ ] relations sémantiques/version restantes.

### Périodes / qualité

- [x] BOAS `divers_Rapport_S1_BOAS.pdf` = S1 2019, preuve visuelle.
- [x] BOAM : 2013/2014 sans PDF direct et 2015 absent restent des constats de classement, pas des absences économiques inférées.
- [ ] périodes économiques fines depuis contenu pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`SCRC_OR_TTLS_LIVE_RECHECK_AND_SHA` puis poursuite par taille croissante.
