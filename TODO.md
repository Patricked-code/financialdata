# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V21 = 3 133 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v21_20260818.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] BNBC : **78 → 92**, delta **+14**, versionné avant SHA (V20), puis SHA 92/92 terminé.
- [x] TRITRAF : hash historique 8/8 réconcilié avec un registre issuer-level manquant, sans double comptage.
- [x] ETIT : **81 → 100**, delta **+19**, versionné avant SHA (V21).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 133** à ce stade.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] BNBC **92/92**, 92 SHA uniques, 0 groupe exact, registre blob-validé `fb567fcdbf57af2aa6bb017544d2c29583e8359f`.
- [x] TRITRAF **8/8** déjà calculés ; registre restauré depuis `p1_document_manifest.csv`, blob validé `c7a9c31558d4a9de5a1bea532d0cc4a2580876e6` ; aucun ajout au compteur global.
- [x] total SHA vérifiés avant ETIT : **1 530 / 3 133 = 48,83 %**.
- [x] restant non hashé avant ETIT : **1 603 PDF**.
- [x] groupes exacts globaux : **16**.
- [ ] ETIT : matérialiser **100/100**, valider signatures/tailles et calculer SHA-256 exhaustif.
- [ ] ETIT : créer `inventory/hashes/ETIT.csv` puis valider le blob GitHub post-commit.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] BNBC 2019 EF plain / `_2` : `VERSION_OF`, pas `SUPERSEDES` sans preuve explicite.
- [x] BNBC garde-fou période : `2024_Etats_Financiers_BNBC_2.pdf` porte sur l'exercice clos au 31/12/2023 malgré son nom physique.
- [ ] ETIT : qualifier les collisions exactes puis seulement les relations sémantiques justifiées ; variantes historiques jusqu'à `_7`.
- [ ] aucune relation `SUPERSEDES` sans preuve explicite.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] ETIT : cardinal live recompté en deux sous-périmètres disjoints (`51 + 49 = 100`) pour contourner proprement le plafond de 100 résultats du connecteur.
- [x] ETIT : les noms génériques/de filiales ne sont pas exclus du périmètre SOURCE parent-scoped.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`ETIT_MATERIALIZE_AND_SHA_100`, puis validation blob, fermeture ETIT et poursuite des corpus réellement non hashés après vérification des registres existants.
