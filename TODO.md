# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V22 = 3 137 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] ETIT : **81 → 100**, delta **+19**, versionné avant SHA (V21), puis SHA 100/100 terminé.
- [x] NTLC : **81 → 85**, delta **+4**, versionné avant SHA (V22), puis SHA 85/85 terminé.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 137** à ce stade.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] NTLC **85/85**, 85 SHA uniques, 0 groupe exact.
- [x] NTLC registre `inventory/hashes/NTLC.csv` blob-validé : `90cd7791f2a57754ba3a21f873c8f1a18b543cf2`.
- [x] total SHA vérifiés : **1 715 / 3 137 = 54,67 %**.
- [x] restant non hashé : **1 422 PDF**.
- [x] groupes exacts globaux : **16**.
- [ ] CFAC : recheck live strict du snapshot **94**, puis SHA exhaustif du périmètre confirmé.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv` ; NTLC n'en ajoute aucun.
- [x] NTLC 2024 EF plain / `_rev` : même période et mêmes principaux chiffres mais représentation/pagination différentes ; famille de version/représentation conservatrice, aucun `SUPERSEDES`.
- [x] NTLC 2023 EF plain / `_2` : même exercice, formats/contenus comparatifs distincts ; deux objets SOURCE conservés, aucun `SUPERSEDES`.
- [ ] aucune relation `SUPERSEDES` sans preuve explicite.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] NTLC : périmètre live défini par 28 parent IDs réels 1998–2025 et non par ticker seul.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`CFAC_LIVE_RECHECK_AND_SHA`, avec checkpoint préalable V23 si le live diffère du snapshot 94, puis validation blob et poursuite des corpus réellement non hashés.
