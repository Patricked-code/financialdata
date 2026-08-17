# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V18 = 3 077 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v18_20260817.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] BOAC : 60 → 74, delta +14 versionné avant SHA (V14).
- [x] BICC : 61 → 70, delta +9 versionné avant SHA (V15).
- [x] CIEC : 61 → 62, delta +1 versionné avant SHA (V16).
- [x] SLBC : 65 → 70, delta +5 versionné avant SHA (V17).
- [x] PRSC : 68 → **70**, delta **+2** versionné avant SHA (V18).
- [ ] continuer la revérification live société par société, prochain corpus : **SAFC** (snapshot 73), puis PALC (75).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 077**.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, y compris BICC, CIEC, SLBC et PRSC.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] BICC **70/70**, 69 SHA uniques, 1 groupe exact.
- [x] CIEC **62/62**, 61 SHA uniques, 1 groupe exact.
- [x] SLBC **70/70**, 70 SHA uniques, 0 groupe exact.
- [x] PRSC **70/70**, **70 SHA uniques, 0 groupe exact**.
- [x] total SHA calculés : **1 267 / 3 077 = 41,18 %**.
- [x] restant non hashé : **1 810 PDF**.
- [x] groupes exacts globaux : **13**.
- [x] BICC registre post-commit validé via blob `25baddade1e9e0366f3bdabfa6cdb2f13a5993ae`.
- [x] CIEC registre post-commit validé via blob `be1e68b95394d3c921adf506af3f0736b8d0c753`.
- [x] SLBC registre post-commit validé via blob `6b54e3cfc5f6616e274846ec041b1b758b491251`.
- [x] PRSC registre post-commit validé via blob `78c6332bf1849eae6dff57f37e910d5ce2863348`.
- [ ] prochain : **SAFC** après revérification live stricte.

### Doublons / versions

- [x] treize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv` ; SLBC et PRSC n'en ajoutent aucun.
- [x] BICC T3 2022 plain / `_2` : `EXACT_DUPLICATE`, SHA `492df4551aa01c2e97415323331b50a3f4eed65e952d38e2e97b7a524b64fae0`.
- [x] CIEC EF 2016 plain / `_2` : `EXACT_DUPLICATE`, SHA `87c568d69a67b3fe08befd474a348ab1e15d5c1ccadc035d2f751eda6cd4d0b8`.
- [x] CIEC EF 2017 plain / `_rev` : `VERSION_OF`, pas `EXACT_DUPLICATE` ni `SUPERSEDES` sans preuve.
- [x] BICC EF 2019 plain / `_rev` : `VERSION_OF`, pas doublon exact ni supersedes automatique.
- [x] SLBC S1 2020 : deux binaires distincts mais rendu identique ; `VERSION_OF`, pas `EXACT_DUPLICATE`, pas `SUPERSEDES` sans preuve.
- [x] PRSC EF 2023 plain / `_rev` : même exercice annuel 2023 sous formes détaillée/synthèse ; `VERSION_OF`, pas `EXACT_DUPLICATE` ni `SUPERSEDES` automatique.
- [x] PRSC S1 2023 : trois objets physiquement et visuellement distincts ; aucune fusion automatique.
- [x] PRSC EF 2024 : `_3` = semestriel 30/06/2024, plain/`_2` = annuels 31/12/2024 ; ne pas fusionner par suffixe.
- [x] PRSC EF 2025 plain / `_2` : scans distincts ; aucune fusion automatique.
- [x] AGLC T1 2025 plain / `_rev` : versions distinctes ; pas de `SUPERSEDES` sans preuve explicite.
- [x] SIVC T3 2025 : source explicitement `annule et remplace`, cible précédente encore à retrouver via P1-FRESH/BRVM.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] CIEC deep pilot existant conservé ; la passe SHA ajoute la preuve binaire sans refaire le modèle conceptuel.
- [x] SLBC : erratum AGO 2025 conservé comme SOURCE ; aucun filtrage par type documentaire.
- [x] PRSC : deux noms génériques récupérés uniquement par parent-scoped ; la recherche ticker n'est pas une définition de corpus.
- [x] PRSC : delta structurel des dossiers 2008–2010 documenté sans effacer la mémoire historique.
- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`SAFC_LIVE_RECHECK_AND_SHA` puis `PALC_LIVE_RECHECK_AND_SHA`, ensuite poursuite des corpus réellement non hashés par taille croissante.
