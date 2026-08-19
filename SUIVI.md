# SUIVI — financialdata

Dernière mise à jour : 2026-08-19

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

- SHA calculés et vérifiés : **1 630 / 3 133 = 52,03 %** ;
- restant non hashé : **1 503 PDF** ;
- groupes exacts prouvés : **16**.

### ETIT — V21 terminé

- snapshot **81** → live strict **100**, delta **+19** ;
- cardinal live prouvé par deux sous-périmètres disjoints : `51 + 49 = 100` ;
- **100/100 PDF** matérialisés et signatures `%PDF-` valides ;
- **100 SHA uniques**, **0 groupe exact** ;
- registre `inventory/hashes/ETIT.csv` ;
- blob local/GitHub validé bit-for-bit : `908ac3c78239e14204ea21849775ed2eb75eb292` ;
- 2020/2021 S1 : tableaux d'activité et rapports d'examen limité conservés comme documents compagnons distincts ;
- 2021 EF audité/non audité : même exercice, publications distinctes conservées, aucun `SUPERSEDES` inféré ;
- 2022 T3 plain / `_2` : même période, petites différences chiffrées, famille de publication non exacte, aucun `SUPERSEDES` ;
- 2018 annual plain / `_2` : scopes internes différents (Groupe Ecobank vs Ecobank Côte d'Ivoire), donc pas traités comme versions sur la seule base du suffixe.

BNBC reste terminé **92/92** avec 92 SHA uniques et registre blob-validé `fb567fcdbf57af2aa6bb017544d2c29583e8359f`.

TRITRAF reste réconcilié **8/8** avec registre issuer-level blob-validé `c7a9c31558d4a9de5a1bea532d0cc4a2580876e6`, sans double comptage.

### Doublons exacts

Les **16 groupes exacts** prouvés restent tous conservés dans `inventory/p1_duplicate_groups.csv`. ETIT n'ajoute aucun groupe. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. revalider le corpus Drive **NTLC** strictement par ses dossiers SOURCE réels ;
2. comparer le live au snapshot manifeste **81** ;
3. si delta, créer le checkpoint suivant avant SHA et corriger le dénominateur ;
4. matérialiser 100 % du périmètre NTLC live ;
5. valider signatures/tailles, SHA-256, doublons exacts et familles de version justifiées ;
6. créer puis blob-valider `inventory/hashes/NTLC.csv` ;
7. finaliser NTLC, manifeste, `SUIVI.md` et `TODO.md`, puis poursuivre le corpus réellement non hashé suivant.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3133 | MASTER_CONSOLIDATED=14/3133 | SHA256_VERIFIED=1630/3133 | SHA_COVERAGE=52.03% | UNHASHED=1503 | EXACT_DUPLICATE_GROUPS=16 | ETIT=100/100_SHA_COMPLETE | ETIT_REGISTRY_BLOB=908ac3c78239e14204ea21849775ed2eb75eb292 | NEXT=NTLC_LIVE_RECHECK_AND_SHA`
