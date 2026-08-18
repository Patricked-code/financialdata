# SUIVI — financialdata

Dernière mise à jour : 2026-08-18

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V20 = 3 114 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v20_20260818.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V20 provient de BNBC : snapshot **78** → live strict parent-scoped **92**, delta **+14**, persisté avant SHA. V19 provenait de PALC : 75 → 98 (+23), également versionné avant SHA.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 114** à ce stade ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 438 / 3 114 = 46,18 %** ;
- restant non hashé : **1 676 PDF** ;
- groupes exacts prouvés : **16**.

Corpus récemment terminés : PRSC 70/70 ; SAFC 73/73 ; PALC 98/98. BNBC est en cours après verrouillage du nouveau périmètre live.

### Résultats PALC — V19

- snapshot **75** → live **98**, delta **+23** ;
- **98/98** PDF valides ; **96 SHA uniques** ;
- 2 groupes exacts : annuel 2007 `_2` / `_3` SHA `5c7b218089532b8275bff06fc0c3e9199fc891b5c12c03cdf373f4c182982c1c`, et T3 2018 plain / `_2` SHA `ae8fd065f86a129033728594ecc5162eda448e2a99624c218b2e55c05e24fe00` ;
- annuel 2009 plain / `_rev` : `VERSION_OF`, pas `SUPERSEDES` sans preuve explicite ;
- registre `inventory/hashes/PALC.csv` validé bit-for-bit, blob `5dbe863af2b7b3854b0a6e20d29cb67c6a9f7a35`.

### BNBC — recheck V20 / pré-hash

- dossier Drive canonique : `10u65PBoBi1nWppgn1Ttm-r96iCwdzsKs` ;
- **28 dossiers directs**, couverture continue `1998–2025` ;
- snapshot **78** → live strict parent-scoped **92**, delta **+14** ;
- checkpoint V20 créé avant SHA ; SOURCE global **3 114** ;
- cardinal annuel vérifié : `1998–2002: 1/an`, `2003–2008: 2/an`, `2009–2011: 4/an`, `2012: 5`, `2013: 4`, `2014: 3`, `2015: 2`, `2016: 3`, `2017: 4`, `2018: 5`, `2019: 9`, `2020: 6`, `2021: 5`, `2022: 5`, `2023: 3`, `2024: 6`, `2025: 3` ;
- 2019 contient cinq états financiers physiques (`plain`, `_2`, `_3`, `_4`, `_5`) ; revue SHA puis contenu obligatoire ;
- 2020 contient deux rapports S1 et deux états financiers ; 2022/2024 ont également des variantes d'états financiers ;
- aucune relation de doublon/version n'est encore déclarée avant SHA.

### Doublons exacts

Les **16 groupes exacts** prouvés restent tous conservés dans `inventory/p1_duplicate_groups.csv`. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. matérialiser les **92/92 PDF BNBC** live ;
2. valider signatures `%PDF-` et tailles ;
3. calculer SHA-256 exhaustif ;
4. identifier les groupes exacts et revoir les variantes 2019/2020/2022/2024 par contenu ;
5. créer `inventory/hashes/BNBC.csv` ;
6. valider post-commit le blob GitHub contre le blob Git calculé localement ;
7. finaliser BNBC, manifeste, doublons, `SUIVI.md` et `TODO.md` ;
8. poursuivre ensuite les corpus réellement non hashés par taille croissante.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3114 | MASTER_CONSOLIDATED=14/3114 | SHA256_VERIFIED=1438/3114 | SHA_COVERAGE=46.18% | UNHASHED=1676 | EXACT_DUPLICATE_GROUPS=16 | PALC=98/98_SHA_COMPLETE | BNBC=92_LIVE_HASH_PENDING | NEXT=BNBC_MATERIALIZE_AND_SHA`
