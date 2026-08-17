# SUIVI — financialdata

Dernière mise à jour : 2026-08-17

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V19 = 3 100 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v19_20260817.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V19 provient de PALC : snapshot **75** → live strict parent-scoped **98**, delta **+23**, persisté avant SHA. V18 provenait de PRSC : 68 → 70 (+2). SAFC a ensuite été rechecké 73 → 73, delta 0, sans version artificielle.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 100** à ce stade ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 438 / 3 100 = 46,39 %** ;
- restant non hashé : **1 662 PDF** ;
- groupes exacts prouvés : **16**.

Corpus récemment terminés : PRSC 70/70 ; SAFC 73/73 ; **PALC 98/98**.

### Résultats SAFC — V18

- snapshot 73 → live 73, delta 0 ;
- 73/73 PDF valides ; 72 SHA uniques ;
- 1 groupe exact : 2007 plain / `_3`, SHA `85f0a68ee4e126d93fcb09dafbf644e24b61454d428974787391c6f5cde8884c` ;
- registre `inventory/hashes/SAFC.csv`, blob validé `4d68e2f99a3d8a90fe70ecf858c7064924f27dd3`.

### Résultats PALC — V19

- dossier Drive canonique : `1w2XGE38g12wfH6Dm0UdZKAraYmg7vzNZ` ;
- 25 dossiers directs live ; couverture `1999`, `2001`, puis `2003–2025` ;
- snapshot **75** → live strict parent-scoped **98**, delta **+23** ;
- checkpoint V19 créé avant SHA ; SOURCE global **3 100** ;
- **98/98** matérialisés et signatures `%PDF-` valides ;
- **96 SHA uniques** ;
- **2 groupes exacts** :
  - annuel 2007 `_2` / `_3`, SHA `5c7b218089532b8275bff06fc0c3e9199fc891b5c12c03cdf373f4c182982c1c` ;
  - T3 2018 plain / `_2`, SHA `ae8fd065f86a129033728594ecc5162eda448e2a99624c218b2e55c05e24fe00` ;
- tous les objets physiques sont conservés et les groupes sont enregistrés dans `inventory/p1_duplicate_groups.csv` ;
- `2009_Rapport_Annuel_PALC.pdf` / `_rev` : même publication économique 2009, binaires et contenus distincts, corrections de postes ; `VERSION_OF`, pas `EXACT_DUPLICATE`, pas `SUPERSEDES` sans preuve explicite ;
- noms génériques `efp_-_palm_ci_-_2014.pdf` et `190430_rapport_dactivite_2nd_semestre_2018_-_palm_ci.pdf` inclus grâce au parent-scoped ;
- registre `inventory/hashes/PALC.csv` ;
- validation post-commit bit-for-bit : blob local = GitHub **`5dbe863af2b7b3854b0a6e20d29cb67c6a9f7a35`**.

### Doublons exacts

Les **16 groupes exacts** restent tous conservés dans `inventory/p1_duplicate_groups.csv`. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. traiter **BNBC** — snapshot manifeste **78 PDF** ;
2. recheck strict du Drive canonique par dossiers enfants réels + `mimeType='application/pdf'` ;
3. si delta : créer **V20** et mettre à jour le dénominateur avant tout SHA ;
4. matérialiser/hash 100 %, revue collisions et versions ;
5. mettre à jour inventaire, registre SHA, manifeste, doublons, `SUIVI.md` et `TODO.md` ;
6. poursuivre ensuite les corpus réellement non hashés par taille croissante ;
7. continuer le backfill du manifeste documentaire, P1-R et P1-FRESH avant extraction RAW exhaustive.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3100 | MASTER_CONSOLIDATED=14/3100 | SHA256_VERIFIED=1438/3100 | SHA_COVERAGE=46.39% | UNHASHED=1662 | EXACT_DUPLICATE_GROUPS=16 | SAFC=73/73_SHA_COMPLETE | PALC=98/98_SHA_COMPLETE | NEXT=BNBC_LIVE_RECHECK_AND_SHA`
