# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V18 = 3 077 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v18_20260817.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] PRSC : 68 → 70, delta +2 versionné avant SHA (V18).
- [x] SAFC : **73 → 73**, delta 0 ; V18 préservé sans version artificielle.
- [ ] continuer la revérification live société par société : **PALC (snapshot 75)**, puis BNBC (78).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 077**.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, désormais y compris SAFC.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] PRSC **70/70**, 70 SHA uniques, 0 groupe exact.
- [x] SAFC **73/73**, **72 SHA uniques, 1 groupe exact**.
- [x] total SHA calculés : **1 340 / 3 077 = 43,55 %**.
- [x] restant non hashé : **1 737 PDF**.
- [x] groupes exacts globaux : **14**.
- [x] SAFC registre post-commit validé via blob `4d68e2f99a3d8a90fe70ecf858c7064924f27dd3`.
- [ ] prochain : **PALC** après revérification live stricte.

### Doublons / versions

- [x] quatorze groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] SAFC 2007 plain / `_3` : `EXACT_DUPLICATE`, taille 1 475 293 octets, SHA `85f0a68ee4e126d93fcb09dafbf644e24b61454d428974787391c6f5cde8884c` ; deux objets physiques conservés.
- [x] SAFC : les collisions de suffixes restantes ne sont pas fusionnées sans SHA/contenu.
- [x] SAFC : fichiers génériques T4 2022 et T4 2024 récupérés grâce au parent-scoped.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] SAFC : absence du dossier 2015 documentée comme lacune SOURCE, sans reconstruction artificielle.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`PALC_LIVE_RECHECK_AND_SHA` puis `BNBC_LIVE_RECHECK_AND_SHA`, ensuite poursuite des corpus réellement non hashés par taille croissante.
