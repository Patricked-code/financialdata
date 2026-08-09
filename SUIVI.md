# SUIVI — financialdata

Dernière mise à jour : 2026-08-09

## Point de reprise courant

Dépôt canonique : `Patricked-code/financialdata`.
Git : `main` uniquement, aucune branche/PR normale.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / LIVE_SOURCE_REFRESH / TRANSVERSE_PASSES_ACTIVE**

### Inventaire 48 sociétés

- sociétés : **48 / 48** ;
- snapshot initial : **2 950 PDF** — `inventory/P1_48_ISSUERS_CHECKPOINT.md` ;
- état live courant : **2 957 PDF** ;
- checkpoint live : `inventory/P1_48_ISSUERS_CHECKPOINT_v2_20260809.md` ;
- index live : `inventory/p1_issuer_manifest.csv`.

CBIBF est passé de 8 à 15 PDF pendant la session ; l'ancien snapshot reste conservé.

## P1_TRANSVERSE — DOCUMENT MANIFEST

Schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
Stratégie incrémentale : `docs/P1_MANIFEST_SHARDING.md`.

- cible maître : `inventory/p1_document_manifest.csv` ;
- lignes actuellement consolidées dans le maître : **14 / 2 957** ;
- sources distinctes déjà capturées maître + shards, après suppression des recouvrements par Drive ID : **27 / 2 957**.

### Shards / couvertures complètes

- TRITRAF : **8 / 8** dans le maître ;
- BIIC : **2 / 2** dans le maître ;
- CBIBF : **15 / 15** dans `inventory/manifests/CBIBF.csv`, dont la paire S1 2024 est déjà aussi présente dans le maître ;
- SNTS/ONATEL : 1 anomalie seed ;
- BICC 2022 : 1 seed.

La consolidation finale refusera tout `source_drive_file_id` dupliqué entre maître et shards.

## P1_TRANSVERSE — SHA256

- SHA calculés : **23 / 2 957** ;
- TRITRAF : **8 / 8** ;
- CBIBF : **15 / 15** ;
- registre CBIBF : `inventory/hashes/CBIBF.csv`.

### CBIBF

Les 15 fichiers correspondent à **14 contenus binaires uniques**. Seule la paire :

`2024_Rapport_S1_CBIBF.pdf` / `2024_Rapport_S1_CBIBF_2.pdf`

est `EXACT_DUPLICATE`, SHA commun :
`8fb042a2d9fe05d6881c4496dedf54a68900159f2a4fcc1c6ae8bfeaf661bc05`.

Groupe enregistré dans `inventory/p1_duplicate_groups.csv`.

### TRITRAF 2004

Les deux variantes ont des SHA différents : doublon binaire exclu ; relation sémantique/version non revue.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## Prochaine action exacte

Continuer sur les corpus courts :

`ORAC (14) → SICC (19) → MVSC (20) → UNLC (20)`.

Pour chaque émetteur : shard document-level complet → matérialisation Drive → SHA-256 → doublons exacts → mise à jour inventaire et compteurs.

## Point de reprise exact

`48/48 ISSUERS | LIVE_TOTAL=2957 | CAPTURED_DOCUMENT_RECORDS=27/2957 | MASTER_CONSOLIDATED=14/2957 | SHA256=23/2957 | EXACT_DUPLICATE_GROUPS=1 | NEXT=ORAC`
