# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live **V15 = 3 069 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v15_20260817.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] BOAC : 60 → 74, delta +14 versionné avant SHA (V14).
- [x] BICC : 61 → **70**, delta **+9** versionné avant SHA (V15).
- [x] BOAN 60, AGLC 60 : aucun delta lors de leur passe courante.
- [ ] continuer la revérification live société par société, prochain corpus : **CIEC** (snapshot 61).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 069**.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, y compris BOAB, BOAC, BOAN, AGLC et BICC.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] BICC **70/70**, 69 SHA uniques, 1 groupe exact.
- [x] total SHA calculés : **1 065 / 3 069 = 34,70 %**.
- [x] restant non hashé : **2 004 PDF**.
- [x] groupes exacts globaux : **12**.
- [x] AGLC registre post-commit validé via blob `4c25045ffeb194aad7929b3b106a6fe6b7c7241c`.
- [x] BICC registre post-commit validé via blob `25baddade1e9e0366f3bdabfa6cdb2f13a5993ae`.
- [ ] prochain : **CIEC** après revérification live stricte.

### Doublons / versions

- [x] douze groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] BICC T3 2022 plain / `_2` : `EXACT_DUPLICATE`, SHA `492df4551aa01c2e97415323331b50a3f4eed65e952d38e2e97b7a524b64fae0`.
- [x] BICC EF 2019 plain / `_rev` : `VERSION_OF`, pas doublon exact ; mêmes valeurs économiques principales, variante révisée plus complète avec commentaire explicatif supplémentaire.
- [x] BICC EF 2019 : ne pas renseigner automatiquement `supersedes_source_file_id`, aucune formule explicite `annule et remplace` trouvée.
- [x] AGLC T1 2025 plain / `_rev` : versions distinctes ; pas de `SUPERSEDES` sans preuve explicite.
- [x] SIVC T3 2025 : source explicitement `annule et remplace`, cible précédente encore à retrouver via P1-FRESH/BRVM.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] BICC : T2 2022 et S1 2022 préservés comme périodes distinctes.
- [x] BICC `bilan_et_compte_de_resultat_bicici_31_12_2022_.pdf` conservé comme profil P1-R utile.
- [x] règle : noms/dossiers ne dictent jamais seuls période, scope, version ou doublon ; le contenu et les octets prévalent.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`CIEC_LIVE_RECHECK_AND_SHA`, puis poursuite des corpus non hashés par taille croissante.
