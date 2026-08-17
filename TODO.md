# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V19 = 3 100 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v19_20260817.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] PRSC : 68 → 70, delta +2 versionné avant SHA (V18).
- [x] SAFC : 73 → 73, delta 0 ; pas de version artificielle.
- [x] PALC : **75 → 98**, delta **+23**, versionné avant SHA (V19).
- [ ] prochain recheck live : **BNBC** (snapshot 78).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 100** à ce stade.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, y compris SAFC et PALC.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] SAFC **73/73**, 72 SHA uniques, 1 groupe exact.
- [x] PALC **98/98**, **96 SHA uniques, 2 groupes exacts**.
- [x] total SHA calculés : **1 438 / 3 100 = 46,39 %**.
- [x] restant non hashé : **1 662 PDF**.
- [x] groupes exacts globaux : **16**.
- [x] SAFC registre post-commit validé : blob `4d68e2f99a3d8a90fe70ecf858c7064924f27dd3`.
- [x] PALC registre post-commit validé : blob `5dbe863af2b7b3854b0a6e20d29cb67c6a9f7a35`.
- [ ] prochain : **BNBC** après revérification live stricte.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] PALC annuel 2007 `_2` / `_3` : `EXACT_DUPLICATE`, SHA `5c7b218089532b8275bff06fc0c3e9199fc891b5c12c03cdf373f4c182982c1c`.
- [x] PALC T3 2018 plain / `_2` : `EXACT_DUPLICATE`, SHA `ae8fd065f86a129033728594ecc5162eda448e2a99624c218b2e55c05e24fe00`.
- [x] PALC annuel 2009 plain / `_rev` : `VERSION_OF`; corrections de contenu, pas `EXACT_DUPLICATE`, pas `SUPERSEDES` sans preuve explicite.
- [x] tous les objets physiques PALC/SAFC restent conservés.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] PALC : deux noms génériques hors motif ticker inclus grâce au périmètre parent-scoped.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`BNBC_LIVE_RECHECK_AND_SHA`, puis poursuite des corpus réellement non hashés par taille croissante, en parallèle du backfill documentaire et de P1-R/P1-FRESH.
