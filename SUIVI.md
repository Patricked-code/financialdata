# SUIVI — financialdata

Dernière mise à jour : 2026-08-20

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`. Git : `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

- sociétés : **48 / 48** ;
- état live courant : **V22 = 3 137 PDF** ;
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md` ;
- index : `inventory/p1_issuer_manifest.csv`.

V22 provient de NTLC : snapshot **81** → live strict parent-scoped **85**, delta **+4**, persisté avant SHA. V21 provenait d'ETIT : 81 → 100 (+19), également versionné avant SHA.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- maître : `inventory/p1_document_manifest.csv` ;
- consolidé : **14 / 3 137** à ce stade ;
- les corpus hashés disposent de Drive IDs + tailles + SHA dans `inventory/hashes/*.csv` ;
- backfill temporel/shards toujours requis.

## P1_TRANSVERSE — SHA256

- SHA calculés et vérifiés : **1 715 / 3 137 = 54,67 %** ;
- restant non hashé : **1 422 PDF** ;
- groupes exacts prouvés : **16**.

### NTLC — V22 terminé

- snapshot **81** → live strict **85**, delta **+4** ;
- cardinal live prouvé par deux sous-périmètres disjoints : `33 + 52 = 85` ;
- **85/85 PDF** matérialisés et signatures `%PDF-` valides ;
- **85 SHA uniques**, **0 groupe exact** ;
- registre `inventory/hashes/NTLC.csv` ;
- sérialisation LF canonique, 14 239 octets ;
- blob local/GitHub validé bit-for-bit : `90cd7791f2a57754ba3a21f873c8f1a18b543cf2` ;
- une première écriture textuelle divergente a été détectée par le garde-fou blob et remplacée avant toute déclaration de complétude ;
- 2024 EF plain / `_rev` : même période 31.12.2024 et mêmes principaux chiffres, mais pagination/représentation différentes (Excel 4 pages vs PDFium/DocuSign 1 page) ; famille de version/représentation conservatrice, aucun `SUPERSEDES` ;
- 2023 EF plain / `_2` : même exercice, formats/contenus comparatifs distincts, deux objets SOURCE conservés ; aucun `SUPERSEDES`.

ETIT reste terminé **100/100** avec registre blob-validé `908ac3c78239e14204ea21849775ed2eb75eb292`.

BNBC reste terminé **92/92** avec 92 SHA uniques et registre blob-validé `fb567fcdbf57af2aa6bb017544d2c29583e8359f`.

TRITRAF reste réconcilié **8/8** avec registre issuer-level blob-validé `c7a9c31558d4a9de5a1bea532d0cc4a2580876e6`, sans double comptage.

### Doublons exacts

Les **16 groupes exacts** prouvés restent tous conservés dans `inventory/p1_duplicate_groups.csv`. NTLC n'ajoute aucun groupe. Aucun objet SOURCE n'est supprimé ou fusionné physiquement.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. revalider le corpus Drive **CFAC** strictement par ses dossiers SOURCE réels ;
2. comparer le live au snapshot manifeste **94** ;
3. si delta, créer le checkpoint V23 avant SHA et corriger le dénominateur ;
4. matérialiser 100 % du périmètre CFAC live ;
5. valider signatures/tailles, SHA-256, doublons exacts et familles de version justifiées ;
6. créer puis blob-valider `inventory/hashes/CFAC.csv` ;
7. finaliser CFAC, manifeste, `SUIVI.md` et `TODO.md`, puis poursuivre le corpus réellement non hashé suivant.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=3137 | MASTER_CONSOLIDATED=14/3137 | SHA256_VERIFIED=1715/3137 | SHA_COVERAGE=54.67% | UNHASHED=1422 | EXACT_DUPLICATE_GROUPS=16 | NTLC=85/85_SHA_COMPLETE | NTLC_REGISTRY_BLOB=90cd7791f2a57754ba3a21f873c8f1a18b543cf2 | NEXT=CFAC_LIVE_RECHECK_AND_SHA`
