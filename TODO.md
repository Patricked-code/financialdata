# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V21 = 3 133 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v21_20260818.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] ETIT : **81 → 100**, delta **+19**, versionné avant SHA (V21), puis SHA 100/100 terminé.

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 133** à ce stade.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] ETIT **100/100**, 100 SHA uniques, 0 groupe exact.
- [x] ETIT registre `inventory/hashes/ETIT.csv` blob-validé : `908ac3c78239e14204ea21849775ed2eb75eb292`.
- [x] total SHA vérifiés : **1 630 / 3 133 = 52,03 %**.
- [x] restant non hashé : **1 503 PDF**.
- [x] groupes exacts globaux : **16**.
- [ ] NTLC : recheck live strict du snapshot **81**, puis SHA exhaustif du périmètre confirmé.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv` ; ETIT n'en ajoute aucun.
- [x] ETIT 2020/2021 S1 : documents compagnons distincts, pas de doublon ni `SUPERSEDES`.
- [x] ETIT 2021 EF audité / non audité : même exercice, publications distinctes conservées ; pas de `SUPERSEDES` sans preuve explicite.
- [x] ETIT 2022 T3 plain / `_2` : même période avec petites différences chiffrées ; non exacts, aucun `SUPERSEDES` inféré.
- [x] ETIT 2018 annual plain / `_2` : scopes internes différents, pas versions sur la seule base du suffixe.
- [ ] aucune relation `SUPERSEDES` sans preuve explicite.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] ETIT : noms génériques/de filiales conservés dans le périmètre parent-scoped ; identité interne utilisée pour la revue sémantique.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`NTLC_LIVE_RECHECK_AND_SHA`, avec checkpoint préalable si le live diffère du snapshot 81, puis validation blob et poursuite des corpus réellement non hashés.
