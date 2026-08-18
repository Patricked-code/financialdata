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

- SHA calculés et vérifiés : **1 530 / 3 114 = 49,13 %** ;
- restant non hashé : **1 584 PDF** ;
- groupes exacts prouvés : **16**.

Corpus récemment terminés : PRSC 70/70 ; SAFC 73/73 ; PALC 98/98 ; **BNBC 92/92**.

### Résultats BNBC — V20

- dossier Drive canonique : `10u65PBoBi1nWppgn1Ttm-r96iCwdzsKs` ;
- **28 dossiers directs**, couverture continue `1998–2025` ;
- snapshot **78** → live strict parent-scoped **92**, delta **+14** ;
- checkpoint V20 créé avant SHA ; SOURCE global **3 114** ;
- **92/92** PDF matérialisés, signatures `%PDF-` et tailles validées ;
- **92 SHA uniques**, donc **0 groupe exact BNBC** ;
- registre `inventory/hashes/BNBC.csv` ; validation post-commit bit-for-bit : blob local = GitHub **`fb567fcdbf57af2aa6bb017544d2c29583e8359f`** ;
- 2019 EF plain / `_2` : même publication économique IFRS annuelle 2019, binaires distincts et correction de date d'arrêté/approbation ; relation conservatrice `VERSION_OF`, pas `EXACT_DUPLICATE`, pas `SUPERSEDES` sans preuve explicite ;
- 2019 `_3`, `_4`, `_5` : publications synthétique, certifiée/de synthèse et provisoire distinctes, conservées séparément ;
- 2020 S1 : deux publications distinctes, dont l'une explicitement IFRS ; aucune fusion ;
- garde-fou de période : `2024_Etats_Financiers_BNBC_2.pdf` porte explicitement sur l'exercice clos au **31/12/2023** malgré son nom physique ; la période économique est donc 2023 ;
- aucun changement de `inventory/p1_duplicate_groups.csv` requis.

### Doublons exacts

Les **16 groupes exacts** prouvés restent tous conservés dans `inventory/p1_duplicate_groups.csv`. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. identifier le plus petit corpus **réellement non hashé** en contrôlant l'existence du registre `inventory/hashes/<TICKER>.csv` plutôt qu'en se fiant au seul statut manifeste ;
2. candidat prioritaire : **TRITRAF**, snapshot manifeste **8 PDF**, sous réserve d'absence de registre SHA déjà existant ;
3. si réellement non hashé : recheck live strict parent-scoped, versionner tout delta SOURCE avant SHA, puis matérialiser/hash 100 % ;
4. poursuivre ensuite les corpus réellement non hashés par taille croissante ;
5. continuer le backfill du manifeste documentaire, P1-R et P1-FRESH avant extraction RAW exhaustive.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3114 | MASTER_CONSOLIDATED=14/3114 | SHA256_VERIFIED=1530/3114 | SHA_COVERAGE=49.13% | UNHASHED=1584 | EXACT_DUPLICATE_GROUPS=16 | BNBC=92/92_SHA_COMPLETE | NEXT=VERIFY_TRITRAF_HASH_STATE_THEN_LIVE_RECHECK_AND_SHA`
