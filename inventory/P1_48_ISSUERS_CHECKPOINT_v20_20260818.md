# P1 — CHECKPOINT V20 — 48 ISSUERS — 2026-08-18

## Objet

Versionner le delta SOURCE détecté lors de la revérification live de `BNBC` avant tout calcul SHA-256 sur ce corpus.

## Baseline précédente

- checkpoint précédent : `inventory/P1_48_ISSUERS_CHECKPOINT_v19_20260817.md` ;
- total SOURCE V19 : **3 100 PDF** ;
- BNBC snapshot manifeste V19 : **78 PDF**.

## Revérification live BNBC

- émetteur : Bernabé Côte d'Ivoire / `BNBC` ;
- dossier Drive canonique : `10u65PBoBi1nWppgn1Ttm-r96iCwdzsKs` ;
- recheck : recherche strictement bornée aux **28 dossiers enfants réels** avec `mimeType = application/pdf` ;
- couverture live : **1998–2025** sans dossier annuel manquant ;
- PDF live : **92** ;
- delta net PDF : **+14** par rapport au snapshot 78 ;
- cardinal annuel vérifié : `1998–2002: 1/an`, `2003–2008: 2/an`, `2009–2011: 4/an`, `2012: 5`, `2013: 4`, `2014: 3`, `2015: 2`, `2016: 3`, `2017: 4`, `2018: 5`, `2019: 9`, `2020: 6`, `2021: 5`, `2022: 5`, `2023: 3`, `2024: 6`, `2025: 3` ;
- 2019 contient cinq objets `Etats_Financiers` distincts par identité Drive (`plain`, `_2`, `_3`, `_4`, `_5`) et exige une revue binaire puis sémantique ;
- 2020 contient deux rapports S1 et deux états financiers ; 2022 et 2024 contiennent également des variantes d'états financiers.

Aucun fichier SOURCE n'est supprimé, déplacé ou renommé. Le checkpoint décrit uniquement l'état live actuellement vérifiable.

## Nouveau total SOURCE

`3 100 + 14 = 3 114 PDF`

Le dénominateur canonique devient donc **V20 = 3 114 PDF** avant tout SHA BNBC.

## Règles de preuve

- le snapshot antérieur n'est pas traité comme vérité live ;
- aucun document n'est exclu à cause de son nom ou d'un suffixe ;
- les suffixes `_2`, `_3`, `_4`, `_5` ne déterminent aucune relation sans preuve binaire/sémantique ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `SUPERSEDES` exige une preuve explicite ;
- SOURCE physique reste immuable dans le processus de réconciliation.

## Suite immédiate

1. matérialiser les **92/92** PDF BNBC live ;
2. valider signatures PDF et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/BNBC.csv` ;
5. qualifier les collisions exactes et revoir les variantes 2019/2020/2022/2024 par contenu lorsque les SHA diffèrent ;
6. revalider le registre GitHub après commit par comparaison du blob Git local attendu et du blob GitHub ;
7. mettre à jour BNBC, manifeste, doublons, `SUIVI.md` et `TODO.md`.

## Point de reprise

`SOURCE_VERSION=V20 | LIVE_TOTAL=3114 | BNBC_SNAPSHOT=78 | BNBC_LIVE=92 | BNBC_DELTA=+14 | BNBC_HASH=PENDING`
