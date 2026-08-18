# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V20 = 3 114 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v20_20260818.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] PALC : 75 → 98, delta +23 versionné avant SHA (V19).
- [x] BNBC : **78 → 92**, delta **+14**, versionné avant SHA (V20).
- [x] BNBC : 28 dossiers annuels `1998–2025` vérifiés parent-scoped.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 114** à ce stade.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] PALC **98/98**, 96 SHA uniques, 2 groupes exacts, registre post-commit validé.
- [x] total SHA actuellement vérifiés : **1 438 / 3 114 = 46,18 %**.
- [x] restant non hashé après correction du dénominateur V20 : **1 676 PDF**.
- [x] groupes exacts globaux actuellement prouvés : **16**.
- [ ] BNBC : matérialiser **92/92**, valider signatures/tailles et calculer SHA-256.
- [ ] BNBC : créer `inventory/hashes/BNBC.csv` puis valider le blob GitHub post-commit.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [ ] BNBC 2019 : comparer cinq variantes d'états financiers (`plain`, `_2`, `_3`, `_4`, `_5`) d'abord par SHA puis par contenu si non exactes.
- [ ] BNBC 2020 : comparer les deux rapports S1 et les deux états financiers.
- [ ] BNBC 2022/2024 : comparer les variantes d'états financiers.
- [ ] aucune relation `SUPERSEDES` sans preuve explicite.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] BNBC : snapshot 78 rejeté comme vérité live après preuve parent-scoped de 92 objets.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`BNBC_MATERIALIZE_AND_SHA_92`, puis validation blob, fermeture BNBC et poursuite des corpus réellement non hashés par taille croissante.
