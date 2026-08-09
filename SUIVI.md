# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- snapshot initial : **2 950 PDF** — conservé dans `inventory/P1_48_ISSUERS_CHECKPOINT.md` ;
- état live revérifié : **2 957 PDF** ;
- checkpoint live v2 : `inventory/P1_48_ISSUERS_CHECKPOINT_v2_20260809.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

### Pourquoi 2 950 → 2 957

CBIBF est passé de **8 à 15 PDF** pendant la même session. Sept fichiers ont été ajoutés dans Drive avec des `created_time` vers 06:36–06:37Z :

- 2022 : +3 ;
- 2024 : +2 S1 ;
- 2025 : +2.

L'ancien état n'est pas supprimé : il reste un snapshot historique.

## P1_TRANSVERSE — DOCUMENT MANIFEST

- schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md` ;
- manifeste : `inventory/p1_document_manifest.csv` ;
- couverture : **14 / 2 957 sources**.

Présents : BICC seed, BIIC 2/2, SNTS anomalie seed, TRITRAF 8/8, paire CBIBF S1 2024.

## P1_TRANSVERSE — SHA256

- SHA calculés : **10 / 2 957** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **2 / 15**.

### Doublon exact CBIBF

`2024_Rapport_S1_CBIBF.pdf` et `2024_Rapport_S1_CBIBF_2.pdf` :

- même taille : 1 549 372 octets ;
- même SHA-256 : `8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05` ;
- verdict : `EXACT_DUPLICATE`.

Les deux lignes SOURCE sont conservées. Groupe enregistré dans `inventory/p1_duplicate_groups.csv`.

### TRITRAF 2004

Les deux variantes 2004 ont des SHA différents : doublon binaire exclu ; relation sémantique/version encore non revue.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

1. compléter les **13 autres lignes CBIBF** dans `p1_document_manifest.csv` ;
2. calculer les 13 SHA restants CBIBF ;
3. poursuivre par ORAC, SICC, MVSC, UNLC ;
4. maintenir le total live et `first_seen_at/last_seen_at` à chaque delta.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=2957 | DOCUMENT_MANIFEST=14/2957 | SHA256=10/2957 | EXACT_DUPLICATE_GROUPS=1 | NEXT=COMPLETE_CBIBF`
