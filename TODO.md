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
- [x] BNBC **92/92**, **92 SHA uniques, 0 groupe exact**.
- [x] BNBC registre post-commit validé : blob `fb567fcdbf57af2aa6bb017544d2c29583e8359f`.
- [x] total SHA vérifiés : **1 530 / 3 114 = 49,13 %**.
- [x] restant non hashé : **1 584 PDF**.
- [x] groupes exacts globaux : **16**.
- [ ] vérifier l'existence d'un registre SHA pour **TRITRAF** avant tout nouveau travail ; si absent, recheck live strict puis SHA 100 %.

### Doublons / versions

- [x] seize groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] BNBC 2019 EF plain / `_2` : `VERSION_OF`, binaires distincts, correction de date d'arrêté/approbation ; pas `SUPERSEDES` sans preuve explicite.
- [x] BNBC 2019 `_3/_4/_5` : formes de publication distinctes, aucune fusion.
- [x] BNBC 2020 S1 : deux publications distinctes, dont une explicitement IFRS ; aucune fusion.
- [x] BNBC n'ajoute aucun groupe exact ; registre global des doublons inchangé.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] règle : noms/dossiers/suffixes ne dictent jamais seuls période, scope, version ou doublon ; contenu et octets prévalent.
- [x] BNBC : snapshot 78 rejeté comme vérité live après preuve parent-scoped de 92 objets.
- [x] garde-fou BNBC : `2024_Etats_Financiers_BNBC_2.pdf` porte explicitement sur l'exercice clos au **31/12/2023** ; période économique 2023 malgré le nom physique.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`VERIFY_TRITRAF_HASH_STATE`, puis, uniquement si le registre n'existe pas, `TRITRAF_LIVE_RECHECK_AND_SHA`; poursuivre ensuite les corpus réellement non hashés par taille croissante.
