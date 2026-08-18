# SUIVI — financialdata

Dernière mise à jour : 2026-08-18

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V21 = 3 133 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v21_20260818.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V21 provient d'ETIT : snapshot **81** → live strict parent-scoped **100**, delta **+19**, persisté avant SHA. V20 provenait de BNBC : 78 → 92 (+14), également versionné avant SHA.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 133** à ce stade ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 530 / 3 133 = 48,83 %** ;
- restant non hashé : **1 603 PDF** ;
- groupes exacts prouvés : **16**.

BNBC est terminé **92/92** avec 92 SHA uniques et registre blob-validé `fb567fcdbf57af2aa6bb017544d2c29583e8359f`.

TRITRAF était déjà hashé **8/8** dans le manifeste documentaire et son inventaire, mais son registre issuer-level manquait. `inventory/hashes/TRITRAF.csv` a été restauré sans recalcul ni double comptage, puis validé bit-for-bit : blob `c7a9c31558d4a9de5a1bea532d0cc4a2580876e6`. Son statut manifeste est désormais `SHA256_COMPLETE`.

### ETIT — recheck V21 / pré-hash

- dossier Drive canonique : `183KoqvNUQNaj6kdfw80PkkIGupbvuSia` ;
- **23 dossiers directs**, continus `2003–2025` ;
- snapshot **81** → live strict **100**, delta **+19** ;
- le résultat global atteignant le plafond de 100 du connecteur, le cardinal a été recompté sur deux sous-périmètres disjoints : `2003–2014 = 51`, `2015–2025 = 49` ;
- checkpoint V21 créé avant SHA ; SOURCE global **3 133** ;
- des noms génériques/de filiales du groupe existent dans le périmètre, notamment `ra_-_ecobank_tg_-_excercice_2010.pdf` ; aucun filtre ticker n'est utilisé comme vérité SOURCE ;
- aucun SHA ETIT nouveau n'est encore déclaré à ce stade.

### Doublons exacts

Les **16 groupes exacts** prouvés restent tous conservés dans `inventory/p1_duplicate_groups.csv`. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. matérialiser les **100/100 PDF ETIT** du périmètre parent-scoped V21 ;
2. valider signatures `%PDF-` et tailles ;
3. calculer SHA-256 exhaustif ;
4. identifier les collisions exactes et revoir seulement les familles de versions justifiées par le contenu ;
5. créer `inventory/hashes/ETIT.csv` avec LF, calculer le blob Git local et vérifier le blob GitHub post-commit ;
6. finaliser ETIT, manifeste, doublons, `SUIVI.md` et `TODO.md` ;
7. poursuivre ensuite les corpus réellement non hashés après contrôle de l'existence des registres.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3133 | MASTER_CONSOLIDATED=14/3133 | SHA256_VERIFIED=1530/3133 | SHA_COVERAGE=48.83% | UNHASHED=1603 | EXACT_DUPLICATE_GROUPS=16 | BNBC=92/92_SHA_COMPLETE | TRITRAF=8/8_REGISTRY_RECONCILED | ETIT=100_LIVE_HASH_PENDING | NEXT=ETIT_MATERIALIZE_AND_SHA`
